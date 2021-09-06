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

    다항식 $f_1(x), f_2(x), \dots, f_n(x)$ 를 동시에 나누는 다항식이 존재하지 않으면 $f_1(x), f_2(x), \dots, f_n(x)$ 를 서로소라 한다.

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

    $$ \begin{equation}\begin{split} f(\mathbf{T})(a, b)&= (\mathbf{T}^{2}+2 \mathbf{T}-3 \mathbf{I})(a, b)\\ &= (5,a+b,a+2b)+(4a+2b,2a-2b)-3(a,b)\\ &= (6a+3b,3a-3b) \end{split}\end{equation} \tag*{} $$

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
