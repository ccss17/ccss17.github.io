# 선택공리

!!! tldr ""

    선택공리(axiom of choice, AC) : 공집합이 아닌 집합에서 한 원소를 택할 수 있고, 이를 무한히 반복할 수 있다는 공리로써 다음의 동치 명제들

    1. 함수 $f: X \to Y$ 가 전사이면 $f \circ g = 1_Y$ 인 함수 $g: Y \to X$ 가 존재한다.

    2. 집합 $X$ 의 분할 $\mathcal{P}$ 에 대하여, 각 $A \in \mathcal{P}$ 에 대하여 다음이 성립한다.

        $$ \exists g: \mathcal{P} \to X \text{ s.t. }\ g(A) \in A $$

    3. 집합 $X$ 에 대한 각 $A \in 2 ^{X} \text{ \textbackslash }\{\varnothing \}$ 에 대하여 다음이 성립한다.

        $$ \exists h: 2 ^{X} \text{ \textbackslash }\{\varnothing \} \to X \text{ s.t. }\ h(A) \in A$$

    4. $I \neq \varnothing \land  \forall i \in I , X_i \neq \varnothing \implies \displaystyle \prod_{i \in I}^{}X_i \neq \varnothing$

    로 정의된다.
    
- 하나의 형식문으로써 

    $$ \forall X \bigg [\varnothing \not \in X \implies \exists f: X \to \bigcup_{}^{}X \quad \forall A \in X(f(A) \in A) \bigg ] $$

    라고 나타낼 수 있다. 이 형식문은 비어있지 않은 임의의 $X$ 에 대하여 $X$ 위에서 정의된 선택 함수 $f$ 가 존재한다 라는 뜻이다.

- 아래의 2) 에서 3) 을 도출하는 증명에서 $h(A) \in A$ 를 만족하는 함수 $h$ 를 집합 $X$ 의 선택함수라고 하고, 3) 을 선택공리라고 부른다.

- 1) 에서 2) 를 도출하는 증명 

    집합 $X$ 의 분할 $\mathcal{P}$ 가 주어졌을 때 각 $x \in X$ 가 속하는 $A \in \mathcal{P}$ 가 유일하게 결정되는데 이를 $f(x)$ 라고 두면, $f: X \to \mathcal{P}$ 는 전사함수이다. 이때 1) 이 가정이므로 $f \circ g = 1 _{\mathcal{P}}$ 인 함수 $g: \mathcal{P}\to X$ 가 존재한다. 

    그러면 $f(g(A)) = A$ 이므로 $g(A) \in A$ 이다. ■ 
    
    $g(A)$ 는 $X$ 의 원소 가운데 $A$ 에 들어가는 것을 하나 고른 것이다.

- 2) 에서 1) 을 도출하는 증명 

    $f: X \to Y$ 가 전사이면 $\mathcal{P} = \{f ^{-1}(\{y\}) : y \in Y\}$ 는 $X$ 의 분할이다. (*왜냐하면 $\mathcal{P}$ 은 $f$ 의 공역 $Y$ 의 원소 $y$ 에 대한 집합 $\{y\}$ 를 $f$ 의 역함수 $f ^{-1}$ 에 집어넣어서 그것에 대응하는 $X$ 의 원소 $x$ 의 집합으로 구성되었기 때문이다. 이것이 가능한 이유는 $f$ 가 전사 사상이기 때문이고, 하나의 $y \in Y$ 로 가는 여러개의 $x$ 가 있을 수도 있으므로 $\mathcal{P}$ 의 원소들은 원소의 갯수가 하나 이상이다.*) 따라서 $\forall y \in Y$ 에 대하여 $g[f ^{-1}(\{y\})] \in f ^{-1}(\{y\})$ 를 만족하는 함수 $g : \mathcal{P} \to X$ 가 존재한다. 

    이때 각 $y \in Y$ 에 대하여 

    $$ h(y) = g[f ^{-1}(\{y\})] $$

    라 정의하면 $h: Y \to X$ 는 함수이고, $h(y) \in f ^{-1}(\{y\})$ 이므로 증명하고자 하는 바인 $f(h(y))=y$ 가 성립한다. (*이 함수 $h$ 는 같은 $y \in Y$ 로 대응되는 $x \in X$ 들로 이루어진 집합 중에서 하나를 택하는 함수라고 이해하면 될 것 같다.*) ■ 

- 2) 에서 3) 을 도출하는 증명 

    각 $A \in 2 ^{X} \text{ \textbackslash }\{\varnothing \}$ 에 대하여 

    $$ \tilde{A} = \{(A, a) : a \in A\} \subset (2 ^{X} \text{ \textbackslash }\{\varnothing \}) \times X $$

    라 두면 $\mathcal{P} = \{\tilde{A} : A \in 2 ^{X} \text{ \textbackslash }\{\varnothing \}\}$ 은 집합 $Y = \bigcup_{}^{}\{\tilde{A} : A \in 2 ^{X} \text{ \textbackslash }\{\varnothing \}\}$ 의 분할이다. 이때 $\forall A \in 2 ^{X} \text{ \textbackslash }\{\varnothing \}$ 에 대하여 $g(\tilde{A}) \in \tilde{A}$ 를 만족하는 함수 $g: \mathcal{P} \to Y$ 가 존재한다.

    이때 $\pi _2:(2 ^{X} \text{ \textbackslash }\{\varnothing \}) \times X \to X$ 를 사영이라 두고 $A \in 2 ^{X} \text{ \textbackslash }\{\varnothing \}\}$ 에 대하여

    $$ h: A \mapsto \pi _2(g(\tilde{A})) $$

    라 정의하면 $h: 2 ^{X} \text{ \textbackslash }\{\varnothing \} \to X$ 가 원하는 함수이다. ■  

- 3) 에서 2) 를 도출하는 증명 

    집합 $X$ 의 분할 $\mathcal{P}$ 는 $2 ^{X} \text{ \textbackslash }\{\varnothing \}\}$ 의 부분집합이므로 3) 을 가정하면 2) 는 바로 도출된다. ■ 

- 3) 에서 4) 를 도출하는 증명 

    먼저 집합 $X (\neq \varnothing )$ 와 $Y (\neq \varnothing )$ 의 곱집합 $X \times Y$ 가 $\varnothing$ 이 아님은 자명하다. 왜냐하면 $x \in X$ 와 $y \in Y$ 를 택하면 $(x,y) \in X \times Y$ 이기 때문이다.

    임의의 집합족 $\{X_i : i \in I\}$ 에 대하여 4) 를 정의했는데 3) 에서 4) 를 도출해보자. 먼저 3) 을 가정했으므로 집합 $X = \bigcup_{i \in I}^{}X_i$ 의 선택함수 $h: 2 ^{X} \text{ \textbackslash }\{\varnothing \}\} \to X$ 가 존재하는데, 함수 $g: I \to X$ 를 

    $$ g(i) = h(X_i) $$

    라 정의하자. 