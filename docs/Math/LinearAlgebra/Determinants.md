!!! info "ref"

    Stephen H. Friedberg, Linear Algebra, 4th Edition

# $2 \times 2$ 행렬의 행렬식

!!! tldr "$2 \times 2$ 행렬의 행렬식"

    $2 \times 2$ 행렬 $A = \begin{pmatrix} a&b\\ c&d\\ \end{pmatrix}$ 에 대하여 행렬식 $\det: \mathbf{M}_{2 \times 2}(\mathbf{F} ) \to \mathbf{F}$ 은 다음과 같이 정의된 함수이다.

    $$ \det (A) = ad - bc $$

## $2 \times 2$ 행렬의 행렬식의 성질

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

# 행렬식의 정의

!!! tldr "$\tilde{A}$ 의 정의"

    $n \geq 2$ 일 때 행렬 $A \in \mathbf{M}_{n \times n}(\mathbf{F} )$ 에 대하여 $A$ 의 $i$ 행과 $j$ 열을 제거하여 얻은 $(n - 1) \times (n - 1)$ 행렬 $\tilde{A} _{ij}$ 라고 한다.

- 예시 

    $$A = \begin{pmatrix} 1&2&3\\ 4&5&6\\ 7&8&9\\ \end{pmatrix} \implies \tilde{A} _{11} = \begin{pmatrix} 5&6\\ 8&9\\ \end{pmatrix}$$

!!! tldr "여인수(cofactor) 의 정의"

    스칼라 $(-1) ^{i+j}\det(\tilde{A}_{ij})$ 를 $A$ 의 $i$ 행 $j$ 열 성분에 대한 여인수라고 한다. 

!!! tldr "여인수 전개(cofactor expansion) 의 정의"

    $A$ 의 $i$ 행에 대한 여인수 전개를 다음과 같이 정의한다.

    $$ \det(A) = \sum_{j=1}^{n}(-1) ^{i + j}A _{ij} \cdot \det(\tilde{A}_{ij}) $$

- 즉, $A$ 의 $i$ 행에 대한 여인수 전개는 $A$ 의 $i$ 행의 각 성분에 여인수를 곱하여 더한 결과이다.

!!! tldr "행렬식(determinant) 의 정의"

    행렬 $A \in \mathbf{M}_{n \times n}(\mathbf{F} )$ 에 대하여 행렬식 $\det: \mathbf{M}_{n \times n}(\mathbf{F} ) \to \mathbf{F}$ 은 다음과 같은 함수이다.

    $$ \det(A) = \begin{cases} A _{11} & n = 1\\ \displaystyle \sum_{j=1}^{n}(-1) ^{1+j}A _{1j} \cdot \det(\tilde{A}_{1j}) &n \geq 2\\ \end{cases} $$

- $A$ 의 $i$ 행 $j$ 열에 대한 여인수를 $c _{ij} = (-1) ^{i + j}\det(\tilde{A}_{ij})$ 로 표기하면 $A$ 의 행렬식을 다음과 같이 표현할 수 있다. 

    $$ \det(A) = \sum_{j=1}^{n}A _{1j}c _{1j} $$

    즉, $A$ 의 행렬식은 $A$ 의 1행의 각 성분에 여인수를 곱하여 더한 결과이다. 이는 행렬의 행렬식이란 1행에 대한 여인수 전개라는 것을 말해준다.

- 예시 

    $A \in \mathbf{M}_{2 \times 2}(\mathbf{F} )$ 에 대한 1행의 여인수 전개는 다음과 같다. 

    $$ \det(A) = A _{11}(-1) ^{1 + 1}\det(\tilde{A}_{11}) + A _{12}(-1) ^{1 + 2}\det(\tilde{A}_{12}) = A _{11}A _{22} - A _{12}A _{21} $$

    $2 \times 2$ 행렬의 행렬식 정의와 같다는 것을 알 수 있다.

## 항등행렬의 행렬식

!!! tldr ""

    $$ n \in \N : \det(I_n) = 1 $$

- 증명

    $n = 1$ 일 때 $I_n = (1) \implies \det(I_n) = 1$ 이다.

    $n \geq 2$ 일 때 $\det(I _{n-1}) = 1$ 을 가정하자. $I$ 를 $n \times n$ 항등행렬이라고 하자. 그러면 $\tilde{I} _{11} = I _{n-1}$ 이다. 그러므로 다음이 성립한다. 

    $$ \det(I) = (-1) ^{2}(1) \det(\tilde{I}_{11}) + (-1) ^{3}(0) \det(\tilde{I}_{12}) + \dots + (-1) ^{1+n}(0) \det(\tilde{I}_{1n}) = 1 + 0 + \dots + 0 = 1 \tag*{■} $$

## 행렬식의 성질

!!! tldr "정리 4.3"

    $n \times n$ 행렬의 행렬식은 어떤 행을 제외한 나머지 행들이 고정되었을 때, 그 행에 대하여 선형함수이다. 즉, $1 \leq r \leq n$, 스칼라 $k$, 벡터 $u, v \in \mathbf{F} ^{n}$ 에 대하여 다음이 성립한다.

    $$ \det \begin{pmatrix} a_1\\ \vdots \\ a _{r-1}\\ u+kv\\ a _{r+1}\\ \vdots \\ a_n \\ \end{pmatrix} = \det \begin{pmatrix} a_1\\ \vdots \\ a _{r-1}\\ u\\ a _{r+1}\\ \vdots \\ a_n \\ \end{pmatrix} + k \det \begin{pmatrix} a_1\\ \vdots \\ a _{r-1}\\ v\\ a _{r+1}\\ \vdots \\ a_n \\ \end{pmatrix} $$

- 이 정리는 2형 기본행연산과 행렬식 사이의 관계를 말해준다. 즉, 위 정리에서 $u=0$ 으로 두면 [정리 4.3 따름정리](#e337b8376)에 의하여 다음이 성립한다.

    $$ \det \begin{pmatrix} a_1\\ \vdots \\ a _{r-1}\\ kv\\ a _{r+1}\\ \vdots \\ a_n \\ \end{pmatrix} = k \det \begin{pmatrix} a_1\\ \vdots \\ a _{r-1}\\ v\\ a _{r+1}\\ \vdots \\ a_n \\ \end{pmatrix} $$

    이는 행렬 $A$ 의 한 행에 스칼라 $k$ 를 곱하여 얻은 행렬 $B$ 에 대하여 다음이 성립함을 의미한다.

    $$ \det(A) = k \det(B) $$

- 증명 

    $n = 1$ 일 때 자명하게 성립한다. ▲ 

    $n \geq 2$ 와 $(n - 1) \times (n - 1)$ 행렬에 대하여 성립함을 가정하자. 

    $n \times n$ 행렬 $A$ 의 각 행 $a_1, a_2, \dots, a_n$ 과 $1 \leq r \leq n$ 인 $r$ 과 $u = (b_1, b_2, \dots, b_n), v = (c_1, c_2, \dots, c_n)$ 와 스칼라 $k$ 에 대하여 $a_r = u + kv$ 로 두자. $A$ 의 $r$ 행을 $u, v$ 로 바꾼 행렬을 각각 $B, C$ 로 두면 $\det(A) = \det(B) + k \det(C)$ 를 보이면 증명이 끝난다. 

    $r = 1$ 일 경우를 증명해보자. $A$ 의 1행은 다음과 같다.

    $$ a_1 = u + kv = (b_1+kc_1, b_2+kc_2, \dots, b_n+kc_n)  $$

    이는 $A _{1j} = b_j + kc_j = B _{1j} + k C _{1j}$ 임을 뜻한다. 또한 $A, B, C$ 는 $1$ 행을 제외하고 서로 같으므로 $\tilde{A}_{1j} = \tilde{B}_{1j} = \tilde{C}_{1j} \iff \det(\tilde{A}_{1j}) = \det(\tilde{B}_{1j}) = \det(\tilde{C}_{1j})$ 이다. 그러므로 $\det(A)$ 는 다음과 같다.

    $$ \begin{equation}\begin{split} \det(A) &= \sum_{j=1}^{n}(-1)^{1+j}A _{1j} \cdot \det(\tilde{A}_{1j})  \\ &= \sum_{j=1}^{n}(-1)^{1+j}(B _{1j} + k C _{1j}) \cdot \det(\tilde{A}_{1j})  \\ &= \sum_{j=1}^{n}(-1)^{1+j}B _{1j} \cdot \det(\tilde{A}_{1j}) +  k\sum_{j=1}^{n}(-1)^{1+j}C _{1j} \cdot \det(\tilde{A}_{1j}) \\ &= \sum_{j=1}^{n}(-1)^{1+j}B _{1j} \cdot \det(\tilde{B}_{1j}) +  k\sum_{j=1}^{n}(-1)^{1+j}C _{1j} \cdot \det(\tilde{C}_{1j}) \\ &= \det(B) + k \det(C) \end{split}\end{equation} \tag*{} $$

    그러므로 $n \geq 2, r = 1$ 일 때 $n \times n$ 행렬에 대하여 본 정리가 성립한다. ▲ 

    $r > 1$ 인 경우 $1 \leq j \leq n$ 에 대하여 $\tilde{A}_{1j},\tilde{B}_{1j},\tilde{C}_{1j}$ 는 $r - 1$ 행을 제외한 나머지 행이 서로 같다. $\tilde{A}_{1j}$ 의 $r-1$ 행은 다음과 같다. 

    $$ (b_1+kc_1, \dots, b _{j-1}+kc _{j-1}, b _{j+1} + kc _{j+1}, \dots, b_n + kc_n) $$

    이는 $\tilde{B}_{1j}$ 의 $r-1$ 행과 $\tilde{C}_{1j}$ 의 $r-1$ 행의 $k$ 배와의 합이다. $\tilde{B}_{1j}, \tilde{C}_{1j}$ 는 $(n - 1) \times (n - 1)$ 행렬이므로 가정에 의하여 다음이 성립한다. 

    $$ \det(\tilde{A}_{1j}) = \det(\tilde{B}_{1j}) + k \det(\tilde{C}_{1j}) $$

    $r-1$ 행을 제외하면 $A, B, C$ 는 서로 같으므로 $A _{1j} = B _{1j} = C _{1j}$ 이다. 따라서 $\det(A)$ 는 다음과 같다. 

    $$ \begin{equation}\begin{split} \det(A) &= \sum_{j=1}^{n}(-1) ^{1+j}A _{1j} \cdot \det(\tilde{A}_{1j})  \\ &= \sum_{j=1}^{n}(-1) ^{1+j}A _{1j} \cdot ( \det(\tilde{B}_{1j}) + k\det(\tilde{C}_{1j})) \\ &= \sum_{j=1}^{n}(-1) ^{1+j}A _{1j} \cdot \det(\tilde{B}_{1j}) + k\sum_{j=1}^{n}(-1) ^{1+j} A _{1j} \cdot  \det(\tilde{C}_{1j}) \\ &= \sum_{j=1}^{n}(-1) ^{1+j}B _{1j} \cdot \det(\tilde{B}_{1j}) + k\sum_{j=1}^{n}(-1) ^{1+j} C _{1j} \cdot  \det(\tilde{C}_{1j}) \\ &= \det(B) + k \det(C) \end{split}\end{equation} \tag*{} $$

    그러므로 $n \times n$ 행렬에 대해서도 성립한다. ■ 

!!! tldr "정리 4.3 따름정리"

    행렬 $A \in \mathbf{M}_{n \times n}(\mathbf{F} )$ 의 어느 행의 모든 성분이 $0$ 이면 $\det(A) = 0$ 이다.

- 증명

    스칼라 $k \neq 0$ 에 대하여 정리 4.3 에 의하여 다음이 성립한다.

    $$ \det(A) = \det \begin{pmatrix} a_1\\ \vdots \\ a _{r-1}\\ 0+k \cdot 0\\ a _{r+1}\\ \vdots \\ a_n \\ \end{pmatrix} = \det \begin{pmatrix} a_1\\ \vdots \\ a _{r-1}\\ 0\\ a _{r+1}\\ \vdots \\ a_n \\ \end{pmatrix} + k \cdot \det \begin{pmatrix} a_1\\ \vdots \\ a _{r-1}\\ 0\\ a _{r+1}\\ \vdots \\ a_n \\ \end{pmatrix} $$

    $$ \iff  \det(A)  = \det(A)  +k \det(A)  \iff k \det(A)  = 0 \iff \det(A)  = 0 \tag*{■} $$

!!! tldr "정리 4.3 보조정리 1"

    $n \geq 2$ 인 행렬 $B \in \mathbf{M}_{n \times n}(\mathbf{F} )$ 의 $i$ 행이 $1 \leq k \leq n$ 인 어떤 $k$ 에 대하여 $e_k$ 이면 다음이 성립한다. 
    
    $$ \det(B) = (-1)^{i+k}\det(\tilde{B}_{ik}) $$

- 행렬식은 정사각행렬의 1행에 대한 여인수 전개로 정의되었지만, 이 정리는 임의의 행에 대한 여인수 전개 또한 행렬식이 된다는 것을 말해준다. 

- 증명

    $n = 2$ 일 때를 살펴보자. 행렬 $B \in \mathbf{M}_{2 \times 2}(\mathbf{F} )$ 의 $i$ 행이 $1 \leq k \leq 2$ 인 어떤 $k$ 에 대하여 $e_k$ 이면 $\det(B) = (-1)^{i+k}\det(\tilde{B}_{ik})$ 임을 보이면 된다. 

    $1$ 행이 $e_1$ 일 경우, $1$ 행이 $e_2$ 일 경우, $2$ 행이 $e_1$ 일 경우, $2$ 행이 $e_2$ 일 경우에 각각 다음과 같이 성립한다.

    $$ B = \begin{pmatrix} 1&0\\ c&d\\ \end{pmatrix} \implies \det(B) = (-1) ^{1 + 1} \det(\tilde{B}_{11}) = d $$

    $$ B = \begin{pmatrix} 0&1\\ c&d\\ \end{pmatrix} \implies \det(B) = (-1) ^{1 + 2} \det(\tilde{B}_{12}) = -c $$

    $$ B = \begin{pmatrix} a&b\\ 1&0\\ \end{pmatrix} \implies \det(B) = (-1) ^{2 + 1} \det(\tilde{B}_{21}) = -b $$

    $$ B = \begin{pmatrix} a&b\\ 0&1\\ \end{pmatrix} \implies \det(B) = (-1) ^{2 + 2} \det(\tilde{B}_{22}) = a $$

    그러므로 $n = 2$ 일 때 성립한다. ▲ 

    $n > 2$ 일 때 $(n - 1) \times (n - 1)$ 행렬에 대하여 성립함을 가정하자.

    행렬 $B \in \mathbf{M}_{n \times n}(\mathbf{F} )$ 의 $i$ 행이 $1 \leq k \leq n$ 인 어떤 $k$ 에 대하여 $e_k$ 이면 $\det(B) = (-1)^{i+k}\det(\tilde{B}_{ik})$ 임을 보이면 된다.

    $i = 1$ 이면 $B _{1k} = 1$ 이고 $B$ 의 나머지 1행의 성분들은 모두 $0$ 이다. 그러므로 다음이 성립한다. 

    $$ \det(B) = \sum_{j=1}^{n}(-1) ^{1+j}B _{1j} \cdot \det(\tilde{B}_{1j}) = (-1) ^{1+k}\det(\tilde{B}_{1k}) $$

    그러므로 $n > 2, i = 1$ 일 때 성립한다. ▲ 

    $n > 2, 1 < i \leq n$ 을 가정하자. 

    $(n - 2) \times (n - 2)$ 행렬 $C _{ij}$ 를 $B$ 의 $1$행, $i$행, $j$열, $k$열을 제거하여 얻은 행렬이라고 하자.

    각 $j$ 에 대하여 $\tilde{B}_{1j}$ 의 $i - 1$ 행은 다음과 같은 벡터이다. 

    $$ \begin{cases} e _{k-1} \in \mathbf{F} ^{n-1} &j < k\\ 0 \in \mathbf{F} ^{n-1} &j = k\\ e _{k} \in \mathbf{F} ^{n-1} &j > k\\ \end{cases} $$

    $\tilde{B}_{1j}$ 는 위 벡터가 $i-1$ 행에 있는 $(n-1) \times (n-1)$ 행렬이다. 행렬 $\tilde{B}_{1j}$ 에서 $i-1$ 을 제거하는 것은 $B$ 의 $i$ 행을 제거하는 것이다. $j < k$ 의 경우 행렬 $\tilde{B}_{1j}$ 에서 $k-1$ 을 제거하는 것은 $B$ 에서 $k$ 를 제거하는 것인데 반해 $j > k$ 의 경우 행렬 $\tilde{B}_{1j}$ 에서 $k$ 을 제거하는 것은 $B$ 에서 $k$ 를 제거하는 것이다. 그러므로 정리 4.3 따름정리와 가정에 의하여 다음이 성립한다.

    $$ \det(\tilde{B}_{1j})  = \begin{cases} (-1) ^{(i-1)+(k-1)}\det(C _{ij})  & j < k\\ 0  & j = k\\ (-1) ^{(i-1)+k}\det(C _{ij})  & j > k\\ \end{cases} $$

    $n \in \N : (-1) ^{n-1} = (-1) ^{n+1}$ 이다. 다음이 성립한다. 

    $$ \begin{equation}\begin{split}
    \det(B) &= \sum_{j=1}^{n}(-1) ^{1+j}B _{1j} \cdot \det(\tilde{B}_{1j})  \\
    &= \sum_{j<k}(-1) ^{1+j}B _{1j} \cdot \det(\tilde{B}_{1j}) +\sum_{j>k}(-1) ^{1+j}B _{1j} \cdot \det(\tilde{B}_{1j})  \\
    &= \sum_{j<k}(-1) ^{1+j}B _{1j} \cdot \{(-1) ^{(i-1)+(k-1)}\det(C _{ij}) \}  \\
    &\qquad + \sum_{j>k}(-1) ^{1+j}B _{1j} \cdot \{(-1) ^{(i-1)+k}\det(C _{ij})\}  \\
    &= (-1) ^{i+k} \bigg \{\sum_{j<k}(-1) ^{1+j}B _{1j} \cdot \det(C _{ij}) + \sum_{j>k}(-1) ^{1+(j-1)}B _{1j} \cdot \det(C _{ij}) \bigg \} \\
    &= (-1) ^{i+k} \bigg \{\sum_{j<k}(-1) ^{1+j}B _{1j} \cdot \det(C _{ij}) + \sum_{j=k+1}^{n}(-1) ^{1+(j-1)}B _{1j} \cdot \det(C _{ij}) \bigg \} \\
    \end{split}\end{equation} \tag*{}
    $$

    중괄호 안의 식은 $\tilde{B}_{ik}$ 의 1행에 대한 여인수 전개이므로 다음이 성립한다. 

    $$ \det(B) = (-1) ^{i+k}\det(\tilde{B}_{ik}) $$

    그러므로 $n > 2, 1 < i \leq n$ 일 때 성립한다. ■ 

!!! tldr "정리 4.4"

    $A \in \mathbf{M}_{n \times n}(\mathbf{F} )$ 와 $i \in \{1, \dots, n\}$ 에 대하여 다음이 성립한다. 

    $$ \det(A) = \sum_{j=1}^{n}(-1)^{i+j}A _{ij} \cdot \det(\tilde{A}_{ij}) $$

- 이 정리는 행렬식을 1행에 대한 여인수 전개로 얻을 수 있을 뿐만 아니라 임의의 행에 대한 여인수 전개로 구할 수 있음을 말해준다. 

- 증명

    $i = 1$ 일 때 행렬식의 정의와 같으므로 증명할 것이 없다. ▲ 

    $i > 1$ 일 때를 증명해보자.

    $1 \leq j \leq n$ 에 대하여 $A$ 의 $i$ 행을 $e_j$ 로 대체한 행렬을 $B_j$ 라고 하자. 정리 4.3 은 행렬식의 덧셈과 스칼라곱 대한 선형성을 보장해주므로 다음이 성립한다.

    $$ \det(A) = \sum_{j=1}^{n}A _{ij} \cdot \det(B_j) $$

    정리 4.3 보조정리 1 은 $i$ 행이 $e_j$ 인 $B_j$ 에 대하여 $\det(B_j) = (-1) ^{i+j}\det(\tilde{B}_{ij})$ 임을 말해준다. $A$ 와 $B_j$ 는 $i$ 행을 제외하고 서로 같기 때문에 $\tilde{B}_{ij}=\tilde{A}_{ij}$ 이다. 그러므로 $\det(B_j) = (-1) ^{i+j}\det(\tilde{A}_{ij})$ 이고, 이에 따라 다음이 성립한다.


    $$ \det(A) = \sum_{j=1}^{n}(-1)^{i+j}A _{ij} \cdot \det(\tilde{A}_{ij}) \tag*{■} $$

!!! tldr "정리 4.4 따름정리"

    $A \in \mathbf{M}_{n \times n}(\mathbf{F} )$ 의 두 행이 같으면 $\det(A) = 0$ 이다.

- 증명

    $n = 2$ 일 때 자명하게 성립한다. ▲ 

    $n \geq 3$ 일 때 $(n - 1) \times (n - 1)$ 행렬에 대하여 정리가 성립함을 가정하자. 서로 같은 두 행을 $r$행, $s$행이라 하자. $r, s$ 가 아니고 $1 \leq i \leq n$ 인 $i$ 에 대하여 정리 4.4 에 의하여 다음과 같이 $i$행에 대한 여인수 전개를 할 수 있다.

    $$ \det(A) = \sum_{j=1}^{n}(-1)^{i+j}A _{ij} \cdot \det(\tilde{A}_{ij}) $$

    $\tilde{A}_{ij}$ 는 $(n - 1) \times (n - 1)$ 행렬이고 서로 다른 두 행($r$ 행, $s$ 행)이 같으므로 가정에 의하여 $\det(\tilde{A}_{ij}) = 0$ 이다. 그러므로 $\det(A) = 0$ 이다. ■ 

!!! tldr "정리 4.5"

    행렬 $A \in \mathbf{M}_{n \times n}(\mathbf{F} )$ 의 두 행을 교환하여 얻은 행렬 $B$ 에 대하여 $\det(B) = - \det(A)$ 이다.

- 이 정리는 1형 기본행연산과 행렬식 사이의 관계를 말해준다. 

- 증명

    $A$ 의 행 $a_1, a_2, \dots, a_n$ 에 대하여 $r < s$ 인 $r$행과 $s$ 행을 교환하여 얻은 $B$ 행은 다음과 같다. 

    $$ A = \begin{pmatrix} a_1\\ \vdots \\ a_r\\ \vdots \\ a_s\\ \vdots \\ a_n \\ \end{pmatrix}, B = \begin{pmatrix} a_1\\ \vdots \\ a_s\\ \vdots \\ a_r\\ \vdots \\ a_n \\ \end{pmatrix} $$

    $A$ 의 $r$행, $s$행을 $a_r+a_s$ 로 바꾼 행렬은 정리 4.4 따름정리에 의하여 행렬식이 $0$ 이 된다. 또한 [정리 4.3](#e013b5962) 에 의하여 다음이 성립한다. 

    $$ 0 = \begin{pmatrix} a_1\\ \vdots \\ a_r+a_s\\ \vdots \\ a_r+a_s\\ \vdots \\ a_n \\ \end{pmatrix}= \begin{pmatrix} a_1\\ \vdots \\ a_r\\ \vdots \\ a_r+a_s\\ \vdots \\ a_n \\ \end{pmatrix}+ \begin{pmatrix} a_1\\ \vdots \\ a_s\\ \vdots \\ a_r+a_s\\ \vdots \\ a_n \\ \end{pmatrix} $$

    $$ = \begin{pmatrix} a_1\\ \vdots \\ a_r\\ \vdots \\ a_r\\ \vdots \\ a_n \\ \end{pmatrix}+ \begin{pmatrix} a_1\\ \vdots \\ a_r\\ \vdots \\ a_s\\ \vdots \\ a_n \\ \end{pmatrix}+ \begin{pmatrix} a_1\\ \vdots \\ a_s\\ \vdots \\ a_r\\ \vdots \\ a_n \\ \end{pmatrix}+ \begin{pmatrix} a_1\\ \vdots \\ a_s\\ \vdots \\ a_s\\ \vdots \\ a_n \\ \end{pmatrix} = 0 + \det(A) + \det(B) + 0 $$

    즉, $\det(B) = - \det(A)$ 이다. ■ 

!!! tldr "정리 4.6"

    행렬 $A \in \mathbf{M}_{n \times n}(\mathbf{F} )$ 와 $A$ 의 한 행에 다른 행의 스칼라 배를 더하여 얻은 행렬 $B$ 에 대하여 $\det(B) = \det(A)$ 이다.

- 이 정리는 3형 기본행연산과 행렬식 사이의 관계를 말해준다.

- 증명

    $A$ 의 $s$행에 $r$행의 $k$배를 더하여 얻은 행렬을 $B$ 라 하자.

    $A$ 의 행을 $a_1, a_2, \dots, a_n$, $B$ 의 행을 $b_1, b_2, \dots, b_n$ 이라 하자. 다음이 성립한다.

    $$ \begin{cases}
    a_i = b_i & i \neq s\\
    b_s = a_s + ka_r & i = s\\
    \end{cases} 
    $$

    $A$ 의 $s$ 행을 $a_r$ 로 바꾼 행렬을 $C$ 라 하면 $\det(C) = 0$ 이다. $B$ 의 $s$행에 [정리 4.3](#e013b5962) 을 적용하면 다음이 성립한다. 

    $$ \det(B) = \det(A) +k \det(C) = \det(A) \tag*{■} $$

!!! tldr "정리 4.6 따름정리"

    $$A \in \mathbf{M}_{n \times n}(\mathbf{F} ) : \text{rank} (A) < n \implies \det(A) = 0 $$

- [정리 4.2](#16d997576) 는 $2 \times 2$ 행렬이 가역인 것과 행렬식이 $0$ 이 아닌 것은 동치임을 말해준다. 이는 $n \times n$ 행렬에 일반화된다. 이 정리는 $n \times n$ 행렬이 가역이면 행렬식이 $0$ 이 아님을 말해준다. 정리 4.7 의 따름정리는 그 역을 증명해준다.

- 증명

    행렬 $A$ 의 랭크가 $n$ 미만이면 

    $\text{rank} (A) < n$ 이면 $A$ 의 행 $a_1, a_2, \dots, a_n$ 은 일차종속이다. 그러므로 어떤 행 $a_r$ 을 다음과 같이 다른 행들의 일차결합으로 나타낼 수 있다.

    $$ a_r = c_1a_1 + \dots + c _{r-1}a _{r-1} + c _{r+1}a _{r+1} + \dots + c_na_n $$

    $i \neq r$ 인 $i$ 에 대하여 $A$ 의 $r$행에 $i$행의 $-c_i$ 배를 더하여 얻은 행렬 $B$ 는 $b_r = 0$ 이므로 [정리 4.3 따름정리](#e337b8376)에 의하여 $\det(B) = 0$ 이다. 정리 4.6 에 의하여 $\det(B) = \det(A) = 0$ 이다. ■ 

## 행렬식과 기본행연산의 관계

!!! tldr "기본행연산과 행렬식의 관계"

    기본행연산과 $A \in \mathbf{M}_{n \times n}(\mathbf{F} )$ 의 행렬식의 관계는 다음과 같다.

    1. $A$ 의 두 행을 교환하여 얻은 행렬 $B$ 에 대하여 $\det(B) = -\det(A)$ 이다.

    2. $A$ 의 한 행에 영이 아닌 스칼라 $k$ 를 곱하여 얻은 행렬 $B$ 에 대하여 $\det(B) = k \det(A)$ 이다.

    3. $A$ 의 한 행에 다른 행의 스칼라 배를 더하여 얻은 행렬 $B$ 에 대하여 $\det(B) = \det(A)$ 이다.

- 증명

    [정리 4.3(2형 기본행연산과 행렬식의 관계)](#e013b5962), [정리 4.5(1형 기본행연산과 행렬식의 관계)](#f4dc3fe35), [정리 4.6(3형 기본행연산과 행렬식의 관계)](#031b9b6c8) 에 의하여 증명된다.

## 상삼각행렬의 행렬식

!!! tldr "문제 4.2-23"

    상삼각행렬 $A \in \mathbf{M}_{n \times n}(\mathbf{F} )$ 에 대하여 $\det(A) = \text{tr} (A)$ 이다.

- 정사각행렬은 1형과 3형 기본행연산을 통하여 상삼각행렬이 된다. 그러므로 정사각행렬의 행렬식을 쉽게 구할 수 있다.

    지금까지의 정리들은 여인수 전개를 통해 행렬식을 귀납적으로 구하는 것이 매우 번거롭기 때문에 행렬식을 효과적으로 구할 수 있도록 기본연산과 행렬식 간의 관계를 밝히기 위한 것들이었다.

    그리고 이 정리는 상삼각행렬의 행렬식이 대각합으로 매우 쉽게 구해질 수 있다는 것을 말해줌으로써 기본연산의 목표를 상삼각행렬을 만드는 것으로 두는 것이 좋다는 결론을 알려준다.

    $n \times n$ 행렬의 행렬식을 구하기 위해 여인수 전개를 사용하면 $n!$ 번 이상의 곱셈이 필요한데 비해 기본행연산으로 행렬식을 계산하면 $\frac{1}{3}(n ^{3}+2n-3)$ 번의 곱셈이 필요하다.

- 증명

    상삼각행렬 $A \in \mathbf{M}_{n \times n}(\mathbf{F} )$ 는 다음과 같다. 

    $$ A = \begin{pmatrix} A_{11}&A_{12}&\dots&A_{1n}\\ 0&A_{22}&\dots&A_{2n}\\ \vdots& \vdots& \ddots& \vdots \\ 0&0&\dots&A_{nn}\\ \end{pmatrix} $$

    $A$ 에 기본행연산을 적용하여 $A$ 를 항등행렬로 바꿀 수 있다.

    $$ \begin{pmatrix} A_{11}&A_{12}&\dots&A_{1n}\\ 0&A_{22}&\dots&A_{2n}\\ \vdots& \vdots& \ddots& \vdots \\ 0&0&\dots&A_{nn}\\ \end{pmatrix} \to \begin{pmatrix} 1&?&\dots&?\\ 0&A_{22}&\dots&A_{2n}\\ \vdots& \vdots& \ddots& \vdots \\ 0&0&\dots&A_{nn}\\ \end{pmatrix} \to \begin{pmatrix} 1&0&\dots&?\\ 0&A_{22}&\dots&A_{2n}\\ \vdots& \vdots& \ddots& \vdots \\ 0&0&\dots&A_{nn}\\ \end{pmatrix} \to $$ 

    $$ \begin{pmatrix} 1&0&\dots&?\\ 0&1&\dots&?\\ \vdots& \vdots& \ddots& \vdots \\ 0&0&\dots&A_{nn}\\ \end{pmatrix} \to \dots \to \begin{pmatrix} 1&0&\dots&0\\ 0&1&\dots&0\\ \vdots& \vdots& \ddots& \vdots \\ 0&0&\dots&A_{nn}\\ \end{pmatrix} \to \begin{pmatrix} 1&0&\dots&0\\ 0&1&\dots&0\\ \vdots& \vdots& \ddots& \vdots \\ 0&0&\dots&1\\ \end{pmatrix} $$

    위 과정은 다음 연산을 반복한 것에 불과하다.

    1. $i$ 행에 스칼라를 곱한 것을 $i-1$ 행에 더하여 $A _{ii}$ 를 제외한 $i$ 열의 성분들을 $0$ 으로 만든다.

    2. $i$ 행에 스칼라를 곱하여 $A _{ii}$ 를 $1$ 로 만든다.

    $\det(I_n) = 1$ 이므로 기본행연산이 어떻게 적용되었는지 역추적을 해보자. $A _{j}$ 를 $A$ 에 기본행연산을 $j$ 번 적용한 행렬이라고 하자.

    1. 먼저 $1$ 행에 스칼라 $\frac{1}{A _{11}}$ 를 곱했다. $\det(A_1) = \frac{1}{A _{11}}\det(A)$ 이다.

    2. $2$ 행의 스칼라배를 $1$ 행에 더하여 1행 2열의 성분을 $0$ 으로 만들었다. $\det(A_2) = \det(A_1)$ 이다.

    3. $2$ 행에 스칼라 $\frac{1}{A _{22}}$ 를 곱했다. $\det(A_3) = \frac{1}{A _{22}}\det(A_2)$ 이다.

    4. $\dots$

    이를 통하여 행렬식 $\det(A)$ 에 대각 성분의 곱셈의 역원이 계속해서 곱해졌음을 알 수 있다. 따라서 다음이 성립한다. 

    $$ \det(I_n) = \dfrac{1}{A _{11} A _{22} \dots A _{nn}} \det(A) = 1 $$

    그러므로 다음이 성립한다. 

    $$ \therefore \det(A) = A _{11} A _{22} \dots A _{nn} \tag*{■} $$

- 예시 

    $A = \begin{pmatrix} 1&3&-3\\ 0&4&-7\\ 0&0&10\\ \end{pmatrix}$  에 대하여 다음이 성립한다.

    $$ \det(A) = \text{tr} (A) = 40 $$

!!! tldr ""

    삼각행렬 $A \in \mathbf{M}_{n \times n}(\mathbf{F} )$ 에 대하여 $\det(A) = \text{tr} (A)$ 이다.

- 증명

    상삼각행렬일 경우 문제 4.2-23 에서 증명이 끝났다. ▲ 

    하삼각행렬일 경우 문제 4.2-23 의 증명과정과 거의 비슷하게 증명 가능하다. ■ 

## 기본행렬의 행렬식


!!! tldr "기본행렬의 행렬식"

    1. $I$ 의 두 행의 위치를 바꾸어 얻은 기본행렬 $E$ 에 대하여 $\det(E) = -1$ 이다.

    2. $I$ 의 한 행에 영이 아닌 스칼라 $k$ 를 곱하여 얻은 기본행렬 $E$ 에 대하여 $\det(E) = k$ 이다.

    3. $I$ 의 한 행에 다른 행의 스칼라 배를 더하여 얻은 기본행렬 $E$ 에 대하여 $\det(E) = 1$ 이다.

- 증명

    행렬식과 기본행연산의 관계와 $\det(I) = 1$ 에 의하여 바로 증명된다. ■ 

!!! tldr "정리 4.7"

    $$ A, B \in \mathbf{M}_{n \times n}(\mathbf{F} ) : \det(AB) = \det(A) \det(B) $$

- 이 정리는 행렬식이 곱을 보존하는 함수임을 말해준다.

- 증명

    $A$ 가 $I$ 의 두 행의 위치를 바꾸어 얻은 기본행렬이면 $\det(A) = -1$ 인데, [정리 3.1](../MatrixOperation/#1c860f354) 에 의하여 행렬 $AB$ 는 $B$ 의 두 행을 바꾼 것이다. 그러면 [정리 4.5](#f4dc3fe35) 에 의하여 $\det(AB) = - \det(B) = \det(A) \det(B)$ 이다.

    $A$ 가 $I$ 의 한 행에 영이 아닌 스칼라 $k$ 를 곱하여 얻은 기본행렬이면 $\det(A) = k$ 이다. [정리 3.1](../MatrixOperation/#1c860f354) 에 의하여 행렬 $AB$ 는 $B$ 의 한 행에 스칼라 $k$ 를 곱한 것이다. 그러면 [정리 4.3](#e013b5962) 에 의하여 $\det(AB) = k \det(B) = \det(A) \det(B)$ 이다.

    $A$ 가 $I$ 의 한 행에 다른 행의 스칼라 배를 더하여 얻은 기본행렬 기본행렬이면 $\det(A) = 1$ 이다. [정리 3.1](../MatrixOperation/#1c860f354) 에 의하여 행렬 $AB$ 는 $B$ 의 한 행에 다른 행의 스칼라 $k$배 를 곱한 것을 더하여 얻은 것이다. 그러면 [정리 4.6](#031b9b6c8) 에 의하여 $\det(AB) = \det(B) = \det(A) \det(B)$ 이다. 

    이렇게 $A$ 가 기본행렬일 경우 정리가 성립한다. ▲ 

    [정리 4.6 따름정리](#e9f88afe6) 에 의하여 $\text{rank} (A) < n$ 이면 $\det(A) = 0$ 이다. [정리 3.7](../MatrixOperation/#68242c9ae) 에 의하여 $\text{rank} (AB) \leq \text{rank} (A) < n$ 이므로 $\det(AB) = 0$ 이다. 따라서 $\det(AB) = \det(A) \det(B)$ 이다. ▲ 

    [$\text{rank} (A) = n$ 이면 $A$ 는 가역이다](../MatrixOperation/#54a88bd9a). 그러므로 [$A$ 는 기본행렬의 곱이다](../MatrixOperation/#18150efeb). $A = E_m \dots E_1$ 로 두자. 기본행렬에 대하여 본 정리를 가정할 수 있으므로 다음이 성립한다. 

    $$ \begin{equation}\begin{split} \det(AB) &= \det(E_m \dots E_1B)  \\ &= \det(E_m) \det(E _{m-1} \dots E_1B)  \\ &= \det(E_m) \det(E _{m-1}) \det(E _{m-2} \dots E_1B)  \\ & \vdots  \\ &= \det(E_m) \dots \det(E _1)\det(B)  \\ &= \det(E_m \dots E _1)\det(B)  \\ &= \det(A)\det(B)  \\ \end{split}\end{equation} \tag*{} $$

    그러므로 $\text{rank} (A) = n$ 일 때 정리가 성립한다. ■ 

!!! tldr "정리 4.7 따름정리"

    $A \in \mathbf{M}_{n \times n}(\mathbf{F} )$ 에 대하여 다음은 동치이다.

    1. $A$ 는 가역이다. 이 경우 $\det(A ^{-1})  = \dfrac{1}{\det(A) }$ 이다.

    2. $\det(A) \neq 0$

- 증명

    $A$ 가 가역이 아니면 $\text{rank} (A) < n$ 이므로 $\det(A) = 0$ 이다. $A$ 가 가역이면 다음이 성립한다. 

    $$ \det(A) \det(A ^{-1}) = \det(AA ^{-1}) = \det(I) = 1 $$

    이는 $\det(A) \neq 0, \det(A ^{-1}) = \dfrac{1}{\det(A) }$ 를 뜻한다. ■ 

!!! tldr "문제 4.2-29"

    기본행렬 $E$ 에 대하여 $\det(E ^{t}) = \det(E)$ 이다.

- 증명

    $I_n$ 의 $i$ 행과 $j$ 행을 교환하여 얻은 행렬 $E$ 는 $E$ 의 행 $E_1, E_2, \dots, E_n$ 에 대하여 다음과 같이 정의된다.

    $$ \begin{cases} E_k = e_k & k \neq i, k \neq j\\ E_i = e_j &\\ E_j = e_i &\\ \end{cases} $$

    $E ^{t}$ 의 $k$ 행 $E'_k$ 은 벡터 $E_1, E_2, \dots, E_n$ 의 $k$ 번째 성분으로 구성되므로 다음이 성립한다.

    $$ \begin{cases} E'_k = e_k & k \neq i, k \neq j\\ E'_i = e_j & \\ E'_j = e_i & \\ \end{cases} $$

    모든 행이 서로 같으므로 $E = E ^{t}$ 이다. 그러므로 기본행연산 1형을 한 번 적용한 기본행렬의 경우 정리가 자명하게 성립한다. ▲ 

    $I_n$ 의 $i$ 행에 스칼라 $c$ 를 곱하여 얻은 행렬 $E$ 는 $E$ 의 행 $E_1, E_2, \dots, E_n$ 에 대하여 다음과 같이 정의된다.

    $$ \begin{cases} E_k = e_k & k \neq i\\ E_i = ce_i &\\ \end{cases} $$

    $E ^{t}$ 의 $k$ 행 $E'_k$ 은 벡터 $E_1, E_2, \dots, E_n$ 의 $k$ 번째 성분으로 구성되므로 다음이 성립한다.

    $$ \begin{cases} E'_k = e_k & k \neq i\\ E'_i = ce_i & \\ \end{cases} $$

    모든 행이 서로 같으므로 $E = E ^{t}$ 이다. 그러므로 기본행연산 2형을 한 번 적용한 기본행렬의 경우 정리가 자명하게 성립한다. ▲ 

    $I_n$ 의 $i$ 행에 스칼라 $c$ 를 곱하여 $j$ 행에 더하여 얻은 행렬 $E$ 는 $E$ 의 행 $E_1, E_2, \dots, E_n$ 에 대하여 다음과 같이 정의된다.

    $$ \begin{cases} E_k = e_k & k \neq j\\ E_j = ce_i + e_j &\\ \end{cases} $$

    $E ^{t}$ 의 $k$ 행 $E'_k$ 은 벡터 $E_1, E_2, \dots, E_n$ 의 $k$ 번째 성분으로 구성되므로 다음이 성립한다.

    $$ \begin{cases} E'_k = e_k & k \neq i\\ E'_i = e_i + ce_j & \\ \end{cases} $$
    
    $E$ 가 $I_n$ 의 $i$ 행에 스칼라 $c$ 를 곱하여 $j$ 행에 더한 행렬인데 비해 $E ^{t}$ 는 $j$ 행에 스칼라 $c$ 를 곱해 $i$ 행에 더한 행렬임을 알 수 있다. 

    $E$ 가 상삼각행렬임을 가정하면 $\det(E) = \text{tr} (E) = 1$ 이다. $E ^{t}$ 는 하삼각행렬이므로 $\det(E ^{t}) = \text{tr} (E ^{t}) = 1$ 이다. $E$ 가 하삼각행렬이고 $E ^{t}$ 가 상삼각행렬일 경우도 마찬가지이다. 그러므로 기본행연산 3형을 한 번 적용한 기본행렬의 경우 정리가 성립한다. ▲ 

    이제 기본행연산을 한번 적용한 기본행렬의 행렬식이 전치행렬의 행렬식과 같다는 것을 가정할 수 있다.

    이제 임의의 기본행렬 $E$ 를 생각하자. [기본행렬은 가역](../MatrixOperation/#c576bf96c)이고 [가역은 기본행렬의 곱](../MatrixOperation/#18150efeb)이다. 그러므로 다음을 만족하는 $I$ 에 기본행연산을 한번 적용한 기본행렬 $E_1, E_2, \dots, E_k$ 가 존재하여 다음을 만족시킨다.

    $$ E = E_1 E_2 \dots E_k $$

    $$ E ^{t} = E_k ^{t} E _{k-1} ^{t} \dots E_1 ^{t} $$

    기본행연산을 한번만 적용한 기본행렬의 행렬식이 전치행렬의 행렬식이 같다는 것과 정리 4.7 에 의하여 다음이 성립한다.

    $$ \begin{equation}\begin{split}
    \det(E)&= \det(E_1 E_2 \dots E_k) \\
    &= \det(E_1) \det(E_2) \dots \det(E_k) \\
    &= \det(E_1^{t}) \det(E_2^{t}) \dots \det(E_k^{t}) \\
    &= \det(E_k^{t}) \det(E _{k-1}^{t}) \dots \det(E_1^{t}) \\
    &= \det(E_k^{t}E _{k-1}^{t}\dots E_1^{t}) \\
    &= \det(E^{t}) \\
    \end{split}\end{equation} \tag*{}
    $$

    이로써 모든 증명이 끝났다. ■ 

!!! tldr "정리 4.8"

    $$ A \in \mathbf{M}_{n \times n}(\mathbf{F} ) : \det(A ^{t}) = \det(A) $$

- 지금까지의 정리들은 행에 대한 여인수 전개, 기본행연산과 행렬식의 관계 등등 행의 관점에서 행렬식을 연구한 결과이다. 그러나 이 정리는 지금까지의 정리들이 열의 관점에서도 그대로 성립함을 말해준다. $A$ 의 행이 $A ^{t}$ 에서는 열이기 때문이다.

- 증명


# end