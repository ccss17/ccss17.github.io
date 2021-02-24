
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

    을 가지는 집합 $\mathcal{A}$ 에 대하여 집합

    $$ \N := \bigcap_{}^{}\mathcal{A} $$

    의 원소를 자연수라고 한다.

!!! tldr ""

    페아노 공리계 : 집합 $\N$ 은 다음 성질을 만족하고, 이 성질을 페아노 공리계라고 한다. 

    1. $0 \in \N$

    2. $n \in \N \Rightarrow n ^{+} \in \N$

    3. $\forall n \in \N, n ^{+} \neq 0$

    4. 집합 $X \subset \N$ 이 다음 두 성질 

        $$ 0 \in X, \qquad  n \in X \Rightarrow n ^{+}\in X $$

        을 만족하면 $X = \N$ 이다. 

    5. 만일 $m, n \in \N$ 에 대하여 $m ^{+} = n ^{+}$ 이면 $m=n$ 이다.

- 세번째 성질은 $n ^{+} = n \cup \{n\} \neq \emptyset$ 이므로 당연하고, 

    네번째 성질은 수학적 귀납법을 통하여 증명된다. 
    
    다섯번째 성질의 증명은 다음과 같다. 먼저 

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

!!! tldr ""

    집합 $X$ 의 한 원소 $a \in X$ 와 함수 $f: X \to X$ 에 대하여 다음 성질 

    $$ \gamma (0) = a \tag{1} $$

    $$ \forall n \in \N, \gamma (n ^{+}) = f(\gamma (n)) \tag{2}$$

    을 만족하는 함수 $\gamma : \N \to X$ 가 유일하게 존재한다. 

- 이 정리는 집합 $X$ 의 원소 $\gamma (0), \gamma (1), \gamma (2), \dots$ 가 특정 점화식을 만족하도록 귀납적으로 정의할 수 있음을 말해준다. 이는 자연수의 연산을 정의하는데 중요한 역할을 한다. 

- 함수 $f$ 는 $\gamma$ 가 씌워진 자연수 $n$ 에 $^{+}$ 를 한 효과를 준다고 직관적으로 이해해보자. 즉, $f(\gamma (n)) = \gamma (n ^{+})$ 인 것이다.

- 유일성 증명 

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

- 존재성 증명

    *($X = \N$ 이지만 계속 $X$ 라는 표기를 사용한다. 따라서 이는 상징적인 의미이다. 즉, $X$ 를 $\gamma$ 의 출력 집합이라고 생각하면 될 것 같다.)*

    이제 존재성을 보이기 위하여 다음 성질 

    $$ (0, a) \in A\tag{1.1} $$

    $$  (n, x) \in A \Rightarrow (n ^{+}, f(x)) \in A \tag{1.2} $$

    을 만족하는 $A \subset \N \times X$ 전체의 집합을 $\mathcal{A}$ 라 두면 이 성질을 만족하는 모든 집합이 $\mathcal{A}$ 에 속하게 되므로 $\N \times X$ 도 $\mathcal{A}$ 에 속한다. 즉, $\N \times X \in \mathcal{A}$ 이다. 따라서 $\mathcal{A}$ 는 비어있지 않다. 

    *(이러한 $A$ 는 곱집합의 부분집합인 함수 $\gamma$ 의 기반을 정의하기 위해서 생성되었다. 그러므로 이제 집합 $A$ 가 같은 입력에 대하여 다른 출력을 가지지 않는다는 것을 증명하면 함수의 조건이 충족된다.)*

    이제 $\gamma = \bigcap_{}^{}\mathcal{A}$ 라고 두자. 만일 $\gamma \subset \N \times X$ 가 함수이면 

    $$ \gamma (n) = x \Rightarrow (n, x) \in \gamma $$

    $$ \Rightarrow (n ^{+}, f(x)) \in \gamma  $$ 
    
    $$ \Rightarrow \gamma (n ^{+}) = f(x) = f( \gamma (n)) $$

    이다. 

    *(이로써 $\N \times X$ 의 부분집합 $\gamma = \bigcap_{}^{}\mathcal{A}$ 가 함수라면 자연수 전체에서 성립함을 보였다. 그러므로 $\gamma$ 가 함수임을 증명하기만 하면 된다.)*
    
    그러므로 $\gamma \subset \N \times X$ 가 함수임을 보이면 증명이 끝난다. 이를 위하여 $\gamma$ 가 함수임을 보장하는 입력 집합

    $$ \mathcal{X} = \{n \in \N:(n,x) \in \gamma \text{ 를 만족하는 } x \in X \text{ 가 유일하게 존재한다}\} $$

    을 정의하고 귀납법을 사용하자. 만약 $0 \not \in \mathcal{X}$ 라면 $(0,b) \in \gamma , b \neq a$ 인 $b \in X$ 가 존재한다. 왜냐하면 $0$ 이 $\gamma$ 가 함수임을 보장하는 입력 집합에 속하지 않았으므로 $0$ 을 $\gamma$ 에 입력하면 출력이 2개 이상 나올 것이기 때문이다. 

    그런데 $b \neq a$ 이므로 페아노 공리계 성질 3) $\forall n \in \N, n ^{+} \neq 0$ 에 의하여 $\gamma \text{ \textbackslash } \{(0,b)\} \subset \N \times X$ 도 $(1.1), (1.2)$ 을 만족한다. 이는 $\gamma = \bigcap_{}^{}\mathcal{A}$ 에 모순이다. 

    *($(1.1), (1.2)$ 을 만족하는 집합 $A$ 중에는 $(0, b) \in A$ 인 집합과 $(0, b) \not \in A$ 인 집합도 존재한다. 그러므로 $\gamma = \bigcap_{}^{} \mathcal{A}$ 에는 $(0,b)$ 가 존재하지 않다. 즉, $(0, b) \not \in \gamma$ 이다. 즉, 증명에서 이것을 $\gamma$ 에 $(0, b)$ 를 제외한 집합 $\gamma \text{ \textbackslash }\{(0,b)\}$ 도 $(1.1), (1.2)$ 을 만족한다면 $\gamma = \bigcap_{}^{}\mathcal{A}$ 에 모순이라는 식으로 보인 것이다. 왜냐하면 어떤 원소를 $\gamma$ 에서 제외해도 $(1.1), (1.2)$ 이 성립한다면 교집합에 포함되지 않을 것이기 때문에 집합족의 교집합으로 정의한 $\gamma$ 집합의 조건에 위배되기 때문이다.)*

    그러므로 

    $$ 0 \in \mathcal{X} $$

    이다.

    이제 $n \in \mathcal{X}$ 이지만 $n ^{+} \not \in \mathcal{X}$ 라고 하면 $(n ^{+}, f(x)) \in \gamma$ 이므로 $(n ^{+}, y) \in \gamma , y \neq f(x)$ 인 $y \in X$ 가 존재한다. 그러면 마찬가지로 $\gamma \text{ \textbackslash }\{(n ^{+}, y)\} \in \mathcal{A}$ 임을 보이면 $\gamma = \bigcap_{}^{}\mathcal{A}$ 에 모순이고, 결국 $y$ 는 존재하지 않으며 최종적으로 

    $$ n \in \mathcal{X} \Rightarrow n ^{+} \in \mathcal{X} $$

    이 증명된다. 그렇게 되면 $\gamma$ 가 함수임을 보장하는 공간 $\mathcal{X}$ 는
    
    $$ \mathcal{X} = \N $$

    이고, 결국 $\gamma$ 는 항상 함수가 되어 모든 증명이 끝난다.

    *(즉, 이제 $\gamma \text{ \textbackslash }\{n ^{+}, y)\}$ 가 $(1.1), (1.2)$ 을 만족함을 보이면 되는 것이다.)*

    일단 $n ^{+} \neq 0$ 이므로 $(0, a) \in \gamma \text{ \textbackslash }\{(n ^{+}, y)\}$ 이다. 이제 

    $$ (m, z) \in \gamma \text{ \textbackslash }\{(n ^{+}, y)\} $$

    라고 하자. 만약 $m = n$ 이면 $z = x$ 이고, 또한 $y \neq f(x)$ 이므로 $(m ^{+}, f(z)) = (n ^{+}, f(x)) \in \gamma \text{ \textbackslash }\{(n ^{+}, y)\}$ 이다. 만약 $m \neq n$ 이면 페아노 공리계 성질 5) 에 의하여 $m ^{+} \neq n ^{+}$ 이고, 따라서 

    $$ (m ^{+}, f(z)) \in \gamma \text{ \textbackslash }\{(n ^{+}, y)\} $$

    이다. 그러므로 $\forall (n, x) \in \gamma \text{ \textbackslash }\{(n ^{+}, y)\}$ 에 대하여 $(1.2)$ 가 성립한다. 이것으로 모든 증명이 끝났다. ■ 

!!! tldr ""

    더하기 : 각 자연수 $m \in \N$ 에 대하여 

    $$ \gamma _m(0) = m, \qquad n \in \N \Rightarrow \gamma _m(n ^{+}) = [\gamma _m(n)]^{+} $$

    를 만족하면서 유일하게 존재하는 함수 $\gamma _m:\N \to \N$ 에 대하여 자연수의 더하기를 $m, n \in \N$ 에 대하여 

    $$ m + n = \gamma _m(n) $$

    라고 정의한다. 

- 그러면 $m, n \in \N$ 에 대하여 

    $$ m + 0 = m, \qquad m + n ^{+} = (m + n) ^{+} $$

    이 성립한다.

- 이런 성질은 $n \in \N$ 에 대하여

    $$ n ^{+} = 1 + n $$

    이다 를 기반으로 한다.

    - 증명 

        먼저 

        $$ 0 ^{+} = 1 = 1 + 0 $$

        이다. 왜냐하면 더하기의 정의에 따라 $1+0 = \gamma _1(0) = 1$ 이기 때문이다. 한편 이 등식이 자연수 $n$ 에 대하여 성립한다고 가정하면 다음과 같이 $n+1$ 에서도 성립한다.

        $$ (n ^{+}) ^{+} = (1 + n) ^{+} = 1 + n ^{+} $$

        그러므로 수학적 귀납법을 적용할 수 있으므로 증명이 끝났다. 

!!! tldr ""

    곱하기 : 각 자연수 $m \in \N$ 에 대하여 

    $$ \delta _m(0) = 0, \qquad n \in \N \Rightarrow \delta _m(n ^{+}) = \delta _m(n)+m $$

    를 만족하면서 유일하게 존재하는 함수 $\delta _m: \N \to \N$ 에 대하여 자연수의 곱하기를 $m,n \in \N$ 에 대하여

    $$ mn = \delta _m(n) $$

    라고 정의한다. 

- 그러면 $m, n \in \N$ 에 대하여 

    $$ m0 = 0, \qquad mn ^{+} = mn + m $$

    이 성립한다. 

!!! tldr ""

    $\forall m,n,k \in \N$ 에 대하여 다음이 성립한다. 

    1. $0+n=n, (m+n)+k=m+(n+k), m+n=n+m$ (더하기의 항등원/결합법칙/교환법칙)

    2. $0n=0, 1n = n, (mn)k=m(nk), mn=nm$ (곱하기의 항등원/결합법칙/교환법칙)

    3. $m(n+k)=mn+mk, (n+k)m=nm+km$ (더하기와 곱하기의 분배법칙)

- 증명 

    수학적 귀납법으로 모든 명제를 증명할 수 있다. 가령 이미 참임을 알고 있는 명제 $0 + 0 = 0$ 에서 출발하여 

    $$ 0 + n = n \Rightarrow 0 + n ^{+} = (0 + n) ^{+} = n ^{+} $$

    이므로 1) 의 첫째 명제가 증명된다.

    둘째 명제는 $m,n$ 을 고정하고 $k$ 에 대한 귀납법을 사용한다.

!!! tldr ""

    자연수의 순서 : 두 자연수 $m, n \in \N$ 에 대하여 

    $$ m \leq n \iff m \in n \lor m = n $$

    이다. 

- 자연수의 순서의 정의에 따라 다음과 같은 성질이 생긴다. 

    1. $m \leq m$ 이다.

    2. $m \leq n \land n \leq m \Rightarrow m = n$ 이다. 

        - 증명 

            $m \neq n$ 이면 $m \in n \land n \in m$ 인데 페아노 공리계의 5번째 성질을 증명할 때 사용했던 정리 

            $$ n \in \N, x \in n \Rightarrow x \subset n $$

            에 의하여 $m \subset n, n \subset m$ 이 성립하므로 

            $$ m = n $$

            이 된다. 이는 처음의 가정과 모순이다. 그러므로 $m = n$ 이다.
    
    3. $m \leq n, n \leq k \Rightarrow m \leq k$ 이다.

        - 증명 

            $m \leq n, n \leq k$ 는 다음 4가지 경우를 내포한다. 

            $$ m \in n, n \in k, \qquad m \in n, n = k, \qquad m = n, n \in k, \qquad m = n, n = k $$

            처음 3가지 경우에서 $m \in k$ 가 성립하고, 마지막 경우에는 $m = k$ 가 성립하므로 

            $$ \therefore m \leq k $$

            이다. ■ 

            또한 이로써 $\leq$ 는 순서관계가 된다.
            
!!! tldr ""

    $\forall n \in \N$ 에 대하여 

    $$ n \not \in n $$

    이다. 

- 증명 

    이것을 수학적 귀납법으로 보이기 위하여 

    $$ n \not \in n \Rightarrow n ^{+} \not \in n ^{+} $$

    임을 보이면 되는데, 이것의 대우 명제인 

    $$ n ^{+} \in n ^{+} \Rightarrow n \in n $$

    을 보여도 된다. 만약 $n ^{+} \in n ^{+} = n \cup \{n\}$ 이면 $n ^{+} \in n \lor n ^{+} = n$ 이다. 이때 $n ^{+}\in n$ 이면 페아노 공리계의 5번째 성질을 증명할 때 사용했던 정리 

    $$ n \in \N, x \in n \Rightarrow x \subset n $$

    에 의하여 $n \subset n ^{+} \subset n$ 이므로 $n ^{+} = n$ 이다. 그러므로 항상 

    $$ n ^{+} = n $$

    인데, 이것에서부터 $n \cup \{n\} = n ^{+} = n$ 을 도출할 수 있다. 그렇다면 $\{n\}$ 이 $n$ 의 부분집합이 되므로 

    $$ \{n\} \subset n $$

    이고 이에따라 $n \in n$ 이다. 그러므로 증명이 끝났다. ■ 

- 또한 $\forall n \in \N, n \not \in n$ 이 증명되었으므로 

    $$ m \leq n, m \neq n \iff m \in n $$

    이 성립함을 알 수 있다. 

!!! tldr ""

    두 자연수 $m,n \in \N$ 이 $m \in n$ 일 때 

    $$ m < n $$

    이라고 쓴다.

- 이 정리에 따라 

    $$ m \leq n, m \neq n \iff m < n $$

    이 성립한다.

- 이 정리는 자연수 집합에 정의된 순서관계의 핵심적인 성질이다.
