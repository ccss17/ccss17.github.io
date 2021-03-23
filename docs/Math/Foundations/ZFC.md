!!! tldr ""

    러셀의 역설 : $S = \{x : x \not\in x\}$ 와 같이 정의된 집합은 모순이다. 

- $S \in S$ 이면 정의에 의하여 $S \not\in S$ 이다. 한편 $S \not\in S$ 이면 $S \in S$ 을 얻는다. 이 역설은 기존의 집합론에 모순이 있음을 말해주었고, 수학 학계에 수학의 엄밀한 기초를 세워야한다는 사실을 알려주었다.

    이 역설은 함부로 집합을 만들면 모순이 생긴다는 것을 알려주었고, 수학자들은 다음 공리계를 세워서 어느때 집합을 만들면 올바른지 엄밀하게 정의하였다.

!!! tldr ""

    ZFC 공리계(Zermelo–Fraenkel set theory with the axiom of choice) : 다음 공리를 갖는 공리체계이다.

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

