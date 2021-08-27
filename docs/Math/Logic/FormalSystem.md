!!! info "참고 및 출처"
    
    https://en.wikipedia.org/wiki/Propositional_calculus

    https://en.wikipedia.org/wiki/Formal_system

    https://en.wikipedia.org/wiki/Axiomatic_system

    https://en.wikipedia.org/wiki/Theory_(mathematical_logic)

    https://en.wikipedia.org/wiki/Formal_proof

    https://en.wikipedia.org/wiki/Mathematical_proof

    https://en.wikipedia.org/wiki/Contradiction

    https://en.wikipedia.org/wiki/Principle_of_explosion

    https://en.wikipedia.org/wiki/Completeness_(logic)

    https://en.wikipedia.org/wiki/Primitive_notion

    https://en.wikipedia.org/wiki/Model_theory

    https://en.wikipedia.org/wiki/Isomorphism

    https://en.wikipedia.org/wiki/Recursive_set

    https://en.wikipedia.org/wiki/Recursively_enumerable_set

    https://en.wikipedia.org/wiki/Interpretation_(logic)

    https://en.wikipedia.org/wiki/Metatheorem

    https://en.wikipedia.org/wiki/Metamathematics

    https://en.wikipedia.org/wiki/Metalanguage

    https://en.wikipedia.org/wiki/Metatheory

    https://en.wikipedia.org/wiki/Arity

    https://en.wikipedia.org/wiki/Hilbert_system

    https://en.wikipedia.org/wiki/Substitution_(logic)

    https://ko.wikipedia.org/wiki/%EC%9E%90%EC%97%B0_%EC%97%B0%EC%97%AD

    https://en.wikipedia.org/wiki/Method_of_analytic_tableaux

    https://en.wikipedia.org/wiki/Mathematical_model

    https://math.stackexchange.com/questions/105575/what-is-the-difference-between-completeness-and-soundness-in-first-order-logic

    https://en.wikipedia.org/wiki/Deduction_theorem

    https://en.wikipedia.org/wiki/Automated_theorem_proving

    https://en.wikipedia.org/wiki/Decidability_(logic)#Semidecidability

    https://en.wikipedia.org/wiki/Metalogic

    https://en.wikipedia.org/wiki/Categorical_theory

    https://en.wikipedia.org/wiki/Type_theory

    https://en.wikipedia.org/wiki/%CE%A9-inconsistent_theories

# 형식체계 

!!! def ""

    형식 체계(formal system) : 공리로부터 추론규칙을 통해 정리를 이끌어낼 수 있는 논리적 체계이다.

- 그러한 추론 규칙을 형식체계의 명제논리(logical calculus) 라고 한다.

- 힐베르트가 수학의 기초를 형식체계로 건설하자고 제안했다. 형식 체계는 추상적 생각의 체계를 잘 다듬은 것이다.

- 형식체계는 공리로부터 유한한 형식 언어를 구성하기 위하여 유한개의 원시 기호(primitive symbol) 를 사용한다. 좀 더 구체적으로 형식체계는 다음과 같이 구성된다. 

    1. 유한개의 원시 기호를 택한다.

    2. 원시 기호로 명제을 구성할 문법을 택한다. 어떤 명제이 잘 구성되었다(well-formed)고 하는 것은 원시 기호에 구성 문법을 가하여 그 명제을 얻을 수 있다는 것이다.

    3. 잘 구성된 명제인 공리를 택한다.

    4. 추론 규칙을 택한다. 공리로부터 추론(증명)되는 잘 구성된 명제을 정리(theorem) 이라고 한다. 

- 어떤 형식체계가 recursive 하다는 것은 그 공리들과 추론규칙들이 결정 가능한 집합(decidable sets, recursive set), 혹은 semidecidable sets 이라는 것이다.

- 어떤 형식체계가 다른 형식체계를 포함하거나 서로 동형일 수 있다. 이 경우 포함된 형식체계의 무모순성이 다른 형식체계에 의하여 상대적으로 증명가능하다.

- 연역 체계란 공리와 추론규칙으로 구성되어 정리를 이끌어낼 수 있는 체계이다. 연역 체계의 한 예시로 1차 논리를 들 수 있다.

- 논리 체계 혹은 language 란 비논리적 공리와 문법이 있는 (보통 1차 논리를 사용하는) 연역 체계이다. 모델 이론의 해석(interpretation) 에 의하여 논리 체계의 문법은 어떤 잘 구성된 명제이 주어진 구조(structure) 를 만족하는지 확인해준다.

    이때 형식 체계의 공리를 모두 만족하는 구조(structure) 를 논리 체계의 모델(model) 이라고 한다.

    - 어떤 논리 체계가 건전하다(sound)는 것은 공리로 연역된 모든 명제이 논리 체계의 모든 모델(model) 을 만족한다는 것이다. 즉 건전성(soundness)은 증명가능한 명제(정리)가 의미론 상으로도 참이된다는 성질이다. 
    
        역으로 논리 체계가 완전하다(complete) 는 것은 모든 모델을 만족하는 명제가 공리로 연역될 수 있다(증명될 수 있다)는 것이다. 즉, 건전성은 완전성과 역관계이다.

        그러나 괴델의 불완전성 정리로 산술을 표현할만큼 강력한 모든 형식체계는 건전하면서 완전하지 못하다. 왜냐하면 참이면서 증명할 수 없는 명제가 반드시 존재하기 때문이다. 

!!! def ""

    공리 체계(axiomatic system) : 명제논리로 공리로부터 정리를 이끌어낼 수 있는 임의의 공리 집합이다.

- 무모순(consistent)적인 어떤 이론(theory)은 공리체계를 포함하며 그것들로부터 도출된 정리들을 포함한다.

- 공리체계는 형식체계의 특수자이다. 즉, 공리체계의 일반화가 형식체계이다.

- 형식적 이론이란 공리체계(주로 모델 이론model theory 으로 형식화된)로 설명되는 명제의 집합이다. 이렇게 공리체계에서 도출된 이론에 포함된 정리들은 형식적 증명이라고 한다.

- 공리체계가 무모순(consistent)이라는 것은 모순을 포함하지 않는다는 것이다. 즉, 공리체계로부터 어떤 명제과 그 부정문이 도출되지 않는다는 것이다.

    무모순은 모든 공리체계에 있어야 하는 필수적인 속성인데, 왜냐하면 모순이 존재하면 폭발 원리(principle of explosion) 에 의하여 모든 명제이 증명되기 때문이다.

- 공리가 다른 공리로부터 도출될 수 없다면 독립성이 있다고 한다. 그러나 무모순성이 공리체계에 반드시 있어야 하는 조건인 것과 달리 독립성은 반드시 있어야 하는 조건은 아니다.

- 공리체계가 완전하다(complete)는 것은 모든 명제이 공리로부터 도출된다는 것이다. 즉, 그 공리체계로 표현가능한 모든 명제이 참이든 거짓으로든 증명 가능하다는 것이다.

- 상대적 무모순성이란 어떤 공리 체계의 무정의 술어의 정의가 다른 공리 체계로부터 주어져서, 전자의 공리체계가 후자의 공리체계의 정리가 되는 상황을 뜻한다. 

    - 예시 

        유클리드 기하학의 무모순성은 실수 체계의 무모순성이 증명되면 곧바로 증명된다. 왜냐하면 기하학은 실수 체계에 대하여 상대적으로 무모순적이기 때문이다. 

        가령 기하학에서의 무정의 술어인 점과 선은 실수 체계에서 의미와 정의를 부여받는다.

- 공리체계에서 모델은 무정의 술어에 의미를 부여하는, 잘 정의된 집합이다. 

    - concrete model 의 존재는 공리체계의 무모순성을 증명해준다.(*하지만 이 부분은 논쟁이 있음*)

    어떤 모델이 concrete 하다는 것은 추상적 모델과는 달리 의미가 부여된 대상과 관계가 현실 세계로부터 왔다는 것이다.

    모델은 어떤 공리의 독립성을 보이는데도 사용된다. 가령 어떤 공리체계의 특정 공리를 제외하여 생성된 부분체계가 올바른(valid) 모델을 구성했을 때 제외된 그 공리가 다른 공리로부터 독립적이라고 말할 수 있고, 부분체계에서 필요없다고 할 수 있다.

    두 모델이 서로간의 성분의 관계를 보존하는 전사함수(one-to-one correspondence)를 가지면, 서로 동형(isomorphic)이라고 한다.

    만약 어떤 공리체계의 모든 모델이 서로 동형이면 그 공리체계를 categorial 하다고 한다. 공리체계가 categoriality 를 가지면 공리체계의 완전성이 보장된다. 그러나 그 역은 성립하지 않는다. 즉, 완전성은 categoriality 를 보장해주지 못한다. 

    - 예시 

        1차 논리를 기반으로 다음과 같은 가산 무한의 공리를 갖는 공리체계를 생각하자. 

        $$ \exists x_1: \exists x_2: x_1 \neq x_2 $$

        $$ \exists x_1: \exists x_2: \exists x_3 : x_1 \neq x_2 \neq x_3 $$

        $$ \vdots $$

        이 공리체계의 가산 무한개의 공리들은 공리꼴(axiom schema) 로 생성된 것이다. 이 무한한 공리는 무한히 많은 대상이 존재함을 말하고 있다. 이 공리체계는 최소한 2개의 모델을 갖는다. 하나는 가산 무한 집합의 기수를 갖는 집합과 동형인 자연수이고, 다른 하나는 연속체의 기수와 동형인 실수이다. 사실 이 공리체계는 무한한 모델을 갖는다. 그러나 그러한 모델들을 구분하는 것은 기수(cardinality) 이다. 기수는 아직 이 공리체계에 정의되지 않았으므로, 이 공리체계는 categorial 하지 못하다. 그러나 이 공리체계가 완전하다는 것은 보일 수 있다.

- 무정의 술어를 두는 이유는 어떤 개념을 무한히 거슬러서 정의할 수 없기 때문이다. 이것을 공리적 방법(axiomatic method) 라고 한다. 공리적 방법에 대한 개념은 논리주의 학파에서 나왔다. 논리주의는 모든 것을 논리적으로 설명하려는 시도인데, 러셀은 "수학 원리" 에서 모든 수학의 정리를 공리를 기반으로 논리적으로 설명하려 했다. 이것은 현대의 수학에서 호몰로지 대수(homological algebra) 로 발전했다.

    공리적 방법은 수학의 추상적 위계를 명확하게 설정하는데 큰 도움을 준다. 가령 에미 뇌터의 첫 제안과는 달리 수학자들은 환(ring)에 commutative 가 성립하지 않아도 된다고 정의했고, 하우스도르프의 첫 정의와는 달리 위상 공간(topological space)이 separation axiom 없이 더 일반적으로 정의된다. ZFC 체계에서는 공리적 방법으로 러셀의 역설 등을 제거할 수 있었다. 

    - 모든 무모순적인 명제가 공리적 방법으로 설명될 수 있는 것은 아니다. 어떤 프로그램이 주어진 명제가 정리인지 확인할 수 있다면 그 공리체계를 재귀 집합(recursive, 계산 가능한) 이라고 한다. 그러나 괴델의 불완전성 정리에 의하여 무모순적이지만 재귀 집합에 속하지 않은 명제가 있다는 것이 밝혀졌다. 즉, 컴퓨터는 어떤 증명이 올바른지 확인할 수 있지만, 어떤 명제의 증명이 존재한다는 것을 밝힐 수 있다는 보장은 해줄 수 없다. 

        그러나 상위 체계 혹은 또 다른 체계에 해당 명제의 증명이 존재하는 경우가 있다. 

        가령 어떤 산술에서의 명제을 산술의 공리로 표현할 수 있지만, 그것에 대한 증명이 위상수학이나 복소해석학의 공리체계에 의존하게 될 수도 있다. 즉, 산술의 명제이라 할지라도 그것의 증명을 페아노 공리체계(Peano axioms)에서 찾을 수 있다는 보장은 없다. 

# 명제논리 

!!! def ""

    명제논리(Propositional logic, zeroth-order logic, Propositional calculus) : 내부 구조가 없는 명제들에 논리 연산을 가하여 구성한 명제들을 다루는 형식 체계이다. 

- 1차 논리와는 달리 명제 논리는 비논리적 대상, 그것에 대한 술어(속성, 조건), 양화사($\exists , \forall$)를 다루지 않는다. 그러나 명제논리는 1차 논리와 고차 논리의 기반이 된다.

- 논리는 자연어를 연결한다. 가령 and, or, not, if 를 들 수 있다.

    - 예시 

        다음은 명제논리 추론의 간단한 예시이다. 

        Premise 1: If it's raining then it's cloudy.

        Premise 2: It's raining.

        Conclusion: It's cloudy.
    
    위의 예시는 전건 긍정(modus ponens) 를 적용한 추론이다.

- 명제 논리는 논리적 접속사(and, or, not, if)로 연결된 명제를 더 이상 분해하지 않는다. 위의 예시에서의 명제는 변수로 나타낼 수 있다.

    - 예시 

        Premise 1: $P \to Q$

        Premise 2: $P$

        Conclusion: $Q$
    
    위 예시의 추론을 간결하게

    $$ P \to Q, P \vdash Q $$

    와 같이 표현할 수 있다. 

- 공리와 추론 규칙으로 명제로부터 또 다른 명제가 도출되는데 이를 정리(theorem) 라고 하며, 참인 명제로 여겨진다. 이 도출과정을 정리에 대한 증명이라고 부른다.

- 명제논리는 다음과 같이 구성된다. 

    - language (원시기호의 모음과 다른 기호들)

    - 공리 집합 

    - 추론 규칙의 집합

- 명제 논리는 진리값 참과 거짓을 가지며, 다음과 같은 연산을 갖는다. 

    - 부정 $\lnot P$, 그리고 $P \land Q$, Material conditional $P \to  Q$, IFF $P \leftrightarrow  Q$

    - 명제 논리는 이러한 연산에 대하여 닫혀있다. 즉, 이 연산을 적용한 대상 또한 명제이다.

- 명제 논리는 다음과 같은 추론 규칙을 가진다. 

    먼저 다음은 명제 $P, Q$ 에 대한 전건 긍정(modus ponens)이다.

    $$ \begin{array}{rl}1.&amp;P\to Q\\2.&amp;P\\\hline \therefore &amp;Q\end{array} $$

    다른 추론 규칙도 있으면 편리하지만, 필요하지는 않다. 전건 긍정만 있으면 다른 추론 규칙을 구성할 수 있기 때문이다. 그러나 이것이 1차 논리에서도 적용되지는 않는다. 1차 논리는 완전성(completeness) 를 위한 추론 규칙이 최소한 하나 더 필요하다.

    - 추론 규칙의 중요한 특징은 이미 알고 있는 진실로부터 또 다른 진실을 발견하게 해준다는 것이다. 우리는 이로써 어떤 명제 집합에 추론 규칙을 적용하여 다른 명제를 연역해낼 수 있다.

        가령 명제 집합 $A = \{P \lor Q, \lnot Q \land R, (P \lor Q) \to R\}$ 이 존재할 때, 우리는 이 명제 집합에서 연역되는 모든 명제의 집합인 연역 체계 $\Gamma$ 를 정의할 수 있다. $\Gamma$ 는 먼저 $A$ 의 원소를 포함할 것이고 전건 긍정에 의하여 $R$ 도 포함하여 

        $$ P \lor Q, \lnot Q \land R, (P \lor Q) \to R \in \Gamma , R \in \Gamma $$

        를 만족한다. 

- 명제논리는 다음과 같이 일반적으로 표현된다. 

    명제논리는 다음 조건을 만족하는 형식체계 $\mathcal{L} = \mathcal{L}(\Alpha , \Omega , \Zeta, \Iota)$ 이다. 이를 language $\mathcal{L}$ 라고도 한다.

    - $\Alpha$ 는 명제 기호 또는 명제 변수로 이루어진 가산 무한집합이다. 이는 language $\mathcal{L}$ 의 기본 구성을 이룬다. 관례적으로 $\Alpha$ 의 원소를 $p,q,r, \dots$ 로 표기한다. 

    - $\Omega$ 는 연산 기호 또는 논리 접속사로 이루어진다. 집합 $\Omega$ 는 서로소 집합의 합 

        $$ \Omega = \Omega _0 \sqcup \Omega _1 \sqcup \Omega _2 \sqcup \dots \sqcup  \Omega _m $$

        으로 이루어진다. $\Omega _j$ 는 연산 기호 항수(artiy) j 의 집합이다. 가령 

        $$ \Omega _1 = \{\lnot \}, \Omega _2 \subseteq = \{\land , \lor , \to , \leftrightarrow  \} $$

        이다. 보통 항수(artiy) zero 는 논리값 (False, True) 을 나타내는 $\Omega _0 = \{\top , \bot \}$  이 된다.
    
    - $\Zeta$ 는 추론 규칙(변환 규칙) 의 유한 집합이다. 

    - $\Iota$ 는 공리로 이루어진 가산 집합이다. language $\mathcal{L}$ 이 다음 조건을 만족할 때 잘 정의된 명제의 집합이라고 한다. 

        1. Base: $\Alpha$ 의 원소가 $\mathcal{L}$ 의 명제이다. 

        2. $p_1, p_2, \dots, p_j$ 가 $\mathcal{L}$ 의 명제이고 $f$ 가 $\Omega_j$ 에 속했다면, $f(p_1, p_2, \dots, p_j)$ 도 $\mathcal{L}$ 의 명제이다. 

        3. 닫혀있음: 그 외에 것들은 $\mathcal{L}$ 의 명제이 아니다.

        위와 같은 규칙을 반복함으로써 더 복잡한 명제를 생성할 수 있다. 가령 $p$ 가 명제이면 $\lnot p$ 도 명제이고, $(\lnot p \lor q)$ 도 명제가 된다.
    
    - 예시 (고전 명제 논리, 또는 힐베르트 연역 체계)

        다음과 같이 정의된 간단한 공리 체계 $\mathcal{L}_1 = \mathcal{L}(\Alpha ,\Omega ,\Zeta ,\Iota )$ 를 생각하자.

        $\Alpha$ 는 가산 무한집합 $A = \{p,q,r,s,t,u,p_2, \dots\}$ 이다.

        $\Omega$ 는 $\Omega _0 = \{\top ,\bot \}, \Omega _1 = \{\lnot \}, \Omega _2 = \{\to \}$ 에 대한 

        $$ \Omega = \Omega _0 \sqcup \Omega _1 \sqcup \Omega _2 $$

        이다. $\lnot , \to$ 로 $\land , \lor$ 을 만들 수 있고, $(a \to b) \land (b \to a)$ 와 같이 $a \leftrightarrow  b$ 를 만들 수 있다.

        $\Iota$ 에 해당하는 공리는 다음과 같은 치환 실례(substitution instance) 로 구성된다.

        1. $(p \to (q \to p))$

        2. $((p \to (q \to r)) \to ((p \to q) \to (p \to r)))$

        3. $((\lnot p \to \lnot q) \to (q \to p))$

        $\Zeta$ 에 해당하는 추론 규칙은 전건긍정(modus ponens) 이다.

        이 체계가 [Metamath](http://us.metamath.org/mpegif/mmset.html#scaxioms) 의 형식적 증명 데이터베이스에 사용된다.

    - 예시 (자연 연역 체계)

        다음 조건을 만족하는 체계 $\mathcal{L}_2 = \mathcal{L}(\Alpha ,\Omega ,\Zeta ,\Iota )$ 를 자연 연역 체계라고 한다. 

        $\Alpha = \{p,q,r,s,t,u,p_2, \dots\}$ 는 가산 무한집합이다.

        $\Omega$ 는 $\Omega _0 = \{\top ,\bot \}, \Omega _1 = \{\lnot \}, \Omega _2 = \{\land ,\lor ,\to ,\leftrightarrow  \}$ 에 대한 

        $$ \Omega = \Omega _0 \sqcup \Omega _1 \sqcup \Omega _2 $$

        이다. 공리 집합 $\Iota = \varnothing$ 는 공집합이다. 즉, 공리가 없다. 추론 규칙 집합 $\Zeta$ 는 다음 11개의 규칙으로 이루어진다. 첫 10개는 잘 구성된 명제에서 잘 구성된 명제를 도출할 수 있다는 것이고, 마지막 규칙은 어떤 명제를 가정했을 때 다른 명제를 도출할 수 있다는 가상의 추론(hypothetical rule)을 뜻한다. 첫 10 개의 규칙은 non-hypothetical rule 이라고 한다.

        추론 규칙을 효과적으로 표현하기 위하여 $\vdash$ 를 사용한다. 가령 $\Gamma \vdash \psi$ 는 가정 $\Gamma$ 에서 결론 $\psi$ 가 도출된다는 것이다. 이때 $\Gamma = \varnothing$ 일 수도 있다. 또 다른 뜻은 $\Gamma$ 가 정리이라면(즉, 공리와 같은 진리값을 가진다면) $\psi$ 도 정리라는 것이다. 아래의 연언 도입(Conjunction introduction) 은 $\Gamma$ 가 2개 이상의 명제를 가지면 그것을 하나의 명제로 줄일 수 있음을 뜻한다.

        1. Negation introduction: $\{(p \to q), (p \to \lnot q)\} \vdash \lnot p$

        2. Negation elimination: $\{\lnot p\} \vdash (p \to r)$

        3. Double negation elimination: $\lnot \lnot p \vdash p$

        4. Conjunction introduction: $\{p,q\} \vdash (p \land q)$

        5. Conjunction elimination: $(p \land q) \vdash p$ and $(p \land q) \vdash q$

        6. Disjunction introduction: $p \vdash (p \lor q)$ and $q \vdash (p \lor q)$

        7. Disjunction elimination: $\{p \lor q, p \to r, q \to r\} \vdash r$

        8. Biconditional introduction: $\{p \to  q, p \to p\} \vdash (p \leftrightarrow  q)$

        9. Biconditional elimination: $(p \leftrightarrow  q) \vdash (p \to q)$ and $(p \leftrightarrow  q) \vdash (q \to p$

        10. Modus ponens(conditional elimination): $\{p, p \to q\} \vdash q$

        11. Conditional proof(conditional introduction): $(p \vdash q) \vdash (p \to q)$ 
        
            ($p$ 가 $q$ 를 증명한다고 가정하면, $p \to q$ 이다)

- 명제 논리는 일반적으로 다음과 같은 기본적인 추론 규칙들을 가질 수 있다.

    |Name|Sequent|
    |:---:|:---:|
    |Modus Ponens|$((p \to q) \land p) \vdash q$|
    |Modus Tollens|$((p \to q) \land \lnot q) \vdash \lnot p$|
    |Hypothetical Syllogism|$((p \to q) \land (q \to r)) \vdash (p \to r)$|
    |Disjunctive Syllogism|$((p \lor  q) \land \lnot  p) \vdash q$|
    |Constructive Dilemma|$((p \to q) \land (r \to s) \land (p \lor r)) \vdash (q \lor s)$|
    |Destructive Dilemma|$((p \to q) \land (r \to s) \land (\lnot q \lor \lnot s)) \vdash (\lnot p \lor \lnot r)$|
    |Bidirectional Dilemma|$((p \to q) \land (r \to s) \land (p \lor \lnot s)) \vdash (q \lor \lnot r)$|
    |Simplification|$(p \land  q) \vdash p$|
    |Conjunction|$p,q \vdash (p \land q)$|
    |Addition|$p \vdash (p \lor q)$|
    |Composition|$((p \to q) \land (p \to r)) \vdash (p \to (q \land r))$|
    |De Morgan's Theorem 1|$\lnot (p \land q) \vdash (\lnot p \lor \lnot q)$|
    |De Morgan's Theorem 2|$\lnot (p \lor q) \vdash (\lnot p \land \lnot q)$|
    |Commutation 1|$(p \lor q) \vdash (q \lor p)$|
    |Commutation 2|$(p \land q) \vdash (q \land p)$|
    |Commutation 3|$(p \leftrightarrow  q) \vdash (q \leftrightarrow  p)$|
    |Association 1|$(p \lor (q \lor r)) \vdash ((p \lor q) \lor r)$|
    |Association 2|$(p \land (q \land r)) \vdash ((p \land q) \land r)$|
    |Distribution 1|$(p \land (q \lor r)) \vdash ((p \land q) \lor (p \land r))$|
    |Distribution 2|$(p \lor (q \land r)) \vdash ((p \lor q) \land (p \lor r))$|
    |Double Negation|$p \vdash \lnot \lnot p$, $\lnot \lnot p \vdash p$|
    |Transposition|$(p \to q) \vdash (\lnot q \to \lnot p)$|
    |Material Implication|$(p \to q) \vdash (\lnot p \lor q)$|
    |Material Equivalence 1|$(p \leftrightarrow   q) \vdash ((p \to q) \land (q \to p))$|
    |Material Equivalence 2|$(p \leftrightarrow   q) \vdash ((p \land  q) \lor (\land p \land \lnot q))$|
    |Material Equivalence 3|$(p \leftrightarrow   q) \vdash ((p \lor \lnot  q) \land (\lnot p \lor q))$|
    |Exportation|$((p \land q) \to r) \vdash (p \to (q \to r))$|
    |Importation|$(p \to (q \to r)) \vdash ((p \land q) \to r)$|
    |Tautology 1|$p \vdash (p \lor p)$|
    |Tautology 2|$p \vdash (p \land p)$|
    |Tertium non datur(배중률)|$\vdash (p \lor \lnot p)$|
    |Law of Non Contradiction(무모순성)|$\vdash \lnot (p \land \lnot p)$|

    - Conjunction : $p$, $q$ 가 독립적으로 참이면 $p \land q$ 가 참이다.

    - Exportation : $p$ 와 $q$ 가 참이면 $r$ 이 참이라는 것으로부터 ($p$ 가 참이면 ($q$ 가 참일 때 $r$ 이 참)이라는 것)을 증명할 수 있다.

- 명제 논리가 실제로 사용되는 용도는 어떤 명제와 다른 명제의 동등 관계를 확인하려 함이다. 가령 참임을 알고 있는, 혹은 참이라고 가정한 어떤 명제에 추론 규칙을 적용하여 다른 명제를 도출할 수 있는지 확인하는 것이다. 이때 도출되는 명제로까지의 과정(명제의 나열)을 증명(proof) 이라고 한다.

    - 예시 (자연 연역에서의 증명)

        $$ \begin{array}{rl} 1.&amp; A \\ 2.&amp; A \lor A  \\ 3.&amp; (A \lor A) \land A \\ 4.&amp; A \quad (\text{conjunction elimination)}\\ 5.&amp; A \vdash  A \quad(\text{Summary of 1 through 4}) \\ 6.&amp; \vdash  A \to  A \quad(\text{conditional proof}) \\ \end{array} $$

        위의 증명에서 $A \vdash A$ 를 "$A$ 를 가정하면 $A$ 가 증명된다." 로 해석하면 된다. $\vdash A \to A$ 를 "아무것도 가정하지 않아도, $A$ 가 $A$ 를 도출한다는 것이 증명된다." 로 해석하면 된다. 즉, "$A$ 가 $A$ 를 도출하는 것은 진리이다" 라고 해석하면 된다.

    - 예시 (고전 명제논리에서의 증명)

        이제 $A \to A$ 를 고전 명제논리에서도 증명해보자. 먼저 고전 명제 논리가 다음의 공리를 갖는다는 것을 기억하자.

        1. $(p \to (q \to p))$

        2. $((p \to (q \to r)) \to ((p \to q) \to (p \to r)))$

        3. $((\lnot p \to \lnot q) \to (q \to p))$

        먼저 $A$ 를 가정하면 공리 1 에 의하여 $A \to ((B \to A) \to A)$ 이다. 그러므로 다음과 같이 증명이 끝난다.

        $$ \begin{array}{rl} 1.&amp; A \to ((B \to A) \to A) \\ 2.&amp; (A \to ((B \to A) \to A)) \to ((A \to (B \to A)) \to (A \to A)) \quad (\text{axiom 2})\\ 3.&amp; (A \to (B \to A)) \to (A \to A) \quad (\text{modus ponens from 1 and 2})\\ 4.&amp; A \to (B \to A) \quad (\text{axiom 1})\\ 5.&amp; A \to A\quad (\text{modus ponens from 3 and 4})\\ \end{array} $$

- 어떤 형식 체계 $\mathcal{P}$ 에 대한 진리 함수적인 해석은 명제에 대한 진리표를 작성하는 것이다. $n$ 개의 명제들에 대한 진리값은 $2 ^{n}$ 의 가능성을 갖는다. 

    가령 어떤 명제 $a$ 는 참, 거짓 두 가지 경우 뿐이므로 $2 ^{1} = 2$ 의 가능성을 갖고, 어떤 명제 $a, b$ 는 $2 ^{2} = 4$ 가지 가능성을 갖는다.

    $\mathcal{P}$ 가 가산 집합만큼의 명제를 갖는다면, 즉 $\mathcal{P}$ 가 $\aleph _0$ 이라면 $2 ^{\aleph _0} = \mathfrak{c}$ 의 가능성을 갖는다. 즉, $\mathcal{P}$ 을 해석할 수 있는 가능성이 비가산 무한 집합만큼(실수의 개수만큼) 있는 것이다.

- 명제 논리에서 어떤 명제의 증명을 찾는 것은 NP 문제이다. 그러나 대부분의 유용한 명제를 자동으로 증명해 수 있는 현실적인 알고리즘들이 존재한다. 가령 [DPLL algorithm (1962)](https://en.wikipedia.org/wiki/DPLL_algorithm) 이나 [Chaff algorithm (2001)](https://en.wikipedia.org/wiki/Chaff_algorithm) 이 있다. 최근에는 [SAT solver](https://en.wikipedia.org/wiki/Boolean_satisfiability_problem#Algorithms_for_solving_SAT) 알고리즘을 산술 연산을 포함하는 명제를 해결할 수 있도록 확장한 [SMT solver](https://en.wikipedia.org/wiki/Satisfiability_modulo_theories) 가 제안되었다.
    
!!! def ""

    건전성(soundness) : 형식 체계의 성질 "임의의 명제가 증명가능하면 참이다" 이다.

- 건전성은 형식체계의 임의의 명제가 거짓이라면 증명할 수 없다는 성질이다.

    가설 명제 집합 $\Sigma$ 와 증명하고자 하는 명제 $\Phi$ 를 생각하자. $\Sigma \vDash \Phi$ 는 $\Sigma$ 가 의미적으로 $\Phi$ 를 함의한다는 뜻이다. 즉, $\Sigma$ 가 참이면 $\Phi$ 도 참이라는 것이다. 반면 $\Sigma \vdash \Phi$ 는 $\Sigma$ 에 추론규칙을 적용하여 $\Phi$ 를 도출할 수 있다는 것이다. 즉 $\Phi$ 가 $\Sigma$ 로부터 증명가능하다는 것이다.

    건전성이란 $\Sigma \vdash \Phi \implies \Sigma \vDash \Phi$ 이다. 즉, $\Phi$ 를 $\Sigma$ 로부터 증명할 수 있다면, $\Sigma$ 가 주어졌을 때 $\Phi$ 가 참이라는 것이다. 이는 $\Sigma$ 가 주어졌을 때 $\Phi$ 가 거짓이라면 $\Sigma$ 로부터 $\Phi$ 를 증명할 수 없음을 뜻한다. 그래서 건전성은 "거짓이라면 무엇이든지 증명할 수 없다" 혹은 "증명할 수 있다면 그것은 참이다" 는 성질이다. 

- 건전성 증명은 일반적으로 다음과 같이 이루어진다.

    $G$ 가 명제 집합이라고 하고 $A,B,C$ 를 명제라고 하자. 우리가 보이려 하는 것은 
    
    $$G \vdash A \implies G \vDash A$$
    
    이다. 그런데 $G \vdash A$(어떤 명제가 다른 명제를 증명한다) 는 귀납적으로 정의할 수 있다. 그러므로 우리는 다음을 증명하면 된다.

    1. $A \in G \implies G \vDash A$

    2. $A$ 가 공리이면 $G \vDash A$ 이다.

    3. 증명의 길이 $n$ 에 대하여 다음이 성립한다.

        1. 임의의 $G$ 와 $G$ 가 $n$ 이나 $n$ 보다 적은 단계로 증명할 수 있는 $A$ 에 대하여 $G \vDash A$ 이다.

        2. 추론규칙을 $n+1$ 단계에 적용하여 $G$ 가 $B$ 를 도출했다면 $G \vDash B$ 이다.
    
    a), b) 는 $G$ 의 원소인 명제가 $G$ 에 함의된다는 것을 말해준다. c) 는 $A$ 가 증명가능하면 추론규칙이 적용된 정리, 가령 $A \lor B$ 도 증명가능하다는 것을 말해준다. 그러면 $G$ 를 참으로 만드는 임의의 평가는 $A$ 도 참으로 만든다. 이렇게 증명은 귀납적으로 분석 가능하므로, 일반적으로 모든 추론 규칙이 의미적 함의를 보존한다는 것을 검증함으로써 건전성을 증명할 수 있다. 

!!! def ""

    극대 집합(Maximal Set) : 어떤 조건을 만족하는 가장 큰 집합이다.

!!! def ""

    Order type : 순서 집합 $X, Y$ 이 다음 동치명제를 만족하면 같은 order type 을 갖는다고 한다. 

    1. $X, Y$ 가 순서동형이다. 

    2. $X$ 와 $Y$ 사이에 전단사 사상이 존재한다.

- 모든 정렬집합은 하나의 서수와 대응된다. 

    - 예시

        $\N$ 의 order type 은 $\omega$ 이다.

- 정렬 집합 $V$ 의 order type 은 $\text{ord}(V)$ 로 표현된다. 즉 $\text{ord}(\N) = \omega$ 이다.

- 예시
    
    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/OrderTypeExamples_svg.svg/1143px-OrderTypeExamples_svg.svg.png)

- 예시 

    $\mathbb{Z}$ 집합은 짝수 집합과 같은 order type 을 갖는다. 두 집합 사이에 $n \mapsto 2n$ 이라는 전단사 사상이 존재하기 때문이다.

    반면 $\mathbb{Z}$ 는 $\mathbb{Q}$ 에 대하여 $\mathbb{Z} \approx \mathbb{Q}$ 이지만, 같은 order type 을 갖지는 않는다. 왜냐하면 두 집합 모두 가산 무한 집합이지만, 두 집합 사이에 순서를 보존하는 전단사 사상은 존재하지 않기 때문이다.

- 예시 

    $\omega \cdot 2 + 7$ 보다 작은 짝수 서수는 

    $$ V = \{0,2,4, \dots; \omega , \omega +2, \omega +4, \dots; \omega 2, \omega 2 + 2, \omega 2 + 4, \omega 2 + 6\} $$

    인데, 이것의 order type 은 

    $$ \text{ord}(V) = \omega 2 + 4 = \{0,1,2, \dots; \omega , \omega +1, \omega +2, \dots; \omega 2, \omega 2 + 1, \omega 2 + 2, \omega 2 + 3\} $$

    이다. 왜냐하면 가산 무한 집합이 $2$개 있고, 그 이후에 $4$개의 원소가 있기 때문이다.

- 임의의 가산 전순서 집합은 $\mathbb{Q}$ 에 순서를 보존하면서 단사될 수 있다. 임의의 조밀한(dense) 가산 전순서 집합은 극대 원소나 극소 원소가 순서를 보존하면서 $\mathbb{Q}$ 로 전단사 될 수 없기 때문이다.

    일반적으로 $\mathbb{Q}$ 의 order type 을 $\eta$ 로 표기한다.

!!! def ""

    완전성(completeness) : 형식 체계의 성질 "임의의 명제가 참이면 증명가능하다" 이다.

- 추론 규칙의 핵심적인 성질은 건전성(sound) 과 완전성(complete) 이다. 쉽게 말해 이 성질은 추론 규칙이 올바르고, 다른 추론규칙이 필요하지 않다는 뜻이다. 건전성과 완전성에 대한 증명은 명제 논리 안에서의 증명이 아니라 명제 논리의 속성을 증명하기 위하여 메타이론(metatheory) 로써 사용되는 ZFC 에서의 증명이다.

- 완전성은 형식체계의 임의의 명제가 참이라면 증명할 수 있다는 성질이다.

    완전성이란 $\Sigma \vDash \Phi \implies \Sigma \vdash \Phi$ 이다. 만약 $\Sigma$ 가 주어졌을 때 $\Phi$ 가 참이면 $\Sigma$ 로부터 $\Phi$ 를 증명할 수 있다는 것이다. 즉, "임의의 명제가 참이라면 증명 가능하다" 는 것이 완전성이다.

- 건전성이 "증명할 수 있다면 그것은 참이다" 이고, 완전성이 "참이면 증명할 수 있다" 이므로 이 둘은 서로 역관계이다.

- 우리가 바라는 이상적인 형식 체계는 완전성과 건전성이 성립하는 체계일 것이다.

- 완전성 증명은 일반적으로 다음과 같이 이루어진다.

    완전성 증명은 $G \vDash A \implies G \vdash A$ 을 보이는 것이다. 이때 대우명제 $G \not \vdash A \implies G \not \vDash A$ 를 보이자. 만약 $A$ 는 거짓이 되고 $G$ 는 참이 되는 모델이 존재하면, $G \not \vDash A$ 이다. 그러므로 $G \not \vdash A$ 라는 가정으로부터 그러한 모델이 존재한다는 것을 보이면, 완전성 증명이 끝난다.

    1. $G \not \vdash A$ (가정)

    2. $G \not \vdash A$ 이므로 $G ^{*} \not \vdash A, G \subset G ^{*}$ 인  극대집합 $G ^{*}$ 를 정의할 수 있다. $G ^{*}$ 는 무한집합일 수도 있다.

        1. order type $\omega$ 로 language 의 모든 명제에 명제의 길이에 의한 순서 관계를 부여하자. 그러면 가장 짧은 명제가 맨앞에 있을 것이다. 길이가 같은 것들은 사전순서로 순서를 결정하면 된다. 그러면 모든 명제에 순서가 부여되는데 이 명제들에 숫자를 부여하여 $E_1, E_2, \dots$ 와 같이 나타내자. 

        2. 집합 $G_0, G_1, \dots$ 의 집합 $G_n$ 을 다음과 같이 귀납적으로 정의하자.

            - $G_0 = G$

            - $G_k \cup \{E _{k+1}\} \vdash A \implies G _{k+1} = G_k$

            - $G_k \cup \{E _{k+1}\} \not \vdash A \implies G _{k+1} = G_k \cup \{E _{k+1}\}$
        
        3. $G ^{*}$ 를 $\displaystyle  G ^{*} = \bigcup_{i \in \N}^{}G_i$ 와 같이 정의하자.

        4. 그러면 우선 $G ^{*}$ 는 $G$ 를 포함하게 된다. ▲ 또한 $G ^{*}$ 는 $A$ 를 증명하지 않는다. 왜냐하면 증명은 유한한 명제의 집합이고, 그 증명의 마지막 명제가 어떤 $G_n$ 에 포함된다고 하면 $G_n$ 이 $A$ 를 증명하게 되는데 이는 $G_n$ 의 정의에 위배되기 때문이다. ▲ 또한 $G ^{*}$ 는 $A$ 에 대한 극대 집합이다. 만약 $G ^{*}$ 에 어떤 명제가 추가되면 $G ^{*}$ 는 $A$ 를 증명하게 된다. 왜냐하면 $G ^{*}$ 에 어떤 명제가 추가될 수 있었다면 $G_n$ 의 정의에 의하여 그것은 이미 반드시 추가되었을 것이기 때문이다.
    
    3. 만약 $G ^{*}$ 가 $A$ 에 대하여 극대 집합이면 이것은 무모순성을 갖는다. 즉, 임의의 명제 $C$ 에 대하여 $C \in G ^{*} \iff \lnot C \not\in G ^{*}$ 이다. 이것을 보이기 위하여 이 공리 체계가 다음을 만족할 수 있도록 강력하다는 것을 보여야 한다. 

        - 임의의 명제 $C, D$ 에 대하여 공리 체계가 $C$ 와 $\lnot C$ 를 증명한다면 $D$ 도 증명한다. 이로써 $A$ 에 대한 극대집합 $G ^{*}$ 는 $C$ 와 $\lnot C$ 를 동시에 증명할 수 없어야 한다.

        - 임의의 명제 $C, D$ 에 대하여 공리 체계가 $C \to D$ 와 $\lnot C \to D$ 를 증명한다면 $D$ 도 증명한다. 이로써 $G ^{*}$ 는 $C \to D$ 와 $\lnot C \to D$ 를 동시에 증명할 수 없어야 한다.
        
            이것은 연역 정리(deduction theorem) 와 함께 임의의 명제가 그것의 부정문과 함께 $G ^{*}$ 에 포함됨을 보이기 위하여 사용된다. 가령 $B$ 가 $G ^{*}$ 에 속하지 않았다면 $B \cup G ^{*}$ 는 $A$ 를 증명한다. 이때 연역 정리에 의하여 $G ^{*}$ 는 $B \to A$ 를 증명한다. 그러나 $\lnot B$ 도 $G ^{*}$ 에 속하지 않는다고 가정하면 동일한 논리로 $\lnot B \to A$ 도 증명 가능하다. 그러나 이로써 우리가 거짓이라고 증명했던 $G ^{*}$ 가 $A$ 를 증명한다는 것이 참이 된다.

        - 임의의 명제 $C, D$ 에 대하여 공리 체계가 $C, D$ 를 증명한다면 $C \to D$ 도 증명한다.

        - 임의의 명제 $C, D$ 에 대하여 공리 체계가 $C, \lnot  D$ 를 증명한다면 $\lnot (C \to D)$ 도 증명한다.

        - 임의의 명제 $C, D$ 에 대하여 공리 체계가 $\lnot C$ 를 증명한다면 $C \to D$ 도 증명한다.

        만약 $\land, \lor$ 같은 추가적인 논리 연산이 존재한다면, "공리 체계가 $C, D$ 를 증명한다면 $C \land D$ 도 증명한다" 같은 추가적인 조건이 요구된다.
    
    4. 만약 $G ^{*}$ 가 무모순성을 갖는다면, $G ^{*}$ 에 속한 모든 명제가 참이고 그 이외의 명제는 거짓이라는 $G ^{*}$ 에 대한 평가(Canonical valuation of the language)가 존재한다.

    5. 그러면 그 $G ^{*}$ 에 대한 평가는 원래의 집합 $G$ 를 참으로 만들고 $A$ 를 거짓으로 만든다. 

    6. $G$ 가 참이고 $A$ 가 거짓이라는 평가(valutation)가 존재하면 $G \not \vDash A$ 이다.

    이로써 $G \not \vdash A \implies G \not \vDash A$ 가 증명되었고, 그 대우명제 $G \vDash A \implies G \vdash A$ 도 증명되었다. 

    위에서 본 것과 같이 전건 긍정을 추론 규칙으로 가지고 다음 정리를 증명할 수 있는 모든 체계는 완전성을 갖는다. 처음 5개 정리는 c) 단계에서 필요한 작업이고, 나머지 3개는 deduction theorem 을 증명하기 위한 정리이다.

    - $p \to (\lnot p \to q)$

    - $(p \to q) \to ((\lnot p \to q) \to q)$

    - $p \to (q \to (p \to q))$

    - $p \to (\lnot q \to \lnot (p \to q))$

    - $\lnot p \to (p \to q)$

    - $p \to p$

    - $p \to (q \to p)$

    - $(p \to (q \to r)) \to ((p \to q) \to (p \to r))$

- 완전성 증명에 대한 또 다른 증명법은 다음과 같다. 

    어떤 명제가 tautology 라면 그 명제를 참이라고 평가하는 진리표가 존재한다. 그 평가를 생각하자. 명제의 길이에 대한 수학적 귀납법으로 명제 변수에 따르는 명제들이 참인지 거짓인지 평가할 수 있다. "(참인 $P$ 에 대하여 $P \vDash S$ 이다) $\vDash$ ((거짓인 $P$ 에 대하여 $P \vDash S$) $\vDash S$) 이다." 를 모든 명제 변수의 의존성이 해결될 때까지 반복한다면 주어진 tautology 는 증명가능하고 해당 논리 체계는 완전하다.

    (*이게 뭔 소릴까 대체. 영문 위키도 그렇게 매번 속 시원한 설명을 주지는 않네.*)

# 1차 논리 

!!! def ""

    논의 영역(domain of discourse, universe of discourse, universal set, universe) : 형식적 논의의 대상이 되는 객체의 집합이다.

- set of domain of discourse 를 보통 기호 $\mathbb{D}$ 로 표현한다.

- 논의 영역은 1차 논리에서의 양화사의 범위로 표현된다. 가령 $\forall x, (x ^{2} \neq 2)$ 는 논의 영역이 명시되지 않아서 모호하다. 논의 영역은 $\R$ 이 될 수도 있고 $\N$ 이 될 수도 있다.

!!! def ""

    1차 논리(first-order logic, predicate logic) : 원소에 한정기호를 사용할 수 있고, 술어에 한정기호를 사용할 수 없는 형식 체계이다.

- 명제 논리와 달리 변수에 한정기호를 사용할 수 있지만, 2차 논리와는 달리 변수들의 집합에 한정기호를 사용할 수 없다. 명제 논리는 1차 논리의 기반이 된다. 명제 논리와 달리 1차 논리는 술어와 양화사를 다룰 수 있다.

- 1차 논리에서는 완전성 정리, 콤팩트성 정리, 스콜렘 정리같은 메타 논리에서의 중요한 정리들이 성립한다.

- 1차 논리는 수학, 철학, 언어학, 컴퓨터 공학 등에서 사용된다.

- 1차 논리에서는 건전하면서 완전한 연역 체계들이 많이 존재한다.

- 논리 체계가 준결정가능성(semidecidable) 을 가져도, 상당히 많은 진전이 1차 논리 속에서의 자동 정리 증명(Automated theorem proving)을 통해서 이루어질 수 있다.

- 1차 논리는 수학의 기초로 여겨진다. 가령 페아노 공리계와 ZF 가 1차 논리에서 공리화되었다. 그러나 1차 논리는 자연수나 실수같은 무한한 정의역을 가진 구조를 설명할 수 있는 능력은 없다. 이들 두 구조는 2차 논리 같은 더 강력한 논리 체계로 설명가능하다.

- 술어는 논의 영역을 입력으로 받아서 참이나 거짓을 출력한다. 

    - 예시 

        "소크라테스는 철학자이다" 와 "플라톤은 철학자이다" 는 명제 논리에서 단지 $p, q$ 로 표현되어 서로 관계가 없어 보인다. 하지만 술어 "는(은) 철학자이다" 가 두 문장에 등장하므로 두 명제가 같은 구조로 되어 있음을 알 수 있고, 변수 "소크라테스" 와 "플라톤" 을 가짐을 알 수 있다. 1차 논리에서는 이와 같은 술어로 명제를 표현할 수 있다.
    
    술어간의 관계를 논리적 접속사로 표현할 수 있다. 가령 1차 논리의 명제 "A 가 철학자이면, A 는 학자이다." 의 진리값은 변수 A 에 의하여 결정된다.

    이때 변수 A 에 양화사를 가하여 범위를 지정할 수 있다. 가령 "모든 A 에 대하여" 라는 식으로. 

    1차 논리에서의 부정을 살펴보면 "모든 A 에 대하여, A 가 철학자이면 A 는 학자이다." 의 부정은 "A 가 존재하는데, A 는 철학자이고 A 는 학자가 아니다." 이다.

- 1차 논리는 문법과 의미라는 두 개의 핵심 구성요소를 가진다. 문법은 어떤 기호로 구성된 명제가 잘 구성되었는지 결정하고, 의미는 어떤 명제의 의미를 결정한다.

    자연어와 달리 1차 논리의 명제는 완벽하게 형식적이어서 어떤 명제가 잘 구성되었는지 기계적으로 결정할 수 있다. 잘 구성된 명제는 용어와 술어로 구성된다. 용어와 술어는 기호의 나열이다. 기호는 항상 같은 의미를 갖는 논리적 기호와 해석에 따라 의미가 달라지는 비논리적 기호로 구분된다. 

    가령 논리적 기호 $\land$ 는 항상 "그리고" 라는 의미를 가지는데, 비논리적 기호인 $\text{Phil}(x)$ 같은 술어는 해석에 따라서 "x 가 철학자(philosopher) 이다" 라거나 "x 가 Philip 이다" 라는 의미를 가진다.

- 1차 논리에서 사용되는 논리적 기호는 다음과 같다. 

    - 양화사 기호 $\forall$ 는 보편 양화사이고, $\exists$ 는 존재 양화사로 사용된다. 

    - 논리 접속사 $\land , \lor , \to , \leftrightarrow, \lnot$ 가 사용된다.

    - 괄호 $(, )$ 와 대괄호 $\{, \}, [, ]$ 와 기타 구두점 $.,"'$ 등이 사용된다.

    - 변수의 무한 집합을 표현하기 위하여 보통 $x, y, z, \dots$ 을 사용한다. 

    - 동등함을 표현하기 위하여 $=$ 를 사용한다. 

    - 참을 표현하기 위하여 $\bot$ 을, 거짓을 표현하기 위하여 $\top$ 을 사용한다. 

- $0$ 보다 큰 항수를 갖는 술어(관계) 기호: $n$ 항수를 갖는 술어는 $n$ 개의 객체의 관계를 표현한다. 가령 $Q(x, y)$ 는 "$x$ 가 $y$ 보다 크다" 는 관계를 표현한다. 

- $0$ 보다 큰 항수를 갖는 함수 기호: 함수 기호는 일반적으로 $f, g, h, \dots$ 로 표현한다. 가령 $f(x)$ 는 "$x$ 의 가족" 을 뜻할 수도 있고 "$-x$" 를 뜻할 수도 있다. $g(x, y)$ 는 "$x+y$" 를 뜻할 수도 있다. 항수 $0$ 을 갖는 함수는 상수로써 보통 $a,b,c$ 로 표현된다. 

- Formation rule 은 1차 논리에서의 용어와 명제를 정의한다. 

    - 용어 집합은 다음과 같이 귀납적으로 정의된다.

        1. 변수들. 모든 변수는 용어이다. 

        2. 함수들. $n$ 개의 파라미터를 갖는 임의의 함수 $f(t_1, \dots,t_n)$ 는 용어이다. 

    - 식(formula) 집합은 다음과 같이 귀납적으로 정의된다.

        1. 술어 기호들. $n$ 항수를 갖는 $P(t_1, \dots, t_n)$ 는 식이다.

        2. 동등성. $t_1, t_2$ 가 용어이면 $t_1 = t_2$ 는 식이다. 

        3. 부정. $\phi$ 가 식이면 $\lnot \phi$ 도 식이다.

        4. 이항 연결사. $\phi , \psi$ 가 식이면 이항관계 $R$ 에 대하여 $\phi R \psi$ 도 식이다. 가령 $\phi , \psi$ 가 식이면 $\phi \to \psi$ 은 식이다.

        5. 양화사. $\phi$ 가 식이고, $x$ 가 변수이면 $\forall x \phi$ 이나 $\exists x \phi$ 는 식이다.

        1차 논리에서는 오직 위의 5가지 규칙을 유한하게 구성하여 얻어진 표현만 식이다. 가령 $\forall xx \to$ 는 식이 아니다.
        
        참고로 첫번째와 두번쨰 규칙만 적용하여 얻은 식을 [원자적 식(atomic formulas)](https://en.wikipedia.org/wiki/Atomic_formula) 라고 한다.

        괄호는 모든 식이 유일한 귀납적 방법으로 생성되었음을 알려준다. 이는 모든 식이 유일한 [parse tree](https://en.wikipedia.org/wiki/Parse_tree) 를 갖는 것을 말해준다.

        위와 같은 1차 논리에서의 식은 다음과 같은 [BNF 형식](https://en.wikipedia.org/wiki/Backus-Naur_form)으로도 표현할 수 있다.

        ```bnf
        <index>             ::= "" 
                            | <index> "'"
        <variable>          ::= "x" <index>
        <constant>          ::= "c" <index>
        <unary function>    ::= "f1" <index>
        <binary function>   ::= "f2" <index>
        <ternary function>  ::= "f3" <index>
        <unary predicate>   ::= "p1" <index>
        <binary predicate>  ::= "p2" <index>
        <ternary predicate> ::= "p3" <index>
        <term>              ::= <variable> 
                            | <constant> 
                            | <unary function> "(" <term> ")" 
                            | <binary function> "(" <term> "," <term> ")" 
                            | <ternary function> "(" <term> "," <term> "," <term> ")"
        <atomic formula>    ::= "TRUE" 
                            | "FALSE"
                            | <term> "=" <term>
                            | <unary predicate> "(" <term> ")" 
                            | <binary predicate> "(" <term> "," <term> ")" 
                            | <ternary predicate> "(" <term> "," <term> "," <term> ")"
        <formula>           ::= <atomic formula> 
                            | "¬" <formula>
                            | <formula> "∧" <formula>
                            | <formula> "∨" <formula>
                            | <formula> "⇒" <formula>
                            | <formula> "⇔" <formula>
                            | "(" <formula> ")"
                            | "∀" <variable> <formula>
                            | "∃" <variable> <formula>
        ```

- 1차 논리에서의 논리 연산자들은 먼저 계산되어야 할 우선순위를 갖는다.

    1. $\lnot$ 이 가장 먼저 계산된다.

    2. $\land, \lor$ 이 다음으로 계산된다.

    3. 양화사가 다음으로 계산된다.

    4. $\to$ 가 마지막으로 계산된다.

    그러므로 $\lnot \forall xP(x) \to \exists x \lnot P(x)$ 를 

    $$ (\lnot [\forall xP(x)]) \to \exists x[\lnot P(x)] $$

    로 표현하면 더 읽기 쉽다.

- 1차 논리에서의 식에 포함된 변수는 free 이거나 bound 이다. 쉽게 말하면 양화사에 속박된 변수를 bound 라고 생각하고, 그 이외의 변수를 free 로 생각하면 된다. 가령 $\forall y P(x, y)$ 에서 $y$ 는 bound 이고 $x$ 는 free 이다. free 와 bound 변수는 다음과 같이 귀납적으로 정의된다. 

    1. 원자적 식(atomic formulas): $\phi$ 가 원자적 식이면 $\phi$ 에 등장하는 변수는 free 이다. 원자적 식에 bound 변수는 존재하지 않는다. 

    2. 부정: $\lnot \phi$ 에 나타나는 변수 $x$ 가 free 이면 $\phi$ 에 나타나는 변수 $x$ 도 free 이다. 마찬가지로 $\phi$ 의 변수가 bound 이면 $\lnot \phi$ 의 변수도 bound 이다.

    3. 이항 연결사: $\phi$ 나 $\psi$ 에서 $x$ 가 free 이면 이항 연결사 $R$ 에 대하여 $\phi R \psi$ 의 $x$ 도 free 이다. 가령 $\phi$ 에서 $x$ 가 free 이면 $\phi \to \psi$ 의 $x$ 도 free 이다. bound 의 경우도 마찬가지이다.

    4. 양화사: $\forall y \phi$ 의 변수 $x$ 가 free 이면 $\phi$ 에서도 free 이다. $\forall y \phi$ 의 $x$ 가 bound 이려면, $x$ 가 $y$ 이거나 $\phi$ 에서도 $x$ 가 bound 이어야 한다. $\exists$ 에서도 마찬가지이다.

- free 변수가 없는 식을 sentence 라고 한다.

- 예시 

    아벨리안 순서군(ordered abelian groups) 은 상수 $0$, 영항 함수 $-$, 이항 함수 $+$, 이항 관계 $\leq$ 를 갖는다. 아벨리안 순서군에서 $x+y, x+y-z$ 들은 용어이다. $x+y=0, x+y-z \leq x+y$ 들은 원자적 식이다. $\forall x \forall y(x+y \leq z) \to \forall x \forall y(x+y=0)$ 는 free 변수 $z$ 를 갖는 식이다.

    아벨리안 순서군의 공리는 language 의 sentence 집합이다. 가령 군의 공리인 commutative 는 $(\forall x)(\forall y)[x+y=y+x]$ 이다.

- 1차 논리의 해석은 language 의 비논리적 기호에 명시적 의미를 부여한다. 각각의 용어는 그것을 대표하는 객체를 부여받고, 술어는 객체의 속성을 부여받고, sentence 는 진리값을 부여받는다. 형식 언어의 해석에 대한 연구를 [formal semantics](https://en.wikipedia.org/wiki/Semantics_of_logic) 라 한다. 이로써 1차 논리는 표준적인 또는 [Tarskian 의미](https://en.wikipedia.org/wiki/Semantic_theory_of_truth#Tarski.27s_Theory) 를 부여받는다. 혹은 1차 논리에 [게임 의미](https://en.wikipedia.org/wiki/Game_semantics#Classical_logic) 를 부여할 수도 있다.

    논의 영역 $\mathbb{D}$ 는 객체들의 집합이다. 식은 이러한 객체들에 대한 문장이다. 가령 $\exists xP(x)$ 는 술어 $P$ 를 만족하는 객체 $x$ 의 존재성을 뜻한다. 
    
    함수 기호에 대한 해석은 함수이다. 가령 항수 $2$ 를 갖는 함수 기호 $f$ 는 두 정수의 합을 계산하는 함수로 해석 가능하다. 상수 기호는 항수 $0$ 을 갖는 함수로 해석한다. 가령 상수 기호 $c$ 를 $I(c) = 10$ 으로 해석할 수 있다. $I$ 는 해석을 뜻하는 메타 기호이다.

    항수 $n$ 에 대한 술어는 논의 영역 $\mathbb{D}$ 에서 술어를 참이 되게 하는 $n$-순서쌍으로 해석할 수 있다.

    - 1차 논리의 해석을 규정하는 가장 일반적인 방법은 구조(structure) 를 정의하는 것이다. 구조를 모델(model) 로도 부른다. 구조는 공집합이 아닌 $\mathbb{D}$ 와 비논리 기호의 해석 $I$ 를 갖는다. 해석은 그 자체로 다음과 같은 함수가 된다.

        - 항수 $n$ 인 함수 기호 $f$ 는 함수 $I(f): \mathbb{D} ^{n} \to \mathbb{D}$ 로 할당된다. 각가의 부호수기호들은 논의 영역의 객체로 할당된다. 

        - 항수 $n$ 인 술어 기호 $P$ 는 관계 $I(P): \mathbb{D} ^{n} \to \{\bot , \top \}$ 으로 할당된다.
    
    식은 주어진 해석에 의하여 참이나 거짓을 부여받고, 논의 영역의 변수에 따르는 값 $\mu$ 를 할당받는다. 값의 할당이 필요한 이유는 $y = x$ 에서의 free 변수에 할당하기 위해서이다. 이 식의 진리값은 $x, y$ 에 따라 달라진다.

    값 할당 $\mu$ 는 각각의 용어가 논의 영역 $\mathbb{D}$ 의 원소에 대응되는 결과에 의하여 language 의 모든 용어로 확장된다. 할당 규칙은 다음과 같다. 

    1. 변수들: 각각의 변수 $x$ 는 $\mu (x)$ 로 할당된다. 

    2. 함수들: 논의 영역의 원소 $d_1, \dots, d_n$ 로 할당된 주어진 용어 $t_1, \dots, t_n$ 에 대하여 함수 기호 $f$ 의 용어 $f(t_1, \dots, t_n)$ 는 $(I(f))(d_1, \dots, d_n)$ 으로 할당된다.

    이렇게 값이 할당된 이후에 각각의 식의 진리값이 할당된다. 다음과 같이 진리값을 귀납적으로 할당하는 귀납적 정의를 [T-schema](https://en.wikipedia.org/wiki/T-schema) 라고 한다.

    1. 원자적 식 1: $\big <v_1, \dots, v_n\big > \in I(P)$ 로 할당된 용어 $t_1, \dots, t_n$ 에 대한 식 $P(t_1, \dots, t_n)$ 의 진리값은 $\big <v_1, \dots, v_n\big >$ 의 값에 의존한다.

    2. 원자적 식 2: 식 $t_1 = t_2$ 는 $t_1$ 와 $t_2$ 에 할당된 $\mathbb{D}$ 의 객체가 같을 때 진리값 참을 부여받는다.

    3. 논리적 연결사: $\lnot \phi , \phi \to \psi$ 같은 식의 진리값은 명제 논리에서와 같이 논리 연산자의 진리표에 따라 부여된다. 

    4. 존재 양화사: 식 $\exists x \phi (x)$ 는 $x$ 의 해석 값 $\mu$ 와 $\phi$ 의 해석 $M$ 에 대하여 $M$ 에서 술어 $\phi$ 를 참이 되게 하는 $\mu$ 와 다른  $\mu '$ 가 존재하면 참을 부여받는다. 

    5. 보편 양화사: 식 $\forall x \phi (x)$ 는 $x$ 의 해석 값 $\mu$ 와 $\phi$ 의 해석 $M$ 에 따른 모든 페어가 식 $\phi (x)$ 을 참이 되게 할 때 참을 부여 받는다. 

    주어진 해석 $M$ 에 대하여 sentence $\phi$ 가 참을 부여받으면 이를 $M \vDash \phi$ 라고 표기하며, sentence 가 어떤 해석 아래에서 참이면 statisfiable 하다고 한다.

    식이 valid 하다는 것은 모든 해석에 대하여 참이라는 것이다. 이러한 식은 명제 논리의 tautology 와 비슷한 역할을 한다. 

    식 $\phi$ 가 식 $\psi$ 의 논리적 결과(logical consequence)라는 것은 $\psi$ 를 참으로 만드는 모든 해석이 $\phi$ 도 참으로 만든다는 것이다. 이것을 $\phi \vDash \psi$ 로 표기한다.

- 1차 논리에 의미를 부여하는 또 다른 방법은 추상 대수학을 통해서이다. 이 접근은 명제 논리에 대한 [Lindenbaum-Tarski algebra](https://en.wikipedia.org/wiki/Lindenbaum%E2%80%93Tarski_algebra) 을 일반화한 것이다. 1차 논리의 양화사를 제거하는 방법이 다음과 같이 3 가지 있다. 

    - Cylindric 대수학, Polyadic 대수학, Predicate functor 논리 

    이 대수학들은 [two-element Boolean 대수학](https://en.wikipedia.org/wiki/Two-element_Boolean_algebra) 을 적절히 확장한 lattice(격자)이다. Tarski 와 Givant 는 원자적 식을 갖지 않는 1차 논리의 파편이 relation algebra 와 같은 표현력을 갖는다는 것을 보였다. 이 파편은 사람들의 흥미를 끌었는데, 이것이 페아노 공리계와 ZFC 를 포함한 공리적 집합론들을 만족시켰기 때문이다.

- 한편 논의 영역 $\mathbb{D}$ 가 공집합인 경우도 존재한다.

- 1차 논리에서 동등함을 나타내기 위하여 기호 $=$ 를 사용하는데, 이것을 해석했을 때 실제로 동등함을 뜻하도록 하기 위하여 다음과 같은 공리를 추가한다. 

    1. Reflexivity: 변수 $x$ 에 대하여 $x=x$ 이다.

    2. Substitution for functions: 변수 $x, y$ 와 함수 기호 $f$ 에 대하여 $x = y \to f(x) = f(y)$ 이다. 

    3. Substitution for formulas: 변수 $x, y$ 와 식 기호 $\phi (x)$ 에 대하여 $\phi '$ 가 $x$ 를 $y$ 로 치환해서 얻은 식이라면, $x = y \to (\phi \to \phi ')$ 이다.

    이들은 공리꼴이므로 무한한 공리집합을 형성한다. 동등함에 관한 다른 성질들은 위 공리의 논리적 귀결이다. 가령 다음과 같은 성질들은 위 공리의 귀결에 불과하다. 

    1. Symmetry: $x = y \implies y = x$

    2. Transitivity: $x = y \land y = z \implies x = z$

- 고차 논리가 아닌 1차 논리를 사용하는 주된 이유는 중요한 메타논리적 성질들이 성립하기 때문이다. 이 성질들은 1차 이론들에 개별적으로 적용되는 것이 아니라 1차 논리 전체에 적용된다. 이 성질들은 1차 이론의 모델을 구성할 수 있는 근본적인 도구를 제공해준다. 그 메타논리적 성질들은 다음과 같다. 

    - 완전성과 결정불가능성: 괴델의 완전성 정리는 건전하고, 완전하고, effective 한 연역 체계가 1차 논리에 존재함을 말해준다. $\phi$ 가 $\psi$ 를 함의할 때 $\phi$ 가 임의의 기수를 가질 수 있으므로 논리적 도출 과정을 검증하는 것이 효율적으로 이루어질 수 없다. 그러나 $\phi$ 에서 도출된 $\psi$ 들을 유한하게 나열할 수 있어서 검증이 가능해진다. 즉, 1차 논리는 준결정가능성을 갖는다.

        명제논리와 달리 1차 논리는 결정불가능성을 갖는다. 이는 어떤 식이 논리적으로 올바른지 검증하는 결정 절차가 존재하지 않는다는 것이다. 이는 알론조 처치와 앨런 튜링이 힐베르트가 제안한 [Entscheidungsproblem](https://en.wikipedia.org/wiki/Entscheidungsproblem) 에 대답하려는 연구에 의하여 밝혀졌다. 이들의 증명은 1차 논리의 결정 문제의 해결불가능성과 정지 문제의 해결 불가능성에 대한 대응을 보이는 것이었다.

        그러나 1차 논리보다는 약하지만 결정 절차가 존재하는 논리가 있는데, 명제 논리와 monadic predicate logic 등이 있다. monadic predicate logic 은 1차 논리에서 함수 기호를 제외하고 술어가 항수 $0$ 만을 가지도록 제한한 것이다. 1차 논리의 [guarded fragment](https://en.wikipedia.org/wiki/Guarded_logic) 도 결정가능성을 갖고 Bernays-Schonfinkel class 도 결정 가능성을 갖는다.

        1차 논리의 결정가능성을 갖는 부분집합을 연구하는 분야를 [Description logic](https://en.wikipedia.org/wiki/Description_logic) 이라 한다.

    - 뢰벤하임-스콜렘 정리: 이 정리는 기수 $\lambda$ 를 갖는 1차 이론이 무한한 모델을 가진다면, 1차 이론이 $\lambda$ 보다 같거나 큰 모든 무한 기수의 모델을 가진다는 것을 말해준다.

        모델 이론의 초기 성과는 가산 집합인 부호수를 기반으로 하는 1차 논리의 언어로 가산성과 비가산성을 나타내는 것이 불가능하다는 것을 보인 것이다. 즉, 1차 논리 식 $\phi (x)$ 과 $\phi$ 를 만족하는 임의의 모델 $M$ 에 대하여, $M$ 이 가산이거나 비가산이면 식 $\phi$ 는 존재할 수 없다는 것이다.

        이 정리는 무한한 구조가 1차 논리에서 categorical 하게 공리화될 수 없음을 말한다. 가령 오직 실수의 직선을 모델로 갖는 1차 논리는 존재하지 않는다. 이는 무한한 모델을 갖는 1차 논리는 반드시 연속체보다 큰 기수를 가지는 모델을 갖는다는 것이다. 그렇다면, 실수의 직선을 만족하는 모든 이론은 비표준 모델에 의하여 만족된다.

        이 정리가 1차 집합 이론에 적용되면 스콜렘의 역설 같은 비직관적인 결과가 도출된다. 

    - 콤팩트성 정리: 1차 논리의 sentence 집합이 모델을 가지고, 그것의 모든 유한 부분집합이 모델을 갖는다는 것이다. 이는 식(formula)이 1차 논리의 무한 공리 집합에서 도출되었다면 그것은 유한 공리 집합의 논리적 도출이라는 것이다. 이 정리는 괴델이 그의 완전성 정리에서 도출한 정리이다. 이 정리는 모델 이론에서 모델을 구성하는 기본적인 도구가 된다. 

        콤팩트성 정리를 함의한 1차 논리에는 여러 제한이 있다. 가령 컴퓨터 공학에서 많은 상황이 그래프로 모델링되는데, 그러한 체계를 증명하는 것은 좋은 상태가 나쁜 상태로 도달하지 않는다는 것을 보이는 것이다. 하지만 콤팩트성 정리는 그래프가 1차 논리에서 elementary class 가 아님을 보여주고 식 $x$ 에서 $y$ 로 가는 경로를 뜻하는 식 $\phi (x,y)$ 가 존재하지 않음을 보여준다.

    - 린드스트롬 정리(Lindstrom's theorem): 이 정리는 지금까지 논의한 메타논리적 성질이 1차 논리보다 강력한 논리 체계에서는 만족되지 못한다는 것을 말한다. 이 정리를 만족하는 논리 체계는 1차 논리를 포함하며 뢰벤하임-스콜렘 정리와 콤팩트성 정리를 만족하는 논리체계가 1차 논리와 동등하다는 것을 말해준다. 

- 1차 논리가 수학과 컴퓨터 공학을 형식화하기에 충분하지만, 그 표현력에 제한이 있다. 가령 1차 논리는 결정불가능성을 갖는다. 이는 증명가능성에 대한 건전하고 완전한 결정 과정이 존재하지 않음을 뜻한다. 이는 오직 두개의 변수를 갖는 1차 논리인 $C_2$ 같은 결정가능한 1차 논리의 부분집합에 대한 연구를 시작시켰다. 

    뢰벤하임-스콜렘 정리는 무한한 모델을 갖는 1차 이론이 모든 기수에 대한 무한 모델을 갖는다는 것을 말해준다. 즉, categorical 한 무한 모델을 갖는 1차 이론은 존재하지 않는다. 더 자세히 말해서 오로지 $\N$ 이나 $\R$ 을 논의 영역으로 갖는 1차 이론은 존재하지 않는다. 1차 논리의 확장인 무한 논리나 고차 논리는 무한 집합을 논의 영역으로 가져도 categorial 하게 공리화할 수 있다. 하지만 린드스트롬 정리에 의하여 1차 논리보다 강력한 논리 체계는 콤팩트성 정리나 뢰벤하임-스콜램 정리가 성립하지 않는다는 단점이 있다. 

    또한 1차 논리는 "모든 사람은 숨을 쉰다." 같은 간단한 자연어를 형식화할 수 있지만, 더 복잡한 자연어를 표현하기 어렵다. 자연어를 분석하려면 1차 논리보다 강력한 논리 체계가 필요하다.

- 1차 논리를 제한하거나 확장함으로써 얻어진 여러 변형이 있다. 가령 무한 논리는 무한한 크기의 식을 허용하고, 양화 논리는 가능성이나 필요성을 표현하는 기호를 도입했다.

    - 1차 논리는 다음과 같이 제한될 수 있다. $\exists x \phi (x)$ 는 $\lnot \forall x \lnot \phi (x)$ 로 표현될 수 있고, 그 역도 가능하다. 그러므로 $\exists$ 나 $\forall$ 중 하나를 제외할 수 있다. 마찬가지의 이유로 $\land$ 나 $\lor$ 중 하나를 제외시킬 수 있다. $\land , \lor$ 이나 $\land , \land$ 이나 $\lnot , \to$ 이나 NAND 나 NOR 만으로 다른 논리 연산자를 다 표현할 수 있다. 함수 기호도 제외시킬 수 있는데  상수 $0$ 을 술어 $0(x)$ 으로 표현하거나 함수 $f(x)$ 를 술어 $F(x, y)$ 로 표현하는 것이다.

        1차 논리를 제한하면 추론 규칙이나 공리 꼴의 수를 줄일 수 있어서 메타 논리 증명이 짧아져서 편하다. 
    
    - 추가적인 양화사를 도입할 수도 있다. 가령 유일하게 존재한다는 것을 표현하기 위하여 $\exists !xP(x)$ 와 같이 $\exists !$ 를 도입하는 경우가 있다. 이는 $\exists x (P(x) \land \forall y(P(y) \to (x=y)))$ 의 축약이다. 이를 uniqeuenss quantification 이라 하고, branching quantifier 나 bounded quantifier 같은 양화사도 있다. 

    - 무한논리는 sentence 의 무한한 길이를 허용하는 것이다. 가령 $\lor$ 이나 $\land$ 를 무한히 이어붙이게 할 수도 있고, 무한한 변수에 양화사를 붙힐수도 있고, 무한한 항수를 가지는 함수나 관계를 허용할 수도 있다. 무한 논리는 위상수학와 모델 이론에서 자주 사용된다. 무한논리를 유한한 글자로 표현할 수 없기에 트리를 사용하기도 한다. 이때 사용하는 게 parse tree 이다. 

        무한논리에서 $L _{\alpha \beta }$ 와 같은 표현을 사용하는데 $\alpha$ 와 $\beta$ 는 기수이거나 $\infty$ 이다. 이로써 1차 논리의 서수를 $L _{\omega \omega }$ 로 표현할 수 있고, $L _{\infty \omega }$ 논리는 무한한 $\lor , \land$ 나 무한한 변수를 사용할 수 있게 한다. 요점은 논리 체계 $L _{\kappa \omega }$ 가 $\kappa$ 개 이하의 논리 연산자($\lor ,\land$) 의 사용을 허용한다는 것이다. 

        $L _{\kappa \infty }$ 논리체계의 경우 무한한 변수에 양화사를 가할 수 있다. 즉, $L _{\kappa \lambda }$ 는 $\lambda$ 보다 작은 변수에 양화사를 가할 수 있고, $\kappa$ 보다 작은 길이의 논리 연산자($\land ,\lor$) 를 허용한다.

    - [직관 1차 논리(직관 논리, Intuitionistic first-order logic)](https://en.wikipedia.org/wiki/Intuitionistic_logic) 는 고전적인 명제 논리가 아닌 직관을 사용한다. 가령 직관논리에서는 $\lnot \lnot \phi \neq \phi$ 이다.

    - 1차 양화 논리는 좀 더 현실 세계의 논리를 표현해준다. 즉, "$\phi$ 가 필요하다" 나 "$\phi$ 가 가능하다" 같은 명제를 표현할 수 있다.

    - 1차 퍼지 논리는 고전 명제 논리가 아닌 명제 퍼지 논리를 사용한다.

- 1차 논리는 객체에 양화사를 사용할 수 있지만 술어에는 사용할 수 없다. 가령 $\exists a(P(a))$ 는 1차 논리에서 올바르지만 $\exists P(P(a))$ 는 올바르지 않다. 2차 논리는 1차 논리를 확장하여 후자의 명제도 올바르게 만든다.

    1차 논리가 오직 하나의 의미(semantic)를 연구하는 것과 달리 2차 논리에는 가능한 몇몇의 의미가 존재한다. 2차 논리와 고차 논리에서의 의미는 full semantic 을 뜻한다. 

- [자동 정리 증명](https://en.wikipedia.org/wiki/Automated_theorem_proving) 은 수학 정리의 증명을 찾는 컴퓨터 프로그램을 뜻한다. 증명을 찾는 것은 search space 가 매우 크기 때문에 정말 어렵고 사실은 NP 문제라서 컴퓨터로 해결하기에 불가능하다. 따라서 휴리스틱 알고리즘들이 많이 개발되었다. 

    비슷한 영역으로 [증명 검증](https://en.wikipedia.org/wiki/Proof_verification) 이 있는데 자동 정리 증명보다 훨씬 적은 비용으로 인간이 만든 증명을 검증해줄 수 있다. 이런 프로그램들은 타입 이론같은 1차 논리보다 강력한 형식 체계를 사용한다. 

    자동 정리 증명은 어떤 알고리즘의 타당성을 검증하는 [형식 검증](https://en.wikipedia.org/wiki/Formal_verification) 에도 사용될 수 있다. 

!!! def ""

    부호수(signature) : 집합 $S _{\text{func}}, S _{\text{rel}}$ 과 함수 $\text{ar}$ 대하여 

    $$ \sigma = (S _{\text{func}}, S _{\text{rel}}, \text{ar}) $$

    이다.

- $S _{\text{func}}$ 은 함수 기호로써 가령 $+, \times , 0, 1$ 로 구성된다. $S _{\text{rel}}$ 은 관계 기호 혹은 술어로써 가령 $\leq , \in$ 로 구성된다. $\text{ar}: S _{\text{func}} \cup S _{\text{rel}} \to \N$ 은 모든 함수와 관계에 자연수를 부여하는 항수(arity)라고 부른다.

    - 영항수(0-ary) 함수기호를 상수라고 한다.
    
- 부호수는 형식 언어에서 사용하는 비논리 기호의 집합이다. 1차 논리에서 사용되는 비논리적 기호는 술어(관계), 함수, 논의 영역을 지칭하는 집합 등을 표현한다. 

    - 예시 
    
        군에서는 부호수가 $\{1, \times \}$ 이고, 순서체에서는 $\{0,1,+,\times , <\}$ 이다. 
        
    하지만 비논리 기호에 제한은 없다. 부호수는 공집합일 수 있고, 유한할 수도 있고, 무한할 수도 있고, 비가산 집합일 수도 있다. 비가산 부호수는 뢰벤하임-스콜렘 정리의 증명에서 등장한다. 

    - 예시 

        무한 부호수는 무한 스칼라 체 $F$ 에 대하여 $S _{\text{func}} = \{+\} \cup \{f_a:a \in F\}$ 와 $S _{\text{rel}} = \{=\}$ 를 사용하여 벡터 공간을 형식화하는데 사용된다. $f_a$ 는 $a$ 에 의한 스칼라곱 단항 연산을 표현하는데 사용된다.

- 부호수에서 함수기호 $S _{\text{func}}$ 가 없는 것을 관계 부호수(relational signature) 라고 하고, 부호수에서 관계기호 $S _{\text{rel}}$ 가 없는 것을 대수적 부호수라고 한다. 집합 $S _{\text{func}}$ 과 $S _{\text{rel}}$ 유한하면 유한 부호수(finite signature) 라고 한다.

- 부호수 $\sigma = (S _{\text{func}}, S _{\text{rel}}, \text{ar})$ 의 기수는 

    $$ |\sigma | = | S _{\text{func}} | + | S _{\text{rel}} | $$

    와 같이 정의된다. 한편 부호수 $\sigma$ 를 갖는 language $L$ 의 기수는 거의 언제나 무한이다. 만약 $\sigma$ 가 유한하면 $L$ 의 기수는 $\aleph _0$ 이다.

- language of signature 는 해당 부호수의 기호로 구성된 모든 잘 구성된 sentence 의 집합이다.

- 보편 대수학에서 부호수는 대수 구조를 특징짓는 연산의 리스트이다. 모델이론에서 부호수는 비논리 기호를 표현하는데에도 사용되고, 연산 기호의 집합을 표현하는데에도 사용된다.

    보편 대수학에서 부호수는 타입(type) 으로도 불리고, 모델이론에서 부호수를 단어(vocabulary) 라고도 부른다.

- 부호수의 정확한 정의를 매번 내리는 것이 불편하므로 부호수는 종종 비형식적인 방식으로 편하게 정의된다. 

    - 예시 

        가환군의 부호수는 종종 $\sigma = (+,-,0)$ 으로 정의된다.

!!! note

    우리에게 필요한 것은 자동 정리 증명에 딥러닝이나 머신러닝을 적용하여 그것의 성능을 최대한 올리는 것이고, GEB 나 TS is near 에서 말했듯 다루고 있는 체계보다 상위 체계에서 하위 체계를 다룰 수 있는 능력이다. 이것으로 기계적인 수준의 정리들에 의미를 부여하거나 결정불가능한 정리도 "결정불가능하다" 는 결론을 내려줄 수 있다. 

    상위 체계로 도약할 수 있는 능력을 부여한다면, 하위 체계에서 상위체계로 도약하는 행위 자체를 추상화시킬 수 있다는 것을 학습시킬 수 있다.

!!! def ""

    1차 이론(first-order theory) : 1차 논리에서 1차 이론이란 부호수의 기호로 구성된 sentence 인 공리들의 집합이다.

- 공리들의 집합은 유한하거나 [재귀적으로 열거가능](https://en.wikipedia.org/wiki/Recursively_enumerable)해야 한다. 이 경우 이론이 effective 하다고 한다. 종종 이론은 공리의 모든 논리적 귀결 또한 포함해야 한다고 여겨진다.

- 주어진 이론의 모든 sentence 를 만족하는 1차 구조(structure) 를 이론의 모델(model) 이라고 한다. elementary class 는 주어진 이론을 만족하는 모든 구조의 집합이다. 이러한 class 는 모델 이론의 주요 연구 대상이다.

- 대부분의 이론은 의도된 해석을 가진다. 가령 페아노 공리계의 의도된 해석은 우리가 일상에서 사용하던 자연수이다. 그러나 뢰벤하임-스콜렘 정리는 거의 모든 1차 이론이 비표준 모델을 갖는다는 것을 보여준다. 비표준 모델이란 표준 모델에 대한 동형사상을 갖는 이론의 또 다른 모델이다.

- 1차 이론이 일관적이라는 것(무모순성, consistent)은 주어진 이론의 공리가 모순을 도출하지 않는다는 것이고, 1차 이론이 완전하다는 것은 부호수의 모든 식이 공리로부터 도출된다는 것이다.

    그러나 괴델의 불완전성 정리는 자연수 이론을 만족하는 effective 한 이론은 일관성과 완전성을 동시에 만족할 수 없음을 보여준다.

- 예시 

    순서, 격자, 군, 환, 체, 기하학, 미분 대수, 자연수, 산술, 집합론 등이 1차 이론이다.

!!! def ""

    연역 체계 : 1차 논리에서 연역 체계란 순수하게 추론 규칙만으로 어떤 식이 다른 식의 논리적 귀결임을 보이려하는 형식 체계이다.

- 1차 논리에서 힐베르트 연역 체계, 자연 연역, 시퀸트 계산, tableaux method, resolution 등이 연역 체계이다. 이들은 연역이 유한적으로 구성되어야 한다는 속성을 갖는다. 이러한 유한한 연역을 증명 이론에서는 derivation 이라고 한다. 이 유한한 연역을 증명이라고 부르지만, 이는 자연어에 의한 증명과는 달리 완벽하게 형식화되었다.

- 연역 체계가 건전하다(sound)는 것은 증명된 식이 의미적으로 올바르다는 것이고, 완전하다(complete)는 것은 모든 올바른 식이 증명가능하다는 것이다. 

- 연역 체계의 핵심 성질이 명제가 순수하게 변형 규칙에 의하여 도출되므로, 연역 체계에서는 명제의 의미를 해석할 필요 없이 명제의 참과 거짓을 검증할 수 있다.

- 일반적으로 1차 논리의 논리적 결론들은 [준결정적](https://en.wikipedia.org/wiki/Decidability_(logic)#Semidecidability)이다. 

- 추론 규칙(연역 규칙) 은 가정이 되는 명제 집합에서 결론을 이끌어낸다. 이때 추론 규칙이 건전하다(sound, truth-preserving)는 것은 참인 가정에 이 규칙을 적용하여 도출한 결론도 참이라는 것이다.

    - 예시 

        추론 규칙의 한 예시는 치환이다. 용어 $t$ 와 변수 $x$ 를 갖는 식 $\phi$ 에 대하여 $\phi [t/x]$ 는 $x$ 를 $t$ 로 치환한 명제이다. 

    치환 규칙에서는 $t$ 의 free 변수가 치환 도중에 bound 될 수 없다. 가령 산술 부호수$(0,1,+,\times,=)$ 위에서 정의된 식 $\phi$ 가 $\exists x(x=y)$ 라고 하자. 이때 용어 $t$ 를 $x+1$ 라고 하면 식 $\phi [t/y]$ 는 $\exists x(x=x+1)$ 이 된다. 하지만 이것은 대다수의 해석이 거짓을 부여할 것이다. 이 문제는 $t$ 의 자유 변수 $x$ 가 치환 도중에 bound 되었기 때문이다. 이 상황에 대한 해결책은 식 $\phi$ 의 bound 변수 $x$ 를 $z$ 로 바꾸는 것이다. 그러면 $\exists z(z=x+1)$ 이 되어 참인 명제가 된다.

    위와 같은 제한을 기반으로 추론 규칙을 적용해야 무의미한 기호들을 계속 연역해나가도 그것들이 해석했을 때 참인 명제라는 보장을 얻을 수 있다. 요점은 명제가 진리임을 보존하는 연역 규칙을 적용해야 한다.

- 예시 

    힐베르트 스타일 체계는 논리적 공리를 갖는다. 논리적 공리는 공리꼴로 구성된다. 추론 규칙은 양화사를 조작할 수 있게 해준다. 힐베르트 스타일 체계의 특징은 매우 적은 추론 규칙과 무한한 논리적 공리의 공리꼴을 갖는다는 것이다. 보통 전건 긍정과 일반화(universal generalization) 만을 추론규칙으로 갖는다.

    자연연역은 힐베르트 스타일 체계를 닮았다. 자연 연역은 논리 꼴은 갖지 않고 그 대신 추론 규칙을 좀 더 추가한다.

- 예시 

    시퀸트 계산(Sequent calculus)은 자연 연역 체계의 성질을 연구하기 위하여 개발되었다. 시퀸트 계산은 한번에 하나의 식을 다루는 다음과 같은 형태의 대신 시퀸트를 다룬다.

    $$ A_1, \dots,A_n \vdash B_1, \dots, B_k $$

    이 식은 $(A_1 \land \dots \land A_n) \implies (B_1 \lor \dots \lor B_k)$ 라는 뜻이다.

- 예시 

    Tableaux method 는 식의 나열을 다루지 않고, 트리 형태로 식을 다룬다. Tableaux 는 식 $A$ 가 증명가능하다는 것을 보이기 위하여 그 부정문 $\lnot  A$ 가 증명될 수 없음을 보인다.

    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Prop-tableau-4.svg/225px-Prop-tableau-4.svg.png)

- 예시 

    [분해 증명(resolution)](https://en.wikipedia.org/wiki/Resolution_(logic)) 은 [unification](https://en.wikipedia.org/wiki/Unification_(computer_science)#Definition_of_unification_for_first-order_logic) 과 함께 하나의 추론 규칙인데, 1차 논리에서 건전하고 완전하다.

    tableaux 와 같이 어떤 식을 증명하기 위하여 그 부정문이 성립하지 않음을 보인다. 분해 증명은 자동 정리 증명에서 사용된다. 

# 형식 언어, 이론, 모델

!!! def ""

    형식 언어(formal language) : 알파벳 $\Sigma$ 위의 형식 언어 $L$ 은 $\Sigma ^{*}$ 의 부분집합이다.

- 형식 언어는 alphabet 을 기호로 한다. alphabet 은 특정 문자들의 집합을 뜻한다. alphabet 은 무한 집합일 수도 있지만, 형식 언어의 대부분의 정의는 유한 집합의 alphabet 을 정의한다. 

    word 는 alphabet 으로 이루어진 유한열(string)이다. alphabet 집합 $\Sigma$ 위의 모든 word 집합을 $\Sigma ^{*}$ 로 표기한다.

- 예시 

    알파벳 $\Sigma = \{0,1,2,3,4,5,6,7,8,9,+,=\}$ 위의 형식 언어 $L$ 이 다음 규칙을 따른다고 하자. 

    1. 공집합이 아닌 string 은 $+, =$ 를 포함하지 않으며 $0$ 으로 시작하지 않는다. 

    2. string "$0$" 은 $L$ 의 원소이다. 

    3. "$=$" 를 포함한 string 이 있다면 $=$ 는 반드시 하나만 존재하고, 이는 두 $L$ 의 string 을 구분한다.

    4. string 에 $+$ 가 있고 $=$ 가 없다면 $+$ 가 두 $L$ 의 string 을 구분하는 경우이다.

    5. 위 규칙 이외의 string 은 $L$ 에 존재하지 않는다. 

    이 규칙에 따르면 string "$23+4=555$" 은 $L$ 에 속했지만, string "$=234=+$" 은 속하지 못한다.

- 위의 예시에서 $0$ 을 zero 라고 부르고 싶고, $+$ 를 덧셈이라고 부르고 싶겠지만, 형식 언어에서 각각의 기호들은 전적으로 무의미한 기호에 불과하다. 그러나 이것을 모델에 의한 해석을 하면 일상에서의 의미이 zero 나 덧셈으로 부를 수 있다.

- $L$ 이 공집합일 수도 있고, 유한 집합일 수도 있지만 보통 $L$ 은 무한집합이다. 

    - 예시 

        유한 알파벳 $\Sigma = \{a,b\}$ 은 무한 집합 $L = \{a, aaa, abb, abba, \dots\}$ 을 생성한다.

    - 예시

       주어진 프로그래밍 언어(alphabet) 에 대하여 문법적으로 올바른 프로그램 집합은 형식 언어 $L$ 이다.

       입력 집합에 대한 특정한 튜링 머신은 형식 언어 $L$ 이다.
 
- 컴퓨터 공학에서 형식 언어는 프로그래밍 언어의 문법을 정의하는 기반을 형성하는데 사용된다. 계산 이론에서 결정 문제를 보통 형식 언어를 사용하여 정의하고 [복잡도 집합](https://en.wikipedia.org/wiki/Complexity_class) 을 정의할 때 사용된다.

- 논리학과 수학기초론에서는 공리 체계의 문법을 표현할 때 사용된다. 형식주의가 이런 형식 언어로 모든 수학을 표현할 수 있다는 철학이다.

- 프레게가 형식 언어를 사용하였다.

- 형식 언어 간의 연산도 정의할 수 있다. 이러한 연산들은 형식 언어의 폐포(closure) 의 성질을 연구할 때 사용된다. 대표적으로 다음과 같은 연산들이 있다.

    |Operation||
    |:---:|:---:|
    |Union|$L_1 \cup L_2 = \{w : w \in L_1 \lor w \in L_2\}$|
    |Intersacetion|$L_1 \cap L_2 = \{w : w \in L_1 \land w \in L_2\}$|
    |concatenation|$L_1 \cdot  L_2 = \{wz : w \in L_1 \land z \in L_2\}$|

- 형식 언어는 프로그래밍 언어에 응용된다.

- 수리논리학에서 형식 이론(formal theory)란 형식 언어의 sentence 집합이다.

- 형식 체계는 연역 규칙와 형식 언어로 구성된다. 형식 언어가 그것의 식(formula)을 식별할 수 있는데 반해, 형식 체계는 그것의 정리를 식별할 수 없다.

    다음 그림은 형식 체계의 문법적 구분을 보여준다. string 은 nonsense 와 잘 구성된 식으로 구분되며, 잘 구성된 식은 비정리와 정리로 구분된다.

    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Formal_languages.svg/450px-Formal_languages.svg.png)

- 형식 언어는 완벽하게 문법적이고, 의미를 배제하고 정의된다. 그러나 진리값에 의한 해석이 형식 언어의 식에 부여될 수 있다. 형식 언어의 해석을 연구하는 분야를 [formal semantic](https://en.wikipedia.org/wiki/Semantics_of_logic) 이라고 한다.

    모델 이론에서는 식의 용어가 수학적 구조의 객체로 해석되고 그것의 진리값을 결정하는 결정 절차가 용어의 진리값을 결정한다. 식(formula) 에 대한 **모델(model) 이란 식을 참으로 만드는 용어에 대한 해석** 을 뜻한다.

!!! def ""

    sentence : 자유변수가 없는 술어 논리의 Boolean-valued 식이다.

- 술어논리는 1차 논리 등을 뜻한다.

- 예시 

    1차 논리의 $\forall y \exists x (x ^{2} = y)$ 는 sentence 이다. 자유변수란 양화사가 가해지지 않은 변수이므로 이 명제에 자유변수는 없다. 이 명제의 논의 영역이 $\R ^{+}$ 라면 참이고, $\R$ 이면 거짓이며, $\mathbb{C}$ 이면 참이다.

    반면 $\exists x(x ^{2} = y)$ 는 sentence 가 아니다.

!!! def ""

    이론(theory) : 형식 언어의 sentence 집합이다.

- 이론 $T$ 의 원소 $\phi \in T$ 를 정리(theorem)라고 한다.

- 대부분의 경우 연역 체계에는 $\Sigma \subset T$ 인 $T$ 의 공리 집합이 존재한다. 이 경우 연역 체계를 공리적 체계라고 한다. 정의에 의하여 공리는 정리가 된다. 

- 1차 이론이란 추론 규칙을 공리에 재귀적으로 적용하여 얻어진 1차 논리의 sentence 집합이다.

- 이론을 구성하는 첫단계는 명제로 구성된 비어있지 않은 개념적 클래스 $\mathcal{E }$ 를 정의하는 것이다. 이 초기 명제들을 이론의 원시 원소(primitive elements) 혹은 기본 명제라고 한다. 

    이론 $\mathcal{T}$ 는 이러한 기본 명제들로 구성된 개념적 클래스이다. $\mathcal{T}$ 의 기본 명제를 $\mathcal{T}$ 의 기본 정리(elementary theorem) 이라고 하고 진리값 참을 부여한다. 이로써 이론이란 $\mathcal{E }$ 에 참인 명제를 부여하는 것으로 볼 수 있다.

    그래서 한 이론에서 명제가 참일 수도 있고, 다른 이론에서 동일한 명제가 거짓이 될 수도 있다.

- $\mathcal{S}$ 가 $\mathcal{T}$ 의 부분이론이라는 것은 $\mathcal{S} \subset \mathcal{T}$ 라는 것이다. 반면 $\mathcal{T} \subset \mathcal{S}$ 이라면 $\mathcal{S}$ 를 $\mathcal{T}$ 의 확장 또는 초이론(supertheory)이라고 한다.

- 연역적 이론(deductive theory)이란 이론의 내용이 형식적 연역 체계에 기반을 두고 있고, 기본 명제들 중 몇몇이 공리로 채택된 이론이다. 이로써 연역적 이론에서는 모든 sentence 가 공리의 논리적 귀결이 된다.

https://en.wikipedia.org/wiki/Structure_(mathematical_logic)

!!! def ""

    모델 이론(model theory) : 형식 이론과 그것의 모델의 관계에 대한 연구 분야이다. 

- 이때 말하는 모델이란 그 이론의 sentence 들을 참이 되게 하는 해석을 뜻한다.

!!! def ""

    구조(structure) : 논의영역 $A$, 부호수 $\sigma$, 해석 함수 $I$ 에 대하여 

    $$ \mathcal{A} = (A, \sigma , I) $$

    이다.

- 해석 함수 $I$ 는 부호수가 논의영역에서 어떻게 해석될지 정한다. 

- 보편대수학과 모델 이론에서 구조란 유한 항수와 관계가 정의된 집합이다.

- 보편 대수학에서 연구하는 구조란 군, 환, 체, 벡터 공간 같은 대수구조를 일반화시킨 것이다. 보편대수학이라는 기호는 관계기호가 없는 구조에 사용된다.

- 모델 이론의 관점에서 구조는 1차 논리에서의 의미를 정의하는데 사용된다. 모델 이론에서 구조가 해당 이론의 공리를 만족하면 구조를 모델(model) 이라고 부른다. 논리학자들은 구조를 해석이라고도 부른다.

- 논의영역은 임의의 집합이다. 보편대수학에서는 carrier 라고도 부르고 모델 이론에서는 universe 라고도 부른다. 1차 논리에서는 논의영역이 공집합이 되는 것을 허용하지 않는다. 구조 $\mathcal{A}$ 의 논의 영역을 $\text{dom}(\mathcal{A})$ 로 표현한다.

    가끔 구조 $\mathcal{A}$ 의 논의 영역을 $\mathcal{A}$ 로 표현할 때도 있다.

- 해석 함수 $I$ 는 함수과 관계에 부호수의 기호를 할당한다. 항수 $n$ 인 함수기호 $f$ 를 항수 $n$ 함수로 $f ^{\mathcal{A}} = I(f)$ 와 같이 사상시킨다. 마찬가지로 관계 기호 $R$ 을 관계 $R$ 로 $R ^{\mathcal{A}} = I(R) \subseteq A ^{\text{ar}(R)}$ 와 같이 사상시킨다. 

- 예시 

    체의 표준부호수 $\sigma _{f}$ 는 두 이항 함수 기호 $+, \times$ 으로 구정된다. 이 부호수에 대한 구조는 두 이항함수가 정의된 집합으로 구성된다. 하지만 이때의 구조가 체의 공리를 만족해야 할 필요는 없다. $\mathbb{Q} , \mathbb{R} , \mathbb{C}$ 같은 체들은 부호수 $\sigma$ 에 대한 구조 $\sigma$-structure 

    $$ \mathcal{Q} = (\mathbb{Q} , \sigma _f, I _{\mathbb{Q} }) $$

    $$ \mathcal{R} = (\mathbb{R} , \sigma _f, I _{\mathbb{R} }) $$

    $$ \mathcal{C} = (\mathbb{C} , \sigma _f, I _{\mathbb{C} }) $$

    로 여겨진다. 이 구조의 부호수는 

    $$ S_f = \{+, \times , -, 0, 1\} $$

    $$ \text{ar}_f(+) = \text{ar}_f(\times ) = 2, \enspace \text{ar}_f(-)=1, \enspace \text{ar}_f(0)=\text{ar}_f(1) = 0 $$

    에 대하여

    $$ \sigma _f = (S_f, \text{ar}_f) $$

    이다. 해석함수는 다음과 같으며

    $$ I _{\mathcal{Q}}(+): \mathbb{Q} \times \mathbb{Q} \to \mathbb{Q} $$

    $$ I _{\mathcal{Q}}(\times ): \mathbb{Q} \times \mathbb{Q} \to \mathbb{Q} $$

    $$ I _{\mathcal{Q}}(- ): \mathbb{Q} \times \mathbb{Q} \to \mathbb{Q} $$

    $$ I _{\mathcal{Q}}(0 ) \in  \mathbb{Q}, I _{\mathcal{Q}}(1 ) \in  \mathbb{Q} $$

    각각 덧셈, 곱셈, 뺄셈, 유리수 $0$, 유리수 $1$ 로 정의된다. 해석함수 $I _{\mathcal{R}}, I _{\mathcal{C}}$ 도 비슷하게 정의된다.

    이때 체가 아닌 정수 집합 $\mathbb{Z}$ 은 환인데, 마찬가지로 $\sigma _f$-structure 로 비슷하게 정의된다. 마찬가지로 $\sigma _f$-structure 가 체의 공리를 만족해야 할 필요는 없다. 

    순서체의 부호수는 추가적으로 $< , \leq$ 와 같은 이항 관계가 추가된다. 따라서 이 부호수는 대수적 부호수가 아니다.

    집합론의 부호수는 오직 이항 관계 $\in$ 만을 갖는다. 이 부호수의 구조는 집합의 원소와 이 원소들의 관계 $\in$ 에 대한 해석으로 구성된다.

- 구조가 반드시 1차 논리에서 정의되는 것은 아니다. 1차 논리에서 정의된 구조를 모델(model) 이라고 한다. 1차 논리 구조 $\mathcal{M}$ 은 만족 관계(satisfaction relation) $\mathcal{M} \vDash \phi$ 를 갖는데, 이 만족 관계는 language 의 모든 식 $\phi$ 와 language 의 구조 $\mathcal{M}$ 에서 정의된다. 이 관계는 Tarski 의 T-schema 에 의하여 귀납적으로 정의된다.

    language 의 구조 $\mathcal{M}$ 이 language 의 이론 $T$ 와 같으며, $\mathcal{M}$ 이 모든 $T$ 의 sentence 를 만족하면 구조 $\mathcal{M}$ 을 이론 $T$ 의 모델이라고 한다.

    - 예시 

        환은 환 공리를 만족하는 환의 language 의 구조이다. 그리고 ZFC 의 모델은 ZFC 공리를 만족하는 집합론의 language 의 구조이다.

# 완전성 정리 

!!! def ""

    완전성 정리(Godel's completeness theorem) : 

- 1차 논리에서 의미적인 참과 문법적인 증명가능성 사이의 대응을 설립하는 근본 정리이다.

- 완전성 정리는 모든 1차 이론에 적용된다.

# 2차 논리

!!! note

    완전성 정리를 살펴보려 했는데 모델이론의 모델이라는 개념 같이 대수학, 추상대수학, 보편대수학, 모델이론 등에 대한 지식이 있어야 이해가 수월한 이야기들이 많아서 지금 살펴보는 것은 비효율적인 것 같았다. 나중에 기반지식이 좀 쌓였을 때 증명이론, 계산이론, 튜링 머신의 위키에서의 엄밀한 정의 같은 것들을 살펴보는 것이 더 효율적인듯.