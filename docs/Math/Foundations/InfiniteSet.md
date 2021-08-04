!!! info "ref"

    [집합과 수의 체계](http://www.math.snu.ac.kr/~kye/book/set-number.html)

!!! note

    아래의 논의의 "순서관계" 란 부분순서관계를 뜻한다.

# 선택공리

!!! tldr ""

    선택 함수(choice function) : 집합족 $\{S_i\} _{i \in I}$ 위의 선택함수 $f: I \to \bigcup_{i \in I}^{}S_i$ 는 다음과 같이 정의된 함수이다.

    $$ \forall i \in I: f(i) \in S_i $$

- 만약 $\varnothing \in \{S_i\}_{i \in I}$ 이면 $\{S_i\} _{i \in I}$ 는 선택 함수를 가질 수 없다.

- 아래의 선택공리에 의하여 공집합을 포함하지 않는 모든 집합족은 선택 함수를 갖는다.

!!! tldr "선택공리(axiom of choice, AC)"

    선택공리는 공집합이 아닌 집합들의 집합이 주어지면, 각 원소로부터 한 원소를 택할 수 있고, 이를 무한히 반복할 수 있다는 공리

    $$ \forall X \bigg [\varnothing \not \in X \implies \exists f: X \to \bigcup_{}^{}X \quad \forall A \in X(f(A) \in A) \bigg ] $$

    로써 다음의 동치 명제들로도 정의된다.

    1. 함수 $f: X \to Y$ 가 전사이면 $f \circ g = 1_Y$ 인 함수 $g: Y \to X$ 가 존재한다.

    2. 집합 $X$ 의 분할 $\mathcal{P}$ 에 대한 각 $A \in \mathcal{P}$ 에 대하여 다음이 성립한다.

        $$ \exists g: \mathcal{P} \to X \text{ s.t. }\ g(A) \in A $$

    3. 집합 $X$ 에 대한 각 $A \in 2 ^{X} \setminus \{\varnothing \}$ 에 대하여 다음이 성립한다.

        $$ \exists h: 2 ^{X} \setminus \{\varnothing \} \to X \text{ s.t. }\ h(A) \in A$$

    4. 집합 $I$ 와 각 $i \in I$ 에 대한 집합 $X_i$ 에 대하여 다음이 성립한다.
    
        $$I \neq \varnothing \land  \forall i \in I , X_i \neq \varnothing \implies \displaystyle \prod_{i \in I}^{}X_i \neq \varnothing$$
    
- 아래의 2) 에서 3) 을 도출하는 증명에서 $h(A) \in A$ 를 만족하는 함수 $h$ 를 집합 $X$ 의 선택함수라고 하고, 3) 을 선택공리라고 부른다.

- 선택공리가 수학에서 사용될 때 대부분 순서와 관련된다. 아래에서 살펴볼 [초른 보조정리](#8e7118900)와 [하우스도르프 극대 원리](#4f540f90d)은 선택공리과 동치인 명제인데 수학의 여러 분야에서 널리 쓰인다.

    선택공리를 사용하는 정리들은 수학의 각 분야에서 매우 중요한 역할을 하는 경우가 많다. 

- 선택공리는 다음과 같이 각 집합 $S_i$ 를 그 속의 원소 $x_i \in S_i$ 로 대응시킨다. 

    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Axiom_of_choice.svg/330px-Axiom_of_choice.svg.png)

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

    각 $A \in 2 ^{X} \setminus \{\varnothing \}$ 에 대하여 

    $$ \tilde{A} = \{(A, a) : a \in A\} \subset (2 ^{X} \setminus \{\varnothing \}) \times X $$

    라 두면 $\mathcal{P} = \{\tilde{A} : A \in 2 ^{X} \setminus \{\varnothing \}\}$ 은 집합 $Y = \bigcup_{}^{}\{\tilde{A} : A \in 2 ^{X} \setminus \{\varnothing \}\}$ 의 분할이다. 이때 $\forall A \in 2 ^{X} \setminus \{\varnothing \}$ 에 대하여 $g(\tilde{A}) \in \tilde{A}$ 를 만족하는 함수 $g: \mathcal{P} \to Y$ 가 존재한다.

    이때 $\pi_2 :(2 ^{X} \setminus \{\varnothing \}) \times X \to X$ 를 사영이라 두고 $A \in 2 ^{X} \setminus \{\varnothing \}$ 에 대하여

    $$ h: A \mapsto \pi_2 (g(\tilde{A})) $$

    라 정의하면 $h: 2 ^{X} \setminus \{\varnothing \} \to X$ 가 원하는 함수이다. ■  

- 3) 에서 2) 를 도출하는 증명 

    집합 $X$ 의 분할 $\mathcal{P}$ 는 $2 ^{X} \setminus \{\varnothing \}$ 의 부분집합이므로 3) 을 가정하면 2) 는 바로 도출된다. ■ 

- 3) 에서 4) 를 도출하는 증명 

    먼저 집합 $X (\neq \varnothing )$ 와 $Y (\neq \varnothing )$ 의 곱집합 $X \times Y$ 가 $\varnothing$ 이 아님은 자명하다. 왜냐하면 $x \in X$ 와 $y \in Y$ 를 택하면 $(x,y) \in X \times Y$ 이기 때문이다.

    임의의 집합족 $\{X_i : i \in I\}$ 에 대하여 4) 를 정의했는데 3) 에서 4) 를 도출해보자. 먼저 3) 을 가정했으므로 집합 $X = \bigcup_{i \in I}^{}X_i$ 의 선택함수 $h: 2 ^{X} \setminus \{\varnothing \} \to X$ 가 존재하는데, 함수 $g: I \to X$ 를 

    $$ g(i) = h(X_i) $$

    라 정의하자. 그러면 각 $i \in I$ 에 대하여 $g(i) = h(X_i) \in X_i$ 이므로 

    $$ g \in \prod_{i \in I}^{}X_i $$

    이다. ■ 

- 4) 에서 3) 를 도출하는 증명 

    4) 가 가정인 것에서 $\prod_{}^{}\{A:A \in 2 ^{X} \setminus \{\varnothing \}\} \neq \varnothing$ 이므로 
    
    $$ \exists h \text{ s.t. }\ h \in \prod_{}^{}\{A:A \in 2 ^{X} \setminus \{\varnothing \}\} $$

    이다. 그러면 각 $A \in 2 ^{X} \setminus \{\varnothing \}$ 에 대하여 $h(A) \in A$ 이므로 $h$ 는 $X$ 의 선택함수이다. ■ 

!!! tldr ""

    사슬(chain) : 순서집합 $X$ 의 부분집합 $A$ 가 다음을 만족하면 $A$ 를 $X$ 의 사슬이라 한다.

    $$ a, b \in A \implies a \leq b \lor a \geq b $$

- 즉 사슬 속의 서로 다른 두 원소는 항상 비교 가능하다.

- 예시 

    집합 $X$ 의 멱집합 $2 ^{X}$ 에 포함관계에 의한 순서를 부여하여 $A \subset B \iff A \leq B$ 라고 정의하자. $a,b,c \in X$ 에 대하여 

    $$ \{\{a\}, \{a,c\}\}, \quad \{\varnothing , \{a\},\{a,b\},\{a,b,c\},X\} $$

    등은 $2 ^{X}$ 의 사슬이고, $X$ 는 사슬의 상계이다.

!!! tldr ""

    반사슬(antichain) : 순서집합 $X$ 의 부분집합 $A$ 의 서로 다른 두 원소를 비교할 순서관계가 없을 때 $A$ 를 $X$ 의 반사슬이라 한다.

- 즉 반사슬 속의 서로 다른 두 원소는 비교 불가능하다.

!!! tldr ""

    극대원소(maximal element) : 순서집합 $X$ 의 원소 $m \in X$ 이 다음을 만족하면 $m$ 을 $X$ 의 극대원소라 한다.

    $$ x \in X, x \geq m \implies x = m $$

- 예시 

    사슬의 예시에서 순서집합 $2 ^{X}$ 의 극대원소는 $X$ 이다.

    한편 $\N$ 이나 $\mathbb{Z}$ 는 그 자체가 사슬이지만, 극대원소가 존재하지 않는다.

!!! tldr ""

    극소원소(minimal element) : 순서집합 $X$ 의 원소 $n \in X$ 이 다음을 만족하면 $n$ 을 $X$ 의 극대원소라 한다.

    $$ x \in X, x \leq n \implies x = n $$

## 초른의 보조정리

!!! tldr "정리 3.1.1"

    초른의 보조정리(Zorn lemma) : 공집합이 아닌 순서집합 $X$ 의 모든 사슬이 상계를 가지면 $X$ 는 극대원소를 가진다.

- 선택공리과 동치인 명제로써 수학의 여러 분야에서 널리 쓰인다.

## 하우스도르프 극대 원리

!!! tldr "정리 3.1.2"

    하우스도르프 극대 원리(Hausdorff maximal principle) : 임의의 순서집합은 극대 사슬을 가진다.

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

    우선 [초른 보조정리](#8e7118900)를 가정하자. 그리고 포함관계에 의한 순서를 부여받은 순서집합 $X$ 의 모든 사슬을 모은 순서집합 $\mathcal{C}(X)$ 에 [초른 보조정리](#8e7118900)를 적용해보고, [하우스도르프 극대 원리](#4f540f90d)가 도출되는지 보자. 

    [정리 "포함관계에 의하여 순서가 부여된 집합 $X$ 의 사슬의 집합 $\mathcal{C}(X)$ 의 사슬 $\mathcal{C}$ 에 대하여 모든 사슬 $\mathcal{C}$ 의 원소의 합집합 $\bigcup_{}^{}\mathcal{C} (\subset X)$ 은 $X$ 의 사슬이다."](#460d5f66d) 에서

    $$ C = \bigcup_{}^{}\mathcal{C} $$

    라고 두면 $C$ 는 $\mathcal{C}$ 들의 합집합이므로 $\mathcal{C} \subset \mathcal{C}(X)$ 의 상계임이 자명하다. 그러므로 순서집합 $\mathcal{C}(X)$ 는 [초른 보조정리](#8e7118900)의 가정을 만족하고, $\mathcal{C}(X)$ 는 [초른 보조정리](#8e7118900)의 귀결(극대원소를 가진다) 또한 만족한다. 이처럼 $\mathcal{C}(X)$ 이 [초른 보조정리](#8e7118900)를 만족하는데, 위의 증명이 보인 것은 $\mathcal{C}(X)$ 이 극대 사슬 $C$ 를 가진다는 것이다. 따라서 [초른 보조정리](#8e7118900)를 가정하면 [하우스도르프 극대 원리](#4f540f90d)가 성립한다. ■ 

- [하우스도르프 극대 원리](#4f540f90d)에서 [초른 보조정리](#8e7118900)를 도출하는 증명 

    $X$ 의 모든 사슬이 상계를 가진다고 가정하자. 그러면 [하우스도르프 극대 원리](#4f540f90d)에 의하여 $X$ 는 극대 사슬 $C$ 를 가지는데 가정에 의하여 이것의 상계 $m \in X$ 또한 존재한다. 이제 이 $m$ 이 극대원소임을 보이면 된다.

    먼저 $x \in X, x > m$ 이라고 가정하자. 그러면 $x$ 는 $C$ 의 임의의 원소와 비교 가능하고, 따라서 $C \cup \{x\}$ 도 사슬이다. 그런데 $C \subsetneq C \cup \{x\}$ 이므로 $C$ 가 극대사슬이라는 것에 모순이다. 따라서 $x$ 는 존재하지 않으며 $m$ 이 $X$ 의 극대원소가 된다. ■ 

!!! tldr "도움정리 3.1.3"

    순서집합 $X$ 의 부분집합족 $\mathcal{X} \subset 2 ^{X}$ 가 다음을 만족하면 $\mathcal{X}$ 는 극대원소를 가진다. 

    1. $A \in \mathcal{X}, B \subset A \implies B \in \mathcal{X}$

    2. $\mathcal{C}$ 이 $\mathcal{X}$ 의 사슬이면 $\bigcup_{}^{}\mathcal{C}\in \mathcal{X}$ 이다.

- [정리 "초른 보조정리는 하우스도르프 극대 원리와 동치이다."](#a4f694c36) 의 증명과정에서 살펴보았듯 포함관계에 의한 순서가 부여된 $X$ 의 사슬 집합 $\mathcal{C}(X)$ 는 본 정리의 두 가지 조건을 만족한다. 

    따라서 하우스드로프 극대 원리는 이 정리에서 바로 도출된다.

- 증명 

    조건 1), 2) 를 만족하는 $\mathcal{X}$ 가 존재할 때 극대원소가 존재함을 보이면 증명이 된다. 그러므로 $\mathcal{X}$ 이 존재한다고 하면, 조건 1) 에 의하여 $\mathcal{X}$ 는 임의의 원소 $A \in \mathcal{X}$ 의 모든 부분집합을 원소로 갖는다. 
    
    그러면 각 $A \in \mathcal{X}$ 에 대하여 

    $$ \tilde{A} = \{x \in X : A \cup \{x\}\in \mathcal{X}\} $$

    라고 하자. 그러면 임의의 $A \in \mathcal{X}$ 가 결정되었을 때 그 $A$ 의 원소인 $x \in X$ 에 대하여 $A \cup \{x\} \in \mathcal{X}$ 도 성립하므로 당연히 $A$ 의 모든 원소는 기본적으로 $\tilde{A}$ 에 속하고, 추가적으로 $A$ 를 포함하면서 $A$ 보다 큰 집합 $B (\supset A)$ 가 $\mathcal{X}$ 에 존재하면 $B \setminus A$ 의 원소들 또한 $\tilde{A}$ 에 속하게 될 것이다. 그러므로 먼저 자명하게 $A \subset \tilde{A}$ 이고, $A$ 가 $\mathcal{X}$ 의 극대 원소일 필요충분조건은 $A$ 보다 큰 집합이 없다는 것에서 $A = \tilde{A}$ 이다. ▲ 

    이제 집합 $X$ 의 선택함수 $h$ 를 택하고 함수 $g: \mathcal{X}\to \mathcal{X}$ 를 

    $$ g(A) = \begin{cases} A \sqcup \{h(\tilde{A}\setminus A)\} & A \subsetneq \tilde{A}\\ A & A = \tilde{A}\\ \end{cases} $$

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

    에 대하여 $(1)$ 을 보이려 한다. 이때 $(1)$ 의 첫째 조건은 자명하고, [정리 "포함관계에 의하여 순서가 부여된 집합 $X$ 의 사슬의 집합 $\mathcal{C}(X)$ 의 사슬 $\mathcal{C}$ 에 대하여 모든 사슬 $\mathcal{C}$ 의 원소의 합집합 $\bigcup_{}^{}\mathcal{C} (\subset X)$ 은 $X$ 의 사슬이다."](#460d5f66d) 에 의하여 $\mathcal{Y}$ 의 모든 사슬의 합집합 $\bigcup_{}^{}C$ 은 $\mathcal{Y}$ 의 사슬인데 $\mathcal{Y}$ 는 조건 2) 를 만족하므로 $(1)$ 의 셋째 조건도 자명하다. 

    둘째 조건을 보이기 위하여 $\forall A \in \mathcal{Y}_0$ 에 대하여 

    $$ A \subset C \lor g(C) \subset A \implies g(A) \subset C \lor g(C) \subset g(A) \tag{3} $$

    를 보이면 된다. 
    
    - $A = C$ 이면 $g(C) = g(A)$ 이므로 $(3)$ 이 성립한다.

    - $g(C) \subset A$ 이면 $g(C) \subset A \subset g(A)$ 이므로 성립한다. 

    - $A \subsetneq C$ 이면 $C$ 가 comparable element 이므로 $g(A) \subset C \lor C \subset g(A)$ 이다. 
    
        - $g(A) \subset C$ 이면 성립한다.
        
        - $C \subsetneq g(A)$ 이면 $A \subsetneq C \subsetneq g(A)$ 이므로 $g(A) \setminus A$ 가 두 개 이상의 원소를 갖는데(*$g(C), C$ 가 $g(A)$ 에 속하기 때문*), 이는 $g$ 의 정의에 의하여 불가능하다. (*왜냐하면 $g$ 는 $A$ 이거나 $A$ 이외에 다른 원소를 하나만 갖기 때문에 $g(A)\setminus A$ 의 원소의 갯수는 $0$ 이거나 $1$ 이기 때문.*) 그러므로 $C \subsetneq g(A)$ 은 모순이고, 반드시 $C \supset g(A)$ 이다.

    이로써 $(3)$ 이 증명되었고, 집합족 $\mathcal{U}$ 는 $(1)$ 을 만족한다. ▲ 

    집합족 $\mathcal{Y}_0$ 는 $(1)$ 을 만족하는 최소의 집합족인데 $\mathcal{U}\subset \mathcal{Y}_0$ 이므로 $\mathcal{U}=\mathcal{Y}_0$ 이다. 따라서 $\forall A \in \mathcal{Y}_0, A \subset C \subset g(C) \lor g(C) \subset A$ 이다. 즉, $g(C)$ 는 comparable element 라는 말이다. 집합 $C \in \mathcal{Y}_0$ 가 임의의 comparable element 이므로 $(2)$ 가 증명되었고 모든 증명이 끝났다. ■ 

- 이 정리로부터 하우스드로프 극대 원리를 도출하는 증명

# 정렬집합

!!! tldr ""

    정렬 집합(well ordered set) : 순서집합 $X$ 에서 $\forall A \in 2 ^{X}$ 에 대하여 $A \neq \varnothing$ 인 $A$ 가 최소 원소를 가지면 $X$ 를 정렬집합이라고 한다. 

- 정렬 집합의 순서관계를 정렬 순서라 한다. 

- [정리 2.1.4](../numbers#5efd87f3f) 는 자연수집합 $\N$ 이 정렬 집합임을 말해준다.

- 정렬 집합은 그 자체로서 사슬이 된다.

!!! tldr ""

    정렬 순서(well ordered) : 정렬 집합이 갖는 순서관계이다.

## 체르멜로 정렬정리

!!! tldr "정리 3.1.4"

    체르멜로 정렬정리(Well-ordering theorem, Zermelo's theorem) : 임의의 집합에는 정렬순서가 존재한다.

- 아래의 증명은 [초른 보조정리](#8e7118900)를 사용하는데 이는 [초른 보조정리](#8e7118900)가 적용되는 대표적인 사례이다.


- 증명

    먼저 $X$ 의 부분집합 $A$ 와 $G \subset A \times A$ 로써 $A$ 의 정렬순서를 부여해주는 관계들의 순서쌍 $(A,G)$ 를 생각하고, 이런 순서쌍 전체 집합을 $\mathcal{X}$ 라 두자. 이때 $(A,G), (B,H) \in \mathcal{X}$ 가 

    $$ A \subset B, \quad G \subset H, \quad x \in A, y \in B \setminus A \implies (x, y) \in H $$

    를 만족할 때 $(A, G) \leq (B, H)$ 라 정의하면 순서관계가 됨을 바로 확인할 수 있다.

    순서집합 $\mathcal{X}$ 에 [초른 보조정리](#8e7118900)를 적용하기 위하여 $\mathcal{C}$ 가 $\mathcal{X}$ 의 사슬이라고 하고 

    $$ A_0 = \bigcup_{}^{}\{A \subset X:(A,G) \in \mathcal{C}\} $$

    $$ G_0 = \bigcup_{}^{}\{G \subset X \times X:(A,G) \in \mathcal{C}\} $$

    라 두자. 이제 $(A_0, G_0) \in \mathcal{X}$ 임을 보이려 하는데 먼저 $G_0$ 가 $A_0$ 의 순서관계임을 보이려 한다. ▲ 

    만약 $x \in A_0$ 이면 $\exists  (A, G) \in \mathcal{C} \text{ s.t. }\ x \in A$ 이다. 이때 $G$ 는 $A$ 의 정렬순서를 부여하므로 순서관계도 부여한다. 따라서 순서관계의 조건 1) 에 의하여 $x \in A \subset  A_0 \implies (x, x) \in G \subset G_0$ 이다. $A$ 와 $G$ 가 순서관계 조건 1) 을 만족하는 것에서 $x \in A_0 \implies (x, x) \in \subset G_0$ 을 도출했으므로 $A_0$ 와 $G_0$ 는 순서관계 조건 1) 을 만족한다.

    순서관계 조건 2) 를 보이기 위하여 $x, y \in A_0, (x, y) \in G_0, (y, x) \in G_0$ 을 가정하자. 그러면 $(x, y)$ 와 $(y, x)$ 라는 순서관계도 어떤 집합에 속하게 되므로 $(x, y) \in G$ 와 $(y, x) \in H$ 라고 하자. 그러면 $(A, G), (B, H) \in \mathcal{C}$ 가 존재한다. 이때 $\mathcal{C}$ 가 사슬이므로 $(A, G) \leq (B, H) \lor (A, G) \geq (B, H)$ 이다. 어느 경우에나 $(x,y)$ 와 $(y,x)$ 는 $G \cup H = (A \cup B) \times (A \cup B)$ 에 속하게 된다. 그런데 $G \cup H$ 는 $A \cup B$ 의 모든 원소의 순서관계를 잘 부여하는데 순서관계의 조건 2) 에 의하여 $(x, y) \in G \cup H, (y, x) \in G \cup H \implies x = y$ 이다. 이로써 $x = y$ 가 도출되었고, $G_0$ 이 $A_0$ 에 대한 순서관계 2) 를 만족한다는 것이 증명되었다.

    마지막으로 순서관계 3) 이 성립함을 보여야하는데, $(x, y) , (y, z) \in G_0$ 를 가정하면, 이번에도 $(x, y) \in G$ 이고 $(y, z) \in H$ 인 $(A, G), (B, H) \in \mathcal{C}$ 가 존재하므로 순서관계 2) 를 증명했던 것과 마찬가지의 방법으로 $(x, z) \in G_0$ 이 증명된다. 

    그러므로 $G_0$ 는 $A_0$ 의 순서관계이다. ▲ 

    이제 $G_0$ 가 $A_0$ 의 정렬순서임을 보이려 한다. $\varnothing \neq B \subset A_0$ 라 하면 $(A, G) \in \mathcal{C}$ 가 존재하여 $B \cap A \neq \varnothing$ 을 만족한다. 이때 $\varnothing \neq B \cap A \subset A$ 이고, $G$ 가 $A$ 의 정렬순서이므로 $B \cap A$ 는 최소 원소 $b$ 를 가진다. 이러한 최소원소 $b$ 는 모든 원소 $\forall a \in B \cap A$ 에 대하여 $b \leq a \iff (b, a) \in G$ 를 만족하므로 

    $$ b \in B \cap A, \quad a \in B \cap A \implies (b, a) \in G $$

    이다. 이제 $b \in B$ 가 $B (\subset A_0)$ 의 최소 원소임을 보이려 한다. 즉, 

    $$ x \in B \implies (b, x) \in G_0 $$

    임을 보이려 한다. $x \in B$ 가 가정이므로 $x \in A$ 이면 $x \in B \cap A$ 이다. 그러므로 $(b, x) \in G \subset G_0$ 이다. 만약 $x \not\in A$ 이면 적절한 $(C, K) \in \mathcal{C}$ 에 대하여 $x \in C$ 인데, $x \in C \setminus A$ 이므로 $C \not \subseteq A$ 이다. 따라서 $(C, K) \not \leq (A, G)$ 인데 $\mathcal{C}$ 가 사슬이므로 $(A, G) \leq (C, K)$ 이다. 그런데 $b \in A \land x \in C \setminus A$ 이므로 $(A, G) \leq (C, K)$ 의 정의에 의하여 $(b, x) \in K \subset G_0$ 이다. 이로써 $b$ 가 $B$ 의 최소원소임이 증명되었다. ▲ 

    이제 $(A_0, G_0) \in \mathcal{X}$ 가 $\mathcal{C}$ 의 상계임을 보이려 하는데 방금 증명한 방법과 비슷하기에 생략한다. ▲ 

    지금까지 순서집합 $\mathcal{X}$ 가 [초른 보조정리](#8e7118900)의 가정부를 만족함을 보였다. 그러므로 $\mathcal{X}$ 는 극대원소 $(D, L) \in \mathcal{X}$ 을 가진다. 이제 $D=X$ 임을 보일 것이다. $D \subsetneq X$ 이면 $x \in X \setminus D$ 를 잡고 

    $$ E = D \cup \{x\}, \quad M = L \cup \{(a,x):a \in D\} \cup \{(x,x)\} $$

    라 두자. 그러면 $M$ 은 $E$ 의 순서관계가 되는데 $x$ 는 임의의 $a \in D$ 보다 큰 원소이다. 따라서 $(E,M)$ 은 정렬집합이고 $(E,M) \in \mathcal{X}$ 인데 $(E,M)>(D,L)$ 이다. 이는 $(D,L)$ 이 극대원소라는데 모순이므로 $D=X$ 이고 $L$ 은 $X$ 에 정의된 정렬순서이다. ■ 

!!! tldr ""

    선택공리, 초른 보조정리, 하우스도르프 극대 원리, 체르멜로 정렬정리는 서로 동치이다.

- 증명 

    [체르멜로 정렬정리](#0d9cd4880) 를 가정하면 선택공리를 쉽게 얻을 수 있다. 

    집합 $X$ 가 정렬집합일 때 임의의 $A \in 2 ^{X}\setminus \{\varnothing \}$ 에 대하여 $A$ 의 최소원소를 $h(A)$ 라 하면 

    $$ h: 2 ^{X}\setminus \{\varnothing \} \to X $$

    는 선택함수이다. 그러므로 선택공리, [초른 보조정리](#8e7118900), [하우스도르프 극대 원리](#4f540f90d), [체르멜로 정렬정리](#0d9cd4880)가 모두 동치임을 알 수 있다. ■ 

## 절편

!!! tldr ""

    정렬집합의 절편(segment) : 정렬집합 $A$ 와 $x \in A$ 에 대하여 다음을 $x$ 에 의한 $A$ 의 절편이라 한다.

    $$S_x = \{a \in A: a < x\}$$ 

- 절편은 정렬집합이다.

- 예시 

    $$ \forall n \in \omega , S_n = n $$

    $$ \forall m \in n, S_m = m $$

- 예시 

    $\R$ 의 한 절편은 $S_0 = (- \infty , 0)$ 이다.

    $\N$ 의 한 절편은 $S_3 = \{1,2\}$ 이다.

!!! tldr ""

    서로소 집합의 순서 : 서로소인 두 정렬집합 $A, B$ 에 대하여 합집합 $A \sqcup B$ 에 대하여 다음을 $x \leq y$ 라고 정의한다.

    $$ (x, y \in A : x \leq y) \lor (x, y \in B : x \leq y) \lor (x \in A, y \in B) $$
    
- 그러면 이 관계는 정렬순서가 된다.

    - 증명 

- $A \sqcup B$ 와 $B \sqcup A$ 는 집합으로서는 같지만 순서집합으로서는 다르다.

    - 예시 

        $\omega \sqcup \{x\}$ 에서는 맨 뒤에 있는 $x \in \{x\}$ 가 최대 원소이다. 하지만 $\{x\} \sqcup \omega$ 에는 최대원소가 없다. 직관에 어긋나지만, $\{x\} \sqcup \omega$ 와 $\omega$ 는 같은 순서집합이다. 

        $$ \begin{equation}\begin{split} \omega : & 0, 1, 2, 3, \dots\\ \{x\} \sqcup \omega : & x, 0, 1, 2, \dots\\ \omega \sqcup \{x\} : & 0, 1, 2, 3, \dots, x \end{split}\end{equation} \tag*{} $$

!!! tldr ""

    증가함수(increasing function) : 순서집합 $A, B$ 사이에 정의된 함수 $f: A \to B$ 가 다음을 만족하면 증가함수라 한다.

    $$ x, y \in A, x \leq y \implies f(x) \leq f(y) $$

- 증가함수는 단조 함수(monotonic function)인데 단조함수는 주어진 순서를 보존하는 함수이다. 

- 이러한 함수 $f$ 에 대하여 $f$ 가 단조 증가(monotonically increasing) 한다고 한다.

## 순서동형

!!! tldr ""

    순서 동형(order isomorphism) : 순서집합 $A, B$ 에 정의된 전단사 함수 $f: A \to B$ 가 증가함수이고 그 역함수 $f ^{-1}$ 도 증가함수이면 $A$ 와 $B$ 는 순서동형이다. 

- **두 순서 동형 집합 $A,B$ 를 $A \approxeq B$ 와 같이 표기한다.**

- 순서동형은 부분순서 집합의 동형(isomorphism)이란 무엇인지 정의해준다. 두 부분순서 집합이 순서동형이라면 두 집합은 본질적으로 같은 것으로 여겨진다. 왜냐하면 한 집합의 원소들이 이루는 순서를 다른 집합으로부터 완전히 구성할 수 있기 때문이다.

- 예시 

    다음과 같이 정의된 함수 $f: \{x\} \sqcup \omega \to \omega$ 는 전단사 함수이고 증가함수 이므로 순서동형을 정의해준다. 

    $$ f(a) = \begin{cases} 0 & a = x\\ a + 1 & a \in \omega \\ \end{cases} , \qquad f ^{-1} (a) = \begin{cases} x & a = 0\\ a - 1 & a > 0 \\ \end{cases} $$

    이로써 $\{x\}\sqcup \omega$ 와 $\omega$ 가 순서동형이고, 본질적으로 서로 같은 집합임을 알 수 있다.

!!! tldr ""

    사전순서(lexicographical order) : 순서집합 $A,B$ 의 곱집합 $A \times B$ 의 두 원소 $(a_1, b_1) \in A \times B, (a_2, b_2) \in A \times B$ 에 대하여 다음이 성립할 때 $(a_1, b_1) \leq (a_2, b_2)$ 라고 정의된 순서를 사전순서라 한다.

    $$ a_1 < a_2 \lor (a_1 = a_2 \land b_1 \leq b_2) $$

!!! tldr ""

    반사전순서(anti-lexicographical order) : 순서집합 $A,B$ 의 곱집합 $A \times B$ 의 두 원소 $(a_1, b_1) \in A \times B, (a_2, b_2) \in A \times B$ 에 대하여 다음이 성립할 때 $(a_1, b_1) \leq (a_2, b_2)$ 라고 정의된 순서를 사전순서라 한다.

    $$ b_1 < b_2 \lor (b_1 = b_2 \land a_1 \leq a_2) $$

- $A,B$ 가 정렬집합이면 $A \times B$ 에 정의된 사전순서나 반사전순서는 모두 정렬순서이다.

- 한편, 아래의 논의에서부터는 정렬집합의 곱집합에는 반사전순서가 부여된 것으로 간주하자.

- 예시 

    정렬집합의 곱하기에는 교환법칙이 성립하지 않는다.

    가령 $X = \{x,y\}$ 일 때 $\omega \times X$ 의 순서는 

    $$ (0, x), (1, x), (2, x), \dots, (0, y), (1, y), (2, y), \dots $$

    로써 $\omega$ 가 $n \in \omega$ 에 대한 $(n, x)$ 형태의 튜플에 모두 대응되어 순서동형일 수 없다. 하지만 $X \times \omega$ 의 순서는 

    $$ (x, 0), (y, 0), (x, 1), (y, 1), (x, 2), (y, 2), \dots $$

    로써 $\omega$ 와 순서동형이다. 왜냐하면 증가함수이면서 전단사함수인 $f: \omega \to X \times \omega$ 가 존재하기 때문이다. 

    $$ f(n) = \begin{cases} \bigg (x, \dfrac{n}{2}\bigg ) & n \text{ is even }\\ \bigg (y, \dfrac{n-1}{2}\bigg ) & n \text{ is odd } \end{cases} , \quad f ^{-1}(a, b) = \begin{cases} 2b & a = x\\ 2b+1 & a = y \end{cases} $$
    
    그러므로 

    $$ \omega \approxeq X \times \omega, \quad \omega \not \approxeq \omega \times X $$

    이다.

!!! tldr "정리 3.3.1"

    두 정렬집합 $A, B$ 가 주어지면 다음 중 하나가 성립한다. 

    1. $A \approxeq B$

    2. $b \in B : A \approxeq S_b$

    3. $a \in A : S_a \approxeq B$

- 이 정리는 쉽게 말해서 두 정렬집합을 비교할 때, 두 정렬집합이 서로 같거나 어느 한쪽이 다른 쪽의 절편이 됨을 말해준다. 

- 증명 

    먼저 집합 $B$ 의 $p, q \in B$ 에 대한 절편 $S_q, S_p$ 에 대하여 

    $$ f: S_q \to S_p \text{ 가 증가 단사함수 } \implies q \leq p \tag{1} $$

    를 증명하자. 이를 위하여 $f$ 가 증가 단사함수임에도 $p<q$ 라고 해보자. 이때 

    $$ P = \{x \in S_q: f(x) < x\} $$

    라 정의하면 $P \neq \varnothing \implies \exists m \text{ s.t. }\ m = \min P$ 이다. 그런데 $f(m) < m \implies f(f(m))<f(m)$ 이므로 $f(m) \in P$ 인데 $f(m) < m$ 이므로 $m$ 이 최소원소라는 것에 모순이다. 그러므로 $P = \varnothing$ 이고, $p<q$ 에서 $p \in S_q \setminus P$ 이므로 $f(p) \geq p$ 이다. 그러므로 $f(p) \not\in S_p$ 인데, $\text{Cdm} (f) = S_p$ 이므로 모순이다. 그러므로 $(1)$ 이 증명되었다. ▲ 

    한편 그러므로 $(1)$ 에 의하여 

    $$ p, q \in B, S_p \approxeq S_q \implies p = q \tag{2} $$

    임이 자명하다. ▲ 

    이제 정렬집합 $A$ 의 부분집합 $C$ 를 (*이때 $x \in X$ 에 대한 절편 $S_x$ 는 $X$ 의 절편이고, $y \in Y$ 에 대한 절편 $S_y$ 는 $Y$ 의 절편인 것 같다. 표기가 조금 헷갈리네. $S _{x \in X}, S _{y \in Y}$ 로 표기했으면 안헷갈렸을텐데.*)

    $$ C = \{x \in A : \exists p \in B \text{ s.t. }\  S_x \approxeq S_p  \} $$

    와 같이 정의하자.(*그러면 이 $C$ 는 만약 $A$ 가 $B$ 보다 클 경우 $B$ 의 사이즈에 맞는 $A$ 절편이 되고, $A$ 가 $B$ 보다 작을 경우 그냥 $A$ 가 될 것 같은데. 맞나?*) 또 함수 $\phi : C \to B$ 를 정의하는데 $(2)$ 에 의하여 $x \in A$ 에 대하여 $S_x \approxeq S_p \land S_x \approxeq S_q$ 라면 $S_p \approxeq S_q$ 이므로(*이로써 한 입력이 두 출력을 갖지않음이 보장됨*) 함수 $\phi$ 를
    
    $$ \phi (x) = p \quad (\impliedby x \in C \land S_x \approxeq S_p) $$
    
    라 정의할 수 있다.(*이때 $S_x$ 는 $C$ 의 절편이고 $S_p$ 는 $B$ 의 절편이며, 두 절편이 순서동형이라는 것은 두 절편의 크기가 같다는 말인 것 같다. 그러면 $\phi$ 함수는 한 절편의 원소에 대응되는 다른 절편의 원소로 가는 단사함수지.*) 그러면 이 함수 $\phi$ 는 단사함수가 된다. 왜냐하면 $\phi (x) = \phi (y) = p \implies S_x \approxeq S_p \approxeq S_y$ 인데 $(2)$ 에 의하여 $x = y (= p)$ 이기 때문이다. 이제 

    $$ x, y \in C, x \leq y \implies \phi (x) \leq \phi (y) \tag{3} $$

    이 성립함을 보일 것이다. $f : S_x \to S _{\phi (x)}, g: S_y \to S _{\phi (y)}$ 가 순서동형을 정의하므로 $f, g$ 는 전단사함수이며 증가함수이고 그 역함수 $f ^{-1}, g ^{-1}$ 도 증가함수이다. 그러면 $x \leq y$ 이므로 포함함수 $\iota : S_x \hookrightarrow S_y$ 가 존재하고, 합성함수 

    $$ g \circ \iota \circ f ^{-1}: S _{\phi (x)} \to S _{\phi (y)} $$

    는 증가 단사함수이다. 왜냐하면 $f ^{-1}$ 는 증가함수이고, $\iota$ 는 항등함수(포함함수)이고, $g$ 는 증가함수이기 때문에 결국 이 합성함수는 증가함수이다. 그런데 이때 $(1)$ 에 의하여 $\phi (x) \leq \phi (y)$ 가 증명되고, 이로써 함수 $\phi : C \to \phi (C)$ 는 순서동형을 정의한다는 것을 알 수 있다. (*$B$ 가 아닌 새로운 공역 $\phi (C)$ 로 정의된 $\phi : C \to \phi (C)$ 는 전사함수이다. 왜냐하면 공역으로의 $\phi (C)$ 가 치역 $\phi (C)$ 와 같기 때문이다. $\phi$ 가 단사함수임은 이미 살펴보았으므로 $\phi$ 는 전단사함수이고, 또한 증가함수이므로 $\phi$ 는 순서동형을 정의한다.*) ▲ 

    이제 $C = A$ 이거나 $C$ 는 $A$ 의 절편임을 보이자. 이를 위하여 

    $$ x \in A, y \in C, x < y \implies  x \in C \tag{4} $$

    임을 보일 것이다. 먼저 $y \in C$ 이므로 순서동형 $g : S_y \to S _{\phi (y)}$ 가 존재한다.(*$y$ 에 의한 $C$ 의 절편과 순서동형인 $B$ 의 절편 $S _{\phi (y)}$ 을 만들 수 있다는 거지.*) 한편 $x<y$ 이므로 $S_x \subset S_y$ 인데 $g(S_x) = S _{g(x)}$ 임을 보이자. 만일 $z \in S_y$ 이면 (*$g(z)<g(x)$ 라는 것은 $g(x)$ 에 의하여 생성된 절편에 $g(z)$ 가 포함됨을 뜻하므로*)

    $$ z \in S_x \iff z<x \iff g(z)<g(x) \iff g(z) \in S _{g(x)} $$

    이다. 이는 $S_x$ 에 속하는 임의의 원소 $z$ 에 대하여 $g(z)$ 는 $S _{g(x)}$ 에 속한다는 것이고, 그 역도 성립한다는 것이다. 그러므로 임의의 원소 $z \in S_x$ 에 대한 $g(z)$ 를 집합 전체로 $g(S_x)$ 라고 표현하면 $g(S_x) \subset S _{g(x)}$ 인데 그 역도 성립하므로 $g(S_x) \supset S _{g(x)}$ 이다. 따라서 $g(S_x) = S _{g(x)}$ 인데, $g$ 의 제한 

    $$ g | _{S_x} : S_x \to g(S_x) $$

    은 전사함수이므로 함수 $g$ 처럼 순서동형을 정의한다. 따라서 $g | _{S_x} : S_x \to S _{g(x)}$ 도 순서동형을 정의한다. 따라서 $x \in C$ 이다.(*대충 이런 뜻인 것 같은데. $y$ 로 형성된 절편 $S_y$ 와 순서동형인 $S _{\phi (y)}$ 을 만들 수 있고, 이렇게 만들어주는 함수 $g:S_y \to S _{\phi (y)}$ 를 만들었어. 근데 $x<y$ 이면 $g$ 를 $S_x$ 에 제한한 함수 $g| _{S_x}:S_x \to S _{g(x)}$ 를 만들 수 있더라. 그러니까 $x \in C$ 이다 라는 것 같은데.*) ▲ 

    일반적으로 정렬집합 $A$ 의 부분집합 $C$ 가 $(4)$ 를 만족하면 자동으로 $C=A$ 이거나 $C$ 는 $A$ 의 절편이 된다. 이를 보이기 위하여 $C \subsetneq A$ 라 하면 $A \setminus C$ 는 최소 원소 $l$ 을 갖는다. 이 경우 $C = S_l$ 인데, 이것을 보이자. 만약 $x \in S_l$ 이면 $x<l$ 이므로 $x \in C$ 이다. 왜냐하면 $x \in A \setminus C$ 이면 $l$ 이 $A \setminus C$ 의 최소원소라는데에 모순이기 때문이다. 그러므로 

    $$ x \in S_l \implies x \in C $$

    이다. 반대로 $x \in C$ 라고 하면 $l \leq x$ 일 때 $(4)$ 에 의하여 $l \in C$ 인데 이것도 $l$ 이 $A \setminus C$ 의 최소 원소라는데 모순이다. 따라서 $x \in C$ 이면 $l > x$, 즉 $x \in S_l$ 이다. 그러므로

    $$ x \in C \implies x \in S_l $$

    이다. 따라서 $x \in C \iff x \in S_l$ 이므로 $C = S_l$ 이 증명되었다. 그러므로 $l$ 의 값에 따라서 $C = A$ 이거나 $C$ 는 $A$ 의 절편이 된다. ▲ 

    마찬가지로 $\phi (C) = B$ 이거나 $\phi (C)$ 는 $B$ 의 절편이다. 그러므로 다음 네 가지 경우가 생긴다. 

    1. $C = A, \phi (C) = B$

    2. $C = A, \phi (C)$ 는 $B$ 의 절편이다.

    3. $C$ 는 $A$ 의 절편이고, $\phi (C) =B$ 이다.

    4. $C$ 는 $A$ 의 절편이고, $\phi (C)$ 는 $B$ 의 절편이다.

    $\phi : C \to \phi (C)$ 가 순서동형을 정의하는 것을 보였기에 d) 만 일어나지 않음을 보이면 모든 증명이 끝난다.

    이를 위하여 $x \in A, p \in B$ 에 대하여 $A$ 의 절편으로써의 $C = S_x$, $B$ 의 절편으로써의 $\phi (C) = S_p$ 라고 하자. 그러면 $C \approxeq \phi (C)$ 이므로 $S_x \approxeq S_p$ 이다. 그런데 $(4)$ 를 가정했으므로 이는 $x \in C = S_x$ 임을 뜻한다. 즉, $x < x$ 를 뜻하는데 이는 모순이다. 그러므로 d) 는 발생하지 않는다. 그러므로 모든 증명이 끝났다. ■ 

- 아, 문장이 중의적이어서 착각했던 거구나.    

    1. $A$ 와 $B$ 는 순서동형이다.

    2. $A$ 는 $B$ 의 절편과 순서동형이다.

    3. $B$ 는 $A$ 의 절편과 순서동형이다.

    여기에서 $A$ 는 $B$ 의 "절편" 과 "순서동형" 이다 가 아니라 $A$ 는 "$B$ 의 절편" 과 순서동형이다 라고 해석해야하구나. 역시 자연어로 쓰니까 이런 일이 발생하구나. 최대한 기호로 써야겠네.

!!! note

    집합론과 수체계를 공부하다보니 이러한 증명들이 완전하게 형식화되어 있어서 문득 이해하기 어렵지만, 실상 이 증명을 떠올린 수학자들은 오로지 무모순의 제약만 걸려있는 자유롭고 자유로운 상상의 세계에서 증명을 떠올렸지 않았을까. 그러면 내가 할 일은 그 자유로운 세계에서 떠올린 핵심 아이디어이다. 그것은 이러한 형식문처럼 딱딱하고 이해하기 어렵지 않다. 실상은 그러한 직관이 통찰한 핵심 아이디어를 엄밀하게 전달하기 위하여 이러한 딱딱한 형식문으로 형식화한 것이기 때문에, 내가 알아야 할 것은 수학자들이 원래 떠올렸던 직관이다. 

# 서수

!!! tldr ""

    순서수, 서수(ordinal) : 정렬집합 $\alpha$ 가 다음을 만족하면 서수라고 한다. 

    $$ \xi \in \alpha \implies S _{\xi } = \xi $$

- 서수란 집합에 순서를 부여하기 위하여 고안된 개념이다. 유한집합이나 가산 무한집합에 순서를 부여하기 위해서는 자연수만으로 충분하지만, 비가산 집합에 순서를 부여하기 위해서는 자연수만으로 불충분하다. 이것을 해결하기 위하여 자연수를 포괄하면서 순서가 주어진 수체계가 필요했는데 그것이 서수이다.

    - 서수란 쉽게 말해 정렬 전순서 집합의 "길이" 를 측정하기 위하여 고안된 수이다.

- 임의의 유한 정렬집합 $X$ 는 어떤 자연수 $n$ 과 유일하게 순서동형이다. 가령 $X = \{a, x, j\} \approxeq 3 = \{0, 1, 2\}$ 이다. 이때 $\text{ord }(X) = 3$ 이라고 한다. 즉, 임의의 유한 정렬집합 $X$ 의 서수를 

    $$ \text{ord }(X) $$

    라고 쓴다. 

- 서수 $\alpha$ 의 원소는 $\alpha$ 의 부분집합이다. 

    - 예시 

        $\beta \in \alpha$ 이면 $\beta  = S _{\beta } \subset \alpha$ 이다.

!!! tldr ""

    $$ \text{ord }(\N) = \omega $$
    
- 이제 자연수 집합 $\N$ 의 서수를 $\omega$ 라고 쓴다. 

- 예시 

    자연수 전체의 정렬집합 $\omega$ 는 서수이다. $n \in \omega \implies  S_n = n$ 이기 때문이다.
    
    각 자연수 $n \in \omega$ 도 서수이다. $m \in n \implies  S_m = m$ 이기 때문이다.

!!! tldr ""

    절대적 무한(Absolute Infinite) : 이보다 더 큰 수가 존재하지 않는 무한수이다.

- 절대 무한을 $\Omega$ 라고 표기한다.

- 초한수 수열 $\aleph _0, \alpha _1, \alpha _2, \dots$ 을 극한으로 보낼 수 있고, $\alpha _{\alpha _0}, \alpha _{\alpha _1},\alpha _{\alpha _2},  \dots$ 수열도 극한으로 보낼 수 있는데, 이 과정 자체를 극한으로 보내면 $\Omega$ 에 도달할 수 있다.

!!! tldr ""

    초한수(Transfinite number) : 절대적 무한이 아닌 무한이다.

- 모든 유한수는 기수와 서수로 표현할 수 있는데 기수는 집합의 크기를 나타내고, 서수는 정렬집합에서의 순서 길이를 나타낸다.

- 자연수의 초한서수를 $\omega$, 초한기수를 $\aleph_0$ 으로 나타낸다.

!!! tldr ""

    유한서수 : 자연수 $0,1,2,3,\dots$ 는 서수인데 이들을 유한서수라고 한다.

## 초한서수

!!! tldr ""

    초한서수(Transfinite ordinal number), 초유한서수 : 무한 정렬 집합에서의 어떤 위치를 나타내는 수이다.

- 가장 작은 초한서수는 자연수 집합 $\N$ 을 정렬집합으로 이해할 때의 

    $$ \omega $$

    이다. 이는 아래에서 살펴보듯이 자연수 집합을 서수로서 사용할 때 $\omega$ 로 쓴다.

- 초한 서수를 다음과 같이 열거할 수 있다. 

    $$ \omega , \omega +1, \omega +2, \dots, \omega 2, \omega 2+1, \omega 2+2,\dots, \omega 3, \omega 3+1,\dots $$

    마찬가지로

    $$ \omega , \omega 2, \omega 3, \dots, \omega ^{2} $$

    을 얻고, 이런식으로 반복하면

    $$ \omega ^{2} + 1, \omega ^{2} + 2, \dots, \omega ^{2} + \omega , \omega ^{2} + \omega + 1, \omega ^{2} + \omega + 2, \omega ^{2} + \omega 2, $$

    $$ \omega ^{2}+ \omega 2+1, \omega ^{2}+ \omega 3, \dots, \omega ^{2}+ \omega 4, \omega ^{2}2, \dots, \omega ^{3}, \dots, \omega ^{4}, \dots $$

    $$ \omega ^{\omega }, \dots, \omega ^{\omega ^{\omega } }, \dots, \omega ^{\omega ^{\omega ^{\omega } } }, \dots, \epsilon_0, \epsilon_0 + 1, \epsilon_0 + 2, \dots, \epsilon_0 + \omega , $$

    $$ \epsilon_0 + \omega 2 , \dots, \epsilon_0 + \omega ^{2} , \dots, \epsilon_0 + \omega ^{\omega } , \dots, \epsilon_0 2, \dots, \epsilon_0 \omega, \epsilon_0 \omega ^{\omega } ,\dots, \epsilon_0 ^{2} \dots $$

    와 같이 계속 된다. $\epsilon_0$ 은 엄밀하게 

    $$ \epsilon _0 = \sup \{0, \omega ^{0}=1, \omega ^{1}=\omega , \omega ^{\omega }, \omega ^{\omega ^{\omega }}, \dots\} $$

    와 같이 정의되며, 

    $$ \omega ^{\alpha } = \alpha \tag{1} $$
    
    를 만족하는 가장 작은 $\alpha$ 로 여겨진다. $\epsilon _1$ 는 $(1)$ 를 만족하는 두번째 $\alpha$ 이다. $\epsilon _1$ 는 $\epsilon _0$ 처럼 $0$ 부터 시작하는 수열의 상한이 아닌 $\epsilon _0+1$ 부터 시작하는 수열의 상한

    $$ \epsilon _1 = \sup \{\epsilon _0 + 1, \omega ^{\epsilon _0 + 1}, \omega ^{\omega ^{\epsilon _0 + 1}}, \dots\} $$

    으로 정의된다. 이때 

    $$ \omega ^{\epsilon _0 + 1} = \omega ^{\epsilon _0} \omega $$

    $$ \omega ^{\omega ^{\epsilon _0 + 1}} = \omega ^{\epsilon _0 \omega } = (\omega ^{\epsilon _0})^{\omega }=\epsilon _0 ^{\omega } $$

    $$ \omega ^{\omega ^{\omega ^{\epsilon _0 + 1}}} = \omega ^{\epsilon _0 ^{\omega }} = \omega ^{\epsilon _0 ^{1 + \omega }} = \omega ^{\epsilon _0 \epsilon _0 ^{\omega }} = (\omega ^{\epsilon _0}) ^{\epsilon _0 ^{\omega }} = \epsilon _0 ^{\epsilon _0 ^{\omega }} $$

    이므로 $\epsilon _1$ 을 다음과 같은 수열의 상한으로도 정의할 수 있다.

    $$ \epsilon _1 = \sup \{0,1,\epsilon _0, \epsilon _0 ^{\epsilon _0}, \epsilon _0 ^{\epsilon _0 ^{\epsilon _0}}, \dots\} $$

    일반적으로 엡실론 수 $\epsilon _{\alpha +1}$ 은 다음과 같이 정의된다.

    $$ \begin{equation} \begin{split}   \epsilon _{\alpha +1} &= \sup \{\epsilon _{\alpha }+1, \omega ^{\epsilon _{\alpha } + 1}, \omega ^{\omega ^{\epsilon _{\alpha } + 1}}\}\\ &= \sup \{0, 1, \epsilon _{\alpha }, \epsilon _{\alpha } ^{\epsilon _{\alpha }}, \epsilon _{\alpha } ^{\epsilon _{\alpha } ^{\epsilon _{\alpha }}}\} \end{split} \end{equation} \tag*{} $$

    이때 다음과 같이 엡실론 수의 수열의 극한 으로 $\epsilon _{\omega }$ 을 얻는다.

    $$ \epsilon _{\omega } = \sup \{\epsilon _0, \epsilon _1, \epsilon _2, \dots\} $$

    비슷한 방식으로 $\epsilon _{\epsilon _0}$ 을 정의할 수 있고, 이를 기반으로 $\zeta _0$ 를 다음과 같이 정의한다.

    $$ \zeta _0 = \sup \{0, \epsilon _0, \epsilon _{\epsilon _0}, \epsilon _{\epsilon _{\epsilon _0}}, \dots\} $$

    $\epsilon _0$ 이 최초로 $\omega ^{\alpha } = \alpha$ 를 만족하는 서수라는 것과 같이 $\zeta _0$ 는 최초로 $\epsilon _{\alpha } = \alpha$ 를 만족하는 서수이다. 
    
    그러나 그리스 알파벳은 초한서수들을 모두 나타내기에 부족하므로 초한서수들을 나타내기에 적합한 강력한 표현법인 [Veblen function](https://en.wikipedia.org/wiki/Veblen_function) 이 고안되었다. 이 함수는 $\varphi _{\gamma }(\beta )$ 의 형태로 초한귀납적으로 정의되어 초깃값으로 $\varphi _0(\beta ) = \omega ^{\beta }$ 을 정의한 후 $\varphi _1(\beta ) = \epsilon _{\beta }, \varphi _2(\beta ) = \zeta _{\beta }, \dots$ 와 같이 정의 된다.

!!! tldr ""

    극한서수(limit ordinal) : 서수 $\alpha$ 가 $\alpha = \beta ^{+}$ 인 $\beta$ 를 가지지 않으면 $\alpha$ 를 극한서수라고 한다. 

- 가령 $\omega$ 는 $\omega = \alpha ^{+}$ 인 $\alpha$ 가 존재하지 않으므로 극한서수이다.

!!! tldr ""

    서로소 집합 함수 : $g: A \to C, h: B \to D$ 에 대하여 함수 $g \sqcup h : A \sqcup B \to C \sqcup D$ 를 다음과 같이 정의한다.

    $$ (g \sqcup h) (x) = \begin{cases} g(x) & x \in A\\ h(x) & x \in B\\ \end{cases} $$

- $g,h$ 가 순서동형을 정의한다면 $g \sqcup h$ 도 순서동형을 정의한다.

## 서수의 덧셈과 곱셈

!!! tldr ""

    서수의 더하기 : $\text{ord }(A) = \alpha , \text{ord }(B) = \beta$ 인 서로소인 정렬집합 $A, B$ 에 대하여 다음과 같이 정의한다.

    $$ \alpha + \beta = \text{ord }(A \sqcup B) $$

- 이때 $A \sqcap B$ 의 정렬순서는 정의 "서로소 집합의 순서" 에 의하여 결정된다.

- 교환법칙이 성립하지 않는다.

    - 예시 

        정의 "서로소 집합의 순서" 의 예시에서 보았듯 

        $$ \omega + 1 \neq 1 + \omega = \omega $$

        이다. 

- 결합법칙이 성립한다.

    - 증명

!!! tldr ""

    서수의 곱하기 : 반사전순서가 부여된 $A \times B$ 에 대하여 다음과 같이 정의한다.

    $$ \alpha \beta  = \text{ord }(A \times B) $$

- 교환법칙이 성립하지 않는다.

    - 예시 

        정의 "반사전순서" 의 예시에서 보았듯 $\omega \approxeq X \times \omega, \quad \omega \not \approxeq \omega \times X$ 으로써 

        $$ \omega 2 \neq 2 \omega = \omega $$

        이다.

- 결합법칙이 성립한다.

    - 증명

- 분배법칙은 항상 성립하지 않으므로 조심히 다뤄야 한다. 즉, 왼쪽 분배법칙은 성립하나, 오른쪽 분배법칙은 성립하지 않는다.

    - 증명

    - 예시 

        가령 

        $$ (1 + 1) \omega = 2 \omega \neq \omega 2=\omega +\omega =1 \omega +1 \omega $$

        이다. 하지만 왼쪽 분배법칙 

        $$ \alpha (\beta + \gamma ) = \alpha \beta + \alpha \gamma $$

        은 성립한다.
    
!!! tldr ""

    서수의 제곱 : 임의의 서수 $\alpha ,\beta$ 에 대하여 다음과 같이 정의한다.

    $$ \alpha ^{\beta } = \begin{cases} \sup \{\alpha ^{\gamma } : \gamma < \beta \} & \beta \text{ 가 극한서수이다 }\\ \alpha ^{\gamma }\alpha & \beta = \gamma + 1\\ \end{cases} $$
    
## 서수의 순서관계

!!! tldr ""

    서수의 순서 : 서수 $\alpha , \beta$ 에 대한 $\text{ord }(A) =\alpha ,\text{ord }(B) = \beta$ 인 정렬집합 $A, B$ 에 대하여 $A$ 가 $B$ 의 절편과 순서동형이면 다음과 같이 정의한다.

    $$ \alpha < \beta $$

- 서수인 정렬집합 $A$ 에서 임의의 $a \in A$ 에 대하여 $a \leq A$ 이다.

- 물론 $\alpha < \beta \lor \alpha = \beta$ 이면 

    $$ \alpha \leq \beta $$

    로 정의한다. 

- [정리 3.3.1](#90ba9203e) 는 임의의 서수 $\alpha , \beta$ 에 대하여 

    $$ \alpha < \beta , \quad  \alpha = \beta , \quad  \alpha > \beta $$

    중 하나가 성립함을 말해준다. 

!!! tldr "정리 3.3.2"

    정렬집합 $A$ 의 부분집합 $B$ 가 다음을 만족하면 $B = A$ 이다.

    $$ x \in A, S_x \subset B \implies x \in B $$

- 이 정리는 정렬집합 $\omega$ 에 관한 귀납법이 임의의 정렬집합에 대하여 어떻게 확장되는지 보여준다. 

- 증명 

    $A \setminus B \neq \varnothing$ 이면 최소원소 $a \in A \setminus B$ 를 가진다. 그러면 $S_a \subset B$ 이고 $a \in B$ 가 되어 모순이다. 그러므로 $A \setminus B = \varnothing$ 이다. ■ 

!!! tldr "정리 3.3.3"

    정렬집합에 관한 성질 $P$ 와 임의의 정렬집합 $X$ 에 대하여 다음이 만족되면 임의의 정렬집합이 $P$ 를 만족한다.

    - $X$ 의 모든 절편이 $P$ 를 만족하면 $X$ 도 $P$ 를 만족한다.

- 이 정리는 정렬집합 $\omega$ 에 관한 귀납법이 임의의 정렬집합에 대하여 어떻게 확장되는지 보여준다. 

- 증명 

    어떤 정렬집합 $X$ 가 $P$ 를 만족하지 않는다면 

    $$ Y = \{x \in X : S_x \text{ 가 } P \text{ 를 만족하지 않는다 }\} \neq \varnothing $$

    이고, $Y$ 는 최소원소 $a \in X$ 를 갖는다. 그러면 $S_a$ 의 모든 절편은 $P$ 를 만족하는데, 가정에 의하여 $S_a$ 도 $P$ 를 만족하므로 모순이다. ■ 

# 무한집합

## 집합의 대등

!!! tldr ""

    집합의 대등(equinumerous) : 두 집합 $X$ 와 $Y$ 사이에 전단사함수가 존재하면 $X$ 와 $Y$ 가 대등하다고 하고,

    $$ X \approx Y $$

    라고 쓴다.

- 이는 집합 $A$ 의 크기 $|A|$ 를 비교하기 위한 정의로써 $A \approx B \iff |A| = |B|$ 가 성립한다.

!!! tldr ""

    $$ \N \approx \mathbb{Z} \approx \mathbb{Q} $$

- 이 정리는 자연수집합 $\N$, 정수집합 $\mathbb{Z}$, 유리수집합 $\mathbb{Q}$ 이 대등하다는 것을 말해준다.

- 증명 

    함수 $f: \N \to \mathbb{Z}$ 를 

    $$ f(2n) = -n, \quad f(2n-1) = n $$

    라 정의하면 $f$ 는 자연수 전체 집합 $\N$ 에서 정수 전체 집합 $\mathbb{Z}$ 로 가는 함수가 된다. 한편 함수 $g : \mathbb{Z} \to \N$ 를 

    $$ g(n) = 2n-1, g(-n) = 2n $$

    이라 정의하면 $f$ 와 $g$ 는 역함수관계를 갖고 $f$ 와 $g$ 는 전단사 함수가 된다. 그러므로 

    $$ \therefore \N \approx \mathbb{Z} $$

    이다. ▲ 

    양의 유리수 집합 $\mathbb{Q} ^{+}$ 를 

    $$ \dfrac{1}{1},\enspace \dfrac{1}{2}, \dfrac{2}{1},\enspace \dfrac{1}{3}, \dfrac{2}{2}, \dfrac{3}{1},\enspace \dfrac{1}{4}, \dfrac{2}{3}, \dfrac{3}{2}, \dfrac{4}{1},\enspace \dfrac{1}{5}, \dfrac{2}{4}, \dfrac{3}{3}, \dfrac{4}{2}, \dfrac{5}{1}, \dots $$

    와 같이 나열하고 이 나열의 $n$번째 유리수를 $f(n)$ 이라 두면 $f: \N \to \mathbb{Q} ^{+}$ 는 전사함수가 된다. 이때 중복되는 유리수를 제거하여 

    $$ \dfrac{1}{1},\enspace \dfrac{1}{2}, \dfrac{2}{1},\enspace \dfrac{1}{3}, \dfrac{3}{1},\enspace \dfrac{1}{4}, \dfrac{2}{3}, \dfrac{3}{2}, \dfrac{4}{1},\enspace \dfrac{1}{5}, \dfrac{5}{1}, \dots $$

    를 만들고 마찬가지로 $n$ 번째 유리수를 $g(n)$ 라 두면 $g: \N \to \mathbb{Q} ^{+}$ 은 전단사함수가 된다. 그러므로 

    $$ \therefore \N \approx \mathbb{Q} ^{+} $$

    이다. 이때 공역을 음의 유리수 $\mathbb{Q} ^{-}$ 와 $0$ 를 포함하도록 확장하고 정의역을 $\N$ 에서 $\mathbb{Z}$ 로 바꾸면 같은 방식으로 전단사 함수 $h: \mathbb{Z} \to \mathbb{Q}$ 를 쉽게 만들 수 있음을 알 수 있다. 그러므로 

    $$ \therefore \mathbb{Z} \approx \mathbb{Q} $$

    이다. ▲ 
    
    그러므로 최종적으로
    
    $$ \therefore \N \approx \mathbb{Z} \approx \mathbb{Q} $$

    이다. ■ 

!!! tldr ""

    두 선분 위의 점들의 집합은 선분의 길이에 관계없이 항상 대등하다.

- 한편 이 정리를 더 확장하여 

    $$ [x_1, x_2] \approx [y_1, y_2] \text{ s.t. }\  \forall x_1, x_2, y_1, y_2 \in \R $$

    라고 할 수 있다.

- 증명 

    길이가 같은 선분 사이에 전단사함수가 존재함은 자명하다. ▲ 

    ![image](https://user-images.githubusercontent.com/16812446/111862271-a2d70680-8997-11eb-8367-9aca8a3c0b07.png)

    위와 같이 길이가 다른 선분 $\overline{AB}, \overline{CD}$ 가 존재한다. 그러면 $\overline{AC}$ 와 $\overline{BD}$ 의 연장선은 평행하지 않으므로 한 점 $O$ 에서 만난다. 이때 선분 $\overline{AB}$ 위의 점 $P$ 에 대하여 $\overline{OP}$ 의 연장선이 $\overline{CD}$ 와 만나는 점을 $f(P)$ 로 두면 함수 

    $$ f: \overline{AB} \to \overline{CD} $$

    는 전단사함수이다. ■ 

!!! tldr ""

    $$\N \not \approx [0, 1]$$

- 이 정리는 자연수 집합 $\N$ 이 폐구간 $[0, 1]$ 과 대등하지 않다는 것을 말해준다.

- 아래의 증명이 그 유명한 칸토어의 대각선 논법이다. 

- 증명 

    $\N$ 에서 $[0,1]$ 로 가는 전사함수가 존재하지 않음을 보이면 된다. 만약 함수 $f: \N \to [0,1]$ 이 전사함수라고 가정하자. 그러면 함수 $f$ 의 상은 무한소수로 표현될 수 있으므로 

    $$ f(0) = 0. x _{00} x _{01} x _{02} \dots x _{0n} \dots $$

    $$ f(1) = 0. x _{10} x _{11} x _{12} \dots x _{1n} \dots $$

    $$ f(2) = 0. x _{20} x _{21} x _{22} \dots x _{2n} \dots $$

    $$ \vdots $$

    $$ f(n) = 0. x _{n0} x _{n1} x _{n2} \dots x _{nn} \dots $$

    $$ \vdots $$

    와 같이 표현할 수 있다. 이때 수열 $\big <a_n\big >$ 을 

    $$ a_n = \begin{cases} 0 &x _{nn} \neq 0\\ 1 &x _{nn} = 0 \end{cases} $$

    로 정의하면 소수 $\alpha  =0.a_0 a_1 a_2 \dots a_n \dots \in [0, 1]$ 은 

    $$ \alpha \not\in \{f(0), f(1), f(2), \dots\} = \text{ran} (f)  $$

    이다. 그러므로 $f$ 는 전사함수가 아니다. ■ 

!!! tldr ""

    $$\N \times \N \approx \N$$

- 증명 

    $\N$ 에 속하는 자연수들을 다음과 같은 규칙으로 좌표평면의 1사분면에 나열하자.

    $$ \begin{equation}\begin{split} \vdots &\\ 10&\\ 6&\enspace 11\\ 3&\enspace 7\enspace 12\enspace \\ 1&\enspace 4\enspace 8\enspace 13 \\ 0&\enspace 2\enspace 5\enspace 9\enspace 14\enspace \dots \\ \end{split}\end{equation} \tag*{} $$

    즉, 자연수 $\N = \{0, 1, 2, 3, \dots\}$ 를 $\searrow$ 방향으로 $n, m \in \N$ 에 대한 1사분면의 좌표 $(n, m)$ 에 나열하는 것이다. 그러면 $\N$ 을 1사분면의 자연수 좌표에 모두 대응시킬 수 있다. 이때 첫번째 세로열에서 나타나는 좌표 $(0, m)$ 들의 수열은 $a _{0m} = 0 + \sum_{k=0}^{m+0}k$ 로 나타낼 수 있다. 또 두번째 세로열에서 나타나는 좌표 $(1, m)$ 들의 수열은 $a _{1m} = 1 + \sum_{k=0}^{m+1}k$ 로 나타낼 수 있다. 이때 $n$ 번째 세로열에서 나타나는 좌표 $(n,m)$ 들의 수열은 $a _{nm} = n + \sum_{k=0}^{m+n}k$ 이다. 그러므로 임의의 좌표 $(n, m)$ 에 대응되는 함수 $f: \N \times \N \to \N$ 을 

    $$ f(n, m) = n + \sum_{k=0}^{n+m}k = n + \dfrac{(n+m+1)(n+m)}{2} = \dfrac{(m+n) ^{2} + 3n + m}{2} $$

    로 정의할 수 있다. 이는 $\N \times \N$ 을 $\N$ 으로 대응시키는 전단사 사상이다. ■ 

- (*이건 왜 이렇게 되는지 아직 모르겠네*)한편, 역함수를 정의해보면 각 $k \in \N$ 에 대하여 

    $$ \dfrac{1}{2}l(l+1) \leq k < \dfrac{1}{2}(l+1)(l+2) $$

    인 유일한 자연수 $l \in \N$ 을 잡고 

    $$ g(k) = \bigg (k - \dfrac{1}{2}l(l+1), l - \bigg [k - \dfrac{1}{2}l(l+1)\bigg ]\bigg ) $$

    라 정의하면된다.

!!! tldr ""

    $n \in \N$ 에 대하여 다음이 성립한다.

    $$\N ^{n} \approx \N$$

- 증명

    $$ \because \N \times \N \approx \N $$

!!! tldr "3.16"

    무한 집합의 특성 : 자기자신과 대등한 진부분집합이 존재한다. 즉, 집합 $X$ 가 무한집합이면 다음이 만족한다.

    $$ \exists A \approx X \text{ s.t. }\ A \subset X $$

- 정의 "집합의 대등" 의 여러가지 예시에서 다룬 집합들은 모두 이 특성을 만족한다. 

    - 예시 

        자연수 집합 $\N$ 은 짝수 집합과 대등하다. 

        실수 집합 $\R$ 은 개구간 $(0, 1)$ 과 대등하다. 이 사실은 다음과 같은 탄젠트 함수 $y = \tan \bigg (\pi x - \dfrac{\pi }{2}\bigg )$ 를 살펴보면 쉽게 이해할 수 있다.

        ![](https://user-images.githubusercontent.com/16812446/83792797-8868c080-a6d6-11ea-8dac-6238abb22dfa.png)

        즉, 놀랍게도 $\R \approx (0, 1)$ 이다.

!!! tldr "도움정리 3.4.1"

    집합 $X$ 가 무한 집합의 특성을 만족하고 $X \approx Y$ 이면 $Y$ 도 무한 집합의 특성을 만족한다.

- 증명 

    집합 $X$ 에 대하여 $\exists A \text{ s.t. }\ A \subsetneq X$ 이고, 가정에 의하여 전단사함수 $f: X \to A$ 가 존재한다. 또한 집합 $Y$ 에 대하여 가정에 의하여 전단사 함수 $g: X \to Y$ 가 존재한다. ▲ 

    그러면 제한 $g|_A : A \to g(A)$ 는 전단사함수이고, 이에따라 

    $$ (g|_A) \circ f \circ g ^{-1}: Y \to g(A) $$

    도 전단사함수이다. 그러므로 $g(A)$ 가 $Y$ 의 진부분집합이면 증명이 끝난다. ▲ 

    그런데 $x \in X \setminus A \implies g(x) Y \setminus g(A)$ 이므로 $g(A) \subsetneq  Y$ 이다. 그러므로 

    $$ \therefore g(A) \approx Y $$

    이다. ■ 

!!! tldr "도움정리 3.4.2"

    집합 $X$ 가 무한 집합의 특성을 만족하고 $X \subset  Y$ 이면 $Y$ 도 무한 집합의 특성을 만족한다.

- 증명 

    집합 $X$ 의 진부분집합 $A$ 에 대하여 전단사함수 $f: X \to A$ 가 존재한다. 이때 함수 $g: Y \to Y$ 를 

    $$ g(y) = \begin{cases} y & y \in Y \setminus X\\ f(y) & y \in X \end{cases} $$ 

    라 정의하면 $g$ 는 단사함수이고 치역이 $A \sqcup (Y \setminus X)$ 이다. 그런데 $A \subsetneq X$ 이므로 
    
    $$A \sqcup (Y \setminus X) \subsetneq Y = X \sqcup (Y \setminus X)$$
    
    이다. 그러면 함수 $g$ 의 공역을 축소시킨 $h: Y \to A \sqcup (Y \setminus X)$ 는 전사함수이다. $g$ 는 단사함수이었으므로 $h$ 는 전단사함수이고, 따라서 

    $$ \therefore  Y \approx A \sqcup (Y \setminus X) $$

    이다. ■ 

!!! tldr ""

    비둘기 집 원리(Pigeonhole principle) : $n = \{0,1,2, \dots, n-1\} \in \N$ 에 대한 임의의 단사함수 $f: n \to n$ 가 전사이다.

- 증명

    $n=0$ 일 때는 자명하다. $n$ 일때 성립한다고 하고 $n ^{+}$ 일 때도 성립함을 보이기 위하여 함수 

    $$ f: n ^{+} \to n ^{+} $$

    가 단사라고 하자. 함수 $f$ 를 $n ^{+} = n \sqcup \{n\}$ 의 부분집합 $n$ 에 제한하면 단사함수 $f|_n:n \to n ^{+}$ 를 얻는다.

    우선 $f(n) \subset n$ 이라고 하면 가정에 의하여(*$f$ 가 $n$ 에 대하여 전단사라는 가정*) $f(n) = n \subset n ^{+}$ 이다. (*이때 주의할 점은 $f(n)=n$ 을 한 원소의 대응으로 해석하는 게 아니라 $n$ 이라는 집합에 집합 $n$ 이 대응된다고 해석해야한다는 것이다. $f:n \to n$ 가 $n$ 에 대하여 전단사이므로 정의역과 치역이 $n$ 이다. 그런 의미에서 $f(n)=n$ 이라고 표기한 것이다*) 따라서 $f(n) = n \in n ^{+}$ 이고(*이때의 $f(n)=n$ 은 $n$ 이라는 집합이 $n$ 에 대응되는 것으로써 표기한 것이 아니라 한 원소 $n$ 이 $n$ 으로 대응된다는 것으로써 표기한 것이다. 그러므로 $f(n) = n$ 이 공역 $n ^{+} = n \sqcup \{n\}$ 의 $\{n\}$ 에 대응되므로 공역이 곧 치역이 되어 전사함수가 된다는 것이다.*), $f$ 는 전사함수이다. 그러므로 $f$ 는 전단사 함수이다. ▲ 
    
    (*위 증명에서 $f(n) = n \subset n ^{+}$ 은 정의역 $n$ 이 치역 $n$ 으로 대응된다는 것이고 $f(n) = n \in n ^{+}$ 은 한 원소 $n$ 이 $n$ 으로 대응된다는 것으로 표기한 것이 매우 애매하고 헷갈렸던 이유는 전자의 함수의 입출력이 집합이라는 단서가 오로지 $\subset$ 기호에 있고, 후자의 함수의 입출력이 원소라는 단서가 오로지 $\in$ 기호에 있기 때문이었던 거지..*)

    이제 $f(n) \not \subseteq n$ 인 경우를 생각하자. 그러면 $f(k) \not\in n$ 인 $k \in n$ 이 존재한다. 그러면 $f(k) \in n ^{+} \setminus n$ 이므로 $f(k) = n \in n ^{+}$ 이다.

    이제 함수 $g: n ^{+} \to n ^{+}$ 를 

    $$ g(k) = n \in n ^{+}, \enspace g(n) = k \in n ^{+}, \enspace g(x) = x, \enspace x \in n \setminus \{k\} $$

    와 같이 정의하자. 그러면 $g$ 는 $n ^{+} = \{n\}\sqcup \{k\}\sqcup (n \setminus \{k\})$ 에서 단지 $n$ 과 $k$ 만을 바꾸고 나머지는 그대로 대응시키는 함수에 불과 하므로 자명하게 전단사함수이다. 

    합성함수 $f \circ g : n ^{+} \to n ^{+}$ 에 대하여 $(f \circ g)(n) \subset n \subset n ^{+}$ 이고 (*이 부분도 마찬가지로 집합 $n$ 이 집합 $n$ 으로 대응됨을 뜻한다*) $(f \circ g)(n) = n \in n ^{+}$ 이다. (*이 부분도 원소 $n$ 이 $n$ 으로 대응됨을 뜻하지*) 
    
    따라서 $(f \circ g)|_n:n \to n$ 에 귀납법의 가정(*$f$ 가 $n$ 에서 전단사라는 가정*)을 적용하면 $(f \circ g)|_n$ 이 전단사임을 알 수 있다. (*이로써 $(f \circ g)(n) = n \subset n ^{+}$ 이 보장되는 거지. 그래서 이제 함수의 제한을 풀고 $(f \circ g)(n) = n \in n ^{+}$ 만 보이면 전사함수가 되는데 이건 이미 위에서 보였으니까*) 따라서 $f \circ g$ 는 전단사이고, $f = (f \circ g) \circ g ^{-1}$ 도 전단사이다.(*$g$ 가 전단사이므로 $g ^{-1}$ 도 전단사니까*) ■ 

!!! tldr "정리 3.4.3"

    자연수 $n = \{0, 1, 2, \dots, n-1\}$ 의 부분집합 $A$ 에 대하여 다음이 성립한다.

    $$ n \approx A \implies n = A $$

- 증명 

    $A \subset n$ 에 대하여 $n \approx A$ 이므로 전단사 함수 $f: n \to A$ 가 존재한다. $n \neq A$ 라고 한다면 $k \in n \setminus A$ 가 존재하여 $k \not\in A$ 이다. 그런데 $f$ 는 전단사함수이므로 $f(k) = l \in A$ 이다. 이때 $n \setminus \{k\} = A \lor n \setminus \{k\} \supsetneq A$ 이다. 
    
    $n \setminus \{k\} = A$ 인 경우 $f$ 가 전단사이므로 $f(n \setminus \{k\}) = f(A) = A$ 가 되어 
    
    $$ \exists k' \in n \setminus \{k\} \text{ s.t. }\  f(k') = l $$

    이다. $f$ 는 단사이므로 $f(k) = l \land f(k') = l$ 는 모순이다. ▲ 

    $n \setminus \{k\}\supsetneq A$ 인 경우 $n \setminus \{k\} \neq A$ 이므로 $k' \in n \setminus A \cup \{k\}$ 이다. 그런데 $f$ 는 전단사이므로 $f(k') = l' \in A$ 이다. 그러면 또 다시 $n \setminus \{k,k'\} = A \lor n \setminus \{k,k'\} \supsetneq A$ 이다. 이런식으로 $A$ 에 속하지 않는 $n$ 의 원소 $k'', k''', \dots$ 을 제거한 집합 $n'$ 을 만들어 $n' = A$ 가 되게 할 수 있다. 그러면 위의 논증과 마찬가지로 $f(n') = A$ 가 되는데 

    $$ \exists x \in n' \text{ s.t. }\ f(x) = l $$

    에서 $f(k) = l \land f(x) = l$ 인데 $f$ 는 단사이므로 모순이 된다. ▲ 

    그러므로 
    
    $$ \therefore  n = A$$ 
    
    이다.

    - [비둘기 집 원리](#794c1114c) 는 집합 $n$ 에서 $n$ 으로 가는 단사 함수라면 전사함수이라고 말하고 있고, 이 정리는 $n$ 에서 $A (\subset n)$ 으로 가는 전단사함수가 존재하면 $n=A$ 라고 말하고 있네. 그럼 이 둘이 서로 역인데, 어떻게 비둘기 집 원리 정리를 적용할 수 있을까.

        위 증명은 어떻게 비둘기 집 원리 정리가 본 정리의 증명에 적용되는지 모르겠어서 내가 만든 것이므로 오류가 있을 수 있다.

## 유한집합의 정의

!!! tldr ""

    유한집합(finite set) : 집합 $X$ 가 다음을 만족하면 유한집합이라 한다. 

    $$ \exists n \in \N \text{ s.t. }\ n \approx X $$

- [정리 3.4.3](#b64052abc) 는 어떤 자연수 $n$ 도 무한집합의 특성을 만족하지 않음을 말한다.

    따라서 도움정리 3.4.1 를 적용하면 임의의 유한집합은 무한집합의 특성을 만족하지 않는다. 이제 이 역을 보이려 하는데, 유한집합이 아니면 무한집합의 특성을 만족한다는 것을 보이려 하는 것이다. 

    도움정리 3.4.2 가 있으므로 이미 $\N$ 이 무한집합의 특성을 만족한다는 것을 알게 되었다. 그러므로 다음 정리를 증명하면 된다. 

!!! tldr "도움정리 3.4.4"

    집합 $X$ 가 유한집합이 아니면, $\exists A \subset X \text{ s.t. }\ \N \approx A$ 이다.

- 증명     

    먼저 선택공리에 의하여 집합 $X$ 의 선택함수 $h: 2 ^{X} \setminus \{\varnothing \} \to X$ 를 택하자. $X$ 의 모든 유한 부분집합들의 모임 $\mathcal{F}(X)$ 에 대하여 [정리 2.1.2](../numbers#3a99b431b) 를 적용할 것이다. $X$ 는 유한집합이 아니므로 임의의 $A \in \mathcal{F}(X)$ 에 대하여 $X \setminus A \neq \varnothing$ 이고 따라서 $h(X \setminus A) \in X \setminus A$ 이다. 이제 함수 $F: \mathcal{F}(X) \to \mathcal{F}(X)$ 를 $A \in \mathcal{F}(X)$ 에 대하여

    $$ F(A) = A \sqcup \{h(X \setminus A)\} $$

    라고 정의하면 $n \in \N$ 에 대하여

    $$ \gamma (0) = \varnothing , \quad \gamma (n ^{+}) = F(\gamma (n)) $$

    인 함수 $\gamma : \N \to \mathcal{F}(X)$ 가 존재한다.

    $\forall n \in \N$ 에 대하여 $\gamma (n)$ 은 $X$ 의 유한부분집합이므로 $X \setminus \gamma (n) \neq \varnothing$ 이고 함수 $\delta : \N \to X$ 를 $n \in \N$ 에 대하여

    $$ \delta (n) = h(X \setminus \gamma (n)) $$

    와 같이 정의할 수 있다. 그러면 각 $n \in \N$ 에 대하여 

    $$ \gamma (n ^{+}) = F(\gamma (n)) = \gamma (n) \sqcup \{h(X \setminus \gamma (n))\} = \gamma (n) \sqcup \{\delta (n)\} $$

    이므로 $\gamma (n ^{+})$ 란 $\gamma (n) \subset X$ 에 $\delta (n) \in X$ 이라는 원소를 추가한 것임을 알 수 있다.

    이제 $\delta : \N \to X$ 가 단사함수임을 보이기 위해 $n<m$ 라고 두는데, $n ^{+} \leq m$ 이므로 $\delta (n) \in \gamma (n ^{+}) \subset \gamma (m)$ 이다. 따라서 

    $$ \delta (m) = h(X \setminus \gamma (m)) \in X \setminus \gamma (m) $$

    이 되어 $\delta (n) \neq \delta (m)$ 이다. 그러므로 함수 $\delta :\N \to X$ 의 상 $\delta (\N)$ 은 $X$ 의 부분집합이고, $\N$ 과 대등하다. 즉, $X$ 의 부분집합 $\delta (\N)$ 은

    $$ \delta (\N) \approx \N $$

    이므로 증명이 끝났다. ■ 

    - 이 증명을 쉽게 말하면 다음과 같다. $x_1 \in X$ 를 하나 잡으면 $X \setminus \{x_1\} \neq \varnothing$ 이다. 따라서 $x_2 \in X \setminus \{x_1\}$ 를 택할 수 있고, $x_3 \in X \setminus \{x_1, x_2\}$ 도 택할 수 있다. 만약 $x_1, x_2, \dots, x_n \in X$ 을 택했다고 해도 $\forall n \in \N$ 에 대하여

    $$ X \setminus \{x_1, x_2, \dots, x_n \} \neq \varnothing $$

    이다. 이렇게 계속 $x_n$ 을 택함으로써 집합 

    $$ A = \{x_n : n = 1, 2, \dots \} $$

    을 만들자. 그러면 $A$ 는 $X$ 의 부분집합이고 $A \approx \N$ 이다. 이렇게 무한히 선택할 수 있다는 것이 선택공리가 주장하는 것이다.

## 무한집합의 정의

!!! tldr "정리 3.4.5"

    집합 $X$ 에 대하여 다음은 동치이다.

    1. $X$ 가 유한집합이 아니다. 즉, $\forall n \in \N, X \not \approx n$ 이다.

    2. $\exists A \subsetneq X \text{ s.t. }\ X \approx A$

- 지금까지의 정리들의 결론이 이 무한집합의 정의이다.

!!! tldr ""
    
    무한집합(infinite set) : 정리 3.4.5 의 동치조건을 만족하는 집합이다. 

# 기수

!!! tldr ""

    기수(cardinal number) : 임의의 집합 $X$ 에 대하여 $X$ 와 동등한 서수 전체의 집합의 최소원소

    $$ |X| := \min \{\xi : \xi \approx X, \xi \preccurlyeq 2 ^{X}\} $$

    를 $X$ 의 기수라고 한다.

- 기수는 $|X| = \text{card }(X)$ 라고도 표기한다.

- 기수란 집합에 들어있는 원소의 갯수를 의미한다.

- 이 정의는 아래에서 살펴볼 [정리 3.6.4](#f69fd2ad6) 를 기반으로 한다.
    
- 유한집합에 대해서는 기수의 정의를 다음과 같이 쉽게 생각해도 된다.

    "유한집합 $X$ 와 대등한 자연수 $n \in \N$ 으로써 

    $$ |X| = n $$

    이다."

- 기수는 임의의 집합 $A$ 에 대하여 

    $$ A_1 \approx A_2 \iff |A_1| = |A_2| $$

    를 만족해야 한다. 

## 기수의 덧셈과 곱셈

!!! tldr ""

    기수의 더하기 : 서로소 집합 $A, B$ 와 그 기수 $a = |A| ,b = |B|$ 에 대하여 다음과 같이 정의한다.

    $$ a + b = |A \sqcup B| $$

- 이 연산은 잘 정의되어 있다. 

    - 증명 

        $$ A \approx C , B \approx D \implies A \sqcup B \approx C \sqcup D $$

        를 보이면 된다. 만약 $g: A \to C, h: B \to D$ 가 전단사이면 함수 $g \sqcup h: A \sqcup B \to C \sqcup D$ 도 전단사이므로 $a+b$ 가 잘 정의되어 있음을 알 수 있다.

- 교환법칙이 성립한다. 

    - 증명 

        $A \sqcup B = B \sqcup A$ 이므로 $a+b=b+a$ 이다.

- 결합법칙이 성립한다. 

    - 증명 

        집합의 합집합의 결합법칙이 성립하므로 $(a+b)+c=a+(b+c)$ 도 성립한다.

!!! tldr ""

    기수의 곱하기 : $|A| =a, |B| = b$ 인 집합 $A, B$ 에 대하여 다음과 같이 정의한다.

    $$ ab = |A \times B| $$

- 이 연산은 잘 정의되어 있고, 교환법칙/결합법칙/분배법칙이 성립한다.

    - 증명 

!!! tldr ""

    기수의 제곱 : $|A| =a,|B| =b$ 에 대하여 다음과 같이 정의한다.

    $$ a ^{b} = |A ^{B}| $$

!!! tldr ""

    기수의 제곱은 잘 정의되어 있다.

- 증명 

    $g:A \to C, h:B \to D$ 가 전단사라고 하고 함수 $f_1: A ^{B} \to C ^{D}, f_2:C ^{D} \to A ^{B}$ 를 

    $$ f_1(\alpha ) = g \circ \alpha \circ h ^{-1}, \quad \alpha \in A ^{B} $$

    $$ f_2(\beta ) = g ^{-1} \circ \beta \circ h , \quad \beta \in C ^{D} $$

    와 같이 정의하면 

    $$ f_1(f_2(\beta )) = g \circ (g ^{-1} \circ \beta \circ h) \circ h ^{-1} = \beta $$

    이고, 마찬가지로 $f_2(f_1(\alpha ))=\alpha$ 이므로 $f_1$ 과 $f_2$ 는 서로 역함수이다. 그러므로 이들은 전단사 함수이고, 이는 곧 

    $$ A ^{B} \approx C ^{D} $$

    를 의미한다. ■ 

!!! tldr ""

    $B \cup C = \varnothing$ 인 집합 $A,B,C$ 에 대한 기수 $a = |A| , b = |B| , c = |C|$ 에 대하여 다음이 성립한다.

    - $a ^{b+c} = a ^{b}a ^{c}$

    - $(ab) ^{c} = a ^{c} b ^{c}$

    - $(a ^{b})^{c} = a ^{bc}$

- 증명

    pass

## 베른슈타인의 정리

!!! tldr ""

    집합 $A, B$ 사이에 단사함수 $f: A \to B$ 가 존재하면 다음과 같이 표기한다.

    $$ A \preccurlyeq B $$

- 임의의 집합 $A$ 에 대하여 $A \preccurlyeq A$ 이다.

- 단사의 합성이 단사이므로 

    $$ A \preccurlyeq B, B \preccurlyeq C \implies A \preccurlyeq C $$

    이다.

!!! tldr "정리 3.5.1"

    임의의 집합 $A, B$ 에 대하여 다음이 성립한다.

    $$ A \preccurlyeq B \lor B \preccurlyeq A $$

- 증명

    임의의 집합 $A, B$ 에 대하여 [체르멜로 정렬정리](#0d9cd4880) 를 적용하여 정렬순서를 부여하자. 

    그러면 [정리 3.3.1](#90ba9203e) 에 의하여 $A \approx B$ 이거나 적절한 $a \in A, b \in B$ 에 대하여 $A \approx S_b \subset B$ 혹은 $B \approx S_a \subset A$ 가 성립한다.

!!! tldr "정리 3.5.2"

    베른슈타인의 정리(Schröder–Bernstein theorem) : 집합 $A, B$ 에 대하여 다음이 성립한다. 
    
    $$A \preccurlyeq B \land B \preccurlyeq A \implies A \approx B$$

- 이 정리는 쉽게 말해 두 집합 $A, B$ 사이에 $A \to B$ 로 가는 단사함수와 $B \to A$ 로 가는 단사함수가 존재하면 $A, B$ 사이에 전단사 함수가 존재함을 말해준다.

- 이 정리는 기수의 연산에서 핵심적인 역할을 한다.

- 증명 

    단사함수 $f: A \to B, g: B \to A$ 를 두고, [정리 2.1.2](#3a99b431b) 를 적용하여 $A$ 의 부분집합 $C_n$ 과 $B$ 의 부분집합 $D_n$ 을 $n \in \N$ 에 대하여

    $$ C_0 = A \setminus g(B), \enspace D_0 = f(C_0) $$

    $$ C _{n+1} = g(D_n), \enspace D_n = f(C_n) $$

    라고 정의하자. 이제 $C = \bigcup_{n=0}^{\infty }C_n \subset A$ 라 하고 함수 $h: A \to B$ 를 

    $$ h(x) = \begin{cases} f(x) &x \in C\\ g ^{-1}(x) & x \in A \setminus C\\ \end{cases} $$

    와 같이 정의한다. $x \in A \setminus C$ 이면 $x \in A \setminus C_0=g(B)$ 이므로 $g ^{-1}(x) \in B$ 가 잘 정의된다. ▲ 

    $h$ 가 단사임을 보이기 위해 $x_1 \neq x_2$ 인 $x_1, x_2 \in A$ 를 잡자. $x_1, x_2 \in C$ 이거나 $x_1, x_2 \in A \setminus C$ 이면 자명하게 $h(x_1) \neq h(x_2)$ 이다. 그러니 $x_1 \in C, x_2 \in A \setminus C$ 라고 하자.

    그러면 적절한 $n$ 에 대하여 $x_1 \in C_n$ 이므로 $h(x_1) = f(x_1) \in D_n$ 이다. 한편 $h(x_2) = g ^{-1}(x_2) \in D_n$ 이면 $x_2 \in g(D_n) \subset C$ 이므로 $x_2 \not\in C$ 라는 것에 모순이다. 따라서 $h(x_2) \not\in D_n$ 이다. 그러므로 $h(x_1) \neq h(x_2)$ 이다. ▲ 

    $h$ 가 전사임을 보이기 위해 $D = \bigcup_{n=0}^{\infty  }$ 라고 두자. 우선 $h(C) = f(C) = D$ 이므로 $D \subset h(A)$ 이다. 이제 $B \setminus D \subset h(A)$ 임을 보이면 $h$ 는 전사가 된다. 

    이를 위하여 $y \in B \setminus D$ 라고 하면 $C_0 = A \setminus g(B)$ 이므로 $g(y) \not\in C_0$ 은 당연하다. 또 각 $n = 0,1,2,\dots$ 에 대하여 $y \not\in D_n$ 이고 $C _{n+1}=g(D_n)$ 인데 $g$ 가 단사이므로 $D$ 에 속하지 않는 원소 $y$ 의 상은 $C$ 에 속하지 않는다. 즉, $g(y) \not\in C _{n+1}$ 이다.

    그러므로 $g(y) \not\in C$ 인데, $h$ 의 정의에 의하여 $y = g ^{-1}(g(y)) = h(g(y)) \in h(A)$ 에서 결국 임의의 $B \setminus D$ 의 원소 $y$ 에 대하여

    $$ y \in h(A) $$

    가 성립하여, $h$ 가 전사임이 증명되었다. ▲ 

    그러므로 $h$ 는 전단사이고 모든 증명이 끝났다. ■ 

- 또 다른 증명

    pass

## 기수의 순서관계

!!! tldr ""

    기수의 순서 : 두 기수 $a = |A| , b = |B|$ 에 대하여 다음과 같이 정의한다.

    $$ A \preccurlyeq B \iff a \leq b $$

- 이 순서는 잘 정의되어 있고, 순서관계의 조건을 만족시킨다.

!!! tldr ""

    기수 $a, b, c$ 에 대하여 $a \leq b \iff \exists c \text{ s.t. }\ b = a + c$ 이다.

- 이 정리는 기수의 순서가 자연수의 순서와 유사한 성질을 갖는다는 것을 말해준다.

- 증명 

    먼저 $a \leq b$ 이면 $A \preccurlyeq B$ 이므로 단사함수 $f: A \to B$ 가 존재한다. 이때 $c = |B \setminus f(A)|$ 라 두면 $a + c = |A \sqcup (B \setminus f(A))| = |B| = b$ 이다. 왜냐하면 기수간의 $=$ 은 전단사함수의 존재성을 뜻하는데 서로소 집합 $A, B$ 에 대하여 $B \setminus f(A)$ 에 $A$ 를 $\sqcup$ 된 집합은 $B$ 와 일대일 대응될 수 있기 때문이다. ▲ 

    역으로 $c =|C|$ 인 집합 $C$ 가 존재하고 $f: A \sqcup C \to B$ 가 전단사이면 $f|_A: A \to B$ 는 단사이고 따라서 $a \leq b$ 이다. ■ 

# 초한기수

!!! tldr ""

    임의의 무한집합 $X$ 에 대하여 다음이 성립한다.

    $$ |\N| \leq |X|$$

- 증명

    $X$ 가 무한집합이면 [도움정리 3.4.4](#8ab5072fc) 에 의하여 단사함수 $f: \N \to X$ 가 존재한다. ■ 

## 자연수의 초한기수

!!! tldr "자연수의 초한기수"

    $$\aleph _0 = |\N|$$

- 이는 가장 작은 초한기수이다.

- $\N \approx \mathbb{Z} \approx \mathbb{Q}$ 이므로 

    $$ |\N| = |\mathbb{Z}| = |\mathbb{Q}| = \aleph _0 $$

    이다.

## 실수의 초한기수

!!! tldr "실수의 초한기수"

    $$\mathfrak{c} = |\R|$$

- 단사함수 $f: \N \to \R$ 은 존재하지만 $\R$ 을 $\N$ 으로 보내는 단사함수는 존재하지 않으므로 

    $$ \aleph _0 < \mathfrak{c} $$

    이다.

!!! tldr ""

    가산 집합(countable set) : 집합 $X$ 의 기수가 다음을 만족하면 $X$ 를 셀 수 있는 집합이라고 한다.

    $$ |X| \leq \aleph _0 $$

- 유한집합은 가산집합이다. 

- $\N , \mathbb{Z} , \mathbb{Q}$ 는 가산 무한집합이다. 가산 무한집합을 가부번 집합이라고도 한다.

!!! tldr ""

    비가산 집합(uncountable set) : 집합 $X$ 의 기수가 다음을 만족하면 $X$ 를 셀 수 없는 집합이라고 한다.

    $$ |X| > \aleph _0 $$

- $\R$ 는 비가산집합이다.

## 초한기수의 성질

!!! tldr ""

    $$ \aleph _0 \aleph _0 = \aleph _0 $$

- 이것은 무한기수의 독특한 특징이다.

- 증명 

    $$ \because \N \times \N \approx \N $$

!!! tldr "정리 3.5.3"

    임의의 무한기수 $a$ 에 대하여 $aa = a$ 이다.

- 증명 

    $|A|  = a$ 인 무한집합 $A$ 를 잡으면 [도움정리 3.4.4](#8ab5072fc) 에 의하여 $\exists D \subset A \text{ s.t. }\  D \approx \N$ 이다. 이때 $\N \times \N \approx \N$ 이므로 $D \approx D \times D$ 가 되어 전단사 함수 $f: D \to D \times D$ 가 존재한다. 이때 

    $$ D \subset B \subset A, \quad  g|_D=f, \quad g:B \to B \times B \text{ is bijection } $$

    을 만족하는 순서쌍 $(B, g)$ 들의 전체 집합 $\mathcal{B}$ 을 정의하고, 여기에 

    $$ (B_1, g_1) \leq (B_2, g_2) \iff B_1 \subset B_2, g_2| _{B_1} = g_1 $$

    와 같은 순서를 부여하면 $\mathcal{B}$ 는 순서집합이 된다. 또 이로써 [초른 보조정리](#8e7118900)의 조건부가 만족된다. 그러므로 $\mathcal{B}$ 에는 극대원소 $(C, h)$ 가 존재한다.

    이제 $|C| = c$ 로 두고, $c=a$ 을 보이면 증명이 끝난다. ▲ 

    $c<a$ 라고 가정하면, $b = |A \setminus C|$ 가 존재한다. 이때 

    $$ c  = 0 + c \leq c + c = 1c + 1c = 2c \leq cc = c $$

    이므로 $c + c \leq c$ 인데, 애초에 $c \leq c + c$ 이므로 $c = c+ c$ 이다. 만약 $b \leq c$ 이면 

    $$ a = b + c \leq c + c = c $$

    이므로 $a \leq c$ 가 되어 모순이므로 [정리 3.5.1](#1267052d9) 에 의하여 $c < b$ 이다. $C$ 보다 $A \setminus C$ 가 더 크므로 $C \approx E$ 인 $E \subset A \setminus C$ 가 존재한다. 이때 합집합과 곱집합의 분배법칙에 의하여

    $$ (C \sqcup E) \times (C \sqcup E) = (C \times C) \sqcup (C \times E) \sqcup (E \times C) \sqcup (E \times E) $$

    인데, $(C \times E) , (E \times C) , (E \times E)$ 들의 기수는 $c$ 이므로 

    $$ |(C \times E) \sqcup (E \times C) \sqcup (E \times E)| = (c+c)+c=c+c=c $$

    이다. 그러므로 전단사 함수 

    $$ k: E \to (C \times E) \sqcup (E \times C) \sqcup (E \times E) $$

    가 존재한다. 한편 전단사 함수 $h:C \to C \times C$ 에 대하여 서로소 집합 함수 $h \sqcup k$ 는 

    $$ h \sqcup k:C \sqcup E \to (C \sqcup E) \times (C \sqcup E) $$

    는 전단사 함수가 된다. 그러면 $(C \sqcup E, h \sqcup k) > (C, h)$ 인데, 이는 $(C, h)$ 가 극대 원소라는데 모순이다. 그러므로 $c = a$ 이다. ▲ 

    $c$ 는 조건에 의하여 $cc = c$ 였으므로 결국 $aa=a$ 이다. ■ 

!!! tldr ""

    무한기수 $a, b$ 에 대하여 다음이 성립한다.

    1. $a \leq b \implies a + b = ab = b$

    2. $a ^{b} = 2 ^{b}$

- 증명

    $1 \leq a$ 에서 $b = 1b \leq ab \leq bb = b$ 이므로 $ab = b$ 이다. ▲ 
    
    또한 $b = 0+b \leq a+b \leq b + b = 2b \leq bb = b$ 이므로 $a + b = b$ 인데 이때의 $a$ 는 어떤 기수라도 관계 없다. ▲ 

    무한 기수 $a = |A|$ 와 $2 ^{a} = |2 ^{A}|$ 에 대하여 $a \leq 2 ^{a}$ 이므로 $a ^{b} \leq (2 ^{a})^{b} = 2 ^{ab} = 2 ^{b}$ 이고, $2 \leq a$ 이므로 $2 ^{b} \leq a ^{b}$ 이다. ■ 

!!! tldr ""

    다음은 동치이다.

    1. 임의의 기수 $a$ 에 대하여 $a < 2 ^{a}$ 이다.

    2. 임의의 집합 $X$ 에 대하여 임의의 함수 $f: X \to 2 ^{X}$ 는 전사가 아니다.

- 이 정리는 어떤 집합의 기수가 그것의 부분집합 전체 집합의 기수보다 반드시 작다는 것인데, 이것도 칸토어의 대각선 논법이다.

- 한편 이 정리는 더욱 더 큰 기수를 발견할 수 있다는 가능성을 보여준다.

- 증명 

    함수 $f: X \to 2 ^{X}$ 에 대하여 

    $$ A = \{x \in X: x \not\in f(x)\} $$

    라 두고, $f$ 가 전사라고 가정하자. 그러면 이 함수 $f$ 는 임의의 $x \in X$ 를 $X$ 의 모든 부분집합으로 대응시키기 때문에 $X$ 의 부분집합인 $A$ 에 대해서도 $f(x_0) = A$ 인 $x_0$ 가 존재한다. ▲ 

    $x_0 \in A$ 이면 $A$ 의 정의에 의하여 $x_0 \not\in f(x_0)$ 인데 $f(x_0) = A$ 이므로 $x_0 \not\in A$ 이다. 따라서 모순이다. ▲ 

    $x_0 \not \in A$ 이면 $x_0 \in f(x_0) = A$ 이 또한 모순이다. ▲ 

    그러므로 $f(x_0) = A$ 인 $x_0$ 는 존재하지 않고, $f$ 는 전사가 아니다. ■ 

## 실수의 크기

!!! tldr "$\R$ 의 기수"

    $$ 2 ^{\aleph_0} = \mathfrak{c} $$

- 증명 (https://proofwiki.org/wiki/Continuum_equals_Cardinality_of_Power_Set_of_Naturals)

    [실수 집합과 데데킨트 절단 집합 사이에 전단사 사상이 존재하므로](../numbers#458a3d85a) 전단사 사상 

    $$ f: \R \to \mathscr{D} $$

    가 존재한다. 절단은 $\mathbb{Q}$ 의 부분집합이므로 $\mathscr{D} \subset 2 ^{\mathbb{Q}}$ 이고, 곧 $|\mathscr{D}| \leq |2 ^{\mathbb{Q} }|$ 이다. $\mathbb{Q} \approx \mathbb{N}$ 이므로 $2 ^{\N} \approx 2 ^{\mathbb{Q} }$ 이고, $\mathscr{D} \approx \R$ 이므로

    $$ |\R| \leq |2^{\N}| \iff \mathfrak{c} \leq 2 ^{\aleph _0} $$

    이다. ▲ 

    사상 $h: \text{Fin}(\N) \times  2 ^{\N} \to \R ^{+}$ 을 

    $$ \forall F \in \text{Fin}(\N), A \in 2 ^{\N} : h(F, A) = \sum_{i \in F} 2 ^{i} + \sum_{i \in A} \bigg (\dfrac{1}{2}\bigg ) ^{i} $$

    와 같이 정의하자. $\text{Fin}(\N)$ 은 $\N$ 의 모든 유한 부분집합의 집합이다.

    그러면 $(F, A)$ 는 실수 $h(F, A)$ 로 대응된다. 이는 $h$ 가 전사 사상임을 뜻한다. 전사 사상의 정의역과 공역은 

    $$ |\text{Fin}(\N) \times 2 ^{\N}| \leq |\R^{+}| $$

    의 관계를 갖는다. 이때 정의에 의하여 $\text{Fin}(\N) \subset 2 ^{\N}$ 이므로 $|\text{Fin}(\N)| \leq |2^{\N}|$ 이다. 임의의 무한 기수 $a$ 와 유한 기수 $b$ 에 대하여 $ab = a$ 이므로 $|\text{Fin}(\N) \times 2 ^{\N}| = |2^{\N}|$ 이고, $\R ^{+} \subset \R$ 이므로 $|\R^{+}| \leq |\R|$ 이다. 그러므로 

    $$ |2^{\N}| \leq |\R| \iff 2 ^{\aleph _0} \leq \mathfrak{c} $$

    이다. ▲ 

    그러므로 $2 ^{\aleph _0} = \mathfrak{c}$ 이다. ■ 

# 서수의 성질

!!! tldr "도움정리 3.6.1"

    서수 $\alpha , \beta$ 에 대하여 $\alpha \approxeq \beta \implies \alpha = \beta$ 이다.

- 증명 

    함수 $f: \alpha \to \beta$ 가 순서동형을 정의할 때 $\forall \xi \in \alpha, f(\xi ) = \xi$ 임을 보이면 본 정리가 증명된다. 

    $$ X = \{a \in \alpha : f(a ) = a \} $$

    라고 정의하고, $\xi \in \alpha$ 에 대하여 $S _{\xi } \subset X$ 라고 가정하자. 즉, $b < \xi \implies f(b ) = b$ 를 가정한다. 

    먼저 $\eta \in \xi = S _{\xi } \implies \eta < \xi \implies f(\eta )<f(\xi )$ 인데 가정에 의하여 $\eta \in X \implies \eta = f(\eta )<f(\xi )$, 즉 $\eta \in  S _{f(\xi )} = f(\xi )$ 이다. 즉, 

    $$ \eta \in \xi  \implies \eta \in f(\xi ) $$

    이다. ▲ 

    반대로 $f(\eta ) \in f(\xi ) = S _{f(\xi )} \implies f(\eta ) < f(\xi )$ 인데 $f$ 는 순서를 보존하므로 $\eta < \xi$ 이다. 그러면 가정이 성립하여 $\eta  = f(\eta )$ 이므로 $f(\eta ) < \xi$ 이다. 그러므로 

    $$ f(\eta ) \in f(\xi ) \implies f(\eta) \in \xi $$

    이다. ▲ 

    이는 어떤 원소가 $\xi$ 에 속하면 $f(\xi)$ 에 속하고, 역으로 $f(\xi)$ 에 속하면 $\xi$ 에도 속함을 뜻한다. 그러므로 $\xi = f(\xi )$ 즉, $\xi \in X$ 이다. 그러면 [정리 3.3.2](#eaed9d1d0) 에 의하여 $X = \alpha$ 이다. ■ 

!!! tldr "도움정리 3.6.2"

    서수 $\alpha ,\beta$ 에 대하여 다음이 성립한다.

    $$ \alpha < \beta \iff \alpha \in \beta \iff \alpha \subsetneq \beta $$

- 증명 

    $\alpha < \beta \implies \gamma \in \beta \text{ s.t. }\ \alpha \approxeq S _{\gamma }$ 이다. 이때 $\alpha , S _{\gamma }$ 가 서수이므로 [도움정리 3.6.1](#6d3c99905) 에 의하여 $\alpha = S _{\gamma } = \gamma \in \beta$ 이다. ▲ 

    $\alpha \in \beta$ 이면 $\alpha = S _{\alpha } \subsetneq \beta$ 이다. ▲ 

    $\alpha \subsetneq \beta$ 라고 하자. $\exists \gamma \in \alpha \text{ s.t. }\ \beta \approxeq S _{\gamma }$ 이면 $\beta = S _{\gamma } = \gamma \subset \alpha$ 가 되어 모순이다. (*즉 $\beta$ 가 $\alpha$ 의 절편과 순서동형인가 했더니 모순이라는 것이다.*) 따라서 [정리 3.3.1](#90ba9203e) 에 의하여 $\alpha$ 는 $\beta$ 의 절편과 순서동형이고, 따라서 $\alpha < \beta$ 이다. ■ 

- $A \iff B \iff C$ 를 보이기 위하여 $A \implies B \implies C \implies A$ 를 증명했네. 이러면 $B \implies C \land C \implies A \implies B$ 니까 $B \iff C$ 이고, 결국 $A \iff B \iff C$ 가 증명되는 식인듯.

!!! tldr "정리 3.6.3"

    임의의 정렬집합 $A$ 에 대하여 $A \approxeq \alpha$ 인 서수 $\alpha$ 가 유일하게 존재한다.

- 증명

    먼저 유일성 증명은 [도움정리 3.6.1](#6d3c99905) 에 의하여 해결되므로 존재성 증명만 하면 된다.

    $\forall a \in A$ 에 대하여 $S_a$ 가 어떤 서수 $\alpha (a)$ 가 존재하여 $S_a \approxeq \alpha (a)$ 를 만족한다고 가정하자. 그러면 

    $$ S = \{\alpha (a):a \in A\} $$

    를 정의할 수 있다. 이때 [정리 3.3.3](#b91fdee1f) 에 의하여 $S$ 가 서수이고 $S \approxeq A$ 을 보이면 임의의 정렬집합과 순서동형인 서수가 존재한다는 것이 증명된다. ▲ 

    먼저 $\alpha (a) \leq \alpha (b) \iff a \leq b$ 라 정의하면 $S$ 는 정렬집합이 된다. ▲ 

    임의의 $b \in A$ 에 대하여 [도움정리 3.6.2](#1d485307d) 에 의하여

    $$ \alpha (b) \in \alpha (a) \iff \alpha (b) < \alpha (a) \iff \alpha (b) \in S _{\alpha (a)} $$

    이므로 $\alpha (a) = S _{\alpha (a)}$ 이고, $S$ 가 서수임을 알 수 있다. ▲ 

    $a \mapsto \alpha (a)$ 가 $A$ 에서 $S$ 로 가는 순서동형이므로 $A \approxeq S$ 이다. ■ 

!!! tldr "정리 3.6.4"

    비어있지 않은 임의의 서수들의 집합은 최소원소를 가진다. 

- 증명 

    서수들의 집합 $E$ 의 원소 $\alpha$ 를 선택하자. $\forall \beta \in E, \alpha \leq \beta$ 이면 증명이 끝난다. 
    
    따라서 $\beta < \alpha$ 라고 하자. 그러면 $\beta \in \alpha \implies \alpha \cap E \neq \varnothing$ 이다. $\alpha \cap E$ 는 정렬집합 $\alpha$ 의 부분집합이므로 최소원소 $\gamma$ 를 가진다.

    $\delta \in E$ 라고 하자. $\alpha \leq \delta \implies \gamma < \alpha \leq \delta$ 이고, $\alpha > \delta \implies \delta \in \alpha \cap E$ 이므로 $\gamma \leq \delta$ 이다. 언제나 $\gamma \leq \delta$ 이므로 $\gamma$ 가 $E$ 의 최소원소이다.

!!! tldr ""

    서수 $\alpha$ 가 집합 $X$ 에 대하여 $\alpha = |X|$ 이면 다음이 성립한다.

    $$ \beta \leq \alpha , \beta \approx \alpha \implies \beta = \alpha $$

- 이는 기수의 정의에서 $\xi \approx X$ 인 $\xi$ 중 최소인 $\xi$ 가 $\alpha$ 라는 말이므로 $\beta \leq \alpha$ 가 $\beta \approx \alpha$ 이면 $\beta =\alpha$ 임이 당연하다.

!!! tldr ""

    시작서수 : 어떤 기수 $\alpha$ 에 대하여 기수의 정의에 의해 $\alpha$ 보다 작은 서수는 $\alpha$ 와 동등하지 않은데, 이러한 서수 $\alpha$ 를 시작서수라고 한다.

- 즉, 모든 기수는 시작서수이다. 

    역으로, $\alpha$ 가 시작서수이면 $\alpha = |\alpha|$ 이므로 기수가 된다. 즉, 임의의 시작서수는 기수이다.

!!! tldr "정리 3.6.5"

    임의의 서수들의 집합은 최소상계를 가진다.

- 증명 

    [정리 3.6.4](#f69fd2ad6) 에 의하여 서수들의 집합 $C$ 에 대한 집합

    $$ \alpha  = \bigcup_{}^{}\{\xi :\xi \in C\} $$

    은 정렬집합이다. 또한 $\xi \in \alpha$ 의 절편을 $\alpha$ 안에서 취하나 $\xi$ 안에서 취하나 마찬가지이므로 $\alpha$ 는 서수이다(*이거 왜 이해가 안되지*).

    $\forall \xi \in C$ 에 대하여 $\xi \in \alpha$ 이므로 $\xi \leq \alpha$ 이다. $\beta$ 가 $C$ 의 상계이면 $\forall \xi \in C$ 에 대하여 $\xi \subset \beta$ 이고, 따라서 $\alpha \subset \beta \implies \alpha \leq \beta$ 이다(*뭔가 너무 추상적인 논증이라 이해가 안되는 느낌인데*). 

    그러므로 $\alpha = \sup C$ 이다. ■ 

# 연속체 가설

!!! tldr "$\aleph _1$ "

    $$ \aleph _1 := \min \{\xi : \aleph _0 < |\xi| \leq 2 ^{\aleph _0} \} $$

- 이렇게 정의된 $\aleph _1$ 은 정의에 의하여 기수가 되고,

    $$ \aleph _1 > \aleph _0, \quad \xi \in \aleph _1 \implies |S _{\xi }| \leq  \aleph _0 $$

    이 성립한다.

!!! tldr ""

    $$\aleph _1 = \sup \{\xi : \xi \approx \aleph _0\}$$

- 증명

!!! tldr "연속체 가설(Continuum hypothesis)"

    $$\aleph _1 = 2 ^{\aleph _0}$$

- 이 정리는 쉽게 말해 자연수의 개수보다 많고 실수의 개수보다 적은 집합이 존재하지 않음을 말한다.

- 증명 

    선택공리를 가정한 체르멜로-프렝켈 집합론(ZFC) 가 무모순이라면, 연속체 가설은 ZFC 와 독립적이다. 즉, 연속체 가설이 참이든, 거짓이든 ZFC 공리체계로 증명되지도 않고 반박되지도 않는다.

    결론은 "증명할 수 없다." 이다.

- 유클리드 기하학의 평행선 공리는 역사적으로 증명되거나, 반박되려 했으나 모두 실패했다. 수학자들은 평행선 공리가 거짓임을 증명하려고 일단 평행선 공리를 가정하고 공리체계를 이끌어내어 모순을 얻으려 했으나, 결국 모순을 얻지 못하였고 그들이 만들어낸 새로운 기하학 공리체계가 비유클리드 기하학을 형성했음을 알게 되었다. 

    연속체 가설이 기하학에서의 평행선 공리와 같은 위치에 있다.

!!! tldr "$\aleph _n$ "

    $$ \aleph _n := \min \{\xi : \aleph _{n-1} < |\xi| \leq 2 ^{\aleph _{n-1}} \} $$

- 이 정의는 [정리 2.1.2](../numbers#3a99b431b) 를 사용하여 $\aleph _1$ 의 정의를 임의의 자연수 $n = 1, 2, \dots$ 에 대하여 확장한 것이다.

- 또한 $\aleph _{\omega } = \sup \{\aleph _n:n < \omega \}$ 라 두면 새로운 기수를 계속해서 얻을 수 있다.

!!! tldr "일반 연속체 가설(generalized continuum hypothesis)"

    임의의 기수 $\alpha$ 에 대하여 $\aleph _{\alpha ^{+}} = 2 ^{\aleph _{\alpha }}$ 이다.

- 증명