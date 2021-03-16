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

- 선택공리가 수학에서 사용될 때 대부분 순서와 관련된다. 아래에서 살펴볼 소른 도움정리와 하우스도르프 극대 원칙은 선택공리과 동치인 명제인데 수학의 여러 분야에서 널리 쓰인다.

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

    라 정의하자. 그러면 각 $i \in I$ 에 대하여 $g(i) = h(X_i) \in X_i$ 이므로 

    $$ g \in \prod_{i \in I}^{}X_i $$

    이다. ■ 

- 4) 에서 3) 를 도출하는 증명 

    4) 가 가정인 것에서 $\prod_{}^{}\{A:A \in 2 ^{X} \text{ \textbackslash }\{\varnothing \}\} \neq \varnothing$ 이므로 
    
    $$ \exists  h \in \prod_{}^{}\{A:A \in 2 ^{X} \text{ \textbackslash }\{\varnothing \}\} \neq \varnothing$$

    이다. 그러면 각 $A \in 2 ^{X} \text{ \textbackslash }\{\varnothing \}$ 에 대하여 $h(A) \in A$ 이므로 $h$ 는 $X$ 의 선택함수이다. ■ 

!!! tldr ""

    사슬(chain) : 순서집합 $X$ 의 부분집합 $A$ 가 

    $$ a, b \in A \implies a \leq b \lor a \geq b $$

    이면 $A$ 를 $X$ 의 사슬이라 한다.

- 즉 사슬 속의 서로 다른 두 원소는 항상 비교 가능하다.

- 예시 

    집합 $X$ 의 멱집합 $2 ^{X}$ 에 포함관계에 의한 순서를 부여하여 $A \subset B \iff A \leq B$ 라고 정의하자. $a,b,c \in X$ 에 대하여 

    $$ \{\{a\}, \{a,c\}\}, \quad \{\varnothing , \{a\},\{a,b\},\{a,b,c\},X\} $$

    등은 $2 ^{X}$ 의 사슬이고, $X$ 는 사슬의 상계이다.

!!! tldr ""

    반사슬(antichain) : 순서집합 $X$ 의 부분집합 $A$ 의 서로 다른 두 원소를 비교할 순서관계가 없을 때 $A$ 를 $X$ 의 반사슬이라 한다.

- 즉 반사슬 속의 서로 다른 두 원소는 비교 불가능하다.

!!! tldr ""

    극대원소(maximal element) : 순서집합 $X$ 의 원소 $m \in X$ 이 

    $$ x \in X, x \geq m \implies x = m $$

    일 때 $m$ 을 $X$ 의 극대원소라 한다.

- 예시 

    사슬의 예시에서 순서집합 $2 ^{X}$ 의 극대원소는 $X$ 이다.

    한편 $\N$ 이나 $\mathbb{Z}$ 는 그 자체가 사슬이지만, 극대원소가 존재하지 않는다.

!!! tldr ""

    극소원소(minimal element) : 순서집합 $X$ 의 원소 $n \in X$ 이 

    $$ x \in X, x \leq n \implies x = n $$

    일 때 $n$ 을 $X$ 의 극대원소라 한다.

!!! tldr ""

    초른의 보조정리(Zorn lemma) : 공집합이 아닌 순서집합 $X$ 의 모든 사슬이 상계를 가지면 $X$ 는 극대원소를 가진다.

- 선택공리과 동치인 명제로써 수학의 여러 분야에서 널리 쓰인다.

!!! tldr ""

    하우스도르프 극대 원리(Hausdorff maximal principle) : 임의의 순서집합 $X$ 는 극대 사슬을 가진다.

- 선택공리과 동치인 명제로써 수학의 여러 분야에서 널리 쓰인다.

- 예시

    포함관계에 의한 순서를 부여받은 순서집합 $X$ 의 모든 사슬을 모은 집합 $\mathcal{C}(X)$ 는 포함관계에 의하여 다시 순서집합이 된다. 이 정리는 순서집합 $\mathcal{C}(X)$ 가 극대원소를 가진다는 것을 말한다. 

!!! tldr ""

    포함관계에 의하여 순서가 부여된 집합 $X$ 의 사슬의 집합 $\mathcal{C}(X)$ 의 사슬 $\mathcal{C}$ 에 대하여 모든 사슬 $\mathcal{C}$ 의 원소의 합집합 $\bigcup_{}^{}\mathcal{C} (\subset X)$ 은 $X$ 의 사슬이다. 즉, 다음이 성립한다.

    $$ \bigcup_{}^{}\mathcal{C} \in \mathcal{C}(X) $$

- 증명
    
    $\forall  a,b \in \bigcup_{}^{}\mathcal{C}$ 와 $\mathcal{C}(X)$ 의 어떤 사슬 $\mathcal{C}$ 에 대하여

    $$ \exists C_1, C_2 \text{ s.t. }\ a \in C_1 \in \mathcal{C}, b \in C_2 \in \mathcal{C} $$

    이다. $\mathcal{C}$ 은 사슬이므로 $C_1 \subset C_2 \lor C_2 \subset C_1$ 이다. $C_1 \subset C_2$ 일 경우 $a,b \in C_2$ 인데 $C_2$ 는 $X$ 의 사슬이므로 $a \leq b \lor b \leq a$ 이다. 마찬가지로 $C_2 \subset C_1$ 인 경우에도 $a \leq b \lor b \leq a$ 이다. 이로써 $\bigcup_{}^{}\mathcal{C}$ 의 임의의 두 원소가 서로 비교 가능함을 알 수 있고, 이에따라 $\bigcup_{}^{}\mathcal{C}$ 는 $X$ 의 사슬임이 증명되었다. 즉 $\bigcup_{}^{}\mathcal{C} \in \mathcal{C}(X)$ 이다. ▲

!!! tldr ""

    초른의 보조정리는 하우스도르프 극대 원리와 동치이다.

- 초른의 보조정리에서 하우스도르프 극대 원리를 도출하는 증명 

    우선 초른의 보조정리를 가정하자. 그리고 포함관계에 의한 순서를 부여받은 순서집합 $X$ 의 모든 사슬을 모은 순서집합 $\mathcal{C}(X)$ 에 초른의 보조정리를 적용해보고, 하우스도르프 극대 원리가 도출되는지 보자. 

    정리 "포함관계에 의하여 순서가 부여된 집합 $X$ 의 사슬의 집합 $\mathcal{C}(X)$ 의 사슬 $\mathcal{C}$ 에 대하여 모든 사슬 $\mathcal{C}$ 의 원소의 합집합 $\bigcup_{}^{}\mathcal{C} (\subset X)$ 은 $X$ 의 사슬이다." 에서

    $$ C = \bigcup_{}^{}\mathcal{C} $$

    라고 두면 $C$ 는 $\mathcal{C}$ 들의 합집합이므로 $\mathcal{C} \subset \mathcal{C}(X)$ 의 상계임이 자명하다. 그러므로 순서집합 $\mathcal{C}(X)$ 는 초른의 보조정리의 가정을 만족하고, $\mathcal{C}(X)$ 는 초른의 보조정리의 귀결(극대원소를 가진다) 또한 만족한다. 이처럼 $\mathcal{C}(X)$ 이 초른의 보조정리를 만족하는데, 위의 증명이 보인 것은 $\mathcal{C}(X)$ 이 극대 사슬 $C$ 를 가진다는 것이다. 따라서 초른의 보조정리를 가정하면 하우스도르프 극대 원리가 성립한다. ■ 

- 하우스도르프 극대 원리에서 초른의 보조정리를 도출하는 증명 

    $X$ 의 모든 사슬이 상계를 가진다고 가정하자. 그러면 하우스도르프 극대 원리에 의하여 $X$ 는 극대 사슬 $C$ 를 가지는데 가정에 의하여 이것의 상계 $m \in X$ 또한 존재한다. 이제 이 $m$ 이 극대원소임을 보이면 된다.

    먼저 $x \in X, x > m$ 이라고 가정하자. 그러면 $x$ 는 $C$ 의 임의의 원소와 비교 가능하고, 따라서 $C \cup \{x\}$ 도 사슬이다. 그런데 $C \subsetneq C \cup \{x\}$ 이므로 $C$ 가 극대사슬이라는 것에 모순이다. 따라서 $x$ 는 존재하지 않으며 $m$ 이 $X$ 의 극대원소가 된다. ■ 

!!! tldr ""

    순서집합 $X$ 의 부분집합족 $\mathcal{X} \subset 2 ^{X}$ 가 

    1. $A \in \mathcal{X}, B \subset A \implies B \in \mathcal{X}$

    2. $\mathcal{C}$ 이 $\mathcal{X}$ 의 사슬이면 $\bigcup_{}^{}\mathcal{C}\in \mathcal{X}$ 이다.

    을 만족하면 $\mathcal{X}$ 는 극대원소를 가진다. 

- 정리 "초른의 보조정리는 하우스도르프 극대 원리와 동치이다." 의 증명과정에서 살펴보았듯 포함관계에 의한 순서가 부여된 $X$ 의 사슬 집합 $\mathcal{C}(X)$ 는 본 정리의 두 가지 조건을 만족한다. 

    따라서 하우스드로프 극대 원리는 이 정리에서 바로 도출된다.

- 증명 

    조건 1), 2) 를 만족하는 $\mathcal{X}$ 가 존재할 때 극대원소가 존재함을 보이면 증명이 된다. 그러므로 $\mathcal{X}$ 이 존재한다고 하면, 조건 1) 에 의하여 $\mathcal{X}$ 는 임의의 원소 $A \in \mathcal{X}$ 의 모든 부분집합을 원소로 갖는다. 
    
    그러면 각 $A \in \mathcal{X}$ 에 대하여 

    $$ \tilde{A} = \{x \in X : A \cup \{x\}\in \mathcal{X}\} $$

    라고 하자. 그러면 임의의 $A \in \mathcal{X}$ 가 결정되었을 때 그 $A$ 의 원소인 $x \in X$ 에 대하여 $A \cup \{x\} \in \mathcal{X}$ 도 성립하므로 당연히 $A$ 의 모든 원소는 기본적으로 $\tilde{A}$ 에 속하고, 추가적으로 $A$ 를 포함하면서 $A$ 보다 큰 집합 $B (\supset A)$ 가 $\mathcal{X}$ 에 존재하면 $B \text{ \textbackslash }A$ 의 원소들 또한 $\tilde{A}$ 에 속하게 될 것이다. 그러므로 먼저 자명하게 $A \subset \tilde{A}$ 이고, $A$ 가 $\mathcal{X}$ 의 극대 원소일 필요충분조건은 $A$ 보다 큰 집합이 없다는 것에서 $A = \tilde{A}$ 이다. ▲ 

    이제 집합 $X$ 의 선택함수 $h$ 를 택하고 함수 $g: \mathcal{X}\to \mathcal{X}$ 를 

    $$ g(A) = \begin{cases} A \sqcup \{h(\tilde{A}\text{ \textbackslash }A)\} & A \subsetneq \tilde{A}\\ A & A = \tilde{A}\\ \end{cases} $$

    로 두자. 그러면 $g(A)=A$ 를 만족하는 $A \in \mathcal{X}$ 의 존재성을 보이면 증명이 끝난다. 함수 $g$ 의 특성상 $A \subset g(A)$ 는 항상 성립하므로 $g(A) \subset A$ 인 $A$ 를 보이면 된다. ▲ 

    이제 조건

    $$ \varnothing \in \mathcal{Y}, \quad A \in \mathcal{Y} \implies g(A) \in \mathcal{Y}, \quad \mathcal{C} \in \mathcal{C}(\mathcal{Y}) \implies \bigcup_{}^{}\mathcal{C}\in \mathcal{Y} \tag{1} $$

    을 만족하는 $\mathcal{X}$ 의 부분집합 $\mathcal{Y} \subset \mathcal{X}$ 를 생각해보자. 이런 조건을 만족하는 $\mathcal{X}$ 의 모든 부분집합들의 교집합을 $\mathcal{Y}_0$ 이라고 하자. 그러면 $\varnothing \in \mathcal{Y}_0$ 이므로 $\mathcal{Y}_0 \neq \varnothing$ 이고, $(1)$ 을 만족하는 최소의 집합족이 된다. 이때 이 $\mathcal{Y}_0$ 이 $\mathcal{X}$ 의 사슬임을 보이려 한다. 만약 $\mathcal{Y}_0$ 이 $\mathcal{X}$ 의 사슬이면 $\mathcal{Y}_0 \in \mathcal{C}(\mathcal{Y}_0)$ 이므로 $\bigcup_{}^{}\mathcal{Y}_0 \in \mathcal{Y}_0$ 인데 $A = \bigcup_{}^{}\mathcal{Y}_0$ 로 두면 $A = \bigcup_{}^{}\mathcal{Y}_0 \in \mathcal{Y}_0$ 에서 $g(A) \in \mathcal{Y}_0$ 이므로 

    $$ g(A) \subset \bigcup_{}^{}\mathcal{Y}_0 = A $$

    가 되어 증명이 끝난다. ▲ 

    $C \in \mathcal{Y}_0$ 가 

    $$ D \in \mathcal{Y}_0 \implies C \subset D \lor D \subset C $$
    
    를 만족할 때 $C$ 를 comparable element 이라고 하자. 가령 $\varnothing$ 는 comparable element 이다. 우리의 목표는 다음을 증명하는 것이다.

    $$ C \text{ is comparable element  } \implies g(C) \text{ is comparable element   } \tag{2} $$

    이것을 증명하면 $\mathcal{Y}_0$ 의 모든 comparable element 의 집합 $\mathcal{C}_0$ 이 $(1)$ 을 만족함을 알 수 있다. (*$(1)$ 의 $\mathcal{Y}$ 를 $\mathcal{C}_0$ 으로 대체하여 따져보면 쉽게 알 수 있다.*) 그런데 $\mathcal{Y}_0$ 은 $(1)$ 을 만족하는 최소의 집합족이었으므로 $\mathcal{Y}_0 \subset \mathcal{C}_0$ 인데 $\mathcal{C}_0$ 은 $\mathcal{Y}_0$ 의 원소로 구성되어 있으므로 $\mathcal{C}_0 \subset \mathcal{Y}_0$ 이므로 $\mathcal{Y}_0=\mathcal{C}_0$ 이다. 이는 $\mathcal{Y}_0$ 의 모든 원소가 비교가능하는 것을 말해준다. 그렇게 되면 $\mathcal{Y}_0$ 는 사슬이라는 말이 되고, 결국 모든 증명이 끝난다. ▲ 

    이제 $(2)$ 를 증명하기 위해 comparable element 인 $C \in \mathcal{Y}_0$ 를 고정하고 집합족 

    $$ \mathcal{U} = \{A \in \mathcal{Y}_0 : A \subset C \lor g(C) \subset A\} $$

    에 대하여 $(1)$ 을 보이려 한다. 이때 $(1)$ 의 첫째 조건은 자명하고, 정리 "포함관계에 의하여 순서가 부여된 집합 $X$ 의 사슬의 집합 $\mathcal{C}(X)$ 의 사슬 $\mathcal{C}$ 에 대하여 모든 사슬 $\mathcal{C}$ 의 원소의 합집합 $\bigcup_{}^{}\mathcal{C} (\subset X)$ 은 $X$ 의 사슬이다." 에 의하여 $\mathcal{Y}$ 의 모든 사슬의 합집합 $\bigcup_{}^{}C$ 은 $\mathcal{Y}$ 의 사슬인데 $\mathcal{Y}$ 는 조건 2) 를 만족하므로 $(1)$ 의 셋째 조건도 자명하다. 

    둘째 조건을 보이기 위하여 $\forall A \in \mathcal{Y}_0$ 에 대하여 

    $$ A \subset C \lor g(C) \subset A \implies g(A) \subset C \lor g(C) \subset g(A) \tag{3} $$

    를 보이면 된다. 
    
    - $A = C$ 이면 $g(C) = g(A)$ 이므로 $(3)$ 이 성립한다.

    - $g(C) \subset A$ 이면 $g(C) \subset A \subset g(A)$ 이므로 성립한다. 

    - $A \subsetneq C$ 이면 $C$ 가 comparable element 이므로 $g(A) \subset C \lor C \subset g(A)$ 이다. 
    
        - $g(A) \subset C$ 이면 성립한다.
        
        - $C \subsetneq g(A)$ 이면 $A \subsetneq C \subsetneq g(A)$ 이므로 $g(A) \text{ \textbackslash }A$ 가 두 개 이상의 원소를 갖는데(*$g(C), C$ 가 $g(A)$ 에 속하기 때문*), 이는 $g$ 의 정의에 의하여 불가능하다. (*왜냐하면 $g$ 는 $A$ 이거나 $A$ 이외에 다른 원소를 하나만 갖기 때문에 $g(A)\text{ \textbackslash }A$ 의 원소의 갯수는 $0$ 이거나 $1$ 이기 때문.*) 그러므로 $C \subsetneq g(A)$ 은 모순이고, 반드시 $C \supset g(A)$ 이다.

    이로써 $(3)$ 이 증명되었고, 집합족 $\mathcal{U}$ 는 $(1)$ 을 만족한다. ▲ 

    집합족 $\mathcal{Y}_0$ 는 $(1)$ 을 만족하는 최소의 집합족인데 $\mathcal{U}\subset \mathcal{Y}_0$ 이므로 $\mathcal{U}=\mathcal{Y}_0$ 이다. 따라서 $\forall A \in \mathcal{Y}_0, A \subset C \subset g(C) \lor g(C) \subset A$ 이다. 즉, $g(C)$ 는 comparable element 라는 말이다. 집합 $C \in \mathcal{Y}_0$ 가 임의의 comparable element 이므로 $(2)$ 가 증명되었고 모든 증명이 끝났다. ■ 

- 이 정리로부터 하우스드로프 극대 원리를 도출하는 증명

!!! tldr ""

    정렬 집합(well ordered set) 또는 정렬 전순서 집합(well totally ordered set) : 순서집합 $X$ 에서 $\forall A \in 2 ^{X}$ 에 대하여 $A \neq \varnothing$ 인 $A$ 가 최소 원소를 가지면 $X$ 를 정렬집합이라고 한다. 

- 정렬 집합의 순서관계를 정렬 순서라 한다. 

- 정리 "비어있지 않은 자연수들의 집합은 최소 원소를 가진다." 는 자연수집합 $\N$ 이 정렬 집합임을 말해준다.

- 정렬 집합은 그 자체로서 사슬이 된다.

!!! tldr ""

    정렬 순서(well ordered) : 정렬 집합이 갖는 순서관계이다.


!!! tldr ""

    임의의 집합 $X$ 에 정렬순서를 부여할 수 있다.

- 아래의 증명은 초른의 보조정리를 사용하는데 이는 초른의 보조정리가 적용되는 대표적인 사례이다.

- 증명

    먼저 $X$ 의 부분집합 $A$ 와 $G \subset A \times A$ 로써 $A$ 의 정렬순서를 부여해주는 관계들의 순서쌍 $(A,G)$ 를 생각하고, 이런 순서쌍 전체 집합을 $\mathcal{X}$ 라 두자. 이때 $(A,G), (B,H) \in \mathcal{X}$ 가 

    $$ A \subset B, \quad G \subset H, \quad x \in A, y \in B \text{ \textbackslash }A \implies (x, y) \in H $$

    를 만족할 때 $(A, G) \leq (B, H)$ 라 정의하면 순서관계가 됨을 바로 확인할 수 있다.
