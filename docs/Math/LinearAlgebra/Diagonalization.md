!!! info "ref"

    Stephen H. Friedberg, Linear Algebra, 4th Edition

# Diagonalizable

!!! tldr "선형연산자의 대각화가능(diagonalizable) 의 정의"

    유한차원 벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 에 대하여 $[\mathbf{T} ]_{\beta }$ 가 대각행렬이 되도록 하는 $\mathbf{V}$ 의 순서기저 $\beta$ 가 존재하면 $\mathbf{T}$ 를 대각화가능하다고 한다.

- 유한차원 벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 를 대각화가능하게 만드는, 즉 $[\mathbf{T} ]_{\beta}$ 가 대각행렬이 되게 하는 순서기저 $\beta = \{v_1, v_2, \dots, v_n \}$ 를 어떻게 찾을 수 있을까.

    $D = [\mathbf{T} ] _{\beta }$ 가 대각행렬이면 [선형변환의 행렬표현](../LinearTransformation/#9a08985c1) 에 의하여 $v_j \in \beta$ 와 $\lambda _i = D _{jj}$ 에 대하여 $\mathbf{T} (v_j) = \displaystyle \sum_{i=1}^{n}D _{ij}v_j = \lambda _jv_j$ 이다. 

    역으로 스칼라 $\lambda _1, \lambda _2, \dots, \lambda _n$ 에 대하여 $\beta$ 가 $\mathbf{T} (v_j) = \lambda _jv_j$ 를 만족하면 다음이 성립한다. 

    $$ [\mathbf{T} ]_{\beta } = \begin{pmatrix} \lambda _{1}&0&\dots&0\\ 0&\lambda _2&\dots&0\\ \vdots& \vdots& \ddots& \vdots \\ 0&0&\dots&\lambda _n\\ \end{pmatrix} $$

    선형연산자 $\mathbf{T}$ 가 대각화가능이면 기저 $\beta$ 의 각 벡터 $v$ 는 적절한 스칼라 $\lambda$ 에 대하여 $\mathbf{T} (v) = \lambda v$ 를 만족한다. $v$ 는 기저의 원소이므로 영벡터가 아니다. 이를 기반으로 고유벡터의 정의를 내릴 수 있다.

!!! tldr "정사각행렬의 대각화가능(diagonalizable) 의 정의"

    선형연산자 $\mathbf{L}_{A}$ 가 대각화가능이면 정사각행렬 $A$ 를 대각화가능이라고 한다.

# Eigenvector

!!! tldr "선형연산자의 고유벡터(eigenvector) 와 고윳값(eigenvalue) 의 정의"

    벡터공간 $\mathbf{V}$  의 선형연산자 $\mathbf{T}$ 에 대하여 다음과 같이 정의한다.
    
    - 영벡터가 아닌 벡터 $v \in \mathbf{V}$ 와 스칼라 $\lambda$ 에 대하여 $\mathbf{T} (v) = \lambda v$ 이면 벡터 $v$ 를 $\mathbf{T}$ 의 고유벡터라 한다.

    - 스칼라 $\lambda$ 를 고유벡터 $v$ 에 대응하는 고윳값이라 한다.

- 고유벡터는 특성벡터(characteristic vector, proper vector), 고윳값은 특성값(characteristic value, proper value) 라고도 부른다.

!!! tldr "정사각행렬의 고유벡터(eigenvector) 와 고윳값(eigenvalue) 의 정의"

    행렬 $A \in \mathbf{M}_{n \times n}(\mathbf{F} )$ 에 대하여 다음과 같이 정의한다. 

    - $\mathbf{L}_{A}$ 의 고유벡터, 즉 스칼라 $\lambda$ 에 대하여 $Av = \lambda v$ 를 만족하는 영벡터가 아닌 벡터 $v \in \mathbf{F} ^{n}$ 을 $A$ 의 고유벡터라 한다.

    - 스칼라 $\lambda$ 를 고유벡터 $v$ 에 대응하는 행렬 $A$ 의 고윳값이라 한다.

## Properties of eigenvector

!!! tldr "정리 5.1"

    유한차원 벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 가 대각화가능인 것과 $\mathbf{T}$ 의 고유벡터로 이루어진 $\mathbf{V}$ 의 순서기저 $\beta$ 가 존재하는 것은 동치이다.

    즉, $\beta = \{v_1, v_2, \dots, v_n \}$ 가 $\mathbf{T}$ 의 고유벡터로 이루어진 $\mathbf{V}$ 의 순서기저이면 $D = [\mathbf{T} ] _{\beta}$ 는 대각행렬이며 $D _{jj}$ 는 $v_j$ 에 대응하는 고윳값이다.

!!! tldr "정리 5.1 따름정리"

    행렬 $A \in \mathbf{M}_{n \times n}(\mathbf{F} )$ 가 대각화가능인 것과 $A$ 의 고유벡터로 이루어진 $\mathbf{F} ^{n}$ 의 순서기저가 존재하는 것은 동치이다.

    $\{v_1, v_2, \dots, v_n\}$ 를 $A$ 의 고유벡터로 이루어진 $\mathbf{F} ^{n}$ 의 순서기저라고 하면 $j$ 열이 벡터 $v_j$ 인 $n \times n$ 행렬 $Q$ 에 대하여 $D = Q ^{-1}AQ$ 는 대각행렬이며 $D _{jj}$ 는 $v_j$ 에 대응하는 $A$ 의 교윳값이다.

- 이 정리는 행렬 $A$ 가 대각화가능인 것과 대각행렬과 닮음인 것이 동치임을 말해준다. 

- 선형연산자를 대각화한 행렬이 $D = [\mathbf{T} ]_{\beta }$ 인데, 정사각행렬을 대각화한 행렬이 $D = Q ^{-1}AQ$ 인 이유는 [정리 2.23 따름정리](../LinearTransformation/#b7acffb79) 에서 바로 나온다.

- 예시 

    행렬 $A = \begin{pmatrix} 1&3\\ 4&2\\ \end{pmatrix}$ 와 벡터 $v_1 = \begin{pmatrix} 1\\ -1\\ \end{pmatrix}, v_2 = \begin{pmatrix} 3\\ 4\\ \end{pmatrix}$ 에 대하여 다음이 성립한다. 

    $$ \mathbf{L}_{A}(v_1) = \begin{pmatrix} -2\\ 2\\ \end{pmatrix} = -2v_1 $$

    $$ \mathbf{L}_{A}(v_2) = \begin{pmatrix} 15\\ 20\\ \end{pmatrix} = 5v_2 $$

    그러므로 $v_1, v_2$ 는 $\mathbf{L}_{A}$ 와 $A$ 의 고유벡터이다. $v_1, v_2$ 에 대응하는 고윳값은 $\lambda _1 = -2, \lambda _2 = 5$ 이다.

    이때 $\beta = \{v_1, v_2\}$ 는 $A$ 와 $\mathbf{L}_{A}$ 의 고유벡터로 이루어진 $\R ^{2}$ 의 순서기저이다. 따라서 $A$ 와 $\mathbf{L}_{A}$ 는 대각화가능이다. 

    또한 정리 5.1 과 따름정리에 의하여 $Q = \begin{pmatrix} 1&3\\ -1&4\\ \end{pmatrix}$ 에 대하여 $Q ^{-1}AQ = [\mathbf{L}_{A}]_{\beta } = \begin{pmatrix} -2&0\\ 0&5\\ \end{pmatrix}$ 이다.

!!! tldr ""

    고유벡터와 고윳값을 가지지 않는 선형연산자나 행렬이 존재한다.

- 증명

    $\R ^{2}$ 의 벡터를 $\dfrac{\pi }{2}$ 만큼 회전시키는 선형연산자 $\mathbf{T}$ 와 영이 아닌 벡터 $v \in \R ^{2}$ 에 대하여 $\mathbf{T} (v)$ 는 $0$ 과 $v$ 를 지나는 직선 위에 있지 않다. 

    이는 $\mathbf{T} (v)$ 를 $v$ 의 스칼라배로 표현할 수 없다는 것이다. 따라서 $\mathbf{T}$ 는 고유벡터와 고윳값을 가지지 않으며, 대각화 불가능하다.

## Characteristic polynomial

!!! tldr "정리 5.2"

    행렬 $A \in \mathbf{M}_{n \times n}$ 에 대하여 스칼라 $\lambda$ 가 $A$ 의 고윳값인 것과 $\det(A - \lambda I_n) = 0$ 인 것은 동치이다.

- 이 정리는 고윳값을 계산하는 방법을 제시한다.

- 이 정리는 특성다항식의 근을 찾으면 유한차원 벡터공간의 행렬 또는 선형연산자의 고윳값을 모두 밝힐 수 있음을 말해준다.

- 증명

    스칼라 $\lambda$ 가 $A$ 의 고윳값임을 가정하자.  스칼라 $\lambda$ 가 $A$ 의 고윳값인 것과 $Av = \lambda v$ 인 영이 아닌 벡터 $v \in \mathbf{F} ^{n}$ 가 존재하는 것은 동치이다. 그러므로 $(A - \lambda I_n) (v) = 0$ 이다.

    $A - \lambda I_n$ 이 가역이면 $v = 0$ 이므로 모순이다. 즉, $A - \lambda I_n$ 는 가역이 아니다. [정리 4.7 따름정리](../Determinants/#b40051741) 에 의하여 $\det(A - \lambda I_n) = 0$ 이다.

!!! tldr "정사각행렬의 특성다항식(Characteristic polynomial) 의 정의"

    행렬 $A \in \mathbf{M}_{n \times n}(\mathbf{F} )$ 에 대하여 $A$ 의 특성다항식은 다항식 $f(t) = \det(A - tI_n)$ 이다.

- 정리 5.2 는 행렬의 고윳값이 특성다항식의 근임을 말해준다. 이는 특성다항식의 계산을 통하여 행렬 또는 선형연산자의 고윳값을 얻을 수 있음을 뜻한다. 

- 이때 $A - tI_n \not\in \mathbf{M}_{n \times n}(\mathbf{F} )$ 이다. 행렬 $A - tI_n$ 는 $\mathbf{F}$ 를 계수로 가지는 $t$ 에 대한 유리식으로 이루어진 체 $\mathbf{F} (t)$ 에 속해있다. 즉, $A - tI_n \in \mathbf{M}_{n \times n}(\mathbf{F}(t) )$ 이다.

    행렬식에 대한 정리들을 $\mathbf{F} (t)$ 에서도 사용할 수 있다.

- 예시 

    행렬 $A = \begin{pmatrix} 1&1\\ 4&1\\ \end{pmatrix} \in \mathbf{M}_{2 \times 2}(\R )$ 의 고윳값을 구하기 위하여 다음 특성다항식을 풀어보자. 

    $$ \det(A - tI_2) = \det \begin{pmatrix} 1-t&1\\ 4&1-t\\ \end{pmatrix} = t ^{2} - 2t - 3 = (t - 3)(t + 1) $$

    정리 5.2 에 의하여 $A$ 의 고윳값은 $3, -1$ 뿐이다.

!!! tldr "선형연산자의 행렬식(determinant) 의 정의"

    유한차원 벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 와 $\mathbf{V}$ 의 순서기저 $\beta$ 에 대하여 $\mathbf{T}$ 의 행렬식을 다음과 같이 정의한다.

    $$ \det(\mathbf{T} ) := \det([\mathbf{T} ]_{\beta }) $$

!!! tldr "선형연산자의 특성다항식(Characteristic polynomial) 의 정의"

    유한차원 벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 와 $\mathbf{V}$ 의 순서기저 $\beta$ 에 대하여 $\mathbf{T}$ 의 특성다항식을 다음과 같이 정의한다.

    $$ f(t) = \det([\mathbf{T} ]_{\beta } - tI_n) $$

!!! tldr "문제 5.1-13"

    닮은 행렬은 같은 특성다항식을 가진다.

    유한차원 벡터공간 $\mathbf{V}$ 의 선형연산자의 행렬식과 특성다항식의 정의는 $\mathbf{V}$ 의 기저의 선택에 관계없다.

- 이 정리는 선형연산자의 행렬식과 특성다항식의 정의의 기저로 어떤 기저를 선택하든 관계없다는 것을 말해준다.

- 증명

    $A, B$ 가 닮음이면 가역행렬 $Q$ 에 대하여 $B = Q ^{-1}AQ$ 이다. 그러므로 다음이 성립한다.

    $$ Q ^{-1}(A-tI_n)Q = Q ^{-1}AQ - t Q ^{-1}I_nQ = B - tI_n $$

    그러므로 $A-tI_n$ 과 $B-tI_n$ 은 닮음이다. 따라서 [문제 4.3-15](../Determinants/#f21707098) 에 의하여 다음이 성립한다.
    
    $$ \det(A -tI_n) = \det(B-tI_n) $$

    한편 [정리 2.23](../LinearTransformation/#acf61b9cb) 은 선형연산자의 서로 다른 순서기저에 의한 행렬표현이 서로 닮음임을 말해준다. 그러므로 모든 증명이 끝났다. ■ 

- 예시 

    벡터공간 $\mathbf{P}_{2}(\R)$ 의 선형연산자 $\mathbf{T} (f(x)) = f(x) + (x+1) f'(x)$ 의 고윳값을 $\mathbf{P}_{2}(\R)$ 의 표준순서기저 $\beta$ 로 구해보자. 다음이 성립한다.

    $$ \mathbf{T} (1) = 1 + (x + 1) \cdot 0 = 1 $$

    $$ \mathbf{T} (x) = x + (x + 1) \cdot 1 = 1 + 2x $$

    $$ \mathbf{T} (x ^{2}) = x ^{2} + (x + 1) \cdot 2x = 0 + 2x + 3x ^{2}$$

    $$ [\mathbf{T} ]_{\beta } = \begin{pmatrix} 1&1&0\\ 0&2&2\\ 0&0&3\\ \end{pmatrix} $$

    선형연산자 $\mathbf{T}$ 의 특성다항식의 정의와 [문제 4.2-23](../Determinants/#aad94de43) 에 의하여 다음이 성립한다.

    $$ \begin{equation}\begin{split} \det([\mathbf{T} ]_{\beta } - tI_3) &= \det \begin{pmatrix} 1-t&1&0\\ 0&2-t&2\\ 0&0&3-t\\ \end{pmatrix} \\ &= (1-t)(2-t)(3-t)\\ &= -(t-1)(2-t)(3-t)\\ \end{split}\end{equation} \tag*{} $$

    정리 5.2 에 의하여 선형연산자 $\mathbf{T}$ 또는 행렬 $[\mathbf{T} ]_{\beta }$ 의 고윳값은 $1,2,3$ 뿐이다.

!!! tldr "정리 5.3"

    행렬 $A \in \mathbf{M}_{n \times n}(\mathbf{F} )$ 에 대하여 다음이 성립한다. 

    1. $A$ 의 특성다항식은 $n$차 다항식이고, 최고차항의 계수는 $(-1) ^{n}$ 이다.

    2. $A$ 에는 최대 $n$ 개의 서로 다른 고윳값이 있다.

- 증명

    $n = 1$ 을 가정하자. $A = (A _{11}) \in \mathbf{M}_{1 \times 1}(\mathbf{F} )$ 의 특성다항식은 다음과 같다.

    $$ \det(A - tI_1) = \det((A _{11} - t)) = A _{11} - t $$

    $n = 1$ 일 때 $A$ 의 특성다항식은 $1$차 다항식이고, 최고차항의 계수가 $(-1) ^{1} = -1$ 이다. 또한 정리 5.2 에 의하여 $1$차 다항식이 최대 $1$ 개의 서로 다른 근을 가지기 때문에 $A$ 는 최대 $1$ 개의 서로 다른 고윳값을 가진다. ▲ 

    $n - 1$ 에 대하여 정리가 성립함을 가정하고 $n$ 에 대하여 정리가 성립함을 보이면 증명이 끝난다. $A \in \mathbf{M}_{n \times n}(\mathbf{F} )$ 에 대하여 $B = A - tI_n$ 로 두면 $A$ 의 특성다항식은 다음과 같다. 

    $$ \begin{equation}\begin{split} \det(B) &= (-1) ^{1 + 1} (A _{11} - t) \cdot \det(\tilde{B}_{11}) + \sum_{j=2}^{n}(-1) ^{1+j} A _{1j} \cdot \det(\tilde{B}_{1j}) \\ &= (-1) ^{1+1}(-t)\det(\tilde{B}_{11}) + (-1) ^{1+1}(A _{11})\det(\tilde{B}_{11}) + \sum_{j=2}^{n}(-1) ^{1+j} A _{1j} \cdot \det(\tilde{B}_{1j}) \\ &= -t \cdot \det(\tilde{B}_{11}) + \sum_{j=1}^{n}(-1) ^{1+j} A _{1j} \cdot \det(\tilde{B}_{1j}) \\ \end{split}\end{equation} \tag*{} $$ 

    $\det(\tilde{B}_{1j})$ 는 $(n-1) \times (n-1)$ 행렬의 특성다항식이다. $n - 1$ 에 대하여 정리가 성립하므로 $\det(\tilde{B}_{1j})$ 는 $n-1$ 차 다항식이고, 최고차항의 계수가 $(-1) ^{n-1}$ 이다. $\displaystyle \sum_{j=1}^{n}(-1) ^{1+j}A _{1j}$ 은 스칼라이므로 $-t \cdot \det(\tilde{B}_{11})$ 에 의하여 $\det(B)$ 는 최고차항의 계수가 $(-1) ^{n}$ 인 $n$ 차 다항식이 된다. 또한 정리 5.2 에 의하여 $n$차 다항식이 최대 $n$ 개의 서로 다른 근을 가지기 때문에 $A$ 는 최대 $n$ 개의 서로 다른 고윳값을 가진다. ■ 

!!! tldr "정리 5.4"

    행렬 $A \in \mathbf{M}_{n \times n}(\mathbf{F} )$ 와 고윳값 $\lambda$ 에 대하여 벡터 $v \in \mathbf{F} ^{n}$ 가 $\lambda$ 에 대응하는 $A$ 의 고유벡터인 것과 $v \neq 0 \land (A-\lambda I)v = 0$ 인 것은 동치이다.

- 이 정리는 고윳값에 대응하는 고유벡터를 찾는 방법을 알려준다.

- 증명

    $v$ 가 고윳값 $\lambda$ 에 대응하는 $A$ 의 고유벡터이면 고유벡터의 정의에 의하여 $Av = \lambda v \implies (A - \lambda I)v = 0$ 와 $v \neq 0$ 이 성립한다. 

    역으로 영벡터가 아닌 벡터 $v$ 에 대하여 $(A - \lambda I)v = 0 \implies Av = \lambda v$ 가 성립하면 고유벡터의 정의에 의하여 $v$ 는 고윳값 $\lambda$ 에 대응하는 고유벡터이다.

- 예시 

    행렬 $A = \begin{pmatrix} 1&1\\ 4&1\\ \end{pmatrix}$ 의 모든 고유벡터를 구해보자. $A$ 의 고윳값은 $\lambda _1 = 3, \lambda _2 = -1$ 이다. 
    
    $B_1 = A - \lambda _1I = \begin{pmatrix} -2&1\\ 4&-2\\ \end{pmatrix}$ 를 정의하면 $\lambda _1$ 에 대응하는 고유벡터 $x = \begin{pmatrix} x_1\\ x_2\\ \end{pmatrix} \in \R ^{2}$ 는 $x \neq 0 \land x \in \mathbf{N} (\mathbf{L} _{B_1})$ 을 만족한다. 즉, 다음이 성립해야 한다. 

    $$ \begin{pmatrix} -2&1\\ 4&-2\\ \end{pmatrix}\begin{pmatrix} x_1\\ x_2\\ \end{pmatrix}= \begin{pmatrix} -2x_1+x_2\\ 4x_1-2x_2\\ \end{pmatrix}= \begin{pmatrix} 0\\ 0\\ \end{pmatrix} $$

    이 방정식의 해집합은 $t \in \R$ 에 대하여 $t \begin{pmatrix} 1\\ 2\\ \end{pmatrix}$ 이므로 $t \neq 0$ 에 대하여 $x = t \begin{pmatrix} 1\\ 2\\ \end{pmatrix}$ 는 $\lambda _1$ 에 대응하는 고유벡터이다. ▲ 

    $B_2 = A - \lambda _2I = \begin{pmatrix} 2&1\\ 4&2\\ \end{pmatrix}$ 를 정의하면 $\lambda _2$ 에 대응하는 고유벡터 $x = \begin{pmatrix} x_1\\ x_2\\ \end{pmatrix} \in \R ^{2}$ 는 $x \neq 0 \land x \in \mathbf{N} (\mathbf{L} _{B_2})$ 을 만족한다. 즉, 다음이 성립해야 한다. 

    $$ \begin{pmatrix} 2&1\\ 4&2\\ \end{pmatrix}\begin{pmatrix} x_1\\ x_2\\ \end{pmatrix}= \begin{pmatrix} 2x_1+x_2\\ 4x_1+2x_2\\ \end{pmatrix}= \begin{pmatrix} 0\\ 0\\ \end{pmatrix} $$

    이 방정식의 해집합은 $t \in \R$ 에 대하여 $t \begin{pmatrix} 1\\ -2\\ \end{pmatrix}$ 이므로 $t \neq 0$ 에 대하여 $x = t \begin{pmatrix} 1\\ -2\\ \end{pmatrix}$ 는 $\lambda _2$ 에 대응하는 고유벡터이다. ▲ 

    집합 $\bigg \{\begin{pmatrix} 1\\ 2\\ \end{pmatrix}, \begin{pmatrix} 1\\ -2\\ \end{pmatrix}\bigg \}$ 은 일차독립이고 기수가 $2$ 이므로 [정리 1.10 따름정리 2](../VectorSpace/#cd7879a47) 에 의하여 기저이다. 이 기저는 $A$ 의 고유벡터로 이루어진 기저이므로 $A$ 와 $\mathbf{L}_{A}$ 는 대각화가능하다.

