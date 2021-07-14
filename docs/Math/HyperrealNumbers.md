
!!! info "ref"

    https://sites.math.washington.edu/~morrow/336_15/papers/gianni.pdf

    https://arthasekuritas.com/researchpdf/arthalastcompany.pdf

# 초실수

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

    $$ \big < r_n \big > \equiv \big < s_n \big > \iff \{n \in \N : r_n = s_n\} \in \mathcal{F} $$

- 초실수를 정의하기 위한 $\R ^{\N}$ 에서의 이 [동치관계](../Foundations/Set/#6a7f4dd92)는 서로 동치인 집합을 잡아내기 위하여 ultrafilter 를 사용한다. 

- 쉽게 말해서 실수 수열이 유한하게 서로 다르다면 두 실수 무한수열(초실수)이 서로 같다고 정의한다는 것이다.

- 예시 

    두 실수 무한 수열 $x = \big < 1,2,3,4, \dots \big >, y = \big < 1,2,2,4, \dots \big >$ 가 오직 $3$ 번째 항에서 다르다면 $x \equiv y$ 라고 정의한다.

!!! tldr ""

    $\equiv$ 는 동치관계이다.

- 증명

    $\{n \in \N : r_n = r_n\} = \N$ 이고 $\N \in \mathcal{F}$ 이므로 $\equiv$ 는 reflexive 하다. ▲ 

    $\{ n \in \N : r_n = s_n\} = \{n \in \N : s_n = r_n\}$ 이므로 어느 한쪽이 $\mathcal{F}$ 에 속하면 다른 한쪽도 속한다. 그러므로 $\equiv$ 는 symmetric 하다. ▲ 

    $\big < r_n \big > \equiv \big < s_n \big > \land \big < s_n \big > = \big < t_n \big >$ 라고 하면 

    $$ \{n \in \N : r_n = s_n\}  \in \mathcal{F} \land \{n \in \N : s_n = t_n\} \in \mathcal{F} $$

    이다. 

    $$ \{n \in \N : r_n = s_n\}  \cap  \{n \in \N : s_n = t_n\} \subseteq \{n \in \N : r_n = t_n\} $$

    인데 $\mathcal{F}$ 는 ultrafilter 로써 교집합에 대하여 닫혀있고 superset 에 대하여 닫혀있으므로

    $$  \{n \in \N : r_n = t_n\} \in \mathcal{F} $$

    이다. 그러므로 $\big < r_n \big > \equiv \big < t_n \big >$ 이다. 즉, $\equiv$ 는 transitive 하다. ■ 

!!! tldr "초실수의 정의"

    초실수(Hyperreal number) : $\R ^{\N}$ 의 동치관계 $\equiv$ 에 대한 동치류 $[r] = \{s \in \R ^{\N} : r \equiv s\}$ 에 대한 집합

    $$ ^{*}\R = \{[r] : r \in \R ^{\N}\} = \R ^{\N} \text{ \textbackslash }\equiv $$

    이다. 

- 유리수가 실수의 부분체이듯이, 실수는 초실수의 부분체이다. 

- 초실수에서의 실수는 그것 자신의 무한 수열이다.

    - 예시 

        $=$ 좌측은 초실수이고 우측은 실수 무한수열의 동치류이다. 

        $$ 0 = [\big <0, 0, 0, \dots\big >] $$

        $$ \pi  = [\big <\pi, \pi, \pi, \dots\big >] $$

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

    $$ [r] + [s] = [\big <r_n + s_n\big >] $$

    $$ [r] \cdot [s] = [\big <r_n \cdot s_n\big >] $$

!!! tldr "$<$ 의 정의"

    $\N$ 에 대한 ultrafilter $\mathcal{F}$ 에 대하여 $<$ 를 다음과 같이 정의한다.

    $$ [r] < [s] \iff \{n \in \N : r_n < s_n\} \in \mathcal{F} $$

!!! tldr ""

    두 수열 $\big <r_n\big >, \big <s_n\big >$ 에 대하여 다음과 같이 정의한다. 

    $$ \llbracket  r = s \rrbracket  := \{n \in \N : r_n = s_n\} $$

    $$ \llbracket  r < s \rrbracket  := \{n \in \N : r_n < s_n\} $$

- 이제부터 $\llbracket \rrbracket$ 를 다른 모든 관계기호에도 자유롭게 사용할 것이다. 

    - 예시 

        $$ \llbracket r \in A \rrbracket  = \{n \in \N : r_n \in A\} $$

!!! tldr ""

    초실수 연산 $+, \cdot$ 과 관계 $<$ 은 잘 정의(well-defined)되었다.

- 증명 

    $+$ 가 잘 정의되었음을 보이자. $\big <r_n\big > \equiv \big <r'_n\big >, \big <s_n\big > \equiv \big <s'_n\big >$ 은 $\llbracket r = r' \rrbracket \in \mathcal{F}, \llbracket s = s' \rrbracket \in \mathcal{F}$ 을 뜻한다. 또 이는 [ultrafilter 의 성질](#67081dab0)에 의하여 $\llbracket r=r' \rrbracket \cap \llbracket s = s' \rrbracket \in \mathcal{F}$ 을 함의한다. 

    우리가 보여야 할 것은 $\llbracket r + s = r' + s' \rrbracket \in \mathcal{F}$ 이다. 어떤 $k \in \N$ 에 대하여 
    
    $$r_k = r'_k, s_k = s'_k \implies r_k + s_k = r'_k + s'_k$$
    
    이므로 만약 $k \in \llbracket r=r' \rrbracket \cap \llbracket s = s' \rrbracket$ 이면 $k \in \llbracket r+s = r'+s' \rrbracket$ 이다. 이는 

    $$ \llbracket r = r' \rrbracket \cap \llbracket s = s' \rrbracket \subseteq \llbracket r+s = r'+s' \rrbracket $$

    임을 말해준다. $\llbracket r=r' \rrbracket \cap \llbracket s = s' \rrbracket \in \mathcal{F}$ 이므로 [ultrafilter 의 성질](#67081dab0)에 의하여 $\llbracket r+s = r'+s' \rrbracket$ 이다. 그러므로 

    $$ r \equiv r' \land s \equiv s' \implies r+s \equiv r'+s' $$

    이다. ▲ 

    $\cdot$ 이 잘 정의되었다는 것도 비슷하게 증명된다. ▲ 

    $<$ 가 잘 정의되었다는 것은 

    $$ \big <r_n\big > \equiv \big <r'_n\big > \land \big <s_n\big > \equiv \big <s'_n\big > \land \llbracket r<s \rrbracket  \in \mathcal{F} \implies \llbracket r' < s' \rrbracket \in \mathcal{F} $$

    이다. 이것을 증명해야 한다. 먼저 [ultrafilter 의 성질](#67081dab0) 과 가정에 의하여 

    $$ \llbracket r=r' \rrbracket \cap \llbracket s=s' \rrbracket \cap \llbracket r<s \rrbracket \in \mathcal{F} $$

    이다. 만약 $k \in \llbracket r=r' \rrbracket \cap \llbracket s=s' \rrbracket \cap \llbracket r<s \rrbracket$ 이면 $r_k = r'_k, s_k = s'_k, r_k < s_k$ 이고, 그러므로 $r'_k < s'_k$ 이다. 따라서 $k \in \llbracket r' < s' \rrbracket$ 이다. 이는 

    $$ \llbracket r=r' \rrbracket \cap \llbracket s=s' \rrbracket \cap \llbracket r<s \rrbracket \subseteq \llbracket r' < s' \rrbracket $$

    을 뜻하고, [ultrafilter 의 성질](#67081dab0) 에 의하여 $\llbracket r' < s' \rrbracket \in \mathcal{F}$ 이다. ■ 

## 무한소와 무한대 

!!! tldr "무한소(infinitesimal)의 존재 정리"

    $$ \exists \epsilon \in {}^{*}\R \text{ s.t. }\ \forall r \in \R ^{+} : 0 < \epsilon < r $$

- 이 정리는 무한소를 정의하고 존재성을 증명한다. 무한소의 정의로 인하여 무한소는 양수도 될 수 있고 음수도 될 수 있으나 일단 이 논의에서는 걱정하지 않아도 된다. 

- 증명

    우선 $r \in \R$ 을 ${}^{*}\R$ 에서 $^{*}r \in {}^{*}\R$ 로 표현해야 하지만 편의상 $*$ 를 제거하고 실수 $r$ 을 초실수 $r$ 로 표현하자. 

    $\epsilon = \bigg [\bigg <1, \dfrac{1}{2}, \dfrac{1}{3}, \dfrac{1}{4}, \dots\bigg >\bigg ] = \bigg [\bigg <\dfrac{1}{n}\bigg >\bigg ]$ 라고 두자. 그러면 임의의 $r \in \R$ 에 대하여 $\bigg \{n \in \N : \dfrac{1}{n} > r \bigg \}$ 은 유한집합이다. 그러므로 $\bigg\{n \in \N : \dfrac{1}{n} < r \bigg \} \in \mathcal{F}$ 이다. 그러므로 $\epsilon < r$ 이다. ▲ 

    또한 $\{n \in \N : 0 < \frac{1}{n}\} = \N \in \mathcal{F}$ 이므로 $0 < \epsilon$ 이다. ■ 

!!! tldr "무한대(unlimited)의 존재 정리"

    $$ \exists \omega \in {}^{*}\R \text{ s.t. }\ \forall x \in \R : \omega > x $$

- 증명 

    $\omega = [\big <1,2,3,\dots\big >] = [\big <n\big >]$ 라고 두자. 임의의 실수 $r$ 에 대하여 $\{n \in \N : r \geq n\}$ 은 유한집합이므로 $\{n \in \N : r < n\} \in \mathcal{F}$ 이다. 이는 $\omega > r$ 임을 말해준다. ■ 

- 초실수체의 무한소와 무한대

    ![](https://upload.wikimedia.org/wikipedia/commons/5/53/N%C3%BAmeros_hiperreales.png)

- 초실선

    ![](http://www.vias.org/calculus/img/01_real_and_hyperreal_numbers-83.gif)

# 초실수로의 도약

## Set Enlargement

!!! tldr ""

    Enlarged set : 집합 $A \subset \R$ 에 대하여 다음 조건이 충족되면 enlarged set $^{*}A \in {}^{*}\R$ 을 정의할 수 있다. 

    $$ [r] \in {}^{*}A \iff \{n \in \N : r_n \in A\} \in \mathcal{F} $$

- 예시 

    $A = \N, \omega = \big <1,2,3,\dots\big >$ 로 두자. 그러면 

    $$ \llbracket \omega \in \N \rrbracket  = \N \in \mathcal{F} \implies \omega \in {}^{*}\N $$

    이다. $^{*}\N$ 을 초자연수(hypernatural) 이라고 한다. 

- 예시 

    $A = \{0, 1\}, r = \big <0.9, 0.99, 0.999, \dots\big >$ 로 두자. 그러면 

    $$ \llbracket r \in \N \rrbracket  = \N \in \mathcal{F} \implies r \in {}^{*}\{0, 1\} $$

    이다. 

!!! tldr ""

    Enlarged set 은 잘 정의되었다.

- 증명 

    $\llbracket r \in A \rrbracket = \{n \in \N : r_n \in A\}$ 에서 

    $$ \llbracket r=r' \rrbracket \cap \llbracket r \in A \rrbracket \subseteq \llbracket r' \in A \rrbracket $$

    이다. $r \equiv r' \land \llbracket r \in A \rrbracket \in \mathcal{F}$ 이면 $\llbracket r' \in A \rrbracket \in \mathcal{F}$ 이므로 증명이 끝났다. ■ 

## Extending functions

!!! tldr ""

    Extension of real function : 
    
    실함수 $f: \R \to \R$ 를 초현실수를 표현하는 수열의 성분에 

    $$ {}^{*}f([\big <r_1, r_2, \dots\big >]) = [\big <f(r_1), f(r_2), \dots\big >] $$
    
    와 같이 적용하여 $^{*}f: {}^{*}\R \to {}^{*}\R$ 를 얻는 것이다.
    
!!! tldr ""

    Function extension 은 잘 정의되었다. 

- 증명 

    먼저 편의상 $f \circ r$ 을 초실수 $r$ 의 수열을 함수 $f$ 에 적용한 수열 

    $$ f \circ r := \big <f(r_1), f(r_2), \dots\big > $$

    로 정의하자. 

    일반적으로 $\llbracket r=r' \rrbracket \subseteq \llbracket f \circ r = f \circ r' \rrbracket$ 가 성립한다. 그러므로 
    
    $$ r \equiv r' \implies {}^{*}f(r) = f \circ r \equiv f \circ r' = {}^{*}f(r')$$

    이다. 그러므로 Funciton extension 은 잘 정의되었다. ■ 
    
!!! tldr ""

    Extension of real-valued function : $A \subset \R$ 에 대한 실가함수 $f: A \to \R$ 의 extension $^{*}f: {}^{*}A \to {}^{*}\R$ 은 수열

    $$ s_n = \begin{cases} f(r_n) & r_n \in A \\ 0 & r_n \not\in A \\ \end{cases} $$

    에 대하여 

    $$ {}^{*}f([\big <r_n\big >]) = [\big <s_n\big >] $$

    이다.

- 실가함수의 경우 이렇게 정의되는 이유는 $r \in {}^{*}A$ 의 모든 성분이 $A$ 에 포함되지 않을 수도 있기 때문이다. 즉, $f(r_i)$ 가 정의되지 않은 인덱스 $i$ 가 존재할 수도 있다. 

    따라서 이런 경우에, 즉 $r_i \not\in A$ 일 때는 $f(r_i) = 0$ 로 정의해버리는 것이다.

!!! tldr ""

    초수열(hypersequence) : 수열 $\big <s_n\big > = \big <s_1,s_2, \dots\big >$ 는 실가함수 $s : \N \to \R$ 인데, 이를 초실수로 확장한 

    $$ s : {}^{*}\N \to {}^{*}\R $$

    을 초수열이라 한다.

- 실가함수의 function extension 이 잘 정의되어서 초수열 $s: {}^{*}\N \to {}^{*}\R$ 에서 $s_n$ 가 $n \in {}^{*}\N \text{ \textbackslash } \N$ 일 때도 초수열을 만들 수 있다. 

## Transfer Principle

!!! tldr ""

    Transfer Principle : 잘 정의된 $\R$ 에 대한 1차논리 명제 $\phi$ 와 ${}^{*}\R$ 에 대한 $\phi$ 의 $*$-변환 명제 ${}^{*}\phi$ 는 동치이다. 즉, 

    $$ \phi \iff {}^{*}\phi $$

    이다.

- 이 정리는 실수에 대하여 잘 정의된 1차논리 명제를 $*$-변환(Set Enlargement, Function extension, etc.)으로 초실수에 대한 명제로 변환하면 두 명제의 진리값이 서로 같다는 것을 말해준다. 

- $\phi$ 를 ${}^{*}\phi$ 로 ${}^{*}-$변환을 한 것은 Set Enlargement, Funciton extension 등을 사용하여 일차논리 명제 $\phi$ 가 포함하는 관계 $P$, 함수 $f$, 상수 $r$ 을 모두 ${}^{*}P, {}^{*}f, {}^{*}r$ 로 치환한다는 것이다. 

    - 예시 

        $$ \forall n \in \N \exists m \in \N : m > n $$

        의 $*$-변환은 

        $$ \forall n \in {}^{*}\N \exists m \in {}^{*}\N : m {}^{*}> n $$

        이다.

        $$ \forall x \in \R : \sin (x) < 2 $$

        의 $*$-변환은 

        $$ \forall x \in {}^{*}\R : {}^{*}\sin (x) {}^{*}< {}^{*}2 $$

        이다. 근데 일반적으로 편의상 상수와 함수와 부등호에 있는 $*$ 는 제거한다. 그래서 결국 

        $$ \forall n \in {}^{*}\N \exists m \in {}^{*}\N : m>n $$

        $$ \forall x \in {}^{*}\R : \sin (x) < 2 $$

        가 된다. 

- 이 정리가 비표준 해석학에서 가장 중요한 도구 중 하나이다.

- 이 정리 덕분에 실수에 대한 명제를 그대로 초실수에 대한 명제로써 사용할 수 있다. 이는 모델 이론 덕분에 가능하다. 

    - 예시 

        실수에 대한 commutativity 를 초실수에서도 사용할 수 있다.

        실수는 순서체이다. 그러므로 초실수도 순서체이다. 
 
- 초실수 이론은 1차 논리를 사용한다. 

- ${}^{*}\R \to \R$ 방향으로 이 정리를 사용해야 할 때도 있을 것이다. 이것도 물론 가능하다. 그러나 초실수 명제에서 초실수 상수를 포함하면 안된다는 제약이 있다. 

    그러나 초실수 상수를 포함하는 명제를 반드시 실수로 변환해야 하는 상황이라면 초실수 상수를 변수 $x$ 로 치환하고 $A \subseteq \R$ 에 대한 $\exists x \in {}^{*}A$ 라는 양화사를 추가하는 것이 한가지 방법이다. 

- 증명 

    이 정리에 대한 엄밀한 증명은 매우 어려운 모델 이론과 공리적 연역을 사용하므로 생략한다.

    이 정리가 왜 성립하는지에 대한 아이디어는 이해하기 쉽다. $M_i$ 의 곱집합에 대한 ultrafilter $\mathcal{U}$ 

    $$ \prod_{i \in \N}^{} M_i \text{ \textbackslash }\mathcal{U} $$

    를 생각하자. 만약 1차 논리 명제 $\phi$ 가 각각의 $M_i$ 에 대하여 성립하고 ultrafilter 에 의하여 captured 된다면 $\phi$ 는 ultraproduct 에서도 성립한다. ■ 

    - *ultrafilter, ultraproduct 에 대한 이해가 부족해서 captured 된다는 것이 뭔지 잘 모르겠다*

## Using the Transfer Principle

!!! tldr ""

    structure $\big <{}^{*}\R ,+,\cdot ,<\big >$ 은 $+$ 의 항원원과 $\cdot$ 의 항등원을 갖는 순서체이다. 

- 증명 

    [절단에 의한 정리](../Foundations/numbers/#e53c4f1e1)와 [코시 수열에 의한 정리](../Foundations/numbers/#765b33eaf)에 의하여 $\R$ 은 순서체이다. 이는 일차논리에 의한 명제로 표현가능하다. 

    $\R$ 의 commutativity 에 대한 정리를 transfer principle 로 다음과 같이 변환할 수 있다. 

    $$ \forall x, y \in \R : x+y=y+x $$

    $$ \forall x,y \in {}^{*}\R : x + y = y + x $$

    마찬가지로 [순서체의 나머지 모든 공리](../Foundations/numbers/#717ad086f)들은 1차 논리 명제이므로 transfer principle 로 초실수의 명제로 변환시킬 수 있다. 

    그러므로 $\big <{}^{*}\R , +, \cdot , <\big >$ 은 순서체이다. ■ 

- 물론 [$\R$ 의 중요한 성질 중 하나는 실수체가 완비적](../Foundations/numbers/#050ce8566)이라는 것이다. 그러므로 $\R$ 의 공집합이 아니고 위로 유계인 부분집합은 상한을 가진다.

    그러면 이상하다. [이 정리](../Foundations/numbers/#71e5fdcc6) 에 의하여 완비순서체는 오로지 실수체라는 것을 우리는 이미 알고 있다. 그런데 Transfer principle 로 실수의 완비성에 대한 명제를 초실수로 변환할 수 있지 않을까?

    하지만 실수의 완비명제를 초실수로 변환하는 것은 불가능하다. 실수의 완비성이 초실수의 완비성으로 변환될 수 없는 이유는 초실수의 완비성이 오로지 2차 논리 명제로만 표현되기 때문이다. 왜냐하면 단순히 $\R$ 의 성분을 언급하는 것이 아니라 $\R$ 의 부분집합을 언급해야만 하기 때문이다. 

    사실은 그래서 초실수체 ${}^{*}\R$ 는 완비적이지 않다. 

    - 예시 

        개구간 $(0, 1) \in \R$ 은 ${}^{*}\R$ 에서 상한을 갖지 않는다. 

!!! tldr ""

    임의의 집합 $A, B \subset \R$ 에 대하여 다음이 성립한다. 

    - ${}^{*}(A \cup B) = {}^{*}A \cup {}^{*}B$

    - ${}^{*}(A \cap B) = {}^{*}A \cap {}^{*}B$

    - ${}^{*}(A \text{ \textbackslash }  B) = {}^{*}A \text{ \textbackslash }  {}^{*}B$

- 증명 

    임의의 집합 $A, B \subset \R$ 에 대하여 [합집합의 정의](../Foundations/Set/#063667813) 에 의하여 

    $$ \forall x \in \R : ( x \in A \cup B  \iff x \in A \lor x \in B) $$

    가 성립한다. transfer principle 에 의하여 이 명제를 변환한 명제

    $$ \forall x \in {}^{*} \R : ( x \in {}^{*}(A \cup B)  \iff x \in {}^{*} A \lor x \in {}^{*} B) \tag{1} $$

    도 성립한다. 또한 임의의 집합 $X,Y \in {}^{*}\R$ 에 대하여 

    $$ \forall x \in {}^{*} \R : ( x \in (X \cup Y)  \iff x \in  X \lor x \in  Y) \tag{2} $$

    가 성립한다. $(1), (2)$ 를 결합하여 

    $$ \forall \in {}^{*}\R : x \in {}^{*}(A \cup B) \iff x \in ({}^{*}A \cup {}^{*}B) $$

    가 성립한다. 그러므로 

    $$ {}^{*}(A \cup B) = {}^{*}A \cup {}^{*}B $$

    이다. ▲ 

    나머지 명제도 비슷하게 증명가능하다. ■ 

- ${}^{*}(\bigcup_{n \in \N}^{}) A_n$ 이 $(\bigcup_{n \in \N}^{} {}^{*}A_n)$ 과 같을 필요는 없다. 

    가령 $A_n = \{n\}$ 이면 

    $$ {}^{*}\bigg (\bigcup_{n \in \N}^{} A_n\bigg ) = {}^{*}\N $$

    이지만 

    $$ \bigg (\bigcup_{n \in \N}^{} {}^{*} A_n\bigg ) = \N $$

    이 된다. 

# 초실수의 성질

!!! tldr ""

    초실수 $b$ 을 다음의 조건들에 따라 다음과 같이 부르기로 한다.

    - 유한(limited) : $\exists r,s \in \R : r < b < s$

    - 양의 무한대(positive unlimited) : $\forall r \in \R : r < b$

    - 음의 무한대(negative unlimited) : $\forall r \in \R : b < r$

    - 무한대(unlimited) : 양의 무한대이거나 음의 무한대일 때.

    - 양의 무한소(positive infinitesimal) : $\forall r \in \R ^{+} : 0 < b < r$

    - 음의 무한소(negative infinitesimal) : $\forall r \in \R ^{-} : r < b < 0$

    - 무한소(infinitesimal) : 양의 무한대이거나 음의 무한대일 때.

    - appreciable : 유한이지만 무한소가 아닐 때.

- 개별 숫자를 지칭할 때 유한(limited), 무한대(unlimited) 을 사용한다. 집합을 지칭할 때 finite 와 infinite 를 사용한다.

!!! tldr ""

    $\forall X \in {}^{*}\R$ 에 대하여 다음과 같이 정의한다.

    $$ X _{\infty} = \{x \in X | x \text{ is unlimited }\} $$

    $$ X^{+} = \{x \in X | x > 0 \} $$

- $X ^{+} _{\infty}$ 는 $X$ 의 모든 양의 무한대 집합을 뜻한다. 

## 초실수 연산

!!! tldr "초실수 연산 규칙"

    무한소 $\epsilon , \delta$ 과 appreciable $b, c$ 와 무한대 $H, K$ 에 대하여 초실수 연산 규칙은 다음과 같다. 

    - $\epsilon + \delta$ 는 무한소이다. 

    - $b + \epsilon$ 는 apprecable 이다.

    - $H + \epsilon$, $H + b$ 는 무한대이다. 

    - $b+c$ 는 유한이다. 

    - $-\epsilon$ 은 무한소이다.

    - $-b$ 는 apprecable 이다.

    - $-H$ 는 무한대이다.

    - $\epsilon \cdot \delta$, $\epsilon \cdot b$ 는 무한소이다. 

    - $b \cdot c$ 는 appreciable 이다. 

    - $b \cdot H$, $H \cdot K$ 는 무한대이다. 

    - $\frac{1}{\epsilon }$ 은 $\epsilon \neq 0$ 이면 무한대이다. 

    - $\frac{1}{b }$ 은 appreciable 이다. 

    - $\frac{1}{H }$ 은 무한소이다. 

    - $\frac{\epsilon }{b }$, $\frac{\epsilon }{H }$, $\frac{b }{H }$ 은 무한소이다. 

    - $\frac{b}{c }$ 은 appreciable 이다. 

    - $\frac{b }{\epsilon  }$, $\frac{H }{\epsilon  }$, $\frac{H }{b }$ 은  $\epsilon \neq 0$ 이면 무한대이다. 

- 증명 

- 이 논의에서는 이 연산 규칙을 증명하지 않는다. 그러나 transfer principle 이나 실수 수열에 대한 논의를 전개하면 쉽게 증명할 수 있다. 

- $\frac{\epsilon }{\delta }, \frac{H}{K}, \epsilon \cdot H, H + K$ 를 따로 정의하지는 않는다. 이들은 무한소, 무한대, appreciable 의 값을 모두 가질 수 있다. 

## Halos

!!! tldr "$\backsimeq$ 의 정의"

    ${}^{*}\R$ 에서의 동치관계 $\backsimeq$ 를 다음과 같이 정의한다. 

    $$ x \backsimeq y \iff x - y = 0 \lor x - y \text{ is infinitesimal } $$

- 이 동치관계가 잘 정의되었음을 증명하는 것은 쉽다. 

- $\epsilon \backsimeq 0$ 에서 "무한히 가까운" 이라는 개념이 나온다. 이것에 해석학의 증명의 핵심이 있기 때문에 잘 이해해야 한다.

!!! tldr ""

    halo : $b \in {}^{*}\R$ 의 halo 는 동치관계 $\backsimeq$ 의 동치류

    $$ \text{hal}(b) = \{c \in {}^{*}\R : b \backsimeq c\} $$

    이다. 

- 쉽게 말해 초실수 $b$ 의 halo 는 $b$ 와 무한히 가까운 모든 초실수의 집합이라는 것이다. 

!!! tldr ""

    $$ \forall b, c \in \R : b \backsimeq c \implies b = c $$

- 증명

    $b \backsimeq c \land b \neq c$ 를 가정하자. 그러면 $b - c = r \neq 0$ 이다. 하지만 $r$ 이 무한소가 아니므로 이는 $b \backsimeq c$ 이라는 가정과 모순이다. ■ 
