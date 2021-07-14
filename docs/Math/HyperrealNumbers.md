
# 초실수

!!! info "ref"

    https://sites.math.washington.edu/~morrow/336_15/papers/gianni.pdf

    https://arthasekuritas.com/researchpdf/arthalastcompany.pdf

!!! tldr ""

    Cofinite subset : $Y \subset X$ 인 집합 $X, Y$ 에 대하여 $X \text{ \textbackslash }Y$ 가 유한집합일 때 $Y$ 를 cofinite 라고 한다. 

- Cofinite 는 무한집합일 수도 있고 유한집합일 수도 있다. 

!!! tldr ""

    Ultrafilter : 집합 $X$ 에 대한 ultrafilter 는 다음을 만족하는 $X$ 의 부분집합의 집합이다. 

    1. $X \in \mathcal{F}$

    2. $\varnothing \not \in \mathcal{F}$

    3. $A, B \in \mathcal{F} \implies A \cap B \in \mathcal{F}$

    4. $A \subset X \implies A \in \mathcal{F} \nleftrightarrow X \text{ \textbackslash }A \in \mathcal{F}$

    5. $A \in \mathcal{F} \land A \subset B \implies B \in \mathcal{F}$

- 초실수를 구성하기 위하여 우리는 $\N$ 에 대한 ultrafilter 를 사용한다.

!!! tldr ""

    $\N$ 의 free ultrafilter 가 존재한다. 

- 이때 ultrafilter 가 free 하다는 것을 ultrafilter 가 $\N$ 의 유한 부분집합을 포함하지 않는다는 것으로 정의한다. 그러면 free ultrafilter 는 성질 4) 로 인하여 $\N$ 의 모든 유한 부분집합에 대한 cofinite 를 포함한다.

    그러므로 우리가 사용할 $\N$ 의 free ultrafilter 는 무한집합만을 포함한다. 그리고 이 무한집합들은 $\N$ 의 유한집합에 대한 cofinite 들인 것이다.

    Ultrafilter 는 무한 실수 수열의 집합에서 그들이 유한번 달라서 동치 관계 $\equiv$ 로 묶일 수 있는 원소들을 수집해준다. 

    ultrafilter 는 큰 집합이 필요할 때 작은 집합을 걸러내는 체처럼 사용된다.

- 이제부터 $\N$ 의 free ultrafilter 를 $\mathcal{F}$ 로 두고 계속 사용할 것이다. 

- 증명

!!! tldr "$\equiv$ 의 정의"

    $\N$ 의 free ultrafilter $\mathcal{F}$ 에 대한 $\R ^{\N}$ 의 동치관계 $\equiv$ 를 다음과 같이 정의한다. 

    $$ (r_n) \equiv (s_n) \iff \{n \in \N : r_n = s_n\} \in \mathcal{F} $$

- 초실수를 정의하기 위한 $\R ^{\N}$ 에서의 이 [동치관계](../Foundations/Set/#6a7f4dd92)는 서로 동치인 집합을 잡아내기 위하여 ultrafilter 를 사용한다. 

- 쉽게 말해서 실수 수열이 유한하게 서로 다르다면 두 실수 무한수열(초실수)이 서로 같다고 정의한다는 것이다.

- 예시 

    두 실수 무한 수열 $x = (1,2,3,4, \dots), y = (1,2,2,4, \dots)$ 가 오직 $3$ 번째 항에서 다르다면 $x \equiv y$ 라고 정의한다.

!!! tldr ""

    $\equiv$ 는 동치관계이다.

- 증명

    $\{n \in \N : r_n = r_n\} = \N$ 이고 $\N \in \mathcal{F}$ 이므로 $\equiv$ 는 reflexive 하다. ▲ 

    $\{ n \in \N : r_n = s_n\} = \{n \in \N : s_n = r_n\}$ 이므로 어느 한쪽이 $\mathcal{F}$ 에 속하면 다른 한쪽도 속한다. 그러므로 $\equiv$ 는 symmetric 하다. ▲ 

    $(r_n) \equiv (s_n) \land (s_n) = (t_n)$ 라고 하면 

    $$ \{n \in \N : r_n = s_n\}  \in \mathcal{F} \land \{n \in \N : s_n = t_n\} \in \mathcal{F} $$

    이다. 

    $$ \{n \in \N : r_n = s_n\}  \cap  \{n \in \N : s_n = t_n\} \subseteq \{n \in \N : r_n = t_n\} $$

    인데 $\mathcal{F}$ 는 ultrafilter 로써 교집합에 대하여 닫혀있고 superset 에 대하여 닫혀있으므로

    $$  \{n \in \N : r_n = t_n\} \in \mathcal{F} $$

    이다. 그러므로 $(r_n) \equiv (t_n)$ 이다. 즉, $\equiv$ 는 transitive 하다. ■ 

!!! tldr "초실수의 정의"

    초실수(Hyperreal number) : $\R ^{\N}$ 의 동치관계 $\equiv$ 에 대한 동치류 $[r] = \{s \in \R ^{\N} : r \equiv s\}$ 에 대한 집합

    $$ ^{*}\R = \{[r] : r \in \R ^{\N}\} = \R ^{\N} \text{ \textbackslash }\equiv $$

    이다. 

- 유리수가 실수의 부분체이듯이, 실수는 초실수의 부분체이다. 

- 초실수에서의 실수는 그것 자신의 무한 수열이다.

    - 예시 

        $=$ 좌측은 초실수이고 우측은 실수 무한수열의 동치류이다. 

        $$ 0 = [(0, 0, 0, \dots)] $$

        $$ \pi  = [(\pi, \pi, \pi, \dots)] $$

- 비표준해석학(Non-standard analysis)은 해석학을 연구하기 위하여 $\epsilon,\delta$ 와 거리함수를 사용하는 대신 초실수(주로 무한소)를 사용한다. 

- 일반적인 실수체에서는 무한대와 무한소가 존재하지 않는데 초실수체에서는 무한대와 무한소가 존재하여 비표준해석학을 전개할 수 있다.

- 역사적으로 라이프니츠가 미적분에 무한소를 사용했지만 아무도 그것에 이의를 제기하지 않았다. 가령 오일러는 많은 정리를 증명하기 위하여 무한소를 사용했지만 무한소에 대한 이론적 기반은 전무했다. 예를 들어 $f(x) = x ^{2}$ 를 미분하여 

    $$ \dfrac{(x+\epsilon )^{2}-x ^{2}}{\epsilon } = \dfrac{2x \epsilon +\epsilon ^{2}}{\epsilon }=2x+\epsilon $$

    를 얻으면 $\epsilon$ 을 무한소로 취급하여 무시하고 $2x$ 라는 결과를 얻었다. 하지만 19세기 수학의 엄밀함이 중요하다는 인식이 널리 퍼지면서 무한소가 폐지되고 Weierstrass 이 $\epsilon - \delta$ 논법으로 극한을 정의했다. 이후 1960년대 로빈슨이 모델이론을 정립할 때까지 무한소에 대한 이론은 정립되지 않았다. 

- 초실수의 구성은 자연수, 정수, 유리수, 실수의 구성 과정과 같은 맥락이다. 

    우리는 [$\N$ 을 공집합으로부터 $S(x) = x \cup \{x\}$ 연산으로 구성](../Foundations/numbers/#75c139b38)해내었다. [$\N$ 을 기반으로하는 ordered pair 로 $\mathbb{Z}$ 를 구성](../Foundations/numbers/#738b11833)해내었다. [$\mathbb{Q}$ 는 $\mathbb{Z}$ 를 기반으로 하는 동치류로 구성](../Foundations/numbers/#2b9285e85)했었다. $\R$ 은 $\mathbb{Q}$ 를 기반으로 [데데킨트 절단으로 구성](../Foundations/numbers/#219959e7e)할 수 있고 [코시 수열의 동치류로도 구성](../Foundations/numbers/#f86aac66c)할 수 있었다. 

    초실수의 구성, 즉 $^{*}\R$ 의 구성은 코시 수열의 동치류로 $\R$ 을 구성했던 것과 비슷하다. 초실수의 구성은 무한한 실수 수열의 집합인 $\R ^{\N}$ 의 동치류를 기반으로 이루어진다. 이 동치관계를 정의하기 위하여 ultrafilter 라는 수학적 장치가 필요한 것이다. 

!!! tldr ""

    초실수 연산은 다음과 같이 componentwise 하게 정의된다.

    $$ [r] + [s] = [(r_n + s_n)] $$

    $$ [r] \cdot [s] = [(r_n \cdot s_n)] $$

!!! tldr "$<$ 의 정의"

    $\N$ 에 대한 ultrafilter $\mathcal{F}$ 에 대하여 $<$ 를 다음과 같이 정의한다.

    $$ [r] < [s] \iff \{n \in \N : r_n < s_n\} \in \mathcal{F} $$

!!! tldr ""

    두 수열 $(r_n), (s_n)$ 에 대하여 다음과 같이 정의한다. 

    $$ \llbracket  r = s \rrbracket  := \{n \in \N : r_n = s_n\} $$

    $$ \llbracket  r < s \rrbracket  := \{n \in \N : r_n < s_n\} $$

- 이제부터 $\llbracket \rrbracket$ 를 다른 모든 관계기호에도 자유롭게 사용할 것이다. 

    - 예시 

        $$ \llbracket r \in A \rrbracket  = \{n \in \N : r_n \in A\} $$

!!! tldr ""

    초실수 연산 $+, \cdot$ 과 관계 $<$ 은 잘 정의(well-defined)되었다.

- 증명 

    $+$ 가 잘 정의되었음을 보이자. $(r_n) \equiv (r'_n), (s_n) \equiv (s'_n)$ 은 $\llbracket r = r' \rrbracket \in \mathcal{F}, \llbracket s = s' \rrbracket \in \mathcal{F}$ 을 뜻한다. 또 이는 [ultrafilter 의 성질]()에 의하여 $\llbracket r=r' \rrbracket \cap \llbracket s = s' \rrbracket \in \mathcal{F}$ 을 함의한다. 

    우리가 보여야 할 것은 $\llbracket r + s = r' + s' \rrbracket \in \mathcal{F}$ 이다. 어떤 $k \in \N$ 에 대하여 
    
    $$r_k = r'_k, s_k = s'_k \implies r_k + s_k = r'_k + s'_k$$
    
    이므로 만약 $k \in \llbracket r=r' \rrbracket \cap \llbracket s = s' \rrbracket$ 이면 $k \in \llbracket r+s = r'+s' \rrbracket$ 이다. 이는 

    $$ \llbracket r = r' \rrbracket \cap \llbracket s = s' \rrbracket \subseteq \llbracket r+s = r'+s' \rrbracket $$

    임을 말해준다. $\llbracket r=r' \rrbracket \cap \llbracket s = s' \rrbracket \in \mathcal{F}$ 이므로 [ultrafilter 의 성질]()에 의하여 $\llbracket r+s = r'+s' \rrbracket$ 이다. 그러므로 

    $$ r \equiv r' \land s \equiv s' \implies r+s \equiv r'+s' $$

    이다. ▲ 

    $\cdot$ 이 잘 정의되었다는 것도 비슷하게 증명된다. ▲ 

    $<$ 가 잘 정의되었다는 것은 

    $$ (r_n) \equiv (r'_n) \land (s_n) \equiv (s'_n) \land \llbracket r<s \rrbracket  \in \mathcal{F} \implies \llbracket r' < s' \rrbracket \in \mathcal{F} $$

    이다. 이것을 증명해야 한다. 먼저 [ultrafilter 의 성질]() 과 가정에 의하여 

    $$ \llbracket r=r' \rrbracket \cap \llbracket s=s' \rrbracket \cap \llbracket r<s \rrbracket \in \mathcal{F} $$

    이다. 만약 $k \in \llbracket r=r' \rrbracket \cap \llbracket s=s' \rrbracket \cap \llbracket r<s \rrbracket$ 이면 $r_k = r'_k, s_k = s'_k, r_k < s_k$ 이고, 그러므로 $r'_k < s'_k$ 이다. 따라서 $k \in \llbracket r' < s' \rrbracket$ 이다. 이는 

    $$ \llbracket r=r' \rrbracket \cap \llbracket s=s' \rrbracket \cap \llbracket r<s \rrbracket \subseteq \llbracket r' < s' \rrbracket $$

    을 뜻하고, [ultrafilter 의 성질]() 에 의하여 $\llbracket r' < s' \rrbracket \in \mathcal{F}$ 이다. ■ 

# Transfer Principle

!!! tldr ""

    Transfer Principle : Any appropriately formaulated first-order logic statement $\phi$ about $\R$ is true iff $^{*}\phi$ is true for $^{*}\R$.

- 이 정리 덕분에 실수에 대한 명제를 그대로 초실수에 대한 명제로써 사용할 수 있다. 이는 모델 이론 덕분에 가능하다. 

    - 예시 

        실수에 대한 commutativity 를 초실수에서도 사용할 수 있다.

        실수는 순서체이다. 그러므로 초실수도 순서체이다. 
 
- 초실수 이론은 1차 논리를 사용한다. 

- 증명 

    이 정리에 대한 엄밀한 증명은 매우 어려운 모델 이론과 공리적 연역을 사용하므로 생략한다.

    이 정리가 왜 성립하는지에 대한 아이디어는 이해하기 쉽다. $M_i$ 의 곱집합에 대한 ultrafilter $\mathcal{U}$ 

    $$ \prod_{i \in \N}^{} M_i \text{ \textbackslash }\mathcal{U} $$

    를 생각하자. 만약 1차 논리 명제 $\phi$ 가 각각의 $M_i$ 에 대하여 성립하고 ultrafilter 에 의하여 captured 된다면 $\phi$ 는 ultraproduct 에서도 성립한다. ■ 

    - *ultrafilter, ultraproduct 에 대한 이해가 부족해서 captured 된다는 것이 뭔지 잘 모르겠다*

# 무한소와 무한대 

!!! tldr "무한소(infinitesimal)의 존재 정리"

    $$ \exists \epsilon \in {}^{*}\R \text{ s.t. }\ \forall r \in \R ^{+} : 0 < \epsilon < r $$

- 이 정리는 무한소를 정의하고 존재성을 증명한다. 무한소의 정의로 인하여 무한소는 양수도 될 수 있고 음수도 될 수 있으나 일단 이 논의에서는 걱정하지 않아도 된다. 

- 증명

    우선 $r \in \R$ 을 ${}^{*}\R$ 에서 $^{*}r \in {}^{*}\R$ 로 표현해야 하지만 편의상 $*$ 를 제거하고 실수 $r$ 을 초실수 $r$ 로 표현하자. 

    $\epsilon = \bigg [\bigg (1, \dfrac{1}{2}, \dfrac{1}{3}, \dfrac{1}{4}, \dots\bigg )\bigg ] = \bigg [\bigg (\dfrac{1}{n}\bigg )\bigg ]$ 라고 두자. 그러면 임의의 $r \in \R$ 에 대하여 $\bigg \{n \in \N : \dfrac{1}{n} > r \bigg \}$ 은 유한집합이다. 그러므로 $\bigg\{n \in \N : \dfrac{1}{n} < r \bigg \} \in \mathcal{F}$ 이다. 그러므로 $\epsilon < r$ 이다. ▲ 

    또한 $\{n \in \N : 0 < \frac{1}{n}\} = \N \in \mathcal{F}$ 이므로 $0 < \epsilon$ 이다. ■ 

!!! tldr "무한대(unlimited)의 존재 정리"

    $$ \exists \omega \in {}^{*}\R \text{ s.t. }\ \forall x \in \R : \omega > x $$

- 증명 

    $\omega = [(1,2,3,\dots)] = [(n)]$ 라고 두자. 임의의 실수 $r$ 에 대하여 $\{n \in \N : r \geq n\}$ 은 유한집합이므로 $\{n \in \N : r < n\} \in \mathcal{F}$ 이다. 이는 $\omega > r$ 임을 말해준다. ■ 

!!! tldr ""

    ${}^{*}\R$ 에서의 동치관계 $\backsimeq$ 를 다음과 같이 정의한다. 

    $$ x \backsimeq y \iff x - y = 0 \lor x - y \text{ is infinitesimal } $$

- 이 동치관계가 잘 정의되었음을 증명하는 것은 쉽다. 

- $\epsilon \backsimeq 0$ 에서 "arbitrary close" 라는 개념이 나온다. 이것에 해석학의 증명의 핵심이 있기 때문에 잘 이해해야 한다.