!!! info "ref"

    Stephen H. Friedberg, Linear Algebra, 4th Edition

# Complex Number

!!! tldr "허수(imaginary number)"

    허수는 $i = \sqrt[]{-1}$ 이다.

!!! tldr "복소수(Complex Number)"

    복소수는 실수 $a, b$ 와 허수 $i$ 에 대하여 $z = a+ bi$ 이다.

- 제곱하여 음수인 $-1$ 이 나오는 실수는 존재하지 않는다. 그러나 대수학을 전개하다보면 실수체만으로는 일반적인 이론을 전개하기가 쉽지 않다. 가령 $x ^{2}+1$ 의 해를 표현할 때 실수체에서 계수를 가져온 다항식의 해는 존재하지 않는다. 따라서 존재하지 않는 수인 허수 $i$ 를 도입하여 실수체를 복소수체로 확장한다.

- **복소수 $z = a+bi$ 의 실수부를 $\Re (z) = \mathcal{Re}(z) = \text{Re}(z) = a$ 로 표기하고, 허수부를 $\Im (z) = \mathcal{Im}(z) = \text{Im}(z) = b$ 로 표기한다.**

!!! tldr "복소수체(Complex number field)"

    복소수체 $\mathbb{C}$ 는 두 복소수 $z = a+bi, w = c+di$ 에 대하여 다음의 합과 곱이 정의된 실수체의 확장체이다.

    1. $z+w = (a+bi) + (c+di) = (a+c) + (b+d)i$

    2. $zw = (a+bi)(c+di) = (ac-bd) + (bc + ad)i$

- 복소수체가 체라는 것은 쉽게 증명할 수 있다. 가령 실수 $0$ 은 덧셈의 항등원이고 실수 $1$ 은 곱셈의 항등원이며 $a+bi$ 의 덧셈의 역원은 $(-a)+(-b)i$ 이다. 또한 $0$ 이 아닌 복소수 $a+bi$ 의 곱셈의 역원은 $\dfrac{a}{a ^{2}+b ^{2}}+\bigg (\dfrac{b}{a ^{2}+b ^{2}}\bigg )i$ 이다. 체의 나머지 공리도 쉽게 증명가능하다.

!!! tldr "켤레복소수(complex conjugate)"

    복소수 $a+bi$ 의 켤레복소수는 $\overline{a+bi} = a-bi$ 이다.

## Properties of Complex Number (1)

!!! tldr "켤레복소수의 성질 (1)"

    복소수 $z, w$ 에 대하여 다음이 성립한다. 

    1. $\overline{\overline{z}} = z$

    2. $\overline{z+w} = \overline{z}+\overline{w}$

    3. $\overline{zw} = \overline{z}\cdot \overline{w}$

    4. $w \neq 0 \implies \overline{\dfrac{z}{w}}= \dfrac{\overline{z}}{\overline{w}}$

    5. $z \in \R \implies z = \overline{z}$

- 증명

    복소수의 정의와 복소수의 합과 곱의 정의, 그리고 켤레복소수의 정의에 의하여 다 매우 쉽게 증명 가능하다.

## Absolute Value

!!! tldr "복소수의 절댓값(absolute value) 또는 법(modulus)"

    복소수 $z = a + bi$ 의 절댓값은 실수 $|z| = \sqrt[]{a ^{2}+b ^{2}}$ 이다.

- 임의의 복소수 $z = a+bi$ 에 대하여 $z \overline{z}=(a+bi)(a-bi)=a ^{2}+b ^{2} \geq 0$ 이므로 $z \overline{z}$ 는 음이 아닌 실수이다. 

!!! tldr "복소수의 절댓값의 성질"

    복소수 $z$ 에 대하여 다음이 성립한다.

    1. $z \overline{z} = |z| ^{2}$

    2. $|z| = |\overline{z}|$

- 증명

    복소수의 정의와 절댓값의 정의에 의하여 쉽게 증명된다.

## Properties of Complex Number (2)

!!! tldr "켤레복소수의 성질 (2)"

    두 복소수 $z, w$ 에 대하여 다음이 성립한다.

    1. $|zw| = |z||w|$

    2. $w \neq 0 \implies \bigg |\dfrac{z}{w} \bigg | = \dfrac{|z|}{|w|}$

    3. $|z+w| \leq |z| + |w|$

    4. $|z| - |w| \leq |z + w|$

- 증명

    1:

    $$ |zw| ^{2} = zw \overline{zw} = zw \overline{z}\cdot \overline{w} = z \overline{z}w \overline{w} = |z|^{2}|w|^{2} \tag*{■}$$

    2:

    $$ |z| = \bigg |  \frac{z}{w}w\bigg | = \bigg |\frac{z}{w} \bigg ||w| = \bigg |\frac{1}{w}z \bigg ||w| = \bigg |\frac{1}{w} \bigg ||z||w| = \frac{1}{|w|}|z||w| $$

    $$ \iff \bigg |\frac{z}{w} \bigg ||w| = \frac{1}{|w|}|z||w| \iff \bigg |\frac{z}{w} \bigg | = \frac{|z|}{|w|} \tag*{■}$$

    3:

    복소수 $x = a + bi$ 에 대하여 다음이 성립한다. 

    $$ x + \overline{x} = (a+bi) +(a-bi) = 2a \leq 2 \sqrt[]{a ^{2} + b ^{2}} = 2|x| $$

    즉, $x + \overline{x} \leq 2|x|$ 가 성립한다. 이 사실과 켤레복소수의 성질 (1) 과 이미 증명한 1) 에 의하여 적당한 복소수 $w, z$ 에 대하여 $x = w \overline{z}$ 를 가정하면 다음이 성립한다. 

    $$ w \overline{z} + \overline{w}z \leq 2|w \overline{z}| = 2|w||\overline{z}| = 2|z||w| $$

    즉, $w \overline{z}+ \overline{w}z \leq 2|z||w|$ 이다. 이 사실과 복소수의 절댓값의 성질과 켤레복소수의 성질 (1) 에 의하여 다음이 성립한다.

    $$ \begin{equation}\begin{split} |z+w| ^{2} &= (z+w)\overline{(z+w)}=(z+w)(\overline{z}+\overline{w}) = z \overline{z} + w \overline{z} + z \overline{w} + w \overline{w}\\ &\leq |z|^{2} + 2|z||w| + |w| ^{2} = (|z| + |w|) ^{2}\\ \end{split}\end{equation} \tag*{} $$

    $$ \iff  |z+w|^{2} \leq (|z| + |w|) ^{2} \iff |z+w| \leq |z|+|w| \tag*{■} $$

    4:

    이미 증명한 1), 3) 에 의하여 다음이 성립한다. 

    $$ |z| = |z+w-w| \leq |z+w| + |-w| = |z+w| + |w| $$

    $$ \iff |z|-|w| \leq |z+w| \tag*{■} $$

## Complex plane

!!! tldr "복소평면(Complex plane)"

    복소평면은 복소수체 $\mathbb{C}$ 를 $x$축을 실수부, $y$축을 허수부로하는 좌표평면 $\R ^{2}$ 에 대응시킨 좌표평면이다.

- 정의에 의하여 $x$축을 실수축(real axis), $y$축을 허수축(imaginary axis)으로 부른다.

- 복소수체 $\mathbb{C}$ 와 벡터공간 $\R ^{2}$ 는 동형사상 $f: \mathbb{C}\to \R ^{2}, x+yi \mapsto (x, y)$ 이 존재함으로 인하여 모든 구조와 성질이 그대로 보존되고, 복소수를 좌표평면의 좌표로 일대일 대응시킬 수 있다.

- 복소평면에서 복소수 $z = x+iy$ 는 다음과 같이 벡터이다. 

    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Complex_conjugate_picture.svg/330px-Complex_conjugate_picture.svg.png)

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

## Conjugate Transpose

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

    $\mathbf{F} \in \{\R, \mathbb{C}\}$ 인 $\mathbf{F}$-벡터공간 $\mathbf{V}$ 와 $\mathbf{W}$ 와 벡터 $x, y \in \mathbf{V}$ 와 스칼라 $a, b \in \mathbf{F}$ 대하여 다음을 만족하는 함수 $f: \mathbf{V}\to \mathbf{W}$ 를 antilinear 또는 켤레 선형이라고 한다.

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

## Norm of Euclidean Space

!!! tldr "유클리드 공간(Euclidean vector space)"

    n차원 유클리드 공간 $\R ^{n}$ 은 표준내적이 부여된 유한차원 내적공간이다.

- 유클리드 공간은 유클리드가 연구했던 평면과 공간을 일반화한 것이다. 일반화란 유클리드가 생각했던 거리(distance)와 길이(norm)와 좌표계를 도입하여 임의 차원의 공간으로 확장한 것이다.

- $\R$-벡터공간 $\R ^{n}$ 에 표준내적이 부여됨에 따라 실수 힐베르트 공간을 이루고 내적 공간, 바나흐 공간, 노름 공간, 벡터 공간, 완비 거리 공간, 위상 공간을 이룬다.

- 유클리드 공간을 아핀 공간을 기반으로 정의하는 것이 있는데 나중에 알아봐야 할듯.

- 예시 

    유클리드 공간에는 아래에서 볼 수 있듯이 유클리드 노름이 가장 자주 사용되며 우리의 직관 속에 녹아들어있다. 그러나 전혀 새로운 노름을 정의할 수도 있다. 가령 4차원 유클리드 공간 $\R ^{4}$ 과 벡터 $x = (x_1, x_2, x_3, x_4) \in \R ^{4}$ 에 대하여 다음과 같은 노름을 정의할 수 있다.

    $$ \|x\| = 2|x_1| + \sqrt[]{3|x_2| ^{2} + \max (|x_3|, 2|x_4|) ^{2}}
    $$

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

!!! tldr "체비셰프 거리(Chebyshev distance), 최대 거리(maximum distance), $L _{\infty }$ 거리($L _{\infty }$ 거리)"

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

!!! tldr "정규직교집합(orthonormal)"

    내적공간의 부분집합이 단위벡터로 구성된 직교집합이면 정규직교집합이라 한다.

- 집합 $S = \{v_1, v_2, \dots\}$ 가 정규직교집합인 것과 $\big <v_i,v_j \big > = \delta _{ij}$ 인 것은 동치이다. 

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

# Gram–Schmidt Process

!!! tldr "정규직교기저(orthonormal basis)"

    내적공간의 부분집합이 정규직교집합이고 순서기저이면 정규직교기저라 한다.

- 표준내적이 부여된 $\mathbb{C}^{n}$ 와 $\R ^{n}$ 의 표준순서기저는 벡터들이 정규직교집합을 이루기 때문에 특별한 성질을 가진다. 벡터공간을 구성하는 기본 조각이 기저라면, 내적공간을 구성하는 기본 조각은 정규직교기저이다.

- 예시 

    $\mathbf{F}^{n}$ 의 표준 순서기저는 $\mathbf{F} ^{n}$ 의 정규직교기저이다.

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

    내적공간 $\mathbf{V}$ 의 일차독립인 부분집합 $S = \{w_1, w_2, \dots, w_n\}$ 에 대하여 집합 $S' = \{v_1, v_2, \dots, v_n\}$ 을 다음과 같이 정의하면 $S'$ 는 $\text{span} (S') = \text{span} (S)$ 이고 영이 아닌 벡터로 이루어진 직교 집합이다.

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

!!! tldr "르장드르 다항식(Legendre polynomial)"

    $\mathbf{P}_{}(\R)$ 의 표준순서기저 $\{1,x,x ^{2}, \dots\}$ 에 그람-슈미트 직교화를 적용하여 얻은 직교기저 $\{v_1, v_2, \dots\}$ 에 대한 다항식 $\dfrac{v_k}{v_k(1)}$ 를 $k$차 르장드르 다항식이라 한다.

- 처음 세 르장드르 다항식은 $1, x, \frac{1}{2}(3x ^{2}-1)$ 이다.

!!! tldr "정리 6.5"

    점공간이 아닌 유한차원 내적공간 $\mathbf{V}$ 에 정규직교기저 $\beta$ 가 존재한다.

    $\beta = \{v_1, v_2, \dots, v_n\}$ 와 $x \in \mathbf{V}$ 에 대하여 $\displaystyle x = \sum_{i=1}^{n}\big <x,v_i \big >v_i$ 이다.

- 이 정리는 주어진 벡터를 정규직교기저의 일차결합으로 나타내는 방법을 말해준다.

- 증명

    [벡터공간에는 기저가 존재한다.](../VectorSpace/#2b881d6d6) $\mathbf{V}$ 의 순서기저 $\beta _0$ 에 대하여 그람-슈미트 직교화로 직교집합 $\beta '$ 를 얻을 수 있고, $\text{span} (B') = \text{span} (\beta _0) = \mathbf{V}$ 이다. $\beta '$ 를 정규화하면 정규직교집합 $\beta$ 을 얻는다. 정리 6.3 따름정리 2 에 의하여 $\beta$ 는 일차독립이므로 정규직교기저이다. ▲ 
    
    정규직교기저 $\beta$ 의 존재성 증명이 끝났으니 나머지 증명은 정리 6.3 따름정리 1 에서 바로 나온다. ■ 

!!! tldr "정리 6.5 따름정리"

    정규직교기저 $\beta = \{v_1, v_2, \dots, v_n\}$ 를 갖는 유한차원 벡터공간 $\mathbf{V}$ 와 선형연산자 $\mathbf{T}$ 에 대하여 $A = [\mathbf{T}]_{\beta }$ 로 두면 임의의 $i, j$ 에 대하여 $A _{ij} = \big <\mathbf{T}(v_j), v_i \big >$ 이다.

- 이 정리를 사용하면 선형연산자의 정규직교기저에 대한 행렬표현 성분을 쉽게 구할 수 있다.

- 증명

    정리 6.5 에 의해 $\mathbf{T}(v_j) = \displaystyle \sum_{i=1}^{n}\big <\mathbf{T}(v_j), v_i \big >v_i$ 이다. 즉, $A _{ij} = \big <\mathbf{T}(v_j), v_i \big >$ 이다.

# Orthogonal Complements
