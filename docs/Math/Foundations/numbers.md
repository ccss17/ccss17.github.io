
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

    4. 



