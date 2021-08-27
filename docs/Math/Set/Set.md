# Proposition

!!! def "명제(proposition)"

    문장들 가운데 참 또는 거짓인 것이다.

- 예시 

    "$5$ 는 자연수이다." 는 명제이다.

!!! def "명제의 부정(negation of proposition)"

    명제 $p$ 에 대한 명제 "$p$가 아니다." 이다.

- 명제의 부정을  $\lnot p$ 로 표기한다.

- 예시 

    명제 $p$ "$5$ 는 자연수이다." 의 부정 $\lnot p$ 은 "$5$ 는 자연수가 아니다." 이다.

!!! def "진리표(Truth table)"

    명제 $p$ 에 따른 다른 명제들의 결과를 표로 정리한 것이다.

- 예시 

    명제 $p$ 가 참이면 부정 $\lnot p$ 은 거짓이 되고, 거짓이면 참이 되는데 이것을 표로 정리하면 다음과 같다. 

    |$p$|$\lnot p$|$\lnot (\lnot p)$|
    |:---:| :---:| :---:|
    |$T$|$F$|$T$|
    |$F$|$T$|$F$|

    진리표를 통하여 $p$ 와 $\lnot (\lnot p)$ 의 옳고 그름이 같다는 것을 알 수 있다.

!!! def "논리합(Logical disjuntion)"

    명제 $p, q$ 에 대하여 명제 $p \lor q$ 이다.

- "$p \lor q$" 는 $p$와 $q$ 중 하나만 참이어도 $p \lor q$ 가 참이 된다.

- 예시 

    명제 "$18$은 $4$의 배수이거나 $6$의 배수이다." 는 명제 "[$18$은 $4$의 배수이다.] $\lor$ [$18$은 $6$ 의 배수이다.]" 이다.

- $p \lor q$, 즉 "$p$ 또는 $q$" 의 부정은 "$p$도 아니고 $q$도 아니다.", 즉 $(\lnot p) \land (\lnot q)$ 이다.

    - 예시 

        "그곳에 풀이나 나무 중 적어도 한 가지가 있었다." 의 부정은 "그곳에 풀도 없었고 나무도 없었다." 가 된다.

    - 위 예시로 $\lnot (p \lor q) \equiv (\lnot p) \land (\lnot q)$ 임을 알 수 있다.

- 그러므로 진리표는 다음과 같다. 

    |$p$|$q$ |$p \lor q$|$\lnot (p \lor q)$|$(\lnot p) \land (\lnot q)$|
    |:---:| :---:| :---:| :---:| :---:|
    |$T$|$T$|$T$|$F$|$F$|
    |$T$|$F$|$T$|$F$|$F$|
    |$F$|$T$|$T$|$F$|$F$|
    |$F$|$F$|$F$|$T$|$T$|

!!! def "논리곱(Logical conjunction)"

    명제 $p, q$ 에 대한 명제 $p \land q$ 이다.

- "$p \land q$" 는 $p$와 $q$ 가 둘 다 참이어야 $p \land q$ 가 참이 된다.

- 진리표는 다음과 같다. 

    |$p$|$q$ |$p \land q$|$\lnot (p \land q)$|$(\lnot p) \lor (\lnot q)$|
    |:---:| :---:| :---:| :---:| :---:|
    |$T$|$T$|$T$|$F$|$F$|
    |$T$|$F$|$F$|$T$|$T$|
    |$F$|$T$|$F$|$T$|$T$|
    |$F$|$F$|$F$|$T$|$T$|

!!! def "실질 조건문(material conditional)"

    명제 $p,q$ 에 대한 명제 $p \to q$ 이다.

- "$p$ 이면 $q$ 이다" 로 읽는다. 이 명제의 부정은 $p$는 성립하지만 $q$ 는 성립하지 않는 것이므로 

    $$ \lnot (p \to q) \equiv p \land (\lnot q) $$

    이다. 이것을 다시 쓰면

    $$ p \to q \equiv \lnot  p \lor q $$

    이다. 그러므로 진리표는

    |$p$|$q$ |$\lnot  p \lor q$|$p \to q$|
    |:---:| :---:| :---:| :---:|
    |$T$|$T$|$T$|$T$|
    |$T$|$F$|$F$|$F$|
    |$F$|$T$|$T$|$T$|
    |$F$|$F$|$T$|$T$|

    이다.

    그러므로 $p$ 가 거짓이면 $p \to q$ 는 항상 참이다. 이것을 공진리라고 한다.

- $p \to q$ 이고 $q \to p$ 일때 즉, $(p \to q)\land (q \to p)$ 일 때 $p \iff q$ 라고 한다.

!!! def "$p \implies q$"

    $p \to q$ 가 참일 때 $p \implies q$ 라고 한다.

- $p \implies q$ 이고 $q \implies p$ 일 때, $p \iff q$ 라고 한다.

!!! def "조건(condition)"

    변수 $x$ 를 포함하는 문장은 변수가 정해짐에 따라 명제가 되는데, 이런 문장을 조건이라고 한다.

- 예시 

    변수 $x$ 를 포함하는 문장 "$x$ 는 $6$ 의 약수이다." 는 $x$ 가 초기화됨에 따라 명제가 되므로 조건이다.

# Set

!!! def "집합(set)"

    어떤 기준에 부합하는 대상들의 모임이다.

- 어떤 대상이 특정 집합에 속해있으면 그 대상을 집합의 원소라고 한다. 

- 원소 $a$ 가 집합 $A$ 에 속해있으면 

    $$ a \in A $$

    로 표현하고 원소 $a$ 가 집합 $A$ 에 속해있지 않으면 

    $$ a \not \in A $$

    로 표현한다.

- 1895년 칸토어가 집합론을 처음 발표했을 때 그가 내린 집합의 정의는 "직관이나 사고를 통해 명확히 구별할 수 있는 대상을 하나의 전체로 묶어 놓은 것"이다. 

- 예시 

    - 키가 $160$cm 이상인 학생들의 모임

    - 대한민국 국적을 가진 사람들의 모임

- 집합은 다음 $3$ 가지 방법으로 표현할 수 있다.

    1. 원소나열법 : $\{ \}$ 안에 집합의 모든 원소를 나열하는 것이다. 

        - 예시 

            $A = \{ \text{재석, 명수, 준하, 하하, 세호, 세형}\}$

    2. 조건제시법 : $\{x|x \text{의 조건}\}$ 과 같이 모든 원소들의 공통된 성질을 제시하는 방법이다. 

        - 원소나열법으로 집합을 나타내기 어려운 경우 자주 사용된다. 

        - 예시 

            $A = \{x|x \text{ 는 대한민국 국적을 가진 사람 }\}$

    3. 벤다이어그램 : 도형을 통하여 집합을 나타내는 방법이다.

- 집합은 다음과 같이 분류된다.

    - 유한집합 : 원소의 개수가 유한한 집합이다. 

        - 유한집합 $A$ 의 원소의 개수는 $n(A)$ 로 나타낸다. 

    - 무한집합 : 원소의 개수가 무한한 집합이다. 

    - 공집합 : 원소가 하나도 없는 집합이다.

        - 공집합은 $\emptyset$ 으로 표시한다.

!!! def "진리집합(truth set)"

    변수 $x$ 를 포함하는 조건을 참이되게 하는 변수 $x$ 의 집합이다.

- 예시 

    변수 $x$ 에 대한 조건 "$x$ 는 $6$ 의 약수이다." 의 진리집합은 

    $$ P = \{x:x\text{는 6 의 약수} \} $$

    이다. 이때 "$x \in P$" 와 "$x$ 는 $6$ 의 약수" 는 같다.

- 조건은 이미 존재하는 집합을 상정하고 그 집합에 특정 조건을 가하여 얻은 부분집합으로 구성하는 경우가 많다. 

    만약 전체집합을 $U$ 로 가정하는 경우 조건 $p(x)$ 를 집합 $U$ 에서 정의했다고 한다.

    - 예시 

        변수 $x$ 에 대한 조건 "$x$ 는 $6$ 의 약수이다." 은 자연수 집합 $\mathbb{N}$ 을 상정하고 정의된 것이므로 진리집합을 더 엄밀하게 쓰면

        $$ P = \{x \in \mathbb{N}:x\text{는 6 의 약수} \} = \{1,2,3,6\}$$

        이 된다.

!!! def "집합의 상등(set equality)"

    조건 $p$ 의 진리집합 $A$, 조건 $q$ 의 진리집합 $B$ 에 대하여 다음 동치조건이 성립하면 $A = B$ 라 한다.

    - $p \iff q$
    
    - $x \in A \iff x \in B$

- 두 집합이 서로 같다는 것은 서로가 서로의 부분집합이라는 것이다. 임의의 두 집합 $A, B$ 가 서로 같다는 것은 $A \subset B$ 와 $B \subset A$ 를 만족한다는 것이고 $A = B$ 로 표현한다.

- $x \in A$ 는 조건 $p$ 를 참이되게 하는 $A$ 의 원소 $x$ 에 대한 것이므로 참이 된 조건 $p$ 를 뜻한다. 

    그러므로 $x \in A$ 라는 표기는 참과 거짓이 정해졌으므로 더 이상 조건이 아니라 명제를 뜻한다.

!!! def "대우명제(Contraposition)"

    $p \to q$ 의 대우는 $\lnot q \to \lnot p$ 이다.

- 조건 $p(x)$ 의 진리집합 $P$ 에 대하여 명제 "어떤 $x$ 에 대하여 $p(x)$ 이다." 는 어떤 $x$ 에 대하여 $p(x)$ 가 참이되게 하는 $x$ 가 하나 이상 있다는 뜻이다. 그러므로 이 명제는

    $$ P \neq \emptyset $$

    와 같다. 이것을 부정하면 $P = \emptyset$ 인데, 이것은 곧 $P ^{c} = U$ 이므로 

    $$ U = P ^{c} = \{x|\lnot p(x)\} $$

    이고, 이것을 말로 설명하면 "임의의 $x$ 에 대하여 $\lnot p(x)$ 이다." 이다.

    그러므로 $\lnot [\text{어떤 x 에 대하여 p(x)}] \equiv \text{임의의 x 에 대하여} \lnot  \text{p(x)}$ 즉, 

    $$ \lnot [\exists x, p(x)] \equiv [\forall x, \lnot p(x)] $$

    이다. 마찬가지로

    $$ \lnot [\forall x, p(x)] \equiv [\exists  x, \lnot p(x)] $$

    이다.

    - 예시 

        "임의의 $a < 0$ 에 대하여 $x \geq a$ 이다." 는 변수 $x$ 에 관한 조건인데, 이것의 대우명제는 "$x<a$ 인 음수 $a<0$ 이 존재한다." 이다.

!!! def "부분집합(subest)"

    조건 $p$ 의 진리집합 $A$, 조건 $q$ 의 진리집합 $B$ 에 대하여 다음 동치조건을 만족하는 $A$ 를 $B$ 의 부분집합이라 한다.

    - $p \to q$
    
    - $x \in A \to x \in B$
    
- **$A$ 가 $B$ 의 부분집합이라는 것을 $A \subset B$ 라고 표기한다.**

- 집합 $A$ 의 모든 원소가 집합 $B$ 에 속하면 집합 $A$ 는 집합 $B$ 의 부분집합이다. 따라서 모든 집합은 자기 자신의 부분집합이다. 이것은 $A \subset A$ 로 표현된다. 

- 공집합은 모든 집합의 부분집합이다. 이것은 $\emptyset \subset A$ 로 표현된다. 

- $A$ 가 $B$ 의 부분집합이라는 것을 $A \subset B$ 이라고 표현한다. 

- $A$ 가 $B$ 의 부분집합이 아니라는 것을 $A \not \subset B$ 이라고 표현한다. 

- 예시 

    세 집합 $A, B, C$ 가 $A = \{a, b, c\}, B = \{a, b, c, d, e\}, C = \{d, e, f, g\}$ 일 때 집합 $A$ 의 원소가 모두 $B$ 에 속하지만 $C$ 의 원소가 $B$ 에 속하지는 않는다. 따라서 다음이 성립한다. 

    $$ A \subset B $$

    $$ C \not \subset B $$

!!! def "진부분집합(proper subset)"

    집합 $A, B$ 에 대하여 $A \neq B \land A \subset B$ 이면 $A$ 를 $B$ 의 진부분집합이라고 한다.

!!! def "여집합(complement set)"

    집합 $A$ 에 대하여 $A ^{c}=\{x:x \not \in A\}$ 를 $A$ 의 여집합이라고 한다.

- 조건 $p$ 의 진리집합이 $P$ 이면 그 부정 $\lnot p$ 의 진리집합은 $P ^{c}$ 이다.

- 집합 $A$ 에 대하여 다음이 성립한다.

    1. $(A ^{c})^{c} = A$

    - 증명 

        $$ x \in (A ^{c})^{c} \iff \lnot (x \in A ^{c}) \iff \lnot (\lnot x \in A) \iff x \in A $$

!!! def "공집합(empty set)"

    원소가 없는 집합 $\emptyset$ 이다.

- 전체집합 $U$ 에 대하여 다음이 성립한다.

    - $\emptyset ^{c} = U, U ^{c} = \emptyset$

    - $A \cup A ^{c} = U, A \cap A ^{c} = \emptyset$

!!! def "집합족(family of sets)"

    집합을 원소로 하여 구성된 집합이다.

- 집합 $X$ 속의 집합족이란 $X$ 의 부분집합으로 이루어진 집합이다. 

    즉, $X$ 속의 집합족은 $X$ 의 멱집합 $\mathcal{P}(X)$ 의 부분집합 $\mathcal{F} \subseteq  \mathcal{P}(X)$ 이다.

- 예시 

    집합 $\{\{2, \{3\}\}, \{1\}, \{5,6\}\}$ 은 모든 원소가 집합이므로 집합족이다.

    임의의 집합 $X$ 에 대하여 공집합 $\emptyset$ 과 $X$ 의 멱집합 $\mathcal{P}(X)$ 은 $X$ 속의 집합족이다.

!!! def "서로소인 집합족(disjoint family of sets)"

    집합족 $\mathcal{A} = \{A_i : i \in I\}$ 가 다음을 만족하면 서로소인 집합족이라 한다.

    $$ i,i \in I, i \neq j \implies A_i \cap A_j = \emptyset $$

- 서로소인 집합족의 합집합을 

    $$ \bigsqcup_{i \in I}^{}A_i $$

    로 표현한다.

## Union

!!! def "합집합(union)"

    두 집합 $A, B$ 에 대하여 
    
    $$ A \cup B = \{x:x \in A \lor x \in B\} $$
    
    이다.

- 정의에 따라 조건 $p, q$ 의 진리집합 $P, Q$ 에 대하여 조건 $p \lor q$ 의 진리집합은 $P \cup Q$ 이다.

- 예시 

    $$ \{1,2,3\}\cup \{3,4\}=\{1,2,3,4\} $$

    이다.

    $$ A \cup B \cup C = \{x : x \in A \lor x \in B \lor x \in C\} $$

    이다.

- 가산 개의 집합의 합집합

    자연수 개수만큼 무한히 많은 집합을 다음과 같이 일렬로 나열 가능하다면,

    $$ A, B, C, D , \dots $$

    다음과 같이 이들에게 자연수를 매길 수 있다. 

    $$ A_1, A_2, A_3, A_4, \dots $$

    이때 이것들의 합집합을 다음과 같이 표기한다. 

    $$ A_1 \cup A_2 \cup \dots = \bigcup_{i=0}^{\infty}A_i =\bigcup_{i \in \mathbb{N}}^{}A_i := \{x: \exists i \in \mathbb{N}, x \in A_i\} $$

- 임의의 첨수족의 합집합

    자연수 $\mathbb{N}$ 으로 번호를 매기는 것은 과하거나(유한 개의 집합들), 적당하거나(자연수 개수만큼 많은 집합들), 부족(비가산 개의 집합들)할 수 있다. 
    
    그러므로 적당한 첨수 $i \in I$ 를 부여받은 집합 $A_i$ 들의 합집합(적어도 한 집합의 원소인 대상들의 집합)을 다음과 같이 표기할 수 있다.

    $$ \bigcup_{i \in I}^{}A_i := \{x : \exists i \in I, x \in A_i\} $$

    - 예시 

        만일 $I = \{1,2\}$ 이면 집합족은 $\mathcal{A} = \{A_1, A_2\} = \{A_i : i \in \{1,2\}\}$ 이고 합집합은 

        $$ \bigcup_{i \in I}^{} A_i = \bigcup_{}^{}\{A_i : i \in I\} = \bigcup_{}^{}\mathcal{A} = \bigcup_{}^{}\{A \in \mathcal{A}\} = \bigcup_{}^{}\{X \in \mathcal{A}\} = A_1 \cup A_2 $$

        이다.

- 임의의 합집합 

    집합족 $\mathcal{M}$ 의 합집합은 그에 속하는 집합들의 모든 원소를 합쳐놓은 집합

    $$ \bigcup_{}^{}\mathcal{M} = \bigcup_{A \in \mathcal{M}}^{} A := \{x : \exists A \in \mathcal{M}, x \in A\} $$

    이다. 이는 가산 개의 집합의 합집합과 임의의 첨수족의 합집합을 모두 포함하는 일반적인 정의이다.

- 예시 

    각 양수 $r>0$ 에 대하여 $A_r = \{x \in \R : x \geq r\}$ 이라 두면 

    $$ \bigcup_{r>0}^{} A_r = \{x \in \R : x > 0\} $$

    이 된다. $A = \{x \in \R : x > 0\}$ 라 두면 각 $r>0$ 에 대하여 $A_r \subset A$ 이므로 $\bigcup_{r>0}^{}A_r \subset A$ 이다. 역으로 $A \subset \bigcup_{r>0}^{}A_r$ 을 증명하는 것은 

    $$ x>0 \implies \exists r > 0 \text{ s.t. } x \geq r $$

    을 증명하는 것이다. $r = x$ 라 두면 $0 < r \leq x$ 이므로 $A \subset \bigcup_{r>0}^{}A_r$ 이 성립하므로 $A = \bigcup_{r>0}^{}A_r$ 이다. 

    사실 양수 전체의 집합을 $P$ 로 두고 $\bigcup_{r \in P}^{}A_r$ 와 같이 표현해야 하지만, 관례상 $\bigcup_{r>0}^{}A_r$ 와 같이 쓴다.

## Intersection

!!! def "교집합(intersection)"

    두 집합 $A, B$ 에 대하여 
    
    $$ A \cap B = \{x:x \in A \land x \in B\} $$
    
    이다.

- 합집합과 교집합은 다음 성질을 갖는다.

    - $A \cup \emptyset  = A, A \cap \emptyset = \emptyset$

    - $A \cup B  = B \cup  A, A \cap B = B \cap A$

    - $A \cup (B \cup C)  = (A \cup B) \cup C, A \cap (B \cap C) = (A \cap B) \cap C$

    - $A \cup A = A, A \cap A =A$

    - $A \cap (B \cup C) = (A \cap B) \cup (A \cap C), A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$

    - $(A \cup B) ^{c} = A ^{c} \cap B ^{c}, (A \cap B)^{c}=A ^{c}\cup B ^{c}$

        - 증명 

        $$ x \in (A \cup B) ^{c} \iff \lnot (x \in A \lor x \in B) $$

        $$ \iff (x \not \in A) \land (x \not \in B) \iff (x \in A ^{c}) \land (x \in B ^{c}) $$

        $$ \iff x \in A ^{c} \cap B ^{c} $$

- 정의에 따라 조건 $p, q$ 의 진리집합 $P, Q$ 에 대하여 조건 $p \land q$ 의 진리집합은 $P \cap Q$ 이다.

- 집합 $A_1,A_2,A_3,A_4,A_5$ 의 교집합은 $A_1 \cap A_2 \cap A_3 \cap A_4 \cap A_5$ 으로 나타낼 수 있는데, 이것을 

    $$ \bigcap_{i=1}^{5}A_i $$

    로 나타낼 수 있다. 이때 

    $$ x \in \bigcap_{i \in I}^{}A_i \iff \forall i \in I, x \in A_i $$

    가 성립한다.

- 집합족 $\mathcal{A}$ 의 교집합은 $\mathcal{A}$ 의 모든 원소에 동시에 속하는 대상으로 이루어진 집합 

    $$ x \in \bigcap_{}^{}\mathcal{A} \iff \forall A \in \mathcal{A}, x \in A $$

    이다.

- 집합족에 대한 합집합과 교집합은 전체집합 $U$ 안에 있는 집합 $A_i$ 들에 대하여 다음이 성립한다. 

    - $\displaystyle \bigg (\bigcup_{i \in I}^{}A_i\bigg ) ^{c} = \bigcap_{i \in I}^{} A_i ^{c}$

        - 증명

        $$\displaystyle \bigg (\bigcup_{i \in I}^{}A_i\bigg ) ^{c} = \bigcap_{i \in I}^{} A_i ^{c} \iff x \not \in \bigcup_{i \in I}^{} A_i$$

        $$ \iff \lnot (\exists i \in I, x \in A_i) \iff \forall  i \in I, x  \not \in A_i$$

        $$ \iff \forall  i \in I, x  \in A_i ^{c} \iff x \in \bigcap_{i \in I}^{} A_i ^{c} $$

    - $\displaystyle \bigg (\bigcap_{i \in I}^{}A_i\bigg ) ^{c} = \bigcup_{i \in I}^{} A_i ^{c}$

    - $\displaystyle  A \cap \bigg (\bigcup_{i \in I}^{}A_i\bigg ) = \bigcup_{i \in I}^{}(A \cap A_i)$

    - $\displaystyle  A \cup \bigg (\bigcap_{i \in I}^{}A_i\bigg ) = \bigcap_{i \in I}^{}(A \cup A_i)$

## Ordered pair

!!! def "순서쌍(ordered pair, 2-tuple)"

    두 개의 수학적 대상 $a,b$ 를 순서를 정하여 짝지어 나타낸 쌍
    
    $$ (a, b) := \{\{a\}, \{a,b\}\} $$
    
    이다.

- 두 원소 $a,b$ 로 이루어진 집합은 $\{a,b\}=\{b,a\}$ 이지만, 순서쌍은 $a \neq b$ 인 한

    $$ (a,b) \neq (b,a) $$

    이다.

- 곱집합, 함수, 이항관계 등이 순서쌍을 이용해 정의된다.

- 순서쌍의 성분은 스칼라, 벡터, 다른 순서쌍일 수도 있다.

- 순서쌍으로 n-tuple 을 귀납적으로 정의할 수 있다. 

    - 예시 

        $3$-튜플 순서쌍을 $(a,b,c) := (a, (b, c))$ 로 정의할 수 있다.

- 순서쌍의 가장 기본적인 성질은 두 순서쌍이 같을 필요충분조건이 두 성분이 각각 같은 것이라는 것이다. 즉, 

    $$ (a,b) = (c,d) \iff (a = c) \land (b = d) $$

- 보통 순서쌍을 $(a,b)$ 로 표현하지만 개구간과 혼동하지 않기 위하여 $\big <a, b\big >$ 로 나타내기도 한다.

!!! def "정리 1.1.1"

    $(a,b) = (c,d) \implies a=c, b=d$ 

- 증명 

    $a=b$ 인 경우 
    
    $$\{\{a\}\} = (a, b) = (c,d) = \{\{c\},\{c,d\}\}$$ 
    
    에서 $\{a\}=\{c\}=\{c,d\}$ 이므로 $a=b=c=d$ 이다.

    $a \neq b$ 인 경우 $\{a,b\}$ 는 두 원소의 집합이므로 한 원소의 집합이 아니다. 그러므로 

    $$ \{c\} \in \{\{c\},\{c,d\}\} = \{\{a\}, \{a,b\}\} $$

    에서 명백하게 $\{c\} \neq \{a,b\}$ 이다. 그러므로 당연히 

    $$ \{c\}=\{a\} \implies a = c $$

    이다. 마찬가지로

    $$ \{a,b\} \in \{\{a\}, \{a,b\}\} = \{\{c\}, \{c,d\}\} $$

    에서 명백하게 $\{a,b\}\neq \{c\}$ 이다. 그러므로 당연히 

    $$ \{a,b\} = \{c,d\} $$

    인데 $b \in \{c,d\} = \{a,b\}$ 로부터 $b=c$ 또는 $b=d$ 이다.

    그런데 $b=c$ 이면 $a=c=b$ 이므로 모순이다. 그러므로 $b=d$ 이다.

## Product Set

!!! def "곱집합(product set) 또는 데카르트 곱(cartesian product)"

    임의의 집합족 $\{X_i : i \in I\}$ 에 대한 곱집합 $\prod_{i \in I}^{}X_i$ 를 

    $$ \prod_{i \in I}^{}X_i = \bigg \{f \in (\bigcup_{i \in I}^{}X_i) ^{I} : f(i) \in X_i, i \in I \bigg \} $$

    와 같이 정의하고, 어느 함수 $f \in \prod_{i \in I}^{}X_i$ 를 곱집합의 원소

    $$ (x_i) _{i \in I} $$

    라고 한다.

- 물론 어느 함수 $f$ 는 실제로는 곱집합 $I \times \bigcup_{i \in I}^{}X_i$ 의 부분집합으로써

    $$ \{(i_1, x_1), (i_2, x_2), \dots, (i_n, x_n), \dots\} $$

    와 같은 $I$ 에서 $\bigcup_{i \in I}^{}X_i$ 로 가는 함수지만, 이것을 

    $$ (x_1,  x_2, \dots,  x_n, \dots) $$

    으로 표기하자고 약속하는 것이다.

- 위 정의에서 $(\bigcup_{i \in I}^{}X_i) ^{I}$ 는 $I$ 에서 $\bigcup_{i \in I}^{}X_i$ 로 가는 함수 전체의 집합을 뜻한다.

- 임의의 $i \in I$ 에 대하여 $X_i = X$ 이면 $\prod_{i \in I}^{}X_i = X ^{I}$ 이다. 

- 예시 

    $\R$ 을 $n \in \N$ 개 곱한 곱집합 $\R ^{n}$ 에서 $n = \{0,1,2, \dots, n-1\}$ 이므로 $\R ^{n}$ 는 $n \to \R$ 인 함수 전체의 집합

    $$ \prod_{i=1}^{n}\R =  \{f \in \R ^{n} : f(i) \in \R, i \in n  \} $$
    
    이다. 그리고 $n = \{0,1,2,\dots,n-1\}$ 을 $\R$ 로 대응시키는 어느 함수

    $$ i \mapsto a_i, \quad i = 0,1,2,\dots,n-1 $$

    는 실제로

    $$ \{(0, a_0), (1, a_1), (2, a_2), \dots, (n-1, a _{n-1})\} $$

    와 같은 곱집합 $n \times X$ 의 부분집합이지만,

    $$ (a_0, a_1, a_2, \dots, a _{n-1}) $$

    라고 표시한다.

- 두 집합 $A,B$ 의 곱집합 $A \times B$ 는 
    
    $$ A \times B := \{(a,b):a \in A, b \in B\} $$
    
    이다.

    - 이때 다음이 성립한다. 

        $$ A \times (B \cup C) = (A \times B) \cup (A \times C) $$

        $$ A \times (B \cap C) = (A \times B) \cap (A \times C) $$

        $$ (A \times B) \cap (C \times D) = (A \cap C) \times (B \cap D) $$

- 유한개의 집합 $A_1, A_2, \dots, A_n$ 의 곱집합 $A_1 \times A_2 \times \dots \times A_n$ 은 

    $$ A_1 \times A_2 \times \dots \times A_n = \{(a_1, a_2, \dots, a_n) : a_i \in A_i\} $$

    이다. 이것을 간단하게 표기하여 집합 $A, I$ 에 대하여 $A$ 의 $I$ 번 곱집합 $A ^{I}$ 는 

    $$ A ^{I} = \{(a_i) _{i \in I} : a_i \in A\} $$

    이다. 

- 예시 

    우리에게 익숙한 데카르트 공간 $\mathbb{R} ^{2}$, 즉 직교좌표계는 
    
    $$ \R ^{2} = \mathbb{R} \times \mathbb{R} = \{(x,y) : x, y \in \R \}$$
    
    로써 곱집합이다. 또한 공간좌표계는 

    $$ \R ^{3} = \mathbb{R} \times \mathbb{R} \times \R = \{(x,y, z) : x, y, z \in \R \}$$

    이다.

## Power set

!!! def "멱집합(power set)"

    주어진 집합의 모든 부분 집합으로 구성된 집합이다.

- 즉, 집합 $S$ 의 멱집합 $\mathcal{P}(S)$ 또는 $2 ^{S}$ 는

    $$ \mathcal{P}(S) := \{A: A \subseteq S\} $$

    이다.

- 예시 

    집합 \{x,y,z\} 의 멱집합 원소들의 부분 집합 관계는

    ![](https://upload.wikimedia.org/wikipedia/commons/e/ea/Hasse_diagram_of_powerset_of_3.svg)

    와 같은 헤세 도형으로도 표현할 수 있다.

# Function

!!! def "함수(function)"

    두 집합 $X, Y$ 의 곱집합 $X \times Y$ 의 부분집합 $f \subset X \times Y$ 가 
    
    1. $x \in X \to (x,y) \in f$ 를 만족하는 $y \in Y$ 가 존재한다.
    
    2. $(x, y_1) \in f, (x, y_2) \in f \to y_1 = y_2$
    
    을 만족하면 $X$ 에서 $Y$ 로 가는 함수라고 한다.

- $(x,y) \in f$ 일 때 

    $$f(x) = y \text{  또는  } f: x \mapsto y$$

    라고 쓴다.

- 집합 $X$ 를 $f$ 의 정의역, $Y$ 를 $f$ 의 공역이라고 하고, 

    $$ f: X \to Y $$

    라고 쓴다.

    - 앞으로 정의역과 공역은 항상 공집합이 아니라고 간주한다.

- $f: x \mapsto x, X \to Y$ 는 $f: X \to Y$ 가 함수이고 $(x, y) \in f$ 라는 뜻이다.

- 상황에 따라 "함수(function)" 를 "사상(mapping)", "변환(transformation)" 으로 부르기도 하는데 다 같은 뜻이다.

- 예시 

    데카르트 공간 $\mathbb{R} ^{2}$, 즉 직교좌표계의 부분집합 

    $$ x \in X, y \in Y, x ^{2}+y ^{2} = 4 $$

    는 함수가 아니다. $(0, -2), (0, +2)$ 가 이 관계에 속하는데 이는 함수의 두번째 조건

    2. $(x, y_1) \in f, (x, y_2) \in f \to y_1 = y_2$

    을 위배하기 때문이다.

!!! def "함수의 상등(function equality)"

    함수 $f: X \to Y$ 와 $g: X \to Y$ 가 같은 함수일 필요충분조건은 

    $$ f(x) = g(x), x \in X $$

    이다. 

- 증명 

    $f = g$ 이면 임의의 $x \in X$ 에 대하여 

    $$ y = f(x) \iff (x, y) \in f \iff (x, y) \in g \iff y = g(x) $$

    이므로 $f(x) = g(x)$ 이다.

    반대로 임의의 $x \in X$ 에 대하여 $f(x) = g(x)$ 이면 

    $$ (x,y) \in f \iff y = f(x) \iff y = g(x) \iff (x,y) \in g $$

    이므로 $f=g$ 이다. ■ 

## Identity Function

!!! def "항등함수(identity function)"

    집합 $X$ 에 대하여 
    
    $$ \{(x_1, x_2) \in X \times X:x_1 = x_2\} $$
    
    로 주어진 함수를 $X$ 에서 정의된 항등함수
    
    $$ 1 _{X} : X \to X, x \mapsto x $$
    
    라 한다.

- 즉, 항등함수는 $x \in X$ 에 대하여

    $$ 1 _{X}(x) = x $$

    이다.

- 항등함수를 $1_X$ 로도 표기하고 $\text{ id }_X$ 로도 표기한다. 

!!! def "포함함수(inclusion function), 포함사상(inclusion map)"

    $A \subset X$ 일 때 
    
    $$ \{(a,a) \in A \times X : a \in A\} $$
    
    로 주어진 함수를 포함함수 
    
    $$ \iota _{A}:A \hookrightarrow X, x \mapsto x $$
    
    라고 한다.

- 즉 포함 함수란 정의역이 공역의 부분 집합이며, 정의역의 모든 원소를 자신으로 대응시키는 함수이다. 

- 모든 포함함수는 단사 함수이다. 

- 모든 단사 함수는 전단사 함수와 포함 함수의 합성이다.

!!! def "정리 1.2.1"

    두 함수 $f: X \to Y$ 와 $g: X \to Y$ 에 대하여 

    $$ f = g \iff x \in X, f(x) = g(x) $$

    이다.

- 즉, 두 함수 $f,g$ 가 같은 함수일 필요충분조건이 $x \in X$ 에 대하여 $f(x)=g(x)$ 라는 것이다.

- 증명 

    $f = g$ 이면 (*이는 곱집합의 부분집합으로써의 $f$ 와 $g$ 가 서로 같다는 것이다. 즉, 단지 두 집합이 서로 같다는 것이다.*) $\forall x \in X$ 에 대하여 

    $$ y = f(x) \iff (x,y) \in f \iff (x,y) \in g \iff y = g(x) $$

    이므로 $f(x) = g(x)$ 이다. 

    역으로 $\forall x \in X$ 에 대하여 $f(x) = g(x)$ 이면 (*이는 두 함수 $f, g$ 의 상이 서로 같다는 것이다. 즉, 두 함수의 함숫값이 같다는 거지.*)

    $$ (x, y) \in f \iff y = f(x) \iff y = g(x) \iff (x, y) \in g $$

    이므로 $f = g$ 이다. 

## Restriction

!!! def "함수의 제한(restriction)"

    함수 $f: X \to Y$ 의 정의역 $X$ 의 부분집합 $A$ 에 대한 합성함수 $f \circ \iota _{A}:A \to Y$ 를 $f$ 의 제한 
    
    $$ f | _{A} : A \to Y $$
    
    이라고 한다.

- 그냥 $f$ 의 대응 규칙을 유지한 채 정의역만 $A$ 로 줄인 함수이다.

## Composite Function

!!! def "합성함수(composite function)"

    함수 $f: X \to Y$ 와 $g: Y \to Z$ 에 대한 합성함수 $g \circ f : X \to Z$ 는 
    
    $$ (g \circ f)(x) = g(f(x)), x \in X $$
    
    이다.

- $f$ 와 $g$ 는 각각 곱집합 $X \in Y$ 와 $Y \times Z$ 의 부분집합이므로 

    $$ g \circ f = \{(x, z) \in X \times Z: (\exists y) ((x, y) \in f, (y, z) \in g)\} $$

    와 같이 정의할 수도 있다. 이는 $(x, y) \in f, (y, z) \in g$ 인 $y$ 가 존재한다는 말이다.

## Composite Function satisfies Associativity

!!! def ""

    함수의 합성은 결합법칙을 만족한다. 즉, 함수 $f: X \to Y, g: Y \to Z, h:Z \to W$ 에 대하여 

    $$ h \circ (g \circ f) = (h \circ g) \circ f $$

    이다. 

- 증명 

    합성함수의 정의에 의하여 각 $x \in X$ 에 대하여 

    $$ h \circ (g \circ f)(x) = h(g \circ f(x)) = h(g(f(x))) = h \circ g(f(x)) = (h \circ g) \circ f(x) $$

    이다. 그러므로 

    $$ h \circ (g \circ f) = (h \circ g) \circ f $$

    이다. ■ 

## Injection

!!! def "단사함수(injection, one-to-one function)"

    함수 $f:X \to Y$ 가 

    $$ x_1, x_2 \in X, f(x_1)=f(x_2) \implies x_1 = x_2 $$

    를 만족하면 단사함수이다.

- 즉, 단사 함수는 다음과 같이 정의역의 서로 다른 원소를 공역의 서로 다른 원소로 대응시키는 함수이다. 

    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Injection.svg/1024px-Injection.svg.png" width="50%" height="auto">

!!! def "정리 1.2.2"

    함수 $f: X \to Y$ 에 대하여 다음은 동치이다. 

    1. $f$ 는 단사함수이다. 

    2. $g \circ f = 1 _{X}$ 를 만족하는 함수 $g: Y \to X$ 가 존재한다. 

- 즉, 이 정리는 $x$ 를 $y$ 로 보내면 그 $y$ 를 다시 $x$ 로 보낼 수 있음을 말하고 있다. 전사함수라면 이렇게 할 수 없을 수도 있는데, $y$ 에 대응되는 $x$ 가 유일하지 않을 수도 있기 때문이다. 

- 증명 

    $g \circ f = 1 _{X}$ 를 만족하는 $g$ 가 있으면 

    $$ f(x_1) = f(x_2) \implies x_1 = (g \circ f)(x_1) = (g \circ f)(x_2) = x_2 $$

    이므로 $f$ 가 단사함수의 조건을 만족하여 단사함수가 된다.

    이제 역으로 $f$ 가 단사함수라면 $g \circ f = 1 _{X}$ 인 함수 $g: Y \to X$ 가 존재함을 보이기 위하여

    $$ B = \{y \in Y: f(x) = y \text{ 를 만족하는 } x \in X \text{ 가 존재한다}\} $$

    라고 두자. 즉, $B = \text{ran} f$ 이다. $y \in B$ 이면 $f$ 가 단사함수라는 가정에 의하여 $f(x) = y$ 를 만족하는 $x \in X$ 가 유일하게 존재하는데, 이때 함수 $g$ 를 $g(y) = x$ 라고 정의하자. 만약 $y \not \in B$ 이면 $g(y)$ 는 아무렇게나 정의하자. 

    가령 $X$ 의 한 원소 $x_0 \in X$ 에 대하여 

    $$ g(y) = \begin{cases} x, &y \in B, y = f(x) \\ x_0,& y \not \in B\\ \end{cases} $$

    라고 정의하는 것이다. 그러면 

    $$ g \circ f = 1 _{X} $$

    임이 바로 확인된다. 왜냐하면 어차피 정의역의 원소 $x_0$ 에 대응되는 치역의 원소 $y$ 가 존재하지 않는다면 이 원소 $x_0$ 에 대한 함수 $f$ 는 정의되지 않기 때문에 결국 우리는 $g(y) = x$ 만 생각하면 되기 때문이다. 그렇다면 $g(f(x)) = x$ 이므로 $g \circ f$ 는 항등함수 $1 _{X}$ 가 된다. ■ 

## Surjection

!!! def "전사함수(surjection, onto)"

    함수 $f: X \to Y$ 가 성질

    $$ \forall y \in Y, \exists x \in X, f(x) = y $$

    를 만족하면 이를 전사함수라 한다.

- 예시 

    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Surjection.svg/200px-Surjection.svg.png" width="50%" height="auto">

!!! def "정리 1.2.3"

    함수 $f: X \to Y$ 에 대하여 다음은 동치이다. 

    1. $f$ 는 전사함수이다. 

    2. $f \circ g = 1 _{Y}$ 를 만족하는 함수 $g: Y \to X$ 가 존재한다. 

- 즉, 이 정리는 $y$ 를 $x$ 로 보내면 그 $x$ 를 다시 $y$ 로 보낼 수 있음을 말하고 있다. 단사함수라면 이렇게 할 수 없을 수도 있는데, $y$ 에 대응되는 $x$ 가 존재하지 않을 수도 있기 때문이다. 

- 증명 

    먼저 $f \circ g = 1 _{Y}$ 를 만족하는 함수 $g: Y \to X$ 가 존재한다고 가정하자. 각 $y \in Y$ 에 대하여 $x=g(y)$ 라 두면 $f \circ g$ 이 항등함수라고 하였으므로

    $$ f(x) = f(g(y)) = y $$

    이다. 그러면 이 관계에 의하여 임의의 $y \in Y$ 가 함수 $g$ 와 $f$ 를 통하여, 즉 정의역의 원소 $x$ 를 통하여 다시 $y$ 로 대응되므로 전사함수의 조건이 성립하여 $f$ 가 전사함수가 된다. 

    이제 역으로 $f$ 가 전사함수이면 $f \circ g = 1 _{Y}$ 인 $g$ 가 존재함을 보이기 위하여 

    $$ A_y = \{x \in X: f(x) = y\} $$

    라고 두면 $A_y \neq \varnothing$ 이다. 왜냐하면 $f$ 가 전사함수이므로 $Y$ 의 모든 원소가 $X$ 의 적당한 원소로 대응되기 때문이다. 이때 각 $y \in Y$ 에 대하여 $A_y$ 의 원소 $x$ 를 택하여 이 $x$ 를 $x = g(y) \in X$ 라 두면 

    $$ f(g(y)) = y $$

    이다. ■ 

- 위 증명에서 $A_y$ 의 원소를 하나 택한다고 하였는데 이렇게 하나씩 택하는 것이 가능한가에 대한 문제는 좀더 신중한 접근이 필요하다. 한편 이것이 가능하다고 가정하는 것이 선택공리이다. 

## Bijection

!!! def "전단사함수(bijection, one-to-one correspondence)"

    두 집합 $X, Y$ 사이의 함수 $f: X \to Y$ 에 대하여 성질 

    $$ \forall y \in Y, \exists ! x \in X, f(x) = y $$
    
    을 만족하는 함수이다. 

- 즉, 전사이면서 동시에 단사인 함수를 전단사함수라 한다.

- 예시 

    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Bijection.svg/220px-Bijection.svg.png" width="50%" height="auto">

## Inverse Function

!!! def "역함수(inverse function)"

    함수 $f: X \to Y$ 에 대하여 
    
    $$ g \circ f = 1 _{X}, f \circ g = 1 _{Y} $$
    
    인 $g: Y \to X$ 가 존재하면 이를 $f$ 의 역함수라 한다.

- $f$ 의 역함수 $g$ 를 $f ^{-1} : Y \to X$ 로 표기한다.

- 예시 

    함수 $f: \N \to \mathbb{Z}$ 를
    
    $$f(2n) = -n, \qquad f(2n-1) = n$$

    이라 정의하면 그 역함수 $g: \mathbb{Z} \to \N$ 는 

    $$ g(n) = 2n-1, g(-n) = 2n $$

    가 된다. 

!!! def ""

    역함수는 유일하다. 

- 증명 

    $g$ 와 $h$ 가 $f$ 의 역함수라면 
    
    $$ g = 1 _{X} \circ g = (h \circ f) \circ g = h \circ (f \circ g) = h \circ 1 _{Y} = h \tag{1} $$

    가 된다.

!!! def ""

    함수가 역함수를 가지면 그 함수는 전단사함수이다. 

- 증명 

    [정리 1.2.2](#5869db153) 와 [정리 1.2.3](#d9b0737d6) 에 의하여 증명이 된다.

- 함수 $f: X \to Y$ 가 전단사 함수이면 $h \circ f = 1 _{X}$ 인 $h: Y \to X$ 와 $f \circ g = 1 _{Y}$ 인 $g: Y \to X$ 가 존재하는데, $(1)$ 에 의하여 $g = h$ 가 되어 $f$ 의 역함수가 된다. 

- 함수 $f: X \to Y$ 와 $A \subset X, B \subset Y$ 에 대하여 

    $$ f ^{-1}(B) = \{x \in X:f(x) \in B\} $$

    $$ f (A) = \{f(x) \in Y:x \in A\} $$

    라 정의하자. 집합 $f ^{-1}(B)$ 를 $B$ 의 역상이라 하고 $f(A)$ 를 $A$ 의 상이라 한다.

    이때 $f$ 가 전사일 필요충분조건은 $f(X)=Y$ 이다.

!!! def "정리 1.2.4"

    함수 $f: X \to Y$ 에 대하여 다음은 동치이다. 

    1. $f$ 는 전단사 함수이다.

    2. $f$ 의 역함수가 존재한다. 

- 한편 정의역이나 공역을 축소하여 전단사함수가 되게 한 후 역함수를 정의할 수도 있다. 삼각함수의 역함수가 이런 식으로 정의된다. 

!!! def "따름정리 1.2.5"

    두 집합 $X, Y$ 에 대하여 다음은 동치이다. 

    1. 단사함수 $f: X \to Y$ 가 존재한다. 

    2. 전사함수 $g: Y \to X$ 가 존재한다. 

- 증명 

## Binary Operation

!!! def "이항연산(binary operation)"

    함수 $X \times X \to X$ 이다.

- 자연수의 덧셈이나 곱셈 등은 모두 이항연산이다.

## Set of All Functions

!!! def "함수 전체 집합(set of all functions)"

    집합 $X$ 에서 $Y$ 로 가는 함수 전체의 집합을 $Y ^{X}$ 라고 한다.

- 예시 

    집합 $X$ 와 $\forall A \in 2 ^{X}$ 에 대하여 $\Phi (A) \in \{0,1\}^{X}$ 를 

    $$ \Phi (A)(x) = \begin{cases}
    1 &x \in A\\
    0 &x \not \in A\\
    \end{cases} 
    $$

    로 정의하자. 또 임의의 함수 $f \in \{0,1\}^{X}$ 에 대하여 $X$ 의 부분집합 $\Psi (f) \in 2 ^{X}$ 를 

    $$ \Psi (f) = \{x \in X : f(x) = 1\} $$

    라 정의하자. ▲ 

    그러면 임의의 $f: X \to \{0,1\}$ 에 대하여 

    $$ \Phi (\Psi (f))(x) = 1 \iff x \in \Psi (f) \iff f(x) = 1 $$

    이므로 $\Phi (\Psi (f)) = f$ 이다. 또한 임의의 $A \in 2 ^{X}$ 에 대하여 

    $$ x \in \Psi (\Phi (A)) \iff \Phi (A)(x) = 1 \iff x \in A $$

    이므로 $\Psi (\Phi (A))=A$ 이다. (*$\Psi(f)$ 는 $f$ 가 $1$ 이 되게 하는 정의역 집합인데, $\Psi (\Phi (A))$ 이므로 $\Phi (A)$ 가 $1$ 이 되게 하는 정의역 집합이다. 근데 $\Phi (A)$ 란 $x$ 가 $A$ 에 속하면 $1$ 이므로 결국 $A$ 의 원소들로 구성된다.*)

    그러므로 두 함수 

    $$ \Psi : 2 ^{X} \to \{0,1\} ^{X}, \quad \Psi : \{0,1\}^{X}\to 2 ^{X} $$

    는 서로 역함수이다.

## Characteristic Function

!!! def "특성함수(characteristic function) 또는 지시함수(indicator function)"

    임의의 $A \in \mathcal{P}(X)$ 에 대하여 $\chi_A \in \{0,1\}^{X}$ 를 
    
    $$ \chi_A(x) = \begin{cases} 1 &x \in A\\ 0 &x \not \in A\\ \end{cases} $$
    
    라고 정의하고 특성함수라 한다.

- 특정 집합에 특정 값이 속하는지 표시하는 함수이다. 특정 값이 집합에 속하면 $1$, 속하지 않으면 $0$ 의 값을 가진다. 

## Projection

!!! def "사영(projection)"

    각 $i \in I$ 에 대하여 함수 

    $$ \pi _i: \prod_{i \in I}^{}X_i \to X_i, f \mapsto f(i) $$

    이다.

- 이 정의에서 $f$ 란 [곱집합의 정의](#9f10c2d3d) 에서의 $f$ 를 뜻한다.

- 즉, $i \in I$ 에 대한 사영은 집합족 $\{X_i : i \in I\}$ 의 곱집합 $\prod_{i \in I}^{}X_i$ 에 존재하는 함수들 중 어느 함수를 입력하면, 그것을 그 함수의 $i$ 번째 사상으로 대응시킨다.

- 예시 

    $\R ^{n}$ 의 사영 $\pi _i$ 는 곱집합 $\R ^{n}$ 의 어느 한 원소

    $$ (a_1, a_2, \dots, a_n), \quad a_i \in \R $$

    를 입력하면 $i$ 번째 원소 $a_i$ 를 출력하는 함수이다.

# Equivalence Relation

!!! def "관계(relation)"

    집합족 $\{X_i\}_{i \in I}$ 위의 관계는 곱집합의 부분집합

    $$ R \subseteq \prod_{i \in I}^{}X_i $$

    이다.

- 이를 통해 순서수 $\alpha$ 에 대하여 집합 $X$ 위의 $\alpha$항 관계를 거듭제곱 집합의 부분집합

    $$ R \subseteq X ^{\times \alpha } $$

    로 정의한다.

- 예시 

    집합 $X$ 위의 영항관계(nullary relation) 은 $R \subseteq \{\cdot \}$ 즉, $R = \emptyset$ 이다.

    집합 $X$ 위의 단항관계(unary relation) 은 $R \subseteq X$ 이다.

    집합 $X$ 위의 이항관계(binary relation) 은 $R \subseteq X \times X$ 이다. 특히 이항관계에서 $(x, y) \in R$ 일 경우 $xRy$ 와 같이 자주 표기한다. 
    
    - 가령 집합 $\mathbb{N}$ 위의 이항관계 $+ \subseteq \mathbb{N} \times \mathbb{N}$ 에서 $(1, 2) \in \mathbb{N}$ 을 $1 + 2$ 로 표기한다.

    집합 $X$ 위의 삼항관계(ternary relation) 은 $R \subseteq X \times X \times X$ 이다. 
    
    - 프로그래밍 언어에서 $x = (condition) ? a : b;$ 와 같이 사용되기도 한다.
    
    집합 $X$ 위의 $n$항관계(n-ary relation) 은 $R \subseteq X ^{\times n}$ 이다. 이때 $(x_1, \dots, x_n) \in R$ 을 $R(x_1, \dots, x_n)$ 와 같이 표기한다.

- 두 집합 $X, Y$ 의 곱집합 $X \times Y$ 의 부분집합이다.

- 집합 $X$ 에 관계가 주어졌다는 것은 곱집합 $X \times X$ 의 부분집합이 주어졌다는 것이다.
    
- 예시 

    데카르트 공간 $\mathbb{R} ^{2}$, 즉 직교좌표계의 부분집합 

    $$ x \in X, y \in Y, x ^{2}+y ^{2} = 4 $$

    는 관계이다.

!!! def "동치관계(equivalence relation)"

    집합 $X$ 에 대한 관계 $R \subset X \times X$ 가 
    
    1. 임의의 $x \in X$ 에 대하여 $(x,x)\in R$ 이다.(reflexive relation)
    
    2. $(x, y) \in R$ 이면 $(y, x) \in R$ 이다.(symmetric relation)
    
    3. $(x, y) \in R$ 이고 $(y,z)\in R$ 이면 $(x, z) \in R$ 이다.(transitive relation)
    
    를 만족하면 $R$ 을 동치관계라 한다.

- 동치관계 $R \subset X \times X$ 의 원소 $(x, y) \in R$ 을 

    $$ x \sim y $$

    라고 쓴다.

- 동치관계의 조건을 다시 열거하면 다음과 같이 된다.
    
    $$ x \in X \to x \sim x $$

    $$ x \sim y \to y \sim x $$

    $$ x \sim y, y \sim z \to x \sim z $$

- 예시 

    "같다" 는 동치관계의 예시이다.

    "서로 평행이다", "서로 닮음이다" 도 동치관계의 예시이다.

## Equivalence Class

!!! def "동치류(equivalence class)"

    집합 $X$ 에 동치관계 $\sim$ 가 주어져 있을 때 각 $x \in X$ 에 대하여
    
    $$ [x] = \{z \in X: z \sim x\} $$
    
    를 $x$ 의 동치류라 한다.

- 예시 

    집합 $X = \{a,b,c\}$ 에 

    $$ R = \{(a,a), (b,b), (c,c), (a,b), (b,a)\} $$

    와 같은 동치 관계가 주어져있다고 하자. 그러면 

    $$ [a]=\{a,b\}, \qquad [b]=\{a,b\}, \qquad [c]=\{c\} $$

    이므로 집합 $X=\{a,b,c\}$ 가 집합족 

    $$ \{\{a,b\}, \{c\}\} $$

    으로 분할된다. 

!!! def ""

    $$ x \sim y \iff [x]=[y] $$
    
    $$ x \not \sim y \iff [x] \cap [y] = \varnothing $$

- 증명 

    $x \sim y$ 이면 동치관계의 성질 2), 3) 에 의하여 

    $$ z \in [x] \iff z \sim x \iff z \sim y \iff z \in [y] $$

    이다. 역으로 $[x] = [y]$ 이면 $x \sim x$ 이므로 $x \in [x] = [y]$ 가 되고 따라서 $x \sim y$ 임을 알 수 있다. 

    두번째 성질을 증명하기 위하여 

    $$ [x] \cap [y] \neq \varnothing \implies [x] = [y] $$

    임을 보이자. 만약 $z \in [x] \cap [y]$ 이면 $z \sim x, z \sim y$ 가 성립하고 따라서 $x \sim y$ 이다. $\forall x \in X, x \in [x]$ 이므로 성질 $(1)$ 에 의해 집합 $X$ 는 집합족

    $$ \{[x]:x \in X\} $$

    으로 분할됨을 알 수 있다. 

## Partition

!!! def "분할(partition)"

    집합 $X$ 의 공집합이 아닌 부분집합족 $\{A_i : i \in I\}$ 가 

    1. $X = \bigcup_{i \in I}^{}A_i$

    2. $\forall i,j \in I, A_i = A_j \lor A_i \cap A_j = \varnothing$

    를 만족하면 이를 $X$ 의 분할이라 한다. 

- 집합 $X$ 에 동치관계 $\sim$ 가 주어지면 자동적으로 $X$ 의 분할이 생김을 알 수 있는데, 이러한 분할을 

    $$ X/\sim $$

    라고 표시한다. 이 집합족을 몫집합이라고 한다.

- 만약 각 집합 $[x]$ 의 원소를 하나 택하여 $r_x$ 라 두고 $I = \{r_x:x \in X\}$ 라 두면 $\{[r]:r \in I\}$ 는 서로소인 집합족이 되고, 따라서 

    $$ X = \bigcup_{}^{}\{[r]:r \in I\} $$

    임을 알 수 있다. 

- 이제 거꾸로 집합 $X$ 의 분할 $\mathcal{P} = \{X_i : i \in I\}$ 가 주어졌을 때 동치관계를 이끌어내보자. $\forall x, y \in X$ 가 "$x, y \in X_i$ 인 $i \in I$ 가 존재한다" 를 만족할 때 $x \sim y$ 라고 정의하자. 그러면 $\sim$ 이 동치관계임을 바로 알 수 있다. 

    실제로 $x \in X$ 이면 분할의 정의 1) $X = \bigcup_{i \in I}^{}X_i$ 에 의하여 $x \in X_i$ 인 $i \in I$ 를 찾을 수 있고, 이에 따라 $x \sim x$ 가 성립하며, 이로써 동치관계의 조건 1) reflexive relation 이 성립한다.

    동치관계의 조건 2) symmetric relation 은 $x \sim y$ 로부터 $y \sim x$ 를 이끌어내면 증명되는데, $x, y \in X_i$ 인 $i \in I$ 가 존재하면, $y, x \in X_i$ 인 $i \in I$ 가 존재함은 자명하다. 

    그러면 이제 동치관계의 조건 3) transitive relation 을 보이기 위하여 $x \sim y, y \sim z$ 라 가정하자. 그러면 $x, y \in X_i$ 인 $i \in I$ 와 $y,z \in X_j$ 인 $j \in I$ 가 존재한다. 그런데 $y \in X_i \cap X_j$ 이므로 $X_i = X_j$ 이고, 이에따라 $x \sim z$ 이다. 

- 예시 

    정수 집합 $\mathbb{Z}$ 에 관계 

    $$ m \sim n \iff \exists k \in \N, m - n = 2k $$

    를 정의하면 동치관계가 됨을 바로 알 수 있다. 

    이때 $m$ 이 짝수면 $[m] = \{2n \in \N : n \in \N\}$ 가 되고, $m$ 이 홀수면 $[m] = \{2n+1 \in \N : n \in \N\}$ 가 된다. 따라서 

    $$ \mathbb{Z}/\sim\ = \{[x]:m \in \mathbb{Z}\} = \{[m]:m = 0, 1\} = \{[0], [1]\} $$

    가 되고, $\mathbb{Z} = [0] \cup [1]$ 이 된다. 이때 $0, 1$ 대신 $8, 5$ 를 택하여 $\mathbb{Z} = [8] \cup [5]$ 라고 써도 마찬가지이다. 

- 예시 

    집합 $\N \times \N = \{(m,n):m,n \in \N\}$ 에 관계 $\sim$ 를 

    $$ (m,n) \sim (m',n') \iff m+n' = n+m' $$

    와 같이 부여하면 동치관계가 된다. reflexive, symmetric 이 성립함은 자명하고, transitive 가 성립함을 보이자. 이는 $x \sim y, y \sim z \to x \sim z$ 를 보임으로써 완성된다.
    
    만약 $(m,n) \sim (m',n') \land (m', n') \sim (m'', n'')$ 라면 $m+n'=n+m' \land m'+n''=n'+m''$ 이므로 

    $$ (m+n'')+(m'+n') = (m+n')+(m'+n'') $$

    $$ = (n+m') + (n'+m'')=n+m''+(m'+n') $$

    이 성립한다. 따라서 $m+n''=n+m''$ 이고, 이에따라 

    $$ \therefore (m,n) \sim (m'',n'') $$

    이다. ■ 
    
    한편 이 경우 

    $$ \N \times \N / \sim = \{[(0, 0)], [(n, 0)], [(0, n)] : n \in \N \setminus \{0\} \} $$

    이 성립함을 금방 알 수 있는데, 이것이 정수 체계의 정의로 곧바로 연결된다. 왜냐하면, 사실 이렇게 이해하는 게 더 편하다. 동치 관계 

    $$ (m,n) \sim (m',n') \iff m+n' = n+m' $$

    를 

    $$ (m,n) \sim (m',n') \iff m-n = m'-n' $$

    로 생각하면 이는 $a \in \N \times \N$ 의 첫번째 원소와 두번째 원소의 차이값이다. 

!!! def "정리 1.3.1"

    집합 $X$ 에 정의된 동치관계 $\sim$ 에 대하여 $\sim = \sim _{(X/\sim )}$ 이 성립한다.

    역으로, 임의의 분할 $\mathcal{P}$ 에 대하여 $\mathcal{P} = X/\sim _{\mathcal{P}}$ 가 성립한다. 
    
    즉, $\forall  x, y \in X$ 와 $A \in 2 ^{X}$ 에 대하여 

    $$ x \sim y \iff x \sim _{(X/\sim )}y, \qquad A \in \mathcal{P}\iff A \in X/ \sim _{\mathcal{P}} $$

    가 성립한다.

- 첫번째 명제의 증명 

    먼저 $x \sim y$ 이면 $x \in [x], y \in [x]$ 이고 $[x] \in X/\sim$ 이므로 $x \sim _{(X/\sim )}y$ 가 성립한다. 역으로 $x \sim _{(X/\sim )}y$ 이면 $x \in [z], y \in [z]$ 인 $[z] \in X/\sim$ 이 존재한다. 그러면 $x \sim z, y \sim z$ 이므로 $x \sim y$ 이다.

- 두번째 명제의 증명 

    $A \in \mathcal{P}$ 라고 가정하고, $a \in A$ 를 택하자. 만약 $x \in A$ 이면 정의에 의하여 $x \sim _{\mathcal{P}} a$ 이다. 만약 $x \sim _{\mathcal{P}}a$ 이면 $x \in B, a \in B$ 인 $B \in \mathcal{P}$ 가 존재하는데 $a \in A \cap B$ 이므로 $A=B$ 이고, 따라서 $x \in A$ 이다. 그러므로 

    $$ A = \{x \in X:x \sim _{\mathcal{P}}a\} \in X/\sim _{\mathcal{P}} $$

    이다. 

    역으로 $A \in X / \sim _{\mathcal{P}}$ 이면 적절한 $a \in X$ 에 대하여 $A = \{x \in X:x \sim _{\mathcal{P}}a\}$ 이다. 한편 분할 $\mathcal{P}$ 에서 $a \in X$ 가 포함되는 것을 $B \in \mathcal{P}$ 라 하자. 그러면 방금 증명한 바에 의하여 $A=B$ 이고, 따라서 $A \in \mathcal{P}$ 이다.

- 예시 

    홀수 전체 집합을 $O$, 짝수 전체 집합을 $E$ 라 두면 $\mathcal{P} = \{O, E\}$ 는 정수 전체 집합 $\mathbb{Z}$ 의 분할이다. 그러면 동치관게 $\sim _{\mathcal{P}}$ 의 정의에 의하여 

    $$ m \sim _{\mathcal{P}} n \iff \exists a, b \in \N, (m = 2a-2, n = 2b-2) \lor (m = 2a - 1, n = 2b - 1) $$

    $$ \iff \exists c \in \N, m - n = 2c $$

    이다. 그러므로 동치관계 $\sim _{\mathcal{P}}$ 는 "분할" 의 예시에서 정의한 $\mathbb{Z}/\sim$ 과 같은 것이 된다.

    - "분할" 의 예시에서는 정수 집합 $\mathbb{Z}$ 에 관계 

        $$ m \sim n \iff \exists k \in \N, m - n = 2k $$

        를 정의하여 $\mathbb{Z}/\sim$ 가 짝수와 홀수의 집합으로 구성된다는 사실을 이끌어 내었고, 
        
        이 예시는 역으로 정수 집합 $\mathbb{Z}$ 를 짝수와 홀수로 분할한 집합 $\mathcal{P} = \{O,E\}$ 에 대한 동치관계 $m \sim _{\mathcal{P}} n$ 로부터 이 동치관계가 

        $$ m \sim _{\mathcal{P}} n \iff \exists c \in \N, m - n = 2c $$

        를 뜻함을 이끌어 냄으로써 

        동치관계의 정의로부터 도출된 분할과 분할의 정의로부터 도출된 동치관계가 서로 동일함을 보여주고 있는 것이다. 
    
- 즉, 이 정리는 정의된 동치관계로 구분된 원소들이 갖는 관계가 동치관계로 분할된 집합족의 부분집합들이 갖는 관계와 같고,

    어떤 집합에 임의의 분할 집합을 정의하면 그 분할이 갖는 동치관계로 집합을 분할하여도 결국 분할 집합과 같다는 것을 말해준다.  

    *(솔직히 이 정리 자체가 의미하는 것을 제대로 이해하기가 어렵네 잘아는 사람한테 물어봐야 할듯)*

## Quotient Set

!!! def "몫집합(quotient set), 상집합"

    집합 $X$ 의 동치관계 $\sim$ 혹은 분할 $\mathcal{P}$ 에 의하여 얻은 집합 

    $$ X / \sim $$

    을 몫집합이라고 한다. 

!!! def "목사상(quotient map)"

    집합 $X$ 와 그것의 몫집합 $X/ \sim$ 에 대한 함수  

    $$ q : X \to X/ \sim : x \mapsto [x] $$

    이다.

- 목사상은 전사사상이다.

- 함수 $f:X \to Y$ 가 

    $$ x \sim y \implies f(x) = f(y) \tag{1} $$

    를 만족할 때 함수 

    $$ \tilde{f}:X/ \sim \to Y:[x] \to f(x) $$

    를 정의할 수 있다. 이때 이 정의가 잘 정의되어 있는지 살펴봐야 하는데, 왜냐하면 $[x]$ 의 함수값을 정의하기 위하여 $x$ 를 사용하였는데 $[x]$ 를 대표하는 원소가 $x$ 이외에 더 있을 수 있기 때문이다. 즉, 다른 원소 $y$ 에 대하여 $[x]=[y]$ 라면 $y$ 도 $[x]$ 를 대표하게 되는데 이런 때에도 $f(x)=f(y)$ 가 성립하여야 $\tilde{f}$ 가 함수가 될 수 있다. 이것을 보장하는 조건이 $(1)$ 인 것이다. 

    역으로 $\tilde{f}\circ q = f$ 가 성립하는 함수 $\tilde{f}:X/\sim \to Y$ 가 존재하면 조건 $(1)$ 이 성립하는 것은 자명하다. 

!!! def "정리 1.3.2"

    집합 $X$ 와 동치관계 $\sim$ 와 함수 $f: X \to Y$ 에 대하여 다음 명제들은 서로 동치이다.

    1. $\tilde{f} \circ q = f$ 인 함수 $\tilde{f}: X/\sim \to Y$ 가 유일하게 존재한다. 

    2. $x \sim y \to f(x)=f(y)$

- $\tilde{f}$ 의 유일성 증명

    $\tilde{f} \circ q = f$ 를 만족하는 $\tilde{f}$ 가 존재하면 유일함을 보이자. 두 함수 $\tilde{f}_{1}, \tilde{f}_{2}: X/\sim \to Y$ 가 

    $$ \tilde{f}_{1} \circ q = f = \tilde{f}_{2} \circ q $$

    이라면, 

    $$ \tilde{f} _{1} = \tilde{f} _{2} $$

    임을 보이면 된다. 

    (*음.. 어려운데? $q$ 의 정의역을 축소하여 전단사사상으로 바꾸면 $q ^{-1}$ 를 정의할 수 있지만, $q$ 의 정의역을 축소하는 것이 올바른지 검증하는 게 어렵네 일단 시간이 너무 없긴 해서 넘어가야할듯*)

- 예시 

    좌표평면 $\R ^{2}$ 의 한 점 $A = (a_1, a_2)$ 에서 출발하여 $B = (b_1, b_2)$ 로 가는 화살표 $\overrightarrow{AB}$ 전체의 집합을 $X$ 라 하고, $X$ 에 관계 

    $$ \overrightarrow{AB} \sim \overrightarrow{CD} \iff B-A = D-C $$

    를 정의하자. 그러면 이 관계는 동치관계가 된다. 

    이때 $\forall \overrightarrow{AB} \in X$ 에 대하여 $A+C=B$ 인 $C = \in \R ^{2}$ 를 잡으면 $O = (0, 0)$ 에 대하여 $\bigg [\overrightarrow{AB}\bigg ] = \bigg [\overrightarrow{OC}\bigg ]$ 이다. 따라서 

    $$ X/\sim = \bigg \{\bigg [\overrightarrow{OC}\bigg ] : C \in \R ^{2} \bigg \} $$

    이다. 이때 함수 

    $$ C \mapsto \bigg [\overrightarrow{OC}\bigg ] : \R ^{2} \to X/\sim $$

    은 전단사함수이다. 즉, 좌표평면 위의 모든 벡터는 한 점에 의하여 결정되므로 점 $(a_1, a_2) \in \R ^{2}$ 을 벡터라 부른다. 이는 원점에서 그 점으로 가는 화살표로 이해하려는 것이다.

- 예시 

    실수체 $\R$ 위의 벡터공간 $V$ 와 그 부분공간 $W$ 에 대하여 

    $$ x \sim _{W} y \iff x - y \in W $$

    라고 정의하면 동치관계가 된다. 이때 $\forall x \in V$ 에 대하여 

    $$ [x] = \{y : x-y \in W\} = \{x+z:z \in W\} $$

    가 되는데, $V / \sim _{W}$ 에 $x, y \in V, a \in \R$ 에 대한 연산 

    $$ [x]+[y]=[x+y], \qquad a[x]=[ax] $$

    를 정의하자. 그러면 $V/ \sim _{W}$ 는 벡터공간이 되는데, 이것을 $V/W$ 라고 쓰고 몫공간이라고 한다. 

    그런데 $[x+y]$ 를 정의하기 위하여 $x$ 를 사용했는데 $[x]$ 를 대표하는 원소가 $x$ 만 있는 것이 아니기 때문에 이것이 잘 정의되었는가 검증해야 한다. 즉, 

    $$ [x_1] = [x_2], [y_1] = [y_2] \implies [x_1+y_1] = [x_2+y_2], [ax_1] = [ax_2] $$

    임을 증명해야 한다. 먼저 $[x_1] = [x_2], [y_1] = [y_2]$ 이면 $x_1 \sim x_2, y_1 \sim y_2$ 이므로 $x_1 - x_2, y_1 - y_2 \in W$ 이고, 이로부터 

    $$ (x_1+y_1) - (x_2+y_2) = (x_1-x_2)+(y_1-y_2)\in W $$

    $$ ax_1-ax_2=a(x_1-x_2) \in W $$

    임을 알 수 있다. 

# Order

!!! note

    이 책은 부분순서를 "순서" 라고 표현하고 있다.

!!! def "원순서 관계(preordered relation)"

    집합 $X$ 의 관계 $R \subset X \times X$ 이 

    1. $\forall  x \in X, (x, x) \in R$ (reflexivity)

    2. $(x, y) \in R \land (y, z) \in R \to (x, z) \in R$ (transitivity)

    을 만족시키면 원순서 관계라고 한다.

- 이 관계를 $\lesssim$ 으로 표현하면 다음과 같다.

    1. $\forall a \in X, a \lesssim a$

    2. $\forall a, b, c \in X, a \lesssim b \lesssim \implies  a \lesssim c$

- 원순서 관계에 반대칭성 조건

    $$ a \lesssim b \land b \lesssim a \implies a = b $$

    을 추가하면 부분 순서가 된다.

!!! def "원순서 집합(preordered set, proset)"

    원순서 관계를 만족하는 집합이다. 

- 원순서 집합은 두 원소를 추이적으로 비교할 수 있는 집합이다. 


!!! def "부분 순서관계(partial ordered relation)"

    집합 $X$ 의 관계 $R \subset X \times X$ 이 
    
    1. $\forall  x \in X, (x, x) \in R$ (reflexivity)
    
    2. $(x, y) \in R, (y, x) \in R \implies  x = y$ (antisymmetry)
    
    3. $(x, y) \in R \land (y, z) \in R \implies  (x, z) \in R$ (transitivity)
    
    를 만족하면 이를 부분 순서관계라고 한다.

- 순서관계는 $\leq$ 로 표현한다. 

    이를 통해 순서관계의 세 조건을 

    $$ x \in X \to x \leq x $$

    $$ x \leq y, y \leq x \implies  x = y $$

    $$ x \leq y, y \leq z \implies  x \leq z $$

    와 같이 쓸 수 있다.

- 만약 $x \leq y$ 이면서 $x \neq y$ 이면 $x < y$ 라고 쓴다.

- ("수체계", "무한집합" 파트에서 말하는 "순서" 라는 용어는 이 부분 순서를 뜻함)

!!! def "부분 순서집합(partially ordered set)"

    부분 순서관계가 정의되어 있는 집합이다.

- 예시 

    집합 $X = \{a,b,c\}$ 에 관계 

    $$ R = \{(a,a),(b,b),(c,c),(a,b),(a,c)\}\subset X \times X $$

    를 정의하면 $R$ 은 순서관계가 된다. 이때 원소 $a,b,c$ 사이에 다음의 순서 

    $$ a \leq a, b \leq b, c \leq c, a \leq b, a \leq c $$

    가 있게 된다.

!!! def "절대 부분 순서 관계(strict partial order), 순부분 순서"

    집합 $X$ 위의 관계 $R \subset X \times X$ 이 

    1. $\forall x \in X, x \not < x$ (irreflexivity)

    2. $a<b \land b < c \implies  a < c$ (transitivity)

    3. $a < b \to y \not < x$ (asymmetry)

- 예시 

    부분 순서 $\leq \subseteq X ^{2}$ 가 존재할 때 $x, y \in X$ 에 대하여

    $$ x < y \iff x \leq y \neq x $$

    를 만족하는 이항 관계 $< \subseteq X ^{2}$ 는 절대 부분순서이다.

- 예시 

    절대 부분 순서 $< \subseteq X ^{2}$ 가 존재할 때 $x, y \in X$ 에 대하여

    $$ x < y \iff x < y \lor x = y $$

    를 만족하는 이항 관계 $\leq  \subseteq X ^{2}$ 는 부분순서이다.

!!! def "원전순서 집합(pretotally ordered set, totally preordered set, weakly ordered set)"

    원순서 집합 $(X, \lesssim )$ 이 

    $$ \forall x, y \in X, x \lesssim y \lor y \lesssim x $$

    을 만족하면 원전순서 집합이다.

- 원전순서 집합은 두 원소가 항상 비교 가능한 원순서 집합이다.

!!! def "전순서 집합(totally ordered set, toset)"

    원전순서 집합인 부분 순서 집합 $(X, \leq )$ 으로써 

    1. $x \leq y \leq z \implies x \leq z$

    2. $\forall x, y \in X, x \leq y \land y \leq x \implies x = y$

    3. $\forall x, y \in X, x \leq y \lor y \leq x$

    을 만족하는 집합이다.

!!! def "도약(jump)"

    전순서 집합 $(X, \leq )$ 의 도약 $(a, b) \in X ^{2}$ 은 

    1. $a<b$

    2. $\not \exists c \in X, a < c < b$

    을 만족시키는 순서쌍이다.

- 도약이 없는 전순서를 조밀 순서라 한다.

!!! def "조밀 순서(dense order)"

    집합 $X$ 의 부분순서 $\leq$ 가 

    - $\forall x, z \in X, x < z \implies \exists y \in X \text{ s.t.  }\  x < y < z$

- 조밀 순서는 비교 가능한 서로 다른 두 원소 사이에 항상 제 3의 원소가 존재하는 부분순서이다.

## Relation of Order Relations

!!! def ""

    순서 관계의 함의 관계는 다음과 같다. 

    $$ \begin{CD} \text{전순서 집합} @> >> \text{원전순서 집합} \\ @V VV @VV V \\ \text{부분순서 집합} @> >> \text{원순서 집합} \end{CD} $$

# Bounded Set

## Supremum

!!! def "상계(upper bound)"

    순서집합 $X$ 의 부분집합 $S \subset X$ 와 한 원소 $a \in X$ 에 대하여 
    
    $$ x \in S \to x \leq a $$
    
    가 성립하면 $a$ 를 $S$ 의 상계라고 한다.

- 상계 중 가장 작은 원소를 최소상계(least upper bound) 또는 상한(supremum)이라 한다.

!!! def "상한(supremum) 또는 최소상계(least upper bound)"

    상계 중 가장 작은 원소 즉, 집합 $X$ 과 부분집합 $S \subset X$ 에 대하여 
    
    1. $\alpha$ 는 $S$ 의 상계이다. 즉, $x \in S \to x \leq \alpha$ 이다.
    
    2. $\beta$ 가 $S$ 의 상계이면 반드시 $\alpha \leq \beta$ 이다. 즉, $\forall x \in S, x \leq \beta \to \alpha \leq \beta$ 이다.
    
    를 만족하는 원소 $\alpha \in X$ 이다.

- 집합 $S$ 가 상한을 가지면 두번째 조건에 의하여 상한이 오직 하나밖에 없음을 쉽게 알 수 있다.

    그 상한을 

    $$ \sup S $$

    라고 쓴다.

- 어느 집합의 상한은 그 집합의 원소일 수도 있고, 아닐 수도 있다.

    만약 $\sup A$ 가 $A$ 의 원소가 되면, $\sup A$ 는 자명하게 $A$ 에서 가장 큰 원소이다.

    - 예시 

        실수집합 $\mathbb{R}$ 의 부분집합을 취하고 순서를 부여하여 개구간 

        $$ (0, 1) = \{x \in \mathbb{R}: 0 < x < 1\} $$

        을 얻으면, 이것의 상계 전체 집합은 

        $$ \{x \in \mathbb{R} : x \geq 1\} $$

        이다. 이 집합의 최소원소는 $1$ 이므로 

        $$ \sup (0, 1) = 1 $$

        이다.

        마찬가지로 실수집합 $\mathbb{R}$ 의 부분집합을 취하고 순서를 부여하여 폐구간 

        $$ [0, 1] = \{x \in \mathbb{R}: 0 \leq x \leq 1\} $$

        을 얻으면, 이것의 상한은

        $$ \sup [0, 1] = 1 $$

        이다.

!!! def "위로 유계(bounded from above)"

    순서집합의 부분집합이 상계를 가지면 이 집합을 위로 유계라고 한다.

!!! def ""

    정수집합 $\Z$ 과 $\Z$ 의 순서관계 $\leq$ 에 대하여
    
    $\emptyset \subset S \subseteq \Z$ 인 집합 $S$ 가 $(\Z, \leq )$ 에서 위로 유계라면 $S$ 는 가장 큰 원소를 갖는다.

- 증명 

    $S$ 가 위로 유계이므로 $\exists M \in \Z: \forall s \in S: s \leq M$ 이다. 즉, 모든 $S$ 의 원소 $s$ 에 대하여 적당한 정수 $M$ 이 존재하여 항상 $s \leq M$ 라는 것이다.

    그러므로 $\forall s \in S: 0 \leq M - s$ 이다. 그러면 집합 $T$ 를 이렇게 정의해보자.

    $$ T = \{M - s : s \in S\} \subseteq \mathbb{N} $$

    그러면 [Well-Ordering Principle](https://proofwiki.org/wiki/Well-Ordering_Principle) 에 의하여 $T$ 는 가장 작은 원소를 갖는다. 그것을 $b _{T} \in T$ 라고 하자.

    > **Well-Ordering Principle 구체화 필요**

    그렇다면 

    $$ (\forall s \in S: b _{T} \leq M - s) \land (\exists g _{S} \in S:b _{T} = M - g _{S}) $$

    이다. 즉, $S$ 의 모든 원소 $s$ 에 대하여 $M-s$ 는 $b _{T}$ 와 같거나 크고, $S$ 의 원소 $g _{S}$ 가 존재하여 $b _{T} = M - g _{S}$ 가 된다는 것이다.

    그러므로 

    $$ \forall s \in S : b _{T} \leq M - s $$

    $$ \iff  \forall s \in S : M - g _{S} \leq M - s $$

    $$ \iff  \forall s \in S : - g _{S} \leq - s $$

    $$ \iff  \forall s \in S : g _{S} \geq s $$

    $$ \iff g _{S} \in S \land (\forall s \in S : g _{S} \geq s ) $$

    이다. 즉, $S$ 의 모든 원소 $s$ 보다 큰 원소 $g _{S}$ 가 존재한다는 것이다.

    그러므로 $S$ 의 가장 큰 원소 $g _{S}$ 가 존재한다.

!!! def "위로 무계(unbounded from above)"

    순서집합 $(S, \leq )$ 의 부분집합 $T \subseteq S$ 이 위로 유계가 아니면 위로 무계이다.

!!! def ""
    
    $x \in \mathbb{R}$ 이 $x > 1$ 일 때 집합 $S = \{x ^{n}:n \in \mathbb{N}\}$ 은 위로 무계 집합이다.

- 증명 

    $S$ 가 위로 유계라고 하자. 그러면 $S$ 는 상한 $B = \sup S$ 를 갖는다.

    $x > 1$ 이므로 $\dfrac{x}{B} > \dfrac{1}{B}$ 에서 $\dfrac{B}{x} < B$ 이다.

    $B$ 가 최소상계, 즉 상한인데도 $\dfrac{B}{x} < B$ 이므로 $\dfrac{B}{x}$ 는 상계가 될 수 없다. 그러므로 

    $$ \exists n \in \mathbb{N}: x ^{n} > \dfrac{B}{x} \implies x ^{n+1} > B $$

    이다. 즉, $\dfrac{B}{x}$ 가 상계가 아니므로 와 적당한 자연수 $n$ 에 대한 $x ^{n}$ 이 존재하여 $x ^{n} > \dfrac{B}{x}$ 인데, 이는 곧 $x ^{n+1} > B$ 이 된다. 그런데 $B$ 를 최소상계라고 했으므로 이는 모순이다.

    그러므로 $B$ 는 상계가 아니다. 

    이로써 $S$ 가 위로 유계라는 가정 또한 모순이다. 그러므로 $S$ 는 위로 무계 집합이다.

!!! def "역진귀납법(backwards induction)"

    자연수 집합 $\mathbb{N}$ 과 명제함수 $P$ 에 대하여 
    
    1. $\forall n \in \mathbb{N} : P(2 ^{n})$
    
    2. $P(n) \implies P(n-1)$
    
    이면 $P(n)$ 은 $\forall n \in N$ 에 대하여 성립한다.

- 증명 

    적당한 자연수 $\exists k \in \mathbb{N}$ 가 존재하여 $P(k)$ 가 거짓이 된다고 하자.

    그러면 정리 "$x \in \mathbb{R}$ 이 $x > 1$ 일 때 집합 $S = \{x ^{n}:n \in \mathbb{N}\}$ 은 위로 무계 집합이다." 에 의하여 $\{2 ^{n} : n \in \mathbb{N}\}$ 은 위로 무계이다.

    쉽게 말해서 $2$ 의 제곱수는 상계가 없다. 그러므로 $k \in \mathbb{N}$ 가 아무리 크더라도 

    $$ M = 2 ^{N} > k $$

    를 만족하는 $N, M \in \mathbb{N}$ 이 존재한다. 그러면 이제 집합 $S$ 를 다음과 같이 만들어보자.

    $$ S = \{n \in \mathbb{N} : n < M, P(n) \text{ is false}\} $$

    쉽게 말해 $M$ 보다 작은 자연수 $n$ 중에서 명제함수 $P(n)$ 가 거짓이 되는 자연수 $n$ 의 모임으로 집합 $S$ 를 정의하는 것이다. 그러면 $k$ 는 반드시 $S$ 의 원소이므로 $S \neq \emptyset$ 이다. ($\because k < M , P(k) \text{ is false}$)

    그리고 $S$ 는 $\forall x \in S: x < M$ 이므로 위로 유계이다.

    그렇다면 정리 "정수집합 $\Z$ 과 $\Z$ 의 순서관계 $\leq$ 에 대하여 $\emptyset \subset S \subseteq \Z$ 인 집합 $S$ 가 $(\Z, \leq )$ 에서 위로 유계라면 $S$ 는 가장 큰 원소를 갖는다." 에 의하여 $S$ 는 가장 큰 원소 $g _{S}$ 를 갖는다.

    그러면 $S$ 의 가장 큰 원소 $g _{S}$ 보다 큰 자연수 $m$ 에 대하여 $m < n \leq M$ 인 자연수 $n$ 이 존재하여 $P(n)$ 을 참이 되게 한다. 그리고 그러므로 $P(m+1)$ 도 참이다.

    그런데 명제함수 $P$ 의 두번째 성질

    2. $P(n) \implies P(n-1)$

    에 의하여 $P(m+1) \implies P(m)$ 이다. 즉, $P(m+1)$ 이 참이면 $P(m)$ 도 참이다. 이에따라 $P(m-1)$ 도 참이고, $P(m-2)$ 도 참이고, $\dots$, $P(1)$ 도 참이다.

    그러므로 $S$ 의 가장 큰 원소 $g _{S}$ 가 존재하지 않으며, 이에따라 $S = \emptyset$ 이라는 결론을 얻는다. 이는 모순이다. 

    그러므로 $P(k)$ 가 거짓이 되게 하는 $k \in \mathbb{N}$ 는 존재하지 않는다. ■

## Infimum

!!! def "하계(lower bound)"

    순서집합 $X$ 의 부분집합 $S \subset X$ 와 한 원소 $a \in X$ 에 대하여 
    
    $$ x \in S \to x \geq a $$
    
    가 성립하면 $a$ 를 $S$ 의 하계라고 한다.

- 하계 중 가장 작은 원소를 최대하계(greatest lower bound) 또는 하한(infimum)이라 한다.

!!! def "하한(infimum) 또는 최대하계(greatest lower bound)"

    하계 중 가장 큰 원소 즉, 집합 $X$ 과 부분집합 $S \subset X$ 에 대하여 
    
    1. $\alpha$ 는 $S$ 의 하계이다. 즉, $x \in S \to x \geq \alpha$ 이다.
    
    2. $\beta$ 가 $S$ 의 하계이면 반드시 $\alpha \geq \beta$ 이다. 즉, $\forall x \in S, x \geq \beta \to \alpha \geq \beta$ 이다.
    
    를 만족하는 원소 $\alpha \in X$ 이다.

- 마찬가지로 하한도 집합 $S$ 에 대하여 오직 하나밖에 없는데 그 하한을 

    $$ \inf S $$

    라고 한다.

- 예시 

    집합 $X$ 의 멱집합 $2 ^{X}$ 에 포함관계에 의한 순서를 부여하자. 즉, $A \subset B \to A \leq B$ 로 정의한다는 것이다. 이 관계가 순서관계를 만족한다는 것은 자명하다.

    이때 집합족 $\mathcal{A} \subset 2 ^{X}$ 이 주어지면 

    $$ \sup \mathcal{A} = \bigcup_{}^{}\mathcal{A}, \inf \mathcal{A} = \bigcap_{}^{}\mathcal{A} $$

    이다. 이것을 증명해보자.

    먼저 $\forall A \in \mathcal{A} \to A \leq \bigcup_{}^{}\mathcal{A}$ 이므로 $\bigcup_{}^{}\mathcal{A}$ 은 $\mathcal{A}$ 의 상계이다. 만약 $S \in 2 ^{X}$ 가 $\mathcal{A}$ 의 상계라면, 임의의 $A \in \mathcal{A}$ 에 대하여 $A \subset S$ 이므로 

    $$ x \in \bigcup_{}^{}\mathcal{A} \implies \exists A \in \mathcal{A}, x \in A \implies x \in S $$

    이다. 그러므로 $\bigcup_{}^{}\mathcal{A} \leq S$ 이고, 

    $$ \sup \mathcal{A} = \bigcup_{}^{}\mathcal{A} $$

    이다.

!!! def "아래로 유계(bounded from below)"

    순서집합의 부분집합이 하계를 가지면 이 집합을 아래로 유계라고 한다.

## Convex Set

!!! def "볼록집합(convex set)"

    좌표공간 $\R ^{\mathcal{v}}$ 의 부분집합 $C \subset \R ^{\mathcal{v}}$ 가 

    $$ x,y \in C, 0 \leq t \leq 1 \to tx + (1-t)y \in C $$

    를 만족하면 이를 볼록집합이라 한다.

- 볼록집합은 쉽게 말해 유클리드 공간 속의 집합에서 임의의 두 점을 골랐을 때 둘을 연결하는 선분이 그 집합에 포함되면 볼록집합이다.

    <figure>
      <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Convex_polygon_illustration1.svg/440px-Convex_polygon_illustration1.svg.png" width="70%" />
      <figcaption><i>볼록 집합</i></figcaption>
    </figure>

    <figure>
      <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Convex_polygon_illustration2.svg/440px-Convex_polygon_illustration2.svg.png" width="70%" />
      <figcaption><i>볼록 집합이 아닌 예</i></figcaption>
    </figure>

- 블록집합 $C$ 의 볼록부분집합 $F$ 가 

    $\exists t \in (0, 1) \text{ s.t. } x,y \in C, tx + (1-t)y \in F \implies x,y \in F$ 

    를 만족하면 $F$ 를 $C$ 의 면이라고 한다.

- 한 점으로 이루어진 볼록집합의 면을 꼭지점이라 하다.

## Lattice

!!! def "격자(lattice)"

    순서집합 $X$ 에서 $\forall x, y \in X$ 에 대하여 $x \lor y$ 와 $x \land y$ 가 존재하면 $X$ 를 격자라 한다.

- 이 정의에서 주의할 점은 $x \lor y = \sup \{x, y\}$ 와 $x \land y = \inf \{x, y\}$ 로 정의한다는 것이다.

- 위에서 말한 상한의 정의를 다시 반복하면 $x \lor y$ 은 

    $$ x \leq x \lor y, \quad y \leq x \lor y $$

    $$ x \leq z, y \leq z \to x \lor y \leq z $$

    를 만족한다. 이때 

    $$ (x, y) \mapsto x \lor y, \quad (x, y) \mapsto x \land y $$

    은 이항연산이다.

!!! def "완비격자(complete lattice)"

    임의의 부분집합이 상한과 하한을 가지는 격자이다.

!!! def "1.22"

    $\forall x, y, z \in X$ 에 대하여 다음이 성립한다.

    1. $x \lor x = x, x \land x = x$

    2. $x \lor y = y \lor x, x \land y = y \land x$

    3. $(x \lor y) \lor z = x \lor (y \lor z), (x \land y) \land z = x \land (y \land z)$

    4. $(x \lor y) \land x = x, (x \land y) \lor x = x$

- 증명 

    1), 2) 는 자명하다. $\lor$ 의 결합법칙을 보이기 위하여 

    $$ (x \lor y) \lor z \leq x \lor (y \lor z) \tag{1} $$

    를 보이자. 먼저 $x \leq x \lor (y \lor z)$ 와 $y \leq y \lor z \leq x \lor (y \lor z)$ 에서 

    $$ x \lor y \leq x \lor (y \lor z) $$

    가 성립한다. 또한 $z \leq y \lor z \leq x \lor (y \lor z)$ 을 함께 생각하면 $(1)$ 이 성립함을 알 수 있다. 반대 부등식도 같은 방식으로 증명되고 $\land$ 의 결합법칙도 같은 방식으로 증명된다.

    마지막 명제 $(x \lor y) \land x = x$ 를 보이기 위해서 

    $$ x \leq x, \quad x \leq x \lor y $$

    $$ z \leq x, z \leq x \lor y \to z \leq x $$

    를 보이면 되는데 이는 자명하다. ■ 

!!! def "정리 1.4.1"

    순서집합 $X$ 의 $\forall x, y \in X$ 에 대하여 $x \lor y$ 와 $x \land y$ 가 존재하면 (1.22) 가 성립한다. 역으로 집합 $X$ 에 이항연산 $\lor , \land$ 가 정의되어 (1.22) 를 만족한다고 할 때 

    $$ x \leq y \iff x \lor y = y $$

    라 정의하면 $X$ 는 순서집합이 되고 이 순서에 대한 격자가 된다.

- 증명 

    첫째 명제는 위에서 이미 증명하였고, $x \leq x$ 는 [1.22](#9f4b6b716) 의 첫째 성질에서 나온다. $x \leq y, y \leq x$ 이면 $x \lor y = y$ 이고 $y \lor x = x$ 이다. 이때 $\lor$ 이 교환법칙을 만족하므로 $x=y$ 이다. 만약 $x \leq y, y \leq z$ 이면 

    $$ x \lor z = x \lor (y \lor z) = (x \lor y) \lor z = y \lor z = z $$

    이므로 $x \leq z$ 가 성립한다. 이제 $\sup \{x, y\} = x \lor y$ 임을 보이자. 먼저 

    $$ x \lor (x \lor y) = (x \lor x) \lor y = x \lor y $$

    이므로 $x \leq x \lor y$ 가 성립하고 $x$ 와 $y$ 의 역할을 바꾸면 

    $$ y \leq y \lor x = x \lor y $$

    이다. 마지막으로 $x \leq z, y \leq z$ 이면 

    $$ (x \lor y) \lor z = x \lor (y \lor z) = x \lor z = z $$

    이다. 따라서 $x \lor y \leq z$ 이다. 그러므로 $\sup \{x, y\} = x \lor y$ 이다. ■ 

---

ref:

:   [집합과 수의 체계](http://www.math.snu.ac.kr/~kye/book/set-number.html)
