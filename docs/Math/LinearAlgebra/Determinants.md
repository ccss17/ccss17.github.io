!!! info "ref"

    Stephen H. Friedberg, Linear Algebra, 4th Edition

# 2차 정사각행렬의 행렬식

!!! tldr "$2 \times 2$ 행렬의 행렬식"

    $2 \times 2$ 행렬 $A = \begin{pmatrix} a&b\\ c&d\\ \end{pmatrix}$ 에 대하여 행렬식 $\det: \mathbf{M}_{2 \times 2}(\mathbf{F} ) \to \mathbf{F}$ 은 다음과 같이 정의된 함수이다.

    $$ \det (A) = ad - bc $$

!!! tldr ""

    함수 $\det : \mathbf{M}_{2 \times 2}(\mathbf{F} ) \to \mathbf{F}$ 은 선형이 아니다.

- 증명

    행렬 $A = \begin{pmatrix} 1&2\\ 3&4\\ \end{pmatrix}, B = \begin{pmatrix} 3&2\\ 6&4\\ \end{pmatrix}, A+B = \begin{pmatrix} 4&4\\ 9&8\\ \end{pmatrix}$ 에 대하여 다음이 성립한다.

    $$ \det(A) = -2, \det(B) = 0 , \det(A+B) = -4$$

    따라서 다음이 성립한다.

    $$\det (A+B) \neq \det (A) + \det (B)$$

    그러므로 함수 $\det$ 은 선형이 아니다. ■ 

!!! tldr "정리 4.1"

    함수 $\det: \mathbf{M}_{2 \times 2}(\mathbf{F} ) \to \mathbf{F}$ 는 $2 \times 2$ 행렬의 한 행이 고정되었을 때, 나머지 행에 대하여 선형이다. 즉, $u, v, w \in \mathbf{F} ^{2}$ 와 스칼라 $k$ 에 대하여 다음이 성립한다. 

    1. $\det \begin{pmatrix} u+kv\\ w\\ \end{pmatrix} = \det \begin{pmatrix} u\\ w\\ \end{pmatrix} + k \det \begin{pmatrix} v\\ w\\ \end{pmatrix}$

    2. $\det \begin{pmatrix} w\\ u+kv\\ \end{pmatrix} = \det \begin{pmatrix} w\\ u\\ \end{pmatrix} + k \det \begin{pmatrix} w\\ v\\ \end{pmatrix}$

- 이 정리는 함수 $\det: \mathbf{M}_{2 \times 2}(\mathbf{F} ) \to \mathbf{F}$ 가 선형이 아니지만, 그래도 선형적 성질을 갖는다는 것을 말해준다.

- 증명

    1:

    $u = (a_1, a_2), v = (b_1, b_2), w = (c_1, c_2) \in \mathbf{F} ^{2}$ 와 스칼라 $k$ 에 대하여 다음이 성립한다. 

    $$ \begin{equation}\begin{split} \det \begin{pmatrix} u\\ w\\ \end{pmatrix} + k \det \begin{pmatrix} v\\ w\\ \end{pmatrix} &= \det \begin{pmatrix} a_1&a_2\\ c_1&c_2\\ \end{pmatrix} + k \det \begin{pmatrix} b_1&b_2\\ c_1&c_2\\ \end{pmatrix}   \\ &= (a_1 + kb_1)c_2 - (a_2 + kb_2)c_1 \\ &= \det \begin{pmatrix} a_1+kb_1&a_2+kb_2\\ c_1&c_2\\ \end{pmatrix} \\ &= \det \begin{pmatrix} u+kv\\ w\\ \end{pmatrix} \end{split}\end{equation} \tag*{} $$

    2:

    1) 과 비슷하게 증명된다. ■ 

!!! tldr "정리 4.2"

    행렬 $A \in \mathbf{M}_{2 \times 2}(\mathbf{F} )$ 에 대하여 다음은 동치이다. 

    1. $\det(A) \neq 0$

    2. $A$ 는 가역이고, $A ^{-1} = \dfrac{1}{\det(A) }\begin{pmatrix} A_{22}&-A_{12}\\ -A_{21}&A_{11}\\ \end{pmatrix}$ 이다.

- 증명

    $\det(A) \neq 0$ 이면 다음과 같이 정의된 행렬 $M$ 에 대하여 $AM=MA=I$ 가 성립함을 쉽게 확인할 수 있다. 

    $$ M = \frac{1}{\det(A) } \begin{pmatrix} A_{22}&-A _{12}\\ -A_{21}&A _{11}\\ \end{pmatrix} $$

    이는 $A$ 가 가역이고 $M = A ^{-1}$ 임을 뜻한다. ▲ 

    역으로 다음과 같은 가역행렬 $A$ 의 존재를 가정하자.

    $$ A = \begin{pmatrix} A _{11}&A _{12}\\ A _{21}&A _{22}\\ \end{pmatrix} $$

    [$2 \times 2$ 행렬 $A$ 가 가역이면 $\text{rank} (A) = 2$](../MatrixOperation/#54a88bd9a) 이다. 이는 $A _{11} \neq 0 \lor A _{21} \neq 0$ 을 뜻한다. $A _{11} \neq 0$ 를 가정하면 $A$ 에 기본연산을 적용하여 다음 행렬을 얻는다.

    $$ \begin{pmatrix} A _{11}& A _{12}\\ 0& A _{22} - \dfrac{A _{12} A _{21}}{A _{11}}\\ \end{pmatrix}$$

    [정리 3.4 따름정리](../MatrixOperation/#108500177) 에 의하여 기본연산은 행렬의 랭크를 보존한다. 이는 다음을 뜻한다.

    $$A _{22} - \dfrac{A _{12} A _{21}}{A _{11}} \neq 0$$

    즉, $\det(A) = A _{11}A _{22} - A _{12}A _{21} \neq 0$  이다. $A _{21} \neq 0$ 를 가정해도 비슷한 논리로 $\det(A) \neq 0$ 를 얻는다. ■ 

## 평행사변형의 넓이

이 절은 $2 \times 2$ 행렬의 행렬식을 기하학으로 특수화했을 때 어떤 의미를 가지는지 알아본다.

!!! tldr "각(angle) 의 정의"

    $\R ^{2}$ 의 두 벡터의 각은 같은 크기와 방향을 가지고 시점이 원점인 두 벡터가 이루는 각이다.

- 예시 

    다음과 그림에서 왼쪽 두 벡터가 이루는 각은 같은 크기와 방향을 가지고 시점이 원점인 두 벡터가 이루는 각이다.

    ![image](https://user-images.githubusercontent.com/16812446/127306408-3ff07c6f-57a1-4658-a57a-bbde4e5e5878.png)

!!! tldr "향(orientation) 의 정의"

    $\beta =\{u,v\}$ 가 $\R ^{2}$ 의 순서기저일 때 $\beta$ 의 향은 다음과 같은 실수이다. 

    $$ \mathcal{O} \begin{pmatrix} u\\ v\\ \end{pmatrix} = \dfrac{\det \begin{pmatrix} u\\ v\\ \end{pmatrix} }{\bigg |\det \begin{pmatrix} u\\ v\\ \end{pmatrix} \bigg |} = \pm 1 $$

- [이 정리](../MatrixOperation/#c2617fe5d)와 정리 4.2 에 의하여 위 식의 분모는 $0$ 이 아니다. 그러므로 $\mathcal{O} \begin{pmatrix} u\\ v\\ \end{pmatrix} = \pm 1$ 이다.

- [$\{u, v\}$ 가 일차종속(서로 평행)이면 행렬 $\begin{pmatrix} u\\ v\\ \end{pmatrix}$ 가 가역이 아니라서](../MatrixOperation/#c2617fe5d) $\det \begin{pmatrix} u\\ v\\ \end{pmatrix} = 0$ 이지만 편의상 $\{u, v\}$ 가 일차종속이면 $\mathcal{O} \begin{pmatrix} u\\ v\\ \end{pmatrix} = 1$ 으로 정의한다.

!!! tldr ""

    $$ \mathcal{O} \begin{pmatrix} e_2\\ e_1\\ \end{pmatrix} = -1 $$

    $$ \mathcal{O} \begin{pmatrix} e_1\\ e_2\\ \end{pmatrix} = 1 $$

- 증명

!!! tldr "오른손 좌표계(right-handed coordinate system) 의 정의"

    $\R ^{2}$ 의 순서기저 $\{u, v\}$ 에 대하여 벡터 $u$ 를 시계 반대방향으로 $\theta (0 < \theta < \pi)$ 만큼 회전하여 벡터 $v$ 에 포갤 수 있으면 좌표계 $\{u, v\}$ 는 오른손 좌표계이다.

- 예시

    ![image](https://user-images.githubusercontent.com/16812446/127310867-dd35e776-5d31-49fd-8df5-b4e8ac3a6b56.png)

!!! tldr "왼손 좌표계(left-handed coordinate system) 의 정의"

    $\R ^{2}$ 의 순서기저 $\{u, v\}$ 에 대하여 벡터 $u$ 를 시계 방향으로 $\theta (0 < \theta < \pi)$ 만큼 회전하여 벡터 $v$ 에 포갤 수 있으면 좌표계 $\{u, v\}$ 는 왼손 좌표계이다.

- 예시 

    ![image](https://user-images.githubusercontent.com/16812446/127310881-e48495a7-ae4c-4c4d-a56f-68597d8584c1.png)

!!! tldr ""

    행렬식 $\det: \mathbf{M}_{2 \times 2}(\mathbf{F} ) \to \mathbf{F}$ 와 행렬 $A, B \in \mathbf{M}_{2 \times 2}(\mathbf{F} )$ 대하여 다음이 성립한다. 

    $$ \det(AB) = \det(A) \det(B) $$
    
- 증명

!!! tldr "문제 4.1-11"

    함수 $\delta : \mathbf{M}_{2 \times 2}(\mathbf{F} ) \to \mathbf{F}$ 는 다음을 만족한다.

    1. 행렬의 한 행이 고정되어 있을 때, 나머지 행에 대하여 $\delta$ 는 선형함수이다.

    2. 행렬 $A \in \mathbf{M}_{2 \times 2}(\mathbf{F} )$ 의 두 행이 같으면 $\delta (A) = 0$ 이다.

    3. $\delta (I_2) = 1$

    함수 $\delta$ 에 대하여 다음이 성립한다.

    1. 기본행렬 $E \in \mathbf{M}_{2 \times 2}(\mathbf{F} )$ 에 대하여 $\delta (E) = \det(E)$ 이다.

    2. 행렬 $A \in \mathbf{M}_{2 \times 2}(\mathbf{F} )$, 기본행렬 $E \in \mathbf{M}_{2 \times 2}(\mathbf{F} )$ 에 대하여 $\delta (EA) = \delta (E) \delta (A)$ 이다.

- 증명

    성질 1) 로부터 다음이 성립한다.

    $$ \delta \begin{pmatrix} a&b\\ c&d\\ \end{pmatrix} = \delta \begin{pmatrix} a&0\\ c&d\\ \end{pmatrix} + \delta \begin{pmatrix} 0&b\\ c&d\\ \end{pmatrix} = a\delta \begin{pmatrix} 1&0\\ c&d\\ \end{pmatrix} + b\delta \begin{pmatrix} 0&1\\ c&d\\ \end{pmatrix} $$

    이때 성질 1), 2), 3) 으로부터 다음이 성립한다.

    $$ a\delta \begin{pmatrix} 1&0\\ c&d\\ \end{pmatrix} = a\delta \begin{pmatrix} 1&0\\ c&0\\ \end{pmatrix} + a\delta \begin{pmatrix} 1&0\\ 0&d\\ \end{pmatrix} = ac\delta \begin{pmatrix} 1&0\\ 1&0\\ \end{pmatrix} + ad\delta \begin{pmatrix} 1&0\\ 0&1\\ \end{pmatrix} = 0 + ad $$

    $$ b\delta \begin{pmatrix} 0&1\\ c&d\\ \end{pmatrix} = b\delta \begin{pmatrix} 0&1\\ c&0\\ \end{pmatrix} + b\delta \begin{pmatrix} 0&1\\ 0&d\\ \end{pmatrix} = bc\delta \begin{pmatrix} 0&1\\ 1&0\\ \end{pmatrix} + bd\delta \begin{pmatrix} 0&1\\ 0&1\\ \end{pmatrix} = bc \delta \begin{pmatrix} 0&1\\ 1&0\\ \end{pmatrix} + 0 $$

    또한 성질 1), 2), 3) 으로부터 다음이 성립한다.

    $$ \begin{pmatrix} 1&1\\ 1&1\\ \end{pmatrix} = \begin{pmatrix} 1&0\\ 1&1\\ \end{pmatrix}+ \begin{pmatrix} 0&1\\ 1&1\\ \end{pmatrix} = \begin{pmatrix} 1&0\\ 0&1\\ \end{pmatrix}+ \begin{pmatrix} 1&0\\ 1&0\\ \end{pmatrix}+ \begin{pmatrix} 0&1\\ 1&0\\ \end{pmatrix} + \begin{pmatrix} 0&1\\ 0&1\\ \end{pmatrix}  = 1 + 0 + \begin{pmatrix} 0&1\\ 1&0\\ \end{pmatrix} + 0 = 0 $$

    그러므로 다음을 얻는다. 

    $$ \delta \begin{pmatrix} a&b\\ c&d\\ \end{pmatrix} = ad - bc $$

    그러므로 $\delta = \det$ 이다. 그러므로 $A \in \mathbf{M}_{2 \times 2}(\mathbf{F}) : \delta (A) = \det(A)$ 이다. 조건 1) 은 이것의 특수한 경우이다. ▲ 

    조건 2) 는 $\det(AB) = \det(A) \det(B)$ 에서 바로 나온다. ■ 

    > 증명하려 했는데 결국 실패하고 솔루션을 찾아봤다. 솔루션에서는 내가 증명에 있어서 전혀 상관없겠다고 직관적으로 판단한 스칼라에 대한 선형이라는 조건을 증명의 첫걸음으로 삼았었다. 증명에 실패한 원인이 내 직관에 의지하여 이 단서를 더 연구하면 문제가 풀릴 것 같다는 것에 매몰되었고 내 직관에 끌리지 않는 단서는 아무런 연구도 하지 않은 것이었다. 직관에 의지하지 않고 객관적으로 연관된 모든 단서를 충분하고 공평하게 연구했으면 스스로 풀 수도 있었을듯.

!!! tldr "문제 4.1-12"

    문제 4.1-11 의 함수 $\delta$ 와 $A \in \mathbf{M}_{2 \times 2}(\mathbf{F} )$ 에 대하여 $\delta (A) = \det(A)$ 이다.

- 증명

    문제 4.1-11 의 증명에 의하여 증명이 끝난다.

!!! tldr ""

    $\R ^{2}$ 의 순서기저 $\{u, v\}$ 에 대하여 다음은 동치이다.

    $$ \mathcal{O}\begin{pmatrix} u\\ v\\ \end{pmatrix} = 1\iff \{u, v\} \text{ is right-handed coordinate system } $$

- 증명

!!! tldr "평행사변형(parallelogram) 의 정의"

    원점을 시점으로 하는 벡터 $u, v \in \R ^{2}$ 에 대하여 이웃한 두 변 $u, v$ 를 가지는 평행사변형을 $u, v$ 의 평행사변형이라 한다.

- $\{u, v\}$ 가 일차종속(서로 평행)이면 $u, v$ 의 평행사변형은 선분이 된다.

- 예시

    ![image](https://user-images.githubusercontent.com/16812446/127340680-ef926a8b-8e2b-41be-8a98-d5c00212fb88.png)

!!! tldr ""

    $u, v$ 의 평행사변형의 넓이는 $\bigg |\det\begin{pmatrix} u\\ v\\ \end{pmatrix} \bigg |$ 이다.

- 예시 

    $u = (-1, 5), v = (4, -2)$ 의 평행사변형의 넓이는 다음과 같다. 

    $$ \bigg |\det \begin{pmatrix} u\\ v\\ \end{pmatrix}\bigg | = \bigg |\det \begin{pmatrix} -1&5\\ 4&-2\\ \end{pmatrix} \bigg | = 18 $$

- 다음 증명은 이 정리가 $\R ^{n}$ 에서도 성립함을 유추할 수 있게 해준다.

- 증명

    $u, v$ 의 평행사변형의 넓이를 $\mathcal{A}\begin{pmatrix} u\\ v\\ \end{pmatrix}$ 라고 두면 향(orientation)의 정의에 의하여 본 정리는 다음과 같다.

    $$ \mathcal{A}\begin{pmatrix} u\\ v\\ \end{pmatrix} = \bigg |\det\begin{pmatrix} u\\ v\\ \end{pmatrix} \bigg | = \mathcal{O}\begin{pmatrix} u\\ v\\ \end{pmatrix} \cdot \det\begin{pmatrix} u\\ v\\ \end{pmatrix} $$

    $\mathcal{O}\begin{pmatrix} u\\ v\\ \end{pmatrix} = \pm 1$ 이므로 이것을 곱한 식인 다음을 증명해도 된다.

    $$ \mathcal{O}\begin{pmatrix} u\\ v\\ \end{pmatrix} \mathcal{A}\begin{pmatrix} u\\ v\\ \end{pmatrix} = \det \begin{pmatrix} u\\ v\\ \end{pmatrix} $$

    이때 $\delta \begin{pmatrix} u\\ v\\ \end{pmatrix} =\mathcal{O}\begin{pmatrix} u\\ v\\ \end{pmatrix} \mathcal{A}\begin{pmatrix} u\\ v\\ \end{pmatrix}$ 라고 정의한 다음 $\delta$ 가 문제 4.1-11 에서의 3 가지 성질을 만족함을 보이면 문제 4.1-12 에 의하여 $\delta = \det$ 이 증명되어 모든 증명이 끝난다. ▲ 

    먼저 벡터 $u, v$ 와 스칼라 $c$ 에 대하여 성질 1) 의 스칼라 곱이 보존됨을 성립함을 보이자. 즉, 다음을 보이자.

    $$ \delta \begin{pmatrix} u\\ cv\\ \end{pmatrix} = c \delta \begin{pmatrix} u\\ v\\ \end{pmatrix} $$

    $c = 0$ 이면 $\delta \begin{pmatrix} u\\ cv\\ \end{pmatrix} = \mathcal{O}\begin{pmatrix} u\\ 0\\ \end{pmatrix} \mathcal{A}\begin{pmatrix} u\\ 0\\ \end{pmatrix} = 1 \cdot 0 = 0$ 이므로 성립한다. $\begin{pmatrix} u\\ 0\\ \end{pmatrix}$ 가 일차종속이므로 $\mathcal{O}$ 가 $1$ 로 정의되고, $u, 0$ 의 평행사변형의 넓이는 $0$ 이기 때문이다.

    $c \neq 0$ 인 경우를 살펴보자. $u, v$ 의 평행사변형의 넓이와 $u, cv$ 의 평행사변형의 넓이의 관계는 이렇다. 두 벡터 $u, v$ 가 이루는 각 $\theta = \arccos \bigg (\dfrac{a \cdot b}{\|a\|\|b\|}\bigg )$ 에 대하여 평행사변형의 높이는 $\|u\| \sin \theta$ 이다. 그러므로 평행사변형의 넓이는 밑변 $\|v\|$ 과 높이를 곱하여 $\mathcal{A}\begin{pmatrix} u\\ v\\ \end{pmatrix} = \|v\|\|u\| \sin \theta$ 이다. 반면 $u, cv$ 의 평행사변형의 넓이는 밑변 $v$ 가 $cv$ 로 변형된 것이므로 $\|cv\|\|u\| \sin \theta = |c|\|v\|\|u\| \sin \theta= |c| \mathcal{A}\begin{pmatrix} u\\ v\\ \end{pmatrix}$ 이다. 그러므로 $\mathcal{A}\begin{pmatrix} u\\ cv\\ \end{pmatrix} = |c| \mathcal{A}\begin{pmatrix} u\\ v\\ \end{pmatrix}$ 이다. 

    $u, v$ 의 평행사변형의 향과 $u, cv$ 의 평행사변형의 향의 관계는 이렇다. $u = (a_1, a_2), v = (b_1, b_2)$ 로 두면 $\det \begin{pmatrix} u\\ v\\ \end{pmatrix} = a_1b_2 - a_2b_1$ 이므로 다음이 성립한다. 

    $$ \mathcal{O}\begin{pmatrix} u\\ v\\ \end{pmatrix} = \dfrac{a_1b_2 - a_2b_1}{|a_1b_2 - a_2b_1|}
    $$

    $$ \mathcal{O}\begin{pmatrix} u\\ cv\\ \end{pmatrix} = \dfrac{ca_1b_2 - ca_2b_1}{|ca_1b_2 - ca_2b_1|} = \frac{c}{|c|}\dfrac{a_1b_2 - a_2b_1}{|a_1b_2 - a_2b_1|} $$

    그러므로 $\mathcal{O}\begin{pmatrix} u\\ cv\\ \end{pmatrix} = \dfrac{c}{|c|}\mathcal{O}\begin{pmatrix} u\\ v\\ \end{pmatrix}$ 이다. 따라서 다음이 성립한다. 

    $$ \delta \begin{pmatrix} u\\ cv\\ \end{pmatrix} = \mathcal{O}\begin{pmatrix} u\\ cv\\ \end{pmatrix}\mathcal{A}\begin{pmatrix} u\\ cv\\ \end{pmatrix} = \frac{c}{|c|}\mathcal{O}\begin{pmatrix} u\\ v\\ \end{pmatrix}|c| \mathcal{A}\begin{pmatrix} u\\ v\\ \end{pmatrix} = c \cdot  \mathcal{O}\begin{pmatrix} u\\ v\\ \end{pmatrix}\mathcal{A}\begin{pmatrix} u\\ v\\ \end{pmatrix} = c \cdot  \delta \begin{pmatrix} u\\ v\\ \end{pmatrix} $$

    이로써 $\delta$ 가 성질 1) 의 스칼라 곱에 대한 선형성을 만족한다는 것이 증명되었다. ▲ 

    같은 변으로 구성된 평행사변형은 선분이 되어 넓이가 $0$ 이 된다. 즉, $\mathcal{A}\begin{pmatrix} u\\ u\\ \end{pmatrix} = 0$ 이다. 그러므로 다음이 성립한다. 

    $$ \delta \begin{pmatrix} u\\ u\\ \end{pmatrix} = \mathcal{O}\begin{pmatrix} u\\ u\\ \end{pmatrix} \mathcal{A}\begin{pmatrix} u\\ u\\ \end{pmatrix} = 0 $$

    이로써 $\delta$ 가 성질 2) 를 만족한다는 것이 증명되었다.  ▲ 

    이제 성질 1) 의 벡터합을 증명하자. 즉 $u, v_1, v_2 \in \R ^{2}$ 에 대하여 다음이 성립함을 보이자. 

    $$ \delta \begin{pmatrix} u\\ v_1 + v_2\\ \end{pmatrix} = \delta \begin{pmatrix} u\\ v_1\\ \end{pmatrix} + \delta \begin{pmatrix} u\\ v_2\\ \end{pmatrix} $$

    $u = 0$ 이면 평행사변형의 넓이가 $0$ 이 되므로 자명하게 성립한다. $u \neq 0$ 를 가정하자. $u$ 와 일차독립인 벡터 $w \in \R ^{2}$ 를 아무거나 선정하면 $\dim (\R ^{2}) = 2$ 이므로 [정리 1.10 따름정리 2](../VectorSpace/#cd7879a47) 에 의하여 $\{u, w\}$ 는 $\R ^{2}$ 의 기저가 된다. 그러므로 $i \in \{1, 2\}$ 에 대하여 다음을 만족하는 스칼라 $a_i, b_i$ 가 존재한다.

    $$ v_i = a_iu + b_iw $$

    그러므로 성질 2) 에 의하여 다음이 성립한다. 

    $$ \begin{equation}\begin{split} \delta \begin{pmatrix} u\\ v_1 + v_2\\ \end{pmatrix} &= \delta \begin{pmatrix} u\\ (a_1+a_2)u + (b_1+b_2)w\\ \end{pmatrix} = (b_1 + b_2) \begin{pmatrix} u\\ w\\ \end{pmatrix}\\ &= \delta \begin{pmatrix} u\\ a_1u + b_1w\\ \end{pmatrix} + \delta \begin{pmatrix} u\\ a_2u + b_2w\\ \end{pmatrix} = \delta \begin{pmatrix} u\\ v_1\\ \end{pmatrix} + \delta \begin{pmatrix} u\\ v_2\\ \end{pmatrix} \end{split}\end{equation} \tag*{} $$

    같은 논리로 다음을 증명할 수 있다.

    $$ \delta \begin{pmatrix} v_1 + v_2\\ u\\ \end{pmatrix} = \delta \begin{pmatrix} v_1\\ u\\ \end{pmatrix} + \delta \begin{pmatrix} v_2\\ u\\ \end{pmatrix} \tag*{} $$

    이로써 $\delta$ 가 성질 1) 의 벡터합을 만족한다는 것이 증명되었다. ▲ 

    마지막으로 성질 3) 을 증명하자. $e_1, e_2$ 의 평행사변형은 정사각형이므로 다음이 성립한다. 

    $$ \delta \begin{pmatrix} e_1\\ e_2\\ \end{pmatrix} = \mathcal{O}\begin{pmatrix} e_1\\ e_2\\ \end{pmatrix}\mathcal{A}\begin{pmatrix} e_1\\ e_2\\ \end{pmatrix}= 1 \cdot 1 = 1 $$

    즉, $\delta (I_2) = 1$ 이다. 이로써 모든 증명이 끝났다. ■ 

# n차 정사각행렬의 행렬식

# 행렬식의 성질
