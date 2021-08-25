!!! info "ref"

    Stephen H. Friedberg, Linear Algebra, 4th Edition

# Diagonalizable

!!! tldr "선형연산자의 대각화가능(diagonalizable)"

    유한차원 벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 에 대하여 $[\mathbf{T} ]_{\beta }$ 가 대각행렬이 되도록 하는 $\mathbf{V}$ 의 순서기저 $\beta$ 가 존재하면 $\mathbf{T}$ 를 대각화가능하다고 한다.

- 유한차원 벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 를 대각화가능하게 만드는, 즉 $[\mathbf{T} ]_{\beta}$ 가 대각행렬이 되게 하는 순서기저 $\beta = \{v_1, v_2, \dots, v_n \}$ 를 찾아보자. $D = [\mathbf{T} ] _{\beta }$ 가 대각행렬이면 [선형변환의 행렬표현](../LinearTransformation/#c16bc5e5b) 에 의하여 $v_j \in \beta$ 와 $\lambda _j = D _{jj}$ 에 대하여 $\mathbf{T} (v_j) = \displaystyle \sum_{i=1}^{n}D _{ij}v_j = \lambda _jv_j$ 이다. 

    역으로 스칼라 $\lambda _1, \lambda _2, \dots, \lambda _n$ 에 대하여 $\beta$ 가 $\mathbf{T} (v_j) = \lambda _jv_j$ 를 만족하면 다음이 성립한다. 

    $$ [\mathbf{T} ]_{\beta } = \begin{pmatrix} \lambda _{1}&0&\dots&0\\ 0&\lambda _2&\dots&0\\ \vdots& \vdots& \ddots& \vdots \\ 0&0&\dots&\lambda _n\\ \end{pmatrix} $$

    선형연산자 $\mathbf{T}$ 가 대각화가능이면 기저 $\beta$ 의 각 벡터 $v$ 는 적절한 스칼라 $\lambda$ 에 대하여 $\mathbf{T} (v) = \lambda v$ 를 만족한다. $v$ 는 기저의 원소이므로 영벡터가 아니다. 이를 기반으로 고유벡터의 정의를 내릴 수 있다.

!!! tldr "정사각행렬의 대각화가능(diagonalizable)"

    선형연산자 $\mathbf{L}_{A}$ 가 대각화가능이면 정사각행렬 $A$ 를 대각화가능이라고 한다.

# Eigenvector

!!! tldr "선형연산자의 고유벡터(eigenvector) 와 고윳값(eigenvalue)"

    벡터공간 $\mathbf{V}$  의 선형연산자 $\mathbf{T}$ 에 대하여 다음과 같이 정의한다.
    
    - 영벡터가 아닌 벡터 $v \in \mathbf{V}$ 와 스칼라 $\lambda$ 에 대하여 $\mathbf{T} (v) = \lambda v$ 이면 벡터 $v$ 를 $\mathbf{T}$ 의 고유벡터라 한다.

    - 스칼라 $\lambda$ 를 고유벡터 $v$ 에 대응하는 고윳값이라 한다.

- 고유벡터는 특성벡터(characteristic vector, proper vector), 고윳값은 특성값(characteristic value, proper value) 라고도 부른다.

!!! tldr "정사각행렬의 고유벡터(eigenvector) 와 고윳값(eigenvalue)"

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

## Characteristic polynomial (Finding eigenvalue)

!!! tldr "정리 5.2"

    행렬 $A \in \mathbf{M}_{n \times n}$ 에 대하여 스칼라 $\lambda$ 가 $A$ 의 고윳값인 것과 $\det(A - \lambda I_n) = 0$ 인 것은 동치이다.

- 이 정리는 고윳값을 계산하는 방법을 제시한다.

- 이 정리는 특성다항식의 근을 찾으면 유한차원 벡터공간의 행렬 또는 선형연산자의 고윳값을 모두 밝힐 수 있음을 말해준다.

- 증명

    스칼라 $\lambda$ 가 $A$ 의 고윳값임을 가정하자.  스칼라 $\lambda$ 가 $A$ 의 고윳값인 것과 $Av = \lambda v$ 인 영이 아닌 벡터 $v \in \mathbf{F} ^{n}$ 가 존재하는 것은 동치이다. 그러므로 $(A - \lambda I_n) (v) = 0$ 이다.

    $A - \lambda I_n$ 이 가역이면 $v = 0$ 이므로 모순이다. 즉, $A - \lambda I_n$ 는 가역이 아니다. [정리 4.7 따름정리](../Determinants/#b40051741) 에 의하여 $\det(A - \lambda I_n) = 0$ 이다.

!!! tldr "정사각행렬의 특성다항식(Characteristic polynomial) "

    행렬 $A \in \mathbf{M}_{n \times n}(\mathbf{F} )$ 에 대하여 $A$ 의 특성다항식은 다항식 $f(t) = \det(A - tI_n)$ 이다.

- 정리 5.2 는 행렬의 고윳값이 특성다항식의 근임을 말해준다. 이는 특성다항식의 계산을 통하여 행렬 또는 선형연산자의 모든 고윳값을 얻을 수 있음을 뜻한다. 

- 이때 $A - tI_n \not\in \mathbf{M}_{n \times n}(\mathbf{F} )$ 이다. 행렬 $A - tI_n$ 는 $\mathbf{F}$ 를 계수로 가지는 $t$ 에 대한 유리식으로 이루어진 체 $\mathbf{F} (t)$ 에 속해있다. 즉, $A - tI_n \in \mathbf{M}_{n \times n}(\mathbf{F}(t) )$ 이다.

    행렬식에 대한 정리들을 $\mathbf{F} (t)$ 에서도 사용할 수 있다.

- 예시 

    행렬 $A = \begin{pmatrix} 1&1\\ 4&1\\ \end{pmatrix} \in \mathbf{M}_{2 \times 2}(\R )$ 의 고윳값을 구하기 위하여 다음 특성다항식을 풀어보자. 

    $$ \det(A - tI_2) = \det \begin{pmatrix} 1-t&1\\ 4&1-t\\ \end{pmatrix} = t ^{2} - 2t - 3 = (t - 3)(t + 1) $$

    정리 5.2 에 의하여 $A$ 의 고윳값은 $3, -1$ 뿐이다.

!!! tldr "선형연산자의 행렬식(determinant)"

    유한차원 벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 와 $\mathbf{V}$ 의 순서기저 $\beta$ 에 대하여 $\mathbf{T}$ 의 행렬식을 다음과 같이 정의한다.

    $$ \det(\mathbf{T} ) := \det([\mathbf{T} ]_{\beta }) $$

!!! tldr "선형연산자의 특성다항식(Characteristic polynomial)"

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

    선형연산자 $\mathbf{T}$ 의 특성다항식의 정의와 [문제 4.2-23](../Determinants/#f334dfff7) 에 의하여 다음이 성립한다.

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

## Finding eigenvector

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

!!! tldr ""

    차원이 각각 $n$ 이고 순서기저가 $\beta$ 인 벡터공간 $\mathbf{V}$ 와 선형변환 $\mathbf{T} : \mathbf{V} \to \mathbf{V}$ 와 행렬 $A = [\mathbf{T} ]_{\beta}$ 에 대하여 다음이 성립한다. 즉, $\mathbf{L}_{A} \circ \phi _{\beta } = \phi _{\beta  } \circ \mathbf{T}$ 이다.

    $$ \begin{CD} \mathbf{V} @> \mathbf{T}  >> \mathbf{V}  \\ @V \phi _{\beta } VV @VV \phi _{\beta } V \\ \mathbf{F} ^{n} @> \mathbf{L}_{A} >> \mathbf{F} ^{n} \end{CD} $$

    이때 다음이 성립한다.
    
    1. $v \in \mathbf{V}$ 가 $\lambda$ 에 대응하는 $\mathbf{T}$ 의 고유벡터인 것과 $\phi _{\beta }(v)$ 가 $\lambda$ 에 대응하는 $A$ 의 고유벡터인 것은 동치이다.

    2. $A$ 와 $\mathbf{T}$ 의 고윳값 $\lambda$ 에 대하여 벡터 $y \in \mathbf{F} ^{n}$ 가 $\lambda$ 에 대응하는 $A$ 의 고유벡터인 것과 $\phi _{\beta } ^{-1}(y)$ 가 $\lambda$ 에 대응하는 $\mathbf{T}$ 의 고유벡터인 것은 동치이다.

- 이 정리는 유한차원 벡터공간에서 정의된 선형연산자의 고유벡터를 찾는 것을 행렬의 고유벡터를 찾는 것으로 귀결시킬 수 있음을 말해준다.

- 증명

    첫번째 명제는 [그림 2.2](../LinearTransformation/#ea96f31c4) 에서 $\mathbf{V} = \mathbf{W}, \gamma = \beta$ 인 경우이다. ▲ 

    두번째 명제를 보이자. $v$ 가 $\lambda$ 에 대응하는 $\mathbf{T}$ 의 고유벡터임을 가정하자. 그러면 $\mathbf{T} (v) = \lambda v$ 이고 첫번째 명제에 의하여 다음이 성립한다. 

    $$ A \phi _{\beta }(v) = \mathbf{L}_{A}\phi _{\beta }(v) = \phi _{\beta }\mathbf{T} (v) = \phi _{\beta }(\lambda v) = \lambda \phi _{\beta }(v) $$

    $\phi _{\beta }$ 는 동형사상이므로 단사이고 $v = 0$ 일 때에만 $\phi _{\beta }(v) = 0$ 이다. $v$ 가 고유벡터임을 가정했으므로 $v \neq 0$ 이므로 $\phi _{\beta }(v) \neq 0$ 이다. 따라서 $\phi _{\beta }(v)$ 는 $A$ 의 고유벡터이다.
    
    역으로 $\phi _{\beta }(v)$ 가 $A$ 의 고유벡터이면 $v$ 가 $\lambda$ 에 대응하는 $\mathbf{T}$ 의 고유벡터임을 비슷한 논리로 쉽게 보일 수 있다. ▲ 

    세번째 명제는 두번째 명제에서 바로 나온다. ■ 

- 예시 

    $\mathbf{P}_{2}(\R)$ 의 선형연산자 $\mathbf{T} (f(x)) = f(x) + (x+1)f'(x)$ 의 고윳값은 $1, 2, 3$ 이다. 
    
    $\lambda _1 = 1$ 에 대응하는 $A$ 의 고유벡터는 $a \neq 0$ 에 대하여 $a \begin{pmatrix} 1\\ 0\\ 0\\ \end{pmatrix}=ae_1$ 이다. $\beta$ 를 $\mathbf{P}_{2}(\R)$ 의 표준순서기저로 두었을 때 $\lambda _1 = 1$ 에 대응하는 $\mathbf{T}$ 의 고유벡터는 다음과 같다. 

    $$ \phi ^{-1} _{\beta } (ae_1) = a \phi ^{-1}_{\beta } = a \cdot 1 = a $$

    $\lambda _2 = 2$ 에 대하여 정리 5.4 를 통하여 고유벡터를 찾기 위해 다음과 같은 행렬 $B_2$ 를 정의하면 $\mathbf{N} (\mathbf{L}_{B_2}) = \bigg \{a \begin{pmatrix} 1\\ 1\\ 0\\ \end{pmatrix}:a \in \R\bigg \}$ 이다.

    $$ B_2 = A - \lambda _2I=\begin{pmatrix} -1&1&0\\ 0&0&2\\ 0&0&1\\ \end{pmatrix} $$

    따라서 $\lambda _2 = 2$ 에 대응하는 $\mathbf{T}$ 의 고유벡터는 $a \neq 0$ 에 대하여 다음과 같다. 

    $$ \phi _{\beta }^{-1}\bigg (a \begin{pmatrix} 1\\ 1\\ 0\\ \end{pmatrix}\bigg ) = a \phi _{\beta }^{-1}(e_1+e_2) = a(1+x) $$

    $\lambda _3 = 3$ 에 대응하는 $\mathbf{T}$ 의 고유벡터는 $a \neq 0$ 에 대하여 $a(1+2x+x ^{2})$ 이다.

    $a = 1$ 인 고유벡터 집합 $\gamma = \{1, 1+x, 1+2x+x ^{2}\}$ 는 $\mathbf{T}$ 의 고유벡터로 이루어진 $\mathbf{P}_{2}(\R)$ 의 순서기저이므로 $\mathbf{T}$ 를 다음과 같이 대각화할 수 있다.

    $$ [\mathbf{T} ]_{\gamma } = \begin{pmatrix} 1&0&0\\ 0&2&0\\ 0&0&3\\ \end{pmatrix} $$

## Geometric Interpretation of Eigenvector of Linear Operator

!!! tldr ""

    $\R$-벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 의 고유벡터 $v$, 대응하는 고윳값 $\lambda$ 와 $v$ 에 의해 생성된 $\mathbf{V}$ 의 1차원 부분공간 $\mathbf{W} = \text{span} (\{v\})$ 은 $0$ 과 $v$ 를 지나는 직선이다. 이때 다음이 성립한다. 

    1. $\lambda > 1$ 일 때 $\mathbf{T}$ 는 $\mathbf{W}$ 의 벡터를 $0$ 에서 밀어낸다.

    2. $\lambda = 1$ 일 때 $\mathbf{T}$ 는 $\mathbf{W}$ 에서 항등연산자이다.

    3. $0 < \lambda < 1$ 일 때 $\mathbf{T}$ 는 $\mathbf{W}$ 의 벡터를 $0$ 방향으로 당긴다.

    4. $\lambda = 0$ 일 때 $\mathbf{T}$ 는 $\mathbf{W}$ 에서 영 연산자이다.

    5. $\lambda < 0$ 일 때 $\mathbf{T}$ 는 $\mathbf{W}$ 의 벡터를 $0$ 의 반대 방향으로 옮긴다.

- 다음 그림이 이 정리를 설명해준다.

    ![image](https://user-images.githubusercontent.com/16812446/127796880-bf7e7a64-1189-4c4c-a5ca-969ac825e29f.png)

- 예시 

    $\R ^{2}$ 의 $x$ 축 대칭 $\mathbf{T} (a_1, a_2) = (a_1, -a_2)$ 은 고유벡터 $e_1, e_2$ 를 갖는다. 이는 각각 고윳값 $1, -1$ 에 대응한다. 

    $e_1$ 과 $e_2$ 는 각각 1차원 벡터공간 $x$ 축과 $y$ 축을 생성한다. $\mathbf{T}$ 는 $x$축에서 항등변환, $y$축에서 방향을 바꾸는 변환이다.

# Diagonalizability

!!! tldr "정리 5.5"

    벡터공간의 선형연산자 $\mathbf{T}$ 와 $\mathbf{T}$ 의 서로 다른 고윳값 $\lambda_1, \lambda_2, \dots, \lambda_k$ 에 대하여 $\lambda_i$ 에 대응하는 $\mathbf{T}$ 의 고유벡터로 이루어진 유한집합을 $S_i$ 라고 하자. 각 $S_i$ 가 일차독립이면 $\displaystyle \bigcup_{i=1}^{k}S_i$ 도 일차독립이다.

- 이 정리는 각 고윳값에 대응하는 고유벡터를 하나씩 선택하여 형성한 집합은 반드시 일차독립인 집합을 이룬다는 것을 말해준다.

- 증명

    $k = 1$ 인 경우 증명할 것이 없다. ▲ 

    $k > 1$ 을 가정하고 $k - 1$ 에 대하여 정리가 성립함을 가정하자. 또한 서로 다른 $k$ 개의 고윳값 $\lambda_1, \lambda_2, \dots, \lambda_k$ 에 대하여 $S_i = \{v _{i1},v _{i1},\dots,v _{in _{i}}\}$ 가 $\lambda _i$ 에 대응하는 일차독립인 $\mathbf{T}$ 의 고유벡터 집합임을 가정하자.

    $i \in \{1,2,\dots,k\}, j \in \{1,2,\dots,n_i\}$ 에 대하여 다음을 만족하는 스칼라 $a _{ij}$ 가 존재한다.

    $$ \sum_{i=1}^{k}\sum_{j=1}^{n_i}a _{ij}v _{ij} = 0 \tag{1} $$

    $v _{ij}$ 는 $\lambda _i$ 에 대응하는 $\mathbf{T}$ 의 고유벡터이므로
    양 변에 $\mathbf{T} - \lambda _k \mathbf{I}$ 를 적용하면 다음이 성립한다.

    $$ \sum_{i=1}^{k}\sum_{j=1}^{n_i}a _{ij}(\lambda _i - \lambda _k)v _{ij} = 0 \iff  \sum_{i=1}^{k-1}\sum_{j=1}^{n_i}a _{ij}(\lambda _i - \lambda _k)v _{ij} = 0 $$

    가정에 의하여 $\displaystyle \bigcup_{i=1}^{k-1}S_i$ 가 일차독립이므로 $i \in \{1,2,\dots,k-1\}$ 에 대하여 $a _{ij}(\lambda _i- \lambda _k) = 0$ 이다. $\lambda_1, \lambda_2, \dots, \lambda_k$ 는 같지 않으므로 $i \in \{1,2,\dots,k-1\}$ 에 대하여 $a _{ij} = 0$ 이다.

    그러므로 $(1)$ 은 $\sum_{j=1}^{n_k}a _{kj}v _{kj} = 0$ 이 된다. 가정에 의해 $S_k$ 는 일차독립이므로 $a _{kj} = 0$ 이다. 그러므로 모든 증명이 끝났다. ■ 

!!! tldr "정리 5.5 따름정리"

    $n$차원 벡터공간의 선형연산자 $\mathbf{T}$ 가 서로 다른 $n$개의 고윳값을 가지면 $\mathbf{T}$ 는 대각화가능하다.

- 증명

    $n$차원 벡터공간을 $\mathbf{V}$ 라 하자. $\mathbf{T}$ 에서 서로 다른 $n$개의 고윳값 $\lambda _1,\dots,\lambda _n$ 이 존재함을 가정하자. 각 $i$ 에 대하여 $\lambda _i$ 에 대응하는 고유벡터 $v_i$ 를 선택한다. 정리 5.5 에 의하여 $\{v_1, v_2, \dots, v_n \}$ 는 일차독립이고 $\dim (\mathbf{V} ) = n$ 이므로 [정리 1.10 따름정리 2](../VectorSpace/#cd7879a47) 에 의하여 이 집합은 기저이다.

    [정리 5.1](#57f0cd776) 에 의하여 $\mathbf{T}$ 는 대각화가능하다.

- 예시 

    행렬 $A = \begin{pmatrix} 1&1\\ 1&1\\ \end{pmatrix}$ 의($\mathbf{L}_{A}$ 의) 특성다항식은 다음과 같다. 

    $$ \det(A-tI) \det \begin{pmatrix} 1-t&1\\ 1&1-t\\ \end{pmatrix} = t(t-2) $$

    $\mathbf{L}_{A}$ 의 고윳값은 $0, 2$ 이고 $\dim (\R ^{2}) = 2$ 이므로 $\mathbf{L}_{A}$ (와 $A$) 는 대각화 가능하다.

- $\mathbf{T}$ 가 대각화 가능하면 서로 다른 $n$ 개의 고윳값을 가지는 것은 아니다. 가령 항등연산자는 하나의 고윳값 $\lambda =1$ 을 가지지만 대각화가능하다.

## split over

!!! tldr "체 $\mathbf{F}$ 위에서 완전히 인수분해됨(split over $\mathbf{F}$) 의 정의"

    다항식 $f(t) \in \mathbf{P}_{\mathbf{F} }$ 가 스칼라 $c, a_1, a_2, \dots, a_n \in \mathbf{F}$ 에 대하여 다음을 만족하면 체 $\mathbf{F}$ 위에서 완전히 인수분해된다고 한다.

    $$ f(t) = c(t-a_1)(t-a_2)\dots(t-a_n) $$

- 예시 

    $f(t) = t ^{2} - 1 = (t+1)(t-1)$ 이므로 $f(t)$ 는 $\R$ 위에서 완전히 인수분해된다.

    $g(t) = t ^{2} + 1$ 는 $\R$ 위에서 완전히 인수분해되지 않는다. 그러나 $g(t) = (t + i)(t - i)$ 이므로 $g(t)$ 는 $\mathbb{C}$ 위에서 완전히 인수분해된다.

!!! tldr "정리 5.6"

    $\mathbf{F}$-벡터공간 $\mathbf{V}$ 의 대각화가능한 선형연산자의 특성다항식은 $\mathbf{F}$ 위에서 완전히 인수분해된다.

- 이 정리는 선형연산자 $\mathbf{T}$ 의 특성다항식이 중근을 가질 수도 있으므로 대각화가능하기 위하여 서로 다른 $n$ 개의 고윳값을 가질 필요가 없음을 말해준다.

- 증명

    $n$차원 벡터공간 $\mathbf{V}$ 의 대각화가능한 선형연산자를 $\mathbf{T}$ 라 하고 $[\mathbf{T} ]_{\beta } = D$ 가 대각행렬이 되도록 하는 $\mathbf{V}$ 의 순서기저를 $\beta$ 라 하면 $D$ 는 다음과 같다.

    $$ D = \begin{pmatrix} \lambda _{1}&0&\dots&0\\ 0&\lambda _2&\dots&0\\ \vdots& \vdots& \ddots& \vdots \\ 0&0&\dots&\lambda _n\\ \end{pmatrix} $$

    $\mathbf{T}$ 의 특성다항식 $f(t)$ 는 다음과 같다.

    $$ \begin{equation}\begin{split} f(t) &= \det(D-tI) = \begin{pmatrix} \lambda _{1}-t&0&\dots&0\\ 0&\lambda _2-t&\dots&0\\ \vdots& \vdots& \ddots& \vdots \\ 0&0&\dots&\lambda _n-t\\ \end{pmatrix} \\ &= (\lambda _1-t)(\lambda _2-t)\dots(\lambda _n-t)=(-1)^{n}(t-\lambda _1)(t-\lambda _2)\dots(t-\lambda _n) \end{split}\end{equation} \tag*{} $$

    ■ 
     
- 한편 $\mathbf{T}$ 의 특성다항식이 완전히 인수분해되어도 $\mathbf{T}$ 가 대각화 불가능일 수도 있다.

!!! tldr "문제 5.2-9"

    유한차원 벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 에 대하여 $[\mathbf{T}]_{\beta }$ 가 상삼각행렬이 되게 하는 순서기저 $\beta$ 가 존재하면 $\mathbf{T}$ 의 특성다항식이 완전히 인수분해된다.

    상삼각행렬 $A \in \mathbf{M}_{n \times n}(\mathbf{F})$ 의 특성다항식은 완전히 인수분해된다.

- 증명

    $\dim (\mathbf{V}) = n$ 을 가정하자.

    $\mathbf{T}$ 의 특성다항식 $f(t) = \det([\mathbf{T}]_{\beta } - tI_n)$ 의 $A = [\mathbf{T}]_{\beta }-tI_n$ 은 상삼각행렬이다. [문제 4.2-23](../Determinants/#f334dfff7) 에 의하여 $\det(A) = \prod_{i=1}^{n}A _{ii}$ 이다. 따라서 $\mathbf{T}$ 의 특성방정식은 완전히 인수분해된다. ▲ 

    상삼각행렬의 특성다항식이 완전히 인수분해된다는 것도 같은 논리로 증명 가능하다. ■ 

!!! tldr "문제 5.2-12"

    행렬 $A \in \mathbf{M}_{n \times n}(\mathbf{F})$ 의 특성다항식이 완전히 인수분해되면 $A$ 는 상삼각행렬과 닮은 행렬이다.

    유한차원 벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 에 대하여 $\mathbf{T}$ 의 특성다항식이 완전히 인수분해되면 $[\mathbf{T}]_{\beta }$ 가 상삼각행렬이 되게 하는 순서기저 $\beta$ 가 존재한다. 

- 증명

    1:

    $n = 1$ 이면 $A$ 의 특성다항식은 $\det(A _{11} - tI_1) = A _{11} - tI_1$ 으로 완전히 인수분해된다. 또한 $A$ 는 상삼각행렬이다. ▲ 

    $n - 1$ 에서 정리가 성립함을 가정하고 $n$ 에 대하여 증명하자. 가정에 의하여 $A$ 의 특성다항식은 완전히 인수분해된다. 이로써 최소 하나 이상의 고윳값 $\lambda$ 가 존재하고 이 고윳값에 대응하는 최소 하나 이상의 고유벡터 $v_1$ 가 존재한다.

    $\{v_1\}$ 을 확장하여 $\mathbf{F}^{n}$ 의 기저 $\gamma = \{v_1, v_2, \dots, v_n\}$ 를 만들 수 있다. $j$열이 $v_j$ 인 $n \times n$ 행렬을 $P$ 로 두면 $[\mathbf{L}_{A}]_{\gamma } = P ^{-1}AP$ 이다. 

    선형변환의 행렬표현에 의하여 다음이 성립한다.

    $$ \mathbf{L}_{A}(v_1) = Av_1 = \lambda v_1 $$

    $$ \mathbf{L}_{A}(v _{2}) = Av _{2} = \sum_{i=1}^{n} a _{i2}v_i $$

    $$ \vdots $$

    $$ \mathbf{L}_{A}(v _{n}) = Av _{n} = \sum_{i=1}^{n} a _{i,n}v_i $$

    $$ \implies  [\mathbf{L}_{A}]_{\gamma } = \begin{pmatrix} \lambda & u\\ O & B \\ \end{pmatrix} \implies  [\mathbf{L}_{A}]_{\gamma } - tI = \begin{pmatrix} \lambda -t & u\\ O & B - tI \\ \end{pmatrix} $$

    문제 4.3-21 에 의하여 다음이 성립한다.

    $$ \det([\mathbf{L}_{A}]_{\gamma } - tI) = (\lambda - t) \det(B - tI) $$

    $A$ 의 특성다항식이 완전히 인수분해되는데 $[\mathbf{L}_{A}]_{\gamma }$ 는 $A$ 와 닮은 행렬이므로 문제 5.1-13 에 의하여 $[\mathbf{L}_{A}]_{\gamma }$ 의 특성다항식은 완전히 인수분해된다. 따라서 $\det(B-tI)$ 도 완전히 인수분해된다. $B$ 는 $n -1 \times n-1$ 행렬이므로 귀납법의 가정에 의하여 가역행렬 $Q$ 에 대하여 $U = Q ^{-1}BQ$ 인 상삼각행렬이 존재한다.

    $R = \begin{pmatrix} 1&O'\\ O&Q\\ \end{pmatrix}, R ^{-1} = \begin{pmatrix} 1&O'\\ O&Q ^{-1}\\ \end{pmatrix}$ 로 두고 $M = PR$ 로 두면 다음이 성립한다. 

    $$ \begin{equation}\begin{split} M ^{-1}AM &= R ^{-1}(P ^{-1}AP)R \\ &= \begin{pmatrix} 1&O'\\ O&Q ^{-1}\\ \end{pmatrix}\begin{pmatrix} \lambda & u\\ O&B\\ \end{pmatrix} \begin{pmatrix} 1&O'\\ O&Q\\ \end{pmatrix}\\ &= \begin{pmatrix} \lambda &uQ\\ O&U \\ \end{pmatrix}= U' \end{split}\end{equation} \tag*{} $$

    즉, $A$ 가 상삼각행렬 $U'$ 와 닮음이니 모든 증명이 끝났다. ■ 

    2:

    $\mathbf{V}$ 의 순서기저 $\gamma = \{x_1, x_2, \dots, x_n\}$ 에 대하여 $A = [\mathbf{T}]_{\gamma }$ 로 두자. 정리의 가정에 의하여 $\mathbf{T}$ 의 특성다항식은 완전히 인수분해 되고 특성다항식의 정의에 의하여 $A$ 의 특성다항식도 완전히 인수분해된다. 따라서 이미 증명한 1) 에 의하여 $A$ 는 상삼각행렬 $U$ 와 닮은 행렬이다. 가역행렬 $Q$ 가 $U = Q ^{-1}AQ$ 를 만족한다고 하면 $j \in \{1,\dots,n\}$ 에 대하여 다음이 성립한다. 

    $$ y_j = \sum_{i=1}^{n}Q _{ij}x_i $$

    문제 2.5-13 에 의하여 $\beta = \{y_1, y_2, \dots, y_n\}$ 는 $\mathbf{V}$ 의 기저이고 $Q$ 는 $\beta$ 좌표를 $\gamma$ 좌표로 변환하는 좌표변환행렬이다. [정리 2.23](../LinearTransformation/#acf61b9cb) 에 의하여 다음이 성립한다. 

    $$ \therefore [\mathbf{T}]_{\beta } = Q ^{-1}[\mathbf{T}]_{\gamma }Q = Q ^{-1}AQ = U \tag*{■} $$

## Algebraic Multiplicity

!!! tldr "대수적 중복도(algebraic multiplicity)"

    특성다항식이 $f(t)$ 인 선형연산자(또는 행렬)의 고윳값 $\lambda$ 에 대하여 $(t - \lambda )^{k}$ 가 $f(t)$ 의 인수가 되도록 하는 가장 큰 자연수 $k$ 를 $\lambda$ 의 대수적 중복도라고 한다.

- 단순하게 중복도라고도 한다.

- 예시 

    $A = \begin{pmatrix} 3&1&0\\ 0&3&4\\ 0&0&4\\ \end{pmatrix}$ 의 특성다항식은 $f(t) = -(t-3)^{2}(t-4)$ 이므로 $\lambda =3$ 의 중복도는 $2$, $\lambda =4$ 의 중복도는 $1$ 이다.

## Eigenspace

!!! tldr "선형연산자의 고유공간(eigenspace)"

    벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 와 고윳값 $\lambda$ 에 대하여 다음 집합 $\mathbf{E}_{\lambda}$ 를 고윳값 $\lambda$ 에 대응하는 $\mathbf{T}$ 의 고유공간이라 한다.

    $$ \mathbf{E}_{\lambda} = \{x \in \mathbf{V} : \mathbf{T} (x) = \lambda x\} = \mathbf{N} (\mathbf{T}-\lambda \mathbf{I} _{\mathbf{V} }) $$

- 즉, 고유공간은 특정 고윳값에 대응하는 모든 고유벡터를 모아둔 집합이다.

- 고유공간은 고윳값에 대응하는 모든 벡터의 집합인데 [정리 5.4](#2514593f4) 는 고윳값에 대응하는 모든 고유벡터를 찾는 방법을 알려준다. 따라서 고유공간은 정리 5.4 의 방법을 기반으로 정의된다.

    정리 5.4 는 행렬에 대하여 고윳값에 대응하는 모든 벡터를 구하는 방법을 서술하지만, 동형사상인 표준표현 $\phi _{\beta }$ 로 인하여 이 정리를 동일하게 선형연산자에서 사용할 수 있다. 다시 말해 정리 5.4 가 $(A - \lambda I)v=0$ 을 풀어서 고윳값에 대응하는 모든 고유벡터를 구하라고 말하는데, 이것은 동형사상인 표준표현에 의하여 영공간 $\mathbf{N} (\mathbf{T} - \lambda \mathbf{I} _{\mathbf{V}})$ 을 구하는 것과 동치가 된다.

- 이때 정리 5.4 와 달리 $v \neq 0$ 라는 제한이 없으므로 [정리 2.1](../LinearTransformation/#eb957cbf0) 에 의하여 $\mathbf{E}_{\lambda}$ 는 고윳값 $\lambda$ 에 대응하는 $\mathbf{T}$ 의 고유벡터와 영벡터로 이루어진 $\mathbf{V}$ 의 부분공간이다. 즉, $\mathbf{E}_{\lambda}$ 의 차원은 고윳값 $\lambda$ 에 대응하는 일차독립인 $\mathbf{T}$ 의 고유벡터의 최대 개수이다.

!!! tldr "행렬의 고유공간(eigenspace)"

    벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{L}_{A}$ 와 고윳값 $\lambda$ 에 대하여 다음 집합 $\mathbf{E}_{\lambda}$ 를 고윳값 $\lambda$ 에 대응하는 $A$ 의 고유공간이라 한다.

    $$ \mathbf{E}_{\lambda} = \{x \in \mathbf{V} : \mathbf{L}_{A} (x) = \lambda x\} = \mathbf{N} (\mathbf{L}_{A}-\lambda \mathbf{I} _{\mathbf{V} }) $$

!!! tldr "정리 5.7"

    유한차원 벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 와 중복도가 $m$ 인 $\mathbf{T}$ 의 고윳값 $\lambda$ 에 대하여 $1 \leq \dim (\mathbf{E}_{\lambda} )\leq m$ 이다.

- 이 정리는 $\mathbf{E}_{\lambda}$ 의 차원과 $\lambda$ 의 중복도의 관계를 말해준다.

- 증명

    [정리 1.11 따름정리](../VectorSpace/#dd66d2443) 에 의하여 $\mathbf{E}_{\lambda}$ 의 순서기저 $\{v_1, v_2, \dots, v_p\}$ 를 확장하여 $\mathbf{V}$ 의 순서기저 $\beta = \{v_1, v_2, \dots, v_p, v _{p+1}, \dots, v_n\}$ 를 만들 수 있다. [선형변환의 행렬표현](../LinearTransformation/#c16bc5e5b) 에 의하여 $[\mathbf{T} ]_{\beta }=A$ 을 $1$ 열부터 $n$ 열까지는 다음과 같다. 

    $$ \mathbf{T} (v_1) = a _{11}v_1 = \lambda _1v_1 $$

    $$ \vdots $$

    $$ \mathbf{T} (v_p) = a _{pp}v_p = \lambda _pv_p $$

    $$ \mathbf{T} (v _{p+1}) = \sum_{i=1}^{n} a _{i,p+1} v _{p+1} $$

    $$ \vdots $$

    $$ \mathbf{T} (v _{n}) = \sum_{i=1}^{n} a _{in} v _{n} $$

    그러므로 어떤 행렬 $B, C$ 와 영행렬 $O$ 에 대하여 $A$ 는 다음과 같다.

    $$ A = \begin{pmatrix} \lambda I_p&B\\ O&C\\ \end{pmatrix} $$

    문제 4.3-21 에 의하여 $\mathbf{T}$ 의 특성다항식은 다음과 같다. 

    $$ \begin{equation}\begin{split} f(t)&= \det(A - tI_n) = \det \begin{pmatrix} (\lambda -t)I_p&B\\ O&C - tI _{n-p}\\ \end{pmatrix}  \\ &= \det((\lambda -t)I_p)  \det(C-tI _{n-p}) \\ &= (\lambda -t)^{p}g(t) \end{split}\end{equation} \tag*{} $$

    따라서 $\lambda$ 의 중복도 $m$ 에 대하여 $p \leq m$ 이다. 그런데 $\dim (\mathbf{E}_{\lambda} ) = p$ 이므로 $\dim (\mathbf{E}_{\lambda} ) \leq m$ 이다. ■ 

!!! tldr "정리 5.8"

    유한차원 벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 에 대하여 $\mathbf{T}$ 의 특성다항식이 완전히 인수분해되고 $\lambda _1, \dots, \lambda _k$ 가 서로 다른 $\mathbf{T}$ 의 고윳값일 때 다음이 성립한다. 

    1. $\mathbf{T}$ 가 대각화가능한 것과 모든 $i$ 에 대하여 $\lambda _i$ 의 중복도가 $\dim (\mathbf{E}_{\lambda_i})$ 인 것은 동치이다.

    2. $\mathbf{T}$ 가 대각화가능하고 각각의 $i$ 에 대하여 $\beta _{i}$ 가 $\mathbf{E}_{\lambda_i}$ 의 순서기저일 때 $\beta = \displaystyle \bigcup_{i=1}^{k}\beta _{i}$ 는 $\mathbf{T}$ 의 고유벡터로 이루어진 $\mathbf{V}$ 의 순서기저이다.

- 순서기저 $\beta = \displaystyle \bigcup_{i=1}^{k}\beta _{i}$ 의 순서는 $\beta_1, \dots, \beta_k$ 의 벡터를 나열하는 순서 그대로이다.

- 증명

    각각의 $i$ 에 대하여 $m_i$ 는 $\lambda _i$ 의 중복도, $d_i = \dim (\mathbf{E}_{\lambda_i})$, $n = \dim (\mathbf{V} )$ 라고 하자.

    $\mathbf{T}$ 가 대각화가능함을 가정하면 $\mathbf{T}$ 의 고유벡터로 이루어진 $\mathbf{V}$ 의 기저 $\beta$ 가 존재한다. 각 $i$ 에 대하여 $\beta _i = \beta \cap \mathbf{E}_{\lambda_i}$ 의 기수를 $|\beta _i| = n_i$ 라 하면 $n_i \leq d_i$ 이다. [정리 1.10 따름정리 2](../VectorSpace/#cd7879a47) 에 의하여 일차독립인 집합은 벡터공간의 차원보다 기수가 작기 때문이다. 또한 정리 5.7 에 의하여 $d_i \leq m_i$ 이다. 

    $\lambda _i$ 에 대응하는 $v_i$ 들은 모두 서로 다르다. 만약 같은 $v$ 에 대하여 $\mathbf{T} (v) = \lambda _iv = \lambda _jv$ 가 성립하면 $(\lambda _i-\lambda _j)v = 0 \implies \lambda _i = \lambda _j$ 가 된다. 그러므로 $|\beta| = n \implies \sum_{i=1}^{k}n_i = n$ 이다.

    중복도는 그 정의에 의하여 모든 중복도의 합이 곧 특성다항식의 차수가 된다. $[\mathbf{T}]_{\beta} \in \mathbf{M}_{n \times n}(\mathbf{F} )$ 의 특성다항식의 차수 $n$ 이므로 $\sum_{i=1}^{k}m_i = n$ 이다. 정리 5.5 는 $\beta _i$ 가 일차독립 집합임을 말해준다. 

    일차독립 집합은 [정리 1.10](../VectorSpace/#6cf7acf90) 에 의하여 반드시 $\mathbf{E}_{\lambda_i}$ 의 차원과 기수가 같거나 작다. 또한 정리 5.7 에 의하여 $\mathbf{E}_{\lambda_i}$ 의 차원은 $\lambda _i$ 의 중복도 $m_i$ 와 같거나 작다. 따라서 다음이 성립한다. 

    $$ n = \sum_{i=1}^{k}n_i \leq \sum_{i=1}^{k}d_i \leq \sum_{i=1}^{k}m_i = n $$

    그러므로 $\displaystyle \sum_{i=1}^{k}(m_i - d_i) = 0$ 이다. 정리 5.7 에 의하여 $m_i - d_i \geq 0$ 이므로 각 $i$ 에 대하여 $m_i = d_i$ 이다. ▲ 

    이제 모든 $i$ 에 대하여 $m_i = d_i$ 를 가정하고, $\mathbf{T}$ 가 대각화가능인 것과 2) 를 증명하자.

    각 $i$ 에 대하여 $\mathbf{E}_{\lambda_i}$ 의 순서기저를 $\beta _i$ 라 하고 $\beta = \bigcup_{i=1}^{k}\beta _i$ 를 정의하자. 그러면 정리 5.5 에 의해 $\beta$ 는 일차독립이다. 또한 $|\beta | = \sum_{i=1}^{k}d_i = \sum_{i=1}^{k}m_i = n$ 이다. 중복도의 합이 특성다항식의 차수 $n$ 이 되기 때문이다. [정리 1.10 따름정리 2](../VectorSpace/#cd7879a47) 에 의하여 $\beta$ 는 $\mathbf{V}$ 의 고유벡터로 이루어진 $\mathbf{V}$ 의 순서기저이다. 그러므로 [정리 5.1](#57f0cd776) 에 의하여 $\mathbf{T}$ 는 대각화가능하다. ■ 

- 예시

    $\R ^{3}$ 의 선형연산자 $\mathbf{T}$ 를 다음과 같이 정의하자. 

    $$ \mathbf{T} \begin{pmatrix} a_1\\ a_2\\ a_3\\ \end{pmatrix} = \begin{pmatrix} 4a_1+a_3\\ 2a_1+3a_2+2a_3\\ a_1+4a_3\\ \end{pmatrix} $$

    표준순서기저 $\beta$ 에 대한 $\mathbf{T}$ 의 행렬표현은 다음과 같다. 

    $$ [\mathbf{T} ]_{\beta }=\begin{pmatrix} 4&0&1\\ 2&3&2\\ 1&0&4\\ \end{pmatrix} $$

    $\mathbf{T}$ 의 특성다항식으로 모든 고윳값을 구해보자.

    $$ \det([\mathbf{T} ]_{\beta }-tI) = \det \begin{pmatrix} 4-t&0&1\\ 2&3-t&2\\ 1&0&4-t\\ \end{pmatrix} = -(t-5)(t-3)^{2} $$

    고윳값 $\lambda _1 = 5$ 와 $\lambda _2 = 3$ 중복도는 각각 $1, 2$ 이므로 $\mathbf{E}_{\lambda_1}$ 와 $\mathbf{E}_{\lambda_2}$ 기저가 각각 $1, 2$ 이면 $\mathbf{T}$ 는 대각화 가능하다.

    $\mathbf{E}_{\lambda_1}$ 는 다음과 같다. 

    $$ \mathbf{E}_{\lambda_1} = \mathbf{N} (\mathbf{T}-\lambda _1 \mathbf{I})  = \Bigg \{\begin{pmatrix} x_1\\ x_2\\ x_3\\ \end{pmatrix}\in \R ^{3} : \begin{pmatrix} -1&0&1\\ 2&-2&2\\ 1&0&-1\\ \end{pmatrix}\begin{pmatrix} x_1\\ x_2\\ x_3\\ \end{pmatrix}=\begin{pmatrix} 0\\ 0\\ 0\\ \end{pmatrix}\Bigg \} $$

    따라서 $\mathbf{E}_{\lambda_1}$ 은 다음 연립방정식의 해공간 $\mathbf{K} = \mathbf{E}_{\lambda_1}$ 이다.

    $$ -x_1+x_3=0 $$
    
    $$ 2x_1-2x_2+2x_3=0 $$

    $$ x_1-x_3=0 $$

    계수행렬 $A$ 의 3행은 1행에 대하여 일차종속이므로 $\text{rank} (A) = 2$ 이다. [정리 3.8](../MatrixOperation/#b7b9c78d0) 에 의하여 $\dim (\mathbf{K} ) = \dim (\mathbf{E}_{\lambda_1}) = 3 - \text{rank} (A) = 3 - 2 = 1$ 이다. 기저를 구해보면 $\bigg \{\begin{pmatrix} 1\\ 2\\ 1\\ \end{pmatrix}\bigg \}$ 이다.

    같은 방법으로 $\dim (\mathbf{E}_{\lambda_2}) = 2$ 를 알 수 있다. 기저를 구해보면 $\bigg \{\begin{pmatrix} 0\\ 1\\ 0\\ \end{pmatrix}, \begin{pmatrix} -1\\ 0\\ 1\\ \end{pmatrix}\bigg \}$ 이다.

    그러면 각 고윳값 $\lambda _i$ 의 중복도가 고유공간 $\mathbf{E}_{\lambda_i}$ 의 차원과 같으므로 정리의 1) 에 의하여 $\mathbf{T}$ 는 대각화가능하다.

    $\mathbf{T}$ 가 대각화가능이므로 $\mathbf{E}_{\lambda_1}, \mathbf{E}_{\lambda_2}$ 의 순서기저의 합집합 $\bigg \{\begin{pmatrix} 1\\ 2\\ 1\\ \end{pmatrix}, \begin{pmatrix} 0\\ 1\\ 0\\ \end{pmatrix}, \begin{pmatrix} -1\\ 0\\ 1\\ \end{pmatrix}\bigg \}$ 은 정리의 2) 에 의하여 $\mathbf{V}$ 의 순서기저이다.

## Diagonalizable Determination

!!! tldr "대각화 가능 판정법(Diagonalizable Determination)"

    $n$차원 벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 가 대각화가능한 것과 다음 두 조건이 성립하는 것은 동치이다.

    1. $\mathbf{T}$ 의 특성다항식이 완전히 인수분해된다.

    2. $\mathbf{T}$ 의 고윳값 $\lambda$ 의 중복도가 $2$ 이상인 것들이 $\dim(\mathbf{E}_{\lambda}) = \text{nullity} (\mathbf{T} - \lambda \mathbf{I}) = n - \text{rank} (\mathbf{T} - \lambda \mathbf{I} )$ 와 같다.

- 이 정리는 정리 5.8 의 첫번째 명제를 되풀어 말한 것 뿐이다.

- 정사각행렬 $A$ 가 대각화가능한지 판정할 때도 이 방법을 사용한다. $A$ 의 대각화 가능성과 $\mathbf{L}_{A}$ 의 대각화 가능성이 동치이기 때문이다.

- $\mathbf{T}$ 가 대각화가능한 연산자이고 $\beta _1, \dots, \beta _k$ 가 $\mathbf{T}$ 의 각각의 고유공간 $\mathbf{E}_{\lambda_i}$ 의 순서기저이면 [정리 5.8](#7050c2a83) 에 의해 $\beta = \bigcup_{}^{}\beta _i$ 는 $\mathbf{V}$ 의 기저이고, $[\mathbf{T} ]_{\beta }$ 는 대각행렬이다.

    $\mathbf{T}$ 가 대각화가능한지 판정하려면 $\mathbf{V}$ 의 기저 $\alpha$ 에 대한 $B = [\mathbf{T} ]_{\alpha}$ 를 다룬다. $B$ 의 특성다항식이 완전히 인수분해되면 중복도가 $2$ 이상인 고윳값들이 $n - \text{rank} (B - \lambda I)$ 와 같은지 확인한다. 모두 같으면 $B$ 와 $\mathbf{T}$ 는 대각화 가능이다. (중복도가 $1$ 인 고윳값들은 [정리 5.7](#b5fbbceb6) 에 의하여 자동으로 조건 2) 를 만족하게 된다.)

    $\mathbf{T}$ 의 대각화가능이 확인되었다면 $\mathbf{T}$ 의 고유벡터로 이루어진 $\mathbf{V}$ 의 기저 $\beta$ 를 찾아야 한다. 이를 위해 $B$ 의 각 고유공간에 대한 기저를 찾는다. 그러면 정리 5.8 에 의해 이 기저들의 합집합을 $B$ 의 고유벡터로 이루어진 $\mathbf{F} ^{n}$ 의 기저 $\gamma$ 로 둘 수 있다. 

    $\gamma$ 의 각 벡터는 $\mathbf{T}$ 의 고유벡터로 이루어진 $\alpha$ 에 대한 좌표벡터이다. 따라서 $\gamma$ 를 통해 $\beta$ 를 구할 수 있다. 이 $\beta$ 를 통해 최종적으로 $\mathbf{T}$ 를 $[\mathbf{T} ]_{\beta }$ 로 대각화할 수 있다.

- 증명

    [정리 5.6](#867268fd3) 은 $\mathbf{T}$ 가 대각화가능이면 특성다항식이 완전히 인수분해됨을 말해준다. 그러나 완전히 인수분해된다고 해서 $\mathbf{T}$ 가 대각화가능인 것은 아니다. 하지만 완전히 인수분해된다는 조건은 $\mathbf{T}$ 가 대각화가능하기 위한 필요조건이다. 

    $\mathbf{T}$ 의 특성다항식이 완전히 인수분해되면 각각의 고윳값에 따른 중복도를 구할 수 있다. 이때 각 고윳값 $\lambda$ 의 중복도가 $\dim (\mathbf{E}_{\lambda})$ 와 같으면 [정리 5.8](#7050c2a83) 에 의하여 $\mathbf{T}$ 는 대각화가능이 된다.

    중복도가 $1$ 인 고윳값들은 [정리 5.7](#b5fbbceb6) 에 의하여 자동으로 조건 2) 를 만족하게 된다.

    $\dim (\mathbf{E}_{\lambda})$ 는 특성다항식 $\mathbf{T} - \lambda \mathbf{I} _{\mathbf{V} }$ 의 영공간의 차원이다. 또한 [정리 3.8](../MatrixOperation/#b7b9c78d0) 에 의하여 계수행렬 $\mathbf{T} - \lambda \mathbf{I}$ 를 가지는 일차연립방정식의 해공간이기도 하다. ■ 

- 예시 

    행렬 $A = \begin{pmatrix} 3&1&0\\ 0&3&0\\ 0&0&4\\ \end{pmatrix} \in \mathbf{M}_{3 \times 3}(\R)$ 의 대각화 가능성을 판정하자. $\det(A - tI) = -(t-4)(t-3)^{2}$ 이므로 $\lambda _1 = 4$ 는 조건 2) 를 자동으로 만족한다. $\lambda _2 = 3$ 에 대한 조건 2) 의 성립만 확인하면 $\mathbf{T}$ 는 대각화가능하다.

    행렬 $A - \lambda _2I = \begin{pmatrix} 0&1&0\\ 0&0&0\\ 0&0&1\\ \end{pmatrix}$ 의 랭크가 $2$ 이므로 $3 - \text{rank} (A - \lambda _2I) = 1$ 은 $\lambda _2$ 의 중복도와 다르다. 따라서 $A$ 는 대각화 불가능이다.

- 예시 

    다음과 같은 벡터공간 $\mathbf{P}_{2}(\R)$ 의 선형연산자 $\mathbf{T}$ 가 존재한다. 

    $$ \mathbf{T} (f(x)) = f(1) + f'(0)x + (f'(0)+f''(0))x ^{2} $$

    $\mathbf{T}$ 의 대각화 가능성을 판정해보자. 표준순서기저 $\alpha$ 에 대하여 $B = [\mathbf{T} ]_{\alpha }= \begin{pmatrix} 1&1&1\\ 0&1&0\\ 0&1&2\\ \end{pmatrix}$ 이다. $B$ 와 $\mathbf{T}$ 의 특성다항식은 $-(t-1)^{2}(t-2)$ 으로써 완전히 인수분해된다. $\lambda _1=1$ 의 중복도는 $2$, $\lambda _2 = 2$ 의 중복도는 $1$ 이다. $\lambda _1=1$ 이 조건 2) 를 만족하는지 살펴보자. 

    $$ 3 - \text{rank} (B - \lambda _1I)  = 3 - \text{rank} \begin{pmatrix} 0&1&1\\ 0&0&0\\ 0&1&1\\ \end{pmatrix}=3-1=2 $$

    따라서 $\mathbf{T}$ 는 대각화 가능하다.

    이제 $\mathbf{T}$ 를 대각화해보자. $\lambda _1 = 1$ 의 고유공간 $\mathbf{E}_{\lambda_1}$ 는 다음과 같다. 

    $$ \mathbf{E}_{\lambda_1} = \bigg \{\begin{pmatrix} x_1\\ x_2\\ x_3\\ \end{pmatrix} \in \R ^{3} : \begin{pmatrix} 0&1&1\\ 0&0&0\\ 0&1&1\\ \end{pmatrix}\begin{pmatrix} x_1\\ x_2\\ x_3\\ \end{pmatrix} = 0\bigg \} $$

    이 고유공간의 기저는 $\gamma _1 = \bigg \{\begin{pmatrix} 1\\ 0\\ 0\\ \end{pmatrix}, \begin{pmatrix} 0\\ -1\\ 1\\ \end{pmatrix}\bigg \}$ 이다.

    $\mathbf{E}_{\lambda_2}$ 의 기저는 $\gamma _2 = \bigg \{\begin{pmatrix} 1\\ 0\\ 1\\ \end{pmatrix}\bigg \}$ 이다. $\gamma = \gamma _1 \cup \gamma _2 = \bigg \{\begin{pmatrix} 1\\ 0\\ 0\\ \end{pmatrix}, \begin{pmatrix} 0\\ -1\\ 1\\ \end{pmatrix}, \begin{pmatrix} 1\\ 1\\ 0\\ \end{pmatrix}\bigg \}$ 은 $B$ 의 고유벡터로 이루어진 $\R ^{3}$ 의 순서기저이다. $\gamma \in \mathbf{F} ^{3}$ 의 각 벡터는 $\beta = \{1, -x+x ^{2}, 1+x ^{2}\} \in \mathbf{P}_{2}(\R)$ 의 $\alpha$ 에 대한 좌표벡터이다. $\beta$ 는 $\mathbf{T}$ 의 고유벡터로 이루어진 $\mathbf{P}_{2}(\R)$ 의 순서기저이므로 $\mathbf{T}$ 를 대각화해보면 다음과 같다.

    $$ [\mathbf{T} ]_{\beta } = \begin{pmatrix} 1&0&0\\ 0&1&0\\ 0&0&2\\ \end{pmatrix} $$

# Direct sum

!!! tldr "집합의 덧셈, 합(sum) "

    벡터공간 $\mathbf{V}$ 의 부분공간 $\mathbf{W} _1, \mathbf{W} _2, \dots, \mathbf{W} _k$ 에 대하여 다음 집합을 부분공간의 합이라 한다.

    $$ \sum_{i=1}^{k}\mathbf{W} _i := \bigg \{\sum_{i=1}^{k}v_i : v_i \in \mathbf{W} _i \bigg \} $$

- 예시

    $\R ^{3}$ 의 부분공간 $xy$ 평면 $\mathbf{W} _1$, $yz$ 평면 $\mathbf{W} _2$ 에 대하여 다음이 성립한다. 

    $$ (a, b, c) = (a, 0, 0) + (0, b, c) \in \R ^{3} $$

    $(a, 0, 0) \in \mathbf{W} _1, (0, b, c) \in \mathbf{W} _2$ 이므로 $\R ^{3} = \mathbf{W} _1 + \mathbf{W} _2$ 이다.

!!! tldr "직합(direct sum)"

    벡터공간 $\mathbf{V}$ 의 부분공간 $\mathbf{W} _1, \mathbf{W} _2, \dots, \mathbf{W} _k$ 와 $i, j \in \{1,\dots,k\}$ 에 대하여 다음을 만족하는 $\mathbf{W}$ 를 $\mathbf{W} _1, \mathbf{W} _2, \dots, \mathbf{W} _k$ 의 직합이라 한다.

    1. $\displaystyle \mathbf{W} = \sum_{i=1}^{k}\mathbf{W} _i$
    
    2. $\displaystyle \mathbf{W} _j \cap \sum_{i \neq j}^{}\mathbf{W} _i = \{0\}$ 

    또한 $\mathbf{W} _1, \mathbf{W} _2, \dots, \mathbf{W} _k$ 의 직합 $\mathbf{W}$ 를 다음과 같이 표기한다.

    $$ \boxed{\mathbf{W} := \mathbf{W} _1 \oplus \mathbf{W} _2 \oplus \dots \oplus \mathbf{W} _k = \bigoplus_{i=1}^{k}\mathbf{W} _k} $$ 

- 직합은 $\mathbf{V}$ 를 간단한 부분공간으로 분해하는 방법을 제공한다. 이는 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 가 $\mathbf{V}$ 에 어떻게 작용하는지 파악할 수 있게 해준다.

    또한 직합은 대각화 불가능한 선형연산자를 다룰 때 유용하게 사용된다.

- 예시 

    $\R ^{5}$ 의 $\mathbf{W} = \{(x_1, x_2, x_3, x_4, x_5) : x_5 = 0\}, \mathbf{W}_1 = \{(a, b, c, 0, 0) : a, b, c \in \R \}, \mathbf{W}_2 = \{(0, 0, 0, d, 0) : d \in \R \}$ 에 대하여 다음이 성립한다. 

    $$ (a, b, c, d, 0) = (a, b, c, 0, 0) + (0, 0, 0, d, 0) \in \mathbf{W} _1 + \mathbf{W} 2 $$

    따라서 $\mathbf{W} = \sum_{i=1}^{2}\mathbf{W} _i$ 이다.

    또한 $\mathbf{W} _1 \cap \mathbf{W} _2 = \{0\}$ 이다. 따라서 $\displaystyle \mathbf{W} _1 \oplus \mathbf{W} _2 = \mathbf{W}$ 이다.

- 책에는 직합에 $\mathbf{W} _i \subseteq \mathbf{W}$ 라는 조건이 있다. 근데 내 생각에 이 조건은 1) 이 함의한다. 왜냐하면 영벡터 $0$ 이 다른 부분공간들을 대표하면 특정 $k$ 에 대하여 $\sum \mathbf{W}_i = \mathbf{W}_k \subset \mathbf{W}$ 가 되기 때문이다.

## Properties of direct sum

!!! tldr "정리 5.9"

    유한차원 벡터공간 $\mathbf{V}$ 의 부분공간 $\mathbf{W} _1, \mathbf{W} _2, \dots, \mathbf{W} _k$ 와 $i \in \{1, \dots, k\}$ 에 대하여 다음은 동치이다.

    1. $\displaystyle \mathbf{V} = \bigoplus_{i=1}^{k}\mathbf{W} _i$

    2. $\displaystyle \mathbf{V} = \sum_{i=1}^{k}\mathbf{W} _i$ 이고 $v_i \in \mathbf{W} _i$ 에 대하여 $\displaystyle \sum_{i=1}^{k}v_i = 0$ 이면 $v_i = 0$ 이다.

    3. $v \in \mathbf{V}$ 에 대하여 $v = \displaystyle \sum_{i=1}^{k}v_i$ 를 만족하는 $v_i \in \mathbf{W} _i$ 가 유일하게 존재한다.

    4. $\mathbf{W} _i$ 의 순서기저 $\gamma _i$ 에 대하여 $\displaystyle \bigcup_{i=1}^{k}\gamma _i$ 는 $\mathbf{V}$ 의 순서기저이다.

    5. $\displaystyle \bigcup_{i=1}^{k}\gamma _i$ 가 $\mathbf{V}$ 의 순서기저가 되게 하는 $\mathbf{W} _i$ 의 순서기저 $\gamma _i$ 가 존재한다.

- 이 정리는 직합의 정의와 동치인 명제들을 말해준다.

- 1 에서 2 를 도출하는 증명

    직합의 정의에 의하여 $\mathbf{V} = \displaystyle \sum_{i=1}^{k}\mathbf{W} _i$ 이고 가정에 의하여 $v_i \in \mathbf{W} _i$ 에 대하여 $\displaystyle \sum_{i=1}^{k}v_i = 0$ 이다. 임의의 $j$ 에 대하여 합의 정의에 의하여 $-v_j = \displaystyle \sum_{i\neq j}^{} v_i \in \displaystyle \sum_{i\neq j}^{}\mathbf{W} _i$ 이다. 부분공간은 스칼라곱에 대하여 닫혀있으므로 $-v_j \in \mathbf{W} _j$ 이고, 직합의 정의에 의하여 $-v_j \in \mathbf{W} _j \cap \displaystyle \sum_{i\neq j}^{}\mathbf{W} _i = \{0\}$ 이다. 이는 $v_j = 0$ 임을 뜻한다. ■ 

- 2 에서 3 를 도출하는 증명

    2) 는 부분공간의 합이 곧 원래의 벡터공간이 됨을 말하므로 $v \in \mathbf{V}$ 와 $v_i \in \mathbf{W} _i$ 에 대하여 $v = v_1 + v_2 + \dots + v_k$ 인 벡터 $v_1, v_2, \dots, v_k$ 가 존재한다. 

    존재성 증명이 되었으니 유일성을 증명하자. $v_i \neq w_i \in \mathbf{W} _i$ 에 대하여 $v = w_1 + w_2 + \dots + w_k$ 가 성립한다고 하면 다음이 성립한다. 

    $$ (v_1 - w_1) + (v_2 - w_2) + \dots + (v_k - w_k) = v - v = 0 $$

    $v_i - w_i \in \mathbf{W} _i$ 인데 2) 를 가정했으므로 $v_i - w_i = 0 \implies v_i = w_i$ 이다. 이는 모순이다. ■ 

- 3 에서 4 를 도출하는 증명

    3) 을 가정했으므로 $\mathbf{V} = \displaystyle \sum_{i=1}^{k}\mathbf{W} _i$ 이다. 집합 $\gamma _i$ 는 모든 $v_i \in \mathbf{W} _i$ 를 생성한다. 따라서 집합 $\displaystyle \bigcup_{}^{}\gamma _i$ 로 모든 $\displaystyle \sum_{i=1}^{k}v_i \in \mathbf{V}$ 를 생성할 수 있다.

    이 생성집합이 일차독립임을 보이면 기저이므로 증명이 끝난다. $j \in \{1,2, \dots, |\gamma _i|\}$ 에 대한 $\displaystyle \sum_{i=1}^{k}\displaystyle \sum_{j=1}^{|\gamma _i|}a _{ij} v _{ij} = 0$ 인 벡터 $v _{ij} \in \gamma _i$ 와 스칼라 $a _{ij}$ 가 존재한다. $w_i = \displaystyle \sum_{j=1}^{|\gamma _i|}a _{ij}v _{ij}$ 로 두면 $w_i \in \text{span} (\gamma _i) = \mathbf{W} _i$ 이고 다음이 성립한다. 

    $$ w_1 + w_2 + \dots + w_k = \sum_{i=1}^{k}\sum_{j=1}^{|\gamma _i|}a _{ij}v _{ij} = 0 $$

    부분공간은 벡터공간이므로 $0 \in \mathbf{W} _i$ 이다. 따라서 $w_1 = 0, w_2 = 0, \dots, w_k = 0$ 을 가정할 경우 $w_1 + w_2 + \dots + w_k = 0+0+\dots+0 = 0$ 이다. 3) 을 가정했는데 3) 에 따르면 이 표현은 유일하다. 즉, $w_i \neq 0$ 일 경우 $w_1 + w_2 + \dots + w_k = 0$ 는 성립하지 않는다. 그러므로 $w_i = 0$ 이다. 이는 다음이 성립함을 뜻한다. 

    $$  0 = w_i = \sum_{j=1}^{|\gamma _i|} a _{ij}v _{ij} $$

    $\gamma _i$ 는 일차독립이므로 위 식이 성립하기 위한 스칼라는 영벡터의 자명한 표현 뿐이다. 즉, $a _{ij} = 0$ 이다. 이는 $\displaystyle \bigcup_{}^{}\gamma _i$ 가 일차독립임을 뜻한다. ■ 

- 4 에서 5 를 도출하는 증명

    4) 를 가정하면 5) 가 바로 나온다.

- 5 에서 1 을 도출하는 증명

    문제 1.4-14 에 의하여 다음이 성립한다.

    $$ \begin{equation}\begin{split}
    \mathbf{V} &= \text{span} (\gamma _1 \cup \gamma _2 \cup \dots \cup \gamma _k) \\
    &= \text{span} (\gamma _1) + \text{span} (\gamma _2) + \dots + \text{span} (\gamma _k) = \sum_{i=1}^{k}\mathbf{W} _i\\
    \end{split}\end{equation} \tag*{}
    $$

    어떤 $j$ 와 영이 아닌 벡터 $v \in \mathbf{V}$ 에 대하여 $v \in \mathbf{W} _j \cap \displaystyle \sum_{i \neq j}^{}\mathbf{W} _i$ 를 가정하면 $v \in \mathbf{W} _j = \text{span} (\gamma _j) \land v \in \displaystyle \sum_{i \neq j}^{}\mathbf{W} _i = \text{span} \bigg (\bigcup_{i \neq j}^{}\gamma i\bigg )$ 이다. 따라서 $v$ 는 $\gamma _j$ 와 $\displaystyle \bigcup_{i \neq j}^{}\gamma _i$ 의 자명하지 않은 일차결합이다. 그러므로 $v$ 를 $\displaystyle \bigcup_{i=1}^{k}\gamma _i$ 의 일차결합으로 표현하는 방식이 유일하지 않다. 이는 [정리 1.8](../VectorSpace/#8a514fc5c) 에 의하여 모순이다. 따라서 $\mathbf{W} _j \cap \displaystyle \sum_{i \neq j}^{}\mathbf{W} _i = \{0\}$ 이다. ■ 

!!! tldr "정리 5.10"

    유한차원 벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 가 대각화가능인 것과 $\mathbf{V}$ 가 $\mathbf{T}$ 의 고유공간의 직합인 것은 동치이다.

- 증명

    $\mathbf{T}$ 의 서로 다른 고윳값을 $\lambda _1, \lambda _2, \dots , \lambda _k$ 라 하자. 
    
    $\mathbf{T}$ 가 대각화가능임을 가정하자. 각 $i$ 에 대한 고유공간 $\mathbf{E}_{\lambda_i}$ 의 순서기저를 $\gamma _i$ 라 하자. [정리 5.8](#7050c2a83) 은 $\bigcup_{}^{}\gamma _i$ 가 $\mathbf{V}$ 의 기저임을 말해준다. 이로써 정리 5.9 의 4) 가 충족된다. 정리 5.9 의 1) 은 4) 와 진리값이 같으므로 $\mathbf{V} = \bigoplus_{}^{}\mathbf{E}_{\lambda_i}$ 이다. ▲ 

    $\mathbf{V}$ 가 $\mathbf{T}$ 의 고유공간의 직합임을 가정하자. 각 $i$ 에 대하여 $\mathbf{E}_{\lambda_i}$ 의 순서기저 $\gamma _i$ 가 존재한다. 정리 5.9 의 1) 이 참이므로 4) 도 참이 되어 $\bigcup_{}^{}\gamma _i$ 는 $\mathbf{V}$ 의 기저가 된다. 이 기저는 $\mathbf{T}$ 의 고유벡터로 이루어진 기저이므로 $\mathbf{T}$ 는 대각화가능하다. ■ 

- 예시 

    벡터공간 $\R ^{5}$ 에 부분공간 $\mathbf{W} = \{(x_1, x_2, x_3, x_4, x_5) : x_5 = 0\}, \mathbf{W}_1 = \{(a, b, 0, 0, 0) : a, b \in \R\}, \mathbf{W}_2 = \{(0, 0, c, 0, 0) : c \in \R\}, \mathbf{W}_3 = \{(0, 0, 0, d, 0) : d \in \R\}$ 이 존재한다. $(a, b, c, d, 0) \in \mathbf{W}$ 에 대하여 다음이 성립한다. 

    $$ (a, b, c, d, 0) = (a, b, 0, 0, 0) + (0, 0, c, 0, 0) + (0, 0, 0, d, 0) \in \mathbf{W} _1 +\mathbf{W} _2 +\mathbf{W} _3 $$

    $$ \mathbf{W} _1 \cap (\mathbf{W} _2 + \mathbf{W} _3) = \mathbf{W} _2 \cap (\mathbf{W} _1 + \mathbf{W} _3) = \mathbf{W} _3 \cap (\mathbf{W} _1 + \mathbf{W} _2) =\{0\} $$

    그러므로 $\mathbf{W} = \displaystyle \bigoplus_{i=1}^{3}\mathbf{W} _i$ 이다.

    벡터공간 $\R ^{4}$ 의 선형연산자 $\mathbf{T} (a, b, c, d) = (a, b, 2c, 3d)$ 에 대하여 $\mathbf{T}$ 가 대각화가능이고 고윳값 $1, 2, 3$ 을 갖는다는 것을 알 수 있다. 이때 각 고윳값에 대응하는 고유공간들이 각각 $\mathbf{W} _1, \mathbf{W} _2, \mathbf{W} _3$ 와 같음을 알 수 있다. 이때 정리를 사용하면 $\R ^{4} = \mathbf{W} _1 \oplus \mathbf{W} _2 \oplus \mathbf{W} _3$ 임을 알 수 있다.

# Invariant Subspace

!!! tldr "$\mathbf{T}$-불변 부분공간($\mathbf{T}$-invariant subspace)"

    벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 와 $\mathbf{V}$ 의 부분공간 $\mathbf{W}$ 에 대하여 $\mathbf{T} (\mathbf{W} ) \subseteq \mathbf{W}$ 인 $\mathbf{W}$ 를 $\mathbf{V}$ 의 $\mathbf{T}$-불변 부분공간이라 한다.

- 즉, $\forall v \in \mathbf{W} : \mathbf{T} (v) \in \mathbf{W}$ 이면 $\mathbf{W}$ 가 $\mathbf{V}$ 의 $\mathbf{T}$-불변 부분공간이라는 것이다.

    쉽게 말해, 부분공간의 원소가 $\mathbf{T}$ 를 통과해서 나왔는데도 부분공간에 속했으면 $\mathbf{T}$-불변이다.

- 예시 

    벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 에 대하여 다음의 부분공간들이 $\mathbf{T}$-불변임을 확인해보자.

    $\{0\}$:

    [선형변환의 성질](../LinearTransformation/#841cc7807) 에 의하여 $\mathbf{T} (0) = 0 \in \{0\}$ 이므로 $\{0\}$ 는 $\mathbf{T}$-불변이다.

    $\mathbf{V}$:

    선형연산자 $\mathbf{T} : \mathbf{V} \to \mathbf{V}$ 의 공역이 $\mathbf{V}$ 이므로 $\mathbf{T} (\mathbf{V} ) \subset \mathbf{V}$ 이다. 따라서 $\mathbf{V}$ 는 $\mathbf{T}$-불변이다.

    $\mathbf{R} (\mathbf{T})$:

    $\mathbf{R} (\mathbf{T}) \subset \mathbf{V}$ 인 $\mathbf{V}$ 에 대하여 $\mathbf{T} (\mathbf{V} ) = \mathbf{R} (\mathbf{T})$ 이다. 따라서 $\mathbf{T} (\mathbf{R} (\mathbf{T}) ) \subset \mathbf{T} (\mathbf{V} ) = \mathbf{R} (\mathbf{T})$ 이다.

    $\mathbf{N} (\mathbf{T})$:

    $\mathbf{T} (\mathbf{N} (\mathbf{T}) ) = \{0\}$ 이므로 $\mathbf{T} (\mathbf{N} (\mathbf{T}) ) = \{0\} \subset \mathbf{N} (\mathbf{T})$ 이다.

    $\mathbf{T}$ 의 고윳값 $\lambda$ 에 대한 $\mathbf{E}_{\lambda}$:

    $x \in \mathbf{E}_{\lambda}$ 에 대하여 $\mathbf{T} (x) = \lambda x$ 이다. $\mathbf{T} (\lambda x) = \lambda \mathbf{T} (x) = \lambda \cdot \lambda x$ 이다. 벡터공간은 스칼라곱에 닫혀있으므로 $\lambda x \in \mathbf{V}$ 이다. 따라서 $\lambda x \in \mathbf{V} \implies \lambda x \in \mathbf{E}_{\lambda}$ 이다. 따라서 $\mathbf{T} (\mathbf{E}_{\lambda} ) \subset \mathbf{E}_{\lambda}$ 이다.

## $\mathbf{T}$-cyclic subspace

!!! tldr "$\mathbf{T}$-순환 부분공간($\mathbf{T}$-cyclic subspace)"

    벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 와 영이 아닌 벡터 $x \in \mathbf{V}$ 에 대하여 다음과 같은 부분공간 $\mathbf{W}$ 를 $x$ 에 의해 생성된 $\mathbf{V}$ 의 $\mathbf{T}$-순환 부분공간이라 한다.

    $$ \mathbf{W} = \text{span} (\{x, \mathbf{T} (x), \mathbf{T} ^{2}(x), \dots \}) $$

- 문제 5.4-31 은 순환 부분공간으로 행렬식 없이 선형연산자의 특성다항식을 구하는 방법을 말해준다.

- 순환 부분공간은 대각화 불가능한 선형연산자의 행렬표현을 다룰 때 매우 중요한 역할을 한다.

- 예시 

    $\R ^{3}$ 의 선형연산자 $\mathbf{T}$ 를 $\mathbf{T}(a,b,c)=(-b+c,a+c,3c)$ 라고 정의하고 $e_1 = (1, 0, 0)$ 에 의해 생성된 $\mathbf{T}$-순환 부분공간을 구해보자. 다음이 성립한다.

    $$\mathbf{T}(e_1) = \mathbf{T}(1,0,0) = (0, 1,0) = e_2$$

    $$\mathbf{T}^{2}(e_1) = \mathbf{T}(\mathbf{T}(e_1)) = \mathbf{T}(e_2) = (-1,0,0) = -e_1 $$

    그러므로 $e_1$ 에 의해 생성된 $\mathbf{T}$-순환 부분공간은 다음과 같다.

    $$ \text{span} (\{e_1, \mathbf{T}(e_1), \mathbf{T}^{2}(e_1), \dots\}) = \text{span} (\{e_1, e_2\}) = \{(s, t, 0) : s, t \in \R\} $$

!!! tldr "문제 5.4-11"

    벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 와 영이 아닌 벡터 $v \in \mathbf{V}$, $v$ 에 의해 생성된 $\mathbf{V}$ 의 $\mathbf{T}$-순환 부분공간 $\mathbf{W}$ 에 대하여 다음이 성립한다.

    1. $\mathbf{W}$ 는 $\mathbf{T}$-불변이다.

    2. $v$ 를 포함하는 $\mathbf{V}$ 의 임의의 $\mathbf{T}$-불변 부분공간은 $\mathbf{W}$ 를 포함한다.

- 이 정리는 $\mathbf{T}$-순환 부분공간이 $\mathbf{T}$-불변임을 말해준다.

- 이 정리는 $x$ 를 포함하는 $\mathbf{T}$-불변 부분공간이 반드시 $x$ 에 의해 생성된 $\mathbf{T}$-순환 부분공간을 포함함을 말해준다. 즉, $\mathbf{T}$-순환 부분공간은 $x$ 를 포함하는 가장 작은 $\mathbf{T}$-불변 부분공간이다.

    가령 벡터공간 $\mathbf{V}$ 의 $x$ 를 포함하는 $\mathbf{T}$-불변 부분공간 $\mathbf{W}_1, \mathbf{W}_2, \dots, \mathbf{W}_n$ 과 $x$ 에 의해 생성된 $\mathbf{T}$-순환 부분공간 $\mathbf{Z}$ 를 가정하면 다음이 성립한다. 

    $$ \mathbf{Z} \subset \mathbf{W}_1, \mathbf{Z} \subset \mathbf{W}_2, \dots, \mathbf{Z} \subset \mathbf{W}_n $$

    이는 [정리 1.11](../VectorSpace/#26f9238cb) 와 그 따름정리에 의해 $\mathbf{Z}$ 의 기저가 다른 모든 $\mathbf{T}$-불변 부분공간의 기저에 포함됨을 뜻한다. 따라서 $\mathbf{T}$-순환 부분공간은 가장 작은 $\mathbf{T}$-불변 부분공간이 된다.

- 증명

    집합 $\beta = \{v, \mathbf{T}(v), \mathbf{T}^{2}(v), \dots\}$ 가 $\mathbf{W}$ 를 생성한다. 다음을 만족하는 무한한 스칼라 $a_0, a_1, a_2, \dots$ 가 존재한다.

    $$ x \in \mathbf{W} \implies x = a_0v + a_1 \mathbf{T}(v) + a_2 \mathbf{T}^{2}(v) + \dots $$

    $$ \implies \mathbf{T}(x) = a_0 \mathbf{T}(v) + a_1 \mathbf{T}^{2}(v) + a_2 \mathbf{T}^{3}(v) + \dots $$

    $\mathbf{T}(x)$ 는 $\beta$ 에 의한 일차결합이므로 $\mathbf{T}(x) \in \mathbf{W}$ 이다. 따라서 $\mathbf{W}$ 는 $\mathbf{T}$-불변이다. ▲ 

    $\mathbf{T}$-불변 부분공간 $\mathbf{Z}$ 가 $v \in \mathbf{Z}$ 를 만족하면 다음이 성립한다.

    $$ v \in \mathbf{Z} \implies \mathbf{T}(v) \in \mathbf{Z} \implies \mathbf{T}^{2}(v) \in \mathbf{Z} \implies \dots $$

    그러므로 $\beta \subset  \mathbf{Z}$ 이다. $\mathbf{Z}$ 가 $\mathbf{W}$ 의 기저를 포함하므로 $\mathbf{W}$ 의 모든 벡터는 $\mathbf{Z}$ 에 포함된다. 즉, $\mathbf{W} \subset \mathbf{Z}$ 이다. ■ 

## restriction

!!! tldr "제한(restriction)"

    벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}:\mathbf{V} \to \mathbf{V}$ 와 $\mathbf{T}$-불변 부분공간 $\mathbf{W}$ 에 대하여 $\mathbf{T}$ 를 $\mathbf{W}$ 로 제한한 $\mathbf{T}_{\mathbf{W}}$ 는 $\mathbf{T}$ 의 정의역과 공역을 $\mathbf{W}$ 로 제한한 함수 $\mathbf{T}_{\mathbf{W}}:\mathbf{W}\to \mathbf{W}$ 이다.

- 함수의 제한은 정의역만 축소시키는 것으로 정의되지만, 이 경우 정의역이 $\mathbf{T}$-불변 부분공간으로 축소되므로 공역도 어차피 $\mathbf{T}$-불변 부분공간으로 축소된다.

- $\mathbf{T}_{\mathbf{W}}$ 는 선형변환이다.(문제 5.4-7) 즉, $\mathbf{T}_{\mathbf{W}}$ 는 $\mathbf{W}$ 의 선형연산자이다.

- $\mathbf{T}_{\mathbf{W}}$ 는 $\mathbf{T}$ 의 성질을 그대로 상속한다.

!!! tldr "문제 5.4-12"

    유한차원 벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 와 $\mathbf{T}$-불변 부분공간 $\mathbf{W}$ 에 대한 $\mathbf{T}_{\mathbf{W}}$ 의 순서기저 $\gamma = \{v_1, v_2, \dots, v_k\}$ 를 확장하여 $\mathbf{V}$ 의 순서기저 $\beta = \{v_1, v_2, \dots, v_k, v _{k+1}, \dots, v_n\}$ 을 만들고 $A = [\mathbf{T}]_{\beta }, B_1 = [\mathbf{T}_{\mathbf{W}}]_{\gamma }$ 로 두자.

    영행렬 $O$ 에 대하여 다음이 성립한다.

    $$ A = \begin{pmatrix} B_1&B_2\\ O&B_3\\ \end{pmatrix} $$

- 증명

    $i \in \{1, \dots, k\}$ 에 대하여 $A$ 의 $i$ 열은 다음과 같다. 

    $$ \mathbf{T}(v_i) = \sum_{i=1}^{n}a _{ij}v_i \in \mathbf{W} $$

    $v_i \in \mathbf{W}$ 이므로 $\mathbf{T}(v_i) \in \mathbf{W}$ 이다. 만약 $\sum_{i=k+1}^{n}a _{ij}v_i \neq 0$ 이면 $\mathbf{T}(v_i)$ 를 $\mathbf{W}$ 의 기저로 표현하는 것이 불가능하므로 $\mathbf{T}(v_i) \not\in \mathbf{W}$ 이다. 이는 모순이다. 따라서 $\sum_{i=k+1}^{n}v_i = 0$ 이다. 그러므로 $A$ 의 $i$ 열은 다음과 같다.

    $$ \mathbf{T}(v_i) = \sum_{i=1}^{k}a _{ij}v_i $$

    이로써 모든 증명이 끝났다. ■ 

!!! tldr "정리 5.20"

    유한차원 벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 와 $\mathbf{T}$-불변 부분공간 $\mathbf{W}$ 에 대한 $\mathbf{T}_{\mathbf{W}}$ 의 특성다항식은 $\mathbf{T}$ 의 특성다항식을 나눈다.

- 이 정리는 선형연산자와 $\mathbf{T}$-불변 부분공간에 의한 제한과의 관계를 말해준다.

- 증명

    $\mathbf{W}$ 의 순서기저를 $\gamma = \{v_1, v_2, \dots, v_k\}$ 라 하면 $\gamma$ 를 확장하여 $\mathbf{V}$ 의 순서기저 $\beta = \{v_1, v_2, \dots, v_k, v _{k+1}, \dots, v_n\}$ 을 만들 수 있다. $A = [\mathbf{T}]_{\beta }, B_1 = \{\mathbf{T}_{\mathbf{W}}\}_{\gamma }$ 라 하면 문제 5.4-12 에 의하여 다음이 성립한다. 

    $$ A = \begin{pmatrix} B_1&B_2\\ O&B_3\\ \end{pmatrix} $$

    $\mathbf{T}$ 의 특성다항식 $f(t)$, $\mathbf{T}_{\mathbf{W}}$ 의 특성다항식 $g(t)$ 에 대하여 [문제 4.3-21](../Determinants/#48155e536) 에 의하여 다음이 성립한다. 

    $$ f(t) = \det(A - tI_n) = \det \begin{pmatrix} B_1-tI_k&B_2\\ O&B_3-tI _{n-k}\\ \end{pmatrix} = g(t) \det(B_3-tI _{n-k}) $$

    따라서 $g(t)$ 는 $f(t)$ 를 나눈다. ■ 

!!! tldr "문제 5.4-19"

    스칼라 $a_0, a_1, \dots, a _{k-1} \in \mathbf{F}$ 와 다음과 같이 정의된 행렬 $A \in \mathbf{M}_{k \times k}(\mathbf{F})$ 의 특성다항식은 $(-1) ^{k}(a_0+ a_1t+ \dots + a _{k-1}t^{k-1} + t ^{k})$ 이다.

    $$ A= \begin{pmatrix} 0&0&\dots&0&-a_0\\ 1&0&\dots&0&-a_1\\ 0&1&\dots&0&-a_2\\ \vdots& \vdots& \ddots& \vdots& \vdots \\ 0&0&\dots&1&-a _{k-1}\\ \end{pmatrix} $$

- 증명

    $k = 2$ 을 가정하면 $A = \begin{pmatrix} 0&-a_0\\ 1&-a_1\\ \end{pmatrix}$ 이다. 다음이 성립한다. 
    
    $$f(t) = \det(A - tI_2) = \det \begin{pmatrix} -t&-a_0\\ 1&-a_1-t\\ \end{pmatrix} = t(a_1+t) + a_0 = (-1) ^{2}(a_0 + a_1t + t ^{2}) \tag*{▲} $$

    $k-1$ 에서 정리가 성립함을 가정하고 $k$ 에서 정리가 성립함을 증명하자. $B = A - tI_k$ 로 두면 $A \in \mathbf{M}_{k \times k}(\mathbf{F})$ 의 특성다항식은 다음과 같다.

    $$ \begin{equation}\begin{split} \det(B) &= \det \begin{pmatrix} -t&0&\dots&0&-a_0\\ 1&-t&\dots&0&-a_1\\ 0&1&\dots&0&-a_2\\ \vdots& \vdots& \ddots& \vdots& \vdots \\ 0&0&\dots&1&-a _{k-1}-t\\ \end{pmatrix} \\ &= (-1)^{1 + 1}B _{11} \det(\tilde{B}_{11})  + (-1) ^{1 + k}B _{1k}\det(\tilde{B}_{1k}) \\ &= -t \det(\tilde{B}_{11})  + (-1) ^{1 + k}\cdot (-a_0) \cdot 1 \\ \end{split}\end{equation} \tag*{} $$

    $\tilde{B}_{11}$ 은 $\tilde{A}_{11}$ 의 특성다항식이다.  $k-1$ 에서 정리가 성립하므로 $\det(\tilde{B}_{11})$ 은 적절한 스칼라 $b_0, b_1, \dots, b_{k-1} \in \mathbf{F}$ 에 대하여 $(-1) ^{k-1}(b_0+ b_1t+ \dots + b_{k-2}t^{k-2} + t ^{k-1})$ 이다. 따라서 다음이 성립한다.

    $$ \begin{equation}\begin{split} \det(A - tI_k) &= -t \cdot (-1) ^{k-1}(b_0+ b_1t+ \dots + b_{k-2}t^{k-2} + t ^{k-1}) + (-1) ^{k}\cdot a_0 \\ &= (-1) ^{k}(b_0t+ b_1t ^{2}+ \dots + b_{k-2}t^{k-1} + t ^{k}) + (-1) ^{k}\cdot a_0 \\ &= (-1) ^{k}(a_0 + b_0t+ b_1t ^{2}+ \dots + b_{k-2}t^{k-1} + t ^{k}) \\ &= (-1) ^{k}(a_0 + a_1t+ a_2t ^{2}+ \dots + a_{k-1}t^{k-1} + t ^{k}) \\ \end{split}\end{equation} \tag*{} $$

    단순히 $b_i = a _{i+1}$ 로 선택하면 위와 같은 결론을 얻을 수 있다. 정리가 임의의 스칼라들에 대하여 성립하므로 이렇게 선택해도 괜찮다. ■ 

!!! tldr "정리 5.21"

    유한차원 벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 와 영이 아닌 벡터 $v \in \mathbf{V}$ 에 의해 생성된 $\mathbf{T}$-순환 부분공간 $\mathbf{W}$ 에 대하여 $k = \dim (\mathbf{W})$ 이면 다음이 성립한다. 

    1. $\{v, \mathbf{T}(v), \dots, \mathbf{T}^{k-1}(v)\}$ 는 $\mathbf{W}$ 의 기저이다. 

    2. 스칼라 $a_0, a_1, \dots, a _{k-1}$ 에 대하여 $a_0v + a_1 \mathbf{T}(v) + \dots + a _{k-1}\mathbf{T}^{k-1}(v)+\mathbf{T}^{k}(v) = 0$ 이면 $\mathbf{T}_{\mathbf{W}}$ 의 특성다항식은 $f(t) = (-1)^{k}(a_0+a_1t+\dots+a _{k-1}t ^{k-1}+t ^{k})$ 이다.

- 정리 5.20 은 $\mathbf{T}_{\mathbf{W}}$ 의 특성다항식으로 $\mathbf{T}$ 의 특성다항식의 정보를 얻게 해준다. 이 정리는 $\mathbf{T}_{\mathbf{W}}$ 의 특성다항식을 쉽게 얻게 해준다는 관점에서 순환 부분공간의 유용함을 증명해준다.

    - 1) 는 $\mathbf{T}$-순환 부분공간을 정의하기 위하여 사용된 생성집합

        $$ \text{span} (\{v, \mathbf{T} (v), \mathbf{T} ^{2}(v), \dots \}) $$

        에서 $\mathbf{T}^{k}(v)$ 이상의 것들은 불필요함을 알려준다. 또한 $\mathbf{T}$-순환 부분공간의 기저를 쉽게 알 수 있는 방법을 알려준다.

    - 2) 는 $\mathbf{T}_{\mathbf{W}}$ 의 특성다항식을 쉽게 구하는 방법을 알려준다. 즉 $\mathbf{T}^{k}(v)$ 를 기저로 표현하는 일차결합의 계수만 알아내면 특성다항식을 바로 구할 수 있다는 것이다. 너무 자명하지만, 이 일차결합 표현은 반드시 존재한다.

- 증명

    $v \neq 0$ 이므로 $\{v\}$ 는 일차독립이다. $\beta = \{v, \mathbf{T}(v), \dots, \mathbf{T}^{j-1}(v)\}$ 가 일차독립이 되게 하는 가장 큰 자연수 $j$ 가 존재한다. $\mathbf{V}$ 가 유한차원이므로 유한한 기저보다 기수가 작은 일차독립 집합들이 존재하기 때문이다. 

    $\mathbf{Z}=\text{span} (\beta )$ 로 두면 $\beta$ 는 $\mathbf{Z}$ 의 기저이다. $j$ 가 $\beta$ 를 일차독립이 되게 하기 위한 마지막 자연수이므로 $j+1$ 에 대하여 일차종속이 되므로 $\beta$ 의 일차결합으로 $\mathbf{T}^{j}(v)$ 를 표현할 수 있다. 따라서 [정리 1.7](VectorSpace/#97eff1e4d) 의 세번째 명제에 의하여 $\mathbf{T}^{j}(v) \in \mathbf{Z}$ 이다.

    $w \in \mathbf{Z}$ 이면 $w = b_0v + b_1 \mathbf{T}(v) + \dots + b_{j-1}\mathbf{T}^{j-1}(v)$ 인 스칼라 $b_0, b_1, \dots, b _{j-1}$ 가 존재한다. 이 식에 $\mathbf{T}$ 를 씌우면 다음과 같다. 

    $$ \mathbf{T}(w) = b_0 \mathbf{T}(v) + b_1 \mathbf{T}^{2}(v) + \dots + b _{j-1} \mathbf{T}^{j}(v) $$

    $\mathbf{T}(w)$ 는 $\mathbf{Z}$ 의 기저의 일차결합이므로 $\mathbf{T}(w) \in \mathbf{Z}$ 이다. 따라서 $\mathbf{Z}$ 는 $\mathbf{T}$-불변이다. 문제 5.4-11 에 의하여 $\mathbf{W}$ 는 $v$ 를 포함하는 가장 작은 $\mathbf{T}$-불변 부분공간이므로 $\mathbf{W}\subset \mathbf{Z}$ 이다.

    그런데 $\mathbf{Z}$ 의 생성집합 $\beta$ 가 $\mathbf{W}$ 의 생성집합에 포함되므로 자명하게 $\mathbf{Z}\subset \mathbf{W}$ 이다. 따라서 $\mathbf{Z} = \mathbf{W}$ 이다. 그러므로 $\beta$ 는 $\mathbf{W}$ 의 기저이고 $\dim (\mathbf{W})=j=k$ 이다. ▲ 

    이제 $\beta = \{v, \mathbf{T}_{\mathbf{W}}(v), \dots, \mathbf{T}_{\mathbf{W}}^{k-1}(v)\}$ 가 $\mathbf{W}$ 의 순서기저임을 가정할 수 있다. $[\mathbf{T}_{\mathbf{W}}]_{\beta }$ 는 다음과 같다. 

    $$ \mathbf{T}_{\mathbf{W}}(v) = 1 \cdot \mathbf{T}_{\mathbf{W}}(v) $$

    $$ \mathbf{T}_{\mathbf{W}}(\mathbf{T}_{\mathbf{W}}(v)) = 1 \cdot \mathbf{T}_{\mathbf{W}}^{2}(v) $$

    $$ \mathbf{T}_{\mathbf{W}}(\mathbf{T}_{\mathbf{W}}^{k-2}(v)) = 1 \cdot \mathbf{T}_{\mathbf{W}}^{k-1}(v) $$

    $$ \mathbf{T}_{\mathbf{W}}(\mathbf{T}_{\mathbf{W}}^{k-1}(v)) = \mathbf{T}_{\mathbf{W}}^{k}(v) = -a_0v - a_1 \mathbf{T}(v) - \dots - a _{k-1}\mathbf{T}^{k-1}(v) $$

    $$ \implies [\mathbf{T}_{\mathbf{W}}]_{\beta } = \begin{pmatrix} 0&0&\dots&0&-a_0\\ 1&0&\dots&0&-a_1\\ \vdots& \vdots& \ddots& \vdots&\vdots  \\ 0&0&\dots&1&-a _{k-1}\\ \end{pmatrix} $$

    문제 5.4-19 에 의하여 $[\mathbf{T}_{\mathbf{W}}]_{\beta }$ 의 특성다항식은 $f(t) = (-1)^{k}(a_0+a_1t+\dots+a _{k-1}t ^{k-1}+t ^{k})$ 이다. 선형연산자의 특성다항식은 선형연산자의 행렬표현의 특성다항식으로 정의되므로 증명이 끝났다. ■ 

## Cayley-Hamilton theorem

!!! tldr ""

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

!!! tldr "정리 5.22 케일리-해밀턴 정리(Cayley-Hamilton theorem)"

    유한차원 벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 와 $\mathbf{T}$ 의 특성다항식 $f(t)$ 에 대하여 $f(\mathbf{T}) = \mathbf{T}_0$ 이다.

- 이 정리는 정리 5.21 의 중요성을 보여준다. 왜냐하면 이 정리가 널리 사용되기 때문이다.

- 증명

    $\forall v \in \mathbf{V}: f(\mathbf{T})(v) = 0$ 을 보이면 된다. $v = 0$ 를 가정하면 $f(\mathbf{T})$ 가 선형이므로 증명할 것이 없다. ▲ 

    $v \neq 0$ 을 가정하자. $v$ 에 의해 생성된 $\mathbf{T}$-순환 부분공간 $\mathbf{W}$ 를 가정하고 $\dim (\mathbf{W}) = k$ 로 두면 정리 5.21 의 첫번째 명제에 의하여 다음을 만족하는 스칼라 $a_0, a_1, a_2, \dots, a _{k-1}$ 가 존재한다. 

    $$ a_0v + a_1 \mathbf{T}(v) + \dots + a _{k-1}\mathbf{T}^{k-1}(v) + \mathbf{T}^{k}(v) = 0 $$

    정리 5.21 의 두번째 명제에 의하여 $\mathbf{T}_{\mathbf{W}}$ 의 특성다항식은 다음과 같다. 

    $$ g(t) = (-1)^{k}(a_0 + a_1t+ \dots+ a _{k-1}t ^{k-1}+t ^{k}) $$

    따라서 다음이 성립한다. 

    $$ g(\mathbf{T})(t) = (-1)^{k}(a_0 \mathbf{I} + a_1 \mathbf{T}+ \dots+ a _{k-1} \mathbf{T} ^{k-1}+\mathbf{T}^{k})(v) = 0 $$

    [정리 5.20](#3d097218e) 은 $g(t)$ 가 $f(t)$ 나눈다는 것을 알려준다. 즉, 다음이 성립한다. 

    $$ f(\mathbf{T})(v) = q(\mathbf{T})g(\mathbf{T})(v) = q(\mathbf{T})(g(\mathbf{T})(v)) = q(\mathbf{T})(0)=0 $$

    따라서 $f(\mathbf{T}) = \mathbf{T}_0$ 이다. ■ 

- 예시 

    $\R ^{2}$ 의 선형연산자 $\mathbf{T}(a,b)=(a+2b, -2a+b)$ 와 $\mathbf{T}$ 의 특성다항식 $f(t) = \det([\mathbf{T}]_{\beta }-tI) = \det \begin{pmatrix} 1-t&2\\ -2&1-t\\ \end{pmatrix}=t ^{2}-2t+5$ 에 대하여 $f(\mathbf{T}) = \mathbf{T}^{2}-2 \mathbf{T}+5 \mathbf{I} = \mathbf{T}_0$ 이다.

!!! tldr "정리 5.22 따름정리"

    $n \times n$ 행렬 $A$ 와 그 특성다항식 $f(t)$ 에 대하여 $f(A) = O$ 이다.

- 증명

## Invariant subspace and Direct sum 

!!! tldr "정리 5.23"

    유한차원 벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 와 $i \in \{1,\dots,k\}$ 에 대하여 $\mathbf{W}_i$ 가 $\mathbf{T}$-불변이고 $\mathbf{V} = \displaystyle \bigoplus_{i=1}^{k}\mathbf{W}_i$ 가 성립함을 가정하자.

    $\mathbf{T}_{\mathbf{W}_i}$ 의 특성다항식 $f_i(t)$ 에 대하여 $f_1(t) \cdot f_2(t) \cdot \dots \cdot f_k(t)$ 는 $\mathbf{T}$ 의 특성다항식이다.

- 유한차원 벡터공간 $\mathbf{V}$ 가 주어지면 이 공간을 가능한 많은 $\mathbf{T}$-불변 부분공간의 직합으로 분해하는 것이 좋다. $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 의 행동을 직합을 구성하는 각각의 부분공간에서 추론할 수 있기 때문이다. 가령 $\mathbf{T}$ 가 대각화가능한 것과 $\mathbf{V}$ 가 1차원 $\mathbf{T}$-불변 부분공간의 직합으로 완전히 분해되는 것은 동치이다.

- $\mathbf{T}$ 가 유한차원 벡터공간 $\mathbf{V}$ 의 대각화가능한 선형연산자이고 서로 다른 고윳값을 $\lambda _1, \lambda _2, \dots, \lambda _k$ 로 두면 [정리 5.10](#fbcd60c9f) 에 의하여 $\mathbf{V}$ 는 $\mathbf{T}$ 의 고유공간의 직합이다. 즉, $\mathbf{V}= \displaystyle \bigoplus_{i=1}^{k}\mathbf{E}_{\lambda_i}$ 이다. [불변 부분공간](#2fec2004a) 의 예시에서 고유공간은 $\mathbf{T}$-불변임을 증명했었다. 따라서 각 고유공간들은 정리 5.23 의 가정을 충족시킨다.

    [정리 5.8](#7050c2a83) 에 의하여 $\dim (\mathbf{E}_{\lambda_i} ) = m_i$ 는 $\lambda _i$ 의 중복도와 같다는 사실과 [정리 5.6](#867268fd3) 에 의하여 $\mathbf{T}$ 의 특성다항식 $f(t)$ 은 스칼라 $a$ 에 대하여 다음과 같이 완전히 인수분해된다. 

    $$ f(t) = a \prod_{i=1}^{k}(t - \lambda _i) ^{m_i} $$

    우리가 이미 잘 알고 있었던 이 결과를 본 정리를 통하여 다시 도출해보자.  각 고윳값 $\lambda _i$ 에 대하여 제한 $\mathbf{T}_{\mathbf{E}_{\lambda_i} }$ 을 만들면 이것의 특성다항식은 $(\lambda _i -t) ^{m_i}$ 이다. 본 정리에 의하여 $\mathbf{T}$ 의 특성다항식은 다음과 같다.

    $$ f(t) = (\lambda _1 - t) ^{m_1} (\lambda _2 - t) ^{m_2} \dots (\lambda _k - t) ^{m_k} $$

- 증명

    $\mathbf{T}$ 의 특성다항식을 $f(t)$ 라고 하자. 
    
    $k = 2$ 일 때 $\mathbf{W}_1$ 의 순서기저를 $\beta _1$, $\mathbf{W}_2$ 의 순서기저를 $\beta _2$ 라 하고 $\beta = b_1 \cup b_2$ 로 두자. [정리 5.9(4)](#748907edc) 에 의하여 $\beta$ 는 $\mathbf{V}$ 의 순서기저이다. $A = [\mathbf{T}]_{\beta }, B_1 = [\mathbf{T}_{\mathbf{W}_1}]_{\beta _1}, B_2 = [\mathbf{T}_{\mathbf{W}_2}]_{\beta _2}$ 로 두면 정리 5.24 에 의하여 $A = \begin{pmatrix}
    B_1&O\\
    O'&B_2\\
    \end{pmatrix}$ 이다. [정리 5.20](#3d097218e) 의 증명과정에서처럼 $f(t)$ 를 다음과 같이 전개할 수 있다.

    $$ f(t) = \det(A - tI) = \det(B_1-tI) \det(B_2-tI) = f_1(t) \cdot f_2(t) $$

    따라서 $k=2$ 일 때 정리가 참이다. ▲ 

    $k-1 \geq 2$ 인 $k-1$ 에 대하여 정리가 성립함을 가정하고 $k$ 에 대하여 성립함을 보이자. $\mathbf{W} = \displaystyle \bigoplus_{i=1}^{k}\mathbf{W}_i$ 로 두면 $\mathbf{W}$ 가 $\mathbf{T}$-불변이고 $\mathbf{V}= \mathbf{W}\oplus \mathbf{W}_k$ 임은 자명하다. $k = 2$ 일 때를 가정할 수 있으므로 $\mathbf{T}_{\mathbf{W}}$ 의 특성다항식 $g(t)$ 에 대하여 $f(t) = g(t) \cdot f_k(t)$ 이다. $k-1$ 에서 정리가 성립하므로 $g(t) = f_1(t) \cdot f_2(t) \cdot \dots \cdot f _{k-1}(t)$ 이다. 그러므로 다음이 성립한다. 

    $$ \therefore f(t) = g(t) \cdot f_k(t) = f_1(t) \cdot f_2(t) \cdot \dots \cdot f_k(t) \tag*{■} $$

    - 정리 5.23 은 드물게 이후의 정리인 5.24 를 기반으로 증명되는데, 5.24 가 5.23 을 가정하지 않으므로 순환논리가 되지는 않는다. 즉, 논리적으로 문제는 없다.

    - 원래 증명에서는 $\mathbf{W} = \displaystyle \sum_{i=1}^{k-1}\mathbf{W}_i$ 로 두는데 $\mathbf{V}= \displaystyle \bigoplus_{i=1}^{k}\mathbf{W}_i$ 라는 가정이 $i, j \in \{1, \dots, k-1\}$ 에 대하여 $\mathbf{W}_j \cap \displaystyle \sum_{i \neq j}\mathbf{W}_i = \{0\}$ 를 함의한다고 생각해서 그냥 $\mathbf{W} = \displaystyle \bigoplus_{i=1}^{k-1}\mathbf{W}_i$ 로 바꿨다.

- 예시 

    $\R ^{4}$ 의 선형연산자 $\mathbf{T}(a,b,c,d,) = (2a-b,a+b,c-d,c+d)$  와 $\mathbf{W}_1=\{(s,t,0,0) : s,t \in \R\}, \mathbf{W}_2=\{(0,0,s,t) : s,t \in \R\}$ 를 정의하면 $\mathbf{W}_1, \mathbf{W}_2$  는 $\mathbf{T}$-불변이고 $\R ^{4}= \mathbf{W}_1 \oplus \mathbf{W}_2$ 이다. $\beta _1=\{e_1,e_2\},\beta _2=\{e_3,e_4\},\beta =\beta_1 \cup \beta _2$ 로 두고 각각을 $\mathbf{W}_1, \mathbf{W}_2, \R ^{4}$ 의 순서기저로 두자. $A = [\mathbf{T}]_{\beta }, B_1 = [\mathbf{T}_{\mathbf{W}_1}]_{\beta _1}, B_2= [\mathbf{T}_{\mathbf{W}_2}]_{\beta _2}$ 는 다음과 같다.

    $$ B_1 = \begin{pmatrix} 2&-1\\ 1&1\\ \end{pmatrix}, B_2 = \begin{pmatrix} 1&-1\\ 1&1\\ \end{pmatrix}, A = \begin{pmatrix} B_1&O\\ O&B_2\\ \end{pmatrix} = \begin{pmatrix} 2&-1&0&0\\ 1&1&0&0\\ 0&0&1&-1\\ 0&0&1&1\\ \end{pmatrix} $$

    $\mathbf{T}$ , $\mathbf{T}_{\mathbf{W}_1}$ , $\mathbf{T}_{\mathbf{W}_2}$ 의 특성다항식을 $f(t),f_1(t),f_2(t)$ 로 두면 다음이 성립한다.

    $$ f(t) = \det(A-tI) =\det(B_1-tI) \det(B_2-tI) =f_1(t) \cdot f_2(t) $$

!!! tldr "두 행렬의 직합(direct sum of two matrices)"

    $B_1 \in \mathbf{M}_{m \times m}(\mathbf{F}), B_2 \in \mathbf{M}_{n \times n}(\mathbf{F})$ 에 대하여 $B_1, B_2$ 의 직합은 다음과 같은 $(m + n) \times (m + n)$ 행렬 $A$ 로 정의하고 $B_1 \oplus B_2$ 로 표기한다.

    $$ A _{ij} = \begin{cases} (B_1) _{ij} & 1 \leq i, j \leq m\\ (B_2) _{(i-m),(j-m)} & m+1 \leq i, j \leq n+m\\ 0 & \text{ otherwise }\\ \end{cases} $$

- **즉, 적절한 영행렬 $O$ 에 대하여 $A = B_1 \oplus B_2 = \begin{pmatrix} B_1&O\\ O&B_2\\ \end{pmatrix}$ 라고 정의하는 것이다.**

!!! tldr "행렬의 직합(direct sum of matrices)"

    정사각행렬 $B_1, B_2, \dots, B_k$ 에 대하여 $B_1, B_2, \dots, B_k$ 의 직합은 재귀적으로 $\displaystyle \bigoplus_{i=1}^{k}B_i = \bigg (\bigoplus_{i=1}^{k-1}B_i\bigg ) \oplus B_k$ 라 정의한다.
    
- **즉, 적절한 영행렬 $O$ 에 대하여 $A = \displaystyle \bigoplus_{i=1}^{k}B_i$ 를 다음과 같이 정의하는 것이다.**

    $$ A = \displaystyle \bigoplus_{i=1}^{k}B_i = \begin{pmatrix} B_1&O&\dots&O\\ O&B_2&\dots&O\\ \vdots& \vdots& \ddots& \vdots \\ O&O&\dots&B_k\\ \end{pmatrix} $$

- 예시 

    정사각행렬 $B_1 = \begin{pmatrix} 1&2\\ 1&1\\ \end{pmatrix}, B_2 = (3), B_3 = \begin{pmatrix} 1&2&1\\ 1&2&3\\ 1&1&1\\ \end{pmatrix}$ 에 대하여 $B_1 \oplus B_2 \oplus B_3$ 는 다음과 같다.

    $$ \bigoplus_{i=1}^{3}B_i = \begin{pmatrix} 1&2&0&0&0&0\\ 1&1&0&0&0&0\\ 0&0&3&0&0&0\\ 0&0&0&1&2&1\\ 0&0&0&1&2&3\\ 0&0&0&1&1&1\\ \end{pmatrix} $$

!!! tldr "정리 5.24"

    유한차원 벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 와 $\mathbf{V}= \displaystyle \bigoplus_{i=1}^{k}\mathbf{W}_i$ 인 $\mathbf{T}$-불변 부분공간 $\mathbf{W}_1, \mathbf{W}_2, \dots, \mathbf{W}_k$ 에 대하여 각 $i$ 에 대한 $\beta _i$ 는 $\mathbf{W}_i$ 의 순서기저이고 $\beta = \displaystyle \bigcup_{i=1}^{k}\beta _i$ 라고 하고 $A = [\mathbf{T}]_{\beta }, B_i = [\mathbf{T}_{\mathbf{W}_i}]_{\beta _{i}}$ 라고 하면 다음이 성립한다.

    $$ A = \bigoplus_{i=1}^{k} B_i $$

- 이 정리가 하는 역할은 행렬의 직합을 불변 부분공간의 직합과 연관짓는것이다.

- 증명

    $k = 2$ 를 가정하자. 

    [문제 5.4-12](#d5371600a) 의 증명과정은 $\mathbf{T}$-불변 부분공간의 순서기저로 이루어진 $\mathbf{V}$ 의 기저로 $\mathbf{T}$ 를 행렬표현하면 $\mathbf{T}$-불변의 기저로 표현된 열들이 반드시 $\mathbf{T}$-불변의 기저로만 표현되어야 함을 말해준다. 즉, $\beta _1 = \{v_1, \dots, v_s\}, \beta _2 = \{v _{s+1}, \dots, v_t\}$ 를 가정하면 $\beta = \beta _1 \cup \beta _2$ 는 $\mathbf{V}$ 의 순서기저가 되고 $A = [\mathbf{T}]_{\beta }$ 는 다음과 같다.

    $$ \mathbf{T}(v_1) = \sum_{i=1}^{s}a _{i1}v_1 $$

    $$ \vdots $$

    $$ \mathbf{T}(v_s) = \sum_{i=1}^{s}a _{is}v_s $$

    $$ \mathbf{T}(v _{s+1}) = \sum_{i=s+1}^{t}a _{i,s+1}v _{s+1} $$

    $$ \vdots $$

    $$ \mathbf{T}(v _{t}) = \sum_{i=t}^{t}a _{it}v _{t} $$

    $$ \implies A = \begin{pmatrix} B_1&O\\ O&B_2\\ \end{pmatrix} $$

    이는 $A = B_1 \oplus B_2$ 을 뜻한다. ▲ 

    $k-1$ 에서 정리가 성립함을 가정하고 $k$ 에 대하여 성립함을 보이자. $\mathbf{W}=\displaystyle \bigoplus_{i=1}^{k-1}\mathbf{W}_i$ 에 대하여 $\beta ' = \displaystyle  \bigcup_{i=1}^{k-1}\beta _i$ 로 두면 다음이 성립한다.
    
    $$ [\mathbf{T}_{\mathbf{W}}]_{\beta '} = \bigoplus_{i=1}^{k-1}B_i = B' $$

    [문제 5.4-12](#d5371600a) 의 증명과정은 $\mathbf{T}$-불변 부분공간의 순서기저로 이루어진 $\mathbf{V}$ 의 기저로 $\mathbf{T}$ 를 행렬표현하면 $\mathbf{T}$-불변의 기저로 표현된 열들이 반드시 $\mathbf{T}$-불변의 기저로만 표현되어야 함을 말해준다. 즉, $\beta ' = \{v_1, \dots, v_s\}, \beta _k = \{v _{s+1}, \dots, v_t\}$ 를 가정하면 $\beta = \beta ' \cup \beta _k$ 는 $\mathbf{V}$ 의 순서기저가 되고 $A = [\mathbf{T}]_{\beta }$ 는 다음과 같다.

    $$ \mathbf{T}(v_1) = \sum_{i=1}^{s}a _{i1}v_1 $$

    $$ \vdots $$

    $$ \mathbf{T}(v_s) = \sum_{i=1}^{s}a _{is}v_s $$

    $$ \mathbf{T}(v _{s+1}) = \sum_{i=s+1}^{t}a _{i,s+1}v _{s+1} $$

    $$ \vdots $$

    $$ \mathbf{T}(v _{t}) = \sum_{i=t}^{t}a _{it}v _{t} $$

    $$ \implies A = \begin{pmatrix} B'&O\\ O&B_k\\ \end{pmatrix} $$

    이는 $A = B' \oplus B_k$ 을 뜻한다. $\displaystyle  B' = \bigoplus_{i=1}^{k-1}B_i$ 이므로 다음이 성립한다. 

    $$ \therefore A = \bigg (\bigoplus_{i=1}^{k-1}B_i\bigg ) \oplus B_k = \bigoplus_{i=1}^{k}B_i \tag*{■} $$

