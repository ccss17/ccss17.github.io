
# 자연수의 정의

!!! tldr ""

    집합 $A ^{+}$ : 집합 $A$ 에 대한 집합 $A ^{+}$ 을 

    $$ A ^{+} = A \cup \{A\} $$

    으로 정의한다. 

- 예시 

    $0 = \varnothing$ 으로 두고,

    $$ 1 = 0 ^{+}, 2 = 1 ^{+}, 3 = 2 ^{+}, \dots $$

    으로 정의하면 

    $$ 0 = \varnothing $$

    $$ 1 = 0 ^{+} = 0 \cup \{0\} = \varnothing \cup \{0\} = \{0\} $$

    $$ 2 = 1 ^{+} = 1 \cup \{1\} = \{0\} \cup \{1\} = \{0, 1\} $$

    $$ 3 = 2 ^{+} = 2 \cup \{2\} = \{0, 1\} \cup \{2\} = \{0, 1, 2\} $$

    이다.

!!! tldr ""

    자연수(natural number) : 다음 두 가지 성질 

    $$ \varnothing \in \mathcal{A}, A \in \mathcal{A} \Rightarrow A ^{+} \in \mathcal{A} $$

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

- 세번째 성질은 $n ^{+} = n \cup \{n\} \neq \varnothing$ 이므로 당연하고, 

    네번째 성질은 수학적 귀납법을 통하여 증명된다. 
    
    다섯번째 성질의 증명은 다음과 같다. 먼저 

    $$ n \in n ^{+} = m ^{+} = m \cup \{m\} $$

    이므로 $n \in m \lor n = m$ 이다. 마찬가지로 $m \in n \lor n = m$ 이다. 그러므로 $n \in m$ 과 $m \in n$ 에서 $n = m$ 을 이끌어내면 된다. 그렇다면

    $$ n \in \N, x \in n \Rightarrow x \subset n \tag{1}  $$

    을 증명하면 $n \subset m \land m \subset n$ 이 성립하여 $n = m$ 을 이끌어낼 수 있다. 

    일단 

    $$ X = \{n \in \N : x \in n \Rightarrow x \subset n\} $$

    으로 두자. 먼저 $0 \in X$ 이다. $x \in \varnothing \Rightarrow x \subset \varnothing$ 이기 때문이다.

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

    $$\forall n \in \N, n \not \in n$$

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

!!! tldr ""

    비어있지 않은 자연수들의 집합은 최소 원소를 가진다. 

- 증명 

    비어있지 않은 자연수들의 집합 $A \subset \N$ 가 최소 원소를 가지지 않는다고 하고 

    $$ X = \{n \in \N: m \in A \Rightarrow n \leq m\} $$

    이라고 두자. 즉, $X$ 는 집합 $A$ 의 최소 원소보다 같거나 작은 자연수로 구성된다. 만약 $k \in X \cap A$ 이면 $k$ 는 $A$ 의 최소 원소가 되므로 $X \cap A = \varnothing$ 이어야 한다. 여기서 귀납법으로 $X = \N$ 임을 보이면 $A = \varnothing$ 이 되어 모순을 얻는다. 

    그러므로 먼저 $0 \in X$ 라고 가정하자. 즉, $\forall m \in \N$ 에 대하여 $0 \leq m$ 임을 보이는 것이다. 이렇게 $\forall m \in \N$ 인 $m$ 에 대하여 보이게 되면 $A$ 가 어떤 원소로 구성되었든 간에 안정적으로 $0 \in X$ 를 보일 수 있다. 이것 또한 귀납법으로 보이게 된다. 먼저 $0 \leq 0$ 은 자명하다. 만약 $0 \leq m$ 이면 $m \in m ^{+}$ 에서 $m \leq m ^{+}$ 이므로 $0 \leq m ^{+}$ 을 얻는다. 그러므로 $0 \in X$ 이 증명되었다. 

    이제 $n \in X \Rightarrow n ^{+} \in X$ 을 보이기 위하여 $n \in X$ 라고 가정하자. 즉, 

    $$ m \in A \Rightarrow n \leq m $$

    이라고 두는 것이다. 만약 $n \in A$ 이면 $n$ 은 $A$ 의 최소원소가 되고 이는 가정에 어긋난다. 그러므로 $n \not \in A$ 이고 

    $$ m \in A \Rightarrow n < m $$

    이 성립한다. 이제 

    $$ n < m \Rightarrow n ^{+} \leq m $$

    을 보이면 $X = \N$ 이 되어 모든 증명이 끝난다. 이것에도 귀납법을 사용하는데, $n$ 을 고정하고 $m$ 에 대한 귀납법을 사용하기 위하여 

    $$ Y = \{m \in \N : n < m \Rightarrow n ^{+} \leq m\} $$

    라고 두자. 먼저 $n < 0$ 이면 $n \in \varnothing$ 인데 이런 원소 $n$ 이 없으므로 $0 \in Y$ 임은 자명하다.(**이해 안되는 부분**) 

    이제 $m \in Y$ 라고 가정하고, $m ^{+} \in Y$ 임을 보이자. $n < m ^{+}$ 이면, 
    
    $$n \in m ^{+} = m \cup \{m\} \Rightarrow n \in m \lor n = m$$
    
    이다. 먼저 $n \in m$ 이면 $n < m$ 이므로 귀납법의 가정 $m \in Y$ 에 의하여 

    $$ n ^{+} \leq m < m ^{+} $$

    이고, $n = m$ 이면 $n ^{+} = m ^{+}$ 이므로 항상 

    $$ n ^{+} \leq m ^{+} $$

    이다. 그러므로 

    $$ n < m ^{+} \Rightarrow n ^{+}\leq m ^{+} $$
    
    가 성립하고 $m ^{+} \in Y$ 임에 따라

    $$ Y = \N $$

    이고 이로써 모든 증명이 끝났다. ■ 

!!! tldr ""

    $$\forall m,n \in \N, m \leq n \lor n \leq m$$

- 증명 

    $\forall  m,n \in \N$ 에 대하여 $\{m,n\} \subset \N$ 은 최소원소를 갖는데, 

    $$ (\min \{m,n\} = m \Rightarrow m \leq n) \lor (\min \{m,n\} = n \Rightarrow n \leq m) $$

    이다.

!!! tldr ""

    $$ n \in \N \Rightarrow n = 0 \lor (\exists m \in \N, n = m ^{+}) $$

- 증명 (이 증명의 풀이는 책에 나와있는게 아니라 문제로 되어있어서 내가 만든 것. 그래서 오류가 있을 수 있음)

    $n = 0$ 일 경우 $0 = 0$ 이다.

    $n = x(x \neq 0)$ 일 경우 성립한다고 가정하고 $n = x ^{+}$ 일때도 성립함을 보이자. $n = x$ 이면 
    
    $$ \exists m \in \N, x = m ^{+} $$

    이다. 그러면 

    $$ \iff x ^{+} = [m ^{+}] ^{+} $$

    인데 페아노 공리계 2) $n \in \N \Rightarrow n ^{+} \in \N$ 은 어떤 자연수 $n$ 에 $^{+}$ 를 취하면 그것도 자연수가 됨을 보증해준다. 그러므로 

    $$ [m ^{+}] ^{+} \in \N $$

    이다. 이로써 모든 증명이 끝났다. ■ 

!!! tldr ""

    위로 유계이며 비어있지 않은 자연수들의 집합 $A \subset \N$ 는 최대 원소를 가진다. 

- 증명 

    집합 $A$ 의 상계 전체의 집합을 $B$ 라 두면, 가정에 의하여 $B \neq \varnothing$ 이고 정리 "비어있지 않은 자연수들의 집합은 최소 원소를 가진다." 에 의하여 $B$ 는 최소 원소 $k \in \N$ 를 가진다. $\forall n \in A, n \leq k$ 이므로 이므로 $k \in A$ 임을 보이면 $k$ 가 $A$ 의 최대원소임이 증명된다.

    $k \not \in A$ 라고 가정하자. 그러면 $n \in A$ 을 하나 잡았을 때 $k > n \geq 0$ 이고 따라서 정리 "$n \in \N \Rightarrow n = 0 \lor (\exists m \in \N, n = m ^{+})$" 에 의하여 $k = s ^{+}$ 이다. 

    만약 $s \not \in B$ 이면 $s < t$ 인 $t \in A$ 가 존재(**이해 안되는 부분**)하고 

    $$ s ^{+} \leq t \leq k = s ^{+} \Rightarrow k = t \in A $$

    가 되어 모순이다. 그러므로 $s \in B$ 인데, $s < k$ 이므로 이는 $k$ 가 최소원소라는 것에 모순이다.

    그러므로 

    $$ k \in A $$

    이다. 

!!! tldr ""

    $\forall n,m,k \in \N, n = m + k \to n \geq m$ 이고, 
    
    역으로 두 자연수 $m,n \in \N$ 에 대하여 $n \geq m$ 이면 $n=m+k$ 를 만족하는 자연수 $k \in \N$ 가 유일하게 존재한다.

- 이 정리는 큰 수에서 작은 수를 뺄 수 있음을 말해주는데, 이는 정수를 정의하는데 중요한 역할을 한다. 

- 이 정리의 유일성은 

    $$ \forall m,k,l \in \N, m + k = m + l \Rightarrow k = l $$

    로 명확하게 표현할 수 있다.

- 첫번째 명제의 증명 

    $m+k \geq m$ 을 보이면 되는데 $k$ 에 관한 귀납법을 사용한다. $k=0$ 이면 당연히 성립하고 $m+k \geq m$ 이라고 가정하면 

    $$ m+k ^{+} = (m+k) ^{+} > m+ k \geq m $$

    이다. ■ 

- 두번째 명제의 존재성 증명 

    $$ X = \{l \in \N, m+l \geq n\} $$

    라 두면 $n \in X \Rightarrow X \neq \varnothing$ 이다. 따라서 정리 "비어있지 않은 자연수들의 집합은 최소 원소를 가진다." 에 의하여 $X$ 는 최소 원소 $k \in X$ 를 가지는데, $n = m+k$ 를 증명하면 된다. 

    먼저 $m+k>n$ 라고 가정하자. (*이는 $n = m+k$ 를 만족하는 $k$ 가 존재하지 않는다고 가정하는 것이다. 그러므로 이 가정으로부터 모순이 도출된다면 $k$ 는 존재한다는 것이 증명된다.*) $k=0$ 이면 $m>n$ 이 가정 $n \geq m$ 에 위배되므로 $k \neq 0$ 이고 정리 "$n \in \N \Rightarrow n = 0 \lor (\exists m \in \N, n = m ^{+})$" 에 의하여 $s \in \N, k = s ^{+}$ 이다. 그러면 

    $$ (m + s) ^{+} = m + s ^{+} = m + k > n $$

    에서 $m + s \geq n$ 이고, 이에따라 $s \in X$ 인데 $s < s ^{+} = k$ 이므로 $k$ 가 $X$ 의 최소원소라는 데에 모순이다. ■ 

- 두번째 명제의 유일성 증명 

    두번째 명제의 유일성 증명은

    $$ \forall m,k,l \in \N, m + k = m + l \Rightarrow k = l $$

    를 $k$ 에 관한 귀납법으로 보임으로써 완성된다. $k=0$ 이면 

    $$ m + 0 + m + l \Rightarrow 0 = l $$

    이다. 만약 $m=m+l$ 인데 $l \neq 0$ 이면 $l = s ^{+}$ 이고,

    $$ m = m+l = m + s ^{+} = (m+s) ^{+} \geq m ^{+} > m $$

    이 되어 모순이다. 그러므로 $l = 0$ 이다.

    이제 $k$ 에 대하여 성립한다고 가정하고 $k ^{+}$ 에서 성립함을 보이면 된다. 

    $$ m + k ^{+} = m + l $$

    이라고 두자. 여기에서 $l = 0$ 이면 존재성 증명에서 보인바와 같이 $k ^{+} = 0$ 이므로 $l \neq 0$ 이고 $l = t ^{+}$ 이다. 그러면 

    $$ (m+k)^{+}=m+k ^{+}=m+l=m+t ^{+}=(m+t)^{+} $$

    에서 $m+k=m+t$ 를 얻고, 가정에 의하여 $k=t$ 와 $k ^{+}=t ^{+} = l$ 을 얻는다. 이것으로써 

    $$ \forall m,k,t \in \N, m + k ^{+} = m + t ^{+} \Rightarrow k ^{+} = t ^{+} $$

    를 얻었으므로 유일성 증명이 끝났다. ■ 

!!! tldr ""

    $m,l \in \N, 0 < m \leq l$ 이면 

    $$ l=mn+r, \qquad 0 \leq r<m $$

    을 만족하는 자연수 $n,r \in \N$ 이 유일하게 존재한다. 

- 존재성 증명 

    집합 $P = \{k \in \N:mk \leq l\}$ 는 $1 \in P$ 이므로 $P \neq \varnothing$ 이다. 또한 $\forall k \in P, k \leq mk \leq l$ 이므로 $P$ 는 위로 유계이다. 그러므로 정리 "위로 유계이며 비어있지 않은 자연수들의 집합 $A \subset \N$ 는 최대 원소를 가진다." 에 의하여 $P$ 는 최대원소 $n$ 을 가진다. 그러면 

    $$ mn \leq l < mn ^{+} = mn + m $$

    이므로 (*이렇게 되는 것은 매우 간단한데, $l \geq mn ^{+}$ 가 성립한다면 $n$ 이 최대원소라는 가정에 모순이기 때문이다.*) 정리 "$m,n \in \N$ 에 대하여 $n \geq m$ 이면 $n=m+k$ 를 만족하는 자연수 $k \in \N$ 가 유일하게 존재한다." 에 의하여 

    $$ l = mn + r $$

    인 $r \in \N$ 이 유일하게 존재한다. 이때 $mn + r < mn + m \Rightarrow r < m$ 이다. ■ 

    한편 이 증명으로 $n, r$ 의 존재성 증명이 끝남과 동시에 $r$ 의 유일성 증명도 끝났으므로 $n$ 의 유일성 증명만 하면 된다.

- 유일성 증명 

    $$ l = mk+s, \qquad 0 \leq s < m, \qquad k \neq n $$

    이라고 하자. 그러면 $k < n \lor k > n$ 이다. $k < n$ 이면 $k ^{+} \leq n$ 이므로 $mk ^{+} \leq mn \leq l$ 인데
    
    $$ l = mk + s < mk + m = mk ^{+} $$

    이므로 모순이다. 같은 방식으로 $k>n$ 도 모순을 도출한다. 그러므로 

    $$ \therefore k = n $$

    이다. ■ 

# 정수의 정의

!!! tldr ""

    빼기 : $n \leq m$ 인 $m,n \in \N$ 은 정리 

    "두 자연수 $m,n \in \N$ 에 대하여 $n \geq m$ 이면 $n=m+k$ 를 만족하는 자연수 $k \in \N$ 가 유일하게 존재한다."

    에 의하여 $m = n + k$ 인 $k \in \N$ 가 유일하게 존재하는데 이 $k$ 를 

    $$ k := m - n $$

    라고 정의한다. 

!!! tldr ""

    정수 집합(integer set) : 동치관계 

    $$ (m,n)\sim (m',n') \iff m+n'=n+m' $$

    가 부여된 집합 $\N \times \N$ 에 대하여 집합 
    
    $$\N \times \N/ \sim\ = \mathbb{Z}$$

    을 정수 집합 $\mathbb{Z}$ 이라고 정의한다. 

- 이때 동치류 $[(m,n)]$ 을 간단하게 $[m,n]$ 로 표현하면 집합 $\mathbb{Z}$ 의 모든 원소를 자연수 $n = 1,2,\dots$ 에 대하여 

    $$ [n,0],[0,0],[0,n] $$

    으로 표현할 수 있다. 

    - $[n, 0]$ 를 $n$ 으로, $[0, 0]$ 을 $0$ 으로 $[0, n]$ 을 $-n$ 으로 이해하면 편하다. 왜냐하면 정수 집합의 동치관계는 결국 

        $$ (m,n) \sim (m',n') \iff m-n = m'-n' $$

        과 같기 때문이다. 

- $\mathbb{Z}$ 의 원소를 정수(integer)라고 한다.

!!! tldr ""

    정수의 표기 : $[n, 0], [0, 0], [0, n] \in \mathbb{Z}$ 를 

    $$ [n, 0] := n, \qquad [0, 0] = 0, \qquad [0, n] = -n $$

    으로 표기한다.

!!! tldr ""

    정수의 순서관계 : 집합 $\mathbb{Z}$ 에 부여된 관계

    $$ [m, n] \geq [k, l] \iff m+l \geq n+k $$

    이다. 

- 이 순서관계 또한

    $$ [m, n] \geq [k, l] \iff m-n \geq k-l $$

    로 이해하면 편하다. 

- 만일 $(m,n) \sim (m',n')$ 이고 $(k,l) \sim (k', l')$ 이면(*이 동치관계를 $m-n=m'-n'$ 과 $k-l=k'-l'$ 로 이해하면 편하다.*)

    $$ m+n' = n + m', k+l'=l+k' $$

    인데 정리 

    "$\forall n,m,k \in \N, n = m + k \to n \geq m$ 이고, 역으로 두 자연수 $m,n \in \N$ 에 대하여 $n \geq m$ 이면 $n=m+k$ 를 만족하는 자연수 $k \in \N$ 가 유일하게 존재한다."

    에 의하여 

    $$ m+l \geq n+k \iff m'+l' \geq n'+k' $$

    이므로(*이해 안되는 부분*) 순서관계가 잘 정의되어 있음을 알 수 있다. 

!!! tldr ""

    정수 집합 $\mathbb{Z}$ 에 대하여 다음이 성립한다. 

    1. $\forall a,b \in \mathbb{Z}, a \geq b \lor b \geq a$

    2. $A \neq \varnothing$ 인 $A \subset \mathbb{Z}$ 가 위로 유계이면 $A$ 가 최대원소를 가지고, 아래로 유계이면 최소원소를 가진다.

- 증명 

    $m \geq n$ 이면 

    $$ [m, 0] \geq [n, 0] \geq [0, 0] \geq [0, n] \geq [0, m] $$

    이므로 1) 이 증명된다(*이해 안되는 부분*).

    2) 를 증명하기 위해 $A$ 가 위로 유계라고 하고, $A$ 의 모든 정수를 $[n, 0]$ 의 형태로 두어서 집합 $B$ 를 

    $$ B = \{k \in \N : [k, 0] \in A\} $$

    로 정의하자. $B \neq \varnothing$ 이면 $B$ 가 위로 유계이므로 정리 "위로 유계이며 비어있지 않은 자연수들의 집합 $A \subset \N$ 는 최대 원소를 가진다." 에 의하여 최대 원소 $n$ 을 가지는데, 그러면 $[n,0]$ 이 $A$ 의 최대원소가 된다.

    만약 $B = \varnothing$ 이면 $A$ 의 모든 원소들이 $[0, k]$ 의 꼴로 표현되므로 집합 $C$ 를 

    $$ C = \{k \in \N: [0, k] \in A\} $$

    로 정의하자. 이 $C$ 의 최소원소를 $m$ 이라 두면 $[0, m]$ 이 $A$ 의 최대 원소가 된다.

    집합 $A$ 가 아래로 유계일 때도 비슷하게 증명할 수 있다. ■ 

!!! tldr ""

    정수의 더하기 : $m,n,k,l \in \mathbb{Z}$ 에 대하여 

    $$ [m,n]+[k,l] = [m+k,n+l] $$

    이다. 

- 이 연산은 잘 정의되어 있고 commutative 와 associative 가 성립한다.

- 또한 $[0, 0] \in \mathbb{Z}$ 이 항등원의 역할을 하고, $[n, m]$ 의 역원은 $[m, n]$ 이 된다. 

!!! tldr ""

    정수의 곱하기 : 집합 $\N \times \N$ 의 원소 $[m, n]$ 과 $[k, l]$ 에 대하여 

    $$ [m, n] \cdot [k, l] = [mk + nl, ml + nk] $$

    이다. 

- 정수의 곱하기는 잘 정의되어 있고, commutative 와 associative 와 distributive 가 성립한다.

- $[1, 0]$ 은 곱하기의 항등원이다. 정수 곱하기의 역원은 존재하지 않는다.

!!! tldr ""

    함수 $f: \N \to \mathbb{Z}$ 를 

    $$ f: n \mapsto [n, 0] $$

    로 정의하면 $f$ 는 단사함수이고, 각 자연수 $m, n \in \N$ 에 대하여 

    $$ f(m + n) = f(n) + f(m) $$

    $$ f(mn) = f(m)f(n) $$

    $$ m \geq n \iff f(m) \geq f(n) $$

    이 성립하므로 더하기, 곱하기, 순서관계에 관한 한

    $$ \N \subset \mathbb{Z} $$

    이다.

!!! tldr ""

    체(field) : 집합 $F$ 에 두 이항연산 

    $$ (x, y) \mapsto x+y, \qquad (x, y) \mapsto x \cdot y $$

    가 주어져서 다음 성질을 만족하면 이를 체라고 한다.

    1. $\forall a, b, c \in F, a+(b+c) = (a+b)+c$ (더하기의 associative)

    2. 다음 성질을 만족하는 원소 $e \in F$ 가 존재한다. (더하기의 항등원)

        $$ \forall a \in F, a + e = e + a = a $$
    
    3. 각 $a \in F$ 에 대하여 다음 성질을 만족하는 원소 $x \in F$ 가 존재한다. (더하기의 역원)

        $$ a + x = x+ a = 0 $$
    
    4. $\forall a, b \in F, a+b = b+a$ (더하기의 commutative)
    
    5. $\forall a, b, c \in F, a(bc) = (ab)c$ (곱하기의 associative)

    6. 다음 성질을 만족하는 $0$ 이 아닌 원소 $1 \in F$ 이 존재한다. (곱하기의 항등원)

        $$ \forall a \in F, a \cdot 1 = 1 \cdot a = a $$

    7. $a \in F \text{ \textbackslash }\{0\}$ 에 대하여 성질 $ax = xa = 1$ 을 만족하는 원소 $x \in F$ 가 존재한다. (곱하기의 역원)

    8. $\forall a, b \in F, ab = ba$ (곱하기의 commutative)

    9. $\forall a,b,c \in F, a(b+c) = ab + ac$ (더하기와 곱하기의 distributive)
    
- $x \cdot y$ 를 그냥 $xy$ 로 쓸 수 있다. 

- 성질 2) 의 더하기의 항등원 $e$ 는 유일하다. 

    - 증명 

        또 다른 항등원 $e'$ 가 있다면 

        $$ e = e + e' = e' $$

        이다.

- 더하기의 항등원 $e$ 를 $0$ 으로 쓰기로 한다. 

- 성질 3) 의 더하기의 역원은 유일하다.

    - 증명 

        또 다른 역원 $y \in F$ 이 있다면 

        $$ x = x + 0 = x + (a + y) = (x + a) + y = 0 + y = y $$

        이다.

- $a \in F$ 에 대한 더하기의 역원을 $-a$ 라고 쓰기로 한다. 또한 $b + (-a)$ 를 $b-a$ 로 쓰기로 한다.

- $a \in F$ 에 대한 곱하기의 역원을 $a ^{-1}$ 혹은 $\dfrac{1}{a}$ 라고 쓰기로 한다. 

- 어떤 집합이 체(field) 라고 함은 더하기와 곱하기가 정의되고, 덧셈/뺄셈/곱셈/나눗셈이 자유롭다는 뜻이다.

!!! tldr ""

    순서체(ordered field) : 체 $F$ 의 부분집합 $S$ 에 대하여 집합 

    $$ -S = \{-a: a \in S\} $$

    를 정의하였을 때, 체 $F$ 의 $P \neq \varnothing$ 인 $P \subset F$ 이 

    1. $a, b \in P \Rightarrow a+b,ab \in P$

    2. $F = P \cup \{0\} \cup (-P)$

    3. $P \cap \{0\} \cap -P = \varnothing$

    을 만족하면 $F$ 를 순서체라고 한다.

- 이때 $P$ 의 원소를 양수(positive number) 라 한다. 
