# 고윳값과 고유 벡터

!!! tldr ""

    고유벡터(eigenvector) : $n \times n$ 행렬 $A$ 의 고유 벡터는 어떤 스칼라 $\lambda$ 에 대하여 
    
    $$ Ax = \lambda x $$
    
    를 만족하는 영이 아닌 벡터 $x$ 이다.

- 고유벡터의 정의 $Ax = \lambda x$ 를 $Ax = \lambda E x$ 로 쓰면

    $$ (A- \lambda  E) x = 0 $$

    을 얻는다. 여기에서 $(A- \lambda  E)$ 의 역행렬이 존재하면 양변에 곱하여

    $$ (A- \lambda  E) ^{-1}(A- \lambda  E) x = (A- \lambda  E)^{-1} 0 $$

    $$ x = (A- \lambda  E)^{-1} 0 = 0 $$

    이 된다. 그러나 $x = 0$ 은 $x$ 가 영이 아닌 벡터라는 정의의 조건에 모순되므로 $(A- \lambda  E)$ 가 역행렬을 갖는다는 가정이 틀렸다는 것을 알 수 있다. 

    따라서 고유벡터가 존재하려면 

    $$ \det (A - \lambda E) = 0 $$

    이어야 한다. 

- 예시 

    $$ A = \begin{bmatrix} 1&6\\5&2 \end{bmatrix}, u = \begin{bmatrix} 6\\-5 \end{bmatrix}, v = \begin{bmatrix} 3\\-2 \end{bmatrix} $$

    에서 $u, v$ 가 $A$ 의 고유 벡터인지 확인하자.

    $$ Au = \begin{bmatrix} 1&6\\5&2 \end{bmatrix}\begin{bmatrix} 6\\-5 \end{bmatrix} = \begin{bmatrix} -24\\20 \end{bmatrix} = -4 \begin{bmatrix} 6\\-5 \end{bmatrix} = -4u $$

    $$ Av = \begin{bmatrix} 1&6\\5&2 \end{bmatrix}\begin{bmatrix} 3\\-2 \end{bmatrix} = \begin{bmatrix} -9\\11 \end{bmatrix} \neq \lambda \begin{bmatrix} 3\\-2 \end{bmatrix} $$

    따라서 $u$ 는 $-4$ 에 대응하는 고유벡터이지만

    $v$ 는 $Av$ 가 $v$ 의 스칼라배가 아니므로 고유 벡터가 아니다.

!!! tldr ""

    고윳값(eigenvalue) : $n \times n$ 행렬 $A$ 에서
    
    $$ Ax = \lambda x $$
    
    의 영이 아닌 해, 즉 자명하지 않은(nontrivial) 해인 벡터 $x$ 가 존재할 때 스칼라 $\lambda$ 를 고윳값이라 한다.

- 예시 

    $$ A = \begin{bmatrix} 1&6\\5&2 \end{bmatrix}$$

    의 고윳값이 $7$ 임을 보이자. 

    이것은 다음 등식이 영이 아닌 해를 가지는 것과 동치이다. 

    $$ Ax = 7x $$

    이 등식은 

    $$ (A - 7I)x = 0 $$

    과 같으므로 

    $$ A - 7I = \begin{bmatrix} 1&6\\5&2 \end{bmatrix} - \begin{bmatrix} 7&0\\0&7 \end{bmatrix} = \begin{bmatrix} -6&6\\5&-5 \end{bmatrix} $$

    이다. $A - 7I$ 의 열들은 선형종속이므로 영이 아닌 해를 가진다.

    그러므로 $7$ 은 $A$ 의 고윳값이다. 

> 인공에서 선생님 없는 학습이라 불리는 비지도학습에서 주성분 분석이라는 기법이 사용되는데, 이것으 다차원 데이터를 다루기 쉽게 $2$ 차원이나 $3$ 차원으로 압축하는 방법이다. 데이터가 많이 흩어져 있는 분포 상황에서 문제를 해결하기 위해 고유값과 고유벡터가 사용된다. 

> 또 고유값은 어떤 데이터가 특징을 얼마나 잘 설명할 수 있는지 가늠할 때도 사용된다. 기여율이라는 것은 각 주성분, 즉 고유벡터에 대응되는 고유값을 전체 고유값들의 총합을 나눈것으로 주성분이 데이터를 얼마나 잘 설명할 수 있는지 평가할 때 사용된다.

!!! tldr ""

    고유벡터와 고유값의 기하학적 의미 : 어떤 행렬에 벡터를 곱하는 선형변환 연산을 했을 때 일반적으로 벡터의 방향이 바뀌지만 
    
    고유벡터로 선형변환을 하면 방향이 바뀌지 않거나 역방향이 된다.

- 따라서 고유값은 선형변환 전과 후의 벡터 길이의 비율로 볼 수 있다. 

- 다음 그래프를 보자.

    ![캡처](https://user-images.githubusercontent.com/16812446/79184344-d0920200-7e4e-11ea-836b-867fa2004f8e.PNG)

    벡터 $u$ 를 벡터 $\overrightarrow{AC}, \overrightarrow{AF}$ 로 변환시킨 선형변환은 고유벡터가 사용된 것이고, 고유값이 길이의 비율에 해당한다. 

    벡터 $w$ 를 벡터 $\overrightarrow{AE}$ 로 선형변환시킨 것도 방향이 바뀌지 않았으므로 고유벡터가 사용된 것이다. 

    그러나 벡터 $u, w$ 가 벡터 $c$ 로 선형변환되었다면 방향이 바뀌었으므로 고유벡터가 사용되지 않은 것이다.

!!! tldr ""

    고유공간(eigenspace) : 행렬 $A$ 를 고윳값에 대하여 정리한 행렬방정식
    
    $$ (A - \lambda I)x = 0 $$
    
    의 해들의 집합은 행렬 $A - \lambda I$ 의 영공간인데, 이 집합을 $\lambda$ 에 대응하는 $A$ 의 고유공간이라 한다.

- 예시 

    $$ A = \begin{bmatrix} 4&-1&6\\2&1&6\\2&-1&8 \end{bmatrix} $$

    에서 $2$ 가 $A$ 의 고윳값이라 할 때 고유공간을 찾아보자. 

    $$ A - 2I = \begin{bmatrix} 2&-1&6\\ 2&-1&6\\ 2&-1&6\\ \end{bmatrix} $$

    이므로 $(A-2I)x = 0$ 의 첨가행렬을 행 축소하여 

    $$ \begin{bmatrix} 2&-1&6&0\\ 2&-1&6&0\\ 2&-1&6&0\\ \end{bmatrix} \sim \begin{bmatrix} 2&-1&6&0\\ 0&0&0&0\\ 0&0&0&0\\ \end{bmatrix} $$

    를 얻는다. 그러므로 $x = \begin{bmatrix} x_1\\x_2\\x_3 \end{bmatrix}$ 에서

    $$ 2x_1 -x_2 + 6x_3 = 0 $$

    을 얻고 $x_2, x_3$ 은 자유변수(독립변수), $x_1$ 은 기본변수(종속변수) 임을 알 수 있다. 

    이제 해집합을 구해보면

    $$ x = \begin{bmatrix} x_1\\x_2\\x_3 \end{bmatrix} = \begin{bmatrix} \frac{1}{2}x_2 - 3x_3\\x_2\\x_3 \end{bmatrix} = x_2 \begin{bmatrix} \frac{1}{2}\\1\\0 \end{bmatrix} + x_3\begin{bmatrix} -3\\0\\1 \end{bmatrix} $$

    이다. $x_2, x_3$ 이 그 어떠한 값이 되든간에 각각

    $$ x_2 \begin{bmatrix} \frac{1}{2}\\1\\0 \end{bmatrix} + x_3\begin{bmatrix} -3\\0\\1 \end{bmatrix} $$

    의 형태로 벡터들에 곱해진다면 $x_1$ 도 알아서 결정되고 행렬방정식 $(A - \lambda I)x = 0$ 이 성립하는 것이다. 

    따라서 영공간, 즉 고유공간은 $\mathbb{R} ^{3}$ 의 $2$ 차원 부분 공간이며 기저는 

    $$ \Bigg \{ \begin{bmatrix} 1\\2\\0 \end{bmatrix}, \begin{bmatrix} -3\\0\\1 \end{bmatrix} \Bigg \} $$

    이다. 즉 $u = \begin{bmatrix} 1\\2\\0 \end{bmatrix}, v= \begin{bmatrix} -3\\0\\1 \end{bmatrix}$ 라고 할 때

    $$ \text{Span} \{u, v\} $$

    이 고유공간이다.

!!! tldr ""

    고유방정식(eigenvalue equation) : 행렬 $A$ 에 대한 $\lambda$ 의 방정식
    
    $$ \det (A - \lambda E) = 0 $$
    
    을 고유방정식이라 한다.

- 예시 

    행렬 $A = \begin{bmatrix} 2&4\\-1&-3 \end{bmatrix}$ 의 고유값과 고유벡터를 구해보자. 고유벡터가 존재하려면 

    $$ \det (A - \lambda E) = 0 $$

    이 만족되어야만 한다. 그러므로 

    $$ \det \Bigg ( \begin{bmatrix} 2&4\\-1&-3 \end{bmatrix} - \lambda \begin{bmatrix} 1&0\\0&1 \end{bmatrix} \Bigg ) = 0$$

    $$ \det \begin{pmatrix} 2 - \lambda  & 4\\ -1 & -3 - \lambda \end{pmatrix} = 0 $$

    에서 

    $$ (2- \lambda )(-3 - \lambda ) -(4)(-1) = 0 $$

    $$ \lambda ^{2} + \lambda -2 = 0$$

    $$ (\lambda +2)(\lambda -1) =0 $$

    이다. 따라서 고유값은 

    $$ \therefore \lambda = -2, \lambda = 1 $$

    이다.

    이제 각각의 경우에 고유벡터를 구해보자. 

    $\lambda = -2$ 일 때 

    $$ (A - \lambda E)x = 0 $$

    $$ (A - (-2) E)x = 0 $$

    $$ \begin{bmatrix} 2 - (-2) & 4\\-1 & -3 - (-2) \end{bmatrix}x = \begin{bmatrix} 4&4\\-1&-1 \end{bmatrix}x = 0 $$

    이므로 첨가행렬을 행축약하여 다음과 같은 기약사다리꼴로 만든다.

    $$ \begin{bmatrix} 4&4&0\\-1&-1&0 \end{bmatrix} \sim \begin{bmatrix} 1&1&0\\0&0&0 \end{bmatrix} $$

    그러므로 $x = \begin{bmatrix} x_1\\x_2 \end{bmatrix}$ 일 때 기본변수 $x_1$ 와 자유변수 $x_2$ 은 

    $$ x_1 + x_2 = 0 $$

    의 관계를 가진다. 따라서

    $$ x = \begin{bmatrix} x_1\\x_2 \end{bmatrix} = \begin{bmatrix} -x_2\\x_2 \end{bmatrix} = x_2 \begin{bmatrix} -1\\1 \end{bmatrix} $$ 

    이므로 고유벡터 $x$ 는 $\begin{bmatrix} -1\\1 \end{bmatrix}$ 의 모든 스칼라배 

    $$ \therefore x \in  \text{Span}\bigg \{\begin{bmatrix} -1\\1 \end{bmatrix}\bigg \} $$

    이다.

    $\lambda = 1$ 일 때 

    $$ (A - \lambda E)x = 0 $$

    $$ (A - (1) E)x = 0 $$

    $$ \begin{bmatrix} 2 - (1) & 4\\-1 & -3 - (1) \end{bmatrix}x = \begin{bmatrix} 1&4\\-1&-4 \end{bmatrix}x = 0 $$

    이므로 첨가행렬을 행축약하여 

    $$ \begin{bmatrix} 1&4&0\\-1&-4&0 \end{bmatrix} \sim \begin{bmatrix} 1&4&0\\0&0&0 \end{bmatrix} $$

    을 얻는다. 그러므로 $x = \begin{bmatrix} x_1\\x_2 \end{bmatrix}$ 일 때 기본변수 $x_1$ 와 자유변수 $x_2$ 은 

    $$ x_1 + 4x_2 = 0 $$

    의 관계를 가진다. 따라서

    $$ x = \begin{bmatrix} x_1\\x_2 \end{bmatrix} = \begin{bmatrix} -4x_2\\x_2 \end{bmatrix} = x_2 \begin{bmatrix} -4\\1 \end{bmatrix} $$ 

    이므로 고유벡터 $x$ 는 $\begin{bmatrix} -4\\1 \end{bmatrix}$ 의 모든 스칼라배 

    $$ \therefore x \in  \text{Span}\bigg \{\begin{bmatrix} -4\\1 \end{bmatrix}\bigg \} $$

    이다.
