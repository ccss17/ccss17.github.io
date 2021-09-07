# Polynomial

!!! def "다항식(polynomial)"

    계수가 체 $\mathbf{F}$ 의 원소인 다항식은 다음과 같다. 

    $$ f(x) = a_nx ^{n} + a _{n-1} x ^{n-1} + \dots + a_1x + a_0 $$

- $n$ 을 차수(degree)라 하고 $\deg (f) = n$ 이라 표기한다. 차수는 음이 아닌 정수이다. 차수는 계수가 $0$ 이 아닌 항의 $x$ 의 지수 중 가장 큰 값으로 정의된다.

- $a_k$ 를 $x ^{k}$ 의 계수(coefficient)라 한다. 계수는 $\mathbf{F}$ 의 원소이다.

- $f(x) = 0$, 즉 $a_n = a _{n-1} = \dots = a_0 = 0$ 이면 $f(x)$ 를 영 다항식(zero polynomial)이라 한다. 영 다항식의 차수는 $-1$ 로 정의한다.

!!! def "다항식의 상등(equality of polynomial)"

    다음 두 다항식 $f, g$ 에 대하여 $m = n \land \forall i \in \{0, \dots, n\} : a_i = b_i$ 이면 $f, g$ 를 같다고 한다.

    $$ f(x) = a_nx ^{n} + a _{n-1} x ^{n-1} + \dots + a_1x + a_0 $$

    $$ g(x) = b_mx ^{m} + b _{m-1} x ^{m-1} + \dots + b_1x + b_0 $$

!!! def ""

    체 $\mathbf{F}$ 가 무한집합이면 $\mathbf{F}$ 에서 계수를 가져온 다항식은 $\mathbf{F}\to \mathbf{F}$ 위에서 정의된 함수이다.

- 함수 $f(x) = a_nx ^{n} + a _{n-1} x ^{n-1} + \dots + a_1x + a_0$ 의 $c \in \mathbf{F}$ 에서의 함숫값은 다음 스칼라이다.

    $$ f(c) = a_nc ^{n} + a _{n-1} c ^{n-1} + \dots + a_1c + a_0 $$

- $\mathbf{F}$ 가 무한집합일 때 $\mathbf{F}$ 에서 계수를 가져온 다항식을 $\mathbf{F}$ 에서 $\mathbf{F}$ 로 가는 함수로 볼 수 있다. 아래에서 정리 10 을 보자.

## Vector Space $\mathbf{P}_{}(\mathbf{F})$

!!! def "벡터공간 $\mathbf{P}_{}(\mathbf{F})$"

    다음과 같은 체 $\mathbf{F}$ 에서 계수를 가져온 두 다항식 $f, g$ 에 대하여 $m \leq n$ 일 때 $b _{m+1} = b _{m+2} = \dots = b_n= 0$ 으로 정의하자.

    $$ f(x) = a_n x ^{n} + a _{n-1}x ^{n-1} + \dots + a_1x + a_0 $$

    $$ g(x) = b_m x ^{m} + a _{m-1}x ^{m-1} + \dots + b_1x + b_0 $$

    두 다항식의 합과 스칼라곱을 다음과 같이 정의한 $\mathbf{F}$ 에서 계수를 가져온 모든 다항식 집합을 벡터공간 $\mathbf{P}(\mathbf{F})$ 이라 정의한다.

    $$ f(x) + g(x) = (a_n+b_n) x ^{n} + (a _{n-1}+b _{n-1})x ^{n-1} + \dots+(a_1+b_1)x+(a_0+b_0) $$

    $$ cf(x) = ca_n x ^{n} + ca _{n-1}x ^{n-1} + \dots + ca_1x + ca_0 $$

- $\mathbf{P}_{}(\mathbf{F})$ 에서 [벡터공간](../LinearAlgebra/VectorSpace/#115df4450)의 공리가 모두 성립한다.

- 차수가 $n$ 인 다항식 집합을 $\mathbf{P}_{n}(\mathbf{F}) (\subset \mathbf{P}_{}(\mathbf{F}))$ 라 한다.

- 벡터공간 $\mathbf{P}(\mathbf{F})$ 와 다음 예제에서 보이는 벡터공간은 [본질적으로 같다.](../LinearAlgebra/LinearTransformation/#28bdb2c98) 

- 예시 

    임의의 체 $\mathbf{F}$ 위에서 정의된 수열(sequence)은 $\N \to \mathbf{F}$ 인 함수이다. 보통 수열 $\sigma (n) = a_n$ 을 $(a_n)$ 으로 표기한다. 체 $\mathbf{F}$ 에서 정의된 모든 수열의 집합을 $\mathbf{V}$ 라고 하자. 두 수열 $(a_n),(b_n)$ 을 다음과 같이 합과 스칼라곱으로 정의하면 $\mathbf{V}$ 는 벡터공간이다.

    $$ (a_n)+(b_n)=(a_n+b_n) \qquad t(a_n) = (ta_n) $$

# Division of Polynomial

!!! def "다항식의 나눗셈(division of polynomial)"

    두 다항식 $f, g$ 에 대하여 $g(x) = f(x)q(x)$ 인 다항식 $q$ 가 존재하면 다항식 $f$ 가 다항식 $g$ 를 나눈다고 정의한다.

!!! def "정리 1 다항식의 나눗셈 정리(division algorithm for polynomials)"

    다항식 $f(x)$ 와 다항식 $g(x)$ 에 대하여 $\deg (g) \geq 0$ 이면 다음을 만족하는 다항식 $q(x), r(x)$ 가 유일하게 존재하고, $\deg (r) < \deg (g)$ 이다.

    $$ f(x) = q(x)g(x) + r(x) $$

- **$q(x), r(x)$ 를 각각 $f(x)$ 를 $g(x)$ 로 나누었을 때의 몫(quotient) 과 나머지(remainder) 라 한다.**

- 증명

    $\deg (f) < \deg (g)$ 일 때 $q(x) = 0, r(x) = f(x)$ 로 두면 정리가 성립한다. ▲ 

    $0 \leq \deg (g) < \deg (f) \land \deg (f) = 0$ 이면 $f, g$ 는 상수 다항식이므로 $q(x) = \dfrac{f(x)}{g(x)}, r(x) = 0$ 으로 두면 정리가 성립한다. ▲ 

    $0 \leq \deg (g) < \deg (f) \land \deg (f) > 0$ 일 때 $\deg (f) = n, \deg (g) = m$ 으로 두자.  $n$ 미만의 차수를 갖는 다항식에서 정리가 성립함을 가정하자. $n$차 다항식 $f$ 와 $m$차 다항식 $g$ 와 또 다른 다항식 $h$ 를 다음과 같이 정의하자.

    $$ f(x) = a_n x ^{n} + a _{n-1}x ^{n-1} + \dots + a_1x + a_0 $$

    $$ g(x) = b_m x ^{m} + a _{m-1}x ^{m-1} + \dots + b_1x + b_0 $$

    $$ h(x) = f(x) - \frac{a_n}{b_m}x ^{n-m}g(x) \tag{1} $$

    $h$ 는 $\deg (h) < \deg (f)$ 인 다항식이다. 귀납법의 가정에 의하여 $g, h$ 에 대하여 정리가 성립하므로 다음을 만족하는 다항식 $q_1, r$ 이 유일하게 존재하고, $\deg (r) < \deg (m)$ 이다.

    $$ h(x) = q_1(x)g(x) + r(x) \tag{2} $$

    $(1), (2)$ 를 $f(x)$ 에 대하여 풀면 $q(x) = a_nb_m ^{-1}x ^{n-m} + q_1(x)$ 에 대하여 $f(x) = q(x)g(x) + r(x)$ 이다. 존재성 증명이 끝났으므로 유일성 증명만 하면 모든 증명이 끝난다. ▲ 

    이제 본 정리의 존재성을 가정할 수 있으므로 다음을 만족하는 다항식 $q_1,q_2,r_1,r_2$ 가 존재하고, $\deg (r_1) < \deg (g), \deg (r_2) < \deg (g)$ 이다.

    $$ f(x) = q_1(x)g(x) + r_1(x) = q_2(x)g(x) + r_2(x) $$

    식을 정리하면 다음이 성립한다.

    $$ \{q_1(x) - q_2(x)\}g(x) = r_2(x) - r_1(x) $$

    $\deg (r_2(x) - r_1(x))<\deg (g)$ 이므로 만약 $\deg (q_1(x) - q_2(x))\geq 0$ 이면 모순이다. 따라서 $\deg (q_1(x) - q_2(x)) = -1$ 이다. 따라서 $q_1(x) - q_2(x) = 0 \implies q_1 = q_2$ 이다. 그러면 $0 = r_2(x) - r_1(x) \implies r_1 = r_2$ 도 성립한다. ■ 

!!! def "정리 1 다항식의 나눗셈 정리(division algorithm for polynomials) 따름정리 1"

    $a \in \mathbf{F}$ 에 대하여 다항식 $f(x)$ 가 $\deg (f) \geq 1$ 이면 다음은 동치이다. 

    - $f(a) = 0$

    - $x-a$ 가 $f(x)$ 를 나눈다.

- 이 정리는 다항식이 해를 가지면 [완전히 인수분해](../LinearAlgebra/Diagonalization/#12bf9c352)됨을 말해준다.

- 증명

    $x-a$ 가 $f(x)$ 를 나눈다고 하면 $f(x) = (x-a)q(x)$ 인 다항식 $q(x)$ 가 존재하므로 $f(a) = 0$ 이다. ▲ 

    $f(a) = 0$ 을 가정하자. 다항식의 나눗셈 정리에 의하여 $f(x) = q(x)(x-a) + r(x)$ 를 만족하는 다항식 $q,r$ 이 존재한다. $\deg (r) < 1$ 이다. 즉, $c \in \mathbf{F} : r(x) = c$ 이다. 그러면 $f(a) = 0 + r(a) = 0$ 이 성립하므로 $c = 0$ 을 얻는다. ■ 

!!! def "정리 1 다항식의 나눗셈 정리(division algorithm for polynomials) 따름정리 2"

    $n (\geq 1)$차 다항식은 최대 $n$ 개의 서로 다른 근이 있다.

- 증명

    $n = 1$ 인 경우는 자명하다. ▲ 

    $n$ 에 대하여 성립함을 가정하고 $n + 1$ 의 경우를 증명하자. $\deg (f) = n+1$ 인 $f(x)$ 의 해가 없다면 정리가 자동으로 성립한다. ▲ 
    
    $f(x)$ 의 해가 있다고 가정하면 정리 1 따름정리 1 에 의하여 $a \in \mathbf{F}$ 에 대하여 $f(x) = (x - a)q(x)$ 가 성립한다. $\deg (q) < n+1$ 이다. 귀납법의 가정에 의하여 $q$ 는 최대 $n$ 개의 해를 가진다. $f$ 의 해는 $a$ 와 $q$ 의 해이므로 $f$ 는 최대 $n+1$ 개의 해를 가진다. ■ 

## relatively prime

!!! def "서로소(relatively prime)"

    다항식 $f_1(x), f_2(x), \dots, f_n(x)$ 를 동시에 나누는 다항식이 오직 상수 다항식이면 $f_1(x), f_2(x), \dots, f_n(x)$ 를 서로소라 한다.

- 예시 

    다항식 $f(x) = x(x-1)$ 와 $h(x) = (x-1)(x-2)$ 은 서로소가 아니다. 다항식 $f(x)$ 와 $g(x) = (x-2)(x-3)$ 은 서로소이다. 

- 아래의 정리 9 는 다항식의 인수분해가 유일함을 말해준다. 즉, 위 예시에서 다항식 $f, g$ 가 또 다른 형태로 인수분해되어 서로소가 아니게 될 가능성이 없다는 것이다.

!!! def "보조정리"

    서로소인 두 다항식 $f_1(x), f_2(x)$ 에 대하여 $q_1(x)f_1(x) + q_2(x)f_2(x) = 1$ 을 만족하는 다항식 $q_1(x), q_2(x)$ 가 존재한다. 

- 증명

    $\deg (f_1) \geq \deg (f_2)$ 를 가정해도 일반성이 보존된다.

    $\deg (f_2) = 0$ 이면 $c \in  \mathbf{F}\setminus \{0\} : f_2(x) = c$ 이므로 $q_1(x) = 0, q_2(x) = \dfrac{1}{c}$ 로 두면 정리가 성립한다. ▲ 

    자연수 $n$ 미만의 차수 다항식에서 정리가 성립함을 가정하고 $n$ 에 대하여 증명하자. $\deg (f_2) = n > 0$ 으로 두자. 다항식의 나눗셈 정리에 의하여 다음을 만족하는 다항식 $q,r$ 이 유일하게 존재하고, $\deg (r) < \deg (f_2) = n$ 이다.

    $$ f_1(x) = q(x)f_2(x) + r(x) \tag{1} $$

    $f_1, f_2$ 가 서로소이므로 $\deg (r) \geq 0$ 이다. 즉, $0 \leq \deg (r) < \deg (f_2)$ 이다.

    $f_2(x)$ 와 $r(x)$ 가 서로소가 아니면 이 둘을 나누는 다항식 $g(x)$ 가 존재하므로 $(1)$ 에 의하여 $g$ 는 $f_1$ 도 나눈다. $g$ 가 $f_1, f_2$ 를 동시에 나누므로 $f_1, f_2$ 가 서로소라는 가정에 모순이다. 따라서 $f_2, r$ 은 서로소이다.

    $\deg (r) < n$ 이므로 귀납법의 가정에 의하여 $f_2, r$ 에 대하여 다음을 만족하는 다항식 $g_1, g_2$ 가 존재한다. 

    $$ g_1(x)f_2(x) + g_2(x)r(x) = 1 \tag{2} $$

    $(1), (2)$ 에 의하여 다음이 성립한다. 

    $$ \begin{equation}\begin{split} 1&= g_1(x)f_2(x) + g_2(x) \{f_1(x) - q(x)f_2(x)\} \\ &= g_2(x)f_1(x) + \{g_1(x) - g_2(x)q(x)\}f_2(x) \\ \end{split}\end{equation} \tag*{} $$

    ■ 

!!! def "정리 2"

    서로소인 다항식 $f_1(x), f_2(x), \dots, f_n(x)$ 에 대하여 다음을 만족하는 다항식 $q_1(x), q_2(x), \dots, q_n(x)$ 가 존재한다. 
    
    $$ q_1(x)f_1(x) + q_2(x)f_2(x) + \dots + q_n(x)f_n(x) = 1 $$

- 증명

    다항식의 개수를 $n$ 으로 두고 수학적 귀납법을 사용하자.

    $n = 2$ 의 경우는 보조정리에서 증명되었다. ▲ 

    $n \geq 3$ 일 때 $n-1$ 개의 다항식에 대하여 정리가 성립함을 가정하고 $n$개의 다항식에서 정리를 증명하자. 처음 $n-1$개의 다항식이 서로소라고 가정하면 귀납법의 가정에 의하여 다음을 만족하는 다항식 $q_1, q_2, \dots, q _{n-1}$ 이 존재한다. 

    $$ q_1(x)f_1(x) + q_2(x)f_2(x) + \dots + q _{n-1}(x)f _{n-1}(x) = 1 $$

    $q_n(x) = 0$ 으로 두면 $q_1(x)f_1(x) + q_2(x)f_2(x) + \dots + q _{n}(x)f _{n}(x) = 1$ 이므로 증명이 끝난다. ▲ 

    처음 $n-1$개의 다항식이 서로소가 아니라고 가정하면 이들을 모두 나누고 가장 큰 차수를 가지고 최고차항의 계수가 $1$인 다항식 $g(x)$ 가 존재한다. 따라서 $k \in \{1,\dots,n-1\}$ 에 대하여 $f_k(x) = g(x)h_k(x)$ 인 다항식 $h_k$ 가 존재하고, $h_1, h_2, \dots, h _{n-1}$ 은 서로소이다. 귀납법의 가정에 의하여 다음을 만족하는 다항식 $\phi _1, \phi _2, \dots, \phi _{n-1}$ 이 존재한다.

    $$ \phi _1(x)h_1(x) + \phi _2(x)h_2(x) + \dots + \phi  _{n-1}(x)h _{n-1}(x) = 1 $$

    이 식에 $g(x)$ 를 곱하면 다음이 성립한다.

    $$ \phi _1(x)f_1(x) + \phi _2(x)f_2(x) + \dots + \phi  _{n-1}(x)f _{n-1}(x) = g(x) $$

    정리의 가정에 의하여 $g(x)$ 는 $f_n(x)$ 과 서로소이다. 서로소가 아니면 정리의 가정에 위배된다. 보조정리에 의하여 $p(x)g(x) + q_n(x)f_n(x) = 1$ 인 다항식 $p(x), q_n(x)$ 이 존재한다. $i \in \{1, \dots, n-1\}$ 에 대하여 $q_i(x) = p(x)\phi _i(x)$ 라 하면 다음이 성립한다.

    $$ \begin{equation}\begin{split}
    1 &= p(x)g(x) + q_n(x)f_n(x) \\
    &= p(x)\{\phi _1(x)f_1(x) + \phi _2(x)f_2(x) + \dots + \phi  _{n-1}(x)f _{n-1}(x)\} + q_n(x)f_n(x)\\
    &=q_1(x)f_1(x) + q_2(x)f_2(x) + \dots + q _{n}(x)f _{n}(x) 
    \end{split}\end{equation} \tag*{} $$

    ■ 

# Polynomial and Linearity

!!! def ""

    체 $\mathbf{F}$ 의 원소를 계수로 하는 다음과 같은 다항식 $f(x)$ 가 존재한다.

    $$ f(x) = a_0 + a_1x + \dots + a_nx ^{n} $$

    $\mathbf{F}$-벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 에 대하여 $f(\mathbf{T})$ 를 다음과 같이 정의한다.

    $$ f(\mathbf{T}) = a_0 \mathbf{I} + a_1 \mathbf{T} + \dots + a_n \mathbf{T}^{n} $$

    행렬 $A \in \mathbf{M}_{n \times n}(\mathbf{F})$ 에 대하여 $f(A)$ 를 다음과 같이 정의한다.

    $$ f(A) = a_0I_n + a_1A + \dots + a_nA ^{n} $$

- 예시

    $\R ^{2}$ 의 선형연산자 $\mathbf{T}(a, b) = (2a+b,a-b)$  와 $f(x) = x ^{2}+2x-3$ 를 가정하자. $\mathbf{T}^{2}(a,b) = (5a+b,a+2b)$ 이다. 다음이 성립한다.

    $$ \begin{equation}\begin{split} f(\mathbf{T})(a, b)&= (\mathbf{T}^{2}+2 \mathbf{T}-3 \mathbf{I})(a, b)\\ &= (5a+b,a+2b)+(4a+2b,2a-2b)-3(a,b)\\ &= (6a+3b,3a-3b) \end{split}\end{equation} \tag*{} $$

    행렬 $A = \begin{pmatrix} 2&1\\ 1&-1\\ \end{pmatrix}$ 에 대하여 다음이 성립한다. 

    $$ f(A)=A ^{2}+2A-3I_2=\begin{pmatrix} 5&1\\ 1&2\\ \end{pmatrix}+2 \begin{pmatrix} 2&1\\ 1&-1\\ \end{pmatrix}-3 \begin{pmatrix} 1&0\\ 0&1\\ \end{pmatrix}= \begin{pmatrix} 6&3\\ 3&-3\\ \end{pmatrix} $$

!!! def "정리 3"

    다항식 $f(x) \in \mathbf{P}_{}(\mathbf{F})$ 와 $\mathbf{F}$-벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 에 대하여 다음이 성립한다.

    1. $f(\mathbf{T})$ 는 $\mathbf{V}$ 의 선형연산자이다.

    2. $\mathbf{V}$ 의 유한순서기저 $\beta$ 와 $A = [\mathbf{T}]_{\beta }$ 에 대하여 $[f(\mathbf{T})]_{\beta } = f(A)$ 이다.

- 증명

    1:

    [선형연산자](../LinearAlgebra/LinearTransformation/#c96eea3c8) 의 정의가 충족되는지 살펴보자. $f$ 를 다음과 같이 정의하자.

    $$ f(x) = a_0 + a_1x + \dots + a_nx ^{n} $$

    $f(\mathbf{T})$ 는 다음과 같다.

    $$ f(\mathbf{T}) = a_0 \mathbf{I} + a_1 \mathbf{T} + \dots + a_n \mathbf{T}^{n} $$

    [선형변환의 합과 스칼라곱도 선형](../LinearAlgebra/LinearTransformation/#91b876399)이다. 따라서 $f(\mathbf{T})$ 는 선형이다. ▲ 

    [$\mathbf{R}(\mathbf{T})$ 는 $\mathbf{T}$-불변](../LinearAlgebra/Diagonalization/#a55a4420e)이므로 $n \in \N : \mathbf{R}(\mathbf{T}^{n}) \in \mathbf{V}$ 이다. [$\mathbf{R}(\mathbf{T})$ 는 $\mathbf{V}$ 의 부분공간](../LinearAlgebra/LinearTransformation/#eb957cbf0)이므로 덧셈에 대하여 닫혀있다. 따라서 $f(\mathbf{T})\in \mathbf{V}$ 이다. ▲ 

    2:

    [선형변환의 행렬표현은 덧셈과 스칼라곱에 대하여 선형적](../LinearAlgebra/LinearTransformation/#aa431d8ac)이므로 다음이 성립한다. 

    $$ \begin{equation}\begin{split} [f(\mathbf{T})]_{\beta } &= [a_0 \mathbf{I} + a_1 \mathbf{T} + \dots + a_n \mathbf{T}^{n} ]_{\beta }\\ &= a_0[ \mathbf{I}]_{\beta } + a_1[ \mathbf{T}]_{\beta } + \dots + a_n[ \mathbf{T}^{n} ]_{\beta }\\ \end{split}\end{equation} \tag*{} $$

    [선형변환의 행렬표현은 선형변환의 합성을 보존하여 행렬곱으로 표현할 수 있게 해주므로](../LinearAlgebra/LinearTransformation/#143fdacba) $[\mathbf{T}^{2}]_{\beta }=[\mathbf{T}]_{\beta }[\mathbf{T}]_{\beta }$ 이다. 즉, 다음이 성립한다. 

    $$ [f(\mathbf{T})]_{\beta } = a_0I + a_1A + \dots + a_nA^{n} = f(A) \tag*{■} $$

!!! def "정리 4"

    $\mathbf{F}$-벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 와 $\mathbf{F}$ 의 원소를 성분으로 하는 정사각행렬 $A$ 임의의 다항식 $f_1(x), f_2(x) \in \mathbf{P}_{}(\mathbf{F})$ 에 대하여 다음이 성립한다. 

    1. $f_1(\mathbf{T})f_2(\mathbf{T}) = f_2(\mathbf{T})f_1(\mathbf{T})$

    2. $f_1(A)f_2(A) = f_2(A)f_1(A)$

- 증명

    1:

    $f_1, f_2$ 를 다음과 같이 정의하자.

    $$ f_1(x) = a_0 + a_1x + \dots + a_nx ^{n} $$

    $$ f_2(x) = b_0 + b_1x + \dots + b_mx ^{m} $$

    $n \geq m$ 을 가정하고 $b_n = b _{n-1} = \dots = b _{m+1} = 0$ 으로 정의하면 $f_2$ 는 다음과 같다.

    $$ f_2(x) = b_0 + b_1x + \dots + b_nx ^{n} $$

    $f_1(\mathbf{T}), f_2(\mathbf{T})$ 는 다음과 같다.

    $$ f_1(\mathbf{T}) = a_0 \mathbf{I} + a_1 \mathbf{T} + \dots + a_n \mathbf{T}^{n} $$

    $$ f_2(\mathbf{T}) = b_0 \mathbf{I} + b_1 \mathbf{T} + \dots + b_n \mathbf{T}^{n} $$

    [선형변환의 합성의 성질](../LinearAlgebra/LinearTransformation/#273a736ad)에 의하여 다음이 성립한다.

    $$ \begin{equation}\begin{split} f_1(\mathbf{T})f_2(\mathbf{T})&=(a_0 \mathbf{I} + a_1 \mathbf{T} + \dots + a_n \mathbf{T}^{n})(b_0 \mathbf{I} + b_1 \mathbf{T} + \dots + b_n \mathbf{T}^{n}) \\ &=(b_0 \mathbf{I} + b_1 \mathbf{T} + \dots + b_n \mathbf{T}^{n})(a_0 \mathbf{I} + a_1 \mathbf{T} + \dots + a_n \mathbf{T}^{n}) = f_2(\mathbf{T})f_1(\mathbf{T})\\ \end{split}\end{equation} \tag*{} $$

    ▲ 

    2:

    [행렬곱의 성질](../LinearAlgebra/LinearTransformation/#e08d1e569) 에 의하여 1) 의 증명과 비슷하게 쉽게 증명 가능하다. ■ 

!!! def "정리 5"

    $\mathbf{F}$-벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 와 행렬 $A \in \mathbf{M}_{n \times n}(\mathbf{F})$ 와 서로소인 두 다항식 $f_1(x), f_2(x) \in \mathbf{P}_{}(\mathbf{F})$ 에 대하여 다음을 만족하는 다항식 $q_1(x), q_2(x) \in \mathbf{P}_{}(\mathbf{F})$ 가 존재한다.

    1. $q_1(\mathbf{T})f_1(\mathbf{T})+q_2(\mathbf{T})f_2(\mathbf{T}) = \mathbf{I}$

    2. $q_1(A)f_1(A) + q_2(A)f_2(A) = I$

- 증명

    보조정리에 의하여 서로소인 다항식 $f_1, f_2$ 에 대하여 $q_1(x)f_1(x) + q_2(x)f_2(x) = 1$ 를 만족하는 다항식 $q_1, q_2$ 가 존재한다. 따라서 $q_1(\mathbf{T})f_1(\mathbf{T})+q_2(\mathbf{T})f_2(\mathbf{T}) = \mathbf{I}$ 가 성립하고, $q_1(A)f_1(A) + q_2(A)f_2(A) = I$ 가 성립한다. ■ 

# monic, irreducible

!!! def "모닉(monic)"

    다항식 $f(x) \in \mathbf{F}$ 의 최고차항의 계수가 $1$ 이면 모닉이라 한다.

!!! def "기약(irreducible)"

    다항식 $f(x)$ 가 $\deg (f) \geq 1$ 이고 다음을 만족하면 $f(x)$ 를 기약이라 한다.

    $$ f(x) = q(x)r(x) \implies \deg (q) = 0 \lor \deg (r) = 0 $$

- 즉, 상수가 아닌 다항식 $f(x) \in \mathbf{P}_{}(\mathbf{F})$ 가 상수가 아닌 다항식으로 인수분해되지 않으면 $f(x)$ 를 기약이라 한다.

- 차수가 $1$ 인 다항식도 기약이다. 대수적으로 닫힌 체의 원소로 구성된 다항식은 차수가 $1$ 인 다항식만 기약다항식이다. 대수학의 기본정리에 의하여 복소수체에서는 차수가 $1$ 인 다항식만 기약다항식이다.

- 다항식은 그것이 속한 체에 따라 기약인지, 기약이 아닌지가 결정된다.

- 예시

    다항식 $f(x) = x ^{2} + 1$ 은 $\mathbf{P}_{}(\R )$ 위에서 기약이다. 하지만 $\mathbf{P}_{}(\mathbb{C})$ 위에서는 $x ^{2} + 1 = (x + i)(x - i)$ 이 되어 기약이 아니다.

    다항식 $f(x) = x ^{2} - 2$ 는 $\mathbf{P}_{}(\mathbb{Z})$ 위에서 기약이다. 하지만 $f(x) = (x-\sqrt[]{2})(x+\sqrt[]{2})$ 이므로 $\mathbf{P}_{}(\R )$ 위에서 기약이 아니다.

!!! def "정리 6"

    다항식 $\phi (x)$ 와 $f(x)$ 에 대하여 $\phi (x)$ 가 기약이고 $\phi (x)$ 가 $f(x)$ 를 나누지 않으면 $\phi (x)$ 와 $f(x)$ 는 서로소이다.

- 증명

    정리의 가정이 모두 충족되었는데도 두 다항식이 서로소가 아니면 다음을 만족하는 다항식 $g$ 가 존재하고 $\deg (g) \geq 1$ 를 만족한다.

    $$ \phi (x) = g(x)q_1(x) $$

    $$ f(x) = g(x)q_2(x) $$

    $\phi$ 는 기약이므로  $\deg (g) = 0 \lor \deg (q_1) = 0$ 이다. 따라서 $\deg (q_1) = 0$ 이다.  그러면 $c \in \mathbf{F} : q_1(x) = c \implies \phi (x) = c \cdot g(x)$ 이므로 $\phi$ 가 $f$ 를 나누게 되어 모순이다. ■ 

!!! def "정리 7"

    서로 다른 기약 모닉 다항식은 서로소이다.

- 증명

    서로 다른 기약 모닉 다항식 $f, g$ 가 서로소가 아니라고 해보자. 그러면 다음을 만족하는 다항식 $h$ 가 존재하고 $\deg (h) \geq 1$ 를 만족한다.

    $$ f (x) = h(x)q_1(x) $$

    $$ g(x) = h(x)q_2(x) $$

    $f, g$ 가 기약이므로 $\deg (q_1) = 0, \deg (q_2) = 0$ 이다. $f, g$ 가 모닉이므로 $q_1(x) = 1, q_2(x) = 1$ 이다. 따라서 $f(x) = h(x) = g(x)$ 이고, 이는 모순이다. ■ 

!!! def "정리 8"

    다항식 $f(x), g(x), h(x)$ 에 대하여 $h(x)$ 가 기약이고 $h(x)$ 가 $f(x)g(x)$ 를 나누면 $h(x)$ 는 $f(x)$ 를 나누거나 $g(x)$ 를 나눈다.

- 증명

    $\phi$ 가 $f$ 를 나누지 않으면 정리 6 에 의하여 이 둘은 서로소이다. 그러면 보조정리에 의하여 $1 = q_1(x)\phi (x) + q_2(x)f(x)$ 인 다항식 $q_1, q_2$ 가 존재한다. 이 식에 $g(x)$ 를 곱하면 다음을 얻는다. 

    $$ g(x) = q_1(x)\phi (x)g(x) + q_2(x)f(x)g(x) $$

    $\phi(x)$ 는 $f(x)g(x)$ 를 나누므로 $g(x)$ 도 나눈다. ▲ 

    $\phi$ 가 $g$ 를 나누지 않는다고 가정하면 똑같은 논리로 $f$ 를 나누는 것을 보일 수 있다. ■ 

!!! def "정리 8 따름정리"

    기약 모닉 다항식 $\phi (x), \phi _1(x), \dots, \phi _n(x)$ 에 대하여 $\phi (x)$ 가 $\phi_1(x)\phi _2(x)\dots \phi _n(x)$ 를 나누면 $\exists i \in \{1, \dots, n\} : \phi (x) = \phi _i(x)$ 이다.

- 증명

    $n = 1$ 이면 정리 7 에 의하여 성립한다. ▲ 

    $n > 1$ 일 때 $n - 1$ 개의 기약 모닉 다항식에 대하여 정리가 성립함을 가정하자. 정리에 따라 $\phi (x)$ 가 다음 식을 나눈다고 가정하자. 

    $$ \phi _1(x)\dots \phi _{n}(x) = \{\phi _1(x)\dots \phi _{n-1}(x)\}\phi _n(x) $$

    정리 8 에 의하여 $\phi (x)$ 는 $\phi _1(x)\dots \phi _{n-1}(x)$ 를 나누거나 $\phi _n(x)$ 를 나눈다. 전자의 경우 귀납법의 가정에 의하여 $\exists i \in \{1,\dots,n-1\} : \phi (x) = \phi _i(x)$ 이고, 후자의 경우 $\phi (x) = \phi _n(x)$ 이다. ■ 

## Uniqueness of Polynomial Factorization

!!! def "정리 9 다항식 인수분해의 유일성(Unique Factorization Theorem for Polynomials)"

    다항식 $f(x)$ 가 $\deg (f) \geq 1$ 이면 다음을 만족하는 상수 $c$, 서로 다른 기약 모닉 다항식 $\phi _1(x), \phi _2(x), \dots, \phi _k(x)$, 자연수 $n_1, n_2, \dots, n_k$ 가 유일하게 존재한다.

    $$ f(x) = c \prod_{i=1}^{k}\{\phi _i(x)\}^{n_i} = c \{\phi _1(x)\}^{n_1}\{\phi _2(x)\}^{n_2}\dots\{\phi _k(x)\}^{n_k} $$

- **지금까지의 정리들의 결론이 이 정리이다.** 이 정리에 선형대수학의 [특성다항식 이론](../LinearAlgebra/Diagonalization/#characteristic-polynomial-finding-eigenvalue)과 표준형 이론이 많이 의존한다.

- 증명

    인수분해의 존재성:

    $f(x) \in \mathbf{P}_{}(\mathbf{F})$ 의 차수에 대한 수학적 귀납법을 사용하자.

    $n = 1$ 일 때 $\deg (f)=1$ 이면 $f(x) = ax + b$ 를 만족하는 $a \neq 0, b \in \mathbf{F}$ 가 존재한다. $\phi (x) = x + \dfrac{b}{a}$ 로 두면 $f(x)=a \phi (x)$ 이다. ▲ 

    $n > 1$ 일 때 $\deg (f) < n$ 인 다항식 $f$ 에 대하여 인수분해의 존재성을 가정하고 $\deg (f) = n$ 로 두자. 그러면 $f(x) = a_nx ^{n} + \dots + a_1x+a_0$ 을 만족하는 $a_n \neq 0, a _{n-1}, \dots, a_0 \in \mathbf{F}$ 가 존재한다. $f$ 가 기약이면 다음이 성립하므로 인수분해가 존재한다. 

    $$ f(x) = a_n \bigg (x ^{n} + \sum_{i=n-1}^{0}\dfrac{a _{i}}{a_n}x ^{i} \bigg ) \tag*{▲} $$

    $f(x)$ 가 기약이 아니면 $f(x) = g(x)h(x)$ 인 다항식 $g, h$ 가 존재한다. $\deg (g) < n, \deg (h)<n$ 이므로 귀납법의 가정에 의하여 $g, h$ 의 인수분해가 존재한다. 즉, $g, h$ 는 상수와 기약 모닉 다항식의 곱으로 표현된다. 따라서 $f$ 의 인수분해가 존재한다. ▲ 

    인수분해의 유일성:

    다음을 만족하는 상수 $c, d$, 기약 모닉 다항식 $\phi _i(x), \psi _j(x)$, 자연수 $n_i, m_j$ 의 존재를 가정하자. $i \in \{1, \dots, k\}, j \in \{1, \dots, r\}$ 이다.

    $$ \begin{equation}\begin{split}
    f(x)&= c \{\phi _1(x)\}^{n_1}\{\phi _2(x)\}^{n_2}\dots \{\phi _k(x)\}^{n_k} \\
    &= d \{\psi _1(x)\}^{m_1}\{\psi _2(x)\}^{m_2}\dots \{\psi _r(x)\}^{m_r} \\
    \end{split}\end{equation} \tag*{}
    $$

    $c, d$ 는 $f(x)$ 의 최고차항의 계수이므로 $c = d$ 이다. ▲ 

    위 식을 $c$ 로 나누면 다음을 얻는다.

    $$ \{\phi _1(x)\}^{n_1}\{\phi _2(x)\}^{n_2}\dots \{\phi _k(x)\}^{n_k} = \{\psi _1(x)\}^{m_1}\{\psi _2(x)\}^{m_2}\dots \{\psi _r(x)\}^{m_r} \tag{1} $$

    정리 8 따름정리에 의하여 $\forall i \in \{1, \dots, k\}, \exists j \in \{1, \dots, r\} : \phi _i(x) = \psi _j(x)$ 이다. $\phi _i, \psi _j$ 들은 모두 서로 다르므로 $r = k$ 이다. 또한 $\forall i \in \{1, \dots,k\} : \phi _i = \psi_i$ 로 두어도 상관없다. 상수의 유일성, 기약 모닉 다항식의 유일성을 보였으니 거듭제곱을 하는 자연수의 유일성만 마저 보이면 된다. ▲ 

    $\exists i \in \{1,\dots,k\} : n_i \neq m_i$ 를 가정하자. $i = 1, n_1 > m_1$ 이라고 가정해도 일반성이 보존된다. $(1)$ 을 $\{\phi _1(x)\}^{m_1}$ 으로 나누면 다음이 성립한다.

    $$ \{\phi _1(x)\}^{n_1 - m_1}\{\phi _2(x)\}^{n_2}\dots \{\phi _k(x)\}^{n_k} = \{\phi _1(x)\}^{m_2}\dots \{\phi _r(x)\}^{m_r} $$

    따라서 $\phi _1(x)$ 는 좌변도 나누고 우변도 나눈다. 그러면 정리 8 따름정리에 의하여 $\exists i \in \{1, \dots,k\} : \phi _1(x) = \phi _i(x)$ 이다. 이는 모순이다. 따라서 $\forall i \in \{1, \dots, k\} : n_i = m_i$ 이다. ■ 

# Polynomial Function

!!! def "일변수 다항함수(polynomial function of one variable)"

    체 $\mathbf{F}$ 와 $a_0, a_1, \dots, a_n \in \mathbf{F}$ 에 대한 일변수 다항함수 $f:\mathbf{F}\to \mathbf{F}$ 는 다음과 같이 정의된다.

    $$ f(x) = a_nx ^{n} + a _{n-1}x ^{n-1} + \dots + a_1x + a_0 $$

- $\mathbf{P}_{}(\mathbf{F})$ 위의 다항식을 $\mathbf{F}\to \mathbf{F}$ 에서 정의된 함수로 보면 다항함수가 된다. 다항식을 다항함수로 볼 때 편한 상황들이 많이 있다. 

!!! def "이변수 다항함수(polynomial function of two variables)"

    변수 2개를 갖는 다항함수이다.

- 예시

    $$ f(x, y) = 2x ^{3} + 4x ^{2}y +xy ^{5} + y ^{2} -y $$

!!! def "다변수 다항함수(polynomial functions of several variables, multivariate polynomial function)"

    2개 이상의 변수를 갖는 다항함수이다.

!!! def "정리 10"

    무한체 $\mathbf{F}$ 와 $\mathbf{F}\to \mathbf{F}$ 위에서 정의된 모든 함수 집합 $\mathcal{F}(\mathbf{F}, \mathbf{F})$ 에 대하여 다항식을 다항함수로 보내는 대응 $\mathbf{P}_{}(\mathbf{F})\to \mathcal{F}(\mathbf{F},\mathbf{F})$ 은 단사이다.

- 유한체 $\mathbf{F}$ 와 $\mathbf{F}\to \mathbf{F}$ 위에서 정의된 모든 함수 집합 $\mathcal{F}(\mathbf{F}, \mathbf{F})$ 에 대한 대응 $\mathbf{P}_{}(\mathbf{F})\to \mathcal{F}(\mathbf{F},\mathbf{F})$ 은 [단사](../Set/Set/#eadfd845f)가 아닐 수도 있다. 쉽게 말해서 서로 다른 다항식인데도 같은 다항함수가 될 수도 있다는 것이다. 

    - 예시

        유한체 $\mathbb{Z}_{2} = \{0, 1\}$ 를 다음과 같이 정의하자.

        $$ 0 + 0 = 0, \qquad 0+1 = 1+0 = 1, \qquad 1+1 = 0, $$

        $$ 0 \cdot 0 = 0, \qquad 0 \cdot 1 = 1 \cdot 0 = 0, \qquad 1 \cdot 1 = 1 $$

        다항식 $f(x) = x ^{2}, g(x) = x \in \mathbf{P}_{}(\mathbb{Z}_{2})$ 을 다항함수 $f: \mathbb{Z}_{2} \to \mathbb{Z}_{2}, g: \mathbb{Z}_{2} \to \mathbb{Z}_{2}$ 로 만들자. 그러면 다음이 성립한다. 

        $$ f(x) \neq  _{\mathbf{P}_{}(\mathbb{Z}_{2})} g(x) $$

        $$ f(x) = _{\mathcal{F}(\mathbb{Z}_{2},\mathbb{Z}_{2})} g(x) $$

        즉, $f, g$ 가 다항식으로써는 서로 다르지만 다항함수로써는 서로 같다는 것이다. [다항식의 상등](#b3486412c) 의 정의과 [함수의 상등의 정의](../Set/Set/#57b118c60) 를 참고하자.

    그러나 **이 정리는 무한한 원소를 가진 무한체에서는 이러한 이상한 일이 일어나지 않는다는 것을 보장해준다.**

- 증명

    [단사](../Set/Set/#eadfd845f) 의 정의에 의하여 다음이 성립함을 보여야 한다.

    $$ f, g \in \mathcal{F}(\mathbf{F},\mathbf{F}) : f = _{\mathcal{F}(\mathbf{F},\mathbf{F})} g \implies f = _{\mathbf{P}_{}(\mathbf{F})} g $$

    [함수의 상등의 정의](../Set/Set/#57b118c60) 에 의하여 이는 다음을 보이는 것과 같다.

    $$ \forall a \in \mathbf{F} : f(a) = g(a) \implies f =_{\mathbf{P}_{}(\mathbf{F})} g $$

    $f \neq  _{\mathbf{P}_{}(\mathbf{F})} g$ 라고 하고 모순을 이끌어내면 증명이 끝난다. 다항식 $h(x) = f(x) - g(x)$ 을 정의하면 $\deg (h) = -1 \implies f = _{\mathbf{P}_{}(\mathbf{F})} g$ 이므로 $\deg (h) \geq 0$ 이어야 한다.

    $\deg (h) = 0$ 이라 하면 $f, g$ 가 상수항에서 서로 다르다. 따라서 $\forall a \in \mathbf{F}: f(a) = g(a)$ 에 모순이다. [체의 임의의 원소에 $0$ 을 곱하면 $0$ 이 되므로](../LinearAlgebra/VectorSpace/#a822715aa) $f(0) \neq g(0)$ 이기 때문이다. ▲ 

    $\deg (h) \geq 1$ 이라 하자. [정리 1 따름정리 2](#bb1063b23) 에 의하여 $h$ 는 최대 $\deg (h)$ 개의 해를 갖는다. 그런데 $\forall a \in \mathbf{F}:h(a) = 0$ 이므로 $h$ 의 해는 무한히 많다. 따라서 모순이다. ▲ 

    그러니까 반드시 $\deg (h) = -1$ 이어야 하고 이로써 $f \neq _{\mathbf{P}_{}(\mathbf{F})}g$ 라는 가정이 틀렸다는 것을 알 수 있다. ■ 

    <!-- - $\mathbf{F}$ 가 유한체면 $\forall a \in \mathbf{F} :h(a) = 0$ 에서 $h$ 가 무한히 많은 해를 갖는다는 결론이 나오지 않는다. -->

# Fundamental Theorem of Algebra

!!! def "대수학의 기본 정리(fundamental theorem of algebra)"

    $\mathbf{P}(\mathbb{C})$ 의 다항식 $p(z) = a_nz ^{n} + \dots + a_1z + a_0$ 의 차수가 $n \geq 1$ 이면 $p(z)$ 는 해가 있다.

- 17세기부터 수학자들이 옳으리라고 추측했던 유명한 정리이다. 대수학의 기본 정리이지만 순수하게 대수적인 증명은 누구도 해내지 못했고, 훗날 위상수학과 해석학을 도입하여 증명을 할 수 있었다. 그래서 복소해석학에 의한 증명과 위상수학에 의한 증명이 존재한다.

- 증명

!!! def "대수학의 기본 정리(fundamental theorem of algebra) 따름정리"

    차수가 $n \geq 1$ 이고 복소계수를 포함한 다항식 $p(z) = a_nz ^{n} + \dots + a_1z + a_0$ 에 대하여 다음을 만족하는 복소수 $c_1, c_2, \dots, c_n$ 이 존재한다. 

    $$ p(z) = a_n(z-c_1)(z-c_2)\dots(z-c_n) $$

- 이 정리는 **[복소내적공간](../LinearAlgebra/InnerProductSpaces/#653ace4b3)의 선형연산자의 [특성다항식](../LinearAlgebra/Diagonalization/#2f3482489)이 반드시 [완전히 인수분해](../LinearAlgebra/Diagonalization/#12bf9c352)됨을 말해준다.** 

- 체의 원소를 계수로 가지고 차수가 자연수인 다항식이 일차식의 곱으로 표현되는 체를 대수적으로 닫힌(algebraically closed) 체라 한다. 이 정리는 복소수체가 대수적으로 닫혀있음을 말해준다. 

- 증명

    대수학의 기본정리에 의하여 $p(z) \in \mathbf{P}_{}(\mathbb{C})$ 는 해 $c_1 \in \mathbb{C}$ 를 가진다. 정리 1 따름정리 1 에 의하여 $z - c_1$ 가 $p(z)$ 를 나누므로 차수가 $n-1$ 이고 최고차항의 계수가 $1$ 인 다항식 $f(z)$ 에 대하여 다음이 성립한다. 

    $$ p(z) = a_n(z - c_1)f(z) $$

    $f(z)$ 처럼 $p(z)$ 를 나누는 다항식의 차수가 $1$ 이상인 한 대수학의 기본정리에 의하여 항상 해가 존재하여 위와 같은 일차식 $z - c_1$ 으로 $p(z)$ 를 나눌 수 있다. 따라서 다음이 성립한다.

    $$ p(z) = a_n(z - c_1)\dots(z-c_n) \tag*{■} $$


---

ref:

:   Stephen H. Friedberg, Linear Algebra, 5th Edition

:   https://ko.wikipedia.org/wiki/%EC%84%9C%EB%A1%9C%EC%86%8C_%EC%95%84%EC%9D%B4%EB%94%94%EC%96%BC