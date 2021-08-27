!!! info "ref"

    Stephen H. Friedberg, Linear Algebra, 4th Edition

# Linear Transformation

!!! def "선형변환(linear transformation, linear map, vector space homomorphism)"

    $\mathbf{V} , \mathbf{W}$ 이 $\mathbf{F}$-벡터공간이라고 하자. $\forall x, y \in \mathbf{V} , \forall c \in \mathbf{F}$ 에 대하여 다음을 만족하는 함수 $\mathbf{T}: \mathbf{V} \to \mathbf{W}$ 를 $\mathbf{V}$ 에서 $\mathbf{W}$ 로 가는 선형변환이라 한다. 

    1. $\mathbf{T}(x + y) = \mathbf{T}(x) + \mathbf{T}(y)$

    2. $\mathbf{T}(cx) = c\mathbf{T}(x)$

- 지금까지 벡터공간을 살펴보았는데 이제 벡터공간의 구조를 보존하는 함수를 다룬다. 이런 함수를 선형변환이라고 한다. 

    미분연산자나 적분연산자가 선형변환의 대표적인 예시이다. 이런 연산자는 미분방정식과 적분방정식을 특정한 벡터공간에서 정의된 선형변환으로 이해할 수 있게 해준다. 기하학에서의 선형변환은 회전, 대칭, 사영 같은 것들이 있다.

    - $x, y \in \mathbf{V} \implies x+y \in \mathbf{V}$ 인데 $\mathbf{T}(x), \mathbf{T}(y) \in \mathbf{W} \implies \mathbf{T}(x+y) \in \mathbf{W}$ 이므로 $\mathbf{T}$ 가 벡터공간의 구조를 보존한다고 하는 것이다. 스칼라곱에 대해서도 마찬가지.

- $\mathbf{F} = \mathbb{Q}$ 이면 2) 는 1) 에서 도출된다. 그러나 일반적으로 1) 과 2) 는 독립된 명제이다.

- $\mathbf{T}$ 가 선형변환이라는 것을 편의상 "$\mathbf{T}$ 는 선형(linear) 이다" 라고 한다.

- 벡터공간의 준동형사상(vector space homomorphism) 이라는 정의는 준동형사상의 정의에 의하여 직관적을 알 수 있다.

!!! def "선형변환의 성질"

    선형변환 $\mathbf{T}: \mathbf{V} \to \mathbf{W}$ 는 다음 성질을 만족한다. 

    1. $\mathbf{T}$ 가 선형이면 $\mathbf{T}(0) = 0$ 이다.

    2. $\mathbf{T}$ 가 선형이기 위한 필요충분조건은 $\forall x, y \in \mathbf{V} , \forall c \in \mathbf{F} : \mathbf{T}(cx + y) = c\mathbf{T}(x) + \mathbf{T}(y)$ 이다.

    3. $\mathbf{T}$ 가 선형이면 $\forall x, y \in \mathbf{V} : \mathbf{T}(x -y) = \mathbf{T}(x) - \mathbf{T}(y)$ 이다.

    4. $\mathbf{T}$ 가 선형이기 위한 필요충분조건은 $\forall x_1, \dots, x_n \in \mathbf{V}, \forall a_1, \dots, a_n \in \mathbf{F}$ 에 대하여 다음이 성립하는 것이다. 

        $$ \mathbf{T} \bigg (\sum_{i=1}^{n}a_ix_i\bigg ) = \sum_{i=1}^{n}a_i\mathbf{T}(x_i) $$

- 증명 

    1:

    $x = 0$ 으로 두면 다음이 성립한다.
    
    $$\mathbf{T} (0 + y) = \mathbf{T} (0) + \mathbf{T} (y) \iff \mathbf{T} (y) = \mathbf{T} (0) + \mathbf{T} (y)$$

    $$0 = \mathbf{T} (0) $$

    2), 3), 4) 의 증명은 너무 자명하다. 솔직히 1) 의 증명도 너무 자명한데 예의상 한번 써봤다. ■ 

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

## Identity Transformation

!!! def "항등변환(identity transformation)"

    $\mathbf{F}$-벡터공간 $\mathbf{V}$ 에 대하여 $\mathbf{I} _{\mathbf{V} }: \mathbf{V} \to \mathbf{V}, x \mapsto x$ 로 정의된 선형변환이다.

- 항등변환 $\mathbf{I} _{\mathbf{V} }$ 을 편의상 $\mathbf{I}$ 라 표기하기도 한다.
    
## Zero Transformation

!!! def "영변환(zero transformation)"

    $\mathbf{F}$-벡터공간 $\mathbf{V} , \mathbf{W}$ 에 대하여 $\mathbf{T} _{ 0}: \mathbf{V} \to \mathbf{W}, x \mapsto 0$ 로 정의된 선형변환이다.

# Null Space, Range

!!! def "영공간(null space, kernel)"

    벡터공간 $\mathbf{V}, \mathbf{W}$ 와 선형변환 $\mathbf{T}: \mathbf{V} \to \mathbf{W}$ 에 대하여 영공간은 다음과 같은 집합이다.
    
    $$ \mathbf{N}(\mathbf{T}) = \{x \in \mathbf{V} : \mathbf{T}(x) = 0\}$$

- 선형변환 $\mathbf{T}: \mathbf{V} \to \mathbf{W}$ 의 영공간을 $\mathbf{N}(\mathbf{T})$ 또는 $\text{Null}(\mathbf{T})$ 또는 $\text{ker}(\mathbf{T})$ 로 표기한다.

- 예시 

    항등변환 $\mathbf{I} : \mathbf{V} \to \mathbf{V}$ 에 대하여 $\mathbf{N}(\mathbf{I}) = \{0\}$ 이다.

    영변환 $\mathbf{T}_0 : \mathbf{V} \to \mathbf{W}$ 에 대하여 $\mathbf{N}(\mathbf{T}_0) = \mathbf{V}$ 이다.

!!! def "상공간(range, image)"

    벡터공간 $\mathbf{V}, \mathbf{W}$ 와 선형변환 $\mathbf{T}: \mathbf{V} \to \mathbf{W}$ 에 대하여 상공간은 다음과 같은 집합이다.
    
    $$ \mathbf{R}(\mathbf{T}) = \{\mathbf{T}(x) \in \mathbf{W} : x \in \mathbf{V} \}$$

- 선형변환 $\mathbf{T}: \mathbf{V} \to \mathbf{W}$ 의 상공간을 $\mathbf{R}(\mathbf{T})$ 또는 $\text{ran}(\mathbf{T})$ 으로 표기한다.

- 예시 

    항등변환 $\mathbf{I} : \mathbf{V} \to \mathbf{V}$ 에 대하여 $\mathbf{R}(\mathbf{I}) = \mathbf{V}$ 이다.

    영변환 $\mathbf{T}_0 : \mathbf{V} \to \mathbf{W}$ 에 대하여 $\mathbf{R}(\mathbf{T}_0) = \{0\}$ 이다.

!!! def "정리 2.1"

    벡터공간 $\mathbf{V} ,\mathbf{W}$ 와 선형변환 $\mathbf{T}:\mathbf{V} \to \mathbf{W}$ 에 대하여 $\mathbf{N}(\mathbf{T}), \mathbf{R}(\mathbf{T})$ 는 각각 $\mathbf{V} , \mathbf{W}$ 의 부분공간이다.

- 증명 

    $\mathbf{V} , \mathbf{W}$ 의 영벡터를 각각 $0 _{\mathbf{V} },0 _{\mathbf{W} }$ 라 하자.

    $\mathbf{T}(0 _{\mathbf{V} }) = 0 _{\mathbf{W} }$ 이므로 $0 _{\mathbf{V} } \in \mathbf{N}(\mathbf{T})$ 이다. $x, y \in \mathbf{N}(\mathbf{T})$, $c \in \mathbf{F}$ 에 대하여 

    $$ \mathbf{T}(x+y)=\mathbf{T}(x)+\mathbf{T}(y)=0 _{\mathbf{W} }+0 _{\mathbf{W} }=0 _{\mathbf{W} }, \enspace \mathbf{T}(cx) = c\mathbf{T}(x) = c 0 _{\mathbf{W} } = 0 _{\mathbf{W} } $$

    이므로 $x+y \in \mathbf{N}(\mathbf{T}), cx \in \mathbf{N}(\mathbf{T})$ 이다. 따라서 $\mathbf{N}(\mathbf{T})$ 은 $\mathbf{V}$ 의 부분공간이다. ▲ 

    $\mathbf{T}(0 _{\mathbf{V} }) = 0 _{\mathbf{W} }$ 이므로 $0 _{\mathbf{W} } \in \mathbf{R}(\mathbf{T})$ 이다. $x, y \in \mathbf{R}(\mathbf{T}), c \in \mathbf{F} : \exists v, w \in \mathbf{V} \text{ s.t. }  \mathbf{T}(v) = x, \mathbf{T}(w) = y$ 이다. 따라서 

    $$ \mathbf{T}(v+w) =\mathbf{T}(v) +\mathbf{T}(w) = x+y, \enspace \mathbf{T}(cv) = c\mathbf{T}(v) = cx $$

    이고, $x+y \in \mathbf{R}(\mathbf{T}), cx \in \mathbf{R}(\mathbf{T})$ 이다. 그러므로 $\mathbf{R}(\mathbf{T})$ 는 $\mathbf{W}$ 의 부분공간이다. ■ 

!!! def "정리 2.2"

    벡터공간 $\mathbf{V} ,\mathbf{W}$ 와 선형변환 $\mathbf{T}: \mathbf{V} \to \mathbf{W}$ 와 $\mathbf{V}$ 의 기저 $\beta = \{v_1, v_2, \dots, v_n\}$ 에 대하여 다음이 성립한다. 

    $$ \mathbf{R}(\mathbf{T}) = \text{span}(\mathbf{T}(\beta )) = \text{span}(\{\mathbf{T}(v_1), \mathbf{T}(v_2), \dots, \mathbf{T}(v_n)\}) $$

- 이 정리는 선형변환의 상공간을 생성하는 방법을 알려준다.

- 이 정리는 $\beta$ 가 무한집합일 때도 성립한다. 즉, 

    $$ \mathbf{R}(\mathbf{T}) = \text{span}(\{\mathbf{T}(v) : v \in \beta \}) $$

    이다.

- 증명 

    $\mathbf{T}(\beta) \subset \mathbf{R}(\mathbf{T})$ 이고 $\mathbf{R}(\mathbf{T})$ 가 부분공간이므로 [정리 1.5](../VectorSpace#aad599671) 에 의하여

    $$ \text{span}(\{\mathbf{T}(v_1), \mathbf{T}(v_2), \dots, \mathbf{T}(v_n)\}) =\text{span}(\mathbf{T}(\beta )) \subset \mathbf{R}(\mathbf{T})  $$

    이다. ▲

    $w \in \mathbf{R}(\mathbf{T}) \implies \exists v \in \mathbf{V} \text{ s.t. } w = \mathbf{T}(v)$ 인데 $\beta$ 가 $\mathbf{V}$ 의 기저이므로 $a_1, a_2, \dots, a_n \in \mathbf{F}$ 에 대하여

    $$ v = \sum_{i=1}^{n}a_iv_i $$

    이다. $\mathbf{T}$ 는 선형이므로 
    
    $$w = \mathbf{T}(v) = \mathbf{T} \bigg (\sum_{i=1}^{n}a_iv_i\bigg ) = \sum_{i=1}^{n}a_i\mathbf{T}(v_i) \in \text{span}(\mathbf{T}(\beta ))$$
   
    이다. 이는 $\forall w \in \mathbf{R}(\mathbf{T}) \implies w \in \text{span}(\mathbf{T}(\beta ))$ 을 뜻하므로

    $$ \mathbf{R}(\mathbf{T}) \subset \text{span}(\mathbf{T}(\beta )) = \text{span}(\{\mathbf{T}(v_1), \mathbf{T}(v_2), \dots, \mathbf{T}(v_n)\}) $$

    이 된다. ■ 

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

## Nullity

!!! def "영공간의 차원(Nullity)"

    벡터공간 $\mathbf{V} , \mathbf{W}$ 와 선형변환 $\mathbf{T}: \mathbf{V} \to \mathbf{W}$ 에 대하여 $\mathbf{N}(\mathbf{T})$ 가 유한차원 일 때 $\mathbf{N}(\mathbf{T})$ 의 차원을 

    $$  \text{nullity}(\mathbf{T}) = \dim(\mathbf{N}(\mathbf{T})) $$

    라고 한다. 

- 지금까지 우리는 부분공간의 크기를 가늠할 때 차원을 사용했다. 영공간의 차원은 특히 중요하므로 새로운 이름 $\text{nullity}$ 을 붙혀서 다룬다.

## Rank

!!! def "랭크(rank), 계수"

    벡터공간 $\mathbf{V} , \mathbf{W}$ 와 선형변환 $\mathbf{T}: \mathbf{V} \to \mathbf{W}$ 에 대하여 $\mathbf{R}(\mathbf{T})$ 가 유한차원 일 때 $\mathbf{R}(\mathbf{T})$ 의 차원을 

    $$ \text{rank}(\mathbf{T}) = \dim(\mathbf{R}(\mathbf{T})) $$

    라고 한다. 

- 지금까지 우리는 부분공간의 크기를 가늠할 때 차원을 사용했다. 상공간의 차원은 특히 중요하므로 새로운 이름 $\text{rank}$ 을 붙혀서 다룬다.

## Dimension Theorem

!!! def "정리 2.3 차원정리(dimension theorem)"

    벡터공간 $\mathbf{V} , \mathbf{W}$ 와 선형변환 $\mathbf{T}: \mathbf{V} \to \mathbf{W}$ 에 대하여 $\mathbf{V}$ 가 유한차원이면 다음이 성립한다.

    $$ \text{nullity}(\mathbf{T})+\text{rank}(\mathbf{T})= \dim(\mathbf{V} ) $$

- 직관적으로 선형변환에서 nullity 가 커질수록 랭크는 작아진다. 즉, 더 많은 벡터가 영벡터 $0$ 로 갈수록 상공간은 작아진다. 역으로 랭크가 커질수록 nullity 는 작아진다. 이 정리가 랭크과 nullity 의 관계를 말해준다. 

- 증명 

    $\dim(\mathbf{V} ) = n, \dim(\mathbf{N}(\mathbf{T} )) = k$ 라 하고 $\mathbf{N}(\mathbf{T} )$ 의 기저를 $\{v_1, v_2, \dots, v_k\}$ 라 하면 [정리 1.11 따름정리](../VectorSpace#73d920332) 에 의하여 $\{v_1, v_2, \dots, v_k\}$ 를 확장하여 $\mathbf{V}$ 의 기저 $\beta = \{v_1, v_2, \dots, v_n\}$ 을 얻을 수 있다. ▲ 

    그러면 
    
    $$S = \mathbf{T} (\beta - \{v_1, \dots, v_k\}) = \{\mathbf{T} (v _{k+1}), \mathbf{T} (v _{k+2}), \dots, \mathbf{T} (v _{n})\}$$
    
    이 $\mathbf{R}(\mathbf{T} )$ 의 기저임을 보이자. 먼저 $\text{span}(S) = \mathbf{R}(\mathbf{T} )$ 임을 보이기 위하여 $1 \leq i \leq k : \mathbf{T} (v_i) = 0$ 과 [정리 2.2](#f380ab529) 를 사용하면 

    $$ \begin{equation}\begin{split}   \mathbf{R}(\mathbf{T} ) &= \text{span}(\{\mathbf{T} (v_1), \mathbf{T} (v_2), \dots, \mathbf{T} (v_n)\}) \\ &= \text{span}(\{\mathbf{T} (v _{k+1}), \mathbf{T} (v _{k+2}), \dots, \mathbf{T} (v_n)\}) = \text{span}(S) \\ \end{split}\end{equation}\tag*{} $$

    이다. ▲ 

    $S$ 가 선형독립임을 보이기 위하여 $b _{k+1}, \dots, b _{n} \in \mathbf{F}$ 에 대하여 $\displaystyle \sum_{i=k+1}^{n}b_i \mathbf{T} (v_i) = 0$ 라고 하면 $\mathbf{T}$ 가 선형이므로 

    $$ \mathbf{T} \bigg (\sum_{i=k+1}^{n}b_iv_i\bigg ) = 0 \iff \sum_{i=k+1}^{n}b_iv_i \in \mathbf{N}(\mathbf{T} ) $$

    이다. 그러면 다음 식을 만족하는 $c_1, \dots, c_k \in \mathbf{F}$ 가 존재한다.

    $$ \sum_{i=k+1}^{n}b_iv_i = \sum_{i=1}^{k}c_iv_i \iff \sum_{i=1}^{k}(-c_i)v_i + \sum_{i=k+1}^{n}b_iv_i = 0 $$

    이때 $\beta$ 가 기저, 즉 일차독립이므로 이 식이 성립하려면 반드시 $-c_1 = \dots = -c_k = b _{k+1} = \dots = b_n = 0$ 이어야 한다. 그러므로 $S$ 는 일차독립이다. 그러므로 $S$ 는 $\mathbf{R}(\mathbf{T} )$ 의 기저이다. ▲ 

    $S = \mathbf{T} (\beta - \{v_1, \dots, v_k\})$ 가 $\mathbf{R}(\mathbf{T} )$ 의 기저이므로 $\mathbf{T}$ 는 최소한 

    $$ \text{card}(\{v _{k+1}, \dots, v_n\}) = \text{card}(\{\mathbf{T} (v _{k+1}) , \dots, \mathbf{T} (v_n)\}) $$

    을 보장한다. 그러므로 $\text{card}(S) = \text{card}(\beta ) - \text{card}(\{v_1, \dots, v_k\})$ 라고 할 수 있고, 이에 따라 

    $$ \therefore  \text{rank}(\mathbf{T} ) = \dim(\mathbf{V} ) - \text{nullity}(\mathbf{T} ) $$

    이다. ■ 

## Properties of Linear Map, Range, Null Space

!!! def "정리 2.4"

    벡터공간 $\mathbf{V} , \mathbf{W}$ 와 선형변환 $\mathbf{T} : \mathbf{V} \to \mathbf{W}$ 에 대하여 다음은 동치이다. 

    1. $\mathbf{T}$ 가 단사사상이다.

    2. $\mathbf{N}(\mathbf{T} ) = \{0\}$

- 증명

    $x \in \mathbf{N}(\mathbf{T} )$ 이면 $\mathbf{T} (x) = 0 = \mathbf{T} (0)$ 인데, $\mathbf{T}$ 가 [단사](../../Set/Set/#b9a0b7bf1)이므로 $x = 0$ 이다. 또한 이는 $\forall x \in \mathbf{N}(\mathbf{T} ) : x = 0$ 을 의미하므로 $\mathbf{N}(\mathbf{T} ) = \{0\}$ 이다. ▲ 

    역으로 $\mathbf{N}(\mathbf{T} ) = \{0\}$ 과 $\mathbf{T} (x) = \mathbf{T} (y)$ 을 가정하자. 선형변환의 성질 3) 에 의하여 $0 = \mathbf{T} (x) - \mathbf{T} (y) = \mathbf{T} (x - y)$ 이므로 

    $$ x - y \in \mathbf{N}(\mathbf{T} ) = \{0\} \iff x - y = 0 $$

    이다. 즉, $x = y$ 이므로 $\mathbf{T}$ 는 단사함수이다. ■ 

!!! def "정리 2.5"

    유한차원 벡터공간 $\mathbf{V} ,\mathbf{W}$ 에 대하여 $\dim(\mathbf{V} ) = \dim(\mathbf{W} )$ 이면 선형변환 $\mathbf{T} : \mathbf{V} \to \mathbf{W}$ 에 대하여 다음 명제가 동치이다. 

    1. $\mathbf{T}$ 는 단사이다.

    2. $\mathbf{T}$ 는 전사이다.

    3. $\text{rank}(\mathbf{T} ) = \dim(\mathbf{V} )$

- 이 정리는 차원이 같은 유한차원 사이의 선형사상이 단사이면 전단사임을 말해준다. 그러나 무한차원 $\mathbf{V}$ 에 대한 선형사상 $\mathbf{T} : \mathbf{V} \to \mathbf{V}$ 에 대해서는 단사와 전사가 동치가 아니다.

- 증명 

    [차원정리](#6187a9f9c) 에 의하여 $\text{rank}(\mathbf{T} )+\text{nullity}(\mathbf{T} ) = \dim(\mathbf{V} )$ 인데, [정리 2.4](#7d40e8276) 에 의하여 

    $$ \mathbf{T} \text{ is injection } \iff \mathbf{N}(\mathbf{T} ) = \{0\} $$

    $$ \iff \text{nullity}(\mathbf{T} ) = 0 \iff \text{rank}(\mathbf{T} ) = \dim(\mathbf{V} ) $$

    $$ \iff \text{rank}(\mathbf{T} ) = \dim(\mathbf{W} ) \iff \dim(\mathbf{R}(\mathbf{T} )) = \dim(\mathbf{W} ) $$

    이다. 그런데 [정리 1.11](../VectorSpace/#26f9238cb) 에 의하여 

    $$ \iff \mathbf{R}(\mathbf{T} ) = \mathbf{W} $$

    이다. 상공간과 공역이 같으므로 $\mathbf{T}$ 는 전사이다. ■ 

- 예시 

    선형변환 $\mathbf{T} : \mathbf{F} ^{2} \to \mathbf{F} ^{2}$ 이 

    $$ \mathbf{T} (v, w) = (v+w, v) $$

    와 같이 정의되면 $\mathbf{N}(\mathbf{T} ) = \{0\}$ 이므로 $\mathbf{T}$ 는 전단사이다.

!!! def ""

    벡터공간 $\mathbf{V} ,\mathbf{W}$ 의 선형변환 $\mathbf{T} : \mathbf{V} \to \mathbf{W}$ 과 $\mathbf{V}$ 의 부분집합 $S$ 에 대하여 다음이 동치이다.
    
    1. $S$ 가 일차독립이다.

    2. $\mathbf{T} (S)$ 가 일차독립이다.

- 증명

- 예시 

    선형변환 $\mathbf{T} : \mathbf{P} _2(\R) \to \R ^{3}$ 이 

    $$ \mathbf{T} (a_0+a_1x+a_2x ^{2}) = (a_0, a_1, a_2) $$

    와 같이 정의되면 $\mathbf{T}$ 는 단사이다. $S = \{2-x+3x ^{2}, x+x ^{2}, 1-2x ^{2}\}$ 라고 하면 $\mathbf{T} (S) = \{(2,-1,3), (0,1,1), (1,0,-2)\}$ 가 $\R ^{3}$ 에서 일차독립이므로 $S$ 도 일차독립이다.

!!! def "정리 2.6"

    $\mathbf{F}$-벡터공간 $\mathbf{V} , \mathbf{W}$ 와 $\mathbf{V}$ 의 기저 $\{v_1, \dots, v_n\}$ 와 벡터 $w_1, \dots, w_n \in \mathbf{W}$ 에 대하여 

    $$ i \in \{1,2,\dots, n\} : \mathbf{T} (v_i) = w_i $$

    을 만족하는 선형변환 $\mathbf{T} : \mathbf{V} \to \mathbf{W}$ 가 유일하게 존재한다.

- 이 정리는 선형변환이 기저에 따라 어떻게 행동할지 완벽하게 결정된다는 것을 말해준다. 이 정리와 따름정리는 매우 중요해서 선형대수학 전반에 널리 사용된다.

- 증명 

    $x \in \mathbf{V}$ 를 다음과 같이 $a_1, \dots, a_n \in \mathbf{F}$ 에 대하여 기저의 유일한 일차결합 표현으로 나타낼 수 있다. 

    $$ x = \sum_{i=1}^{n}a_iv_i $$

    이때 선형변환 $\mathbf{T} : \mathbf{V} \to \mathbf{W}$ 를 $\mathbf{T} (x) = \sum_{i=1}^{n} a_iw_i$ 로 정의하자. ▲ 

    그리고 먼저 $\mathbf{T}$ 가 선형임을 보이자. $u, v \in \mathbf{V} , d \in \mathbf{F}$ 와 $b_1, \dots, b_n \in \mathbf{F}$ 와 $c_1, \dots, c_n \in \mathbf{F}$ 에 대하여 

    $$ u = \sum_{i=1}^{n}b_iv_i, \enspace v = \sum_{i=1}^{n}c_iv_i $$

    이다. 그러면 $du + v = \sum_{i=1}^{n} (db_i+c_i)v_i$ 이므로 

    $$ \mathbf{T} (du+v) = \sum_{i=1}^{n}(db_i+c_i)w_i = d \sum_{i=1}^{n}b_iw_i + \sum_{i=1}^{n}c_iw_i = d \mathbf{T} (u) + \mathbf{T} (v) $$

    이다. ▲ 

    또한 정의에 의하여 $i \in \{1, \dots, n\} : \mathbf{T} (v_i) = w_i$ 이다. ▲ 

    마지막으로 $\mathbf{T}$ 의 유일성을 보이자. 선형변환 $\mathbf{U}:\mathbf{V} \to \mathbf{W}$ 가 $i \in \{1, \dots, n\} : \mathbf{T} (v_i) = w_i$ 를 만족한다고 하면 $x = \sum_{i=1}^{n}a_iv_i \in \mathbf{V}$ 에 대하여

    $$ \mathbf{U} (x) = \sum_{i=1}^{n}a_i \mathbf{U} (v_i) = \sum_{i=1}^{n}a_iw_i = \mathbf{T} (x) $$

    이므로 $\mathbf{U} =\mathbf{T}$ 이다. ■ 

!!! def "정리 2.6 따름정리"

    벡터공간 $\mathbf{V} , \mathbf{W}$ 에 대하여 $\mathbf{V}$ 가 유한집합 기저 $\{v_1, \dots, v_n\}$ 을 가지면 두 선형변환 $\mathbf{U} , \mathbf{T} : \mathbf{V} \to \mathbf{W}$ 에 대하여 다음이 성립한다.

    $$ i \in \{1, \dots, n\} : \mathbf{U} (v_i) = \mathbf{T} (v_i) \implies \mathbf{U} = \mathbf{T}  $$

- 이 정리는 두 선형변환이 기저에서 상이 같으면 같은 선형변환임을 말하고 있다.

- 예시

    선형변환 $\mathbf{T} :\R ^{2} \to \R ^{2}$ 이 

    $$ \mathbf{T} (a_1, a_2) = (2a_2 - a_1, 3a_1) $$

    와 같이 정의되었다고 하자. 그러면 $\{(1,2), (1,1)\}$ 이 $\R ^{2}$ 의 기저이므로 선형변환 $\mathbf{U} : \R ^{2} \to \R ^{2}$ 이 $\mathbf{U} (1,2)=(3,3), \mathbf{U} (1,1)=(1,3)$ 이면 $\mathbf{U} =\mathbf{T}$ 이다.
    
# Coordinate Vector

!!! def "순서기저(ordered basis)"

    유한차원 벡터공간의 순서가 주어진 기저이다.

- 즉, 순서기저란 일차독립이고 벡터공간을 생성하는 수열이다.

- 예시 

    $\mathbf{F} ^{3}$ 에서 $\beta = \{e_1, e_2, e_3\}, \gamma = \{e_2, e_1, e_3\}$ 은 순서기저이다. 순서기저의 관점에서 $\beta \neq \gamma$ 이다.

- 표준기저와 마찬가지로 표준순서기저(standard ordered basis)도 정의할 수 있다.

    - 예시 
    
        벡터공간 $\mathbf{F} ^{n}$ 에서 $\{e_1, e_2, \dots, e_n\}$ 을 표준순서기저라고 한다.

        벡터공간 $\mathbf{P}_n(\mathbf{F} )$ 에서 $\{1, x, \dots, x ^{n}\}$ 이 표준순서기자이다.

!!! def "좌표벡터(coordinate vector)"

    유한차원 벡터공간 $\mathbf{V}$ 의 순서기저 $\beta = \{u_1, u_2, \dots, u_n\}$ 와 벡터 $x \in \mathbf{V}$ 에 대하여 $x = \displaystyle  \sum_{i=1}^{n}a_iu_i$ 을 만족하는 유일한 스칼라 $a_1, a_2, \dots, a_n$ 가 존재한다. 이때 $\beta$ 에 대한 $x$ 의 좌표벡터 $[x] _{\beta }$ 를 

    $$ [x] _{\beta } = \begin{pmatrix} a_1\\ a_2\\ \vdots\\ a_n \end{pmatrix} $$

    와 같이 정의한다.

- $[x] _{\beta }$ 를 $x$ 라는 벡터를 기저 $\beta$ 의 일차결합으로 나타낸 것의 coefficient matrix 라고 생각하면 편하다.

- 변환 $\mathbf{V} \to \mathbf{F} ^{n}, x \mapsto [x] _{\beta }$ 는 선형변환이다.

    - 증명

- 예시 

    순서기저 $\beta = \{1, x, x ^{2}\}$ 를 가지는 벡터공간 $\mathbf{V} = \mathbf{P} _2 (\R)$ 에 대하여 

    $$ f(x) = 4+6x-7x ^{2} \iff [f] _{\beta } = \begin{pmatrix} 4\\ 6\\ -7\\ \end{pmatrix} $$

    이다.

- 예시 

    표준순서기저를 순서기저 $\beta$ 로 갖는 벡터공간 $\R ^{3}$ 에 대하여 벡터 $x \in \R ^{3}$ 가 $x = (-100, 2, 50)$ 이라면 

    $$ x = -100  e_1 + 2  e_2 + 50  e_3 $$

    이므로 

    $$ [x] _{\beta } = \begin{pmatrix} -100\\ 2\\ 50\\ \end{pmatrix} $$

    이 된다.

!!! def ""

    벡터공간 $\mathbf{F} ^{n}$ 와 표준순서기저 $\beta = \{e_1, e_2, \dots, e_n\}$ 와 벡터 $x \in \mathbf{F} ^{n}$ 에 대하여 

    $$ [x] _{\beta} = x $$

    이다.

- 이는 어떤 벡터의 좌표벡터를 표준순서기저에 대하여 나타낸다면 그 결과가 결국 본래의 벡터라는 것을 말해준다. 

- 증명 

    $$ x = \begin{pmatrix} x_1\\ x_2\\ \vdots \\ x_n\\ \end{pmatrix} = x_1 e_1 + x_2 e_2 + \dots + x_n e_n = \sum_{i=1}^{n}x_ie_i \implies [x] _{\beta } = \begin{pmatrix} x_1\\ x_2\\ \vdots \\ x_n\\ \end{pmatrix} \tag*{■} $$

# Matrix Representation of Linear Map

!!! def "선형변환의 행렬표현(matrix representation)"

    유한차원 벡터공간 $\mathbf{V} , \mathbf{W}$ 의 각각의 순서기저 $\beta = \{v_1, \dots, v_n\}, \gamma = \{w_1, \dots, w_m\}$ 에 대하여 선형변환 $\mathbf{T} : \mathbf{V} \to \mathbf{W}$ 을 정의하면 $j \in \{1,\dots,n\}, i \in \{1, \dots, m\}$ 에 대하여

    $$ \mathbf{T} (v_j) = \sum_{i=1}^{m}a _{ij}w_i $$

    을 만족하는 유일한 스칼라 $a _{ij}\in \mathbf{F}$ 가 존재한다. 성분이 $A _{ij} = a _{ij}$ 인 $m \times n$ 행렬 $A$ 를 순서기저 $\beta , \gamma$ 에 대한 선형변환 $\mathbf{T}$ 의 행렬표현

    $$ \boxed{A = [\mathbf{T} ] ^{\gamma } _{\beta } }$$ 

    라 한다.

- 스칼라 $a _{ij}$ 의 유일성은 [정리 1.8](../VectorSpace/#8a514fc5c) 이 보장해준다. 

- 우리는 이렇게 행렬과 선형변환을 연결했는데, [정리 2.8](#aa431d8ac) 은 이 연결이 합과 스칼라 곱을 보존함을 말해준다. 이를 위해 먼저 선형변환의 합과 스칼라 곱을 정의해볼 것이다.

- **$\mathbf{V} = \mathbf{W} \land \beta = \gamma$ 이면 간단하게 $A = [\mathbf{T} ]_{\beta }$ 라고 표기한다.**

- **$A$ 의 $j$ 열은 $[\mathbf{T} (v_j)] _{\gamma }$ 이다.**

- 선형변환 $\mathbf{U} : \mathbf{V} \to \mathbf{W}$ 가 $[\mathbf{U} ] ^{\gamma } _{\beta } = [\mathbf{T} ]^{\gamma }_{\beta }$ 를 만족하면 [정리 2.6 따름정리](#52dd3d90f) 에 의하여 $\mathbf{U} = \mathbf{T}$ 이다.

- 예시 

    선형변환 $\mathbf{T} : \R ^{2} \to \R ^{3} , (a_1, a_2) \mapsto (a_1 + 3a_2, 0, 2a_1 - 4a_2)$ 를 정의하고 $\R ^{2}, \R ^{3}$ 의 순서기저 $\beta , \gamma$ 를 각각의 표준순서기저로 두면 

    $$ \mathbf{T} (1, 0) = (1, 0, 2) = 1e_1 + 0e_2 + 2e_3 $$ 

    $$ \mathbf{T} (0, 1) = (3, 0, -4) = 3e_1 + 0e_2 - 4e_3 $$ 

    가 성립하므로 

    $$ [\mathbf{T} ]^{\gamma } _{\beta } = \begin{pmatrix} 1&3\\ 0&0\\ 2&-4\\ \end{pmatrix} $$

    이다. 만약 $\R ^{3}$ 의 순서기저로써 $\gamma ' = \{e_3, e_2, e_1\}$ 를 가져오면 

    $$ [\mathbf{T} ] ^{\gamma '} _{\beta } =\begin{pmatrix} 2&-4\\ 0&0\\ 1&3\\ \end{pmatrix} $$

    이 된다.

- 예시 

    선형변환 $\mathbf{T} : \mathbf{P} _3(\R) \to \mathbf{P} _2(\R)$ 가 $\mathbf{T} (f(x)) = f'(x)$ 와 같이 정의되었고,  $\mathbf{P} _3(\R), \mathbf{P} _2(\R)$ 의 순서기저 $\beta , \gamma$ 를 표준순서기저라 하면 

    $$ \mathbf{T} (1) = 0 \cdot 1 + 0 \cdot x + 0 \cdot x ^{2} $$

    $$ \mathbf{T} (x) = 1 \cdot 1 + 0 \cdot x + 0 \cdot x ^{2} $$

    $$ \mathbf{T} (x ^{2}) = 0 \cdot 1 + 2 \cdot x + 0 \cdot x ^{2} $$

    $$ \mathbf{T} (x ^{3}) = 0 \cdot 1 + 0 \cdot x + 3 \cdot x ^{2} $$

    이 성립하므로 

    $$ [\mathbf{T} ]^{\gamma } _{\beta } = \begin{pmatrix} 0&1&0&0\\ 0&0&2&0\\ 0&0&0&3\\ \end{pmatrix} $$

    이다.

!!! def ""

    영변환의 행렬표현은 영행렬이다.

- 예시 

    유한차원 벡터공간 $\mathbf{V} , \mathbf{W}$ 의 순서기저를 $\beta = \{v_1, \dots, v_n\}, \gamma = \{w_1, \dots, w_m\}$ 이라 하면 

    $$ \mathbf{T} _0(v_j) = 0 = 0w_1+\dots+0w_m $$

    이므로 $[\mathbf{T} _0] ^{\gamma } _{\beta } = O$ 이다. $O$ 는 $m \times n$ 영행렬이다.

!!! def ""

    항등변환의 행렬표현은 항등행렬이다.

- 예시

    유한차원 벡터공간 $\mathbf{V} , \mathbf{W}$ 의 순서기저를 $\beta = \{v_1, \dots, v_n\}, \gamma = \{w_1, \dots, w_n\}$ 이라 하면 

    $$ \mathbf{I} _{\mathbf{V} }(v_j) = v_j = 0v_1 + \dots + 0v _{j-1} + 1v_j+ 0 v _{j+1}  \dots + 0 v_n $$

    이므로 $\mathbf{I} _{\mathbf{V} }$ 의 $j$ 열은 $e_j$ 이다. 따라서 

    $$ [\mathbf{I} _{\mathbf{V} }]_{\beta } = \begin{pmatrix} 1&0&\dots&0\\ 0&1&\dots&0\\ \vdots & \vdots & \ddots & \vdots \\ 0&0&\dots&1\\ \end{pmatrix} = I_n $$ 

    이다. $[\mathbf{I} _{\mathbf{V} }]_{\beta }$ 는 $n \times n$ 항등행렬 $I_n$ 이다.

!!! def "문제 2.2-12"

    벡터공간 $\mathbf{V}$ 의 순서기저 $\beta = \{v_1, v_2, \dots, v_n\}$ 와 선형연산자 $\mathbf{T}$ 와 $j \in \{1, \dots, n\}$ 에 대하여 $[\mathbf{T}]_{\beta }$ 가 상삼각행렬인 것과 $\mathbf{T}(v_j) \in \text{span} (\{v_1, v_2, \dots, v_j\})$ 인 것은 동치이다.

- 증명

    $[\mathbf{T}]_{\beta }$ 가 상삼각행렬이면 다음이 성립한다. 

    $$ \mathbf{T}(v_j) = \sum_{i=1}^{j}a _{ij}v_i \in \text{span} (\{v_1, v_2, \dots, v_j\}) \tag*{▲} $$

    $\mathbf{T}(v_j) \in \text{span} (\{v_1, v_2, \dots, v_j\})$ 를 가정하면 다음이 성립한다. 

    $$ \mathbf{T}(v_j) = \sum_{i=1}^{j}a _{ij}v_i $$

    따라서 $[\mathbf{T}]_{\beta }$ 는 상삼각행렬이다. ■ 

# Kronecker delta

!!! def "크로네커 델타(Kronecker delta)"

    $$\delta _{ij} = \begin{cases} 1 & i = j\\ 0 & i \neq j\\ \end{cases}$$

- 예시 

    $n \times n$ 항등행렬 $I_n$ 의 성분은 $(I_n) _{ij} = \delta _{ij}$ 이다.

# Addition, Multiples of Linear Maps

!!! def ""

    $\mathbf{F}$-벡터공간 $\mathbf{V} , \mathbf{W}$ 에서 정의된 임의의 함수 $\mathbf{T} , \mathbf{U} : \mathbf{V} \to \mathbf{W}$ 와 $a \in \mathbf{F}$ 와 $\forall x \in \mathbf{V}$ 에 대하여 두 함수의 합과 스칼라곱을 다음과 같이 정의한다.

    - $\mathbf{T} + \mathbf{U} : \mathbf{V} \to \mathbf{W}, (\mathbf{T} + \mathbf{U} )(x) = \mathbf{T} (x) + \mathbf{U} (x)$

    - $a \mathbf{T} : \mathbf{V} \to \mathbf{W}, (a \mathbf{T} )(x) = a \mathbf{T} (x)$

- 이는 함수의 합의 스칼라 곱에 대한 보편적 정의인데 선형변환의 합과 스칼라 곱이 여전히 선형임을 [다음 정리](#91b876399)가 말해준다.

## Set of All Linear Maps is Vector Space

!!! def "정리 2.7"

    $\mathbf{F}$-벡터공간 $\mathbf{V} , \mathbf{W}$ 와 선형변환 $\mathbf{T} , \mathbf{U} : \mathbf{V} \to \mathbf{W}$ 에 대하여 다음이 성립한다.

    1. $\forall a \in \mathbf{F}$ 에 대하여 $a \mathbf{T} + \mathbf{U}$ 은 선형이다.

    2. $\mathbf{V} \to \mathbf{W}$ 에서 정의된 모든 선형변환의 집합은 $\mathbf{F}$-벡터공간이다.

- 증명

    1:

    $x, y \in \mathbf{V} , c \in \mathbf{F}$ 에 대하여 다음이 성립한다. 

    $$ \begin{equation}\begin{split}   (a \mathbf{T} + \mathbf{U} )(cx+y)&=a \mathbf{T} (cx+y) + \mathbf{U} (cx + y)\\ &=a[\mathbf{T} (cx+y)] + c \mathbf{U} (x) + \mathbf{U} (y)\\ &=a[c\mathbf{T} (x) + \mathbf{T}(y)] + c \mathbf{U} (x) + \mathbf{U} (y)\\ &=ac\mathbf{T} (x) + c\mathbf{U}(x) + a \mathbf{T} (y) + \mathbf{U} (y)\\ &=c(a\mathbf{T} + \mathbf{U} ) (x) + (a \mathbf{T} + \mathbf{U} )(y)\\ \end{split}\end{equation}\tag*{} $$

    그러므로 $a \mathbf{T} + \mathbf{U}$ 는 선형이다. ■ 

    2:

    [위의 정의](#63a07e35d)는 임의의 함수에 대한 두 함수의 합, 스칼라 곱을 정의한 것이므로 선형변환의 합과 스칼라곱에도 적용된다. 그러므로 이 합과 스칼라 곱을 만족하는 선형변환 집합이 [벡터공간의 조건](../VectorSpace#57bd9d1ab)을 만족하는지 확인하면 된다. 

    $\mathbf{V} \to \mathbf{W}$ 에서 정의된 모든 선형변환의 집합을 $\mathcal{L}$ 라고 하자. 그러면 영변환 $\mathbf{L} _0: \mathbf{V} \to \mathbf{W}$ 는 $\mathcal{L}$ 에서 영벡터의 역할을 한다. 또한 $\mathcal{L}$ 가 벡터공간의 8 가지 조건을 만족한다는 것을 쉽게 확인할 수 있다. 

    그러므로 $\mathcal{L}$ 는 $\mathbf{F}$-벡터공간이다. ■ 

!!! def "벡터공간 $\mathcal{L}(\mathbf{V} , \mathbf{W} )$ "

    벡터공간 $\mathcal{L}(\mathbf{V} , \mathbf{W} )$ 은 $\mathbf{F}$-벡터공간 $\mathbf{V} , \mathbf{W}$ 에 대하여 $\mathbf{V} \to \mathbf{W}$ 에서 정의된 모든 선형변환의 집합이다.

- $\mathbf{V} = \mathbf{W}$ 이면 간단하게 $\mathcal{L}(\mathbf{V} )$ 라 표기한다.

- 참고로 2.4 절에서 차원 $\dim(\mathbf{V} ) = n, \dim(\mathbf{W} ) = m$ 인 벡터공간 $\mathbf{V} , \mathbf{W}$ 에 대하여 $\mathcal{L}(\mathbf{V} , \mathbf{W} )$ 와 $\mathbf{M} _{m \times n}(\mathbf{F} )$ 가 본질적으로 같다는 것을 보일 것이다.

!!! def "정리 2.8"

    체 $\mathbf{F}$ 에 대한 유한차원 $\mathbf{F}$-벡터공간 $\mathbf{V} , \mathbf{W}$ 와 각각의 순서기저 $\beta , \gamma$ 와 선형변환 $\mathbf{T} , \mathbf{U} : \mathbf{V} \to \mathbf{W}$ 에 대하여 다음이 성립한다. 

    1. $[\mathbf{T} + \mathbf{U} ] ^{\gamma } _{\beta } = [\mathbf{T} ] ^{\gamma } _{\beta } + [\mathbf{U} ] ^{\gamma } _{\beta }$

    2. $\forall a \in \mathbf{F} ,[a \mathbf{T} ] ^{\gamma } _{\beta } = a[ \mathbf{T} ] ^{\gamma } _{\beta }$

- 증명

    $\beta = \{v_1, \dots, v_n\}, \gamma = \{w_1, \dots, w_m\}$ 에 대하여 

    $$ \mathbf{T} (v_j) = \sum_{i=1}^{m}a _{ij}w_i, \enspace  \mathbf{U} (v_j) = \sum_{i=1}^{m}b _{ij}w_i, \qquad j \in \{1, \dots, n\} $$

    을 만족하는 유일한 스칼라 $a _{ij}, b _{ij} \enspace (i \leq i \leq m, 1 \leq j \leq n)$ 가 존재한다. 즉, 

    $$ (\mathbf{T} + \mathbf{U} ) (v_j) = \sum_{i=1}^{m}(a _{ij} + b _{ij}) w_i $$

    이고 

    $$ ([\mathbf{T} + \mathbf{U} ] ^{\gamma } _{\beta }) _{ij} = a _{ij} + b _{ij} = ([\mathbf{T} ] ^{\gamma } _{\beta } + [\mathbf{U} ] ^{\gamma } _{\beta }) _{ij} $$

    이다. ▲ 

    두번째도 행렬의 원소가 같다는 것을 보이는 방식으로 증명가능하다. ■ 

- 예시 

    선형변환 $\mathbf{T} : \R ^{2} \to \R ^{3}, \mathbf{U} : \R ^{2} \to \R ^{3}$ 을 

    $$ \mathbf{T} (a_1, a_2) = (a_1 + 3a_2, 0, 2a_1 - 4a_2), \enspace \mathbf{U} (a_1, a_2) = (a_1 - a_2, 2a_1, 3a_1 + 2a_2) $$

    와 같이 정의하고, $\R ^{2}, \R ^{3}$ 의 순서기저로써 각각의 표준순서기저 $\beta , \gamma$ 를 두면 

    $$ \mathbf{T} (1, 0) = (1, 0, 2) = 1e_1 + 0e_2 + 2e_3 $$
    
    $$ \mathbf{T} (0, 1) = (3, 0, -4) = 3e_1 + 0e_2 + -4e_3 $$

    이고, $\mathbf{U}$ 의 경우도 표준순서기저의 일차결합의 스칼라를 구해보면
    
    $$ [\mathbf{T} ] ^{\gamma } _{\beta } = \begin{pmatrix} 1&3\\ 0&0\\ 2&-4\\ \end{pmatrix}, [\mathbf{U} ] ^{\gamma } _{\beta } = \begin{pmatrix} 1&-1\\ 2&0\\ 3&2\\ \end{pmatrix} $$

    이 성립한다.  ▲ 

    $\mathbf{T} + \mathbf{U}$ 는 [정의](#63a07e35d)에 따라 

    $$ (\mathbf{T} + \mathbf{U} )(a_1, a_2) = (2a_1 + 2a_2, 2a_1, 5a_1 - 2a_2) $$

    이다. 그러면 

    $$ (\mathbf{T} + \mathbf{U} )(1, 0) = (2, 2, 5) = 2e_1 + 2e_2 + 5e_3 $$

    $$ (\mathbf{T} + \mathbf{U} )(0, 1) = (2, 0, -2) = 2e_1 + 0e_2 - 2e_3 $$

    이므로

    $$ [\mathbf{T} + \mathbf{U} ] ^{\gamma } _{\beta } = \begin{pmatrix} 2&2\\ 2&0\\ 5&-2\\ \end{pmatrix} $$

    이다. 그러므로 $[\mathbf{T} + \mathbf{U} ] ^{\gamma}_{\beta} = [\mathbf{T} ] ^{\gamma}_{\beta}+[\mathbf{U} ]^{\gamma}_{\beta}$ 임을 알 수 있다. ■ 

# Composition of Linear Map

!!! def "정리 2.9"

    $\mathbf{F}$-벡터공간 $\mathbf{V} ,\mathbf{W} , \mathbf{Z}$ 와 선형변환 $\mathbf{T} : \mathbf{V} \to \mathbf{W} , \mathbf{U} : \mathbf{W} \to \mathbf{Z}$ 에 대하여 두 선형변환의 합성 $\mathbf{U} \mathbf{T} : \mathbf{V} \to \mathbf{Z}$ 는 선형이다.

- 두 선형변환 $\mathbf{U} , \mathbf{T}$ 의 합성 $\mathbf{U} \circ \mathbf{T}$ 을 편의상 $\mathbf{U} \mathbf{T}$ 로 표기하자.

- 증명

    $x, y \in \mathbf{V} , a \in \mathbf{F}$ 에 대하여 

    $$ \begin{equation}\begin{split}   \mathbf{U} \mathbf{T} (ax + y)&= \mathbf{U} (\mathbf{T} (ax +y)) \\ &= \mathbf{U} (a \mathbf{T} (x) + \mathbf{T} (y))\\ &=a \mathbf{U} (\mathbf{T} (x)) + \mathbf{U} (\mathbf{T} (y)) \\ &=a (\mathbf{U} \mathbf{T} )(x) + \mathbf{U} \mathbf{T} (y) \\ \end{split}\end{equation}\tag*{} $$

    이 성립한다. ■ 

!!! def "문제 2.3-12"

    $\mathbf{F}$-벡터공간 $\mathbf{V} ,\mathbf{W} , \mathbf{Z}$ 와 선형변환 $\mathbf{T} : \mathbf{V} \to \mathbf{W} , \mathbf{U} : \mathbf{W} \to \mathbf{Z}$ 과 그 합성변환 $\mathbf{UT} : \mathbf{V} \to \mathbf{Z}$ 대하여 다음이 성립한다.

    1. $\mathbf{UT}$ 가 단사이면 $\mathbf{T}$ 도 단사이다.

    2. $\mathbf{UT}$ 가 전사이면 $\mathbf{U}$ 도 전사이다.

    3. $\mathbf{T} , \mathbf{U}$ 가 전단사이면 $\mathbf{UT}$ 도 전단사이다.

- 증명

    1:

    [$\mathbf{U} \circ \mathbf{T}$ 가 단사이면 $\mathbf{S} \circ (\mathbf{U} \circ \mathbf{T} ) = \mathbf{I} _{\mathbf{V}}$ 을 만족하는 변환 $\mathbf{S}: \mathbf{Z} \to \mathbf{V}$ 가 존재](../../Set/Set/#5869db153)한다. [함수의 합성은 결합법칙을 만족](../../Set/Set/#ede6df07e)하므로

    $$ \mathbf{S} \circ (\mathbf{U} \circ \mathbf{T} ) = (\mathbf{S} \circ \mathbf{U} ) \circ \mathbf{T}  = \mathbf{I} _{\mathbf{V} } $$

    이다. [단사함수와의 동치명제에 대한 정리](../../Set/Set/#5869db153)에 의하여 $\mathbf{T}$ 는 단사이다. ▲ 

    이로써 $\mathbf{UT}, \mathbf{T}$ 가 단사임을 가정할 수 있다. 이제 $\mathbf{UT}$ 가 단사이면 $\mathbf{U}$ 도 단사여야 하는지 살펴보자. $\mathbf{U}$ 가 [단사](../../Set/Set/#b9a0b7bf1)가 아니라고 가정하면 $\mathbf{U} (y_1) = \mathbf{U} (y_2) \implies y_1 \neq y_2$ 를 만족하는 $y_1, y_2 \in \mathbf{W}$ 가 존재한다. $y_1 = \mathbf{T} (x_1), y_2 = \mathbf{T} (x_2)$ 라고 하면 

    $$ \mathbf{U} (\mathbf{T} (x_1)) = \mathbf{U} (\mathbf{T} (x_2)) $$

    이므로 $\mathbf{UT}$ 가 단사인 것에서 $x_1 = x_2$ 이다. 그러면 $\mathbf{T} (x_1) = \mathbf{T} (x_2) = y_1 = y_2$ 이다. 이는 모순이다. 그러므로 $\mathbf{U}$ 는 단사이다. 

    그러나 $y_1 = \mathbf{T} (x_1), y_2 = \mathbf{T} (x_2)$ 를 가정할 수 없는 경우 즉, $\mathbf{T}$ 의 함수값이 $y_1, y_2$ 에서 정의되지 않은 경우 $\mathbf{U}$ 가 단사라는 것을 보장 할 수 없다. 실제로 $\mathbf{U}$ 가 $\mathbf{W} \to \mathbf{Z}$ 위에서 단사가 아니어도 $\mathbf{T}$ 의 함수값이 정의된 곳에서, 즉 $\mathbf{R} (\mathbf{T}) \to \mathbf{Z}$ 위에서는 $\mathbf{U}$ 가 단사라면 $\mathbf{UT}$ 가 단사라는 조건에 모순되지 않는다. 그러므로 $\mathbf{U}$ 가 반드시 단사라고 할 수 없다. ▲ 

    2:
    
    [$\mathbf{U} \circ \mathbf{T}$ 가 전사이면 $(\mathbf{U} \circ \mathbf{T} ) \circ \mathbf{S} = \mathbf{I} _{\mathbf{W}}$ 을 만족하는 변환 $\mathbf{S}: \mathbf{Z}\to \mathbf{V}$ 가 존재](../../Set/Set/#d9b0737d6)한다. [함수의 합성은 결합법칙을 만족](../../Set/Set/#ede6df07e)하므로

    $$ (\mathbf{U} \circ \mathbf{T} ) \circ \mathbf{S} = \mathbf{U} \circ  (\mathbf{T} \circ \mathbf{S} ) = \mathbf{I} _{\mathbf{W} } $$

    이다. [전사함수와의 동치명제에 대한 정리](../../Set/Set/#d9b0737d6)에 의하여 $\mathbf{T}$ 는 단사이다. ▲ 

    이로써 $\mathbf{UT}, \mathbf{T}$ 가 전사임을 가정할 수 있다. $\mathbf{T}$ 도 전사여야 하는지 살펴보자. $\mathbf{T}$ 가 전사가 아니라면 $x \in \mathbf{W} \land x \not\in \mathbf{R} (\mathbf{T})$ 인 $x$ 가 존재한다. $\mathbf{U}$ 가 전사이므로 $\mathbf{T}$ 의 함수값이 정의되지 않은 $x \in \mathbf{W}$ 에 대한 함수값 $\mathbf{U} (x) \in \mathbf{Z}$ 가 항상 존재한다. 따라서 $\mathbf{UT}$ 가 전사이기 위하여 $\mathbf{U} (x) = \mathbf{U} (\mathbf{T} (a))$ 를 만족하는 $a \in \mathbf{V}$ 가 존재해야 한다. 즉, 조건

    $$ x \in \mathbf{W} \land x \not\in \mathbf{R} (\mathbf{T}) \implies a \in \mathbf{R} (\mathbf{T}) \land \mathbf{U} (\mathbf{T} (a)) = \mathbf{U} (x) $$
    
    이 만족된다면 $\mathbf{T}$ 가 전사일 필요는 없다. ▲ 

    3:

    $\mathbf{T} , \mathbf{U}$ 가 [전단사](../../Set/Set/#3a14a1347)이면 [역함수 $\mathbf{T}^{-1} : \mathbf{W} \to \mathbf{V} , \mathbf{U} ^{-1} : \mathbf{Z}\to \mathbf{W}$ 가 존재한다](../../Set/Set/#4d4309496). 또한 [함수의 합성은 결합법칙을 만족하므로](../../Set/Set/#ede6df07e)

    $$ (\mathbf{U} \circ \mathbf{T}) \circ (\mathbf{T} ^{-1} \circ \mathbf{U} ^{-1}) = \mathbf{U} \circ \mathbf{I} _{\mathbf{W}} \circ \mathbf{U} ^{-1} = \mathbf{I} _{\mathbf{Z}} $$

    $$ (\mathbf{T} ^{-1} \circ \mathbf{U} ^{-1}) \circ (\mathbf{U} \circ \mathbf{T}) = \mathbf{T} ^{-1} \circ \mathbf{I} _{\mathbf{W}} \circ \mathbf{T} = \mathbf{I} _{\mathbf{V} } $$
    
    이다. [역함수가 존재함은 전단사 함수인 것과 동치](../../Set/Set/#4d4309496) 이므로 $\mathbf{U} \mathbf{T}$ 는 전단사이다. ■ 

!!! def "정리 2.10"

    체 $\mathbf{F}$ 에 대한 $\mathbf{F}$-벡터공간 $\mathbf{V}$ 와 선형연산자 $\mathbf{T} , \mathbf{U} _1, \mathbf{U} _2$ 에 대하여 다음이 성립한다.

    1. $\mathbf{T} (\mathbf{U} _1 + \mathbf{U} _2) = \mathbf{T} \mathbf{U} _1 + \mathbf{T} \mathbf{U} _2$

    2. $(\mathbf{U} _1 + \mathbf{U} _2)\mathbf{T} = \mathbf{U} _1 \mathbf{T} +\mathbf{U} _2 \mathbf{T}$

    3. $\mathbf{T} (\mathbf{U} _1 \mathbf{U} _2) = (\mathbf{T} \mathbf{U} _1) \mathbf{U} _2$

    4. $\mathbf{T} \mathbf{I} = \mathbf{I} \mathbf{T} = \mathbf{T}$

    5. $\forall a \in \mathbf{F} : a(\mathbf{U} _1 \mathbf{U} _2) = (a \mathbf{U} _1)\mathbf{U} _2 = \mathbf{U} _1(a \mathbf{U} _2)$

- 증명

    1:

    [함수의 덧셈의 정의](#63a07e35d)에 의하여 다음이 성립한다.

    $$ \mathbf{T}(\mathbf{U}_{1} + \mathbf{U}_{2})(x) = \mathbf{T}(\mathbf{U}_{1}(x) + \mathbf{U}_{2}(x)) $$ 

    이 결과는 [선형변환의 정의](#98f9dba02)에 의하여 다음과 같아진다.

    $$ = \mathbf{T}(\mathbf{U}_{1}(x) + \mathbf{U}_{2}(x)) = \mathbf{T}(\mathbf{U}_{1}(x)) + \mathbf{T}(\mathbf{U}_{2}(x)) = (\mathbf{T}\mathbf{U}_{1})(x) + (\mathbf{T}\mathbf{U}_{2})(x) $$

    이 결과는 다시 함수의 덧셈의 정의에 의하여 다음과 같아진다.

    $$ = (\mathbf{T}\mathbf{U}_{1} + \mathbf{T}\mathbf{U}_{2})(x) $$

    따라서 $\mathbf{T} (\mathbf{U} _1 + \mathbf{U} _2) = \mathbf{T} \mathbf{U} _1 + \mathbf{T} \mathbf{U} _2$ 이다. ▲ 

    2: 

    [함수의 덧셈의 정의](#63a07e35d)에 의하여 다음이 성립한다.

    $$ (\mathbf{U}_{1} + \mathbf{U}_{2})(\mathbf{T}(x)) = \mathbf{U}_{1}(\mathbf{T}(x)) + \mathbf{U}_{2}(\mathbf{T}(x)) = (\mathbf{U}_{1}\mathbf{T})(x) + (\mathbf{U}_{2}\mathbf{T})(x) = (\mathbf{U}_{1}\mathbf{T} + \mathbf{U}_{2}\mathbf{T})(x) \tag*{▲} $$

    3: 

    [함수의 합성은 결합법칙을 만족한다.](../../Set/Set/#ede6df07e) 선형변환은 함수이다. ▲ 

    4:

    자명하다. ▲ 

    5:

    [함수의 스칼라곱의 정의](#63a07e35d)에 의하여 다음이 성립한다.

    $$ ((a \mathbf{U}_{1})\mathbf{U}_{2})(x) = a (\mathbf{U}_{1}\mathbf{U}_{2})(x) $$

    다시 [함수의 스칼라곱의 정의](#63a07e35d)에 의하여 다음이 성립한다. 

    $$ (\mathbf{U}_{1}(a \mathbf{U}_{2}))(x) = \mathbf{U}_{1}(a \cdot \mathbf{U}_{2}(x)) $$

    그러면 다음과 같이 선형변환의 정의에 의하여 스칼라 $a$ 를 바깥으로 뺄 수 있다.

    $$ \mathbf{U}_{1}(a \cdot \mathbf{U}_{2}(x)) = a (\mathbf{U}_{1}(\mathbf{U}_{2}(x))) = a (\mathbf{U}_{1}\mathbf{U}_{2})(x) \tag*{■} $$

- 이 정리는 선형변환의 정의역과 공역이 같은 경우를 말하고 있지만, 선형변환의 정의역과 공역이 같지 않으면 더 일반적인 결과가 성립한다. 

    - 증명

!!! def ""

    벡터공간 $\mathbf{V}$ 에서 정의된 선형변환 $\mathbf{T} \in \mathcal{L}(\mathbf{V} )$ 와 $k \in \N$ 에 대하여 다음과 같이 정의한다.

    $$ \mathbf{T} ^{k} = \begin{cases} \mathbf{T} ^{k-1} \mathbf{T}  & k \geq 2\\ \mathbf{T}  & k = 1\\ \mathbf{I} _{\mathbf{V} }  & k = 0\\ \end{cases} $$

- 예시 

    무한번 미분가능한 실함수 집합 $\mathbf{V}$ 에 대하여 $\mathbf{T} : \mathbf{V} \to \mathbf{V}, \mathbf{T} (f) = f'$ 와 같이 정의된 선형변환의 합성을 표현할 때 

    $$ \mathbf{T} \mathbf{T} (f) = \mathbf{T} ^{2} (f) = \mathbf{T} (f') = (f')' = f'' $$

    $$ \mathbf{T} \mathbf{T} \mathbf{T}  (f) = \mathbf{T} ^{3} (f) = \mathbf{T} ^{2} (f') = \mathbf{T}  (f'') = f''' $$

    와 같이 표현한다.

## Matrix Multiplication

!!! def "행렬곱(matrix multiplication, matrix product)"

    $m \times n$ 행렬 $A$ 와 $n \times p$ 행렬 $B$ 에 대하여 두 행렬 $A, B$ 의 곱 $AB$ 는 $1 \leq i \leq m, 1 \leq j \leq p$ 에 대하여

    $$ (AB) _{ij} = \sum_{k=1}^{n}A _{ik}B _{kj} $$

    인 $m \times p$ 행렬이다.

- $(AB) _{ij}$ 를 $A$ 의 $i$ 행과 $B$ 의 $j$ 열의 성분들을 곱하고 합한 것으로 보면 편하다. 

- 행렬곱이 실제로 어떻게 이루어지는지 살펴보자. $m \times n$ 행렬 $A$, $n \times p$ 행렬 $B$ 의 실제모습을 다음과 같이 살펴보자. 

    $$ A = \begin{pmatrix} a _{11} & a _{12} & \dots & a _{1n}\\ a _{21} & a _{22} & \dots & a _{2n}\\ \vdots& \vdots& \ddots& \vdots \\ a _{m1} & a _{m2} & \dots & a _{mn}\\ \end{pmatrix}, B = \begin{pmatrix} b_{11} & b_{12} & \dots & b_{1p}\\ b_{21} & b_{22} & \dots & b_{2p}\\ \vdots& \vdots& \ddots& \vdots \\ b_{n1} & b_{n2} & \dots & b_{np}\\ \end{pmatrix}, $$

    이 두 행렬의 행렬곱 $m \times p$ 행렬 $AB$ 의 실제 모습은 다음과 같다. 

    $$ \begin{equation}\begin{split} AB &= \begin{pmatrix} a _{11} b _{11} + \dots + a _{1n} b _{n1} & a _{11} b _{12} + \dots + a _{1n} b _{n2} & \dots& a _{11} b _{1p} + \dots + a _{1n} b _{np} \\ a _{21} b _{21} + \dots + a _{2n} b _{n1} & a _{21} b _{12} + \dots + a _{2n} b _{n2} & \dots& a _{21} b _{1p} + \dots + a _{2n} b _{np} \\ \vdots& \vdots& \ddots& \vdots \\ a _{m1} b _{11} + \dots + a _{mn} b _{n1} & a _{m1} b _{12} + \dots + a _{mn} b _{n2} & \dots& a _{m1} b _{1p} + \dots + a _{mn} b _{np} \\ \end{pmatrix}\\ &= \begin{pmatrix} \sum_{k=1}^{n} a _{1k}b _{k1} & \sum_{k=1}^{n} a _{1k}b _{k2} & \dots& \sum_{k=1}^{n} a _{1k}b _{kp} \\ \sum_{k=1}^{n} a _{2k}b _{k1} & \sum_{k=1}^{n} a _{2k}b _{k2} & \dots& \sum_{k=1}^{n} a _{2k}b _{kp} \\ \vdots& \vdots& \ddots& \vdots \\ \sum_{k=1}^{n} a _{mk}b _{k1} & \sum_{k=1}^{n} a _{mk}b _{k2} & \dots& \sum_{k=1}^{n} a _{mk}b _{kp} \\ \end{pmatrix} \end{split}\end{equation} \tag*{} $$

    그러므로 $m \times p$ 행렬 $AB$ 의 $i$ 열 $j$ 행 성분은 

    $$ (AB) _{ij} = \sum_{k=1}^{n} a _{ik}b _{kj} $$

    이다. 

- 지금까지 하고 있는 일은 선형변환과 행렬 간의 대응관계를 연구하는 것이다. 먼저 [선형변환과 행렬의 대응](#c16bc5e5b)을 살펴보았다. 그리고 [선형변환의 합과 스칼라곱을 정의](#63a07e35d)한 다음 [이 연산이 행렬에서의 합과 스칼라곱의 구조를 보존한다](#aa431d8ac)는 것을 증명했다. 이제 두 선형변환의 합성에 어떤 행렬의 연산이 대응되는지 연구해야 한다. 즉, 행렬곱에 대하여 정의할 차례인 것이다.

    그렇다면 행렬 곱은 어째서 이렇게 정의되었나? 행렬 곱 정의가 두 선형변환의 합성의 구조를 보존해야 하기 때문이다. 

    유한차원 벡터공간 $\mathbf{V} ,\mathbf{W} ,\mathbf{Z}$ 와 선형변환 $\mathbf{T} : \mathbf{V} \to \mathbf{W} , \mathbf{U} : \mathbf{W} \to \mathbf{Z}$ 를 생각하자. 이때 $\mathbf{V}, \mathbf{W}, \mathbf{Z}$ 의 순서기저를 각각 

    $$ \text{ordered basis of } \mathbf{V} : \alpha = \{v_1, \dots, v_n\} $$

    $$ \text{ordered basis of } \mathbf{W} : \beta = \{w_1, \dots, w_m\} $$

    $$ \text{ordered basis of } \mathbf{Z} : \gamma = \{z_1, \dots, z_p\} $$

    으로 정의하고 선형변환 $\mathbf{T} , \mathbf{U}$ 의 행렬표현을 

    $$ m \times n \text{ 행렬 } B = [\mathbf{T} ] ^{\beta }_{\alpha } $$

    $$ p \times m \text{ 행렬 } A = [\mathbf{U} ] ^{\gamma}_{\beta} $$
    
    라고 하자. 그러면 $\mathbf{U} \mathbf{T} : \mathbf{V} \to \mathbf{Z}$ 에 대하여

    $$ \boxed{ AB = [\mathbf{U} \mathbf{T} ] ^{\gamma}_{\alpha }} $$

    가 성립하도록 행렬곱 $AB$ 를 정의하면 된다. $j = 1, 2, \dots, n$ 에 대하여 다음이 성립한다. 

    $$ \begin{equation}\begin{split}   (\mathbf{U} \mathbf{T} ) (v_j) &= \mathbf{U} (\mathbf{T} (v_j)) = \mathbf{U} \bigg (\sum_{k=1}^{m}B _{kj} w_k\bigg ) = \sum_{k=1}^{m}B _{kj}\mathbf{U} (w_k)  \\ &= \sum_{k=1}^{m}B _{kj} \bigg (\sum_{i=1}^{p}A _{ik}z_i\bigg ) = \sum_{i=1}^{p} \bigg (\sum_{k=1}^{m}A _{ik}B _{kj}\bigg ) z_i \\ \end{split}\end{equation}\tag*{} $$

    그러므로 행렬곱 $AB$ 를 $p \times n$ 행렬 

    $$ (AB) _{ij} = \sum_{k=1}^{m}A _{ik} B _{kj} $$

    라고 정의할 수 있다.

- 행렬 $A, B$ 의 형상이 다음과 같이 맞아야 행렬곱 연산을 할 수 있다. 

    $$ (m \times n) \cdot (n \times p) = (m \times p) $$

    내부 차원이 맞아야 행렬 곱 $AB$ 가 정의되고, 외부 차원이 행렬 $AB$ 의 크기를 결정한다. 

    - 예시 

        다음과 같이 $(2 \times 3) \cdot (3 \times 1) = 2 \times 1$ 이다.

        $$ \begin{pmatrix} 1&2&1\\ 0&4&-1\\ \end{pmatrix} \cdot \begin{pmatrix} 4\\ 2\\ 5\\ \end{pmatrix} = \begin{pmatrix} 13\\ 3\\ \end{pmatrix} $$

- 함수의 합성에 교환법칙이 성립하지 않으므로 행렬곱에도 교환법칙이 성립하지 않는다.

    - 예시 

        다음은 두 행렬 $A,B$ 가 $AB \neq BA$ 을 만족한다.

        $$ \begin{pmatrix} 1&1\\ 0&0\\ \end{pmatrix} \begin{pmatrix} 0 & 1\\ 1 & 0\\ \end{pmatrix} = \begin{pmatrix} 1 & 1\\ 0 & 0\\ \end{pmatrix} , \quad  \begin{pmatrix} 0&1\\ 1&0\\ \end{pmatrix} \begin{pmatrix} 1&1\\ 0&0\\ \end{pmatrix} = \begin{pmatrix} 0&0\\ 1&1\\ \end{pmatrix} $$
    
!!! def ""

    $m \times n$ 행렬과 항등행렬 $I_m, I_n$ 에 대하여 다음이 성립한다. 

    $$ I_mA = AI_n = A $$

- 증명

!!! def ""

    $$ (AB) ^{t} = B ^{t} A ^{t} $$

- 증명 

    $$(AB) ^{t} _{ij} = (AB) _{ji} = \sum_{k=1}^{n}A _{jk}B _{ki}$$

    $$(B ^{t} A ^{t}) _{ij} =  \sum_{k=1}^{n}(B ^{t})_{ik}(A ^{t}) _{kj} = \sum_{k=1}^{n}B _{ki}A _{jk} $$

!!! def "정리 2.11"

    유한차원 벡터공간 $\mathbf{V} , \mathbf{W} , \mathbf{Z}$ 와 각각의 순서기저 $\alpha , \beta , \gamma$ 와 선형변환 $\mathbf{T} : \mathbf{V} \to \mathbf{W} , \mathbf{U} : \mathbf{W} \to \mathbf{Z}$ 에 대하여 다음이 성립한다. 

    $$ [\mathbf{U} \mathbf{T} ] ^{\gamma}_{\alpha } = [\mathbf{U} ] ^{\gamma}_{\beta} [\mathbf{T} ] ^{\beta }_{\alpha } $$

- 이 정리가 행렬 곱 연산이 두 선형변환의 합성의 구조를 보존한다는 것을 말해준다. 
- 증명 

    행렬곱의 정의에 의하여 이 정리가 성립함을 쉽게 알 수 있다.

- 예시 

    선형변환 $\mathbf{U}: \mathbf{P} _3(\R), \mathbf{T}:\mathbf{P} _2(\R) \to \mathbf{P} _3(\R)$ 를 

    $$ \mathbf{U} (f(x)) = f'(x), \quad \mathbf{T} (f(x)) = \int_{0}^{x}f(t)dt $$

    로 정의하면 $\mathbf{U} \mathbf{T} = \mathbf{I}$ 이다. $\alpha , \beta$ 를 $\mathbf{P} _3(\R), \mathbf{P} _2(\R)$ 의 표준순서기저라 하면 

    $$ [\mathbf{U} \mathbf{T} ] _{\beta } = [\mathbf{U} ] ^{\beta }_{\alpha }[\mathbf{T} ]^{\alpha } _{\beta } = \begin{pmatrix} 0&1&0&0\\ 0&0&2&0\\ 0&0&0&3\\ \end{pmatrix}\begin{pmatrix} 0&0&0\\ 1&0&0\\ 0&\dfrac{1}{2}&0\\ 0&0&\dfrac{1}{3}\\ \end{pmatrix} = \begin{pmatrix} 1&0&0\\ 0&1&0\\ 0&0&1\\ \end{pmatrix} = [\mathbf{I} ] _{\beta } $$

    이 성립한다.

!!! def "정리 2.11 따름정리"

    유한차원 벡터공간 $\mathbf{V}$ 와 순서기저 $\beta$ 와 선형연산자 $\mathbf{T} , \mathbf{U} \in \mathcal{L}(\mathbf{V} )$ 에 대하여 다음이 성립한다. 

    $$ [\mathbf{U} \mathbf{T} ] _{\beta } = [\mathbf{U} ] _{\beta }[\mathbf{T} ] _{\beta } $$

> p113. 정리 2.10, 정리 2.16 의 메타데이터

!!! def "정리 2.12"

    $A$ 가 $m \times n$ 행렬, $B$ 와 $C$ 가 $n \times p$ 행렬, $D$ 와 $E$ 가 $q \times m$ 행렬일 때, 다음이 성립한다.

    1. $A(B+C) = AB+AC, (D+E)A = DA+EA$

    2. 임의의 스칼라 $a$ 에 대하여 $a(AB) = (aA)B=A(aB)$

    3. $I_mA = A=AI_n$

- 1) 의 증명

    $$ \begin{equation}\begin{split}   
    [A(B+C)] _{ij} &= \sum_{k=1}^{n}A _{ik}(B+C) _{kj} = \sum_{k=1}^{n}A _{ik}(B _{kj} + C _{kj})  \\
    &= \sum_{k=1}^{n} (A _{ik}B _{kj} + A _{ik}C _{kj}) = \sum_{k=1}^{n} A _{ik} B _{kj} + \sum_{k=1}^{n} A _{ik} C _{kj} \\
    &= (AB) _{ij} + (AC) _{ij} = [AB +AC] _{ij}
    \end{split}\end{equation}\tag*{}
    $$

    $$ \iff A(B+C) = AB+AC $$

- 3) 의 증명 

    $\displaystyle (I_mA) _{ij} = \sum_{k=1}^{m}(I_m) _{ik}A _{kj} = \sum_{k=1}^{m}\delta _{ik}A _{kj} = A _{ij}$

!!! def "정리 2.12 따름정리"

    $m \times n$ 행렬 $A$ 와 $n \times p$ 행렬 $B_1, B_2, \dots, B_k$ 와 $q \times m$ 행렬 $C_1, C_2, \dots, C_k$ 와 스칼라 $a_1, a_2, \dots, a_k$ 에 대하여 다음이 성립한다. 

    $$ A \bigg (\sum_{i=1}^{k}a_iB_i\bigg ) = \sum_{i=1}^{k}a_iAB_i, \quad \bigg (\sum_{i=1}^{k}a_iC_i\bigg )A = \sum_{i=1}^{k}a_iC_iA $$

- 증명

!!! def ""

    $n \times n$ 행렬 $A$ 에 대하여 행렬의 지수를 다음과 같이 정의한다.

    $$ A ^{k} = \begin{cases} A ^{k-1}A & k \geq 2\\ A & k = 1\\ I_n & k = 0\\ \end{cases} $$

!!! def ""

    행렬곱에서 소거법칙이 성립하지 않는다.

- 증명

    $A = \begin{pmatrix} 0&0\\ 1&0\\ \end{pmatrix} \implies A \neq O \land A ^{2} = O$ 이다. 이때 소거법칙이 성립한다고 가정하면

    $$ A \cdot A = A ^{2} = O = A \cdot O \implies A = O $$

    이다. 이는 모순이다. ■ 

!!! def "정리 2.13"

    $m \times n$ 행렬 $A$ 와 $n \times p$ 행렬 $B$ 와 $j = 1, 2, \dots, p$ 에 대하여 $AB$ 의 $j$ 열을 $u_j$, $B$ 의 $j$ 열을 $v_j$ 이라 하면 다음이 성립한다. 

    1. $u_j = Av_j$

    2. $v_j = Be_j$ (단, $e_j$ 는 $\mathbf{F} ^{p}$ 의 $j$ 번째 표준벡터)

- 1) 의 증명

    $$ u_j = \begin{pmatrix} (AB) _{1j}\\ (AB) _{2j}\\ \vdots \\ (AB) _{mj}\\ \end{pmatrix} = \begin{pmatrix} \sum_{k=1}^{n}A _{1k}B _{kj}\\ \sum_{k=1}^{n}A _{2k}B _{kj}\\ \vdots\\ \sum_{k=1}^{n}A _{mk}B _{kj}\\ \end{pmatrix} = A \begin{pmatrix} B _{1j}\\ B _{2j}\\ \vdots \\ B _{nj}\\ \end{pmatrix} = A v_j \tag*{■} $$

- 2) 의 증명

    $$ Be_j = \begin{pmatrix} b_{11} & b_{12} & \dots & b_{1p}\\ b_{21} & b_{22} & \dots & b_{2p}\\ \vdots& \vdots& \ddots& \vdots \\ b_{n1} & b_{n2} & \dots & b_{np}\\ \end{pmatrix} \begin{pmatrix} 0\\ 0\\ \vdots \\ 1\\ \vdots \\ 0\\ \end{pmatrix} = \begin{pmatrix} b_{1j}\\ b_{2j}\\ \dots\\ b_{nj}\\ \end{pmatrix} \tag*{■} $$

!!! def "정리 2.14"

    유한차원 벡터공간 $\mathbf{V} , \mathbf{W}$ 과 각각의 순서기저 $\beta , \gamma$ 에 대한 선형변환 $\mathbf{T} : \mathbf{V} \to \mathbf{W}$ 과 $u \in \mathbf{V}$ 에 대하여 다음이 성립한다. 

    $$ [\mathbf{T} (u)] _{\gamma } = [\mathbf{T} ] ^{\gamma}_{\beta} [u] _{\beta } $$

- 이 정리는 선형변환에 어떤 벡터를 입력하여 행렬로 표현한 것과 선형변환과 벡터를 행렬로 표현한 후 행렬곱 한 것이 같음을 말해준다. 

- 증명

    $u \in \mathbf{V}$ 를 고정하고 다음과 같은 선형변환 $f: F \to \mathbf{V} , g: F \to \mathbf{W}$ 를 정의하자. 

    $$ \forall a \in F : f(a) = au, g(a) = a \mathbf{T} (u) $$

    $F$ 의 표준순서기저를 $\alpha = \{1\}$ 라고 하자. [선형변환의 조건]() 에 의하여 $g(a) = a \mathbf{T} (u) = \mathbf{T} (au) = \mathbf{T} f(a)$ 이므로 $g = \mathbf{T} f$ 이다. 

    행렬의 각 열을 벡터로 보고 [정리 2.11](#2fc8f26aa) 을 적용하면 다음이 성립한다. 

    $$ [\mathbf{T} (u)] _{\gamma } = [g(1)] _{\gamma } = [g] ^{\gamma}_{\alpha }  = [\mathbf{T} f] ^{\gamma}_{\alpha }  = [\mathbf{T} ] ^{\gamma}_{\beta} [f] ^{\beta }_{\alpha } = [\mathbf{T} ] ^{\gamma}_{\beta} [f(1)] _{\beta } = [\mathbf{T} ]^{\gamma}_{\beta} [u] _{\beta } \tag*{■} $$

## Left Multiplication Transformation

!!! def "좌측 곱 변환(left multiplication transformation)"

    체 $\mathbf{F}$ 에서 성분을 가져온 $m \times n$ 행렬 $A$ 에 대하여 선형변환 

    $$ \mathbf{L} _{A} : \mathbf{F} ^{n} \to \mathbf{F} ^{m}, x \mapsto Ax $$

    을 좌측 곱 변환이라 한다.

- $x$ 는 $\mathbf{F} ^{n}$ 의 열벡터이다. 

- 좌측 곱 변환은 선형변환의 성질로 행렬의 성질을 유추하거나, 행렬의 성질로 선형변환의 성질을 유추할 때 유용하게 사용되는 도구이다. 

- 예시 

    $A = \begin{pmatrix} 1&2&1\\ 0&1&2\\ \end{pmatrix}, x= \begin{pmatrix} 1\\ 3\\ -1\\ \end{pmatrix}$ 에 대하여 $\mathbf{L} _A(x) = Ax = \begin{pmatrix} 1&2&1\\ 0&1&2\\ \end{pmatrix}\begin{pmatrix} 1\\ 3\\ -1\\ \end{pmatrix} = \begin{pmatrix} 6\\ 1\\ \end{pmatrix}$ 이다. 

!!! def "정리 2.15"

    체 $\mathbf{F}$ 에서 성분을 가져온 $m \times n$ 행렬 $A$ 에 대하여 좌측 곱 변환 $\mathbf{L} _{A}: \mathbf{F} ^{n} \to  \mathbf{F} ^{m}$ 은 선형이다.

    또한 체 $\mathbf{F}$ 에서 성분을 가져온 $m \times n$ 행렬 $B$ 와 $\mathbf{F} ^{n}$ 의 표준순서기저 $\beta$, $\mathbf{F} ^{m}$ 의 표준순서기저 $\gamma$ 에 대하여 다음이 성립한다. 

    1. $[\mathbf{L} _A] ^{\gamma}_{\beta} = A$

    2. $\mathbf{L} _A = \mathbf{L} _B \iff A = B$

    3. $\mathbf{L} _{A+B} = \mathbf{L} _A + \mathbf{L} _B$

    4. $\forall a \in \mathbf{F} : \mathbf{L} _{aA} = a \mathbf{L} _A$

    5. $\mathbf{T} : \mathbf{F} ^{n} \to \mathbf{F} ^{m}$ 이 선형이면 $\mathbf{T} = \mathbf{L} _C$ 인 $m \times n$ 행렬 $C$ 가 유일하게 존재한다. 또한 $C = [\mathbf{T} ] ^{\gamma}_{\beta}$ 이다.

    6. $n \times p$ 행렬 $E$ 에 대하여 $\mathbf{L} _{AE} = \mathbf{L} _A \mathbf{L} _E$ 이다.

    7. $m = n \implies \mathbf{L} _{I_n} = \mathbf{I} _{\mathbf{F} ^{n}}$

- 이 정리는 $\mathbf{L} _A$ 가 선형이고 유용한 도구를 많이 제공한다는 것을 말해준다. 

- 2) 가 좌측곱변환을 행렬로 연결시켜주네. 이로써 선형변환에서 성립하는 모든 성질들이 행렬에서도 성립한다고 말할 수 있겠네. 

- 증명

    $\mathbf{L}_{A}$ 는 선형이다:

    [정리 2.12]() 에 의하여 $A(B+C) = AB+AC$ 이다. 이는 $\mathbf{L} _A(x + y) = A(x+y) = Ax + Ay = \mathbf{L} (x) + \mathbf{L} (y)$ 임을 뜻한다. 
    
    또한 [정리 2.12]() 에 의하여 스칼라 $a$ 에 대하여 $A(aB) = a(AB)$ 이다. 이는 $\mathbf{L} _A(cx) = A(cx) = c(Ax) = c\mathbf{L} (x)$ 임을 뜻한다. 그러므로 $\mathbf{L} _A$ 는 선형이다. ▲ 

    1:

    일단 $\beta = \{e_1, e_2, \dots, e_n\}$ 이고 $\gamma = \{e_1, e_2, \dots, e_m\}$ 이다. 

    $[\mathbf{L}_{A}] ^{\gamma}_{\beta}$ 의 $j$ 열은 $[\mathbf{L}_{A}(e_j)] _{\gamma} = [Ae_j] _{\gamma}$ 인데 [$Ae_j$ 는 $A$ 의 $j$ 열](#546d2897f)이다. 또 $[Ae_j] _{\gamma }$ 는 [표준순서기저로 $A$ 의 $j$ 열을 나타낸 행렬이므로 결국 다시 $A$ 의 $j$ 열이 된다](#d636bb40f). 이는 $[\mathbf{L}_{A}]^{\gamma}_{\beta}$ 의 모든 열이 $A$ 의 열임을 뜻한다. 그러므로 $[\mathbf{L}_{A}]^{\gamma}_{\beta} = A$ 이다. ▲ 

    2:

    이미 증명한 1) 에 의하여 

    $$ A = [\mathbf{L}_{A}] ^{\gamma}_{\beta} = [\mathbf{L}_{B}] ^{\gamma}_{\beta} = B $$

    이다. 그 역도 쉽게 증명가능하다. ▲ 

    3: 

    이미 증명한 1) 과 [정리 2.8 - 1](#aa431d8ac) 에 의하여 다음이 성립한다. 

    $$ [\mathbf{L}_{A+B}] ^{\gamma}_{\beta} = A + B = [\mathbf{L}_{A}] ^{\gamma}_{\beta} + [\mathbf{L}_{B}] ^{\gamma}_{\beta} = [\mathbf{L}_{A} + \mathbf{L}_{B}] ^{\gamma}_{\beta} \tag*{▲} $$

    4:

    $$ [\mathbf{L}_{aA}]^{\gamma}_{\beta} = aA = a[\mathbf{L}_{A}]^{\gamma}_{\beta} \tag*{▲} $$

    5: 

    $C = [\mathbf{T} ] ^{\gamma}_{\beta}$ 라고 하자. [정리 2.14](#93b3bc7a2) 에 의하여 $[\mathbf{T} (x)]^{\gamma}_{\beta} = [\mathbf{T}]^{\gamma}_{\beta} [x]_{\beta } = C[x]_{\beta}$ 이므로 
    
    $$\forall x \in \mathbf{F} ^{n} :  \mathbf{T} (x) = Cx = \mathbf{L}_{C}(x)$$ 
    
    이다. 이는 $\mathbf{T} = \mathbf{L}_{C}$ 을 의미한다. 이로써 $C$ 의 존재성이 증명되었다. $C$ 의 유일성은 2) 에서 곧바로 알 수 있다. ▲ 

    6:

    [$(AE)e_j$ 는 $AE$ 의 $j$ 열](#6be0b1ca1)이다. [정리 2.13 - 1](#546d2897f) 에 의하여 $AE$ 의 $j$ 열은 $A(Be_j)$ 이다. 그러므로 

    $$ \mathbf{L}_{AE}(e_j) = (AE)e_j = A(Ee_j) = \mathbf{L}_{A}(Ee_j) = \mathbf{L}_{A}(\mathbf{L}_{E}(e_j)) $$

    이다. [정리 2.6 따름정리](#52dd3d90f) 에 의하여 $\mathbf{L}_{AE} = \mathbf{L}_{A}\mathbf{L}_{E}$ 이다. ▲ 

    7: 

    먼저 $[\mathbf{L}_{I_n}] ^{\gamma}_{\beta} = I_n$ 이다. 
    
    $[\mathbf{I} _{\mathbf{F} ^{n}}] _{\beta }$ 의 $j$ 열은 $[\mathbf{I} _{\mathbf{F} ^{n}}(e_j)] _{\beta} = [e_j] _{\beta}$ 이다. 이는 $e_j$ 를 뜻한다. 그러므로 $[\mathbf{I} _{\mathbf{F} ^{n}}] _{\beta } = I_n$ 이다. ■ 

!!! def "정리 2.16"

    $A(BC)$ 가 정의된 행렬 $A, B, C$ 에 대하여 다음이 성립한다.
    
    1. $(AB)C$ 가 정의되어 있다.
    
    2. $A(BC) = (AB)C$ 가 성립한다.

- 2) 는 행렬곱 연산에서 결합법칙이 성립함을 말해준다. 

- 1) 의 증명 

- 2) 의 증명 

    [함수의 합성은 결합법칙을 만족한다.](../../Set/Set/#ede6df07e) 또한 [정리 2.15 - 6](#c3298a7b3) 에 의하여 다음이 성립한다. 

    $$ \mathbf{L}_{A(BC)} = \mathbf{L}_{A}\mathbf{L}_{BC} = \mathbf{L}_{A}(\mathbf{L}_{B}\mathbf{L}_{C}) = (\mathbf{L}_{A}\mathbf{L}_{B})\mathbf{L}_{C} = \mathbf{L}_{AC}\mathbf{L}_{C} = \mathbf{L}_{(AB)C} $$

    그러므로 [정리 2.15 - 2](#c3298a7b3) 에 의하여 

    $$ \therefore  A(BC) = (AB)C $$

    이다. ■ 

- 이 정리는 지금까지 했던 것처럼 행렬의 성분을 비교하는 방식으로도 증명 가능하다. 그러나 그렇게 번거로운 방법보다 지금까지 정립해온 정리를 사용하면 위와 같이 세련되게 증명할 수 있다. 

!!! def "정리 2.16 따름정리"

    행렬곱 연산에서 결합법칙이 성립한다.

- 증명

    $\because$ 정리 2.16 - 2 에 의하여 본 정리가 성립한다. 

> p118 결합행렬을 현실세상에 응용하기

# Invertibility

!!! def "역함수(inverse)"

    벡터공간 $\mathbf{V} ,\mathbf{W}$ 와 선형변환 $\mathbf{T} : \mathbf{V} \to \mathbf{W}$ 에 대하여 
    
    $$\mathbf{T} \mathbf{T^{-1}} = \mathbf{I} _{\mathbf{W} }, \mathbf{T^{-1}} \mathbf{T} = \mathbf{I} _{\mathbf{V} }$$
    
    를 만족하는 함수 $\mathbf{T^{-1}} : \mathbf{W} \to \mathbf{V}$ 를 $\mathbf{T}$ 의 역함수라고 한다. 

- 선형변환의 역함수 정의는 [일반적인 함수의 역함수 정의](../../Set/Set/#b64f666e2)와 같다.

- 역함수가 존재하는 선형변환을 가역(invertible)이라 한다.

!!! def ""

    선형변환의 역함수는 유일하다.

- 증명

    [함수의 역함수는 유일하다.](../../Set/Set/#41c513e50) 선형변환은 함수이다. ■ 

!!! def ""

    선형변환이 가역이기 위한 필요충분조건은 전단사라는 것이다. 

- 증명 

    [함수의 역함수가 존재하기 위한 필요충분조건은 전단사라는 것이다.](../../Set/Set/#4d4309496) 선형변환은 함수이다. ■ 

!!! def ""

    가역인 함수 $\mathbf{T} , \mathbf{U}$ 에 대하여 다음이 성립한다.

    1. $(\mathbf{T} \mathbf{U} ) ^{-1} = \mathbf{U} ^{-1} \mathbf{T} ^{-1}$

    2. $(\mathbf{T} ^{-1}) ^{-1} = \mathbf{T}$ 이다. 특히 $\mathbf{T} ^{-1}$ 는 가역이다.

    3. $\dim (\mathbf{V} ) = \dim (\mathbf{W} )$ 인 벡터공간 $\mathbf{V} , \mathbf{W}$ 에 대하여 선형변환 $\mathbf{T} : \mathbf{V} \to \mathbf{W}$ 가 가역이기 위한 필요충분조건은 $\text{rank} (\mathbf{T} ) = \dim (\mathbf{V} )$ 이다.

- 3) 의 증명 

    [정리 2.5](#dfd4ff297) 에 의하여 $\mathbf{T}$ 가 전단사라는 것과 $\text{rank} (\mathbf{T} ) = \dim (\mathbf{V} )$ 은 동치이다. 선형변환이 가역이기 위한 필요충분조건은 전단사라는 것이다. ■ 

- 예시 

    선형변환 $\mathbf{T} : \mathbf{P}_{1}(\R) \to \R ^{2}, a+bx \mapsto (a, a+b)$ 의 역함수는 

    $$ \mathbf{T} ^{-1}:\R ^{2} \to \mathbf{P}_{1}(\R), (c, d) \mapsto c + (d-c)x $$

    이다.

!!! def "정리 2.17"

    선형변환의 역함수는 선형이다.

- 증명 

    벡터공간 $\mathbf{V} , \mathbf{W}$ 와 가역인 선형변환 $\mathbf{T} : \mathbf{V} \to \mathbf{W}$ 에 대한 역함수 $\mathbf{T} ^{-1}: \mathbf{W} \to \mathbf{V}$ 가 선형임을 보이자. 

    $\mathbf{T}$ 가 전단사이므로 $y_1, y_2 \in \mathbf{W}$ 에 대한 $\mathbf{T} (x_1) = y_1, \mathbf{T} (x_2) = y_2$ 를 만족하는 벡터 $x_1, x_2 \in \mathbf{V}$ 가 유일하게 존재한다. 그러므로 스칼라 $c \in \mathbf{F}$ 에 대하여 

    $$ \begin{equation}\begin{split} \mathbf{T} ^{-1}(cy_1 + y_2) &= \mathbf{T} ^{-1}[c \mathbf{T} (x_1) + \mathbf{T} (x_2)] = \mathbf{T} ^{-1}(\mathbf{T} (cx_1 + x_2))\\ &= cx_1 + x_2 = c \mathbf{T} ^{-1} (y_1) + \mathbf{T} ^{-1}(y_2) \end{split}\end{equation} \tag*{} $$

    이다. ■ 

!!! def "정리 2.17 따름정리"

    선형변환 $\mathbf{T} : \mathbf{V} \to \mathbf{W}$ 가 가역이면 다음이 성립한다. 

    - $\mathbf{V}$ 가 유한차원인 것과 $\mathbf{W}$ 가 유한차원인 것은 동치이다. 

    - $\mathbf{V} , \mathbf{W}$ 가 유한차원이면 $\dim (\mathbf{V} ) = \dim (\mathbf{W} )$ 이다.

- 증명 

    $\mathbf{V}$ 가 유한차원이라고 하고 기저를 $\beta = \{x_1, x_2, \dots, x_n\}$ 이라고 하자. $\mathbf{T}$ 가 전단사이므로 공역과 치역이 같다. 그러면 [정리 2.2](#f380ab529) 에 의하여 $\text{span} (\mathbf{T} (\beta )) = \mathbf{R} (\mathbf{T}) = \mathbf{W}$ 이다. 유한집합이 $\mathbf{W}$ 를 생성하므로 [정리 1.9](../VectorSpace/#2d3716e93) 에 의하여 $\mathbf{W}$ 는 유한차원이다. ▲ 

    역으로 $\mathbf{W}$ 가 유한차원임을 가정하면 $\mathbf{T} ^{-1}$ 를 사용하여 비슷한 논법으로 $\mathbf{V}$ 가 유한차원임을 증명할 수 있다. ▲ 

    이제 $\mathbf{V} , \mathbf{W}$ 가 유한차원이라는 사실을 사용할 수 있다. $\mathbf{T}$ 가 단사이므로 [정리 2.4](#7d40e8276) 에 의하여 

    $$ \mathbf{N} (\mathbf{T}) = \{0\} \implies \text{nullity} (\mathbf{T}) = 0 $$

    이다. 또한 $\mathbf{T}$ 가 전사이므로 공역과 치역이 같다. 그러므로 

    $$ \text{rank} (\mathbf{T} ) = \dim (\mathbf{W} ) $$

    이다. 그러면 [차원정리](#6187a9f9c) 에 의하여 $\dim (\mathbf{W}) = \dim (\mathbf{V} )$ 임을 알 수 있다. ■ 

!!! def ""

    벡터공간 $\mathbf{V} , \mathbf{W}$ 와 선형변환 $\mathbf{T} : \mathbf{V} \to \mathbf{W}$ 에 대하여 $\dim (\mathbf{V} ) = \dim (\mathbf{W} )$ 이면 다음이 동치이다.

    - $\mathbf{T}$ 가 단사이다.

    - $\mathbf{T}$ 가 전사이다.

    - $\mathbf{T}$ 가 전단사이다.

    - $\mathbf{T}$ 가 가역이다.

- 증명

    [정리 2.5](#dfd4ff297) 에 의하면 같은 차원을 갖는 두 유한차원 벡터공간 사이에 정의된 선형변환에 대하여 단사, 전사가 동치이다. 이로써 전단사도 동치이며 가역도 동치이다.

## Invertible matrix

!!! def "가역행렬(invertible matrix)"

    $n \times n$ 행렬 $A$ 에 대하여 $AB=BA=I$ 인 $n \times n$ 행렬 $B$ 가 존재할 때 $A$ 를 가역이라고 한다.

- 이는 역함수의 정의와 비슷하다. 선형변환을 행렬과 대응시키고 그 연산도 보존해보았듯이 선형변환과 행렬의 역연산도 연결시켜볼 것이다.

!!! def ""

    역행렬(inverse matrix) : $A$ 가 가역일때 $AB = BA = I$ 를 만족하는 행렬 $B$ 이다.

- 예시 

    $\begin{pmatrix} 5&7\\ 2&3\\ \end{pmatrix}$ 의 역행렬은 $\begin{pmatrix} 3&-7\\ -2&5\\ \end{pmatrix}$ 이다.

!!! def ""

    역행렬은 유일하다.

- 증명 

    역행렬을 선형변환의 역함수와 연결시킨다면 [역함수가 유일하다](../../Set/Set/#41c513e50) 는 정리로도 증명가능하다. 그러나 일단은 $AC=CA = I$ 를 만족하는 또 다른 행렬 $C$ 가 존재한다면 

    $$ C = CI = C(AB) = (CA)B = IB = B $$

    로써 증명을 마친다. ■ 

## Properties of Invertibility

!!! def "정리 2.18"

    유한차원 벡터공간 $\mathbf{V} , \mathbf{W}$ 와 각각의 순서기저 $\beta , \gamma$, 선형변환 $\mathbf{T} : \mathbf{V} \to \mathbf{W}$ 에 대하여 다음이 성립한다. 

    - $\mathbf{T}$ 가 가역인 것과 $[\mathbf{T} ] ^{\gamma}_{\beta}$ 가 가역인 것은 동치이다. 

    - $[\mathbf{T} ^{-1}] ^{\beta }_{\gamma } = ([\mathbf{T} ] ^{\gamma}_{\beta} ) ^{-1}$

- 이 정리는 선형변환의 역함수와 행렬의 역행렬을 연결시켜준다.

- 증명

    $\mathbf{T}$ 가 가역이면 [정리 2.17 따름정리](#87bea1c24)로부터 $\dim (\mathbf{V} ) = \dim (\mathbf{W} )$ 이다. $n = \dim (\mathbf{V} )$ 라고 하면 $[\mathbf{T} ] ^{\gamma}_{\beta}$ 는 $n \times n$ 행렬이다. 또 역함수 $\mathbf{T} ^{-1}$ 에 대하여 $\mathbf{T} ^{-1}\mathbf{T}  = \mathbf{I} _{\mathbf{V} }$ 이다. 이러한 사실들과 [항등변환의 행렬표현은 항등행렬이다](#2bb4853fd) 와 [정리 2.11](#2fc8f26aa) 에 의하여 

    $$ I_n = [\mathbf{I} _{\mathbf{V} }] _{\beta } = [\mathbf{T} ^{-1}\mathbf{T} ] _{\beta } = [\mathbf{T} ^{-1}] ^{\beta }_{\gamma } [\mathbf{T} ]^{\gamma}_{\beta} $$

    이다. 같은방식으로 

    $$ I_n = [\mathbf{T} ]^{\gamma}_{\beta}[\mathbf{T} ^{-1}] ^{\beta }_{\gamma }  $$

    을 얻을 수 있다. 그러므로 $\mathbf{T}$ 가 가역임을 가정했을 때 $[\mathbf{T}]^{\gamma}_{\beta}$ 는 가역이고, $([\mathbf{T} ]^{\gamma}_{\beta} )^{-1} = [\mathbf{T} ^{-1}] ^{\beta }_{\gamma}$ 이다. ▲ 

    $A = [\mathbf{T} ] ^{\gamma}_{\beta}$ 가 가역이면 $AB = BA = I_n$ 을 만족하는 $n \times n$ 행렬 $B$ 가 존재한다.  우선 $\gamma = \{w_1, w_2, \dots, w_n\}, \beta = \{v_1, v_2, \dots, v_n\}$ 이라고 하자. 그러면 [정리 2.6](#f2d6e699f) 에 의하여 

    $$ j \in \{1,2,\dots,n\} : \mathbf{U} (w_j) = \sum_{i=1}^{n}B _{ij}v_i $$

    을 만족하는 선형변환 $\mathbf{U} : \mathcal{L}(\mathbf{W} ,\mathbf{V} )$ 이 유일하게 존재한다. 이는 $[\mathbf{U} ] ^{\beta }_{\gamma } = B$ 임을 말해준다. 그러면 [정리 2.11](#2fc8f26aa) 에 의하여 

    $$ [\mathbf{U} \mathbf{T} ] _{\gamma } = [\mathbf{U} ]^{\beta }_{\gamma } [\mathbf{T} ]^{\gamma}_{\beta} = BA = I_n = [\mathbf{I} _{\mathbf{V} }]_{\beta } $$

    이다. 따라서 $\mathbf{U} \mathbf{T} = \mathbf{I} _{\mathbf{V} }$ 이다. 같은 방식으로 $\mathbf{T} \mathbf{U} = \mathbf{I} _{\mathbf{W} }$ 를 보일 수 있다. 그러므로 $[\mathbf{T} ] ^{\gamma}_{\beta}$ 가 가역임을 가정했을 때 $\mathbf{T}$ 도 가역이다. ■ 

!!! def "정리 2.18 따름정리 1"

    유한차원 벡터공간 $\mathbf{V}$ 의 순서기저 $\beta$ 와 선형변환 $\mathbf{T} : \mathbf{V} \to \mathbf{V}$ 에 대하여 다음이 성립한다. 

    - $\mathbf{T}$ 가 가역인 것과 $[\mathbf{T} ]_{\beta}$ 가 가역인 것은 동치이다. 

    - $[\mathbf{T} ^{-1}] _{\beta } = ([\mathbf{T} ] _{\beta} ) ^{-1}$

- 증명

!!! def "정리 2.18 따름정리 2"

    $n \times n$ 행렬 $A$ 에 대하여 다음이 성립한다.

    - $A$ 가 가역인 것과 $\mathbf{L}_{A}$ 가 가역인 것은 동치이다.

    - $(\mathbf{L}_{A}) ^{-1} = \mathbf{L}_{A ^{-1}}$

- 증명

!!! def "문제 2.4-4"

    $A, B$ 가 $n \times n$ 가역행렬이면 다음이 성립한다.
    
    1. $AB$ 가 가역이다.

    2. $(AB) ^{-1} = B ^{-1}A ^{-1}$

- 증명

    $A, B$ 가 가역이므로 $A A ^{-1} = A ^{-1} A = I_n$, $B B ^{-1} = B ^{-1} B = I_n$ 인 $A ^{-1}, B ^{-1}$ 가 존재한다. [정리 2.16 따름정리](#7cbb5cb1a) 에 의하여 행렬의 결합법칙이 성립하므로 다음이 성립한다.

    $$ (AB) B ^{-1}A ^{-1} = AI_nA ^{-1} = I_n $$

    $$  B ^{-1}A ^{-1} (AB) = BI_nB ^{-1} = I_n $$

    그러므로 $AB$ 는 가역이고, $(AB) ^{-1} = B ^{-1} A ^{-1}$ 이다. ■ 

!!! def "문제 2.4-5"

    가역행렬 $A$ 에 대하여 $A ^{t}$ 가 가역이고 $(A ^{t}) ^{-1} = (A ^{-1}) ^{t}$ 이다.

- 증명

    $A A ^{-1} = A ^{-1}A = I$ 인 $A ^{-1}$ 가 존재한다. [$(AB) ^{t} = B ^{t} A ^{t}$](#3fe7e9e98) 이므로 다음이 성립한다.

    $$(AA ^{-1}) ^{t} = (A ^{-1}) ^{t} A ^{t} = I$$

    $$(A ^{-1} A ) ^{t} = A ^{t} (A ^{-1}) ^{t} = I$$

    따라서 $(A ^{t}) ^{-1} = (A ^{-1}) ^{t}$ 이다.

!!! def "문제 2.4-9"

    $n \times n$ 행렬 $A, B$ 에 대하여 $AB$ 가 가역이면 $A, B$ 모두 가역이다.

- 증명

    [정리 2.18 따름정리 2](#80bc2f76a) 에 의하여 $AB$ 가 가역이면 $\mathbf{L}_{AB}$ 도 가역이다. [정리 2.15 - 1](#c3298a7b3) 에 의하여 $\mathbf{L}_{AB}$ 는 $\mathbf{F} ^{n} \to \mathbf{F} ^{n}$ 위에서 정의된 선형변환이다. [정리 2.15 - 6](#c3298a7b3) 에 의하여 $\mathbf{L} _{AB} = \mathbf{L}_{A}\mathbf{L}_{B}$ 이다. 

    [$\mathbf{L}_{A}\mathbf{L}_{B}$ 가 전단사이므로 $\mathbf{L}_{B}$ 가 단사이고, $\mathbf{L}_{A}$ 는 전사이다](#de2683c1b). 그런데 [$\dim (\mathbf{F} ^{n}) = \dim (\mathbf{F} ^{n})$ 이므로 $\mathbf{L}_{A}$ 와 $\mathbf{L}_{B}$ 는 가역이다](#08a4e4fdc). 그러면 다시 [정리 2.18 따름정리 2](#80bc2f76a) 에 의하여 $A$ 와 $B$ 도 가역이다. ■ 

!!! def "문제 2.4-10"

    $AB = I_n$ 인 $n \times n$ 행렬 $A, B$ 에 대하여 다음이 성립한다. 

    1. $A, B$ 는 가역이다. 

    2. $A = B ^{-1}$

- 증명

    1:

    [정리 2.15 - 1](#c3298a7b3) 에 의하여 $AB = I_n$ 은 $\mathbf{L}_{AB} = \mathbf{L}_{I_n}$ 이다. 이는 [정리 2.15 - 6, 7](#c3298a7b3) 에 의하여 $\mathbf{L}_{A}\mathbf{L}_{B} = \mathbf{I} _{\mathbf{F} ^{n}}$ 가 된다. 그러므로 [$\mathbf{L}_{A}$ 는 전사](../../Set/Set/#5869db153)이고, [$\mathbf{L}_{B}$ 는 단사](../../Set/Set/#d9b0737d6)이다. 그런데 [$\dim (\mathbf{F} ^{n}) = \dim (\mathbf{F} ^{n})$ 이므로 $\mathbf{L}_{A}$ 와 $\mathbf{L}_{B}$ 는 가역이다](#08a4e4fdc). 그러면 [정리 2.18 따름정리 2](#80bc2f76a) 에 의하여 $A$ 와 $B$ 도 가역이다. ■ 

    2:

    $A$ 가 가역이므로 $A ^{-1}A = I_n$ 인 $A ^{-1}$ 가 존재한다. 따라서 

    $$ AB = I_n \iff A ^{-1}AB = A ^{-1} \iff B = A ^{-1} $$

    이다.

# Isomorphism

!!! def "동형(isomorphic)"

    벡터공간 $\mathbf{V} , \mathbf{W}$ 사이에 가역인 선형변환 $\mathbf{T} : \mathbf{V} \to \mathbf{W}$ 가 존재하면 $\mathbf{V}$ 와 $\mathbf{W}$ 는 동형이다.

- 예시 

    $\mathbf{M}_{2 \times 2}(\mathbf{F} )$ 의 원소 $\begin{pmatrix} a&b\\ c&d\\ \end{pmatrix}$ 를 $\mathbf{F} ^{4}$ 의 원소 $(a,b,c,d)$ 에 대응시키면 벡터 합과 스칼라 곱이 비슷하게 작동한다. 이는 두 벡터공간이 구조적으로 동형임을 뜻한다.

!!! def "동형사상(isomorphism)"

    벡터공간 $\mathbf{V} , \mathbf{W}$ 사이에 가역인 선형변환 $\mathbf{T} : \mathbf{V} \to \mathbf{W}$ 이다.

- 동형사상이 정의된 두 대수구조는 본질적으로 서로 같다.

- 일반적으로 동형사상은 전단사인 준동형사상으로 설명된다. 본 정의에서는 전단사라는 조건이 가역으로, 준동형사상이라는 조건이 선형변환으로 설명된 것뿐이다.

- 예시 

    $\mathbf{M}_{2 \times 2}(\mathbf{F} )$ 와 $\mathbf{F} ^{4}$ 사이에 동형사상이 존재하므로 이 두 벡터공간은 동형이다. 즉 말 그대로 생긴 구조가 동일하다.

!!! def ""

    동형은 동치관계이다.

- ^^**앞으로 두 벡터공간이 동형이라는 것을 동치관계 $\cong$ 으로 표기한다.**^^

- 증명

    $\mathbf{F}$-벡터공간을 원소로 가지는 집합족 $\mathcal{V}$ 의 임의의 두 원소 $\mathbf{V}, \mathbf{W}$ 가 동형이라는 것을 관계 $\mathbf{V} \sim \mathbf{W}$ 로 표기하자. $\sim$ 이 동치관계임을 보여야 한다. 

    $\mathbf{I} _{\mathbf{V} }(x) = x$ 은 $\mathbf{V} \to \mathbf{V}$ 에서 정의된 가역인 선형변환이다. 그러므로 $\mathbf{V} \sim \mathbf{V}$ 이다. ▲ 

    $\mathbf{V} , \mathbf{W} \in \mathcal{V}$ 에 대하여 $\mathbf{V} \to \mathbf{W}$ 에 가역인 선형변환 $\mathbf{T}: \mathbf{V} \to \mathbf{W}$ 가 정의되었다고 하자. 그러면 선형역변환 $\mathbf{T} ^{-1} : \mathbf{W} \to \mathbf{V}$ 이 존재한다. $\mathbf{T} ^{-1}$ 는 $\mathbf{W} \to \mathbf{V}$ 에서 정의된 가역인 선형변환이다. 그러므로 $\mathbf{V} \sim \mathbf{W} \implies \mathbf{W} \sim \mathbf{V}$ 이다. ▲ 

    (transitivity 는 전단사 합성함수의 성질로 쉽게 증명할 수 있을 듯.)

!!! def "정리 2.19"

    같은 체 위에서 정의된 유한차원 벡터공간 $\mathbf{V} , \mathbf{W}$ 에 대하여 다음이 성립한다.
    
    $$\mathbf{V} \cong \mathbf{W} \iff \dim (\mathbf{V} ) = \dim (\mathbf{W} ) $$

- 증명

    $\mathbf{V} \cong \mathbf{W}$ 를 가정하면 [정리 2.17 따름정리](#87bea1c24) 에 의하여 $\dim (\mathbf{V} ) = \dim (\mathbf{W} )$ 이다. ▲ 

    $\dim (\mathbf{V} ) = \dim (\mathbf{W} )$ 를 가정하자. 그리고 $\mathbf{V}, \mathbf{W}$ 의 각각의 기저를 $\beta = \{v_1, v_2, \dots, v_n \}, \gamma = \{w_1, w_2, \dots, w_n \}$ 라고 하자. [정리 2.6](#f2d6e699f) 에 의하여 $\mathbf{T} (v_i) = w_i$ 인 선형변환이 유일하게 존재한다. [정리 2.2](#f380ab529) 에 의하면 

    $$ \mathbf{R} (\mathbf{T}) = \text{span} (\mathbf{T} (\beta ))  = \text{span} (\gamma ) = \mathbf{W} $$

    이므로 $\mathbf{T}$ 는 전사이다. 그러면 [정리 2.5](#dfd4ff297) 에 의하여 $\mathbf{T}$ 는 단사이다. 그러므로 $\mathbf{T}$ 는 동형사상이고 결국 $\mathbf{V} \cong \mathbf{W}$ 이다. ■ 

!!! def ""

    두 벡터공간 $\mathbf{V} , \mathbf{W}$ 에 대하여 $\mathbf{V} \cong \mathbf{W}$ 이면 둘 다 유한차원이거나 둘 다 무한차원이다.

- 증명 

    [정리 2.17 따름정리](#87bea1c24) 에 의하여 증명이 끝난다. ■ 

!!! def ""

    $\mathbf{F}$-벡터공간 $\mathbf{V}$ 와 $\mathbf{F} ^{n}$ 에 대하여 다음이 성립한다.

    $$ \mathbf{V} \cong \mathbf{F} ^{n} \iff \dim (\mathbf{V} ) = n $$

- 증명 

    [정리 2.17 따름정리](#87bea1c24) 에 의하여 증명이 끝난다. ■ 

## Linear Map and Matrix are essentially the same

!!! def "정리 2.20"

    차원이 각각 $n, m$ 이고 순서기저가 각각 $\beta , \gamma$ 인 $\mathbf{F}$-벡터공간 $\mathbf{V}, \mathbf{W}$ 에 대하여 다음과 같이 정의된 함수는 동형사상이다.
    
    $$\Phi ^{\gamma}_{\beta} : \mathcal{L}(\mathbf{V} , \mathbf{W} ) \to \mathbf{M}_{m \times n}(\mathbf{F} ), \mathbf{T} \mapsto [\mathbf{T} ]^{\gamma}_{\beta}  $$

- 이 정리는 모든 선형변환이 유일한 행렬로 표현가능하고, 행렬 또한 유일한 선형변환으로 표현가능하다는 것을 말해준다. 

    쉽게말해, 이 정리는 선형변환과 행렬은 본질적으로 같다는 것을 말해준다.

- 증명

    [정리 2.8](#aa431d8ac) 에 의하여 $\Phi ^{\gamma}_{\beta}$ 가 선형임은 쉽게 알 수 있다. ▲ 

    이제 $\Phi ^{\gamma}_{\beta}$ 가 전단사임을 보이자. 임의의 $m \times n$ 행렬마다 선형변환 $\mathbf{T} : \mathbf{V} \to \mathbf{W}$ 가 유일하게 존재함을 보이면 된다. 

    $\beta = \{v_1, v_2, \dots, v_n \}, \gamma = \{w_1, w_2, \dots, w_n \}$ 에 대하여 [정리 2.6](#f2d6e699f) 에 의하여 다음 선형변환 $\mathbf{T} : \mathbf{V} \to \mathbf{W}$ 이 유일하게 존재한다.

    $$ j \in \{1,2,\dots,n\} : \mathbf{T} (v_j) = \sum_{i=1}^{m}A _{ij} w_j $$

    그러면 [선형변환의 행렬표현](#c16bc5e5b) 에 의하여 $A = [\mathbf{T}] ^{\gamma}_{\beta} = \Phi ^{\gamma}_{\beta} (\mathbf{T} )$ 이다. 그러므로 $\Phi ^{\gamma}_{\beta}$ 은 전단사이고, 결국 동형사상이다. ■ 

!!! def "정리 2.19 따름정리"

    차원이 각각 $n, m$ 인 $\mathbf{F}$-벡터공간 $\mathbf{V}, \mathbf{W}$ 에 대하여 다음이 성립한다.

    $$ \mathcal{L}(\mathbf{V} , \mathbf{W} ) \cong \mathbf{M}_{m \times n}(\mathbf{F} ) $$
    
- 증명

    정리 2.20 에 의하여 주어진 두 벡터공간 사이에 동형사상이 존재한다. ■ 

!!! def "정리 2.20 따름정리"

    유한차원 벡터공간 $\mathbf{V} , \mathbf{W}$ 에 대하여 $\dim (\mathcal{L}(\mathbf{V} , \mathbf{W} )) = \dim (\mathbf{V})\dim (\mathbf{V})$ 이다.

- 이 정리는 차원이 각각 $n,m$ 인 벡터공간 $\mathbf{V} , \mathbf{W}$ 에 대하여 $\dim (\mathcal{L}(\mathbf{V} , \mathbf{W} )) = nm$ 임을 말해준다.

- 증명 

    $\mathcal{L}(\mathbf{V} , \mathbf{W} ) \cong \mathbf{M}_{m \times n}(\mathbf{F} )$ 이고 $\dim (\mathbf{M}_{m \times n}(\mathbf{F} )) = mn$ 이다. 그러면 정리 2.19 에 의하여 증명이 끝난다. ■ 

## Standard Representation

!!! def "표준표현(standard representation)"

    체 $\mathbf{F}$ 위의 $n$차원 벡터공간 $\mathbf{V}$ 의 순서기저를 $\beta$ 라고 하자. $\beta$ 에 대한 $\mathbf{V}$ 의 표준표현은 다음과 같은 함수이다.

    $$ \phi _{\beta }: \mathbf{V} \to \mathbf{F} ^{n}, x \mapsto [x] _{\beta } $$

- 이는 추상적인 벡터공간에 정의된 선형변환과 $\mathbf{F} ^{n}\to \mathbf{F} ^{m}$ 에서 정의된 선형변환의 관계를 보여준다.

- 예시 

    $\R ^{2}$ 의 두 순서기저 $\beta = \{e_1, e_2\} = \{(1, 0), (0, 1)\}, \gamma = \{(1, 2), (3, 4)\}$ 와 $x = (1, -2) \in \R ^{2}$ 에 대하여 

    $$ \phi _{\beta }(x) = [x] _{\beta } = \begin{pmatrix} 1\\ -2\\ \end{pmatrix}, \phi _{\beta }(x) = [x] _{\gamma  } = \begin{pmatrix} -5\\ 2\\ \end{pmatrix} $$

    이다.

!!! def ""

    유한차원 벡터공간 $\mathbf{V}$ 의 순서기저 $\beta$ 에 대하여 $\phi _{\beta }$ 은 선형이다.

- 증명

    [선형변환의 성질](#841cc7807) 에 의하여 $\phi _{\beta }(cx + y) = c \phi _{\beta }(x) + \phi _{\beta }(y)$ 를 증명하면 된다. 이는 $[cx + y] _{\beta } = c[x] _{\beta } + [y]_{\beta }$ 를 증명하는 것이다.

    $x, y \in \mathbf{V}, c \in \mathbf{F}$ 에 대하여 $\beta = \{v_1, v_2, \dots, v_n \}$ 일 때 $x = a_1v_1 + a_2v_2 + \dots + a_nv_n, y = b_1v_1 + b_2v_2 + \dots + b_nv_n$ 이면 다음이 성립한다.

    $$ [x] _{\beta } = \begin{pmatrix} a_{1}\\ a_{2}\\ \vdots\\ a_{n}\\ \end{pmatrix}, [y] _{\beta } = \begin{pmatrix} b_{1}\\ b_{2}\\ \vdots\\ b_{n}\\ \end{pmatrix} \implies c[x] _{\beta } + [y] _{\beta } = \begin{pmatrix} ca_{1} + b_1\\ ca_{2} + b_2\\ \vdots\\ ca_{n} + b_n\\ \end{pmatrix}$$

    $$ \phi _{\beta }(cx + y) = [cx + y] _{\beta } = [(ca_1+b_1)v_1 + (ca_2+b_2)v_2 + \dots + (ca_n+b_n)v_n] _{\beta } = \begin{pmatrix} ca_1 + b_1\\ ca_2 + b_2\\ \vdots \\ ca_n + b_n\\ \end{pmatrix}$$

    $$ \therefore [cx + y] _{\beta } = c[x] _{\beta } + [y]_{\beta } \tag*{■} $$

!!! def "정리 2.21"

    유한차원 벡터공간 $\mathbf{V}$ 의 순서기저 $\beta$ 에 대하여 $\phi _{\beta }$ 는 동형사상이다.

- 증명

    $\beta = \{v_1, v_2, \dots, v_n \}$ 라고 하자.

    $[x] _{\beta } \in \mathbf{F} ^{n}$ 에 대하여 $x$ 가 유일하게 존재한다는 것을 보여야 한다. $[x] _{\beta } = \begin{pmatrix} a_{1}\\ a_{2}\\ \vdots\\ a_{n}\\ \end{pmatrix}$ 라고 하면 [좌표벡터의 정의](#be888949c) 에 의하여 $x = \sum_{i=1}^{n}a_iv_i$ 인 $x \in \mathbf{V}$ 가 존재한다.

    벡터 $x$ 의 $\beta$ 일차결합 표현은 [정리 1.8](../VectorSpace/#8a514fc5c) 에 의하여 유일하다. ■ 

!!! def ""

    $n$차원 벡터공간은 $\mathbf{F} ^{n}$ 과 동형이다.

- 증명

    정리 2.19 따름정리와 정리 2.21 에 의하여 증명이 끝난다. ■ 

## Relation between Linear Map and Matrix

!!! def "그림 2.2"

    차원이 각각 $n, m$ 이고 순서기저가 각각 $\beta, \gamma$ 인 벡터공간 $\mathbf{V} , \mathbf{W}$ 와 선형변환 $\mathbf{T} : \mathbf{V} \to \mathbf{W}$ 와 행렬 $A = [\mathbf{T} ] ^{\gamma}_{\beta}$ 에 대하여 다음이 성립한다. 즉, $\mathbf{L}_{A} \circ \phi _{\beta } = \phi _{\gamma } \circ \mathbf{T}$ 이다.

    $$ \begin{CD} \mathbf{V} @> \mathbf{T}  >> \mathbf{W}  \\ @V \phi _{\beta } VV @VV \phi _{\gamma } V \\ \mathbf{F} ^{n} @> \mathbf{L}_{A} >> \mathbf{F} ^{m} \end{CD} $$

- 동형사상 $\phi _{\beta }$ 를 통해 $\mathbf{V}$ 와 $\mathbf{F} ^{n}$ 을 동일시할 수 있고 동형사상 $\phi _{\gamma  }$ 를 통해 $\mathbf{W}$ 와 $\mathbf{F} ^{m}$ 을 동일시할 수 있다.

    물론 $\mathbf{T}$ 가 동형사상이면 $\mathbf{V}$ 와 $\mathbf{W}$ 을 동일시할 수 있고 $\mathbf{L}_A$ 가 동형사상이면 $\mathbf{F} ^{n}$ 와 $\mathbf{F} ^{m}$ 을 동일시할 수 있다.

- 이 그림은 다루기 힘든 추상적인 두 벡터공간 사이에 정의된 연산을 우리에게 친숙한 $\mathbf{F} ^{n}$ 와 $\mathbf{F} ^{m}$ 사이에 정의된 연산으로 나타낼 수 있다는 것을 말해준다. 

- 예시 

    선형변환 $\mathbf{T} :\mathbf{P}_{3}(\R) \to \mathbf{P}_{2}(\R), f(x) \mapsto f'(x)$ 에서 $\beta , \gamma$ 를 각각 $\mathbf{P}_{3}(\R), \mathbf{P}_{2}(\R)$ 의 순서기저라 하자.

    또한 $\phi _{\beta }: \mathbf{P}_{3}(\R) \to  \R ^{4}, \phi _{\gamma } : \mathbf{P}_{2}(\R) \to \R ^{3}$ 을 각각의 기저에 대한 표준표현이라고 하자.

    $\mathbf{T}$ 의 행렬표현은 다음과 같다. 

    $$ [\mathbf{T} ] ^{\gamma}_{\beta} = A = \begin{pmatrix} 0&1&0&0\\ 0&0&2&0\\ 0&0&0&3\\ \end{pmatrix} $$

    이제 위 그림이 말하는 $\mathbf{L}_{A} \circ \phi _{\beta } = \phi _{\gamma } \circ \mathbf{T}$ 가 정말 성립하는지 다항식 $p(x) = 2 + x - 3x ^{2} + 5x ^{3}$ 에 대하여 확인해보자. 

    $$ \mathbf{L}_{A} (\phi _{\beta }(p(x))) = \begin{pmatrix} 0&1&0&0\\ 0&0&2&0\\ 0&0&0&3\\ \end{pmatrix} \begin{pmatrix} 2\\ 1\\ -3\\ 5\\ \end{pmatrix}=\begin{pmatrix} 1\\ -6\\ 15\\ \end{pmatrix} $$

    $$ \phi _{\gamma }(T(p(x))) = \phi _{\gamma }(p'(x))= \phi _{\gamma }(1-6x+15x ^{2}) = \begin{pmatrix} 1\\ -6\\ 15\\ \end{pmatrix} $$

!!! def ""

    유한차원 벡터공간 $\mathbf{V} , \mathbf{W}$ 와 동형사상 $\mathbf{T} : \mathbf{V} \to \mathbf{W}$, $\mathbf{V}$ 의 부분공간 $\mathbf{V}_0$ 에 대하여 다음이 성립한다. 

    1. $\mathbf{T} (\mathbf{V} _0)$ 은 $\mathbf{W}$ 의 부분공간이다.

    2. $\dim (\mathbf{V} _0) = \dim (\mathbf{T} (\mathbf{V} _0))$

- 증명

    1:

    [선형변환의 성질](#841cc7807) 에 의하여 $\mathbf{T} (0) = 0 \in \mathbf{W}$ 이다. ▲ 

    $x, y \in \mathbf{V} _0$ 에 대하여 $\mathbf{T} (x) \in \mathbf{T} (\mathbf{V} _0), \mathbf{T} (y) \in \mathbf{T} (\mathbf{V} _0)$ 이다. 이때 $\mathbf{V} _0$ 이 부분공간이므로 $x + y \in \mathbf{V} _0$ 이다. 그러므로 $\mathbf{T} (x + y) = \mathbf{T} (x) + \mathbf{T} (y) \in \mathbf{T} (\mathbf{V} _0)$ 이다. ▲ 

    $a \in \mathbf{F}, x \in \mathbf{V} _0$ 에 대하여 $\mathbf{V} _0$ 가 부분공간이므로 $ax \in \mathbf{V} _0$ 이다. 그러므로 $\mathbf{T} (ax) = a \mathbf{T} (x) \in \mathbf{T} (\mathbf{V} _0)$ 이다. ▲ 

    [정리 1.3](../VectorSpace/#42f9c15c6) 에 의하여 $\mathbf{T} (\mathbf{V} _0)$ 은 $\mathbf{W}$ 의 부분공간이다. ■ 

    2:

    변환 $\mathbf{T} : \mathbf{V} \to \mathbf{W}$ 의 제한 $\mathbf{T} | _{\mathbf{V}_0}: \mathbf{V} _0 \to \mathbf{T}(\mathbf{V} _0)$ 은 전사이다. 동형사상 $\mathbf{T}$ 가 단사이므로 $\mathbf{T}$ 의 대응규칙을 유지한채 논의영역을 축소시킨 $\mathbf{T}|_{\mathbf{V} _0}$ 도 단사이다. 그러므로 $\mathbf{T}|_{\mathbf{V} _0}$ 는 동형사상이며 $\mathbf{V} _0 \cong \mathbf{T} (\mathbf{V} _0)$ 이다. 그러므로 [정리 2.19](#af05a99e0) 에 의하여 

    $$ \therefore \dim (\mathbf{V} _0) = \dim (\mathbf{T} (\mathbf{V} _0)) $$

    이다. ■ 

!!! def ""

    $n$차원 벡터공간 $\mathbf{V}$ 와 $m$차원 벡터공간 $\mathbf{W}$, 선형변환 $\mathbf{T} : \mathbf{V} \to \mathbf{W}$, $\mathbf{V}$ 의 순서기저 $\beta$, $\mathbf{W}$ 의 순서기저 $\gamma$, 행렬 $A = [\mathbf{T} ]^{\gamma}_{\beta}$ 에 대하여 다음이 성립한다. 

    1. $\text{rank} (\mathbf{T} )  = \text{rank} (\mathbf{L}_{A})$

    2. $\text{nullity} (\mathbf{T} ) = \text{nullity} (\mathbf{L}_{A})$

- 증명

    1:

    $\phi _{\beta }$ 가 전사이고 [$\mathbf{L}_{A} \circ \phi _{\beta } = \phi _{\gamma } \circ \mathbf{T}$](#ea96f31c4) 이므로 다음을 얻는다.

    $$ \mathbf{R} (\mathbf{L}_A) = \mathbf{L}_{A}(\mathbf{F} ^{n}) = \mathbf{L}_{A}\phi _{\beta }(\mathbf{V} ) = \phi _{\gamma }\mathbf{T} (\mathbf{V} ) = \phi _{\gamma }(\mathbf{R} (\mathbf{T}) ) $$

    그러므로 $\phi _{\gamma }(\mathbf{R} (\mathbf{T}) ) = \mathbf{R} (\mathbf{L} _A)$ 이다. [$\mathbf{R} (\mathbf{T})$ 가 $\mathbf{W}$ 의 부분공간](#eb957cbf0)이고 [정리 2.21](#f0ddc0f9b) 에 의하여 $\phi _{\gamma }$ 가 동형사상이므로 [$\dim (\mathbf{R} (\mathbf{T})) = \dim (\mathbf{R} (\mathbf{L}_A))$ 이다](#1e331034c). 그러므로 

    $$ \text{rank} (\mathbf{T})  = \text{rank} (\mathbf{L}_{A}) $$

    이다. ■ 

    2:

    $y \in \phi _{\beta }(\mathbf{N} (\mathbf{T}) )$ 이면 $x \in \mathbf{N} (\mathbf{T})$ 에 대하여 $y = \phi _{\beta }(x)$ 이다. 그러므로 [$\mathbf{L}_{A} \circ \phi _{\beta } = \phi _{\gamma } \circ \mathbf{T}$](#ea96f31c4) 와 [$\phi _{\gamma }$ 가 선형](#51765b179) 인 것에 의하여 다음을 얻는다.

    $$ \mathbf{L}_{A}(y) = \mathbf{L}_{A}(\phi _{\beta }(x)) = \phi _{\gamma }\mathbf{T} (x) = \phi _{\gamma }(0) = 0 $$

    즉, $y \in \phi _{\beta }(\mathbf{N} (\mathbf{T}) ) \implies y \in \mathbf{N} (\mathbf{L}_A)$ 이므로 $\phi _{\beta }(\mathbf{N} (\mathbf{T}) ) \subset \mathbf{N} (\mathbf{L}_A)$ 이다. ▲ 

    역으로 $y \in \mathbf{N} (\mathbf{L}_A)$ 이면 $\mathbf{L}_{A}(y) = 0$ 이다. $\phi _{\beta }$ 가 전사이므로 $y = \phi _{\beta }(x)$ 인 $x \in \mathbf{V}$ 가 존재한다. 
    
    만약 $\mathbf{T} (x) = 0$ 이라면 $x \in \mathbf{N} (\mathbf{T}) \implies y \in \phi _{\beta }(\mathbf{N} (\mathbf{T}) )$ 이다. 그러면 $y \in \mathbf{N} (\mathbf{L}_A) \implies y \in \phi _{\beta }(\mathbf{N} (\mathbf{T}) )$ 이므로 $\mathbf{N} (\mathbf{L}_A) \subset \phi _{\beta }(\mathbf{N} (\mathbf{T}) )$ 이고 결국 $\phi _{\beta }(\mathbf{N} (\mathbf{T}) ) = \mathbf{N} (\mathbf{L}_A)$ 가 된다. 그러면 [$\mathbf{N} (\mathbf{T})$ 가 $\mathbf{V}$ 의 부분공간](#eb957cbf0) 이고 [정리 2.21](#f0ddc0f9b) 에 의하여 $\phi _{\beta }$ 가 동형사상이므로 [$\dim (\mathbf{N} (\mathbf{T}) ) = \dim (\mathbf{N} (\mathbf{L}_A))$](#1e331034c) 을 얻고 모든 증명이 끝난다.
    
    다음이 성립한다.

    $$ \phi _{\gamma }(\mathbf{T} (x)) = \mathbf{L}_{A}(\phi _{\beta }(x)) = \mathbf{L}_{A}(y) = 0 $$

    $\phi _{\gamma }$ 가 단사이므로 [정리 2.4](#7d40e8276) 에 의하여 $\mathbf{T} (x) = 0$ 이다. ■ 

# Change of basis

!!! def "정리 2.22"

    유한차원 벡터공간 $\mathbf{V}$ 의 두 순서기저 $\beta , \beta '$ 에 대하여 $Q = [\mathbf{I} _{\mathbf{V} }] ^{\beta}_{\beta'}$ 라고 하면 다음이 성립한다. 

    1. $Q$ 는 가역행렬이다.

    2. $\forall v \in \mathbf{V} : [v] _{\beta } = Q[v] _{\beta '}$

- 증명 

    [정리 2.18](#7ab982f5b) 에 의하여 $\mathbf{I} _{\mathbf{V}}$ 가 가역이므로 $Q$ 도 가역이다. ▲ 

    [정리 2.14](#93b3bc7a2) 에 의하여 

    $$ \forall v \in \mathbf{V} : [v] _{\beta } = [\mathbf{I} _{\mathbf{V} }(v)]_{\beta} = Q[v]_{\beta '} $$

    이다. ■ 

!!! def "좌표변환 행렬(change of coordinate matrix, change of basis matrix)"

    유한차원 벡터공간 $\mathbf{V}$ 의 두 순서기저 $\beta , \beta '$ 에 대하여 $\beta '$ 좌표를 $\beta$ 좌표로 변환하는 행렬 $Q  = [\mathbf{I} _{\mathbf{V} }] ^{\beta}_{\beta'}$ 이다.

- *정리 2.22 와 본 정의는 기저 $\beta '$ 를 $\beta$ 로 변환한다는 형식으로 논의되었는데, 이 정리와 본 정의가 도출된 과정을 설명하는 아래의 논의에서는 내가 실수로 $\beta$ 를 $\beta '$ 으로 변환한다는 형식을 사용해버렸다. 이제와서 고치기에 너무 늦었다.*

- 이것은 벡터공간 $\mathbf{V}$ 의 서로 다른 기저 $\beta , \beta '$ 와 어떤 벡터 $v$ 에 대하여 

    $$ v \to [v] _{\beta } \qquad v \to [v] _{\beta' } $$

    와 같이 좌표벡터를 구한 것에서 

    $$ [v] _{\beta } \to [v] _{\beta '} $$

    와 같이 어떤 좌표를 다른 기저에 대한 좌표로 변환하는 수학적 장치이다.

- 유한차원 벡터공간 $\mathbf{V}$ 가 차원이 $n$ 이고 서로 다른 기저 $\beta = (u_1, u_2, \dots, u_n), \beta ' = (w_1, w_2, \dots, w_n)$ 을 갖는다고 하자. 어떤 벡터 $v \in \mathbf{V}$ 가 $[v] _{\beta }$ 나 $[v] _{\beta '}$ 와 같은 좌표벡터로 표현되어 있을 때 이것으로부터 어떻게 다른 기저에 대한 좌표벡터를 구할 수 있을까? 이것을 [정리 2.14](#93b3bc7a2) 를 사용하지 말고 행렬 성분을 실제로 다뤄보면서 알아보자. 

    먼저 [좌표벡터](#be888949c) 의 정의에 의하여 $[v] _{\beta }= \begin{pmatrix} c_1\\ c_2\\ \vdots \\ c_n\\ \end{pmatrix}$ 는 다음과 같은 기저 $\beta$ 의 일차결합이다. $c_1, c_2, \dots, c_n$ 은 스칼라이다.

    $$ v = c_1u_1 + c_2u_2 + \dots + c_nu_n $$

    이때 기저 $\beta$ 의 벡터 $u_1, u_2, \dots, u_n$ 들을 다음과 같이 기저 $\beta '$ 에 대한 좌표벡터로 나타낼 수 있다. $a_{ij}$ 들은 스칼라이다.

    $$ [u_1] _{\beta '} = \begin{pmatrix} a _{11}\\ a _{21}\\ \vdots\\ a _{n1}\\ \end{pmatrix}, [u_2] _{\beta '} = \begin{pmatrix} a _{12}\\ a _{22}\\ \vdots\\ a _{n2}\\ \end{pmatrix}, \dots, [u_n] _{\beta '} = \begin{pmatrix} a _{1n}\\ a _{2n}\\ \vdots\\ a _{nn}\\ \end{pmatrix} \tag{1} $$

    그러므로 $\beta$ 를 다음과 같이 $\beta '$ 의 일차결합으로 나타낼 수 있다.

    $$ u_1 =  a _{11}w_1+ a _{21}w_2+ \dots+ a _{n1}w_n $$ 

    $$ u_2 =  a _{12}w_1+ a _{22}w_2+ \dots+ a _{n2}w_n $$ 

    $$ \vdots $$

    $$ u_n =  a _{1n}w_1+ a _{2n}w_2+ \dots+ a _{nn}w_n $$ 

    그렇다면 $v = c_1u_1 + c_2u_2 + \dots + c_nu_n$ 와 같이 표현된 일차결합에서 $u_i$ 들을 위와 같은 $\beta '$  의 일차결합 표현으로 치환해버리면 $[v] _{\beta }$ 를 $[v] _{\beta '}$ 로 변환할 수 있다. 즉, 다음과 같이 $v$ 의 $\beta$ 일차결합 표현을 $\beta '$ 일차결합 표현으로 변환하는 것이다.

    $$ \begin{equation}\begin{split} v = \enspace & c_1(a _{11}w_1+ a _{21}w_2+ \dots+ a _{n1}w_n ) + \\ &c_2(a _{12}w_1+ a _{22}w_2+ \dots+ a _{n2}w_n ) + \\ &\dots + \\ &c_n(a _{1n}w_1+ a _{2n}w_2+ \dots+ a _{nn}w_n ) \\ \end{split}\end{equation} \tag*{} $$

    $$ \begin{equation}\begin{split} v = \enspace & (c_1a _{11}+ c_2a _{21}+ \dots+ c_na _{n1} )w_1 + \\ &(c_1a _{12}+ c_2a _{22}+ \dots+ c_na _{n2} )w_2 + \\ &\dots + \\ &(c_1a _{1n}+ c_2a _{2n}+ \dots+ c_na _{nn} )w_n \\ \end{split}\end{equation} \tag*{} $$

    그렇다면 [좌표벡터](#be888949c) 의 정의에 의하여 

    $$ [v] _{\beta '} = \begin{pmatrix} c_1 a _{11} & c_2 a _{21} & \dots & c_n a _{n1} & \\ c_1 a _{12} & c_2 a _{22} & \dots & c_n a _{n2} & \\ \vdots \\ c_1 a _{1n} & c_2 a _{2n} & \dots & c_n a _{nn} & \\ \end{pmatrix} = \begin{pmatrix} a_{11}&a_{12}&\dots&a_{1n}\\ a_{21}&a_{22}&\dots&a_{2n}\\ \vdots& \vdots& \ddots& \vdots \\ a_{n1}&a_{n2}&\dots&a_{nn}\\ \end{pmatrix} \begin{pmatrix} c_{1}\\ c_{2}\\ \vdots\\ c_{n}\\ \end{pmatrix} = \begin{pmatrix} a_{11}&a_{12}&\dots&a_{1n}\\ a_{21}&a_{22}&\dots&a_{2n}\\ \vdots& \vdots& \ddots& \vdots \\ a_{n1}&a_{n2}&\dots&a_{nn}\\ \end{pmatrix} [v] _{\beta } $$

    가 된다. 그러면 행렬 $\begin{pmatrix} a_{11}&a_{12}&\dots&a_{1n}\\ a_{21}&a_{22}&\dots&a_{2n}\\ \vdots& \vdots& \ddots& \vdots \\ a_{n1}&a_{n2}&\dots&a_{nn}\\ \end{pmatrix}$ 은 좌표벡터 $[v] _{\beta }$ 를 $[v] _{\beta '}$ 로 변환해주는 변환행렬이 되는 것이다. 이 행렬을 $A$ 라고 하면 기저 $\beta$ 를 $\beta '$ 로 변환해준다는 의미로 아래첨자를 써서 $A _{\beta \to \beta '}$ 로 표기하기도 한다. 그러면 간략하게 

    $$ [v] _{\beta '} = A _{\beta \to \beta '}[v] _{\beta } $$

    라고 표기할 수 있다. 

- 그러면 어떤 기저 $\beta$ 를 다른 기저 $\beta '$ 로 변환해주는 행렬 $A _{\beta \to \beta '}$ 이 정말로 다음을 만족할까? 

    $$ \boxed{[\mathbf{I} _{\mathbf{V} }] ^{\beta'}_{\beta} = A _{\beta \to \beta '}} \tag{2}  $$ 

    [선형변환의 행렬표현](#c16bc5e5b) 에 의하여 $[\mathbf{I} _{\mathbf{V} }] ^{\beta}_{\beta'}$ 의 $j$ 열은 $[\mathbf{I} _{\mathbf{V} }(u_j)] _{\beta '}$ 인데 [항등변환의 정의](#c604a0153)에 의하여 이는 곧 $[u_j] _{\beta '}$ 가 되고 [좌표벡터](#be888949c) 의 정의와 위에서 정의했었던 $(1)$ 의하여 결국

    $$ [u_j] _{\beta '} = \begin{pmatrix} a _{1j}\\ a _{2j}\\ \vdots \\ a _{nj}\\ \end{pmatrix} $$

    가 된다. 즉, $[\mathbf{I} _{\mathbf{V} }] ^{\beta'}_{\beta}$ 의 $j$ 열과 $A _{\beta \to \beta '}$ 의 $j$ 열이 같으므로 $(2)$ 가 성립함을 알 수 있다.

- 예시 

    $\R ^{2}$ 의 서로 다른 기저 $\beta = \{(1,1), (1, -1)\}, \beta ' = \{(2,4), (3,1)\}$ 에 대하여 

    $$ (2, 4) = 3(1, 1) - 1(1, -1) $$

    $$ (3, 1) = 2(1, 1) + 1(1, -1) $$

    이므로 $Q = \begin{pmatrix} 3&2\\ -1&1\\ \end{pmatrix}$ 이다. 그러므로 다음이 성립한다. 

    $$ [(2, 4)] _{\beta } = Q[(2, 4)] _{\beta '} = Q \begin{pmatrix} 1\\ 0\\ \end{pmatrix} = \begin{pmatrix} 3\\ -1\\ \end{pmatrix} $$

!!! def ""

    유한차원 벡터공간 $\mathbf{V}$ 의 두 순서기저 $\beta , \beta '$ 에 대하여 $\beta '$ 좌표를 $\beta$ 좌표로 변환하는 좌표변환 행렬 $Q = [\mathbf{I} _{\mathbf{V} }] ^{\beta}_{\beta'}$ 에 대하여 역행렬 $Q^{-1}$ 는 $\beta$ 의 좌표를 $\beta '$ 으로 변환한다.

- 증명

    $$ [v] _{\beta } = Q[v]_{\beta '} \iff Q ^{-1} [v] _{\beta } = [v]_{\beta '} \tag*{■} $$

## Linear Operator

!!! def "선형연산자(linear operator)"

    벡터공간 $\mathbf{V}$ 에 대하여 $\mathbf{V}$ 의 선형연산자는 $\mathbf{V} \to \mathbf{V}$ 에서 정의된 선형변환이다.

!!! def "정리 2.23"

    유한차원 벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 와 $\mathbf{V}$ 의 순서기저 $\beta , \beta '$ 와 $\beta '$ 좌표를 $\beta$ 좌표로 변환하는 좌표변환 행렬 $Q$ 에 대하여 다음이 성립한다. 

    $$ [\mathbf{T} ] _{\beta '} = Q ^{-1}[\mathbf{T} ] _{\beta }Q $$

- **정리 2.22 가 한 기저로 표현된 벡터를 다른 기저 표현의 벡터로 변환하는 방법을 알려주었다면, 이 정리는 한 기저로 표현된 선형변환을 다른 기저로 표현된 선형변환으로 변환하는 방법을 알려준다.**

    즉, $\beta$ 로 표현된 선형변환을 $\beta '$ 으로 표현된 선형변환으로 바꾸려면 $\beta$ 로 표현된 선형변환의 우측에 $\beta '$ 좌표를 $\beta$ 좌표로 변환하는 행렬을 곱하고, 좌측에 $\beta$ 좌표를 $\beta '$ 좌표로 변환하는 행렬을 곱하면 된다.

    정리 2.22 는 다음과 같이 좌표벡터의 기저를 변환하는 수학적 장치를 제공했다. 

    $$ [v]_{\beta '} \mapsto [v]_{\beta} $$

    반면 이 정리는 다음과 같이 선형변환 행렬표현의 기저를 변환하는 수학적 도구를 제공한다.

    $$ [\mathbf{T}]_{\beta '} \mapsto [\mathbf{T}]_{\beta } $$

- 증명

    항등변환 $\mathbf{I}$ 가 $\mathbf{T} = \mathbf{T} \mathbf{I} = \mathbf{I} \mathbf{T}$ 인 것과 [정리 2.11](#2fc8f26aa) 인 것으로부터 다음이 성립한다. 

    $$ Q[\mathbf{T} ] _{\beta '} = [\mathbf{I} ]^{\beta}_{\beta'} [\mathbf{T} ]^{\beta'}_{\beta'} = [\mathbf{I} \mathbf{T} ]^{\beta}_{\beta'} = [\mathbf{T} \mathbf{I} ]^{\beta}_{\beta'} = [\mathbf{T} ]^{\beta}_{\beta} [\mathbf{I} ]^{\beta}_{\beta'}  = [\mathbf{T} ]_{\beta }Q $$

    그러므로 $[\mathbf{T} ] _{\beta '} = Q ^{-1}[\mathbf{T} ] _{\beta }Q$ 이다.

!!! def "정리 2.23 따름정리"

    $A \in \mathbf{M}_{n \times n}(\mathbf{F} )$ 와 $\mathbf{F} ^{n}$ 의 순서기저 $\gamma$ 와 $\gamma$ 의 벡터들을 열로 구성한 행렬 $Q$ 에 대하여 다음이 성립한다. 

    $$ [\mathbf{L}_{A}] _{\gamma } = Q ^{-1} AQ $$

- 이 정리는 좌측곱변환을 임의의 기저로 표현하는 방법을 알려준다.

- 증명

    정리 2.23 에 의하여 $\mathbf{F}^{n}$ 의 표준순서기저 $\beta$ 와 $\gamma$ 좌표를 $\beta$ 좌표로 변환하는 좌표변환행렬 $Q$ 에 대하여 다음이 성립한다. 

    $$ [\mathbf{L}_{A}]_{\gamma } = Q ^{-1}[\mathbf{L}_{A}]_{\beta }Q $$

    [정리 2.15-(1)](#c3298a7b3) 에 의하여 $[\mathbf{L}_{A}]_{\beta} = A$ 이므로 다음이 성립한다.

    $$ [\mathbf{L}_{A}]_{\gamma } = Q ^{-1}AQ \tag*{▲} $$

    $\gamma = \{v_1, v_2, \dots, v_n\}, v_j = \begin{pmatrix} a_{1j}\\ a_{2j}\\ \vdots\\ a_{nj}\\ \end{pmatrix}$ 로 두면 다음이 성립한다.

    $$ \mathbf{I}_{\mathbf{V}}(v_j) = v_j = a_{1j} e_1 + a_{2j} e_2 + \dots + a_{nj}e_n = \sum_{i=1}^{n}a_{ij}e_i $$

    따라서 $(Q)_{ij} = ([\mathbf{I}_{\mathbf{V}}]_{\gamma }^{\beta }) _{ij} = a_{ij}$ 이다. 즉, $Q$ 는 $\gamma$ 의 벡터들을 열로 구성한 행렬이다. ■ 

- 예시 

    다음과 같은 집합 $A$ 와 $\R ^{3}$ 의 순서기저를 생각하자. 

    $$ A = \begin{pmatrix} 2&1&0\\ 1&1&3\\ 0&-1&0\\ \end{pmatrix}, \gamma = \Bigg \{ \begin{pmatrix} -1\\ 0\\ 0\\ \end{pmatrix}, \begin{pmatrix} 2\\ 1\\ 0\\ \end{pmatrix}, \begin{pmatrix} 1\\ 1\\ 1\\ \end{pmatrix} \Bigg \} $$

    그러면 $Q, Q ^{-1}$ 은 다음과 같다. 

    $$ Q = \begin{pmatrix} -1&2&1\\ 0&1&1\\ 0&0&1\\ \end{pmatrix}, Q ^{-1} = \begin{pmatrix} -1&2&-1\\ 0&1&-1\\ 0&0&1\\ \end{pmatrix} $$

    그러므로 다음이 성립한다. 

    $$ [\mathbf{L}_{A}]_{\gamma } = Q ^{-1}AQ = \begin{pmatrix} 0&2&8\\ -1&4&6\\ 0&-1&-1\\ \end{pmatrix} $$

## Matrix Similarity

!!! def "행렬의 닮음(matrix similarity)"

    $A, B \in \mathbf{M}_{n \times n}(\mathbf{F} )$ 에 대하여 $B = Q ^{-1}AQ$ 인 가역행렬 $Q$ 가 존재하면 $A$ 와 $B$ 는 서로 닮음이다.

- 행렬의 닮음은 두 행렬이 같은 선형변환의 서로 다른 기저에 대한 행렬표현임을 나타내는 관계이다.

- 행렬의 닮음은 동치관계이다.

    - 증명

!!! def "정리 2.23 의 일반화"

    유한차원 벡터공간 $\mathbf{V}, \mathbf{W}$ 의 선형변환 $\mathbf{T}: \mathbf{V} \to \mathbf{W}$ 와 $\mathbf{V}$ 의 순서기저 $\beta , \beta '$ 와 $\mathbf{W}$ 의 순서기저 $\gamma , \gamma '$ 와 $\beta '$ 좌표를 $\beta$ 좌표로 변환하는 좌표변환 행렬 $Q$ 와 $\gamma '$ 좌표를 $\gamma$ 좌표로 변환하는 좌표변환 행렬 $P$ 에 대하여 다음이 성립한다. 

    $$ [\mathbf{T} ] ^{\gamma'}_{\beta'}  = P ^{-1}[\mathbf{T} ] ^{\gamma}_{\beta} Q $$

- 증명

- 이 정리는 서로 다른 벡터공간 $\mathbf{V} , \mathbf{W}$ 사이에 정의된 선형변환에서도 성립한다. 이 경우 $\mathbf{V}$ 의 기저를 바꾸듯이 $\mathbf{W}$ 의 기저도 바꿀 수 있다. 

!!! def "문제 2.5-13"

    유한차원 $\mathbf{F}$-벡터공간 $\mathbf{V}$ 와 순서기저 $\beta = \{x_1, x_2, \dots, x_n\}$, 가역행렬 $Q \in \mathbf{M}_{n \times n}(\mathbf{F})$ 와 $j \in \{1, \dots, n\}$ 에 대하여 $x'_j$ 를 다음과 같이 정의하자. 

    $$ x'_j = \sum_{i=1}^{n}Q _{ij}x_i $$

    집합 $\beta ' = \{x'_1, x'_2, \dots, x'_n\}$ 은 $\mathbf{V}$ 의 기저이고 $Q$ 는 $\beta '$ 좌표를 $\beta$ 좌표로 변환하는 좌표변환 행렬이다.

- 증명

    $|\beta '| = n$ 이므로 $\beta '$ 가 일차독립임을 보이면 된다. $a_1, a_2, \dots, a_n \in \mathbf{F}$ 에 대하여 다음이 성립한다.
    
    $$ \begin{equation}\begin{split} a_1x'_1 + a_2x'_2 + \dots + a_nx'_n &= \sum_{j=1}^{n}a_jx'_j = \sum_{j=1}^{n}a_j \bigg ( \sum_{i=1}^{n}Q _{ij}x_i\bigg ) \\ &= \sum_{j=1}^{n}\sum_{i=1}^{n}a_jQ _{ij}x_i = \sum_{i=1}^{n}\sum_{j=1}^{n}a_j Q _{ij}x_i \\ &= \sum_{j=1}^{n} a_j Q _{1j}x_1 + \sum_{j=1}^{n} a_j Q _{2j}x_2 + \dots + \sum_{j=1}^{n} a_j Q _{nj}x_n = 0 \end{split}\end{equation} \tag*{} $$ 

    $$ \implies \sum_{j=1}^{n}a_j Q _{1j} = \sum_{j=1}^{n}a_j Q _{2j} = \dots = \sum_{j=1}^{n}a_j Q _{nj} = 0 \tag{1} $$

    $Q$ 의 $j$열을 $Q_j$ 라 하면 $Q_j = \begin{pmatrix} Q_{1j}\\ Q_{2j}\\ \vdots \\ Q_{nj}\\ \end{pmatrix}$ 이다. [$Q$ 가 가역이므로 $\text{rank} (Q) = n$](../MatrixOperation/#8252ffa8b) 이다. 또한 [랭크는 행렬의 열들의 극대 일차독립 집합의 기수](../MatrixOperation/#0ce821e3f)를 뜻하므로 $Q$ 의 모든 열이 일차독립이다. 즉, 다음이 성립한다.

    $$ \forall c_1, c_2, \dots, c_n \in \mathbf{F} : c_1Q_1 + c_2Q_2 + \dots + c_nQ_n = 0 \implies c_1 = c_2 = \dots = c_2 = 0 $$ 

    이는 다음이 성립함을 뜻한다.

    $$ \sum_{i=1}^{n}c_i Q _{1i} = 0 \land \sum_{i=1}^{n}c_i Q _{2i} = 0 \land \dots \land \sum_{i=1}^{n}c_i Q _{ni} = 0 \implies c_1 = c_2 = \dots = c_2 = 0 $$

    따라서 $(1)$ 에 의하여 다음이 성립한다.

    $$ a_1 = a_2 = \dots = a_n = 0 $$

    그러므로 $\beta '$ 는 기저이다. ▲ 

    선형변환의 행렬표현에 의하여 다음이 성립한다는 것은 $[\mathbf{I}_{\mathbf{V}}] _{\beta '}^{\beta }$ 의 $i$행 $j$열 성분이 $Q _{ij}$ 임을 뜻한다. 

    $$ \mathbf{I}_{\mathbf{V}}(x'_j) = x'_j = \sum_{i=1}^{n}Q _{ij}x_i $$

    즉, $Q = [\mathbf{I}]_{\beta '} ^{\beta }$ 이다. 좌표변환 행렬의 정의에 의하여 $Q$ 는 $\beta '$ 좌표를 $\beta$ 좌표로 변환하는 좌표변환 행렬이다. ■ 

# Dual Space

!!! def "선형범함수(linear functional, linear form, one-form, covector)"

    $\mathbf{F}$-벡터공간 $\mathbf{V}$ 에 대하여 $\mathbf{V}\to \mathbf{F}$ 에서 정의된 선형변환이다.

- 체 $\mathbf{F}$ 는 $\mathbf{F}$ 에서의 1차원 벡터공간이다.

- 이제 선형범함수를 $\mathbf{f}, \mathbf{g}, \mathbf{h}, \dots$ 와 같은 서체로 나타내자.

- 예시

    $\mathbf{V}= \mathbf{M}_{n \times n}(\mathbf{F})$ 에 대하여 함수 $\mathbf{f}: \mathbf{V}\to \mathbf{F}, A \to \text{tr} (A)$ 는 선형범함수이다.

!!! def "푸리에 계수(Fourier coefficient)"

    폐구간 $[0, 2 \pi ]$ 에서 정의된 연속인 실함수로 이루어진 벡터공간 $\mathbf{V}$ 에 대하여 $g \in \mathbf{V}$ 를 고정하여 다음과 같이 정의한 함수 $\mathbf{h}: \mathbf{V}\to \R$ 를 가정하자.

    $$ \mathbf{h}(x) = \frac{1}{2 \pi }\int_{0}^{2 \pi }x(t)g(t)dt $$

    $g(t) = \sin nt$ 또는 $g(t) = \cos nt$ 일 때 $\mathbf{h}(x)$ 를 $x$ 의 $n$번째 푸리에 계수라고 한다.

- 함수 $\mathbf{h}$ 는 선형범함수의 예시이다.

## Coordinate Function

!!! def "좌표함수(coordinate function)"

    순서기저 $\beta = \{x_1, x_2, \dots, x_n\}$ 를 가지는 유한차원 벡터공간 $\mathbf{V}$ 와 $i \in \{1,\dots,n\}$ 에 대하여 다음과 같이 정의된 함수 $\mathbf{f}_i: \mathbf{V}\to \mathbf{F}$ 를 기저 $\beta$ 에 대한 $i$번째 좌표함수라 한다.

    $$ x \in \mathbf{V} : [x] _{\beta } = \begin{pmatrix} a_{1}\\ a_{2}\\ \vdots\\ a_{n}\\ \end{pmatrix} \implies \mathbf{f}_i(x) = a_i $$

- 좌표함수는 $\mathbf{V}$ 의 선형범함수이다.

- $\mathbf{f}_i(x_j) = \delta _{ij}$ 이다.

!!! def "쌍대공간(dual space)"

    $\mathbf{F}$-벡터공간 $\mathbf{V}$ 에 대한 벡터공간 $\mathbf{V}^{*} := \mathcal{L}(\mathbf{V},\mathbf{F})$ 를 $\mathbf{V}$ 의 쌍대공간이라 한다.

- $\mathbf{V}^{*}$ 은 [함수의 합과 스칼라곱](#63a07e35d) 이 정의된 $\mathbf{V}$ 의 모든 선형범함수로 이루어진 벡터공간이다.

!!! def ""

    유한차원 벡터공간 $\mathbf{V}$ 와 쌍대공간 $\mathbf{V}^{*}$ 에 대하여 다음이 성립한다.

    $$ \mathbf{V} \cong \mathbf{V}{}^{*} $$

- 증명

    $\mathbf{F}$ 는 1차원 벡터공간이므로 $\dim (\mathbf{F}) = 1$ 이다. 따라서 [정리 2.20 따름정리](#955ca765c) 에 의하여 다음이 성립한다. 

    $$ \dim (\mathbf{V}{}^{*}) = \dim (\mathcal{L}(\mathbf{V}, \mathbf{F})) = \dim (\mathbf{V}) \dim (\mathbf{F}) = \dim (\mathbf{V}) $$

    [정리 2.19](#af05a99e0) 에 의하여 $\mathbf{V}$ 와 $\mathbf{V}^{*}$ 은 동형이다. ■ 

## Double Dual

!!! def "이중 쌍대공간(double dual)"

    벡터공간 $\mathbf{V}$ 의 쌍대공간 $\mathbf{V}^{*}$ 의 쌍대공간 $\mathbf{V}^{**}$ 을 $\mathbf{V}$ 의 이중 쌍대공간이라 한다.

!!! def ""

    유한차원 벡터공간 $\mathbf{V}$ 에 대하여 다음이 성립한다.

    $$ \mathbf{V}\cong \mathbf{V}{}^{*}\cong \mathbf{V}{}^{*}{}^{*}\cong \mathbf{V}{}^{*}{}^{*}{}^{*}\cong \dots $$

- *$\mathbf{V}\cong \mathbf{V}{}^{*}$ 라는 정리에서 이 정리도 성립할 거라고 생각했는데 검증필요.*

- 증명

    $$ \because \mathbf{V}\cong \mathbf{V}{}^{*} $$

- 여기에서 다루는 쌍대공간의 정리들은 이 정리만 제외하고 무한차원에서도 성립한다. 가령 쌍대공간의 존재성 정리나 쌍대기저의 존재성 정리 같은 것들은 무한차원에서도 성립하지만, 무한차원 벡터공간에서는 $\mathbf{V}, \mathbf{V}{}^{*}, \mathbf{V}{}^{*}{}^{*}$ 중 어느 두 공간도 동형이 아니다. 

!!! def "정리 2.24"

    순서기저 $\beta  = \{x_1, x_2, \dots, x_n \}$ 을 가지는 유한차원 벡터공간 $\mathbf{V}$ 와 $\beta$ 의 $i$번째 좌표함수 $\mathbf{f}_i$ 에 대하여 $\beta {}^{*} = \{\mathbf{f}_1, \mathbf{f}_2, \dots, \mathbf{f}_n \}$ 는 $\mathbf{V}^{*}$ 의 순서기저이다. 즉, 다음이 성립한다.

    $$ \forall \mathbf{f} \in \mathbf{V}{}^{*} : \mathbf{f} = \sum_{i=1}^{n}\mathbf{f}(x_i)\mathbf{f}_i $$

- 증명

    $\dim (\mathbf{V}{}^{*}) = n$ 이므로 다음과 같이 $\beta {}^{*}$ 가 $\mathbf{V}^{*}$ 을 생성함을 보이면 증명이 끝난다.
    
    $$ \forall \mathbf{f}\in \mathbf{V}{}^{*} : \mathbf{f} = \sum_{i=1}^{n}\mathbf{f}(x_i)\mathbf{f}_i $$

    $\displaystyle \mathbf{g} = \sum_{i=1}^{n}\mathbf{f}(x_i)\mathbf{f}_i$ 로 두면 $j \in \{1,\dots,n\}$ 에 대하여 [함수의 합의 정의](#63a07e35d) 에 의하여 다음이 성립한다. 

    $$ \begin{equation}\begin{split}
    \mathbf{g}(x_j) &= \bigg (\sum_{i=1}^{n}\mathbf{f}(x_i)\mathbf{f}_i \bigg )(x_j) = \sum_{i=1}^{n}\mathbf{f}(x_i)\mathbf{f}_i(x_j) \\
    &= \sum_{i=1}^{n}\mathbf{f}(x_i)\delta _{ij} = \mathbf{f}(x_j)\\
    \end{split}\end{equation} \tag*{} $$

    [정리 2.6 따름정리](#52dd3d90f)에 의하여 $\mathbf{f} = \mathbf{g}$ 이다. ■ 

## Dual Basis

!!! def "쌍대기저(dual basis)"

    순서기저 $\beta  = \{x_1, x_2, \dots, x_n \}$ 을 가지는 유한차원 벡터공간 $\mathbf{V}$ 와 $i, j \in \{1,\dots,n\}$ 에 대하여 $\mathbf{f}_i(x_j) = \delta _{ij}$ 를 만족하는 $\mathbf{V}^{*}$ 의 순서기저 $\beta {}^{*} = \{\mathbf{f}_1, \mathbf{f}_2, \dots, \mathbf{f}_n \}$ 를 $\beta$ 의 쌍대기저라고 한다.

- 순서기저 $\beta$ 의 원소 $x_j$ 에 대하여 $\mathbf{f}_i(x_j) = \delta _{ij}$ 인 것은 좌표함수라는 뜻이다. 따라서 쌍대기저의 정의는 정리 2.24 에서의 집합 $\beta {}^{*}$ 와 같다.

    또한 정리 2.24 는 쌍대기저 $\beta {}^{*}$ 의 존재성을 보장해준다.

    쌍대기저의 존재성이 보장된 것을 기반으로 이 쌍대기저의 정의는 정리 2.24 에서 말하는 쌍대공간 $\mathbf{V}^{*}$ 의 기저를 구하는 방법을 알려준다. 아래 예시를 보자.

- 예시 

    벡터공간 $\R ^{2}$ 의 순서기저 $\beta = \{(2,1), (3,1)\}$ 에 대한 $\beta$ 의 쌍대기저 $\beta {}^{*}=\{\mathbf{f}_1, \mathbf{f}_2\}$ 를 구해보자. 

    $$ 1 = \mathbf{f}_1(2, 1) = \mathbf{f}_1(2e_1 + e_2) = 2 \mathbf{f}_1(e_1) + \mathbf{f}_1(e_2) $$

    $$ 0 = \mathbf{f}_1(3, 1) = \mathbf{f}_1(3e_1 + e_2) = 3 \mathbf{f}_1(e_1) + \mathbf{f}_1(e_2) $$

    연립방정식을 풀면 $\mathbf{f}_{1}(e_1) = -1, \mathbf{f}_{1}(e_2) = 3$ 을 얻는다. 따라서 $\mathbf{f}_{1}(x, y) = -x + 3y$ 이다. 같은 방식으로 $\mathbf{f}_{2}(x,y)=x-2y$ 를 얻을 수 있다. 

## Transpose of Linear Map

!!! def "정리 2.25"

    $\mathbf{F}$-벡터공간 $\mathbf{V}$ 와 $\mathbf{W}$ 의 각각의 순서기저 $\beta , \gamma$ 와 선형변환 $\mathbf{T}: \mathbf{V}\to \mathbf{W}$ 에 대하여 다음을 만족하는 함수 $\mathbf{T}^{t}: \mathbf{W}{}^{*}\to \mathbf{V}{}^{*}$ 를 가정하자.

    $$ \forall \mathbf{g}_{} \in \mathbf{W}{}^{*} : \mathbf{T}^{t}(\mathbf{g}_{}) = \mathbf{g}_{}\mathbf{T} $$

    함수 $\mathbf{T}^{t}$ 는 선형변환이고, $[\mathbf{T}^{t}]^{\beta {}^{*}}_{\gamma {}^{*}} = ([\mathbf{T}]^{\gamma}_{\beta} )^{t}$ 를 만족한다.

- [정리 2.20](#48fa4f52a) 은 선형변환 $\mathbf{T}$ 에 대응하는 행렬 $A = [\mathbf{T}]^{\gamma}_{\beta}$ 가 존재함을 말해준다. 이 정리는 $A ^{t}$ 에 대응하는 선형변환이 무엇인지 알려준다. 

- 증명

    $\mathbf{g}_{}\in \mathbf{W}{}^{*}$ 는 $\mathbf{W}\to \mathbf{F}$ 에서 정의된 선형변환이다. 따라서 $\mathbf{T}^{t}(\mathbf{g}_{})=\mathbf{g}_{}\mathbf{T}:\mathbf{V}\to \mathbf{F}$ 는 $\mathbf{V}$ 의 선형범함수이다. 그러므로  $\mathbf{g}_{}\mathbf{T}\in \mathbf{V}{}^{*}$ 이다. 따라서 $\mathbf{T}^{t}$ 는 $\mathbf{W}{}^{*}\to \mathbf{T}{}^{*}$ 에서 정의된 함수이다. ▲ 

    이제 $\mathbf{T}^{t}$ 가 선형인지 확인하자. 먼저 $\mathbf{T}^{t}$ 의 정의에 의하여 다음이 성립한다.
    
    $$ \mathbf{T}^{t}(c \mathbf{g}_{1} + \mathbf{g}_{2})= (c \mathbf{g}_{1} + \mathbf{g}_{2}) \circ \mathbf{T} $$

    그러면 $\mathbf{g}_{1}, \mathbf{g}_{2}\in \mathbf{W}{}^{*}$ 에 대하여 [함수의 합과 스칼라 곱의 정의](#63a07e35d)에 의하여 다음이 성립한다.

    $$ \begin{equation}\begin{split} (c \mathbf{g}_{1} + \mathbf{g}_{2}) \circ \mathbf{T}(x) &= (c \mathbf{g}_{1} + \mathbf{g}_{2}) (\mathbf{T}(x)) \\ &= (c \mathbf{g}_{1})(\mathbf{T}(x)) + (\mathbf{g}_{2}) (\mathbf{T}(x)) \\ &= c (\mathbf{g}_{1})(\mathbf{T}(x)) + (\mathbf{g}_{2}) (\mathbf{T}(x)) \\ &= c (\mathbf{g}_{1} \mathbf{T})(x) + (\mathbf{g}_{2}\mathbf{T})(x) \\ &= c (\mathbf{T}^{t}(\mathbf{g}_{1})) (x) + (\mathbf{T}^{t}(\mathbf{g}_{2}))(x) \\ \end{split}\end{equation} \tag*{} $$

    그러므로 [함수의 합과 스칼라 곱의 정의](#63a07e35d)에 의하여 다음이 성립한다. 따라서 $\mathbf{T}^{t}$ 는 선형이다.

    $$ \mathbf{T}^{t}(c \mathbf{g}_{1} + \mathbf{g}_{2})= (c \mathbf{g}_{1} + \mathbf{g}_{2}) \circ \mathbf{T} = c (\mathbf{T}^{t}(\mathbf{g}_{1}))  + (\mathbf{T}^{t}(\mathbf{g}_{2})) \tag*{▲} $$

    순서기저를 $\beta = \{x_1, x_2, \dots, x_n \}$, $\gamma = \{y_1, y_2, \dots, y_m\}$ 으로 두고 각각의 쌍대기저를 $\beta {}^{*} = \{\mathbf{f}_{1}, \mathbf{f}_{2}, \dots, \mathbf{f}_{n}\}, \gamma {}^{*}= \{\mathbf{g}_{1}, \mathbf{g}_{2}, \dots, \mathbf{g}_{m}\}$ 로 두고 $A = [\mathbf{T}]^{\gamma}_{\beta}$ 로 두자. [선형변환의 행렬표현](#c16bc5e5b)을 구하기 위하여 $[\mathbf{T}^{t}]^{\beta {}^{*}}_{\gamma {}^{*}}$ 의 $j$ 열을 구하기 위해 $\mathbf{T}^{t}(\mathbf{g}_{j})$ 를 $\beta {}^{*}$ 의 일차결합으로 나타내자. $\mathbf{g}_{j}\mathbf{T}: \mathbf{V}\to \mathbf{F}\in \mathbf{V}{}^{*}$ 이므로 [정리 2.24](#f818af77d) 에 의하여 다음이 성립한다.

    $$ \mathbf{T}^{t}(\mathbf{g}_{j}) = \mathbf{g}_{j}\mathbf{T} = \sum_{s=1}^{n}(\mathbf{g}_{j}\mathbf{T})(x_s)\mathbf{f}_{s} $$

    $[\mathbf{T}^{t}]^{\beta {}^{*}}_{\gamma {}^{*}}$ 의 $j$ 열은 $[\mathbf{T}^{t}(\mathbf{g}_{j})]_{\beta {}^{*}}$ 이다. 따라서 $i$행 $j$열의 성분은 $s = i$ 일 때 $\beta {}^{*}$ 의 $i$번째 순서기저 $\mathbf{f}_{i}$ 를 제외한 스칼라 $(\mathbf{g}_{j}\mathbf{T})(x_i)$ 이다. 이때 [선형변환의 행렬표현](#c16bc5e5b) 에 의하여 다음이 성립한다.

    $$ \begin{equation}\begin{split} (\mathbf{g}_{j}\mathbf{T})(x_i) = \mathbf{g}_{j}(\mathbf{T}(x_i))&=\mathbf{g}_{j}\bigg (\sum_{k=1}^{m}A _{ki}y _{k} \bigg ) \\ &= \sum_{k=1}^{m}A _{ki}\mathbf{g}_{j}(y_k) = \sum_{k=1}^{m}A _{ki}\delta _{jk}=A _{ji} \\ \end{split}\end{equation} \tag*{} $$

    따라서 $[\mathbf{T}^{t}]^{\beta {}^{*}}_{\gamma {}^{*}} = A ^{t}$ 이다. ■ 

!!! def "선형변환의 전치(transpose of linear map)"

    $\mathbf{F}$-벡터공간 $\mathbf{V}$ 와 $\mathbf{W}$ 의 각각의 순서기저 $\beta , \gamma$ 와 선형변환 $\mathbf{T}: \mathbf{V}\to \mathbf{W}$ 에 대하여 다음을 만족하는 선형변환 $\mathbf{T}^{t}: \mathbf{W}{}^{*}\to \mathbf{V}{}^{*}$ 를 $\mathbf{T}$ 의 전치라 한다.

    $$ \forall \mathbf{g}_{} \in \mathbf{W}{}^{*} : \mathbf{T}^{t}(\mathbf{g}_{}) = \mathbf{g}_{}\mathbf{T} $$

- 이렇게 정의한 $\mathbf{T}^{t}$ 가 $([\mathbf{T}]^{\gamma}_{\beta} )^{t} = [\mathbf{T}^{t}]^{\beta {}^{*}}_{\gamma {}^{*}}$ 를 만족하기 때문에 선형변환의 전치라고 부른다.

- 예시

    선형변환 $\mathbf{T}: \mathbf{P}_{1}(\R)\to \R ^{2}$ 를 $\mathbf{T}(p(x)) = (p(0), p(2))$ 로 정의하자. $\mathbf{P}_{1}(\R)$ 의 표준순서기저 $\beta$ 와 $\R ^{2}$ 의 표준순서기저 $\gamma$ 에 대하여 $[\mathbf{T}]^{\gamma}_{\beta} =\begin{pmatrix} 1&0\\ 1&2\\ \end{pmatrix}$ 이다. 이제 $[\mathbf{T}^{t}]^{\beta^{*}}_{\gamma^{*}}$ 를 구해보자. 

    $\beta {}^{*}=\{\mathbf{f}_{1},\mathbf{f}_{2}\}$ 와 $\gamma {}^{*}=\{\mathbf{g}_{1}, \mathbf{g}_{2}\}$ 에 대하여 $[\mathbf{T}^{t}]^{\beta^{*}}_{\gamma^{*}} = \begin{pmatrix} a&b\\ c&d\\ \end{pmatrix}$ 로 두면 [선형변환의 행렬표현](#c16bc5e5b)에 의하여 다음이 성립한다. 
    
    $$\mathbf{T}^{t}(\mathbf{g}_{1}) = a \mathbf{f}_{1} + c \mathbf{f}_{2}$$
    
    $$\mathbf{T}^{t}(\mathbf{g}_{2}) = b \mathbf{f}_{1} + d \mathbf{f}_{2}$$
    
    $\beta = \{1, x\}$ 이므로 $\mathbf{f}_{1}(1) = 1, \mathbf{f}_{2}(1) = 0, \mathbf{f}_{1}(x) = 0, \mathbf{f}_{2}(x) = 1$ 이다. 따라서 다음이 성립한다.

    $$ \mathbf{T}^{t}(\mathbf{g}_{1})(1) = (a \mathbf{f}_{1}+ c \mathbf{f}_{2})(1) = a \mathbf{f}_{1}(1) + c \mathbf{f}_{2}(1) = a \cdot 1  + c \cdot 0 = a $$

    또한 $\gamma = \{(1, 0), (0, 1)\}$ 이므로 $\mathbf{g}_{1}(1, 0) = 1 \mathbf{g}_{2}(1, 0) = 0, \mathbf{g}_{1}(0, 1) = 0, \mathbf{g}_{2}(0, 1) = 1$ 이다. 따라서 다음이 성립한다.

    $$ (\mathbf{T}^{t}(\mathbf{g}_{1}))(1) = \mathbf{g}_{1}(\mathbf{T}(1)) = \mathbf{g}_{1}(1,1) = \mathbf{g}_{1}(e_1) + \mathbf{g}_{1}(e_2) = 1 $$

    즉, $a = 1$ 이다. 같은 논리로 $c = 0, b = 1, d = 2$ 를 얻는다. 결국 $[\mathbf{T}^{t}]^{\beta {}^{*}}_{\gamma {}^{*}} = \begin{pmatrix} 1&1\\ 0&2\\ \end{pmatrix} = ([\mathbf{T}]^{\gamma}_{\beta} )^{t}$ 를 직접 계산으로 확인하였다. 이는 본 정리와 같은 결과이다.

!!! def "정리 2.25 보조정리"

    유한차원 벡터공간 $\mathbf{V}$ 와 벡터 $x \in \mathbf{V}$ 와 $\mathbf{f}_{}\in \mathbf{V}{}^{*}$ 에 대하여 함수 $\hat{x}: \mathbf{V}{}^{*}\to \mathbf{F}$ 를 $\hat{x}(\mathbf{f}_{}) = \mathbf{f}_{}(x)$ 라 정의하면 다음이 성립한다.

    $$ \hat{x}(\mathbf{f}_{}) = 0 \implies x = 0 $$

- $\hat{x}$ 이 $\mathbf{V}^{*}$ 의 선형범함수라는 것은 쉽게 확인할 수 있다. 즉, $\hat{x} \in \mathbf{V}{}^{*}{}^{*}$ 이다.

- 증명

    대우명제 $x \neq 0 \implies \hat{x}(\mathbf{f}_{}) = 0$ 를 보여도 된다. 즉, $x \neq 0$ 일 때 $\hat{x}(\mathbf{f}_{}) \neq 0$ 인 $\mathbf{f}_{}\in \mathbf{V}{}^{*}$ 가 존재함을 보이면 된다. 

    $x_1 = x$ 인 $\mathbf{V}$ 의 순서기저 $\beta = \{x_1, x_2, \dots, x_n \}$ 가 존재한다. [정리 2.24](#f818af77d) 는 기저 $\beta$ 에 따른 쌍대기저 $\beta {}^{*} = \{\mathbf{f}_{1}, \mathbf{f}_{2}, \dots, \mathbf{f}_{n}\}$ 의 존재를 보장해준다. $\mathbf{f}_{1}(x_1) = \delta _{11} = 1 \neq 0$ 이다. $\mathbf{f}_{1} = \mathbf{f}_{}$ 로 두면 증명이 끝난다. ■ 

    - *$x_1 = x$ 인 순서기저 $\beta$ 의 존재성을 보장하는 정리가 존재하지 않는다. 증명을 보완해야 함. 하지만 not now..*

!!! def "정리 2.26"

    유한차원 벡터공간 $\mathbf{V}$ 와 $x \in \mathbf{V}$ 와 $\mathbf{f}_{}\in \mathbf{V}{}^{*}$ 에 대한 함수 $\hat{x}: \mathbf{V}{}^{*}\to \mathbf{F}, \mathbf{f}_{} \to \mathbf{f}_{}(x)$ 에 대하여 함수 $\psi : \mathbf{V}\to \mathbf{V}{}^{*}{}^{*}$ 를 $\psi (x) = \hat{x}$ 으로 정의하면 $\psi$ 는 동형사상이다.

- 이 정리가 보여주는 $x$ 와 $\hat{x}$ 사이의 대응으로 유한차원 벡터공간 $\mathbf{V}$ 와 이중 쌍대공간 $\mathbf{V}^{**}$ 을 동일화하는 방법을 찾을 수 있다. 이는 두 벡터공간의 기저와 관계없이 $\mathbf{V}$ 와 $\mathbf{V}^{**}$ 사이의 동형사상이 존재함을 뜻한다.

- 증명

    $x, y \in \mathbf{V}, c \in \mathbf{F}$ 와 임의의 $\mathbf{f}_{}\in \mathbf{V}{}^{*}$ 에 대하여 [함수의 합의 정의](#63a07e35d) 에 의하여 다음이 성립한다. 

    $$ \begin{equation}\begin{split}
    \psi (cx+y)(\mathbf{f}_{})&= \mathbf{f}_{}(cx+y) = c \mathbf{f}_{}(x) + \mathbf{f}_{}(y) = c \hat{x}(\mathbf{f}_{})+ \hat{y}(\mathbf{f}_{}) \\
    &= (c \hat{x}+ \hat{y})(\mathbf{f}_{})\\
    \end{split}\end{equation} \tag*{}
    $$

    즉, $\psi (cx + y) = c \hat{x} + \hat{y} = c \psi (x) + \psi (y)$ 이다. 따라서 $\psi$ 는 선형이다. ▲ 

    $x \in \mathbf{V}$ 에 대하여 $\psi (x) \in \mathbf{V}{}^{*}{}^{*}$ 를 $\mathbf{V}{}^{*}\to \mathbf{F}, \hat{x}(\mathbf{f}_{}) \mapsto 0$ 으로 두자. 그러면 임의의 $\mathbf{f}_{}\in \mathbf{V}{}^{*}$ 에 대하여 $\hat{x}(\mathbf{f}_{}) = 0$ 이다. 정리 2.25 보조정리에 의하여 $x = 0$ 를 얻는다. 이는 $\mathbf{N} (\psi ) = \{0\}$ 을 뜻한다. [정리 2.4](#7d40e8276) 에 의하여 $\psi$ 는 단사이다. ▲ 

    $\psi$ 가 단사이므로 [정리 2.5](#dfd4ff297) 에 의하여 [$\psi$ 는 가역](#373708dc7)이다. 또한 [$\dim (\mathbf{V}) = \dim (\mathbf{V}{}^{*}{}^{*})$ 이므로](#f61ee38ab) $\psi$ 는 동형사상이다. ■ 

!!! def ""

    유한차원 벡터공간 $\mathbf{V}, \mathbf{W}$ 에 대하여 동형사상 $\psi_1 : \mathbf{V}\to \mathbf{V}{}^{*}{}^{*}, x \mapsto \hat{x}$ 과 동형사상 $\psi _2: \mathbf{W}\to \mathbf{W}{}^{*}{}^{*}, x \mapsto \hat{x}$ 을 정의하고, $\mathbf{T}: \mathbf{V}\to \mathbf{W}$ 가 선형일 때 $\mathbf{T}^{tt}=(\mathbf{T}^{t})^{t}$ 라 정의하면 다음과 같이 $\psi _2 \mathbf{T}= \mathbf{T}^{tt}\psi _1$ 가 성립한다.

    $$ \begin{CD} \mathbf{V} @> \mathbf{T}  >> \mathbf{W}  \\ @V \psi _{1} VV @VV \psi _{2} V \\ \mathbf{V} {}^{*}{}^{*} @> \mathbf{T}^{tt} >> \mathbf{W}{}^{*}{}^{*} \end{CD} $$

- 동형사상 $\psi _1, \psi _2$ 는 정리 2.26 과 같이 정의된 것이다.

- 증명

!!! def "정리 2.26 따름정리"

    유한차원 벡터공간 $\mathbf{V}$ 와 쌍대공간 $\mathbf{V}^{*}$ 에 대하여 $\mathbf{V}^{*}$ 의 모든 순서기저는 $\mathbf{V}$ 의 어떤 기저의 쌍대기저이다.

- 증명

    먼저 $x \in \mathbf{V}$ 와 $\mathbf{f}_{}\in \mathbf{V}{}^{*}$ 에 대한 함수 $\hat{x}: \mathbf{V}{}^{*}\to \mathbf{F}, \mathbf{f}_{} \to \mathbf{f}_{}(x)$ 를 정의하자. $\mathbf{V}^{*}$ 의 순서기저를 $\{\mathbf{f}_{1}, \mathbf{f}_{2}, \dots, \mathbf{f}_{n}\}$ 으로 두자. 
    
    [정리 2.24](#f818af77d) 와 정리 2.26 에 의하여 $\mathbf{V}^{*}$ 의 기저와 $i, j \in \{1, \dots, n\}$ 에 대하여 $\delta _{ij} = \hat{x_i}(\mathbf{f}_{i}) = \mathbf{f}_{j}(x_i)$ 인 쌍대기저 $\{\hat{x}_1, \hat{x}_2, \dots, \hat{x}_n\} \subset \mathbf{V}{}^{*}{}^{*}$ 가 존재한다. [쌍대기저의 정의](#3184d9033) 에 의하여 $\{\mathbf{f}_{1}, \mathbf{f}_{2}, \dots, \mathbf{f}_{n}\}$ 는 $\{x_1, x_2, \dots, x_n\}$ 의 쌍대기저이다. ■ 

<!-- # Homogeneous Linear Differential Equations with Constant Coefficients

!!! def "선형 미분방정식(linear differential equation)"

    $t$ 에 대한 함수 $a_1, a_2, \dots, a_n$ 와 $f$, 그리고 $y$ 의 $k$계도함수 $y ^{(k)}$ 에 대하여 다음 형태의 미분방정식을 선형(linear)라 한다.

    $$ a_ny ^{(n)} +a _{n-1} y ^{(n-1)} +\dots+a_1y ^{(1)} +a_0y = f \tag{2.4}  $$

- 함수 $a_i$ 는 미분방정식 $(2.4)$ 의 계수(coefficient)이다. 함수 $f$ 가 영함수이면 동차 선형 미분방정식이고, $a_1, a_2, \dots, a_n$ 들이 상수이면 상수 계수를 갖는 동차 선형미분방정식이다. 여기에서는 미분방정식을 깊게 다루지 말고, 상수 계수를 갖는 동차 선형미분방정식을 선형대수학으로 푸는 방법만을 다뤄보자.

- $a_n \neq 0$ 이면 $(2.4)$ 를 $n$계(order) 미분방정식이라 한다. 이 경우 양변을 $a_n$ 으로 나누어도 상관없으므로 $b_i = a_i/a_n$ 에 대하여 주로 다음 형태의 미분방정식을 다루는 것이 편하다.

    $$ y ^{(n)} +b _{n-1} y ^{(n-1)} +\dots+b_1y ^{(1)} +b_0y = 0   $$

- 미분방정식의 해는 $t$ 에 대한 영함수를 만드는 함수 $y = y(t)$ 이다.

    - 예시

        상수 $\frac{k}{m}$ 에 대하여 다음 미분방정식은 계수가 상수이고 함수 $f$ 가 영함수인 동차 선형 미분방정식이다.

        $$ y'' + \frac{k}{m} y = 0 $$

        함수 $y(t) = \sin \sqrt[]{\frac{k}{m}}t$ 를 미분방정식에 대입하면 다음이 성립한다.

        $$ y''(t) + \frac{k}{m}y(t) = - \frac{k}{m}\sin \sqrt[]{\frac{k}{m}}t + \frac{k}{m}\sin \sqrt[]{\frac{k}{m}}t = 0 $$

        하지만 $y(t) = t$ 를 대입하면 다음이 성립하고, 이는 영함수가 아니므로 $y(t) = t$ 는 해가 아니다. 

        $$ y''(t) + \frac{k}{m}y(t) = \frac{k}{m}t $$

!!! def ""

    함수공간 $\mathcal{F}(\R, \mathbb{C})$ 에 대한 실변수 $t$ 에 대한 복소함수 $x \in \mathcal{F}(\R, \mathbb{C})$ 에 대하여 다음을 만족하는 실함수 $x_1, x_2$ 가 유일하게 존재한다.

    $$ t \in \R : x(t) = x_1(t) + ix_2(t) $$

- $x_1$ 과 $x_2$ 를 각각 실변수 복소함수 $x:\R \to \mathbb{C}$ 의 실수부, 허수부라고 한다.

- 미분방정식을 다룰 때 방정식이 물리적으로 의미를 가지면 실함수라고 하더라도 복소함수로 다루면 편하다.

- 증명

!!! def "실변수 복소함수의 미분가능(differentiable)과 도함수(derivative)"

    실수부가 $x_1$, 허수부가 $x_2$ 인 실변수 복소함수 $x \in \mathcal{F}(\R, \mathbb{C})$ 가 미분가능하다는 것과 $x_1, x_2$ 가 미분가능하다는 것은 동치이다.

    미분가능한 실변수 복소함수 $x$ 의 도함수(derivative) $x'$ 는 다음과 같다. 

    $$ x' = x'_1 + ix'_2 $$

- 예시 

    $x(t) = \cos 2t + i \sin 2t$ 의 도함수는 $x'(t) = -2 \sin 2t + 2i \cos 2t$ 이다.

!!! def "정리 2.27"

    계수가 상수인 동차 선형 미분방정식의 해는 무한히 미분가능하다. 즉, $x$ 가 방정식의 해이면 $k \in \N$ 에 대한 $x ^{(k)}$ 가 존재한다.

- 이 정리는 $\mathcal{F}(\R, \mathbb{C})$ 보다 훨씬 작은 벡터공간을 조사해도 충분하다는 것을 말해준다.

- 증명

- 이 정리의 증명과정은 다음 예시에서 보여주는 귀납법과 비슷하다. 그러나 여기에서는 선형대수학이라는 논의 주제를 너무 벗어나므로 생략하자.

- 예시

    방정식 $y ^{(2)}+4y=0$ 에서 함수 $y$ 가 해이면 $y ^{(2)} = -4y$ 이다. 즉, $y$ 는 두번 미분가능해야 한다. $y ^{(2)}$ 가 두번 미분가능한 함수 $y$ 의 상수배이므로 $y ^{(2)}$ 는 두 번 이상 미분가능하고 $y ^{(4)}$ 가 존재한다. 즉, $y ^{(4)} = -4y ^{(2)}$ 이다. 그러면 같은 논리로 $y ^{(6)}$ 도 존재하고 무한히 미분가능하다는 것을 알 수 있다.  -->