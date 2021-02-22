
# 자연수의 정의

!!! tldr ""

    집합 $A ^{+}$ : 집합 $A$ 에 대한 집합 $A ^{+}$ 을 

    $$ A ^{+} = A \cup \{A\} $$

    으로 정의한다. 

- 예시 

    $0 = \emptyset$ 으로 두고,

    $$ 1 = 0 ^{+}, 2 = 1 ^{+}, 3 = 2 ^{+}, \dots $$

    으로 정의하면 

    $$ 0 = \emptyset $$

    $$ 1 = 0 ^{+} = 0 \cup \{0\} = \emptyset \cup \{0\} = \{0\} $$

    $$ 2 = 1 ^{+} = 1 \cup \{1\} = \{0\} \cup \{1\} = \{0, 1\} $$

    $$ 3 = 2 ^{+} = 2 \cup \{2\} = \{0, 1\} \cup \{2\} = \{0, 1, 2\} $$

    이다.

!!! tldr ""

    자연수(natural number) : 다음 두 가지 성질 

    $$ \emptyset \in \mathcal{A}, A \in \mathcal{A} \Rightarrow A ^{+} \in \mathcal{A} $$

    을 가지는 집합 $\mathcal{A}$ 들의 전체의 교집합을 $\N$ 이라고 할 때,

    $\N$ 의 원소를 자연수라고 한다.

- 집합 $\N$ 은 다음 성질을 만족하고, 이 성질을 페아노 공리계라고 한다. 

    1. $0 \in \N$

    2. $n \in \N \Rightarrow n ^{+} \in \N$

    3. $\forall n \in \N, n ^{+} \neq 0$

    4. 집합 $X \subset \N$ 이 다음 두 성질 

        $$ 0 \in X, \qquad  n \in X \Rightarrow n ^{+}\in X $$

        을 만족하면 $X = \N$ 이다. 

    5. 만일 $m, n \in \N$ 에 대하여 $m ^{+} = n ^{+}$ 이면 $m=n$ 이다.

- 세번째 성질은 $n ^{+} = n \cup \{n\} \neq \emptyset$ 이므로 당연하고, 네번째 성질은 수학적 귀납법을 통하여 증명된다. 다섯번째 성질의 증명은 다음과 같다. 

    먼저 

    $$ n \in n ^{+} = m ^{+} = m \cup \{m\} $$

    이므로 $n \in m \lor n = m$ 이다. 마찬가지로 $m \in n \lor n = m$ 이다. 그러므로 $n \in m$ 과 $m \in n$ 에서 $n = m$ 을 이끌어내면 된다. 그렇다면

    $$ n \in \N, x \in n \Rightarrow x \subset n \tag{1}  $$

    을 증명하면 $n \subset m \land m \subset n$ 이 성립하여 $n = m$ 을 이끌어낼 수 있다. 

    일단 

    $$ X = \{n \in \N : x \in n \Rightarrow x \subset n\} $$

    으로 두자. 먼저 $0 \in X$ 이다. $x \in \emptyset \Rightarrow x \subset \emptyset$ 이기 때문이다.

    이제 수학적 귀납법으로 증명을 하기 위하여 $n \in X$ 라고 하자. 만약 $x \in n ^{+} = n \cup \{n\}$ 이면 $x \in n \lor x = n$ 이다. 

    $x = n$ 이면 $x = n \subset n ^{+}$ 이고, $x \in n$ 이면 집합 $X$ 의 조건에 의하여 $x \subset n$ 이므로 $x \subset n \subset n ^{+}$ 이다. 그러므로

    $$ \therefore X = \N $$

    이다. 그렇다면 조건 $(1)$ 를 모든 자연수가 만족한다는 것이다. 그러므로 증명이 끝났다. 

- 정리 

    집합 $X$ 의 한 원소 $a \in X$ 와 함수 $f: X \to X$ 에 대하여 다음 성질 

    $$ \gamma (0) = a \tag{1} $$

    $$ \forall n \in \N, \gamma (n ^{+}) = f(\gamma (n)) \tag{2}$$

    을 만족하는 함수 $\gamma : \N \to X$ 가 유일하게 존재한다. 

    - 이 정리는 집합 $X$ 의 원소 $\gamma (0), \gamma (1), \gamma (2), \dots$ 가 특정 점화식을 만족하도록 귀납적으로 정의할 수 있음을 말해준다. 이는 자연수의 연산을 정의하는데 중요한 역할을 한다. 

    - 함수 $f$ 는 $\gamma$ 가 씌워진 자연수 $n$ 에 $^{+}$ 를 한 효과를 준다고 직관적으로 이해해보자. 즉, $f(\gamma (n)) = \gamma (n ^{+})$ 인 것이다.

    - 증명 

        $(1),(2)$ 를 동시에 만족하는 함수 $\gamma _1, \gamma _2$ 가 있다고 가정하고 

        $$ X = \{n \in \N: \gamma _1(n) = \gamma _2(n)\} $$

        라고 하자.

        일단 $\gamma _1 (0) = a = \gamma _2(0)$ 이므로 $0 \in X$ 이다. 만약 $n \in X$ 이면 

        $$ \gamma _1(n ^{+}) = f(\gamma _1(n)) = f(\gamma _2(n)) = \gamma _2(n ^{+}) $$

        이므로 $n ^{+} \in X$ 이다. 그러므로 수학적 귀납법에 의하여 

        $$ X = \N $$

        이고 
        
        $$ \therefore \forall n \in \N, \gamma _1(n) = \gamma _2(n) $$

        이다. 

        이제 존재성을 보이기 위하여 다음 성질 

        $$ (0, a) \in A, (n, x) \in A \Rightarrow (n ^{+}, f(x)) \in A $$

        을 만족하는 $A \subset \N \times X$ 전체의 집합을 $\mathcal{A}$ 라 두면 $\N \times X \in \mathcal{A}$ 이므로(**이해 안되는 부분**) $\mathcal{A}$ 는 비어있지 않다. 

        