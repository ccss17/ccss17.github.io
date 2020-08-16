# 직교성과 최소제곱법 

## 내적, 길이, 직교

!!! tldr ""

    내적(inner product) 또는 스칼라곱(dot product) : $\mathbb{R} ^{n}$ 공간 상의 두 $n \times 1$ 행렬, 즉 두 벡터 $u, v$ 의 내적은 행렬곱
    
    $$ u \cdot v = u ^{T}v $$
    
    이다.

- $u ^{T}$ 는 $u$ 의 전치벡터로써 $1 \times n$ 행렬이 되므로 $n \times 1$ 행렬 $v$ 와 행렬곱 연산을 할 수 있다.

    - 또한 행렬곱연산을 했을 시 $1 \times 1$ 행렬이 되며

        이것을 간단히 스칼라(단일 실수) 로 표현하기도 한다.

- 예시 

    두 벡터

    $$ u = \begin{bmatrix} 2\\-5\\1 \end{bmatrix}, v =\begin{bmatrix} 3\\2\\-3 \end{bmatrix} $$

    에 대한 내적 $u \cdot v, v \cdot u$ 을 구해보자. 

    $$ u \cdot v = u ^{T}v = \begin{bmatrix} 2&-5&1\\ \end{bmatrix} \begin{bmatrix} 3\\2\\-3 \end{bmatrix} = -1 $$

    $$ v \cdot u = v ^{T}u = \begin{bmatrix} 3&2&-3\\ \end{bmatrix} \begin{bmatrix} 2\\-5\\-1 \end{bmatrix} = -1 $$

!!! tldr ""

    내적의 성질 : $\mathbb{R} ^{n}$ 공간 상의 벡터 $u, v, w$ 와 스칼라 $c$ 에 대하여 다음이 성립한다.
    
    1. (교환법칙) $u \cdot v = v \cdot u$
    
    2. (분배법칙) $(u + v) \cdot w = v \cdot w + v \cdot w$
    
    3. (분배법칙) $(cu) \cdot v = c (u \cdot v) = u \cdot(cv)$
    
    4. $u \cdot u \geq 0$, 그리고 $u \cdot u = 0 \iff u = 0$

- $2, 3$ 을 사용하여

    $$ (c_1u_1 + \dots + c_pu_p)\cdot w = c_1(u_1 \cdot w) + \dots + c_p(u_p \cdot w) $$

    을 연역할 수 있다.

!!! tldr ""

    벡터의 크기(length) 또는 노름(norm) : $\mathbb{R} ^{n}$ 공간 상의 벡터 $v$ 가 성분 $v_1, \dots, v_n$ 을 가질 때 양수 스칼라
    
    $$ ||v|| = \sqrt[]{v \cdot v} = \sqrt[]{v_1^{2} + v_2 ^{2} + \dots + v_n ^{2}} $$
    
    를 벡터의 크기 또는 노름이라고 정의한다.

- 직선 사이의 크기, 평면 사이의 크기, 공간 사이의 크기를 $n$ 차원에 적용되도록 일반화 한 것이다. 

- 벡터 $u$ 에 대한 내적의 성질 때문에 $v \cdot v$ 는 음이 아닌 실수이므로 $\sqrt[]{v \cdot v}$ 이 실수로 잘 정의된다.

- 예시 

    $\mathbb{R} ^{2}$ 공간 상의 벡터 $v = \begin{bmatrix} a\\b \end{bmatrix}$ 를 좌표평면 상의 벡터 $\big < a, b \big >$ 로 생각할 수 있다. 

    이때 $||v||$ 는 원점에서 $v$ 까지의 선분의 길이이다.

    $\mathbb{R} ^{3}$ 공간 상의 벡터, 즉 $3$ 차원 공간좌표에서도 마찬가지로 원점에서 $v$ 까지의 길이로 생각할 수 있다.

!!! tldr ""

    벡터의 크기의 성질 : 임의의 스칼라 $c$ 와 벡터 $v$ 에 대하여 벡터 $cv$ 의 크기는 $v$ 의 크기 $||v||$ 의 $|c|$ 배이다.

- 즉,

    $$ ||cv|| = |c| \cdot  ||v|| $$

    이다. 

    $$ \because ||cv|| ^{2} = (cv)\cdot (cv) = c ^{2} v \cdot v = c ^{2} ||v|| ^{2} $$

    이기 때문이다.

!!! tldr ""

    단위벡터(unit vector) : 크기가 $1$ 인 벡터이다.

- 예시 

    $\mathbb{R} ^{2}$ 공간 상의 벡터 $u = \begin{bmatrix} 1\\0 \end{bmatrix}$ 는 단위벡터이다. 

    $\mathbb{R} ^{3}$ 공간 상의 벡터 $u = \begin{bmatrix} 0\\1\\0 \end{bmatrix}$ 는 단위벡터이다.

!!! tldr ""

    정규화(normalizatoin) : 벡터 $v$ 로부터 단위벡터 $u$ 를 얻는 과정이다.

- $0$ 이 아닌 벡터 $v$ 를 그 크기로 나누면 $v$ 방향을 향하는 단위벡터를 얻을 수 있다. 

    - 즉,

        $$ u = \frac{v}{||v||} $$

        의 크기는 

        $$ ||u|| = \frac{||v||}{||v||} = 1$$

        이다. 

- 예시 

    $\mathbb{R} ^{4}$ 공간 상의 벡터 $v = \begin{bmatrix} 1\\-2\\2\\0 \end{bmatrix}$ 에 대하여 $v$ 의 방향을 방하는 단위벡터 $u$ 를 구해보자.

    벡터 $v$ 의 크기는 

    $$ ||v|| ^{2} = v \cdot v = (1)^{2}+(-2)^{2}+(2)^{2}+(0)^{2}=9 $$

    에서 

    $$ ||v|| = \sqrt[]{9} = 3 $$

    이다. 따라서 $v$ 에 $\dfrac{1}{||v||}$ 를 곱하면

    $$ \therefore  u = \frac{1}{||v||}v = \frac{1}{3}v = \begin{bmatrix} 1/3\\-2/3\\2/3\\0 \end{bmatrix} $$

    을 얻는다.

!!! tldr ""

    두 벡터 $u, v$ 사이의 거리(distance) : $\mathbb{R} ^{n}$ 상의 두 벡터 $u, v$ 의 거리는 벡터 $u - v$ 의 크기
    
    $$ \text{dist}(u, v) = ||u - v|| $$
    
    이다.

- $\mathbb{R} ^{3}$ 공간 상의 두 벡터 $u = \begin{bmatrix} u_1\\u_2\\u_3 \end{bmatrix}, v = \begin{bmatrix} v_1\\v_2\\v_3 \end{bmatrix}$ 의 거리는 

    $$ \text{dist}(u, v) = ||u - v|| = \sqrt[]{(u - v) \cdot (u - v)} = \sqrt[]{(u_1 - v_1) ^{2} + (u_2 - v_2) ^{2} + (u_3 - v_3) ^{2}} $$

    이다. 

- 직선 사이의 거리, 평면 사이의 거리, 공간 사이의 거리를 $n$ 차원에 적용되도록 일반화 한 것이다. 

- 예시 

    두 벡터 

    $$ u = \begin{bmatrix} 7\\1 \end{bmatrix}, v = \begin{bmatrix} 3\\2 \end{bmatrix} $$

    의 거리를 구해보자. 

    $$ u - v = \begin{bmatrix} 4\\-1 \end{bmatrix} $$

    이므로 $u$ 와 $v$ 의 거리는 

    $$ ||u - v|| = \sqrt[]{4 ^{2} + (-1)^{2}} = \sqrt[]{17} $$

    이다.

!!! tldr ""

    벡터 $u, v$ 의 직교(orthogonal) : $\mathbb{R} ^{n}$ 상의 두 벡터 $u ,v$ 가
    
    $$ u \cdot v = 0 $$
    
    또는 
    
    $$ ||u + v|| ^{2} = ||u|| ^{2} + ||v||^{2} $$
    
    를 만족하면 서로 직교한다.

- 증명 

    $\mathbb{R} ^{n}$ 상에서 원점을 지나고 벡터 $u, v$ 에 결정되는 두 직선을 생각하자.

    두 직선이 수직일 필요충분조건은 $u$ 에서 $v$ 까지의 거리가 $u$ 에서 $-v$ 까지의 거리와 같다는 것이다.

    ![캡처](https://user-images.githubusercontent.com/16812446/80373873-b20d1b80-88d0-11ea-9423-356b765a3c14.PNG)

    이것은 거리의 제곱들이 서로 같음을 의미한다.

    $u, -v$ 의 거리의 제곱은

    $$ [\text{dist}(u, -v)] ^{2} = ||u -(-v)^{2}|| = ||u + v|| ^{2} $$

    $$ = (u+v)\cdot (u+v) $$

    $$ = u \cdot u + u \cdot v + v \cdot u + v \cdot v $$

    $$ = ||u||^{2} + ||v|| ^{2} + 2 u \cdot v $$

    이다. 이제 $-v$ 만 $v$ 로 바꿔서 계산해보면

    $$ [\text{dist}(u, -v)] ^{2} = ||u||^{2} + ||-v|| ^{2} + 2 u \cdot (-v) $$

    $$ = ||u||^{2} + ||v|| ^{2} - 2 u \cdot v $$

    이다. 그러므로 두 거리의 제곱이 같을 조건은 결국 

    $$ 2 u \cdot v = - 2 u \cdot v $$

    에서 

    $$ \therefore u \cdot v = 0 $$

    이다. 

- 유클리드 기하학의 수직 개념을 $\mathbb{R} ^{n}$, 즉 $n$ 차원에서 적용할 수 있도록 일반화한 것이다. 

- 모든 벡터 $v$ 은 $0 ^{T}v = 0$ 이므로 $\mathbb{R} ^{n}$ 에서 영벡터는 모든 벡터와 직교한다. 

## 직교여공간

!!! tldr ""

    부분공간과 직교하는 벡터 : 어떤 벡터 $z$ 가 $\mathbb{R} ^{n}$ 의 부분공간 $W$ 의 모든 벡터와 직교한다면
    
    $z$ 는 $W$ 에 직교한다고 말한다.

!!! tldr ""

    직교여공간(orthogonal complement) : 부분공간 $W$ 와 직교하는 모든 벡터의 집합
    
    $$ W ^{\perp } $$
    
    이다.

- 예시 

    $W$ 를 $\mathbb{R} ^{3}$ 공간에서 원점을 지나는 평면을 나타내는 부분공간이라고 하고

    $L$ 을 원점을 지나며 $W$ 평면에 수직인 직선이라고 하자.

    영이 아닌 벡터 $z, w$ 에 대하여 $z$ 는 직선 $L$ 위에 있고 $w$ 는 평면 $W$ 에 있다면, 

    벡터 $z$ 와 $w$ 는 서로 수직이다. 즉, 

    $$ z \cdot w = 0 $$

    이다. 따라서 $L$ 위의 모든 벡터는 $W$ 안의 임의의 벡터와 직교한다.

    그러므로 $L$ 은 $W$ 안에 있는 모든 벡터와 직교하는 벡터로 구성되었다. 즉, 

    $$ \therefore L = W ^{\perp } $$

    이다. ■  

    그런데 $W$ 또한 $L$ 위의 모든 벡터와 직교하는 벡터로 구성되었다. 즉,

    $$ \therefore W = L ^{\perp } $$

    이다. ■

!!! tldr ""

    직교여공간의 성질
    
    1. 벡터 $x$ 가 $W ^{\perp }$ 의 원소일 필요충분조건은 $x$ 가 $W$ 를 생성하는 집합의 모든 벡터와 직교하는 것이다.
    
    2. $W ^{\perp }$ 는 $\mathbb{R} ^{n}$ 의 부분공간이다.

!!! tldr ""

    행렬의 행공간과 영공간의 직교여공간에 의한 관계 : 행렬 $A$ 를 $m \times n$ 행렬이라 할 때 $A$ 의 행공간 $\text{Row} A$ 에 대한 직교여공간은 $A$ 의 영공간 $\text{Nul} A$ 이고,
    
    $A$ 의 영공간 $\text{Nul} A$ 에 대한 직교여공간은 $A$ 의 행공간 $\text{Row} A$ 이다.
    
    $$ (\text{Row} A)^{\perp } = \text{Nul} A, (\text{Nul} A)^{\perp } = \text{Row} A $$

- 증명 

    **구체화 필요**

## 직교집합

!!! tldr ""

    직교집합(orthogonal set) : $\mathbb{R} ^{n}$ 공간의 벡터 집합 $S = \{u_1, \dots, u_p\}$ 에서 그 집합의 모든 서로 다른 벡터가 직교한다면, 즉
    
    $i \neq j$ 에 대하여 $u_j \cdot u_i = 0$ 이면 벡터 집합 $S$ 는 직교집합이다.

- 즉, 서로 다른 모든 두 벡터가 직교하는 집합이 직교집합이다. 

- 예시 

    벡터 $\displaystyle u_1 = \begin{bmatrix} 3\\1\\1 \end{bmatrix}, u_2 = \begin{bmatrix} -1\\2\\1 \end{bmatrix}, u_3 = \begin{bmatrix} -1/2\\-2\\7/2 \end{bmatrix}$ 에 대한 벡터 집합 $S = \{u_1,u_2,u_3\}$ 이 직교집합인지 확인해보자.

    각각의 서로 다른 벡터에 대한 내적은 모두

    $$ u_1 \cdot u_2 = 0 $$

    $$ u_1 \cdot u_3 = 0 $$

    $$ u_2 \cdot u_3 = 0 $$

    이다. 그러므로 $S$ 는 직교집합이다. 

- $S = \{u_1, u_2, \dots, u_p\}$ 를 $\mathbb{R} ^{n}$ 의 $0$ 이 아닌 벡터들로 이루어진 직교집합이라 할 때 

    집합 $S$ 는 일차독립이고 $S$ 는 $S$ 에 의해 생성된 부분공간의 기저이다.

    - 증명 

        스칼라 $c_1, \dots, c_p$ 에 대하여 $0 = c_1u_1 + \dots + c_pu_p$ 이면 벡터 $u_1$ 은

!!! tldr ""

    직교기저(orthogonal basis) : $\mathbb{R} ^{n}$ 의 부분공간 $W$ 의 기저인 동시에 직교인 집합을 $W$ 의 직교기저라 한다.

## 직교사영

!!! tldr ""

    직교사영(orthogonal projection) :

## 정규직교집합

!!! tldr ""

    정규직교집합(orthonormal set) : 벡터집합 $\{u_1, \dots, u_p\}$ 가 단위벡터로 이루어진 직교집합일 때 정규직교집합이라 한다.

!!! tldr ""

    정규직교기저(orthonormal basis) : 부분공간 $W$ 의 기저가 되는 정규직교집합이다.

- 예시 

    $\mathbb{R} ^{n}$ 의 표준기저 $\{e_1, \dots, e_n\}$ 은 정규직교기저이다.

!!! tldr ""

    직교행렬(orthogonal matrix) : 정사각 정칙행렬 $U$ 가 $U ^{-1} = U ^{T}$ 를 만족할 때 $U$ 를 직교행렬이라 한다.
