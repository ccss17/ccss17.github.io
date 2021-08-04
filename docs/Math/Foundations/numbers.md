!!! info "ref"

    [집합과 수의 체계](http://www.math.snu.ac.kr/~kye/book/set-number.html)

# 자연수의 정의

!!! tldr ""

    집합 $A ^{+}$ : 집합 $A$ 에 대한 집합 $A ^{+}$ 을 다음과 같이 정의한다.

    $$ A ^{+} = A \cup \{A\} $$

- 예시 

    $0 = \varnothing$ 으로 두고,

    $$ 1 = 0 ^{+}, 2 = 1 ^{+}, 3 = 2 ^{+}, \dots $$

    으로 정의하면 

    $$ 0 = \varnothing $$

    $$ 1 = 0 ^{+} = 0 \cup \{0\} = \varnothing \cup \{0\} = \{0\} $$

    $$ 2 = 1 ^{+} = 1 \cup \{1\} = \{0\} \cup \{1\} = \{0, 1\} $$

    $$ 3 = 2 ^{+} = 2 \cup \{2\} = \{0, 1\} \cup \{2\} = \{0, 1, 2\} $$

    이다.

!!! tldr "자연수 집합(natural number set) "

    자연수 집합은 다음 성질을 만족하는 집합 $\mathcal{A}$ 에 대한 집합 $\N = \bigcap_{}^{}\mathcal{A}$ 이다.

    - $\varnothing \in \mathcal{A}$
    
    - $A \in \mathcal{A} \implies A ^{+} \in \mathcal{A}$

!!! tldr ""

    자연수(natural number) : 자연수 집합 $\N$ 의 원소이다.

!!! tldr "정리 2.1.1"

    집합 $\N$ 은 다음 성질을 만족한다.

    1. $0 \in \N$

    2. $n \in \N \implies n ^{+} \in \N$

    3. $\forall n \in \N : n ^{+} \neq 0$

    4. 집합 $X \subset \N$ 이 다음 두 성질을 만족하면 $X = \N$ 이다. 

        - $0 \in X$

        - $n \in X \implies n ^{+}\in X$

    5. $m, n \in \N: m ^{+} = n ^{+} \implies m=n$

- 이 5 가지 성질은 페아노 공리계(Peano's axioms)라 불린다.

- 증명 

    세번째 성질은 $n ^{+} = n \cup \{n\} \neq \varnothing$ 이므로 당연하고, 

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

    $$ n \in \N, x \in n \implies x \subset n $$

- 증명 

    (위에서 증명되었다.)

## 자연수의 덧셈과 곱셈

!!! tldr "정리 2.1.2"

    집합 $X$ 의 한 원소 $a \in X$ 와 함수 $f: X \to X$ 에 대하여 다음 성질을 만족하는 함수 $\gamma : \N \to X$ 가 유일하게 존재한다. 

    1. $\gamma (0) = a$

    2. $\forall n \in \N, \gamma (n ^{+}) = f(\gamma (n))$

- 이 정리는 집합 $X$ 의 원소 $\gamma (0), \gamma (1), \gamma (2), \dots$ 가 특정 점화식을 만족하도록 귀납적으로 정의할 수 있음을 말해준다. 이는 자연수의 연산을 정의하는데 중요한 역할을 한다. 

- 그러니까 쉽게 말하면 $\gamma$ 함수는 자연수 집합에 정의하고자 하는 덧셈이나 곱셈같은 연산의 추상적 대상이다. 그래서 $0$ 에 대응되는 $\gamma$ 함수의 값을 정의하고, 모든 자연수에서 $\gamma$ 가 값을 갖게 하기 위하여 귀납적으로 $n ^{+}$ 에서의 $\gamma$ 의 값을 

    $$ f(\gamma (n)) $$

    으로 정의한 것이다. 이는 $n ^{+}$ 의 $\gamma$ 함수값을 바로 이전 자연수인 $n$ 의 $\gamma (n)$ 를 기반으로 정의한다는 것이다. 그리고 물론 $\gamma (n)$ 의 값이 그대로 $\gamma (n ^{+})$ 이 되는 건 의미가 없으니까 "어떤 연산" 을 취할 것인데, 그 연산을 추상적으로 함수 $f$ 라고 표현한 것이다. 

- 유일성 증명 

    $(1),(2)$ 를 동시에 만족하는 함수 $\gamma _1, \gamma _2$ 가 있다고 가정하고 

    $$ Z = \{n \in \N: \gamma _1(n) = \gamma _2(n)\} $$

    라고 하자.

    일단 $\gamma _1 (0) = a = \gamma _2(0)$ 이므로 $0 \in Z$ 이다. 만약 $n \in Z$ 이면 

    $$ \gamma _1(n ^{+}) = f(\gamma _1(n)) = f(\gamma _2(n)) = \gamma _2(n ^{+}) $$

    이므로 $n ^{+} \in Z$ 이다. 그러므로 수학적 귀납법에 의하여 

    $$ Z = \N $$

    이고 
    
    $$ \therefore \forall n \in \N, \gamma _1(n) = \gamma _2(n) $$

    이다. 

- 존재성 증명

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

    그런데 $b \neq a$ 이므로 페아노 공리계 성질 3) $\forall n \in \N, n ^{+} \neq 0$ 에 의하여 $\gamma \setminus  \{(0,b)\} \subset \N \times X$ 도 $(1.1), (1.2)$ 을 만족한다. 이는 $\gamma = \bigcap_{}^{}\mathcal{A}$ 에 모순이다. 

    *($(1.1), (1.2)$ 을 만족하는 집합 $A$ 중에는 $(0, b) \in A$ 인 집합과 $(0, b) \not \in A$ 인 집합도 존재한다. 그러므로 $\gamma = \bigcap_{}^{} \mathcal{A}$ 에는 $(0,b)$ 가 존재하지 않다. 즉, $(0, b) \not \in \gamma$ 이다. 즉, 증명에서 이것을 $\gamma$ 에 $(0, b)$ 를 제외한 집합 $\gamma \setminus \{(0,b)\}$ 도 $(1.1), (1.2)$ 을 만족한다면 $\gamma = \bigcap_{}^{}\mathcal{A}$ 에 모순이라는 식으로 보인 것이다. 왜냐하면 어떤 원소를 $\gamma$ 에서 제외해도 $(1.1), (1.2)$ 이 성립한다면 교집합에 포함되지 않을 것이기 때문에 집합족의 교집합으로 정의한 $\gamma$ 집합의 조건에 위배되기 때문이다.)*

    그러므로 

    $$ 0 \in \mathcal{X} $$

    이다.

    이제 $n \in \mathcal{X}$ 이지만 $n ^{+} \not \in \mathcal{X}$ 라고 하면 $(n ^{+}, f(x)) \in \gamma$ 이므로 $(n ^{+}, y) \in \gamma , y \neq f(x)$ 인 $y \in X$ 가 존재한다. 그러면 마찬가지로 $\gamma \setminus \{(n ^{+}, y)\} \in \mathcal{A}$ 임을 보이면 $\gamma = \bigcap_{}^{}\mathcal{A}$ 에 모순이고, 결국 $y$ 는 존재하지 않으며 최종적으로 

    $$ n \in \mathcal{X} \implies n ^{+} \in \mathcal{X} $$

    이 증명된다. 그렇게 되면 $\gamma$ 가 함수임을 보장하는 공간 $\mathcal{X}$ 는
    
    $$ \mathcal{X} = \N $$

    이고, 결국 $\gamma$ 는 항상 함수가 되어 모든 증명이 끝난다.

    *(즉, 이제 $\gamma \setminus \{(n ^{+}, y)\}$ 가 $(1.1), (1.2)$ 을 만족함을 보이면 되는 것이다.)*

    일단 $n ^{+} \neq 0$ 이므로 $(0, a) \in \gamma \setminus \{(n ^{+}, y)\}$ 이다. 이제 

    $$ (m, z) \in \gamma \setminus \{(n ^{+}, y)\} $$

    라고 하자. 만약 $m = n$ 이면 $z = x$ 이고, 또한 $y \neq f(x)$ 이므로 $(m ^{+}, f(z)) = (n ^{+}, f(x)) \in \gamma \setminus \{(n ^{+}, y)\}$ 이다. 만약 $m \neq n$ 이면 페아노 공리계 성질 5) 에 의하여 $m ^{+} \neq n ^{+}$ 이고, 따라서 

    $$ (m ^{+}, f(z)) \in \gamma \setminus \{(n ^{+}, y)\} $$

    이다. 그러므로 $\forall (n, x) \in \gamma \setminus \{(n ^{+}, y)\}$ 에 대하여 $(1.2)$ 가 성립한다. 이것으로 모든 증명이 끝났다. ■ 

!!! tldr "자연수 덧셈"

    더하기(addition) : 각 자연수 $n, m \in \N$ 에 대하여 다음을 만족하면서 유일하게 존재하는 함수 $\gamma _m:\N \to \N$ 에 대하여 자연수의 더하기를 $m + n = \gamma _m(n)$ 라고 정의한다. 

    - $\gamma _m(0) = m$ 
    
    - $n \in \N \implies \gamma _m(n ^{+}) = [\gamma _m(n)]^{+}$

- 그러면 $m, n \in \N$ 에 대하여 

    $$ m + 0 = m, \qquad m + n ^{+} = (m + n) ^{+} $$

    이 성립한다.

    - 이 성질들은 아래의 정리 $n ^{+} = 1 + n$ 를 기반으로 한다.

!!! tldr ""

    $$ n ^{+} = 1 + n $$

- 증명 

    먼저 

    $$ 0 ^{+} = 1 = 1 + 0 $$

    이다. 왜냐하면 더하기의 정의에 따라 $1+0 = \gamma _1(0) = 1$ 이기 때문이다. 한편 이 등식이 자연수 $n$ 에 대하여 성립한다고 가정하면 다음과 같이 $n+1$ 에서도 성립한다.

    $$ (n ^{+}) ^{+} = (1 + n) ^{+} = 1 + n ^{+} $$

    그러므로 수학적 귀납법을 적용할 수 있으므로 증명이 끝났다. 

!!! tldr "자연수 곱셈"

    곱하기(multiplication) : 각 자연수 $n, m \in \N$ 에 대하여 다음을 만족하면서 유일하게 존재하는 함수 $\delta _m: \N \to \N$ 에 대하여 자연수의 곱하기를 $mn = \delta _m(n)$ 라고 정의한다. 

    - $\delta _m(0) = 0$
    
    - $n \in \N \implies \delta _m(n ^{+}) = \delta _m(n)+m$

- 그러면 $m, n \in \N$ 에 대하여 

    $$ m0 = 0, \qquad mn ^{+} = mn + m $$

    이 성립한다. 

!!! tldr "정리 2.1.3"

    $\forall m,n,k \in \N$ 에 대하여 다음이 성립한다. 

    1. $0+n=n, (m+n)+k=m+(n+k), m+n=n+m$ (더하기의 항등원, 결합법칙, 교환법칙)

    2. $0n=0, 1n = n, (mn)k=m(nk), mn=nm$ (곱하기의 항등원, 결합법칙, 교환법칙)

    3. $m(n+k)=mn+mk, (n+k)m=nm+km$ (더하기와 곱하기의 분배법칙)

- 증명 

    수학적 귀납법으로 모든 명제를 증명할 수 있다. 가령 이미 참임을 알고 있는 명제 $0 + 0 = 0$ 에서 출발하여 

    $$ 0 + n = n \implies 0 + n ^{+} = (0 + n) ^{+} = n ^{+} $$

    이므로 1) 의 첫째 명제가 증명된다.

    둘째 명제는 $m,n$ 을 고정하고 $k$ 에 대한 귀납법을 사용한다.

## 자연수의 순서관계

!!! tldr "자연수 순서관계(natural number order)"

    두 자연수 $m, n \in \N$ 에 대하여 다음과 같이 정의한다.

    $$ m \leq n \iff m \in n \lor m = n $$

    $$ m < n \iff m \leq n, m \neq n $$

- 이는 자연수 집합에 정의된 순서관계의 핵심적인 성질이다.

!!! tldr ""

    자연수의 순서의 정의에 따라 다음이 성립한다.

    1. $m \leq m$

    2. $m \leq n \land n \leq m \implies m = n$

    3. $m \leq n, n \leq k \implies m \leq k$

- 2) 의 증명 

    $m \neq n$ 이면 $m \in n \land n \in m$ 인데 페아노 공리계의 5번째 성질을 증명할 때 사용했던 정리 

    $$ n \in \N, x \in n \implies x \subset n $$

    에 의하여 $m \subset n, n \subset m$ 이 성립하므로 

    $$ m = n $$

    이 된다. 이는 처음의 가정과 모순이다. 그러므로 $m = n$ 이다.

- 3) 의 증명 

    $m \leq n, n \leq k$ 는 다음 4가지 경우를 내포한다. 

    $$ m \in n, n \in k, \qquad m \in n, n = k, \qquad m = n, n \in k, \qquad m = n, n = k $$

    처음 3가지 경우에서 $m \in k$ 가 성립하고, 마지막 경우에는 $m = k$ 가 성립하므로 

    $$ \therefore m \leq k $$

    이다. ■ 

    또한 이로써 $\leq$ 는 순서관계가 된다.
    
!!! tldr ""

    $$\forall n \in \N : n \not \in n$$

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

!!! tldr "정리 2.1.4"

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

!!! tldr "따름정리 2.1.5"

    $$\forall m,n \in \N : m \leq n \lor n \leq m$$

- 증명 

    $\forall  m,n \in \N$ 에 대하여 $\{m,n\} \subset \N$ 은 최소원소를 갖는데, 

    $$ (\min \{m,n\} = m \implies m \leq n) \lor (\min \{m,n\} = n \implies n \leq m) $$

    이다.

!!! tldr "2.7"

    $$ n \in \N \implies n = 0 \lor \exists m \in \N \text{ s.t. } n = m ^{+} $$

- 증명 (*검증 필요*)

    $n = 0$ 일 경우 $0 = 0$ 이다.

    $n = x(x \neq 0)$ 일 경우 성립한다고 가정하고 $n = x ^{+}$ 일때도 성립함을 보이자. $n = x$ 이면 
    
    $$ \exists m \in \N, x = m ^{+} $$

    이다. 그러면 

    $$ \iff x ^{+} = [m ^{+}] ^{+} $$

    인데 페아노 공리계 2) $n \in \N \implies n ^{+} \in \N$ 은 어떤 자연수 $n$ 에 $^{+}$ 를 취하면 그것도 자연수가 됨을 보증해준다. 그러므로 

    $$ [m ^{+}] ^{+} \in \N $$

    이다. 이로써 모든 증명이 끝났다. ■ 

!!! tldr "따름정리 2.1.6"

    위로 유계이며 비어있지 않은 자연수들의 집합 $A \subset \N$ 는 최대 원소를 가진다. 

- 증명 

    집합 $A$ 의 상계 전체의 집합을 $B$ 라 두면, 가정에 의하여 $B \neq \varnothing$ 이고 [정리 2.1.4](#5efd87f3f)  에 의하여 $B$ 는 최소 원소 $k \in \N$ 를 가진다. $\forall n \in A, n \leq k$ 이므로 이므로 $k \in A$ 임을 보이면 $k$ 가 $A$ 의 최대원소임이 증명된다.

    $k \not \in A$ 라고 가정하자. 그러면 $n \in A$ 을 하나 잡았을 때 $k > n \geq 0$ 이고 따라서 [2.7](#d3944f7ad) 에 의하여 $k = s ^{+}$ 이다. 

    만약 $s \not \in B$ 이면 $s < t$ 인 $t \in A$ 가 존재(**이해 안되는 부분**)하고 

    $$ s ^{+} \leq t \leq k = s ^{+} \implies k = t \in A $$

    가 되어 모순이다. 그러므로 $s \in B$ 인데, $s < k$ 이므로 이는 $k$ 가 최소원소라는 것에 모순이다.

    그러므로 

    $$ k \in A $$

    이다. 

!!! tldr "정리 2.1.7"

    $n, m, k \in \N$ 에 대하여 다음이 성립한다.

    - $n = m + k \implies n \geq m$
    
    - $n \geq m \implies \exists ! k \in \N \text{ s.t. }\ n=m+k$

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

    라 두면 $n \in X \implies X \neq \varnothing$ 이다. 따라서 [정리 2.1.4](#5efd87f3f) 에 의하여 $X$ 는 최소 원소 $k \in X$ 를 가지는데, $n = m+k$ 를 증명하면 된다. 

    먼저 $m+k>n$ 라고 가정하자. (*이는 $n = m+k$ 를 만족하는 $k$ 가 존재하지 않는다고 가정하는 것이다. 그러므로 이 가정으로부터 모순이 도출된다면 $k$ 는 존재한다는 것이 증명된다.*) $k=0$ 이면 $m>n$ 이 가정 $n \geq m$ 에 위배되므로 $k \neq 0$ 이고 [2.7](#d3944f7ad) 에 의하여 $s \in \N, k = s ^{+}$ 이다. 그러면 

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

!!! tldr "정리 2.1.8"

    $m,l \in \N$ 에 대하여 $0 < m \leq l$ 이면 다음을 만족하는 자연수 $n,r \in \N$ 이 유일하게 존재한다. 

    - $l = mn + r$
    
    - $0 \leq r < m$

- 존재성 증명 

    집합 $P = \{k \in \N:mk \leq l\}$ 는 $1 \in P$ 이므로 $P \neq \varnothing$ 이다. 또한 $\forall k \in P, k \leq mk \leq l$ 이므로 $P$ 는 위로 유계이다. 그러므로 [따름정리 2.1.6](#749829205) 에 의하여 $P$ 는 최대원소 $n$ 을 가진다. 그러면 

    $$ mn \leq l < mn ^{+} = mn + m $$

    이므로 (*이렇게 되는 것은 매우 간단한데, $l \geq mn ^{+}$ 가 성립한다면 $n$ 이 최대원소라는 가정에 모순이기 때문이다.*) [정리 2.1.7](#2d730de01) 에 의하여 

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

!!! tldr "동치관계 $\sim$ "

    $m, n, m', n' \in \N$ 에 대하여 $\N \times \N$ 위에서 정의된 다음의 관계 $\sim$ 는 동치관계이다.

    $$ (m, n) \sim (m', n') \iff m + n' = n + m' $$

- 증명

!!! tldr "정수 집합(integer set) "

    정수집합은 동치관계 $\sim$ 에 대한 몫집합 $\mathbb{Z} = \N \times \N/ \sim$ 이다.

- 이때 동치류 $[(m,n)]$ 을 간단하게 $[m,n]$ 로 표현하면 집합 $\mathbb{Z}$ 의 모든 원소를 자연수 $n = 1,2,\dots$ 에 대하여 

    $$ [n,0],[0,0],[0,n] $$

    으로 표현할 수 있다. 

    - $[n, 0]$ 를 $n$ 으로, $[0, 0]$ 을 $0$ 으로 $[0, n]$ 을 $-n$ 으로 이해하면 편하다. 왜냐하면 정수 집합의 동치관계는 결국 

        $$ (m,n) \sim (m',n') \iff m-n = m'-n' $$

        과 같기 때문이다. 

!!! tldr ""

    정수(integer) : $a, b \in \N$ 에 대한 $\mathbb{Z}$ 의 원소인 동치류 $[(a, b)]$ 이다.

- 동치류 $[(a, b)]$ 를 편하게 $[a, b]$ 로 쓰기로 한다.

!!! tldr "정수 뺄셈"

    빼기(subtraction) : $m, n \in \N : n \leq m$ 이면 $m = n + k$ 인 $k \in \N$ 가 유일하게 존재하는데 이 $k$ 를 다음과 같이 정의한다.

    $$ k = m - n $$

- 이 정의는 [정리 2.1.7](#2d730de01) 에 의존한다.

!!! tldr ""

    $n \in \N$ 에 대한 $[n, 0], [0, 0], [0, n] \in \mathbb{Z}$ 를 다음과 같이 표기한다.

    $$ [n, 0] = n $$
    
    $$ [0, 0] = 0 $$
    
    $$ [0, n] = -n $$

## 정수의 순서관계

!!! tldr "정수 순서관계(integer order)"

    정수의 순서관계는 집합 $\mathbb{Z}$ 위의 다음과 같은 관계이다.

    $$ [m, n] \geq [k, l] \iff m+l \geq n+k $$

- 이 순서관계 또한

    $$ [m, n] \geq [k, l] \iff m-n \geq k-l $$

    로 이해하면 편하다. 

- 만일 $(m,n) \sim (m',n')$ 이고 $(k,l) \sim (k', l')$ 이면(*이 동치관계를 $m-n=m'-n'$ 과 $k-l=k'-l'$ 로 이해하면 편하다.*)

    $$ m+n' = n + m', k+l'=l+k' $$

    인데 [정리 2.1.2](#3a99b431b) 에 의하여 

    $$ m+l \geq n+k \iff m'+l' \geq n'+k' $$

    이므로(*이해 안되는 부분*) 순서관계가 잘 정의되어 있음을 알 수 있다. 

!!! tldr "정리 2.2.1"

    정수 집합 $\mathbb{Z}$ 에 대하여 다음이 성립한다. 

    1. $\forall a,b \in \mathbb{Z} : a \geq b \lor b \geq a$

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

## 정수의 덧셈과 곱셈

!!! tldr "정수 덧셈"

    정수의 덧셈 $+$ 은 다음과 같이 정의된 함수 $+: \mathbb{Z} \times \mathbb{Z} \to \mathbb{Z}$ 이다.
    
    $$ [m,n]+[k,l] = [m+k,n+l] $$

- 이 연산은 잘 정의되어 있고 commutative 와 associative 가 성립한다.

- 또한 $[0, 0] \in \mathbb{Z}$ 이 항등원의 역할을 하고, $[n, m]$ 의 역원은 $[m, n]$ 이 된다. 

!!! tldr "정수 곱셈"

    정수의 곱셈 $\cdot$ 은 다음과 같이 정의된 함수 $\cdot : \mathbb{Z} \times \mathbb{Z} \to \mathbb{Z}$ 이다.

    $$ [m, n] \cdot [k, l] = [mk + nl, ml + nk] $$

- 정수의 곱하기는 잘 정의되어 있고, commutative 와 associative 와 distributive 가 성립한다.

- $[1, 0]$ 은 곱하기의 항등원이다. 정수 곱하기의 역원은 존재하지 않는다.

!!! tldr ""

    자연수의 덧셈, 곱셈, 순서관계는 정수의 덧셈, 곱셈, 순서관계에 매장된다. 즉, $\N \subset \mathbb{Z}$ 이다.

- 증명

    함수 $f: \N \to \mathbb{Z}$ 를 

    $$ f: n \mapsto [n, 0] $$

    로 정의하면 $f$ 는 단사함수이고, 각 자연수 $m, n \in \N$ 에 대하여 

    $$ f(m + n) = f(n) + f(m) $$

    $$ f(mn) = f(m)f(n) $$

    $$ m \geq n \iff f(m) \geq f(n) $$

    이 성립하기 때문이다.

# 체

!!! tldr "체(field)"

    체 $F$ 는 두 이항연산 합과 곱
    
    $$ +: F \times F \to F, (a, b) \mapsto a+b $$ 
    
    $$ \cdot: F \times F \to F, (a, b) \mapsto ab $$ 
    
    을 가지고, $x, y \in F$ 에 대한 $x+y, x \cdot y$ 가 $F$ 에 유일하게 존재하며, $\forall a,b,c \in F$ 에 대하여 다음 공리가 성립하는 집합이다.

    1. $a+b=b+a,a \cdot b = b \cdot a$ (Commutativity of addition and multiplication)

    2. $(a+b)+c=a+(b+c)$ (Associativity of addition)

    3. $(a \cdot b) \cdot c = a \cdot (b \cdot c)$ (Associativity of multiplication)

    4. $\exists 0 \in F \text{ s.t. }\ a + 0 = a$ (Additive identity)

    5. $\exists 1 \in F \text{ s.t. }\ a \cdot 1 = a$ (multiplicative identity)

    6. $\exists -a \in F \text{ s.t. }\ a + (-a) = 0$ (Additive inverses)

    7. $\exists a ^{-1} \in F \setminus \{0\} \text{ s.t. }\ a \cdot a ^{-1} = 1$ (Multiplicative inverses)

    8. $a \cdot (b+c) = a \cdot b + a \cdot c$ (Distributivity of multiplication over addition)

- $a \in F$ 에 대한 더하기의 역원을 $-a$ 라고 쓰기로 한다. 또한 $b + (-a)$ 를 $b-a$ 로 쓰기로 한다.

- $a \in F$ 에 대한 곱하기의 역원을 $a ^{-1}$ 혹은 $\dfrac{1}{a}$ 라고 쓰기로 한다. 

- 더하기의 항등원 $e$ 를 $0$ 으로 쓰기로 한다. 

- 어떤 집합이 체(field) 라고 함은 더하기와 곱하기가 정의되고, 덧셈/뺄셈/곱셈/나눗셈이 자유롭다는 뜻이다.

- 예시 

    정수 집합 $\mathbb{Z}$ 의 세 원소 $a, b, c \in \mathbb{Z}$ 에 대하여 체의 조건 1) - 6) 과 8), 9) 가 성립한다.

!!! tldr ""

    체에서 더하기의 항등원 $0$ 는 유일하다. 

- 증명 

    또 다른 항등원 $0'$ 가 있다면 $0 = 0 + 0' = 0'$ 이다. ■ 

!!! tldr ""

    체에서 더하기의 역원은 유일하다.

- 증명 

    $a \in F$ 에 대한 역원 $-a$ 이외에 또 다른 역원 $-a' \in F$ 이 있다면 다음이 성립한다.

    $$ -a = -a + 0 = -a + (a + -a') = (-a + a) + -a' = 0 + -a' = -a' \tag*{■} $$

# 순서체

!!! tldr ""

    체 $F$ 의 부분집합 $S$ 에 대하여 다음과 같이 정의한다. 
    
    $$ -S = \{-a: a \in S\} $$

!!! tldr "양수(positive number) 집합"

    체 $F$ 의 양수집합 $P$ 는 다음을 만족하는 집합이다.

    1. $P \neq \varnothing, P \subset F$

    2. $a, b \in P \implies a+b,ab \in P$

    3. $F = P \cup \{0\} \cup (-P)$

    4. $P \cap \{0\} \cap -P = \varnothing$

- 이때 $P$ 의 원소를 양수(positive number) 라 한다. 

- 체에 양수집합이 존재하지 않을 수도 있다. 이 경우 그 체는 순서체가 아니다.

- **체 $F$ 의 양수집합 $P$ 를 보통 $P _{F}$ 라고 표기한다.**

!!! tldr "순서체(ordered field)"

    순서체는 양수집합이 존재하는 체이다.

- 예시 

    $P _{\mathbb{Z}} \subseteq \mathbb{Z} = \N \setminus  \{0\}$ 으로 두면 $\mathbb{Z}$ 에는 양수집합이 존재한다. $\mathbb{Z}$ 는 곱셈의 역원을 제외한 체의 모든 조건도 만족시킨다. 그래서 $\mathbb{Z}$ 는 체도 아니고 순서체도 아니다.

## 순서체의 순서관계

!!! tldr "순서체의 순서관계"

    순서체 $F$ 의 두 원소 $a, b \in F$ 에 대하여 다음과 같이 정의한다. 
    
    $$ a \leq b \iff b - a \in P _{F} \lor a = b $$

    $$ a < b \iff b - a \in P _{F} \land a \neq b $$

- 아래에서 살펴보듯이 $\mathbb{Q}$ 가 순서체이므로 이 관계에 의하여 $\mathbb{Q}$ 의 순서관계가 주어진다.

## 절댓값

!!! tldr ""

    절댓값(absolute value, modulus) : 순서체 $F$ 의 원소 $a \in F$ 의 절댓값 $|a|$ 를 다음과 같이 정의한다.

    $$ |a| = \begin{cases} a &a \geq 0\\ -a & a < 0\\ \end{cases} $$

- 절댓값은 실수를 구성할 때 중요한 역할을 한다. 

!!! tldr "정리 2.2.2"

    순서체 $F$ 의 임의의 원소 $a,b,c \in F$ 에 대하여 다음이 성립한다. 

    1. $|a| \geq 0$, $|a| = 0 \iff a = 0$

    2. $|ab| = |a| |b|$

    3. $b \geq 0 \implies (|a| \leq b \iff -b \leq a \leq b)$

    4. $||a|-|b|| \leq |a \pm b| \leq |a| + |b|$

    5. $|a-c| \leq |a-b| + |b-c|$

- 4) 의 우측 부등식을 삼각부등식(triangle inequality), 4) 의 좌측부등식을 역삼각부등식(reverse triangle inequality)이라고 한다.

- 증명 

    1), 2), 3) 은 가능한 모든 경우를 따져보는 브루트 포싱으로 증명된다. ▲ 

    3) 에서 $b = a$ 이고 $b \geq 0$ 라는 조건이 없을 때 

    $$ -|a| \leq a \leq |a| \tag{1} $$

    임을 알 수 있고 $b$ 나 $-b$ 에서도 마찬가지이므로 

    $$ -|b| \leq \pm b \leq |b| \tag{2} $$

    이다. $(1), (2)$ 를 더하면 

    $$ -(|a| + |b|) \leq a \pm b \leq |a| + |b| \iff |a \pm b| \leq |a| + |b| $$

    이다. 이것으로 4) 의 우측 부등식이 증명된다. ▲ 

    이제 $|a + b| \leq |a| + |b|$ 를 가정할 수 있다. 따라서 

    $$ |a| + |b - a| \geq |a + b - a| = |b| \iff |b - a| \geq |b| - |a| $$

    $$ |b| + |a - b| \geq |b + a - b| = |a| \iff |a - b| \geq |a| - |b| $$

    이다. $|a - b| = |b - a|$ 이고 절댓값의 정의에 의하여

    $$ ||a| - |b|| \leq |a - b| \tag{3} $$

    이다. 이때 $b$ 를 $-b$ 로 치환하면  

    $$ ||a| - |-b|| \leq |a + b| \iff ||a| - |b|| \leq |a + b| \tag{4} $$

    를 얻는다. $(3)$ 과 $(4)$ 를 병합하면 4) 의 좌측 부등식이 증명된다. ▲ 

    $|x + y| \leq |x| + |y|$ 에서 $x = a - b, y = b - c$ 로 두면 

    $$ |(a - b) + (b - c)| \leq |a - b| + |b - c| \iff |a - c| \leq |a - b| + |b - c| $$

    이므로 5) 가 증명되었다. ■ 

# 유리수의 정의

!!! tldr "동치관계 $\sim$ "

    $a, b, c, d \in \mathbb{Z}$ 에 대하여 $\mathbb{Z} \times (\mathbb{Z} \setminus \{0\})$ 에서 정의된 다음의 관계 $\sim$ 은 동치관계이다.

    $$ (a, b) \sim (c, d) \iff ad = cb $$

- 증명

!!! tldr "유리수 집합(rational number set)"

    유리수 집합은 동치관계 $\sim$ 에 대한 몫집합 $\mathbb{Q} = \mathbb{Z} \times  (\mathbb{Z} \setminus \{0\})/\sim$ 이다.

- $\mathbb{Z}$ 에서 곱셈의 역원의 존재성에 대한 체의 조건이 성립하도록 확장한 것이 $\mathbb{Q}$ 이다. 이 과정은 빼기를 하기 위하여 자연수를 정수로 확장한 과정과 비슷하다. 

    즉, 유리수 집합 $\mathbb{Q}$ 부터는 덧셈, 뺄셈, 곱셈, 나눗셈을 자유롭게 할 수 있는 체(field)이다.

!!! tldr ""

    유리수(rational number) : $a, b \in \mathbb{Z}$ 에 대한 $\mathbb{Q}$ 의 원소인 동치류 $[(a, b)]$ 이다.

- 유리수 집합과 그 동치관계를 다룰 때 동치류 $[(a, b)]$ 를 편하게 $[a, b]$ 로 쓰기로 한다.

    또한 유리수 $[a, b]$ 를 더욱 편하게 $\dfrac{a}{b}$ 라고 쓸 수도 있다.

- 유리수의 동치관계도 정수에서와 마찬가지로 

    $$ \dfrac{a}{c} = \dfrac{b}{d} $$

    로 이해하면, 즉 두 정수의 비율로 이해하면 편하다. 

## 유리수의 덧셈과 곱셈

!!! tldr "유리수 덧셈"

    유리수의 덧셈 $+$ 는 다음과 같이 정의된 함수 $+: \mathbb{Q} \times \mathbb{Q} \to \mathbb{Q}$ 이다.

    $$ [a, b] + [c, d] = [ad + bc, bd] $$
    
!!! tldr "유리수 곱셈"

    유리수의 곱셈 $\cdot$ 는 다음과 같이 정의된 함수 $\cdot : \mathbb{Q} \times \mathbb{Q} \to \mathbb{Q}$ 이다.

    $$ [a, b] \cdot [c, d] = [ac, bd] $$

- 유리수의 덧셈의 항등원과 곱셈의 항등원은 각각 $0 ^{*}, 1 ^{*}$ 이다.

!!! tldr ""

    $a \in \mathbb{Z}$ 에 대하여 다음과 같이 정의한다.

    $$ a ^{*} = [a, 1] \in \mathbb{Q} $$

!!! tldr ""

    정수의 덧셈, 곱셈, 순서관계는 유리수의 덧셈, 곱셈, 순서관계에 매장된다. 즉, $\mathbb{Z} \subset \mathbb{Q}$ 이다. 

- 증명 

    함수 $a \mapsto a ^{*} = [a, 1] : \mathbb{Z} \to \mathbb{Q}$ 가 단사함수임은 자명하다. 또한 

    $$ (a+b) ^{*} = a ^{*} + b ^{*} $$

    $$ (ab)^{*} = a ^{*}b ^{*} $$

    $$ a \geq b \iff a ^{*} \geq b ^{*} $$

    가 성립하므로 더하기, 곱하기, 순서에 관한 한

    $$ \mathbb{Z} \subset \mathbb{Q} $$

    이다. 

## 유리수 집합은 순서체이다

!!! tldr ""

    $\mathbb{Q}$ 는 순서체이다.

- 그러므로 $\mathbb{Q}$ 의 순서관계를 따로 정의할 필요 없다. [순서체의 순서관계](#f68548353)를 따르기 때문이다. 

- 증명

    $\mathbb{Q}$ 는 체의 조건을 만족시킨다. ▲ 

    $P _{\mathbb{Z}} \subseteq \mathbb{Z} = \N \setminus  \{0\}$ 으로 두면 $\mathbb{Z}$ 에는 양수집합이 존재한다. 이 $P _{\mathbb{Z}}$ 에 의하여 $\mathbb{Z}$ 는 

    $$ \mathbb{Z} = P_{\mathbb{Z}} \cup \{0\} \cup (-P_{\mathbb{Z}}) $$

    로 분할된다. 그러므로 유리수 집합은
    
    $$ \mathbb{Q} = \mathbb{Z} \times (\mathbb{Z} \setminus \{0\}) = (P_{\mathbb{Z}} \cup \{0\} \cup (-P_{\mathbb{Z}})) \times (P_{\mathbb{Z}} \cup (-P_{\mathbb{Z}})) $$

    이다. 그러므로 $\mathbb{Q}$ 의 모든 원소가 

    $$ \{0\} \times (\mathbb{Z} \setminus \{0\}), \quad  P_{\mathbb{Z}} \times P_{\mathbb{Z}}, \quad  P_{\mathbb{Z}} \times (-P_{\mathbb{Z}}), \quad  (-P_{\mathbb{Z}}) \times P_{\mathbb{Z}}, \quad  (-P_{\mathbb{Z}}) \times (-P_{\mathbb{Z}}) $$

    로 분할된다. 이때 $\forall (a, b) \in \mathbb{Z}\times (\mathbb{Z}\setminus \{0\}) : (a,b) \sim (-a, -b)$ 이므로 임의의 유리수는 세 집합 

    $$ \{0\} \times P_{\mathbb{Z}}, \qquad P_{\mathbb{Z}} \times P_{\mathbb{Z}}, \qquad (-P_{\mathbb{Z}}) \times P_{\mathbb{Z}} $$

    에 속하는 원소들을 대표원으로 하는 동치류에 의해 결정된다. 이제 

    $$ P _{\mathbb{Q}} = \{[a, b]:(a,b) \in P_{\mathbb{Z}}\times P_{\mathbb{Z}}\} $$

    라 정의하면 $P _{\mathbb{Q} }$ 는 양수집합의 조건 1), 3), 4) 가 만족된다. 또한 유리수의 더하기와 곱하기가 다음과 같이 정의되었었으므로 $P _{\mathbb{Q} }$ 는 덧셈과 곱셈에 대하여 닫혀있어서 양수집합의 조건 2) 도 만족한다.

    $$ [a, b] + [c, d] = [ad + bc, bd], \qquad [a, b] \cdot [c, d] = [ac, bd] $$

    그러므로 $P _{\mathbb{Q} }$ 는 양수집합이고 이 양수집합이 $\mathbb{Q}$ 에 존재하므로 $\mathbb{Q}$ 는 순서체이다. ■ 

!!! tldr "정리 2.2.3"

    임의의 순서체 $F$ 에 대하여 다음을 만족하는 단사함수 $\gamma : \mathbb{Q} \to  F, r \mapsto r \cdot 1_F$ 가 유일하게 존재한다. 

    1. $\forall r, s \in \mathbb{Q} : \gamma (r+s)=\gamma (r)+\gamma (s), \gamma (rs) = \gamma (r) \gamma (s)$

    2. $\gamma (P _{\mathbb{Q}}) = \gamma (\mathbb{Q}) \cap P _{F}$

- 이 정리는 임의의 순서체 $F$ 가 유리수체 $\mathbb{Q}$ 를 포함하며, 두 순서체의 연산과 순서를 구별할 필요가 없음을 말해준다. 

    그러므로 임의의 순서체 $F$ 를 다룰 때 

    $$ \mathbb{Q} \subset F $$

    으로 간주한다. 

- 증명

    임의의 순서체 $F$ 는 체이므로 더하기와 곱하기의 항등원 $0$ 과 $1$ 을 가진다. [정리 2.1.2](#3a99b431b) 에 의하여 다음을 만족하는 함수 $\gamma : \N \to F$ 가 유일하게 존재한다.

    $$ \gamma (0) = 0 $$

    $$ \forall n \in \N : \gamma (n+1) = \gamma (n ^{+}) = \gamma (n) + 1 $$

    이때 좌변의 $\gamma (n+1)$ 의 더하기는 $\N$ 에서 정의된 더하기이고, 우변의 $\gamma (n)+1$ 는 순서체 $F$ 의 더하기이다. 또 우변의 $0, 1$ 은 순서체 $F$ 의 더하기와 곱하기의 항등원이다.

    이제 $m,n \in \N$ 에 대하여 다음이 성립함을 보일 것이다.

    $$ \gamma (n+m) = \gamma (n) + \gamma (m) \tag{1} $$
    
    $$ \gamma (nm) = \gamma (n)\gamma (m) \tag{2} $$

    먼저 $m = 0$ 이면 자명하게 성립한다. 수학적 귀납법을 사용하기 위하여 $m \in \N$ 에서 성립한다고 가정하면 

    $$ \gamma (n+m ^{+}) = \gamma ((n + m) ^{+}) = \gamma (n+m)+1 $$

    $$ = \gamma (n) + \gamma (m) + 1 = \gamma (n) + \gamma (m ^{+}) $$

    이므로 임의의 $m, n \in \N$ 에서 $(1)$ 이 성립함을 알 수 있다. $\blacktriangle$ 
    
    $(2)$ 도 마찬가지로 $m=0$ 이면 자명하고 귀납법을 사용하여 

    $$ \gamma (nm ^{+}) = \gamma (nm+n)= \gamma (nm)+\gamma (n) $$

    $$ = \gamma (n)\gamma (m)+\gamma (n) = \gamma (n)[\gamma (m) +1] = \gamma (n)\gamma (m ^{+}) $$

    가 되어 증명된다. $\blacktriangle$ 

    한편, 임의의 순서체에서 $0<1 \implies 1 \in P _{F}$ 이다. 그러므로 $\gamma (n) \in P _{F}$ 이면 $\gamma (n ^{+}) = \gamma (n) + 1 \in P _{F}$ 이 되어 $n \in \N \setminus \{0\}$ 에 대하여

    $$ \gamma (n) \in P _{F} \tag{3} $$

    이다. $\blacktriangle$ 

    마지막으로 $\gamma : \N \to F$ 가 단사함수임을 보일 것이다. 먼저 $n> m, \gamma (n) = \gamma (m)$ 이라고 가정하여 단사함수의 조건에 어긋나게 하자. 그러면 $n = m + k$ 인 $k \in \N \setminus \{0\}$ 가 존재하여 

    $$ \gamma (k) = [\gamma (m) + \gamma (k)] - \gamma (m) $$

    $$ = \gamma (m+k) - \gamma (m) = \gamma (n) - \gamma (m) = 0 \not \in P _{F} $$

    인데, 이는 $(3)$ 에 모순이므로 $\gamma : \N \to F$ 는 단사함수이다. $\blacktriangle$ 

    이제 $\N \subset \mathbb{Z} \subset \mathbb{Q}$ 를 염두하며 $\gamma : \N \to F$ 역을 $\mathbb{Q}$ 로 확장할 것이다. 먼저 $\mathbb{Z}$ 로 확장하여 함수 $\gamma : \mathbb{Z} \to F$ 를 $n \in \N$ 에 대하여

    $$ \gamma (n) = \gamma (n), \qquad \gamma (-n) = - \gamma (n) \tag{4} $$

    라 정의하자. 두 함수 $\gamma : \N \to F, \gamma : \mathbb{Z} \to F$ 는 함숫값이 $\N$ 위에서 똑같으므로 같은 기호를 사용해도 된다. 비슷하게 $\gamma : \mathbb{Q} \to F$ 를 

    $$ \gamma \bigg (\dfrac{a}{b}\bigg ) = \dfrac{\gamma (a)}{\gamma (b)}, \qquad (a,b) \in \mathbb{Z}\times (\mathbb{Z}\setminus \{0\}) \tag{5} $$

    로 정의하자. 그러면 이렇게 정의된 함수 $\gamma : \mathbb{Q} \to F$ 는 잘 정의되어 있고, $(1),(2),(3)$ 을 만족하는 단사함수가 된다. ▲ 

    이제 순서체 $F$ 의 곱하기의 항등원 $1 _{F}$ 에 대하여 $\gamma$ 함수가 다음을 만족하는지 확인해보자.
    
    $$ \forall r \in \mathbb{Q} : \gamma (r) = r \cdot 1_F $$

    $\gamma : \N \to F$ 의 정의는 자연수의 덧셈의 정의에 의하여 $\gamma _0(n) = 0 + n$ 와 같다. 그러므로 $r \in \N, \gamma (r) = r$ 이다. $\blacktriangle$ 

    $\gamma : \mathbb{Z} \to F$ 의 정의 $(4)$ 는 곧 $\gamma (r) = \begin{cases} r & r \in \N\\ - \gamma (-r) & r \in \mathbb{Z} \text{\textbackslash}\N\\ \end{cases}$ 이므로 $r \in \mathbb{Z}, \gamma (r) = r$ 이다. $\blacktriangle$ 

    $\gamma : \mathbb{Q} \to F$ 의 정의 $(5)$ 는 $\gamma (a) \in \mathbb{Z}, \gamma (b) \in \mathbb{Z} \text{\textbackslash}\{0\}$ 이므로 $r \in \mathbb{Z}, \gamma (r) = r$ 에서

    $$ \gamma \bigg (\dfrac{a}{b}\bigg ) = \dfrac{a}{b} $$

    이다. ■ 

    - (*증명이 허술한 것 같다*)

!!! tldr "정리 2.2.4"

    순서체 $F$ 에 대하여 다음은 동치이다.

    1. $x>0 \implies  \exists n \in \N \setminus \{0\} \text{ s.t.  }\  x > \dfrac{1}{n}$

    2. $x>0 \implies  \exists n \in \N \setminus \{0\} \text{ s.t.  }\  x < n$

    3. 집합 $\N \subset F$ 은 위로 유계가 아니다. 

    4. $\exists n \in \N \setminus \{0\} \text{ s.t. }\ \forall x, y \in P _{F}: y < nx$

- 순서체가 이 동치 조건을 만족하면 아르키메데스의 성질을 만족한다고 한다. 

- 증명 

!!! tldr ""

    아르키메데스의 성질(Archimedean property) : 전순서를 가지는 군 $G$ 의 양의 원소 $x, y$ 에 대하여 다음을 만족하는 $n \in \N$ 이 존재한다.

    $$ y < n \cdot x $$

- 즉, 아무리 작은 원소라도 그것을 유한번 더하여 어떤 원소보다 커질 수 있다면 아르키메데스 성질을 가지고 있다는 것이다. 

- 전순서를 가지는 군 $G$ 의 양의 원소 $x, y$ 에 대하여 

    $$ \forall n \in \N, nx < y $$

    이면 $x$ 는 $y$ 의 무한소(infinitesimal) 이며, $y$ 는 $x$ 의 무한(infinite)이다. 즉, 무한소와 무한이 원소로써 존재하지 않는 군 $G$ 는 아르키메데스의 성질을 가진다는 것이다. 

- 예시 

    $\mathbb{Z}, \mathbb{Q}, \R$ 는 아르키메데스 성질을 만족한다.

    [초실수체 $^{*}\R$](../../HyperrealNumbers/#6d47b2373) 은 아르키메데스의 체가 아니다.

!!! tldr "정리 2.2.5"

    유리수체는 아르키메데스의 성질을 만족한다. 

- 증명 

    $$ m,n \in P _{\mathbb{Z}} \implies \dfrac{n}{m}<2n $$

# 데데킨트 절단으로 정의하는 실수

## 데데킨트 절단

!!! tldr ""

    데데킨트 절단(Dedekind Cut) : 유리수의 집합 $\alpha \subset \mathbb{Q}$ 가 다음을 만족하면 데데킨트 절단이라고 한다.

    1. $\alpha \neq \varnothing , \alpha \neq \mathbb{Q}$

    2. $p \in \alpha , q \in \mathbb{Q}, q < p \to q \in \alpha$ (아래로 무계)

    3. $p \in \alpha \to \exists r \in \alpha \text{ s.t.  }\  p < r$ (최댓값이 존재하지 않음)

- 혹은 더욱 편하게 그냥 절단이라고도 한다. 

!!! tldr ""

    $\forall r \in \mathbb{Q}$ 에 대하여 $r ^{*} = \{p \in \mathbb{Q} : p < r\}$ 은 절단이다. 

- 예시 

    집합 $\alpha = \{p \in \mathbb{Q} : p \leq 0\} \cup \{p \in \mathbb{Q} : 0 < p, p ^{2} < 2\}$ 이 절단임을 보이자.

    $0 \in \alpha , 2 \not \in \alpha$ 이므로 절단의 조건 1) 을 만족한다. ▲ 

    $q < p \in \alpha$ 일 때 $q \leq 0 \implies  q \in \alpha$ 이고, $0 < q < p \land p ^{2} < 2 \implies  q ^{2} < 2$ 이므로 $q \in \alpha$ 이다. 이로써 절단의 조건 2) 를 만족한다. ▲ 

    $p \in \alpha$ 에 대하여 $p \leq 0 \to p < 1 \in \alpha$ 이다. 한편 $0 < p, p ^{2} < 2$ 이면 [정리 2.2.5](#225d37510) 를 적용하여 $\dfrac{1}{n}(2p+1) < 2 - p ^{2}$ 인 $n \in \N$ 을 잡을 수 있다. 그러면 $p ^{2} + \dfrac{2}{n}p + \dfrac{1}{n} < 2$ 에서 $\dfrac{1}{n} \leq \dfrac{1}{n ^{2}}$ 이므로

    $$ \bigg (p + \dfrac{1}{n}\bigg ) ^{2} \leq p ^{2} + \dfrac{2}{n}p + \dfrac{1}{n} < 2 $$

    이다. 그러므로 
    
    $$ p + \dfrac{1}{n} \in \alpha$$ 
    
    이다. 이로써 절단의 조건 3) 도 성립한다. 그러므로 $\alpha$ 는 절단이다. ■ 

    - 한편 이 절단 $\alpha$ 는 무리수 $\sqrt[]{2}$ 를 유리수로부터 정의하기 위하여 존재하는데, 더 명확하게 이를 보이기 위하여 
    
        $$ \forall r \in \mathbb{Q} : \alpha \neq r ^{*} = \{p \in \mathbb{Q} : p < r\}$$ 
        
        임을 보이자. 이를 위해 $\alpha  = r ^{*}$ 인 유리수 $r \in \mathbb{Q}$ 이 있다고 가정한다. 만약 $r ^{2} < 2$ 이면 위에서 한 것처럼 

        $$ \bigg (r + \dfrac{1}{n}\bigg )^{2} < 2 $$

        인 자연수 $n \in \N$ 이 존재한다. 그러면 $r + \dfrac{1}{n} \in \alpha \land r + \dfrac{1}{n} \not \in r ^{*}$ 이 되어 모순이다. 

        반대로 $r ^{2} > 2$ 라고 가정하자. 그러면 비슷하게 

        $$ \bigg (r - \dfrac{1}{m}\bigg )^{2} > 2 $$

        인 자연수 $m \in \N$ 이 존재한다. 그러면 $r - \dfrac{1}{m} \not\in \alpha \land r - \dfrac{1}{m} \in r ^{*}$ 가 되어 모순이다. 그러므로 

        $$ \therefore r ^{2} = 2 $$

        인데 이와같은 $r \in \mathbb{Q}$ 는 존재하지 않는다. 왜냐하면 무리수이기 때문이다. ■ 

!!! tldr ""

    절단 $\alpha$ 에 대하여 $\alpha ^{c} = \mathbb{Q} \setminus \alpha$ 라 두면 다음이 성립한다.

    - $p \in \alpha , q \in \alpha ^{c} \implies p < q$
    
    - $r \in \alpha ^{c}, r < s \implies s \in \alpha ^{c}$

- 그러므로 두 집합 $\alpha , \alpha ^{c}$ 를 수직선 위의 점들로 보면, 다음과 같이 각각이 수직선을 왼쪽과 오른쪽으로 분할하는 것으로 표현된다. 단, 왼쪽 점들 $\alpha$ 는 절단의 조건 3) 에 의하여 최댓값을 가지지 않는다. 

    ![](https://upload.wikimedia.org/wikipedia/commons/7/72/Dedekind_cut_sqrt_2.svg)

## 실수의 정의

!!! tldr "데데킨트 절단으로 정의하는 실수 집합(real number set)"

    실수 집합은 데데킨트 절단 전체의 집합 $\R$ 이다. 

- 유리수 $\mathbb{Q}$ 에 의하여 정의된 모든 절단들은 그 절단으로 자동으로 생성되는 오른쪽 절단과 함께 유리수나 무리수를 그 사이에 둘 수 있게 된다. 가령 위에서 살펴본 절단이 무리수 $\sqrt[]{2}$ 를 표현한 것처럼 말이다.

    이로써 모든 절단을 곧 모든 유리수와 모든 무리수로 대응시키는 전단사 함수를 만들 수 있다. 그러므로 실수(유리수와 무리수)를 데데킨트 절단으로 구성할 수 있다는 것이다. 

!!! tldr ""

    양의 실수 집합은 $0 ^{*} = \{p \in \mathbb{Q} : p < 0\}$ 에 대하여 다음의 집합으로 정의된다.

    $$ P _{\R} = \{\alpha \in \R : \alpha > 0 ^{*}\} $$

!!! tldr ""

    실수 집합과 데데킨트 절단 집합 사이에 전단사 사상이 존재한다.

- 이 증명은 모든 실수가 데데킨드 절단으로 하나도 빠짐없이 대응되고, 그 역도 성립함을 말해준다.

- 증명 (https://proofwiki.org/wiki/Reals_are_Isomorphic_to_Dedekind_Cuts)

    $\R$ 과 데데킨트 절단 집합 $\mathscr{D}$ 사이의 사상 $f:\R \to \mathscr{D}$

    $$ \forall x \in \R: f(x) = \{y \in \mathbb{Q} : y < x\} $$

    이 전단사임을 보이자.

    먼저 $\forall x \in \R : f(x) \in \mathscr{D}$ 를 보일 것이다. $x \in \R$ 라고 하자. 우리는 $f(x)$ 가 

    $$ \forall z \in f(x) : \forall y \in \mathbb{Q} : y < z \implies y \in f(x) \tag{1} $$

    $$ \forall z \in f(x) : \exists y \in f(x) : z < y \tag{2} $$

    인 $\mathbb{Q}$ 의 진부분집합 임을 보여야 한다. 우선 $f$ 의 정의에 의하여 $x \not\in f(x) = \{y \in \mathbb{Q} : y < x\}$ 이므로 $f$ 는 $\mathbb{Q}$ 의 진부분집합 이다. ▲ 

    $z \in f(x), y \in \mathbb{Q} \text{ s.t. } y < z$ 이라고 하자. 그러면 $f(x)$ 의 정의 에 의하여 $z < x$ 이므로 $y < z < x$ 인데, $f(x)$ 의 정의에 의하여 $y \in f(x)$ 이다. 이로써 $(1)$ 이 증명되었다. ▲ 

    $f(x)$ 의 정의에 의하여 $z < x$ 인데 [정리 2.5.2](#849201a15) 에 의하여 

    $$ \exists r \in \mathbb{Q} : z < r < x $$

    이다. 그러면 $f(x)$ 의 정의에 의하여 $r \in f(x)$ 이므로 $\exists r \in f(x) : z < r$ 이 되어 $(2)$ 가 증명되었다. ▲ 

    이제 $f$ 가 단사이면서 전사임을 보이면 된다. 
    
    먼저 $f: \R \to \mathscr{D}$ 가 단사임을 보이자. $x_1, x_2 \in \R$ 에 대하여 $f(x_1) = f(x_2) \implies x_1 \neq x_2$ 라고 하자. 이때 $x_1 < x_2$ 라고 가정해도 무방하므로 [정리 2.5.2](#849201a15) 에 의하여 

    $$ \exists r \in \mathbb{Q} : x_1 < r < x_2 $$

    이다. 그러면 $f(x)$ 의 정의에 의하여 $r \not\in f(x_1) \land r \in f(x_2)$ 이다. 이는 $f(x_1) = f(x_2)$ 에 모순이다. 그러므로 $x_1 = x_2$ 이다. 그러므로 $f$ 는 단사이다. ▲ 

    이제 $f: \R \to \mathscr{D}$ 가 전사임을 보일 것이다. 이를 위하여 $L \in \mathscr{D}$ 에 대하여 $\exists  x \in \R \text{ s.t. } f(x) = L$ 임을 보이면 된다. 절단의 정의에 의하여 $L$ 은 $\mathbb{Q}$ 의 진부분집합 이고 진부분집합 의 정의에 의하여 

    $$ \exists r \in \mathbb{Q} : r \not\in L $$

    이다. 그러면 절단의 정의에 의하여 

    $$ \forall x \in L : \forall y \in \mathbb{Q} : y < x \implies y \in L \tag{3} $$

    이므로 $\forall x \in L : r \not < x \land r \neq x$ 이고, 결국 $\forall x \in L : x < r$ 이다. 그러면 $L$ 은 위로 유계이고 $\sup (L) \leq r$ 이 성립한다. 한편 절단의 상한이 실수에 대응되므로 $\sup (L) \in \R$ 이다. 이때 상한의 정의에 의하여 

    $$ \forall x \in L : x < \sup (L) $$

    이다. 이제 다음을 증명할 것이다. 이것이 증명되면 $L$ 에 대응되는 실수가 $\sup (L)$ 임이 증명되어 $L = f(\sup (L))$ 이므로 공역의 임의의 원소에 대응되는 정의역의 원소가 존재한다고 할 수 있다. 그러면 $f: \R \to \mathscr{D}$ 이 전사임이 증명되고, 이로써 모든 증명이 끝난다.

    $$ \forall x \in \mathbb{Q} : x < \sup (L) \implies x \in L $$

    $x \in \mathbb{Q}$ 가 $x < \sup (L)$ 인데 $x \not\in L$ 이라고 하자. 
    
    $x$ 이 $L$ 에 속하지 않으므로 절단의 정의 $(3)$ 에 의하여 $\forall y \in L : x \geq y$ 이다. 그러면 $x$ 은 $L$ 의 상계이고 $x \geq \sup (L)$ 이다. 이는 $x < \sup (L)$ 와 모순이다. ■ 

    - 아.. proofwiki 에서 마지막 부분에 $x$ 를 $r$ 로 써놔서 엄청 헷갈렸네. 아으..

## 실수의 순서관계

!!! tldr "실수의 순서관계"

    절단 $\alpha , \beta$ 에 대하여 다음과 같이 정의한다.

    $$ \alpha \leq \beta \iff \alpha \subset \beta $$

    $$ \alpha < \beta \iff \alpha \leq \beta \land \alpha \neq \beta $$

!!! tldr "정리 2.3.1"

    $\forall \alpha , \beta \in \R$ 에 대하여 다음 중 한 명제만 성립한다. 

    - $\alpha > \beta$
    
    - $\alpha = \beta$
    
    - $\alpha < \beta$

- 증명 

    만약 $\beta \subset \alpha$ 이면 $p \not \in \beta$ 인 $p \in \alpha$ 가 존재한다. 이때 $q \in \beta$ 이면 $p \not\in \beta$ 로부터 $q<p$ 임을 알 수 있으므로 $q \in \alpha$ 이다. 

    즉, $\alpha \subset \beta$ 가 아니면 $\beta \subset \alpha$ 가 되므로 두 절단 $\alpha , \beta$ 가 주어지면 $\alpha \leq \beta  \lor \alpha \geq \beta$ 이다. ■ 

- 이 정리는 양의 실수 $P _{\R} = \{\alpha \in \R : \alpha > 0 ^{*}\}$ 가 순서체의 조건 2), 3) 을 만족함을 말해준다. 

- 그냥, 어떤 절단들이 주어지면 최소상계가 더 오른쪽에 주어진 절단이 왼쪽의 절단을 전부 다 포함한다는 것을 떠올리면 된다. 이것이 아닐 경우 두 절단은 서로 같다.

!!! tldr "정리 2.3.2"

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
    
    와 같이 두자. 그러면 $\delta \subsetneq \alpha$ 이므로 유리수 $r \in \alpha \setminus \delta$ 가 존재한다. 이때 $r \in \alpha$ 로부터 $r \in \beta$ 인 $\beta \in A$ 가 존재한다. 그렇다면 $r \in \beta \land r \not\in \delta \implies \beta \not \leq \delta$ 이고 [정리 2.3.1](#24bb59962) 에 의하여 $\delta < \beta$ 이다. 그런데 $\beta \in A$ 이므로 $\delta$ 는 자명하게 $A$ 의 최소상계가 아니다. 이는 가정 "$\delta$ 가 최소상계이다" 에 모순이므로 $\delta$ 가 $A$ 의 최소상계라면 
    
    $$\delta \geq \alpha$$
    
    이것은 명백하게 $\alpha$ 가 상한임을 말해준다. ■ 

## 실수의 덧셈

!!! tldr "실수 덧셈"

    실수의 덧셈 $+$ 는 다음과 같이 정의된 함수 $+: \R \times \R \to \R$ 이다.

    $$ \alpha + \beta = \{s + t \in \mathbb{Q} : s \in \alpha , t \in \beta \} $$

!!! tldr ""

    $$ \alpha + \beta \in \R $$

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

!!! tldr ""

    실수의 덧셈은 결합법칙과 교환법칙을 만족한다.

- 증명

!!! tldr ""

    $0 ^{*} = \{p \in \mathbb{Q} : p<0\} \in \R$ 은 실수 덧셈의 항등원이다.

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

!!! tldr ""

    실수의 더하기의 역원이 존재한다. 

- 실수 $\alpha$ 의 더하기의 역원을 $-\alpha$ 라고 한다.

- 증명 

    각 $\alpha \in \R$ 에 대하여 

    $$ \beta = \{p \in \mathbb{Q} : \exists r \in \mathbb{Q}, r > p \land -r \not\in \alpha \} $$

    라 두고 $\beta \in \R$ 과 $\alpha + \beta = 0 ^{*}$ 임을 보일 것이다. 
    
    이때 조건 $-r \not\in \alpha$ 은 $-r$ 이 절단 $\alpha$ 의 오른쪽에 존재한다는 것이다. 그렇다면 절단 $\alpha$ 오른쪽을 뜻하는 $\mathbb{Q}\setminus \alpha$ 에 대하여 유리수 $s \in \mathbb{Q}\setminus \alpha$ 를 택하면 이 $s$ 는 $-r$ 과 같다고 생각할 수 있으므로 $-s > p$ 인 $p \in \mathbb{Q}$ 를 택하면 $p \in \beta$ 이다. (*이로써 절단의 조건 1) 의 첫째 명제 $\beta \neq \varnothing$ 가 증명되었다.*)

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

    이 증명되었다. $\blacktriangle$ 

    이제 $\alpha + \beta = 0 ^{*}$ 을 보일텐데, $q \in \alpha , p \in \beta$ 이면 $r > p, -r \not\in \alpha$ 인 $r \in \mathbb{Q}$ 이 다음과 같이 존재한다.

    ![image](https://user-images.githubusercontent.com/16812446/110421597-2a439080-80e1-11eb-9e50-53f0d424795d.png)

    ![image](https://user-images.githubusercontent.com/16812446/110421731-6aa30e80-80e1-11eb-8c98-a05c5b3a0232.png)

    그러면 $q \in \alpha , -r \not\in \alpha \implies q < -r$ 이다. 그러므로 

    $$ -(q + p) = (r - p) + (-r - q) > 0 $$

    이고, (*왜냐하면 $0 < -r -q, r - p > 0$ 이기 때문*) 
    
    $$ \iff  q + p < 0 $$

    이므로 $\alpha + \beta \subset 0 ^{*}$ 이다. $\blacktriangle$ 
    
    이제 $0 ^{*} \subset \alpha + \beta$ 를 보이면 모든 증명이 끝난다. 이를 위하여 $s \in 0 ^{*}$ 에 대한 $t = \dfrac{-s}{2} > 0$ 인 $t \in \mathbb{Q}$ 에 대하여 

    $$ A = \{n \in \mathbb{Z} : nt \in \alpha \} $$

    라 두자. 이때 $A$ 가 위로 유계가 아니라고 가정하자. (*하지만 집합 $A$ 의 정수 $n$ 는 절단 $\alpha$ 에 $nt$ 가 속할 때 정의되므로 $n$ 에 상계가 있을 것으로 보인다.*) 그러면 [정리 2.2.5](#225d37510) 에 의하여 $\forall q \in \mathbb{Q}, q < mt$ 인 $m \in \N$ 이 존재한다. 그런데 $A$ 가 위로 무계라고 가정하였으므로 $m$ 은 $A$ 의 상계가 아니고, $m < n$ 인 $n \in A$ 이 존재한다. 결국 $q < nt$ 이고, $nt \in \alpha$ 이므로 
    
    $$\forall q \in \mathbb{Q}, q \in \alpha \implies \alpha = \mathbb{Q}$$

    가 되어 모순이다. 그러므로 $A$ 는 위로 유계이고, [따름정리 2.1.6](#749829205) 에 의하여 즉, $n_0t \in \alpha \land (n_0+1)t \not\in \alpha$ 이다. 이제 

    $$ r = s - n_0 t = -(n_0 + 2)t $$

    라 두면, $-(n_0+1)t > r \land (n_0+1)t \not\in \alpha$ 이므로 $r \in \beta$ 임을 알 수 있다. 따라서 $s \in 0 ^{*}$ 이

    $$ s = n_0t + r \in \alpha + \beta $$

    의 관계를 가지므로 $\forall s \in 0 ^{*}, s \in \alpha + \beta$ 를 알 수 있고, 이에 따라 

    $$ 0 ^{*} \subset \alpha + \beta $$

    이며, 이로써 모든 증명이 끝났다. ■ 

## 실수의 곱셈

!!! tldr "실수 곱셈"

    양의 실수의 곱셈 $\cdot$ 은 다음과 같이 정의된 함수 $\cdot : P_{\R} \times P_{\R} \to P_{\R}$ 이다.

    $$ \alpha \beta  = \{p \in \mathbb{Q} : \exists r \in \alpha \cap P _{\mathbb{Q}} \land \exists s \in \beta \cap P _{\mathbb{Q}} \text{ s.t. }\ p \leq rs \} $$

    양의 실수에 대한 곱셈 $\cdot$ 을 기반으로 실수에 대한 곱셈 $\cdot : \R \times \R \to \R$ 을 다음과 같이 정의한다.

    $$ \alpha \beta = \begin{cases} 0 ^{*} &\alpha = 0 ^{*} \lor \beta = 0 ^{*}\\ -(-\alpha )\beta  &\alpha \in -P _{\R}, \beta \in P _{\R}\\ -\alpha (-\beta)  &\alpha \in P _{\R}, \beta \in -P _{\R}\\ (-\alpha )(-\beta)  &\alpha \in -P _{\R}, \beta \in -P _{\R}\\ \end{cases} $$

!!! tldr ""

    $\alpha , \beta \in P _{\R}$ 에 대하여 $\alpha \beta \in \R$ 이다. 

- 증명 

    $0 \in \alpha , 0 \in \beta \implies 0 \in \alpha \beta \implies \alpha \beta \neq \varnothing$ 이므로 절단의 조건 1) 의 첫째 명제가 증명되었다. 

    $u \not\in \alpha , v \not\in \beta \to uv \not\in \alpha \beta \implies \alpha \beta \neq \mathbb{Q}$ 이므로 절단의 조건 1) 의 둘째 명제가 증명되었다. 실제로 $\forall s \in \alpha , t \in \beta, s < u \land t < u \implies st < uv$ 이다. 

    절단의 조건 2), 3) 은 정의에 의하여 자명하다. 그러므로 

    $$ \therefore \alpha \beta \in \R $$

    이다. ■ 

    특히, 순서체의 조건 1) 의 둘째 명제 "$a,b \in P, ab \in P$ (곱하기에 대하여 닫혀있음)" 도 증명되었다. 

!!! tldr ""

    실수 곱셈에 대한 역원이 존재한다. 

- 증명 

    각 $\alpha \in P _{\R}$ 에 대하여 

    $$ \gamma = 0 ^{*} \cup \{0\} \cup \{q \in P _{\mathbb{Q}} : r > q, \dfrac{1}{r} \not\in \alpha \text{ 인 } r \in P _{\mathbb{Q}} \text{ 이 존재한다}\} $$

    라 정의하면 $\gamma$ 가 절단이고 $\alpha \gamma = 1 ^{*}$ 임을 보일 수 있지만, 조금 시간이 흐른 후 보이겠다. 

    이제 $\alpha \in -P _{\R}$ 에 대하여 

    $$ \alpha \bigg (- \dfrac{1}{- \alpha }\bigg ) = - \alpha \bigg (\dfrac{1}{- \alpha }\bigg ) = (- \alpha )\bigg (\dfrac{1}{- \alpha }\bigg ) = 1 ^{*} $$

    이므로 최종적으로 $\alpha \neq 0$ 인 $\alpha \in \R$ 는 곱하기의 역원을 가진다. 

!!! tldr ""

    $P_{\R}$ 은 덧셈과 곱셈에 대하여 닫혀있다.

- 증명

    만약 $\alpha > 0 ^{*}$ 이면 (*양수인*) $p \in \alpha \setminus 0 ^{*}$ 을 택할 수 있다. 이는 $0 \leq p, p \in \alpha$ 이므로 (*절단의 조건 2) 에 의하여*) $0 \in \alpha$ 이다. 반대로 $0 \in \alpha$ 이면 (*절단의 조건 2) 에 의하여*) $p < 0 \implies p \in \alpha$ 인데 (*이는 절단 $\alpha$ 가 $0$ 을 포함하면서 아래로 무계인데 $0 ^{*}$ 는 $0$ 을 포함하지 않는 절단이므로*) 이는 $0 ^{*} < \alpha$ 임을 뜻한다. 그러므로 

    $$ 0 ^{*} < \alpha \iff 0 \in \alpha $$

    이다. 이 결과로 덧셈에 대하여 닫혀있음을 바로 알 수 있다. 어떤 절단 $a,b$ 가 $a > 0 ^{*} \land b > 0^{*}$ 이면 $0 \in a \land 0 \in b$ 이므로 $a > 0, b > 0$ 이기 때문이다. 

## 실수는 순서체이다

!!! tldr ""

    $\R$ 은 순서체이다. 

- 지금까지의 논의의 결과가 이 정리이다. 특히 $\R$ 이 정리 2.3.2 를 만족한다는 사실도 중요한데 이것과 $\R$ 이 순서체라는 것에 의하여 $\R$ 이 완비순서체가 되기 때문이다. 

## 실수의 성질

!!! tldr ""

    $\forall r, s \in \mathbb{Q}$ 에 대하여 다음이 성립한다.

    - $r = s \iff  r ^{*} = s ^{*}$

    - $(r + s ) ^{*} = r ^{*} + s ^{*}$

    - $(rs) ^{*} = r ^{*} s ^{*}$

    - $r \in P _{\mathbb{Q}} \iff r ^{*} \in P _{\R}$

- 이 정리는 $r \mapsto r ^{*} : \mathbb{Q} \to \R$ 이 연산과 순서를 보존하는 단사함수임을 말해준다. 

# 코시 수열로 정의하는 실수

## 코시 수열

!!! tldr ""

    수열(sequence) : 집합 $X$ 에 대한 함수 $x : \N \to X$ 이다. 

!!! tldr ""

    수렴(convergence) : 순서체 $F$ 의 수열 $x : \N \to F$ 와 $a \in F$ 가 주어졌을 때 $\forall e \in P _{F}$ 에 대하여 다음을 만족하는 $N \in \N$ 이 존재하면 $x$ 가 $a \in F$ 로 수렴한다고 한다.

    $$ i \geq N \implies |x(i) - a| < e $$

- 이 정의에서 $\forall e \in P _{F}$ 의 의미는 체 $F$ 의 양의 원소 $e$ 가 아주 아주 작은 값으로 줄어든다는 것이고, $|x(i) - a|$ 는 수열의 값 $x(i)$ 와 $a$ 와의 차이값을 뜻한다. 

    그러므로 얼마나 작은 $e$ 를 가져오든지간에 

    $$  |x(i) - a| < e $$

    를 만족시키는 자연수 $N$ 이 존재하여 수열이 $a$ 와 $e$ 보다 가깝다는 것을 보여주는 정의이다. 이로써 이 정의는 수열 $x$ 가 $a$ 와 무한히 가까워지는 형태를 표현할 수 있는 것이다.

!!! tldr "코시 수열(cauchy sequence)"

    체 $F$ 에 대한 $\forall e \in P _{F}$ 와 수열 $x : \N \to F$ 에 대하여 다음을 만족하는 자연수 $N$ 이 존재하면 $x$ 를 코시 수열이라 한다.

    $$ i,j \geq N \implies |x(i) - x(j)| < e $$

- 쉽게 말해 수열의 항들이 임의의 거리 내로 수렴해가면 코시 수열이다. 즉, 다음은 코시 수열이다.

    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Cauchy_sequence_illustration.svg/375px-Cauchy_sequence_illustration.svg.png)

    다음은 코시수열이 아니다.

    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Cauchy_sequence_illustration2.svg/375px-Cauchy_sequence_illustration2.svg.png)

- 예시 

    수열 $a_n = \sqrt[]{n}$ 은 코시 수열이다. 왜냐하면 다음과 같이 수열의 두 항의 차이값이 임의의 양수보다 작도록 수렴하기 때문이다. 

    $$ a _{n+1} - a_n = \sqrt[]{n+1} - \sqrt[]{n} = \dfrac{1}{\sqrt[]{n+1} + \sqrt[]{n}} < \dfrac{1}{2 \sqrt[]{n}} $$

!!! tldr "기본열"

    기본열은 코시수열 $x : \N \to \mathbb{Q}$ 이다.

!!! tldr ""

    $r \in \mathbb{Q}, i \in \N$ 에 대하여 기본열 같이 정의된 $r ^{*}$ 은 기본열이다.

    $$ r ^{*}(i) = r $$

!!! tldr ""

    유계 수열(bounded sequence) : 순서체 $F$ 의 수열 $x$ 와 $i \in \N$ 에 대하여 다음을 만족하는 $M \in F$ 가 있으면 $x$ 는 유계수열이다.

    $$ |x(i)| \leq M $$

!!! tldr ""

    순서체 $F$ 의 수열 $x : \N \to F$ 가 유계일 필요충분조건은 집합 $\{x(i) \in X : i \in \N\}$ 이 위로 유계이고 동시에 아래로 유계인 것이다. 

- 증명

!!! tldr "정리 2.4.1"

    순서체 $F$ 의 수열 $x : \N \to F$ 가 수렴하면 코시수열이다.

    임의의 코시 수열은 유계이다.

- 증명 

    순서체 $F$ 의 수열 $x : \N \to F$ 가 $\forall e \in P _{F}$ 에 대하여 $a \in F$ 로 수렴한다고 하면

    $$ i \geq N \implies |x(i) - a| < \dfrac{e}{2} $$

    인 $N \in \N$ 이 존재한다. 그러면 임의의 $i, j \geq N$ 에 대하여 [정리 2.2.2](#84983902d) 에 의하여

    $$ |x(i) - x(j)| \leq |x(i) - a| + |x(j) - a| < \dfrac{e}{2} + \dfrac{e}{2} = e $$

    가 되어 $x$ 는 코시 수열이다. $\blacktriangle$ 

    이제 역으로 $x$ 가 코시 수열이라고 가정하면 $i, j \geq N \implies |x(i) - x(j)| < 1$ 인 $N \in \N$ 이 존재한다. [정리 2.2.2 의 5)](#84983902d) 에서 $c = 0$ 으로 두면 $|a| - |b| \leq |a - b|$ 이므로 임의의 자연수 $i \geq N$ 에 대하여 
    
    $$|x(i) - x(N)| < 1 \iff |x(i)| - |x(N)| \leq |x(i) - x(N)| < 1$$
    
    이므로 $|x(i)| < |x(N)| + 1$ 이다. 이제 

    $$ M = \sup \{|x(0)|, |x(1)|, \dots, |x(N-1)|, |x(N)|+1\} $$

    라 두면 

    $$ \forall i \in \N, |x(i)| \leq M $$

    이다. ■ 

## 실수의 정의

!!! tldr "기본열의 동치관계 $\sim$"

    두 기본열 $\alpha , \beta : \N \to \mathbb{Q}$ 와 $\forall e \in P _{\mathbb{Q}}$ 에 대하여 

    $$ i \geq N \implies |\alpha (i) - \beta (i)| < e $$

    인 $N \in \N$ 이 존재할 때 $\alpha \sim \beta$ 라고 정의한 관계 $\sim$ 는 동치관계이다.

- 증명 

    $\alpha \sim \alpha$ 와 $\alpha \sim \beta \implies \beta \sim \alpha$ 가 성립함은 자명하므로 동치관계의 조건 1), 2) 가 성립한다. 

    $\alpha \sim \beta, \beta \sim \gamma$ 라 두면 

    $$ i \geq N_1 \implies |\alpha (i) - \beta (i)| < \dfrac{e}{2}, \qquad i \geq N_2 \implies |\beta (i) - \gamma (i)| < \dfrac{e}{2} $$

    인 자연수 $N_1, N_2 \in \N$ 이 존재하는데 $N = \sup \{N_1,N_2\}$ 라 두면 임의의 $i \geq N$ 에 대하여 

    $$ |\alpha (i) - \gamma (i)| \leq |\alpha (i) - \beta (i)| + |\beta (i) - \gamma (i)| < \dfrac{e}{2} + \dfrac{e}{2} = e $$

    이므로 

    $$ \alpha \sim \gamma $$

    이다. 이로써 동치관계의 조건 3) 도 성립함을 보였다. 

    그러므로 관계 $\sim$ 은 기본열 전체의 집합 $\mathcal{F}$ 의 동치관계이다.

!!! tldr "코시 수열로 정의하는 실수 집합(real number set)"

    실수 집합은 기본열의 동치관계 $\sim$ 와 기본열 전체의 집합 $\mathcal{F}$ 에 대한 몫집합 $\R = \mathcal{F}/\sim$ 이다.

- 또한 이 몫집합 $\R = \mathcal{F}/\sim$ 의 원소를 실수(real number) 라고 한다.

- 이와 같은 실수의 구성방법을 쉽게 말하면 이렇다. 

    어떤 기본열이 제곱하여 $2$ 보다 작은 수로써 각 항 $i$ 마다 $i-1$ 번째까지 소수 자리를 갖는다고 하자. 그러면 이 기본열은 다음과 같은 형태를 가져서 제곱해도 $2$ 보다 작은 유리수로 구성된다.

    $$ (1, 1.4, 1.41, 1.141, \dots) $$

    이러한 유리수열은 수열의 항 $i$ 가 매우 커짐에 따라 인접한 두 항의 차이값이 $0$ 로 수렴한다. 이것은 분명 유리수열이지만 그 항이 무한이 커짐에 따라 그 값이

    $$ \sqrt[]{2} $$

    로 근사된다. 이처럼 유리수열이지만 무한한 항을 따져보면 무리수가 되는 것이 존재한다. 물론 무한한 항이 유리수인 기본열도 존재한다. 

    코시수열에 의한 실수의 구성은 이러한 모든 기본열을 통틀어서 실수(유리수와 무리수)를 구성하는 것이다.

- 한편, 방금 $(1, 1.4, 1.41, 1.141, \dots)$ 이라는 기본열을 $\sqrt[]{2}$ 라는 실수로 근사시켰는데, 어떤 실수를 구성하기 위한 유리수열은 유일하지 않다. 즉, 실수 $x \in \R$ 로 수렴하는 모든 기본열이 $x$ 의 표현들이며, 이것들을 동치류로 묶어서 표현해버리는 것이다.

    가령 다음과 같이 실수 $\pi$ 를 구성하는 여러가지 방법이 존재한다. 

    $$ \pi = 4 \bigg (\dfrac{1}{1} - \dfrac{1}{3} + \dfrac{1}{5} - \dfrac{1}{7} + \dots\bigg ) \tag{1} $$

    $$ \dfrac{\pi }{2} = \dfrac{2}{1}\cdot \dfrac{2}{3} \cdot \dfrac{4}{3} \cdot \dfrac{4}{5} \cdot \dfrac{6}{5} \cdot \dfrac{6}{7} \cdot \dots \tag{2} $$

    $$ \dfrac{\pi ^{2}}{6} = \dfrac{1}{1 ^{2}} + \dfrac{1}{2 ^{2}} + \dfrac{1}{3 ^{2}} + \dfrac{1}{4 ^{2}} + \dots \tag{3} $$

    $$ \dfrac{2}{\pi } = \dfrac{\sqrt[]{2}}{2} \cdot \dfrac{\sqrt[]{2 + \sqrt[]{2}}}{2} \cdot \dfrac{\sqrt[]{2+ \sqrt[]{2 + \sqrt[]{2}}}}{2} \dots \tag{4} $$

    위에서 보인 $4$ 가지 방법 이외에도 $\pi$ 라는 실수를 구성하는 기본열의 종류는 매우 다양하다. 가령 $(1)$ 에서 나타난 기본열 
    
    $$ \alpha(n) = 4 \sum_{k=1}^{n} (-1) ^{k+1} \dfrac{1}{2k - 1} $$

    은 $n \to \infty \implies \alpha (n) \to \pi$ 가 되는데, 이처럼 $\pi$ 로 근사되는 모든 기본열들을 동치관계로 묶어서 그 동치류를 실수 파이($\pi$)

    $$ \pi = [\alpha (n)] $$

    로 표현하겠다는 것이다.

    - 두 기본열의 무한항의 근사값이 똑같다는 표현을 두 기본열 $\alpha , \beta$ 가 

        $$ \forall e \in P _{\mathbb{Q}}, |\alpha (i) - \beta (i)| < e $$

        라고 표현한 것이다. $e$ 를 $0$ 에 수렴하는 양수라고 생각하면 되니까..

## 실수의 순서관계

!!! tldr "실수 순서관계"

    $[\alpha ], [\beta ] \in \R$ 에 대하여 

    $$ i \geq N \implies \alpha (i) - \beta (i) > d $$

    를 만족하는 유리수 $d > 0$ 와 자연수 $N \in \N$ 가 있을 때 $[\alpha ] > [\beta ]$ 라고 정의한다.
    
- 이 순서관계도 마찬가지로 기본열의 무한항($i$ 가 무한히 커지는 것을 $\exists N \in \N, i \geq N$ 로 표현한 것)이 특정 값으로 근사되었을 때 그 차이값이 양의 유리수 $d > 0$ 보다 크다는 것으로 실수의 순서를 정의한 것으로 이해하면 된다.

!!! tldr "정리 2.4.2"

    $\forall [\alpha ], [\beta ] \in \R$ 에 대하여 다음 중 오직 하나만 성립한다. 

    - $[\alpha ] > [\beta ]$
    
    - $[\alpha ] = [\beta ]$
    
    - $[\alpha ] < [\beta ]$

- 증명 

    $\forall e \in \mathbb{Q}, e > 0$ 에 대하여 

    $$ i \geq N_e \implies |\alpha (i) - \alpha (N_e)| <e, |\beta (i) - \beta (N_e)| <e $$

    가 성립하는 최소 자연수 $N_e$ 이 존재한다. $N_e$ 은 $e$ 에 대하여 결정된다. 그러면 각 $i \geq N_e$ 에 대하여 

    $$ \alpha (N_e) - \beta (N_e) - 2e < \alpha (i) - \beta (i) <\alpha (N_e) - \beta (N_e) + 2e \tag{1} $$

    이다. 이제 

    $$ d_e = \alpha (N_e) - \beta (N_e) -2e, \qquad d'_e = \alpha (N_e) - \beta (N_e) + 2e $$

    로 두자. 

    그러면 적당한 유리수 $e > 0$ 에 대하여 $d_e > 0$ 인 경우 

    $$ i \geq N_e \implies \alpha (i) - \beta (i) > d_e $$

    이므로 $[\alpha ] > [\beta ]$ 이고, 또한 적당한 유리수 $e>0$ 에 대하여 $d'_e<0$ 이면 

    $$ i \geq N_e \implies \beta  (i) - \alpha(i) > -d'_e $$

    이므로 $[\beta ]>[\alpha ]$ 이다. $\blacktriangle$ 

    이제 이 두 가지 경우가 성립하지 않는다고 하면 임의의 유리수 $e > 0$ 에 대하여 
    
    $$d_e= \alpha (N_e) - \beta (N_e) -2e \leq 0,\qquad  d'_e= \alpha (N_e) - \beta (N_e) + 2e \geq 0$$
    
    이다. (*이때 $d_e = d'_e = 0$ 이면 $e=0$ 이 되어 모순이므로 둘 다 $0$ 이면 안된다 조건이 추가되어야 하지 않나*) 그러므로 

    $$ \alpha (N_e) - \beta (N_e) \leq 2e, \qquad \beta (N_e) -  \alpha (N_2) \leq 2e $$

    $$ \iff |\alpha (N_e) - \beta (N_e)| \leq 2e $$

    인데, 

    (*이때 임의의 $e>0$ 에 대하여 $|\alpha (N_e) - \beta (N_e)| \leq 2e$ 가 성립하므로 $e$ 가 $0$ 과 극도로 가까울 때에도 $|\alpha (N_e) - \beta (N_e)|$ 이 그것보다 같거나 작다는 것이므로 $|\alpha (N_e) - \beta (N_e)| = 0$ 이어야 한다. 왜냐하면 $|\alpha (N_e) - \beta (N_e)| = \epsilon > 0$ 이라면 그것보다 작은 유리수 $e$ 가 존재하여 모순을 발생시키기 때문이다. 그러므로 $(1)$ 을 사실상 $|\alpha (i) - \beta (i)| < 2e$ 로 쓸 수 있으므로*)
    
    $(1)$ 에 의하여 

    $$ i \geq N_e \implies |\alpha (i) - \beta (i)| \leq |\alpha (N_e) - \beta (N_e)| + 2 e \leq 4e <5e $$

    이다. 

    (*근데 그렇게 따지면 $|\alpha (i) - \beta (i)| \leq |\alpha (N_e) - \beta (N_e)| + 2 e$  가 아니라 $|\alpha (i) - \beta (i)| < |\alpha (N_e) - \beta (N_e)| + 2 e$ 이어야 하지 않나? 어쨌든..*)
    
    그러므로 $\alpha \sim \beta$ 가 되어 

    $$ [\alpha ] = [\beta ] $$

    이다. ■ 

## 실수의 덧셈

!!! tldr "실수 덧셈"

    기본열 $\alpha + \beta: i \mapsto \alpha (i) + \beta (i)$ 와 $[\alpha], [\beta] \in \R$ 에 대하여 다음과 같이 정의한다.

    $$ [\alpha ]+ [\beta ]=[\alpha + \beta ] $$

- $\alpha + \beta$ 는 기본열이다. 즉, 코시 수열의 덧셈은 닫혀있다.

!!! tldr ""

    기본열 $\alpha$ 에 대하여 $(-\alpha )(i) = - \alpha (i)$ 로 정의된 유리수열 $-\alpha$ 는 기본열이다. 
    
    또한 $[-\alpha]$ 는 $[\alpha]$ 의 더하기의 역원이다.

- 증명 

!!! tldr ""

    실수의 더하기는 잘 정의되어 있고, 결합법칙과 교환법칙을 만족한다. 

- 증명 

!!! tldr ""

    $[0 ^{*}]$ 은 실수 덧셈의 항등원이다. 

- $0 ^{*}$ 은 기본열의 정의에서 살펴본 것처럼 

    $$ 0 ^{*}(i) = 0 $$

    으로 이해하면 된다.

- 증명 

## 실수의 곱셈

!!! tldr "실수 곱셈"

    기본열 $\alpha \beta: i \mapsto \alpha (i) \beta (i)$ 와 $[\alpha] , [\beta] \in \R$ 에 대하여 다음과 같이 정의한다.

    $$ [\alpha ][\beta ]= [\alpha \beta ] $$

!!! tldr ""

    실수의 곱셈은 닫혀있다. 즉, 기본열 $\alpha , \beta$ 에 대하여 $\alpha \beta$ 도 기본열이다.

- 증명 

    [정리 2.4.1](#1d4f8ca83) 에 의하여 $i \in \N$ 에 대하여 

    $$ |\alpha (i)| \leq M_1, |\beta (i)| \leq M_2 $$

    인 $M_1, M_2 \in \mathbb{Q}$ 가 존재한다. 이때 $M = \sup \{M_1, M_2\}$ 라 두면

    $$ i,j \geq N_1 \implies |\alpha (i) - \alpha (j)| < \dfrac{e}{2M} $$

    $$ i,j \geq N_2 \implies |\beta (i) - \beta (j)| < \dfrac{e}{2M} $$

    인 $N_1, N_2 \in \N$ 가 존재한다. 이때 $N = \sup \{N_1, N_2\}$ 라 두면 임의의 $i, j \geq N$ 에 대하여 

    $$ |\alpha (i)\beta (i) - \alpha (j)\beta (j)| \leq |\alpha (i)\beta (i) - \alpha (i)\beta (j)| + |\alpha (i)\beta (j) - \alpha (j)\beta (j)| $$

    인데(*$\because$ [정리 2.2.2](#84983902d) 에 의하여*), 

    $$ = |\alpha (i)||\beta (i) - \beta (j)| + |\beta (j)||\alpha (i)-\alpha (j)| $$

    (*에서 $|\alpha (i)|$ 와 $|\beta (i)|$ 의 상한이 $M$ 이므로*)

    $$ < M \dfrac{e}{2M} + M \dfrac{2}{2M} = e $$

    이다. 그러므로 $\alpha \beta$ 는 기본열이다.

!!! tldr ""

    실수의 곱셈은 결합법칙, 교환법칙, 분배법칙을 만족한다.
    
- 증명

!!! tldr ""

    실수의 곱셈은 항등원 $[1 ^{*}]$ 을 가진다. 

- 증명
    
!!! tldr ""

    실수의 곱하기는 역원을 가진다. 

- 증명 

    $[a] \neq 0 ^{*}$ 이면 [정리 2.4.2](#66a655b45) 에 의하여 $[\alpha ] > 0 ^{*}$ 또는 $[\alpha ] < 0 ^{*}$ 이 둘 중 하나만 성립한다. 그러므로 적당한 유리수 $d>0$ 와 $N_1 \in \N$ 에 대하여 

    $$ i \geq N_1 \implies \alpha (i) > d $$

    과 

    $$ i \geq N_1 \implies \alpha (i) < -d $$

    중 하나만 성립한다. 이때 기본열의 유한개의 항을 바꿔도 (*어차피 그것의 무한항이 근사되는 값은 바뀌지 않고 결국*) 그 동치류도 변하지 않으므로 그냥 

    $$ \forall i \in \N, \alpha (i) \neq 0 $$

    라고 가정해도 좋다. 이제 

    $$ \beta : i \mapsto \dfrac{1}{\alpha (i)} : \N \to \mathbb{Q} $$

    라는 유리수열을 정의하자. $\beta$ 가 기본열임을 보이면 

    $$ [\alpha ][\beta ] = 1 ^{*} $$

    임은 자명하기에 모든 증명이 끝난다. 먼저 $e \in P _{\mathbb{Q}}$ 에 대하여 

    $$ i \geq N_2 \implies |\alpha (i) - \alpha (j)| < d ^{2}e $$

    인 $N_2 \in \N$ 가 존재한다. 이때 $N = \sup \{N_1,N_2\}$ 라고 하자. 그러면 임의의 $i \geq N_1$ 에 대하여 $|\alpha (i)| > d$ 이므로 임의의 $i, j \geq N$ 에 대하여 

    $$ |\beta (i) - \beta (j)| = \bigg |\dfrac{1}{\alpha (i)} - \dfrac{1}{\alpha (j)}\bigg | = \dfrac{1}{|\alpha (i)\alpha (j)|}|\alpha (i) - \alpha (j)| < \dfrac{1}{d ^{2}}d ^{2}e = e $$

    이다. 그러므로 $\beta$ 는 기본열이다. ■ 

## 실수는 순서체이다

!!! tldr ""

    $\R$ 은 순서체이다.

- 지금까지의 정리들을 기반으로 $P _{\R} = \{[\alpha ] \in \R : [\alpha ] > 0 ^{*}\}$ 라 두면 순서체의 조건이 모두 성립한다.

## 실수의 성질

!!! tldr "정리 2.4.3"

    $[\alpha ], [\beta ] \in \R$ 가 $[\alpha ]>[\beta ]$ 이면 다음을 만족하는 유리수 $r \in \mathbb{Q}$ 가 존재한다. 

    $$ [\alpha ] > [r ^{*}] > [\beta ] $$

- 이 성질을 조밀성(density)이라 한다.

- 증명 

    관계 

    $$ i \geq N_1 \implies \alpha (i) - \beta (i) > d $$

    가 성립하는 $N_1 \in \N$ 과 $d > 0$ 인 $d \in \mathbb{Q}$ 가 존재한다. 또한 

    $$ i,j \geq N_2 \implies |\alpha (i) - \alpha (j)| < \dfrac{1}{4}d, \quad |\beta (i) - \beta (j)| < \dfrac{1}{4}d $$

    이 성립하는 $N_2 \in \N$ 가 존재한다. 이때 $N = \sup \{N_1,N_2\}$ 라 두자. 만일 $i \geq N$ 이면 

    $$ \alpha (i) - \bigg (\alpha (N) - \dfrac{1}{2}d\bigg ) = \dfrac{1}{2}d + (\alpha (i) - \alpha (N)) > \dfrac{1}{4}$$

    이므로 (*$-\dfrac{1}{4}d < \alpha (i) - \alpha (j) < \dfrac{1}{4}d$ 에서 $\alpha (i) - \alpha (j) > - \dfrac{1}{4}d$ 이기 때문.*) 

    $$ [\alpha ] > \bigg (\alpha (N) - \dfrac{1}{2}d\bigg ) ^{*} $$

    이다(*임의의 $i \geq N$ 에 대하여 기본열 $\alpha (i)$ 의 무한항의 근사가 기본열 $\bigg (\alpha (N) - \dfrac{1}{2}d\bigg )$ 의 무한항의 근사보다 크다는 사실이 도출되었기 때문*). 

    또한 $i \geq N$ 에 대하여 

    $$ \bigg (\alpha (N) - \dfrac{1}{2}d\bigg ) - \beta (i) = (\alpha (N) - \beta (N)) + (\beta (N) - \beta (i)) - \dfrac{1}{2}d $$

    $$ > d - \dfrac{1}{4}d - \dfrac{1}{2}d = \dfrac{1}{4}d $$

    이므로 

    $$  \bigg (\alpha (N) - \dfrac{1}{2}d\bigg ) ^{*} > [\beta ] $$

    이다. 그러므로 $\alpha (N) - \dfrac{1}{2}d \in \mathbb{Q}$ 가 존재함을 증명하고자 했던 유리수이다. ■ 

!!! tldr ""

    부분 수열(subsequence) : $\forall k \in \{0, 1, 2, \dots\}$ 에 대하여 $i(k) < i(k+1)$ 인 함수 $i : \N \to \N$ 와 수열 $x : i \mapsto x(i)$ 의 합성 

    $$ x \circ i : k \mapsto x(i(k)) $$

    를 $x$ 의 부분 수열이라 한다.

- 순서체 $F$ 의 수열 $x$ 가 $a \in F$ 로 수렴하면, $x$ 의 모든 부분수열도 $a$ 로 수렴함은 자명하다.

!!! tldr "도움정리 2.4.4"

    순서체 $F$ 의 코시 수열 $x$ 의 한 부분수열 $x \circ i$ 가 $a \in F$ 로 수렴하면 $x$ 도 $a \in F$ 로 수렴한다.

- 증명 

    $\forall e \in P _{F}$ 에 대하여 

    $$ i,j \geq N \implies |x(i) - x(j)| < \dfrac{e}{2} $$

    가 성립하는 $N \in \N$ 이 존재한다. 또한 

    $$ k \geq K \implies |x(i(k)) - a| < \dfrac{e}{2}, \qquad i(K) \geq N $$

    이 성립하는 $K \in \N$ 가 존재한다. 이제 $i \geq i(K)$ 이면 

    $$ |x(i) - a| \leq |x(i) - x(i(K))| + |x(i(K)) - a| < \dfrac{e}{2} + \dfrac{e}{2} = e $$

    이 되어 $x$ 가 $a$ 로 수렴함을 알 수 있다. ■ 

!!! tldr "정리 2.4.5"

    $n \in \N, [ \alpha _n] \in \R$ 에 대하여 $n \mapsto [\alpha _n]$ 을 $\R$ 의 코시수열이라고 하면, 이 수열은 $\R$ 에서 수렴한다.

- 유리수의 코시수열이 항상 $\mathbb{Q}$ 에서 수렴하는 것이 아니라 무리수에서도 수렴하여 새로운 수체계 $\R$ 이 정의되었다. 하지만 실수의 코시수열은 그렇지 않고 항상 실수 내부에서 수렴한다는 것을 말해주는 정리이다. 

- 증명 

    우선 $[\alpha _n] \neq [\alpha _{n+1}]$ 라고 하면 [정리 2.4.2](#66a655b45) 에 의하여 $[\alpha _n]$ 과 $[\alpha _{n+1}]$ 사이의 유리수 $r(n) \in \mathbb{Q}$ 가 존재한다. 이때

    $$ |[\alpha _n] - [r(n)^{*}]|<|[\alpha _n]-[\alpha _{n+1}]| $$

    이므로 임의의 양의 실수 $[ \epsilon ] > 0$ 에 대하여 

    $$ n \geq N \implies |[\alpha _n] - [r(n) ^{*}]| < \dfrac{1}{3}[\epsilon] \tag{1} $$

    이 성립하는 $N \in \N$ 이 존재한다.(*이것은 기본열 $\alpha_n$ 의 $n$ 번째 항과 $n+1$ 번째 항 사이에 반드시 어떤 유리수가 존재하고, 그러므로 어떤 실수를 나타내는 실수 수열 $[\alpha _n]$ 과 또 실수 수열 $r(n)^{*}$ 의 무한항의 차이값이 $0$ 으로 근사된다는 의미이다.*)

    한편 $0 < [ \epsilon ]$ 이므로 적당한 자연수 $I_0$ 과 유리수 $d>0$ 에 대하여 

    $$ i \geq I_0 \implies \dfrac{1}{3}\epsilon (i) > d \tag{2} $$

    이 성립한다.(*이떄의 $\epsilon (i)$ 는 $\alpha_n$ 의 $i$ 번째 항에 해당하는 $\epsilon$ 의 값인 것 같다. 아닌가?*)

    이때 유리수열 $n \mapsto r(n)$ 이 기본열임은 자명하므로 

    $$ i, j \geq M \implies |r(i) - r(j)| < d \tag{3} $$

    이 성립하는 자연수 $M \in \N$ 이 존재한다. 이때 $(1)$ 의 자연수 $n \geq N$ 에 대하여 

    $$ i \geq I(n) \implies |\alpha_n(i) - r(n)| < \dfrac{1}{3}\epsilon (i) \tag{4} $$

    이 성립하는 자연수 $I(n)$ 이 존재한다.(*이는 $(1)$ 에서 결정된 자연수 $n \geq N$ 으로 결정된 실수의 기본열 $\alpha _n(i)$ 가 기본열 $r(n)$ 과 또 다시 내부적으로 무한히 가깝게 근사된다는 말이다.*)

    이제 $n \geq \sup \{N, M\}$ 인 $n \in \N$ 을 선택하면, 각 $i \geq \sup \{I_0, I(n), M\}$ 에 대하여 [정리 2.2.2](#84983902d) 에 의하여 

    $$ |\alpha _n(i) - r(i)| \leq |\alpha _n -r(n)| + |r(n) - r(i)| $$

    인데 이때 $(3), (4)$ 에 의하여 

    $$ |\alpha _n -r(n)| + |r(n) - r(i)| < \dfrac{1}{3}\epsilon (i) + d $$

    이고, 다시 $(2)$ 에 의하여

    $$  \dfrac{1}{3}\epsilon (i) + d < \dfrac{1}{3}\epsilon (i) + \dfrac{1}{3}\epsilon (i) = \dfrac{2}{3} \epsilon (i) $$

    이므로 최종적으로 

    $$ |\alpha _n(i) - r(i)| \leq \dfrac{2}{3}\epsilon (i) $$

    을 얻는다. 따라서 각 $n \geq \sup \{N, M\}$ 에 대하여 

    $$ |[\alpha _n] - [r]| \leq \dfrac{2}{3}[\epsilon ] < [\epsilon ] $$

    이므로 실수 수열 $\big <[\alpha _n]\big >$ 은 실수 $[r]$ 로 수렴한다. ■ 

# 완비순서체 

!!! tldr "완비순서체(completeness ordered field) 또는 실수의 완비성 공리(completeness axiom of the real numbers)"

    완비순서체 $F$ 는 다음 동치 조건을 만족하는 순서체이다.

    1. $A \neq \varnothing$ 인 집합 $A \subset F$ 가 위로 유계이면 상한을 가진다.

    2. $A \neq \varnothing$ 인 집합 $A \subset F$ 가 아래로 유계이면 하한을 가진다.

    3. 임의의 코시 수열 $x: \N \to F$ 가 $F$ 안에서 수렴한다. 

- [정리 2.3.2](#febb2f17d) 는 데데킨트 절단으로 정의된 실수체 $\R$ 이 완비순서체임을 말해준다.

    또한 아래 증명을 통해 코시 수열로 구성한 실수체도 완비순서체임이 증명된다. 

- 이것을 완비성이라고 한다. 완비성이란 쉽게 말해서 완비성을 갖는 집합의 원소로 수직선을 빈틈없이 채울 수 있다라는 것이다. 유리수는 조밀하지만, 완비적이지는 않다. 하지만 실수는 완비적이어서 좌표계를 메꿔질 구멍이 없이 채우는 것이 가능하다.

    어떤 집합이 갖는 완비성이라는 성질을 그냥 완비성이 아니라 굳이 "실수의" 완비성 이라고 하는 이유가 완비성이라는 성질을 갖는 집합이 실수체밖에 없기 때문이다.

- 실수가 완비적이라는 것은 증명할 필요가 없는 공리이다.

- 2) 가 1) 과 동치임은 자명하다.

- 3) 을 만족하는 순서체는 완비순서체이다. 이는 조건 3) 으로부터 조건 1) 이 도출됨을 뜻한다.

    - 증명 

        이제 아르키메데스의 성질과 3) 을 가정하고 1) 을 도출함으로써 코시 수열로 구성한 실수체가 완비순서체임을 보이자. 이를 위하여 순서체 $F$ 의 비어 있지 않은 부분집합 $A \subset F$  가 위로 유계라고 하자(*이는 완비순서체의 조건 1) 의 조건절 "위로 유계이면" 으로부터 귀결절 "상한을 가진다" 를 이끌어내야 하기 때문에 조건절을 가정하는 것이다.*). 그리고 

        $$ \mathcal{I} = \{(a, b) \in F \times F : a < b\} $$

        에 대하여 두 함수 $g,h: \mathcal{I} \to F$ 를 

        $$ g((a, b)) = \begin{cases} a & \dfrac{a+b}{2} \text{ 가  } A \text{ 의 상계이다 }\\ \dfrac{a+b}{2} & \dfrac{a+b}{2} \text{ 가  } A \text{ 의 상계가 아니다 }\end{cases} $$ 
        
        $$ h((a, b)) = \begin{cases} \dfrac{a+b}{2} & \dfrac{a+b}{2} \text{ 가  } A \text{ 의 상계이다 }\\ b & \dfrac{a+b}{2} \text{ 가  } A \text{ 의 상계가 아니다 }\end{cases} $$

        로 정의하면, 

        $$ a \leq g((a, b)) < h((a, b)) \leq b, \qquad h((a, b)) - g((a, b)) = \dfrac{1}{2}(b-1) $$

        이다.(*그냥 각 함수가 $g((a,b))=a, h((a,b))=\dfrac{a+b}{2}$ 일 때와 $g((a,b))=\dfrac{a+b}{2}, h((a,b)) = b$ 일 때를 따져보면 된다.*)

        또한 $a$ 가 $A$ 의 상계가 아니고, $b$ 가 $A$ 의 상계라고 하자. (*이때 $\dfrac{a+b}{2}$ 가 $A$ 의 상계일 경우 $g((a,b)) = a$ 이므로 $g((a,b))$ 는 $A$ 의 상계가 아니고, $h((a,b)) = \dfrac{a+b}{2}$ 는 $A$ 의 상계이다. 한편 $\dfrac{a+b}{2}$ 가 $A$ 의 상계가 아닐 경우 $g((a,b)) = \dfrac{a+b}{2}$ 는 $A$ 의 상계가 아니고, $h((a,b)) = b$ 는 $A$ 의 상계이다.*) 그러면 어느 경우든 $g((a,b))$ 는 $A$ 의 상계가 아니고, $h((a,b))$ 는 $A$ 의 상계이다. 그렇다면 $A$ 의 상계가 아닌 첫째 입력과 $A$ 의 상계인 둘째 입력을 받았을 때 함수 $g, h$ 의 성질은 다음과 같다.

        1. $g((a,b))$ 는 $A$ 의 상계가 아니고, $h((a,b))$ 는 $A$ 의 상계이다.

        2. $a \leq g((a, b)) < h((a, b)) \leq b$ 
        
        3. $h((a, b)) - g((a, b)) = \dfrac{1}{2}(b-1)$

        <br/>

        이제 함수 $f: \mathcal{I} \to \mathcal{I}$ 를 

        $$ f:(a,b) \mapsto (g((a,b)), h((a,b))) \tag{1}  $$

        로 정의하자. 이때 $A$ 의 원소가 $1$개면 증명할 것이 없으므로(*왜냐하면 $A$ 의 원소가 하나이면 자동적으로 유계이며, 상한을 가지기 때문에 완비순서체의 조건 3) 에서 1) 을 바로 도출할 수 있기 때문이다.*), $A$ 의 원소가 $2$ 개 이상이라고 하자. 그러면 $A$ 의 상계가 아닌 $a_0 \in A$ 와 $A$ 의 상계 $b_0$ 가 존재한다. 그러면 [정리 2.1.2](#3a99b431b) 를 적용하여 
        
        $$\gamma (0) = (a_0, b_0), \qquad \forall n \in \N, \gamma (n ^{+}) = f(\gamma (n))\tag{2}$$
        
        인 유일하게 존재하는 함수 $\gamma : \N \to \mathcal{I}$ 를 정의할 수 있다. 이제 두 함수 $\pi _1, \pi _2 : \mathcal{I}\to F$ 를 $(a, b) \in \mathcal{I}$ 에 대하여

        $$ \pi _1 : (a,b) \mapsto a, \quad \pi _2:(a,b) \mapsto b \tag{3} $$

        라고 정의하자. 그리고 
        
        $$\alpha  = \pi _1 \circ \gamma , \beta = \pi _2 \circ \gamma \tag{4} $$
        
        라 두면 (*수열의 정의에 의하여*) $\alpha , \beta$ 는 $F$ 의 수열이 되며, (*정의 $(1), (2), (3), (4)$ 과 $\gamma (n) = (a_n,b_n)$ 일 때 $a_n = (\pi _1 \circ \gamma )(n) = \alpha (n), b_n = (\pi _2 \circ \gamma )(n) = \beta (n)$ 인 것에 의하여*)

        $$ \alpha (n ^{+}) = (\pi _1 \circ \gamma )(n ^{+}) = (\pi _1 \circ f)(\gamma (n)) = g(\gamma (n)) = g((\alpha (n), \beta (n))) $$

        $$ \beta (n ^{+}) = (\pi _2 \circ \gamma )(n ^{+}) = (\pi _2 \circ f)(\gamma (n)) = h(\gamma (n)) = h((\alpha (n), \beta (n))) $$

        이 된다. $\alpha, \beta$ 함수에 대해서는 $A$ 의 상계가 아닌 $a_0$ 와 $A$ 의 상계 $b_0$ 에 대하여 초깃값이

        $$ \alpha (0) = \pi _1 \circ \gamma (0) = a_0 , \quad \beta (0) = \pi _2 \circ \gamma (0) = b_0 $$

        이므로 $\alpha (0), \beta (0)$ 는 각각 $A$ 의 상계가 아닌 원소와 상계인 원소를 뜻하는데, 이후에는 $\forall n \in \N \setminus \{0\}$ 에 대하여 

        $$ \alpha (n ^{+}) = g((\alpha (n), \beta (n))) , \quad \beta (n ^{+}) = h((\alpha (n), \beta (n))) $$

        이므로 위에서 첫번째 입력이 상계가 아니고, 두번째 입력이 상계일 때 도출해내었던 함수 $g, h$ 의 성질을 $\alpha ,\beta$ 함수가 그대로 갖게 된다. 그러므로 $n \in \N$ 에 대하여 

        1. $\alpha (n)$ 은 $A$ 의 상계가 아니고, $\beta (n)$ 은 $A$ 의 상계이다.

        2. $\alpha (n) \leq \alpha (n ^{+}) < \beta (n ^{+}) \leq \beta (n)$

        3. $\beta (n ^{+}) - \alpha (n ^{+}) = \dfrac{1}{2}(\beta (n) - \alpha (n))$

        가 성립한다. 이때 아르키메데스의 성질에 의하여 $\forall e \in P _{F}$ 에 대하여 $e \cdot N \geq \beta (0) - \alpha (0)$ 인 자연수 $N$ 이 존재하므로 

        $$ N \geq \dfrac{1}{e}[\beta (0) - \alpha (0)] $$

        이다. 이때 위의 성질 a), b), c) 와 $\forall n \in \N, \dfrac{1}{2 ^{n}} \leq \dfrac{1}{n}$ 인 것에 의하여, 각 $m > n \geq N$ 에 대하여

        $$ 0 \leq  \alpha (m) - \alpha (n) < \beta (n) - \alpha (n) = \dfrac{1}{2 ^{n}}[\beta (0) - \alpha (0)] \leq \dfrac{1}{n}[\beta (0) - \alpha (0)] $$

        인데, $e \geq \dfrac{1}{N} [\beta (0) - \alpha (0)] > \dfrac{1}{n} [\beta (0) - \alpha (0)]$ 이므로 

        $$ \dfrac{1}{n}[\beta (0) - \alpha (0)] < e $$

        이다. 그러므로 $\alpha (m) - \alpha (n) < e$ 에서 $\alpha: \N \to F$ 는 코시 수열이고, 마찬가지로 $\beta$ 도 코시 수열임을 알 수 있다. 

        그런데 완비순서체의 조건 3) 에 의하여 $\alpha , \beta$ 가 수렴함을 알 수 있으므로 각각의 극한값을 $a, b$ 라고 두자. 그러면 성질 c) 는 $\alpha$ 와 $\beta$ 의 차이값이 항이 높아질수록 $1/2$ 된다는 것을 말하고 있으므로 $n \to \infty \implies \beta_n - \alpha_n \to 0$ 이 됨을 알 수 있다. 이는 결국 $a = b$ 임을 뜻한다.

        한편 a) 에 의하여 $\forall x \in A, n \in \N$ 에 대하여 $x \leq \beta (n)$ 이므로 $x \leq b$ 이고, 이에 따라 $b$ 는 $A$ 의 상계이다. 한편 $e>0$ 이면 $\exists  n \in \N \text{ s.t. }\ a - e < \alpha (n) \leq  a = b$ 인데, $\alpha (n)$ 이 $A$ 의 상계가 아니므로 $\exists y \in A \text{ s.t. }\  \alpha (n) < y$ 이다. 그러면 $a - e < y$ 이므로 $a-e$ 는 $A$ 의 상계가 아니다. 그런데 $a=b$ 가 $A$ 의 상계라고 하였고 $e$ 는 임의의 양수이므로 $a = b$ 는 최소상계이다. 왜냐하면 아무리 작은 $e$ 에 의하여 $a-e$ 를 결정해도 그것은 상계가 아니기 때문이다. 

        그렇다면 $A$ 가 상한을 가짐이 증명되었으므로 우리는 방금 완비순서체의 조건 3) 으로부터 1) 을 도출했다. ■ 

- 조건 1) 으로부터 조건 3) 이 도출된다.

    - 증명 

        순서체 $F$ 의 코시 수열 $\alpha : \N \to F$ 가 존재할때 [도움정리 2.4.4](#3a5110cb6) 에 의하여 수열 $\alpha$ 가 수렴하는 부분수열을 가짐을 증명하면 된다. 

        $A = \{\alpha (n) : n \in \N\}$ 이 유한집합이면 간단하고, $A$ 가 무한집합이면 [정리 2.4.1](#1d4f8ca83) 에 의하여 $A$ 는 위로 유계이고 아래로 유계이이다. 그러면 집합 $A$ 의 하계 $a_0$ 와 상계 $b_0$ 를 택하고 조건 1) 에서 3) 을 도출했을 때처럼 구간을 반으로 계속 분할해 나가는데, $A$ 의 원소가 무한개 속하는 쪽을 계속 선택한다. 

        그러면 이 구간들의 왼쪽 끝점의 집합은 유계이고 조건 1) 을 가정했으므로 상한 $a$ 를 가진다. 또한 구간들의 오른쪽 끝점들의 집합은 아래로 유계이므로 조건 1) 과 동치인 2) 에의하여 하한 $b$ 를 가진다. 

        그러면 3) 에서 1) 을 도출했을 때처럼 $a=b$ 가 되고 이 원소 근방에는 무한히 많은 $A$ 의 원소가 있으므로 $A$ 의 원소를 계속 택하여 수열을 만들어 $a$ 로 수렴하게 할 수 있다. 이 수열이 우리가 원하던 원래 $\alpha$ 의 수렴하는 부분수열이 된다. ■ 

!!! tldr "정리 2.5.1"

    완비순서체 $F$ 는 아르키메데스의 성질을 만족한다. 

- 증명 

    집합 $\N \subset F$ 이 위로 유계라고 가정하면, 완비순서체의 조건 1) 에 의하여 $\N$ 의 최소상계 $\alpha \in F$ 가 존재한다. (*이 $\alpha$ 가 자연수라는 보장은 없다. 오히려 자연수가 아니라고 생각해야 모순이 없을듯.*)

    그러면 $\alpha -1 < \alpha$ 이므로 $\alpha -1$ 는 $\N$ 의 상계가 아니다. 그렇다면 (*$\alpha -1$ 보다 큰 자연수가 존재한다는 말이므로*)

    $$ \exists n \in \N \text{ s.t.  }\  \alpha -1<n \leq \alpha $$

    이다. 그러면 (*페아노 공리계의 공리 2) 에 의하여*)

    $$ n + 1 \in \N $$

    임에도 불구하고 

    $$ \alpha -1 < n \iff n+1 > \alpha $$

    이므로 $\alpha$ 가 $\N$ 의 상계라는 것에 모순이다. 그러므로 $\N$ 은 위로 유계가 아니다. ■ 

!!! tldr "정리 2.5.2"

    완비순서체 $F$ 의 두 원소 $x, y \in F$ 가 $x < y$ 이면 

    $$ x<r<y $$

    를 만족하는 유리수 $r \in \mathbb{Q} \subset F$ 이 존재한다.

- 이것을 조밀성(dense)라고 한다. 유리수가 조밀하다 라는 것은 어떤 두 유리수 사이에 반드시 또 다른 유리수가 존재하다는 것이다. 

    그러나 완비순서체의 유일성 증명에서 살펴보는 바와 같이 유리수는 완비적이지는 않다. 즉, 유리수로는 좌표계를 메꿔질 구멍이 없이 채우는 것이 불가능하다.

    - 증명 

        유리수 집합 $\mathbb{Q}$ 가 조밀하면서, 완비적이라고 가정하자. 유리수 집합으로 완비성을 다시 따져보면 다음과 같다. 

        "순서체 $\mathbb{Q}$ 가 다음 조건을 만족하면 완비순서체이다. $A \neq \varnothing$ 인 $A \subset \mathbb{Q}$ 가 위로 유계이면 상한을 가진다."
        
        $A \subset \mathbb{Q}$ 를 $A = \{x \in \mathbb{Q} : x < \sqrt[]{2}\}$ 라고 정의하면 $A$ 는 $A \neq \varnothing$ 이고 위로 유계이다. 그러면 완비성의 조건 에 의하여 상한 $\sup A \in \mathbb{Q}$ 이 존재한다. $\sup A$ 는 유리수이므로 $\sup A \neq \sqrt[]{2}$ 이다. 그러면 $\sup A > \sqrt[]{2} \lor \sup A < \sqrt[]{2}$ 이다. 

        그런데 $\sup A > \sqrt[]{2}$ 일 경우 본 정리에 의하여 $\exists r \in \mathbb{Q} \text{ s.t. }\  \sqrt[]{2} < r < \sup A$ 이므로 $\sup A$ 가 최소상계라는 것에 모순이고, $\sup A < \sqrt[]{2}$ 일 경우 다시 본 정리에 의하여 $\exists r \in \mathbb{Q} \text{ s.t. }\  \sup A < r < \sqrt[]{2}$ 이므로 상계보다 큰 원소가 존재하여 모순이다. 

        그러므로 $\sup A = \sqrt[]{2} \in \mathbb{Q}$ 인데 실제로는 $\sqrt[]{2} \not \in \mathbb{Q}$ 이므로 모순이다. 그러므로 유리수 집합 $\mathbb{Q}$ 는 완비적이지 않다. ■ 

- 증명

    $x = 0$ 이면 [정리 2.5.1](#1963be39a) 와 [정리 2.2.4](#59122b0d2) 를 적용하면 된다. $\blacktriangle$ 

    이제 $0<x<y$ 라고 하면 다시 [정리 2.5.1](#1963be39a) 에 의하여 

    $$ n \in \N \text{ s.t.  }\  0 < \dfrac{1}{n} < y - x $$

    이다. 이때 $\dfrac{1}{n} \in P _{F}$ 와 $x \in P _{F}$ 에 대하여 [정리 2.5.1](#1963be39a) 를 또 적용하면 

    $$ \{k \in \N : k \cdot \dfrac{1}{n} > x \} \neq \varnothing $$

    이다. 그러면 [정리 2.1.4](#5efd87f3f) 에 의하여 이 집합은 최솟값을 갖는데, 이 최솟값을 $m$ 이라 두면 

    $$ \dfrac{m-1}{n} \leq x < \dfrac{m}{n} $$

    이고, 이에 따라 

    $$ x < \dfrac{m}{n} = \dfrac{m-1}{n} + \dfrac{1}{n} \leq x + \dfrac{1}{n} < y $$

    이다. 그러므로 $\dfrac{m}{n}$ 이 바로 $x$ 와 $y$ 사이에 있는 유리수이다. $\blacktriangle$ 

    $x<0$ 일 때는 $\exists n \in \N \text{ s.t.  }\ -x<n$ 이므로 

    $$ 0 < x + n < y + n $$

    인데, 방금 증명했듯이 
    
    $$ \exists r \in \mathbb{Q} \text{ s.t.  }\  x + n < r < y + n$$

    이다. 그러므로 $r-n$ 이 $x$ 와 $y$ 사이에 있는 유리수이다. ■ 

!!! tldr "2.33"

    순서체 $F$ 의 부분집합 $S, T \subset F$ 에 대하여 

    $$ S + T = \{s + t \in F : s \in S, t \in T\} $$

    라고 정의했을 때 

    $$ \sup (S+T) = \sup S + \sup T $$

    이다. 

- 증명

    $\sup S = \alpha , \sup T = \beta$ 라 두자. 그러면 일단 $\forall s \in S, \forall t \in T$ 에 대하여 $s + t \leq \alpha + \beta$ 이므로 $\alpha + \beta$ 는 $S+T$ 의 상계이다.

    이제 $\alpha + \beta$ 가 최소상계임을 보이기 위하여 $\gamma < \alpha + \beta$ 이면 $\gamma$ 가 $S+T$ 의 상계가 아님을 보이려 한다. 즉, $\gamma < \alpha + \beta$ 이면 $\gamma < s+t$ 인 $s \in S$ 와 $t \in T$ 가 존재함을 보이는 것이다.

    이제 $\epsilon = \alpha + \beta - \gamma$ 라 두면 $\epsilon > 0 \implies \dfrac{\epsilon }{2} > 0$ 이고, 따라서 $\alpha - \dfrac{\epsilon }{2} < \alpha$ 인데 $\alpha$ 는 $S$ 의 최소상계이므로 $\alpha - \dfrac{\epsilon }{2}$ 는 $S$ 의 상계가 아니다. 그러므로 $\exists   s \in S \text{ s.t. }\ \alpha - \dfrac{\epsilon }{2} < s$ 이다. 마찬가지로 $\exists t \in T \text{ s.t. }\ \beta - \dfrac{\epsilon }{2} < t$ 이다. 그러면 

    $$ \gamma  = \alpha +\beta -\epsilon = \bigg (\alpha - \dfrac{\epsilon }{2}\bigg ) + \bigg (\beta - \dfrac{\epsilon }{2}\bigg ) < s + t $$

    인데, 이 $s \in S, t \in T$ 가 존재성을 보이려 했던 것들이므로 증명이 끝났다. ■ 

!!! tldr "2.34"

    순서체 $F$ 의 부분집합 $S, T \subset P _{F}$ 에 대하여 

    $$ ST = \{st \in P _{F} : s \in S, t \in T\} $$

    라고 정의했을 때 

    $$ \sup ST = \sup S \sup T $$

    이다.

- 증명

## 최종결론

!!! tldr "정리 2.5.3"

    임의의 두 완비순서체 $F, G$ 가 주어지면 전단사 함수 $f: F \to G$ 가 존재하여 다음을 만족한다.

    1. $\forall x,y \in F: f(x+y)=f(x)+f(y), f(xy)=f(x)f(y)$

    2. $f(P _{F}) = P _{G}$

- 이 정리는 완비순서체가 유일하게 존재함을 말한다. 즉, 완비순서체는 본질적으로 단 하나만 존재하고, 그것이 실수체 $\R$ 이라는 것이다. 만약 완비순서체의 조건을 만족하는 다른 체가 정의된다면, 그 체와 $\R$ 사이에 일대일 대응과 연산의 대응관계 같은 모든 구조를 그대로 보존하는 사상이 존재한다. 따라서 이 정리를 다음과 같이 이해하면 더욱 그 의미가 분명해질 것이다.

    임의의 완비순서체 $F$ 가 주어지면 동형사상 $f: F \to \R$ 가 존재하고 $f(P _{F}) = P _{\R}$ 를 만족한다. 

- 또한 이 정리로써 데데킨트 절단으로 구성한 실수체와 코시 수열로 구성한 실수체가 모두 완비순서체였고, 결국 이들은 본질적으로 같은 순서체임을 알 수 있다. 

- 증명

    [정리 2.2.3](#46891c9a2) 에 의하여 

    $$ \begin{equation}\begin{split} & \gamma (r+s) = \gamma (r) + \gamma (s), \quad \gamma (rs) = \gamma (r)\gamma (s), \quad \gamma (P _{\mathbb{Q}}) = \gamma (\mathbb{Q})\cap P _{F}\\ &\delta (r+s) = \delta (r) + \delta (s), \quad \delta (rs) = \delta (r)\delta (s), \quad \delta (P _{\mathbb{Q}}) = \delta (\mathbb{Q})\cap P _{G} \end{split}\end{equation} \tag{1} $$

    을 만족하는 단사함수 

    $$ \gamma : \mathbb{Q} \to F, r \mapsto r \cdot 1_F $$
    
    $$ \delta : \mathbb{Q} \to G, r \mapsto r \cdot 1_G $$

    가 존재한다. 이제 각 $x \in F$ 에 대하여 

    $$ A_x = \{\delta (r) \in G : r \in \mathbb{Q}, \gamma (r) < x\} $$

    라 정의하면 [정리 2.5.1](#1963be39a) 에 의하여 완비순서체 $F$ 에 대하여 

    $$ \exists n \in \N \text{ s.t. }\  n \cdot 1_F > -x $$

    이고, 이는 $\gamma (-n) = (-n) \cdot 1_F < x$ 를 뜻하므로 (*$\delta (-n) \in A_x$ 에서*) $A_x \neq \varnothing$ 이다. 

    다시 아르키메데스의 법칙으로 $m \cdot 1_F > x$ 인 $m \in \N$ 가 존재하는데, 이 $m$ 에 대하여 

    $$ \delta (m) = m \cdot 1_G $$

    는 $\gamma (m) = m \cdot 1_F > x$ 이므로 $A_x$ 의 상계이다. 그러면 $A_x$ 는 위로 유계이고 $G$ 는 완비순서체이므로 $A_x$ 는 최소상계를 갖는다. 이 $x$ 에 대하여 결정되는 $A_x$ 의 상한을 $f(x)$ 라고 쓰면 $f$ 는 $F$ 에서 $G$ 로 가는 함수이다. 즉, $x \in F$ 에 대하여 $f: F \to G$ 를 

    $$ f(x) = \sup \{\delta (r) \in G: r \in \mathbb{Q}, \gamma (r) < x\} = \sup A_x \in G $$

    와 같이 정의하는 것이다. 그러면 마찬가지로 $G$ 에서 $F$ 로 가는 함수 $g: G \to F$ 를 $y \in G$ 에 대하여

    $$ g(y) = \sup \{\gamma (r) \in F: r \in \mathbb{Q}, \delta (r) < y\} \in F $$

    와 같이 정의할 수 있다. 

    먼저 $(1)$ 에 의하여 각 유리수 $r, s \in \mathbb{Q}$ 에 대하여 

    $$ r < s \iff \gamma (r) < \gamma (s) \iff \delta (r) < \delta (s) $$

    가 성립한다. 따라서 

    $$ \begin{equation}\begin{split} f(\gamma (s)) &= \sup \{\delta (r) \in G: r \in \mathbb{Q}, \gamma (r) < \gamma (s)\}  \\ &= \sup \{\delta (r) \in G: r \in \mathbb{Q}, \delta (r) < \delta (s)\} = \delta (s) \end{split}\end{equation} \tag*{} $$

    이므로 

    $$ f \circ \gamma = \delta , \quad g \circ \delta = \gamma $$

    이다. 그러면 다음과 같은 관계가 성립한다.

    $$ \mathbb{Q} \xrightarrow{\gamma } F, \mathbb{Q} \xrightarrow{\delta  } G, F \xleftrightarrow[f]{g} G $$

    이제 $f(x+y) = f(x)+f(y)$ 임을 보이는데 함수 $f$ 의 정의와 [정리 2.33](#e1b32aaed) 에 의하여 

    $$ f(x) + f(y) = \sup A_x + \sup A_y = \sup (A_x + A_y) = \sup A _{x+y} = f(x + y) $$

    이므로 

    $$ A _{x+y} = A_x + A_y $$

    임을 보이면 된다. 먼저 $\delta (r) \in A_x, \delta (s) \in A_y \implies \gamma (r) < x, \gamma (s) < y$ 이므로 

    $$ \delta (r)+\delta (s)=\delta (r+s), \quad \gamma (r+s)=\gamma (r)+\gamma (s) < x+y $$

    에서 $\delta (r)+\delta (s)\in A _{x+y}$ 이다. 역으로 $\delta (t) \in A _{x+y} \implies \gamma (t) < x+y$ 인데 [정리 2.5.2](#849201a15) 에 의하여 

    $$ \exists s \in \mathbb{Q} \text{ s.t. }\ r(t)-y<r(s)<x $$

    이다. 그러면 

    $$ \gamma (s) < x, \quad \gamma (t-s) = \gamma (t) - \gamma (s) < y $$

    에서 $\delta (t) = \delta (s) + \delta (t-s)\in A_x+A_y$ 이다. $\blacktriangle$ 

    이제 $f(xy) = f(x)f(y)$ 임을 보이기 위하여 $x,y \in P_F$ 인 경우부터 생각하면 다시 [정리 2.5.2](#849201a15) 에 의하여 

    $$ A_x \cap P_G \neq \varnothing , A_y \cap P_G \neq \varnothing $$

    이므로 [2.34](#85dc4bdbb) 를 적용하면 된다. 이로써 1) 의 증명이 끝났다. $\blacktriangle$ 

    이제 

    $$ x > 0 \iff f(x) > 0 $$

    을 보일텐데 먼저 $x>0$ 이면 [정리 2.5.2](#849201a15) 에 의하여 

    $$ \exists r \in \mathbb{Q} \text{ s.t. }\ 0 < \gamma (r) < x $$

    이다. 그러면 $\delta (r) > 0 \land \delta (r) \in A_x \implies f(x) > 0$ 이다.

    역으로 $f(x)>0$ 이면 $0$ 은 집합 $A_x$ 의 상계가 아니다.따라서 

    $$ \exists \delta (r) \in A_x \text{ s.t. }\ \delta (r) > 0 $$

    이다. 그러면 $0 < \gamma (r)<x$ 이고, 이로써 2) 의 증명이 끝났다. $\blacktriangle$ 

    이제 $f$ 가 전단사함수임을 보이면 모든 증명이 끝난다. 이는 $g \circ f = 1_F, f \circ g = 1_G$ 를 보임으로써 이루어진다. $g \circ f = 1_F$ 를 보이기 위하여 $f$ 의 정의에 의하여 $x \in F$ 에 대하여

    $$ x = \sup \{\gamma (r) \in F:r \in \mathbb{Q}, \delta (r) < f(x)\} \tag{2} $$

    를 보이면 된다. (*왜냐하면 $g$ 에 $f(x)$ 라는 입력을 넣었을 때 $x$ 라는 출력이 나왔으면 최초에 $f$ 에 $x$ 라는 입력을 넣었으므로 항등함수 $1_F$ 가 되기 때문이다.*) 이는 

    1. $r \in \mathbb{Q}, \delta (r) < f(x) \implies \gamma (r) \leq x$

    2. $z < x \implies \exists r \in \mathbb{Q} \text{ s.t. }\ z < \gamma (r), \delta (r) < f(x)$

    를 보이는 것과 같다. a) 는 $r$ 이 $(2)$ 를 만족하면 $x$ 가 최소상계이므로 $\gamma (r) \leq x$ 라는 이야기이고, b) 는 최소상계인 $x$ 보다 작은 $z$ 가 존재하면 $z$ 는 상계가 아니라는 말이다. 

    $\delta (r) < f(x)$ 이면 $\delta (r)$ 은 $A_x$ 의 상계가 아니므로 

    $$ \exists s \in \mathbb{Q}, \delta (r) < \delta (s), \gamma (s) < x $$

    이다. 그러면 $\gamma (r) \gamma (s) \implies \gamma (r) < x$ 이다. 이로써 a) 가 증명되었다. $\blacktriangle$ 

    이제 $z<x$ 라고 하면 [정리 2.5.2](#849201a15) 에 의하여 
    
    $$ \exists r \in \mathbb{Q} \text{ s.t. }\  z < \gamma (r) < x$$

    이다. 그러면 $\delta (r) = f(\gamma (r)) < f(x)$ 이므로 b) 가 증명되었다. $\blacktriangle$ 

    $f \circ g = 1_G$ 도 마찬가지의 방법으로 증명가능하고, 결국 $f$ 는 전단사함수임이 증명된다. 이로써 모든 증명이 끝났다. ■ 
