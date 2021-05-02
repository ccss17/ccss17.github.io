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

    항등변환(identity transformation) : $\mathbf{F}$-벡터공간 $\mathbf{V}$ 에 대하여 $\mathbf{I} _{\mathbf{V} }: \mathbf{V} \to \mathbf{V}, x \mapsto x$ 로 정의된 선형변환이다.

- 항등변환 $\mathbf{I} _{\mathbf{V} }$ 을 편의상 $\mathbf{I}$ 라 표기하기도 한다.
    
!!! tldr ""

    영변환(zero transformation) : $\mathbf{F}$-벡터공간 $\mathbf{V} , \mathbf{W}$ 에 대하여 $\mathbf{T} _{ 0}: \mathbf{V} \to \mathbf{W}, x \mapsto 0$ 로 정의된 선형변환이다.

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

!!! tldr ""

    선형변환의 행렬표현(matrix representation) : 유한차원 벡터공간 $\mathbf{V} , \mathbf{W}$ 의 각각의 순서기저 $\beta = \{v_1, \dots, v_n\}, \gamma = \{w_1, \dots, w_m\}$ 에 대하여 선형변환 $\mathbf{T} : \mathbf{V} \to \mathbf{W}$ 을 정의하면 

    $$ \mathbf{T} (v_j) = \sum_{i=1}^{m}a _{ij}w_i \qquad j \in \{1,\dots,n\}, i \in \{1, \dots, m\} $$

    을 만족하는 유일한 스칼라 $a _{ij}\in \mathbf{F}$ 가 존재하는데, 이때 성분이 $A _{ij} = a _{ij}$ 인 $m \times n$ 행렬 $A$ 를 순서기저 $\beta , \gamma$ 에 대한 선형변환 $\mathbf{T}$ 의 행렬표현

    $$ \boxed{A = [\mathbf{T} ] ^{\gamma } _{\beta } }$$ 

    라 한다.

- $\mathbf{V} = \mathbf{W} \land \beta = \gamma$ 이면 간단하게 $A = [\mathbf{T} ]_{\beta }$ 라고 표기한다.

- $A$ 의 $j$ 열은 $[\mathbf{T} (v_j)] _{\gamma }$ 이다.

- 선형변환 $\mathbf{U} : \mathbf{V} \to \mathbf{W}$ 가 $[\mathbf{U} ] ^{\gamma } _{\beta } = [\mathbf{T} ]^{\gamma }_{\beta }$ 를 만족하면 [정리 2.6 따름정리](#759379ac7) 에 의하여 $\mathbf{U} = \mathbf{T}$ 이다.

- 예시 

    선형변환 $\mathbf{T} : \R ^{2} \to \R ^{3} , (a_1, a_2) \mapsto (a_1 + 3a_2, 0, 2a_1 - 4a_2)$ 를 정의하고 $\R ^{2}, \R ^{3}$ 의 순서기저 $\beta , \gamma$ 를 각각의 표준순서기저로 두면 

    $$ \mathbf{T} (1, 0) = (1, 0, 2) = 1e_1 + 0e_2 + 2e_3 $$ 

    $$ \mathbf{T} (0, 1) = (3, 0, -4) = 3e_1 + 0e_2 - 4e_3 $$ 

    가 성립하므로 

    $$ [\mathbf{T} ]^{\gamma } _{\beta } = \begin{pmatrix} 1&3\\ 0&0\\ 2&4\\ \end{pmatrix} $$

    이다. 만약 $\R ^{3}$ 의 순서기저로써 $\gamma ' = \{e_3, e_2, e_1\}$ 를 가져오면 

    $$ [\mathbf{T} ] ^{\gamma '} _{\beta } =\begin{pmatrix} 2&-4\\ 0&0\\ 1&3\\ \end{pmatrix} $$

    이 된다.

- 예시 

    선형변환 $\mathbf{T} : \mathbf{P} _3(\R) \to \mathbf{T} _2(\R)$ 가 $\mathbf{T} (f(x)) = f'(x)$ 와 같이 정의되었고,  $\mathbf{P} _3(\R), \mathbf{P} _2(\R)$ 의 순서기저 $\beta , \gamma$ 를 표준순서기저라 하면 

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

!!! tldr ""

    크로네커 델타(Kronecker delta) : 크로네커 델타는 다음과 같이 정의한다.
    
    $$\delta _{ij} = \begin{cases} 1 & i = j\\ 0 & i \neq j\\ \end{cases}$$

- 예시 

    $n \times n$ 항등행렬 $I_n$ 의 성분은 $(I_n) _{ij} = \delta _{ij}$ 이다.

!!! tldr ""

    $\mathbf{F}$-벡터공간 $\mathbf{V} , \mathbf{W}$ 사이에 정의된 임의의 함수 $\mathbf{T} , \mathbf{U} : \mathbf{V} \to \mathbf{W}$ 와 스칼라 $a \in \mathbf{F}$ 와 $\forall x \in \mathbf{V}$ 에 대하여 두 함수의 합과 스칼라곱을 다음과 같이 정의한다.

    - $\mathbf{T} + \mathbf{U} : \mathbf{V} \to \mathbf{W}$ 의 정의는 다음과 같다. 
    
        $$ (\mathbf{T} + \mathbf{U} )(x) = \mathbf{T} (x) + \mathbf{U} (x)$$

    - $a \mathbf{T} : \mathbf{V} \to \mathbf{W}$ 의 정의는 다음과 같다. 
    
        $$ (a \mathbf{T} )(x) = a \mathbf{T} (x)$$

- 이는 함수의 합의 스칼라 곱에 대한 보편적 정의인데 선형변환의 합과 스칼라 곱이 여전히 선형임을 다음 정리가 말해준다.

!!! tldr "정리 2.7"

    $\mathbf{F}$-벡터공간 $\mathbf{V} , \mathbf{W}$ 와 선형변환 $\mathbf{T} , \mathbf{U} : \mathbf{V} \to \mathbf{W}$ 에 대하여 다음이 성립한다.

    1. $\forall a \in \mathbf{F} ,$


# 선형변환의 합성과 행렬 곱

# 가역성과 동형사상

# 좌표변환 행렬

# 쌍대공간

# 계수가 상수인 동차 선형 미분방정식