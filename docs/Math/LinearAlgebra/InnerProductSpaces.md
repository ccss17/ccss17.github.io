!!! info "ref"

    Stephen H. Friedberg, Linear Algebra, 4th Edition

# Inner product

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

## Standard Inner Product

!!! tldr "표준 내적(standard inner product)"

    표준 내적은 $\mathbf{F}^{n}$ 의 두 벡터 $x = (a_1, a_2, \dots, a_n), y = (b_1, b_2, \dots, b_n)$ 에 대하여 다음과 같이 정의된 내적 $\big <\cdot , \cdot \big > : \mathbf{F}^{n} \times \mathbf{F}^{n} \to \mathbf{F}$ 이다.

    $$ \big <x,y \big > = \sum_{i=1}^{k}a_i \overline{b_i} $$

- 표준 내적이 내적임은 쉽게 증명할 수 있다.

- $\mathbf{F}= \R$ 이면 켤레복소수를 생각할 필요 없다. 이 경우의 표준내적은 우리가 잘 알고 있는 점곰(dot product) $x \cdot y$ 와 같아진다.

- 예시

    $x = (1+i, 4), y = (2-3i, 4+5i) \in \mathbb{C} ^{2}$ 와 표준내적 $\big <\cdot ,\cdot  \big >$ 대하여 다음이 성립한다.

    $$ \big <x,y \big >=(1+i)(2+3i)+4(4-5i)=15-15i
    $$

## Adjoint of Matrix

!!! tldr "켤레 전치행렬(conjugate transpose), 수반행렬(adjoint)"

    행렬 $A \in \mathbf{M}_{m \times n}(\mathbf{F})$ 와 각 $i, j$ 에 대하여 $(A ^{*}) _{ij} = \overline{A}_{ji}$ 인 $n \times m$ 행렬 $A ^{*}$ 를 $A$ 의 수반행렬이라 한다.

- 전치행렬의 켤레복소수를 구한 것이 수반행렬이다. 따라서 행렬의 모든 성분이 실수이면 수반행렬은 전치행렬이다.

- 예시

    $$ A = \begin{pmatrix} i&1+2i\\ 2&3+4i\\ \end{pmatrix}\implies A {}^{*} = \begin{pmatrix} -i&2\\ 1-2i&3-4i\\ \end{pmatrix} $$

## Frobenius Inner Product

!!! tldr "프로베니우스 내적(Frobenius inner product)"

    프로베니우스 내적은 벡터공간 $\mathbf{V}=\mathbf{M}_{n \times n}(\mathbf{F})$ 와 두 행렬 $A, B \in \mathbf{V}$ 에 대한 내적 $\big <A,B \big >_{\text{F}}=\text{tr} (B {}^{*} A)$ 이다.

- $\mathbf{F}=\R$ 일 경우 $B {}^{*} = B {}^{t}$ 이므로 다음이 성립한다.

    $$ (B {}^{*}A) _{ii} = (B {}^{t}A) _{ii} = \sum_{k=1}^{n}(B {}^{t})_{ik}A _{ki} = \sum_{k=1}^{n}B _{ki}A _{ki} $$

    $$ \text{tr} (B {}^{*}A) = \sum_{i=1}^{n}(B {}^{*}A)_{ii} = \sum_{i=1}^{n}\sum_{k=1}^{n}B _{ki}A _{ki} $$

    따라서 실수체의 행렬에서 프로베니우스 내적은 다음과 같이 정의된다.

    $$ \bigg < \begin{pmatrix} a_{11}&a_{12}&\dots&a_{1n}\\ a_{21}&a_{22}&\dots&a_{2n}\\ \vdots& \vdots& \ddots& \vdots \\ a_{n1}&a_{n2}&\dots&a_{nn}\\ \end{pmatrix}, \begin{pmatrix} b_{11}&b_{12}&\dots&b_{1n}\\ b_{21}&b_{22}&\dots&b_{2n}\\ \vdots& \vdots& \ddots& \vdots \\ b_{n1}&b_{n2}&\dots&b_{nn}\\ \end{pmatrix}\bigg > _{\text{F}}= \begin{pmatrix} a_{11}b_{11}&a_{12}b_{12}&\dots&a_{1n}b_{1n}\\ a_{21}b_{21}&a_{22}b_{22}&\dots&a_{2n}b_{2n}\\ \vdots& \vdots& \ddots& \vdots \\ a_{n1}b_{n1}&a_{22}b_{22}&\dots&a_{nn}b_{nn}\\ \end{pmatrix} $$

## Inner Product Space

!!! tldr "내적공간(inner product space), 복소내적공간(complex inner product space), 실내적공간(real inner product)"

    내적공간은 내적이 주어진 $\mathbf{F}$-벡터공간 $\mathbf{V}$ 이다.
    
    $\mathbf{F}=\mathbb{C}$ 이면 $\mathbf{V}$ 를 복소내적공간이라 한다. $\mathbf{F}=\R$ 이면 $\mathbf{V}$ 를 실내적공간이라 한다.

- 특별한 언급이 없는한 $\mathbf{F}^{n}$ 을 표준내적이 정의된 내적공간으로 생각하자.

- 예시

    벡터공간 $\mathbf{M}_{n \times n}(\mathbf{F})$ 에 프로베니우스 내적이 주어지면 이는 내적공간이다.

- 같은 벡터공간이라도 서로 다른 내적이 주어지면 다른 내적공간이 된다.

    - 예시 

        벡터공간 $\mathbf{P}(\R)$ 에 다음과 같은 서로 다른 내적이 주어졌다고 하자.

        $$ \big <f(x),g(x) \big >_{1} = \int_{0}^{1}f(t)g(t)dt $$

        $$ \big <f(x),g(x) \big >_{2} = \int_{-1}^{1}f(t)g(t)dt $$

        벡터 $f(x) = x, g(x) = x ^{2}$ 는 두번째 내적공간에서 $\big <f(x),g(x) \big >_{2}=0$ 이므로 서로 수직이지만 첫번째 내적공간에서는 수직이 아니다.

    이처럼 내적은 벡터공간의 기하학적 성질을 결정짓는다.

## Properties of Inner Product

!!! tldr "정리 6.1"

    내적공간 $\mathbf{V}$ 와 벡터 $x,y,z \in \mathbf{V}$ 와 스칼라 $c \in \mathbf{F}$ 에 대하여 다음이 성립한다.

    1. $\big <x,y+z \big >=\big <x,y \big >+\big <x,z \big >$

    2. $\big <x,cy \big >=\overline{c}\big <x,y \big >$

    3. $\big <x,0 \big >=\big <0,x \big >=0$

    4. $\big <x,x \big >= 0 \iff x=0$

    5. $\big <x,y \big >=\big <x,z \big >\implies y=z$

- 이 성질은 켤레복소수의 성질과 내적공간의 정의에 의해 쉽게 증명된다.

- 증명

    1:

    $$ \begin{equation}\begin{split} \big <x,y+z \big >&= \overline{\big <y+z,x \big >} \\ &= \overline{\big <y,x \big > + \big <z,x \big >} \\ &= \overline{\big <y,x \big >} + \overline{\big <z,x \big >} \\ &= \big <x,y \big > + \big <x,z \big > \\ \end{split}\end{equation} \tag*{} $$

    2:

    $$ \begin{equation}\begin{split} \big <x,cy \big >&= \overline{\big <cy,x \big >} \\ &=\overline{c} \cdot \overline{\big <y,x \big >} \\ &=\overline{c} \cdot \big <x,y \big > \\ \end{split}\end{equation} \tag*{} $$

    3:

    2) 를 가정할 수 있으므로 다음이 성립한다.

    $$ \begin{equation}\begin{split} \big <x,0 \big >&= \big <x,0 \cdot 0 \big > \\ &=0 \big <x,0 \big > = 0 \\ \end{split}\end{equation} \tag*{} $$

    또한 내적의 정의에 의하여 첫번째 성분에 대하여 스칼라 곱에 대하여 선형이므로 $\big <0,x \big >=\big <0 \cdot 0,x \big > = 0 \cdot \big <0,x \big > = 0$ 이다.

    4:

    $\big <x,x \big >=0$ 를 가정하자. $x \neq 0$ 이면 내적의 정의에 의하여 $\big <x,x \big >>0$ 이므로 모순이다. 따라서 $x = 0$ 이다. 

    이제 $x = 0$ 을 가정하자. 첫번째나 두번째 성분이 $0$ 이면 3) 에 의하여 내적의 결과도 $0$ 이므로 $\big <0,0 \big >=0$ 이다.

    5:

    2) 와 켤레복소수의 성질 (1) 에 의하여 다음이 성립한다.

    $$ \big <x,y \big >= \big <x,z \big > $$

    $$ \iff \overline{y}\big <x,1 \big > = \overline{z}\big <x,1 \big > $$

    $$ \iff \overline{y} = \overline{z} \iff y = z $$

## Antilinear Map

!!! tldr "Antilinear map, 켤레선형(conjugate-linear)"

    체 $\mathbf{F} \in \{\R, \mathbb{C}\}$ 인 $\mathbf{F}$-벡터공간 $\mathbf{V}$ 와 $\mathbf{W}$ 와 벡터 $x, y \in \mathbf{V}$ 와 스칼라 $a, b \in \mathbf{F}$ 대하여 다음을 만족하는 함수 $f: \mathbf{V}\to \mathbf{W}$ 를 antilinear 또는 켤레 선형이라고 한다.

    $$ f(ax + by) = \overline{a}f(x) + \overline{b}f(y) $$

- 덧셈에 대하여 선형이고 켤레 복소수 스칼라에 대한 곱셈에 대하여 선형이면 켤레 선형이다. 즉 함수 $f$ 가 덧셈에 대하여 

    $$ f(x+y) = f(x) + f(y) $$

    이고 스칼라곱에 대하여

    $$ f(ax) = \overline{a}f(x) $$

    이면 켤레 선형이다.

- 정리 6.1 의 1) 과 2) 에서 내적이 두번째 선형에 대하여 켤레선형임을 알 수 있다.

# Norm

!!! tldr "노름(norm), 길이(length)"

    $\mathbf{F}$-벡터공간 $\mathbf{V}$ 의 노름은 $x, y \in \mathbf{V}$ 와 스칼라 $c \in \mathbf{F}$ 에 대하여 다음 조건을 만족하는 실가함수 $\|\cdot \|: \mathbf{V}\to \R ^{\geq 0}$ 이다. 

    1. $\|x+y\| \leq \|x\|+ \|y\|$

    2. $\|cx\| = |c| \|x\|$

    3. $\|x\| = 0 \implies x = 0$

- 위 노름의 조건에서 $\|x\|\geq 0$ 라는 조건이 도출된다.

- 노름은 벡터공간의 원소의 크기 또는 길이를 일반화시킨 개념이다. 우리가 직관적으로 좌표평면 $\R ^{2}$ 의 좌표 $(2, 1)$ 를 $(0, 0)$ 에서 $(2, 1)$ 까지의 선분으로 보고 그 길이를 $\sqrt[]{5}$ 라고 생각하던 것을 일반적인 벡터공간에서의 길이로 추상화시킨 것이다.

- **내적공간 $\mathbf{V}$ 와 벡터 $x \in \mathbf{V}$ 에 대하여 $x$ 의 노름은 $\|x\| = \sqrt[]{\big <x,x \big >}$ 이다. 내적공간이 노름공간의 부분집합이므로 내적이 정의되면 노름도 자동으로 정의된다.** 좌표평면 $\R ^{2}$ 에서의 길이나 공간좌표 $\R ^{3}$ 에서의 길이가 벡터 $v = (a, b) \in \R ^{2}, x = (a, b, c) \in \R ^{3}$ 에 대하여 다음과 같이 주어지므로 이렇게 내적을 기반으로 하는 정의는 노름의 정의를 자연스럽게 일반화시킨 것이다.

    $$ \sqrt[]{a ^{2}+ b ^{2}} = \sqrt[]{\big <v, v \big >} $$

    $$ \sqrt[]{a ^{2}+ b ^{2} + c ^{2}} = \sqrt[]{\big <x, x\big >} $$

    그러나 노름의 정의는 내적과 독립적이다. 심지어 노름이 정의된 공간이지만 내적이 존재하지 않을 수도 있다. 아래의 노름공간의 설명을 보자.

## Normed vector space

!!! tldr "노름공간(Normed vector space)"

    노름이 정의된 벡터공간이다.

- 즉, 노름공간은 원소들의 크기 또는 길이가 부여된 벡터공간이다.

- 프리드버그 선형대수학은 내적 $\big <\cdot , \cdot \big >$ 을 먼저 정의하고 이것에 대응하는 노름으로써 $\|x\| = \sqrt[]{\big <x,x \big >}$ 을 정의했다. 다음 그림을 보자.

    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Mathematical_Spaces.png/375px-Mathematical_Spaces.png)

    위 그림은 내적 $\big <\cdot ,\cdot  \big >$ 이 정의되면 노름이 $\|x\|=\sqrt[]{\big <x,x \big >}$ 와 같이 자연스럽게 정의됨을 알려준다. 그러나 그 역은 성립하지 않는다. 즉, 노름이 정의되었다고 해서 그 노름에 대응하는 내적이 자동으로 정의되지는 않는다. 정리 6.2 가 벡터공간 $\mathbf{V}$ 의 내적 $\big <\cdot ,\cdot  \big >$ 을 기반으로 하는 함수 $\sqrt[]{\big <x,x \big >}$ 가 노름의 조건을 만족함을 보장해준다.

    노름 $\|\cdot \|$ 이 정의되면 거리함수(metric function)가 $d(x, y) = \|x-y\|$ 와 같이 자연스레 정의된다. 그러나 그 역은 성립하지 않는다. 거리함수가 존재한다고 해서 그에 대응하는 노름이 항상 존재하지는 않는다. 위 그림이 보여주듯이 거리공간(Metric space)은 벡터공간이 아닌 공간에서도 정의된다. 

    마지막으로 이 모든 공간들은 위상공간의 조건을 만족한다. 그러나 위상공간이라고 해서 거리공간, 노름공간, 내적공간이 된다는 보장은 없다.

- 예시 

    1차원 벡터공간 $\mathbf{V}$ 에서 절댓값이 노름이다. 즉, $\|x\|=|x|$ 이다. 역으로 1차원 노름공간 $\mathbf{V}$ 에서 노름 $p$ 는 항상 절댓값에 대응된다. 이는 노름을 보존하는 동형사상 $f: \mathbf{F} \to \mathbf{V}$ 가 존재하여 임의로 정의된 노름 $\|\cdot \|$ 에 대하여 $|x| = \|f(x)\|$ 를 만족한다는 것이다.

## Properties of Norm

!!! tldr "정리 6.2"

    $\mathbf{F}$-내적공간 $\mathbf{V}$ 와 임의의 벡터 $x, y \in \mathbf{V}$, 스칼라 $c \in \mathbf{F}$ 와 노름 $\|x\|=\sqrt[]{\big <x,x \big >}$ 에 대하여 다음이 성립한다.

    1. $\|cx\|=|c| \cdot  \|x\|$

    2. $\|x\| = 0 \iff x = 0$, $\|x\| \geq 0$

    3. $|\big <x,y \big >| \leq \|x\|\cdot \|y\|$ (Cauchy-Schwarz inequality)

    4. $\|x+y\| \leq \|x\|+\|y\|$ (triangle inequality)

- 이 정리의 1), 2), 4) 는 내적을 기반으로 정의된 함수 $\|x\|=\sqrt[]{\big <x,x \big >}$ 가 노름이라는 것을 증명해준다. 이에 따라 내적공간은 반드시 노름공간이 된다. 즉, 내적이 정의되면 노름이 자동으로 정의된다는 것이다. 그래서 사실 정리의 가정부에서 $\|x\|$ 가 노름이라는 언급을 하면 안되지만, 강조하는 의미에서 노름이라고 썼다.

- 3) 은 유명한 정리인 코시-슈바르츠 부등식이고, 4) 도 유명한 정리인 삼각 부등식이다.

- 증명

    1:

    내적의 정의와 정리 6.1 에 의하여 다음이 성립한다.
    
    $$ \|cx\| ^{2} = \big <cx,cx \big > = c \big <x,cx \big > = c \overline{c}\big <x,x \big > = c ^{2} \|x\| $$

    $$ \therefore \|cx\| = |c| \cdot \|x\| $$

    2:

    내적의 정의와 정리 6.1(4) 에서 바로 나온다.

    3:

    $y = 0$ 이면 성립한다. $y \neq 0$ 를 가정하면 내적의 정의와 정리 6.1 에 의하여 $c \in \mathbf{F}$ 에 대하여 다음이 성립한다. 

    $$ \begin{equation}\begin{split} 0 \leq \big <x-cy,x-cy \big >&= \big <x,x-cy \big >-c \big <y,x-cy \big > \\ &= \big <x,x \big > - \overline{c}\big <x,y \big >-c \big <y,x \big >+c \overline{c}\big <y,y \big >\\ \end{split}\end{equation} \tag*{} $$

    $c = \dfrac{\big <x,y \big >}{\big <y,y \big >}$ 로 두면 우측 세 항이 모두 다 $\dfrac{\big <x,y \big >\big <y,x \big >}{\big <y,y \big >}=\dfrac{|\big <x,y \big >|^{2}}{\|y\|^{2}}$ 이므로 다음이 성립한다. 

    $$ 0 \leq \big <x,x \big > - \dfrac{|\big <x,y \big >|^{2}}{\big <y,y \big >} = \|x\|^{2} + \dfrac{|\big <x,y \big >|^{2}}{\|y\|^{2}} $$

    4:

    3) 에 의하여 다음이 성립한다.

    $$ \begin{equation}\begin{split} \|x+y\|^{2}&=\big <x+y,x+y \big > = \big <x,x \big >+\big <y,x \big >+\big <x,y \big >+\big <y,y \big > \\ &= \|x\|^{2} + 2\Re \big <x,y \big > + \|y\|^{2} \\ &\leq  \|x\|^{2} + 2| \big <x,y \big >| + \|y\|^{2} \\ &\leq  \|x\|^{2} + 2 \|x\|\cdot \|y\| + \|y\|^{2} \\ &= (\|x\|+\|y\|)^{2} \end{split}\end{equation} \tag*{} $$

- 예시 

    코시-슈바르츠 부등식과 삼각 부등식에 의하여 표준내적이 주어진 $\mathbf{F}^{n}$ 에 대하여 다음의 잘 알려진 부등식이 성립한다.

    $$ \bigg |\sum_{i=1}^{n}a_i \overline{b_i} \bigg | \leq \bigg [\sum_{i=1}^{n}|a_i|^{2} \bigg ]^{1/2}\bigg [\sum_{i=1}^{n}|b_i|^{2} \bigg ]^{1/2} $$

    $$ \bigg [\sum_{i=1}^{n}|a_i + b_i|^{2} \bigg ]^{1/2}\leq \bigg [\sum_{i=1}^{n}|a_i|^{2} \bigg ]^{1/2}+\bigg [\sum_{i=1}^{n}|b_i|^{2} \bigg ]^{1/2} $$

## Euclidean Space

!!! tldr "유클리드 공간(Euclidean vector space)"

    n차원 유클리드 공간 $\R ^{n}$ 은 표준내적이 부여된 유한차원 내적공간이다.

- 유클리드 공간은 유클리드가 연구했던 평면과 공간을 일반화한 것이다. 일반화란 유클리드가 생각했던 거리(distance)와 길이(norm)와 좌표계를 도입하여 임의 차원의 공간으로 확장한 것이다.

- $\R$-벡터공간 $\R ^{n}$ 에 표준내적이 부여됨에 따라 실수 힐베르트 공간을 이루고 내적 공간, 바나흐 공간, 노름 공간, 벡터 공간, 완비 거리 공간, 위상 공간을 이룬다.

- 유클리드 공간을 아핀 공간을 기반으로 정의하는 것이 있는데 나중에 알아봐야 할듯.

- 예시 

    유클리드 공간에는 아래에서 볼 수 있듯이 유클리드 노름이 가장 자주 사용되며 우리의 직관 속에 녹아들어있다. 그러나 전혀 새로운 노름을 정의할 수도 있다. 가령 4차원 유클리드 공간 $\R ^{4}$ 과 벡터 $x = (x_1, x_2, x_3, x_4) \in \R ^{4}$ 에 대하여 다음과 같은 노름을 정의할 수 있다.

    $$ \|x\| = 2|x_1| + \sqrt[]{3|x_2| ^{2} + \max (|x_3|, 2|x_4|) ^{2}}
    $$

## Norm of Euclidean Space

!!! tldr "유클리드 노름(Euclidean norm), $L_2$ 노름($L_2$ norm)"

    n차원 유클리드 공간 $\R ^{n}$ 의 벡터 $x = (x_1, x_2, \dots, x_n)$ 의 유클리드 노름은 다음과 같다. 

    $$ \|x\|_{2} := \bigg (\sum_{i=1}^{n}x_i ^{2} \bigg ) ^{1/2} = \sqrt[]{x_1 ^{2} + \dots + x_n ^{2}} $$

- 유클리드 공간은 표준내적이 부여된 내적공간이므로 내적을 사용하여 아래와 같이 유클리드 노름을 정의해보면 좀 더 단순해진다.

    $$ \|x\|_{2} := \sqrt[]{x \cdot x} $$

- 이 유클리드 노름, 즉 유클리드 길이는 피타고라스의 정리에 의하여 자연스럽게 유도되고 이 정의와 같이 n차원으로 확장되었다.

- 유클리드 노름이 $\R ^{n}$ 에서 가장 자주 사용된다. 그러나 아래에서 볼 수 있듯이 $\R ^{n}$ 에는 다른 노름도 존재한다. 그러나 이 모든 노름들은 그것들이 모두 같은 위상에서 정의되었다는 점에서 본질적으로 같다.

!!! tldr "유클리드 거리(Euclidean distance), $L_2$ 거리($L_2$ distance)"

    n차원 유클리드 공간 $\R^{n}$ 과 벡터 $x = (x_1, x_2, \dots, x_n), y = (y_1, y_2, \dots, y_n) \in \R^{n}$ 에 대한 $x$ 와 $y$ 의 유클리드 거리는 다음과 같은 거리함수 $d_2: \R ^{n} \times \R ^{n} \to \R$ 의 상이다.

    $$ d_2(x, y) = \|x-y\|_2 := \bigg (\sum_{i=1}^{n}|x_i-y_i|^{2} \bigg )^{1/2} $$

- 유클리드 거리는 두 유클리드 노름을 기반으로 정의된다.

- 유클리드 공간은 표준내적이 부여된 내적공간이므로 내적을 사용하여 아래와 같이 유클리드 거리를 정의해보면 좀 더 단순해진다.

    $$ \|x - y\| := \sqrt[]{(x-y) \cdot (x-y)} = \sqrt[]{\|x\|^{2} + \|y\|^{2} - 2x \cdot y} $$

- 다음 그림은 좌표평명 $\R ^{2}$ 에서 유클리드 거리를 보여준다. 

    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Euclidean_distance_2d.svg/450px-Euclidean_distance_2d.svg.png)

    이것이 피타고라스의 정리에 의하여 도출되었으므로 피타고라스 거리(Pythagorean distance)라고도 부른다.

!!! tldr "유클리드 거리 제곱(Squared Euclidean distance)"

    n차원 유클리드 공간 $\R^{n}$ 과 벡터 $x = (x_1, x_2, \dots, x_n), y = (y_1, y_2, \dots, y_n) \in \R^{n}$ 에 대한 $x$ 와 $y$ 의 유클리드 거리 제곱은 다음과 같은 거리함수 $d_2 ^{2}: \R ^{n} \times \R ^{n} \to \R$ 의 상이다.

    $$ d_2 ^{2}(x, y) = \sum_{i=1}^{n}|x_i-y_i|^{2} $$

- 거리를 비교해야 하는 실제 상황에서 많은 경우 유클리드 거리의 제곱근을 제거한다. 이렇게 제곱근이 제거된 유클리드 거리를 유클리드 거리 제곱이라고 한다.

- 유클리드 거리 제곱은 거리 공간(metric space)을 형성하지는 않는다. 삼각 부등식을 만족하지 못하기 때문이다.

!!! tldr "Taxicab norm, 맨하튼 노름(Manhattan norm), $L_1$ 노름($L_1$ norm)"

    n차원 유클리드 공간 $\R ^{n}$ 의 벡터 $x = (x_1, x_2, \dots, x_n)$ 의 $L_1$ 노름은 다음과 같다. 

    $$ \|x\|_{1} := \sum_{i=1}^{n}|x_i| $$

- 쉽게 말해 맨하튼 노름이란 주어진 벡터의 모든 성분의 절댓값을 더하겠다는 것이다.

- 이름에서 알 수 있듯이 이 노름은 바둑판처럼 생긴 도로에서 택시가 목적지까지 가는데 걸리는 길이(노름)이다. 다음 그림을 보자.

    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Manhattan_distance.svg/300px-Manhattan_distance.svg.png)

    초록선은 출발지에서 목적지까지 가는 유클리드 노름이다. 빨강, 노랑, 파란선은 $L_1$ 노름이다. 빨강, 노랑, 파란선의 길이가 모두 동일하다는 것에 주목하자.

!!! tldr "Taxicab distance, 맨하튼 거리(Manhattan distance), $L_1$ 거리 ($L_1$ distance)"

    n차원 유클리드 공간 $\R^{n}$ 과 벡터 $x = (x_1, x_2, \dots, x_n), y = (y_1, y_2, \dots, y_n) \in \R^{n}$ 에 대한 $x$ 와 $y$ 의 $L_1$ 거리는 다음과 같은 거리함수 $d_1: \R ^{n} \times \R ^{n} \to \R$ 의 상이다.

    $$ d_1(x, y) = \|x-y\| _{1} = \sum_{i=1}^{n}|x_i-y_i| $$

!!! tldr "p-norm, $L_p$ 노름($L_p$ norm)"

    n차원 유클리드 공간 $\R ^{n}$ 의 벡터 $x = (x_1, x_2, \dots, x_n)$ 의 $L_p$ 노름은 다음과 같다. 
    
    $$ \|x\|_{p} := \bigg (\sum_{i=1}^{n}|x_i| ^{p} \bigg )^{1/p} $$

- $p = 1$ 일 때 $L_1$ 노름이 되고 $p = 2$ 일 때 유클리드 노름이 된다.

!!! tldr "민코프스키 거리(Minkowski distance), $L_p$ 거리($L_p$ distance)"

    n차원 유클리드 공간 $\R^{n}$ 과 벡터 $x = (x_1, x_2, \dots, x_n), y = (y_1, y_2, \dots, y_n) \in \R^{n}$ 에 대한 $x$ 와 $y$ 의 민코프스키 거리는 다음과 같은 거리함수 $d_p: \R ^{n} \times \R ^{n} \to \R$ 의 상이다.

    $$ d_p(p, q) = \bigg (\sum_{i=1}^{n}|x_i-y_i|^{p} \bigg )^{1/p} $$
    
- 민코프스키 거리는 유클리드 거리와 맨하튼 거리의 일반화이다.

!!! tldr "무한 노름(infinity norm), 최대 노름(maximum norm), 상한 노름(supremum norm), $L _{\infty }$ 노름($L _{\infty }$ norm)"

    n차원 유클리드 공간 $\R ^{n}$ 의 벡터 $x = (x_1, x_2, \dots, x_n)$ 의 상한 노름은 다음과 같다. 

    $$ \|x\|_{\infty } := \lim_{p \to \infty} \bigg (\sum_{i=1}^{n}|x_i| ^{p} \bigg )^{1/p} = \max ^{n} _{i=1}|x_i| = \max \{|x_1|, |x_2|, \dots, |x_n|\} $$

- 상한 노름은 쉽게 말해 주어진 벡터의 성분의 최댓값을 노름으로 삼는다는 것이다.

- 유클리드 노름과 $L_1$ 노름을 기반으로 거리 함수가 정의되었듯 이 상한 노름을 기반으로 상한 거리 함수 또는 최대 거리 함수가 정의된다.

- 예시 

    반지름이 $1$ 이고 원점을 중점으로 하는 단위원을 $p = 1, 2, \infty$ 의 노름에서 그려보면 다음과 같다. 

    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Vector_norms.svg/140px-Vector_norms.svg.png)

!!! tldr "체비셰프 거리(Chebyshev distance), 최대 거리(maximum distance), $L _{\infty }$ 거리($L _{\infty }$ distance)"

    n차원 유클리드 공간 $\R^{n}$ 과 벡터 $x = (x_1, x_2, \dots, x_n), y = (y_1, y_2, \dots, y_n) \in \R^{n}$ 에 대한 $x$ 와 $y$ 의 체비셰프 거리는 다음과 같은 상한 거리 함수 $d _{\infty }: \R ^{n} \times \R ^{n} \to \R$ 의 상이다.

    $$ d _{\infty }(x, y) = \lim_{p \to \infty} \bigg (\sum_{i=1}^{n}|x_i-y_i| ^{p} \bigg )^{1/p} = \max ^{n} _{i=1}|x_i-y_i| $$
    
- 체비셰프 거리는 민코프스키 거리에서 $p \to \infty$ 로 보낸 결과이다.

!!! tldr "하한 노름(infimum norm), $L _{- \infty }$ 노름($L _{- \infty }$ norm)"
    
    n차원 유클리드 공간 $\R ^{n}$ 의 벡터 $x = (x_1, x_2, \dots, x_n)$ 의 하한 노름은 다음과 같다. 

    $$ \|x\|_{-\infty } := \lim_{p \to -\infty} \bigg (\sum_{i=1}^{n}|x_i| ^{p} \bigg )^{1/p} = \min _{i=1} ^{n}|x_i| = \min \{|x_1|, |x_2|, \dots, |x_n|\} $$

- 하한 노름은 쉽게 말해 주어진 벡터의 성분의 최솟값을 노름으로 삼는다는 것이다.

- 예시 

    다음 그림은 다양한 $p$-노름에서의 단위원을 보여준다.

    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/2D_unit_balls.svg/1451px-2D_unit_balls.svg.png)

!!! tldr "하한 거리(infimum distance), $L _{- \infty }$ 거리($L _{- \infty }$ distance)"

    n차원 유클리드 공간 $\R^{n}$ 과 벡터 $x = (x_1, x_2, \dots, x_n), y = (y_1, y_2, \dots, y_n) \in \R^{n}$ 에 대한 $x$ 와 $y$ 의 하한 거리는 다음과 같은 하한 거리 함수 $d _{-\infty }: \R ^{n} \times \R ^{n} \to \R$ 의 상이다.
    
    $$ d _{-\infty }(x, y) = \lim_{p \to -\infty} \bigg (\sum_{i=1}^{n}|x_i-y_i| ^{p} \bigg )^{1/p} = \min ^{n} _{i=1}|x_i-y_i| $$

- 민코프스키 거리에서 $p \to - \infty$ 로 보내면 하한 거리 함수를 얻는다.

# Orthogonal

## Orthogonal in Euclidean Space

!!! tldr "코사인(cosine)"

    $C$ 가 직각인 삼각형 $ABC$ 에서 코사인 $A$ 는 다음과 같은 빗변에 대한 밑변의 비율이다.

    $$ \cos A = \frac{\overline{AC}}{\overline{AB}} $$

- 다음 그림은 $\cos A = \frac{b}{h}$ 가 빗변에 대한 밑변의 비율임을 보여준다.

    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Trigonometry_triangle.svg/338px-Trigonometry_triangle.svg.png)

!!! tldr "코사인 법칙(Law of cosines)"

    삼각형 $ABC$ 의 세 각 $A, B, C$ 가 마주하는 변 $a, b, c$ 에 대하여 다음이 성립한다. 

    $$ c ^{2} = a ^{2} + b ^{2} - 2ab \cos C $$

- $C$ 가 직각일 경우 $\cos \dfrac{\pi }{2} = 0$ 이므로 다음과 같은 피타고라스의 정리를 얻는다.

    $$ c ^{2} = a ^{2} + b ^{2} $$

- 증명

    다음 그림처럼 삼각형 $ABC$ 의 세 점 $A, B, C$ 의 각을 각각 $\alpha , \beta , \gamma$ 로 두고 마주하는 변을 각각 $a, b, c$ 로 두자. 

    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Triangle_with_notations_2.svg/330px-Triangle_with_notations_2.svg.png)

    다음 그림은 코사인의 정의에 의하여 $c = a \cos \beta + b \cos \alpha$ 가 성립함을 보여준다.

    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Triangle-with-cosines.svg/450px-Triangle-with-cosines.svg.png)

    같은 원리로 다음을 얻는다.

    $$ a = c \cos \beta + b \cos \gamma $$

    $$ b = c \cos \alpha + a \cos \gamma $$

    이를 기반으로 다음이 성립한다.

    $$ a ^{2} = ac \cos \beta + ab \cos \gamma \tag{1} $$

    $$ b ^{2} = bc \cos \alpha + ab \cos \gamma \tag{2} $$

    $$ c ^{2} = ac \cos \beta + bc \cos \alpha \tag{3} $$

    $(1)$ 과 $(2)$ 를 더하고 $(3)$ 을 빼면 다음이 성립한다.

    $$ a ^{2} + b ^{2} - c ^{2} = 2ab \cos \gamma $$

    이것을 다음과 같이 정리하여 코사인 법칙을 얻는다.

    $$ \therefore c ^{2} = a ^{2} + b ^{2} -2ab \cos C \tag*{■} $$

!!! tldr "두 벡터가 이루는 각"

    2차원 또는 3차원 유클리드 공간 $\mathbb{E} \in \{\R ^{2}, \R ^{3}\}$ 의 벡터 $x, y$ 가 이루는 각은 다음과 같다.

    $$ \theta = \arccos \bigg (\dfrac{\big <u,v \big >}{\|u\|\|v\|} \bigg ) $$

- 유클리드 공간에는 표준내적이 부여되어 있고 표준내적은 점곱(dot product) 로 표현되므로 자주 다음과 같이 정의되기도 한다.

    $$ \theta = \arccos \bigg (\dfrac{u \cdot v}{\|u\|\|v\|} \bigg ) $$

- 증명

    3차원 유클리드 공간 $\R ^{3}$ 에서 증명하면 $\R ^{2}$ 에서는 당연히 성립한다.

    벡터로 표현하는 직선의 방정식의 증명과정에서 보았었던 그림을 다시 보자.

    ![](https://user-images.githubusercontent.com/16812446/113727560-32b6d780-9730-11eb-92c8-c3d69dd3c680.png)

    $u$ 의 종점, 즉 $A$ 의 좌표를 $u = (u_1, u_2, u_3)$ 로 두고 $v$ 의 종점, 즉 $B$ 의 좌표를 $v = (v_1, v_2, v_3)$ 로 두자. 그러면 $w = (v_1-u_1, v_2-u_2, v_3-u_3)$ 이다.

    위 그림에서 벡터 $u, v$ 가 이루는 각 $\theta$ 를 구해보자. 삼각형 $ABO$ 와 각 $\theta$ 에 대하여 코사인 법칙에 의하여 다음이 성립한다. 

    $$\|v\| ^{2} + \|u\| ^{2} - \|w\| ^{2} = 2 \|v\|\|u\| \cos \theta \tag{1} $$

    유클리드 공간에는 표준내적이 부여되었으므로 다음이 성립한다. 

    $$ \|v\|^{2} = \big <v,v \big > = v_1 ^{2} + v_2 ^{2} + v_3 ^{2} \tag{2} $$

    $$ \|u\|^{2} = \big <u,u \big > = u_1 ^{2} + u_2 ^{2} + u_3 ^{2} \tag{3} $$

    $$ \begin{equation}\begin{split}
    \|w\|^{2} &= \big <w,w \big > = (v_1-u_1) ^{2} + (v_2-u_2) ^{2} + (v_3-u_3) ^{2}\\
    &= v_1 ^{2} - 2v_1u_1 + u_1 ^{2} + v_2 ^{2} - 2v_2u_2 + u_2 ^{2} + v_3 ^{2} - 2v_3u_3 + u_3 ^{2} \\
    \end{split}\end{equation} \tag{4} $$

    $(2)$ 과 $(3)$ 를 더하고 $(4)$ 을 빼면 다음이 성립한다. 

    $$ \|v\|^{2} + \|u\|^{2} - \|w\|^{2} = 2v_1u_1 + 2v_2u_2 + 2v_3u_3 $$

    그러면 이것을 $(1)$ 에 적용함으로써 다음이 성립함을 알 수 있다.

    $$ 2 \|v\|\|u\| \cos \theta = 2v_1u_1 + 2v_2u_2 + 2v_3u_3 $$

    $$ \iff \cos \theta = \dfrac{v_1u_1 + v_2u_2 + v_3u_3}{\|u\|\|v\|} = \dfrac{\big <v,u \big >}{\|v\|\|u\|}  $$

    $\theta$ 는 두 벡터가 이루는 각이므로 $0 \leq \theta < \pi$ 를 만족한다. 따라서 두 벡터가 이루는 각은 다음과 같다. 

    $$ \therefore \theta = \arccos \bigg ( \dfrac{\big <v,u \big >}{\|v\|\|u\|}\bigg ) \tag*{■} $$

!!! tldr "유클리드 공간에서의 직교"

    2차원 또는 3차원 유클리드 공간 $\mathbb{E} \in \{\R ^{2}, \R ^{3}\}$ 의 벡터 $x, y$ 가 직교인 것과 $\big <x,y \big > = 0$ 인 것은 동치이다.

- 기본적으로 직교란 두 벡터가 이루는 각이 $90 \degree$ 인 것이다.

- 증명

    두 벡터가 이루는 각이 $90 \degree = \dfrac{\pi }{2}$ 이면 $\cos \dfrac{\pi }{2} = 0$ 이므로 두 벡터가 이루는 각에 의하여 다음이 성립한다. 

    $$ \dfrac{\pi }{2} = \arccos \bigg (\dfrac{\big <u,v \big >}{\|u\|\|v\|} \bigg ) $$

    $$ \iff \cos \frac{\pi }{2} = \dfrac{\big <u,v \big >}{\|u\|\|v\|} = 0 $$

    $$ \iff \big <u,v \big > = 0 \tag*{■} $$

## Definition of Orthogonal

!!! tldr "직교(orthogonal), 수직(perpendicular)"

    내적공간 $\mathbf{V}$ 와 벡터 $x, y \in \mathbf{V}$ 에 대하여 $\big <x,y \big > = 0$ 이면 두 벡터는 직교한다.

- 유클리드 공간에서 두 벡터 $x, y$ 의 직교는 $\big <x,y \big > = 0$ 과 동치였다. 이 수직의 개념을 임의의 내적공간으로 일반화시킨 것이다. 

- 벡터에 영이 아닌 스칼라를 곱해도 직교성은 불변한다.

!!! tldr "직교집합(orthogonal set)"

    내적공간 $\mathbf{V}$ 의 부분집합 $S$ 에 대하여 $S$ 에 속하는 서로 다른 임의의 두 벡터가 직교하면 $S$ 를 직교집합이라 한다.

!!! tldr "단위벡터(unit vector)"

    내적공간 $\mathbf{V}$ 에서 $\|x\| = 1$ 인 벡터이다.

## Orthonormal

!!! tldr "정규직교집합(orthonormal)"

    내적공간의 부분집합이 단위벡터로 구성된 직교집합이면 정규직교집합이라 한다.

- 집합 $S = \{v_1, v_2, \dots\}$ 가 정규직교집합인 것과 $\big <v_i,v_j \big > = \delta _{ij}$ 인 것은 동치이다. 

## Normalizing

!!! tldr "정규화(normalizing)"

    내적공간 $\mathbf{V}$ 의 영이 아닌 벡터를 방향을 유지한채 크기만 단위벡터로 바꾸는 함수 $f: \mathbf{V} \setminus \{0\} \to \mathbf{V} \setminus \{0\}$ 로써 다음과 같이 정의된다.

    $$ f(x) = \dfrac{x}{\|x\|} $$

- 즉, 정규화란 영이 아닌 벡터에 노름의 역수를 곱하는 것이다. 이렇게 하면 원래 벡터 $x$ 의 방향이 보존된 단위벡터를 얻을 수 있다. 

    - 증명

        노름의 조건 2) 를 사용하여 임의의 벡터 $x$ 에 노름의 역수를 곱한 것의 노름을 구해보자.

        $$ \bigg \| \dfrac{1}{\|x\|}x\bigg \| = \bigg |\frac{1}{\|x\|} \bigg |\|x\| = \frac{1}{\|x\|} \|x\| = 1 $$

        즉, 임의의 벡터 $x$ 에 노름의 역수를 곱한 벡터의 노름은 $1$ 이다. 따라서 이렇게 얻어진 벡터는 단위벡터이다.

- 예시 

    $\mathbf{F}^{3}$ 의 부분집합 $\{(1,1,0), (1,-1,1), (-1,1,2)\}$ 은 직교집합이다. 이 집합을 정규화하면 다음과 같은 정규직교집합을 얻는다.

    $$ \bigg \{\frac{1}{\sqrt[]{2}}(1,1,0), \frac{1}{\sqrt[]{3}}(1, -1, 1), \frac{1}{\sqrt[]{6}}(-1, 1, 2) \bigg \} $$

<!-- !!! tldr "복소함수(function of a complex variable)"

    복소함수는 정의역과 공역이 모두 복소수인 함수이다. 

- 즉, 복소함수 $f: \mathbb{C}\to \mathbb{C}$ 는 $u, v: \R ^{2} \to \R$ 에 대하여 다음과 같이 정의된다.

    $$ f(x+iy) = u(x, y) + iv(x, y) $$

- 예시

    함수 $e ^{x+iy} = e ^{x}(\cos y + i \sin y)$ 는 복소함수이다.

!!! tldr ""

    폐구간 $[0, 2 \pi ]$ 에서 연속인 복소함수들로 이루어진 집합에 내적 $\big <f,g \big >=\displaystyle \dfrac{1}{2 \pi }\int_{0}^{2 \pi }f(t)\overline{g(t)}dt$ 가 주어진 내적공간을 $\mathbf{H}$ 라 정의한다.

!!! tldr ""

    복소함수 $f = f_1 + if_2$ 의 적분에 대하여 다음이 성립한다.

    $$ \int_{}^{}f dt=\int_{}^{}f_1dt+i \int_{}^{}f_2dt $$

    $$ \overline{\int_{}^{}fdt} = \int_{}^{}\overline{f}dt $$

- 복소해석학에 대한 자세한 증명과 설명은 생략한다. 복소함수의 적분에서는 허수 $i$ 가 상수취급되므로 위 정리가 성립한다.

!!! tldr "오일러 식(Euler's formula)"

    복소수 $c = a+ib$ 와 자연상수 $e$ 에 대하여 다음과 같이 정의한다.

    $$ e ^{c} = e ^{a}(\cos b + i \sin b) $$

    이 식의 특수한 경우인 $e ^{ib} = \cos b + i \sin b$ 를 오일러 식이라 한다. -->

## Orthonormal Basis

!!! tldr "정규직교기저(orthonormal basis)"

    내적공간의 부분집합이 정규직교집합이고 순서기저이면 정규직교기저라 한다.

- 표준내적이 부여된 $\mathbb{C}^{n}$ 와 $\R ^{n}$ 의 표준순서기저는 벡터들이 정규직교집합을 이루기 때문에 특별한 성질을 가진다. 벡터공간을 구성하는 기본 조각이 기저라면, 내적공간을 구성하는 기본 조각은 정규직교기저이다.

- 예시 

    $\mathbf{F}^{n}$ 의 표준 순서기저는 $\mathbf{F} ^{n}$ 의 정규직교기저이다.

# Gram–Schmidt Process

!!! tldr "정리 6.3"

    내적공간 $\mathbf{V}$ 와 영이 아닌 벡터로 이루어진 직교집합 $S = \{v_1, v_2, \dots, v_k\}$ 와 $y \in \text{span} (S)$ 에 대하여 다음이 성립한다. 

    $$ y = \sum_{i=1}^{k}\dfrac{\big <y,v_i \big >}{\|v_i\|^{2}}v_i $$

- 증명

    $y$ 를 $S$ 의 일차결합으로 나타낼 수 있으므로 $a_1, a_2, \dots, a_k \in \mathbf{F}$ 에 대하여 $y = \sum_{i=1}^{k}a_iv_i$ 이다. $j \in \{1,\dots,k\}$ 에 대하여 내적이 첫번째 성분에 대하여 선형이고 $v_j$ 들이 서로 직교하므로 $\big <y,v_j \big >$ 는 다음과 같다. 

    $$ \big <y,v_j \big > = \bigg <\sum_{i=1}^{k}a_iv_i, v_j \bigg > = \sum_{i=1}^{k}a_i \big <v_i,v_j \big > = a_j \big <v_j,v_j \big > = a_j \|v_j\|^{2} $$

    즉, $a_j = \dfrac{\big <y,v_j \big >}{\|v_j\|^{2}}$ 이다. ■ 

!!! tldr "정리 6.3 따름정리 1"

    내적공간 $\mathbf{V}$ 와 영이 아닌 벡터로 이루어진 정규직교집합 $S = \{v_1, v_2, \dots, v_k\}$ 와 $y \in \text{span} (S)$ 에 대하여 다음이 성립한다. 

    $$ y = \sum_{i=1}^{k}\big <y,v_i \big >v_i $$

- 증명

    $S$ 가 정규직교집합이므로 정리 6.3 에서 바로 증명된다. ■ 

!!! tldr "정리 6.3 따름정리 2"
    
    내적공간에서 영이 아닌 벡터로 이루어진 직교집합은 일차독립이다.

- 증명

    $S$ 의 임의의 원소들 $v_1, v_2, \dots, v_k \in S$ 에 대하여 $\displaystyle \sum_{i=1}^{k}a_iv_i = 0$ 을 가정하자. 정리 6.3 에 의하여 $y = \displaystyle \sum_{i=1}^{k}\dfrac{\big <y,v_i \big >}{\|v_i\|^{2}}v_i$ 인데 $y = 0$ 으로 두면 [정리 6.1](#99baac14a) 에 의하여 $a_i = \dfrac{\big <0,v_j \big >}{\|v_j\|^{2}} = 0$ 이다. ■ 

- 예시 

    $\R ^{3}$ 의 정규직교집합 $\bigg \{\dfrac{1}{\sqrt[]{2}}(1,1,0), \dfrac{1}{\sqrt[]{3}}(1,-1,1), \dfrac{1}{\sqrt[]{6}}(-1,1,2) \bigg \}$ 은 정리에 의하여 $\R ^{3}$ 의 정규직교기저이다.

    이 정규직교기저의 $x = (2, 1, 3)$ 에 대한 일차결합 계수는 정리 6.3 따름정리 1 에 의하여 다음과 같다. 

    $$ a_1 = \frac{3}{\sqrt[]{2}}, a_2 = \frac{4}{\sqrt[]{3}}, a_3 = \frac{5}{\sqrt[]{6}} $$

<!-- > p366 벡터공간 H 관련 데이터 -->

!!! tldr "정리 6.4 그람-슈미트 직교화(Gram-Schmidt process)"

    내적공간 $\mathbf{V}$ 의 일차독립인 부분집합 $S = \{w_1, w_2, \dots, w_n\}$ 에 대하여 집합 $S' = \{v_1, v_2, \dots, v_n\}$ 을 다음과 같이 정의하면 $S'$ 는 영이 아닌 벡터로 이루어진 직교 집합이고 $\text{span} (S') = \text{span} (S)$ 를 만족한다.

    $$ v_k = \begin{cases} w_1 & k = 1\\ w_k - \displaystyle \sum_{j=1}^{k-1}\dfrac{\big <w_k,v_j \big >}{\|v_j\|^{2}}v_j & 2 \leq k \leq n\\ \end{cases} \tag{6.1} $$

- 그람-슈미트 직교화는 결국 벡터공간의 정규직교기저를 구하는 방법을 알려준다. 어떻게 그람-슈미트 직교화가 정규직교기저를 구하게 해주는지는 아래의 예시를 참고하자.

- 내적공간의 일차독립 집합과 같은 부분공간을 생성하는 직교집합을 얻기 위한 과정이 그람-슈미트 직교화이다. 즉, 집합 $S$ 로부터 집합 $S'$ 를 얻는 과정 $(6.1)$ 을 그람-슈미트 직교화라 한다.

- 그람-슈미트 직교화는 다음과 같이 2차원 또는 3차원 벡터공간에서 두 벡터가 이루는 평면을 똑같이 이루는 다른 두 벡터를 찾는 방식을 일반화한 것이다.

    ![image](https://user-images.githubusercontent.com/16812446/129446369-93079430-f833-486e-bbaf-c8e9837e9650.png)

    위 그림은 일차독립인 벡터공간의 부분집합 $\{w_1, w_2\}$ 가 이루는 평면, 즉 부분공간을 동일하게 이루는 벡터 $\{v_1, v_2\}$ 를 보여준다. 이때 상수 $c$ 에 대하여 $v_2 = w_2-cw_1$ 이다. $c$ 는 $v_2$ 가 $w_1$ 과 수직이 되도록하는 적당한 스칼라이다. $v_2, w_1$ 이 직교이므로 다음이 성립한다. 

    $$ 0 = \big <v_2,w_1 \big > = \big <w_2-cw_1,w_1 \big > = \big <w_2,w_1 \big >-c \big <w_1,w_1 \big > $$

    따라서 $c = \dfrac{\big <w_2,w_1 \big >}{\|w_1\|^{2}} \implies v_2 = w_2 - \dfrac{\big <w_2,w_1 \big >}{\|w_1\|^{2}}w_1$ 이다. 

- 증명

    $S_k = \{w_1, w_2, \dots, w_k\}$ 으로 두자.

    $n = 1$ 이면 $v_1 = w_1 \neq 0$ 에서 $S'_1 = S_1$ 이므로 증명이 끝난다. ▲ 

    그람-슈미트 직교화 $(6.1)$ 로 얻은 집합 $S' _{k-1} = \{v_1, v_2, \dots, v _{k-1}\}$ 에서 정리가 성립함을 가정하고 $S'_k = \{v_1, v_2, \dots, v_k\}$ 에서 성립함을 보이면 증명이 끝난다. 이때 $v_k$ 는 $S'_{k-1}$ 에 그람-슈미트 직교화를 적용하여 얻은 벡터이다.

    [정리 1.5](../VectorSpace/#aad599671) 에 의하여 $\text{span} (S_k), \text{span} (S'_k)$ 는 $\mathbf{V}$ 의 부분공간이다. $(6.1)$ 은 $S'_k$ 의 원소들이 $S_k$ 의 일차결합으로 나타나므로 $\text{span} (S'_k) \subset \text{span} (S_k)$ 임을 말해준다. 따라서 $\text{span} (S'_k)$ 는 $\text{span} (S_k)$ 의 부분공간이다. 
    
    $i \in \{1, \dots, k-1\}$ 에 대하여 $v_k$ 와 $v_i$ 의 내적 $\big <v_k,v_i \big >$ 는 $(6.1)$ 과 [내적이 첫번째 성분에 대하여 선형](#3874b2a1f)이라는 사실과 $S' _{k-1}$ 이 직교집합이므로 $i \neq j$ 에 대하여 $\big <v_j,v_i \big > = 0$ 이라는 사실에 의하여 다음과 같다.

    $$ \big <v_k,v_i \big > = \big <w_k,v_i \big > - \sum_{j=1}^{k-1}\dfrac{\big <w_k,v_j \big >}{\|v_j\|^{2}}\big <v_j,v_i \big > = \big <w_k,v_i \big > - \dfrac{\big <w_k,v_j \big >}{\|v_j\|^{2}} \|v_i\|^{2} $$

    이 결과는 $v_k$ 가 $v_1, v_2, \dots, v _{k-1}$ 와 직교임을 말해준다. $v_k = 0$ 이면 $(6.1)$ 에 의하여 $w_k \in \text{span} (S'_{k-1}) = \text{span} (S' _{k-1})$ 인데, 이는 $S_k$ 가 일차독립이라는 가정에 모순이다. 따라서 $v_k \neq 0$ 이다.

    따라서 정리 6.3 따름정리 2 에 의하여 $S'_k$ 는 일차독립이다. 그러므로 $\dim (\text{span} (S'_k)) = \dim (\text{span} (S_k)) = k$ 이다. [정리 1.11](../VectorSpace/#26f9238cb) 에 의하여 $\text{span} (S_k) = \text{span} (S'_k)$ 이다. ■ 

- 예시 

    내적 $\big <f(x),g(x) \big > = \int_{-1}^{1}f(t)g(t)dt$ 가 주어진 벡터공간 $\mathbf{P}_{}(\R)$ 의 부분공간 $\mathbf{P}_{2}(\R)$ 와 표준 순서기저 $\beta={1,x,x ^{2}}$ 를 가정하자. 그람-슈미트 직교화로 $\beta$ 를 직교기저 $\{v_1,v_2,v_3\}$ 로 변환하고 정규화를 통하여 $\mathbf{P}_{2}(\R)$ 의 정규직교기저를 구해보자. 

    $v_1 = 1$ 이므로 $\|v_1\|^{2} = \int_{-1}^{1}1 ^{2}dt = 2$ 이고 $\big <x,v_1 \big > = \int_{-1}^{1}t \cdot t dt = 0$ 이다. 따라서 $v_2$ 는 다음과 같다. 

    $$ v_2 = x - \dfrac{\big <v_1,x \big >}{\|v_1\|^{2}}v_1 = x - 0 = x $$ 

    같은 방식으로 $v_3 = x ^{2} - \frac{1}{3}$ 도 얻는다. 따라서 $\mathbf{P}_{2}(\R)$ 의 직교기저는 $\bigg \{1, x, x ^{2} - \dfrac{1}{3} \bigg \}$ 이다. 이를 정규화하면 $\bigg \{\dfrac{1}{\sqrt[]{2}}, \sqrt[]{\dfrac{3}{2}}x, \sqrt[]{\dfrac{5}{8}}(3x ^{2}-1)\bigg \}$ 을 얻는다. 이는 $\mathbf{P}_{2}(\R)$ 의 정규직교기저이다.

## Legendre Polynomial

!!! tldr "르장드르 다항식(Legendre polynomial)"

    $\mathbf{P}_{}(\R)$ 의 표준순서기저 $\{1,x,x ^{2}, \dots\}$ 에 그람-슈미트 직교화를 적용하여 얻은 직교기저 $\{v_1, v_2, \dots\}$ 에 대한 다항식 $\dfrac{v_k}{v_k(1)}$ 를 $k$차 르장드르 다항식이라 한다.

- 처음 세 르장드르 다항식은 $1, x, \frac{1}{2}(3x ^{2}-1)$ 이다.

## Inner Product Space has an Orthonormal Basis

!!! tldr "정리 6.5"

    점공간이 아닌 유한차원 내적공간에는 정규직교기저가 존재한다.

    점공간이 아닌 유한차원 내적공간 $\mathbf{V}$ 의 정규직교기저 $\beta= \{v_1, v_2, \dots, v_n\}$ 에 대하여 다음이 성립한다.
    
    $$x \in \mathbf{V} : x = \sum_{i=1}^{n}\big <x,v_i \big >v_i $$

- **이 정리는 내적공간의 가장 중요한 결론들 중 하나이다.**

- 이 정리는 내적공간은 정규직교기저를 가진다는 중요한 사실을 말해준다. 또한 임의의 벡터를 정규직교기저의 일차결합으로 나타내는 방법을 말해준다.

- 증명

    [벡터공간에는 기저가 존재한다.](../VectorSpace/#2b881d6d6) $\mathbf{V}$ 의 순서기저 $\beta _0$ 에 대하여 그람-슈미트 직교화로 직교집합 $\beta '$ 를 얻을 수 있고, $\text{span} (B') = \text{span} (\beta _0) = \mathbf{V}$ 이다. $\beta '$ 를 정규화하면 정규직교집합 $\beta$ 을 얻는다. 정리 6.3 따름정리 2 에 의하여 $\beta$ 는 일차독립이므로 정규직교기저이다. ▲ 
    
    정규직교기저 $\beta$ 의 존재성 증명이 끝났으니 나머지 증명은 정리 6.3 따름정리 1 에서 바로 나온다. ■ 

!!! tldr "정리 6.5 따름정리"

    정규직교기저 $\beta = \{v_1, v_2, \dots, v_n\}$ 를 갖는 유한차원 내적공간 $\mathbf{V}$ 와 선형연산자 $\mathbf{T}$ 에 대하여 $A = [\mathbf{T}]_{\beta }$ 로 두면 임의의 $i, j$ 에 대하여 $A _{ij} = \big <\mathbf{T}(v_j), v_i \big >$ 이다.

- 이 정리를 사용하면 선형연산자의 정규직교기저에 대한 행렬표현 성분을 쉽게 구할 수 있다.

- 증명

    정리 6.5 에 의해 $\mathbf{T}(v_j) = \displaystyle \sum_{i=1}^{n}\big <\mathbf{T}(v_j), v_i \big >v_i$ 이다. 즉, $A _{ij} = \big <\mathbf{T}(v_j), v_i \big >$ 이다.

<!-- !!! tldr "푸리에 계수(Fourier coefficient)"

    내적공간 $\mathbf{V}$ 의 정규직교 부분집합 $\beta$ 와 $x \in \mathbf{V}$ 와 $y \in \beta$ 에 대하여 $\big <x,y \big >$ 를 $\beta$ 에 대한 $x$ 의 푸리에 계수라 한다.

- $\beta$ 가 무한집합일 수도 있다. -->

# Orthogonal Complements

!!! tldr "직교여공간(Orthogonal complement)"

    내적공간 $\mathbf{V}$ 의 공집합이 아닌 부분집합 $S$ 에 대하여 다음과 같이 정의된 집합 $S^{\perp}$ 을 $S$ 의 직교여공간이라 한다.

    $$ S^{\perp} = \{x \in \mathbf{V} : \forall y \in S : \big <x,y \big >= 0 \} $$

- 즉, 직교여공간은 $S$ 의 모든 벡터와 수직인 벡터 집합이다.

!!! tldr ""

    직교여공간은 부분공간이다.

- 증명

    [정리 1.3](../VectorSpace/#subspace) 을 기반으로 내적공간 $\mathbf{V}$ 의 부분집합 $S$ 에 대한 직교여공간 $S ^{\perp}$ 가 부분공간인지 판별해보면 된다. 

    내적의 성질에 의하여 $\forall x \in S : \big <x, 0 \big > = 0$ 이므로 $0 \in S ^{\perp}$ 이다. ▲ 

    $x \in S$ 에 대하여 $\big <x,y \big > = 0, \big <x,z \big > = 0$ 이면 $\big <x,y+z \big > = \big <x,y \big > + \big <x,z \big > = 0$ 이므로 $y+z \in S ^{\perp}$ 이다. ▲ 

    $x \in S$ 에 대하여 $\big <x,y \big > = 0$ 이면 스칼라 $c$ 에 대하여 $\big <cy,x \big > = c \big <y,x \big > = c \overline{\big <x,y \big >} = c \cdot \overline{0} = 0$ 이므로 $cy \in S ^{\perp}$ 이다. ■ 

- 예시

    내적공간 $\mathbf{V}$ 에 대하여 $\{0\}^{\perp} = \mathbf{V}$ 이고 $\mathbf{V}^{\perp}=\{0\}$ 이다.

- 예시 

    내적공간 $\R ^{3}$ 의 부분집합 $S = \{e_3\}$ 에 대하여 $S ^{\perp}$ 는 $xy$평면이다. $x = (x_1, x_2, x_3)\in \R ^{3}$ 로 두면 $e_3$ 와 직교하기 위하여 $x_3 = 0$ 이어야 한다. 즉, 다음이 성립한다.

    $$ \begin{equation}\begin{split} S ^{\perp} &= \{x \in \R ^{3} : x \cdot (0, 0, 1) = 0\} \\ &=  \{(x, y, 0) \in \R ^{3} : x, y \in \R \} \\ \end{split}\end{equation} \tag*{} $$

    사실은 직관적으로도 다음 그림과 같이 $z$축 선상에 존재하는 벡터와 직교인 벡터들을 모으면 너무 자명하게 $xy$ 평면이 된다.

    ![image](https://user-images.githubusercontent.com/16812446/129469457-b819249c-188d-4258-9537-7c827dd9d579.png)

## Orthogonal Projection

!!! tldr "문제 6.2-7"

    내적공간 $\mathbf{V}$ 의 부분공간 $\mathbf{W}$ 의 기저 $\beta$ 와 벡터 $z \in \mathbf{V}$ 에 대하여 다음이 성립한다.
    
    $$ z \in \mathbf{W}^{\perp} \iff \forall v \in \beta : \big <z,v \big >= 0 $$

- 이 정리는 벡터가 $\mathbf{W}^{\perp}$ 에 속하기 위해서는 $\mathbf{W}$ 의 기저와 직교하기만 하면 된다는 것을 말해준다.

- 증명

    $z \in \mathbf{W}^{\perp} = \{x \in \mathbf{V}: \forall y \in \mathbf{W}:\big <x,y \big >= 0\}$ 를 가정하면 $\beta \subset \mathbf{W}$ 이므로 $\forall v \in \beta : \big <z,v \big > = 0$ 은 자명하다. ▲ 

    $\forall v \in \beta : \big <z,v \big > = 0$ 을 가정하자. $\beta = \{w_1, w_2, \dots, w_n\}$ 로 두면 $y \in \mathbf{W}$ 와 스칼라 $a_1, a_2, \dots, a_n \in \mathbf{F}$ 에 대하여 $y = \displaystyle \sum_{i=1}^{n}a_iw_i$ 이므로 다음이 성립한다. 

    $$ \big <y,z \big > = \big <\sum_{i=1}^{n}a_iw_i, z \big > = \sum_{i=1}^{n}a_i \big <w_i,z \big > = 0 \tag*{■} $$

!!! tldr "정리 6.6"

    내적공간 $\mathbf{V}$ 의 유한차원 부분공간 $\mathbf{W}$ 와 벡터 $y \in \mathbf{V}$ 에 대하여 다음이 성립한다.
    
    1. $\mathbf{W}$ 의 정규직교기저 $\{v_1, v_2, \dots, v_k\}$ 와 벡터 $u = \displaystyle \sum_{i=1}^{k}\big <y,v_i \big >v_i \in \mathbf{W}$ 에 대하여 $y - u \in \mathbf{W}^{\perp}$ 이다.

    2. $y - u \in \mathbf{W}^{\perp}$ 을 만족하게 하는 벡터 $u \in \mathbf{W}$ 가 유일하게 존재한다. 

- **이 정리는 내적공간 $\mathbf{V}$ 의 임의의 벡터 $y \in \mathbf{V}$ 에 대하여 $y = u + z$ 를 만족하는 $u \in \mathbf{W}, z \in \mathbf{W}^{\perp}$ 가 유일하게 존재함을 말해준다. 즉, [집합의 합](../Diagonalization/#f68ccee5d) 에 대하여 $\mathbf{V} = \mathbf{W}+\mathbf{W}^{\perp}$ 라는 것이다. 앞으로 이 정리는 이러한 형태의 명제로 자주 사용될 것이다.**  1) 이 $y = u + z$ 을 말해주고 2) 가 $u$ 의 유일성을 말해주는데 $u$ 의 유일성이 $z$ 의 유일성을 함의하므로 정리에서는 생략되었다. 

- 가령 다음과 같이 내적공간 $\R ^{3}$ 에서 점 $P$ 와 평면 $\mathbf{W}$ 사이의 거리를 구하는 문제가 존재한다.

    ![image](https://user-images.githubusercontent.com/16812446/129475802-dadd142b-071b-4810-b03b-6da575e6f1ae.png)

    $\overline{OP}$ 을 벡터 $y$ 로 두면 이 문제는 $\mathbf{W}$ 의 벡터 중 $y$ 와 가장 가까운 벡터 $u$ 에 대하여 $\|y-u\|$ 를 계산하는 것이 된다. 위 그림이 보여주듯 $z = y-u$ 는 $\mathbf{W}$ 와 수직이다. 즉, $z \in \mathbf{W}^{\perp}$ 이다.

    이 정리는 그러한 $u$ 를 구하는 방법을 일반화시킨 것이다. 이 정리의 1) 은 $z = y - u \in \mathbf{W}^{\perp}$ 이 되게 하는 $u$ 의 존재성을 말해주고, 2) 는 그 $u$ 의 유일성을 말해준다.

- 증명

    1:

    $y \in \mathbf{V}, u \in \mathbf{W}$ 에 대하여 $z = y - u$ 라고 두고 $z \in \mathbf{W}^{\perp}$ 임을 보이자. 문제 6.2-7 에 의하여 $z$ 가 각 $v_j$ 에 수직임을 보이면 된다. $v_j$ 가 정규화된 기저이므로 $\big <v_j,v_j \big > = \|v_j\|^{2} = 1 ^{2} = 1$ 이고, 다음이 성립한다.

    $$ \begin{equation}\begin{split} \big <z,v_j \big >&= \bigg <\bigg ( y - \sum_{i=1}^{k}\big <y,v_i \big >v_i\bigg ), v_j \bigg > = \big <y,v_j \big >- \sum_{i=1}^{k}\big <y,v_i \big >\big <v_i,v_j \big > \\ &= \big <y,v_j \big >- \big <y,v_j \big > = 0\\ \end{split}\end{equation} \tag*{} $$

    2:

    $y - u' = z' \in \mathbf{W}^{\perp}$ 을 만족하는 $u' \in \mathbf{W}$ 가 존재하면 $y = u + z = u' + z'$ 이다. 부분공간은 합에 대하여 닫혀있으므로 $u - u' = z' - z \in \mathbf{W}\cap \mathbf{W}^{\perp} = \{0\}$ 이다. 즉, $u = u'$ 이다. ■ 

- 프리드버그 선대수에서 서술한 원래의 정리 6.6 는 아래와 같다. 하지만 논리 관계가 이상한 것 같아서 임의로 정리를 수정했다.

    *내적공간 $\mathbf{V}$ 의 유한차원 부분공간 $\mathbf{W}$ 와 벡터 $y \in \mathbf{V}$ 에 대하여 $y = u + z$ 인 벡터 $u \in \mathbf{W}, z \in \mathbf{W}^{\perp}$ 가 유일하게 존재한다.*

    *$\{v_1, v_2, \dots, v_k\}$ 가 $\mathbf{W}$ 의 정규직교기저일 때 다음이 성립한다.*

    $$ u = \sum_{i=1}^{k}\big <y,v_i \big >v_i $$

!!! tldr "문제 6.1-10"

    내적공간 $\mathbf{V}$ 와 서로 직교하는 두 벡터 $x, y \in \mathbf{V}$ 에 대하여 $\|x+y\|^{2} = \|x\|^{2} + \|y\|^{2}$ 이다.

- 이 정리를 유클리드 공간 $\R ^{2}$ 로 특수화시키면 그 유명한 피타고라스의 정리를 얻는다.

- 증명

    $$ \|x+y\|^{2} = \big <x+y,x+y \big > = \big <x,x \big > + \big <x,y \big > + \big <y,x \big > + \big <y,y \big > = \|x\|^{2} + 0 + \overline{\big <x,y \big >} + \|y\|^{2} = \|x\|^{2} + \|y\|^{2} $$

!!! tldr "정리 6.6 따름정리"
    
    내적공간 $\mathbf{V}$ 의 유한차원 부분공간 $\mathbf{W}$ 와 벡터 $y \in \mathbf{V}$ 와 $\mathbf{W}$ 의 정규직교기저 $\{v_1, v_2, \dots, v_k\}$ 와 벡터 $u = \displaystyle \sum_{i=1}^{k}\big <y,v_i \big >v_i \in \mathbf{W}$ 에 대하여 다음이 성립한다.

    $$ \forall x \in \mathbf{W}: \|y - x\| \geq \|y-u\| $$

    이때 $x = u$ 인 것과 $\|y-x\| = \|y-u\|$ 인 것은 동치이다.

- 이 정리는 정리 6.6 의 $u$ 가 $\mathbf{W}$ 의 벡터 중 $y$ 에 가장 가까운 유일한 벡터임을 말해준다. $\forall x \in \mathbf{W}: \|y - x\| \geq \|y-u\|$ 라는 조건이 유일성을 함의한다.

- 증명

    정리 6.6 에서의 $u$ 는 $y \in \mathbf{V}$ 에 대하여 $z = y - u \in \mathbf{W}^{\perp}$ 을 보였다. 따라서 $x \in \mathbf{W}$ 에 대하여 다음이 성립한다.

    $$ \big <u-x,z \big > = \big <u,z \big >- \big <x,z \big > = 0 - 0 = 0 $$

    즉, $u - x$ 는 $z$ 와 직교한다. 문제 6.1-10 에 의하여 다음이 성립한다. 

    $$ \|y-x\|^{2} = \|u+z-x\|^{2} = \|u-x\|^{2} + \|z\|^{2} \geq \|z\|^{2} = \|y-u\|^{2} \tag*{▲} $$

    $\|y-x\| = \|y-u\|$ 로 두면 $\|u-x\|^{2} + \|z\|^{2} = \|z\|^{2}$ 이고 $\|u-x\| = 0 \iff x = u$ 이다. 이것의 역은 자명하다. ■ 

!!! tldr "정사영(orthogonal projection)"

    내적공간 $\mathbf{V}$ 의 유한차원 부분공간 $\mathbf{W}$ 와 벡터 $y \in \mathbf{V}$ 와 $\mathbf{W}$ 의 정규직교기저 $\{v_1, v_2, \dots, v_k\}$ 에 대하여 다음 벡터 $u$ 를 $y$ 의 $\mathbf{W}$ 에 대한 정사영이라 한다.

    $$ u = \sum_{i=1}^{k}\big <y,v_i \big >v_i \in \mathbf{W} $$
    
- 정리 6.6 은 비유적으로 말해서 벡터 $y$ 의 종점에 부분공간 $\mathbf{W}$ 방향으로 빛을 비췄을 때 정사영 $u$ 가 부분공간 $\mathbf{W}$ 에 생기는 그림자이고, 그 그림자가 유일함을 말해준다. 

    정리 6.6 따름정리는 벡터 $y$ 의 종점과 부분공간 $\mathbf{W}$ 사이의 최단거리가 정사영 $u$ 에 의하여 결정된다는 것을 말해준다.

- 우리는 유클리드 공간 $\R ^{2}$ 에서 영이 아닌 벡터 $a \in \R ^{2}$ 와 직선을 이루는 부분공간 $y = \{ta : t \in \R\}$ 와 임의의 벡터 $b \in \R ^{2}$ 에 대하여 $y$ 에 대한 $b$ 의 정사영이 다음과 같다는 것을 아마도 배웠을 것이다.

    $$ \dfrac{a \cdot b}{a \cdot a}a = \dfrac{\big <a,b \big >}{\big <a,a \big >}a = \dfrac{\big <a,b \big >}{\|a\|^{2}}a $$

    직선을 이루는 부분공간 $y$ 는 1차원이므로 $k = 1$ 이다. 또한 $y$ 의 기저는 $\{a\}$ 이고 이것을 [그람-슈미트 직교화](#0ee45a6c5)를 해도 $\{a\}$ 이다. 따라서 [정규화](#ed05bfed9)로 정규직교기저를 만들면 $\bigg \{\dfrac{a}{\|a\|} \bigg \}$ 가 된다. 따라서 이 정리를 사용하여 정사영을 구해보면 [내적의 정의](#3874b2a1f) 와 [내적의 성질](#99baac14a) 에 의하여 다음과 같다. 

    $$ \bigg <b, \dfrac{a}{\|a\|}\bigg > \dfrac{a}{\|a\|} = \overline{\dfrac{1}{\|a\|}} \overline{\big <a,b \big >}\dfrac{a}{\|a\|} = \dfrac{\big <a,b \big >}{\|a\|^{2}}a $$
    
    같은 결과가 나오는 것을 알 수 있다. 이 결과는 이 정의가 2차원 혹은 3차원 유클리드 공간에서 배웠던 정사영을 임의의 내적공간으로 추상화시킨 것임을 말해준다. 

- 예시 

    내적공간 $\mathbf{P}_{3}(\R)$ 와 벡터 $f(x), g(x) \in \mathbf{P}_{3}(\R)$ 에 대하여 $\mathbf{P}_{3}(\R)$ 에 내적 $\big <f(x),g(x) \big > = \displaystyle \int_{-1}^{1}f(t)g(t)dt$ 이 주어졌다고 하자. 함수 $f(x) = x ^{3} \in \mathbf{P}_{3}(\R)$ 의 $\mathbf{P}_{2}(\R)$ 에 대한 정사영 $f_1(x)$ 을 구해보자. 

    $\big <u_1,u_2,u_3 \big > = \bigg \{\dfrac{1}{\sqrt[]{2}}, \sqrt[]{\dfrac{3}{2}}x, \sqrt[]{\dfrac{5}{8}}(3x ^{2} - 1) \bigg \}$ 은 $\mathbf{P}_{2}(\R)$ 의 정규직교기저이므로 다음이 성립한다. 

    $$ \big <f(x),u_1 \big >=0 $$

    $$ \big <f(x),u_2 \big >=\frac{\sqrt[]{6}}{5} $$

    $$ \big <f(x),u_3 \big >=0 $$

    따라서 $f_1(x) = 0 \cdot u_1 + \dfrac{\sqrt[]{6}}{5}u_2 + 0 \cdot u_3 = \dfrac{3}{5}x$ 이다.

## Properties of Orthogonal Complements

!!! tldr "문제 6.2-8"

    영이 아닌 벡터로 이루어진 직교집합에 그람-슈미트 직교화를 하면 동일한 집합이 나온다.

- 증명

    영이 아닌 벡터로 이루어진 직교집합 $S = \{w_1, w_2, \dots, w_k\}$ 에 그람-슈미트 직교화를 적용하여 얻은 직교집합 $S' = \{v_1, v_2, \dots, v_k\}$ 에 대하여 $S = S'$ 임을 보이자. 

    $k = 1$ 을 가정하면 자명하게 성립한다. ▲ 

    $k = n - 1$ 에서 정리가 성립함을 가정하면 [그람-슈미트 직교화](#0ee45a6c5) 에 의하여 다음이 성립한다.

    $$ 
    \begin{equation}\begin{split}
    v_n &= w_n - \sum_{j=1}^{n-1}\dfrac{\big <w_n, v_j \big >}{\|v_j\|^{2}}v_j = w_n - \sum_{j=1}^{n-1}\dfrac{\big <v_n, v_j \big >}{\|v_j\|^{2}}v_j\\
    &= w_n - \sum_{j=1}^{n-1}\dfrac{0}{\|v_j\|^{2}}v_j = w_n\\
    \end{split}\end{equation} \tag*{}
    $$

    이로써 증명이 끝났다. ■ 

!!! tldr "정리 6.7"

    유한차원 내적공간 $\mathbf{V}$ 의 정규직교집합 $S$ 에 대하여 다음이 성립한다. 

    1. $S \subset \beta$ 인 $\mathbf{V}$ 의 정규직교기저 $\beta$ 가 존재한다.

    2. $\mathbf{W}=\text{span} (S)$ 이면 $\beta \setminus S$ 는 $\mathbf{W}^{\perp}$ 의 정규직교기저이다.

    3. $\mathbf{V}$ 의 임의의 부분공간 $\mathbf{W}$ 에 대하여 $\dim (\mathbf{V}) = \dim (\mathbf{W}) + \dim (\mathbf{W}^{\perp})$ 이다.

- [대체정리 따름정리 2](../VectorSpace/#cd7879a47) 는 유한차원 벡터공간에서 임의의 일차독립 집합을 기저로 확장할 수 있음을 말해준다. 이 정리는 유한차원 내적공간의 정규직교 집합에 대하여 비슷한 결과가 성립함을 말해준다.

- 증명

    $\dim (\mathbf{V}) = n$ 으로 두고 $S = \{v_1, v_2, \dots, v_k\}$ 로 두자.

    1:

    [대체정리 따름정리 2](../VectorSpace/#cd7879a47) 와 [정리 6.3 따름정리 2](#562252827) 에 의하여 $S$ 를 확장하여 $\mathbf{V}$ 의 순서기저 $S' = \{v_1, v_2, \dots, v_k, w _{k+1}, \dots, w_n\}$ 을 얻을 수 있다. $S'$ 에 그람-슈미트 직교화를 적용하자. 이렇게 얻은 처음 $k$ 개의 벡터는 문제 6.2-8 에 의하여 $S$ 의 벡터와 같으므로 나머지 $n - k$ 개의 벡터를 정규화하면 정규직교기저 $\beta = \{v_1, v_2, \dots, v_n\}$ 를 얻는다.

    2:

    $\beta \setminus S$ 는 기저의 부분집합이므로 일차독립이고, $S$ 와 직교하므로 [생성집합이 기저를 포함한다는 사실](../VectorSpace/#6cc9cb96b) 과 [문제 6.2-7](#a9dacd0a6) 에 의하여 $\beta \setminus S \subset \mathbf{W}^{\perp}$ 이다.

    정리 6.5 에 의하여 $\forall x \in \mathbf{V} : \displaystyle \sum_{i=1}^{n}\big <x,v_i \big >v_i$ 이다. $w \in \mathbf{W}^{\perp}$ 라면 $i \in \{1,\dots,k\} : \big <x,v_i \big > = 0$ 이므로 다음이 성립한다. 

    $$ x = \sum_{i=k+1}^{n}\big <x_i,v_i \big >v_i \in \text{span} (\beta \setminus S) $$

    즉, $\beta \setminus S$ 는 $\mathbf{W}^{\perp}$ 를 생성한다. 따라서 $\beta \setminus S$ 는 $\mathbf{W}^{\perp}$ 의 정규직교기저이다.

    3:

    $\mathbf{V}$ 의 부분공간 $\mathbf{W}$ 는 $\mathbf{V}$ 의 부분집합으로써 $\mathbf{V}$ 의 성질을 상속받는다. $\mathbf{V}$ 가 유한차원 내적공간이므로 $\mathbf{W}$ 도 유한차원 내적공간이다. 

    정리 6.5 에 의하여 내적공간은 정규직교기저를 가지므로 $\mathbf{W}$ 는 정규직교기저 $\{v_1, v_2, \dots, v_k\}$ 를 가진다. 1) 과 2) 에 의하여 다음이 성립한다. 

    $$ \dim (\mathbf{V}) = n = k + (n - k) = \dim (\mathbf{W}) + \dim (\mathbf{W}^{\perp}) \tag*{■} $$

# Adjoint of Linear Operator

!!! tldr "수반연산자(adjoint)"

    내적공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 와 정규직교기저 $\beta$ 에 대하여 다음을 만족하는 선형연산자 $\mathbf{T}{}^{*}$ 를 $\mathbf{T}$ 의 수반연산자라고 한다.

    $$ [\mathbf{T}{}^{*}]_{\beta } = [\mathbf{T}]{}^{*}_{\beta } $$
    
!!! tldr "정리 6.8"

    유한차원 내적공간 $\mathbf{V}$ 와 정규직교기저 $\{v_1, v_2, \dots, v_n\}$ 와 $\mathbf{g}_{} \in \mathbf{V}{}^{*}$ 와 $y = \displaystyle \sum_{i=1}^{n}\overline{\mathbf{g}_{}(v_i)}v_i \in \mathbf{V}$ 와 $x \in \mathbf{V}$ 에 대하여 다음이 성립한다.

    $$ \exists ! y \in \mathbf{V} : \mathbf{g}_{}(x) = \big <x,y \big > $$

- 이 정리는 내적 $\big <\cdot ,\cdot  \big >:\mathbf{V}\times \mathbf{V}\to \mathbf{F}$ 이 정의된 유한차원 내적공간 $\mathbf{V}$ 의 모든 선형범함수 $\mathbf{V}\to \mathbf{F}$ 가 결국 $\big <x,y \big >$ 와 같음을 말해준다. 

- 증명

    함수 $\mathbf{h}_{}:\mathbf{V}\to \mathbf{F}, x \mapsto \big <x,y \big >$ 를 정의하면 $\mathbf{h}_{}$ 는 선형이다. 또한 $j \in \{1,\dots,n\}$ 에 대하여 [내적의 성질](#99baac14a)에 의하여 다음이 성립한다. 

    $$ \begin{equation}\begin{split} \mathbf{h}_{}(v_j) = \big <v_j,y \big >&= \bigg <v_j,\sum_{i=1}^{n}\overline{\mathbf{g}_{}(v_i)}v_i \bigg > \\ &= \sum_{i=1}^{n}\mathbf{g}_{}(v_i)\big <v_j,v_i \big > =\mathbf{g}_{}(v_j)\\ \end{split}\end{equation} \tag*{} $$

    [정리 2.6 따름정리](../LinearTransformation/#52dd3d90f) 에 의하여 $\mathbf{g}_{}=\mathbf{h}_{}$ 이다. 이제 $y$ 의 유일성 증명만 하면 된다. ▲ 

    이제 $\mathbf{g}_{}(x) = \big <x,y \big >$ 를 가정할 수 있다.  $\mathbf{g}_{}(x) = \big <x,y' \big >$ 를 만족하는 $y'$ 가 존재하면 모든 $x$ 에 대하여 $\big <x,y \big >=\big <x,y' \big > \implies y=y'$ 이다. ■ 

!!! tldr "정리 6.9"

    유한차원 내적공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 와 $x, y \in \mathbf{V}$ 에 대하여 $\big <\mathbf{T}(x),y \big > = \big <x,\mathbf{T}{}^{*}(y) \big >$ 인 수반연산자 $\mathbf{T}{}^{*}$ 가 유일하게 존재한다.

- 이 정리는 유한차원 내적공간에서 선형연산자의 수반연산자의 존재성과 유일성을 보장해준다.

    무한차원 내적공간에서는 선형연산자의 수반연산자가 존재하지 않을 수도 있다. 그러나 특별한 언급이 없으면 무한차원 내적공간에 선형연산자의 수반연산자가 존재한다고 가정하겠다.

- 이 정리에서 함수 $\mathbf{T}{}^{*}$ 의 존재성과 유일성과 선형성을 모두 증명했지만 다음 조건을 만족하는 수반연산자임은 증명하지 않았다. 

    $$ [\mathbf{T}{}^{*}]_{\beta } = [\mathbf{T}]{}^{*}_{\beta } $$

    정리 6.10 은 정리 6.9 에서 $\big <\mathbf{T}(x),y \big > = \big <x,\mathbf{T}{}^{*}(y) \big >$ 을 만족하도록 정의된 선형연산자 $\mathbf{T}{}^{*}$ 가 수반연산자임을 보장해준다.

- 증명

    $y \in \mathbf{V}$ 를 고정하고 임의의 $x \in \mathbf{V}$ 에 대하여 함수 $\mathbf{g}_{}:\mathbf{V}\to \mathbf{F}, x \to \big <\mathbf{T}(x),y \big >$ 를 정의하자.
    
    $x_1, x_2 \in \mathbf{V}, c \in \mathbf{F}$ 에 대하여 다음이 성립한다. 

    $$ \begin{equation}\begin{split} \mathbf{g}_{}(cx_1+x_2)&=\big <\mathbf{T}(cx_1+x_2),y \big > =\big <c \mathbf{T}(x_1) + \mathbf{T}(x_2),y \big >\\ &= c \big <\mathbf{T}(x_1),y \big >+\big <\mathbf{T}(x_2),y \big > = c \mathbf{g}_{}(x_1) + \mathbf{g}_{}(x_2)\\ \end{split}\end{equation} \tag*{} $$

    따라서 $\mathbf{g}_{}$ 는 선형이다. ▲ 

    정리 6.8 에 의하여 $\mathbf{g}_{}(x) = \big <x,y' \big >$ 이 되는 유일한 $y'$ 가 존재하므로 $\big <\mathbf{T}(x),y \big > = \big <x,y' \big >$ 이다. 함수 $\mathbf{T}{}^{*}:\mathbf{V}\to \mathbf{V}, y \mapsto y'$ 를 정의하면 $\big <\mathbf{T}(x),y \big > = \big <x,\mathbf{T}{}^{*}(y) \big >$ 이다. ▲ 

    $y_1, y_2 \in \mathbf{V}, c \in \mathbf{F}$ 를 고정하면 임의의 $x \in \mathbf{V}$ 에 대하여 다음이 성립한다. 

    $$ \begin{equation}\begin{split} \big <x,\mathbf{T}{}^{*}(cy_1 + y_2) \big >&= \big <\mathbf{T}(x),cy_1 + y_2 \big > = \overline{c}\big <\mathbf{T}(x),y_1 \big > + \big <\mathbf{T}(x), y_2 \big >\\ &= \overline{c}\big <x,\mathbf{T}{}^{*}(y_1) \big > + \big <x,\mathbf{T}{}^{*}(y_2) \big > = \big <x, c \mathbf{T}{}^{*}(y_1) + \mathbf{T}{}^{*}(y_2)\big >\\ \end{split}\end{equation} \tag*{} $$

    따라서 $\mathbf{T}{}^{*}$ 는 선형이다. ▲ 

    $\mathbf{U} :\mathbf{V}\to \mathbf{V}$ 가 선형이고 $\forall  x, y \in \mathbf{V}: \big <\mathbf{T}(x), y \big > = \big <x,\mathbf{U} (y) \big >$ 를 만족하면 $\big <x,\mathbf{T}{}^{*}(y) \big > = \big <x,\mathbf{U} (y) \big >$ 이다. 따라서 $\mathbf{T}{}^{*}$ 는 유일하다. ■ 

!!! tldr ""

    유한차원 내적공간의 선형연산자 $\mathbf{T}$ 에 대한 수반연산자 $\mathbf{T}{}^{*}$ 는 다음을 만족하는 유일한 $\mathbf{V}$ 의 연산자이다.

    1. $\big <\mathbf{T}(x),y \big > = \big <x,\mathbf{T}{}^{*}(y) \big >$

    2. $\big <x,\mathbf{T}(y) \big > = \big <\mathbf{T}{}^{*}(x),y \big >$

- 이 정리는 내적 안에서 $\mathbf{T}$ 의 위치를 바꾸면 ${}^{*}$ 가 붙는다는 것을 말해준다.

- 증명

    1) 은 정리 6.9 가 보장해준다. 2) 는 내적의 성질에 의하여 다음이 성립하므로 증명된다. 

    $$ \big <x,\mathbf{T}(y) \big > = \overline{\big <\mathbf{T}(y),x \big >} = \overline{\big <y, \mathbf{T}{}^{*}(x) \big >} = \big <\mathbf{T}{}^{*}(x),y \big > $$

!!! tldr "정리 6.10"

    유한차원 벡터공간 $\mathbf{V}$ 와 정규직교기저 $\beta$, 선형연산자 $\mathbf{T}$ 에 대하여 다음이 성립한다. 

    $$ [\mathbf{T}{}^{*}]_{\beta }=[\mathbf{T}]{}^{*}_{\beta } $$

- 이 정리는 정리 6.9 에서 $\big <\mathbf{T}(x),y \big > = \big <x,\mathbf{T}{}^{*}(y) \big >$ 을 만족하도록 정의된 선형연산자 $\mathbf{T}{}^{*}$ 가 수반연산자임을 보장해준다.

- 이 정리는 수반연산자를 구하는 유용한 방법을 알려준다. 또한 이 정리는 수반연산자와 수반행렬의 관계를 알려준다.

- 아래의 정의에서 주의할 점은 $\mathbf{T}{}^{*}$ 가 수반연산자가 아니라 단지 정리 6.9 의 조건을 만족하도록 정의된 함수라는 것이 가정이라는 것이다. 정리 6.9 의 조건으로부터 수반연산자라는 것을 이끌어내는 증명이다.

- 증명

    $A = [\mathbf{T}]_{\beta }, B = [\mathbf{T}{}^{*}]_{\beta }, \beta =\{v_1, v_2, \dots, v_n\}$ 로 두면 [정리 6.5 따름정리](#a2290266a) 와 [내적의 성질](#99baac14a)과 정리 6.9 와 [수반행렬](#8f2c193aa)의 정의에 의하여 다음이 성립한다. 

    $$ B _{ij} = \big <\mathbf{T}{}^{*}(v_j), v_i \big > = \overline{\big <v_i, \mathbf{T}{}^{*}(v_j) \big >} = \overline{\big <\mathbf{T}(v_i), v_j \big >} = \overline{A}_{ji} = (A {}^{*})_{ij} \tag*{■} $$

- 예시 

    $\mathbb{C}$-벡터공간 $\mathbb{C}^{2}$ 의 선형연산자 $\mathbf{T}(a_1, a_2) = (3a_2 + 2a_1i, a_1 - a_2)$  와 표준순서기저 $\beta = \{(1,0), (0,1)\}$ 에 대하여 [선형변환의 행렬표현](../LinearTransformation/#c16bc5e5b) 과 본 정리에 의하여 다음이 성립한다. 

    $$ \mathbf{T}(1,0) = (2i, 1) $$

    $$ \mathbf{T}(0,1) = (3, -1) $$

    $$ [\mathbf{T}]_{\beta } = \begin{pmatrix} 2i&3\\ 1&-1\\ \end{pmatrix} \implies [\mathbf{T}{}^{*}]_{\beta } = \begin{pmatrix} -2i&1\\ 3&-1\\ \end{pmatrix} $$

    따라서 $\mathbf{T}{}^{*}(a_1, a_2) = (a_2 -2a_1i, 3a_1 - a_2)$ 이다.

    - $\R$-벡터공간 $\mathbb{C}^{2}$ 의 표준순서기저는 $\{(1,0),(0,1),(i,0),(0,i)\}$ 이며 선형변환의 행렬표현이 $4 \times 4$ 행렬이 된다.

!!! tldr "정리 6.10 따름정리"

    $$ A \in \mathbf{M}_{n \times n}(\mathbf{F}) : \mathbf{L}_{A {}^{*}} = (\mathbf{L}_{A}){}^{*} $$

- 증명

    $\mathbf{F}^{n}$ 의 표준순서기저를 $\beta$ 로 두면 [정리 2.15](../LinearTransformation/#c3298a7b3) 와 정리 6.10 에 의하여 $[\mathbf{L}_{A}]_{\beta }=A$ 이므로 다음이 성립한다. 

    $$ [(\mathbf{L}_{A}){}^{*}]_{\beta } = [\mathbf{L}_{A}]{}^{*}_{\beta } = A {}^{*} = [\mathbf{L}_{A {}^{*}}]_{\beta } \tag*{■} $$

!!! tldr "정리 6.11"

    내적공간 $\mathbf{V}$ 와 수반연산자가 존재하는 선형연산자 $\mathbf{T}, \mathbf{U}$ 에 대하여 다음이 성립한다.

    1. $(\mathbf{T}+\mathbf{U}){}^{*}=\mathbf{T}{}^{*}+\mathbf{U}{}^{*}$

    2. $\forall c \in \mathbf{F} : (c \mathbf{T}){}^{*} = \overline{c}\mathbf{T}{}^{*}$

    3. $(\mathbf{T}\mathbf{U}){}^{*}=\mathbf{U}{}^{*}\mathbf{T}{}^{*}$

    4. $\mathbf{T}{}^{*}{}^{*}=\mathbf{T}$

    5. $\mathbf{I}{}^{*}=\mathbf{I}$

- 증명

    1: 

    [함수의 합과 스칼라곱의 정의](../LinearTransformation/#63a07e35d) 과 [내적의 성질](#99baac14a) 에 의하여 $x,y \in \mathbf{V}$ 에 대하여 다음이 성립한다. 

    $$ \begin{equation}\begin{split} \big <x, (\mathbf{T}+\mathbf{U}){}^{*}(y) \big >&= \big <(\mathbf{T}+\mathbf{U})(x), y\big > = \big <\mathbf{T}(x) + \mathbf{U}(x),y \big >\\ &= \big <\mathbf{T}(x),y \big >+\big <\mathbf{U}(x), y\big > = \big <x,\mathbf{T}{}^{*}(y) \big > + \big <x, \mathbf{U}{}^{*}(y) \big >\\ &= \big <x,\mathbf{T}{}^{*}(y)+\mathbf{U}{}^{*}(y) \big > = \big <x, (\mathbf{T}{}^{*}+\mathbf{U}{}^{*})(y) \big > \end{split}\end{equation} \tag*{} $$

    2:

    $$ \begin{equation}\begin{split}
    \big <(c \mathbf{T}){}^{*}(x), y \big >&= \big <x, c \mathbf{T}{}(y) \big > = \overline{c}\big <x,\mathbf{T}(y) \big >\\
    &= \overline{c}\big <\mathbf{T}{}^{*}(x),y \big > = \big <\overline{c}\mathbf{T}{}^{*}(x),y \big >\\
    \end{split}\end{equation} \tag*{}
    $$

    3:

    수반연산자의 정의와 [정리 2.11 따름정리](../LinearTransformation/#143fdacba) 에 의하여 다음이 성립한다.

    $$ [(\mathbf{T}\mathbf{U}){}^{*}]_{\beta } = [\mathbf{T}\mathbf{U}]{}^{*} _{\beta } = ([\mathbf{T}]_{\beta }[\mathbf{U}]_{\beta }){}^{*} = [\mathbf{U}]{}^{*} _{\beta }[\mathbf{T}]{}^{*} _{\beta } $$

    $$ [\mathbf{U}{}^{*}\mathbf{T}{}^{*}]_{\beta } = [\mathbf{U}{}^{*}]_{\beta }[\mathbf{T}{}^{*}]_{\beta } = [\mathbf{U}]{}^{*}_{\beta }[\mathbf{T}]{}^{*}_{\beta } $$

    4:

    $$ x, y \in \mathbf{V} : \big <x,\mathbf{T}(y) \big > = \big <\mathbf{T}{}^{*}(x), y\big > = \big <x, \mathbf{T}{}^{*}{}^{*}(y) \big > $$

    5:

    [항등변환의 행렬표현은 항등행렬이므로](../LinearTransformation/#2bb4853fd) 다음이 성립한다. 

    $$ [\mathbf{I}{}^{*}]_{\beta } = [\mathbf{I}]{}^{*}_{\beta } = I {}^{*} = \overline{I^{t}} = I = [\mathbf{I}]_{\beta } $$

!!! tldr "정리 6.11 따름정리"

    $A, B \in \mathbf{M}_{n \times n}(\mathbf{F})$ 에 대하여 다음이 성립한다. 

    1. $(A+B){}^{*}=A {}^{*}+B {}^{*}$

    2. $c \in \mathbf{F} : (cA) {}^{*} = \overline{c}A {}^{*}$

    3. $(AB) {}^{*} = B {}^{*}A {}^{*}$

    4. $A {}^{*}{}^{*}=A$

    5. $I {}^{*}=I$

- 증명

    정리 6.11 과 [정리 2.15](../LinearTransformation/#c3298a7b3) 와 정리 6.10 따름정리에 의하여 다음이 성립한다. 이때 좌변과 우변을 $\beta$ 에 대한 행렬표현으로 변환하고 [정리 2.8](../LinearTransformation/#aa431d8ac) 과 [정리 2.11](../LinearTransformation/#2fc8f26aa) 을 적용한 다음 정리 2.15-(1) 을 적용하면 증명이 끝난다. 

    1:

    $$ \mathbf{L}_{(A+B){}^{*}} = (\mathbf{L}_{(A+B)}){}^{*} = (\mathbf{L}_{A}+\mathbf{L}_{B}){}^{*} = (\mathbf{L}_{A}){}^{*}+(\mathbf{L}_{B}){}^{*} = \mathbf{L}_{A {}^{*}} + \mathbf{L}_{B {}^{*}} $$

    2:

    $$ \mathbf{L}_{(cA){}^{*}} = (\mathbf{L}_{cA}){}^{*} = (c \mathbf{L}_{A}){}^{*} = \overline{c}\mathbf{L}_{A {}^{*}} $$

    3:

    $$ \mathbf{L}_{(AB){}^{*}} = (\mathbf{L}_{AB}){}^{*} = (\mathbf{L}_{A}\mathbf{L}_{B}) {}^{*} = (\mathbf{L}_{B}){}^{*}(\mathbf{L}_{A}){}^{*}=\mathbf{L}_{B {}^{*}}\mathbf{L}_{A {}^{*}} = \mathbf{L}_{B {}^{*}}\mathbf{L}_{A {}^{*}} $$

    4:

    $$ \mathbf{L}_{A {}^{*}{}^{*}} = (\mathbf{L}_{A {}^{*}}) {}^{*} = (\mathbf{L}_{A}){}^{*}{}^{*} = \mathbf{L}_{A} $$

    5:

    $$ \mathbf{L}_{I {}^{*}} = \mathbf{L}_{I}{}^{*} = \mathbf{I}{}^{*} = \mathbf{I} = \mathbf{L}_{I} $$

- 편의상 정리 6.10 으로 증명이 이루어졌지만 수반행렬의 정의를 직접 사용하여 증명할 수도 있다.

!!! tldr "문제 6.3-5-(b)"

    적절한 형상을 갖는 임의의 행렬 $A, B$ 에 대하여 다음이 성립한다. 

    1. $(A+B){}^{*}=A {}^{*}+B {}^{*}$

    2. $c \in \mathbf{F} : (cA) {}^{*} = \overline{c}A {}^{*}$

    3. $(AB) {}^{*} = B {}^{*}A {}^{*}$

    4. $A {}^{*}{}^{*}=A$

    5. $I {}^{*}=I$

- 이 정리는 정사각행렬에서만 성립하는 정리 6.11 따름정리를 임의의 행렬에서 성립할 수 있도록 확장한 것이다.
    
- 증명


## Least Squares Approximation

!!! tldr ""

    $x, y \in \mathbf{F}^{n}$ 의 표준내적을 $\big <x,y \big >_{n}$ 라 표기하면 열벡터 $x, y$ 에 대하여 $\big <x,y \big >_{n} = y {}^{*}x$ 이다.

- 증명

    [표준 내적](#755926539) 과 [켤레 전치행렬](#8f2c193aa) 의 정의에 의하여 자명하게 성립한다. ■ 

!!! tldr "보조정리 1"

    $A \in \mathbf{M}_{m \times n}(\mathbf{F}), x \in \mathbf{F}^{n}, y \in \mathbf{F}^{m}$ 에 대하여 다음이 성립한다.

    $$ \big <Ax, y \big >_{m} = \big <x, A {}^{*}y \big >_{n} $$

- 증명

    문제 6.3-5-(b) 에 의하여 다음이 성립한다. 

    $$ \big <Ax, y \big >_{m} = y {}^{*}(Ax) = (y {}^{*}A)x = (A {}^{*}y){}^{*}x = \big <x, A {}^{*}y \big >_{n} \tag*{■} $$

!!! tldr "보조정리 2"

    $$ A \in \mathbf{M}_{m \times n}(\mathbf{F}) : \text{rank} (A {}^{*}A) = \text{rank} (A) $$

- 증명

    차원정리와 행렬의 랭크의 정의에 의하여 다음이 성립한다. 

    $$ \text{rank} (A) = \text{rank} (\mathbf{L}_{A}) = \dim (\mathbf{F}^{n}) - \text{nullity} (\mathbf{L}_{A}) = n - \text{nullity} (\mathbf{L}_{A}) $$

    $$ \text{rank} (A {}^{*}A) = \text{rank} (\mathbf{L}_{A {}^{*}A}) = \dim (\mathbf{F}^{n}) - \text{nullity} (\mathbf{L}_{A {}^{*}A}) = n - \text{nullity} (\mathbf{L}_{A {}^{*}A}) $$

    따라서 $A {}^{*}A$ 와 $A$ 의 영공간의 차원이 같음을 보이면 증명이 끝난다. 이는 다시 $A {}^{*}Ax = 0$ 인 것은 $Ax = 0$ 인 것과 동치임을 증명하는 문제가 된다. $Ax = 0$ 이 되게 하는 해공간의 차원이 존재하는데 $A {}^{*}Ax = 0$ 이기 위하여 반드시 $Ax = 0$ 이어야 한다면 $A {}^{*}Ax = 0$ 의 해공간의 차원이 동일해지기 때문이다.

    $Ax = 0 \implies A {}^{*}A = 0$ 은 자명하다. $A {}^{*}Ax = 0$ 을 가정하면 보조정리 2 와 수반연산자의 성질과 문제 6.3-5-(b) 에 의하여 다음이 성립한다. 

    $$ 0 = \big <A {}^{*}Ax, x \big >_{n} = \big <Ax, A {}^{*}{}^{*} x \big >_{m} = \big <Ax, Ax\big >_{m}
    $$

    그러므로 내적의 성질에 의하여 $Ax = 0$ 이다. ■ 

!!! tldr "따름정리"

    $\text{rank} (A) = n$ 인 행렬 $A \in \mathbf{M}_{m \times n}(\mathbf{F})$ 에 대하여 $A {}^{*}A$ 는 가역이다.

- 증명

    [$n \times n$ 행렬의 랭크가 $n$ 이면 가역이다](../MatrixOperation/#8252ffa8b). 보조정리 2 에 의하여 $A {}^{*}A$ 의 랭크는 $n$ 이다. ■ 

!!! tldr "정리 6.12 최소제곱법(least squares approximation)"

    $A \in \mathbf{M}_{m \times n}(\mathbf{F}), y \in \mathbf{F}^{m}$ 에 대하여 다음을 만족하는 $x_0 \in \mathbf{F}^{n}$ 이 존재한다. 

    1. $\forall x \in \mathbf{F}^{n} : \|Ax_0 - y\| \leq \|Ax - y\|$

    2. $(A {}^{*}A)x_0 = A {}^{*}y$

    특히 $\text{rank} (A) = n \implies x_0 = (A {}^{*}A) ^{-1}A {}^{*}y$ 이다.

- 가령 매 시기마다의 실업률을 유클리드 공간 $\R ^{2}$ 의 좌표 $(t_1, y_1), (t_2, y_2), \dots, (t_m, y_m)$ 로 나타내다보니까 이 좌표들의 경향성이 마치 어떤 직선으로 근사될 수 있음을 깨달았다고 하자. 이 직선을 스칼라 $c, d \in \R$ 에 대한 $y = ct + d$ 로 두자.

    ![image](https://user-images.githubusercontent.com/16812446/129932627-b5e4c6f0-1699-4de6-970f-b569e5e5e3d3.png)

    데이터의 좌표와 직선 사이의 $x$축과 수직한 거리의 제곱의 합을 오차 $E$ 로 두고 이 $E$ 를 최소화시키는 스칼라 $c, d$ 를 찾음음로써 근사된 직선을 정의해보자. 따라서 이렇게 정의된 직선을 최소제곱 직선(least squares line) 이라고 부른다. 
    
    먼저 $E$ 는 다음과 같이 정의된다. 

    $$ E = \sum_{i=1}^{m}(y_i - ct_i - d) ^{2} $$

    $A, x, y$ 를 다음과 같이 정의하면 유클리드 거리의 정의에 의하여 $E = \|y - Ax\|^{2}$ 가 된다.

    $$ A = \begin{pmatrix} t_1&1\\ t_2&1\\ \vdots &\vdots \\ t_m&1\\ \end{pmatrix}, x = \begin{pmatrix} c\\ d\\ \end{pmatrix}, y = \begin{pmatrix} y_1\\ y_2\\ \vdots \\ y_m\\ \end{pmatrix} $$

    이 $E$ 를 최소화하는 $x_0 \in \mathbf{F}^{n}$ 은 다음을 만족해야 한다.

    $$ \boxed{\forall x \in \mathbf{F}^{n} : \|Ax_0 - y\| \leq \|Ax - y\|} \tag{1} $$

    $\mathbf{F}^{m}$ 의 부분공간 $\mathbf{W} = \{Ax : x \in \mathbf{F}^{n}\}$ 을 정의하면 $\mathbf{W}= \mathbf{R} (\mathbf{L}_{A})$ 이다. [정리 6.6 따름정리](#bc913e284) 에 의하여 $y$ 에 가장 가까운 $\mathbf{W}$ 의 벡터가 유일하게 존재한다. 이 벡터를 $Ax_0$ 로 두면 $(1)$ 을 만족할 것이다. 그러면 이러한 벡터 $Ax_0$ 는 정리 6.6 에 의하여 $Ax_0 - y \in \mathbf{W}^{\perp}$ 이므로 임의의 $x \in \mathbf{F}^{n}$ 에 대하여 보조정리 1 과 내적의 성질에 의하여 다음이 성립한다.
    
    $$ \big <Ax, Ax_0 - y\big >_{m} = 0 $$

    $$ \iff  \big <x, A {}^{*}(Ax_0 - y ) \big > _{n} = 0 $$

    $$ \iff A {}^{*}(Ax_0 - y) = 0 $$

    따라서 모든 문제는 결국 다음 방정식의 해 $x_0$ 를 구하는 것으로 귀결된다.
    
    $$ \boxed{A {}^{*}Ax = A {}^{*}y} $$

    만약 $\text{rank} (A) = n$ 이면 보조정리 2 에 의하여 다음이 성립하므로 $x_0$ 를 구하는 일이 더욱 쉬워진다. 

    $$ \boxed{x_0 = (A {}^{*}A)^{-1}A {}^{*}y} $$

- 예시 

    위의 설명에서 매 시기 별 실업률 데이터를 조사하는 상황을 예로 들었는데 그러한 데이터가 $(1, 2), (2, 3), (3, 5), (4, 7)$ 이라고 하면 $A, y$ 는 다음과 같다. 

    $$ A = \begin{pmatrix} 1&1\\ 2&1\\ 3&1\\ 4&1\\ \end{pmatrix}, y = \begin{pmatrix} 2\\ 3\\ 5\\ 7\\ \end{pmatrix} $$

    $\text{rank} (A) = 2$ 이므로 $A {}^{*}A$ 는 가역이다. 따라서 다음이 성립한다. 

    $$ A {}^{*}A = \begin{pmatrix} 30&10\\ 10&4\\ \end{pmatrix}, (A {}^{*}A) ^{-1} = \frac{1}{20}\begin{pmatrix} 4&-10\\ -10&30\\ \end{pmatrix} $$

    따라서 다음과 같이 $c, d$ 를 구하여 최소제곱 직선 $y = 1.7t$ 을 구할 수 있다.

    $$ \begin{pmatrix} c\\ d\\ \end{pmatrix} = x_0 = \frac{1}{20}  \begin{pmatrix} 4&-10\\ -10&30\\ \end{pmatrix}\begin{pmatrix} 1&2&3&4\\ 1&1&1&1\\ \end{pmatrix} \begin{pmatrix} 2\\ 3\\ 5\\ 7\\ \end{pmatrix} = \begin{pmatrix} 1.7\\ 0\\ \end{pmatrix} $$

    오차 $E$ 를 계산해보면 $\|Ax_0 - y\|^{2} = 0.3$ 이다.

- 현실세계에서 최소제곱법을 사용하면 행렬 $A$ 의 랭크가 왠만하면 $2$ 가 된다. 왜냐하면 $2$ 가 아니라면 $1$ 열이 $2$ 열의 스칼라 배가 되는데 이는 $1$ 열의 데이터가 모두 같다는 의미가 되기 때문이다. 

- 2차 다항식 $y = ct ^{2} + dt + e$ 으로 데이터를 근사시키고 싶다면 다음과 같이 모델링하면 된다. 

    $$ x = \begin{pmatrix} c\\ d\\ c\\ \end{pmatrix}, y = \begin{pmatrix} y_{1}\\ y_{2}\\ \vdots\\ y_{m}\\ \end{pmatrix}, A = \begin{pmatrix} t_1 ^{2} & t_1 & 1\\ \vdots & \vdots & \vdots \\ t_m ^{2} & t_m & 1\\ \end{pmatrix} $$

    2차원 유클리드 공간의 임의의 선은 무한차 다항식으로 근사시킬 수 있으므로 이 방식을 일반화시키면 선형분류 가능한 모든 데이터를 분류하는 함수를 만들 수 있다. 

## Minimal Solutions to Systems of Linear Equations

!!! tldr "최소해(minimal solution)"

    모순이 없는 연립일차방정식 $Ax = b$ 의 해가 유일하지 않을 때 방정식의 임의의 해 $u$ 에 대하여 $\|s\| \leq \|u\|$ 를 만족하는 $s$ 를 최소해라 한다.

!!! tldr "문제 6.2-6"

    내적공간 $\mathbf{V}$ 와 유한차원 부분공간 $\mathbf{W}$ 에 대하여 다음이 성립한다.
    
    $$ y \in \mathbf{W}^{\perp}\setminus \{0\}: x \in \mathbf{V} \setminus \mathbf{W} \iff \big <x,y \big > \neq 0 $$

- **이 정리는 $\mathbf{W} ^{\perp}$ 와 직교하기 위해서는 반드시 $\mathbf{W}$ 에 속해야 함을 말해준다.** 

    만약 $\mathbf{W}$ 가 부분공간이 아니라 유한집합 $S$ 였다면 $S ^{\perp}$ 와 직교하기 위하여 반드시 $S$ 에 속할 필요가 없을 수도 있다. $\mathbf{V}\setminus S$ 중에서 $S ^{\perp}$ 와 직교하는 벡터가 존재할 수도 있기 때문이다.

- 증명

    $x \in \mathbf{V}\setminus \mathbf{W}$ 을 가정하면 $y \in \mathbf{W}^{\perp}$ 에 대하여 정리 6.6 에 의하여 $x = y + z$ 를 만족하는 $z \in \mathbf{W}$ 가 존재하므로 다음이 성립한다.

    $$ \big <z, y \big > = \big <x - y, y \big > = \big <x, y \big > - \big <y, y\big > = 0 $$

    $$ \iff \big <x, y \big > = \|y\|^{2} $$

    $y = 0$ 이면 $x = 0 + z$ 인데 $x \not\in \mathbf{W}, z \in \mathbf{W}$ 이므로 모순이다. 따라서 $\|y\|^{2} > 0$ 이다. ▲ 

    $\big <x,y \big >\neq 0$ 을 가정하면 $x \not\in \mathbf{W}$ 은 자명하다. ■ 

- 프리드버그 선대수에서 말하는 원래의 정리는 다음과 같은데 논리관계가 이상한 것 같아서 임의로 고쳤다.

    *내적공간 $\mathbf{V}$ 와 유한차원 부분공간 $\mathbf{W}$ 와 $x \in \mathbf{V} \setminus \mathbf{W}$ 에 대하여 $y \in \mathbf{W}^{\perp} \land \big <x,y \big > \neq 0$ 인 벡터 $y \in \mathbf{V}$ 가 존재한다.*

!!! tldr "문제 6.2-13"

    내적공간 $\mathbf{V}$ 의 두 부분집합 $S$ 와 $S_0$ 와 유한차원 부분공간 $\mathbf{W}$ 에 대하여 다음이 성립한다.

    1. $S_0 \subset S \implies S ^{\perp} \subset S_0 ^{\perp}$

    2. $S \subset (S ^{\perp})^{\perp}$
    
    3. $\text{span} (S) \subset (S ^{\perp})^{\perp}$

    4. $\mathbf{W}=(\mathbf{W}^{\perp})^{\perp}$

    5. $\mathbf{V}=\mathbf{W}\oplus \mathbf{W}^{\perp}$
    
- 증명

    1:

    $x \in \mathbf{V}$ 가 $\forall y \in S : \big <x,y \big > = 0$ 를 만족하면 $x \in S ^{\perp}$ 이다. 논의영역 $S$ 를 부분집합 $S_0$ 로 축소시킨 $\forall y \in S_0 : \big <x,y \big > = 0$ 은 참이므로 $x \in S_0 ^{\perp}$ 이다. 따라서 $S ^{\perp}\subset S_0 ^{\perp}$ 이다.

    2:

    $x \in S$ 이면 $\forall y \in S ^{\perp}: \big <x,y \big > = 0$ 이므로 $x$ 는 다음 집합에 포함될 조건을 만족한다. 따라서 $S \subset (S ^{\perp})^{\perp}$ 이다.

    $$ (S ^{\perp})^{\perp} = \{x \in \mathbf{V} : \forall y \in S ^{\perp}: \big <x,y \big > = 0\} $$

    3:

    $S = \{v_1, v_2, \dots, v_n \}$ 로 두면 $w \in \text{span} (S)$ 를 스칼라 $a_1, a_2, \dots, a_n$ 에 대하여 $w = a_1v_1 + a_2v_2 + \dots + a_nv_n$ 로 나타낼 수 있으므로 임의의 $x \in S ^{\perp}$ 에 대하여 다음이 성립한다. 따라서 $w \in (S ^{\perp})^{\perp}$ 이다. 

    $$ \big <w, x \big > = \sum_{i=1}^{n}a_i\big <v_i, x \big > = 0 $$

    4:

    문제 6.2-6 에 의하여 $x \in \mathbf{V}, y \in \mathbf{W}^{\perp}$ 에 대하여 $\big <x,y \big > = 0$ 이면 $x \in \mathbf{W}$ 이다. 따라서 $(\mathbf{W}^{\perp})^{\perp} = \mathbf{W}$ 이다.

    5:

    정리 6.6 은 $\mathbf{V}=\mathbf{W}+\mathbf{W}^{\perp}$ 임을 말해준다. $\mathbf{W}\cap \mathbf{W}^{\perp}=\{0\}$ 이므로 $\mathbf{V}=\mathbf{W}\oplus \mathbf{W}^{\perp}$ 이다.

!!! tldr ""

    내적공간 $\mathbf{V}$ 에 대하여 $\big <x, y \big > = 0$ 인 벡터 $x, y \in \mathbf{V}\setminus \{0\}$ 가 존재한다.

- **이 정리는 $x \neq 0 \land y \neq 0$ 이어도 $\big <x,y \big >=0$ 일 수도 있다는 것을 말해준다.**

- 증명 

    유클리드 공간 $\R ^{2}$ 의 표준기저 $e_1, e_2$ 에 대하여 다음이 성립한다. 

    $$ e_1 \neq 0, e_2 \neq 0, \big <e_1,e_2 \big > = 1 \cdot 0 + 0 \cdot 1 = 0 $$

!!! tldr ""

    내적공간 $\mathbf{V}$ 와 벡터 $y \in \mathbf{V}$ 에 대하여 다음은 동치이다.

    1. $\forall x \in \mathbf{V} : \big <x, y \big > = 0$
    
    2. $y = 0$

- 이 정리는 **내적공간의 모든 벡터와 직교하는 벡터는 영벡터 $0$ 밖에 없다** 는 것을 말해준다. 

- 증명 

    $y = 0$ 을 가정하면 1) 이 바로 나온다. ▲ 

    1) 을 가정하고 $y \neq 0$ 로 두자. 내적의 정의에 의하여 $\big <y,y \big > \neq 0$ 이다. 따라서 $y = 0$ 이다. ■ 

!!! tldr "문제 6.3-12"

    내적공간 $\mathbf{V}$ 와 선형연산자 $\mathbf{T}$ 에 대하여 다음이 성립한다. 

    1. $\mathbf{R} (\mathbf{T}{}^{*})^{\perp} = \mathbf{N} (\mathbf{T})$

    2. $\mathbf{V}$ 가 유한차원이면 $\mathbf{R} (\mathbf{T}{}^{*}) = \mathbf{N} (\mathbf{T})^{\perp}$ 이다.

- 증명

    1:

    $y \in \mathbf{R}(\mathbf{T}{}^{*})^{\perp}$ 를 고정하면 직교여공간의 정의와 상공간의 정의와 정리 6.9 에 의하여 다음이 성립한다.

    $$ \forall x \in \mathbf{V} : \big <\mathbf{T}{}^{*}(x), y \big > = \big <x,\mathbf{T}(y) \big > = 0 $$

    모든 $x \in \mathbf{V}$ 와 직교하는 벡터는 영벡터이므로 $\mathbf{T}(y) = 0$ 이므로 $y \in \mathbf{N}(\mathbf{T})$ 이다. 따라서 $\mathbf{R}(\mathbf{T}{}^{*}) ^{\perp}\subset \mathbf{N}(\mathbf{T})$ 이다. ▲ 

    $y \in \mathbf{N}(\mathbf{T})$ 를 고정하면 $\mathbf{T}(y) = 0$ 이므로 다음이 성립한다.

    $$ \forall x \in \mathbf{V} : \big <\mathbf{T}{}^{*}(x), y \big > = \big <x,\mathbf{T}(y) \big > = 0 $$

    따라서 $y \in \mathbf{R}(\mathbf{T}{}^{*})^{\perp}$ 이다. 즉, $\mathbf{N}(\mathbf{T}) \subset \mathbf{R}(\mathbf{T}{}^{*})^{\perp}$ 이다. ■ 

    2:

    이제 1) 을 가정할 수 있으므로 문제 6.2-13-(4) 에 의하여 다음이 성립한다. 

    $$ (\mathbf{R}(\mathbf{T}{}^{*})^{\perp})^{\perp} = (\mathbf{N}(\mathbf{T}))^{\perp} $$

    $$ \therefore \mathbf{R}(\mathbf{T}{}^{*}) = (\mathbf{N}(\mathbf{T}))^{\perp} \tag*{■}$$

!!! tldr "정리 6.13"

    $A \in \mathbf{M}_{m \times n}(\mathbf{F}), b \in \mathbf{F}^{m}$ 와 모순이 없는 연립일차방정식 $Ax = b$ 에 대하여 다음이 성립한다. 

    1. $Ax = b$ 의 유일한 최소해 $s$ 가 존재한다. 
    
    2. $s \in \mathbf{R} (\mathbf{L}_{A {}^{*}})$

    3. $s$ 는 $\mathbf{R}(\mathbf{L}_{A {}^{*}})$ 에 속하는 $Ax = b$ 의 유일한 해이다. 
    
    4. $(AA {}^{*})u = b$ 인 $u$ 에 대하여 $s = A {}^{*}u$ 이다.

- 1), 2), 3) 이 연립일차방정식의 최소해의 유일성과 존재성을 보장해주고, 4) 가 최소해를 구하는 방법을 말해준다. 

- 증명

    1:

    $Ax = b$ 의 임의의 해 $x$ 에 대하여 정리 6.6 에 의하여 $x = s + y$ 가 되게 하는 $s \in \mathbf{R}(\mathbf{L}_{A {}^{*}})$ 와 $y \in \mathbf{R}(\mathbf{L}_{A {}^{*}})^{\perp}$ 가 존재한다. 문제 6.3-12 와 정리 6.10 따름정리에 의하여 $\mathbf{R}(\mathbf{L}_{A {}^{*}})^{\perp} = \mathbf{N}(\mathbf{L}_{A})$ 이다. 따라서 $b = Ax = As + Ay = As$ 이다. 그러므로 $s$ 는 $Ax = b$ 의 해이다. ▲ 

    $u \in \mathbf{N}(\mathbf{L}_{A})$ 와 $Ax = b$ 의 임의의 해 $v$ 에 대하여 정리 3.9 에 의하여 $v = s + u$ 이다. 문제 6.3-12-(2) 에 의하여 $s \in \mathbf{N}(\mathbf{L}_{A})^{\perp}$ 이므로 문제 6.1-10 에 의하여 다음이 성립한다. 

    $$ \|v\| ^{2} = \|s+u\|^{2} = \|s\|^{2} + \|u\|^{2} \geq \|s\| ^{2} $$

    따라서 $s$ 는 임의의 해 $v$ 보다 항상 같거나 작다. 그러므로 $s$ 는 최소해이다. ▲ 

    $s$ 와 노름이 같은 해가 존재하면 최소해가 된다. 그러니 $\|v\| = \|s\|$ 를 가정하자. 그러면 $u = 0 \implies v = s$ 이므로 최소해 $s$ 는 유일하다. ▲ 

    2:

    1) 의 증명과정에서 증명된다.

    3:

    $v \in \mathbf{R}(\mathbf{L}_{A {}^{*}})$ 가 $Ax = b$ 의 해이면 부분공간은 합에 대하여 닫혀있으므로 $v - s \in \mathbf{R}(\mathbf{L}_{A {}^{*}})$ 이고 $A(v - s) = b - b = 0$ 이므로 $v - s \in \mathbf{N}(\mathbf{L}_{A})$ 이다. 따라서 다음이 성립한다. 

    $$ v - s \in \mathbf{R}(\mathbf{L}_{A {}^{*}}) \cap \mathbf{N}(\mathbf{L}_{A}) = \mathbf{R}(\mathbf{L}_{A {}^{*}}) \cap \mathbf{R}(\mathbf{L}_{A {}^{*}}) = \{0\} $$

    따라서 $v = s$ 이다. ▲ 

    4:

    $(AA {}^{*})u = b$ 를 만족하게 하는 $u$ 에 대하여 $v = A {}^{*}u$ 라고 하면 $v \in \mathbf{R}(\mathbf{L}_{A {}^{*}})$ 이고 $Av = b$ 이다. 그러면 3) 에 의하여 $v = s$ 이고 결국 $s = A {}^{*}u$ 이다. ■ 

- 예시 

    다음 연립일차방정식의 최소해를 찾자.

    $$ x+2y+z = 4 $$

    $$ x-y+2z = -11 $$

    $$ x+5y = 19 $$

    $A, b$ 를 다음과 같이 두면 정리를 사용할 수 있다. 

    $$ A = \begin{pmatrix} 1&2&1\\ 1&-1&2\\ 1&5&0\\ \end{pmatrix}, b = \begin{pmatrix} 4\\ -11\\ 19\\ \end{pmatrix} $$

    그러면 $AA {}^{*}x = b$ 의 해 $u$ 에 대하여 $s = A {}^{*}u$ 를 계산하면 최소해를 찾을 수 있다. $AA {}^{*}$ 는 다음과 같다. 

    $$ AA {}^{*} = \begin{pmatrix} 6&1&11\\ 1&6&-4\\ 11&-4&26\\ \end{pmatrix} $$

    $AA {}^{*}x = b$ 의 해는 $x \in \Bigg \{ \begin{pmatrix} 1 - 2t\\ t - 2\\ t\\ \end{pmatrix} : t \in \R \Bigg \}$ 이다.  $t = 0$ 일 때 $u = \begin{pmatrix} 1\\ -2\\ 0\\ \end{pmatrix}$ 이다. 정리에 의하여 $s = A {}^{*}u = \begin{pmatrix} -1\\ 4\\ -3\\ \end{pmatrix}$ 는 최소해가 된다. 다른 $u$ 를 택해도 상관 없다.

# Normal and Self-Adjoint Operators

!!! tldr "보조정리"

    유한차원 내적공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 가 고유벡터를 가지면 $\mathbf{T}{}^{*}$ 도 고유벡터를 가진다.

- 증명

    고윳값 $\lambda$ 에 대응하는 $\mathbf{T}$ 의 고유벡터를 $v$ 라 하면 임의의 $x \in \mathbf{V}$ 에 대하여 다음이 성립한다. 

    $$  \begin{equation}\begin{split} 0&= \big <0,x \big > = \big <(\mathbf{T} - \lambda \mathbf{I})(v),x \big > \\ &=\big <v,(\mathbf{T}-\lambda \mathbf{I}){}^{*}(x) \big > = \big <v, (\mathbf{T}{}^{*}- \overline{\lambda }\mathbf{I})(x) \big >\\ \end{split}\end{equation} \tag*{} $$

    따라서 $v$ 는 $\mathbf{T}{}^{*}-\overline{\lambda }\mathbf{I}$ 의 치역과 직교한다. 만약 $\mathbf{T}{}^{*}-\overline{\lambda }\mathbf{I} = \mathbf{V}$ 가 되면 $\mathbf{V}$ 의 모든 벡터와 직교하는 벡터는 $0$ 밖에 없으므로 $v = 0$ 인데 이는 모순이다. 따라서 $\mathbf{T}{}^{*}-\overline{\lambda }\mathbf{I}$ 는 전사가 아니다. 그러므로 단사도 아니고, $\mathbf{N}(\mathbf{T}{}^{*}-\overline{\lambda }\mathbf{I}) \neq \{0\}$ 이다. 이 영공간이 속하는 벡터는 고윳값 $\overline{\lambda }$ 에 대응하는 $\mathbf{T}{}^{*}$ 의 고유벡터이다. ■ 

## Schur's theorem

!!! tldr "정리 6.14 슈어의 정리(Schur's theorem)"

    유한차원 내적공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 의 특성다항식이 완전히 인수분해되면 $[\mathbf{T}]_{\gamma }$ 가 상삼각행렬이 되게 하는 정규직교기저 $\gamma$ 가 존재한다.

- 증명

    [문제 5.2-12](../Diagonalization/#bd84c1d47) 에 의하여 $[\mathbf{T}]_{\beta }$ 가 상삼각행렬이 되게 하는 순서기저 $\beta = \{w_1, w_2, \dots, w_n\}$ 이 존재한다. 그람-슈미트 직교화를 통하여 $\beta$ 를 직교기저 $\beta ' = \{v_1, v_2, \dots, v_n\}$ 로 변환할 수 있다. $k \in \{1, \dots, n\}$ 에 대하여 $S_k, S'_k$ 를 다음과 같이 정의하자.

    $$ S_k = \{w_1, w_2, \dots, w_k\}, S'_k = \{v_1, v_2, \dots, v_k\} $$

    [정리 6.4](#0ee45a6c5) 에 의하여 $\text{span} (S_k) = \text{span} (S'_k)$ 이다. $[\mathbf{T}]_{\beta }$ 가 상삼각행렬이 되므로 [문제 2.2-12](../LinearTransformation/#be8fe9c58) 에 의하여 $\mathbf{T}(w_k) \in \text{span} (S_k)$ 이다. [정리 6.4](#0ee45a6c5) 는 $v_k$ 가 $w_1, \dots, w_k$ 의 일차결합으로 표현됨을 말해준다. 따라서 스칼라 $a_1, \dots, a _{k-1}$ 에 대하여 $v_k = w_k + a _{k-1}w _{k-1} + \dots + a_1w_1$ 이다. 그러므로 다음이 성립한다. 

    $$ \mathbf{T}(v_k) = \mathbf{T}(w_k + a _{k-1}w _{k-1} + \dots + a_1w_1) = \mathbf{T}(w_k) + a _{k-1}\mathbf{T}(w _{k-1}) + \dots + a_1 \mathbf{T}(w_1) \in \text{span} (S_k) = \text{span} (S'_k) $$

    따라서 다시 문제 2.2-12 에 의하여 $[\mathbf{T}]_{\beta '}$ 은 상삼각행렬이다.

    이제 $i \in \{1, \dots, n\}$ 에 대하여 $z_i = \dfrac{1}{\left\| v_i \right\| }v_i, \gamma = \{z_1, z_2, \dots, z_n\}$ 를 정의하면 $\gamma$ 는 $\mathbf{V}$ 의 정규직교기저이다. $z_i$ 는 $v_i$ 의 일차결합이므로 결국 $w_i$ 의 일차결합이다. 따라서 위와 같은 논리로 $\mathbf{T}(z_i) \in \text{span} (\{z_1, \dots, z_i\})$ 임을 보일 수 있고, 또 다시 문제 2.2-12 에 의하여 $[\mathbf{T}]_{\gamma }$ 는 상삼각행렬임을 알 수 있다. ■ 

## Normal Operator, Normal Matrix

!!! tldr "정규연산자(normal operator)"

    내적공간 $\mathbf{V}$ 와 선형연산자 $\mathbf{T}$ 가 $\mathbf{T}\mathbf{T}{}^{*} = \mathbf{T}{}^{*}\mathbf{T}$ 를 만족하면 $\mathbf{T}$ 를 정규연산자라 한다.

- 유한차원 내적공간 $\mathbf{V}$ 에서 선형연산자 $\mathbf{T}$ 의 고유벡터로 이루어진 정규직교기저 $\beta$ 가 존재하면 $[\mathbf{T}]_{\beta }$ 는 대각행렬이고 $[\mathbf{T}]{}^{*}_{\beta } = [\mathbf{T}{}^{*}]_{\beta }$ 도 대각행렬이다. 대각행렬은 가환적이다. 즉, 교환법칙이 성립한다. 따라서 $\mathbf{T}$ 와 $\mathbf{T} {}^{*}$ 도 가환적이고 다음 명제가 성립한다. 

    "$\mathbf{V}$ 가 $\mathbf{T}$ 의 고유벡터로 이루어진 정규직교기저를 가지면 $\mathbf{T}\mathbf{T}{}^{*} = \mathbf{T}{}^{*}\mathbf{T}$ 이다."

    선형연산자의 가환성 $\mathbf{T}\mathbf{T}{}^{*}=\mathbf{T}{}^{*}\mathbf{T}$ 을 정규성(normality) 라고 한다. 이러한 정규성을 갖는 연산자를 정규연산자라고 정의하는 것이다. 

    그러나 위 명제의 역이 항상 성립하는 것은 아니다. 즉, 정규성을 가진다고 해서 고유벡터로 이루어진 정규직교기저가 반드시 존재한다는 보장은 없다. 

!!! tldr "정규행렬(normal matrix)"

    체 $\mathbf{F}\in \{\R, \mathbb{C}\}$ 에 대한 행렬 $A \in \mathbf{M}_{n \times n}(\mathbf{F})$ 이 $AA {}^{*} = A {}^{*}A$ 를 만족하면 $A$ 를 정규행렬이라 한다. 

!!! tldr ""

    $\mathbf{T}$ 가 정규연산자인 것과 정규직교기저 $\beta$ 에 대하여 $[\mathbf{T}]_{\beta }$ 가 정규행렬인 것은 동치이다.

- 증명

    $A = [\mathbf{T}]_{\beta }$ 로 두자. $A$ 가 정규행렬이면 $AA {}^{*} = A {}^{*}A$ 이다. 그러면 [정리 6.10](#515861895) 에 의하여 $[\mathbf{T}]_{\beta }[\mathbf{T}{}^{*}]_{\beta } = [\mathbf{T}{}^{*}]_{\beta }[\mathbf{T}]_{\beta }$ 이다. [정리 2.11 따름정리](../LinearTransformation/#143fdacba) 에 의하여 $[\mathbf{T}\mathbf{T}{}^{*}]_{\beta } = [\mathbf{T}{}^{*}\mathbf{T}]_{\beta }$ 이다. ▲ 

    $\mathbf{T}$ 가 정규연산자임을 가정하면 비슷한 논리로 $[\mathbf{T}] _{\beta }$ 가 정규행렬임이 바로 나온다. ■ 
    
- 예시 

    $\mathbf{T}: \R ^{2} \to \R ^{2}$ 를 $0 < \theta < \pi$ 에 대하여 원점을 기준으로 반시계방향으로 $\theta$ 만큼 회전하는 선형변환이라 하자. 표준 순서기저에 대한 $\mathbf{T}$ 의 행렬표현은 다음과 같다. 

    $$ A = \begin{pmatrix} \cos \theta& -\sin \theta\\ \sin \theta& \cos \theta\\ \end{pmatrix} $$

    $AA {}^{*} = I = A {}^{*}A$ 가 성립하므로 $A$ 는 정규행렬이고 $\mathbf{T}$ 는 정규연산자이다.

- 위 예시의 $\mathbf{T}$ 는 고유벡터를 가지지 않는다. 이는 실내적공간에서 정규성(normality)이 고유벡터로 이루어진 정규직교기저의 존재성을 보장해주지는 않는다는 것을 말해준다.

    그러나 정리 6.16 에 의하여 $\mathbf{V}$ 가 복소내적공간이라면 정규성이 고유벡터로 이루어진 정규직교기저의 존재성을 보장해준다. 따라서 정규성과 고유벡터로 이루어진 정규직교의 존재성이 복소내적공간에서는 서로 동치이다. 

!!! tldr "정리 6.15"

    $\mathbf{F}$-내적공간 $\mathbf{V}$ 와 정규연산자 $\mathbf{T}$ 에 대하여 다음이 성립한다.

    1. $\forall x \in \mathbf{V} : \left\| \mathbf{T}(x) \right\| = \left\| \mathbf{T}{}^{*}(x) \right\|$

    2. 임의의 $c \in \mathbf{F}$ 에 대하여 $\mathbf{T}-c \mathbf{I}$ 는 정규연산자이다. 

    3. $\mathbf{T}(x) = \lambda x \implies \mathbf{T}{}^{*}(x) = \overline{\lambda }x$

    4. 고유벡터 $x_1, x_2$ 에 대응하는 $\mathbf{T}$ 의 고윳값 $\lambda _1, \lambda _2$ 에 대하여 $\lambda _1 \neq \lambda _2$ 이면 $x_1$ 과 $x_2$ 는 직교한다. 

- 3) 은 고윳값 $\lambda$ 에 대응하는 $\mathbf{T}$ 의 고유벡터 $x$ 가 고윳값 $\overline{\lambda }$ 에 대응하는 $\mathbf{T}{}^{*}$ 의 고유벡터임을 말해준다. 

- 증명 

    1:

    $$ \left\| \mathbf{T}(x) \right\| ^{2} = \big <\mathbf{T}(x), \mathbf{T}(x) \big > = \big <\mathbf{T}{}^{*}\mathbf{T}(x), x \big > = \big <\mathbf{T}\mathbf{T}{}^{*}(x), x \big > = \big <\mathbf{T}{}^{*}(x), \mathbf{T}{}^{*}(x) \big > = \left\| \mathbf{T}{}^{*}(x) \right\| ^{2} \tag*{▲} $$

    2:

    [정리 6.11](#a9f161221) 에 의하여 다음이 성립한다.

    $$ (\mathbf{T}-c \mathbf{I}) {}^{*} = \mathbf{T}{}^{*} -c \mathbf{I}{}^{*} $$

    [정리 2.10](../LinearTransformation/#273a736ad) 에 의하여 다음이 성립한다.

    $$ \begin{equation}\begin{split} (\mathbf{T} - c \mathbf{I})(\mathbf{T}-c \mathbf{I}){}^{*} &= (\mathbf{T} - c \mathbf{I})(\mathbf{T}{}^{*} -c \mathbf{I}{}^{*}) \\ &= (\mathbf{T} - c \mathbf{I})\mathbf{T}{}^{*} -c (\mathbf{T} - c \mathbf{I})\mathbf{I}{}^{*} \\ &= \mathbf{T}\mathbf{T}{}^{*} -c\mathbf{I}\mathbf{T}{}^{*} -c \mathbf{T}  \mathbf{I}{}^{*} +c^{2} \mathbf{I} \mathbf{I}{}^{*} \\ &= \mathbf{T}{}^{*}\mathbf{T} -c\mathbf{T}{}^{*}\mathbf{I} -c \mathbf{I}{}^{*}\mathbf{T} +c^{2} \mathbf{I}{}^{*}\mathbf{I} \\ &= (\mathbf{T}{}^{*}-c \mathbf{I}{}^{*})\mathbf{T} -c (\mathbf{T}{}^{*}-c \mathbf{I}{}^{*}) \mathbf{I}\\ &= (\mathbf{T}{}^{*}-c \mathbf{I}{}^{*})(\mathbf{T} -c \mathbf{I})\\ &= (\mathbf{T}-c \mathbf{I}){}^{*}(\mathbf{T} -c \mathbf{I})\\ \end{split}\end{equation} \tag*{} $$

    따라서 $\mathbf{T}-c \mathbf{I}$ 는 정규연산자이다. ▲ 

    3:

    어떤 $x \in \mathbf{V}$ 에 대하여 $\mathbf{T}(x) = \lambda x$ 라 하고 $\mathbf{U}=\mathbf{T}-\lambda \mathbf{I}$ 라 하면 $\mathbf{U}(x) = 0$ 이고 2) 에 의하여 $\mathbf{U}$ 는 정규연산자이다. 1) 에 의하여 다음이 성립한다. 

    $$ 0 = \| \mathbf{U}(x) \| = \| \mathbf{U}{}^{*}(x) \| = \| (\mathbf{T}{}^{*}-\overline{\lambda }\mathbf{I})(x) \| = \| \mathbf{T}{}^{*}(x) - \overline{\lambda }x \| $$

    즉, $\mathbf{T}{}^{*}(x) = \overline{\lambda }x$ 이다. ▲ 

    4:

    3) 에 의하여 다음이 성립한다. 

    $$ \lambda _1 \big <x_1,x_2 \big > = \big <\lambda _1x_1, x_2 \big > = \big <\mathbf{T}(x_1), x_2 \big > = \big <x_1, \mathbf{T}{}^{*}(x_2) \big > = \big <x_1, \overline{\lambda _2}x_2 \big > = \lambda _2 \big <x_1,x_2 \big > $$

    $\lambda _1 \neq \lambda_2$ 이므로 $\big <x_1,x_2 \big >= 0$ 이다. ■ 

## Fundamental Theorem of Algebra

!!! tldr "대수학의 기본 정리(fundamental theorem of algebra)"

    $\mathbf{P}(\mathbb{C})$ 의 다항식 $p(z) = a_nz ^{n} + \dots + a_1z + a_0$ 의 차수가 $n \geq 1$ 이면 $p(z)$ 는 해가 있다.

- 17세기부터 수학자들이 옳으리라고 추측했던 유명한 정리이다. 대수학의 기본 정리이지만 순수하게 대수적인 증명은 누구도 해내지 못했고, 훗날 위상수학과 해석학을 도입하여 증명을 할 수 있었다. 그래서 복소해석학에 의한 증명과 위상수학에 의한 증명이 존재한다.

- **대수학의 기본정리는 복소내적공간의 선형연산자의 특성다항식이 반드시 완전히 인수분해됨을 말해준다.**

- 증명

## Diagonalizable Orthonormal Basis in Complex Inner Product Space

!!! tldr "정리 6.16"

    유한차원 복소내적공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 가 정규연산자인 것과 $\mathbf{T}$ 의 고유벡터로 이루어진 $\mathbf{V}$ 의 정규직교기저가 존재한다는 것은 동치이다.

- 이 정리는 복소내적공간에서 정규성과 정규직교기저의 존재성이 동치임을 말해준다. 실내적공간에서는 정규직교기저의 존재성이 보장되면 정규성도 보장되지만, 정규성이 보장된다고 해서 정규직교기저의 존재성이 보장되지는 않는다.

- 증명

    $\mathbf{T}$ 를 복소내적공간의 정규연산자라 하자. 대수학의 기본정리에 의하여 $\mathbf{T}$ 의 특성다항식은 완전히 인수분해된다. 슈어의 정리에 의하여 $A = [\mathbf{T}]_{\beta }$ 를 상삼각행렬이 되게 하는 정규직교기저 $\beta = \{v_1, v_2, \dots, v_n\}$ 가 존재한다. $A$ 가 상삼각행렬이므로 $v_1$ 은 $\mathbf{T}$ 의 고유벡터이다. 따라서 $v_1, v_2, \dots, v _{k-1}$ 이 $\mathbf{T}$ 의 고유벡터이면 $v_k$ 도 $\mathbf{T}$ 의 고유벡터라는 것을 보이면 $v_1, v_2, \dots, v_n$ 이 $\mathbf{T}$ 의 고유벡터가 된다. 

    $j < k$ 에 대하여 고유벡터 $v_j$ 에 대응하는 $\mathbf{T}$ 의 고윳값을 $\lambda _j$ 라 하자. $A$ 가 상삼각행렬이므로 $\mathbf{T}(v_k)$ 는 다음과 같다. 

    $$ \mathbf{T}(v_k) = A _{1k}v_1 + A _{2k}v_2 + \dots + A _{kk}v_k $$

    [정리 6.5 따름정리](#a2290266a) 와 [정리 6.9](#01997fcc2) 정리 6.15-(3) 에 의하여 $\mathbf{T}{}^{*}(v_j) = \overline{\lambda}_jv_j$ 인 것에 의하여 다음이 성립한다. 

    $$ A _{jk} = \big <\mathbf{T}(v_k), v_j \big > = \big <v_k, \mathbf{T}{}^{*}(v_j) \big > = \big <v_k, \overline{\lambda }_j v_j \big > = \lambda _j \big <v_k,v_j \big > = 0 $$

    따라서 $\mathbf{T}(v_k) = A _{kk}v_k$ 이고 $\beta$ 는 $\mathbf{T}$ 의 고유벡터로 이루어진 정규직교기저임이 증명되었다. ▲ 

    선형연산자 $\mathbf{T}$ 의 고유벡터로 이루어진 정규직교기저 $\beta$ 가 존재하면 $[\mathbf{T}]_{\beta }$ 는 대각행렬이고 $[\mathbf{T}]{}^{*}_{\beta } = [\mathbf{T}{}^{*}]_{\beta }$ 도 대각행렬이다. 대각행렬은 가환적이다. 즉, 교환법칙이 성립한다. 따라서 $\mathbf{T}$ 와 $\mathbf{T} {}^{*}$ 도 가환적이다. 그러므로 $\mathbf{T}\mathbf{T}{}^{*} = \mathbf{T}{}^{*}\mathbf{T}$ 이다. ■ 

- 그러나 이 정리는 무한차원 복소내적공간에서는 성립하지 않는다. 

    - 예시 

## Hermitian, Hermitian matrix

!!! tldr "자기수반연산자(self-adjoint), 에르미트 연산자(Hermitian)"

    내적공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 가 $\mathbf{T}=\mathbf{T}{}^{*}$ 를 만족하면 자기수반연산자 또는 에르미트 연산자라 한다.

- 정규성이 실내적공간의 고유벡터로 이루어진 정규직교기저가 존재하기 위한 충분조건이 아님을 이미 알아보았다. 그러나 정규성을 더욱 강한 조건인 $\mathbf{T}=\mathbf{T}{}^{*}$ 로 바꾸면 충분조건이 된다. 이를 만족하는 연산자를 에르미트 연산자라 한다. 정리 6.17 을 보자.

!!! tldr "자기수반행렬(self-adjoint matrix), 에르미트 행렬(Hermitian matrix)"

    체 $\mathbf{F}\in \{\R , \mathbb{C}\}$ 에 대한 행렬 $A \in \mathbf{M}_{n \times n}(\mathbf{F})$ 가 $A = A {}^{*}$ 를 만족하면 자기수반행렬 또는 에르미트 행렬이라 한다.

- 실행렬에서는 자기수반행렬인 조건을 [대칭행렬](../VectorSpace/#96a169304) 로 간소화할 수 있다.

!!! tldr ""

    내적공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 가 자기수반연산자인 것과 $[\mathbf{T}]_{\beta }$ 가 자기수반행렬인 것은 동치이다.
    
- 증명

    $A = [\mathbf{T}]_{\beta }$ 가 자기수반행렬임을 가정하면 $A = A {}^{*}$ 이다. 그러면 정리 6.10 에 의하여 $[\mathbf{T}]_{\beta } = [\mathbf{T}{}^{*}]_{\beta }$ 이다. ▲ 

    $\mathbf{T}$ 가 자기수반연산자임을 가정하면 비슷한 논리로 그 역을 쉽게 증명할 수 있다. ■ 

## Diagonalizable Orthonormal Basis in Real Inner Product Space

!!! tldr "보조정리"

    유한차원 내적공간 $\mathbf{V}$ 의 자기수반연산자 $\mathbf{T}$ 에 대하여 다음이 성립한다. 

    1. $\mathbf{T}$ 의 모든 고윳값은 실수이다.

    2. $\mathbf{V}$ 가 실내적공간이면 $\mathbf{T}$ 의 특성다항식이 완전히 인수분해된다.

- 실내적공간의 선형연산자가 실수인 고윳값만 갖다는 것은 당연하다. 복소내적공간의 자기수반연산자의 고윳값은 반드시 실수이다. 이것을 1) 이 말해준다. 

- 대수학의 기본정리에 의하여 복소내적공간의 모든 선형연산자의 특성다항식이 완전히 인수분해됨은 당연하다. 실내적공간의 실자기수반연산자의 특성다항식도 완전히 인수분해된다. 이것을 2) 가 말해준다. 

- 증명

    1:

    $x \neq 0$ 인 $x \in \mathbf{V}$ 에 대하여 $\mathbf{T}(x) = \lambda x$ 를 가정하자. 자기수반연산자는 정규연산자이므로 정리 6.15-(3) 에 의하여 $\lambda x = \mathbf{T}(x) = \mathbf{T}{}^{*}(x) = \overline{\lambda }x$ 가 성립한다. $\lambda = \overline{\lambda }$ 이므로 $\lambda$ 는 실수이다. ▲ 

    2:

    $\dim (\mathbf{V}) = n$ 라 하고 $\mathbf{V}$ 의 정규직교기저 $\beta$ 에 대하여 $A = [\mathbf{T}]_{\beta }$ 로 두자. $\mathbf{T}$ 가 자기수반연산자이므로 $A$ 는 자기수반행렬이다. $\mathbb{C}^{n}$ 의 선형연산자 $\mathbf{U}$ 를 다음과 같이 정의하자. 

    $$ \forall x \in \mathbb{C}^{n} : \mathbf{U}(x) = Ax $$

    $\mathbb{C}$-벡터공간 $\mathbb{C}^{n}$ 의 표준순서 정규직교기저 $\gamma= \{e_1, e_2, \dots, e_n\}$ 에 대하여 다음이 성립한다. 

    $$ \mathbf{U}(e_j) = Ae_j = \sum_{i=1}^{n}A _{ij}e_j $$

    따라서 $[\mathbf{U}]_{\gamma } = A$ 이고, $\mathbf{U}$ 는 자기수반행렬이다. 
    
    1) 에 의하여 $\mathbf{U}$ 의 고윳값 $\lambda$ 들은 실수이다. 대수학의 기본정리에 의하여 $\mathbf{U}$ 의 특성다항식은 $t - \lambda$ 의 곱으로 완전히 인수분해된다. 모든 $\lambda$ 가 실수이므로 특성다항식이 $\R$ 에서 완전히 인수분해된다. 

    [특성다항식의 정의](../Diagonalization/#2f3482489)에 의하여 $\mathbf{U}$ 의 특성다항식은 $A$ 의 특성다항식이다. 다시 특성다항식의 정의에 의하여 $A$ 의 특성다항식은 $\mathbf{T}$ 의 특성다항식이다. 따라서 $\mathbf{T}$ 의 특성다항식은 완전히 인수분해된다. ■ 

!!! tldr "정리 6.17"

    유한차원 실내적공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 에 대하여 $\mathbf{T}$ 가 자기수반연산자인 것과 $\mathbf{T}$ 의 고유벡터로 이루어진 $\mathbf{V}$ 의 정규직교기저가 존재하는 것은 동치이다.

- **이 정리는 내적공간의 가장 중요한 결론들 중 하나이다.**

- 정규성이 실내적공간의 고유벡터로 이루어진 정규직교기저가 존재하기 위한 충분조건이 아니었다. 그러나 복소내적공간에서는 정규성만으로도 고유벡터로 이루어진 정규직교기저의 존재성이 보장된다.

    정규성을 더욱 강한 조건인 $\mathbf{T}=\mathbf{T}{}^{*}$ 로 바꾸면 실내적공간에서도 충분조건이 된다. 이것을 이 정리가 보장해준다. 

- 증명

    $\mathbf{T}$ 가 자기수반연산자임을 가정하자. 그러면 보조정리에 의하여 $\mathbf{T}$ 의 특성다항식이 완전히 인수분해된다. 그러면 슈어의 정리에 의하여 $A = [\mathbf{T}]_{\beta }$ 가 상삼각행렬이 되게 하는 $\mathbf{V}$ 의 정규직교기저 $\beta$ 가 존재한다. 한편, 다음이 성립한다. 

    $$ A {}^{*}= [\mathbf{T}]{}^{*}_{\beta } = [\mathbf{T}{}^{*}]_{\beta } = [\mathbf{T}]_{\beta } = A $$

    $A$ 와 $A {}^{*}$ 가 상삼각행렬이므로 $A$ 는 대각행렬이다. $\mathbf{T}$ 를 $\beta$ 가 대각화했으므로 $\beta$ 는 $\mathbf{T}$ 의 고유벡터로 이루어져있다. ▲ 

    이제 $\mathbf{T}$ 의 고유벡터로 이루어진 $\mathbf{V}$ 의 정규직교기저가 존재함을 가정하고 $\mathbf{T}$ 가 자기수반연산자임을 증명해보자. 

    ...

    ■ 