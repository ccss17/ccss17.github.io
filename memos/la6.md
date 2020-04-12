# [ccss17.github.io](https://ccss17.github.io)

# 선형대수학 메모 6

# 직교성과 최소제곱법 

## 내적, 길이, 직교

- 내적(inner product) 또는 스칼라곱(dot product) : $\Re ^{n}$ 공간 상의 두 $n \times 1$ 행렬, 즉 두 벡터 $u, v$ 의 내적은 행렬곱

  $$ u ^{T}v $$

  이다. 

  - $u ^{T}$ 는 $u$ 의 전치벡터로써 $1 \times n$ 행렬이 되므로 $n \times 1$ 행렬 $v$ 와 행렬곱 연산을 할 수 있다.

    - 또한 행렬곱연산을 했을 시 $1 \times 1$ 행렬이 되며
    
      이것을 간단히 스칼라(단일 실수) 로 표현하기도 한다.

  - $u \cdot v$ 로도 표기한다. 

  - 예시 

    두 벡터

    $$ u = \begin{bmatrix} 2\\-5\\1 \end{bmatrix}, v =\begin{bmatrix} 3\\2\\-3 \end{bmatrix} $$

    에 대한 내적 $u \cdot v, v \cdot u$ 을 구해보자. 

    $$ u \cdot v = u ^{T}v = \begin{bmatrix} 2&-5&1\\ \end{bmatrix} \begin{bmatrix} 3\\2\\-3 \end{bmatrix} = -1 $$

    $$ v \cdot u = v ^{T}u = \begin{bmatrix} 3&2&-3\\ \end{bmatrix} \begin{bmatrix} 2\\-5\\-1 \end{bmatrix} = -1 $$

- 내적의 성질 : $\Re ^{n}$ 공간 상의 벡터 $u, v, w$ 와 스칼라 $c$ 에 대하여 다음이 성립한다.

  1. (교환법칙) $u \cdot v = v \cdot u$

  2. (분배법칙) $(u + v) \cdot w = v \cdot w + v \cdot w$

  3. (분배법칙) $(cu) \cdot v = c (u \cdot v) = u \cdot(cv)$

  4. $u \cdot u \geq 0$, 그리고 $u \cdot u = 0 \Leftrightarrow u = 0$

  - $2, 3$ 을 사용하여

    $$ (c_1u_1 + \dots + c_pu_p)\cdot w = c_1(u_1 \cdot w) + \dots + c_p(u_p \cdot w) $$

    을 연역할 수 있다. 

- 벡터의 크기(length) 또는 노름(norm) : $\Re ^{n}$ 공간 상의 벡터 $v$ 가 성분 $v_1, \dots, v_n$ 을 가질 때 양수 스칼라

  $$ ||v|| = \sqrt[]{v \cdot v} = \sqrt[]{v_1 ^{2} + v_2 ^{2} + \dots + v_n ^{2}} $$

  를 벡터의 크기 또는 노름이라고 정의한다. 

  - 직선 사이의 크기, 평면 사이의 크기, 공간 사이의 크기를 $n$ 차원에 적용되도록 일반화 한 것이다. 

  - 벡터 $u$ 에 대한 내적의 성질 때문에 $v \cdot v$ 는 음이 아닌 실수이므로 $\sqrt[]{v \cdot v}$ 이 실수로 잘 정의된다.

  - 예시 

    $\Re ^{2}$ 공간 상의 벡터 $v = \begin{bmatrix} a\\b \end{bmatrix}$ 를 좌표평면 상의 벡터 $\big < a, b \big >$ 로 생각할 수 있다. 

    이때 $||v||$ 는 원점에서 $v$ 까지의 선분의 길이이다.

    $\Re ^{3}$ 공간 상의 벡터, 즉 $3$ 차원 공간좌표에서도 마찬가지로 원점에서 $v$ 까지의 길이로 생각할 수 있다. 

- 벡터의 크기의 성질 : 임의의 스칼라 $c$ 와 벡터 $v$ 에 대하여 벡터 $cv$ 의 크기는 $v$ 의 크기 $||v||$ 의 $|c|$ 배이다.

  - 즉,

    $$ ||cv|| = |c| \cdot  ||v|| $$

    이다. 

    $$ \because ||cv|| ^{2} = (cv)\cdot (cv) = c ^{2} v \cdot v = c ^{2} ||v|| ^{2} $$

    이기 때문이다.

- 단위벡터(unit vector) : 크기가 $1$ 인 벡터이다.

  - 예시 

    $\Re ^{2}$ 공간 상의 벡터 $u = \begin{bmatrix} 1\\0 \end{bmatrix}$ 는 단위벡터이다. 

    $\Re ^{3}$ 공간 상의 벡터 $u = \begin{bmatrix} 0\\1\\0 \end{bmatrix}$ 는 단위벡터이다. 

- 정규화(normalizatoin) : 벡터 $v$ 로부터 단위벡터 $u$ 를 얻는 과정이다.

  - $0$ 이 아닌 벡터 $v$ 를 그 크기로 나누면 $v$ 방향을 향하는 단위벡터를 얻을 수 있다. 

    - 즉,

      $$ u = \frac{v}{||v||} $$

      의 크기는 

      $$ ||u|| = \frac{||v||}{||v||} = 1$$

      이다. 

  - 예시 

    $\Re ^{4}$ 공간 상의 벡터 $v = \begin{bmatrix} 1\\-2\\2\\0 \end{bmatrix}$ 에 대하여 $v$ 의 방향을 방하는 단위벡터 $u$ 를 구해보자.

    벡터 $v$ 의 크기는 

    $$ ||v|| ^{2} = v \cdot v = (1)^{2}+(-2)^{2}+(2)^{2}+(0)^{2}=9 $$

    에서 

    $$ ||v|| = \sqrt[]{9} = 3 $$

    이다. 따라서 $v$ 에 $\dfrac{1}{||v||}$ 를 곱하면

    $$ \therefore  u = \frac{1}{||v||}v = \frac{1}{3}v = \begin{bmatrix} 1/3\\-2/3\\2/3\\0 \end{bmatrix} $$

    을 얻는다.

- 두 벡터 $u, v$ 사이의 거리(distance) : $\Re ^{n}$ 상의 두 벡터 $u, v$ 의 거리는 벡터 $u - v$ 의 크기

  $$ \text{dist}(u, v) = ||u - v|| $$

  이다. 

  - $\Re ^{3}$ 공간 상의 두 벡터 $u = \begin{bmatrix} u_1\\u_2\\u_3 \end{bmatrix}, v = \begin{bmatrix} v_1\\v_2\\v_3 \end{bmatrix}$ 의 거리는 

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

- 벡터 $u, v$ 의 직교(orthogonal) : $\Re ^{n}$ 상의 두 벡터 $u ,v$ 가

  $$ u \cdot v = 0 $$

  또는 

  $$ ||u + v|| ^{2} = ||u|| ^{2} + ||v||^{2} $$

  를 만족하면 서로 직교한다.

  - 증명 

    $\Re ^{n}$ 상에서 원점을 지나고 벡터 $u, v$ 에 결정되는 두 직선을 생각하자.

    두 직선이 수직일 필요충분조건은 $u$ 에서 $v$ 까지의 거리가 $u$ 에서 $-v$ 까지의 거리와 같다는 것이다. 이것은 거리의 제곱들이 서로 같음을 의미한다.

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

  - 유클리드 기하학의 수직 개념을 $\Re ^{n}$, 즉 $n$ 차원에서 적용할 수 있도록 일반화한 것이다. 

  - 모든 벡터 $v$ 은 $0 ^{T}v = 0$ 이므로 $\Re ^{n}$ 에서 영벡터는 모든 벡터와 직교한다. 

- 직교집합(orthogonal set) : $\Re ^{n}$ 공간의 벡터 집합 $S = \{u_1, \dots, u_p\}$ 에서 $i \neq j$ 에 대하여 $u_j \cdot u_i = 0$ 이면 벡터 집합 $S$ 는 직교집합이다. 

  - 즉, 서로 다른 모든 두 벡터가 직교하는 집합이 직교집합이다. 