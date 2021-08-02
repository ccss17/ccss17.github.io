!!! info "ref"

    Stephen H. Friedberg, Linear Algebra, 4th Edition

# Diagonalizable

!!! tldr "선형연산자의 대각화가능(diagonalizable) 의 정의"

    유한차원 벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 에 대하여 $[\mathbf{T} ]_{\beta }$ 가 대각행렬이 되도록 하는 $\mathbf{V}$ 의 순서기저 $\beta$ 가 존재하면 $\mathbf{T}$ 를 대각화가능하다고 한다.

- 유한차원 벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 를 대각화가능하게 만드는, 즉 $[\mathbf{T} ]_{\beta}$ 가 대각행렬이 되게 하는 순서기저 $\beta = \{v_1, v_2, \dots, v_n \}$ 를 어떻게 찾을 수 있을까.

    $D = [\mathbf{T} ] _{\beta }$ 가 대각행렬이면 [선형변환의 행렬표현](../LinearTransformation/#9a08985c1) 에 의하여 $v_j \in \beta$ 와 $\lambda _j = D _{jj}$ 에 대하여 $\mathbf{T} (v_j) = \displaystyle \sum_{i=1}^{n}D _{ij}v_j = \lambda _jv_j$ 이다. 

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

## 선형연산자의 고유벡터에 대한 기하학적 의미

!!! tldr ""

    $\R$-벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 의 고유벡터 $v$, 대응하는 고윳값 $\lambda$ 와 $v$ 에 의해 생성된 $\mathbf{V}$ 의 1차원 부분공간 $\mathbf{W} = \text{span } (\{v\})$ 은 $0$ 과 $v$ 를 지나는 직선이다. 이때 다음이 성립한다. 

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

# 대각화 가능성

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

    $n$차원 벡터공간 $\mathbf{V}$ 의 대각화가능한 선형연사자를 $\mathbf{T}$ 라 하고 $[\mathbf{T} ]_{\beta } = D$ 가 대각행렬이 되도록 하는 $\mathbf{V}$ 의 순서기저를 $\beta$ 라 하면 $D$ 는 다음과 같다.

    $$ D = \begin{pmatrix} \lambda _{1}&0&\dots&0\\ 0&\lambda _2&\dots&0\\ \vdots& \vdots& \ddots& \vdots \\ 0&0&\dots&\lambda _n\\ \end{pmatrix} $$

    $\mathbf{T}$ 의 특성다항식 $f(t)$ 는 다음과 같다.

    $$ \begin{equation}\begin{split} f(t) &= \det(D-tI) = \begin{pmatrix} \lambda _{1}-t&0&\dots&0\\ 0&\lambda _2-t&\dots&0\\ \vdots& \vdots& \ddots& \vdots \\ 0&0&\dots&\lambda _n-t\\ \end{pmatrix} \\ &= (\lambda _1-t)(\lambda _2-t)\dots(\lambda _n-t)=(-1)^{n}(t-\lambda _1)(t-\lambda _2)\dots(t-\lambda _n) \end{split}\end{equation} \tag*{} $$

    ■ 
     
- 한편 $\mathbf{T}$ 의 특성다항식이 완전히 인수분해되어도 $\mathbf{T}$ 가 대각화 불가능일 수도 있다.

## 중복도

!!! tldr "대수적 중복도(algebraic multiplicity) 의 정의"

    특성다항식이 $f(t)$ 인 선형연산자(또는 행렬)의 고윳값 $\lambda$ 에 대하여 $(t - \lambda )^{k}$ 가 $f(t)$ 의 인수가 되도록 하는 가장 큰 자연수 $k$ 를 $\lambda$ 의 대수적 중복도라고 한다.

- 단순하게 중복도라고도 한다.

- 예시 

    $A = \begin{pmatrix} 3&1&0\\ 0&3&4\\ 0&0&4\\ \end{pmatrix}$ 의 특성다항식은 $f(t) = -(t-3)^{2}(t-4)$ 이므로 $\lambda =3$ 의 중복도는 $2$, $\lambda =4$ 의 중복도는 $1$ 이다.

## Eigenspace

!!! tldr "선형연산자의 고유공간(eigenspace) 의 정의"

    벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 와 고윳값 $\lambda$ 에 대하여 다음 집합 $\mathbf{E}_{\lambda}$ 를 고윳값 $\lambda$ 에 대응하는 $\mathbf{T}$ 의 고유공간이라 한다.

    $$ \mathbf{E}_{\lambda} = \{x \in \mathbf{V} : \mathbf{T} (x) = \lambda x\} = \mathbf{N} (\mathbf{T}-\lambda \mathbf{I} _{\mathbf{V} }) $$

- [정리 5.4](#2514593f4) 는 벡터 $v \in \mathbf{V}$ 가 고윳값 $\lambda$ 에 대응하는 고유벡터이려면 $(\mathbf{T} - \lambda \mathbf{I} _{\mathbf{V} })(v) = 0$ 이어야 함을 말해준다.

- [정리 2.1](../LinearTransformation/#eb957cbf0) 에 의하여 $\mathbf{E}_{\lambda}$ 는 고윳값 $\lambda$ 에 대응하는 $\mathbf{T}$ 의 고유벡터와 영벡터로 이루어진 $\mathbf{V}$ 의 부분공간이다.

!!! tldr "행렬의 고유공간(eigenspace) 의 정의"

    벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{L}_{A}$ 와 고윳값 $\lambda$ 에 대하여 다음 집합 $\mathbf{E}_{\lambda}$ 를 고윳값 $\lambda$ 에 대응하는 $A$ 의 고유공간이라 한다.

    $$ \mathbf{E}_{\lambda} = \{x \in \mathbf{V} : \mathbf{L}_{A} (x) = \lambda x\} = \mathbf{N} (\mathbf{L}_{A}-\lambda \mathbf{I} _{\mathbf{V} }) $$

!!! tldr "정리 5.7"

    유한차원 벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 와 중복도가 $m$ 인 $\mathbf{T}$ 의 고윳값 $\lambda$ 에 대하여 $1 \leq \dim (\mathbf{E}_{\lambda} )\leq m$ 이다.

- 증명

    [정리 1.11 따름정리](../VectorSpace/#dd66d2443) 에 의하여 $\mathbf{E}_{\lambda}$ 의 순서기저 $\{v_1, v_2, \dots, v_p\}$ 를 확장하여 $\mathbf{V}$ 의 순서기저 $\beta = \{v_1, v_2, \dots, v_p, v _{p+1}, \dots, v_n\}$ 를 만들 수 있다. [선형변환의 행렬표현](../LinearTransformation/#9a08985c1) 에 의하여 $[\mathbf{T} ]_{\beta }=A$ 을 $1$ 열부터 $n$ 열까지는 다음과 같다. 

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

    일차독립 집합은 [정리 1.10](../VectorSpace/#dfa035489) 에 의하여 반드시 $\mathbf{E}_{\lambda_i}$ 의 차원과 기수가 같거나 작다. 또한 정리 5.7 에 의하여 $\mathbf{E}_{\lambda_i}$ 의 차원은 $\lambda _i$ 의 중복도 $m_i$ 와 같거나 작다. 따라서 다음이 성립한다. 

    $$ n = \sum_{i=1}^{k}n_i \leq \sum_{i=1}^{k}d_i \leq \sum_{i=1}^{k}m_i = n $$

    그러므로 $\displaystyle \sum_{i=1}^{k}(m_i - d_i) = 0$ 이다. 정리 5.7 에 의하여 $m_i - d_i \geq 0$ 이므로 각 $i$ 에 대하여 $m_i = d_i$ 이다. ▲ 

    이제 모든 $i$ 에 대하여 $m_i = d_i$ 를 가정하고, $\mathbf{T}$ 가 대각화가능인 것과 2) 를 증명하자.

    각 $i$ 에 대하여 $\mathbf{E}_{\lambda_i}$ 의 순서기저를 $\beta _i$ 라 하고 $\beta = \bigcup_{i=1}^{k}\beta _i$ 를 정의하자. 그러면 정리 5.5 에 의해 $\beta$ 는 일차독립이다. 또한 $|\beta | = \sum_{i=1}^{k}d_i = \sum_{i=1}^{k}m_i = n$ 이다. 중복도의 합이 특성다항식의 차수 $n$ 이 되기 때문이다. [정리 1.10 따름정리 2](../VectorSpace/#cd7879a47) 에 의하여 $\beta$ 는 $\mathbf{V}$ 의 고유벡터로 이루어진 $\mathbf{V}$ 의 순서기저이다. 그러므로 [정리 5.1](#57f0cd776) 에 의하여 $\mathbf{T}$ 는 대각화가능하다. ■ 

- 예시

