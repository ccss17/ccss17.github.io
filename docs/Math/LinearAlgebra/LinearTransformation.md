!!! info

    [프리드버그 선형대수학](https://book.naver.com/bookdb/book_detail.nhn?bid=16374070) 를 공부하면서 노트정리 한 내용입니다.

# 선형변환, 영공간, 상공간

!!! tldr ""

    선형변환(linear transformation) : $\mathbf{V} , \mathbf{W}$ 이 $\mathbf{F}$-벡터공간이라고 하자. $\forall x, y \in \mathbf{V} , \forall c \in \mathbf{F}$ 에 대하여 다음을 만족하는 함수 $\mathbf{T}: \mathbf{V} \to \mathbf{W}$ 를 $\mathbf{V}$ 에서 $\mathbf{W}$ 로 가는 선형변환이라 한다. 

    1. $\mathbf{T}(x + y) = \mathbf{T}(x) + \mathbf{T}(y)$

    2. $\mathbf{T}(cx) = c\mathbf{T}(x)$

- 지금까지 벡터공간을 살펴보았는데 이제 벡터공간의 구조를 보존하는 함수를 다룬다. 이런 함수를 선형변환이라고 한다. 

    미분연산자나 적분연산자가 선형변환의 대표적인 예시이다. 이런 연산자는 미분방정식과 적분방정식을 특정한 벡터공간에서 정의된 선형변환으로 이해할 수 있게 해준다. 기하학에서의 선형변환은 회전, 대칭, 사영 같은 것들이 있다.

    - $x, y \in \mathbf{V} \implies x+y \in \mathbf{V}$ 인데 $\mathbf{T}(x), \mathbf{T}(y) \in \mathbf{W} \implies \mathbf{T}(x+y) \in \mathbf{W}$ 이므로 $\mathbf{T}$ 가 벡터공간의 구조를 보존한다고 하는 것이다. 스칼라곱에 대해서도 마찬가지.

- $\mathbf{F} = \mathbb{Q}$ 이면 2) 는 1) 에서 도출된다. 그러나 일반적으로 1) 과 2) 는 독립된 명제이다.

- $\mathbf{T}$ 가 선형변환이라는 것을 편의상 "$\mathbf{T}$ 는 선형(linear) 이다" 라고 한다.

!!! tldr ""

    선형변환의 성질 : 선형변환 $\mathbf{T}: \mathbf{V} \to \mathbf{W}$ 는 다음 성질을 만족한다. 

    1. $\mathbf{T}$ 가 선형이면 $\mathbf{T}(0) = 0$ 이다.

    2. $\mathbf{T}$ 가 선형이기 위한 필요충분조건은 $\forall x, y \in \mathbf{V} , \forall c \in \mathbf{F} : \mathbf{T}(cx + y) = c\mathbf{T}(x) + \mathbf{T}(y)$ 이다.

    3. $\mathbf{T}$ 가 선형이면 $\forall x, y \in \mathbf{V} : \mathbf{T}(x -y) = \mathbf{T}(x) - \mathbf{T}(y)$ 이다.

    4. $\mathbf{T}$ 가 선형이기 위한 필요충분조건은 $\forall x_1, \dots, x_n \in \mathbf{V}, \forall a_1, \dots, a_n \in \mathbf{F}$ 에 대하여 다음이 성립하는 것이다. 

        $$ \mathbf{T} \bigg (\sum_{i=1}^{n}a_ix_i\bigg ) = \sum_{i=1}^{n}a_i\mathbf{T}(x_i) $$

- 1) 의 $0$ 은 영벡터이다.

- 어떤 함수가 선형임을 보일 때 주로 2) 를 사용한다.

- 예시 

    $\mathbf{T}: \R ^{2} \to \R ^{2}$ 을 $\mathbf{T}(a_1, a_2) = (2a_1 + a_2, a_1)$ 이라 정의하고 이것이 선형인지 확인하자. 

    $c \in \R, x = (b_1, b_2), y = (d_1, d_2)$ 라 하면 $cx + y = (cb_1 + d_1, cb_2 + d_2)$ 이므로 

    $$ \mathbf{T}(cx + y) = (2(cb_1 + d_1) + cb_2 + d_2, cb_1 + d_1) $$

    이고 $c\mathbf{T}(x) + \mathbf{T}(y)$ 도 

    $$ c\mathbf{T}(x) + \mathbf{T}(y) = (2(cb_1 + d_1) + cb_2 + d_2, cb_1 + d_1) $$

    이다. 그러므로 $\mathbf{T}$ 는 선형이다.

- 선형대수학은 기하학에서 널리 사용되는데, 이는 중요한 기하 변환들이 선형이기 때문이다. 

    - 예시 

        각 $\theta$ 에 대하여 $\mathbf{T} _{\theta }: \R ^{2} \to \R ^{2}$ 을 

        $$ \mathbf{T} _{\theta } (a_1, a_2) = \begin{cases}
        (a_1, a_2) \text{ 를 반시계 방향으로 } \theta \text{ 만큼 회전한 벡터} & (a_1, a_2) \neq (0, 0)\\
        (0, 0) & (a_1, a_2) = (0, 0) \\
        \end{cases} 
        $$

        와 같이 정의하면 $\mathbf{T} _{\theta}: \R ^{2} \to \R ^{2}$ 는 2차원 좌표평면의 벡터를 $\theta$ 만큼 회전하는 선형변환이다. 참고로 $\mathbf{T} _{\theta}$ 는 형식적으로

        $$ \mathbf{T} _{\theta}(a_1, a_2) = (a_1 \cos \theta - a_2 \sin \theta, a_1 \sin \theta + a_2 \cos \theta) $$

        로 정의할 수 있다.
    
    - 예시 

        $\mathbf{T}: \R ^{2} \to \R ^{2} , (a_1, a_2) \mapsto (a_1, -a_2)$ 는 $x$축 대칭(reflection about x-axis)이라는 선형변환이다.

    - 예시 

        $\mathbf{T}: \R ^{2} \to \R ^{2} , (a_1, a_2) \mapsto (a_1, 0)$ 는 $x$축으로 사영(projection on the x-axis)이라는 선형변환이다.

- 예시 

    $\mathbf{T}: \mathbf{M} _{m \times n} (\mathbf{F} ) \to \mathbf{M} _{n \times m}(\mathbf{F} ), A \mapsto A ^{t}$ 는 선형변환이다.

- 예시 

    무한번 미분가능한 함수 $f: \R \to \R$ 의 집합 $\mathbf{V}$ 을 정의하면 $\mathbf{V}$ 는 $\R$-벡터공간이된다. 이때 $\mathbf{T}: \mathbf{V} \to \mathbf{V} , f \mapsto f'$ 로 정의하면

    $$ \mathbf{T}(ag+h) = (ag+h)' = ag'+h'=a\mathbf{T}(g) +\mathbf{T}(h) $$

    이므로 선형변환이다.

- 예시 

    $\mathbf{V}$ 를 $\R$ 에서 정의한 모든 연속함수 집합으로 정의하고, $a, b \in \R, a < b$ 에 대하여 $\mathbf{T}: \mathbf{V} \to \R, f \mapsto \int_{a}^{b}f(t)dt$ 로 정의하면 이는 선형변환이다. 왜냐하면 

    $$ \int_{a}^{b}\{pf(t) + qg(t)\}dt = p \int_{a}^{b}f(t)dt + q \int_{a}^{b}g(t)dt $$

    이기 때문이다.

!!! tldr ""

    항등변환(identity transformation) : $\mathbf{F}$-벡터공간 $\mathbf{V}$ 에 대하여 $I _{\mathbf{V} }: \mathbf{V} \to \mathbf{V}, x \mapsto x$ 로 정의된 선형변환이다.

- 항등변환 $I _{\mathbf{V} }$ 을 편의상 $I$ 라 표기하기도 한다.
    
!!! tldr ""

    영변환(zero transformation) : $\mathbf{F}$-벡터공간 $\mathbf{V} , \mathbf{W}$ 에 대하여 $\mathbf{T} _{ 0}: \mathbf{V} \to \mathbf{W}, x \mapsto 0$ 로 정의된 선형변환이다.

!!! tldr ""

    영공간(null space, kernel) : 벡터공간 $\mathbf{V}, \mathbf{W}$ 와 선형변환 $\mathbf{T}: \mathbf{V} \to \mathbf{W}$ 에 대하여 영공간은 집합 
    
    $$ \mathbf{N}(\mathbf{T}) = \{x \in \mathbf{V} : \mathbf{T}(x) = 0\}$$
    
    이다.

- 선형변환 $\mathbf{T}: \mathbf{V} \to \mathbf{W}$ 의 영공간을 $\mathbf{N}(\mathbf{T})$ 또는 $\text{Null}(\mathbf{T})$ 또는 $\text{ker}(\mathbf{T})$ 로 표기한다.

- 예시 

    항등변환 $I : \mathbf{V} \to \mathbf{V}$ 에 대하여 $\mathbf{N}(I) = \{0\}$ 이다.

    영변환 $\mathbf{T}_0 : \mathbf{V} \to \mathbf{W}$ 에 대하여 $\mathbf{N}(\mathbf{T}_0) = \mathbf{V}$ 이다.

!!! tldr ""

    상공간(range, image) : 벡터공간 $\mathbf{V}, \mathbf{W}$ 와 선형변환 $\mathbf{T}: \mathbf{V} \to \mathbf{W}$ 에 대하여 상공간은 집합 
    
    $$ \mathbf{R}(\mathbf{T}) = \{\mathbf{T}(x) \in \mathbf{W} : x \in \mathbf{V} \}$$
    
    이다.

- 선형변환 $\mathbf{T}: \mathbf{V} \to \mathbf{W}$ 의 상공간을 $\mathbf{R}(\mathbf{T})$ 또는 $\text{ran}(\mathbf{T})$ 으로 표기한다.

- 예시 

    항등변환 $I : \mathbf{V} \to \mathbf{V}$ 에 대하여 $\mathbf{R}(I) = \mathbf{V}$ 이다.

    영변환 $\mathbf{T}_0 : \mathbf{V} \to \mathbf{W}$ 에 대하여 $\mathbf{R}(\mathbf{T}_0) = \{0\}$ 이다.

!!! tldr "정리 2.1"

    벡터공간 $\mathbf{V} ,\mathbf{W}$ 와 선형변환 $\mathbf{T}:\mathbf{V} \to \mathbf{W}$ 에 대하여 $\mathbf{N}(\mathbf{T}), \mathbf{R}(\mathbf{T})$ 는 각각 $\mathbf{V} , \mathbf{W}$ 의 부분공간이다.

- 증명 

    $\mathbf{V} , \mathbf{W}$ 의 영벡터를 각각 $0 _{\mathbf{V} },0 _{\mathbf{W} }$ 라 하자.

    $\mathbf{T}(0 _{\mathbf{V} }) = 0 _{\mathbf{W} }$ 이므로 $0 _{\mathbf{V} } \in \mathbf{N}(\mathbf{T})$ 이다. $x, y \in \mathbf{N}(\mathbf{T})$, $c \in \mathbf{F}$ 에 대하여 

    $$ \mathbf{T}(x+y)=\mathbf{T}(x)+\mathbf{T}(y)=0 _{\mathbf{W} }+0 _{\mathbf{W} }=0 _{\mathbf{W} }, \enspace \mathbf{T}(cx) = c\mathbf{T}(x) = c 0 _{\mathbf{W} } = 0 _{\mathbf{W} } $$

    이므로 $x+y \in \mathbf{N}(\mathbf{T}), cx \in \mathbf{N}(\mathbf{T})$ 이다. 따라서 $\mathbf{N}(\mathbf{T})$ 은 $\mathbf{V}$ 의 부분공간이다. ▲ 

    $\mathbf{T}(0 _{\mathbf{V} }) = 0 _{\mathbf{W} }$ 이므로 $0 _{\mathbf{W} } \in \mathbf{R}(\mathbf{T})$ 이다. $x, y \in \mathbf{R}(\mathbf{T}), c \in \mathbf{F} : \exists v, w \in \mathbf{V} \text{ s.t. }  \mathbf{T}(v) = x, \mathbf{T}(w) = y$ 이다. 따라서 

    $$ \mathbf{T}(v+w) =\mathbf{T}(v) +\mathbf{T}(w) = x+y, \enspace \mathbf{T}(cv) = c\mathbf{T}(v) = cx $$

    이고, $x+y \in \mathbf{R}(\mathbf{T}), cx \in \mathbf{R}(\mathbf{T})$ 이다. 그러므로 $\mathbf{R}(\mathbf{T})$ 는 $\mathbf{W}$ 의 부분공간이다. ■ 

!!! tldr "정리 2.2"

    벡터공간 $\mathbf{V} ,\mathbf{W}$ 와 선형변환 $\mathbf{T}: \mathbf{V} \to \mathbf{W}$ 와 $\mathbf{V}$ 의 기저 $\beta = \{v_1, v_2, \dots, v_n\}$ 에 대하여 다음이 성립한다. 

    $$ \mathbf{R}(\mathbf{T}) = \text{span}(\mathbf{T}(\beta )) = \text{span}(\{\mathbf{T}(v_1), \mathbf{T}(v_2), \dots, \mathbf{T}(v_n)\}) $$

- 이 정리는 선형변환의 상공간을 생성하는 방법을 알려준다.

- 이 정리는 $\beta$ 가 무한집합일 때도 성립한다. 즉, 

    $$ \mathbf{R}(\mathbf{T}) = \text{span}(\{\mathbf{T}(v) : v \in \beta \}) $$

    이다.

- 증명 

    $\forall i, \mathbf{T}(v_i) \in \mathbf{R}(\mathbf{T})$ 이다. $\mathbf{R}(\mathbf{T})$ 가 부분공간이므로 [정리 1.5 "벡터공간 $\mathbf{V}$ 의 임의의 부분집합 $S$ 의 생성공간 $\text{span}(S)$ 는 $S$ 를 포함하는 $\mathbf{V}$ 의 부분공간이다. $S$ 를 포함하는 $\mathbf{V}$ 의 부분공간은 $\text{span}(S)$ 을 포함한다."](../VectorSpace#aad599671) 에 의하여

    $$ \text{span}(\{\mathbf{T}(v_1), \mathbf{T}(v_2), \dots, \mathbf{T}(v_n)\}) =\text{span}(\mathbf{T}(\beta )) \subset \mathbf{R}(\mathbf{T})  $$

    이다. 상공간 $\mathbf{R}(\mathbf{T})$ 은 $\mathbf{T}(\beta )$ 를 포함하면서 부분공간이므로 $\text{span}(\mathbf{T}(\beta ))$ 도 포함하기 때문이다. ▲ 

    $w \in \mathbf{R}(\mathbf{T}) \implies \exists v \in \mathbf{V} \text{ s.t. } w = \mathbf{T}(v)$ 인데 $\beta$ 가 $\mathbf{V}$ 의 기저이므로 $a_1, a_2, \dots, a_n \in \mathbf{F}$ 에 대하여

    $$ v = \sum_{i=1}^{n}a_iv_i $$

    이다. $\mathbf{T}$ 는 선형이므로 
    
    $$w = \mathbf{T}(v) = \mathbf{T} \bigg (\sum_{i=1}^{n}a_iv_i\bigg ) = \sum_{i=1}^{n}a_i\mathbf{T}(v_i) \in \text{span}(\mathbf{T}(\beta ))$$
    
    이다. 이는 상공간의 원소가 $\text{span}(\mathbf{T}(\beta ))$ 의 원소임을 뜻하고, 곧 

    $$ \mathbf{R}(\mathbf{T}) \subset \text{span}(\mathbf{T}(\beta )) = \text{span}(\{\mathbf{T}(v_1), \mathbf{T}(v_2), \dots, \mathbf{T}(v_n)\}) $$

    을 뜻한다. ▲ 

    그러므로 증명이 끝났다. ■ 

- 다음 예시는 이 정리를 사용하여 $\mathbf{R}(\mathbf{T})$ 의 기저와 $\mathbf{N}(\mathbf{T})$ 의 기저를 쉽게 찾을 수 있다는 것을 말해준다.

- 예시 

    선형변환 $\mathbf{T}: \mathbf{P} _2(\R) \to \mathbf{M} _{2 \times 2}(\R)$ 을 

    $$ \mathbf{T}(f(x)) = \begin{pmatrix} f(1)-f(2) & 0\\ 0 & f(0)\\ \end{pmatrix} $$

    와 같이 정의하자. $\mathbf{P} _2(\R)$ 의 기저는 $\beta = \{1,x,x ^{2}\}$ 이므로 이 정리를 사용하여 $\mathbf{R}(\mathbf{T})$ 를 다음과 같이 나타낼 수 있다.

    $$ \begin{equation}\begin{split}   \mathbf{R}(\mathbf{T}) &= \text{span}(\mathbf{T}(\beta )) = \text{span}(\{\mathbf{T}(1), \mathbf{T}(x), \mathbf{T}(x ^{2})\}) \\ &= \text{span}\bigg (\bigg \{ \begin{pmatrix} 0 & 0\\ 0 & 1\\ \end{pmatrix}, \begin{pmatrix} -1 & 0\\ 0 & 0\\ \end{pmatrix}, \begin{pmatrix} -3 & 0\\ 0 & 0\\ \end{pmatrix} \bigg \}\bigg ) \\ &= \text{span}\bigg (\bigg \{ \begin{pmatrix} 0 & 0\\ 0 & 1\\ \end{pmatrix}, \begin{pmatrix} -1 & 0\\ 0 & 0\\ \end{pmatrix} \bigg \}\bigg ) \end{split}\end{equation}\tag*{} $$

    이로써 $\mathbf{R}(\mathbf{T})$ 의 기저를 찾았고 $\dim(\mathbf{R}(\mathbf{T})) = 2$ 임을 알 수 있다. ▲ 

    이제 $\mathbf{N}(\mathbf{T})$ 의 기저를 찾아보자. $2 \times 2$ 영행렬 $O$ 에 대하여 $f(x) \in \mathbf{N}(\mathbf{T}) \iff \mathbf{T}(f(x)) = O$ 이므로 

    $$ f(x) \in \mathbf{N}(\mathbf{T}) \iff \begin{pmatrix} f(1) - f(2) & 0\\ 0 & f(0)\\ \end{pmatrix} = \begin{pmatrix} 0&0\\ 0&0\\ \end{pmatrix} $$

    이다. $f(x) = a + bx + cx ^{2}$ 라 하면

    $$ \begin{equation}\begin{split}   0&= f(1) - f(2) = -b -3c\\ 0 &= f(0) = a \end{split}\end{equation}\tag*{} $$

    이므로 

    $$ f(x) = c(-3x + x ^{2}) $$

    이다. 따라서 $\mathbf{N}(\mathbf{T})$ 의 기저는 $\{-3x + x ^{2}\}$ 이다. ▲ 

- 위 예시에서 $\dim(\mathbf{N}(\mathbf{T})) + \dim(\mathbf{R}(\mathbf{T})) = 1 + 2 = 3 = \dim(\mathbf{P} _2(\R))$ 이 성립하였는데 이는 [정리 2.3](#cc24674bf) 에서와 같이 일반적으로 성립한다.

!!! tldr ""

    nullity(영공간의 차원) : 벡터공간 $\mathbf{V} , \mathbf{W}$ 와 선형변환 $\mathbf{T}: \mathbf{V} \to \mathbf{W}$ 에 대하여 $\mathbf{N}(\mathbf{T})$ 가 유한차원 일 때 $\mathbf{N}(\mathbf{T})$ 의 차원을 

    $$  \text{nullity}(\mathbf{T}) = \dim(\mathbf{N}(\mathbf{T})) $$

    라고 한다. 

- 지금까지 우리는 부분공간의 크기를 가늠할 때 차원을 사용했다. 영공간의 차원은 특히 중요하므로 새로운 이름 $\text{nullity}$ 을 붙혀서 다룬다.

!!! tldr ""

    랭크(rank), 계수 : 벡터공간 $\mathbf{V} , \mathbf{W}$ 와 선형변환 $\mathbf{T}: \mathbf{V} \to \mathbf{W}$ 에 대하여 $\mathbf{R}(\mathbf{T})$ 가 유한차원 일 때 $\mathbf{R}(\mathbf{T})$ 의 차원을 

    $$ \text{rank}(\mathbf{T}) = \dim(\mathbf{R}(\mathbf{T})) $$

    라고 한다. 

- 지금까지 우리는 부분공간의 크기를 가늠할 때 차원을 사용했다. 상공간의 차원은 특히 중요하므로 새로운 이름 $\text{rank}$ 을 붙혀서 다룬다.

- 직관적으로 선형변환에서 nullity 가 커질수록 랭크는 작아진다. 즉, 더 많은 벡터가 영벡터 $0$ 로 갈수록 상공간은 작아진다. 역으로 랭크가 커질수록 nullity 는 작아진다. 아래의 정리가 랭크과 nullity 의 관계를 말해준다. 

!!! tldr "정리 2.3"

    차원정리(dimension theorem) : 벡터공간 $\mathbf{V} , \mathbf{W}$ 와 선형변환 $\mathbf{T}: \mathbf{V} \to \mathbf{W}$ 에 대하여 $\mathbf{V}$ 가 유한차원이면 

    $$ \text{nullity}(\mathbf{T})+\text{rank}(\mathbf{T})= \dim(\mathbf{V} ) $$

    이다.

- 증명 


    

# 선형변환의 행렬표현

# 선형변환의 합성과 행렬 곱

# 가역성과 동형사상

# 좌표변환 행렬

# 쌍대공간

# 계수가 상수인 동차 선형 미분방정식
