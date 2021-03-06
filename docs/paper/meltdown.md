# Meltdown (CVE-2017-5754)

![image](https://user-images.githubusercontent.com/16812446/104618940-ab2d6f80-56d0-11eb-888a-e8681ce88d54.png)

- Meltdown : Intel CPU, IBM Power CPU, 일부 ARM 구조 자체에서 발생한 불량 데이터 캐시 적재 취약점이다.

공식 설명에 따르면 추측 실행과 간접적 분기 예측이 권한이 없는 데이터를 유출시킬 수 있다는 취약점이다. 쉽게 말하면 멜트다운은 불량데이터 캐시 적재 취약점을 통하여 유저 어플리케이션이 권한이 없는 메모리 영역을 읽을 수 있게 되는 취약점이다. 멜트다운으로 인하여 임의의 프로세스가 다음의 메모리 영역을 읽을 수 있게 된다.

- 커널 메모리 영역

- 다른 어플리케이션의 메모리 영역

- 컴퓨터의 모든 물리적 메모리 값

이로 인하여 ASLR 및 메모리 보호 기법 무효화되고, 이를 기반으로 세워진 모든 보안기법이 무의미해진다. 또한 메모리 상에 존재하는 중요한 정보 탈취할 수 있다.

기술적으로 멜트다운은 한 번 트리거됬을 때 원하는 영역의 1 바이트 값을 읽어 올 수 있다. 하지만 멜트다운을 계속 실행해서 컴퓨터의 물리적 메모리 전체를 다 읽어 올 수 있다. 

Intel 전 CPU 아키텍트 프랑수아 피에노엘은 *이번 버그는 컴퓨터 공학의 새로운 발견이며, 발견 되기 전에 몰랐다고 해서 과학자들을 비난할 수 없다* 고 말했다.

## Fundamental of Computer Security

컴퓨터 보안의 근본은 메모리 격리이다. 즉, 권한이 없는 메모리 영역에 대한 프로세스의 메모리 읽기, 쓰기, 실행을 방지하는 것이다. 이렇게 메모리를 보호하기 위하여 다음과 같은 보안 기법이 개발되어 왔다.

- ASLR

- NX bit

- Stack Canary

- KASLR

하지만 [멜트다운 논문](https://meltdownattack.com/meltdown.pdf) 에 따르면 유저 프로세스가 커널 메모리 전체를 다 읽을 수 있게 하는 취약점이다.

![image](https://user-images.githubusercontent.com/16812446/104619501-49213a00-56d1-11eb-8da4-227ab5fae29b.png)

위의 캡쳐는 멜트다운의 논문의 내용을 발췌한 것이다. 빨간줄로 표시한 부분에 **user process to read the entire kernel memory of machine** 라고 되어있다.

## 비순차적 실행 (Out of order execution)

비순차적 실행 (Out of order) : 명령어를 순차적으로 실행하는 것이 아니라 빠른 성능을 위하여 명령어를 비순차적으로 실행하는 것이다.

![image](https://user-images.githubusercontent.com/16812446/104619813-9ef5e200-56d1-11eb-986c-06a876440738.png)

위 그림에서와 같이 5개의 명령어가 실행될 때 `add → mul →  mul →  add →  fmul` 와 같이 순차적으로 실행하는 것보다 먼저 결과를 낼 수 있는 부분은 굳이 순서를 지키지 않고 먼저 실행한다면, CPU 성능을 더욱 올릴 수 있다. 그렇기 때문에 빨간색 박스와 같이 비순차적으로 명령어를 실행하는데, 이를 비순차적 실행이라고 한다.

## Toy Example

멜트다운을 이해하기 위하여 간단한 예시를 들어보자. 

```c linenums="1"
raise_exception();
// invalid user
access(probe_array[data * 4096]);
```

위 코드의 첫번째 줄의 `raise_exception` 에서 발생하는 예외 때문에 프로그램의 흐름이 더 이상 진행되지 않고 커널의 예외처리 핸들러로 넘어간다. 세번째 줄의 코드에서는 배열을 참조하고 있는데 이론적으로는 이 코드가 절대로 실행될 수 없다. 그러나 비순차적 실행 때문에 세번째 줄의 코드는 이미 실행이 되었다.

![image](https://user-images.githubusercontent.com/16812446/104620205-1592df80-56d2-11eb-8e45-1a3cdbc3fb2f.png)

즉, `raise_exception` 예외가 권한이 없는 메모리 영역을 읽어서 발생하는 예외라고 해도 비순차적 실행이 그 다음 명령어를 실행하게 되는 것이다. 심지어 결과값을 계산하고 레지스터, RAM, 캐시에 저장까지 합니다. 다만 예외가 처리되는 시점에서 레지스터와 RAM 에 있는 결과값은 버려진다. 

문제는 이미 계산된 결과값이 캐시에는 계속 남아있는 것이다.

이 예시의 `data` 값에 4096 이 곱해져서 `probe_array` 에 접근되기 때문에 데이터의 값이 4KB 의 거리로 메모리 참조가 이루어진다. 이로써 데이터의 값이 메모리 페이지로 맵핑된다. 즉, 다른 값이라면 반드시 다른 페이지로 맵핑되는 것이다. 

![image](https://user-images.githubusercontent.com/16812446/104621144-1d9f4f00-56d3-11eb-8bd6-0e1158253036.png)

위 그림은 원하는 주소값의 데이터를 참조하고, 비순차실행으로 코드를 실행한 결과이다. 캐시를 순차적으로 참조해보면서 Cache Hit 가 일어난 84번째 메모리 페이지에서 참조 속도가 가장 빠르기 때문에 `data = 84` 임을 알 수 있다.

## FLUSH+RELOAD : Understanding Cache

![image](https://user-images.githubusercontent.com/16812446/104620362-42df8d80-56d2-11eb-9721-04500c99a856.png)

비순차적 실행의 문제는 해커가 권한이 없는 메모리에 접근하면 예외가 발생하지만 이미 계산된 값이 캐시에는 남아있다는 것이다. 그러면 이때 해커가 FLUSH+RELOAD 기법을 사용하여 캐시에 있는 특정 값을 알아낼 수 있다.

CPU 가 메모리를 참조할 때 그 값이 먼저 캐시에 있는지 확인한다. 캐시에 없다면 이를 Cache Miss 라고 하며 메모리에서 값을 참조하고, 그 값을 캐시에 저장한다. 캐시에 있다면 이 상황을 Cache Hit 라고 하며, 곧 바로 캐시에서 참조하게 된다. 자명하게 Cache Hit 가 Cache Miss 보다 메모리 참조 시간이 훨씬 빠를 것을 알 수 있다.

![image](https://user-images.githubusercontent.com/16812446/104620677-9baf2600-56d2-11eb-916e-d828cd090dd6.png)

그런데 메모리가 새로운 값으로 수정되었을 경우 캐시와 RAM 의 값이 불일치하는 상황이 발생한다. 이런 상황을 해결하기 위하여 운영체제는 캐시를 텅 비우는 `clflush` 명령어를 제공한다. 따라서 유저 어플리케이션과 해커의 프로그램도 합법적으로 캐시를 텅 비게 만들 수 있다.

- FLUSH+RELOAD : 캐시에 있는 값을 유추하는 해킹 기법이다.

FLUSH+RELOAD 로써 캐시에 있는 값을 유추하는 과정은 매우 간단하게 설명하면 다음과 같다.

1. 먼저 `clflush` 를 통하여 L3 캐시를 전부 다 FLUSH 한다. 이 시점에서 어떤 메모리를 참조하면 그 메모리만 캐시에 로드 됐다는 것이 보장된다.

2. 해커가 원하는 주소값을 참조해본다. 권한이 없는 주소값인 경우 프로그램이 종료되지만, 이 데이터 값 1 바이트가 캐시에는 남아있다.

3. 1 바이트 값의 범위는 0 부터 255 이므로 캐시의 0 번째 주소부터 255 번째 주소까지 참조해본다.

4. 그 중에서 가장 빠른 속도로 읽히는 데이터가 Cache Hit 가 발생한 데이터이므로 해커가 원하는 데이터이다.

## exploit

```assembly linenums="1"
loop:
movzx (%ecx), %eax ; 예외발생
shl $12, %eax 
jz loop
mov (%ebx,%eax,1), %ebx 
```
먼저 위 코드에서 `%ecx` 는 해커가 원하는 메모리 영역이고, `%ebx` 는 `probe_array` 를 뜻한다. 실제로 Meltdown 으로 exploit 을 하는 과정은 다음과 같다. 

1. 코드 `2:` 에서와 같이 `ecx` 주소값의 값을 읽어서 `eax` 에 복사한다. 이는 원하는 영역의 1 byte 를 읽는 것이다. 그러나 권한이 없어서 예외가 발생한다.

2. 코드 `3:` 에서와 같이 `eax` 에 4096 을 곱하고, 코드 `5:` 처럼 곱한 값을 `ebx` 에 저장한다. 이때 해커는 이미 캐시를 FLUSH 했기 때문에 오로지 이 데이터만 캐시에 로드되어있다.

3. FLUSH+RELOAD 로 캐시에 남아 있는 데이터를 알아낸다.

다음은 멜트다운으로 해킹을 시연한 사례이다.

- https://www.youtube.com/watch?v=bReA1dvGJ6Y

- https://www.youtube.com/watch?v=RbHbFkh6eeE

- https://www.youtube.com/watch?v=kwnh7q356Jk

멜트다운의 공식 POC 코드는 https://github.com/IAIK/meltdown 에 있다.

## 웹 페이지로 트리거되는 멜트다운

이 멜트다운은 CPU 구조에서 발견된 취약점이므로 OS 와 어플리케이션에 독립적이다. 또한 코드를 작성하기가 매우 쉬워서 Javascript 로 웹 페이지를 통하여 exploit 될 수도 있다. 이 때문에 크롬, 엣지, 파이어폭스 등의 메이저 브라우저에서 시간 오차율을 임시적으로 높이기도 했다. 멜트다운이 시간 계산을 통해서 트리거되는 취약점이기 때문이다. 
