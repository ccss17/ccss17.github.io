!!! info

    출처/참고 : https://www.nand2tetris.org 

이 책이 다루는 내용은 다음과 같다.

![image](https://user-images.githubusercontent.com/16812446/111190384-5dfb4a80-85fa-11eb-999a-26a14fc22e25.png)

컴퓨팅 시스템이 설계되는 추상적 계층은 다음과 같다. 

![image](https://user-images.githubusercontent.com/16812446/111191133-188b4d00-85fb-11eb-978b-6cb5f79eb81b.png)

이 책을 통하여 어떻게 컴퓨터가 작동하는지, 어떻게 복잡한 문제를 작은 모듈로 나누어 관리할 수 있는지, 어떻게 대규모 하드웨어와 소프트웨어를 개발할 수 있는지 배우게 될 것이다. 

프로그래밍을 배울 때 보통 "Hello Wolrd" 를 출력하는 것을 배웠을 것이다. 하지만 그것이 실제로 어떻게 작동하는지 알아보자. 먼저 알아야 할 것은 프로그램이란 텍스트 파일에 저장된 무의미한 기호들의 모임이라는 것이다. 그러므로 이것을 파싱하고 문법을 해석하고 컴퓨터가 이해할 수 있는 저수준 언어로 재해석해야 한다. 이 과정이 컴파일이다. 

그러한 저수준 언어가 기계어인데 기계어는 하드웨어 구조, 즉 레지스터, 메모리 유닛, ALU 같은 것들에 의하여 다루어진다. 또 이 모든 하드웨어는 논리 게이트의 모임으로 구성된다. 또한 이 논리 게이트는 Nand 와 Nor 게이트로 구성가능하다. 물론 이 논리 게이트들은 트랜지스터로 구현되는 몇몇의 스위칭 기기로 구성되지만, 이 영역부터는 컴퓨터가 아니라 물리학이므로 이곳까지 다루지는 않을 것이다. 

이제 컴퓨터의 끝자락 속에 살았던 여러분에게 컴퓨터의 뿌리부터 이해시켜줄텐데 그것을 컴퓨터를 밑바닥부터 만들어봄으로써 성취시켜줄 것이다.

이때 중요한 것은 추상화이다. 우리는 컴퓨터를 만들 때 컴퓨터를 이루는 계층을 추상화시켜서 만들게 된다. 이 추상화가 주는 효용은 각각의 계층을 독립적으로 다룰 수 있게 된다는 것이다. 이로써 하드웨어 &rarr; 소프트웨어 라는 순서로 컴퓨터를 설계하지 않아도 된다. 임의의 순서로 각각의 계층을 설계할 수 있고 이해할 수 있다. 이로써 우리는 다른 계층을 전혀 걱정하지 않고 독립적으로 우리가 신경쓰고 있는 계층의 설계에만 집중할 수 있게 된다. 하지만 추상적 계층을 잘 분리시켜서 시스템을 설계하는 것은 전적으로 경험 학문이라서, 많은 예시를 봐야 하고 많은 경험을 직접 해보아야 한다. 하지만 독자는 본 책을 읽음으로써 추상 계층을 나누어 시스템을 설계하는 것에 대한 아이디어를 흡수할 수 있다.

> 실제로 이러한 추상적 계층을 독립적으로 설계하는 것은 매우 중요한 아이디어인 것 같다. WICWIU 는 설계가 많이 종속적이었었던가. 어쨌든 설계 계층과 모듈이 추상적 계층으로 나뉘어서 독립성이 유지된다면, 그 모듈과 계층만 분리시켜서 따로 다룰 수 있게 되고 테스트도 따로 할 수 있게 된다. 이렇게 하는게 맞는듯.

# 1. Boolean Logic

컴퓨터, 스마트폰, 라우터 같은 디지털 기기가 서로 다르게 설계되었지만 본질적으로 모두 논리 게이트에 의하여 만들어졌다. 이 논리 게이트를 물이나 흙이나 나무로도 설계할 수 있지만, 현재로써 가장 효율적인 것이 전자공학으로 논리 게이트를 설계하는 것이므로 논리 게이트의 밑에는 전자 공학 기술이 있다. 

이 장에서는 Nand 게이트만 살펴보고, 다른 게이트를 이것을 기반으로 만든다.

먼저 Boolean 게이트를 살펴볼 것인데 이것은 Boolean 함수의 물리적 구현체이므로 Boolean 대수에 대하여 가볍게 알아보자. Boolean 대수는 binary 라고도 부르는 Boolean 을 다루는데, 이 값은 true/false 이다. 이것을 1/0 으로도 나타낼 수 있으므로 1/0 을 사용하자.

Boolean 함수는 binary 입력을 받아서 binary 출력을 낸다. 컴퓨터 하드웨어가 binary 값을 다루기 때문에 Boolean 함수는 하드웨어 설계에서 중요한 역할을 한다. 그러므로 Boolean 함수를 설계하는 것이 하드웨어 설계의 시작이다.

## Truth Table Representation

Boolean 함수의 정의의 시작은 모든 가능한 binary 입력과 그에 대응되는 출력을 다음과 같은 진리표로 나열해보는 것이다.

![image](https://user-images.githubusercontent.com/16812446/111748694-2f1ff580-88d4-11eb-92f1-971302163aa7.png)

Boolean 함수는 위와 같이 입력 벡터 $(v_1, v_2, \dots, v_n)$ 를 출력 $f(v_1, v_2, \dots, v_n)$ 에 대응시키는 함수 

$$f: \{0,1\} ^{n} \to \{0,1\}$$

이다.

!!! tldr ""

    Boolean function : 함수 

    $$f: \{0,1\} ^{n} \to \{0,1\}$$

    이다.

## Boolean Expressions

이와 같은 Boolean 함수는 Boolean 연산에 의하여 표현 가능하다. 그것은 And 와 Or 과 Not 인데, 각각 $x \cdot y$, $x+y$, $\bar{x}$ 로 표현한다. 이 표현법으로 위의 함수 $f$ 는 

$$ f(x, y, z) = (x + y) \cdot \bar{z} $$

로 표현할 수 있게 된다. 이 공식화는 다음과 같은 과정으로 이루어진다. 

1. 함숫값이 $1$ 인 경우를 따져본다.

    $(0, 1, 0) \mapsto 1$, $(1, 0, 0) \mapsto 1$, $(1, 1, 0) \mapsto 1$ 일 때 $1$ 이므로 각각 $\bar{x}y \bar{z}, x \bar{y}\bar{z}, xy \bar{z}$ 로 표현할 수 있다.

2. $1$ 인 경우를 Or 로 묶는다.

    그러면 $f(x, y, z) = \bar{x}y \bar{z} + x \bar{y}\bar{z} + xy \bar{z}$ 을 얻는다. 

3. 최소의 연산만 사용하도록 최적화한다.

    $f(x, y, z) = \bar{x}y \bar{z} + x \bar{y}\bar{z} + xy \bar{z}$ 의 진리표는 $f(x, y, z) = (x + y) \cdot \bar{z}$ 와 같다. 그러므로 최종적으로 함수 $f$ 을 

    $$ f(x, y, z) = (x + y) \cdot \bar{z} $$

    로 정의한다. 

이러한 구성을 얻을 수 있는 중요한 결론은 Boolean 함수가 아무리 복잡하든지 And, Or, Not 으로 표현가능하다는 것이다. 

함수 $f: \{0,1\} ^{2} \to \{0, 1\}$ 중에서 대표적인 것들이 있는데, 다음과 같다. 

![image](https://user-images.githubusercontent.com/16812446/111748740-40690200-88d4-11eb-8e31-43260b30df7f.png)

$$ p \bar{\cdot } q , p \bar{+} q$$

"If x then y" 함수는 $x \to y$ 를 뜻한다. 이중에서 Nand 함수(그리고 Nor 함수)는 이론적으로 재미있는 성질을 갖는데, 그것은 And, Or, Not 을 Nand 로부터 구성할 수 있다는 것이다. 가령 $x + y = (x \bar{\cdot} y) \bar{\cdot} (y \bar{\cdot} y)$ 이다. 모든 Boolean 함수가 And, Or, Not 으로 구성될 수 있으므로 이는 곧 Nand 만으로 모든 Boolean 함수를 구성할 수 있다는 말이다. 

## Logic Gate

게이트는 Boolean 함수의 물리적 구현체이다. Boolean 함수가 $f: \{0,1\} ^{n} \to \{0,1\} ^{m}$ 로 정의되었다면 게이트는 $n$ 개의 입력 핀과 $m$ 개의 출력 핀으로 구현된다. 

이것을 어떻게 구현할지는 현재로써 전자공학이 최선이지만 연구자들은 자기장으로, 광학적으로, 생물학적으로, 수력학적으로, 공기 등으로 구현하면 더 효율적인지 연구하고 있다. 한편, 이 말은 컴퓨터 공학이 그 물리적 기반에 대하여 전혀 걱정할 필요가 없다는 것을 의미한다. 컴퓨터 공학자들은 그 물리적 계층이 구현한 Boolean 대수와 논리 게이트의 추상 계층만 생각하면 된다. 

![image](https://user-images.githubusercontent.com/16812446/111748798-54146880-88d4-11eb-8835-e471bb5c2cef.png)

그러므로 본질과 원류를 추적하는 공부는 좋지만 컴퓨터 공학에서는 위와 같은 논리 게이트의 내부를 블랙박스로 표현하고 그 내부는 물리학자와 전자공학자들이 잘 설계했다고 믿는 것이다. 그러므로 이것이 컴퓨터 공학의 밑바닥이다. 더 이상 내려가면 컴퓨터 공학의 영역이 아니다.

## Primitive and Composite Gates

모든 논리 게이트가 And, Or, Not 으로 구성되지만, 이것을 합성하여 좀 더 복잡한 다변수 함수를 만들어낼 수 있다. 가령 $\text{And} : \{0, 1\} ^{2} \to \{0, 1\}$ 이지만 

$$ \text{And} (a, b, c) = \text{And} (\text{And} (a, b), c) = (a \cdot b) \cdot c = a \cdot b \cdot c $$

와 같은 합성함수를 만들어낼 수 있다. 

!!! note

    이것은 결합법칙이 성립하기 때문에 가능하다. 그렇다면 컴퓨터 공학이 성립하게 된 대수구조를 규명할 수 있다. 마그마? 반군? 모노이드? 군? 환? 가환환? 체? 순서체? 완비순서체? 완비순서체는 실수체니까.. 컴퓨터는 이산적이니까 아닐 것 같다. 컴퓨터가 세워져있는 대수구조는 뭘까?

    컴퓨터의 대수구조를 정의하면, 컴퓨터 위에 설계된 모든 것을 대수구조를 기반으로 형식화할 수 있다. 이것이 이루어지면 좋은 점은, 컴퓨터의 모든 것을 통일된 하나의 추상적 표현으로 표현가능하다는 것이다. 

    그렇게 되면 [취약점에 관하여](../../vul/memo) 에서 했던 이야기를 좀 더 현실화시킬 수 있다.

    어쩌면 추상대수학 보다는 카테고리 이론으로 좀 더 손쉽게 컴퓨터를 추상적 표현으로 형식화시킬 수도 있을 것 같다.

한 가지 예시만 더 들면 Xor 게이트는 다음과 같은 합성함수로 정의된다.

$$ \begin{equation}\begin{split} \text{Xor} (a, b) &= \text{Or} (\text{And} (a, \text{Not}(b)), \text{And} (\text{Not} (a), b))\\ & = (a \cdot \bar{b}) + (\bar{a} \cdot b) \end{split}\end{equation} \tag*{} $$

!!! note

    그런데 이 논리 게이트를 통하여 튜링기계의 universal machine 의 모든 부품이 구현 가능했던 것이지.

## Hardware Description Language (HDL)

실제로 하드웨어를 설계할 때에는 위에서 했던 것처럼 수작업을 하지 않고 HDL 이라는 언어를 사용한다. 이 언어로 프로그램을 짜고 테스트를 해보는 것이지.

![image](https://user-images.githubusercontent.com/16812446/111748900-68586580-88d4-11eb-908a-ca95244d1dbe.png)

위와 같이 HDL 을 사용하여 Xor 게이트를 설계하고 테스트하는 것이다.

HDL 이 하드웨어 구현 언어이기 때문에 HDL 으로 프로그램을 짜고 디버깅하는 것은 소프트웨어에서 하던 그것과 매우 유사하다. 다만 차이점은 컴파일러를 사용하지 않고 하드웨어 시뮬레이터를 사용하여 디버깅하게 된다는 것이다. 

> p 34

## Multi-Bit Versions of Basic Gates

컴퓨터 하드웨어는 bus 라고 부르는 multi-bit array 를 연산하도록 설계된다. 가령 32비트 컴퓨터는 두 개의 32비트 버스 위에서 설계된 And 함수를 동작시킬 수 있다. 32비트 시스템에서는 게이트들이 32비트 입력 버스와 32비스 출력 버스를 갖도록 설계된다.

!!! tldr ""

    Multi-Bit Boolean 함수 : $n$비트 시스템에서 $m$ 개의 입력을 Boolean 함수는 

    $$ f: \{0, 1\} ^{n}
    $$

!!! tldr ""

    Multi-Bit Not : $n$비트 시스템의 $\text{Not}$ 게이트는 함수 

    $$ f: \{0, 1\} ^{n} \to \{0, 1\} ^{n}, (x_1, \dots, x _{n}) \mapsto (\lnot x_1, \dots, \lnot x _{n})$$

    이다.

!!! tldr ""

    Multi-Bit And : $n$비트 시스템의 $\text{And}$ 게이트는 입력으로 a[n], b[n] 을 받아서 out[n] = And(a[n], b[n]) 의 출력을 낸다.

!!! tldr ""

    Multi-Bit Or : $n$비트 시스템의 $\text{Or}$ 게이트는 입력으로 a[n], b[n] 을 받아서 out[n] = Or(a[n], b[n]) 의 출력을 낸다.

!!! tldr ""

    Multi-Bit Mux : $n$비트 시스템의 $\text{Mux}$ 게이트는 입력으로 a[n], b[n], sel 을 받아서 sel=0 이면 출력 out[n]=a[n] 을 내고 sel=1 이면 출력 out[n]=b[n] 을 낸다.

다음은 1비트 Mux 의 설계이다.

![image](https://user-images.githubusercontent.com/16812446/112252863-25fea200-8ca1-11eb-96a5-73c7b93e2b31.png)

다음은 1비트 DMux 의 설계이다.

![image](https://user-images.githubusercontent.com/16812446/112252911-3c0c6280-8ca1-11eb-9389-36ed5342ebb0.png)

다음은 m-way n-bit Mux 의 설계이다.

![image](https://user-images.githubusercontent.com/16812446/112253036-69f1a700-8ca1-11eb-900a-fc36850f5409.png)

다음은 m-way n-bit demultiplexor 의 설계이다.

![image](https://user-images.githubusercontent.com/16812446/112253206-9b6a7280-8ca1-11eb-9e09-bd0cbfa4efa4.png)

2개의 입력을 받는 논리 게이트는 임의의 입력을 받도록 일반화될 수 있다.

!!! tldr ""

    $n$-way Or gate : $n$비트 입력 in[0], in[1], ..., in[n-1] 을 받아서 출력 Or(in[0], in[1], ..., in[n-1]) 을 낸다.

## Implementation

수학에서의 공리처럼 기초 게이트들은 그것으로부터 만들어질 수 있는 모든 것의 기반이 된다. 지금은 기초 게이트(공리)로써 Nand 만을 채택한다.

이 Nand 로 다음과 같은 게이트를 구현할 것이다. 물론 게이트의 구현 방법은 어떤 정리를 증명하는 방법이 유일하지 않듯이 유일하지 않다. 더 간단할수록 좋은 구현(좋은 증명)이다. 

- Not, And, Or/Xor, Multiplexor/Demultiplexor, Multi-Bit Not/And/Or, Multi-Bit Multiplextor, Multi-Way Gates

물론 우리가 공리로 Nand 를 채택한 것처럼 다른 공리체계를 기반으로 컴퓨터를 설계할 수도 있다. 가령 Nor 게이트만으로도 완전한 컴퓨터를 구성해낼 수 있다. 이것은 기하학에서 다른 공리를 채택하여 기하학 체계의 정리들을 도출해내는 것과 이론적으로 동치이다.

!!! note

    그러면 우리가 어떤 프로그램을 만들고자 했을 때 그 프로그램을 "증명 대상" 라고 할 수 있겠고 우리가 사용할 수 있는 레고 블럭들을 "공리" 와 "정리" 라고 할 수 있다. 대상을 증명하기 위한 방법이 유일하지는 않지만 가장 단순하고 효율적으로 공리와 정리로 대상을 증명하는 것이 좋겠지.

    그리고 증명된 대상(우리가 만든 프로그램)은 또 하나의 정리가 되므로, 이 정리를 나중에 다시 사용할 수 있도록 형식화하는 것도 중요할테고.

    한편 이로써 애초에 컴퓨터 프로그램을 만드는 것은 하드웨어 설계자가 제공하는 공리와 정리들을 사용하는 것임을 알 수 있다. 그런데도 우리는 하드웨어가 제공하는 공리와 정리를 사용하는 것이 아니라 이미 그 위에 많이, 그리고 높이 쌓여있는 잘 마련된 정리를 사용한다. 즉, syscall 을 사용하여 프로그래밍을 하는 것이 아니라 print 함수를 사용하여 프로그래밍을 한다는 말이다. 

    이로써 [취약점에 관하여](../../vul/memo) 에서 했던 이야기를 좀 더 설득시킬 수 있다. 즉, 컴퓨터는 완전 체계이고, 어떤 프로그램에 정의한 대상이 유일하다고 잘못 가정한 곳이 있다면 그 잘못 가정한 것에 대한 증명, 즉 완전 체계 내에서의 증명 시도 및 증명 가능성을 곧 "취약점" 으로 정의할 수 있고, 그것을 익스플로잇 하는 것을 "해킹" 으로 정의할 수 있다. 

    이것은 상당한 효용을 가져다 주는데 섀넌이 정보를 수학으로 형식화했었듯 해킹이나 취약점 같은 게 수학적으로 형식화되기 때문이다. 수학적으로 형식화된 대상은 기계적으로 다룰 수도 있다. 모든 수학적 대상을 완전 체계로 사상시킬 수는 없기 때문에.. 불완전 체계에 속하거나 메타수학에만 존재하는 수학적 대상은 컴퓨터로 표현할 수 없으니까.

# 2. Boolean Arithmetic

이 장에서는 산술 연산을 할 수 있는 논리 설계를 할 것이다. 시작점은 이전 장의 논리 게이트이고, 마무리는 ALU 가 될 것이다. 먼저 바이너리 코드와 Boolean 연산을 살펴보고 덧셈 회로를 만들어볼 것이다. 

바이너리 덧셈은 LSB 부터 시작하여 carry bit 가 발생하면 윗 자리로 넘겨서 MSB 가 더해질 때까지 더한다. 이때 다음과 같이 overflow 가 발생할 수도 있다.

![image](https://user-images.githubusercontent.com/16812446/111749777-9a1dfc00-88d5-11eb-952e-285264e2ad0a.png)

바이너리로 음수를 표현하기 위해서는 양수와 음수를 더해서 $0$ 가 나오도록 하기 위하여 2's complement 를 사용한다. 어떤 수 $x$ 의 2's complement 는 

$$ \bar{x} = \begin{cases} 2 ^{n} - x & x \neq 0\\ 0  & x = 0\\ \end{cases} $$

으로 정의된다. 가령 $4$ 비트 시스템에서 양수와 음수를 다음과 같이 표현한다. 맨 앞의 비트가 MSB 라는 건 모두들 너무 잘 아니까, 이게 signed 형식으로 숫자를 표현한다는 건 자명하겠지요.

![image](https://user-images.githubusercontent.com/16812446/111751016-4f04e880-88d7-11eb-8113-1ba20cc18cf9.png)

2's complement 로 숫자를 표현하는 것의 특징은 놀랍게도 음수에서 그냥 덧셈을 그대로 적용해도 잘 더해진다는 것이다. 이러한 덧셈을 기반으로 뺄셈은 양수에 음수를 더하는 것으로 쉽게 정의된다. 

이러한 이론적 기반으로 ALU 는 산술 연산과 논리 연산을 모두 지원하도록 설계되어있다. 이제 ALU 를 만들어볼텐데 가장 기본적인 adder 칩부터 만들어보자.

## Adders

이제 multi-bit adder 를 만들기 위하여 다음과 같은 adder 를 먼저 설계하자. 

- Half-adder : 2bits adder 

- Full-adder : 3bits adder 

- Adder(multi-bit adder) : n-bit adder

또 incrementer 라는 특별한 adder 도 설계할 텐데 주어진 숫자에 1 을 더하는 칩이다.

Half-adder 를 다음과 같이 설계한다. MSB 를 carry 비트라고 표현했다.

![image](https://user-images.githubusercontent.com/16812446/111752902-968c7400-88d9-11eb-9341-b42a94fd97bc.png)

Full-adder 를 다음과 같이 설게한다. Half-adder 에서처럼 덧셈 결과의 LSB 와 carry 비트 두 개만 출력한다.

![image](https://user-images.githubusercontent.com/16812446/111753335-16b2d980-88da-11eb-9e52-30893799ebd1.png)

n 비트 덧셈을 위한 Adder 를 다음과 같이 설계한다. n 은 16, 32, 64 등이 될 수 있다. 이 adder 를 multi-bit adder 라고도 하고 그냥 adder 라고도 한다. 다음 사진으 16 비트 adder 를 표현한다.

![image](https://user-images.githubusercontent.com/16812446/111753295-0bf84480-88da-11eb-89bc-911ddf46dd85.png)

다음은 incrementer 의 설계이다. 

![image](https://user-images.githubusercontent.com/16812446/111753578-609bbf80-88da-11eb-94c1-ba137ade86d9.png)

## ALU 

위에서 소개한 adder 는 상당히 범용적이라 어떤 컴퓨터에서도 사용될 수 있다. 그에 반해 이 섹션에서는 Hack 이라는 컴퓨터 플랫폼에서 사용하는 ALU 를 소개한다. 또 이 ALU 의 설계 원리가 상당히 범용적이라는 것도 설명한다.

Hack 플랫폼의 ALU 는 함수 16 비트 입력 $x, y$ 와 16 비트 출력 $o$ 에 대하여

$$ o = f_i(x, y) $$

를 계산한다. 이 함수 $f_i$ 는 18 가지 경우의 정해진 함수이며, 산술 연산이나 논리 연산을 수행하게 된다. 함수 선택은 control 비트라고 불리는 6 비트의 입력을 통해 정해진다. 입출력의 상세는 슈도코드로 다음과 같이 정의된다. 

![image](https://user-images.githubusercontent.com/16812446/111755848-e4ef4200-88dc-11eb-80ee-2007fb43b20c.png)

![image](https://user-images.githubusercontent.com/16812446/111755878-ee78aa00-88dc-11eb-8f40-ee2dd28c79fe.png)

ALU 는 6 비트의 control 비트로 연산을 정의하는데 6 비트니까 $2 ^{6}=64$ 가지의 기능을 표현할 수 있긴하다. 어쨌든 ALU 의 18 가지 기능은 다음과 같다.

![image](https://user-images.githubusercontent.com/16812446/111760927-9fce0e80-88e2-11eb-9990-05728a38f600.png)

가령 12번째 줄에서 $x-1$ 을 계산할 때 $zx = nx = 0$ 이어서 입력 $x$ 가 zero 가 되지도 않고 반전되지도 않는다. $zy = ny = 1$ 인데 이로써 입력 $y$ 가 zero 가 된 다음 반전된다. 그래서 $y$ 은 처음에 $000 \dots 00$ 이 되었다가 $-1$ 을 뜻하는 $111 \dots 11$ 이 된다. 이때 $f = 1$ 이므로 산술 덧셈이 연산으로써 선택되어 $x+(-1)$ 연산을 하게 된다. 이로써 $x-1$ 연산이 수행되는 것이다. 

## Perspective 

이렇게 ALU 를 설계해보았었는데 이는 최적화가 전혀 고려되지 않은 설계이긴 한다. 가령 carry 비트를 LSB 에서 MSB 까지 전달하는데 많은 시간이 걸린다. 이는 carry look-ahead 기술이라는 최적화 기술로 해결된다.

어떤 컴퓨터든 하드웨어와 소프트웨어 플랫폼의 전반적인 기능성은 ALU 와 OS 를 기반으로 한다. 그러므로 얼마나 많은 기능을 ALU 에 넣을지는 비용/성능의 문제에 달려있다. 일반적으로 산술/논리 연산을 많이 구현하면 비용이 더 들지만, 성능은 높아진다. 

이러한 trade-off 가 있는데 우리는 기능을 덜 구현하고 소프트웨어 레벨에서 더 많은 기증을 구현하도록 한 것이다. 가령 우리의 ALU 에는 곱셈이나 나눗셈 floating point 연산이 없다. 우리는 이 기능과 여타 수학적인 기능을 OS 레벨에서 구현해볼 것이다.

참고로 ALU 의 상세한 설계에 대해서는 대부분의 컴퓨터 구조 전공서적에 자세히 나와있으니 한번 봐라.

# 3. Sequential Logic

지금까지 만든 Boolean, 산술 칩들은 combinational 하다. combinational 칩은 오직 입력의 조합에 의하여 기능이 결정된다. 이들은 ALU 같은 연산 칩에 중요한 기능을 제공하지만 어떤 상태를 관리할 수는 없다. 이제 메모리를 관리할 수 있는 칩을 만들텐데 이런 것들을 sequential 칩이라고 한다.

이것의 구현은 동기화, 클럭킹, 피드백 루프 등이 관련된 복잡한 설계가 필요한데, 그것의 기반에는 플립플롭이 있다. 플립플롭으로 binary cell 에서부터 레지스터까지 만들어볼 거야.

어떤 것을 기억하는 것은 시간 의존적이다. 그러므로 시간의 흐름을 표현할 수 있는 표준적인 수단을 만들어보자.

- Clock : 컴퓨터는 교류신호(0-1, low-high, tick-tack, etc.) 를 번갈아 전송하는 oscillator 에 의하여 시간을 구현한다. "tick" 이 시작되고 "tock" 으로 끝나는 하나의 주기를 cycle 이라고 한다. 이 신호가 회로에 의하여 컴퓨터의 모든 sequential 칩으로 전달된다.

- Filp-Flops : 컴퓨터의 sequential 칩은 filp-flop 을 기반으로 설계된다. flip-flop 은 여러가지 variant 들이 있는데, 우리는 1 비트 입력과 1 비트 출력을 내는 DFF 라고 부르는 data flip-flop 을 살펴볼 것이다. DFF 는 Clock 의 입력을 받아서 시간 기반의 기능 $\text{ out }(t) = \text{ in }(t-1)$ 을 구현한다. 이것을 기반으로 컴퓨터가 상태를 관리할 수 있도록 하여 단순한 binary cell 부터 RAM 까지 구현할 수 있다.

- Register : 레지스터는 어떤 값을 기억하는 기능을 한다. 즉, $\text{ out }(t) = \text{ out }(t-1)$ 의 기능을 한다. 반면 DFF 는 오직 이전 입력에 의하여 기능한다. 즉, $\text{ out }(t) = \text{ in }(t-1)$ 이다. 레지스터는 다음과 같이 DFF 에서 단순히 출력을 그 입력으로 리다이렉트 시킴으로써 구현될 수 있다. 즉, 단순히 임의의 시간 $t$ 에 대하여 시간 $t-1$ 의 출력을 다시 출력해준다는 것이다.

![image](https://user-images.githubusercontent.com/16812446/111954277-30972b00-8b2b-11eb-825d-9aa2253a9494.png)

위 그림에서 가운데 설계는 모호하다. 두 입력 중 어느 것을 사용할지 명확하게 지시하지 않기 때문이다. 이 모호함을 multiplexor 하나를 붙여서 해결할 수 있다. 이 Mux 의 select bit 를 load bit 라고 하는데 레지스터의 새로운 값을 저장하고 싶을 때 load bit 를 1 로 두면 되고, 기존의 값을 유지한채 그 안의 값을 가져오고 싶을 때 load bit 를 0 으로 두면 된다.

이것을 기반으로 다음과 같은 multi-bit 레지스터도 쉽게 구현가능하다. 이 설계의 파라미터는 레지스터의 width 이다. width 는 레지스터가 몇 비트를 저장할 것인지 결정한다. 보통 16, 32, 64 비트가 된다. multi-bit 레지스터 내부의 데이터를 보통 words 라고 부른다.

!!! note

    레지스터가 꽤 오랫동안 32비트였으니까 WORD 가 4바이트를 뜻하게 된 거겠지? Double word 는 8바이트인가.

![image](https://user-images.githubusercontent.com/16812446/111954864-114ccd80-8b2c-11eb-843a-a2c7acd168b2.png)

- Memory : multi-bit 레지스터를 한번 구현해놓으면, 임의의 길이의 memory 도 쉽게 구현가능하다. 다음과 같이 레지스터들을 단지 쌓아놓은 것이 RAM 이 되는 것이다. random accses memory 라는 이름은 임의의 위치의 데이터를 위치에 관계없는 동일한 속도로 읽거나 쓸 수 있게끔 구현했다는 말이다.

이런 개쩌는 구현은 다음과 같이 이루어진다.

1. n 개의 레지스터로 구현된 RAM 의 각각의 word 에 주소값(0 부터 n-1)을 부여한다. 

2. n 레지스터의 배열을 만들뿐 아니라 주소값 j 가 주어지면 주소값 j 를 갖는 레지스터를 선택할 수 있는 논리 게이트 설계를 만든다. 이 주소값은 물리적으로 대응되지 않고, 논리적으로 대응된다. 

RAM 은 입력 데이터, 주소값, load bit 라는 3가지 입력을 받는다. load=0 이면 읽기이고 load=1 이면 쓰기이다. RAM 의 설계 파라미터는 width 와 size 이다. width 는 레지스터가 저장할 비트(word)이고, size 는 word 들의 갯수이다.

![image](https://user-images.githubusercontent.com/16812446/111955228-97691400-8b2c-11eb-8621-687e4138b4ff.png)

- Counters : 카운터는 매 시간 단위마다 상태값을 증가시키는 sequential 칩이다. 즉, $\text{ out }(t) = \text{ out }(t-1) + c$ 의 기능을 한다. $c$ 는 보통 1 이다. 

카운터는 컴퓨터에서 중요한 역할을 한다. 가령 program counter 는 다음에 실행할 명령어의 주소값을 저장하는데, 이때 카운터가 사용된다.

카운터는 adder 와 0 으로 세팅할 수 있는 논리 게이트와 새로운 base 를 세팅할 수 있는 기능과 증가 대신 감소를 할 수 있게 하는 기능으로 설계된다.

- Time Matters : 이 장에서 소개한 모든 칩은 sequential 이고, sequential 은 DFF 를 하나 이상 갖고 있는 칩이다. DFF 는 메모리 유닛에 상태를 유지할 수 있는 기능을 제공하거나, counter 처럼 상태를 조작할 수 있는 기능을 제공한다.

![image](https://user-images.githubusercontent.com/16812446/111963878-5fb39980-8b37-11eb-836d-7b0b5df1f72d.png)

기술적으로 말하면 이 기능은 위와 같은 피드백 루프를 통하여 이루어진다. 시간 t 에서의 출력은 t-1 에서의 출력에 의존적이다. 이것을 기반으로 sequential 칩은 중요한 능력을 얻는다. 그것은 컴퓨터의 전반적인 구조를 동기화시킬 수 있다는 것이다. 

가령, ALU 에 x+y 연산을 하려 하는데 x 의 데이터는 레지스터에 있고 y 의 데이터는 RAM 에 있다고 하자. 그러면 여러가지 물리적 제한(거리, 저항, 간섭, 노이즈 등등) 때문에 x 와 y 의 데이터가 동일한 시간에 ALU 에 도착할 수 없다. 그러나 ALU 는 시간에 독립적인 combinational 칩이므로, x 와 y 의 데이터가 도착할 때까지 쓰레기값을 출력하게 된다. 하지만 ALU 의 출력이 항상 sequential 칩의 통제를 받기 때문에, 우리는 실제로 ALU 의 출력이 쓰레기값인지 아닌지 걱정한 적이 없다.

우리가 해야 할 일은 Clock 을 설계할 때 cycle 을 컴퓨터 구조 내에서 어떤 칩에서 다른 칩으로 비트가 이동하는 가장 먼 거리에 대한 시간보다 살짝 더 길게 만드는 것이다. 이로써 우리는 sequential 칩이 그 상태를 cycle 이 다 되어서 업데이트 할 때 ALU 가 받은 입력이 쓰레기 값이 아니라는 보장을 얻을 수 있다. 

## Specification

이제 다음과 같은 sequential 칩을 설계해보자. 

- Data-flip-flops (DFFs)

- Registers (based on DFF)

- Memory banks (based on registers)

- Counter 칩 (based on registers)

DFF 게이트는 다음과 같이 비트를 입력받아서 비트를 출력한다. Nand 게이트처럼 DFF 게이트는 컴퓨터의 가장 맨 밑바닥에 존재하여 레지스터, 메모리, 카운터의 기반이된다. 모든 DFF 는 하나의 Clock 과 연결된다. Clock cycle 이 시작될 때 DFF 의 모든 출력은 이전 시간 단위 동안 입력에 커밋된다. 다른 때에는 DFF 가 잠금상태가 되어 입력을 바꾸는 것이 출력에 즉각적인 영향을 미치지 않게 된다.

![image](https://user-images.githubusercontent.com/16812446/111976095-9b089500-8b44-11eb-834c-1b21419ef754.png)

싱글비트 레지스터, 혹은 Bit, 혹은 binary cell 은 1 비트 정보를 저장하도록 다음과 같이 설계된다. load 비트가 1 이면 write 라서 내부 내용이 바뀐 후 출력되고, 0 이면 read 라서 내부 내용이 그냥 출력된다.

![image](https://user-images.githubusercontent.com/16812446/111978073-defc9980-8b46-11eb-8035-4ee95479dedf.png)

멀티비트 레지스터는 다음과 같이 16비트 width 로 설계된다. 물론 현재의 컴퓨터는 보통 64비트 레지스터이다.

![image](https://user-images.githubusercontent.com/16812446/111978133-ef147900-8b46-11eb-9403-c3f09452c50b.png)

RAM 은 레지스터의 배열이다. w-비트 레지스터가 n 개의 배열로 쌓인 것이다. 우리는 다음과 같은 16비트 width 를 갖는 RAM 을 만들어 볼 것이다. RAM 의 Read 와 Write 기능은 다음과 같다.

- Read : m 번째 레지스터의 값을 읽고 싶다면, address 에 m 이라고 입력하면 된다. 그러면 출력이 곧바로 나오는데 이는 combinational 기능이라 Clock 에 독립적이다.

- Write : m 번째 레지스터에 값을 쓰고 싶을 때, address 에 m 이라고 입력하고 데이터 d 를 in 에 입력한다. Write 를 사용하려면 load 비트가 활성화되어 있어야 한다. 다음 Clock cycle 부터 해당 레지스터는 새로운 값 d 를 갖게 된다.

![image](https://user-images.githubusercontent.com/16812446/111978605-7104a200-8b47-11eb-98d8-58db68d661cd.png)

!!! note

    Meltdown 은 소프트웨어 설계가 모순적으로 되었을 때 발생하는 취약점만이 취약점이 아니라 하드웨어 설계가 모순되었을 때도 취약점이 발생한다는 것을 말해준다. 

Counter 도 Specification 을 정의해두자. 기본적으로 Clock cycle 마다 1 을 증가시킬 수 있어야 하고, 주소값 n 에 있는 명령어로 점프했을 시 카운터의 값을 n 으로 수정한 후 다시 1 씩 증가시켜야 한다. 그러므로 Counter 도 레지스터와 상당히 비슷한 기능을 한다. 다만 Counter 는 reset 과 inc 라는 control 비트를 가질 뿐이다.

- inc=1 이라면 매 Clock cycle 마다 증가연산을 하게 되고, out(t)=out(t-1)+1 을 출력한다. 

- reset 비트가 활성화되면 Counter 의 값이 0 이 된다. 

- Counter 의 내용을 d 로 바꾸고 싶다면 in 입력에 d 를 넣고 load 비트를 활성화시킨다.

다음 그림은 컨트롤 비트(reset, load, inc) 가 0 으로 설정되어 있는 상태에서 시작된 Counter 의 예시이다.

![image](https://user-images.githubusercontent.com/16812446/112243814-93a2d200-8c91-11eb-9414-988fef4627d4.png)

## Implementation

- Flip-Flop : DFF 게이트는 논리 게이트로부터 완성될 수 있지만, 이 책은 DFF 를 built-in 으로 다루어 구현하지 않는다.

- 1-Bit Register (Bit) : 1비트 레지스터의 구현은 위 사진에서 자세히 설명되어있다.

- Register : 멀티비트 레지스터는 1비트 레지스터를 쌓아놓은 것이다. 우리가 할 일은 load 입력을 모든 레지스터에 뿌려주는 것이다.

- 8-Register Memory(RAM8) : 8 개의 레지스터 배열을 쌓아서 만들면 된다. 그리고 address 입력을 받아서 해당 레지스터에 입력 in 와 load 를 전달하면 되고, 해당 레지스터의 out 을 출력하면 된다.

- n-Register Memory(RAM8) : 임의의 길이의 메모리는 작은 메모리 유닛으로부터 재귀적으로 구성할 수 있다. 가령 아래 그림의 오른쪽 부분과 같이 64-레지스터는 8-레지스터로 재귀적으로 구성할 수 있다. 64-레지스터의 주소값은 6비트로 구성하여 xxxyyy 의 형태를 띈다. MSB 인 xxx 부분은 RAM8 의 칩을 선택하고 LSB 인 yyy 는 RAM8 중 하나의 레지스터를 선택한다.

![image](https://user-images.githubusercontent.com/16812446/112251726-21d18500-8c9f-11eb-8254-f12febd4b378.png)

- Counter : w 비트 카운터는 w 비트 레지스터와 combinational 논리 게이트로 설계된다. combinational 칩은 카운팅과 카운터의 상태를 설정하게 된다.

# 4. Machine Language

컴퓨터는 하드웨어 플랫폼이 어떤 칩으로 설계되었는지 설명할 수 있다는 점에서 constructive 하다. 한편 컴퓨터를 기계어로 설명할 수 있다는 점에서 abstract 하다. 새로운 컴퓨터를 마주했을 때 그것의 기계어를 익히는 것이 컴퓨터와 친해질 수 있는 편리한 방법이다. 이 방법으로써 어떻게 컴퓨터의 프로그램을 유용하게 짤 수 있는지 알 수 있고, 왜 하드웨어가 그렇게 설계되었는지 알 수 있다. 이 챕터와 다음 챕터 Computer Architecture 를 기반으로 범용 컴퓨터를 완성할 것인데, 이는 챕터 1-3 에서의 칩을 기반으로 설계된다.

기계어는 합의된 형식주의라서, 일련의 기계어 수열로 프로그램을 짤 수 있다. 

고수준 언어의 설계 목표가 일반성과 표현의 강력성이라면, 저수준 기계어의 설계 목표는 주어진 하드웨어 플랫폼에 대한 직접 실행과 완전한 통제이다.

기계어는 하드웨어와 소프트웨어가 처음으로 만나는 심오한 인터페이스이다. 왜냐하면 기계어는 프로그래머의 추상적 생각이 형식적 기호로 표현되어 하드웨어에서 실행되는 지점이기 때문이다.

기계어가 하드웨어를 완전히 제어할 수 있도록 설계되었다고 했지만, 하드웨어는 마찬가지로 주어진 기계어를 실행할 수 있도록 설계되었다.

## Background 

### Machines

!!! tldr ""

    기계어(machine language) : 프로세서와 레지스터들을 사용하여 메모리를 조작할 수 있도록 설계된 합의된 형식주의 언어이다.

- Memory : 메모리는 데이터와 기계어를 저장할 수 있는 연속적인 기억장치 배열이다.

- Processeor : 프로세서는 Central Processing Unit(CPU) 로써 일련의 기계어를 실행할 수 있는 장치이다. 산술연산이나 논리연산을 할 수 있다.

- Register : CPU 가 메모리에 접근하려면 시간이 오래걸려서 CPU 가 빠르게 접근할 수 있도록 단일 값을 저장할 수 있는 저장장치이다. 레지스터의 목적은 프로그래머가 메모리 접근 명령어의 사용을 최소화하여 프로그램 실행 속도를 높이도록 하는 것이다.

### Language

기계어 프로그램은 16비트 명령어(16자리 이진법 수)의 수열이다. 가령 16 비트 시스템의 어느 한 명령어는 $1010001100011001 _{2}$ 와 같이 표현된다. 이러한 16자리 이진법 수가 어떤 의미인지 알기 위하여 하드웨어 플랫폼의 규칙을 이해해야 한다. 가령 이런 명령어는 4비트 필드로 구성되어 있는데, 첫 4비트 필드는 CPU 의 어떤 기능을 지시하고, 나머지 4비트 필드들은 파라미터를 명시하게 된다. 이런 규칙은 전적으로 하드웨어 설계과 기계어 문법에 의해 결정된다.

한편 이러한 이진법 수가 사람이 알아보기 쉽지 않으므로 일대일 대응되는 기호가 제공된다. 가령 $1010$ 이 add 를 나타내고 이후의 4비트 필드들이 R3, R1, R9 레지스터를 나타내는 것이라면 `add R3 R1 R9` 와 같은 형식문으로 사상되는 것이다. 

!!! note

    이는 전단사 사상이다. 만약 전단사 사상이 아니면 실수인 것이다. 왜냐하면 기호적인 형식문으로 컴파일된 바이너리 이외의 이진수 명령어가 존재한다면, 그것으로 인하여 발생하는 영향을 예측할 수 없기 때문이다. 이런 경우는 전사 사상일 것이다.

    만약 단사 사상이면 아키텍처 메뉴얼을 잘못 작성한 것이 될 것이다. 그렇게 심각한 문제는 아니다.

우리는 이진수 명령어가 아니라 기호적인 형식문으로 기계어 프로그램을 작성한다. 왜냐하면 이진수들로 코딩을 하기에는 너무 어렵기 때문이다. 그러나 형식문과 실제 기계어 코드에는 전단사 사상이 있으므로 형식문으로 프로그램을 짜두면, 그것을 이진수 기계어 코드로 일대일 대응시킬 수 있다. 이 이진수 기계어 코드가 비로소 CPU 에 입력되어야 하기 때문이다. 

형식문으로 된 그러한 프로그램을 assembly language 라고 하고, 그것을 기계어로 전단사시키는 사상을 assembler 라고 한다.

컴퓨터들은 CPU 기능, 레지스터 개수와 타입, 어셈블리 형식문의 문법이 다르지만, 다음과 같이 모든 기계어가 공통적으로 제공하는 명령어들이 존재한다.

### Commands

- 산술/논리 연산 : 모든 컴퓨터는 덧셈과 뺄셈같은 기본적인 산술 연산을 지원하고, bit-wise negation 이나 bit shift 같은 기본적인 Boolean 연산을 지원한다.

- Memory Access : 모든 메모리 접근 명령어는 두 종류이다. 하나는, 레지스터와 메모리의 데이터에 작동하는 산술연산과 논리연산이다. 두번째는, 레지스터와 메모리 사이의 데이터를 이동하도록 하는 load, store 명령이다.

    메모리 접근 명령어를 사용하기 위해서는 주소값을 표현해야 하는데, 컴퓨터에 따라 주소값 표현 방식이 달라진다. 그러나 모든 컴퓨터는 다음과 같은 주소 표현식을 지원한다. 

    - Direct addressing : 해당 주소값의 절대값으로 표현하는 것이다. 가령 `load r1, 67` 은 Memory[67] 의 값을 r1 에 옮기겠다는 것이다.

    - Immediate addressing : 해당 값을 바로 표현하는 것이다. 가령 `loadi r1, 67` 은 Memory[67] 가 아닌 67 을 그대로 r1 에 옮기겠다는 것이다.

    - Indirect addressing : 해당 주소값을 상대값으로 표현하는 것이다. 이것이 필요한 경우는 어떤 주소값이 하드코딩되어 있지 않은 경우이다. 가령 `x=foo[j]` 라는 코드는 `foo` 라는 배열의 `j` 번째 word 단위 이후의 데이터를 가져와서 `x` 에 저장하겠다는 것인데 `foo` 의 주소값이 어디에 할당될지 아직 알 수 있기 때문에 `foo` 의 베이스 주소값에 `j` 만큼만 더하는 것이다. 그러면 이후에 프로그램이 실제로 실행될 때 `foo` 의 실제 주소값이 구체화될 것이다.

- Flow of Control : 선형적인 흐름으로 끝나지 않는 프로그램의 경우 여러가지 실행흐름이 생기고, 반복문도 생긴다. 이때 필요한 것이 conditional execution 이다. 이는 술어 $\phi (...)$ 를 만족할 때와 만족하지 않을 때 어떤 함수를 계산할 것인지 정하는 것과 같다. 이를 위하여 기계어는 jump 명령어를 제공하고, conditional 과 unconditional 명령어를 제공한다. 가령 unconditional jump 는 무조건 분기이고, conditional jump 는 조건 분기이다.

    Flow of Control 기계어는 다음과 같이 High-level language 로 사상된다.

    ![image](https://user-images.githubusercontent.com/16812446/112981072-a3408000-9195-11eb-8765-c3a66468043a.png)

## Hack Machine Language Specification

Hack 아키텍처는 다음 조건을 만족한다. 

- 폰 노이만 구조이다. 

- 16비트 시스템이다.

- instruction 메모리, data 메모리의 두 가지로 구분된 메모리 모듈을 갖는다.

- screen, keyboard 의 두 I/O 디바이스를 갖는다.

### Memory Address Spaces

Hack 시스템은 instruction 메모리와 data 메모리로 구분되어 있다. 두 메모리는 16비트 wide 에 15비트 주소 공간을 갖는다. 즉 16bit word 의 최대 32K 메모리 주소가 존재할 수 있다. 

instruction 메모리는 read-only ROM 메모리와 같다. 즉, 프로그램을 로드하는 것은 ROM 을 갈아치우는 것을 뜻한다. 따라서 Hack 플랫폼은 기계어 프로그램을 instruction 메모리로 로드하는 기능을 제공해야 한다.

### Registers

Hack 시스템은 16비트 레지스터 D, A 를 갖는다. 이 레지스터는 A=D-1 이나 D=!A 와 같이 산술연산과 논리연산을 수행할 때 사용된다. D 가 데이터를 저장할 때 사용되는데, A 는 데이터와 주소값 둘 다 저장하는데 사용된다. 즉, 상황에 따라 A 의 값이 주소나 데이터로 해석될 수 있다.

Hack instruction 이 16비트인데, 주소값은 15비트를 사용하므로 두 값을 하나의 instruction 에 표현하기란 불가능하다. 따라서 메모리 주소를 뜻하는 라벨 M 을 사용하는데, 이 M 은 항상 A 의 값을 가르킨다. 가령 D=Memory[516]-1 의 instruction 을 표현하기 위하여 516 을 A 에 저장하고 D=M-1 와 같이 표현한다. 

마찬가지로 jump 명령어를 사용할 때에도 instruction 에서 주소값을 직접 표현하지 않고, A 의 값을 참조한다. 가령 `goto 35` 를 위하여 먼저 A 에 35 를 저장하는 명령어를 사용하고, `goto` 명령어를 사용한다.

![image](https://user-images.githubusercontent.com/16812446/113295408-20edc280-9333-11eb-8066-b98ee8814140.png)

위의 예시는 1 부터 100 까지 더하는 예시이다. 보는 것과 같이 Hack 기계어는 원하는 주소값을 선택한 후, 원하는 명령어를 실행하는 식으로 기능하다. 전자의 address instruction 을 A-instruction 이라 하고 compute instruction 을 C-instruction 이라 한다. 

이때 `@value` 라는 특이한 문법이 있는데 `value` 는 어떤 값이나 값을 나타내는 기호가 될 수 있다. 이 명령어는 특정한 값을 A 레지스터에 저장한다. 가령 `sum` 이 메모리 주소 17 을 나타낸다면 `@17` 과 `@sum` 둘 다 `A` 에 17 을 저장한다는 뜻이다.

### A-instruction

![image](https://user-images.githubusercontent.com/16812446/113296711-ca818380-9334-11eb-8725-843c1f8ea0cc.png)

A-instruction 이란 `@value` 이다. `value` 는 음이 아닌 정수이다. A-instruction 은 위와 같이 레지스터 A 를 15 비트 값으로 초기화한다. 가령 `@5` 명령어는 A 를 `0000000000000101` 로 초기화한다.

### C-instruction

![image](https://user-images.githubusercontent.com/16812446/113297028-1cc2a480-9335-11eb-8dbf-bd41b45f14b6.png)

C-instruction 은 1) 무엇을 계산할지, 2) 계산된 값을 어디에 저장할지, 3) 그 이후에 뭘할지 라는 세 가지 질문으로 기계어 코드가 구성된다. 위와 같이 MSB 의 1 은 C-instruction 임을 의미한다. 그 다음 2 비트는 사용되지 않는다. 

C-instruction 의 문법은 `dest = comp;jump` 이다. `comp` 는 ALU 에게 무엇을 계산할지 지정하고, `dest` 는 계산된 ALU 출력을 어디에 저장할지 지정하고, `jump` 는 다음에 실행할 명령에 대한 점프 조건을 명시한다. 각각의 필드를 자세히 살펴보자. 

- The Computation Specification : Hack ALU 는 D, A, M 레지스터를 계산하도록 설계되었다. M 은 Memory[A] 를 뜻한다. `comp` 필드는 7 비트로 구성되었는데, 이로써 128 개의 기능을 구별할 수 있다. 하지만 다음과 같은 28 개의 기능만 사용한다.

    ![image](https://user-images.githubusercontent.com/16812446/113298696-0e758800-9337-11eb-9645-ff40f4ed334e.png)

- The Destination Specification : C-instruction 으로 계산된 값은 `dest` 필드의 3 비트가 지정하는 곳에 저장된다. 첫번째, 두번째 d 비트는 A 레지스터에 저장할지, D 레지스터에 저장할지 구별한다. 세번째 d 비트는 Memory[A] 와 같은 M 에 저장할지 결정한다. 

    ![image](https://user-images.githubusercontent.com/16812446/113299118-7e840e00-9337-11eb-8e7c-bb254ab110ca.png)

    가령 Memory[7] 의 값을 증가시키고 D 레지스터에 저장하려면 다음과 같은 기계어 코드를 입력하면 된다.

    0000 0000 0000 0111 // @7

    1111 1101 1101 1000 // MD=M+1

- The Jump Specification : `jump` 필드는 이후에 무엇을 할지 지정한다. 두 가지 가능성이 있는데 다음 명령어를 실행하거나, 다른 위치에 있는 명령어를 실행하는 것이다. 후자의 경우 A 레지스터가 위치 주소값을 지니고 있다고 가정한다. 

    `jump` 필드의 세 비트는 다음과 같이 ALU 출력이 특정 조건을 만족할 때 점프를 할지 결정한다. `out` 이 ALU 의 출력을 뜻하고, j1 이 활성화되면 양수 조건이 추가되고 j2 가 활성화되면 $= 0$ 조건이 추가되고 j3 가 활성화되면 음수 조건이 추가된다. 활성화된 조건 중 ALU 의 출력인 `out` 이 하나만 만족해도 점프를 하게 된다.

    ![image](https://user-images.githubusercontent.com/16812446/114166916-48fba800-9969-11eb-8ea5-352bfe6e6998.png)

    마지막 `JMP` 는 무조건 분기를 뜻한다.

### Symbols

어셈블리 명령어는 상수나 기호(Symbols)를 사용하여 메모리 주소를 표현할 수 있다. 기호는 다음과 같은 3가지 방법으로 표현된다. 

1. Predefined symbols: RAM 주소의 특별한 부분집합은 다음과 같은 Predefined symbols 로 표현된다. 

    - Virtual registers: 어셈블리 프로그래밍을 단순화하기 위하여 `R0` 부터 `R15` 는 각각 RAM 주소의 0 부터 15 를 표현하기 위해 사용된다.

    - Predefined pointers: `SP, LCL, ARG, THIS, THAT` 은 각각 RAM 주소의 `0` 부터 `5` 을 표현한다. 가령 주소 2 는 `R2` 로도 지칭할 수 있고 `ARG` 로도 지칭할 수 있다.

    - I/O pointers: `SCREEN, KBD` 는 각각 RAM 주소의 16384(0x4000) 과 24576(0x6000) 을 지칭한다.

2. Label symbols: `goto` 명령의 label 목적지를 표현하기 위한 사용자정의 기호이다. 이 기호는 `Xxx` 로 정의된다.

3. Variable symbols: `Xxx` 로 정의된 사용자정의 기호는 variable 로 여겨지며 어셈블러가 RAM 주소 16(0x0010) 로 시작되는 주소값을 부여한다.

### Input/Output Handling

Hack 플랫폼은 screen 과 keyboard 에 연결된다. 이 두 IO 장비는 memory map 을 통하여 컴퓨터와 상호작용한다. 가령 스크린에 픽셀을 그리기 위하여 스크린과 연관된 메모리에 바이너리 값을 써야한다는 것이다. 또 키보드의 입력을 받는 것은 키보드와 연관된 메모리의 값을 읽는 것이다. IO 장비와 연관된 메모리 맵은 refresh loop 에 의하여 동기화된다.

- Screen: Hack 컴퓨터는 512 픽셀을 갖는 256 행으로 구성되고 각 픽셀은 검정이나 흰색을 가진다. 스크린의 내용은 8K 메모리 맵으로 이루어지고, 이 맵은 RAM 주소 16384(0x4000) 에서 시작한다. 물리적 스크린의 각 행은 왼쪽 위에서부터 시작하고 이는 32개의 16비트 word 들로 표현된다. 

    즉, 한 행이 512 픽셀로 구성되었지만, 이것이 16비트 word 의 32개 블록으로 구성되었으므로 $r$ 행을 선택하기 위하여 $16384 + r \cdot 32$ 의 주소를 택한다. 그리고 512 픽셀의 열을 택하기 위하여 32개의 블록 중 $c/16$ 을 더하여 해당 블록을 택한다. 따라서 $16384 + r \cdot 32 + c / 16$ 으로 16비트 블록을 택할 수 있다. 이 블록 중에서 16비트 중 한 픽셀을 읽거나 쓰기 위하여 $c\%16$ 비트를 택하면 된다.

    따라서 r 행의 c 열은 $16384+r \cdot 32 + c/16$ 주소의 $c\%16$ 비트로 매핑된다. 스크린에 흑백을 쓰거나 읽기 위하여 이 메모리에 비트를 다음과 같이 쓰면된다. 1 을 쓰면 흑이고 0 을 쓰면 백이다.

    ```assembly
    @SCREEN
    M=1
    ```

    예를 들어서 0 행의 400 열을 읽거나 쓰기 위하여 $16384 + 0 \cdot 32 + 400 / 16 = 16384 + 0 + 25 = 16409$ 의 블록을 택하고, 이 블록은 16비트로 이루어져있으므로 이 블록 중에서 $400 \% 16 = 0$ 번째 픽셀이 비로소 0 행 400 열의 픽셀이 된다.

- Keyboard: Hack 컴퓨터의 키보드는 RAM 의 24576(0x6000) 의 한 word 에 매핑이된다. 키보드의 키를 누르면 이것은 16 비트 ascii 코드가 RAM[24576] 의 16비트 블록에 배핑이된다. 키보드를 누르지 않으면 이 블록에 0 이라는 값이 존재한다. 대표적인 ascii 코드는 다음과 같다.

    ![image](https://user-images.githubusercontent.com/16812446/114293822-52edea00-9ad4-11eb-96cd-c05813e5e4ff.png)

### Syntax Conventions and File Format

- Binary Code Files: 이 파일은 텍스트 라인들로 구성된다. 각 라인은 16 개의 0 또는 1 의 아스키 캐릭터 수열이다. 이 수열이 하나의 기계어를 나타낸다. 전체의 라인은 기계어 프로그램을 나타낸다. n 번째 라인이 n 번째 기계어 코드를 나타낸다. Hack 플랫폼의 기계어 프로그램은 `hack` 이라는 확장자를 가진다. 가령 `Prog.hack` 처럼.

- Assembly Language Files: 어셈블리 프로그램은 `asm` 확장자에 저장된다. 가령 `Prog.asm`. 어셈브릴 프로그램은 instruction 또는 symbol 을 나타내는 텍스트 라인으로 구성된다. instruction 은 A-instruction 혹은 C-instruction 을 뜻한다. symbol 은 label `Symbol` 에 메모리 주소값을 부여한다.

아래의 컨벤션은 어셈블리 프로그램에 적용되는 것들이다.

- Constants and Symbols: Constants 는 음이 아닌 수이다. 사용자 정의 symbol 은 글자, 숫자, "_", ".", "$", ":" 이 될 수 있다.

- Comments: // 은 주석이다.

- White Space: 공백문자는 무시된다.

- Case Conventions: 모든 assembly mnemonics 은 대문자이다. 다른 것들, 즉 사용자 정의 label 과 변수이름같은 것들은 case sensitive 하다. label 에는 대문자를 사용하고 변수 이름에는 lowercase 를 사용한다.

## Perspective

Hack 기계어는 정말 단순한 기계어이다. 다른 컴퓨터들은 더 많은 instruction, 더 많은 데이터 타입, 더 많은 registers, 더 많은 instruction format, 더 많은 주소값 지칭 모드를 가진다. 하지만 Hack 플랫폼에서 지원하지 않는 기능들은 소프트웨어에서 구현될 것이다. 가령 Hack 은 곱셈과 나눗셈을 지원하지 않는데 이는 OS 수준에서 구현될 것이다.

Hack 은 `@xxx` 뒤에 나오는 `D=D+M` 같은 기계어를 지원하는데 이것이 귀찮으므로 `D=D+M[xxx]` 으로 쓸 수 있고 `@yyy` 뒤에 나오는 `GOTO` 대신 `GOTO yyy` 로 쓸 수 있다.

# 5. Computer Architecture

# 6. Assembler

# 7. Virtual Machine I: Stack Arithmetic

# 8. Virtual Machine II: Program Control

# 9. High-Level Language

# 10. Compiler I: Syntax Analysis

# 11. Compiler II: Code Generation

# 12. Operating System

# 13. Postscript
