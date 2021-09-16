# The Jordan Canonical Form I

!!! def "일반화된 고유벡터(generalized eigenvector)"

    벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 와 스칼라 $\lambda$ 와 어떤 양의 정수 $p$ 에 대하여 $(\mathbf{T}-\lambda \mathbf{I})^{p}(x) = 0$ 을 만족하는 $x \in \mathbf{V}\setminus \{0\}$ 를 고윳값 $\lambda$ 에 대응하는 $\mathbf{T}$ 의 일반화된 고유벡터라 한다.

!!! def "일반화된 고유공간(generalized eigenspace)"

    벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 와 $\mathbf{T}$ 의 고윳값 $\lambda$ 에 대하여 다음 집합을 $\lambda$ 에 대응하는 $\mathbf{T}$ 의 일반화된 고유공간이라 한다.

    $$ \mathbf{K}_{\lambda } = \{x \in \mathbf{V} : \exists p \in \mathbb{Z}^{+} : (\mathbf{T}-\lambda \mathbf{I})^{p}(x) = 0 \} $$

!!! def "정리 7.1"

    벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 와 $\mathbf{T}$ 의 고윳값 $\lambda$ 에 대하여 다음이 성립한다. 

    1. 일반화된 고유공간 $\mathbf{K}_{\lambda}$ 는 고유공간 $\mathbf{E}_{\lambda}$ 를 포함하는 $\mathbf{T}$-불변 부분공간이다.

    2. $\mathbf{T}$ 의 임의의 고윳값 $\mu$ 가 $\mu \neq \lambda$ 이면 $\mathbf{K}_{\lambda} \cap \mathbf{K}_{\mu } = \{0\}$ 이다.

    3. 임의의 스칼라 $\mu \neq \lambda$ 에 대하여 $(\mathbf{T}-\mu \mathbf{I})_{\mathbf{K}_{\lambda}}$ 는 전단사이다.

- 증명

    1:

    $0 \in \mathbf{K}_{\lambda}$ 는 자명하자. 일반화된 고유공간의 정의에 의하여 $x, y \in \mathbf{K}_{\lambda}$ 에 대하여 다음을 만족하는 양의 정수 $p, q$ 가 존재한다. 

    $$ (\mathbf{T}-\lambda \mathbf{I})^{p}(x) = (\mathbf{T}-\lambda \mathbf{I})^{q}(y) = 0 $$

    다음이 성립한다.

    $$ \begin{equation}\begin{split}
    (\mathbf{T}-\lambda \mathbf{I})^{p+q}(x+y)&=(\mathbf{T}-\lambda \mathbf{I})^{p+q}(x) + (\mathbf{T}-\lambda \mathbf{I})^{p+q}(y) \\
    &= (\mathbf{T}-\lambda \mathbf{I})^{q}(0) + (\mathbf{T}-\lambda \mathbf{I})^{p}(0) = 0\\
    \end{split}\end{equation} \tag*{}
    $$

    따라서 $x + y \in \mathbf{K}_{\lambda}$ 이다. 즉, $\mathbf{K}_{\lambda}$ 는 벡터합에 대하여 닫혀있다. $\mathbf{K}_{\lambda}$ 가 스칼라 곱에 대하여 닫혀있음을 보이는 것은 쉽다. 따라서 [정리 1.3](../VectorSpace/#42f9c15c6) 에 의하여 $\mathbf{K}_{\lambda}$ 는 $\mathbf{V}$ 의 부분공간이다. ▲ 

    $x \in \mathbf{K}_{\lambda}$ 에 대하여 $(\mathbf{T}-\lambda \mathbf{I})^{p}(x) = 0$ 인 양의 정수 $p$ 가 존재한다. $\mathbf{T}$ 에 대한 다항식은 $\mathbf{T}$ 와 가환적이다. 즉, $\mathbf{T}(\mathbf{T}-\lambda \mathbf{I})=(\mathbf{T}-\lambda \mathbf{I})\mathbf{T}$ 이므로 다음이 성립한다. 

    $$ (\mathbf{T}-\lambda \mathbf{I})^{p}\mathbf{T}(x) = \mathbf{T}(\mathbf{T}-\lambda \mathbf{I})^{p}(x) = \mathbf{T}(0) = 0 $$

    즉, $\mathbf{T}(x) \in \mathbf{K}_{\lambda}$ 이다. 따라서 $\mathbf{K}_{\lambda}$ 는 $\mathbf{T}$-불변이다. ▲ 

    고유공간 $\mathbf{E}_{\lambda}$ 와 일반화된 고유공간 $\mathbf{K}_{\lambda}$ 의 정의로부터 $\mathbf{E}_{\lambda}\subset \mathbf{K}_{\lambda}$ 는 자명하다. ▲ 

    2:

    $w\in \mathbf{K}_{\lambda}\cap \mathbf{K}_{\mu }$ 이면 다음을 만족하는 자연수 $p,q$ 가 존재한다. 

    $$ (\mathbf{T}-\lambda \mathbf{I})^{p}(w) = (\mathbf{T}- \mu \mathbf{I})^{q}(w) = 0 $$

    $t$ 에 대한 [다항식 $(t - \lambda )^{p}$ 와 $(t - \mu )^{q}$ 는 서로소이므로 다음을 만족하는 다항식 $q_1,  q_2$ 가 존재](../../Polynomials/#942fa2533)한다.

    $$ q_1(t)(t - \lambda ) ^{p} + q_2(t)(t - \mu )^{q} = 1 $$

    그러면 다음이 성립한다.
    
    $$ q_1(\mathbf{T})(\mathbf{T}-\lambda \mathbf{I})^{p} + q_2(\mathbf{T})(\mathbf{T} - \mu \mathbf{I})^{q} = \mathbf{I} $$

    $$ q_1(\mathbf{T})(\mathbf{T}-\lambda \mathbf{I})^{p}(w) + q_2(\mathbf{T})(\mathbf{T} - \mu \mathbf{I})^{q}(w) = w = 0 $$

    ▲ 

    3:

    1) 에 의하여 $\mathbf{K}_{\lambda}$ 는 $\mathbf{T}$-불변이므로 $\mathbf{K}_{\lambda}$ 는 $(\mathbf{T}-\mu \mathbf{I})$-불변이다. $x \in \mathbf{K}_{\lambda}$ 에 대하여 $\mathbf{T}(x) - \mu x \in \mathbf{K}_{\lambda}$ 이기 때문이다. 

    어떤 $w \in \mathbf{K}_{\lambda}$ 에 대하여 $(\mathbf{T}- \mu \mathbf{I})(w) = 0$ 이면 $w \in \mathbf{E}_{\mu } \subset \mathbf{K}_{\mu }$ 이므로 2) 에 의하여 $w = 0$ 이다. 따라서 [정리 2.4](../LinearTransformation/#7d40e8276) 에 의하여 $(\mathbf{T}- \mu \mathbf{I})_{\mathbf{K}_{\lambda}}$ 는 단사이다. ▲ 

    $x \in \mathbf{K}_{\lambda}$ 와 $(\mathbf{T}-\lambda \mathbf{I})^{p}(x) = 0$ 을 만족하는 가장 작은 양의 정수 $p$ 에 대하여 $\mathbf{W}$ 를 다음과 같이 정의하자. 

    $$ \mathbf{W} = \text{span} \{x, (\mathbf{T}-\lambda \mathbf{I})(x), \dots, (\mathbf{T}-\lambda \mathbf{I})^{p-1}(x)\} $$

    $w \in \mathbf{W}$ 를 스칼라 $a_0, a_1, \dots, a _{p-1}$ 에 대하여 다음과 같이 두자.

    $$ w = a_0x+ a_1(\mathbf{T}-\lambda \mathbf{I})(x)+ \dots + a _{p-1}(\mathbf{T}-\lambda \mathbf{I})^{p-1}(x) \in \mathbf{W} $$

    $$ \implies \mathbf{T}(w) = a_0 \mathbf{T}(x)+ a_1(\mathbf{T}-\lambda \mathbf{I})(\mathbf{T}(x))+ \dots + a _{p-1}(\mathbf{T}-\lambda \mathbf{I})^{p-1}(\mathbf{T}(x)) $$

    $\mathbf{W}$ 의 어떤 원소 $\epsilon$ 을 다음과 같이 정의하자.

    $$ \epsilon = a_0 \lambda \mathbf{I}(x) + a_1(\mathbf{T}-\lambda \mathbf{I})( \lambda \mathbf{I}(x)) + \dots + a _{p-1}(\mathbf{T}-\lambda \mathbf{I})^{p-1}(\lambda \mathbf{I}(x)) \in \mathbf{W} $$

    그러면 [정리 2.10](../LinearTransformation/#273a736ad) 에 의하여 다음이 성립한다.

    $$ \mathbf{T}(w) - \epsilon = a_0 (\mathbf{T} - \lambda \mathbf{I})(x)+ a_1(\mathbf{T}-\lambda \mathbf{I})^{2}(x)+ \dots + a _{p-2}(\mathbf{T}-\lambda \mathbf{I})^{p-1}(x)+ 0 \in \mathbf{W} $$

    부분공간은 선형공간이므로 덧셈에 대하여 선형이다. 따라서 다음이 성립한다.

    $$ \mathbf{T}(w) \in \mathbf{W} $$

    즉, $\mathbf{W}$ 는 $\mathbf{K}_{\lambda}$ 의 $\mathbf{T}$-불변 부분공간이다. 그러면 $\mathbf{W}$ 는 $(\mathbf{T}-\mu \mathbf{I})$-불변이다. $w \in \mathbf{W} \implies \mathbf{T}(w) - \mu w \in \mathbf{W}$ 이기 때문이다. 즉, $(\mathbf{T}-\mu \mathbf{I})(\mathbf{W}) \subset \mathbf{W}$ 이다. $(\mathbf{T}-\mu \mathbf{I})_{\mathbf{K}_{\lambda}}$ 가 단사이므로 $(\mathbf{T}-\mu \mathbf{I})_{\mathbf{W}}$ 도 단사이다. $\mathbf{W}$ 는 유한차원이므로 [정리 2.5](../LinearTransformation/#dfd4ff297) 에 의하여 $(\mathbf{T}-\mu \mathbf{I})_{\mathbf{W}}$ 는 전사이다. $x \in \mathbf{W} \subset \mathbf{K}_{\lambda}$ 인데 $(\mathbf{T}-\mu \mathbf{I})_{\mathbf{W}}$ 가 전단사이므로 $(\mathbf{T}-\mu \mathbf{I})(y) = x$ 인 $y \in \mathbf{W} \subset \mathbf{K}_{\lambda}$ 가 존재한다. 

    즉, 위와 같은 논리로 임의의 벡터 $v \in \mathbf{K}_{\lambda}$ 에 대하여 $(\mathbf{T}-\mu \mathbf{I})(y) = v$ 인 $y \in \mathbf{K}_{\lambda}$ 가 항상 존재한다는 것을 보일 수 있다. 그러면 [전사의 정의](../../Set/Set/#2b1f78028) 에 의하여 $(\mathbf{T}-\mu \mathbf{I})_{\mathbf{K}_{\lambda}}$ 는 전사이다. ■ 

!!! def "정리 7.2"

    유한차원 벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 의 특성다항식이 완전히 인수분해되면 중복도가 $m$ 인 $\mathbf{T}$ 의 고윳값 $\lambda$ 에 대하여 다음이 성립한다. 

    1. $\dim (\mathbf{K}_{\lambda})\leq m$

    2. $\mathbf{K}_{\lambda} = \mathbf{N}((\mathbf{T}-\lambda \mathbf{I})^{m})$

- 1) 은 [정리 5.7](../Diagonalization/#b5fbbceb6) 이 일반화된 것이다.

- 2) 는 [고유공간의 정의](../Diagonalization/#7ad38c4e6) 가 일반화된 것이다.

- 증명

    1:

    $\mathbf{T}_{\mathbf{K}_{\lambda}}$ 의 특성다항식을 $h(t)$ 로 두자. 정리 7.1-(2) 는 일반화된 고유공간에 다른 일반화된 고유공간의 고유벡터가 존재하지 않는다는 것을 보장해준다. 따라서 $\mathbf{T}_{\mathbf{K}_{\lambda}}$ 는 유일한 고윳값 $\lambda$ 를 갖는다. $d = \dim (\mathbf{K}_{\lambda})$ 로 두면 [정리 5.3](../Diagonalization/#3cd1e9499) 에 의하여 $h(t) = (-1)^{d}(t - \lambda )^{d}$ 이다. [정리 5.20](../Diagonalization/#3d097218e) 에 의하여 $\mathbf{T}_{\mathbf{K}_{\lambda}}$ 의 특성다항식 $h(t)$ 는 $\mathbf{T}$ 의 특성다항식을 나눈다. 따라서 $d \leq m$ 이다. ▲ 

    2:

    $\mathbf{N}((\mathbf{T} - \lambda \mathbf{I})^{m})$ 은 일반화된 고유공간 $\mathbf{K}_{\lambda}$ 에 포함될 조건을 만족하므로 $\mathbf{N}((\mathbf{T} - \lambda \mathbf{I})^{m}) \subset \mathbf{K}_{\lambda}$ 이다. ▲ 

    $\mu \neq \lambda$ 인 고윳값 $\mu$ 에 대하여 $(t - \mu )$ 을 곱한 꼴인 $g(t)$ 에 대하여 $\mathbf{T}$ 의 특성다항식은 $f(t) = (t - \lambda )^{m}g(t)$ 이다. 정리 7.1-(3) 에 의하여 $g(\mathbf{T})_{\mathbf{K}_{\lambda}}$ 는 전사이다. 따라서 $x \in \mathbf{K}_{\lambda}$ 에 대하여 $g(\mathbf{T})(y) = x$ 인 $y \in \mathbf{K}_{\lambda}$ 가 항상 존재한다. [케일리-해밀턴 정리](../Diagonalization/#a460d1c99) 에 의하여 다음이 성립한다. 

    $$ (\mathbf{T}-\lambda \mathbf{I})^{m}(x) = (\mathbf{T}-\lambda \mathbf{I})^{m}g(\mathbf{T})(y) = f(\mathbf{T})(y) = 0 $$

    따라서 $x \in \mathbf{N}((\mathbf{T}-\lambda \mathbf{I})^{m}) \implies \mathbf{K}_{\lambda}\subset \mathbf{N}((\mathbf{T}-\lambda \mathbf{I})^{m})$ 이다. ■ 

!!! def "정리 7.3"

    유한차원 벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 의 특성다항식이 완전히 인수분해되면 $\mathbf{T}$ 의 서로 다른 고윳값 $\lambda _1, \dots, \lambda _k$ 와 임의의 $x \in \mathbf{V}$ 와 $i \in \{1, \dots, k\}$ 에 대하여 다음을 만족하는 벡터 $v_i \in \mathbf{K}_{\lambda_i}$ 가 유일하게 존재한다.

    $$ x = v_1 + v_2 + \dots + v_k $$

- 증명

    $\mathbf{T}$ 의 특성다항식을 다음과 같이 두자.

    $$ f(t) = (t - \lambda _1)^{n_1} (t - \lambda _2)^{n_2}\dots  (t - \lambda _k)^{n_k} $$

    $j \in \{1,\dots,k\}$ 에 대하여 $f_j(t)$ 를 다음과 같이 두자.

    $$ f_j(t) = \prod_{\substack{i \neq j \\ i = 1}}^{k}(t - \lambda _i)^{n_i} $$

    다항식 $f_i(t)$ 들은 서로소이므로 [서로소 다항식들의 관계 정리](../../Polynomials/#942fa2533)에 대하여 다음이 성립한다. 

    $$ q_1(x)f_1(x) + q_2(x)f_2(x) + \dots + q_k(x)f_k(x) = 1 $$

    따라서 $v \in \mathbf{V}$ 에 대하여 다음이 성립한다.

    $$ q_1(\mathbf{T})f_1(\mathbf{T})(v) + q_2(\mathbf{T})f_2(\mathbf{T})(v) + \dots + q_k(\mathbf{T})f_k(\mathbf{T}) (v) = v $$

    두 다항식은 가환적이다. $v_i = q_i(\mathbf{T})f_i(\mathbf{T})(v) = f_i(\mathbf{T})q_i(\mathbf{T})(v)$ 라 하면 [케일리-해밀턴 정리](../Diagonalization/#a460d1c99) 에 의하여 다음이 성립한다. 

    $$ (\mathbf{T}-\lambda _i \mathbf{I})^{n_i}(v_i) = (\mathbf{T}-\lambda _i \mathbf{I})^{n_i}f_i(\mathbf{T})q_i(\mathbf{T})(v) = f(\mathbf{T})(q_i(\mathbf{T})(v)) = 0 $$

    즉, $v_i \in \mathbf{K}_{\lambda_i}$ 이다. 이로써 $v = \displaystyle \sum_{i=1}^{k}v_i$ 를 만족하는 $v_i \in \mathbf{K}_{\lambda_i}$ 들의 존재성이 증명되었다. ▲ 

    이제 $v_i$ 들의 유일성을 증명하자. 정리 7.1-(1) 에 의하여 $\mathbf{K}_{\lambda_j}$ 는 $\mathbf{T}$-불변이다. 따라서 각 $\mathbf{K}_{\lambda_j}$ 들은 $f_j(\mathbf{T})$-불변이다. 정리 7.1-(3) 에 의하여 $f_j(\mathbf{T})$ 는 $\mathbf{K}_{\lambda_j}$ 에서 단사이고 정리 7.2-(2) 에 의하여 $i \neq j$ 에 대하여 $z \in \mathbf{K}_{\lambda_i} \implies f_j(\mathbf{T})(z) = 0$ 이다. 즉, $f_j(\mathbf{T})(\mathbf{K}_{\lambda_i}) = \{0\}$ 이다.

    $i \in \{1,\dots,k\}$ 에 대한 $v_i, w_i \in \mathbf{K}_{\lambda_i}$ 에 대하여 $\displaystyle v = \sum_{i=1}^{k}v_i = \sum_{i=1}^{k}w_i$ 라 하면 $j \in \{1,\dots,k\}$ 에 대하여 $f_j(\mathbf{T})$ 는 선형이므로 다음이 성립한다. 

    $$ f_j(\mathbf{T})(v) = \sum_{i=1}^{k}f_j(\mathbf{T})(v_i) = \sum_{i=1}^{k}f_j(\mathbf{T})(w_i) $$

    $i \neq j$ 이면 $f_j(\mathbf{T})(v_i) = f_j(\mathbf{T})(w_i) = 0$ 이므로 $f_j(\mathbf{T})(v_j) = f_j(\mathbf{T})(w_j)$ 이다. $f_j(\mathbf{T})$ 는 $\mathbf{K}_{\lambda_j}$ 에서 단사이므로 $v_j = w_j$ 이다. ■ 

!!! def "정리 7.4"

    유한차원 벡터공간 $\mathbf{V}$ 의 선형연산자 $\mathbf{T}$ 의 특성다항식이 다음과 같이 완전히 인수분해된다고 가정하자. 

    $$ (\lambda _1 - t)^{m_1}(\lambda _2 - t)^{m_2}\dots(\lambda _k - t)^{m_k} $$

    $i \in \{1,\dots,k\}$ 와 $\mathbf{K}_{\lambda_i}$ 의순서기저 $\beta _i$ 에 대하여 다음이 성립한다.

    1. $j \neq i \implies \beta _i \cap \beta _j = \varnothing$

    2. $\displaystyle \beta = \bigcup_{i=1}^{k}\beta _i$ 는 $\mathbf{V}$ 의 순서기저이다.

    3. $\forall i : \dim ((\mathbf{K}_{\lambda_i}) = m_i$

- 증명

    1:

    [정리 7.1-(2)](#744719af2) 에서 바로 나온다. ▲ 

    2:

    $\beta _i$ 의 벡터들의 합을 $v_i$ 라 하고 $\beta$ 의 일차결합을 $0$ 이라 하면 다음이 성립한다. 

    $$ v_1 + v_2 + \dots + v_k = 0 $$

---

ref:

:   Stephen H. Friedberg, Linear Algebra, 5th Edition
