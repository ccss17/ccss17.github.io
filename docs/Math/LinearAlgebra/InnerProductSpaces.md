!!! info "ref"

    Stephen H. Friedberg, Linear Algebra, 4th Edition

# Inner product, Norm

!!! tldr "켤레복소수(complex conjugate)"

    복소수 $a+bi$ 의 켤레복소수는 $\overline{a+bi} = a-bi$ 이다.

!!! tldr "내적(inner product)"

    $\mathbf{F}$-벡터공간 $\mathbf{V}$ 에서 정의된 내적은 $x, y, z \in \mathbf{V}, c \in \mathbf{F}$ 에 대한 다음의 조건을 만족하는 함수 $\big < \cdot , \cdot \big >: \mathbf{V} \times \mathbf{V}\to \mathbf{F}$ 이다.

    1. $\big < x + z, y \big > = \big < x, y \big > + \big < z, y \big >$

    2. $\big < cx, y \big > = c \big < x, y \big >$

    3. $\overline{\big < x, y\big >} = \big < y, x\big >$

    4. $x \neq 0 \implies \big < x, x \big > > 0$

- 즉, 내적은 $\mathbf{F}$-벡터공간의 두 벡터 순서쌍을 $\mathbf{F}$ 로 대응시키는 함수이다.

- 3) 의 $\bar{z}$ 는 $z$ 의 켤레복소수이다. 켤레복소수의 정의에 의하여 $\mathbf{F}=\R$ 일 때 3) 은 $\big < x, y \big > = \big < y, x \big >$ 가 된다.

- 1) 과 2) 는 내적이 첫번째 성분에 대하여 선형임을 말해준다. 즉, $a_1, a_2, \dots, a_n \in \mathbf{F}, y, v_1, v_2, \dots, v_n \in \mathbf{V}$ 에 대하여 다음이 성립한다.

    $$ \bigg <\sum_{i=1}^{n}a_iv_i,y\bigg > = \sum_{i=1}^{n}a_i \big <v_i, y \big > $$

- 우리가 무의식적으로 평면좌표 $\R ^{2}$ 나 공간좌표 $\R ^{3}$ 에서 사용하던 각, 길이, 직교성을 일반적인 $\R$-벡터공간이나 $\mathbb{C}$-벡터공간에서 성립하도록 엄밀히 정의해볼 것이다. 이 기하학적 정의는 모두 내적과 관련이 있으므로 내적부터 정의해야 한다.

    내적의 정의를 보면 알 수 있듯이 내적은 특정하게 정의된 함수가 아니라 내적의 조건을 만족하는 모든 함수가 내적으로 불리는 것이다. 다만, 우리가 평면좌표나 공간좌표에서 사용하던 내적과 유클리드 거리의 개념이 다음과 같은 표준 내적으로 정의되었던 것이다.

- 예시 

    벡터공간 $\mathbf{V}$ 의 어떤 내적 $\big <x,y \big >$ 을 기반으로 또 다른 내적 $\big <x,y \big >' = r \big <x,y \big >$ 을 정의할 수 있다. $r \leq 0$ 이면 조건 4) 가 성립하지 않는다.

- 예시 

    폐구간 $[0,1]$ 에서 연속인 실함수를 원소로 하는 벡터공간 $\mathbf{C}([0, 1])$ 에서 함수 $\big <f,g \big > = \int_{0}^{1}f(t)g(t)dt$ 을 정의하자.

    적분은 $f$ 에 대한 선형이므로 내적의 조건 1), 2) 가 만족된다. 조건 3) 은 자명하게 성립한다. $f$ 가 영함수가 아니면 $f ^{2}$ 는 연속함수이므로 $[0,1]$ 에 속하는 적절한 부분공간에서 $0$ 이 아니므로 $\big <f,f \big > \displaystyle =\int_{0}^{1}[f(t)]^{2}dt>0$ 이다. 따라서 함수 $\big <f,g \big >$ 는 내적이다.

!!! tldr "표준 내적(standard inner product)"

    표준 내적은 $\mathbf{F}^{n}$ 의 두 벡터 $x = (a_1, a_2, \dots, a_n), y = (b_1, b_2, \dots, b_n)$ 에 대하여 다음과 같이 정의된 내적 $\big <\cdot , \cdot \big > : \mathbf{F}^{n} \times \mathbf{F}^{n} \to \mathbf{F}$ 이다.

    $$ \big <x,y \big > = \sum_{i=1}^{k}a_i \overline{b_i} $$

- 표준 내적이 내적임은 쉽게 증명할 수 있다.

- $\mathbf{F}= \R$ 이면 켤레복소수를 생각할 필요 없다. 이 경우 우리가 이미 배웠을 가능성이 높은 $big\big <x,y \big >$ 가 아니라 $x \cdot y$ 로 표기하는 내적과 같아진다.

- 예시

    $x = (1+i, 4), y = (2-3i, 4+5i) \in \mathbb{C} ^{2}$ 와 표준내적 $\big <\cdot ,\cdot  \big >$ 대하여 다음이 성립한다.

    $$ \big <x,y \big >=(1+i)(2+3i)+4(4-5i)=15-15i
    $$

!!! tldr "켤레 전치행렬(conjugate transpose), 수반행렬(adjoint)"

    행렬 $A \in \mathbf{M}_{m \times n}(\mathbf{F})$ 와 각 $i, j$ 에 대하여 $(A ^{*}) _{ij} = \overline{A}_{ji}$ 인 $n \times m$ 행렬 $A ^{*}$ 를 $A$ 의 수반행렬이라 한다.

- 전치행렬의 켤레복소수를 구한 것이 수반행렬이다. 따라서 행렬의 모든 성분이 실수이면 수반행렬은 전치행렬이다.

- 예시

    $$ A = \begin{pmatrix} i&1+2i\\ 2&3+4i\\ \end{pmatrix}\implies A {}^{*} = \begin{pmatrix} -i&2\\ 1-2i&3-4i\\ \end{pmatrix} $$

