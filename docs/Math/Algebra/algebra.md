# 수식

!!! tldr ""

    수식 : 수학적 추상 대상물의 관계를 표현한 형식 언어이다.

- 넓은 의미에서 수학 기호를 사용하여 그 형식에 맞게 조합하여 만들어낸 글이다. 

- 자연언어가 글자로 단어를 만들고 문법에 맞게 조합하여 글을 만들어내듯이 수식 또한 언어의 일종이다.

- 대수학은 수식이라는 언어를 사용하여 세상을 표현하는 것을 배우는 것이라고 보는 관점이 있다.

- 수식의 분류는 다음과 같다. 

    - 관계식 

        - 등식 ($=$)

        - 항등식 (항상 성립한다)

        - 방정식 (성립하게 하는 특정한 해가 있다)

        - 부등식 ($<, >, \leq, \geq$)

        - 절대부등식 (항상 성립한다)

        - 조건부등식 (성립하게 하는 특정한 해가 있다)

- 예시 

    - 등식 $1 + 2 = 3$

    - 방정식 $x + 2 = 3$

    - 다항식 $x^2 + 2x + 3$

    - 부등식 $x + 2 > 3$

!!! tldr ""

    미지수(변수, variable) : 수식에 따라 변하는 값이다. 또는 아직 정해지지 않거나 구해야 하는 수를 뜻한다.

- 주로 $x, y, z, w$ 를 사용한다. 미지수가 시간일 경우 $t$ 를, 길이일 경우 $l$ 을, 너비(width)일 경우 $w$ 를, 높이일 경우 $h$ 를, 거리일 경우 $d$ 를, 각도일 경우 $\theta$ 를, 반지름일 경우 $r$ 등으로 나타낸다.

!!! tldr ""

    독립변수(independant variable) : 독립적으로 변하며 다른 변수에 영향을 주는 변수이다.

- 인과관계 및 현상에서 원인을 나타낸다.

- 컴퓨터공학에서 입력을 나타낸다.

- 통계학에서 회귀자(regressor) 라고 부른다.

- 인공지능에서 특징(feature) 라고 부른다.

!!! tldr ""

    종속변수(dependant variable) : 독립변수에 영향을 받아 변하는 변수이다.

- 인과관계 및 현상에서 결과나 효과를 나타낸다. 

- 컴퓨터공학에서 출력을 나타낸다.

!!! tldr ""

    방정식(equation) : 미지수의 값에 따라 참이 되기도 하고 거짓이 되기도 하는 등식이다.

- 이때 방정식을 참이 되게 하는 미지수의 값을 해 또는 근(solution) 이라 한다. 

- 방정식의 해가 존재하지 않을 경우 불능이라 하고, 해가 여러 개일 경우 방정식이라 하고, 모든 값이 해가 될 수 있는 경우 항등식(부정)이라 한다. 

- 예시 

    - $x^2 - 5x + 6 = 0$

!!! tldr ""

    불능 : 해가 존재하지 않는 방정식이다.

- 예시 

    - $0x = 7$

!!! tldr ""

    항등식 : 등식의 변수가 복소수 범위에서 어떤 값이 되든 항상 참인 등식이다.

- 예시

    - $(x+2)^2=x^2+4x+4$

    - $\sin ^2 \theta + \cos ^2 \theta = 1$

    - $\cos x + i\sin x = e^{ix}$ (오일러공식)

!!! tldr ""

    계수(coefficient) : 변수에 곱해진 상수이다.

- 예시 

    $2x^4$ 에서 계수는 $2$ 이고, $x^2$ 에서 계수는 $1$ 이다.

!!! tldr ""

    항 : 계수와 변수로 이루어진 대수적인 수의 표현방식이다.



!!! tldr ""

    단항식(monomial) : 수와 문자 간에 곱셈만을 이요해 표현한 식이다.

- 단 하나의 항으로 이루어진 다항식이다. 

- 예시

    - $5$

    - $2x$

    - $3xy^2$

!!! tldr ""

    수식의 분류

- 유리식 

    - 다항식

    - 분수식

- 무리식

## 다항식

!!! tldr ""

    다항식(polynomial) : 단항식들의 덧셈과 뺄셈으로 이루어진 식이다.

- 예시 

    $x^2 -2x + 3$

!!! tldr ""

    차수(degree) : 다항식의 항에서 특정 변수를 거듭제곱한 지수를 그 항의 그 변수에 대한 차수라고 한다.

- 예시 

    $x^2 -2x +3$ 에서 항 $x^2$ 의 차수는 $2$ 이다.

!!! tldr ""

    최고차항 : 가장 높은 차수의 항이다.

- 예시 

    $5x^2 +1x +7$ 에서 최고차항은 $5x^2$ 이다.

!!! tldr ""

    인수 : 하나의 다항식이 두 개 이상의 단항식이나 다항식의 곱으로 표현될 때, 곱해진 식을 인수라고 한다.

- 예시 

    $x^2+(a+b)x+ab = (x+a)(x+b)$ 에서 인수란 $(x+a)$ 와 $(x+b)$ 이다.

!!! tldr ""

    다항식의 연산에 대한 성질 : $A, B, C$ 를 다항식이라 할 때 다음 법칙이 성립한다.

- 교환법칙 

    $A + B = B + A, AB = BA$

- 결합법칙 

    $(A + B) + C = A + (B + C)$, $(AB)C = A(BC)$

- 분배법칙 

    $A(B + C) = AB + AC$, $(A+B)C = AC+BC$

- 예시 

    $A = (x + 4 - 2y)(x-2y), B=(x+4)x$ 일 때, $A + X = B$ 를 만족시키는 다항식 $X$ 를 구하라.

    $A = \{(x + 4) - 2y\}(x-2y)$

    $= (x + 4)x - (x + 4)2y - 2yx + 4y^2$

    $= B - (x + 4)2y - 2yx + 4y^2$

    $= B - 4xy + 4y^2 -8y$

    $\therefore X = B - A = 4xy - 4y^2 +8y$$

- 그런데 위 예시의 수식을 단지 수식으로만 바라보는 관점은 잘못되었다. 왜냐하면 수학은 자연 대상을 추상화시킨 순수 추상물이기 때문이다. 이 수식은 세상 모든 수로 격하될 수 있는 대상들의 특정한 관계의 추상물이다. 그러므로 수로 변환되어 표현할 수 있는 세상 모든 대상의 특정한 관계가 수식으로 표현될 수 있다고 할 수 있다.

    - **한편 그러한 순수한 추상물을 구성하는 더 작은 기본요소인 더하기($+$) 는 세상에 수로 변환되어 표현할 수 있는 모든 대상들을 합하는 것을 표현할 수 있는 것이다.**

    - **컴퓨터의 기계어를 살펴보면 기본적인 연산인 더하기($+$), 빼기($-$), 곱하기($\times$), 나누기($\div$) 와 저장과 할당이라는 매우 근본적이면서 추상적인 기능들만 제공하는 것을 알 수 있다. 실제로 프로그래밍 언어란 단지 $4$가지 기능(연산, 할당, 종료, ?)의 조합이라고 배웠다. 그러나 실제로 컴퓨터로 얼마나 많은 일을 할 수 있는지 생각해보자. 물론 컴퓨터의 한계도 있다. 컴퓨터로 할 수 있는 일인지 검증하기 위하여 튜링테스트를 하는 걸까? 어쨌든 그러한 기본연산이 추상적으로 어떤 의미를 갖는지 밝혀서 이해할 수 있다면 좋을 것 같다.**

    - **기본연산과 저장과 할당은 매우 추상적이라서 어떤 것으로든 쉽게 구체화될 수 있다는 장점이 있는 것 같다. 가령 로봇의 팔을 드는 것을 어떤 장소에 신호를 주는 것으로 변환한다면 컴퓨터의 "저장" 이라는 추상적 개념을 사용하여 특정 장소에 특정 값을 저장하는 것으로 구현할 수 있는 것이다.**

!!! tldr ""

    일차방정식(선형방정식, linear equation) : 최고차항의 차수가 $1$ 을 넘지 않는 다항 방정식이다.



!!! tldr ""

    이차방정식 : 최고차항의 차수가 $2$ 인 다항 방정식이다.

- 일반적인 모양은 $ax^2 + bx + c = 0 (단, a \ne 0)$ 이다. 

- 위와 같은 일반적 형태의 이차방정식의 일반해는 다음과 같다.

    $$ x = \frac{-b \pm \sqrt[]{b^2-4ac}}{2a} (단, b^2-4ac \ge 0)$$

!!! tldr ""

    다항방정식 : 미지수에 대한 다항식으로만 이루어진 방정식이다.

- 다항방정식은 다음과 같은 꼴로 나타낼 수 있다. 

    $$ \sum_{i=0}^na_ix^i = 0 $$

!!! tldr ""

    곱셈공식

- $m(a+b) = ma + mb$

- $m(a-b)=ma-mb$

- $(a+b)^2 = a^2 + 2ab+b^2$

- $(a-b)^2=a^2-2ab+b^2$

- $(a+b)(a-b) = a^2-b^2$

- $(x+a)(x+b)(x+c) = x^3 + (a+b+c)x^2 + (ab+bc+ca)x+ abc$

- $(a+b)^3 = a^3 +3a^2b+3ab^2+b^3$

- $(a-b)^3 = a^3 -3a^2b+3ab^2 -b^3$

- $(a+b)(a^2-ab+b^2) = a^3+b^3$

- $(a-b)(a^2+ab+b^2) = a^3-b^3$

- $(a+b+c)^2 = a^2+b^2+c^2 + 2(ab+bc+ca)$

- $(a+b+c)(a^2+b^2+c^2 - ab-bc-ca)=a^3+b^3+c^3-3abc$

- $(a^2+ab+b^2)(a^2-ab+b^2) = a^4+a^2b^2+b^4$

!!! tldr ""

    다항식의 나눗셈
    
    **구체화 필요**



!!! tldr ""

    조립제법
    
    **구체화 필요**



!!! tldr ""

    다항식의 여러가지 성질

- 다항식의 나머지 정리

    - 다항식 $f(x)$ 를 일차식 $x-\alpha$ 로 나눌 때 나머지를 $R_1$ 이라 하면 $R_1 = f(\alpha)$ 이다.

    - 다항식 $f(x)$ 를 일차식 $ax-b$ 로 나눌 때 나머지를 $R_2$ 이라 하면 $R_2 = f(\frac{b}{a})$ 이다.

- 다항식의 인수정리

    - 다항식 $f(x)$ 가 일차식 $x-\alpha$ 로 나누어떨어지면 $f(\alpha)=0$ 이다.

    - $f(\alpha)=0$ 이면 $f(x)$ 는 $x-\alpha$ 로 나누어 떨어진다. 즉 $f(x) = (x-\alpha)Q(x)$

!!! tldr ""

    인수분해 : 하나의 다항식을 두 개 이상의 인수들의 곱으로 나타내는 것이다.

- $a^2+2ab+b^2=(a+b)^2$

- $a^2-b^2 = (a+b)(a-b)$

- *더 많은 예시는 단지 곱셈공식의 수식을 역방향으로 살펴보면 결국 그것이 인수분해이다.*

## 부등식

!!! tldr ""

    부등식(inequality) : 두 수 및 두 식에 대한 크기 비교를 나타내는 식이다.

- $a \ne b$ : 두 수가 같지 않다. 

- $a > b$ : $a$ 가 $b$ 보다 크다. 

- $a < b$ : $a$ 가 $b$ 보다 작다.

- $a \ge b$ : $a$ 가 $b$ 보다 크거나 같다.

- $a \le b$ : $a$ 가 $b$ 보다 작거나 같다.

!!! tldr ""

    절대부등식 : 모든 변수의 값에 대하여 성립하는 변수 있는 부등식이다.

- 예시 

    - $x^2 \ne -1 (x \in \mathbb{R})$

    - $x^2 \ge -1 (x \in \mathbb{R})$

    - $x^2 + y^2 \ge 2xy (x, y \in \mathbb{R})$

!!! tldr ""

    산술기하 평균 부등식(arithmetic mean-geometric mean inequality, AM-GM inequality) : $n$개의 양수 $a_1, a_2, \dots, a_n$ 에 대하여 절대부등식
    
    $$ \dfrac{a_1+a_2+\dots+a_n}{n} \geq (a_1a_2 \dots a_n)^{\frac{1}{n}} $$
    
    즉, $\displaystyle \dfrac{1}{n}\bigg (\sum_{k=1}^{n}a_k\bigg ) \geq \bigg (\prod_{k=1}^{n}a_k \bigg )^{1/n}$ 이 성립한다.

- 단 등호는 $a_1 = a_2 = \dots = a_n$ 일때만 성립한다.

- 증명

    $x_1, x_2, \dots, x_n \in \mathbb{R} _{>0}$ 에 대하여 산술평균을 $A_n = \displaystyle \dfrac{1}{n}\bigg (\sum_{k=1}^{n}a_k\bigg )$ 이라고 하고 기하평균을 $\displaystyle  G_n = \bigg (\prod_{k=1}^{n}a_k \bigg )^{1/n}$ 이라고 하자.

    모든 $n \in \Z _{>0}$ 에 대하여 명제 $P(n)$ 을 

    $$ \forall x_1, x_2, \dots, x_n \in \mathbb{R} _{>0} : A_n \geq G_n $$

    이라고 하자.

    $P(1)$ 은 $\dfrac{x_1}{1} \geq x_1 ^{1/1}$ 이므로 성립한다. ▲ 

    $P(2)$ 은 $\dfrac{x_1+x_2}{2} \geq \sqrt[]{x_1x_2}$ 인데, $x_1, x_2 >0$ 이므로

    $$ 0 \leq (\sqrt[]{x_1}-\sqrt[]{x_2}) ^{2} = x_1 -2 \sqrt[]{x_1x_2}+x_2 $$

    에서 

    $$ \sqrt[]{x_1x_2} \leq \dfrac{x_1+x_2}{2} $$

    를 얻는다. 그러므로 $P(2)$ 도 성립한다. ▲ 

    이제 우리는 역진귀납법을 통하여

    1. $k \geq 1$ 에 대하여 $P(2 ^{k})$ 이면 $P(2 ^{k+1})$ 이다.

    2. $k \geq 2$ 에 대하여 $P(k)$ 이면 $P(k-1)$ 이다.

    를 보일 것이다.

    그러면 이제 $A _{2 ^{k}} \geq G _{2 ^{k}}$ 라고 가정하고 $A _{2 ^{k+1}} \geq G _{2 ^{k+1}}$ 임을 보이자.
    
    $m = 2 ^{k}$ 라고 하고 $2 ^{k+1} = 2m$ 라고 하자. $P(m)$ 이 참이라고 가정했으므로 $m$ 개의 양수 $x_1, x_2, \dots, x_m$ 에 대하여

    $$ (x_1x_2 \dots x_m)^{1/m} \leq \dfrac{1}{m}(x_1 + x_2 + \dots+x_m) $$ 

    이고 $m$ 개의 양수 $x _{m+1}, x _{m+2}, \dots, x _{2m}$ 에 대하여

    $$ (x _{m+1}x _{m+2} \dotsx _{2m}) ^{1/m} \leq \dfrac{1}{m} (x _{m+1}+x _{m+2}+\dots+x _{2m}) $$

    이다. 그런데 우리는 $P(2)$ 즉, $\dfrac{x_1+x_2}{2} \geq \sqrt[]{x_1x_2}$ 가 참임을 알고 있다. 그러므로 

    $$ \bigg ( (x_1x_2 \dots x_m)^{1/m}(x _{m+1}x _{m+2} \dotsx _{2m}) ^{1/m} \bigg ) ^{1/2}  \leq \dfrac{1}{2}\bigg ( \dfrac{1}{m}(x_1 + x_2 + \dots+x_m) + \dfrac{1}{m} (x _{m+1}+x _{m+2}+\dots+x _{2m}) \bigg ) $$

    $$ \iff (x_1x_2 \dots x _{2m}) ^{1/2m} \leq \dfrac{x_1 + x_2 + \dots + x _{2m}}{2m} $$

    이다. 그러므로 $P(m) \implies P(2m)$ 즉, $\forall n \in \mathbb{N}$ 에 대하여 $P(2 ^{n})$ 이 성립한다. ▲ 

    이제 $P(k)$ 가 성립한다고 하자. 그러면 

    $$ (x_1x_2 \dots x _{k-1}x _{k})^{1/k} \leq \dfrac{x_1 + x_2 + \dots + x _{k-1} + x _{k}}{k} $$

    인데 이때 $G_{k-1} = x_k$ 로 두면

    $$ (x_1x_2 \dots x _{k-1}G _{k-1})^{1/k} \leq \dfrac{x_1 + x_2 + \dots + x _{k-1} + G _{k-1}}{k} $$

    $$ \iff (G ^{k-1}_{k-1}G _{k-1})^{1/k} \leq \dfrac{(k-1)A _{k-1}+G _{k-1}}{k} $$

    $$ \iff G _{k-1} \leq \dfrac{(k-1)A _{k-1}+G _{k-1}}{k} $$

    $$ \iff kG _{k-1} \leq (k-1)A _{k-1}+G _{k-1} $$

    $$ \iff (k-1) G _{k-1} \leq (k-1)A _{k-1}$$

    $$ \iff  G _{k-1} \leq A _{k-1}$$

    이다. 그러므로 $P(k) \imath P(k-1)$ 이다. ▲ 

    그렇다면 $P(n)$ 은 $\forall n \in \mathbb{N}$ 에 대하여 $P(2 ^{n})$ 이 성립하고, $P(n) \implies P(n-1)$ 이므로 역진귀납법에 의하여 $\forall n \in \mathbb{N}$ 에 대하여 $P(n)$ 즉, $A_n \geq G_n$ 이 성립한다. ■

!!! tldr ""

    산술평균, 기하평균, 조화평균의 관계 : 다음 절대부등식은 두 양수의 특정한 연산 결과의 관계를 나타낸다. 
    
    $$ a>0, b>0 일때, \frac{a+b}{2} \geq \sqrt[]{ab} \geq \frac{2ab}{a+b} $$

- 위 절대부등식의 $3$ 가지 식은 처음부터 각각 산술평균(arithmetic mean), 기하평균(geometric mean), 조화평균(harmonic mean) 이라 한다.

!!! tldr ""

    산술평균, 기하평균, 조화평균의 일반적 관계 : 양수 $a_1, a_2, \dots, a_n$ 에 대하여 다음 절대부등식이 항상 성립한다.
    
    $$ \frac{\sum_{k=1}^{n}a_1}{n} \geq \sqrt[n]{\prod_{k=1}^{n}a_k} \geq \frac{n}{\sum_{k=1}^{n}\frac{1}{a_k}} $$



!!! tldr ""

    코시-슈바르츠(Cauchy-Schwartz) 의 부등식 : $r_i,s_i \in \mathbb{R}$ 에 대하여 절대부등식이 항상 성립한다.
    
    $$ \sum_{i=1}^{n}r_i^2\sum_{i=1}^{n}s_i^2 \geq \bigg (\sum_{i=1}^{n}r_is_i \bigg )^2 $$

- 벡터 $v, w$ 에 대하여 

    $$ \|v\|^{2} \|w\|^{2} \geq \|v \cdot w\|^{2} $$

    이 가장 일반적인 형태이다.

- 등호는 $\displaystyle \frac{s_1}{r_1}=\frac{s_2}{r_2}=\dots=\frac{s_n}{r_n}$ 일 때 성립한다.

- 증명 

    임의의 $\lambda \in \mathbb{R}$ 에 대하여 함수 $f: \mathbb{R} \to \mathbb{R}$ 를 이렇게 정의해보자. 

    $$ f(\lambda ) = \sum_{i=1}^{n}(r_i + \lambda s_i) ^{2} $$

    그러면 이는 실수의 제곱이므로 $f(\lambda ) \geq 0$ 이다. 따라서 
    
    $$ \forall \lambda \in \mathbb{R} : f(\lambda ) \equiv \sum_{i=1}^{n}(r_i ^{2}+2 \lambda r_is_i+\lambda ^{2}s_i ^{2}) \geq 0 $$

    $$ \equiv \sum_{i=1}^{n}r_i ^{2}+2 \lambda \sum_{i=1}^{n}r_is_i+\lambda ^{2}\sum_{i=1}^{n}s_i ^{2} \geq 0 $$

    이다. 이때 $\displaystyle  a = \sum_{i=1}^{n}s_i ^{2}, b =2 \sum_{i=1}^{n}r_is_i, c = \sum_{i=1}^{n}r_i ^{2}$ 로 두면

    $$ \equiv a \lambda ^{2} + b \lambda + c \geq   0$$

    가 되므로 이것이 $\lambda \in \mathbb{R}$ 에 대한 이차방정식이라는 것이 보인다.

    그렇다면 이차방정식 $a \lambda ^{2} + b \lambda + c = 0$ 의 판별식 $b ^{2} - 4ac$ 은

    $$ D := \bigg (2 \sum_{i=1}^{n}r_is_i\bigg ) ^{2} -4 \bigg (\sum_{i=1}^{n} r_i ^{2}\sum_{i=1}^{n}s_i ^{2}\bigg ) $$

    인데, 이 판별식이 양수라고 해보자. 즉, 

    $$ b ^{2} - 4ac = \bigg (2 \sum_{i=1}^{n}r_is_i\bigg ) ^{2} -4 \bigg (\sum_{i=1}^{n} r_i ^{2}\sum_{i=1}^{n}s_i ^{2}\bigg ) > 0 $$

    이라고 해보자. 이차방정식의 판별식이 양수라는 것은 이차방정식이 두 실근 $\lambda _1, \lambda _2$ 를 갖는다는 것이다. 이때 $\lambda _1 \leq \lambda _2$ 라고 하자.

    그렇다면 함수 $f(\lambda ) = a \lambda ^{2}+b \lambda +c$ 는 개구간 $(\lambda _1, \lambda _2)$ 에서 $f(\lambda ) < 0$ 이다.

    그런데 $\forall \lambda \in \mathbb{R} : f(\lambda ) \geq 0$ 이므로 이는 모순이다. 그러므로 판별식은 양수가 아니다. 즉, 

    $$ D = b ^{2} - 4ac \leq 0 $$

    이다. 이는 곧 

    $$ \bigg (2 \sum_{i=1}^{n}r_is_i\bigg ) ^{2} -4 \bigg (\sum_{i=1}^{n} r_i ^{2}\sum_{i=1}^{n}s_i ^{2}\bigg ) \leq  0 $$

    $$ \iff  \sum_{i=1}^{n} r_i ^{2}\sum_{i=1}^{n}s_i ^{2} \geq  \bigg (\sum_{i=1}^{n}r_is_i\bigg ) ^{2} $$

    임을 뜻하며 이로써 증명이 끝났다. ■ 

- 예시 

    코시-슈바르츠(Cauchy-Schwartz) 의 부등식 : $a,b,c,d$ 가 실수일 때 다음 절대부등식이 항상 성립한다.

    $$ (a^2+b^2)(c^2+d^2) \geq (ac+bd)^2 (단, 등호는 \frac{c}{a}=\frac{d}{b} 일 때 성립) $$

!!! tldr ""

    조건부등식 : 특정한 범위의 변수의 값아래에서만 성립하는 변수 있는 부등식이다.

- 예시 

    - $3x + 3 > 0 (x > -1)$

## 유리식

!!! tldr ""

    유리식 : 두 다항식 $A, B$ 의 비이다.

- 유리식은 분수 $\frac{A}{B}(B \neq 0)$ 으로 표현한다. 

- 유리식 집합에는 다항식과 분수식이 포함된다. 

    - 다항식 $A$ 는 $\frac{A}{1}$ 로 나타낼 수 있으므로 모든 정수가 유리수인 것처럼 모든 다항식은 유리식이다. 

- 예시 

    다음은 모두 유리식이다. 

    - $\frac{x-1}{2}$ (다항식)

    - $3x^2 -1$ (다항식)

    - $\frac{1}{x ^{2}-1}$ (분수식)

    - $\frac{x+1}{x ^{2}+x+1}$ (분수식)

!!! tldr ""

    분수식 : 다항식이 아닌 유리식이다.

- 예시 

    - $\frac{1}{x ^{2}-1}$ 

    - $\frac{x+1}{x ^{2}+x+1}$

!!! tldr ""

    가분수식 : 분자의 차수가 분모의 차수보다 큰 분수식이다.



!!! tldr ""

    진분수식 : 분자의 차수가 분모의 차수보다 작거나 같은 분수식이다.



!!! tldr ""

    다항식의 연산 : (너무 직관적이라 일단은 나눗셈에 대하여서만 메모해둠)

- 나눗셈 : 두 다항식 $A, B(B \neg 0)$ 에 대하여 $A$ 를 $B$ 로 나누었을 때의 몫을 $Q$, 나머지를 $R$ 이라 하면 가분수식 $\frac{A}{B}$ 를 다음과 같이 계산할 수 있다. 

    $$ \frac{A}{B} = \frac{BQ+R}{B} = Q + \frac{R}{B} = (다항식) + (진분수식) $$

- 부분분수로의 분해 

  **구체화 필요**

- 번분수식의 계산 

  **구체화 필요**

## 무리식

!!! tldr ""

    무리식 : 근호 안에 문자를 포함하는 식 중에서 유리식으로 나타낼 수 없는 식이다.

- 예시 

    $\sqrt[]{(3-\sqrt[]{10})^2}$ 

## 연립방정식

!!! tldr ""

    연립방정식(simultaneous equation) 또는 방정식계(system of equations) : 2개 이상의 미지수를 포함하는 방정식의 유한 집합이다.

- 미지수의 개수가 $n$ 개이고 최고 차수가 $m$ 일 때 연립 $n$원 $m$차 방정식이라 한다. 

- 이원 연립일차방정식(선형 연립방정식) 예시 

    $\begin{cases} ax+by=p &\text{}\\ cx + dy = q &\text{}\\ \end{cases}$

## 대수학의 기본 정리

!!! tldr ""

    대수학의 기본 정리 : 복소수 계수의 $n$ 차 방정식은 적어도 하나의 복소수 근을 갖는다. (단, $n$ 은 자연수)

- 가우스가 처음으로 증명하였다.

!!! tldr ""

    $k$중근 : $n$차방정식 $f(x)=0$ 의 좌변을 인수분해했을 때 정확히 $k$개의 $(x-\alpha)$ 라는 인수가 있으면, $\alpha$ 를 $f(x)=0$ 의 $k$ 중근이라 한다.



!!! tldr ""

    대수학의 기본 정리의 따름 정리 : 복소수 계수의 $n$ 차방정식에서 $k$중근을 $k$ 개의 근으로 셀 때, 정확히 $n$ 개의 복소수 근을 갖는다. (단, $k, n$은 자연수이고 $n \geq k$)



!!! tldr ""

    가우스 기호

- $x$ 의 정수부 $[x]$ : $x$ 보다 크지 않은 최대의 정수

- $x$ 의 소수부 $frac(x)$ : $x$ 에서 $[x]$ 를 뺀 값으로 $0 \leq frac(x) \leq 1$ 인 수이다.

## 수학적 모델링

!!! tldr ""

    모델(model ; 모형) : 어떤 대상들의 대표성을 가진 것이다.

- 예시 

    네트워크 모델(OSI 7 Layer), 패션 모델, 분자모델, 경제적 합리적 모델, 비즈니스 모델, 치아 모형

!!! tldr ""

    수학적 모델링 : 수학을 기반으로 연구 대상의 중요한 특성을 나타낼 모델을 만드는 것이다.

- 수학을 배우는 이유 중 하나는 세상을 수학으로 표현할 수 있는 능력을 기르기 위함이다.

- 대상을 수학으로 변환시켜 격하하면 수학적 연산을 사용할 수 있게 되기에 대상을 다루기 쉬워지기 때문이다. 

- 예시

    - 가속도가 불변인 중력 모델 : 질량이 $m$ 인 물체와 지구 사이에 작용하는 힘 $F$ 는 $F = mg(g = 9.8m/s^2)$ 이다.

- 수학적 모델링은 대상을 완전하게 대체할 수는 없다. 가령 중력 모델만으로 실제 물체가 떨어지는 것을 완전히 표현할 수 없는데 그 이유 중 하나는 수식에 공기 저항력이 배제되어 있기 때문이다. 그러나 대상의 불변요소를 고정시키고 최대한 단순화 시켜서 대상을 이해하는데에 많은 도움을 준다.



수학적 모델링의 과정 

1. 관찰 : 실제 세상의 대상 및 현상을 관찰, 해석하여 수학적 모델로 격하한다.

2. 분석 : 수학적 모델을 분석하여 수학적인 결론을 내린다.

3. 적용 : 그 결론을 통해 실제 세상의 현상을 예측하는 등 적용한다.

4. 피드백 : 실제 세상의 대상으로부터 오류를 계산하여 수학적 모델에 반영한다.
