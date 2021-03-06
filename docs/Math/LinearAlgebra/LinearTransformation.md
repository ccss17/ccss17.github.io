!!! info "ref"

    [프리드버그 선형대수학](https://book.naver.com/bookdb/book_detail.nhn?bid=16374070) 

# 선형변환

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

    항등변환(identity transformation) : $\mathbf{F}$-벡터공간 $\mathbf{V}$ 에 대하여 $\mathbf{I} _{\mathbf{V} }: \mathbf{V} \to \mathbf{V}, x \mapsto x$ 로 정의된 선형변환이다.

- 항등변환 $\mathbf{I} _{\mathbf{V} }$ 을 편의상 $\mathbf{I}$ 라 표기하기도 한다.
    
!!! tldr ""

    영변환(zero transformation) : $\mathbf{F}$-벡터공간 $\mathbf{V} , \mathbf{W}$ 에 대하여 $\mathbf{T} _{ 0}: \mathbf{V} \to \mathbf{W}, x \mapsto 0$ 로 정의된 선형변환이다.

# 영공간, 상공간

!!! tldr ""

    영공간(null space, kernel) : 벡터공간 $\mathbf{V}, \mathbf{W}$ 와 선형변환 $\mathbf{T}: \mathbf{V} \to \mathbf{W}$ 에 대하여 영공간은 집합 
    
    $$ \mathbf{N}(\mathbf{T}) = \{x \in \mathbf{V} : \mathbf{T}(x) = 0\}$$
    
    이다.

- 선형변환 $\mathbf{T}: \mathbf{V} \to \mathbf{W}$ 의 영공간을 $\mathbf{N}(\mathbf{T})$ 또는 $\text{Null}(\mathbf{T})$ 또는 $\text{ker}(\mathbf{T})$ 로 표기한다.

- 예시 

    항등변환 $\mathbf{I} : \mathbf{V} \to \mathbf{V}$ 에 대하여 $\mathbf{N}(\mathbf{I}) = \{0\}$ 이다.

    영변환 $\mathbf{T}_0 : \mathbf{V} \to \mathbf{W}$ 에 대하여 $\mathbf{N}(\mathbf{T}_0) = \mathbf{V}$ 이다.

!!! tldr ""

    상공간(range, image) : 벡터공간 $\mathbf{V}, \mathbf{W}$ 와 선형변환 $\mathbf{T}: \mathbf{V} \to \mathbf{W}$ 에 대하여 상공간은 집합 
    
    $$ \mathbf{R}(\mathbf{T}) = \{\mathbf{T}(x) \in \mathbf{W} : x \in \mathbf{V} \}$$
    
    이다.

- 선형변환 $\mathbf{T}: \mathbf{V} \to \mathbf{W}$ 의 상공간을 $\mathbf{R}(\mathbf{T})$ 또는 $\text{ran}(\mathbf{T})$ 으로 표기한다.

- 예시 

    항등변환 $\mathbf{I} : \mathbf{V} \to \mathbf{V}$ 에 대하여 $\mathbf{R}(\mathbf{I}) = \mathbf{V}$ 이다.

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

!!! tldr "정리 2.3"

    차원정리(dimension theorem) : 벡터공간 $\mathbf{V} , \mathbf{W}$ 와 선형변환 $\mathbf{T}: \mathbf{V} \to \mathbf{W}$ 에 대하여 $\mathbf{V}$ 가 유한차원이면 

    $$ \text{nullity}(\mathbf{T})+\text{rank}(\mathbf{T})= \dim(\mathbf{V} ) $$

    이다.

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

!!! tldr "정리 2.4"

    벡터공간 $\mathbf{V} , \mathbf{W}$ 와 선형변환 $\mathbf{T} : \mathbf{V} \to \mathbf{W}$ 에 대하여 다음은 동치이다. 

    1. $\mathbf{T}$ 가 단사사상이다.

    2. $\mathbf{N}(\mathbf{T} ) = \{0\}$

- 증명

    $x \in \mathbf{N}(\mathbf{T} )$ 이면 $\mathbf{T} (x) = 0 = \mathbf{T} (0)$ 인데, $\mathbf{T}$ 가 [단사](../../Foundations/Set/#b9a0b7bf1)이므로 $x = 0$ 이다. 또한 이는 $\forall x \in \mathbf{N}(\mathbf{T} ) : x = 0$ 을 의미하므로 $\mathbf{N}(\mathbf{T} ) = \{0\}$ 이다. ▲ 

    역으로 $\mathbf{N}(\mathbf{T} ) = \{0\}$ 과 $\mathbf{T} (x) = \mathbf{T} (y)$ 을 가정하자. [선형변환의 성질 3)](#2dff80fb4) 에 의하여 $0 = \mathbf{T} (x) - \mathbf{T} (y) = \mathbf{T} (x - y)$ 이므로 

    $$ x - y \in \mathbf{N}(\mathbf{T} ) = \{0\} \iff x - y = 0 $$

    이다. 즉, $x = y$ 이므로 $\mathbf{T}$ 는 단사함수이다. ■ 

!!! tldr "정리 2.5"

    유한차원 벡터공간 $\mathbf{V} ,\mathbf{W}$ 에 대하여 $\dim(\mathbf{V} ) = \dim(\mathbf{W} )$ 이면 선형변환 $\mathbf{T} : \mathbf{V} \to \mathbf{W}$ 에 대하여 다음 명제가 동치이다. 

    1. $\mathbf{T}$ 는 단사이다.

    2. $\mathbf{T}$ 는 전사이다.

    3. $\text{rank}(\mathbf{T} ) = \dim(\mathbf{V} )$

- 이 정리는 차원이 같은 유한차원 사이의 선형사상이 단사이면 전단사임을 말해준다. 그러나 무한차원 $\mathbf{V}$ 에 대한 선형사상 $\mathbf{T} : \mathbf{V} \to \mathbf{V}$ 에 대해서는 단사와 전사가 동치가 아니다.

- 증명 

    [차원정리](#b9412bb64) 에 의하여 $\text{rank}(\mathbf{T} )+\text{nullity}(\mathbf{T} ) = \dim(\mathbf{V} )$ 인데, [정리 2.4](#7d40e8276) 에 의하여 

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

!!! tldr ""

    벡터공간 $\mathbf{V} ,\mathbf{W}$ 의 선형변환 $\mathbf{T} : \mathbf{V} \to \mathbf{W}$ 과 $\mathbf{V}$ 의 부분집합 $S$ 에 대하여 다음이 동치이다.
    
    1. $S$ 가 일차독립이다.

    2. $\mathbf{T} (S)$ 가 일차독립이다.

- 증명

- 예시 

    선형변환 $\mathbf{T} : \mathbf{P} _2(\R) \to \R ^{3}$ 이 

    $$ \mathbf{T} (a_0+a_1x+a_2x ^{2}) = (a_0, a_1, a_2) $$

    와 같이 정의되면 $\mathbf{T}$ 는 단사이다. $S = \{2-x+3x ^{2}, x+x ^{2}, 1-2x ^{2}\}$ 라고 하면 $\mathbf{T} (S) = \{(2,-1,3), (0,1,1), (1,0,-2)\}$ 가 $\R ^{3}$ 에서 일차독립이므로 $S$ 도 일차독립이다.

!!! tldr "정리 2.6"

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

!!! tldr "정리 2.6 따름정리"

    벡터공간 $\mathbf{V} , \mathbf{W}$ 에 대하여 $\mathbf{V}$ 가 유한집합 기저 $\{v_1, \dots, v_n\}$ 을 가지면 두 선형변환 $\mathbf{U} , \mathbf{T} : \mathbf{V} \to \mathbf{W}$ 에 대하여 

    $$ i \in \{1, \dots, n\} : \mathbf{U} (v_i) = \mathbf{T} (v_i) \implies \mathbf{U} = \mathbf{T}  $$

    이다.

- 이 정리는 두 선형변환이 기저에서 상이 같으면 같은 선형변홤임을 말하고 있다.

- 예시

    선형변환 $\mathbf{T} :\R ^{2} \to \R ^{2}$ 이 

    $$ \mathbf{T} (a_1, a_2) = (2a_2 - a_1, 3a_1) $$

    와 같이 정의되었다고 하자. 그러면 $\{(1,2), (1,1)\}$ 이 $\R ^{2}$ 의 기저이므로 선형변환 $\mathbf{U} : \R ^{2} \to \R ^{2}$ 이 $\mathbf{U} (1,2)=(3,3), \mathbf{U} (1,1)=(1,3)$ 이면 $\mathbf{U} =\mathbf{T}$ 이다.
    
# 선형변환의 행렬표현

이 절에서는 선형변환과 행렬이 일대일 대응됨을 알아본다.

!!! tldr ""

    순서기저(ordered basis) : 유한차원 벡터공간의 순서가 주어진 기저이다.

- 즉, 순서기저란 일차독립이고 벡터공간을 생성하는 수열이다.

- 예시 

    $\mathbf{F} ^{3}$ 에서 $\beta = \{e_1, e_2, e_3\}, \gamma = \{e_2, e_1, e_3\}$ 은 순서기저이다. 순서기저의 관점에서 $\beta \neq \gamma$ 이다.

- 표준기저와 마찬가지로 표준순서기저(standard ordered basis)도 정의할 수 있다.

    - 예시 
    
        벡터공간 $\mathbf{F} ^{n}$ 에서 $\{e_1, e_2, \dots, e_n\}$ 을 표준순서기저라고 한다.

        벡터공간 $\mathbf{P}_n(\mathbf{F} )$ 에서 $\{1, x, \dots, x ^{n}\}$ 이 표준순서기자이다.

!!! tldr ""

    좌표벡터(coordinate vector) : 유한차원 벡터공간 $\mathbf{V}$ 의 순서기저 $\beta = \{u_1, u_2, \dots, u_n\}$ 와 벡터 $x \in \mathbf{V}$ 에 대하여 $x = \displaystyle  \sum_{i=1}^{n}a_iu_i$ 을 만족하는 유일한 스칼라 $a_1, a_2, \dots, a_n$ 가 존재한다. 이때 $\beta$ 에 대한 $x$ 의 좌표벡터 $[x] _{\beta }$ 를 

    $$ [x] _{\beta } = \begin{pmatrix}
    a_1\\
    a_2\\
    \vdots\\
    a_n
    \end{pmatrix}
    $$

    와 같이 정의한다.

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

!!! tldr ""

    선형변환의 행렬표현(matrix representation) : 유한차원 벡터공간 $\mathbf{V} , \mathbf{W}$ 의 각각의 순서기저 $\beta = \{v_1, \dots, v_n\}, \gamma = \{w_1, \dots, w_m\}$ 에 대하여 선형변환 $\mathbf{T} : \mathbf{V} \to \mathbf{W}$ 을 정의하면 

    $$ \mathbf{T} (v_j) = \sum_{i=1}^{m}a _{ij}w_i \qquad j \in \{1,\dots,n\}, i \in \{1, \dots, m\} $$

    을 만족하는 유일한 스칼라 $a _{ij}\in \mathbf{F}$ 가 존재하는데, 이때 성분이 $A _{ij} = a _{ij}$ 인 $m \times n$ 행렬 $A$ 를 순서기저 $\beta , \gamma$ 에 대한 선형변환 $\mathbf{T}$ 의 행렬표현

    $$ \boxed{A = [\mathbf{T} ] ^{\gamma } _{\beta } }$$ 

    라 한다.

- 우리는 이렇게 행렬과 선형변환을 연결했는데, [정리 2.8](#aa431d8ac) 은 이 연결이 합과 스칼라 곱을 보존함을 말해준다. 이를 위해 먼저 선형변환의 합과 스칼라 곱을 정의해볼 것이다.

- $\mathbf{V} = \mathbf{W} \land \beta = \gamma$ 이면 간단하게 $A = [\mathbf{T} ]_{\beta }$ 라고 표기한다.

- $A$ 의 $j$ 열은 $[\mathbf{T} (v_j)] _{\gamma }$ 이다.

- 선형변환 $\mathbf{U} : \mathbf{V} \to \mathbf{W}$ 가 $[\mathbf{U} ] ^{\gamma } _{\beta } = [\mathbf{T} ]^{\gamma }_{\beta }$ 를 만족하면 [정리 2.6 따름정리](#759379ac7) 에 의하여 $\mathbf{U} = \mathbf{T}$ 이다.

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

- 예시 

    유한차원 벡터공간 $\mathbf{V} , \mathbf{W}$ 의 순서기저를 $\beta = \{v_1, \dots, v_n\}, \gamma = \{w_1, \dots, w_m\}$ 이라 하면 

    $$ \mathbf{T} _0(v_j) = 0 = 0w_1+\dots+0w_m $$

    이므로 $[\mathbf{T} _0] ^{\gamma } _{\beta } = O$ 이다. $O$ 는 $m \times n$ 영행렬이다.

    또한 

    $$ \mathbf{I} _{\mathbf{V} }(v_j) = v_j = 0v_1 + \dots + 0v _{j-1} + 1v_j+ 0 v _{j+1}  \dots + 0 v_n $$

    이므로 $\mathbf{I} _{\mathbf{V} }$ 의 $j$ 열은 $e_j$ 이다. 따라서 

    $$ [\mathbf{I} _{\mathbf{V} }]_{\beta } = \begin{pmatrix} 1&0&\dots&0\\ 0&1&\dots&0\\ \vdots & \vdots & \ddots & \vdots \\ 0&0&\dots&1\\ \end{pmatrix} $$ 

    이다. $[\mathbf{I} _{\mathbf{V} }]_{\beta }$ 는 $n \times n$ 항등행렬이다.

- 위 예시는 영변환의 행렬표현이 영행렬이고, 항등변환의 행렬표현이 항등행렬임을 말해준다.

!!! tldr "크로네커 델타(Kronecker delta)"

    $$\delta _{ij} = \begin{cases} 1 & i = j\\ 0 & i \neq j\\ \end{cases}$$

- 예시 

    $n \times n$ 항등행렬 $I_n$ 의 성분은 $(I_n) _{ij} = \delta _{ij}$ 이다.

!!! tldr ""

    $\mathbf{F}$-벡터공간 $\mathbf{V} , \mathbf{W}$ 에서 정의된 임의의 함수 $\mathbf{T} , \mathbf{U} : \mathbf{V} \to \mathbf{W}$ 와 $a \in \mathbf{F}$ 와 $\forall x \in \mathbf{V}$ 에 대하여 두 함수의 합과 스칼라곱을 다음과 같이 정의한다.

    - $\mathbf{T} + \mathbf{U} : \mathbf{V} \to \mathbf{W}, (\mathbf{T} + \mathbf{U} )(x) = \mathbf{T} (x) + \mathbf{U} (x)$

    - $a \mathbf{T} : \mathbf{V} \to \mathbf{W}, (a \mathbf{T} )(x) = a \mathbf{T} (x)$

- 이는 함수의 합의 스칼라 곱에 대한 보편적 정의인데 선형변환의 합과 스칼라 곱이 여전히 선형임을 [다음 정리](#91b876399)가 말해준다.

!!! tldr "정리 2.7"

    $\mathbf{F}$-벡터공간 $\mathbf{V} , \mathbf{W}$ 와 선형변환 $\mathbf{T} , \mathbf{U} : \mathbf{V} \to \mathbf{W}$ 에 대하여 다음이 성립한다.

    1. $\forall a \in \mathbf{F}$ 에 대하여 $a \mathbf{T} + \mathbf{U}$ 은 선형이다.

    2. $\mathbf{V} \to \mathbf{W}$ 에서 정의된 모든 선형변환의 집합은 $\mathbf{F}$-벡터공간이다.

- 1) 의 증명

    $x, y \in \mathbf{V} , c \in \mathbf{F}$ 에 대하여 다음이 성립한다. 

    $$ \begin{equation}\begin{split}   (a \mathbf{T} + \mathbf{U} )(cx+y)&=a \mathbf{T} (cx+y) + \mathbf{U} (cx + y)\\ &=a[\mathbf{T} (cx+y)] + c \mathbf{U} (x) + \mathbf{U} (y)\\ &=a[c\mathbf{T} (x) + \mathbf{T}(y)] + c \mathbf{U} (x) + \mathbf{U} (y)\\ &=ac\mathbf{T} (x) + c\mathbf{U}(x) + a \mathbf{T} (y) + \mathbf{U} (y)\\ &=c(a\mathbf{T} + \mathbf{U} ) (x) + (a \mathbf{T} + \mathbf{U} )(y)\\ \end{split}\end{equation}\tag*{} $$

    그러므로 $a \mathbf{T} + \mathbf{U}$ 는 선형이다. ■ 

- 2) 의 증명 

    [위의 정의](#63a07e35d)는 임의의 함수에 대한 두 함수의 합, 스칼라 곱을 정의한 것이므로 선형변환의 합과 스칼라곱에도 적용된다. 그러므로 이 합과 스칼라 곱을 만족하는 선형변환 집합이 [벡터공간의 8 가지 조건](../VectorSpace#e992d1df1)을 만족하는지 확인하면 된다. 

    $\mathbf{V} \to \mathbf{W}$ 에서 정의된 모든 선형변환의 집합을 $\mathcal{L}$ 라고 하자. 그러면 영변환 $\mathbf{L} _0: \mathbf{V} \to \mathbf{W}$ 는 $\mathcal{L}$ 에서 영벡터의 역할을 한다. 또한 $\mathcal{L}$ 가 벡터공간의 8 가지 조건을 만족한다는 것을 쉽게 확인할 수 있다. 

    그러므로 $\mathcal{L}$ 는 $\mathbf{F}$-벡터공간이다. ■ 

!!! tldr ""

    벡터공간 $\mathcal{L}(\mathbf{V} , \mathbf{W} )$ : $\mathbf{F}$-벡터공간 $\mathbf{V} , \mathbf{W}$ 에 대하여 $\mathbf{V} \to \mathbf{W}$ 에서 정의된 모든 선형변환의 집합이다.

- $\mathbf{V} = \mathbf{W}$ 이면 간단하게 $\mathcal{L}(\mathbf{V} )$ 라 표기한다.

- 참고로 2.4 절에서 차원 $\dim(\mathbf{V} ) = n, \dim(\mathbf{W} ) = m$ 인 벡터공간 $\mathbf{V} , \mathbf{W}$ 에 대하여 $\mathcal{L}(\mathbf{V} , \mathbf{W} )$ 와 $\mathbf{M} _{m \times n}(\mathbf{F} )$ 가 본질적으로 같다는 것을 보일 것이다.

!!! tldr "정리 2.8"

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

# 선형변환의 합성과 행렬 곱

!!! tldr "정리 2.9"

    $\mathbf{F}$-벡터공간 $\mathbf{V} ,\mathbf{W} , \mathbf{Z}$ 와 선형변환 $\mathbf{T} : \mathbf{V} \to \mathbf{W} , \mathbf{U} : \mathbf{W} \to \mathbf{Z}$ 에 대하여 두 선형변환의 합성 $\mathbf{U} \mathbf{T} : \mathbf{V} \to \mathbf{Z}$ 는 선형이다.

- 두 선형변환 $\mathbf{U} , \mathbf{T}$ 의 합성 $\mathbf{U} \circ \mathbf{T}$ 을 편의상 $\mathbf{U} \mathbf{T}$ 로 표기하자.

- 증명

    $x, y \in \mathbf{V} , a \in \mathbf{F}$ 에 대하여 

    $$ \begin{equation}\begin{split}   \mathbf{U} \mathbf{T} (ax + y)&= \mathbf{U} (\mathbf{T} (ax +y)) \\ &= \mathbf{U} (a \mathbf{T} (x) + \mathbf{T} (y))\\ &=a \mathbf{U} (\mathbf{T} (x)) + \mathbf{U} (\mathbf{T} (y)) \\ &=a (\mathbf{U} \mathbf{T} )(x) + \mathbf{U} \mathbf{T} (y) \\ \end{split}\end{equation}\tag*{} $$

    이 성립한다. ■ 

!!! tldr "정리 2.10"

    체 $\mathbf{F}$ 에 대한 $\mathbf{F}$-벡터공간 $\mathbf{V}$ 와 선형변환 $\mathbf{T} , \mathbf{U} _1, \mathbf{U} _2 \in \mathcal{L}(\mathbf{V} )$ 에 대하여 다음이 성립한다.

    1. $\mathbf{T} (\mathbf{U} _1 + \mathbf{U} _2) = \mathbf{T} \mathbf{U} _1 + \mathbf{T} \mathbf{U} _2, \enspace  (\mathbf{U} _1 + \mathbf{U} _2)\mathbf{T} = \mathbf{U} _1 \mathbf{T} +\mathbf{U} _2 \mathbf{T}$

    2. $\mathbf{T} (\mathbf{U} _1 \mathbf{U} _2) = (\mathbf{T} \mathbf{U} _1) \mathbf{U} _2$

    3. $\mathbf{T} \mathbf{I} = \mathbf{I} \mathbf{T} = \mathbf{T}$

    4. $\forall a \in \mathbf{F} , a(\mathbf{U} _1 \mathbf{U} _2) = (a \mathbf{U} _1)\mathbf{U} _2 = \mathbf{U} _1(a \mathbf{U} _2)$

- 증명

- 이 정리는 선형변환의 정의역과 공역이 같은 경우를 말하고 있지만, 선형변환의 정의역과 공역이 같지 않으면 더 일반적인 결과가 성립한다. 

    - 증명

!!! tldr ""

    벡터공간 $\mathbf{V}$ 에서 정의된 선형변환 $\mathbf{T} \in \mathcal{L}(\mathbf{V} )$ 와 $k \in \N$ 에 대하여 

    $$ \mathbf{T} ^{k} = \begin{cases} \mathbf{T} ^{k-1} \mathbf{T}  & k \geq 2\\ \mathbf{T}  & k = 1\\ \mathbf{I} _{\mathbf{V} }  & k = 0\\ \end{cases} $$

    라고 정의한다.

- 예시 

    무한번 미분가능한 실함수 집합 $\mathbf{V}$ 에 대하여 $\mathbf{T} : \mathbf{V} \to \mathbf{V}, \mathbf{T} (f) = f'$ 와 같이 정의된 선형변환의 합성을 표현할 때 

    $$ \mathbf{T} \mathbf{T} (f) = \mathbf{T} ^{2} (f) = \mathbf{T} (f') = (f')' = f'' $$

    $$ \mathbf{T} \mathbf{T} \mathbf{T}  (f) = \mathbf{T} ^{3} (f) = \mathbf{T} ^{2} (f') = \mathbf{T}  (f'') = f''' $$

    와 같이 표현한다.

!!! tldr ""

    행렬곱(matrix multiplication, matrix product) : $m \times n$ 행렬 $A$ 와 $n \times p$ 행렬 $B$ 에 대하여 두 행렬 $A, B$ 의 곱 $AB$ 는 $1 \leq i \leq m, 1 \leq j \leq p$ 에 대하여

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

- 지금까지 하고 있는 일은 선형변환과 행렬 간의 대응관계를 연구하는 것이다. 먼저 [선형변환과 행렬의 대응](#9a08985c1)을 살펴보았다. 그리고 [선형변환의 합과 스칼라곱을 정의](#63a07e35d)한 다음 [이 연산이 행렬에서의 합과 스칼라곱의 구조를 보존한다](#aa431d8ac)는 것을 증명했다. 이제 두 선형변환의 합성에 어떤 행렬의 연산이 대응되는지 연구해야 한다. 즉, 행렬곱에 대하여 정의할 차례인 것이다.

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

!!! tldr ""

    $$ (AB) ^{t} = B ^{t} A ^{t} $$

- 증명 

    $$(AB) ^{t} _{ij} = (AB) _{ji} = \sum_{k=1}^{n}A _{jk}B _{ki}$$

    $$(B ^{t} A ^{t}) _{ij} =  \sum_{k=1}^{n}(B ^{t})_{ik}(A ^{t}) _{kj} = \sum_{k=1}^{n}B _{ki}A ss    jkA $$

!!! tldr "정리 2.11"

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

!!! tldr "정리 2.11 따름정리"

    유한차원 벡터공간 $\mathbf{V}$ 와 순서기저 $\beta$ 와 선형연산자 $\mathbf{T} , \mathbf{U} \in \mathcal{L}(\mathbf{V} )$ 에 대하여 다음이 성립한다. 

    $$ [\mathbf{U} \mathbf{T} ] _{\beta } = [\mathbf{U} ] _{\beta }[\mathbf{T} ] _{\beta } $$

> p113. 정리 2.10, 정리 2.16 의 메타데이터

!!! tldr "정리 2.12"

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

!!! tldr "정리 2.12 따름정리"

    $m \times n$ 행렬 $A$ 와 $n \times p$ 행렬 $B_1, B_2, \dots, B_k$ 와 $q \times m$ 행렬 $C_1, C_2, \dots, C_k$ 와 스칼라 $a_1, a_2, \dots, a_k$ 에 대하여 다음이 성립한다. 

    $$ A \bigg (\sum_{i=1}^{k}a_iB_i\bigg ) = \sum_{i=1}^{k}a_iAB_i, \quad \bigg (\sum_{i=1}^{k}a_iC_i\bigg )A = \sum_{i=1}^{k}a_iC_iA $$

- 증명

!!! tldr ""

    $n \times n$ 행렬 $A$ 에 대하여 행렬의 지수를 다음과 같이 정의한다.

    $$ A ^{k} = \begin{cases} A ^{k-1}A & k \geq 2\\ A & k = 1\\ I_n & k = 0\\ \end{cases} $$

!!! tldr ""

    행렬곱에서 소거법칙이 성립하지 않는다.

- 증명

    $A = \begin{pmatrix} 0&0\\ 1&0\\ \end{pmatrix} \implies A \neq O \land A ^{2} = O$ 이다. 이때 소거법칙이 성립한다고 가정하면

    $$ A \cdot A = A ^{2} = O = A \cdot O \implies A = O $$

    이다. 이는 모순이다. ■ 

!!! tldr "정리 2.13"

    $m \times n$ 행렬 $A$ 와 $n \times p$ 행렬 $B$ 와 $j = 1, 2, \dots, p$ 에 대하여 $AB$ 의 $j$ 열을 $u_j$, $B$ 의 $j$ 열을 $v_j$ 이라 하면 다음이 성립한다. 

    1. $u_j = Av_j$

    2. $v_j = Be_j$ (단, $e_j$ 는 $\mathbf{F} ^{p}$ 의 $j$ 번째 표준벡터)

- 1) 의 증명

    $$ u_j = \begin{pmatrix} (AB) _{1j}\\ (AB) _{2j}\\ \vdots \\ (AB) _{mj}\\ \end{pmatrix} = \begin{pmatrix} \sum_{k=1}^{n}A _{1k}B _{kj}\\ \sum_{k=1}^{n}A _{2k}B _{kj}\\ \vdots\\ \sum_{k=1}^{n}A _{mk}B _{kj}\\ \end{pmatrix} = A \begin{pmatrix} B _{1j}\\ B _{2j}\\ \vdots \\ B _{nj}\\ \end{pmatrix} = A v_j $$

- 2) 의 증명

!!! tldr "정리 2.14"

    유한차원 벡터공간 $\mathbf{V} , \mathbf{W}$ 과 각각의 순서기저 $\beta , \gamma$ 에 대한 선형변환 $\mathbf{T} : \mathbf{V} \to \mathbf{W}$ 과 $u \in \mathbf{V}$ 에 대하여 다음이 성립한다. 

    $$ [\mathbf{T} (u)] _{\gamma } = [\mathbf{T} ] ^{\gamma}_{\beta} [u] _{\beta } $$

- 이 정리는 선형변환에 어떤 벡터를 입력하여 행렬로 표현한 것과 선형변환과 벡터를 행렬로 표현한 후 행렬곱 한 것이 같음을 말해준다. 

- 증명

    $u \in \mathbf{V}$ 를 고정하고 다음과 같은 선형변환 $f: F \to \mathbf{V} , g: F \to \mathbf{W}$ 를 정의하자. 

    $$ \forall a \in F : f(a) = au, g(a) = a \mathbf{T} (u) $$

    $F$ 의 표준순서기저를 $\alpha = \{1\}$ 라고 하자. [선형변환의 조건]() 에 의하여 $g(a) = a \mathbf{T} (u) = \mathbf{T} (au) = \mathbf{T} f(a)$ 이므로 $g = \mathbf{T} f$ 이다. 

    행렬의 각 열을 벡터로 보고 [정리 2.11](#2fc8f26aa) 을 적용하면 다음이 성립한다. 

    $$ [\mathbf{T} (u)] _{\gamma } = [g(1)] _{\gamma } = [g] ^{\gamma}_{\alpha }  = [\mathbf{T} f] ^{\gamma}_{\alpha }  = [\mathbf{T} ] ^{\gamma}_{\beta} [f] ^{\beta }_{\alpha } = [\mathbf{T} ] ^{\gamma}_{\beta} [f(1)] _{\beta } = [\mathbf{T} ]^{\gamma}_{\beta} [u] _{\beta } \tag*{■} $$

!!! tldr ""

    좌측 곱 변환(left multiplication transformation) : 체 $\mathbf{F}$ 에서 성분을 가져온 $m \times n$ 행렬 $A$ 에 대하여 선형변환 

    $$ \mathbf{L} _{A} : \mathbf{F} ^{n} \to \mathbf{F} ^{m}, x \mapsto Ax $$

    을 좌측 곱 변환이라 한다.

- $x$ 는 $\mathbf{F} ^{n}$ 의 열벡터이다. 

- 좌측 곱 변환은 선형변환의 성질로 행렬의 성질을 유추하거나, 행렬의 성질로 선형변환의 성질을 유추할 때 유용하게 사용되는 도구이다. 

- 예시 

    $A = \begin{pmatrix} 1&2&1\\ 0&1&2\\ \end{pmatrix}, x= \begin{pmatrix} 1\\ 3\\ -1\\ \end{pmatrix}$ 에 대하여 $\mathbf{L} _A(x) = Ax = \begin{pmatrix} 1&2&1\\ 0&1&2\\ \end{pmatrix}\begin{pmatrix} 1\\ 3\\ -1\\ \end{pmatrix} = \begin{pmatrix} 6\\ 1\\ \end{pmatrix}$ 이다. 

!!! tldr "정리 2.15"

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

- 증명

    [정리 2.12]() 에 의하여 $A(B+C) = AB+AC$ 이다. 이는 $\mathbf{L} _A(x + y) = A(x+y) = Ax + Ay = \mathbf{L} (x) + \mathbf{L} (y)$ 임을 뜻한다. 
    
    또한 [정리 2.12]() 에 의하여 스칼라 $a$ 에 대하여 $A(aB) = a(AB)$ 이다. 이는 $\mathbf{L} _A(cx) = A(cx) = c(Ax) = c\mathbf{L} (x)$ 임을 뜻한다. 그러므로 $\mathbf{L} _A$ 는 선형이다. ▲ 



# 가역성과 동형사상

# 좌표변환 행렬

# 쌍대공간

# 계수가 상수인 동차 선형 미분방정식
