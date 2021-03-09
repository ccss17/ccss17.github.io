
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

    $$ \varnothing \in \mathcal{A}, A \in \mathcal{A} \implies A ^{+} \in \mathcal{A} $$

    을 가지는 집합 $\mathcal{A}$ 에 대하여 집합

    $$ \N := \bigcap_{}^{}\mathcal{A} $$

    의 원소를 자연수라고 한다.

!!! tldr ""

    페아노 공리계 : 집합 $\N$ 은 다음 성질을 만족하고, 이 성질을 페아노 공리계라고 한다. 

    1. $0 \in \N$

    2. $n \in \N \implies n ^{+} \in \N$

    3. $\forall n \in \N, n ^{+} \neq 0$

    4. 집합 $X \subset \N$ 이 다음 두 성질 

        $$ 0 \in X, \qquad  n \in X \implies n ^{+}\in X $$

        을 만족하면 $X = \N$ 이다. 

    5. 만일 $m, n \in \N$ 에 대하여 $m ^{+} = n ^{+}$ 이면 $m=n$ 이다.

- 세번째 성질은 $n ^{+} = n \cup \{n\} \neq \varnothing$ 이므로 당연하고, 

    네번째 성질은 수학적 귀납법을 통하여 증명된다. 
    
    다섯번째 성질의 증명은 다음과 같다. 먼저 

    $$ n \in n ^{+} = m ^{+} = m \cup \{m\} $$

    이므로 $n \in m \lor n = m$ 이다. 마찬가지로 $m \in n \lor n = m$ 이다. 그러므로 $n \in m$ 과 $m \in n$ 에서 $n = m$ 을 이끌어내면 된다. 그렇다면

    $$ n \in \N, x \in n \implies x \subset n \tag{1}  $$

    을 증명하면 $n \subset m \land m \subset n$ 이 성립하여 $n = m$ 을 이끌어낼 수 있다. 

    일단 

    $$ X = \{n \in \N : x \in n \implies x \subset n\} $$

    으로 두자. 먼저 $0 \in X$ 이다. $x \in \varnothing \implies x \subset \varnothing$ 이기 때문이다.

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

    $$  (n, x) \in A \implies (n ^{+}, f(x)) \in A \tag{1.2} $$

    을 만족하는 $A \subset \N \times X$ 전체의 집합을 $\mathcal{A}$ 라 두면 이 성질을 만족하는 모든 집합이 $\mathcal{A}$ 에 속하게 되므로 $\N \times X$ 도 $\mathcal{A}$ 에 속한다. 즉, $\N \times X \in \mathcal{A}$ 이다. 따라서 $\mathcal{A}$ 는 비어있지 않다. 

    *(이러한 $A$ 는 곱집합의 부분집합인 함수 $\gamma$ 의 기반을 정의하기 위해서 생성되었다. 그러므로 이제 집합 $A$ 가 같은 입력에 대하여 다른 출력을 가지지 않는다는 것을 증명하면 함수의 조건이 충족된다.)*

    이제 $\gamma = \bigcap_{}^{}\mathcal{A}$ 라고 두자. 만일 $\gamma \subset \N \times X$ 가 함수이면 

    $$ \gamma (n) = x \implies (n, x) \in \gamma $$

    $$ \implies (n ^{+}, f(x)) \in \gamma  $$ 
    
    $$ \implies \gamma (n ^{+}) = f(x) = f( \gamma (n)) $$

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

    $$ n \in \mathcal{X} \implies n ^{+} \in \mathcal{X} $$

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

    $$ \gamma _m(0) = m, \qquad n \in \N \implies \gamma _m(n ^{+}) = [\gamma _m(n)]^{+} $$

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

    $$ \delta _m(0) = 0, \qquad n \in \N \implies \delta _m(n ^{+}) = \delta _m(n)+m $$

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

    $$ 0 + n = n \implies 0 + n ^{+} = (0 + n) ^{+} = n ^{+} $$

    이므로 1) 의 첫째 명제가 증명된다.

    둘째 명제는 $m,n$ 을 고정하고 $k$ 에 대한 귀납법을 사용한다.

!!! tldr ""

    자연수의 순서 : 두 자연수 $m, n \in \N$ 에 대하여 

    $$ m \leq n \iff m \in n \lor m = n $$

    이다. 

- 자연수의 순서의 정의에 따라 다음과 같은 성질이 생긴다. 

    1. $m \leq m$ 이다.

    2. $m \leq n \land n \leq m \implies m = n$ 이다. 

        - 증명 

            $m \neq n$ 이면 $m \in n \land n \in m$ 인데 페아노 공리계의 5번째 성질을 증명할 때 사용했던 정리 

            $$ n \in \N, x \in n \implies x \subset n $$

            에 의하여 $m \subset n, n \subset m$ 이 성립하므로 

            $$ m = n $$

            이 된다. 이는 처음의 가정과 모순이다. 그러므로 $m = n$ 이다.
    
    3. $m \leq n, n \leq k \implies m \leq k$ 이다.

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

    $$ n \not \in n \implies n ^{+} \not \in n ^{+} $$

    임을 보이면 되는데, 이것의 대우 명제인 

    $$ n ^{+} \in n ^{+} \implies n \in n $$

    을 보여도 된다. 만약 $n ^{+} \in n ^{+} = n \cup \{n\}$ 이면 $n ^{+} \in n \lor n ^{+} = n$ 이다. 이때 $n ^{+}\in n$ 이면 페아노 공리계의 5번째 성질을 증명할 때 사용했던 정리 

    $$ n \in \N, x \in n \implies x \subset n $$

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

    $$ X = \{n \in \N: m \in A \implies n \leq m\} $$

    이라고 두자. 즉, $X$ 는 집합 $A$ 의 최소 원소보다 같거나 작은 자연수로 구성된다. 만약 $k \in X \cap A$ 이면 $k$ 는 $A$ 의 최소 원소가 되므로 $X \cap A = \varnothing$ 이어야 한다. 여기서 귀납법으로 $X = \N$ 임을 보이면 $A = \varnothing$ 이 되어 모순을 얻는다. 

    그러므로 먼저 $0 \in X$ 라고 가정하자. 즉, $\forall m \in \N$ 에 대하여 $0 \leq m$ 임을 보이는 것이다. 이렇게 $\forall m \in \N$ 인 $m$ 에 대하여 보이게 되면 $A$ 가 어떤 원소로 구성되었든 간에 안정적으로 $0 \in X$ 를 보일 수 있다. 이것 또한 귀납법으로 보이게 된다. 먼저 $0 \leq 0$ 은 자명하다. 만약 $0 \leq m$ 이면 $m \in m ^{+}$ 에서 $m \leq m ^{+}$ 이므로 $0 \leq m ^{+}$ 을 얻는다. 그러므로 $0 \in X$ 이 증명되었다. 

    이제 $n \in X \implies n ^{+} \in X$ 을 보이기 위하여 $n \in X$ 라고 가정하자. 즉, 

    $$ m \in A \implies n \leq m $$

    이라고 두는 것이다. 만약 $n \in A$ 이면 $n$ 은 $A$ 의 최소원소가 되고 이는 가정에 어긋난다. 그러므로 $n \not \in A$ 이고 

    $$ m \in A \implies n < m $$

    이 성립한다. 이제 

    $$ n < m \implies n ^{+} \leq m $$

    을 보이면 $X = \N$ 이 되어 모든 증명이 끝난다. 이것에도 귀납법을 사용하는데, $n$ 을 고정하고 $m$ 에 대한 귀납법을 사용하기 위하여 

    $$ Y = \{m \in \N : n < m \implies n ^{+} \leq m\} $$

    라고 두자. 먼저 $n < 0$ 이면 $n \in \varnothing$ 인데 이런 원소 $n$ 이 없으므로 $0 \in Y$ 임은 자명하다.(**이해 안되는 부분**) 

    이제 $m \in Y$ 라고 가정하고, $m ^{+} \in Y$ 임을 보이자. $n < m ^{+}$ 이면, 
    
    $$n \in m ^{+} = m \cup \{m\} \implies n \in m \lor n = m$$
    
    이다. 먼저 $n \in m$ 이면 $n < m$ 이므로 귀납법의 가정 $m \in Y$ 에 의하여 

    $$ n ^{+} \leq m < m ^{+} $$

    이고, $n = m$ 이면 $n ^{+} = m ^{+}$ 이므로 항상 

    $$ n ^{+} \leq m ^{+} $$

    이다. 그러므로 

    $$ n < m ^{+} \implies n ^{+}\leq m ^{+} $$
    
    가 성립하고 $m ^{+} \in Y$ 임에 따라

    $$ Y = \N $$

    이고 이로써 모든 증명이 끝났다. ■ 

!!! tldr ""

    $$\forall m,n \in \N, m \leq n \lor n \leq m$$

- 증명 

    $\forall  m,n \in \N$ 에 대하여 $\{m,n\} \subset \N$ 은 최소원소를 갖는데, 

    $$ (\min \{m,n\} = m \implies m \leq n) \lor (\min \{m,n\} = n \implies n \leq m) $$

    이다.

!!! tldr ""

    $$ n \in \N \implies n = 0 \lor (\exists m \in \N, n = m ^{+}) $$

- 증명 (이 증명의 풀이는 책에 나와있는게 아니라 문제로 되어있어서 내가 만든 것. 그래서 오류가 있을 수 있음)

    $n = 0$ 일 경우 $0 = 0$ 이다.

    $n = x(x \neq 0)$ 일 경우 성립한다고 가정하고 $n = x ^{+}$ 일때도 성립함을 보이자. $n = x$ 이면 
    
    $$ \exists m \in \N, x = m ^{+} $$

    이다. 그러면 

    $$ \iff x ^{+} = [m ^{+}] ^{+} $$

    인데 페아노 공리계 2) $n \in \N \implies n ^{+} \in \N$ 은 어떤 자연수 $n$ 에 $^{+}$ 를 취하면 그것도 자연수가 됨을 보증해준다. 그러므로 

    $$ [m ^{+}] ^{+} \in \N $$

    이다. 이로써 모든 증명이 끝났다. ■ 

!!! tldr ""

    위로 유계이며 비어있지 않은 자연수들의 집합 $A \subset \N$ 는 최대 원소를 가진다. 

- 증명 

    집합 $A$ 의 상계 전체의 집합을 $B$ 라 두면, 가정에 의하여 $B \neq \varnothing$ 이고 정리 "비어있지 않은 자연수들의 집합은 최소 원소를 가진다." 에 의하여 $B$ 는 최소 원소 $k \in \N$ 를 가진다. $\forall n \in A, n \leq k$ 이므로 이므로 $k \in A$ 임을 보이면 $k$ 가 $A$ 의 최대원소임이 증명된다.

    $k \not \in A$ 라고 가정하자. 그러면 $n \in A$ 을 하나 잡았을 때 $k > n \geq 0$ 이고 따라서 정리 "$n \in \N \implies n = 0 \lor (\exists m \in \N, n = m ^{+})$" 에 의하여 $k = s ^{+}$ 이다. 

    만약 $s \not \in B$ 이면 $s < t$ 인 $t \in A$ 가 존재(**이해 안되는 부분**)하고 

    $$ s ^{+} \leq t \leq k = s ^{+} \implies k = t \in A $$

    가 되어 모순이다. 그러므로 $s \in B$ 인데, $s < k$ 이므로 이는 $k$ 가 최소원소라는 것에 모순이다.

    그러므로 

    $$ k \in A $$

    이다. 

!!! tldr ""

    $\forall n,m,k \in \N, n = m + k \to n \geq m$ 이고, 
    
    역으로 두 자연수 $m,n \in \N$ 에 대하여 $n \geq m$ 이면 $n=m+k$ 를 만족하는 자연수 $k \in \N$ 가 유일하게 존재한다.

- 이 정리는 큰 수에서 작은 수를 뺄 수 있음을 말해주는데, 이는 정수를 정의하는데 중요한 역할을 한다. 

- 이 정리의 유일성은 

    $$ \forall m,k,l \in \N, m + k = m + l \implies k = l $$

    로 명확하게 표현할 수 있다.

- 첫번째 명제의 증명 

    $m+k \geq m$ 을 보이면 되는데 $k$ 에 관한 귀납법을 사용한다. $k=0$ 이면 당연히 성립하고 $m+k \geq m$ 이라고 가정하면 

    $$ m+k ^{+} = (m+k) ^{+} > m+ k \geq m $$

    이다. ■ 

- 두번째 명제의 존재성 증명 

    $$ X = \{l \in \N, m+l \geq n\} $$

    라 두면 $n \in X \implies X \neq \varnothing$ 이다. 따라서 정리 "비어있지 않은 자연수들의 집합은 최소 원소를 가진다." 에 의하여 $X$ 는 최소 원소 $k \in X$ 를 가지는데, $n = m+k$ 를 증명하면 된다. 

    먼저 $m+k>n$ 라고 가정하자. (*이는 $n = m+k$ 를 만족하는 $k$ 가 존재하지 않는다고 가정하는 것이다. 그러므로 이 가정으로부터 모순이 도출된다면 $k$ 는 존재한다는 것이 증명된다.*) $k=0$ 이면 $m>n$ 이 가정 $n \geq m$ 에 위배되므로 $k \neq 0$ 이고 정리 "$n \in \N \implies n = 0 \lor (\exists m \in \N, n = m ^{+})$" 에 의하여 $s \in \N, k = s ^{+}$ 이다. 그러면 

    $$ (m + s) ^{+} = m + s ^{+} = m + k > n $$

    에서 $m + s \geq n$ 이고, 이에따라 $s \in X$ 인데 $s < s ^{+} = k$ 이므로 $k$ 가 $X$ 의 최소원소라는 데에 모순이다. ■ 

- 두번째 명제의 유일성 증명 

    두번째 명제의 유일성 증명은

    $$ \forall m,k,l \in \N, m + k = m + l \implies k = l $$

    를 $k$ 에 관한 귀납법으로 보임으로써 완성된다. $k=0$ 이면 

    $$ m + 0 + m + l \implies 0 = l $$

    이다. 만약 $m=m+l$ 인데 $l \neq 0$ 이면 $l = s ^{+}$ 이고,

    $$ m = m+l = m + s ^{+} = (m+s) ^{+} \geq m ^{+} > m $$

    이 되어 모순이다. 그러므로 $l = 0$ 이다.

    이제 $k$ 에 대하여 성립한다고 가정하고 $k ^{+}$ 에서 성립함을 보이면 된다. 

    $$ m + k ^{+} = m + l $$

    이라고 두자. 여기에서 $l = 0$ 이면 존재성 증명에서 보인바와 같이 $k ^{+} = 0$ 이므로 $l \neq 0$ 이고 $l = t ^{+}$ 이다. 그러면 

    $$ (m+k)^{+}=m+k ^{+}=m+l=m+t ^{+}=(m+t)^{+} $$

    에서 $m+k=m+t$ 를 얻고, 가정에 의하여 $k=t$ 와 $k ^{+}=t ^{+} = l$ 을 얻는다. 이것으로써 

    $$ \forall m,k,t \in \N, m + k ^{+} = m + t ^{+} \implies k ^{+} = t ^{+} $$

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

    인 $r \in \N$ 이 유일하게 존재한다. 이때 $mn + r < mn + m \implies r < m$ 이다. ■ 

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

- $[n, 0], [0, 0], [0, n] \in \mathbb{Z}$ 를 

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

    더하기, 곱하기, 순서관계에 관한 한

    $$ \N \subset \mathbb{Z} $$

    이다.

- 증명

    함수 $f: \N \to \mathbb{Z}$ 를 

    $$ f: n \mapsto [n, 0] $$

    로 정의하면 $f$ 는 단사함수이고, 각 자연수 $m, n \in \N$ 에 대하여 

    $$ f(m + n) = f(n) + f(m) $$

    $$ f(mn) = f(m)f(n) $$

    $$ m \geq n \iff f(m) \geq f(n) $$

    이 성립하기 때문이다.

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

- 예시 

    정수 집합 $\mathbb{Z}$ 의 세 원소 $a, b, c \in \mathbb{Z}$ 에 대하여 체의 조건 1) - 6) 과 8), 9) 가 성립한다.


!!! tldr ""

    순서체(ordered field) : 체 $F$ 의 부분집합 $S$ 에 대하여 집합 

    $$ -S = \{-a: a \in S\} $$

    를 정의하였을 때, 체 $F$ 의 $P \neq \varnothing$ 인 $P \subset F$ 이 

    1. $a, b \in P \implies a+b,ab \in P$

    2. $F = P \cup \{0\} \cup (-P)$

    3. $P \cap \{0\} \cap -P = \varnothing$

    을 만족하면 $F$ 를 순서체라고 한다.

- 이때 $P$ 의 원소를 양수(positive number) 라 한다. 

- 순서체 $F$ 의 두 원소 $a, b \in F$ 에 대하여 $a -b \in P$ 이면 $a$ 가 $b$ 보다 크다고 하고 이것을 

    $$ a > b, b < a $$

    라고 쓴다. 

- 예시 

    $0$ 을 제외한 자연수 집합을 $P _{\mathbb{Z}} \subseteq \mathbb{Z}$ 라 두면 순서체 조건 1)-3) 이 성립한다. 

!!! tldr ""

    절댓값(absolute value, modulus) : 순서체 $F$ 의 원소 $a \in F$ 의 절댓값 $|a|$ 를 

    $$ |a| = \begin{cases} a &a \geq 0\\ -a & a < 0\\ \end{cases} $$

    와 같이 정의한다.

- 절댓값은 실수를 구성할 때 중요한 역할을 한다. 

!!! tldr ""

    순서체 $F$ 의 임의의 원소 $a,b,c \in F$ 에 대하여 다음이 성립한다. 

    1. $|a| \geq 0$, $|a| = 0 \iff a = 0$

    2. $|ab| = |a| |b|$

    3. $b \geq 0 \to (|a| \leq b \iff -b \leq a \leq b)$

    4. $||a|-|b|| \leq |a \pm b| \leq |a| + |b|$

    5. $|a-c| \leq |a-b| + |b-c|$

- 증명 

    1), 2), 3) 은 가능한 모든 경우를 따져보는 브루트 포싱으로 증명된다. 

    3) 에서 $b = a$ 이고 $b \geq 0$ 라는 조건이 없을 때 

    $$ -|a| \leq a \leq |a| $$

    임을 알 수 있고 $b$ 나 $-b$ 에서도 마찬가지이므로 

    $$ -|b| \leq \pm b \leq |b| $$

    이다. 그러므로 

    $$ -(|a| + |b|) \leq a \pm b \leq |a| + |b| $$

    $$ \iff |a \pm b| \leq |a| + |b| $$

    이다. 이것으로 4) 의 우측 부등식이 증명되고, 이것에서 좌측 부등식도 쉽게 유도된다. (*어떻게 유도되지?*)

    5) 는 4) 에서 바로 나온다. (*어떻게?..*)

# 유리수의 정의 

!!! tldr ""

    유리수 집합(rational number set) : 집합 $\mathbb{Z} \times (\mathbb{Z} \text{ \textbackslash }\{0\})$ 에 관계

    $$ (a, b) \sim (c, d) \iff ad = cb $$

    를 부여하면 동치관계가 되고, 이것의 분할을 유리수 집합 $\mathbb{Q}$

    $$ \mathbb{Z} \sim (\mathbb{Z} \text{ \textbackslash }\{0\})/\sim = \mathbb{Q} $$

    로 정의한다.

- 정수 집합에 체의 조건 7) 이 성립하도록 확장한 것이 유리수 집합이다. 이 과정은 빼기를 하기 위하여 자연수를 정수로 확장한 과정과 비슷하다. 

    즉, 유리수 집합 $\mathbb{Q}$ 부터는 덧셈/뺄셈/곱셈/나눗셈을 자유롭게 할 수 있는 체(field)이다.

- $\mathbb{Q}$ 의 원소 $[(a, b)]$ 를 유리수라고 한다.

    - 유리수 집합과 그 동치관계를 다룰 때에도 동치류 $[(a, b)]$ 를 편하게 $[a, b]$ 로 쓰도록 하자.

    - 또한 유리수 $[a, b]$ 를 더욱 편하게 $\dfrac{a}{b}$ 라고 쓰도록 한다.

- 유리수의 동치관계도 정수에서와 마찬가지로 

    $$ \dfrac{a}{c} = \dfrac{b}{d} $$

    로 이해하면, 즉 두 정수의 비율로 이해하면 편하다. 

- 유리수의 더하기와 곱하기를 

    $$ [a, b] + [c, d] = [ad + bc, bd], \qquad [a, b] \cdot [c, d] = [ac, bd] $$

    로 정의한다. 

- 각 $a \in \mathbb{Z}$ 에 대하여 

    $$ a ^{*} = [a, 1] $$

    라고 정의하면 유리수의 더하기의 항등원과 곱하기의 항등원은 각각 

    $$ 0 ^{*}, 1 ^{*} $$

    이다.

!!! tldr ""

    $\mathbb{Q}$ 는 순서체이다.

- 증명 

    $0$ 을 제외한 자연수 집합을 정수 $\mathbb{Z}$ 의 양수라는 의미에서 $P _{\mathbb{Z}}$ 라고 썼었다. 이 $P _{\mathbb{Z}}$ 에 의하여 $\mathbb{Z}$ 는 

    $$ \mathbb{Z} = P_{\mathbb{Z}} \cup \{0\} \cup (-P_{\mathbb{Z}}) $$

    로 분할된다. 그러면 유리수 집합 $\mathbb{Q}$ 는 

    $$ \mathbb{Q} = \mathbb{Z} \times (\mathbb{Z} \text{ \textbackslash }\{0\}) $$

    이므로 

    $$ = (P_{\mathbb{Z}} \cup \{0\} \cup (-P_{\mathbb{Z}})) \times (P_{\mathbb{Z}} \cup (-P_{\mathbb{Z}})) $$

    집합 $\mathbb{Q} = \mathbb{Z} \times (\mathbb{Z} \text{ \textbackslash }\{0\})$ 의 모든 원소가 

    $$ \{0\} \times (\mathbb{Z} \text{ \textbackslash }\{0\}), \quad  P_{\mathbb{Z}} \times P_{\mathbb{Z}}, \quad  P_{\mathbb{Z}} \times (-P_{\mathbb{Z}}), \quad  (-P_{\mathbb{Z}}) \times P_{\mathbb{Z}}, \quad  (-P_{\mathbb{Z}}) \times (-P_{\mathbb{Z}}) $$

    로 분할된다. 이때 
    
    $$\forall (a, b) \in \mathbb{Z}\times (\mathbb{Z}\text{ \textbackslash }\{0\}), (a,b) \sim (-a, -b)$$

    이므로 임의의 유리수는 세 집합 

    $$ \{0\} \times P_{\mathbb{Z}}, \qquad P_{\mathbb{Z}} \times P_{\mathbb{Z}}, \qquad (-P_{\mathbb{Z}}) \times P_{\mathbb{Z}} $$

    에 속하는 원소들을 대표원으로 하는 동치류에 의해 결정된다. 이제 

    $$ P _{\mathbb{Q}} = \{[a, b]:(a,b) \in P_{\mathbb{Z}}\times P_{\mathbb{Z}}\} $$

    라 정의하면 순서체의 조건 2), 3) 이 만족된다. 또한 유리수의 더하기와 곱하기가 

    $$ [a, b] + [c, d] = [ad + bc, bd], \qquad [a, b] \cdot [c, d] = [ac, bd] $$

    이렇게 정의되었으므로 $P _{\mathbb{Q}}$ 에 대하여 닫혀있다. 그러므로 순서체의 조건 1) 도 성립한다. 

    그러므로 $\mathbb{Q}$ 는 순서체이다. ■ 

!!! tldr ""

    순서체에 정의된 양수 집합 $P$ 에 

    $$ a \leq b \iff b-a \in P \lor a=b $$

    를 정의하면, 이는 순서관계가 된다.

- 증명

- 또한 이 정리와 $\mathbb{Q}$ 가 순서체인 것에 의하여 $\mathbb{Q}$ 의 순서관계가 주어진다.

!!! tldr ""

    더하기, 곱하기, 순서에 관한한 $\mathbb{Z} \subset \mathbb{Q}$ 이다. 

- 증명 

    함수 $a \mapsto a ^{*} = [a, 1] : \mathbb{Z} \to \mathbb{Q}$ 가 단사함수임은 자명하다. 또한 

    $$ (a+b) ^{*} = a ^{*} + b ^{*} $$

    $$ (ab)^{*} = a ^{*}b ^{*} $$

    $$ a \geq b \iff a ^{*} \geq b ^{*} $$

    가 성립하므로 더하기, 곱하기, 순서에 관한 한

    $$ \mathbb{Z} \subset \mathbb{Q} $$

    이다. 

!!! tldr ""

    임의의 순서체 $F$ 에 대하여 

    1. $\forall r, s \in \mathbb{Q}, \quad  \gamma (r+s)=\gamma (r)+\gamma (s), \quad  \gamma (rs) = \gamma (r) \gamma (s)$

    2. $\gamma (P _{\mathbb{Q}}) = \gamma (\mathbb{Q}) \cap P _{F}$

    을 만족하는 단사함수 $\gamma : \mathbb{Q} \to  F$ 가 유일하게 존재한다. 

- 이 정리는 임의의 순서체 $F$ 가 유리수체 $\mathbb{Q}$ 를 포함하며, 두 순서체의 연산과 순서를 구별할 필요가 없음을 말해준다. 

    그러므로 임의의 순서체 $F$ 를 다룰 때 

    $$ \mathbb{Q} \subset F $$

    으로 간주한다. 

- 증명 

    임의의 순서체 $F$ 는 더하기와 곱하기의 항등원 $0$ 과 $1$ 을 가진다. 정리

    "집합 $X$ 의 한 원소 $a \in X$ 와 함수 $f: X \to X$ 에 대하여 다음 성질 

    $$ \gamma (0) = a, \qquad \forall n \in \N, \gamma (n ^{+}) = f(\gamma (n)) $$

    을 만족하는 함수 $\gamma : \N \to X$ 가 유일하게 존재한다."

    에 의하여 성질 

    $$ \gamma (0) = 0 $$

    $$ \gamma (n+1) = \gamma (n ^{+}) = \gamma (n) + 1, \qquad n \in \N $$

    을 만족하는 함수 $\gamma : \N \to F$ 가 유일하게 존재한다. 이때 좌변의 $\gamma (n+1)$ 의 더하기는 $\N$ 에서 정의된 더하기이고, 우변의 $\gamma (n)+1$ 는 순서체 $F$ 의 더하기이다. 또 우변의 $0, 1$ 은 순서체 $F$ 의 더하기와 곱하기의 항등원이다.

    이제 $m,n \in \N$ 에 대한

    $$ \gamma (n+m) = \gamma (n) + \gamma (m) \tag{1} $$
    
    $$ \gamma (nm) = \gamma (n)\gamma (m) \tag{2} $$

    이 성립함을 보일 것이다. 먼저 $m = 0$ 이면 자명하게 성립한다. 수학적 귀납법을 사용하기 위하여 $m \in \N$ 에서 성립한다고 가정하면 

    $$ \gamma (n+m ^{+}) = \gamma ((n + m) ^{+}) = \gamma (n+m)+1 $$

    $$ = \gamma (n) + \gamma (m) + 1 = \gamma (n) + \gamma (m ^{+}) $$

    이므로 임의의 $m, n \in \N$ 에서 $(1)$ 이 성립함을 알 수 있다. □ 
    
    $(2)$ 도 마찬가지로 $m=0$ 이면 자명하고 귀납법을 사용하여 

    $$ \gamma (nm ^{+}) = \gamma (nm+n)= \gamma (nm)+\gamma (n) $$

    $$ = \gamma (n)\gamma (m)+\gamma (n) = \gamma (n)[\gamma (m) +1] = \gamma (n)\gamma (m ^{+}) $$

    가 되어 증명된다. □ 

    한편, 임의의 순서체에서 $0<1 \implies 1 \in P _{F}$ 이다. 그러므로 $\gamma (n) \in P _{F}$ 이면 $\gamma (n ^{+}) = \gamma (n) + 1 \in P _{F}$ 이 되어 $n \in \N \text{ \textbackslash }\{0\}$ 에 대하여

    $$ \gamma (n) \in P _{F} \tag{3} $$

    이다. □ 

    마지막으로 $\gamma : \N \to F$ 가 단사함수임을 보일 것이다. 먼저 $n> m, \gamma (n) = \gamma (m)$ 이라고 가정하여 단사함수의 조건에 어긋나게 하자. 그러면 $n = m + k$ 인 $k \in \N \text{ \textbackslash }\{0\}$ 가 존재하여 

    $$ \gamma (k) = [\gamma (m) + \gamma (k)] - \gamma (m) $$

    $$ = \gamma (m+k) - \gamma (m) = \gamma (n) - \gamma (m) = 0 \not \in P _{F} $$

    인데, 이는 $(3)$ 에 모순이므로 $\gamma : \N \to F$ 는 단사함수이다. □ 

    이제 $\N \subset \mathbb{Q} \subset \mathbb{Q}$ 를 염두하며 $\gamma : \N \to F$ 의 정의역을 $\mathbb{Q}$ 로 확장할 것이다. 먼저 $\mathbb{Z}$ 로 확장하여 함수 $\gamma : \mathbb{Z} \to F$ 를 $n \in \N$ 에 대하여

    $$ \gamma (n) = \gamma (n), \qquad \gamma (-n) = - \gamma (n) $$

    라 정의하자. 두 함수 $\gamma : \N \to F, \gamma : \mathbb{Z} \to F$ 는 함숫값이 $\N$ 위에서 똑같으므로 같은 기호를 사용해도 된다. 비슷하게 $\gamma : \mathbb{Q} \to F$ 를 

    $$ \gamma \bigg (\dfrac{a}{b}\bigg ) = \dfrac{\gamma (a)}{\gamma (b)}, \qquad (a,b) \in \mathbb{Z}\times (\mathbb{Z}\text{ \textbackslash }\{0\}) $$

    로 정의하자. 그러면 이렇게 정의된 함수 $\gamma : \mathbb{Q} \to F$ 는 잘 정의되어 있고, $(1),(2),(3)$ 을 만족하는 단사함수가 되지만 여백이 부족해서 증명을 마저 쓸 수가 없다. ■ 

!!! tldr ""

    순서체 $F$ 에 대하여 다음이 동치이다. 

    1. $x>0 \to \exists n \in \N \text{ \textbackslash }\{0\}, x > \dfrac{1}{n}$

    2. $y>0 \to \exists n \in \N \text{ \textbackslash }\{0\}, y < n$

    3. 집합 $\N \subset F$ 은 위로 유계가 아니다. 

    4. 임의의 $x,y>0$ 에 대하여 $y<nx$ 를 만족하는 자연수 $n \in \N \text{ \textbackslash }\{0\}$ 이 존재한다. 

- 순서체 $F$ 가 이 동치 조건을 만족하면 아르키메데스의 성질을 만족한다고 한다. 

- 증명 

!!! tldr ""

    아르키메데스의 성질(Archimedean property) : 전순서를 가지는 군 $G$ 의 양의 원소 $x, y$ 에 대하여 

    $$ y < n \cdot x $$

    를 만족하는 $n \in \N$ 이 존재한다.

- 즉, 아무리 작은 원소라도 그것을 유한번 더하여 어떤 원소보다 커질 수 있다면 아르키메데스 성질을 가지고 있다는 것이다. 

- 전순서를 가지는 군 $G$ 의 양의 원소 $x, y$ 에 대하여 

    $$ \forall n \in \N, nx < y $$

    이면 $x$ 는 $y$ 의 무한소(infinitesimal) 이며, $y$ 는 $x$ 의 무한(infinite)이다. 즉, 무한소와 무한가 원소로써 존재하지 않는 군 $G$ 는 아르키메데스의 성질을 가진다는 것이다. 

- 예시 

    $\mathbb{Z}, \mathbb{Q}, \R$ 는 아르키메데스 성질을 만족한다.

    초실수체 $^{*}\R$ 은 아르키메데스의 체가 아니다.

!!! tldr ""

    유리수체는 아르키메데스의 성질을 만족한다. 

- 증명 

    $$ m,n \in P _{\mathbb{Z}} \to \dfrac{n}{m}<2n $$

    - 내 생각에는..
    
        이 증명은 4 번째 명제가 유리수체에서 성립함을 보이려 한다. $0$ 이 아닌 자연수 $m, n$ 을 기반으로 유리수체의 원소 $y := \dfrac{n}{m}$ 를 정의하고, 유리수체의 원소 $x := \dfrac{n}{1}$ 를 정의하며, $n := 2$ 로 두었다.

        이로써 4 번째 명제가 "$n, \dfrac{n}{m} > 0$ 에 대하여 $\dfrac{n}{m} < 2n$ 을 만족하는 자연수 $2 \in \N \text{ \textbackslash }\{0\}$ 가 존재한다." 로 특수화되었다.

# 데데킨트 절단을 기반으로 정의하는 실수

!!! tldr ""

    데데킨트 절단(Dedekind Cut) : 유리수들의 집합 $\alpha \subset \mathbb{Q}$ 가 

    1. $\alpha \neq \varnothing , \alpha \neq \mathbb{Q}$

    2. $p \in \alpha , q \in \mathbb{Q}, q < p \to q \in \alpha$ (아래로 무계)

    3. $p \in \alpha \to (\exists r \in \alpha , p < r)$ (최댓값이 존재하지 않음)

    를 만족하면 데데킨트 절단이라고 한다.

- 혹은 더욱 편하게 그냥 절단이라고도 한다. 

- $\forall r \in \mathbb{Q}$ 에 대하여 

    $$ r ^{*} = \{p \in \mathbb{Q} : p < r\} $$

    은 절단이다. 

- 예시 

    집합 

    $$ \alpha = \{p \in \mathbb{Q} : p \leq 0\} \cup \{p \in \mathbb{Q} : 0 < p, p ^{2} < 2\} $$

    이 절단임을 보이자.

    $0 \in \alpha , 2 \not \in \alpha$ 이므로 절단의 조건 1) 을 만족한다. 

    $q < p \in \alpha$ 일 때 $q \leq 0 \to q \in \alpha$ 이고, $0 < q < p \land p ^{2} < 2 \to q ^{2} < 2$ 이므로 $q \in \alpha$ 이다. 이로써 절단의 조건 2) 를 만족한다. 

    $p \in \alpha$ 에 대하여 $p \leq 0 \to p < 1 \in \alpha$ 이다. 한편 $0 < p, p ^{2} < 2$ 이면 정리 "유리수체는 아르키메데스의 성질을 만족한다." 를 적용하여 
    
    $$\dfrac{1}{n}(2p+1) < 2 - p ^{2}$$ 
    
    인 $n \in \N$ 을 잡을 수 있다. 그러면 

    $$ \iff p ^{2} + \dfrac{2}{n}p + \dfrac{1}{n} < 2 $$

    에서 $\dfrac{1}{n} \leq \dfrac{1}{n ^{2}}$ 이므로

    $$ \iff  \bigg (p + \dfrac{1}{n}\bigg ) ^{2} \leq p ^{2} + \dfrac{2}{n}p + \dfrac{1}{n} < 2 $$

    이다. 그러므로 
    
    $$ p + \dfrac{1}{n} \in \alpha$$ 
    
    이다. 이로써 절단의 조건 3) 도 성립한다. 

    그러므로 $\alpha$ 는 절단이다. ■ 

    한편 이 절단 $\alpha$ 는 무리수 $\sqrt[]{2}$ 를 유리수로부터 정의하기 위하여 존재하는데, 더 명확하게 이를 보이기 위하여 
    
    $$ \forall r \in \mathbb{Q}, \alpha \neq r ^{*} = \{p \in \mathbb{Q} : p < r\}$$ 
    
    임을 보이자. 이를 위해 $\alpha  = r ^{*}$ 인 유리수 $r \in \mathbb{Q}$ 이 있다고 가정한다. 만약 $r ^{2} < 2$ 이면 위에서 한 것처럼 

    $$ \bigg (r + \dfrac{1}{n}\bigg )^{2} < 2 $$

    인 자연수 $n \in \N$ 이 존재한다. 그러면 $r + \dfrac{1}{n} \in \alpha \land r + \dfrac{1}{n} \not \in r ^{*}$ 이 되어 모순이다. 

    반대로 $r ^{2} > 2$ 라고 가정하자. 그러면 비슷하게 

    $$ \bigg (r - \dfrac{1}{m}\bigg )^{2} > 2 $$

    인 자연수 $m \in \N$ 이 존재한다. 그러면 $r - \dfrac{1}{m} \not\in \alpha \land r - \dfrac{1}{m} \in r ^{*}$ 가 되어 모순이다. 그러므로 

    $$ \therefore r ^{2} = 2 $$

    인데 이와같은 $r \in \mathbb{Q}$ 는 존재하지 않는다. 왜냐하면 무리수이기 때문이다. ■ 

!!! tldr ""

    절단 $\alpha$ 에 대하여 $\alpha ^{c} = \mathbb{Q} \text{ \textbackslash }\alpha$ 라 두면 

    $$ p \in \alpha , q \in \alpha ^{c} \implies p < q, \qquad r \in \alpha ^{c}, r < s \implies s \in \alpha ^{c} $$

    가 성립한다.

- 그러므로 두 집합 $\alpha , \alpha ^{c}$ 를 수직선 위의 점들로 보면, 다음과 같이 각각이 수직선을 왼쪽과 오른쪽으로 분할하는 것으로 표현된다. 단, 왼쪽 점들 $\alpha$ 는 절단의 조건 3) 에 의하여 최댓값을 가지지 않는다. 

    ![](https://upload.wikimedia.org/wikipedia/commons/7/72/Dedekind_cut_sqrt_2.svg)

!!! tldr ""

    실수 집합(real number set) : 데데킨트 절단 전체의 집합 $\R$ 이다. 

- 유리수 $\mathbb{Q}$ 에 의하여 정의된 모든 절단들은 그 절단으로 자동으로 생성되는 오른쪽 절단과 함께 유리수나 무리수를 그 사이에 둘 수 있게 된다. 가령 위에서 살펴본 절단이 무리수 $\sqrt[]{2}$ 를 표현한 것처럼 말이다.

    이로써 모든 절단을 곧 모든 유리수와 모든 무리수로 대응시키는 전단사 함수를 만들 수 있다(*내 생각이라서 증명 필요*). 그러므로 실수(유리수와 무리수)를 데데킨트 절단으로 구성할 수 있다는 것이다. 

- 양의 실수를 $0 ^{*} = \{p \in \mathbb{Q} : p < 0\}$ 에 대하여

    $$ P _{\R} = \{\alpha \in \R : \alpha > 0 ^{*}\} $$

    라고 둔다.

!!! tldr ""

    실수의 순서관계 : 두 절단 $\alpha , \beta$ 에 대하여 

    $$ \alpha \leq \beta \iff \alpha \subset \beta $$

    로 정의한다.

- 물론 $\alpha \leq \beta \land \alpha \neq \beta$ 를 

    $$ \alpha < \beta $$

    로 표기한다. 

- $\forall \alpha , \beta \in \R$ 에 대하여 다음 중 한 명제만 성립한다. 

    $$ \alpha > \beta , \qquad \alpha = \beta , \qquad \alpha < \beta $$

    - 증명 

        만약 $\beta \subset \alpha$ 이면 $p \not \in \beta$ 인 $p \in \alpha$ 가 존재한다. 이때 $q \in \beta$ 이면 $p \not\in \beta$ 로부터 $q<p$ 임을 알 수 있으므로 $q \in \alpha$ 이다. 

        즉, $\alpha \subset \beta$ 가 아니면 $\beta \subset \alpha$ 가 되므로 두 절단 $\alpha , \beta$ 가 주어지면 $\alpha \leq \beta  \lor \alpha \geq \beta$ 이다. ■ 

    - 이 정리는 양의 실수 $P _{\R} = \{\alpha \in \R : \alpha > 0 ^{*}\}$ 가 순서체의 조건 2), 3) 을 만족함을 말해준다. 

- 그냥, 어떤 절단들이 주어지면 최소상계가 더 오른쪽에 주어진 절단이 왼쪽의 절단을 전부 다 포함한다는 것을 떠올리면 된다. 이것이 아닐 경우 두 절단은 서로 같다.

!!! tldr ""

    $A \neq \varnothing$ 인 집합 $A \subset \R$ 가 위로 유계이면 $A$ 는 최소상계를 갖는다. 

- 실수 $\R$ 을 데데킨트 절단 전체의 모임으로 정의했기 때문에 $r \in \R$ 은 절단 중 하나라고 생각하면 되고, $A \subset \R$ 은 몇몇 절단의 모임이라고 생각하면 편하다. 

- 증명 

    (*$A$: 실수의 부분집합. 즉, 절단들의 모임. 절단은 아래로 무계인 유리수 집합.*)

    $A$ 가 위로 유계일 때, 즉 상계를 가질 때 $\alpha  = \bigcup_{}^{}\{\beta \in A\}$ 가 $A$ 의 최소상계임을 보이려 한다. 

    (*$\alpha$: 실수의 부분집합의 합집합. 즉, 하나의 절단.*)

    먼저 $\alpha \subset \mathbb{Q}$ 가 절단임을 보이자. $\beta \in A$ 를 하나 잡으면 $\alpha \supset \beta \neq \varnothing$ 이고, $A$ 의 상계 $\gamma \in \R$ 를 하나 잡으면 $\alpha \subset \gamma \subsetneq \mathbb{Q}$ 이다. (*왜냐하면 절단이란 최댓값을 갖지 않고 아래로 무계인 유리수 집합이므로 $\bigcup_{}^{}\{\beta \in A\}$ 는 $A$ 에 속한 실수 중 가장 큰 실수, 즉 가장 우측에 수직선을 분할한 절단으로 여겨진다. 이는 모든 실수가 곧 절단이고, 그 절단들에 합집합 연산을 하면 수직선을 가장 오른쪽에 분할한 절단이 다른 모든 절단을 집어삼키기(?) 때문이다.*)

    만약 $p \in \alpha$ 이면 $p  \in \beta$ 인 $\beta \in A$ 가 존재한다. (*즉, $\alpha$ 라는 절단은 곧 유리수 집합이므로 $\alpha$ 에 속한 유리수가 곧 $\beta$ 에도 속하는 절단 $\beta$ 가 $A$ 에 존재한다는 것.*) 
    
    이때 $q < p$ 이면 $q \in \beta \subset \alpha$ 이므로 절단의 조건 2) 가 $\alpha$ 에 성립함이 증명된다.

    또한 $p < q$ 인 $q \in \beta$ 를 잡으면 $q \in \alpha$ 이므로 절단의 조건 3) 이 $\alpha$ 에 성립하고, 그러므로 
    
    $$\alpha \in \R$$
    
    이다.

    이제 $\alpha$ 가 $A$ 의 최소상계임을 보이자. 먼저 $\alpha$ 가 $A$ 의 상계임은 자명하다. (*상계의 정의에 따라 모든 $A$ 의 원소 $a$ 가 $a \leq \alpha$ 를 만족하기 때문.*) 이제 $\alpha$ 가 상계이지만 최소상계가 아니라고 가정하고 $\delta$ 를 최소상계라고 두자. 즉, 
    
    $$\delta < \alpha$$
    
    와 같이 두자. 그러면 $\delta \subsetneq \alpha$ 이므로 유리수 $r \in \alpha \text{ \textbackslash }\delta$ 가 존재한다. 이때 $r \in \alpha$ 로부터 $r \in \beta$ 인 $\beta \in A$ 가 존재한다. 그렇다면 $r \in \beta \land r \not\in \delta \implies \beta \not \leq \delta$ 이고 정리 

    "$\forall \alpha , \beta \in \R$ 에 대하여 다음 중 한 명제만 성립한다. $\alpha > \beta ,  \alpha = \beta ,  \alpha < \beta$"

    에 의하여 $\delta < \beta$ 이다. 그런데 $\beta \in A$ 이므로 $\delta$ 는 자명하게 $A$ 의 최소상계가 아니다. 이는 가정 "$\delta$ 가 최소상계이다" 에 모순이므로 $\delta$ 가 $A$ 의 최소상계라면 
    
    $$\delta \geq \alpha$$
    
    이것은 명백하게 $\alpha$ 가 상한임을 말해준다. ■ 

!!! tldr ""

    실수의 더하기 : $\alpha , \beta \in \R$ 에 대하여 

    $$ \alpha + \beta = \{s + t \in \mathbb{Q} : s \in \alpha , t \in \beta \} $$

    이다. 

- $\alpha + \beta \in \R$ 이다. 

    - 이는 두 절단을 더한 결과도 절단임을 보증한다. 이로써 실수의 더하기는 닫혀있다고 할 수 있다. 즉, 잘 정의되어있다.

    - 증명 

        $\alpha + \beta \neq \varnothing$ 은 자명하다. $u \not\in \alpha , v \not\in \beta$ 에 이면 임의의 $s \in \alpha , t \in \beta$ 에 대하여 $u+v>s+t$ 인데 이는 임의의 $r \in \alpha + \beta$ 에 대하여 $u+v > r$ 라는 말이다. 그러므로 $u + v \not\in \alpha + \beta$ 이고, $\alpha + \beta \neq \mathbb{Q}$ 이다. 이로써 절단의 조건 1) 이 증명되었다.

        이제 $p \in \alpha + \beta$ 라고 하자. 그러면 $s \in \alpha , t \in \beta$ 에 대하여 $p = s + t$ 이다. 

        $q < p$ 이면 

        $$ q < p = s + t \iff  q - t < s, s \in \alpha $$

        에서 $q - t \in \alpha$ 이고 $t \in \beta$ 이므로 
        
        $$q = (q - t)+t \in \alpha + \beta$$
        
        가 성립한다. 그러므로 절단의 조건 2) 가 증명되었다.

        이때 $s < r$ 인 $r \in \alpha$ 를 잡으면 $p < r + t$ 이고 $r+t \in \alpha + \beta$ 이므로 절단의 조건 3) 이 증명되었다. ■ 
    
- 실수의 더하기 연산은 체의 조건 1) 결합법칙과 체의 조건 4) 교환법칙을 만족한다.

    - 증명

- $0 ^{*} = \{p \in \mathbb{Q} : p<0\} \in \R$ 은 더하기의 항등원이다.

    - 증명 

        $\forall \alpha \in \R, \alpha + 0 ^{*} = \alpha$ 임을 보이자. 

        먼저 $r \in \alpha , s \in 0 ^{*}$ 에 대하여 $r + s < r$ 이므로(*$s$ 는 음수인 유리수임이 자명하기 때문*)  $r+s \in \alpha$ 이고(*절단의 조건 2) 에 의하여*), (*이는 절단 $\alpha + 0 ^{*}$ 의 원소가 $\alpha$ 에 속한다는 것이므로*) 
        
        $$ \alpha + 0 ^{*} \subset \alpha \tag{1} $$
        
        이다. $p \in \alpha$ 이면 (*절단의 조건 3) 에 의하여*) $p < r$ 인 $r \in \alpha$ 가 존재한다. 그러면 $p - r \in  0 ^{*}$ 이므로 (*$r$ 은 $\alpha$ 의 원소, $p-r$ 은 $0 ^{*}$ 의 원소이므로*)

        $$ p = r + (p-r) \in \alpha + 0 ^{*} $$

        이다. 그러므로 
        
        $$ \alpha \subset \alpha + 0 ^{*} \tag{2} $$

        이다. 그러면 최종적으로 $(1), (2)$ 에 의하여 

        $$ \therefore \alpha + 0 ^{*} = \alpha $$

        이다.

- 실수의 더하기의 역원이 존재한다. 

    - 실수 $\alpha$ 의 더하기의 역원을 $-\alpha$ 라고 한다.

    - 증명 

        각 $\alpha \in \R$ 에 대하여 

        $$ \beta = \{p \in \mathbb{Q} : \exists r \in \mathbb{Q}, r > p \land -r \not\in \alpha \} $$

        라 두고 $\beta \in \R$ 과 $\alpha + \beta = 0 ^{*}$ 임을 보일 것이다. 
        
        이때 조건 $-r \not\in \alpha$ 은 $-r$ 이 절단 $\alpha$ 의 오른쪽에 존재한다는 것이다. 그렇다면 절단 $\alpha$ 오른쪽을 뜻하는 $\mathbb{Q}\text{ \textbackslash }\alpha$ 에 대하여 유리수 $s \in \mathbb{Q}\text{ \textbackslash }\alpha$ 를 택하면 이 $s$ 는 $-r$ 과 같다고 생각할 수 있으므로 $-s > p$ 인 $p \in \mathbb{Q}$ 를 택하면 $p \in \beta$ 이다. (*이로써 절단의 조건 1) 의 첫째 명제 $\beta \neq \varnothing$ 가 증명되었다.*)

        또한 $q \in \alpha$ 에 대하여 $-q$ 보다 큰 유리수 $r$ 을 생각할 수 있다. 그러면 

        $$ r > -q \implies -r < q \implies -r \in \alpha $$

        가 되는데, 이러한 유리수 $r$ 은 $\beta$ 의 조건 $-r \not\in \alpha$ 를 만족하지 않으므로 

        $$ -q \not\in \beta $$

        이다. (*이로써 절단의 조건 1) 의 둘째 명제 $\beta \neq \mathbb{Q}$ 가 증명되었다.*)
        
        이제 $p \in \beta$ 라 하고 $r > p, -r \not\in \alpha$ 인 $r \in \mathbb{Q}$ 를 잡자. 이때 $q < p \to r > q, -r \not\in \alpha$ 이므로 $q \in \beta$ 이다. (*이로써 절단의 조건 2) 아래로 무계가 증명되었다.*)
        
        만약 $s = \dfrac{p+r}{2}$ 라 두면

        $$ r > p \iff 2r > p + r \iff r > \dfrac{p+r}{2} = s $$

        임에 따라 $r > s, -r \not\in \alpha$ 이므로 $s \in \beta$ 이고 $p<s$ 이다. (*이로써 절단의 조건 3) 최댓값이 없음이 증명되었다.*) 그러므로 $\beta$ 가 절단이라는 것, 즉 

        $$ \beta \in \R $$

        이 증명되었다. □ 

        이제 $\alpha + \beta = 0 ^{*}$ 을 보일텐데, $q \in \alpha , p \in \beta$ 이면 $r > p, -r \not\in \alpha$ 인 $r \in \mathbb{Q}$ 이 다음과 같이 존재한다.

        ![image](https://user-images.githubusercontent.com/16812446/110421597-2a439080-80e1-11eb-9e50-53f0d424795d.png)

        ![image](https://user-images.githubusercontent.com/16812446/110421731-6aa30e80-80e1-11eb-8c98-a05c5b3a0232.png)

        그러면 $q \in \alpha , -r \not\in \alpha \implies q < -r$ 이다. 그러므로 

        $$ -(q + p) = (r - p) + (-r - q) > 0 $$

        이고, (*왜냐하면 $0 < -r -q, r - p > 0$ 이기 때문*) 
        
        $$ \iff  q + p < 0 $$

        이므로 $\alpha + \beta \subset 0 ^{*}$ 이다. □ 
        
        이제 $0 ^{*} \subset \alpha + \beta$ 를 보이면 모든 증명이 끝난다. 이를 위하여 $s \in 0 ^{*}$ 에 대한 $t = \dfrac{-s}{2} > 0$ 인 $t \in \mathbb{Q}$ 에 대하여 

        $$ A = \{n \in \mathbb{Z} : nt \in \alpha \} $$

        라 두자. 이때 $A$ 가 위로 유계가 아니라고 가정하자. (*하지만 집합 $A$ 의 정수 $n$ 는 절단 $\alpha$ 에 $nt$ 가 속할 때 정의되므로 $n$ 에 상계가 있을 것으로 보인다.*) 그러면 정리 "유리수체는 아르키메데스의 성질을 만족한다." 에 의하여 $\forall q \in \mathbb{Q}, q < mt$ 인 $m \in \N$ 이 존재한다. 그런데 $A$ 가 위로 무계라고 가정하였으므로 $m$ 은 $A$ 의 상계가 아니고, $m < n$ 인 $n \in A$ 이 존재한다. 결국 $q < nt$ 이고, $nt \in \alpha$ 이므로 
        
        $$\forall q \in \mathbb{Q}, q \in \alpha \implies \alpha = \mathbb{Q}$$

        가 되어 모순이다. 그러므로 $A$ 는 위로 유계이고, 정리 "비어있지 않은 자연수들의 집합은 최소 원소를 가진다" 에 의하여 최대원소 $n_0 \in A$ 를 가진다. 즉, $n_0t \in \alpha \land (n_0+1)t \not\in \alpha$ 이다. 이제 

        $$ r = s - n_0 t = -(n_0 + 2)t $$

        라 두면, $-(n_0+1)t > r \land (n_0+1)t \not\in \alpha$ 이므로 $r \in \beta$ 임을 알 수 있다. 따라서 $s \in 0 ^{*}$ 이

        $$ s = n_0t + r \in \alpha + \beta $$

        의 관계를 가지므로 $\forall s \in 0 ^{*}, s \in \alpha + \beta$ 를 알 수 있고, 이에 따라 

        $$ 0 ^{*} \subset \alpha + \beta $$

        이며, 이로써 모든 증명이 끝났다. ■ 

!!! tldr ""

    실수의 곱하기 : 양의 실수 $\alpha , \beta \in P _{\R}$ 에 대하여 

    $$ \alpha \beta  = \{p \in \mathbb{Q} : p \leq rs \text{ 인 } r \in \alpha \cap P _{\mathbb{Q}}, s \in \beta \cap P _{\mathbb{Q}} \text{ 가 존재한다}\} $$

    로 정의하고, 일반적인 곱하기를 임의의 실수 $\forall \alpha , \beta \in \R$ 에 대하여 

    $$ \alpha \beta = \begin{cases} 0 ^{*} &\alpha = 0 ^{*} \lor \beta = 0 ^{*}\\ -(-\alpha )\beta  &\alpha \in -P _{\R}, \beta \in P _{\R}\\ -\alpha (-\beta)  &\alpha \in P _{\R}, \beta \in -P _{\R}\\ (-\alpha )(-\beta)  &\alpha \in -P _{\R}, \beta \in -P _{\R}\\ \end{cases} $$

    와 같이 정의한다. 

- $\alpha , \beta \in P _{\R}$ 에 대하여 $\alpha \beta \in \R$ 이다. 

    - 증명 

        (아래에서 $\R$ 이 순서체임을 증명하는 부분에 있다.)

- 곱하기에 대한 역원이 존재한다. 

    - 증명 

        각 $\alpha \in P _{\R}$ 에 대하여 

        $$ \gamma = 0 ^{*} \cup \{0\} \cup \{q \in P _{\mathbb{Q}} : r > q, \dfrac{1}{r} \not\in \alpha \text{ 인 } r \in P _{\mathbb{Q}} \text{ 이 존재한다}\} $$

        라 정의하면 $\gamma$ 가 절단이고 $\alpha \gamma = 1 ^{*}$ 임을 보일 수 있지만, 조금 시간이 흐른 후 보이겠다. 

        이제 $\alpha \in -P _{\R}$ 에 대하여 

        $$ \alpha \bigg (- \dfrac{1}{- \alpha }\bigg ) = - \alpha \bigg (\dfrac{1}{- \alpha }\bigg ) = (- \alpha )\bigg (\dfrac{1}{- \alpha }\bigg ) = 1 ^{*} $$

        이므로 최종적으로 $\alpha \neq 0$ 인 $\alpha \in \R$ 는 곱하기의 역원을 가진다. 

!!! tldr ""

    $\R$ 은 정리 "$A \neq \varnothing$ 인 집합 $A \subset \R$ 가 위로 유계이면 $A$ 는 최소상계를 갖는다" 를 만족시키는 순서체이다. 

- $\R$ 은 순서체의 조건 1) 의 첫째 명제를 만족시킨다.

    - 증명

        만약 $\alpha > 0 ^{*}$ 이면 (*양수인*) $p \in \alpha \text{ \textbackslash }0 ^{*}$ 을 택할 수 있다. 이는 $0 \leq p, p \in \alpha$ 이므로 (*절단의 조건 2) 에 의하여*) $0 \in \alpha$ 이다. 반대로 $0 \in \alpha$ 이면 (*절단의 조건 2) 에 의하여*) $p < 0 \implies p \in \alpha$ 인데 (*이는 절단 $\alpha$ 가 $0$ 을 포함하면서 아래로 무계인데 $0 ^{*}$ 는 $0$ 을 포함하지 않는 절단이므로*) 이는 $0 ^{*} < \alpha$ 임을 뜻한다. 그러므로 

        $$ 0 ^{*} < \alpha \iff 0 \in \alpha $$

        이다. 이 결과로 순서체의 조건 1) 의 첫째명제 $a, b \in P \implies a + b \in P$ 가 성립됨을 바로 알 수 있다. 어떤 절단 $a,b$ 가 $a > 0 ^{*} \land b > 0^{*}$ 이면 $0 \in a \land 0 \in b$ 이므로 $a > 0, b > 0$ 이기 때문이다. ■ 

- $\alpha , \beta \in P _{\R}$ 에 대하여 $\alpha \beta \in \R$ 이다. 

    - 증명 

        $0 \in \alpha , 0 \in \beta \implies 0 \in \alpha \beta \implies \alpha \beta \neq \varnothing$ 이므로 절단의 조건 1) 의 첫째 명제가 증명되었다. 

        $u \not\in \alpha , v \not\in \beta \to uv \not\in \alpha \beta \implies \alpha \beta \neq \mathbb{Q}$ 이므로 절단의 조건 1) 의 둘째 명제가 증명되었다. 실제로 $\forall s \in \alpha , t \in \beta, s < u \land t < u \implies st < uv$ 이다. 

        절단의 조건 2), 3) 은 정의에 의하여 자명하다. 그러므로 

        $$ \therefore \alpha \beta \in \R $$

        이다. ■ 

        특히, 순서체의 조건 1) 의 둘째 명제 "$a,b \in P, ab \in P$ (곱하기에 대하여 닫혀있음)" 도 증명되었다. 
    
!!! tldr ""

    $\forall r, s \in \mathbb{Q}$ 에 대하여 

    $$ r = s \iff  r ^{*} = s ^{*} $$

    $$ (r + s ) ^{*} = r ^{*} + s ^{*} $$

    $$ (rs) ^{*} = r ^{*} s ^{*} $$

    $$ r \in P _{\mathbb{Q}} \iff r ^{*} \in P _{\R} $$

    이 성립한다.

- 이 정리는 

    $$ r \mapsto r ^{*} : \mathbb{Q} \to \R $$

    이 연산과 순서를 보존하는 단사함수임을 말해준다. 


# 코시 수열을 기반으로 정의하는 실수
