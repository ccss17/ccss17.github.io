# 선형대수학 메모 5

# 5장 - 고윳값과 고유 벡터

## 고윳값과 고유 벡터

- 고유벡터(eigenvector) : $n \times n$ 행렬 $A$ 의 고유 벡터는 어떤 스칼라 $\lambda$ 에 대하여 

  $$ Ax = \lambda x $$

  를 만족하는 영이 아닌 벡터 $x$ 이다. 

  - 예시 

    $$ A = \begin{bmatrix} 1&6\\5&2 \end{bmatrix}, u = \begin{bmatrix} 6\\-5 \end{bmatrix}, v = \begin{bmatrix} 3\\-2 \end{bmatrix} $$

    에서 $u, v$ 가 $A$ 의 고유 벡터인지 확인하자.

    $$ Au = \begin{bmatrix} 1&6\\5&2 \end{bmatrix}\begin{bmatrix} 6\\-5 \end{bmatrix} = \begin{bmatrix} -24\\20 \end{bmatrix} = -4 \begin{bmatrix} 6\\-5 \end{bmatrix} = -4u $$

    $$ Av = \begin{bmatrix} 1&6\\5&2 \end{bmatrix}\begin{bmatrix} 3\\-2 \end{bmatrix} = \begin{bmatrix} -9\\11 \end{bmatrix} \neq \lambda \begin{bmatrix} 3\\-2 \end{bmatrix} $$

    따라서 $u$ 는 $-4$ 에 대응하는 고유벡터이지만
    
    $v$ 는 $Av$ 가 $v$ 의 스칼라배가 아니므로 고유 벡터가 아니다.


- 고윳값(eigenvalue) : $n \times n$ 행렬 $A$ 에서

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

- 고유공간(eigenspace) : 행렬 $A$ 를 고윳값에 대하여 정리한 행렬방정식

  $$ (A - \lambda I)x = 0 $$

  의 해들의 집합은 행렬 $A - \lambda I$ 의 영공간인데, 이 집합을 $\lambda$ 에 대응하는 $A$ 의 고유공간이라 한다. 

  - 예시 

    $$ A = \begin{bmatrix} 4&-1&6\\2&1&6\\2&-1&8 \end{bmatrix} $$

    에서 $2$ 가 $A$ 의 고윳값이라 할 때 고유공간을 찾아보자. 

    $$ A - 2I = \begin{bmatrix} 2&-1&6\\ 2&-1&6\\ 2&-1&6\\ \end{bmatrix} $$

    이므로 $(A-2I)x = 0$ 의 첨가행렬을 행 축소하여 

    $$ \begin{bmatrix} 2&-1&6&0\\ 2&-1&6&0\\ 2&-1&6&0\\ \end{bmatrix} \backsim \begin{bmatrix} 2&-1&6&0\\ 0&0&0&0\\ 0&0&0&0\\ \end{bmatrix} $$

    를 얻는다. 그러므로 $x = \begin{bmatrix} x_1\\x_2\\x_3 \end{bmatrix}$ 에서

    $$ 2x_1 -x_2 + 6x_3 = 0 $$

    을 얻고 $x_2, x_3$ 은 자유변수(독립변수), $x_1$ 은 기본변수(종속변수) 임을 알 수 있다. 

    이제 해집합을 구해보면

    $$ x = \begin{bmatrix} x_1\\x_2\\x_3 \end{bmatrix} = \begin{bmatrix} \frac{1}{2}x_2 - 3x_3\\x_2\\x_3 \end{bmatrix} = x_2 \begin{bmatrix} \frac{1}{2}\\1\\0 \end{bmatrix} + x_3\begin{bmatrix} -3\\0\\1 \end{bmatrix} $$

    이다. $x_2, x_3$ 이 그 어떠한 값이 되든간에 각각

    $$ x_2 \begin{bmatrix} \frac{1}{2}\\1\\0 \end{bmatrix} + x_3\begin{bmatrix} -3\\0\\1 \end{bmatrix} $$

    의 형태로 벡터들에 곱해진다면 $x_1$ 도 알아서 결정되고 행렬방정식 $(A - \lambda I)x = 0$ 이 성립하는 것이다. 

    따라서 영공간, 즉 고유공간은 $\Re ^{3}$ 의 $2$ 차원 부분 공간이며 기저는 

    $$ \Bigg \{ \begin{bmatrix} 1\\2\\0 \end{bmatrix}, \begin{bmatrix} -3\\0\\1 \end{bmatrix} \Bigg \} $$

    이다. 즉 $u = \begin{bmatrix} 1\\2\\0 \end{bmatrix}, v= \begin{bmatrix} -3\\0\\1 \end{bmatrix}$ 라고 할 때

    $$ \text{Span} \{u, v\} $$

    이 고유공간이다. 
