
# 명제논리 

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

!!! tldr ""

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

!!! tldr ""

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

!!! tldr ""

    명제논리(Propositional logic, zeroth-order logic) : 명제들에 적용하여 새로운 명제를 도출할 수 있는 추론규칙이다. 

- 1차 논리와는 달리 명제 논리는 비논리적 대상, 그것에 대한 술어(속성, 조건), 한정사($\exists , \forall$)를 다루지 않는다. 그러나 명제논리는 1차 논리와 고차 논리의 기반이 된다.

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
    
!!! tldr ""

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

!!! tldr ""

    극대 집합(Maximal Set) : 어떤 조건을 만족하는 가장 큰 집합이다.

!!! tldr ""

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

!!! tldr ""

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

