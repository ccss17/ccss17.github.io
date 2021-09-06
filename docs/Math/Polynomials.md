# Polynomial

!!! def "다항식(polynomial)"

    계수가 체 $\mathbf{F}$ 의 원소인 다항식은 다음과 같다. 

    $$ f(x) = a_nx ^{n} + a _{n-1} x ^{n-1} + \dots + a_1x + a_0 $$

- $n$ 을 차수(degree)라 한다. 차수는 음이 아닌 정수이다. 차수는 계수가 $0$ 이 아닌 항의 $x$ 의 지수 중 가장 큰 값으로 정의된다.

- $a_k$ 를 $x ^{k}$ 의 계수(coefficient)라 한다. 계수는 $\mathbf{F}$ 의 원소이다.

- $f(x) = 0$, 즉 $a_n = a _{n-1} = \dots = a_0 = 0$ 이면 $f(x)$ 를 영 다항식(zero polynomial)이라 한다. 영 다항식의 차수는 $-1$ 로 정의한다.

!!! def "다항식의 상등(equality of polynomial)"

    다음 두 다항식 $f, g$ 에 대하여 $m = n \land \forall i \in \{0, \dots, n\} : a_i = b_i$ 이면 $f, g$ 를 같다고 한다.

    $$ f(x) = a_nx ^{n} + a _{n-1} x ^{n-1} + \dots + a_1x + a_0 $$

    $$ f(x) = b_mx ^{m} + b _{m-1} x ^{m-1} + \dots + b_1x + b_0 $$

!!! def ""

    체 $\mathbf{F}$ 가 무한집합이면 $\mathbf{F}$ 에서 계수를 가져온 다항식은 $\mathbf{F}\to \mathbf{F}$ 위에서 정의된 함수이다.

- 함수 $f(x) = a_nx ^{n} + a _{n-1} x ^{n-1} + \dots + a_1x + a_0$ 의 $c \in \mathbf{F}$ 에서의 함숫값은 다음 스칼라이다.

    $$ f(c) = a_nc ^{n} + a _{n-1} c ^{n-1} + \dots + a_1c + a_0 $$

- 599쪽

## Vector Space $\mathbf{P}_{}(\mathbf{F})$

!!! def "벡터공간 $\mathbf{P}_{}(\mathbf{F})$"

    다음과 같은 체 $\mathbf{F}$ 에서 계수를 가져온 두 다항식 $f, g$ 에 대하여 $m \leq n$ 일 때 $b _{m+1} = b _{m+2} = \dots = b_n= 0$ 으로 정의하자.

    $$ f(x) = a_n x ^{n} + a _{n-1}x ^{n-1} + \dots + a_1x + a_0 $$

    $$ g(x) = b_m x ^{m} + a _{m-1}x ^{m-1} + \dots + b_1x + b_0 $$

    두 다항식의 합과 스칼라곱을 다음과 같이 정의한 $\mathbf{F}$ 에서 계수를 가져온 모든 다항식 집합을 벡터공간 $\mathbf{P}(\mathbf{F})$ 이라 정의한다.

    $$ f(x) + g(x) = (a_n+b_n) x ^{n} + (a _{n-1}+b _{n-1})x ^{n-1} + \dots+(a_1+b_1)x+(a_0+b_0) $$

    $$ cf(x) = ca_n x ^{n} + ca _{n-1}x ^{n-1} + \dots + ca_1x + ca_0 $$

- $\mathbf{P}_{}(\mathbf{F})$ 에서 [벡터공간](LinearAlgebra/VectorSpace/#115df4450)의 공리가 모두 성립한다.

- 차수가 $n$ 인 다항식 집합을 $\mathbf{P}_{n}(\mathbf{F}) (\subset \mathbf{P}_{}(\mathbf{F}))$ 라 한다.

- 벡터공간 $\mathbf{P}(\mathbf{F})$ 와 다음 예제에서 보이는 벡터공간은 [본질적으로 같다.](LinearAlgebra/LinearTransformation/#28bdb2c98) 

- 예시 

    임의의 체 $\mathbf{F}$ 위에서 정의된 수열(sequence)은 $\N \to \mathbf{F}$ 인 함수이다. 보통 수열 $\sigma (n) = a_n$ 을 $(a_n)$ 으로 표기한다. 체 $\mathbf{F}$ 에서 정의된 모든 수열의 집합을 $\mathbf{V}$ 라고 하자. 두 수열 $(a_n),(b_n)$ 을 다음과 같이 합과 스칼라곱으로 정의하면 $\mathbf{V}$ 는 벡터공간이다.

    $$ (a_n)+(b_n)=(a_n+b_n) \qquad t(a_n) = (ta_n) $$

# Division of Polynomial

!!! def "다항식의 나눗셈(division of polynomial)"

    두 다항식 $f, g$ 에 대하여 $g(x) = f(x)q(x)$ 인 다항식 $q$ 가 존재하면 다항식 $f$ 가 다항식 $g$ 를 나눈다고 정의한다.

!!! def "정리 1 다항식의 나눗셈 정리(division algorithm for polynomials)"

    $n$차 다항식 $f(x)$ 와 $m(\geq 0)$차 다항식 $g(x)$ 에 대하여 다음을 만족하는 다항식 $q(x), r(x)$ 가 유일하게 존재한다. 

    $$ f(x) = q(x)g(x) + r(x) $$

    $r(x)$ 의 차수는 $m$ 보다 작다.

- **$q(x), r(x)$ 를 각각 $f(x)$ 를 $g(x)$ 로 나누었을 때의 몫(quotient) 과 나머지(remainder) 라 한다.**

- 증명

    $n < m$ 일 때 $q(x) = 0, r(x) = f(x)$ 로 두면 정리가 성립한다. ▲ 

    $0 \leq m < n$ 일 때 $n = 0$ 이면 $f, g$ 는 상수 다항식이므로 $q(x) = \dfrac{f(x)}{g(x)}, r(x) = 0$ 으로 두면 정리가 성립한다. ▲ 

    $0 \leq m < n \land n > 0$ 일 때 $n$ 미만의 차수를 갖는 다항식에서 정리가 성립함을 가정하자. $n$차 다항식 $f$ 와 $m$차 다항식 $g$ 와 또 다른 다항식 $h$ 를 다음과 같이 정의하자.

    $$ f(x) = a_n x ^{n} + a _{n-1}x ^{n-1} + \dots + a_1x + a_0 $$

    $$ g(x) = b_m x ^{m} + a _{m-1}x ^{m-1} + \dots + b_1x + b_0 $$

    $$ h(x) = f(x) - \frac{a_n}{b_m}x ^{n-m}g(x) \tag{1} $$

    $h$ 는 차수가 $k (< n)$ 인 다항식이다. 귀납법의 가정에 의하여 $g, h$ 에 대하여 정리가 성립하므로 다음을 만족하는 다항식 $q_1$ 과 차수가 $m$ 미만인 다항식 $r$ 이 유일하게 존재한다. 

    $$ h(x) = q_1(x)g(x) + r(x) \tag{2} $$

    $(1), (2)$ 를 $f(x)$ 에 대하여 풀면 $q(x) = a_nb_m ^{-1}x ^{n-m} + q_1(x)$ 에 대하여 $f(x) = q(x)g(x) + r(x)$ 이다. 존재성 증명이 끝났으므로 유일성 증명만 하면 모든 증명이 끝난다. ▲ 

    이제 본 정리의 존재성을 가정할 수 있으므로 다음을 만족하는 다항식 $q_1,q_2,r_1,r_2$ 가 존재한다.

    $$ f(x) = q_1(x)g(x) + r_1(x) = q_2(x)g(x) + r_2(x) $$

    $r_1, r_2$ 의 차수는 $m$ 미만이다. 다음이 성립한다.

    $$ \{q_1(x) - q_2(x)\}g(x) = r_2(x) - r_1(x) $$

    $r_2(x) - r_1(x)$ 의 차수가 $m$ 미만이고 $g(x)$ 의 차수가 $m$ 이므로 만약 $q_1(x) - q_2(x)$ 의 차수가 $0$ 이상이면 모순이다. 따라서 $-1$ 의 차수를 갖는다. 즉, 영 다항식이다. 따라서 $q_1(x) - q_2(x) = 0 \implies q_1 = q_2$ 이다. 그러면 $0 = r_2(x) - r_1(x) \implies r_1 = r_2$ 도 성립한다. ■ 

!!! def "정리 1 다항식의 나눗셈 정리(division algorithm for polynomials) 따름정리 1"

    차수가 $1$ 이상인 다항식 $f(x)$ 와 $a \in \mathbf{F}$ 에 대하여 다음은 동치이다. 

    - $f(a) = 0$

    - $x-a$ 가 $f(x)$ 를 나눈다.

- 이 정리는 다항식이 해를 가지면 [완전히 인수분해](LinearAlgebra/Diagonalization/#12bf9c352)됨을 말해준다.

- 증명

    $x-a$ 가 $f(x)$ 를 나눈다고 하면 $f(x) = (x-a)q(x)$ 인 다항식 $q(x)$ 가 존재하므로 $f(a) = 0$ 이다. ▲ 

    $f(a) = 0$ 을 가정하자. 다항식의 나눗셈 정리에 의하여 $f(x) = q(x)(x-a) + r(x)$ 를 만족하는 다항식 $q,r$ 이 존재한다. $r$ 의 차수는 $1$ 미만이다. 즉, $c \in \mathbf{F} : r(x) = c$ 이다. 그러면 $f(a) = 0 + r(a) = 0$ 이 성립하므로 $c = 0$ 을 얻는다. ■ 

!!! def "정리 1 다항식의 나눗셈 정리(division algorithm for polynomials) 따름정리 2"

    $n (\geq 1)$차 다항식은 최대 $n$ 개의 서로 다른 근이 있다.

- 증명

    ㅇ

# Fundamental Theorem of Algebra

!!! def "대수학의 기본 정리(fundamental theorem of algebra)"

    $\mathbf{P}(\mathbb{C})$ 의 다항식 $p(z) = a_nz ^{n} + \dots + a_1z + a_0$ 의 차수가 $n \geq 1$ 이면 $p(z)$ 는 해가 있다.

- 17세기부터 수학자들이 옳으리라고 추측했던 유명한 정리이다. 대수학의 기본 정리이지만 순수하게 대수적인 증명은 누구도 해내지 못했고, 훗날 위상수학과 해석학을 도입하여 증명을 할 수 있었다. 그래서 복소해석학에 의한 증명과 위상수학에 의한 증명이 존재한다.

- 증명

!!! def "대수학의 기본 정리(fundamental theorem of algebra) 따름정리"

    차수가 $n \geq 1$ 이고 복소계수를 포함한 다항식 $p(z) = a_nz ^{n} + \dots + a_1z + a_0$ 에 대하여 다음을 만족하는 복소수 $c_1, c_2, \dots, c_n$ 이 존재한다. 

    $$ p(z) = a_n(z-c_1)(z-c_2)\dots(z-c_n) $$

- 이 정리는 **[복소내적공간](LinearAlgebra/InnerProductSpaces/#653ace4b3)의 선형연산자의 [특성다항식](LinearAlgebra/Diagonalization/#2f3482489)이 반드시 [완전히 인수분해](LinearAlgebra/Diagonalization/#12bf9c352)됨을 말해준다.** 

- 체의 원소를 계수로 가지고 차수가 자연수인 다항식이 일차식의 곱으로 표현되는 체를 대수적으로 닫힌(algebraically closed) 체라 한다. 이 정리는 복소수체가 대수적으로 닫혀있음을 말해준다. 

- 증명

    대수학의 기본정리에 의하여 $p(z) \in \mathbf{P}_{}(\mathbb{C})$ 는 해 $c_1 \in \mathbb{C}$ 를 가진다. 정리 1 따름정리 1 에 의하여 $z - c_1$ 가 $p(z)$ 를 나누므로 차수가 $n-1$ 이고 최고차항의 계수가 $1$ 인 다항식 $f(z)$ 에 대하여 다음이 성립한다. 

    $$ p(z) = a_n(z - c_1)f(z) $$

    $f(z)$ 처럼 $p(z)$ 를 나누는 다항식의 차수가 $1$ 이상인 한 대수학의 기본정리에 의하여 항상 해가 존재하여 위와 같은 일차식 $z - c_1$ 으로 $p(z)$ 를 나눌 수 있다. 따라서 다음이 성립한다.

    $$ p(z) = a_n(z - c_1)\dots(z-c_n) \tag*{■} $$


---

ref:

:   Stephen H. Friedberg, Linear Algebra, 5th Edition
