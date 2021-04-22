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

    벡터공간(vector space) 또는 선형공간(linear space) : 체 $\mathbb{F}$ 에서의 벡터공간 $\mathbb{V}$ 는 다음 8가지 조건을 만족하는 두 연산 합 $+ : \mathbb{V} \times \mathbb{V} \to \mathbb{V}$ 과 스칼라곱 $\times : \mathbb{F} \times \mathbb{V} \to \mathbb{V}$ 을 가지는 집합이다. 

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

    이 벡터공간을 $\mathbb{P}(\mathbb{F})$ 라고 표기한다. 

- 위 예시에서 보인 벡터공간 $\mathbb{P}(\mathbb{F})$ 와 다음 예제에서 보이는 벡터공간은 본질적으로 같다. 

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

    벡터(vector) : 벡터공간의 원소이다. 

- 벡터는 벡터공간의 원소로 정의되기 전에 기하학과 물리학에서 유래되었다. 그래서 종종 벡터를 벡터공간 없이 논의하기도 한다. 이 경우 보통 벡터를 힘, 속도, 가속도 같은 물리적 개념에서의 크기와 방향도 가지고 있는 물리량을 벡터로 표현한다. 이때 벡터를 화살표로 표현하는데, 화살표의 길이를 물리량의 크기로, 물리량의 방향을 화살표의 방향으로 표현한다.

    이는 벡터의 위치와 관계없이 크기와 방향이 같으면 같은 벡터로 다루겠다는 것이다.

- 한 지점에 두 물리량이 작용했을 때 그 합력을 계산할 때 두 물리량의 크기만 합한다고 끝이 아니다. 

    - 예시
    
        2마일의 속도의 강물을 1마일의 속도로 거슬러서 수영하는 사람의 속도는 3마일이 아니다. 반면 동일한 방향으로 수영한다면 3마일의 속도를 가지게 된다.

- 위 예시에서 보았듯 두 물리량의 합은 크기와 방향을 고려해야 한다. 두 물리량의 결합은 벡터의 합으로 설명할 수 있는데 이를 다음과 같은 평행사변형의 법칙으로 표현한다.

    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Vector_addition.svg/375px-Vector_addition.svg.png)

    위와 같이 벡터 합은 두 벡터로 이루어진 평행사변형의 대각선으로 나타낸다. 벡터의 스칼라곱도 정의할 수 있는데 이는 다음과 같이 벡터의 확대와 축소를 하는 연산이다.

    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Scalar_multiplication_of_vectors2.svg/375px-Scalar_multiplication_of_vectors2.svg.png)

- 벡터의 시작점을 시점이라 하고 끝점을 종점이라 하는데, 벡터의 위치는 관계가 없으므로 $2$ 차원 평면에서 모든 벡터의 시점을 $(0, 0)$ 로 고정하면 임의의 벡터를 좌표 $(a_1, a_2)$ 로 나타낼 수 있다. 

    그러면 두 벡터 $(a_1, a_2), (b_1, b_2)$ 의 합은 $(a_1 + b_1, a_2 + b_2)$ 로 표현할 수 있고, $t$ 에 대한 스칼라곱은 $(ta_1, ta_2)$ 로 표현할 수 있다. 2차원 평면에서와 비슷하게 3차원 공간에서도 벡터 합과 스칼라 곱을 정의할 수 있다.

!!! tldr ""

    벡터로 표현하는 직선의 방정식 : 두 점 $A, B$ 를 지나는 직선의 방정식은 시점이 $O$ 이고 종점이 각각 $A, B$ 인 두 벡터 $u, v$ 에 대하여 

    $$ \forall t \in \R, x = u + t(v - u) $$

    이다.

- 공간에서 두 점 $A, B$ 를 지나는 직선이 있을 때 이 공간에 좌표를 부여하여 $A = (a_1, a_2), B = (b_1, b_2)$ 라고 하고 원점을 $O = (0, 0)$ 라고 표현하자. 이때 시점이 $O$ 이고 종점이 각각 $A, B$ 인 두 벡터 $u = (a_1, a_2), v = (b_1, b_2)$ 를 생각할 수 있다. 

    또한 시점이 $A$ 이고 종점이 $B$ 인 벡터를 $w$ 라고 했을 때 $w$ 의 시점을 원점 $O$ 로 옮기면 $w = (b_1 - a_1, b_2 - a_2)$ 가 되므로 

    $$ u + w = v, \enspace w = v - u $$

    가 성립한다. 이때 $-u$ 는 $-1$ 에 대한 스칼라곱 벡터 $(-1)u$ 를 의미한다.

    ![image](https://user-images.githubusercontent.com/16812446/113727560-32b6d780-9730-11eb-92c8-c3d69dd3c680.png)

    이때 두 점 $A, B$ 를 지나는 직선은 $A$ 를 시점으로 하는 벡터와 임의의 스칼라 $t$ 에 대한 스칼라곱 $tw$ 으로 표현할 수 있다. 역으로 $A$ 를 시점으로 하는 벡터 $tw$ 의 종점은 두 점 $A, B$ 를 지나는 직선 위의 점이다. 그러므로 두 점 $A, B$ 를 지나는 직선의 방정식을 

    $$ \forall  t \in \R, x = u + tw = u + t(v - u) $$

    로 표현할 수 있다. 이때 $x$ 는 직선 위의 임의의 점이다.

- 예시 

    3차원 공간좌표에서도 동일하게 성립하는데, 두 점 $A(-2, 0, 1), B(4, 5, 3)$ 에 대하여 $A$ 가 시점이고 $B$ 가 종점인 벡터 $C$ 는 $(6,5,2)$ 이므로 두 점 $A,B$ 를 지나는 직선의 방정식은 

    $$ \forall t \in \R, x = (-2, 0, 1) + t(6, 5, 2) $$

    이다.

!!! tldr ""

    벡터로 표현하는 공간의 방정식 : 공간의 세 점 $A, B, C$ 으로 형성되는 공간의 방정식은 시점이 $A$ 이고 종점이 $B, C$ 인 벡터 $u, v$ 에 대하여

    $$ \forall s, t \in \R, x = A + su + tv $$

    이다.

- 시점이 $A$ 이고 종점이 $B, C$ 인 두 벡터 $u, v$ 에 대하여 세 점 $A,B,C$ 로 이루어진 평면 위의 점 $S$ 는 $A$ 를 시점으로 하고 $s, t \in \R$ 에 대한 $su + tv$ 형태의 벡터의 종점이다. 다음 그림을 보자.

    ![image](https://user-images.githubusercontent.com/16812446/113730362-cab5c080-9732-11eb-994c-0497b649eb5a.png)

    따라서 $\forall s, t \in \R$ 에 대하여 벡터 $su + tv$ 는 세 점 $A, B, C$ 으로 형성되는 평면의 한 점이다. 따라서 평면의 방정식을 

    $$ \forall s, t \in \R, x = A + su + tv $$

    와 같이 표현할 수 있다. $x$ 는 평면 위의 점을 뜻한다. 종점 $su+tv$ 의 좌표에 시점 $A$ 을 더한 좌표가 $x$ 가 되는 것이다.

- 특히 $A$ 가 원점이면 평면의 방정식을 더욱 간단하게 

    $$ \forall s, t \in \R, x = su + tv $$

    로 표현할 수 있다.

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

!!! tldr "정리 1.1"

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

!!! tldr "정리 1.2"

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

- 임의의 벡터공간 $\mathbb{V}$ 에 대하여 $\{0\}$ 은 부분공간이다. 특히 $\{0\}$ 은 점공간(zero vector space)인 부분공간(zero subspace)이다.

- 벡터공간의 부분집합이 부분공간인지 확인하기 위해서 다음 성질만 확인하면 된다. 왜냐하면 벡터공간의 조건 1), 2), 5), 6), 7), 8) 은 자명하게 부분집합에서도 성립하기 때문이다. 

    1. $\forall x \in \mathbb{W}, y \in \mathbb{W}, x + y \in \mathbb{W}$

    2. $\forall c \in \mathbb{F}, x \in \mathbb{W}, cx \in \mathbb{W}$

    3. $0 \in \mathbb{W}$ ($\mathbb{W}$ 는 영벡터를 포함한다.)

    4. $\mathbb{W}$ 에 속한 모든 벡터의 덧셈에 대한 역벡터는 $\mathbb{W}$ 의 원소이다. 

- 다음 정리에 따르면 $\mathbb{W}$ 의 영벡터와 $\mathbb{V}$ 의 영벡터는 같다. 따라서 4) 는 확인할 필요 없다. 

!!! tldr "정리 1.3"

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

    와 같이 정의하면 $\mathbb{F}$ 에서 계수를 가져온 모든 다항식 집합은 벡터공간인데, 이 벡터공간을 $\mathbb{P}(\mathbb{F})$ 라고 표기하자. 

    이때 체 $\mathbb{F}$ 에서 계수를 가져온 모든 다항식 집합 $\mathbb{P}(\mathbb{F} )$ 에 대하여 $\mathbb{P}_n(\mathbb{F} )$ 를 $n$ 이하의 차수를 가진 다항식 집합이라 하면, 부분공간이 됨을 보이자.

    먼저 영 다항식의 차수는 $-1$ 이므로 $\mathbb{P} _n(\mathbb{F} )$ 에 속한다. ▲ 차수가 $n$ 이하인 두 다항식을 더하면 차수가 $n$ 이하이다. ▲ 차수가 $n$ 이하인 두 다항식을 곱해도 차수가 $n$ 이하이다. ■ 

- 예시 

    원점과 두 점을 지나는 평면의 방정식은

    $$ \forall s, t \in \R, x = su + tv $$

    로 표현할 수 있는데, 집합 $\mathbb{W} = \{x = su + tv \in \R ^{3} : s, t \in \R \}$ 은 $\R ^{3}$ 의 부분공간이다. $\exists s, t \in \R \text{ s.t. }  x = su + tv = (0, 0, 0)$ 이므로 $0 \in \mathbb{W}$ 이고, $x_1, x_2 \in \mathbb{W}$ 에 대하여 $x_1 + x_2 \in \mathbb{W}$ 이고, $t \in \R$ 에 대하여 $tx_1 \in \mathbb{W}$ 이기 때문이다. 

    - 벡터 $u, v$ 와 스칼라 $s, t$ 에 대한 표현 $su+tv$ 는 벡터공간을 다룰 때 중요하다.

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

!!! tldr "정리 1.4"

    벡터공간 $V$ 의 임의의 교집합은 $V$ 의 부분공간이다. 

- 이 정리는 주어진 부분공간으로 새로운 부분공간을 만드는 방법을 제시해준다. 

- 증명 

    $\mathbb{V}$ 의 모든 부분공간을 원소로 갖는 집합족 $\mathcal{C}$ 에 대하여 $\mathbb{W} = \bigcap_{}^{}\mathcal{C}$ 를 생각하자. 영벡터는 모든 부분공간에 속하므로 $0 \in \mathbb{W}$ 이다. ▲  스칼라 $a$ 와 $x, y \in \mathbb{W}$ 에 대하여 $x, y$ 는 $\mathcal{C}$ 의 모든 부분공간에 속한다. 부분공간은 스칼라 곱과 합에 대하여 닫혀 있으므로 $x+y \in \mathbb{W} , ax \in \mathbb{W}$ 이다. ▲ 그러므로 $\mathbb{W}$ 는 $\mathbb{V}$ 의 부분공간이다. ■ 

    - $\mathbb{W} = \bigcup_{}^{}\mathcal{C}$ 가 부분공간이 된다는 보장은 없다. 영벡터를 포함하고, 스칼라곱에 대하여 닫혀있음은 쉽게 보일 수 있지만 합에 대하여 닫혀있다고 보장할 수 없기 때문이다. $\mathbb{V}$ 의 두 부분공간의 합집합이 부분공간이 되기 위한 필요충분조건은 한 부분공간이 다른 부분공간을 포함하고 있다는 것이다.

# 일차결합과 연립일차방정식

!!! tldr ""

    일차결합(linear combination) : 벡터공간 $\mathbb{V}$ 의 공집합이 아닌 부분집합 $S$ 에 대한 유한개의 벡터 $u_1, u_2, \dots, u_n \in S$ 와 스칼라 $a_1, a_2, \dots, a_n$ 에 대하여 벡터

    $$ v = a_1u_1 + a_2u_2 + \dots + a_nu_n \in \mathbb{V} $$

    를 $S$ 의 일차결합이라 한다.

- $v$ 를 벡터 $u_1, u_2, \dots, u_n$ 의 일차결합이라 하고, $a_1, a_2, \dots, a_n$ 를 이 일차결합의 계수(coefficient) 라 한다.

- 임의의 벡터공간 $\mathbb{V}$ 와 임의의 벡터 $v \in \mathbb{V}$ 에 대하여 $0v=0$ 이므로 영벡터는 공집합이 아닌 모든 부분집합의 일차결합이다. 

> p43 연립방정식의 성질 pass 

!!! tldr ""

    생성공간(span) : 벡터공가 $\mathbb{V}$ 의 공집합이 아닌 부분집합 $S$ 에 대하여 $S$ 의 벡터로 만든 모든 일차결합의 집합을 생성공간 $\text{span}(S)$ 라 표기한다.

- $\text{span}(\varnothing ) = \{0\}$ 으로 정의한다. 이 $0$ 은 영벡터를 뜻한다.

- 예시 

    $\R ^{3}$ 의 원소로 이루어진 집합 $A = \{(1,0,0), (0,1,0)\}$ 의 생성공간은 

    $$ \forall a, b \in \R,  a(1,0,0) + b(0, 1, 0) = (a, b, 0)$$

    형태의 집합 $\text{span}(A) = \{(a, b, 0) \in \R ^{3} : a, b \in \R \}$ 이다. 이 생성공간 $\text{span}(A)$ 는 $xy$평면이고 $\R ^{3}$ 의 부분공간이다.

!!! tldr "정리 1.5"

    벡터공간 $\mathbb{V}$ 의 임의의 부분집합 $S$ 의 생성공간 $\text{span}(S)$ 는 $S$ 를 포함하는 $\mathbb{V}$ 의 부분공간이다.
    
    $S$ 를 포함하는 $\mathbb{V}$ 의 부분공간은 $\text{span}(S)$ 을 포함한다.

- 첫번째 명제의 증명 

    $S = \varnothing$ 이면 $\text{span}(\varnothing ) = \{0\}$ 인데, $S = \varnothing \in \{0\}$ 이고 $\{0\}$ 는 $\mathbb{V}$ 의 모든 부분공간에 포함된다. ▲ 

    $S \neq \varnothing$ 이면 $z \in S$ 에 대하여 $0z = 0 \in \text{span}(S)$ 이다. $x, y \in \text{span}(S)$ 이면 벡터 $u_1, u_2, \dots, u_m \in S$ 와 스칼라 $a_1, a_2, \dots,a_m \in \R$ 이 존재하여 

    $$ x = a_1u_1 + a_2u_2 + \dots + a_mu_m $$

    을 만족하고 벡터 $v_1, v_2, \dots, v_n \in S$ 와 스칼라 $b_1, b_2, \dots,b_n \in \R$ 이 존재하여 

    $$ y = b_1v_1 + b_2v_2 + \dots + b_nv_n $$

    을 만족한다. 그러므로 

    $$ x + y = a_1u_1 + a_2u_2 + \dots + a_mu_m  + b_1v_1 + b_2v_2 + \dots + b_nv_n \in \text{span}(S)$$

    이고, 스칼라 $c$ 에 대하여

    $$ cx = ca_1u_1 + ca_2u_2 + \dots + ca_mu_m \in \text{span}(S) $$

    이므로 $\text{span}(S)$ 는 $\mathbb{V}$ 의 부분공간이다. 이때 $v \in S \implies v = 1 \cdot v \in \text{span}(S)$ 이므로 $S \subset \text{span}(S)$ 이다. ■ 

- 두번째 명제의 증명 

    가정에 의하여 $\mathbb{V}$ 의 부분공간 $\mathbb{W}$ 가 $S$ 를 포함한다. $w \in \text{span}(S)$ 이면 벡터 $w_1, w_2, \dots, w_n \in S$ 와 스칼라 $c_1, c_2, \dots,c_n \in \R$ 이 존재하여 

    $$ w = c_1w_1 + c_2w_2 + \dots + c_nw_n $$

    를 만족한다. 이때 가정에 의하여 $S \subset \mathbb{W}$ 이므로 $w_1, w_2, \dots, w_n \in \mathbb{W}$ 이다. 그런데 $w_1, w_2, \dots, w_n \in \mathbb{W}$ 들은 벡터공간의 원소이므로 

    $$ w = c_1w_1 + c_2w_2 + \dots + c_nw_n $$

    는 자명하게 $w \in \mathbb{W}$ 이다. $w$ 는 $\text{span}(S)$ 의 임의의 원소이므로 

    $$ \therefore \text{span}(S) \subset \mathbb{W} $$

    이다. ■ 

!!! tldr ""

    벡터공간을 생성하는 집합 : 벡터공간 $\mathbb{V}$ 의 부분집합 $S$ 에 대하여 $\text{span}(S)=\mathbb{V}$ 이면 $S$ 는 $\mathbb{V}$ 를 생성한다.

- 이것을 $S$ 의 벡터가 $\mathbb{V}$ 를 생성한다고 하기도 한다.

- 예시 

    $S = \{(1, 1, 0), (1, 0, 1), (0, 1, 1)\}$ 은 $\R ^{3}$ 을 생성한다. 다른 말로 세 벡터 $(1, 1, 0), (1, 0, 1), (0, 1, 1)$ 는 $\R ^{3}$ 을 생성한다. 즉, $\R ^{3}$ 의 임의의 벡터 $(r_1, r_2, r_3)$ 는 이 세 벡터의 일차결합이다. 이는 

    $$ r(1, 1, 0) + s(1, 0, 1) + t(0, 1, 1) = (r_1, r_2, r_3) $$

    을 만족하는 스칼라 $r,s,t$ 를 찾는 것으로 보일 수 있다. 그러면 $r = \dfrac{1}{2}(a_1+a_2-a_3, s = \dfrac{1}{2}(a_1-a_2+a_3), t = \dfrac{1}{2}(-a_1+a_2+a_3)$ 이다.

- 예시 

    세 다항식 $x ^{2} + 3x-2, 2x ^{2} + 5x-3, - x ^{2}-4x+4$ 는 $\mathbb{P} _2(\R)$ 을 생성한다. 임의의 다항식 $ax ^{2} + bx + c \in \mathbb{P} _2(\R)$ 은 다음과 같이 세 다항식의 일차결합이기 때문이다.

    $$ (-8a+5b+3c)(x ^{2}+3x-2) + (4a-2b-c)(2x ^{2} +5x-3) + (-a+b+c)(-x ^{2}-4x+4) = ax ^{2} + bx + c $$

- 예시 

    네 행렬 

    $$ \begin{pmatrix} 1&1\\ 1&0\\ \end{pmatrix}, \begin{pmatrix} 1&1\\ 0&1\\ \end{pmatrix}, \begin{pmatrix} 1&0\\ 1&1\\ \end{pmatrix}, \begin{pmatrix} 0&1\\ 1&1\\ \end{pmatrix} $$

    은 $\mathbb{M} _{2 \times 2}(\R)$ 을 생성한다. 즉, 임의의 행렬 $A \in \mathbb{M} _{2 \times 2}(\R)$ 은 다음과 같이 네 행렬의 일차 결합이다. 

    $$ \begin{pmatrix} a _{11}&a _{12}\\ a _{21}&a _{22}\\ \end{pmatrix} = \bigg (\dfrac{1}{3}a _{11} + \dfrac{1}{3}a _{12} + \dfrac{1}{3}a _{21} - \dfrac{2}{3}a _{22}\bigg ) \begin{pmatrix} 1&1\\ 1&0\\ \end{pmatrix}+ \bigg (\dfrac{1}{3}a _{11} + \dfrac{1}{3}a _{12} - \dfrac{2}{3}a _{21} + \dfrac{1}{3}a _{22}\bigg ) \begin{pmatrix} 1&1\\ 0&1\\ \end{pmatrix}+ $$

    $$ \bigg (\dfrac{1}{3}a _{11} - \dfrac{2}{3}a _{12} + \dfrac{1}{3}a _{21} + \dfrac{1}{3}a _{22}\bigg ) \begin{pmatrix} 1&0\\ 1&1\\ \end{pmatrix}+ \bigg (-\dfrac{2}{3}a _{11} + \dfrac{1}{3}a _{12} + \dfrac{1}{3}a _{21} + \dfrac{1}{3}a _{22}\bigg ) \begin{pmatrix} 0&1\\ 1&1\\ \end{pmatrix} $$

# 일차종속과 일차독립

!!! tldr ""

    영벡터의 자명한 표현(trivial representation of $0$) : 임의의 벡터 $u_1, u_2, \dots, u_n$ 에 대하여 $a_1 = a_2 = \dots = a_n = 0$ 이면 $a_1u_1 + a_2u_2 + \dots + a_nu_n = 0$ 인데 이것은 너무 자명하므로 영벡터의 자명한 표현이라 한다.

!!! tldr ""

    일차종속(linearly dependent) : 벡터공간 $\mathbb{V}$ 의 부분집합 $S$ 에 대하여 $a_1u_1 + a_2u_2 + \dots + a_nu_n = 0$ 을 만족하는 임의의 서로 다른 벡터 $u_1, u_2, \dots, u_n \in S$ 와 적어도 하나는 $0$ 이 아닌 스칼라 $a_1, a_2, \dots, a_n$ 이 존재하면 집합 $S$ 를 일차종속이라 한다. 

- $S$ 의 벡터 또한 일차 종속이다. 

- 어떤 집합이 일차 종속이면 적절한 벡터를 택하여 영벡터를 표현하는 자명하지 않은 표현(nontrivial representation)이다.

- 무한체의 벡터공간 $\mathbb{V}$ 의 부분공간 $\mathbb{W}$ 에 대하여 $\mathbb{W}$ 를 생성하는 유한 부분집합 $S$ 가 존재한다. 이때 가장 작은 $S$ 를 찾는다면 $\mathbb{W}$ 의 모든 벡터를 표현할 때 조금이라도 적은 $S$ 의 벡터의 일차결합으로 표현할 수 있으므로, 연산의 횟수를 줄일 수 있다. 즉, 이것은 $S$ 가 일차종속인지 아닌지 확인하려 하는 것이다. 만약 일차종속이면 $\mathbb{W}$ 를 생성하는 $S' \subsetneq S$ 가 존재하므로 $S'$ 를 사용해야 연산 횟수를 줄일 수 있다.

    - 예시 

        $u_1 = (2, -1, 4), u_2 = (1, -1, 3), u_3 = (1, 1, -1), u_4 = (1, -2, -1)$ 에 대하여 집합 $S = \{u_1, u_2, u_3, u_4\}$ 는 $\R ^{3}$ 의 부분공간 $\mathbb{W}$ 를 생성한다. 이때 $\mathbb{W}$ 를 생성하는 $S' \subsetneq S$ 를 찾는 것은 $S$ 의 어떤 벡터를 $S$ 의 다른 벡터의 일차결합으로 표현할 수 있는지 찾는 것이다.

        $u_3 = 2u_1 - 3u_2 + 0u_4$ 이므로 $u_3$ 은 나머지 세 벡터의 일차결합이다. 이는 

        $$ -2u_1 + 3u_2 + u_3 -0u_4 = 0 $$

        인데, 이와 같이 $S$ 의 어떤 벡터가 다른 벡터의 일차결합이면 영벡터를 $S$ 의 일차결합으로 표현할 때 어떤 계수가 $0$ 이 아니다. 이것의 역도 성립한다.
    
    위 예시에서 볼 수 있듯이 다음 명제는 동치이다. 
        
    - 영벡터를 $S$ 의 벡터의 모든 계수가 $0$ 이 아닌 일차결합으로 표현하는 방법이 존재한다.
    
    - $S$ 의 어떤 벡터는 다른 벡터의 일차결합이다.

    위의 예시에서 $u_1, u_2, u_3$ 의 계수가 $0$ 이 아니므로 $u_1 = au_2 + bu_3$ 와 같이 $u_1$ 을 나머지 세 벡터의 일차결합으로 표현할 수 있다. $u_2, u_3$ 도 마찬가지로 나머지 세 벡터의 일차결합으로 표현된다. 

    그러므로 $S' \subsetneq  S$ 인 $S'$ 를 찾는 방법은 $S$ 의 벡터의 모든 계수가 $0$ 이 아닌 일차결합으로 영벡터를 표현할 수 있는지 확인하는 것이다.

- 예시 

    $\R ^{4}$ 의 부분집합 $S = \{(1,3,-4,2), (2,2,-4,0) , (1,-3,2,-4), (-1,0,1,0)\}$ 에 대하여 $S$ 가 일차종속인지 확인하려면 어떤 벡터가 나머지 벡터의 일차결합임을 보이는 것이다. 이는 다음을 만족하면서 적어도 하나는 $0$ 이 아닌 스칼라 $a_1, a_2, a_3, a_4$ 가 존재함을 보이는 것이다. 

    $$ a_1 (1,3,-4,2)+ a_2 (2,2,-4,0) + a_3 (1,-3,2,-4) + a_4 (-1,0,1,0) = 0 $$

    이는 다음 연립일차방정식의 자명하지 않은 해를 찾는 것과 같다. 

    $$ a_1 + 2a_2 + a_3 - a_4 = 0 $$

    $$ 3a_1 + 2a_2 -3 a_3 + 0 a_4 = 0 $$

    $$ -4a_1 - 4a_2 +2 a_3 + a_4 = 0 $$

    $$ 2a_1 + 0a_2 -4 a_3 + 0a_4 = 0 $$

    변수가 4개인데 관계가 4개이므로 해를 찾을 수 있다. 자명하지 않은 해는 $a_1 = 4, a_2 = -3, a_3 = 2, a_4 = 0$ 이다. 즉 $S$ 는 $\R ^{4}$ 의 일차종속인 부분집합이다. 

!!! tldr ""

    일차독립(linearly independent) : 벡터공간의 부분집합 $S$ 가 임의의 서로 다른 벡터 $u_1, u_2, \dots, u_n \in S$ 와 스칼라 $a_1, a_2, \dots, a_n$ 에 대하여 $a_1u_1 + a_2u_2 + \dots + a_nu_n = 0$ 이 성립하려면 반드시 $a_1 = a_2 = \dots = a_n = 0$ 이어야 한다면 집합 $S$ 를 일차독립이라 한다. 

- 일차독립은 쉽게 말해 벡터공간의 부분집합 $S$ 가 일차종속이 아니면 일차독립이다. 이때 $S$ 의 벡터 또한 일차독립이다.

!!! tldr "벡터공간에서 참인 명제"

    1. 공집합 $\varnothing$ 은 일차독립이다. 어떤 집합이 일차종속이려면 반드시 공집합이 아니어야 한다. 

    2. 영이 아닌 벡터 하나로 이루어진 집합은 일차독립이다. 

    3. 어떤 집합이 일차독립이기 위한 필요충분조건은 영벡터 $0$ 을 주어진 집합에 대한 일차결합으로 표현하는 방법이 자명한 표현뿐인 것이다.

- 2) 의 증명 

    만약 벡터 $u$ 에 대한 집합 $\{u\}$ 가 일차종속이면 스칼라 $a \neq  0$ 에 대하여 $au = 0$ 이므로 $u = a ^{-1}au=a ^{-1}0 = 0$ 이므로 $u$ 는 영벡터가 된다. 이는 모순이다.

- 3) 은 유한집합이 일차독립인지 판단할 때 유용하게 사용된다.

    - 예시 

        $S = \{(1,0,0,-1), (0,1,0,-1), (0,0,1,-1), (0,0,0,1)\}$ 에 대하여 영벡터 $0$ 의 일차결합 표현이 자명한 표현 뿐이라면 $S$ 는 일차독립이다. 스칼라 $a,b,c,d$ 에 대하여 

        $$ a(1,0,0,-1) + b (0,1,0,-1) + c (0,0,1,-1) + d (0,0,0,1) = (0, 0, 0, 0) $$ 

        라고 하면 이는 연립방정식

        $$ a = 0 , b = 0 , c = 0 $$

        $$ -a-b-c+d = 0 $$

        와 같다. 따라서 $a=b=c=d=0$ 이므로 $S$ 는 일차독립이다.

!!! tldr "정리 1.6"

    $\mathbb{V}$ 가 벡터공간이고 $S_1 \subseteq S_2 \subseteq \mathbb{V}$ 일 때 $S_1$ 이 일차종속이면 $S_2$ 도 일차종속이다. 

- 증명 

    $S_1 = \{v_1, v_2, \dots, v_n\}$ 은 일차종속이므로 적어도 하나는 $0$ 이 아닌 스칼라 $a_1, a_2, \dots, a_n$ 에 대하여 

    $$ a_1v_1 + a_2v_2 + \dots + a_nv_n = 0 $$

    이 성립한다. 이때 $S_2= \{v_1, v_2, \dots, v_n, v _{n+1}, \dots, v_m\}$ 가 일차독립이라고 하면 스칼라 $b_1, b_2, \dots, b_m$ 에 대하여 
    
    $$b_1v_1 + b_2v_2 + \dots + b_nv_n + b _{n+1}v _{n+1} + \dots + b_mv_m = 0$$
    
    이 성립하려면 반드시 $b_1 = b_2 = \dots = b_m = 0$ 이어야 한다. 따라서

    $$b_1v_1 + b_2v_2 + \dots + b_nv_n = 0$$

    에서 그 계수들이 반드시 $b_1 = b_2 = \dots = b_n = 0$ 을 만족하는데, 이는 가정과 모순이다. 그러므로 $S_2$ 는 일차종속이다. ■ 
    
!!! tldr "정리 1.6 따름정리"

    $\mathbb{V}$ 가 벡터공간이고 $S_1 \subseteq S_2 \subseteq \mathbb{V}$ 일 때 $S_2$ 이 일차독립이면 $S_1$ 도 일차독립이다. 

- 증명 

    $S_2 = \{v_1, v_2, \dots, v_n\}$ 은 일차독립이므로 스칼라 $a_1, a_2, \dots, a_n$ 에 대하여 

    $$ a_1v_1 + a_2v_2 + \dots + a_nv_n = 0 $$

    이 성립하려면 반드시 $a_1 = a_2 = \dots = a_n = 0$ 이다. 이때 $m \leq n$ 에 대하여 $S_1= \{v_1, v_2, \dots, v_m\}$ 가 일차종속이라고 하면 적어도 하나는 $0$ 이 아닌 스칼라 $b_1, b_2, \dots, b_m$ 에 대하여 
    
    $$b_1v_1 + b_2v_2 + \dots + b_mv_m = 0$$
    
    이 성립한다. 이때 가정에 의하여

    $$a_1v_1 + a_2v_2 + \dots + a_mv_m = 0$$

    에서 그 계수들이 반드시 $a_1 = a_2 = \dots = a_n = 0$ 을 만족하는데, 이는 모순이다. 그러므로 $S_1$ 는 일차독립이다. ■ 
    
!!! tldr ""

    무한체의 벡터공간 $\mathbb{V}$ 의 부분공간 $\mathbb{W}$ 를 생성하는 집합 $S$ 가 일차독립이면 최소생성집합이다.

- 예시 

    위에서 이미 살펴보았던 예시를 다시 살펴보자.

    $u_1 = (2, -1, 4), u_2 = (1, -1, 3), u_3 = (1, 1, -1), u_4 = (1, -2, -1)$ 에 대하여 집합 $S = \{u_1, u_2, u_3, u_4\}$ 는 $\R ^{3}$ 의 부분공간 $\mathbb{W}$ 를 생성한다. 이때 $u_3 = 2u_1 - 3u_2 + 0u_4$ 이므로 $S$ 는 일차 종속이다. 즉 $S$ 의 일차결합 $a_1u_1 + a_2u_2 + a_3u_3 + a_4u_4$ 은 

    $$ a_1u_1 + a_2u_2 + a_3u_3 + a_4u_4 = a_1u_1 + a_2u_2 + a_3(2u_1 - 3u_2 + 0u_4) + a_4u_4 $$

    $$ = (a_1 + 2a_3)u_1 + (a_2 -3a_3)u_2 + a_4u_4 $$

    이므로 $S' = \{u_1, u_2, u_4\} \subsetneq S$ 가 $S$ 와 같은 공간을 생성한다. 그러므로 $S$ 로 벡터공간을 표현하는 것은 비효율적이다.

!!! tldr "정리 1.7"

    집합 $S$ 에 대하여 다음 명제들은 동치이다. 

    1. 두 개 이상의 벡터를 가진 $S$ 가 일차종속일 때 $v \in S$ 를 다른 벡터의 일차결합으로 표현할 수 있으면 $S \text{ \textbackslash }\{v\}$ 도 $S$ 와 같은 공간을 생성한다.

    2. 임의의 $S' \subsetneq S$ 이 $S$ 와 같은 공간을 생성할 수 없으면 $S$ 는 일차독립이다.

    3. 벡터공간 $\mathbb{V}$ 와 일차독립인 부분집합 $S$ 와 벡터 $v \in \mathbb{V} \text{ \textbackslash } S$ 에 대하여 $S \cup \{v\}$ 가 일차종속이기 위한 필요충분조건은 $v \in \text{span}(S)$ 이다. 

- 세번째 명제의 증명 

    $S \cup \{v\}$ 가 일차종속이므로 벡터 $u_1, u_2, \dots, u_n \in S \cup \{v\}$ 와 적어도 하나는 영이 아닌 스칼라 $a_1, a_2, \dots, a_n$ 이 존재하여 

    $$ a_1u_1 +a_2u_2 + \dots +a_nu_n = 0 $$

    을 만족한다. $S$ 가 일차독립이므로 어떤 벡터 $u_i$ 가 $v$ 인데, 이것을 그냥 $u_1$ 이라고 하면 

    $$ v = a_1 ^{-1}( - a_2u_2 - \dots - a_nu_n ) = -(a_1 ^{-1}a_2)u_2 - \dots - -(a_1 ^{-1}a_n)u_n $$ 

    이므로 $v \in \text{span}(S)$ 이다. ▲ 

    역으로 $v \in \text{span}(S)$ 이면 $v_1, v_2, \dots, v_m \in S$ 와 스칼라 $b_1, b_2, \dots, b_m$ 에 대하여

    $$ v = b_1v_1 +b_2v_2 + \dots +b_mv_m $$

    이므로 

    $$ 0 = b_1v_1 +b_2v_2 + \dots +b_mv_m +(-1)v$$

    이다. 그런데 $v \not\in S$ 이고 $v$ 의 계수가 $0$ 이 아니므로 집합 $\{v_1,v_2, \dots,v_m,v\} \subset S \cup \{v\}$ 은 일차종속이다. 그러면 정리 "$\mathbb{V}$ 가 벡터공간이고 $S_1 \subseteq S_2 \subseteq \mathbb{V}$ 일 때 $S_1$ 이 일차종속이면 $S_2$ 도 일차종속이다." 에 의하여 $S \cup \{v\}$ 도 일차종속이다. ■ 

# 기저와 차원 

!!! tldr ""

    기저(basis) : 벡터공간 $\mathbb{V}$ 와 부분집합 $\beta$ 에 대하여 $\beta$ 가 일차독립이고 $\mathbb{V} = \text{span}(\beta )$ 이면 $\beta$ 를 $\mathbb{V}$ 의 기저라고 한다.

- 지금까지 부분공간 $\mathbb{W}$ 의 생성집합 $S$ 에 대한 임의의 $S' \subsetneq S$ 가 $\mathbb{W}$ 를 생성하지 못하면 $S$ 가 일차독립임을 살펴보았다. 또한 아래의 정리로부터 기저에 의한 해당 벡터공간의 벡터의 표현은 유일함을 알 수 있다. 이로써 일차독립인 생성집합은 그 벡터공간을 생성하는 가장 기본적인 레고 블록임을 알 수 있다. 따라서 일차독립인 생성집합을 "기저(basis)" 라고 부른다.

- 예시 

    $\text{span}(\varnothing ) = \{0\}$ 이고 $\varnothing$ 은 일차독립이므로 $\varnothing$ 은 점공간의 기저이다.

- 예시 

    $\{x ^{n} : n \in \N\} = \{1, x, x ^{2}, x ^{3}, \dots\}$ 은 $\mathbb{P} (\mathbb{F} )$ 의 기저이다.

    - 이 예시는 기저가 무한집합일 수도 있다는 것을 말해준다. 심지어 어떤 벡터공간의 기저는 유한집합일 수 없다. 대표적으로 위 예시의 벡터공간 $\mathbb{P} (\mathbb{F} )$ 의 기저는 반드시 무한집합이다.

- 기저 중에는 표준기저(standard basis)라는 특별한 기저도 있다.

    - 예시 

        벡터공간 $\mathbb{F} ^{n}$ 에 대한 벡터 

        $$ e_1 = (1, 0, 0, \dots, 0)
        , e_2 = (0, 1, 0, \dots, 0)
        , \enspace  \dots \enspace 
        , e_n = (0, 0, 0, \dots, 1)
        $$

        의 집합 $\{e_1, e_2, \dots, e_n\}$ 은 $\mathbb{F} ^{n}$ 의 표준기저이다. 
    
    - 예시 

        $\{1, x, x ^{2}, x ^{3}, \dots, x ^{n}\}$ 은 $\mathbb{P}_n (\mathbb{F} )$ 의 표준기저이다.

!!! tldr "정리 1.8"

    벡터공간 $\mathbb{V}$ 와 서로 다른 벡터 $u_1, u_2, \dots, u_n \in \mathbb{V}$ 에 대한 집합 $\beta = \{u_1, u_2, \dots, u_n\}$ 가 $\mathbb{V}$ 에 대하여 다음은 동치이다.

    1. 집합 $\beta = \{u_1, u_2, \dots, u_n\}$ 가 $\mathbb{V}$ 의 기저이다.

    2. 임의의 $v \in \mathbb{V}$ 를 유일한 스칼라 $a_1, a_2, \dots, a_n$ 에 대한 $\beta$ 의 일차결합으로 나타낼 수 있다. 

- 이 정리는 $v \in \mathbb{V}$ 가 주어지면 $\beta$ 의 일차결합에 대한 스칼라 $n$순서쌍 $(a_1, a_2, \dots, a_n)$ 이 유일하게 결정되고, 반대로 $(a_1, a_2, \dots, a_n)$ 이 주어지면 이것을 $\beta$ 의 일차결합 계수로 가지는 유일한 벡터 $v \in \mathbb{V}$ 가 결정됨을 말해준다. ($n$ 은 기저에 존재하는 벡터의 갯수이다.)

- 1 에서 2 를 도출하는 증명 

    $\beta$ 가 기저이므로 $\text{span}(\beta ) = \mathbb{V}$ 이므로 $v \in \mathbb{V} = \text{span}(\beta )$ 이다. 

    $$ v = a_1u_1 + a_2u_2 + \dots + a_nu_n, \enspace v = b_1u_1 + b_2u_2 + \dots + b_nu_n $$

    라고 하면 

    $$ v - v = 0 = (a_1 - b_1)u_1 + (a_2 - b_2)u_2 + \dots + (a_n - b_n)u_n $$

    인데 $\beta$ 가 일차독립이므로 

    $$ a_1 - b_1 = 0, a_2 - b_2 = 0, \dots, a_n - b_n = 0 \iff a_1  = b_1 , a_2  = b_2 , \dots, a_n  = b_n  $$

    이다. ■ 

!!! tldr "정리 1.9"

    유한집합 $S$ 가 벡터공간 $\mathbb{V}$ 를 생성하면 $S$ 의 부분집합 중에 $\mathbb{V}$ 의 기저가 존재한다. 

- 이 정리는 유한집합이 벡터공간을 생성하면 그 벡터공간이 유한집합인 기저를 포함함을 말해준다.

- 증명 

    $S = \varnothing \lor S = \{0\}$ 이면 $\text{span}(S)= \mathbb{V} = \{0\}$ 이다. $\varnothing$ 은 $S$ 의 부분집합이면서 $\mathbb{V}$ 의 기저이다. ▲ 

    영이 아닌 벡터 $u_1$ 에 대하여 $u_1 \in  S$ 이라고 하면 영이 아닌 벡터 하나로 이루어진 집합은 일차독립이므로 $\beta = \{u_1\}$ 은 일차독립이다. 이때 $\beta$ 가 일차독립이 되도록 $S$ 에서 벡터 $u_2, \dots, u_n$ 들을 꺼내서 $\beta$ 에 속하게 하면 $\beta  = \{u_1, \dots, u_n\}$ 이 된다. 

    $\beta = S$ 라면 $S$ 는 일차독립이고 $\mathbb{V}$ 의 생성집합이므로 $\mathbb{V}$ 의 기저이다. ▲ 

    $\beta \subsetneq S$ 라면 정리 1.5 "$S$ 를 포함하는 $\mathbb{V}$ 의 부분공간은 $\text{span}(S)$ 을 포함한다." 에서 $\text{span}(S) = \mathbb{V}$ 이므로 $S \subset \text{span}(\beta )$ 를 보이면 $\text{span}(S) = \mathbb{V} \subset \text{span}(\beta )$ 인데, $\text{span}(\beta ) \subset \text{span}(S)$ 임은 자명하므로 $\text{span}(\beta ) = \mathbb{V}$ 이 되어 $\beta$ 가 $\mathbb{V}$ 의 기저임이 증명된다.

    먼저 $v \in S$ 에 대하여 $v \in \beta \implies v \in \text{span}(\beta )$ 이다. $v \not\in \beta$ 이면 $\beta \cup \{v\}$ 는 $\beta$ 의 정의에 의하여 일차종속이므로 정리 1.7 "벡터공간 $\mathbb{V}$ 와 일차독립인 부분집합 $S$ 와 벡터 $v \in \mathbb{V} \text{ \textbackslash } S$ 에 대하여 $S \cup \{v\}$ 가 일차종속이기 위한 필요충분조건은 $v \in \text{span}(S)$ 이다." 에 의하여 $v \in \text{span}(\beta )$ 이다. 그러므로 어느 경우에나 $\forall v \in S, v \in \text{span}(\beta )$ 이므로 $S \subset \text{span}(\beta )$ 이다. ■ 

- 위 증명과정은 $\mathbb{V}$ 의 유한 생성집합을 축소하여 $\mathbb{V}$ 의 기저를 얻는 방법을 말해준다.

    - 예시 

        집합 $S = \{(2, -3, 5), (8, -12, 20), (1, 0, -2), (0, 2, -1), (7, 2, 0)\}$ 에 대하여 $\text{span}(S) = \R ^{3}$ 인데 $S$ 를 축소하여 $\R ^{3}$ 의 최소 기저를 얻자.

        $S$ 에서 영이 아닌 벡터를 아무거나 택하자. 일단 $(2, -3, 5)$ 를 택하여 $\beta = \{(2, -3, 5)\}$ 를 만든다. 이후 $(8, -12, 20)$ 이 기저 집합에 속할 수 있는지 검증하는데 

        $$ 4(2, -3, 5) - (8, -12, 20) = 0 $$

        에서 집합 $\{(2, -3, 5) , (8, -12, 20)\}$ 은 일차종속이므로 $(8, -12, 20)$ 은 택하지 않는다. ▲ 

        $(2, -3, 5)$ 와 $(1, 0, -2)$ 을 $\beta$ 에 집어넣어도 일차독립이므로 $\beta$ 에 넣는다. ▲ 

        이때 $(7, 2, 0)$ 를 $\beta$ 에 넣어서 $\{(2, -3, 5), (1, 0, -2), (0, 2, -1), (7, 2, 0)\}$ 를 만들었는데 일차종속이라면 $(7, 2, 0)$ 를 $\beta$ 에 넣으면 안된다. 

        $$ 2(2, -3, 5) + 3(1, 0, -2) + 4(0, 2, -1) - (7, 2, 0) = 0 $$

        이므로 일차종속이므로 $\beta$ 에 넣으면 안된다. 그러므로 $\beta$ 는 최종적으로 

        $$ \beta = \{ (2, -3, 5) , (1, 0, -2) , (0, 2, -1) \} $$

        가 된다. 

!!! tldr "정리 1.10"

    대체정리(replacement theorem) : 집합 $G$ 가 벡터공간 $\mathbb{V}$ 에 대하여 $\text{span}(G) = \mathbb{V}$ 이고, $L \subset \mathbb{V}$ 이 일차독립이면 다음이 성립한다.

    1. $\text{card}(L) \leq \text{card}(G)$

    2. $\exists H \subset G \text{ s.t. } \text{span}(L \cup H) = \mathbb{V} \land \text{card}(H) = \text{card}(G) - \text{card}(L)$

- 이 정리의 따름정리들은 벡터공간에 관한 모든 사실 중 가장 중요하다.

- 증명 

    $\text{card}(L) = 0$ 즉, $L = \varnothing$ 일 때 $H = G$ 이면 성립한다. ▲ 

    $\text{card}(L') = m \geq 0$ 에 대하여 성립한다고 가정하고 $\text{card}(L) = m + 1$ 에 대하여 성립함을 보이자. 이때 편의상 $\text{card}(G) = n$ 이라고 하자. 
    
    $L = \{v_1, v_2, \dots, v _{m+1}\}$ 에 대하여 정리 1.6 따름정리 "$\mathbb{V}$ 가 벡터공간이고 $S_1 \subseteq S_2 \subseteq \mathbb{V}$ 일 때 $S_2$ 이 일차독립이면 $S_1$ 도 일차독립이다." 에 의하여 $L' = \{v_1, v_2, \dots, v _{m}\}$ 은 일차독립이다.

    $m$ 에 대해서는 성립한다고 가정했으므로 집합 $H' = \{u_1, u_2, \dots, u _{n-m}\} \subset G$ 이 존재하여 
    
    $$\text{span}(L' \cup H') = \mathbb{V} \tag{1} $$ 
    
    을 만족한다. 그러므로 스칼라 $a_1, \dots, a_m$ 와 스칼라 $b_1, \dots, b _{n-m}$ 이 존재하여 다음과 같이 벡터 $v _{m+1}$ 도 생성한다. 

    $$ a_1v_1 + \dots +a_mv_m + b_1u_1 + \dots + b _{n-m}u _{n-m} = v _{m+1} $$

    $\text{card}(L') \leq \text{card}(G) \iff m \leq n$ 인데 $n = m$ 이면 $v _{m+1}$ 이 $v_1, \dots, v_m$ 의 일차결합이 되므로 정리 1.7 "벡터공간 $\mathbb{V}$ 와 일차독립인 부분집합 $S$ 와 벡터 $v \in \mathbb{V} \text{ \textbackslash } S$ 에 대하여 $S \cup \{v\}$ 가 일차종속이기 위한 필요충분조건은 $v \in \text{span}(S)$ 이다." 에 의하여 $v _{m+1} \in \text{span}(L')$ 에서 $L = L' \cup \{v _{m+1}\}$ 이 일차종속이 되어버린다. 하지만 $L$ 은 일차독립이라고 하였으므로 모순이다. 그러므로 $m \neq n$ 이고 $m < n \iff m + 1 \leq n$ 이다. 즉, $\text{card}(L') + 1 = \text{card}(L) \leq \text{card}(G)$ 이 성립한다. ▲ 

    만약 $b_i$ 들이 모두 $0$ 이면 위와 같은 모순이 또 발생하므로 $b_i$ 중 하나는 반드시 $0$ 이 아니다. 그것을 $b_1$ 이라 하면 

    $$ u_1 = (-b_1 ^{-1}a_1) v_1 + \dots + (-b_1 ^{-1}a_m) v_m + (b_1 ^{-1})v _{m+1} $$

    $$ + (-b_1 ^{-1}b_2) u_2 + \dots + (-b_1 ^{-1}b _{n-m}) u _{n-m} $$

    이다. $H = \{u_2, \dots, u _{n-m}\}$ 이라 하면 $u_1 \in \text{span}(L \cup H)$ 이다. 그러면 $v_1, \dots, v_m, u_2, \dots, u _{n-m} \in \text{span}(L \cup H)$ 이므로 

    $$ \{v_1, \dots, v_m, u_1, \dots, u _{n-m}\} \subseteq \text{span}(L \cup H) $$

    이다. $(1)$ 에서 $\text{span}(\{v_1, \dots, v_m, u_1, \dots, u _{n-m}\}) = \mathbb{V}$ 인데, 정리 1.5 "$S$ 를 포함하는 $\mathbb{V}$ 의 부분공간은 $\text{span}(S)$ 을 포함한다." 에 의하여 $\text{span}(\{v_1, \dots, v_m, u_1, \dots, u _{n-m}\}) = \mathbb{V} \subset \text{span}(L \cup H)$ 이다. $\text{span}(L \cup H) \subset \mathbb{V}$ 은 자명하므로 결국 $\text{span}(L \cup H)= \mathbb{V}$ 이다. ▲ 

    그러면 집합 $H \subset \{u_1, u_2, \dots, u _{n-m}\} \subset G$ 이고 $\text{card}(H) = n - (m + 1) = \text{card}(G) - \text{card}(L)$ 이다. 그러면 수학적 귀납법에 의하여 모든 증명이 끝났다. ■ 

- 이 정리에서 집합 $G$ 를 벡터공간 $\mathbb{V}$ 를 생성하는 극소 생성집합, 즉 기저라고 생각하는 것이 편하다. 왜냐하면 $\mathbb{V}$ 를 생성하는 임의의 생성집합 $G$ 에 대하여 

    $$ \text{card}(L) \leq \text{card}(G) $$

    라는 부등식이 성립해야 하는데, 이 부등식은 어차피 극소 생성집합(기저)인 $G'$ 에 의하여 

    $$ \text{card}(L) \leq \text{card}(G') = \dim(\mathbb{V} ) $$

    로 스케일링되기 때문이다. 그러니까 $\mathbb{V}$ 를 생성하는 집합 $G$ 와 일차독립 $L$ 이 주어졌다고 하자. 그러면 위의 1) 를 만족하므로 

    $$ \text{card}(L) \leq \text{card}(G) $$

    인데 이 1) 는 $\mathbb{V}$ 를 생성하는 $G' \subset G$ 에서도 성립하므로
    
    $$ \text{card}(L) \leq \text{card}(G') = \dim(\mathbb{V} ) \leq \text{card}(G) $$

    가 된다. 음.. 하지만 2) 의 경우 $G$ 에서 성립하므로

    $$\exists H \subset G \text{ s.t. } \text{span}(L \cup H) = \mathbb{V} \land \text{card}(H) = \text{card}(G) - \text{card}(L)$$

    인데 $G' \subset G$ 에서도 성립하므로

    $$\exists H' \subset G' \text{ s.t. } \text{span}(L \cup H') = \mathbb{V} \land \text{card}(H') = \text{card}(G') - \text{card}(L)$$

    가 되겠구나. 그러면 $H$ 가 존재한다는 것과 전혀 다른 $H'$ 가 존재한다는 것이니까 연관성을 주장할 수 없어 보이네. 그러면 이 정리의 $G$ 가 기저여야만 한다고 주장하는 것도 타당해보이지는 않고.

    하지만 1) 의 경우에서는 $G$ 보다 더 작은 생성집합에 대하여 부등식이 스케일링되기 때문에 $G$ 를 기저라고 생각하는 게 편하다. 그러면 1) 을 통하여 

    $$ \exists S \subset \mathbb{V}, \text{card}(S) > \dim(\mathbb{V} ) \implies S \text{ is not linearly independent } $$

    라고 말할 수 있다.

!!! tldr "정리 1.10 따름정리 1"

    벡터공간 $\mathbb{V}$ 가 유한집합인 기저를 포함하면 $\mathbb{V}$ 의 모든 기저는 유한집합이며, 기수가 같다.

- 이 정리는 벡터공간의 기저의 기수가 벡터공간의 본질적인 성질임을 말해준다. 그래서 이 정리 덕분에 아래와 같은 차원, 유한차원, 무한차원을 정의할 수 있다.

- 증명

    $\beta$ 가 $\mathbb{V}$ 의 기저이고, $\gamma$ 가 $\text{card}(\gamma ) > \text{card}(\beta )$ 인 $\mathbb{V}$ 의 기저라고 하면, $\exists S \subset \gamma \text{ s.t. } \text{card}(S) = \text{card}(\beta )+1$ 이다. $S$ 는 일차독립이고 $\text{span}(\beta) = \mathbb{V}$ 이므로 정리 1.10 
    
    "대체정리(replacement theorem) : 집합 $G$ 가 벡터공간 $\mathbb{V}$ 에 대하여 $\text{span}(G) = \mathbb{V}$ 이고 $L \subset \mathbb{V}$ 이 일차독립이면 다음이 성립한다. $\text{card}(L) \leq \text{card}(G)$"
    
    에 의하여 $\text{card}(S) = \text{card}(\beta ) + 1 \leq \text{card}(\beta )$ 인데, 이는 모순이다. 그러므로 $\text{card}(\gamma) \leq \text{card}(\beta )$ 이다. ▲ 

    같은 논리로 $\text{card}(\beta ) \leq \text{card}(\gamma )$ 를 도출할 수 있다. ▲ 

    그러므로 $\text{card}(\beta ) = \text{card}(\gamma )$ 이다. ■ 

!!! tldr ""

    차원(dimension) : 벡터공간의 기저의 기수이다.

- 벡터공간 $\mathbb{V}$ 의 차원을 $\dim(\mathbb{V} )$ 으로 표기한다.

- 예시 

    지금까지 살펴본 여러가지 벡터공간의 차원은 다음과 같다. 

    $$ \dim(\{0\}) = 0 , \enspace \dim(\mathbb{F} ^{n}) = n , \enspace \dim(\mathbb{M} _{m \times n}(\mathbb{F} )) = mn , \enspace \dim(\mathbb{P} _n(\mathbb{F} )) = n+1 $$

- 동일한 벡터공간이라도 어떤 체 위에 존재하는지에 따라 차원이 달라진다.

    - 예시

        복소수체 $\mathbb{C}$ 에서 복소수 벡터공간의 차원은 $1$ 이고 기저는 $\{1\}$ 이다.

        실수체 $\R$ 에서 복소수 벡터공간의 차원은 $2$ 이고 기저는 $\{1, i\}$ 이다.

- 예시 

    벡터공간 $\mathbb{F} ^{5}$ 의 부분공간 

    $$ \mathbb{W} = \{(a_1, a_2, a_3, a_4, a_5) \in \mathbb{F} ^{5} : a_1 + a_3 + a_5 = 0, a_2 = a_4 \} $$

    의 기저는 $\{(-1, 0, 1, 0, 0,), (-1, 0, 0, 0, 1), (0, 1, 0, 1, 0)\}$ 이므로 $\dim(\mathbb{W} ) = 3$ 이다. 

- 예시 

    $n \times n$ 대각행렬 집합 $\mathbb{W}$ 은 $\mathbb{M} _{n \times n}(\mathbb{F} )$ 의 부분공간인데 $\mathbb{W}$ 의 기저는 $\{E ^{11}, E ^{22}, \dots, E ^{nn}\}$ 이다. $E ^{ij}$ 란 $i$ 행 $j$ 열 성분이 $1$ 이고 나머지 성분이 모두 $0$ 인 행렬이다. 

    그러므로 $\dim(\mathbb{W} ) = n$ 이다. 

- 예시 

    $n \times n$ 대칭행렬 집합 $\mathbb{W}$ 는 $\mathbb{M} _{n \times n}(\mathbb{F} )$ 의 부분공간인데, $\mathbb{W}$ 의 기저는 $i$ 행 $j$ 열과 $j$ 행 $i$ 열의 성분만 $1$ 이고 나머지는 $0$ 인 $n \times n$ 행렬 $A ^{ij}$ 에 대하여 

    $$ \{A ^{ij} : 1 \leq i \leq j \leq n\} $$

    이므로 

    $$ \dim(\mathbb{W} ) = n + (n-1) + \dots + 1 = \dfrac{n(n+1)}{2} $$

    이다.

!!! tldr ""

    유한차원(finite dimension) : 기저가 유한집합인 벡터공간이다.

- 정리 1.10 "대체정리(replacement theorem) : 집합 $G$ 가 벡터공간 $\mathbb{V}$ 에 대하여 $\text{span}(G) = \mathbb{V}$ 이고 $L \subset \mathbb{V}$ 이 일차독립이면 다음이 성립한다. 1. $\text{card}(L) \leq \text{card}(G)$ 2. $\exists H \subset G \text{ s.t. } \text{span}(L \cup H) = \mathbb{V} \land \text{card}(H) = \text{card}(G) - \text{card}(L)$"

    를 차원의 관점에서 다시 말해보면

    "유한차원 벡터공간 $\mathbb{V}$ 에서 $\dim(\mathbb{V} )$ 보다 더 많은 개수의 벡터를 가지는 부분집합은 일차독립이 아니다."

    이다. 왜냐하면 차원보다 큰 기수를 가지는 부분집합은 반드시 기저의 일차결합으로 표현가능하기 때문이다.

- 즉, 유한차원 벡터공간 $\mathbb{V}$ 에서 $\dim(\mathbb{V} )$ 보다 더 많은 벡터를 가지면서 일차독립인 부분집합이 존재하지 않는다.

    $$ \not \exists S \subset \mathbb{V} \text{ s.t. } \text{card}(S) > \dim(\mathbb{V} ) \land S \text{ is linearly independent} $$

!!! tldr ""

    무한차원(infinite dimension) : 기저가 무한집합인 벡터공간이다.

- 예시 

    벡터공간 $\mathbb{P} (\mathbb{F} )$ 는 무한집합 $\{x ^{n} : n \in \N\} = \{1, x, x ^{2}, \dots\}$ 을 기저로 가지므로 무한차원이다. 

!!! tldr "정리 1.10 따름정리 2"

    벡터공간 $\mathbb{V}$ 에 대하여 다음이 성립한다.

    1. $\mathbb{V}$ 의 임의의 유한 생성집합 $S$ 는 $\dim(\mathbb{V} ) \leq \text{card}(S)$ 이고, $\dim(\mathbb{V} ) = \text{card}(S)$ 인 생성집합 $S$ 는 $\mathbb{V}$ 의 기저이다.

    2. $S \subset \mathbb{V}$ 가 일차독립이고 $\text{card}(S) = \dim(\mathbb{V} )$ 이면 기저이다.

    3. $L \subset \mathbb{V}$ 이 일차독립이면 $L \subset \beta$ 인 $\mathbb{V}$ 의 기저 $\beta$ 가 존재한다.

- 명제 3) 은 일차독립인 벡터공간의 부분집합을 확장하여 기저를 만들 수 있음을 말해준다. 

- 증명 

    우선 벡터공간 $\mathbb{V}$ 의 기저를 $\beta$ 라고 하면 $\text{card}(\beta ) = \dim(\mathbb{V})$ 이다.

    $\mathbb{V}$ 의 유한 생성집합을 $G$ 라고 하면 정리 1.9 "유한집합 $S$ 가 벡터공간 $\mathbb{V}$ 를 생성하면 $S$ 의 부분집합 중에 $\mathbb{V}$ 의 기저가 존재한다." 에 의하여 $G$ 의 부분집합이자 $\mathbb{V}$ 의 기저인 $H$ 가 존재한다. 정리 1.10 따름정리 1 "벡터공간 $\mathbb{V}$ 가 유한집합인 기저를 포함하면 $\mathbb{V}$ 의 모든 기저는 유한집합이며, 기수가 같다." 에 의하여 $\text{card}(H) = \dim(\mathbb{V} )$ 이다. 따라서 $\dim(\mathbb{V} )\leq \text{card}(G)$ 이고 만약 $\dim(\mathbb{V} ) = \text{card}(G)$ 이면 $G = H$ 으로써 $G$ 는 $\mathbb{V}$ 의 기저이다. ▲ 

    $L \subset \mathbb{V}$ 이 일차독립이고 $\text{card}(L) = \dim(\mathbb{V} )$ 라고 하자. 정리 1.10 "대체정리(replacement theorem) : 집합 $G$ 가 벡터공간 $\mathbb{V}$ 에 대하여 $\text{span}(G) = \mathbb{V}$ 이고 $L \subset \mathbb{V}$ 이 일차독립이면 다음이 성립한다. $\exists H \subset G \text{ s.t. } \text{span}(L \cup H) = \mathbb{V} \land \text{card}(H) = \text{card}(G) - \text{card}(L)$" 에 의하여 

    $$ \exists H \subset \beta  \text{ s.t. } \text{span}(L \cup H) = \mathbb{V} \land \text{card}(H) = \text{card}(\beta) - \text{card}(L)  $$

    인데 $\text{card}(H) = \text{card}(\beta) - \text{card}(L) = \dim(\mathbb{V} ) - \dim(\mathbb{V} ) = 0$ 이다. $\text{card}(H) = 0 \iff H = \varnothing$ 이므로 $\text{span}(L) = \mathbb{V}$ 이고 $L$ 은 일차독립이므로 $L$ 은 $\mathbb{V}$ 의 기저이다. ▲ 

    $L \subset \mathbb{V}$ 가 일차독립이면 정리 1.10 "대체정리(replacement theorem) : 집합 $G$ 가 벡터공간 $\mathbb{V}$ 에 대하여 $\text{span}(G) = \mathbb{V}$ 이고 $L \subset \mathbb{V}$ 이 일차독립이면 다음이 성립한다. $\exists H \subset G \text{ s.t. } \text{span}(L \cup H) = \mathbb{V} \land \text{card}(H) = \text{card}(G) - \text{card}(L)$" 에 의하여 

    $$ \exists H \subset \beta  \text{ s.t. } \text{span}(L \cup H) = \mathbb{V} \land \text{card}(H) = \text{card}(\beta) - \text{card}(L)  $$

    이다. $\text{card}(L \cup H) \leq \text{card}(L) + \text{card}(H) = \text{card}(\beta) = \dim(\mathbb{V} )$ 이다. 1) 은 이미 증명되었으므로 1) 을 사용하면
    
    $$\dim(\mathbb{V} ) \leq \text{card}(L \cup H) \leq \dim(\mathbb{V} )$$

    이므로 $\text{card}(L \cup H) = \dim(\mathbb{V} )$ 이고, $L \subset L \cup H$ 는 $\mathbb{V}$ 의 기저가 된다. ■ 

- 예시 

    집합 

    $$ \{x ^{2} + 3x-2, 2x ^{2} + 5x - 3, -x ^{2} - 4x + 4\} $$

    는 벡터공간 $\mathbb{P} _2(\R)$ 을 생성하는데 이 벡터공간의 차원은 $3$ 이므로 1) 에 의하여 이 집합은 $\mathbb{P} _2(\R)$ 의 기저이다.

- 예시 

    집합 

    $$ \{(1,0,0,-1), (0,1,0,-1), (0,0,1,-1), (0,0,0,1)\} $$

    은 일차독립인데 $\dim(\R ^{4}) = 4$ 이므로 2) 에 의하여 이 집합은 $\R ^{4}$ 의 기저이다.

!!! tldr ""

    벡터공간의 일차독립 집합을 $D$, 기저의 집합을 $B$, 생성집합을 $S$ 라고 하면 다음이 성립한다. 

    $$ B = D \cap S $$

- 지금까지의 논의를 통하여 이 정리가 성립함을 자명하게 알 수 있다.

!!! tldr "정리 1.11"

    유한차원 $\mathbb{V}$ 의 부분공간 $\mathbb{W}$ 에 대하여 다음이 성립한다.
    
    1. $\mathbb{W}$ 는 유한차원이고, $\dim(\mathbb{W} ) \leq \dim(\mathbb{V} )$ 이다.

    2. $\dim(\mathbb{W} ) = \dim(\mathbb{V} ) \implies \mathbb{W} = \mathbb{V}$ 

- 증명 

    $\mathbb{W} = \{0\}$ 이면 $\mathbb{W}$ 는 유한차원이고 $\dim(\mathbb{W} ) = 0 \leq \dim(\mathbb{V} )$ 이다. ▲ 

    $\mathbb{W} \neq \{0\}$ 이면 영이 아닌 벡터 $x_1$ 에 대하여 $x_1 \in \mathbb{W}$ 이다. 이때 $\{x_1\}$ 은 일차독립인데 이 집합이 일차독립이 되도록 $\mathbb{W}$ 에서 $x_1, x_2, \dots, x_k$ 를 꺼내서 $\{x_1, \dots, x_k\}$ 를 만들자. $\mathbb{V}$ 의 일차독립인 집합의 기수는 $\dim(\mathbb{V} )$ 와 같거나 작으므로 $k \leq \dim(\mathbb{V} )$ 이다. 이제 이 집합에 $\mathbb{W}$ 의 임의의 벡터를 하나만 더해도 일차종속이 된다. 
    
    그러면 정리 1.7 "벡터공간 $\mathbb{V}$ 와 일차독립인 부분집합 $S$ 와 벡터 $v \in \mathbb{V} \text{ \textbackslash } S$ 에 대하여 $S \cup \{v\}$ 가 일차종속이기 위한 필요충분조건은 $v \in \text{span}(S)$ 이다." 에 의하여 $\text{span}(\{x_1, \dots, x_k\}) = \mathbb{W}$ 이므로 이는 $\mathbb{W}$ 의 기저이다. 그러므로 $k = \dim(\mathbb{W} ) \leq \dim(\mathbb{V} )$ 이다. ▲ 

    $\dim(\mathbb{W} ) = \dim(\mathbb{V} )$ 이면 $\mathbb{W}$ 의 기저의 기수는 $\dim(\mathbb{V} )$ 이고, 일차독립인 $\mathbb{V}$ 의 부분집합이다. 그러면 정리 1.10 따름정리 2 "벡터공간 $\mathbb{V}$ 에 대하여 다음이 성립한다. $S \subset \mathbb{V}$ 가 일차독립이고 $\text{card}(S) = \dim(\mathbb{V} )$ 이면 기저이다." 에 의하여 $\mathbb{W}$ 의 기저는 $\mathbb{V}$ 의 기저가 되고, 결국 $\mathbb{W} = \mathbb{V}$ 가 된다. ■ 

- 예시 

    $\R ^{2}$ 은 $2$ 차원 벡터공간이므로 부분공간의 차원은 $0, 1, 2$ 이 될 수 있다. $0$차원 부분공간은 $\{0\}$ 이고, $2$차원 부분공간은 $\R ^{2}$ 이다. $1$차원 부분공간은 벡터 $v \in \R ^{2}$ 와 스칼라 $c \in \mathbb{F}$ 에 대한 집합 $\{c \cdot v : c \in \mathbb{F} \}$ 이다.

    벡터공간 $\R ^{2}$ 의 벡터들을 유클리드 공간의 점으로 대응시키면 이 벡터공간을 기하학적으로 해석할 수 있다. 즉, $0$차원 부분공간을 유클리드 공간의 원점으로, $1$차원 부분공간을 유클리드 공간의 원점을 지나는 직선으로, $2$차원 부분공간을 유클리드 평면 전체로 해석할 수 있다.

- 예시 

    위의 예시와 마찬가지로 $\R ^{3}$ 의 부분공간의 차원은 $0,1,2,3$ 이 될 수 있고 $2$차원인 부분공간은 유클리드 공간에서 평면으로, $3$차원 부분공간을 유클리드 공간 전체로 볼 수 있다.

!!! tldr "정리 1.11 따름정리"

    유한차원 $\mathbb{V}$ 의 벡터공간 $\mathbb{W}$ 에 대하여 $\mathbb{W}$ 의 임의의 기저를 확장하여 $\mathbb{V}$ 의 기저를 얻을 수 있다.

- 증명 

    $\mathbb{W}$ 의 기저를 $S$ 라 하면 $S$ 는 $\mathbb{V}$ 의 일차독립인 부분집합이므로 정리 1.10 따름정리 2 "벡터공간 $\mathbb{V}$ 에 대하여 다음이 성립한다. $L \subset \mathbb{V}$ 이 일차독립이면 $L \subset \beta$ 인 $\mathbb{V}$ 의 기저 $\beta$ 가 존재한다." 에 의하여 $\mathbb{V}$ 의 기저로 확장할 수 있다. ■ 

- 예시 

    체 $\mathbb{F}$ 의 스칼라 $a _{18}, a _{16}, \dots, a_2, a_0 \in \mathbb{F}$ 에 대한 다항식 

    $$ a _{18} x ^{18} + a _{16} x ^{16} + \dots + a _{2} x ^{2} + a_0 $$

    을 원소로 갖는 벡터공간 $\mathbb{W}$ 은 $\mathbb{P} _{18}(\mathbb{F} )$ 의 부분공간이다. $\mathbb{W}$ 의 기저는 $\{1, x ^{2}, \dots, x ^{16}, x ^{18}\}$ 인데 이는 $\mathbb{P} _{18}(\mathbb{F} )$ 의 표준기저 $\{1,x,x ^{2}, \dots, x ^{18}\}$ 의 부분집합이다.

> 라그랑주 보간법 pass. 이해는 다 해서 언제나 정리할 수 있음

# 일차독립인 극대 부분집합

여기에서는 "기저와 차원" 의 정리들을 무한차원에서 성립하도록 일반화한다. 이것의 최종 목표는 모든 벡터공간에 기저가 존재함을 보이는 것이다. 이 사실은 무한차원을 다룰 때 중요한데, 왜냐하면 무한차원의 기저를 구체적으로 기술하기란 어렵기 때문이다. 가령 유리수체의 실수 벡터공간의 기저가 어떤 모양인지 상상이 안가지만, 어쨌든 존재하기는 한다. 이제 무한차원으로 일반화를 할텐데 수학적 귀납법을 더 이상 사용할 수 없으므로 그 대신 하우스도르프 극대원리를 사용한다.

!!! note

    아래의 논의는 순서관계를 포함관계로 상정한다.

!!! tldr ""

    극대(maximal) : 집합족 $\mathcal{F}$ 에 대하여 $S \in \mathcal{F}, M \subset S \implies S = M$ 이면 $M$ 을 포함관계에 의한 극대라고 한다.

- 예시 

    집합 $S$ 에 대하여 집합족 $\mathcal{F} = 2 ^{S}$ 을 정의하면 이것의 극대원소는 자명하게 $S$ 이다.

- 예시 

    무한집합 $S$ 에 대하여 $\mathcal{F} = 2 ^{S}$ 을 정의하면 이것의 극대원소는 존재하지 않는다. 
    
    $$ \forall M \in \mathcal{F}, \exists s \text{ s.t. } s \in S \land s \not\in M \implies M \cup \{s\} \in 2 ^{S}$$

    이기 때문이다.

!!! tldr ""

    사슬(chain) : 집합족 $\mathcal{C}$ 에 대하여 

    $$ \forall A, B \in \mathcal{C}, A \subset B \lor B \subset A $$

    이면 $\mathcal{C}$ 를 사슬이라 한다. 

- 사슬이란 그 속의 원소가 항상 비교가능한 집합을 뜻한다.

- 예시 

    집합 $A_n = \{1,2,\dots,n\}$ 에 대한 집합족 $\mathcal{C} = \{A_n : n = 1,2,3, \dots\}$ 은 사슬이다.

!!! tldr ""

    하우스도르프 극대원리 : 집합족 $\mathcal{F}$ 의 임의의 사슬 $\mathcal{C}$ 에 대하여 $\exists U \in \mathcal{F} \text{ s.t. } \mathcal{C} \subset U$ 이면 $\mathcal{F}$ 에는 극대원소가 있다. 

- (*보통 하우스도르프 극대원리는 부분순서집합은 극대사슬을 가진다고 표현되지만, 이 책에서는 포함관계에 의한 부분순서관계를 표현하려고 집합족 $\mathcal{F}$ 의 임의의 사슬 $\mathcal{C}$ 에 대하여 $\mathcal{C}$ 을 포함하는 사슬 $U$ 가 존재한다고 말한 것 같다. 이렇게 말하면 집합족 $\mathcal{F}$ 에 포함관계에 의한 부분순서가 부여되고, 하우스도르프 극대원리에 의하여 $\mathcal{F}$ 에 극대원소가 있음을 말할 수 있다.*)

- 하우스도르프 극대원리는 집합족이 특정 조건을 만족하면 극대원소를 가짐을 말해준다.

!!! tldr ""

    벡터공간의 기저는 일차독립인 극대 부분집합이다.

- 증명 

    벡터공간 $\mathbb{V}$ 와 그 기저 $\beta$ 에 대하여 기저의 정의에 따라 $\beta$ 는 일차독립이다. ▲ 
    
    $v \in \mathbb{V}, v \not\in \beta$ 이면 $\text{span}(\beta ) = \mathbb{V}$ 에서 정리 1.7 "벡터공간 $\mathbb{V}$ 와 일차독립인 부분집합 $S$ 와 벡터 $v \in \mathbb{V} \text{ \textbackslash } S$ 에 대하여 $S \cup \{v\}$ 가 일차종속이기 위한 필요충분조건은 $v \in \text{span}(S)$ 이다." 에 의하여 $\beta \cup \{v\}$ 는 일차종속이므로 $\beta$ 가 일차독립인 극대 부분집합이다. ■ 

!!! tldr "정리 1.12"

    벡터공간 $\mathbb{V}$ 와 $\text{span}(S) = \mathbb{V}$ 인 $S \subset V$ 에 대하여 $\beta$ 가 $S$ 의 일차독립인 극대 부분집합이면 $\beta$ 는 $\mathbb{V}$ 의 기저이다.

- 증명

    $S \not \subset \text{span}(\beta )$ 이면 $v \in S \text{ \textbackslash } \text{span}(\beta )$ 가 존재하여 정리 1.7 "벡터공간 $\mathbb{V}$ 와 일차독립인 부분집합 $S$ 와 벡터 $v \in \mathbb{V} \text{ \textbackslash } S$ 에 대하여 $S \cup \{v\}$ 가 일차종속이기 위한 필요충분조건은 $v \in \text{span}(S)$ 이다." 에 의하여 $\beta \cup \{v\}$ 를 일차독립으로 만든다. 이는 $\beta$ 가 일차독립인 극대 부분집합이라는 것에 모순이다.

    그러므로 $S \subset \text{span}(\beta )$ 이다. 이때 $\text{span}(S) = \mathbb{V}$ 이므로 정리 1.5 "벡터공간 $\mathbb{V}$ 의 임의의 부분집합 $S$ 에 대하여 $S$ 를 포함하는 $\mathbb{V}$ 의 부분공간은 $\text{span}(S)$ 을 포함한다." 에 의하여 $\text{span}(S) = \mathbb{V} \subset \text{span}(\beta )$ 이다. $\text{span}(\beta ) \subset \mathbb{V}$ 은 자명하므로 $\text{span}(\beta ) = \mathbb{V}$ 이다. ■ 

!!! tldr ""

    일차독립인 극대 부분집합(maximal linearly independent subset) : 벡터공간 $\mathbb{V}$ 의 부분집합 $S$ 에 대하여 $S$ 의 부분집합 $B$ 가 다음을 만족하면 일차독립인 극대 부분집합이다.

    1. $B$ 는 일차독립이다. 

    2. $B$ 를 포함하고 일차독립인 $S$ 의 부분집합은 오직 $B$ 이다.

- $S$ 가 $\mathbb{V}$ 를 생성한다면, 이 정의는 정리 1.12 에 의하여 기저의 정의와 같다. 

!!! tldr ""

    벡터공간의 기저와 벡터공간의 일차독립인 극대부분집합은 동치이다. 

- 이 정리는 지금까지의 논의에 의하여 자명하다.

- 이 정리는 모든 벡터공간마다 일차독립인 극대부분집합이 존재함을 보이는 것이 모든 벡터공간이 기저를 가짐을 보이는 것과 같다는 것을 말해준다. 그러므로 지금의 최대 목표인 "모든 벡터공간에 기저가 존재한다" 를 보이기 위하여 바로 다음의 정리를 증명하자.

!!! tldr "정리 1.13"

    벡터공간은 일차독립인 극대 부분집합을 갖는다. 

- 증명 

    벡터공간 $\mathbb{V}$ 과 일차독립인 집합 $S \subset \mathbb{V}$ 에 대하여 $S$ 를 포함하는 일차독립인 $\mathbb{V}$ 의 부분집합을 원소로 갖는 집합족 $\mathcal{F}$ 을 정의하자.
    
    이제 $\mathcal{F}$ 의 임의의 사슬 $\mathcal{C}$ 에 대하여 $\exists U \in \mathcal{F} \text{ s.t. } \mathcal{C} \subset U$ 임을 보일 것이다. 그러면 하우스도르프 극대원리에 의하여 $\mathcal{F}$ 가 극대원소를 가짐을 보일 수 있고 모든 증명이 끝난다.

    $\mathcal{C} = \varnothing$ 일때 $U = S$ 로 정의하면 증명이 끝난다. ▲ 

    $\mathcal{C} \neq \varnothing$ 일때 $U = \bigcup_{}^{}\mathcal{C}$ 로 정의하면, $\mathcal{C} \subset U$ 는 자명하므로 $U \in \mathcal{F}$ 임을 보이면 증명이 끝난다. 즉, $U$ 가 일차독립인 $\mathbb{V}$ 의 부분집합이고 $S$ 를 포함함을 보이는 것이다. $U$ 는 당연히 $S$ 를 포함하는 $\mathbb{V}$ 의 부분집합이므로 일차독립인 것만 보이면 된다.

    $U$ 의 임의의 서로 다른 벡터 $u_1, u_2, \dots, u_n \in U$ 와 스칼라 $a_1, a_2, \dots, a_n$ 에 대하여 $a_1u_1 + a_2u_2 +\dots +a_nu_n = 0$ 이라고 하자. 그러면 $u_i \in U \implies \exists A_i \in \mathcal{C} \text{ s.t. } u_i \in A_i$ 이다. $\mathcal{C}$ 는 포함관계에 의한 사슬이므로 $A_i$ 들을 모두 포함하는 $A_k$ 가 존재한다. 그러면 $\forall u_i, u_i \in A_k$ 이다. $A_k \in \mathcal{F}$ 이므로 $A_k$ 는 일차독립이고 따라서 $a_1u_1 + a_2u_2 +\dots +a_nu_n = 0 \implies a_1 = a_2 = \dots = a_n = 0$ 이다. 그러므로 $U$ 는 일차독립이다. ■ 

!!! tldr "정리 1.13 따름정리"

    벡터공간은 기저를 갖는다.

- 증명 

    정리 1.13 과 정리 "벡터공간의 기저와 벡터공간의 일차독립인 극대부분집합은 동치이다." 에 의하여 증명이 끝난다. ■ 

!!! tldr ""

    무한차원 벡터공간의 모든 기저의 기수가 같다.

- 정리 1.10 따름정리 1 "벡터공간 $\mathbb{V}$ 가 유한집합인 기저를 포함하면 $\mathbb{V}$ 의 모든 기저는 유한집합이며, 기수가 같다." 을 무한차원으로 유추해보면 이 명제를 얻을 수 있다. 

- 이때 무한집합의 기수를 비교할 때에는 이미 잘 알고 있듯이 전단사 사상이 존재함을 보이면 기수가 서로 같다고 말할 수 있다.

- 증명 

    N. Jacobson, Lectures in Abstract Algebra, vol. 2, Linear Algebra, D. Van Nostrand Company, New York, 1953, p. 240 에서 증명을 확인할 수 있다.

!!! tldr ""

    무한차원 벡터공간 $\mathbb{V}$ 에 대하여 다음은 동치이다.
    
    1. $\beta (\subset \mathbb{V})$ 가 기저이다. 

    2. 영이 아닌 벡터 $v \in \mathbb{V}$ 에 대하여 $v = c_1u_1 + c_2u_2 + \dots + c_nu_n$ 을 만족하는 벡터 $u_1, u_2, \dots, u_n \in \beta$ 와 영이 아닌 스칼라 $c_1, c_2, \dots, c_n$ 이 유일하게 존재한다.

- 이 정리는 정리 1.8 "벡터공간 $\mathbb{V}$ 와 서로 다른 벡터 $u_1, u_2, \dots, u_n \in \mathbb{V}$ 에 대한 집합 $\beta = \{u_1, u_2, \dots, u_n\}$ 가 $\mathbb{V}$ 에 대하여 다음은 동치이다. 1. 집합 $\beta = \{u_1, u_2, \dots, u_n\}$ 가 $\mathbb{V}$ 의 기저이다. 2. 임의의 $v \in \mathbb{V}$ 를 유일한 스칼라 $a_1, a_2, \dots, a_n$ 에 대한 $\beta$ 의 일차결합으로 나타낼 수 있다." 을 무한차원으로 일반화한 것이다.

- 증명 

!!! tldr ""

    벡터공간 $\mathbb{V}$ 의 부분집합 $S_1, S_2$ 에 대하여 $S_1 \subset S_2$ 이고, $S_1$ 이 일차독립이고, $\text{span}(S_2) = \mathbb{V}$ 이면 $S_1 \subset \beta \subset S_2$ 인 기저 $\beta$ 가 존재한다.

- 이 정리는 정리 1.9 "유한집합 $S$ 가 벡터공간 $\mathbb{V}$ 를 생성하면 $S$ 의 부분집합 중에 $\mathbb{V}$ 의 기저가 존재한다." 를 무한차원으로 일반화한 것이다.

- 증명

!!! tldr ""

    벡터공간 $\mathbb{V}$ 의 기저 $\beta$ 와 $\mathbb{V}$ 의 일차독립인 부분집합 $S$ 에 대하여 $S \cup S_1$ 가 $\mathbb{V}$ 의 기저인 $S_1 \subset \beta$ 이 존재한다.

- 이 정리는 정리 1.10 "대체정리(replacement theorem) : 집합 $G$ 가 벡터공간 $\mathbb{V}$ 에 대하여 $\text{span}(G) = \mathbb{V}$ 이고, $L \subset \mathbb{V}$ 이 일차독립이면 다음이 성립한다. 1. $\text{card}(L) \leq \text{card}(G)$ 2. $\exists H \subset G \text{ s.t. } \text{span}(L \cup H) = \mathbb{V} \land \text{card}(H) = \text{card}(G) - \text{card}(L)$" 을 무한차원으로 일반화한 것이다. 

- 증명
