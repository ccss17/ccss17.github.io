!!! info

    [프리드버그 선형대수학](https://book.naver.com/bookdb/book_detail.nhn?bid=16374070) 를 공부하면서 노트정리 한 내용입니다.

# 벡터공간 

!!! tldr ""

    체(field) : 두 연산 $+, \cdot$ (덧셈, 곱셈)이 주어진 집합으로써 $\exists x, y \in \mathbb{F}$ 에 대하여 $x+y, x \cdot y$ 가 $\mathbb{F}$ 에 유일하게 존재하고, $\forall a,b,c \in \mathbb{F}$ 에 대하여 다음이 성립한다.

    - F1) 덧셈과 곱셈에 대한 교환법칙 : $a+b=b+a,a \cdot b = b \cdot a$

    - F2) 덧셈과 곱셈에 대한 결합법칙 : $(a+b)+c=a+(b+c),(a \cdot b) \cdot c = a \cdot (b \cdot c)$

    - F3) 덧셈과 곱셈에 대한 항등원 : $0 + a = a, 1 \cdot a = a$ 인 $0 \in \mathbb{F}$ 와 $1 \in \mathbb{F}$ 가 존재한다. 단 $1 \neq 0$ 이다.

    - F4) 덧셈과 곱셈에 대한 역원 : 각 $a \in \mathbb{F}$ 와 영이 아닌 $b \in \mathbb{F}$ 에 대하여 $a+c=0, b \cdot d = 1$ 인 $c \in \mathbb{F}$ 와 $d \in \mathbb{F}$ 가 존재한다

    - F5) 덧셈에 대한 곱셈의 분배법칙 : $a \cdot (b+c) = a \cdot b + a \cdot c$

- 체의 임의의 원소 $a$ 의 덧셈에 대한 역원과 곱셈에 대한 역원은 각각 

    $$ -a, a ^{-1} $$

    로 표기한다. 즉,

    $$ a + (-a) = 0, a \cdot a ^{-1} = 1 $$

    이다.

- 체는 쉽게 말해서 원소를 $0$ 으로 나누는 것을 제외하면 두 원소의 합, 차, 곱, 나눗셈이 주어진 집합의 원소가 되도록 정의된 집합이다.

    즉, 체는 합, 차, 곱, 나눗셈에 대하여 닫혀있도록 정의된 집합이다.

- 예시

    실수 집합 $\R$ 과 유리수 집합 $\mathbb{Q}$ 은 덧셈과 곱셈에 대한 체이다.

    자연수 집합 $\N$ 과 정수 집합 $\mathbb{Z}$ 은 덧셈과 곱셈에 대한 체가 아니다. F4) 가 성립하지 않기 때문이다.

- 예시 

    체 $Z_2$ 는 두 원소 $0, 1$ 를 가지며 덧셈과 곱셈을 다음과 같이 정의한다. 

    $$ 0+0=0, 0+1=1+0=1, 1+1=0 $$

    $$ 0 \cdot 0 = 0, 0 \cdot 1 = 1 \cdot 0 = 0, 1 \cdot 1 = 1 $$

!!! tldr ""

    소거법칙(Cancellation Laws) : 체의 임의의 원소 $a, b, c$ 에 대하여 다음이 성립한다. 

    $$ a+b= c+b \implies  a=c \tag{1}  $$

    $$ a \cdot b = c \cdot b \lor b \neq 0 \implies a=c \tag{2}  $$

- $(1)$ 의 증명 

    체의 성질 F4) 에 따르면 체의 원소는 덧셈에 대한 역원을 갖는다. $b$ 의 역원을 $d$ 라고 하면 $b+d=0$ 이므로 $a+b=c+b$ 의 양변에 $d$ 를 더한 좌변과 우변은

    $$ (a + b) + d = a + (b + d) = a $$

    $$ (c + b) + d = c + (b + d) = c $$

    이다. 그러므로 

    $$ \therefore a = c $$

    이다. 

- $(2)$ 의 증명 

    체의 성질 F4) 에 따르면 $b \neq 0$ 이면 $b \cdot d = 1$ 인 체의 원소 $d$ 가 존재한다. $a \cdot b = c \cdot d$ 의 양변에 $d$ 를 곱한 좌변과 우변은 

    $$ (a \cdot b) \cdot d = a \cdot (b \cdot d) = a \cdot 1 = a $$

    $$ (c \cdot b) \cdot d = c \cdot (b \cdot d) = c \cdot 1 = c $$

    이다. 그러므로 

    $$ \therefore a = c $$

    이다. 

- 소거법칙에 의하여 체의 성질 F3) 의 $0$ 과 $1$, F4) 의 $c$ 와 $d$ 가 유일하다. 

    - 증명 

        $\forall a \in \mathbb{F}$ 에 대하여 $0'+a=a$ 를 만족하는 $0' \in \mathbb{F}$ 가 존재한다면, $\forall a \in \mathbb{F}$ 에 대하여 $0+a=a$ 이므로 

        $$ \forall a \in \mathbb{F}, 0'+a=0+a $$

        인데, 소거법칙 $(1)$ 에 의하여 

        $$ \therefore 0' = 0 $$

        이다. 

!!! tldr ""

    임의의 체의 임의의 원소 $a, b$ 에 대하여 다음이 성립한다. 

    $$ a \cdot 0 = 0 \tag{1} $$

    $$ (-a) \cdot b = a \cdot (-b) = -(a \cdot b) \tag{2} $$

    $$ (-a) \cdot (-b) = a \cdot b \tag{3} $$

- $(1)$ 증명

    $0$ 은 덧셈의 항등원이므로 무엇을 더하든 그것 자체가 연산결과가 된다. 그러므로 

    $$ 0 + a \cdot 0 = a \cdot 0 $$

    에서 $0 + 0 = 0$ 와 체의 성질 F5) 분배법칙에 의하여 

    $$ = a \cdot (0 + 0) = a \cdot 0 + a \cdot 0 $$

    이다. 이때 소거법칙 $(1)$ 에 의하여 

    $$ 0 + a \cdot 0 = a \cdot 0 + a \cdot 0 \iff  0 = a \cdot 0 $$

    이다.

- $(2)$ 증명

    $-(a \cdot b)$ 는 정의에 의하여 $a \cdot b + \{-(a \cdot b)\} = 0$ 를 만족하는 유일한 체 $\mathbb{F}$ 의 원소이다. 그러므로 $(-a) \cdot b = -(a \cdot b)$ 를 보이기 위하여 

    $$ a \cdot b + (-a) \cdot b = 0 $$

    임을 보이면 된다. 그런데 체의 성질 F5) 분배법칙과 소거법칙 $(1)$ 에 의하여 

    $$ a \cdot b + (-a) \cdot b = \{a + (-a)\} \cdot b = 0 \cdot b = 0 $$

    이다. 따라서 증명이 끝났다.

- $(3)$ 증명 

    체의 기본 성질 $(2)$ 를 두 번 적용하면 

    $$ (-a) \cdot (-b) = - \{a \cdot (-b)\} = - \{-(a \cdot b)\} = a \cdot b $$

    이다. 

!!! tldr ""

    지표(characteristic) : 임의의 체 $\mathbb{F}$ 에서 $p = 0$ 인 가장 작은 자연수 $p$ 이다.

- 체에 $p = 0$ 인 자연수 $p$ 가 존재하지 않으면 그 체의 지표는 $0$ 이다. 

- 예시 

    $\mathbb{Z}_2$ 의 지표는 $2$ 이다. $1+1=0$ 이 성립하기 때문이다.
    
    $\R$ 의 지표는 $0$ 이다.

- 체 $\mathbb{F}$ 의 지표가 $p \neq 0$ 이면 

    $$ \forall x \in \mathbb{F}, x \cdot p = 0 $$

    이다. 

- 체의 지표가 $0$ 이 아니면(특히 지표가 $2$ 이면) 예상치 못한 일이 발생하기에 이 책이 소개하는 벡터공간에 대한 몇가지 정리는 지표가 $0$ 인 경우에만(또는 지표가 $2$ 가 아니면) 성립한다.

!!! tldr ""

    벡터공간(vector space) 또는 선형공간(linear space) : 체 $\mathbb{F}$ 에서의 벡터공간 $\mathbb{V}$ 는 다음 8가지 조건을 만족하는 두 연산(합과 스칼라곱)을 가지는 집합이다. 

    1. $\forall  x, y \in \mathbb{V}, x+y=y+x$ (덧셈의 교환법칙)

    2. $\forall  x, y, z \in \mathbb{V}, (x+y)+z=x+(y+z)$ (덧셈의 결합법칙)

    3. $\forall x \in \mathbb{V}$ 에 대하여 $x+0=x$ 인 $0 \in \mathbb{V}$ 이 존재한다. (덧셈의 항등원)

    4. $\forall  x \in \mathbb{V}$ 에 대하여 $x+y=0$ 인 $y \in \mathbb{V}$ 가 존재한다. (덧셈의 역원)

    5. $\forall  x \in \mathbb{V}$ 에 대하여 $1x=x$ 이다. (곱셈의 항등원)

    6. $\forall a, b, x \in \mathbb{V}$ 에 대하여 $(ab)x = a(bx)$ 이다. (곱셈의 결합법칙)

    7. $\forall a, x, y \in \mathbb{V}$ 에 대하여 $a(x+y)=ax+ay$ 이다. (덧셈과 곱셈의 분배법칙)

    7. $\forall a, b, x \in \mathbb{V}$ 에 대하여 $(x+y)a=ax+ay$ 이다. (덧셈과 곱셈의 분배법칙)

- 합이란 $\mathbb{V}$ 의 두 원소 $x,y$ 에 대하여 유일한 원소 $x+y \in \mathbb{V}$ 를 대응하는 연산이다.

- 스칼라 곱이란 체 $\mathbb{F}$ 의 원소 $a$ 와 벡터공간 $\mathbb{V}$ 의 원소 $x$ 마다 유일한 원소 $ax \in \mathbb{V}$ 를 대응하는 연산이다.

- 이때 체 $\mathbb{F}$ 의 원소를 스칼라, 벡터공간 $\mathbb{V}$ 의 원소를 벡터라고 한다. 

- 벡터공간은 체 $\mathbb{F}$ 를 기반으로 정의되므로 정확하게 "$\mathbb{F}-$벡터공간 $\mathbb{V}$" 라고 표기해야 하지만, 벡터공간을 다룰 때 체는 크게 중요하지 않은 요소라 보통 생략한다. 

- 일반적으로 체 $\mathbb{F}$ 는 $\R$ 또는 $\mathbb{C}$ 를 뜻하며, 특별한 언급이 없는한 체의 지표는 $0$ 이다.

- 벡터공간을 정의하기 위해서는 단순힌 집합과 원소(벡터)를 정의하는 게 아니라 두 연산(합과 스칼라 곱)까지 정확히 서술해야 한다.

- 예시 

    체 $\mathbb{F}$ 의 부분집합 $S$ 에 대하여 $\mathcal{F}(S,\mathbb{F})$ 는 $S \to \mathbb{F}$ 인 모든 함수의 집합이다. $\forall s \in S$ 에 대하여 $\mathcal{F}(S,\mathbb{F})$ 에서 $f(s)=g(s)$ 일 때 두 함수 $f, g$ 를 같다고 한다. 

    $$ f,g \in \mathcal{F}(S,\mathbb{F}), c \in \mathbb{F}, s \in S $$

    일 때 합과 스칼라 곱을 다음과 같이 정의하면 $\mathcal{F}(S,\mathbb{F})$ 는 벡터공간이다.

    $$ (f+g)(s) = f(s)+g(s), \qquad (cf)(s) = c[f(s)] $$

- 예시 

    다음과 같은 체 $\mathbb{F}$ 에서 계수를 가져온 두 다항식 $f, g$ 에 대하여

    $$ f(x) = a_n x ^{n} + a _{n-1}x ^{n-1} + \dots + a_1x + a_0 $$

    $$ g(x) = b_m x ^{m} + a _{m-1}x ^{m-1} + \dots + b_1x + b_0 $$

    $m \leq n$ 일 때 $b _{m+1} = b _{m+2} = \dots = b_n= 0$ 으로 두면 $g(x)$ 는 다음과 같다.

    $$ g(x) = b_n x ^{n} + a _{n-1}x ^{n-1} + \dots + b_1x + b_0 $$

    이때 두 다항식의 합과 스칼라곱을 다음과 같이 정의하면 $\mathbb{F}$ 에서 계수를 가져온 모든 다항식 집합은 벡터공간이다. 

    $$ f(x) + g(x) = (a_n+b_n) x ^{n} + (a _{n-1}+b _{n-1})x ^{n-1} + \dots+(a_1+b_1)x+(a_0+b_0) $$

    $$ cf(x) = ca_n x ^{n} + ca _{n-1}x ^{n-1} + \dots + ca_1x + ca_0 $$

    이 벡터공간을 $\mathbb{P}(F)$ 라고 표기한다. 

- 위 예시에서 보인 벡터공간 $\mathbb{P}(F)$ 와 다음 예제에서 보이는 벡터공간은 본질적으로 같다. 

- 예시 

    임의의 체 $\mathbb{F}$ 위에서 정의된 수열(sequence)은 $\N \to \mathbb{F}$ 인 함수이다. 보통 수열 $\sigma (n) = a_n$ 을 $(a_n)$ 으로 표기한다. 체 $\mathbb{F}$ 에서 정의된 모든 수열의 집합을 $\mathbb{V}$ 라고 하자. 두 수열 $(a_n),(b_n)$ 을 다음과 같이 합과 스칼라곱으로 정의하면,

    $$ (a_n)+(b_n)=(a_n+b_n), \qquad t(a_n) = (ta_n) $$

    $\mathbb{V}$ 는 벡터공간이다.

- 벡터공간과 체의 차이점

    내가 볼 때 벡터공간과 체는 거의 비슷한 대수구조인데, 왜 이렇게 구분하는지 궁금해서 [math stackexchange](https://math.stackexchange.com/questions/969720/what-is-the-main-difference-between-a-vector-space-and-a-field) 에서 찾아보았다. 

    1. 체 $\mathbb{F}$ 와 벡터공간 $\mathbb{V}$ 에 대하여 체 $\mathbb{F}$ 의 연산은 

        $$ + : \mathbb{F} \times \mathbb{F} \to \mathbb{F}, \quad \times : \mathbb{F} \times \mathbb{F} \to \mathbb{F} $$

        인데 반해 벡터공간 $\mathbb{V}$ 의 연산은 

        $$ + : \mathbb{V} \times \mathbb{V} \to \mathbb{V}, \quad \times : \mathbb{F} \times \mathbb{V} \to \mathbb{V} $$

        와 같이 정의된다.
    
    2. 체에서는 영이 아닌 원소 $c \in \mathbb{F}$ 에 대하여 곱셈의 역원 $c ^{-1} \in \mathbb{F}$ 이 존재하여 

        $$ c \times c ^{-1} = c ^{-1} \times c = 1 $$

        을 만족하는데, 벡터공간에서는 이러한 조건이 없다.
    
    그래서 임의의 체 $\mathbb{F}$ 는 자기 자신 위에서 벡터공간이다.

!!! tldr ""

    $n$순서쌍($n$-tuple) : $a_1, a_2, \dots, a_n$ 이 체 $\mathbb{F}$ 의 원소일때 
    
    $$(a_1, a_2, \dots, a_n)$$

    라는 수학적 대상을 체 $\mathbb{F}$ 의 $n$순서쌍이라 한다.

- 순서쌍을 구성하는 원소 $a_i$ 를 $n$순서쌍의 성분(entry 또는 component) 라고 한다.

- 체 $\mathbb{F}$ 의 두 $n$순서쌍 $(a_1, a_2, \dots, a_n)$ 과 $(b_1, b_2, \dots, b_n)$ 이 

    $$ \forall i \in \{1,2,\dots,n\} , a_i = b_i $$

    일 때 같다고 정의한다.

- 체 $\mathbb{F}$ 의 모든 $n$순서쌍 집합을 $\mathbb{F} ^{n}$ 이라 표기한다. 

    $$ u = (a_1, a_2, \dots, a_n) \in \mathbb{F} ^{n}, v = (b_1, b_2, \dots, b_n) \in \mathbb{F} ^{n}, c \in \mathbb{F} $$

    일 때 합과 스칼라 곱을 

    $$ u+v=(a_1+b_1,  a_2+b_2, \dots, a_n + b_n), cu = (ca_1, \dots, ca_n) $$

    로 정의하면 이 집합은 $\mathbb{F}-$벡터공간이다.

- 예시 

    $\R ^{3}$  은 벡터공간이다. 합과 스칼라곱이 

    $$ (3, -2, 0) + (-1, 1, 4) = (2, -1, 4) $$ 
    
    $$ -5(1, -2, 0) = (-5, 10, 0) $$

    로 정의되기 때문이다. 마찬가지로 $\mathbb{C} ^{2}$ 도 벡터공간이다. 합과 스칼라곱이 

    $$ (1+i, 2)+(2-3i,4i)=(3-2i, 2+4i) $$

    $$ i(1+i,2) = (-1+i, 2i) $$

    로 정의되기 때문이다. 

!!! tldr ""

    행벡터(row vector) : 체 $\mathbb{F}$ 에 대한 $\mathbb{F} ^{n}$ 의 벡터 

    $$ \begin{pmatrix} a_1& a_2& \dots& a_n \end{pmatrix} $$ 

    이다. 

!!! tldr ""

    열벡터(column vector) : 체 $\mathbb{F}$ 에 대한 $\mathbb{F} ^{n}$ 의 벡터 

    $$ \begin{pmatrix} a_1\\a_2\\\vdots\\a_n \end{pmatrix} $$ 

    이다. 

- 보통 $\mathbb{F} ^{n}$ 의 벡터를 행벡터보다 이러한 열벡터로 표현한다. 

!!! tldr ""

    행렬(matrix) : 체 $\mathbb{F}$ 의 성분을 가져온 $m \times n$ 행렬은 $\forall a _{ij} \in \mathbb{F} (i \leq i \leq m, 1 \leq j \leq n)$ 에 대한 수학적 대상

    $$ \begin{pmatrix} a _{11}& a _{12}& \dots& a _{1n}\\ a _{21}& a _{22}& \dots& a _{2n}\\ \vdots& \vdots& \ddots& \vdots \\ a _{m1}& a _{m2}& \dots& a _{mn} \end{pmatrix} $$

    이다.

- 성분 $a _{i1}, a _{i2}, \dots, a _{in}$ 은 행렬의 $i$번째 행(row), 성분 $a _{1j}, a _{2j}, \dots, a _{mj}$ 은 행렬의 $j$번째 열(column) 이라고 한다.

- 행렬의 각 행을 $\mathbb{F} ^{n}$ 의 벡터로, 각 열을 $\mathbb{F} ^{m}$ 의 벡터로 나타낼 수 있다.

- 모든 성분 $a _{ij}$ 는 $\mathbb{F}$ 의 원소이다. 

- $i=j$ 인 성분 $a _{ij}$ 는 행렬의 대각성분(diagonal entry) 이다.

- 모든 성분이 $0$ 인 $m \times n$ 행렬을 영행렬(zero matrix) 라고 하고 $O$ 라고 표기한다.

- 행렬 $A$ 의 $i$ 행 $j$ 열 성분을 $A _{ij}$ 라고 표기한다. 

- 행의 개수와 열의 개수가 같은 행렬을 정사각행렬(square matrix) 라 한다.

- 행렬 $A, B$ 의 각 성분이 모두 일치할 때 행렬이 같다고 한다고.

- 체 $\mathbb{F}$ 의 원소를 성분으로 갖는 모든 $m \times n$ 행렬의 집합을 $\mathbb{M} _{m \times n}(\mathbb{F})$ 라 표기한다.

    $A, B \in \mathbb{M} _{m \times n}(\mathbb{F}), c \in \mathbb{F}$ 에 대하여 합과 스칼라 곱을 다음과 같이 정의하면 $\mathbb{M} _{m \times n}(\mathbb{F})$ 은 벡터공간이다.

    $$ (A+B) _{ij} = A _{ij}+ B _{ij}, \qquad (cA) _{ij} c A _{ij} $$

    - 예시 

        다음은 $\mathbb{M} _{2 \times 3}(\R)$ 의 합과 스칼라곱의 예시이다.

        $$ \begin{pmatrix} 2&0&-1\\ 1&-1&4 \end{pmatrix}+ \begin{pmatrix} -5&-2&6\\ 3&4&-1 \end{pmatrix}= \begin{pmatrix} -3&-2&5\\ 4&1&3 \end{pmatrix} $$

        $$ -3 \begin{pmatrix} 1&0&-2\\ -3&2&3 \end{pmatrix} = \begin{pmatrix} -3&0&6\\ 9&-6&-9 \end{pmatrix} $$

- 행렬의 합과 스칼라 곱 연산은 체 $\mathbb{F} ^{n}, \mathbb{F} ^{m}$ 에서 정의한 연산이 확장된 것이다. 

!!! tldr ""

    벡터 합의 소거법칙 : 벡터 공간 $\mathbb{V}$ 에 대하여 
    
    $$x,y,z \in \mathbb{V}, x + z = y + z \implies x = y$$

    이다. 

- 증명 

    벡터공간의 성질 4) 에 의하여 $z + v = 0$ 인 벡터 $v \in \mathbb{V}$ 가 존재한다. 이때 벡터공간의 성질 2), 3) 에 의하여 

    $$ x = x + 0 = x + (z + v) = (x + z) + v $$

    $$ = (y + z) + v = y + (z + v) = y + 0 = y $$

    이다. ■ 

!!! tldr ""

    영벡터(zero vector) : 벡터공간 $\mathbb{V}$ 의 임의의 원소 $\forall x \in \mathbb{V}$ 에 대하여 벡터공간의 성질 3) 

    $$ x + 0 = x $$
    
    을 만족하는 벡터 $0$ 을 영벡터라고 한다.

- 영벡터는 유일하다. 

    - 증명 

        체 $\mathbb{F}$ 위의 벡터공간 $\mathbb{V}$ 에서 영벡터 $0, 0'$ 가 존재한다고 가정하자. 그러면 $v \in \mathbb{V}$ 에 대하여

        $$ v + 0 = v = v + 0' \iff v + 0 = v + 0' $$

        인데, 정리 "벡터 합의 소거법칙 : 벡터 공간 $\mathbb{V}$ 에 대하여 $x,y,z \in \mathbb{V}, x + z = y + z \implies x = y$ 이다." 에 의하여 

        $$ \therefore  0 = 0' $$

        이다. ■ 

!!! tldr ""

    덧셈에 대한 역벡터(additive inverse) : 벡터공간 $\mathbb{V}$ 에 대한 $\forall x \in \mathbb{V}$ 에 대하여 벡터공간의 성질 4) 

    $$ x + y = 0 $$
    
    을 만족하는 벡터 $y$ 를 덧셈에 대한 역벡터 $-x$ 라고 한다.

- 벡터공간 $\mathbb{V}$ 의 원소 $x \in \mathbb{V}$ 에 대한 덧셈에 대한 역벡터는 $-$ 를 붙여서 $-x$ 로 표기한다.

- 덧셈에 대한 역벡터는 유일하다. 

    - 증명 

        벡터공간 $\mathbb{V}$ 의 원소 $x \in \mathbb{V}$ 의 덧셈에 대한 역벡터 $y, y'$ 가 있다면 

        $$ x + y = 0 = x + y' \iff x + y = x + y' $$

        인데, 정리 "벡터 합의 소거법칙 : 벡터 공간 $\mathbb{V}$ 에 대하여 $x,y,z \in \mathbb{V}, x + z = y + z \implies x = y$ 이다." 에 의하여 

        $$ \therefore  y = y' $$

        이다. ■ 

!!! tldr ""

    체 $\mathbb{F}$ 위의 임의의 벡터공간 $\mathbb{V}$ 에 대하여 다음이 성립한다. 

    1. $\forall x \in \mathbb{V}, 0x = 0$

    2. $\forall a \in \mathbb{F}, \forall x \in \mathbb{V}, (-a)x = -(ax) = a(-x)$

    3. $\forall a \in \mathbb{F}, a0 = 0$

- 증명 

    $0x + 0x = (0 + 0)x = 0x = 0x + 0 = 0 + 0x$ 인데 정리 "벡터 합의 소거법칙 : 벡터 공간 $\mathbb{V}$ 에 대하여 $x,y,z \in \mathbb{V}, x + z = y + z \implies x = y$ 이다." 에 의하여 $0x = 0$ 이다. ▲ 

    벡터 $-(ax)$ 는 $ax + \{-(ax)\} = 0$ 인 유일한 벡터인데 $ax + (-a)x = 0$ 이면 덧셈에 대한 역벡터는 유일하므로 $(-a)x = -(ax)$ 이다.

    $ax+(-ax) = \{a+(-a)\}x = 0x = 0$ 이므로 $(-ax) = -(ax)$ 이다. 특히 $(-1)x=-x$ 이다. 이제 

    $$ a(-x) = a \{(-1)x\} = \{a(-1)x\} = (-a)x $$

    이다. ▲ 

    3) 의 증명은 2) 와 비슷하다. ■ 

# 부분공간 

!!! tldr ""

    부분공간(subspace) : $\mathbb{F}$-벡터공간 $\mathbb{V}$ 의 부분집합 $\mathbb{W}$ 가 $\mathbb{V}$ 에서 정의한 합과 스칼라 곱을 가진 $\mathbb{F}$-벡터공간일 때 $\mathbb{W}$ 를 $\mathbb{V}$ 의 부분공간이라 한다.

- 대수학의 주요 관심사는 어떤 집합의 부분집합이 서로 대수적 구조가 같은지 연구하는 것이다. 

- 임의의 벡터공간 $\mathbb{V}$ 에 대하여 $\{0\}$ 은 부분공간이다. 특이 $\{0\}$ 은 점공간인 부분공간(zero subspace)이다.

- 벡터공간의 부분집합이 부분공간인지 확인하기 위해서 다음 성질만 확인하면 된다. 왜냐하면 벡터공간의 조건 1), 2), 5), 6), 7), 8) 은 자명하게 부분집합에서도 성립하기 때문이다. 

    1. $\forall x \in \mathbb{W}, y \in \mathbb{W}, x + y \in \mathbb{W}$

    2. $\forall c \in \mathbb{F}, x \in \mathbb{W}, cx \in \mathbb{W}$

    3. $0 \in \mathbb{W}$ ($\mathbb{W}$ 는 영벡터를 포함한다.)

    4. $\mathbb{W}$ 에 속한 모든 벡터의 덧셈에 대한 역벡터는 $\mathbb{W}$ 의 원소이다. 

- 다음 정리에 따르면 $\mathbb{W}$ 의 영벡터와 $\mathbb{V}$ 의 영벡터는 같다. 따라서 4) 는 확인할 필요 없다. 

!!! tldr ""

    부분공간의 조건 : 벡터공간 $\mathbb{V}$ 와 부분집합 $\mathbb{W}$ 에 대하여 $\mathbb{W}$ 가 다음 조건을 만족하면 부분공간이다.

    1. $0 \in \mathbb{W}$

    2. $\forall x \in \mathbb{W}, y \in \mathbb{W}, x + y \in \mathbb{W}$

    3. $\forall c \in \mathbb{F}, x \in \mathbb{W}, cx \in \mathbb{W}$

- 이때 조건 1), 2), 3) 의 연산은 $\mathbb{V}$ 에서 정의된 것과 같다.

- 증명 

    $\mathbb{W}$ 가 $\mathbb{V}$ 의 부분공간이면 $\mathbb{W}$ 는 $\mathbb{V}$ 의 합과 스칼라곱을 상속하므로 2), 3) 이 성립한다. $\mathbb{W}$ 의 영벡터를 $0'$ 라 하면 $x \in \mathbb{W}$ 에 대하여 $x + 0' = x$ 인데, $x \in \mathbb{V}$ 이므로 $x + 0 = x$ 이다. 따라서 $0 = 0'$ 이다. ▲ 

    역으로 1), 2), 3) 이 성립한다고 하자. 그러면 "d) $\mathbb{W}$ 에 속한 모든 벡터의 덧셈에 대한 역벡터는 $\mathbb{W}$ 의 원소이다." 만 확인하면 된다. 먼저 3) 에 의하여 $x \in \mathbb{W} \implies (-1) x \in \mathbb{W}$ 이고 $-x = (-1)x$ 이므로 $-w \in \mathbb{W}$ 이다. 그러므로 $\mathbb{W}$ 는 $\mathbb{V}$ 의 부분공간이다. ■ 

- 즉, 1), 2), 3) 으로부터 "d) $\mathbb{W}$ 에 속한 모든 벡터의 덧셈에 대한 역벡터는 $\mathbb{W}$ 의 원소이다." 가 도출되므로 이것을 확인할 필요 없다는 것이다.

- 예시 

    다음과 같은 체 $\mathbb{F}$ 에서 계수를 가져온 두 다항식 $f, g$ 에 대하여

    $$ f(x) = a_n x ^{n} + a _{n-1}x ^{n-1} + \dots + a_1x + a_0 $$

    $$ g(x) = b_n x ^{n} + a _{n-1}x ^{n-1} + \dots + b_1x + b_0 $$

    두 다항식의 합과 스칼라곱을 

    $$ f(x) + g(x) = (a_n+b_n) x ^{n} + (a _{n-1}+b _{n-1})x ^{n-1} + \dots+(a_1+b_1)x+(a_0+b_0) $$

    $$ cf(x) = ca_n x ^{n} + ca _{n-1}x ^{n-1} + \dots + ca_1x + ca_0 $$

    와 같이 정의하면 $\mathbb{F}$ 에서 계수를 가져온 모든 다항식 집합은 벡터공간인데, 이 벡터공간을 $\mathbb{P}(F)$ 라고 표기하자. 

    이때 체 $\mathbb{F}$ 에서 계수를 가져온 모든 다항식 집합 $\mathbb{P}(\mathbb{F} )$ 에 대하여 $\mathbb{P}_n(\mathbb{F} )$ 를 $n$ 이하의 차수를 가진 다항식 집합이라 하면, 부분공간이 됨을 보이자.

    먼저 영 다항식의 차수는 $-1$ 이므로 $\mathbb{P} _n(\mathbb{F} )$ 에 속한다. ▲ 차수가 $n$ 이하인 두 다항식을 더하면 차수가 $n$ 이하이다. ▲ 차수가 $n$ 이하인 두 다항식을 곱해도 차수가 $n$ 이하이다. ■ 

!!! tldr ""

    전치행렬(transpose matrix) : $m \times n$ 행렬 $A$ 에 대한 전치행렬 $A ^{\operatorname{T} }$ 는 $A$ 의 행과 열을 바꾸어 얻은 $n \times m$ 행렬 $(A ^{\operatorname{T} }) _{ij} = A _{ji}$ 이다. 

- 예시 

    $$ \begin{pmatrix} 1 & -2 &3\\ 0 & 5 &-1 \end{pmatrix} ^{\operatorname{T} } = \begin{pmatrix} 1 & 0\\ -2 & 5\\ 3 & -1\\ \end{pmatrix} $$

!!! tldr ""

    대칭행렬(symmetric matrix) : $A ^{\operatorname{T} } = A$ 인 행렬이다.

- 대칭행렬은 정사각행렬이다.

- 예시 

    $$ \begin{pmatrix} 1 & 2\\ 2 & 3 \end{pmatrix} = \begin{pmatrix} 1 & 2\\ 2 & 3 \end{pmatrix} $$

!!! tldr ""

    $\mathbb{M} _{n \times n}(\mathbb{F} )$ 의 모든 대칭행렬의 집합 $\mathbb{W}$ 은 부분공간이다.

- 증명  

    먼저 영행렬의 전치행렬은 영행렬이다. ▲  행렬 $A, B$ 와 스칼라 $a, b$ 에 대하여 $(aA + bB) ^{\operatorname{T} } = aA ^{\operatorname{T} } + bB ^{\operatorname{T} }$ 을 생각하면 $A \in \mathbb{W} , B \in \mathbb{W} \implies (A + B) ^{\operatorname{T} } = A ^{\operatorname{T} } + B ^{\operatorname{T} } = A + B$ 이다. ▲  마지막으로 행렬 $A$ 와 스칼라 $a$ 에 대하여 $(aA) ^{\operatorname{T} } = a A ^{\operatorname{T} }$ 이므로 $A \in \mathbb{W} \implies (aA) ^{\operatorname{T} } = aA ^{\operatorname{T} } = aA$ 이다. ▲ 그러므로 부분공간의 조건 1), 2), 3) 을 만족하므로 $\mathbb{W}$ 은 부분공간이다. 

!!! tldr ""

    상삼각행렬, 위삼각행렬(upper triangular matrix) : $m \times n$ 행렬 $A$ 의 대각성분 아래의 모든 성분이 $0$ 인행렬이다.

- 즉, $i>j$ 에 대하여 $A _{ij} = 0$ 인 행렬이다.

- 예시 

    $$  \begin{pmatrix} 1 & 2 & 3 & 4\\ 0 & 5 & 3 & 4\\ 0 & 0 & 3 & 4\\ \end{pmatrix} $$

!!! tldr ""

    대각행렬(diagonal matrix) : 대각성분을 제외한 모든 성분이 $0$ 인 정사각행렬이다. 

- 즉, $i \neq j$ 에 대하여 $M _{ij} = 0$ 인 $n \times n$ 행렬 $M$ 이다.

- 예시 

    $$  \begin{pmatrix} 1 & 0 & 0 \\ 0 & 5 & 0 \\ 0 & 0 & 3 \\ \end{pmatrix} $$

- 예시 

    $n \times n$ 영행렬의 모든 성분은 $0$ 이므로 영행렬은 대각행렬이다. $n \times n$ 대각행렬 $A, B$ 는 $i \neq j$ 에 대하여 

    $$ (A+B) _{ij} = A _{ij} + B _{ij} = 0 + 0 = 0, \enspace (cA) _{ij} = c A _{ij} = c0=0 $$

    이므로 대각행렬의 집합은 $\mathbb{M} _{n \times n}(\mathbb{F} )$ 의 부분공간이다.

!!! tldr ""

    대각합(trace) : $n \times n$ 행렬 $M$ 의 대각합은 모든 대각성분의 합 

    $$ \text{tr}(M) = \sum_{k=1}^{n}M _{kk} $$

    이다.

- 대각합이 $0$ 인 $n \times n$ 행렬의 집합은 자명하게 $\mathbb{M} _{n \times n}(\mathbb{F} )$ 의 부분공간이다.

!!! tldr ""

    벡터공간 $V$ 의 임의의 교집합은 $V$ 의 부분공간이다. 

- 이 정리는 주어진 부분공간으로 새로운 부분공간을 만드는 방법을 제시해준다. 

- 증명 

    $\mathbb{V}$ 의 모든 부분공간을 원소로 갖는 집합족 $\mathcal{C}$ 에 대하여 $\mathbb{W} = \bigcap_{}^{}\mathcal{C}$ 를 생각하자. 영벡터는 모든 부분공간에 속하므로 $0 \in \mathbb{W}$ 이다. ▲  스칼라 $a$ 와 $x, y \in \mathbb{W}$ 에 대하여 $x, y$ 는 $\mathcal{C}$ 의 모든 부분공간에 속한다. 부분공간은 스칼라 곱과 합에 대하여 닫혀 있으므로 $x+y \in \mathbb{W} , ax \in \mathbb{W}$ 이다. ▲ 그러므로 $\mathbb{W}$ 는 $\mathbb{V}$ 의 부분공간이다. ■ 

# 일차결합과 연립일차방정식


