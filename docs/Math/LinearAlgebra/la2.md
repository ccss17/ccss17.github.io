# 행렬 대수 

## 행렬 연산

!!! tldr ""

    $m \times n$ 행렬 표기법 : $A$ 가 $m \times n$ 행렬이면 $m$ 개의 행과 $n$ 개의 열로 이루어진 행렬이다. 이 행렬 $A$ 는 다음과 같다. 
    
    $$ \begin{pmatrix} a_{11} & a_{12} & \dots & a_{1n}\\ a_{21} & a_{12} & \dots & a_{1n}\\ \vdots & \vdots  & \ddots & \vdots \\ a_{m1} & a_{m2} & \dots & a_{mn}\\ \end{pmatrix} $$



!!! tldr ""

    행렬의 성분의 표기 : $m \times n$ 행렬 표기법의 행렬 $A$ 에서의 $i$ 번째 행과 $j$ 번째 열에 있는 스칼라 성분을 $(i, j)$ 성분이라 한다.



!!! tldr ""

    대각성분(diagonal entry) :$m \times n$ 행렬 표기법의 행렬 $A$ 에서의 성분 $a_{11}, a_{22}, a_{33}, \dots$ 을 말한다.

- 대각성분은 주대각선main diagonal 을 이룬다.

!!! tldr ""

    대각행렬(diagonal matrix) : 비대각성분(nondiagonal) 이 모두 영인 $n \times  n$ 정사각형 행렬을 대각행렬이라 한다.



!!! tldr ""

    영행렬(zero matrix) : 모든 성분이 $0$ 인 행렬을 영행렬이라 한다.



!!! tldr ""

    행렬의 동치(equal) : 서로 같은 수의 행과 같은 수의 열을 갖고 대응하는 성분이 같으면 두 행렬을 같다고 한다.



!!! tldr ""

    **Theorem 1** 행렬 $A, B, C$ 가 같은 크기의 행렬이고 $r, s$ 가 스칼라라 하면 다음이 성립한다.
    
    1. $A + B = B + A$
    
    2. $(A + B) +C = A + (B + C)$
    
    3. $A + 0 = A$
    
    4. $r(A + B) = rA + rB$
    
    5. $(r + s)A = rA + sA$
    
    6. $r(sA) = (rs)A$



!!! tldr ""

    행렬의 곱 : $A$ 는 $m \times n$ 행렬이고 $B$ 는 $b_1, \dots, b_p$ 를 열로 갖는 $n \times p$ 행렬일 때, 곱 $AB$ 는 열이 $Ab_1, \dots, Ab_p$ 인 $m \times p$ 행렬이다.

- 즉, 다음과 같다. 

    $$ AB = A \begin{pmatrix} b_1&b_2& \dots &b_p \end{pmatrix} = \begin{pmatrix} Ab_1&Ab_2& \dots &Ab_p \end{pmatrix} $$

!!! tldr ""

    행렬곱 $AB$ 의 $(i, j)$ 성분 : $A$ 의 $i$ 행과 $B$ 의 $j$ 열에 대응하는 성분들의 곱의 합이다.

- 즉 다음과 같다.

    $$ (AB)_{ij} = a_{i1}b_{1j} + a_{i2}b_{2j} + \dots + a_{in}b_{nj} $$

!!! tldr ""

    **Theorem 2** 행렬 $A$ 는 $m \times n$ 이고, $B$ 와 $C$ 는 아래 기술된 합과 곱의 정의되는 크기라고 가정하자. 
    
    1. 곱셉의 결합법칙 : $A(BC)=(AB)C$ 
    
    2. 왼쪽 분배법칙 : $A(B+C)=AB+AC$
    
    3. 오른쪽 분배법칙 : $(B+C)A=BA+CA$
    
    4. $r(AB)=(rA)B=A(rB)$ (r 은 임의의 스칼라)
    
    5. 행렬곱에 대한 항등원 : $I_mA = A=AI_n$

- 예시

    $A=\begin{pmatrix}5&1\\3&-2\end{pmatrix}, B = \begin{pmatrix}2&0\\4&3\end{pmatrix}$ 이라 할 때 행렬이 서로 교환가능하지 않다는 것을 보이자. 즉 $AB \neq BA$ 임을 보이자.

    $$ AB = \begin{pmatrix} 5&1\\3&-2 \end{pmatrix} \begin{pmatrix} 2&0\\4&3 \end{pmatrix} = \begin{pmatrix} 14&3\\-2&-6 \end{pmatrix} $$

    $$ BA=\begin{pmatrix} 2&0\\4&3 \end{pmatrix} \begin{pmatrix} 5&1\\3&-2 \end{pmatrix} = \begin{pmatrix} 10&2\\29&-2 \end{pmatrix} $$

!!! tldr ""

    행렬곱의 성질
    
    1. 일반적으로 $AB \neq BA$ 이다.
    
    2. 행렬곱에 대한 소거법칙은 성립하지 않는다. 즉, $AB = AC$ 일 때 일반적으로 $B=C$ 는 참이 아니다.
    
    3. 행렬곱 $AB$ 가 영행렬일 떄, 일반적으로 $A=0$ 또는 $B=0$ 이라고 할 수 없다.

### 행렬의 거듭제곱

!!! tldr ""

    행렬의 거듭제곱 : $A$ 가 $n \times n$ 행렬이고 $k$ 가 양의 정수 일때 $A^k$ 는 다음과 같이 $k$ 개의 $A$ 를 곱한 것이다.
    
    $$ A^k = A \dots A (k개) $$

!!! tldr ""

    행렬의 $0$ 제곱 : $A^0$ 은 단위행렬이다.

- 위 정의에서 $k=0$ 이라면 $A^0x=x$ 가 되어야 자연스럽기 때문이다. 

### 행렬의 전치

!!! tldr ""

    전치행렬(transpost) : 그 열들이 $A$ 의 행들 중 대응하는 것들로 얻어진 것이다.

- $m \times n$ 행렬 $A$ 에 대하여 전치행렬이란 $n \times m$ 행렬 $A^T$ 로 표시한다.

- 예시 

    다음의 행렬을 생각하자.

    $$ A=\begin{pmatrix} a&b\\c&d \end{pmatrix}, B = \begin{pmatrix} -5&2\\1&-3\\0&4 \end{pmatrix} $$

    위 행렬의 각각의 전치행렬은 다음과 같다.

    $$ A^T = \begin{pmatrix} a&c\\b&d \end{pmatrix}, B^T = \begin{pmatrix} -5&1&0\\2&-3&4 \end{pmatrix} $$

!!! tldr ""

    **Theorem 3** $A$ 와 $B$ 는 다음 합과 곱 관련 성질들이 성립되는 행렬이다.
    
    1. $(A^T)^T = A$
    
    2. $(A+B)^T=A^T+B^T$
    
    3. 임의의 스칼라 $r$ 에 대하여, $(rA)^T = rA^T$
    
    4. $(AB)^T=B^TA^T$

## 역행렬

!!! tldr ""

    행렬의 가역성(invertible) : $n \times n$ 행렬 $A$ 는 다음을 만족하는 $n \times n$ 행렬 $C$ 가 존재할 때 가역적이라 한다.
    
    $$ CA = I , AC = I (I 는 n \times n 단위행렬) $$

- 가역적인 행렬을 정칙행렬 또는 가역행렬nonsingular matrix 라 하고 가역적이지 않은 행렬을 특이행렬singular matrix 라 한다.

!!! tldr ""

    역행렬(inverse) : 위의 정의에서 $A$ 를 $I$ 로 만드는 $C$ 를 $A$ 의 역행렬이라 하고 $A^{-1}$ 라 표시한다.

!!! tldr ""

    **Theorem 4** $2 \times 2$ 행렬에 대하여 역행렬이 존재하는지를 확인하는 방법과 역행렬을 구하는 공식 : $A = \begin{pmatrix}a & b\\c & d\end{pmatrix}$ 이라 하자. $ad - bc \neq 0$ 이면 $A$ 는 가역적이고 $A^{-1}$ 는 다음과 같다. $ad-bc=0$ 이면 $A$ 는 가역적이지 않다. 
    
    $$ A^{-1} = \frac{1}{ad-bc}\begin{pmatrix} d &-b\\-c&a \end{pmatrix} $$

!!! tldr ""

    $2 \times 2$ 행렬 $A$ 의 행렬식(determinant) : 위 정리에서 $ad-bc$ 를 $A$ 의 행렬식(determinant) 라 하고 다음과 같이 쓴다.
    
    $$ det A = ad - bc $$

!!! tldr ""

    **Theorem 5** $A$ 가 $n \times n$ 가역행렬이면 $\mathbb{R}^n$ 에 속하는 임의의 $b$ 에 대하여 방정식 $Ax=b$ 는 유일한 해 $x=A^{-1}b$ 를 갖는다.

- 예시 

    $A=\begin{pmatrix}3&4\\5&6\end{pmatrix}$ 일 때 $A$ 의 역행렬을 구하여 다음 방정식계의 해를 구하자.

    $$ 3x_1 + 4x_2 = 3 $$

    $$ 5x_1 + 6x_2 = 7 $$

    $b = \begin{pmatrix}3\\7\end{pmatrix}$ 일 때 위 방정식계는 $Ax=b$ 와 동치이므로 다음을 얻는다.

    $$ x = A^{-1}b = \begin{pmatrix} -3&2\\5/2&-3/2 \end{pmatrix}\begin{pmatrix} 3\\7 \end{pmatrix}=\begin{pmatrix} 5\\-3 \end{pmatrix} $$

!!! tldr ""

    **Theorem 6**
    
    1. $A$ 가 가역행렬이면, $A^{-1}$ 도 가역적이고 다음이 성립한다.
    
    $$ (A^{-1})^{-1} = A $$
    
    2. $A$ 와 $B$ 가 $n \times n$ 가역행렬이면, $AB$ 가 가역이고 $AB$ 의 역행렬은 다음과 같다.
    
    $$ (AB)^{-1} = B^{-1}A^{-1} $$
    
    3. $A$ 가 가역행렬이면, $A^T$ 도 가역행렬이다. 또 $A^T$ 의 역행렬은 $A^{-1}$ 의 전치행렬이다. 즉, 다음이 성립한다.
    
    $$ (A^T)^{-1} = (A^{-1})^T $$

### 기본행렬 (elementary matrix)

!!! tldr ""

    기본행렬(elementary matrix) : 단위 행렬에 기본 행연산을 한 번 적용하여 얻은 행렬이다.

- 예시 

    다음의 행렬을 생각하자.

    $$ E_1 = \begin{pmatrix} 1&0&0\\0&1&0\\-4&0&1 \end{pmatrix}, E_2=\begin{pmatrix} 0&1&0\\1&0&0\\0&0&1 \end{pmatrix}, E_3=\begin{pmatrix} 1&0&0\\0&1&0\\0&0&5 \end{pmatrix}, A=\begin{pmatrix} a&b&c\\d&e&f\\g&h&i \end{pmatrix} $$

    $E_1A, E_2A, E_3A$ 를 계산하고 $A$ 에 어떤 기본 행연산을 적용하면 이 곱들을 얻을 수 있는지 살펴보자. 먼저 주어진 행렬곱을 계산하면 다음과 같다.

    $$ E_1A = \begin{pmatrix} a&b&c\\d&e&f\\g-4a&h-4b&i-4c \end{pmatrix}, E_2A = \begin{pmatrix} d&e&f\\a&b&c\\g&h&i \end{pmatrix}, E_3A = \begin{pmatrix} a&b&c\\d&e&f\\5g&5h&5i \end{pmatrix} $$

    $A$ 의 1 행에 -4 를 곱하여 3행에 더하면 $E_1A$ 가 된다. (행 교체 연산)

    $A$ 의 1 행과 2 행을 교환하면 $E_2A$ 가 된다. (행 교환)

    $A$ 의 3 행에 5 를 곱하면 $E_3A$ 가 된다. (스칼라곱)

- 예시 

    다음 기본 행렬의 역행렬을 구하자. 

    $$E_1=\begin{pmatrix}1&0&0\\0&1&0\\-4&0&1\end{pmatrix}$$

    $E_1$ 을 $I$ 로 변환하기 위해서는 $1$ 행에 $4$ 를 곱하여 $3$ 행에 더해야 하고, 이 연산을 위한 기본행렬은 다음과 같다.

    $$ E_1^{-1} = \begin{pmatrix} 1&0&0\\0&1&0\\4&0&1 \end{pmatrix} $$

!!! tldr ""

    **Theorem 7** $n \times n$ 행렬 $A$ 가 가역적이기 위한 필요충분조건은 $A$ 가 $I_n$ 과 행 동치인 것이다.

- 이 경우 $A$ 를 $I_n$ 으로 축약하는 임의의 기본 행연산의 조합은 $I_n$ 을 $A^{-1}$ 로 변환한다.

- 증명 

    $A$ 가 가역적이라면 각 $b$ 에 대하여 행렬방정식 $Ax=b$ 가 해를 가진다. ($\because x=A^{-1}b$) 또 행렬방정식이 해를 가지기 때문에 $A$ 는 모든 행에 추축위치를 갖는다. 그런데 $A$ 가 정사각행렬이므로 $n$ 개의 추축위치는 반드시 주대각선 위에 있으며, 이는 곧 $A$ 의 $rref$ 가 $I_n$ 이라는 것이다. 즉, $A \sim I_n$ 이다.

    반대로 $A \sim I_n$ 이라고 가정하면 $A$ 를 축약하는 단계가 기본행렬을 왼쪽에 곱하는 것이므로 어떤 기본행렬 $E_1, \dots, E_p$ 가 존재하여 다음을 만족한다.

    $$ A \sim E_1A \sim E_2(E_1A) \sim \dots \sim E_p(E_{p-1} \dots E_1A) = I_n $$

    그러므로 다음이 성립한다.

    $$ E_pE_{p-1} \dots E_1A = I_n \tag{1} $$ 

    가역행렬들의 곱 $E_pE_{p-1} \dots E_1$ 은 가역적이기 때문에 위 식으로부터 다음을 얻는다. 

    $$ (E_pE_{p-1} \dots E_1)^{-1}(E_pE_{p-1} \dots E_1)A = (E_pE_{p-1} \dots E_1)^{-1}I_n $$ 

    $$ A = (E_pE_{p-1} \dots E_1)^{-1} $$ 

    그런데 $A$ 는 가역행렬의 역이므로 가역적이다($\because Theorem 6$). 그러므로 다음이 성립한다. 

    $$ A^{-1} = [(E_pE_{p-1} \dots E_1)^{-1}]^{-1} = E_pE_{p-1} \dots E_1 $$ 

### $A^{-1}$ 을 구하는 일반적인 방법

!!! tldr ""

    $A^{-1}$ 을 구하는 일반적인 방법 : 첨가행렬 $\begin{pmatrix}A&I\end{pmatrix}$ 를 행 축약한다. $A$ 가 $I$ 와 행 동치이면 $\begin{pmatrix}A&I\end{pmatrix}$ 는 $\begin{pmatrix}I&A^{-1}\end{pmatrix}$ 는 행 동치이다.

- 예시 

    행렬 $A = \begin{pmatrix}0&1&2\\1&0&3\\4&-3&8\end{pmatrix}$ 의 역행렬이 존재하면 구해보자. 

    $$ \begin{pmatrix} A & I\\ \end{pmatrix} = \begin{pmatrix} 0&1&2&1&0&0\\ 1&0&3&0&1&0\\ 4&-3&8&0&0&1\\ \end{pmatrix} \sim \begin{pmatrix} 1&0&0&-9/2&7&-3/2\\ 0&1&0&-2&4&-1\\ 0&0&1&3/2&-2&1/2\\ \end{pmatrix} = \begin{pmatrix} I & A^{-1}\\ \end{pmatrix} $$

    $A \sim I$ 이므로 $A$ 는 가역적이고 역행렬은 다음과 같다.

    $$ A^{-1} = \begin{pmatrix} -9/2&7&-3/2\\ -2&4&-1\\ 3/2&-2&1/2\\ \end{pmatrix} $$

## 가역행렬의 특징

!!! tldr ""

    **Theorem 8** 가역행렬 정리 : $A$ 가 $n \times n$ 정사각행렬이라 하면 다음 명제들은 서로 동치이다. 즉, 주어진 $A$ 에 대하여 다음 명제들은 모두 참이거나 모두 거짓이다.
    
    1. $A$ 는 가역행렬이다. 
    
    2. $A$ 는 $n \times n$ 단위행렬과 행 동치이다. 
    
    3. $A$ 는 $n$ 개의 추축위치를 갖는다. 
    
    4. 방정식 $Ax = 0$ 의 해는 자명한 해 뿐이다. 
    
    5. $A$ 의 열들은 일차 독립인 집합을 이룬다. 
    
    6. 선형변환 $x \mapsto Ax$ 는 일대일이다.
    
    7. $\mathbb{R} ^n$ 에 속하는 각 $b$ 에 대하여 방정식 $Ax = b$ 는 적어도 하나의 해를 갖는다. 
    
    8. $A$ 의 열들은 $\mathbb{R} ^n$ 을 생성한다.
    
    9. 선형변환 $x \mapsto Ax$ 는 $\mathbb{R} ^n$ 에서 $\mathbb{R} ^n$ 로의 전사변환이다. 
    
    10. $CA=I$ 를 만족하는 $n \times n$ 행렬 $C$ 가 존재한다. 
    
    11. $AD=I$ 를 만족하는 $n \times n$ 행렬 $D$ 가 존재한다. 
    
    12. $A^T$ 는 가역행렬이다.

- 명제들의 순환관계의 표기 : 명제 (1) 가 참이면 명제 (10) 가 참일 때, (1) 를 (10) 의 충분조건이라 하고 (1)$\implies$(10) 라 쓴다. 

- 명제들의 순환관계

    - $(1) \implies (10) \implies (4) \implies (3) \implies (2) \implies (1)$

        - (1) 이 참이면 (10) 에서 $A^{-1}$ 이 $C$ 의 역할을 한다. 

        - (1) 이 참이면 (10) 에서 $A^{-1}$ 이 $C$ 의 역할을 한다. 

    - $(1) \implies (11) \implies (7) \implies (1)$

    - $(7) \iff (8) \iff (9)$

    - $(4) \iff (5) \iff (6)$

    - $(1) \iff (12)$

- 예시 

    가역행렬 정의를 사용하여 A 가 가역적인지 판단하자.

    $$ A = \begin{pmatrix} 1&0&-2\\3&1&-2\\-5&-1&9 \end{pmatrix} $$

    $$ A \sim \begin{pmatrix} 1&0&-2\\0&1&4\\0&-1&-1 \end{pmatrix} \sim \begin{pmatrix} 1&0&-2\\0&1&4\\0&0&3 \end{pmatrix} $$

    $A$ 가 세 개의 추축위치를 가지므로 가역행렬 정리 (3) 에 의해 가역적이라고 판단할 수 있다. 

### 가역 선형변환

!!! tldr ""

    가역 선형변환의 정의 : 선형변환 $T:\mathbb{R} ^n \to \mathbb{R} ^n$ 에 대해 다음 두 조건을 만족하는 함수 $S:\mathbb{R} ^n \to \mathbb{R} ^n$ 가 존재하면 $T$ 를 가역적(invertible) 이라 한다. 
    
    $$ S(T(x)) = x, 모든 x \in \mathbb{R} ^n \tag{1} $$
    
    $$ T(S(x)) = x, 모든 x \in \mathbb{R} ^n \tag{2} $$ 

!!! tldr ""

    **Theorem 9** $T: \mathbb{R} ^n \to  \mathbb{R} ^n$ 이 선형변환이고 $A$ 가 $T$ 에 대한 표준행렬일 때, $T$가 가역적이기 위한 필요충분조건은 $A$ 가 가역행렬이라는 것이다. 이 경우 $S(x) = A^{-1}x$ 로 주어지는 선형변환 $S$ 은 식 (1), (2) 를 만족하는 유일한 함수이다.

## 분할행렬

!!! tldr ""

    분할행렬 : 행렬을 부분행렬 또는 블록으로 나눈 것이다.

- 예시 

    $$ A = \begin{pmatrix} 3 & 0 & -1 & 5 & 9 & -2\\ -5 & 2 & 4 & 0 & -3 & 1\\ -8 & -6 & 3 & 1 & 7 & -4\\ \end{pmatrix} $$

    이 행렬을 다음과 같이 성분들이 부분행렬인 $2 \times 3$ 분할 행렬로 쓸 수 있다.

    $$ A = \begin{pmatrix} A_{11} & A_{12} &A_{13} \\ A_{21} & A_{22} &A_{23} \\ \end{pmatrix} $$

    $$ A_{11} = \begin{pmatrix} 3&0&-1\\-5&2&4 \end{pmatrix}, A_{12} = \begin{pmatrix} 5&9\\0&-3 \end{pmatrix}, A_{13} = \begin{pmatrix} -2\\1 \end{pmatrix} $$

    $$ A_{21} = \begin{pmatrix} -8 & -6 & 3\\ \end{pmatrix}, A_{22} = \begin{pmatrix} 1 & 7\\ \end{pmatrix}, A_{23} = \begin{pmatrix} -4\\ \end{pmatrix} $$

!!! tldr ""

    행렬의 특정 행의 표기 : $row_k(A)$ 는 $A$ 의 $k$ 번째 행이다.



!!! tldr ""

    행렬의 특정 열의 표기 : $col_k(A)$ 는 $A$ 의 $k$ 번째 열이다.



!!! tldr ""

    블록 상삼각행렬(block upper triangular matrix) : 주대각선 보다 아래쪽 블록들이 0 인 분할행렬.

- 예시 

    $A = \begin{pmatrix}A_{11}&A_{12}\\0&A_{22}\end{pmatrix}$ 와 같은 행렬은 블록 상삼각행렬이다.

!!! tldr ""

    블록 하삼각행렬(block lower triangular matrix) : 주대각선 보다 위쪽 블록들이 0 인 분할행렬.



!!! tldr ""

    블록 대각행렬(block diagonal matrix) : 주대각선 이외의 블록들이 영인 분할행렬.

## 행렬의 분해

!!! tldr ""

    행렬 $A$ 의 분해(factorization) : 행렬 $A$ 를 두 개 이상의 행렬의 곱으로 표시한 방정식.

### LU 분해

!!! tldr ""

    LU 분해 : 행렬 $A$ 가 $m \times m$ 행렬이고 행 교환 없는 행 축약을 통해 사다리꼴로 바꿀 수 있다고 할 때 $A$ 를 $A=LU$ 형태로 쓰는 것이다.

- 이때 $L$ 은 대각선상의 원소가 $1$ 인 $m \times m$ 하삼각행렬이고, $U$ 는 $A$ 의 $m \times n$ 사다리꼴 행렬이다.

!!! tldr ""

    단위하삼각행렬(unit lower triangular matrix) : 위 정의에서 $L$ 을 단위하삼각행렬이라 한다. ($L$ 은 가역적이다)

- 예시 

    다음은 행렬 $A$ 를 $LU$ 분해 한 것이다. 

    $$ A = LU = \begin{pmatrix} 1&0&0&0\\ *&1&0&0\\ *&*&1&0\\ *&*&*&1\\ \end{pmatrix} \begin{pmatrix} @&*&*&*&*\\ 0&@&*&*&*\\ 0&0&0&@&*\\ 0&0&0&0&0\\ \end{pmatrix} $$

!!! tldr ""

    LU 분해의 유용성 : $A=LU$ 일 때, 방정식 $Ax=b$ 는 $L(Ux)=b$ 라 쓸 수 있다. $Ux$ 를 $y$ 라 하면 $x$ 를 다음 두 방정식을 풀어 얻을 수 있다. 
    
    $$ Ly = b $$
    
    $$ Ux = y $$
    
    $Ly = b$ 를 풀어 $y$ 를 구하고 그 다음 $Ux=y$ 를 풀어 $x$ 를 구한다.

- 예시

    행렬 $A$ 에 대해 다음 관계가 성립한다.

    $$ A = \begin{pmatrix} 3 & -7 & -2 & 2\\ -3 & 5 & 1 & 0\\ 6 & -4 & 0 & -5\\ -9 & 5 & -5 & 12\\ \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 & 0\\ -1 & 1 & 0 & 0\\ 2 & -5 & 1 & 0\\ -3 & 8 & 3 & 1\\ \end{pmatrix}\begin{pmatrix} 3 & -7 & -2 & 2\\ 0 & -2 & -1 & 2\\ 0 & 0 & -1 & 1\\ 0 & 0 & 0 & -1\\ \end{pmatrix} = LU $$

    이때 $Ax = b$ 의 해를 구하자. $b = \begin{pmatrix}-9\\5\\7\\11\end{pmatrix}$ 이다. 

    $$ \begin{pmatrix} L & b\\ \end{pmatrix} = \begin{pmatrix} 1&0&0&0&-9\\ -1&1&0&0&5\\ 2&-5&1&0&7\\ -3&8&3&1&11\\ \end{pmatrix} \sim \begin{pmatrix} 1&0&0&0&-9\\ 0&1&0&0&-4\\ 0&0&1&0&5\\ 0&0&0&1&1\\ \end{pmatrix} = \begin{pmatrix} I & y\\ \end{pmatrix} $$

    $$ \begin{pmatrix} U & y\\ \end{pmatrix} = \begin{pmatrix} 3&-7&-2&2&-9\\ 0&-2&-1&2&-4\\ 0&0&-1&1&5\\ 0&0&0&-1&1\\ \end{pmatrix} \sim \begin{pmatrix} 1&0&0&0&3\\ 0&1&0&0&4\\ 0&0&1&0&-6\\ 0&0&0&1&-1\\ \end{pmatrix}$$ 
    
    $$x = \begin{pmatrix} 3\\4\\-6\\-1 \end{pmatrix} $$

### LU 분해 알고리듬

!!! tldr ""

    LU 분해 사전작업 : 행 교체(하나의 방정식을 그 방정식을 상수배하여 합한 것으로 대체) 연산만으로 $A$ 를 사다리꼴 $U$ 로 축약할 수 있다고 하면 다음을 만족하는 단위하삼각 기본행렬들 $E_1, \dots, E_p$ 가 존재한다.
    
    $$ E_p \dots E_1A = U \tag{3} $$ 
    
    그러면 다음이 성립한다. 
    
    $$ A = (E_p \dots E_1)^{-1}U = LU $$
    
    그러므로 $L$ 은 다음과 같다.
    
    $$ L = (E_p \dots E_1)^{-1} \tag{4} $$
    
    $A$ 를 $U$ 로 축약하는 행연산 $E_p \dots E_1$ 은 $L$ 를 $I$ 로 축약한다. 왜냐하면 $E_p \dots E_1L = (E_p \dots E_1)(E_p \dots E_1)^{-1} = I$ 이기 때문이다. 
    
    (4) 로부터 다음이 성립합을 알 수 있다. 
    
    $$ E_p \dots E_1L = I $$
    
    위 식의 $E_p \dots E_1$ 는 (3) 의 식에서 $A$ 를 사다리꼴로 만든다. 그러므로 $A$ 의 $n$ 번째 열을 사다리꼴로 만드는 행연산은 $L$ 의 $n$ 번째 열을 $I$ 의 $n$ 번째 열로 만든다.

!!! tldr ""

    LU 분해를 위한 알고리듬 
    
    1. 가능하다면 $A$ 에 일련의 행 교체(하나의 방정식을 그 방정식을 상수배하여 합한 것으로 대체) 연산을 적용하여 사다리꼴 $U$ 로 축약한다. 
    
    2. 위와 같은 순서의 행연산으로 $L$ 을 $I$ 로 축약하도록 $L$ 의 원소를 정한다.

- 예시 

    다음 행렬 $A$ 의 $LU$ 분해를 구해보자.

    $$ A = \begin{pmatrix} 2&4&-1&5&-2\\ -4&-5&3&-8&1\\ 2&-5&-4&1&8\\ -6&0&7&-3&1\\ \end{pmatrix} $$

    먼저 $A$ 가 $4$ 개의 행을 가지므로 $L$ 은 다음과 같은 꼴이다. 

    $$ L = \begin{pmatrix} 1&0&0&0\\ *&1&0&0\\ *&*&1&0\\ *&*&*&1\\ \end{pmatrix} $$

    그런데 $A$ 의 $1$번째 열 $\begin{pmatrix}2\\-4\\2\\-6\end{pmatrix}$ 을 사다리꼴의 열 $\begin{pmatrix}2\\0\\0\\0\end{pmatrix}$ 로 만드는 행 교체 연산을 $L$ 의 $1$번째 열 $\begin{pmatrix}1\\*\\*\\*\end{pmatrix}$ 에 적용하면 단위행렬 $I$ 의 열이 도출되어야 하므로 분명히 $\begin{pmatrix}1\\0\\0\\0\end{pmatrix}$ 이 계산되어야 한다. 그러므로 $L$ 의 $1$번째 열을 알 수 있다.

    $$ L = \begin{pmatrix} 1&0&0&0\\ -2&1&0&0\\ 1&*&1&0\\ -3&*&*&1\\ \end{pmatrix} $$

    같은 방법으로 $L$ 을 계산할 수 있다. 그럼 먼저 $A$ 를 $U$ 로 변환하는 행연산 알아내기 위하여 행 축약을 해보자. 

    $$ A = \begin{pmatrix} 2&4&-1&5&-2\\ -4&-5&3&-8&1\\ 2&-5&-4&1&8\\ -6&0&7&-3&1\\ \end{pmatrix} \sim \begin{pmatrix} 2&4&-1&5&-2\\ 0&3&1&2&-3\\ 0&-9&-3&-4&10\\ 0&12&4&12&-5\\ \end{pmatrix} \sim \begin{pmatrix} 2&4&-1&5&-2\\ 0&3&1&2&-3\\ 0&0&0&2&1\\ 0&0&0&4&7\\ \end{pmatrix} \sim \begin{pmatrix} 2&4&-1&5&-2\\ 0&3&1&2&-3\\ 0&0&0&2&1\\ 0&0&0&0&5\\ \end{pmatrix} = U $$

    각각의 열을 사다리꼴의 열로 만드는 행연산을 통하여 다음과 같이 $L$ 을 계산할 수 있다. 

    $$ L = \begin{pmatrix} 1&0&0&0\\ -2&1&0&0\\ 1&-3&1&0\\ -3&4&2&1\\ \end{pmatrix} $$

    그런데 $L$ 은 단지 $A$ 를 $U$ 로 행 축약하는 과정에서 추축열을 만드는 연산을 하기 전 상태의 열을 가져온 후 대각성분을 $1$ 로 만드는 나눗셈을 한 결과와도 같다는 것을 알 수 있다. 

## $\mathbb{R} ^n$ 의 부분공간

!!! tldr ""

    $\mathbb{R} ^n$ 의 부분공간 : $\mathbb{R} ^n$ 의 부분공간이란 다음 세 성질을 만족하는 $\mathbb{R} ^n$ 의 집합 $H$ 이다.
    
    1. 영벡터가 $H$ 에 속한다. 
    
    2. $H$ 내의 각 $u, v$ 에 대하여, 합 $u + v$ 가 $H$ 에 속한다.
    
        - 덧셈에 대하여 닫혀있다.
    
    3. $H$ 내의 각 $u$ 와 각 스칼라 $c$ 에 대하여, 벡터 $cu$ 가 $H$ 에 속한다. 
    
        - 곱셈에 대하여 닫혀있다.

- 예시

    $v_1, v_2$ 가 $\mathbb{R} ^n$ 에 속하고 $H = Span\{v_1, v_2\}$ 이면, $H$ 는 $\mathbb{R} ^n$ 의 부분공간임을 보여라. 

    부분공간이 정의된 세 가지 조건을 각각 검증하면 된다.

    먼저 영벡터는 $H$ 에 속한다. ($\because 0v_1 + 0v_2 = (v_1 와 v_2 의 일차결합)$)

    이제 다음과 같이 $H$ 에 속하는 임의의 두 벡터를 생각하자. 

    $$ u = s_1v_1 + s_2v_2, v = t_1v_1 + t_2v_2 $$

    그러면 다음이 성립한다. 

    $$ u + v = (s_1+t_1)v_1 + (s_2+t_2)v_2 $$

    그러므로 $u+v$ 가 $v_1$ 와 $v_2$의 일차결합이고 따라서 $H$에 속한다. 

    마지막으로 임의의 스칼라 $c$ 에 대하여 $cu = c(s_1v_1+s_2v_2)=(cs_1)v_1+(cs_2)v_2$ 이므로 벡터 $cu$ 는 $H$ 에 속한다.

- 예시

    $\mathbb{R} ^n$ 에 속하는 $v_1, \dots, v_p$ 의 모든 일차결합의 집합 $Span\{v_1, \dots, v_p\}$ 은 $\mathbb{R} ^n$ 의 부분공간이다. 증명은 위의 예시와 유사하다. 그러므로 $Span\{v_1, \dots, v_p\}$ 을 $v_1, \dots, v_p$ 에 의해 생성된 부분공간이라 할 수 있다. 

### 행렬의 열공간과 영공간

!!! tldr ""

    열공간(column space) : 행렬 $A$의 열공간 $Col A$ 이란 $A$ 의 열들의 모든 일차결합의 집합이다.

- 그러므로 모든 열벡터가 $\mathbb{R} ^m$ 에 속하는 행렬 $A = \begin{bmatrix}a_1&\dots&a_n\end{bmatrix}$ 의 $Col A$ 는 $Span\{a_1, \dots, a_n\}$ 이다.

- 예시 

    $A, b$ 가 다음과 같을 때 $b$ 가 $A$ 의 열공간에 속하는지 판단하자.

    $$ A=\begin{bmatrix} 1&-3&-4\\ -4&6&-2\\ -3&7&6 \end{bmatrix}, b = \begin{bmatrix} 3\\3\\-4 \end{bmatrix} $$

    벡터 $b$ 가 $A$ 의 열들의 일차결합이 되기 위한 필요충분조건은 $b$ 가 어떤 벡터 $x$ 에 대하여 $Ax$ 로 표시되는 것, 즉 방정식 $Ax = b$ 가 해를 갖는 것이다. 

    $$\because Ax=\begin{bmatrix}1&-3&-4\\-4&6&-2\\-3&7&6\end{bmatrix}\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}=x_1\begin{bmatrix}1\\-4\\-3\end{bmatrix}+x_2\begin{bmatrix}-3\\6\\7\end{bmatrix}+x_3\begin{bmatrix}-4\\-2\\6\end{bmatrix}$$

    그러므로 첨가행렬 $\begin{bmatrix}A\\b\end{bmatrix}$ 를 다음과 같이 축약하자. 

    $$ \begin{bmatrix} 1&-3&-4&3\\ -4&6&-2&3\\ -3&7&6&-4 \end{bmatrix} \sim \begin{bmatrix} 1&-3&-4&3\\ 0&-6&-18&15\\ 0&0&0&0 \end{bmatrix} $$

    이로부터 $Ax = b$ 는 해를 가지며 $b$ 는 $Col A$ 에 속해 있음을 알 수 있다.

!!! tldr ""

    영공간(null space) : 동차방정식 $Ax = 0$ 의 모든 해의 집합이며 $Nul A$ 라고 표기한다.



!!! tldr ""

    **Theorem 12** $m \times n$ 행렬 $A$ 의 영공간 $Nul A$ 는 $\mathbb{R} ^n$ 의 부분공간이다. 이와 동등하게 $n$ 개의 미지수를 갖는 $m$ 개의 동차선형방정식으로 구성된 방정식계 $Ax=0$ 의 모든 해의 집합은 $\mathbb{R} ^n$ 의 부분공간이다.

- $\because$ $A$ 가 $n$ 개의 열을 가질 때, $Ax = 0$ 의 해는 $\mathbb{R} ^n$ 에 속하고 $A$ 의 영공간은 $\mathbb{R} ^n$ 의 부분집합이다.

- $Ax=0$ 의 모든 해집합 $Nul A$ 가 $\mathbb{R} ^n$ 의 부분공간이라는 것에 대한 증명

    - $A0=0$ 이므로 영벡터는 $Nul A$ 에 속한다. $Nul A$ 에 속하는 임의의 두 벡터 $u, v$ 를 취하자. 즉, $Au = 0, Av = 0$ 라고 가정한다. 그러면 행렬곱의 성질에 의해 다음이 성립한다.

        $$ A(u + v) = Au + Av = 0 + 0 = 0 $$

        따라서 $u + v$ 는 $Ax = 0$ 을 만족하여 $Nul A$ 에 속한다. 또한 임의의 스칼라 $c$ 에 대하여 다음이 성립한다. 

        $$ A(cu) = c(Au) = c(0) = 0 $$

        그러므로 $cu$ 도 $Nul A$ 에 속한다. 

### 부분공간의 기저(basis)

!!! tldr ""

    부분공간 $H$ 의 기저(basis) $\Beta$ : $\mathbb{R} ^n$ 의 부분공간 $H$ 의 기저 $\Beta$ 는 $H$ 를 생성하는 $H$ 내의 일차 독립인 집합이다.

- 기저 $\Beta = \{b_1, \dots, b_p\}$ 가 생성하는 부분공간 $H$ 는 $Span \{b_1, \dots, b_p\}$ 과 동일하다.

- 예시 

    $n \times n$ 가역행렬의 열들은 $\mathbb{R} ^n$ 전체에 대한 기저가 된다. 왜냐하면 가역행렬 정리에 의해 이 열들이 일차 독립이며 $\mathbb{R} ^n$ 을 생성하기 때문이다. 이와 같은 행렬의 한 예로 $n \times n$ 항등행렬을 들 수 있다. 그 열들을 다음과 같이 $e_1, \dots, e_n$ 라 하자. 

    $$ e_1=\begin{bmatrix} 1\\0\\\vdots \\0 \end{bmatrix}, e_2=\begin{bmatrix} 0\\1\\\vdots \\0 \end{bmatrix}, \dots, e_n=\begin{bmatrix} 0\\\vdots \\0\\1 \end{bmatrix} $$

    집합 $\{e_1, \dots, e_n\}$ 을 $\mathbb{R} ^n$ 의 표준기저(standard basis) 라 한다. 

- 예시 

    다음 행렬의 영공간 $Nul A$ 에 대한 기저를 구하라. 

    $$ A = \begin{bmatrix} -3&6&-1&1&-7\\1&-2&2&3&-1\\2&-4&5&8&-4 \end{bmatrix} $$

    먼저 $Nul A$ 를 구하기 위하여 $Ax = 0$ 의 해를 매개변수 벡터 형식으로 쓰자. 

    $$ \begin{bmatrix} A&0\\ \end{bmatrix} \sim \begin{bmatrix} 1&-2&0&-1&3&0\\0&0&1&2&-2&0\\0&0&0&0&0&0 \end{bmatrix}, \begin{cases} x_1-2x_2-x_4+3x_5=0 &\text{}\\ x_3+2x_4-2x_5=0 &\text{}\\ 0=0 &\text{}\\ \end{cases} $$

    이를 통하여 자유변수 $x_2, x_4, x_5$ 를 갖는 일반해 $x_1 = 2x_2 + x_4 - 3x_5$, $x_3 = -2x_4 + 2x_5$ 를 얻을 수 있다. 

    $$ \begin{bmatrix} x_1\\x_2\\x_3\\x_4\\x_5 \end{bmatrix} = \begin{bmatrix} 2x_2 + x_4 - 3x_5\\x_2\\-2x_4 + 2x_5\\x_4\\x_5 \end{bmatrix} = x_2 \begin{bmatrix} 2\\1\\0\\0\\0 \end{bmatrix} + x_4 \begin{bmatrix} 1\\0\\-2\\1\\0 \end{bmatrix} + x_5 \begin{bmatrix} -3\\0\\2\\0\\1 \end{bmatrix} $$

    $$ = x_2u + x_4v + x_5w \tag{1} $$

    식 (1) 으로부터 $Nul A$ 가 $u, v, w$ 의 모든 일차결합의 집합 $Span\{u, v, w\}$ 과 일치함을 알 수 있다. ($\because$ $x_2, x_4, x_5$ 가 임의의 값을 갖는 자유변수이기 때문)

    즉, $\{u, v, w\}$ 가 $Nul A$ 를 생성한다. 

    그리고 이렇게 만들어진 $u, v, w$ 는 자동으로 일차 독립이 된다. 왜냐하면 $0 = x_2u + x_4v + x_5w$ 는 가중치 $x_2, x_4, x_5$ 가 모두 영일 때 성립하기 때문이다. 

    그러므로, $\{u, v, w\}$ 는 $Nul A$ 의 한 기저이다. 

- 예시 

    다음 행렬 $B$ 의 열공간 $Col B$ 에 대한 기저를 구해보자. 

    $$ B = \begin{bmatrix} 1&0&-3&5&0\\ 0&1&2&-1&0\\ 0&0&0&0&1\\ 0&0&0&0&0\\ \end{bmatrix} $$

    $B$ 의 열들을 $b_1, \dots, b_5$ 라 하자. 그런데 $b_3 = -3b_1 + 2b_2, b_4 = 5b_1 - b_2$ 이다. 그러므로 $Span\{b_1, \dots, b_5\}$ 은 $Span\{b_1, b_2, b_5\}$ 이 된다. 이에 따라 $Col B$ 에 속하는 임의의 벡터 $v$ 가 다음과 같다면, 

    $$ v = c_1b_1 + c_2b_2 + c_3b_3 + c_4b_4 + c_5b_5 $$

    $v$ 를 다음과 같이 쓸 수 있다. 

    $$ v = c_1b_1 + c_2b_2 + c_3(-3b_1 + 2b_2) + c_4(5b_1 - b_2) + c_5b_5 $$

    이는 $b_1, b_2, b_3$ 의 일차결합이므로 $\{b_1, b_2, b_5\}$ 는 $Col B$ 를 생성한다. 또한 $b_1, b_2, b_3$ 는 항등행렬의 열들이므로 일차독립이다. 따라서 $B$ 의 추축열 $b_1, b_2, b_3$ 는 $Col B$ 의 기저가 된다.

!!! tldr ""

    **Theorem 13** 행렬 $A$ 의 추축열들은 $A$ 의 열공간 $Col A$ 의 기저가 된다.

## 2.9 차원과 계수

### 좌표계

!!! tldr ""

    좌표(coordinates of x relative to the basis $\Beta$) : 집합 $\Beta  = \{b_1, \dots, b_n\}$ 가 부분공간 $H$ 의 기저일 때, $H$ 에 속하는 각 $x$ 에 대하여 기저 $\Beta$ 에 대한 $x$ 의 좌표는 $x = c_1b_1 + \dots + c_pb_p$ 를 만족하는 가중치 $c_1, \dots, c_p$ 이다.



!!! tldr ""

    좌표벡터(coordinates vector of x relative to $\Beta$) : 그리고 $\mathbb{R} ^p$ 에 속하는 다음 벡터를 
    
    $$ \begin{bmatrix} x\\ \end{bmatrix}_\Beta = \begin{bmatrix} c_1\\ \vdots  \\c_p \end{bmatrix} $$
    
    $\Beta$ 에 관한 $x$ 의 좌표벡터 혹은 $x$ 의 $\Beta$-좌표벡터($\Beta$ coordinate vector of x)라 한다.

### 부분공간의 차원

!!! tldr ""

    차원(dimension) : 영이 아닌 부분공간 $H$ 의 차원(dimension) 은 $dim H$ 로 표시하며 $H$ 에 대한 임의의 기저에 포함된 벡터의 개수이다.

- 영 부분공간 $\{0\}$ 의 차원은 영이라고 정의한다. 

- 예시 

    다음 행렬의 영공간 $Nul A$ 의 차원을 구하라. 

    $$ A = \begin{bmatrix} -3&6&-1&1&-7\\1&-2&2&3&-1\\2&-4&5&8&-4 \end{bmatrix} $$

    먼저 $Nul A$ 를 구하기 위하여 $Ax = 0$ 의 해를 매개변수 벡터 형식으로 쓰자. 

    $$ \begin{bmatrix} A&0\\ \end{bmatrix} \sim \begin{bmatrix} 1&-2&0&-1&3&0\\0&0&1&2&-2&0\\0&0&0&0&0&0 \end{bmatrix}, \begin{cases} x_1-2x_2-x_4+3x_5=0 &\text{}\\ x_3+2x_4-2x_5=0 &\text{}\\ 0=0 &\text{}\\ \end{cases} $$

    이를 통하여 자유변수 $x_2, x_4, x_5$ 를 갖는 일반해 $x_1 = 2x_2 + x_4 - 3x_5$, $x_3 = -2x_4 + 2x_5$ 를 얻을 수 있다. 

    $$ \begin{bmatrix} x_1\\x_2\\x_3\\x_4\\x_5 \end{bmatrix} = \begin{bmatrix} 2x_2 + x_4 - 3x_5\\x_2\\-2x_4 + 2x_5\\x_4\\x_5 \end{bmatrix} = x_2 \begin{bmatrix} 2\\1\\0\\0\\0 \end{bmatrix} + x_4 \begin{bmatrix} 1\\0\\-2\\1\\0 \end{bmatrix} + x_5 \begin{bmatrix} -3\\0\\2\\0\\1 \end{bmatrix} $$

    $$ = x_2u + x_4v + x_5w \tag{1} $$

    식 (1) 으로부터 $Nul A$ 가 $u, v, w$ 의 모든 일차결합의 집합 $Span\{u, v, w\}$ 과 일치함을 알 수 있다. ($\because$ $x_2, x_4, x_5$ 가 임의의 값을 갖는 자유변수이기 때문)

    즉, $\{u, v, w\}$ 가 $Nul A$ 를 생성한다. 그리고 이렇게 만들어진 $u, v, w$ 는 자동으로 일차 독립이 된다. 왜냐하면 $0 = x_2u + x_4v + x_5w$ 는 가중치 $x_2, x_4, x_5$ 가 모두 영일 때 성립하기 때문이다. 그러므로 $\{u, v, w\}$ 는 $Nul A$ 의 한 기저이다.

    따라서 행렬 $A$ 의 영공간은 $3$ 개의 벡터로 이뤄진 기저를 갖고 이 경우 $Nul A$ 의 차원은 $3$ 이다. 그런데 각 기저벡터가 $Ax = 0$ 의 자유변수에 대응되므로 $Nul A$ 의 차원($dim Nul A$)을 구하기 위해서 행렬방정식의 자유변수의 개수를 알아내어도 된다.

!!! tldr ""

    행렬 $A$ 의 계수(rank) : $rank A$ 로 표시하며 $A$ 의 열공간의 차원이다. $A$ 의 추축열들이 $Col A$ 의 기저이므로 $A$ 의 계수는 $A$ 의 추축열들의 개수이다.

- 예시 

    다음 행렬 A 의 계수를 구하자. 

    $$ A = \begin{bmatrix} 2&5&-3&-4&8\\ 4&7&-4&-3&9\\ 6&9&-5&2&4\\ 0&-9&6&5&-6 \end{bmatrix} $$

    먼저 $A$ 를 사다리꼴로 축약하자. 

    $$ A \sim \begin{bmatrix} 2&5&-3&-4&8\\ 4&7&-4&-3&9\\ 6&9&-5&2&4\\ 0&-9&6&5&-6 \end{bmatrix} \sim \dots \sim \begin{bmatrix} 2&5&-3&-4&8\\ 0&-3&2&5&-7\\ 0&0&0&4&-6\\ 0&0&0&0&0 \end{bmatrix} $$

    행렬 $A$ 가 $3$ 의 추축열을 가지므로 $rank A = 3$ 이다.

!!! tldr ""

    **Theorem 14** 계수정리(Rank Theorem) : 행렬 $A$ 가 $n$ 개의 열을 가지면 $rank A(추축열) + dim Nul A(자유변수) = n$ 이다.



!!! tldr ""

    **Theorem 15** 기저정리(Basis Theorem) : $H$ 가 $\mathbb{R} ^n$ 의 $p$차원 부분공간이라 하자. $H$ 에 속하는 정확하게 $p$ 개의 요소를 갖는 임의의 일차독립인 집합도 자동적으로 $H$ 에 대한 기저가 된다. 또한 $H$ 에 속하는 $p$ 개로 이루어진 임의의 집합이 $H$ 를 생성하면 이는 자동적으로 $H$ 의 기저가 된다.

### 계수와 가역행렬 정리

!!! tldr ""

    **Theorem** 가역행렬 정리 : $A$ 가 $n \times n$ 행렬이라 하자. 그러면 다음 명제들 각각은 $A$ 가 역행렬을 갖는다는 명제와 동치이다. 

13. $A$ 의 열벡터들은 $\mathbb{R} ^n$ 의 기저이다. 

14. $Col A = \mathbb{R} ^n$

15. $dim Col A = n$

16. $rank A = n$

17. $Nul A = \{0\}$

18. $dim Nul A = 0$
