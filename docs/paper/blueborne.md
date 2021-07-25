# BlueBorne

# Bluetooth SDP Protocol Memory Leak (CVE-2017-0785)

![image](https://user-images.githubusercontent.com/16812446/104615872-0198af00-56cd-11eb-9650-2883c80c56c8.png)

- CVE-2017-0785 : SDP Protocol 구현 시 발생한 결점으로 발생한 메모리 유출 취약점이다. 유출된 메모리 값을 기반으로 ASLR 을 우회할 수 있다.

![image](https://user-images.githubusercontent.com/16812446/104615852-fba2ce00-56cc-11eb-9089-9c8cd88b65cc.png)

## SDP Protocol 이란?

- SDP : Service Discovery Protocol

블루투스의 모든 어플리케이션이 SDP 사용한다. SDP 프로토콜로 블루투스 디바이스는 어떤 서비스를 사용할 수 있는지 검색한다. 다양한 블루투스 서비스로 File I/O, Tethering, Sound I/O, Bluetooth Mouse 등이 있다.

## SDP Protocol 실제 작동 과정

SDP Client 가 검색 패턴을 포함한 SDP Request 전송하면 SDP Server  는 서비스 목록을 포함한 SDP Response 전송한다.

- SDP Continuation State : MTU 보다 전송해야 할 서비스 목록이 클 경우 설정되는 상태이다.

MTU (Maximum Transmission Unit) 는 최대 전송 가능 크기이다. SDP Server 는 MTU 만큼 서비스 목록을 조각내서 SDP Response 를 나눠 보내게 되며, 이 패킷에 SDP Continuation State 구조체가 첨부된다. 즉, SDP 서버는 SDP 레코드를 조각내서 SDP 리스폰을 나눠 보내는 것이다. 이때 Continuation State 은 보내야할 SDP 레코드가 얼마나 남아있는지 알려준다.

## Android Implementation of SDP Protocol

```c
typedef struct {
    uint16_t cont_offset; 
} sdp_cont_state_t;
```

위와 같은 SDP Continuation State 구조체의 `cont_offset` 는 SDP Response 를 어디까지 전송했는지 저장한다.

```c linenums="1"
rem_handles = num_rsp_handles - cont_offset;
p_ccb->cont_offset += cur_handles;
is_cont = TRUE;
for (...)
    UINT32_TO_BE_STREAM (p_rsp, rsp_handles[xx]); 
```

위 코드는 SDP Response 를 보내는 과정이 구현된 안드로이드 커널 소스이다. 변수들의 기능은 다음과 같다.

`num_rsp_handles` : 보내야 할 SDP 전체 크기

`cont_offset` : 보낸 SDP 크기

`rem_handles` : 남은 SDP 크기

첫번째 줄에서  `num_rsp_handles` 에 `cont_offset` 을 빼서 `rem_handles` 에 저장하고 있다. 따라서 `rem_handles` 는 앞으로 보내야할 SDP 리스폰 크기가 된다. 그러고 나서 `for` 문에서 SDP 리스폰을 실제로 전송하게 된다.

## SDP Response 과정 구현 커널의 결점

그런데 이 코드에는 결점이 있다. `num_rsp_handles` 가 새로운 SDP Request 가 들어올 때마다 다시 계산되는데 코드는 `num_rsp_handles` 와 `cont_offset` 이 동일한 SDP Response 를 다루고 있다고 가정한다. 이에 따라 `num_rsp_handles` 을 작게 만들고 `cont_offset` 을 크게 만들어서 `rem_handles = num_rsp_handles – cont_offset` 에 Underflow 를 유도할 수 있다. 

`num_rsp_handles` 과 `cont_offset` 는 SDP 패킷을 보내는 SDP 클라이언트가 조작할 수 있다.

## SDP Procotol Vulnerability

MTU 를 30 byte 라고 가정하고 해커의 노트북을 SDP 클라이언트, 피해자의 안드로이드 스마트폰을 SDP 서버라고 가정하자.

![image](https://user-images.githubusercontent.com/16812446/104617183-7ae4d180-56ce-11eb-910f-aed176a42780.png)

SDP Client 가 검색 패턴을 포함한 SDP Request 전송한다. 이때 SDP Server 에서 100 byte SDP Response 발생했다고 하자. 그러면 SDP Server 는 MTU 가 초과되었으므로 Continuation state 가 덧붙혀진 SDP Response 전송한다. 이때 Android Kernel 에서 `cont_offset = 30 (byte)` 으로 설정된다. MTU 로 인하여 30 byte 밖에 못보냈기 때문이다.

![image](https://user-images.githubusercontent.com/16812446/104617354-b1225100-56ce-11eb-94ca-175f2d9c5c1e.png)

그리고 SDP Client 가 방금 받은 Continuation state 를 덧붙혀서 새로운 SDP Request 전송한다. 이 Request 로 SDP Server 에서 15 byte SDP Response 가 발생했다고 하자. 그러면 Android Kernel 에서 `num_rsp_handles = 15 (byte)` 로 설정된다.

```
cont_offset = 30 (byte)
num_rsp_handles = 15 (byte)
↓
rem_handles = num_rsp_handles - cont_offset;
↓
15 – 30 = -15 = 65521 (byte)
```

`cont_offset` 은 30 인데 `num_rsp_handles` 가 15 이기 때문에 남아있는 SDP 리스폰을 계산하는 `rem_handles` 가 -15 가 된다. 그런데 이 변수는 `unsigned short` 자료형이기 때문에 언더플로우가 발생하여 결국 65521 가 된다. 그래서 안드로이드 커널은 거의 64KB 정도의 SDP 리스폰이 남아있다고 생각하고 4번째와 5번째 코드의 for 문에서 SDP 레코드를 저장하고 있는 `rsp_handles` 버퍼의 경계를 넘어서서 데이터를 계속 보낸다. 그래서 실제 SDP 리스폰이 다 전송되고 나서도 메모리 영역을 넘어서서 권한이 없는 데이터도 해커에게 전송하게 된다.

## Exploit 

다음은 이 취약점을 통하여 안드로이드 커널의 메모리를 소량 유출시켜 본 결과이다.

![Peek 2019-02-10 21-25](https://user-images.githubusercontent.com/16812446/104617846-4ae9fe00-56cf-11eb-8852-579ac0340513.gif)

POC 코드로는 https://github.com/ojasookert/CVE-2017-0785 를 사용하였다.

# Android RCE Vulnerability in BNEP (CVE-2017-0781)

## BNEP Protocol in Bluetooth

- BNEP (Bluetooth network encapsulation protocol) : 블루투스를 통하여 인터넷 프로토콜을 사용할 수 있게 해주는 프로토콜이다. 

이 프로토콜을 통하여 블루투스 테더링 등을 통하여 블루투스를 기반으로한 인터넷 사용이 가능하다.

![](https://t1.daumcdn.net/cfile/tistory/2479D64E56C1521704)

위 그림은 Ethernet 패킷을 블루투스에서 다룰 수 있기 위하여 BNEP 패킷으로 포장한 것을 보여준다.

## Vulnerability

BNEP 프로토콜에서 발생한 Android RCE 취약점은 다음의 안드로이드 커널 소스코드의 `memcpy` 에서 발생했다.

```c linenums="1"
UINT8 * p = ( UINT8 *)( p_buf + 1 ) + p_buf -> offset ;
...
type = * p ++;
extension_present = type >> 7 ;
type &= 0x7f ;
...
switch ( type )
{
    ...
    case BNEP_FRAME_CONTROL :
        ctrl_type = * p ;
        p = bnep_process_control_packet ( p_bcb , p , & rem_len , FALSE );
        if (ctrl_type == BNEP_SETUP_CONNECTION_REQUEST_MSG &&
            p_bcb -> con_state != BNEP_STATE_CONNECTED &&
            extension_present && p && rem_len )
    {
        p_bcb -> p_pending_data = ( BT_HDR *) osi_malloc ( rem_len );
        memcpy (( UINT8 *)( p_bcb -> p_pending_data + 1 ), p , rem_len );
        ...
    }
```

위 코드는 BNEP 컨트롤 메시지를 핸들링하는 과정을 보여준다. `BNEP_FRAME_CONTROL` 은 BNEP 컨트롤 메시지의 스위치 케이스이다. 이는 BNEP 연결 상태가 한 컨트롤 메시지에서 다른 컨트롤 메시지로 전환되는 특수한 상황을 다루기 위한 케이스이다. 이런 상황은 단순히 여러개의 컨트롤 메시지를 전송했을 때 발생한다. 

만약 `SETUP_CONNECTION_REQUEST` 가 컨트롤 메시지로 전달되었다면, 이후에 전송되는 컨트롤 메시지들이 CONNECTED 상태에서 처리되어야 한다. CONNECTED 상태로 전환되는 것은 블루투스 연결 인증 과정이 끝까지 이루어져야 가능하다. 그런데 이 과정은 비동기적으로 이루어지기 때문에 이전까지 블루투스 연결 상태는 IDLE 이다. 이에 따라 전달되는 컨트롤 메시지를 처리할 수 없게 된다. 

이 문제를 해결하기 위하여 전달된 컨트롤 메시지들을 블루투스 연결 인증 과정이 끝난 다음에 처리하기 위하여 위 코드에서 처리되지 않은 블루투스 메시지들을 `p_pending_data` 에 저장한다. 그러나 이 코드에 몇 가지 결점이 존재한다. 

1. `p_pending_data` 가 힙 메모리에 `rem_len` 크기로 할당이 된 후 `memcpy` 가 `p_pending_data + 1` 위치에 `rem_len` 만큼의 메시지를 복사한다. 이에 따라 `memcpy` 는 `sizeof(p_pending_data)` 만큼(8 바이트)의 힙 오버플로우를 발생시킨다. 심지어 이 오버플로우는 컨트롤 메시지가 전달될 때마다 발생한다. 

2. 이 오버플로우로 인하여 `p_pending_data` 의 포인터가 할당 해제가 되지 않기 떄문에 메모리 유출 취약점이 발생한다.

`p_pending_data` 의 타입은 8 바이트 `BT_HDR` 구조체 타입이다. 또한 힙 메모리 할당 크기를 설정하는 `rem_len` 은 해커가 쉽게 조작할 수 있다. 왜냐하면 처리되지 않은 컨트롤 메시지의 크기는 송신 패킷 상에서 조정할 수 있기 때문이다. `memcpy` 의 소스인 `p` 가 해커가 송신하는 블루투스 패킷이다.  

![image](https://user-images.githubusercontent.com/16812446/104637397-15054380-56e8-11eb-8018-76da5b387889.png)

이러한 오버플로우는 위와 같이 조작된 BNEP 패킷에 의하여 발생한다. 패킷을 이렇게 조작하면 안드로이드 커널 내부의 흐름을 오버플로우를 발생시키는 `memcpy` 코드로 보낼 수 있다.

또한 패킷 사이즈는 해커가 조정할 수 있기 때문에 원하는 메모리에 8 바이트 힙 오버플로우를 발생시킬 수 있다. 

## Exploitation on Android 7.1

먼저 ASLR 을 우회하기 위하여 CVE-2017-0785 취약점을 사용하여 메모리를 유출시켜야 한다. 이 취약점은 안드로이드 커널의 ASLR 이 설정된 `libc.so` 의 주소값을 유출시켜주며 안드로이드 블루투스 기능을 제공하는 `bluetooth.default.so` 라이브러리의 bss 영역 주소값을 유출시켜준다. 

이로써 ASLR 을 우회하여 안드로이드 커널에 로드되어 있는 `libc.so` 의 `system` 함수에 임의의 명령어를 실행할 수 있다.

안드로이드 블루투스 데몬은 `com.android.bluetooth` 인데 이 프로세스는 Zygote 의 서브 프로세스이다. Zygote 는 안드로이드의 핵심 process-spawning 데몬인데, 놀랍게도 32 비트 프로세스이므로 ASLR 엔트로피가 매우 제한되어 ASLR 우회를 더욱 쉽게 만든다. 또한 Zygote 는 한번 crash 가 나면 곧바로 재시작되기 때문에 해커가 무한정 공격할 수 있게 해준다.

이 취약점을 exploit 하기 위하여 다음 4 가지 연구가 필요하다. 

1. **Target Object Selcetion** 힙 메모리 영역에 할당되는, 그리고 첫 8 바이트를 함수 포인터로 갖는 객체를 찾는다. 

2. **Loading the Payload into Memory** 조작된 데이터를 예측가능한 메모리 주소에 덮어쓸 수 있는 코드를 찾는다. 

3. **Gromming the Heap** 힙 메모리 영역을 조작할 수 있는 방법을 찾는다. 우리의 경우 1 번 과정에서 찾은 버퍼 바로 전에 `p_pending_data` 의 오버플로우를 통하여 함수 포인터를 덮어써야 한다. 

4. ASLR 을 우회하는 방법을 찾는다. 우리의 경우 CVE-2017-0785 취약점으로 우회한다.

https://jesux.es/exploiting/blueborne-android-6.0.1-english/

### Target Object Selcetion

먼저 우리가 찾은 오버플로우를 계속 일으켜서 `com.android.bluetooth` 데몬 프로세스에 의도적으로 crash 를 일으켜본다.

![image](https://user-images.githubusercontent.com/16812446/104638810-facc6500-56e9-11eb-84dc-cb5a6b1b352c.png)

위와 같이 패킷을 안드로이드 블루투스에 전송하면 오버플로우를 일으킬 수 있다. 이 패킷을 500 번에서 1000번 정도 보내면 데몬에 거의 확실하게 crash 가 발생한다. 이 과정은 1~2초 만에 이루어진다. 그러면 안드로이드  crash 로그를 살펴보면 다음과 같은 결과를 볼 수 있다. 

![image](https://user-images.githubusercontent.com/16812446/104639028-4848d200-56ea-11eb-8233-7918e3778dfc.png)

또한 crash 가 발생한 코드를 IDA 디버거로 찾아보면 다음과 같다.

![image](https://user-images.githubusercontent.com/16812446/104639089-5991de80-56ea-11eb-8028-9637bb31dd20.png)

crash 가 발생한 함수는 `btu_hci_msg_process` 함수였다. 이 함수는 AOSP 에서 확인할 수 있다. 안드로이드 커널 소스코드는 오픈소스이기 때문이다.

![image](https://user-images.githubusercontent.com/16812446/104639190-76c6ad00-56ea-11eb-82c8-71b7de59a610.png)

crash 는 위 코드의 `p_msg->event` 에서 발생했고, R4 레지스터가 `p_msg` 를 저장하고 있다. 

또한 이 결과들은 우리가 `p_msg` 포인터를 조작할 수 있다는 것을 알려준다. R4 레지스터가 0x41414141 이기 때문이다. 한편 event 필드는 `BT_HDR` 구조체의 첫번째 필드이다. 그러므로 우리가 컨트롤 메시지의 모든 필드를 조작할 수 있다는 사실을 알 수 있다. 

더욱 흥미로운 것은 `BTU_POST_TO_TASK_NO_GOOD_HACK` 케이스 인데, 이 event 타입은 `p_msg` 의 `data` 필드의 첫번째 바이트를 함수포인터로써 사용하고 `p_msg` 그 자체를 파라미터로 전달하고 있다. 이 부분을 통하여 `system` 함수를 호출하며 exploit 을 할 수 있게 된다. 

즉, `btu_hci_msg_process` 함수로 전달된 `p_msg` 파라미터는 안드로이드 블루투스로 전달된 블루투스 패킷 데이터를 포인팅하고 있다. 한편 `btu_hci_msg_process` 함수가 호출된 과정을 역추적 해보면 다음과 같다. 

![image](https://user-images.githubusercontent.com/16812446/104640419-d1143d80-56eb-11eb-8253-0d7e1328c770.png)

위 코드는 `btu_hci_msg_process` 함수를 `btu_hci_msg_queue` 로 전달되는 모든 블루투스 메시지의 핸들러로 지정하고 있다. 이 큐는 블루투스 컨트롤러로 전달되는 모든 패킷을 저장하는 데이터구조이다. 이는 해커가 보낸 패킷도 이 큐를 반드시 거쳐가게 된다는 의미이다. 

![image](https://user-images.githubusercontent.com/16812446/104640698-2c463000-56ec-11eb-8fc1-916bf25f2901.png)

위 코드는 crash 가 발생하기 전에 overwritten 되는 실제 버퍼를 보여준다. 위 코드의 `queue->list` 의 `list` 필드는 `list_t` 타입인데, 이는 다음과 같은 `list_node_t` 구조체의 링크드 리스트이다.

![image](https://user-images.githubusercontent.com/16812446/104640867-644d7300-56ec-11eb-92ee-02e6c2add2e7.png)

놀랍게도 이 버퍼의 크기도 8 바이트이다. 그런데 `osi_malloc` 함수는 안드로이드 libc 의 `jemalloc` 함수를 사용하는데, 이 함수는 비슷한 사이즈의 버퍼를 연속된 메모리 공간에 위치시킨다. 

우리가 오버플로우 시키는 버퍼 `p_pending_data` 의 크기가 8 바이트이고 `list_node_t` 도 8 바이트이므로 이들은 같은 힙 메모리 영역에 연속적으로 할당된다.

이로써 crash 가 발생한 이유가 설명된다. `btu_hci_msg_queue` 가 내부적으로 갖고 있던 `list_node_t` 가 `p_pending_data` 의 오버플로우로 인하여 0x41414141 로 overwritten 된 것이다. 이 데이터가 이후에 `p_msg` 로 형변환되고, `btu_hci_msg_process` 함수로 전달되는데, 이때 `data` 필드의 주소값을 함수 포인터로 사용하여 호출하고 있기 때문이다. 이로써 exploit 이 가능하다는 것을 알 수 있다.

그러므로 오버플로우를 통하여 exploit 을 하기 위하여 일단 `list_node_t` 를 힙 메모리에 많이 할당을 시키고, 그 사이에 `p_pending_data` 가 할당될 빈 공간을 마련해두어야 한다는 것을 알 수 있다. 이는 단순히 안드로이드 스마트폰의 블루투스에 똑같은 BNEP 패킷을 여러번 보내는 것으로 이루어질 수 있다. 왜냐하면 모든 패킷이 `btu_hci_msg_queue` 를 거쳐가는데 이 큐가 내부적으로 `list_node_t` 객체를 할당했었기 때문이다. 그리고 이 데이터는 이후에 `bnep_data_ind` 로 전달되어 `p_pending_data` 가 할당되고, 이때 오버플로우가 발생하게 된다.

그렇다면 이제 문제는 어떻게 `list_node_t` 를 힙 메모리 영역에 띄엄띄엄 할당하느냐는 것이다. 왜냐하면 그래야만 `p_pending_data` 가 오버플로우를 일으킬 때 바로 그 다음에 할당되어 있는 `list_node_t` 를 overwrite 할 수 있기 때문이다. 

일단은 우리가 전송할 페이로드에 libc 의 `system` 함수의 주소값을 어떻게 전달할지 연구해야 한다. 

![image](https://user-images.githubusercontent.com/16812446/104642816-c018fb80-56ee-11eb-87b5-9657c8a1f0f6.png)

분석을 해보면 패킷의 8 바이트 이후의 4 바이트의 값이 `data` 필드로 저장된다는 것을 알 수 있다. 그렇다면 이 4 바이트를 libc 의 `system` 함수의 주소값으로 설정하면, `system` 함수에 다음의 파라미터가 전달된 것이 된다.

![image](https://user-images.githubusercontent.com/16812446/104642955-f35b8a80-56ee-11eb-9cee-903e275ef96a.png)

0x41 은 A 를 뜻하고 0x22 는 " 를 뜻하며, 0x3B 는 ; 을 뜻하기 때문에 앞의 명령어가 존재하지 않은 명령어이지만 이후의 명령어를 실행하게 된다 0x23 은 # 으로써 주석을 의미하므로 이후의 문자열은 `system` 함수가 무시한다. 전체 패킷이 `system` 함수의 파라미터로 다시 들어가는 이유는 `p_msg` 가 `p_msg->data` 의 파라미터로 다시 들어갔기 때문이다. 

이 형태는 두 문자열 A 와 B 가 `system("A"; "B"#)` 의 형태로 전달된 것과 같다. 

이 페이로드, 즉 위의 예시에서 문자열 B 를 통하여 안드로이드 시스템에서 해커의 컴퓨터로 리버스 쉘을 실행시킬 수 있다. 

그러면 이제 해야 할 일은 페이로드를 메모리 어딘가에 삽입해두고, 그 페이로드의 주소값으로 문자열 B 부분을 설정하는 것이다.  

### Loading the Payload into Memory

블루투스의 이름은 해커가 임의로 설정할 수 있는데, 이 블루투스 이름은 블루투스 연결 인증 초기 단계에서 안드로이드 블루투스 시스템으로 전달된다.

![image](https://user-images.githubusercontent.com/16812446/104643635-0b7fd980-56f0-11eb-9626-77a9add6c16c.png)

이 블루투스 이름들은 안드로이드 블루투스 라이브러리의 bss 영역에 저장되는데, 저장되는 구조체는 다음과 같다. 

![image](https://user-images.githubusercontent.com/16812446/104643753-32d6a680-56f0-11eb-8a00-e4c0a1e8fab6.png)

`tBTM_CB` 구조체가 안드로이드 블루투스 데몬의 bss 영역에 저장되고, 이곳의 `remote_name` 변수에 해커의 블루투스 이름도 저장된다. 이 영역의 주소값 또한 메모리 유출 취약점을 통하여 쉽게 알아낼 수 있다. 

한편 블루투스 이름을 정의하는 블루투스 상세 스펙을 살펴보면 다음과 같다.

![image](https://user-images.githubusercontent.com/16812446/104644680-6c5be180-56f1-11eb-9e01-7eff98476d4e.png)

즉, 해커는 자신의 블루투스 이름을 UTF-8 로 248 바이트까지 지정할 수 있다. 이로써 페이로드를 자유롭게 248 바이트까지 만들어서 블루투스 이름으로 지정하면, 안드로이드 블루투스에 잘 전달되어 저장된다는 것이다. 그러면 그 페이로드가 저장된 주소값으로 `system` 함수의 문자열 B 를 설정하면 된다. 

### Gromming the Heap

이제 우리가 해야 할 일은 `list_node_t` 를 힙 영역에 띄엄띄엄 할당하는 것이다. 그래야 `p_pending_data` 에서 오버플로우가 발생했을 때 `list_node_t` 를 overwrite 할 수 있다.

그런데 지금까지의 연구를 통하여 단순히 조작된 패킷을 계속 전송하는 것만으로도 overwrite 가 이루어지고 exploit 이 된다는 것을 알 수 있다. 그러나 exploit 을 좀 더 빠르게 하기 위하여 exploit 을 위한 패킷을 전송하기 전에 힙 메모리 영역을 좀 더 다듬을 수 있다. 

![image](https://user-images.githubusercontent.com/16812446/104645172-0f146000-56f2-11eb-8ee2-1fe0212846f1.png)

우리가 원하는 이상적인 힙 메모리 형태는 위와 같다. 위와 같이 힙 메모리가 형성되어 있으면 `p_pending_data` 가 8 바이트 빈 공간에 할당이 될 것이고 오버플로우가 발생했을 때 `list_node_t` 를 페이로드가 존재하는 주소값으로 덮어씀으로써 `system` 함수를 실행시킬 수 있다. 

![image](https://user-images.githubusercontent.com/16812446/104645670-b2657500-56f2-11eb-8c08-c3222e2a0bbb.png)

그러나 조작된 패킷을 보내기 시작했을 때 힙 메모리 구조는 위와 같다. `list_node_t` 들이 힙 메모리의 전반부에 할당이 되고, 처리가 안된 `p_pending_data` 들은 `list_node_t` 이후에 할당이 된다. 이 `p_pending_data` 들이 발생시키는 오버플로우는 `list_node_t` 를 덮어쓰지 못한다.

8 바이트 빈 공간은 `list_node_t` 가 처리된 후 할당이 해제되었을 때 발생한다.

![image](https://user-images.githubusercontent.com/16812446/104645820-f193c600-56f2-11eb-9ca1-3f4a60667a6c.png)

`list_node_t` 가 할당이 해제되어 8 바이트 빈 공간이 발생한 이후 최초로 전반부에 할당되는 `p_pending_data` 가 발생할 경우 이 오버플로우로 인하여 exploit 이 되지는 않는다. 왜냐하면 이후에 처리된 `list_node_t` 로 인하여 연속적으로 8 바이트 빈 공간이 발생하기 때문이다.

그러므로 8 바이트 빈 공간을 무작위로 발생시켜야 한다. 그래야만 할당된 `p_pending_data` 바로 다음에 `list_node_t` 가 존재할 확률이 높아지기 때문이다. 

이를 위하여 BNEP 프로토콜의 다른 컨트롤 메시지를 사용할 수 있다. "Command not understood" 라는 BNEP 프로토콜 패킷이 있는데, 이 BNEP 메시지를 패킷으로 전송하면 다음과 같은 코드에서 처리된다.

![image](https://user-images.githubusercontent.com/16812446/104646210-7bdc2a00-56f3-11eb-9390-c2d5208609bb.png)

이 코드를 실행하기 위하여 패킷을 다르게 조작하기만 하면 된다. 가령 다음과 같이 패킷을 만들 수 있다. 

![image](https://user-images.githubusercontent.com/16812446/104646338-9f06d980-56f3-11eb-8a13-9d2af1b96b9f.png)

이 패킷을 통하여 힙 영역에 또 다른 스레드가 할당과 해제를 관리하는 `xmit` 라는 객체를 생성시킬 수 있다. 이로써 `xmit` 객체가 할당 해제가 될 때 다음과 같이 힙 영역에 무작위의 8 바이트 빈공간을 마련할 수 있다.

![image](https://user-images.githubusercontent.com/16812446/104646553-ee4d0a00-56f3-11eb-95d1-eebee47abe2b.png)

### exploit 요약 

지금까지의 exploit 과정을 요약해보면 다음과 같다.

1. CVE-2017-0785 취약점을 통하여 메모리를 유출시켜 ASLR 을 우회할 준비를 한다.

2. 블루투스 이름에 페이로드를 삽입하여 안드로이드 블루투스에 연결을 시도한다. 

3. "Command not undertood" 로 인식될 BNEP 패킷을 소량 전송한다. 이로써 안드로이드에 8 바이트 빈공간이 마련된다. 

4. 힙 오버플로우를 발생시키는 패킷을 발생하여 exploit 을 시도한다.

Armis 는 실험적으로 이 과정으로 Android 7.1 을 exploit 하면 첫번째 시도만에 50% 의 확률로 exploit 이 성공하여 shell 을 탈취할 수 있음을 확인하였고, 첫번째 시도가 실패하더라도 수 초 또는 수 분 내에 exploit 이 성공하여 안드로이드에 remtoe shell 을 탈취할 수 있다는 것을 확인하였다. 

### 해킹 시연 

이 영상은 CVE-2017-0785 로 메모리를 유출시켜 ASLR 을 우회하고 CVE-2017-0781 로 안드로이드에 RCE 를 하는 영상이다.

https://www.youtube.com/watch?v=Az-l90RCns8


다음은 POC 코드이다.

https://github.com/ArmisSecurity/blueborne