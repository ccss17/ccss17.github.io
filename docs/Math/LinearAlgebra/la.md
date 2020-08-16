# 선형대수학에서의 선형방정식

선형방정식계는 선형대수학의 핵심이다.

1.1절 과 1.2절에서 선형방정식계의 해를 구하는 방법을 소개한다.

1.3절과 1.4절에서 선형방정식계가 어떻게 벡터방정식과 행렬방정식과 동치가 되는지 보여준다. 그리고 이 동치가 벡터의 일차결합에 관한 문제를 선형방정식계에 관한 문제로 축소시킨다. 

## 선형방정식계

!!! tldr ""

    선형방정식(linear equation) : 변수 $x_1, \dots ,x_n$ 에 대하여 다음과 같은 형태로 쓸 수 있는 방정식. (이때 $b$ 와 계수(coefficient) $a_1, ..., a_n$ 은 상수이고 $n$ 은 자연수)
    
    $$a_1x_1 + a_2x_2 + \dots + a_nx_n = b$$

- 예시 

    $4x_1 - 5x_2 + 2 = x_1$ 

- 예시 

    $x_2 = 2(\sqrt 6 - x_1) + x_3$

!!! tldr ""

    선형방정식계(system of linear equations) : 동일한 변수들($x_1, ..., x_n$) 을 포함하는 하나 이상의 선형방정식의 모임이다.

- 선형계(linear system) 라고도 한다.

- 예시

    $$ 2x_1 - x_2 + 1.5x_3 = 8 $$

    $$ x_1 - 4x_3 = -7 \tag{2}  $$ 

!!! tldr ""

    선형계의 해(solution) : 선형계의 변수 $x_1, ..., x_n$ 에 값 $s_1, ..., s_n$ 을 대입했을 때 모든 식이 참이되도록 하는 숫자 목록($s_1, ..., s_n$)이다.

- 예시 

    다음선형계의 해는 $(5, 6, 3)$ 이다.

    $$ x_1 - 4x_3 = -7 \tag{2} $$ 

!!! tldr ""

    해집합(solution set) : 가능한 모든 해들을 모아둔 집합.



!!! tldr ""

    선형계의 동치(equivalent) : 두 선형계가 동일한 해집합을 갖는 것.



!!! tldr ""

    선형계의 성질

- 선형계는 다음 중 하나를 만족한다.

    1. 해를 갖지 않는다(inconsistent).

    2. 하나의 해를 갖는다(consistent).

    3. 무한히 많은 해를 갖는다. 

## 행렬

!!! tldr ""

    행렬(matrix) : 수 또는 문자를 괄호 안에 직사각형 형태로 배열한 것이다.

- 케일리는 연립 일차방정식의 풀이를 연구하면서 $ad - bc$ 의 값에 따라 연립방정식의 해의 존재 여부가 달라진다(궁극적으로는 행렬의 가역 여부)는 것을 발견하고 그것을 결정자(determinant) 라고 불렀다. 그리고 이것이 행렬식이 되었다. 그런데 해밀턴이 케일리의 연구를 보고 연립방정식의 계수만 따로 표기하는 방법을 고안하면서 행렬이 탄생하였다. 

- 행렬은 함수(사상)을 표현하기 위한 도구이다. 모든 선형 변환(일차 변환)은 행렬로 표현할 수 있고 그 역도 성립하기 때문이다. 즉 행렬은 선형변환이고 이것을 선형대수학의 기본정리라 한다. 

- 예시 

    다음은 여섯 개의 원소를 가진 $2 \times 3$ 행렬이다. 

    $$ \begin{bmatrix} 1&9&-13\\20&5&-16 \end{bmatrix} $$

!!! tldr ""

    행(row) : 행렬의 가로줄이다.



!!! tldr ""

    열(column) : 행렬의 세로줄이다.

### 행렬표기법

!!! tldr ""

    계수행렬(coefficient matrix) : 선형계의 각각의 변수를 열로 정렬한 것이다.

- 예시

    다음과 같은 선형계가 있다고 하자.

    $$ x_1 - 2x_2 + x_3 = 0 $$

    $$ 2x_2 - 8x_3 = 8 $$

    $$ 5x_1 - 5x_3 = 10 \tag{3}  $$ 

    선형계(3) 의 계수 행렬은 다음과 같다. 

    $$ \begin{pmatrix} 1 & -2 & 1 \\ 0 & 2  &-8 \\ 5 & 0 & -5 \end{pmatrix} $$

!!! tldr ""

    첨가행렬(augmented matrix) : 계수행렬에 선형계 방정식의 우변의 상수들로 이루어진 열을 추가한 것.

- 예시 

    선형계(3) 의 첨가행렬은 다음과 같다. 

    $$ \begin{pmatrix} 1 & -2 & 1 & 0\\ 0 & 2  & -8 & 8\\ 5 & 0 & -5 & 10 \end{pmatrix} \tag{4} $$ 

!!! tldr ""

    정방행렬(square matrix) : 같은 수의 행과 열을 같는 행렬이다.

- $n \times n$ 행렬로 대표된다.

!!! tldr ""

    행렬의 크기 : 행렬이 $m$ 개의 행과 $n$ 개의 열로 이루어져 있을 때 행렬의 $m \times n$ 이다.

- 예시 

    첨가행렬 (4) 는 3개의 행과 4개의 열로 이루어져 있기 때문에 $3 \times 4$ 행렬이다. 

### 선형계 풀이법

!!! tldr ""

    선형계 풀이법 : 선형계를 풀기 쉬운 동치인 선형계로 단순화 시키는 것이다.

- 첫번째 방정식의 $x_1$ 항으로 나머지 방정식의 $x_1$ 항을 소거한다.

    두번째 방정식의 $x_2$ 항으로 나머지 방정식의 $x_2$ 항을 소거한다.

    이를 계속하면 풀기 쉬운 동치인 선형계를 얻는다.

!!! tldr ""

    기본 행연산 : 선형계의 단순화 시 사용하는 세 가지 기본연산이다.
    
    1. (교체) 하나의 방정식을 그 방정식을 상수배하여 합한 것으로 대체한다. 

        - ~~$i$ 행에 상수 $c$ 를 곱하여 $j$ 행에 더하는 것을 $A_{i, j}(c)$ 로 표현한다.~~

        - 예시 

            $\begin{bmatrix}1&2&3\\2&3&4\\3&4&5\end{bmatrix} \to \begin{bmatrix}1&2&3\\2&3&4\\0&-2&-5\end{bmatrix}$

    2. (교환) 두 방정식을 교환한다. 

        - ~~$i$ 행과 $j$ 행을 교환하는 것을 $A_{i, j}$ 로 표현한다.~~

        - 예시 

            $\begin{bmatrix}1&2&3\\2&3&4\\3&4&5\end{bmatrix} \to \begin{bmatrix}1&2&3\\3&4&5\\2&3&4\end{bmatrix}$

    3. (스칼라곱) 방정식의 모든 항에 0 이 아닌 상수를 곱한다. 

        - ~~$i$ 행에 $0$ 이 아닌 상수 $c$ 를 곱하는 것을 $A_i(c), (c \neq 0)$ 으로 표현한다.~~

- 예시 

    $\begin{bmatrix}1&2&3\\2&3&4\\3&4&5\end{bmatrix} \to \begin{bmatrix}2&4&6\\2&3&4\\3&4&5\end{bmatrix}$



!!! tldr ""

    행 동치(row equivalent) : 한 행렬에 기본 행 연산을 여러 번 적용하여 다른 행렬을 얻을 수 있을 때 두 행렬을 행 동치라 한다.



!!! tldr ""

    행 동치의 성질

- 두 선형계의 첨가행렬이 행 동치이면, 두 선형계는 동일한 해집합을 갖는다. 

### 해의 존재성과 유일성

!!! tldr ""

    선형계의 근본적인 문제

- (존재성) 선형계가 해를 갖는가?

- (유일성) 해가 존재하면 해가 하나뿐인가?

## 행 축약과 사다리꼴

!!! tldr ""

    영이 아닌(nonzero) 행 또는 열 : 적어도 하나의 영이 아닌 성분을 포함하는 행 또는 열.



!!! tldr ""

    선행 성분(leading entry) : 영이 아닌 행에서 가장 왼쪽의 영이 아닌 성분.



!!! tldr ""

    사다리꼴(echelon form) 행렬 : 다음 세 가지 성질을 갖는 직사각행렬이다.
    
    1. 영이 아닌 행은 모든 성분이 영인 행보다 항상 위에 있다. 

    2. 행의 선행 성분은 그 행보다 위에 있는 행의 선행 성분보다 더 오른쪽 열에 있다.

    3. 선행 성분보다 아래에 있는 것은 모두 0 이다. 

- 행사다리꼴(row echelon form) 이라고도 한다. 

- 예시

    $$ \begin{pmatrix} 2 & -3 & 2 & 1 \\ 0 & 1 & -4 & 8 \\ 0 & 0 & 0 & 5/2 \end{pmatrix} $$

!!! tldr ""

    기약사다리꼴(reduced echelon form) 행렬  : 행사다리꼴의 정의를 포함하여 다음의 조건을 만족하는 직사각행렬이다.
    
    4. 영이 아닌 행의 선행 성분은 항상 1 이다.

    5. 선행 성분 1 은 항상 그 열에서 유일한 영이 아닌 성분이다. 

- 기약행사다리꼴(reduced row echelon form) 이라고도 한다.

- 예시

    $$ \begin{pmatrix} 1 & 0 & 9 & 0 & 29 \\ 0 & 1 & 5 & 0 & 16 \\ 0 & 0 & 0 & 1 & 3 \end{pmatrix} $$



!!! tldr ""

    **Theorem 1** 기약사다리꼴 행렬의 유일성 : 하나의 행렬과 행 동치인 기약사다리꼴 행렬은 오직 하나이다.

### 추축위치

!!! tldr ""

    추축위치(pivot position) : 행렬의 기약사다리꼴 행렬의 선행 성분 $1$ 에 대응하는 행렬 내부의 위치.



!!! tldr ""

    추축열(pivot column) : 추축위치를 포함하는 행렬의 열.

- 예시

    행렬 A 에 행연산을 수행하여 사다리꼴 행렬을 얻어서 A 의 추축위치와 추축열을 찾는다.

    $$ A = \begin{pmatrix} 0 & -3& -6& 4& 9 \\ -1& -2& -1& 3& 1\\ -2& -3& 0& 3& -1\\ 1& 4& 5& -9& -7 \end{pmatrix} $$

    다음 사다리꼴에 따라서 추축열은 열 $1$, 열 $2$, 열 $4$ 이다. 추축위치는 $(1, 1), (2, 2), (3, 4)$ 이다.

    $$ \begin{pmatrix} 1 & 4& 5& -9& 7 \\ 0& 2& 4& -6& -6\\ 0& 0& 0& -5& 0\\ 0& 0& 0& 0& 0 \end{pmatrix} $$

### 선형계의 해

!!! tldr ""

    기본변수(basic variable) : 행렬의 추축열에 대응되는 변수.



!!! tldr ""

    자유변수(free variable) : 기본변수 이외의 변수로써 값이 임의로 정해지는 변수.



!!! tldr ""

    선형계의 해 : 첨가행렬을 행 축약하여 기약사다리꼴로 변환하면 해집합을 구할 수 있다.

- 예시

    어떤 선형계의 첨가행렬이 다음의 기약사다리꼴로 변환되었다고 하자.

    $$ \begin{pmatrix} 1 & 0& -5& 1 \\ 0& 1& 1& 4\\ 0& 0& 0& 0 \end{pmatrix} $$

    이에 해당하는 방정식계는 다음과 같다. 

    $$ x_1 - 5x_3 = 1$$

    $$ x_2 + x_3 = 4$$

    $$ 0 = 0 \tag{4} $$ 

    이때 기본변수는 $x_1$ 과 $x_2$ 이고 자유변수는 $x_3$ 이다. 

    $$ \begin{cases} x_1 = 1 + 5x_3 \\ x_2 = 4 - x_3 \\ x_3 은 자유변수 \end{cases} \tag{5} $$ 

    $x_3$ 은 자유변수이기에 값이 임의로 정해진다. 그리고 $x_3$ 에 따라 $x_1$ 과 $x_2$ 이 정해진다. 

### 해집합의 매개변수 표현

!!! tldr ""

    해집합의 매개변수 표현 : (5) 와 같이 표현한 것이다.



!!! tldr ""

    선형계를 푼다 : 해집합의 매개변수 표현을 구하거나 해집합이 공집합이라는 것을 판별하는 것이다.

### 해의 존재성과 유일성

!!! tldr ""

    **Theorem 2** 존재성과 유일성 정리 : 선형계가 해를 갖기 위한 필요충분조건은 첨가행렬의 가장 오른쪽 열이 추축열이 아닌 것이다. 즉 첨가행렬의 사다리꼴 행렬이 다음과 같은 형태의 행을 갖지 않는 것이다.
    
    $$ \begin{pmatrix} 0 & \dots & 0 & b \end{pmatrix} b \ne 0 $$
    
    이 경우 $0 = b$ 가 성립되어 선형계가 해를 갖지 않는다.
    
    하지만 해를 가지면 해집합은 (i) 자유변수가 없을 시 유일한 해를 갖고,
    
    (ii) 자유변수가 있을 시 무한히 많은 해를 갖는다.

## 벡터방정식

!!! tldr ""

    열벡터(column vector) 또는 벡터(vector): 하나의 열만을 갖는 행렬이다.

- 예시

    $u = \begin{pmatrix} 3 \\ -1 \end{pmatrix}$ 

    이는 직교좌표계의 좌표(3, -1)로 생각할 수도 있다.

> 구글이 제안한 벡터에 단어를 대입하여 자연어를 처리하는 word2vec 방식이 있다.

> 페이스북은 이것을 기반으로 fastText 기법을 만들었다. 

> 이것은 숫자에 대응시킬 수 있는 자연대상을 벡터 대수로 처리할 수 있다는 가능성을 보여준다. 즉, 자연어라는 자연대상을 수라는 집합으로 환원하고 그것에 적용되는 연산을 정의하여 대수구조로 만드는 것이다.

!!! tldr ""

    행벡터(row vector) : 하나의 행만을 갖는 행렬이다.

- 예시

    $u = \begin{pmatrix} 3 & -1 \\ \end{pmatrix}$

!!! tldr ""

    영벡터(zero vector) : 모든 성분이 영인 벡터.

### $\mathbb{R}^2$에서의 벡터

!!! tldr ""

    $\mathbb{R}^2$ 의 정의 : $2$ 개의 성분을 갖는 모든 벡터의 집합이다.

- $\mathbb{R}$ 의 의미는 벡터의 성분이 실수라는 것이다.

- 지수 $2$ 의 의미는 각각의 벡터가 $2$ 개의 성분을 갖는다는 뜻이다.

- 예시 

    $$ \begin{bmatrix} 1\\2 \end{bmatrix} $$

    이것은 $\big < 1, 2\big >$ 로도 표현할 수 있고 좌표평면에서의 종점의 좌표가 $(1, 2)$ 인 벡터로 볼 수 있다. 

### $\mathbb{R}^3$에서의 벡터

!!! tldr ""

    $\mathbb{R}^3$ 의 정의 : $3$ 개의 성분($3 \times 1$ 열행렬)을 갖는 벡터의 집합이다.

- 예시 

    $a=\begin{pmatrix} 2 \\ 3 \\ 4 \end{pmatrix}$

    이는 $3$차원 좌표공간에서의 좌표 $(2, 3, 4)$ 로 볼 수 있다.

### $\mathbb{R}^n$에서의 벡터

!!! tldr ""

    $\mathbb{R}^n$ 의 정의 : n 이 양의 정수일때, n 개의 실수로 이루어진 모든 순서 있는 n 짝(ordered n-tuples) 의 집합이다.

- 예시 

    보통 다음과 같이 $n \times 1$ 열행렬로 표시한다.

    $u=\begin{pmatrix} u_1 \\ u_2 \\ \vdots \\ u_n \end{pmatrix}$

    이는 $n$차원 좌표공간에서의 좌표로 볼 수 있다.

!!! tldr ""

    $\mathbb{R}^n$ 의 대수적 성질 : 임의의 벡터들 $u, v, w \in \mathbb{R}^n$ 과 임의의 수 c 와 d 에 대하여 다음이 성립한다.
    
1. $u + v = v + u$

2. $(u + v) + w = u + (v + w)$

3. $u + 0 = 0 + u = u$

4. $u + (-u) = -u + u = 0$

5. $c(u + v) = cv + cu$

6. $(c + d)u = cv + cu$

7. $c(du) = (cd)u$

8. $lu = u$

### 일차결합(linear combination)

!!! tldr ""

    일차결합(linear combination) : 어떤 벡터 $v_1, v_2, \dots, v_p \in \mathbb{R}^n$ 와 스칼라 $c_1, c_2, \dots, c_p$ 에 대하여 
    
    다음과 같이 정의된 벡터 $y$ 를 가중치(weight) $c_1, c_2, \dots, c_p$ 를 갖는 $v_1, v_2, \dots, v_p$ 의 일차결합(linear combination) 이라 한다.
    
    $$y = c_1v_1 + \dots + c_pv_p$$

- 예시 

    다음은 $v_1$ 과 $v_2$ 의 일차결합이다. 

    $\sqrt3v_1 + v_2$

    $\frac{1}{2}v_1 (=\frac{1}{2}v_1 + 0v_2)$

    $0 (= 0v_1 + 0v_2)$

### 벡터방정식 (vector equation)

!!! tldr ""

    벡터방정식 (vector equation) : 어떤 벡터 $v_1, v_2, \dots, v_p \in \mathbb{R}^n$ 와 변수 $x_1, x_2, \dots, x_p$ 에 대하여 
    
    다음과 같이 정의된 벡터 $y$ 를  벡터 방정식(vector equation) 이라 함. 
    
    $$y = x_1y_1 + \dots + x_pv_p$$

- 예시

    - $a_1 = \begin{pmatrix} 1 \\ -2 \\ -5 \end{pmatrix}$ , $a_2 = \begin{pmatrix} 2 \\ 5 \\ 6 \end{pmatrix}$ , $b = \begin{pmatrix} 7 \\ 4 \\ -3 \end{pmatrix}$ 이라 하자. $b$ 를 $a_1$ 과 $a_2$ 의 일차결합으로 표시할 수 있는지, 즉 다음 식을 만족하는 $x_1$ 과 $x_2$ 가 있는지 판별하자.

    $$x_1a_1 + x_2a_2 = b \tag{1} $$ 

    주어진 벡터방정식은 다음과 같다. 

    $$ x_1\begin{pmatrix} 1 \\-2 \\ -5  \end{pmatrix} + x_2\begin{pmatrix} 2 \\5 \\ 6  \end{pmatrix} = \begin{pmatrix} 7 \\4 \\ -3  \end{pmatrix} $$

    이는 다음과 같이 쓸 수 있다. 

    $$ \begin{pmatrix} x_1 + 2x_2\\ -2x_1 +5x_2 \\-5x_1 + 6x_2  \end{pmatrix} = \begin{pmatrix} 7 \\4 \\ -3  \end{pmatrix} \tag{2} $$ 

    (2) 의 좌변과 우변의 벡터가 같게 되기 위해서는 성분이 같아야 한다. 그러므로 $x_1$ 과 $x_2$ 가 (1) 의 해가 되기 위해서는 다음 선형계의 해가 되어야 함. 

    $$x_1 + 2x_2 = 7$$

    $$-2x_1 + 5x_2 = 4$$

    $$-5x_1 + 6x_2 = -3 \tag{3} $$ 

    이 선형계를 풀기 위해 그것의 첨가행렬을 축약하자. 

    $$ \begin{pmatrix}1 & 2 & 7 \\ -2 & 5 & 4 \\ -5 & 6 & -3\end{pmatrix} \sim \begin{pmatrix}1 & 0 & 3 \\ 0 & 1 & 2 \\ 0 & 0 & 0\end{pmatrix} $$

    이때 (3) 의 해는 $x_1 = 3$, $x_2 = 2$ 이기에 b 는 가중치 $x_1 = 3$, $x_2 = 2$ 를 갖는 $a_1$ 과 $a_2$ 의 일차결합이다. 

    그러면 (3) 의 첨가행렬은 단순히 벡터방정식(1) 로부터 얻을 수 있다. 첨가행렬을 단순히 다음과 같이 표현 할 수 있다. 

    $$\begin{pmatrix} a_1 & a_2 & b \end{pmatrix}$$

!!! tldr ""

    벡터방정식의 해집합 
    
    다음과 같은 벡터방정식이 있다고 생각하자. 
    
    $$x_1a_1 + x_2a_2 + \dots + x_na_n = b$$
    
    그러면 위의 논의로부터 방정식의 첨가행렬이 다음과 같은 선형계와 같은 해집합을 갖는다는 것을 알 수 있다.
    
    $$\begin{pmatrix}a_1 & a_2 & \dots & a_n & b\end{pmatrix}$$



!!! tldr ""

    모든 벡터의 집합 $Span$ : 어떤 벡터 $v_1, v_2, \dots, v_p \in \mathbb{R}^n$ 에 대하여 
    
    $v_1, v_2, \dots, v_p$ 의 모든 일차결합의 집합을 $Span\{v_1, \dots, v_p\}$ 이라 한다.

- 즉 스칼라 $c_1, \dots, c_p$ 에 대하여 다음의 형태로 표현되는 모든 벡터의 집합이다. 

    $$c_1v_1 + c_2v_2 + \dots + c_pv_p$$

- 예시

    - $Span\{v\}$ 의 의미

        $v$ 가 $\mathbb{R}^3$ 에 속하는 영이 아닌 벡터라고하자.

        $Span\{v\}$ 는 $v$ 의 모든 스칼라배의 집합이며, $v$ 과 $0$ 을 지나는 $\mathbb{R}^3$ 의 직선의 연장선상 위의 점들의 집합이다. 

        ![3차원 직선](https://user-images.githubusercontent.com/16812446/74583507-095a5a00-500b-11ea-86fe-a1cb8faccfae.png)

    - $Span\{u, v\}$ 의 의미

        $u, v$ 가 $\mathbb{R}^3$ 에 속하는 영이 아닌 벡터라고 하자. 

        $Span\{u, v\}$ 는 $u, v, 0$ 를 포함하는 $\mathbb{R}^3$ 내의 평면이다.

        ![3차원 직선(1)](https://user-images.githubusercontent.com/16812446/74583586-d2387880-500b-11ea-8096-d51df7105043.png)

## 행렬방정식 $Ax = b$

!!! tldr ""

    행렬방정식 $Ax = b$ : $A$ 가 $a_1, \dots, a_n$ 을 열로 갖는 $m \times n$ 행렬
    
    $$ A = \begin{pmatrix} a_1 & a_2 & \dots & a_n \end{pmatrix}$$
    
    이고 $x \in \mathbb{R}^n$ 
    
    $$ x = \begin{pmatrix} x_1 \\ x_2 \\ \dots \\ x_n \end{pmatrix}$$
    
    이면 $A$ 와 $x$ 의 곱 $Ax$ 는 다음과 같은 $A$ 의 열들과 이에 대응하는 $x$ 의 성분들을 가중치로 하는 일차결합이다. 
    
    $$ Ax = \begin{pmatrix} a_1 & a_2 & \dots & a_n \end{pmatrix}\begin{pmatrix} x_1 \\ x_2 \\ \dots \\ x_n \end{pmatrix} = x_1a_1 + x_2a_2 + \dots + x_na_n$$

- 예시

    $$ \begin{pmatrix} 1 & 2 & -1 \\ 0 & -5 & 3 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} 4 \\ 1 \end{pmatrix} $$

!!! tldr ""

    **Theorem 3** 행렬방정식의 해집합(벡터방정식과 선형계와의 관계) : A 가 $a_1, \dots, a_n$ 을 열로 갖는 $m \times n$ 행렬이고, $b \in \mathbb{R}^m$ 이면 다음 행렬방정식
    
    $$ Ax = b$$
    
    는 다음 벡터 방정식과 같은 해집합을 갖는다. 
    
    $$ x_1a_1 + x_2a_2 + \dots + x_na_n = b$$
    
    그리고 다음의 첨가행렬을 갖는 선형계와 같은 해집합을 갖는다. 
    
    $$ \begin{pmatrix} a_1 & a_2 & \dots & a_n & b\end{pmatrix}$$
    
    즉, 선형방정식계는 행렬방정식, 벡터방정식으로 볼 수 있다.

### 해의 존재성

!!! tldr ""

    행렬방정식의 해의 존재성의 필요충분조건 : $Ax = b$ 가 해를 갖기 위한 필요충분조건은 $b$ 가 $A$ 의 열의 일차 결합인 것이다.

- 예시

    $A=\begin{pmatrix}1 & 3 & 4 \\ -4 & 2 & -6 \\ -3 & -2 & -7\end{pmatrix}, b = \begin{pmatrix}b_1\\ b_2 \\ b_3\end{pmatrix}$ 이라 하면, 행렬방정식 $Ax=b$ 가 임의의 $b_1, b_2, b_3$ 에 대하여 해를 갖는가? 

    $Ax = b$ 에 대한 첨가행렬을 축약하면 다음과 같다.

    $$ \begin{pmatrix}1 & 3 & 4 & b_1 \\ -4 & 2 & -6 & b_2 \\ -3 & -2 & -7 & b_3\end{pmatrix} \sim \begin{pmatrix}1 & 3 & 4 & b_1 \\ 0 & 14 & 10 & b_2 + 4b_1 \\ 0 & 0 & 0 & b_3+3b_1-\frac{1}{2}(b_2+4b_1)\end{pmatrix} $$

    열 4 의 3번쨰 성분이 $b_3+3b_1-\frac{1}{2}(b_2+4b_1)$ 인데 적당한 $b$ 에 대하여 $b_3+3b_1-\frac{1}{2}(b_2+4b_1)$ 이 영이 아니게 되면 $0 = n (n\ne 0)$ 라는 식의 모순이 발생한다.

    $\therefore$ 임의의 $b$ 에 대하여 해를 갖는 것은 아니다. 

    위 행렬방정식이 해를 갖기 위해서는 반드시 다음을 만족해야 한다. 

    $$b_1-\frac{1}{2}b_2+b_3 = 0$$

    위 행렬방정식 $Ax = b$ 에서 $A$ 의 **사다리꼴 행렬** 이 영인 행을 가지므로 모든 $b$ 에 대하여 항상 행을 가지지 않는 것이다. 만약 $A$ 의 3 개의 행에 모두 추축이 있었다면 첨가행렬에서 계산을 신경 쓰지 않았을 것이다. 왜냐하면 첨가행렬에 $\begin{pmatrix}0&0&0&1\end{pmatrix}$ 같은 행이 없었을 것이기 때문이다.

!!! tldr ""

    **Theorem 4** $A$ 가 $m \times n$ 행렬이라 하자. 다음 명제들은 모두 동치이다. 
    
    1. 임의의 $b \in \mathbb{R}^m$ 에 대하여, 방정식 $Ax = b$ 가 해를 갖는다. 
    
    2. 임의의 $b \in \mathbb{R}^m$ 는 $A$ 의 열들의 일차결합이다.
    
    3. $A$ 의 열들이 $\mathbb{R}^m$ 을 생성한다. 
    
    4. $A$ 의 모든 행에 추축위치가 있다.

!!! tldr ""

    항등행렬(identity matrix) 의 정의 : 대각성분이 모두 1 이고 나머지 성분은 0 인 행렬이다.

- $n \times n$ 항등행렬은 $I_n$ 으로 표기한다.

- 예시 

    $I_3 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{pmatrix}$

!!! tldr ""

    항등행렬의 성질 : 모든 $n \times n$ 항등행렬에 대하여 $I_nx = x$  이다.

### 행렬과 벡터 곱 $Ax$ 의 성질

!!! tldr ""

    **Theorem 5** $A$가 $m \times n$ 행렬이고, $u, v \in \mathbb{R}^n$ 이며, $c$ 가 스칼라 일 때 다음이 성립한다.
    
    1. $A(u+v) = Au + Av$ 가 해를 갖는다. 
    
    2. $A(cu) = c(Au)$

## 선형계의 해집합 

### 동차선형계 (homogeneous)

!!! tldr ""

    동차선형계(homogeneous) : $m \times n$ 행렬 $A$ 와 영벡터 $0 \in \mathbb{R}^m$ 에 대하여
    
    $Ax = 0$ 형태로 쓸 수 있는 선형방정식계를 동차(homogeneous) 라 한다.



!!! tldr ""

    동차선형계(homogeneous) 의 성질

- 동차선형계 $Ax = 0$ 은 항상 적어도 하나의 해, $x = 0(\mathbb{R}^m 의 영벡터)$  를 갖는다. 그리고 이 해를 자명한 해(trivial solution) 라 한다.

- 동차선형계 $Ax = 0$ 의 자명하지 않은 해(nontirival solution) 은 영이 아닌 벡터 $x$ 이다. 

- 동차선형계가 자명하지 않은 해(nontirival solution) 를 갖기 위한 필요충분조건은 그 방정식이 적어도 하나의 자유변수를 갖는 것이다. 

- 동차선형계의 유일한 해가 영벡터라면 해집합은 $Span\{0\}$ 이다.

- 동차선형계 해의 자유변수가 $1$ 개라면 해집합($Span\{v\}$)은 기하학적으로 직선으로 표현된다.

- 동차선형계 해의 자유변수가 $2$ 개라면 해집합($Span\{u, v\}$)은 기하학적으로 평면으로 표현된다.

- 예시 

    (자명하지 않는 해를 갖는지 판별)

    다음 동차선형계가 자명하지 않은 해를 갖는지 판별하고 해집합을 구하자.

    $$3x_1 + 5x_2 - 4x_3 = 0$$

    $$-3x_1 - 2x_2 + 4x_3 = 0$$

    $$6x_1 + x_2 - 8x_3 = 0$$

    위 선형계의 계수행렬을 $A$ 라 하고 첨가행렬 $\begin{pmatrix}A & 0\end{pmatrix}$ 을 행축약하여 **사다리꼴** 로 변환하자.

    $$ \begin{pmatrix} 3 & 5 & -4 & 0 \\ -3 & -2 & 4 & 0 \\ 6 & 1 & -8 & 0 \\ \end{pmatrix} \sim \begin{pmatrix} 3 & 5 & -4 & 0 \\ 0 & 3 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ \end{pmatrix} $$

    $x_3$ 이 자유변수이므로, $Ax=0$ 은 $x_3$ 의 값에 따라 한 개씩 정해지는 자명하지 않은 해를 갖는다.

- 예시 

    (해집합을 구하는 과정)

    해집합을 구하기 위하여, $\begin{pmatrix}A & 0\end{pmatrix}$ 을 계속해서 행축약하여 **기약사다리꼴** 로 만들자. 

    $$ \begin{pmatrix} 1 & 0 & -\frac{4}{3} & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ \end{pmatrix} $$

    $$ x_1 - \frac{4}{3}x_3 = 0 $$

    $$ x_2 = 0 $$

    $$ 0 = 0 $$

    기본변수 $x_1$ 과 $x_2$ 를 풀어서 $x_1 = \frac{4}{3}x_3$, $x_2 = 0$ 을 얻을 수 있다.

    이제 $Ax=0$ 의 일반해를 다음과 같은 벡터로 나타낼 수 있다. 

    $$ x = \begin{pmatrix}x_1 \\ x_2 \\ x_3\end{pmatrix} = \begin{pmatrix}\frac{4}{3}x_3 \\ 0 \\ x_3\end{pmatrix} = x_3\begin{pmatrix}\frac{4}{3} \\ 0 \\ 1\end{pmatrix} = x_3v $$

    이때

    $$ v = \begin{pmatrix}\frac{4}{3} \\ 0 \\ 1\end{pmatrix} $$

    이다. 그러므로 $x=x_3v$ 가 되어 $Ax=0$ 의 모든 해는 $v$ 의 스칼라배($Span\{v\}$)이다. (물론 자명한 해는 자유변수 $x_3$ 을 $x_3 = 0$ 으로 택하여 얻을 수 있다)

- 예시 
    
    다음 동차선형계의 모든 해를 구하자.
    
    $$10x_1 - 3x_2 - 2x_3 = 0 \tag{1} $$ 
    
    기본변수 $x_1$ 를 자유변수의 항으로 생각하면 일반해는 $x_1 = .3x_2 + .2x_3$ 이다. $x_2$ 와 $x_3$ 은 자유변수이다. 이 일반해를 벡터로 표현하면 다음과 같다.
    
    $$ x = \begin{pmatrix}x_1 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} .3x_2 + .2x_3 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} .3x_2 \\ x_2 \\ 0\end{pmatrix} + \begin{pmatrix} .2x_3 \\ 0\\ x_3 \end{pmatrix} = x_2\begin{pmatrix} .3 \\ 1 \\ 0\end{pmatrix} + x_3\begin{pmatrix} .2 \\ 0\\ 1 \end{pmatrix} \tag{2} $$
    
    $$ u = \begin{pmatrix} .3 \\ 1 \\ 0\end{pmatrix} v = \begin{pmatrix} .2 \\ 0\\ 1 \end{pmatrix} $$
    
    즉 해집합은 $Span\{u, v\}$ 이다.

### 매개변수 벡터 형식

동차선형계 예시 2 에서 방정식을 풀어서 $x = su + tv (s, t \in \mathbb{R})$ 형식으로 나타낸 것을 매개변수 벡터방정식(parametric vector equation) 이라 한다. 

동차선형계 예시 1 에서 방정식 $x = x_3v$ 또는 $x = tv (t\in\mathbb{R})$ 는 직선의 매개변수 벡터방정식이다. 

이렇게 해집합이 벡터들로 명시적으로 표현되었다면 그 해가 매개변수 벡터 형식으로 주어졌다고 한다. 

### 비동차계의 해집합

!!! tldr ""

    비동차계의 해집합 : 비동차계$(Ax = b)$의 일반해는 어떤 동차계에 임의의 일차결합을 더한 배개변수 벡터 형식으로 쓸 수 있다.

- 예시 

    $Ax = b$ 가 다음과 같이 주어졌을 때 해집합을 구하자.

    $$ A = \begin{pmatrix} 3 & 5 & -4 \\ -3 &-2 & 4 \\ 6 & 1 & -8 \\ \end{pmatrix} $$

    $$ b = \begin{pmatrix} 7  \\ -1  \\ -4  \\ \end{pmatrix} $$

    $\begin{pmatrix} A & b\end{pmatrix}$ 에 행연산을 수행하여 다음을 얻자.

    $$ \begin{pmatrix} 3 & 5 & -4 & 7 \\ -3 &-2 & 4 & -1\\ 6 & 1 & -8 & -4\\ \end{pmatrix} \sim \begin{pmatrix} 1 & 0 & -\frac{4}{3} & -1 \\ 0 & 1 & 0 & 2\\ 0 & 0 & 0 & 0\\ \end{pmatrix} $$

    $$x_1 - \frac{4}{3}x_3 = -1 $$

    $$x_2 = 2 $$

    $$0 = 0 $$

    따라서 $x_1$, $x_2$ 는 기본변수, $x_3$ 은 자유변수이다. 

    $Ax=b$ 의 일반해를 벡터형식으로 나타내보자. 

    $$ x = \begin{pmatrix}x_1 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix}-1 + \frac{4}{3}x_3 \\ 2 \\ x_3 \end{pmatrix} = \begin{pmatrix}-1 \\ 2 \\ 0 \end{pmatrix} + x_3\begin{pmatrix}\frac{4}{3}  \\ 0 \\ 1 \end{pmatrix} $$

    $Ax=b$ 의 해집합은 $x = p + x_3v$ 를 $t$ 를 매개변수로 하여 다음과 같이 매개변수 벡터 형식으로 나타낼 수 있다. 

    $$x = p + tv (t\in\mathbb{R})$$

    이는 동차선형계 예시 1 에서의 해집합 $x = tv$ 에 $p$ 를 더하여 얻어진 것이다. 기하학적으로는 $x = tv$ 에서 $p$ 만큼 평행이동하여 $x = p + tv$ 를 얻었다고 할 수 있다.

!!! tldr ""

    **Theorem 6** 주어진 $b$ 에 대하여 방정식 $Ax = b$ 가 해를 갖고 그 해를 $p$ 라 하면, $Ax = b$ 의 해집합은 $w = p + v_h$ 형태인 모든 벡터들의 집합이다. $v_h$ 는 동차방정식 $Ax = 0$ 의 임의의 해이다.

## 일차 독립

!!! tldr ""

    일차 독립(linearly independent) : 어떤 벡터방정식이 자명한 해만을 가질 때 그 방정식을 이루는 벡터들의 집합을 일차 독립이라 한다.

- 예시 

    다음의 벡터방정식을 생각하자.

    $$x_1v_1 + x_2v_2 + \dots + x_pv_p = 0$$

    이 방정식이 오직 자명한 해($x_1=x_2=\dots=x_p=0$)만을 가질 때 벡터들의 집합 $\{v_1, \dots, v_p\} \in \mathbb{R}^n$ 은 일차 독립이다.

!!! tldr ""

    일차 종속(linearly dependent) : 어떤 벡터방정식이 자명하지 않은 해를 가질 때 그 방정식을 이루는 벡터들의 집합을 일차 독립이라 한다.

- 예시 

    다음의 벡터방정식을 생각하자.

    $$x_1v_1 + x_2v_2 + \dots + x_pv_p = 0$$

    이 방정식이 적어도 하나는 영이 아닌 상수 $c_1, \dots, c_p$ 를 해로 가지면, 즉 다음 식

    $$c_1v_1 + c_2v_2 + \dots + c_pv_p = 0$$

    을 만족하면 벡터들의 집합 $\{v_1, \dots, v_p\} \in \mathbb{R}^n$ 은 일차 종속이다. 

- 예시 

    다음 벡터들을 생각하자.

    $$ v_1 = \begin{pmatrix}1 \\ 2 \\ 3\end{pmatrix} v_2 = \begin{pmatrix}4 \\ 5 \\ 6\end{pmatrix} v_3 = \begin{pmatrix}2 \\ 1 \\ 0\end{pmatrix} $$

    집합 $\{v_1, v_2, v_3\}$ 이 일차 독립인지 판별하자. 

    일차독립과 일차종속의 정의에 따라 다음 벡터방정식이 자명하지 않은 해를 갖는지 판단하면 된다. 

    $$ x_1\begin{pmatrix}1\\2\\3\end{pmatrix} + x_2\begin{pmatrix}4\\5\\6\end{pmatrix} + x_3\begin{pmatrix}2\\1\\0\end{pmatrix} = \begin{pmatrix}0\\0\\0\end{pmatrix} $$

    그러면 이 벡터방정식의 첨가행렬을 행연산하여 기약사다리꼴을 얻자. 

    $$ \begin{pmatrix} 1&4&2&0\\ 2&5&1&0\\ 3&6&0&0\\ \end{pmatrix} \sim \begin{pmatrix} 1&0&-2&0\\ 0&1&1&0\\ 0&0&0&0\\ \end{pmatrix} $$

    기본변수가 $x_1, x_2$ 임을 알 수 있고 $x_3$ 이 자유변수라는 것을 알 수 있다. 그러므로 영이 아닌 값 $x_3$ 마다 자명하지 않은 해 하나가 결정되므로 $v_1, v_2, v_3$ 은 일차 종속이다. 

    이제 $v_1, v_2, v_3$ 사이의 일차 종속 관계를 구해보자. 

    $x_3$ 이 자유변수니까 그냥 $x_3 = 5$ 라고 생각하자. 그러면 $x_1 = 2x_3$, $x_2 = -x_3$ 이기 때문에 다음과 같은 벡터방정식을 얻는다.

    $$10v_1 - 5v_2 + 5v_3 = 0$$

    이것은 $v_1, v_2, v_3$ 사이의 무수히 많은 일차 종속 관계 중 하나다.

!!! tldr ""

    행렬 $A$ 의 열들이 일차 독립이기 위한 필요충분조건 : 방정식 $Ax = 0$ 이 자명한 해만을 갖는 것.

- 벡터들의 집합 대신 행렬 $A = \begin{pmatrix}a_1 \dots a_n\end{pmatrix}$ 로 시작한다고 생각하면 행렬방정식 $Ax = 0$ 은 다음과 같이 쓸 수 있다. 

    $$x_1a_1 + x_2a_2 + \dots + x_na_n = 0$$

    그러므로 $A$ 의 열들의 일차 종속 관계는 $Ax = 0$ 의 자명하지 않은 해에 대응한다. 반대로 $A$ 의 열들이 일차 독립 관계이려면 $Ax = 0$ 이 자명한 해만을 가져야 한다.

!!! tldr ""

    한 개의 벡터로 이루어진 집합이 일차 독립이 되는 조건 : 하나의 벡터 $v$ 로 이루어진 집합이 일차 독립인 것은 $v$ 가 영벡터가 아닌 것이다.

- 왜냐하면 $v \ne 0$ 일 때 벡터방정식 $x_1v = 0$ 이 자명한 해만을 갖기 때문이다. $v$ 가 영벡터 일 경우 일차 종속이 되는데, $x_10 = 0$ 이 무수히 많은 자명하지 않은 해를 갖기 때문이다.

!!! tldr ""

    두 개의 벡터로 이루어진 집합이 일차 독립이 되는 조건 : 두 벡터로 이루어진 집합 $\{v_1, v_2\}$ 은 하나의 벡터가 다른 벡터의 스칼라배일 때 일차 종속이다.

- 예시

    다음과 같이 서로 스칼라 배인 벡터 집합과 스칼라 배가 아닌 벡터 집합을 생각하자.

    $$ v_1 = \begin{pmatrix}3 \\ 1\end{pmatrix} , v_2 = \begin{pmatrix}6 \\ 2\end{pmatrix} \tag{a} $$ 

    (a) 의 경우 $v_2$ 가 $v_1$ 의 스칼라배, 즉 $v_2 = 2v_1$ 이므로 $-2v_1 + v_2 = 0$ 이 성립한다. 그러므로 일차 종속의 정의에 따라 집합 $\{v_1, v_2\}$ 은 일차 종속이다. 

    $$ v_1 = \begin{pmatrix}3 \\ 2\end{pmatrix} , v_2 = \begin{pmatrix}6 \\ 2\end{pmatrix} \tag{b} $$ 

    (b) 의 경우 $v_1$ 와 $v_2$ 가 서로 스칼라배가 아니다. 그런데 (b) 가 일차 종속이 되려면 $c$ 와 $d$ 가 다음 식을 만족해야 한다.

    $$cv_1 + dv_2 = 0$$

    $c \ne 0$ 일 경우 $v_1$ 을 $v_2$ 로 표현하여 $v_1 = (-\frac{d}{c})v_2$ 로 나타낼 수 있다. 그러나 $v_1$ 이 $v_2$ 의 스칼라배가 아니므로 모순이다. 따라서 $c = 0$ 이며, 이에 따라 $d = 0$ 이다. 그러므로 (b) 는 일차 독립인 집합이다. 

### 두 개 이상의 벡터로 이루어진 집합의 일차 독립

!!! tldr ""

    **Theorem 7** 일차 종속인 집합의 특성 두 개 이상의 벡터로 이루어진 집한 $S = \{v_1, \dots, v_p\}$ 가 일차 종속일 필요충분조건은 $S$ 에 있는 적어도 하나의 벡터가 다른 벡터들의 일차결합이 되는 것이다.



!!! tldr ""

    **Theorem 8** 어떤 집합에 포함된 벡터의 수가 각 벡터에 있는 성분의 개수보다 많으면, 그 집합은 반드시 일차 종속이다. 즉, 어떤 집합 $\{v_1, \dots, v_p\} \notin \mathbb{R}^n$ 에 대하여 $p > n$ 이면 그 집합은 일차 종속이다.

- 증명 

    $A = \begin{pmatrix}v_1 & \dots & v_p \end{pmatrix}$ 라 하면, $A$ 는 $n \times p$ 행렬이고 방정식 $Ax=0$ 은 $p$ 개의 미지수를 갖는 $n$ 개의 방정식으로 이루어진 선형방정식이다. $p > n$ 이면, 미지수의 개수가 방정식의 개수보다 많으므로 자유변수가 존재하고, 이에 따라 $Ax=0$은 자명하지 않은 해가 존재한다. 그러므로 $A$ 의 열들은 일차 종속이다. 

- 예시 

    다음 3 개의 벡터를 생각하자.

    $$ \begin{pmatrix} 2 \\ 1 \end{pmatrix}, \begin{pmatrix} 4 \\ -1 \end{pmatrix}, \begin{pmatrix} -2 \\ 2 \end{pmatrix} $$

    위의 3개 벡터는 정리 8 에 의해 일차 종속이다. 각 벡터 성분이 2 개인데 3 개의 벡터가 집합에 포함되기 때문이다. 이때 어떤 벡터도 다른 벡터의 스칼라곱이 아님을 유의하자.

!!! tldr ""

    **Theorem 9** $\mathbb{R}^n$에 속하는 집합 $S = \{v_1, \dots, v_p\}$ 가 영벡터를 포함하면 $S$ 는 일차 종속이다.

- 증명 

    벡터의 한 요소 $v_1$ 을  $v_1 = 0$ 이라 가정하면, $cv_1 + 0v2 + \dots + 0v_p = 0 (c\ne0)$ 이 성립한다. 즉 일차 종속이다. 

## 선형변환(linear transformation) 입문

!!! tldr ""

    선형변환 $T$ : $\mathbb{R}^n$ 에서 $\mathbb{R}^m$ 으로의 변환 $T$ 는 $\mathbb{R}^n$ 에 속하는 모든 벡터에 $\mathbb{R}^m$ 에 속하는 벡터 $T(x)$ 를 각각 부여하는 규칙이다.



!!! tldr ""

    정의역(domain) : 선형변환 $T$ 의 정의에서 집합 $\mathbb{R}^n$ 을 $T$ 의 정의역이라 한다.



!!! tldr ""

    공역(codomain) : 선형변환 $T$ 의 정의에서 집합 $\mathbb{R}^m$ 을 $T$ 의 공역이라 한다.

- 선형변환 $T$ 의 정의역과 공역을 

    $$T: \mathbb{R}^n \to \mathbb{R}^m$$

    로 표현하면 $T$ 의 정의역이 $\mathbb{R}^n$ 이고 공역이 $\mathbb{R}^m$ 임을 나타낸다.

!!! tldr ""

    상(image) : 선형변환 $T$ 의 정의에서 $\mathbb{R}^n$ 에 속하는 $x$ 에 대하여 $\mathbb{R}^m$ 의 벡터 $T(x)$ 를 $x$ 의 상(image) 이라 한다.

- 함수값이라고도 한다.

!!! tldr ""

    치역(range) : 선형변환 $T$ 의 정의에서 모든 상 $T(x)$ 들의 집합을 $T$ 의 치역(range) 라 한다.

- 그러므로 치역은 공역의 부분집합이 된다.

### 행렬변환

!!! tldr ""

    행렬변환 : $A$ 가 $m \times n$ 일 때, $\mathbb{R}^n$ 에 속하는 각 $x$ 에 대하여 $T(x)$ 는 $Ax$ 로 계산된다.

- 행렬변환을 간단하게 $x \mapsto Ax$ 로 나타낸다. 

- 예시 

    다음과 같이 주어진 행렬을 생각하자. 

    $$ A = \begin{pmatrix} 1 & -3 \\ 3 & 5 \\ -1 & 7 \\ \end{pmatrix}, u = \begin{pmatrix} 2 \\ -1 \\ \end{pmatrix}, b = \begin{pmatrix} 3 \\ 2 \\ -5 \\ \end{pmatrix} $$

    그리고 변환 $T: \mathbb{R}^2 \to \mathbb{R}^3$ 을 다음과 같이 $T(x) = Ax$ 로 정의하자. 

    $$ T(x) = Ax = \begin{pmatrix} 1 & -3 \\ 3 & 5 \\ -1 & 7 \\ \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ \end{pmatrix} = \begin{pmatrix} x_1 - 3x_2 \\ 3x_1 + 5x_2 \\ -x_1 + 7x_2 \\ \end{pmatrix} $$

    변환 $T$ 에 의한 $u$ 의 상 $T(u)$ 를 구하자.

    $$ T(u) = Au = \begin{pmatrix} 1 & -3 \\ 3 & 5 \\ -1 & 7 \\ \end{pmatrix} \begin{pmatrix} 2 \\ -1 \\ \end{pmatrix} = \begin{pmatrix} 5 \\ 1 \\ -9 \\ \end{pmatrix} $$

    이제 $T$ 에 의한 상이 $b$ 가 되는 $\mathbb{R}^2$ 의 벡터 $x$ 를 구해보자. 

    $T(x) = b$ 의 해 $x$ 를 구한다. 즉, 아래와 같은 $Ax = b$ 를 풀자. 

    $$ \begin{pmatrix} 1 & -3 \\ 3 & 5 \\ -1 & 7 \\ \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ \end{pmatrix} = \begin{pmatrix} 3 \\ 2 \\ -5 \\ \end{pmatrix} $$

    위 행렬방정식의 첨가행렬을 다음과 같이 행 축약하자. 

    $$ \begin{pmatrix} 1 & -3 & 3 \\ 3 & 5 & 2 \\ -1 & 7 & -5 \\ \end{pmatrix} \sim \begin{pmatrix} 1 & 0 & 1.5 \\ 0 & 1 & -.5 \\ 0 & 0 & 0 \\ \end{pmatrix} $$

    따라서 $x_1 = 1.5, x_2 = -.5$ 이고, $x = \begin{pmatrix}1.5\\-.5\end{pmatrix}$ 이다. ($T$ 에 의한 이 $x$ 의 상은 주어진 벡터 $b$ 이다)

### 선형변환

!!! tldr ""

    선형(linear) : 변환 $T$ 가 다음을 만족하면 선형(linear) 라 한다. 
    
    1. $T$ 의 정의역에 속하는 모든 $u, v$ 에 대하여 $T(u + v) = T(u) + T(v)$
    
    2. 모든 스칼라 $c$ 와 $T$ 의 정의역에 속하는 모든 $u$ 에 대하여 $T(cu) = cT(u)$



!!! tldr ""

    선형변환의 성질
    
    3. $T(0) = 0$
    
    4. $T$ 의 정의역에 속하는 모든 벡터 $u, v$ 와 모든 스칼라 $c, d$ 에 대하여 다음이 성립한다. 
    
        $$T(cu + dv) = cT(u) + dT(v)$$
    
    5. 중첩원리 
    
        $$T(c_1v_1 + \dots + c_pv_p) = c_1T(v_1) + \dots + c_pT(v_p)$$

## 선형변환 행렬

!!! tldr ""

    선형변환 $T$ 가 결정되는 조건 : 선형변환 $T$ 는 $n \times n$ 항등행렬 $I_n$ 의 열들에 어떤 작용을 하는가에 의해 완전히 결정된다.

- 다음 예시를 보면 $T(e_1), T(e_2), \dots, T(e_n)$ 에 의해 선형변환 $T$ 가 완전히 결정됨을 알 수 있다.

- 예시 

    $I_2=\begin{pmatrix}1 & 0 \\ 0 & 1\end{pmatrix}$ 의 열은 $e_1 = \begin{pmatrix}1 \\ 0\end{pmatrix}$,$e_2=\begin{pmatrix}0\\1\end{pmatrix}$ 이다. $T$ 는 $\mathbb{R} ^2$ 에서 $\mathbb{R} ^3$ 으로의 선형변환으로 다음을 만족한다. 

    $$ T(e_1)= \begin{pmatrix} 5\\-7\\2 \end{pmatrix} $$

    $$ T(e_2)= \begin{pmatrix} -3\\8\\0 \end{pmatrix} $$

    이때 $\mathbb{R} ^2$ 에 속하는 임의의 벡터 $x$ 의 상을 얻는 식을 구해보자. $x$ 는 다음과 같이 쓸 수 있다.

    $$ x = \begin{pmatrix} x_1\\x_2 \end{pmatrix} = x_1 \begin{pmatrix} 1\\0 \end{pmatrix} + x_2\begin{pmatrix} 0\\1 \end{pmatrix} = x_1e_1 + x_2e_2 $$

    $T$ 는 선형변환이므로 다음을 얻는다. 

    $$T(x) = T(x_1e_1 + x_2e_2) = x_1T(e_1) + x_2T(e_2)$$

    $$ = x_1 \begin{pmatrix} 5\\-7\\2 \end{pmatrix} +x_2 \begin{pmatrix} -3\\8\\0 \end{pmatrix} = \begin{pmatrix} 5x_1 - 3x_2\\ -7x_1 + 8x_2\\ 2x_1 + 0\\ \end{pmatrix} $$

!!! tldr ""

    **Theorem 10** $T: \mathbb{R} ^n \to \mathbb{R} ^m$ 을 선형변환이라 하면 다음을 만족하는 유일한 행렬 $A$ 가 존재한다.
    
    $$ T(x) = Ax, (x \in \mathbb{R} ^n ) $$
    
    $e_j \in \mathbb{R} ^n$ 이 항등행렬의 $j$ 번째 열이라 하면 $A$ 는 $j$번째 열이 벡터 $T(e_j)$ 인 $m \times n$ 행렬이며 다음과 같이 쓸 수 있다. 
    
    $$ A = \begin{pmatrix} T(e_1) & \dots & T(e_n) \end{pmatrix} $$



!!! tldr ""

    선형변환 $T$ 에 대한 표준행렬(standard matrix for the linear transformation T) : 위와 같은 정리 10 에서의 행렬 A 를 선형변환 $T$ 에서의 표준행렬이라 한다.

- 예제 

    팽창변환 $T(x) = 3x, x \in \mathbb{R} ^2$ 에 대한 표준행렬을 구하자.

    정의에 따라 벡터 $T(e_1), T(e_2)$ 을 열로 갖는 행렬 $A$ 를 구하면 된다. 

    $$ T(e_1) = 3e_1 = \begin{pmatrix} 3 \\ 0 \end{pmatrix}, T(e_2) = 3e_2 = \begin{pmatrix} 0 \\ 3 \end{pmatrix} $$

    $$ A = \begin{pmatrix} 3 & 0\\ 0 & 3\\ \end{pmatrix} $$

### 존재성과 유일성 문제

!!! tldr ""

    전사 변환(onto) : $\mathbb{R} ^m$ 에 속하는 각각의 $b$ 가 $\mathbb{R} ^n$ 에 속하는 적어도 한 $x$ 의 상이면, 변환 $T: \mathbb{R} ^n \to \mathbb{R} ^m$ 을 $\mathbb{R} ^m$ 으로의 전사(onto) 변환이라 한다.

- 즉 치역이 공역 $\mathbb{R} ^m$ 전체가 되면 $T$ 는 $\mathbb{R} ^m$ 으로의 전사변환이다.

!!! tldr ""

    일대일 변환(one-to-one) : $\mathbb{R} ^m$ 에 속하는 각각의 $b$ 가 많아야 한 $x \in \mathbb{R} ^n$ 의 상이면, 변환 $T: \mathbb{R} ^n \to \mathbb{R} ^m$ 을 $\mathbb{R} ^m$ 으로의 일대일 변환(one-to-one) 이라 한다.

- 즉 $\mathbb{R} ^m$ 에 속하는 임의의 $b$ 에 대하여 $T(x) = b$ 를 만족하는 유일한 해가 존재하거나 하나도 없다면 $T$ 는 $\mathbb{R} ^m$ 으로의 일대일 변환이다.

!!! tldr ""

    **Theorem 11** : $T: \mathbb{R} ^n \to  \mathbb{R} ^m$ 이 선형변환 일 때, $T$ 가 일대일이 될 필요충분조건은 방정식 $T(x) = 0$ 이 자명한 해만을 갖는 것이다.


!!! tldr ""

    **Theorem 12** : $T: \mathbb{R} ^n \to  \mathbb{R} ^m$ 이 선형변환 이고, $A$ 가 $T$ 에 대한 표준행렬이면 다음이 성립한다.

1. $T$ 가 $\mathbb{R} ^n$ 에서 $\mathbb{R} ^m$ 으로의 전사변환이기 위한 필요충분조건은 $A$ 의 열들이 $\mathbb{R} ^m$ 을 생성한다는 것이다. 

2. $T$ 가 일대일 대응이기 위한 필요충분조건은 $A$ 의 열들이 일차 독립인 것이다. 
