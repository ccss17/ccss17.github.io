!!! def ""

    러셀의 역설 : $S = \{x : x \not\in x\}$ 와 같이 정의된 집합은 모순이다. 

- $S \in S$ 이면 정의에 의하여 $S \not\in S$ 이다. 한편 $S \not\in S$ 이면 $S \in S$ 을 얻는다. 이 역설은 기존의 집합론에 모순이 있음을 말해주었고, 수학 학계에 수학의 엄밀한 기초를 세워야한다는 사실을 알려주었다.

    이 역설은 함부로 집합을 만들면 모순이 생긴다는 것을 알려주었고, 수학자들은 다음 공리계를 세워서 어느때 집합을 만들면 올바른지 엄밀하게 정의하였다.

!!! def "ZFC 공리계(Zermelo–Fraenkel set theory with the axiom of choice)"

    다음 공리를 갖는 공리체계이다.

    - 존재공리(axiom of existence) : $\exists X \forall a (\lnot (a \in X))$
    
        (공집합이 존재한다.)

    - 확장공리(axiom of extensionality) : $\forall X \forall Y(\forall a(a \in X \iff a \in Y) \iff X = Y)$ 
    
        (집합 $x, y$ 가 같을 필요충분조건은 $z \in x \iff z \in y$ 이다.)
    
    - 정칙성 공리(axiom of regulatrity), 기초 공리(axiom of foundation) : 다음과 같다.
    
        $$\forall X (\exists a(a \in X) \implies \exists b(b \in X \land \lnot \exists c(c \in b \land c \in X)))$$

        (공집합이 아닌 모든 집합은 자신과 서로소인 원소를 포함한다.)

    - 분류공리꼴(axiom schema of specification) : $a$ 를 자유변수로 갖는 논리식 $\phi (a)$ 에 대하여 다음과 같다.

        $$ \forall X \exists Y \forall a(a \in Y \iff (a \in X \land \phi (a))) $$
    
        (임의의 집합 $X$ 와 성질 $P(x)$ 에 대하여 $P(x)$ 가 성립하는 모든 $x \in X$ 들의 집합이 존재한다.)

    - 짝공리(axiom of pairing) : $\forall a \forall b \exists X(a \in X \land b \in X)$
    
        (임의의 집합 $X, Y$ 에 대하여 $X \cup Y$ 는 집합이다.)

    - 합집합공리(axiom of union) : $\forall X \exists U \forall a \forall b(b \in X \land a \in b \implies a \in U)$
    
        (임의의 집합 $X$ 에 대하여 $\bigcup_{}^{}\{x : x \in X\}$ 는 집합이다.)

    - 멱집합공리(axiom of the power set) : $\forall X \exists P \forall Y(\forall a (a \in Y \implies a \in X) \implies Y \in P)$
    
        (임의의 집합 $X$ 에 대하여 $\mathcal{P}(X)$ 는 집합이다.)

    - 무한공리(axiom of infinity) : $S(x) = x \cup \{x\}$ 에 대하여 $\exists X(\varnothing \in X \land \forall y(y \in X \implies S(y) \in X))$

    - 치환공리꼴(axiom schema of replacement) : $x, y$ 를 자유변수로 갖는 논리식 $\phi (x,y)$ 에 대하여 다음과 같다.

        $$ \forall X(\forall x \in X \enspace \exists ! y \enspace \phi (x, y) \implies \exists Y \enspace \forall x \in X \enspace \exists y \in Y \enspace \phi (x, y)) $$

    - 선택공리(axiom of choice) : $\forall X(\varnothing \not\in X \implies \exists f: X \to \bigcup_{}^{}X \quad \forall A \in X(f(A) \in A))$

        (공집합이 아닌 집합들의 집합이 주어지면, 각 원소로부터 하나씩의 원소를 선택하는 선택함수가 존재한다.)

- 러셀의 역설 외에서 여러가지 역설이 발견되었었는데, 이러한 역설을 해결하기 위하여 먼저 중의적인 뜻을 항상 내포할 수 있는 자연어를 수학에서 배제하고, 다음의 기호만 쓰기로 했다. 실제로 모든 수학 체계의 내용은 다음의 단어들의 조합이다. 즉, 모든 수학을 다음의 단어만으로 전개할 수 있다.

    $$ \land \quad \lor \quad \lnot \quad \to \quad \iff \quad \exists \quad \forall $$

    또한 "원소", "집합", "$x \in X$" 같은 단어는 무정의 술어로 남겨서, 공리계 내부에서 자연스럽게 의미를 얻도록 했다.

    - 무한공리에서 사용된 비형식적 술어 $\varnothing$ 는 공집합을 뜻한다.

    - 선택공리에서 $\bigcup_{}^{}$ 은 합집합을 뜻하는 비형식적 술어이며, 물론 공리계의 올바른 형식적 술어로 정의된다.

- 분류공리꼴로 인하여 이미 존재하는 집합에 어떤 조건을 가하여 부분 집합을 취할 수 있다. 이때 어떤 성질 $\phi (a)$ 를 만족하는 집합이 바로 존재한다는 것이 아니라 이미 구성된 집합의 부분집합으로써 조건을 만족시키게 하는 것은 러셀의 역설을 피하기 위해서이다.

- 치환공리꼴로 인하여 어떤 논리식이 두 집합의 함수 관계라면, 함수의 상의 집합을 취할 수 있다.

- 무한공리에서 자연수를 정의할 때 쓰이는 성질

    $$ \varnothing \in \mathcal{A}, A \in \mathcal{A} \implies A ^{+} \in \mathcal{A} $$

    에 의하여 자연수가 정의된다. 그러므로 무한공리는 자연수의 존재성을 말하고 있다.

- 무한공리와 분류공리에 의하여 $\varnothing = \{x \in \N : x \neq x\}$ 이므로 존재공리가 유도되어, 존재공리는 공리가 아니게 되지만 그 의미가 너무 커서 그냥 "공리" 라고 부른다. 

    또한 짝공리도 합집합공리에서 도출되지만, 관행상 공리라고 부른다.

- 치환공리를 쉽게 말하면 다음과 같다.

    임의의 $x$ 에 대하여 성질 $P(x, y)$ 가 성립하는 $y$ 가 유일하게 존재한다고 하면, 임의의 집합 $X$ 에 대하여 

    "임의의 $x \in X$ 에 대하여 $P(x,y)$ 가 성립하는 $y \in Y$ 가 존재한다."

    를 만족하는 집합 $Y$ 가 존재한다. 

- 수학의 거의 모든 분야가 ZFC 를 표준적인 공리계로 사용한다. 즉, 현대 수학의 표준적인 수학기초론으로써 ZFC 공리계가 사용된다는 것이다.

    굳이 예외를 들자면 카테고리 이론을 들 수 있다.

    - 선택공리를 제외한 것을 ZF 공리계라고 하는데, ZF 도 표준적인 공리계로 사용된다.

!!! def "무모순성(consistency)"

    어떤 이론을 전개하기 위하여 공리계를 도입할 때 그 공리계에서 모순된 명제가 도출되지 않는다는 성질이다.

!!! def "독립성(independence)"

    공리계의 한 공리가 다른 공리로부터 도출되지 않아야 한다는 성질이다.

- ZFC 공리계에서 존재공리는 다른 공리로부터 유도되지만 그 중요성 때문에 관례상 공리라고 부른다.

!!! def "결정불가능한 명제(undecidable)"

    어떤 공리계 안에서 증명하는 것도, 반증하는 것도 불가능한 명제이다.

!!! def "완전성(completeness)"

    어떤 공리계가 결정불가능한 명제를 가지지 않으면 공리계가 완전하다고 한다.

- 세 개의 명제 $P_1, P_2, P_3$ 에 대하여 이 세 명제를 모두 만족하는 모델이 있으면 세 명제 사이에 모순이 없음을 알 수 있다. 이 경우 $P_1, P_2$ 로부터 $\lnot P_3$ 을 증명하는 것은 불가능하다.

    또한 $P_1, P_2, \lnot P_3$ 을 만족하는 모델이 있으면 $P_1, P_2$ 로부터 $P_3$ 을 증명하는 것은 불가능하다.

    - 예시 

        집합 $X$ 와 이 집합에 정의된 관계 $<$ 에 대한 명제 

        $P_1$: $\forall x, y \in X$ 에 대하여 $x<y$ 와 $y<x$ 가 동시에 성립하지 않는다.

        $P_2$: $\forall x, y, z \in X$ 에 대하여 $x<y \land y < z \implies x < z$ 이다.

        $P_3$: $\forall x, y \in X$ 에 대하여 $x<y, x=y, y<x$ 중 하나가 성립한다. 

        를 생각하자. 모델 $(2 ^{\{0,1\}}, \subsetneq )$ 은 $P_1, P_2$ 을 만족하지만 $P_3$ 은 만족하지 않는다. 따라서 $P_1, P_2$ 에서 $P_3$ 을 증명할 수 없다.

        한편 모델 $(2 ^{\{0\}}, \subsetneq )$ 은 $P_1, P_2$ 을 만족하지만 $\lnot P_3$ 을 만족하지 않으므로 $P_1, P_2$ 로부터 $\lnot P_3$ 을 증명할 수 없다. 따라서 $P_3$ 은 공리계 $\{P_1, P_2\}$ 안에서 결정불가능한 명제이다.

!!! def "정리 4.2.1 괴델의 불완전성 정리(Gödel's incompleteness theorems)"

    페아노 공리계가 무모순이면 그 공리계 안에서 결정불가능한 명제가 존재한다.

- 힐베르트는 산술 체계의 무모순성을 묻는 문제를 공표하면서 산술 체계의 무모순성을 증명함으로써 집합론의 무모순성과 더 나아가 수학의 무모순성을 증명할 수 있을 것이라고 믿었다. 하지만 괴델이 이 정리를 발표하여 산술 체계의 무모순성과 완전성이 양립 불가능함을 보였다. 

    그렇다면 페아노 공리계에 다른 공리를 추가하여 무모순성을 해결하면 되지 않은가 라고 생각할 수 있으나 그 추가된 공리로 인하여 또 다른 결정불가능 명제가 자동으로 생성된다. 즉, 불완전성 정리란 아무리 공리를 추가하여도 무모순성과 완전성을 동시에 만족시킬 수 없음을 말한다.

!!! def "정리 4.2.2"

    ZF 공리계가 무모순이면 ZFC 공리계도 무모순이다.

- 이 정리도 괴델이 보였다. 

- 이 정리는 ZF 공리계가 선택공리를 받아들이는 것이 안전하다는 것을 말해준다. 또한 괴델은 연속체 가설을 ZF 공리계에 받아들이는 것이 안전함을 보였다. 연속체 가설은 $\mathfrak{c} = \aleph _1$ 임을 묻는데, 칸토어는 이를 증명하려고 무던히 노력했지만 실패했다.

!!! def ""

    ZFC 공리계에 $\mathfrak{c} = \aleph _n$ 을 더한 공리계를 
    
    $$\text{ZFC} + (c = \aleph _n)$$

    라고 정의한다.

!!! def "정리 4.2.3"

    ZF 공리계가 무모순이면 $\text{ZFC} + (\mathfrak{c} = \aleph _1)$ 공리계도 무모순이다.

- 이 정리가 연속체 가설이 안전하다는 괴델의 정리이다. 

- 지금까지는 ZF 공리계 안에서 $\mathfrak{c} = \aleph _1$ 을 증명할 수 있는지 알 수 없었다. 즉, $\mathfrak{c} = \aleph _1$ 이 ZF 공리계로부터 독립적인지 알 수 없었다. 그러나 1963년 코헨이 다음의 정리를 증명했다.

!!! def "정리 4.2.4"

    ZF 공리계가 무모순이면, $\forall n \in \N$ 에 대하여 $\text{ZFC} + (\mathfrak{c} = \aleph _n)$ 공리계도 무모순이다.

- 이 정리는 ZF 공리계에서 

    $$ \mathfrak{c} = \aleph _1, \enspace \mathfrak{c} = \aleph _2, \enspace \mathfrak{c} = \aleph _3, \dots $$

    중 어떤 것을 공리로 택해도 안전함을 말해준다. 또 이는 $\mathfrak{c} = \aleph _1$ 이 ZF 공리계에서 증명될 수 없음을 말해주고, $\mathfrak{c} \neq \aleph _1$ 도 증명될 수 없음을 말해준다. 즉 $\mathfrak{c} = \aleph _1$ 는 ZFC 공리계에서 결정불가능한 명제였다.

- 즉, 괴델은 ZF 공리계가 무모순이라는 가정 하에 연속체 가설의 무모순을 보였고, 코헨은 연속체 가설의 독립성을 보였다.

- 유클리드 기하의 평행선 공리는 역사적으로 수학자들이 다른 공리로부터 도출하여 정리로 만드려고 무단히 노력했지만 실패했다. 그러나 결국 19세기 평행선 공리를 부정하면 비유클리드 기하학이 생성된다는 것이 발견되었다. 이는 평행선 공리가 유클리드 기하학의 다른 공리로부터 독립적임을 뜻했다. 

    연속체 가설도 평행선 공리와 같은 위치에 있는 것이다.

---

ref:

:   [집합과 수의 체계](http://www.math.snu.ac.kr/~kye/book/set-number.html)
