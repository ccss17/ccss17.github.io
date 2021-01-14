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

https://jesux.es/exploiting/blueborne-android-6.0.1-english/

BNEP 는 블루투스를 통하여 인터넷 프로토콜을 사용할 수 있게 해주는 프로토콜이다. 이 프로토콜을 통하여 블루투스 테더링 등을 통하여 블루투스를 기반으로한 인터넷 사용이 가능하다.

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
        BLUEBORNE ON ANDROID — © 2019 ARMIS, INC. — 3
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