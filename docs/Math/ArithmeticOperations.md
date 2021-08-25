!!! info "ref"

    https://en.wikipedia.org/wiki/Summation

# Summation

!!! tldr "Summation"

    Summation 은 수열 $g(i)$ 의 덧셈으로써 다음과 같이 재귀적으로 정의된다. 

    $$ \sum_{i=a}^{b}g(i) = \begin{cases}
    0 & b < a\\
    g(b) + \displaystyle \sum_{i=a}^{b-1}g(i) & b \geq a\\
    \end{cases} 
    $$

- 수열은 숫자, 함수, 벡터, 행렬, 다항식 등 임의의 타입의 수학적 대상들로 구성 될 수 있다. 

- 무한수열의 Summation 을 series 라고 한다. 

- 쉽게 말해 Summation 은 다음과 같다. 

    $$ \sum_{i=m}^{n}a_i = a_m + a _{m+1} + \dots + a _{n-1} + a_n $$

    $i$ 를 summation 의 index 라고 한다. $m$ 을 summation 의 하계(lower bound)라고 하고, $n$ 을 summation 의 상계(upper bound)라고 한다. 

    - 예시 

        $$ \sum_{i=3}^{6}i ^{2} = 3 ^{2} + 4 ^{2} + 5 ^{2} + 6 ^{2} = 86 $$

    만약 index 와 하계, 상계를 일일이 표기하지 않아도 될 정도로 맥락이 명확하다면 다음과 같이 생략을 하기도 한다.

    $$ \sum a_i ^{2} = \sum_{i=1}^{n}a ^{2}_i $$

    임의의 논리 조건이 필요하다면 Summation 의 표기법을 일반화시켜서 조건을 충족하는 모든 수열의 덧셈을 표현할 수도 있다.

    - 예시 

        다음은 특정 범위 내의 $k$ 에 대한 $f(k)$ 의 덧셈을 표현한다.

        $$ \sum_{0 \leq k < 100}^{}f(k) $$

        다음은 집합 $S$ 의 원소 $x$ 에 대한 $f(x)$ 의 덧셈을 표현한다. 

        $$ \sum_{x \in S}^{}f(k) $$

    Summation 의 index 를 다음과 같이 일반화할 수도 있다.

    $$ \sum_{i}^{}\sum_{j}^{} = \sum_{i,j}^{} $$

    이러한 표기법들은 $\displaystyle \prod_{}^{}$ 에서도 통용된다.

## Properties of Summation

!!! tldr "Distributivity (1)"

    $$ \sum_{n=s}^{t}C \cdot f(n) = C \cdot \sum_{n=s}^{t}f(n) $$

- 증명

!!! tldr "Commutativity and Associativity (1)"

    $$ \sum_{n=s}^{t}f(n) \pm \sum_{n=s}^{t}g(n) = \sum_{n=s}^{t}(f(n) \pm g(n)) $$

- 증명

!!! tldr "Commutativity and Associativity (2)"

    $$ \sum_{i=k_0}^{k_1}\sum_{j=l_0}^{l_1}a _{ij} = \sum_{j=l_0}^{l_1}\sum_{i=k_0}^{k_1}a _{ij} $$

- 증명

!!! tldr "Commutativity and Associativity (3)"

    $$ \sum_{k \leq j \leq i \leq n}^{} a _{ij} = \sum_{i=k}^{n}\sum_{j=k}^{i}a _{ij}= \sum_{j=k}^{n}\sum_{i=j}^{n}a _{ij}= \sum_{j=0}^{n-k}\sum_{i=k}^{n-j}a _{i+j, i} $$

- 증명

!!! tldr "Distributivity (2)"

    $$ \bigg (\sum_{i=0}^{n}a_i \bigg ) \bigg (\sum_{j=0}^{n}b_j \bigg ) = \sum_{i=0}^{n}\sum_{j=0}^{n}a_ib_j $$

- 증명

!!! tldr "Distributivity (3)"

    $$ \bigg (\sum_{i=s}^{m}a_i \bigg ) \bigg (\sum_{j=t}^{n}b_j \bigg ) = \sum_{i=s}^{m}\sum_{j=t}^{n}a_ib_j $$

- 증명

## Powers and logarithm of arithmetic progression

!!! tldr "등차수열의 합(Sum of arithmetic progression)"

    자연수 $i, n \in \N$ 에 대하여 다음이 성립한다. 

    $$ \sum_{i=0}^{n}i = \sum_{i=1}^{n}i = \frac{n(n+1)}{2} $$

- 증명

!!! tldr "홀수의 합(Sum of odd natural numbers)"

    자연수 $i, n \in \N$ 에 대하여 다음이 성립한다. 

    $$ \sum_{i=1}^{n}(2i - 1) = n ^{2} $$

- 증명

!!! tldr "짝수의 합(Sum of even natural numbers)"

    자연수 $i, n \in \N$ 에 대하여 다음이 성립한다. 

    $$ \sum_{i=1}^{n}2i = n(n + 1) $$

- 증명

!!! tldr "제곱수의 합(Sum of squares)"

    자연수 $i, n \in \N$ 에 대하여 다음이 성립한다. 

    $$ \sum_{i=0}^{n}i ^{2} = \sum_{i=1}^{n}i ^{2} = \frac{n(n+1)(2n+1)}{6} = \dfrac{n ^{3}}{3} + \frac{n ^{2}}{2} = \frac{n}{6} $$
   
- 증명

!!! tldr "Nicomachus's theorem"

    자연수 $i, n \in \N$ 에 대하여 다음이 성립한다. 

    $$ \sum_{i=0}^{n}i ^{3} = \bigg (\sum_{i=0}^{n}i \bigg ) ^{2} = \bigg (\frac{n(n+1)}{2} \bigg ) ^{2} = \dfrac{n ^{4}}{4} + \dfrac{n ^{3}}{2} + \frac{n ^{2}}{4} $$
   
- 증명

!!! tldr "Faulhaber's formula"

    $p > 1$ 와 Bernoulli number $B_k$ 와 binomial coefficient $\displaystyle \binom{p}{k}$ 에 대하여 다음이 성립한다. 

    $$ \sum_{k=1}^{n}k ^{p} = \dfrac{n ^{p+1}}{p + 1} + \frac{1}{2}n ^{p} + \sum_{k=2}^{p}\binom{p}{k}\dfrac{B_k}{p - k + 1}n ^{p - k + 1} $$

- 증명

## Summation index in exponents

!!! tldr "등비수열의 합(sum of a geometric progression) (1)"

    자연수 $i, n \in \N$ 에 대하여 다음이 성립한다. 

    $$ \sum_{i=0}^{n-1}a ^{i} = \dfrac{1 - a ^{n}}{1 - a} $$
    
- 증명

!!! tldr "등비수열의 합(sum of a geometric progression) (2)"

    자연수 $i, n \in \N$ 에 대하여 다음이 성립한다. 

    $$ \sum_{i=0}^{n-1}ia ^{i} = \dfrac{a - na ^{n} + (n - 1)a ^{n+1}}{(1 - a) ^{2}} $$

- 증명

!!! tldr "산술기하수열의 합(sum of an arithmetico-geometric sequence)"

    $$ \begin{equation}\begin{split} \sum_{i=0}^{n-1}(b + id)a ^{i} &= b \sum_{i=0}^{n-1}a ^{i} + d \sum_{i=0}^{n-1}ia ^{i} \\ &= b \bigg (  \dfrac{1 - a ^{n}}{1 - a} \bigg ) + d \bigg (\dfrac{a - na ^{n} + (n-1)a ^{n+1}}{(1 - a) ^{2}} \bigg )  \\ &= \dfrac{b(1-a ^{n}) - (n-1)da ^{n}}{1 - a} + \dfrac{da(1 - a ^{n-1})}{(1 - a) ^{2}} \\ \end{split}\end{equation} \tag*{} $$

- 증명

# Multiplication

!!! tldr "곱셈(Multiplication)"

    덧셈의 반복이다.

- 곱셈은 덧셈 $+$ 이 정의된 수학적 대상에 대하여 덧셈을 반복하는 것이다. 가령 다음과 같이 $3 \times 4$ 는 $4$ 를 $3$ 번 더한 것이다. 

    $$ 3 \times 4 = 4 + 4 + 4 = 12 $$

- 곱셈(Multiplication) 의 결과를 product 라 한다.

!!! tldr "수열의 곱셈(Product of a sequence)"

    수열 $x_i$ 의 곱셈은 다음과 같이 정의된다.

    $$ \prod_{i=m}^{n}x_i = x_m \cdot x _{m+1} \cdot x _{m+2} \cdot \dots \cdot x _{n-1} \cdot x_n $$

- 수열은 숫자, 함수, 벡터, 행렬, 다항식 등 임의의 타입의 수학적 대상들로 구성 될 수 있다. 

- 예시 

    $$ \prod_{i=1}^{4} i = 24 $$

## Properties of Multiplication

!!! tldr "Properties of Multiplication"

    실수체 또는 복소수체에서 곱셈에 대하여 다음이 성립한다.

    1. $x \cdot y = y \cdot x$ (Commutative property)

    2. $(x \cdot y) \cdot z = x \cdot (y \cdot z)$ (Associative property)

    3. $x \cdot (y + z) = x \cdot y + x \cdot z$ (Distributive property)

    4. $x \cdot 1 = x$ (Identity property)

    5. $x \cdot 0 = 0$ (Zero property)

    6. $(-x) + x = 0$ 인 $-x$ 에 대하여 $(-1) \cdot x = (-x)$ 이다. 또한 $(-1) \cdot (-1) = 1$ 이다. (Negation)

    7. $0$ 이 아닌 $x$ 에 대하여 $x \cdot \bigg (\dfrac{1}{x} \bigg ) = 1$ 인 $\dfrac{1}{x}$ 가 존재한다. (Inverse element)

!!! tldr "Associativity and Commutativity (1)"

    $$ \prod_{i=1}^{n}x_iy_i = \bigg (\prod_{i=1}^{n}x_i \bigg )\bigg (\prod_{i=1}^{n}y_i \bigg ) $$

- 증명

!!! tldr "Associativity and Commutativity (2)"

    $$ \bigg (\prod_{i=1}^{n}x_i \bigg ) ^{a} = \prod_{i=1}^{n}x_i ^{a} $$

- 증명

!!! tldr ""

    $$ a \in \N, x_i \in \R ^{+} : \prod_{i=1}^{n}x ^{a_i} = x ^{\sum_{i=1}^{n}a_i} $$

- 증명
