
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

!!! tldr ""

    형식 체계(formal system) : 공리로부터 추론규칙을 통해 정리를 이끌어낼 수 있는 논리적 체계이다.

- 그러한 추론 규칙을 형식체계의 명제논리(logical calculus) 라고 한다.

- 힐베르트가 수학의 기초를 형식체계로 건설하자고 제안했다. 형식 체계는 추상적 생각의 체계를 잘 다듬은 것이다.

- 형식체계는 공리로부터 유한한 형식 언어를 구성하기 위하여 유한개의 원시 기호(primitive symbol) 를 사용한다. 좀 더 구체적으로 형식체계는 다음과 같이 구성된다. 

    1. 유한개의 원시 기호를 택한다.

    2. 원시 기호로 형식문을 구성할 문법을 택한다. 어떤 형식문이 잘 구성되었다(well-formed)고 하는 것은 원시 기호에 구성 문법을 가하여 그 형식문을 얻을 수 있다는 것이다.

    3. 잘 구성된 형식문인 공리를 택한다.

    4. 추론 규칙을 택한다. 공리로부터 추론(증명)되는 잘 구성된 형식문을 정리(theorem) 이라고 한다. 

- 어떤 형식체계가 recursive 하다는 것은 그 공리들과 추론규칙들이 결정 가능한 집합(decidable sets, recursive set), 혹은 semidecidable sets 이라는 것이다.

- 어떤 형식체계가 다른 형식체계를 포함하거나 서로 동형일 수 있다. 이 경우 포함된 형식체계의 무모순성이 다른 형식체계에 의하여 상대적으로 증명가능하다.

- 연역 체계란 공리와 추론규칙으로 구성되어 정리를 이끌어낼 수 있는 체계이다. 연역 체계의 한 예시로 1차 논리를 들 수 있다.

- 논리 체계 혹은 language 란 비논리적 공리와 문법이 있는 (보통 1차 논리를 사용하는) 연역 체계이다. 모델 이론의 해석(interpretation) 에 의하여 논리 체계의 문법은 어떤 잘 구성된 형식문이 주어진 구조(structure) 를 만족하는지 확인해준다.

    이때 형식 체계의 공리를 모두 만족하는 구조(structure) 를 논리 체계의 모델(model) 이라고 한다.

    - 어떤 논리 체계가 건전하다(sound)는 것은 공리로 연역된 모든 형식문이 논리 체계의 모든 모델(model) 을 만족한다는 것이다. 즉 건전성(soundness)은 증명가능한 명제(정리)가 의미론 상으로도 참이된다는 성질이다. 
    
        역으로 논리 체계가 완전하다(complete) 는 것은 모든 모델을 만족하는 명제가 공리로 연역될 수 있다(증명될 수 있다)는 것이다. 즉, 건전성은 완전성과 역관계이다.

        그러나 괴델의 불완전성 정리로 산술을 표현할만큼 강력한 모든 형식체계는 건전하면서 완전하지 못하다. 왜냐하면 참이면서 증명할 수 없는 명제가 반드시 존재하기 때문이다. 

!!! tldr ""

    공리 체계(axiomatic system) : 명제논리로 공리로부터 정리를 이끌어낼 수 있는 임의의 공리 집합이다.

- 무모순(consistent)적인 어떤 이론(theory)은 공리체계를 포함하며 그것들로부터 도출된 정리들을 포함한다.

- 공리체계는 형식체계의 특수자이다. 즉, 공리체계의 일반화가 형식체계이다.

- 형식적 이론이란 공리체계(주로 모델 이론model theory 으로 형식화된)로 설명되는 형식문의 집합이다. 이렇게 공리체계에서 도출된 이론에 포함된 정리들은 형식적 증명이라고 한다.

- 공리체계가 무모순(consistent)이라는 것은 모순을 포함하지 않는다는 것이다. 즉, 공리체계로부터 어떤 형식문과 그 부정문이 도출되지 않는다는 것이다.

    무모순은 모든 공리체계에 있어야 하는 필수적인 속성인데, 왜냐하면 모순이 존재하면 폭발 원리(principle of explosion) 에 의하여 모든 형식문이 증명되기 때문이다.

- 공리가 다른 공리로부터 도출될 수 없다면 독립성이 있다고 한다. 그러나 무모순성이 공리체계에 반드시 있어야 하는 조건인 것과 달리 독립성은 반드시 있어야 하는 조건은 아니다.

- 공리체계가 완전하다(complete)는 것은 모든 형식문이 공리로부터 도출된다는 것이다. 즉, 그 공리체계로 표현가능한 모든 형식문이 참이든 거짓으로든 증명 가능하다는 것이다.

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

    - 모든 무모순적인 명제가 공리적 방법으로 설명될 수 있는 것은 아니다. 어떤 프로그램이 주어진 명제가 정리인지 확인할 수 있다면 그 공리체계를 재귀 집합(recursive, 계산 가능한) 이라고 한다. 그러나 괴델의 불완전성 정리에 의하여 무모순적이지만 재귀 집합에 속하지 않은 명제가 있다는 것이 밝혀졌다. 즉, 컴퓨터는 어떤 증명이 올바른지 확인할 수 있지만, 어떤 형식문의 증명이 존재한다는 것을 밝힐 수 있다는 보장은 해줄 수 없다. 

        그러나 상위 체계 혹은 또 다른 체계에 해당 형식문의 증명이 존재하는 경우가 있다. 

        가령 어떤 산술에서의 형식문을 산술의 공리로 표현할 수 있지만, 그것에 대한 증명이 위상수학이나 복소해석학의 공리체계에 의존하게 될 수도 있다. 즉, 산술의 형식문이라 할지라도 그것의 증명을 페아노 공리체계(Peano axioms)에서 찾을 수 있다는 보장은 없다. 

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

    - 부정 $\lnot P$, 그리고 $P \land Q$, Material conditional $P \to  Q$, IFF $P \iff Q$

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

    명제논리는 다음 조건을 만족하는 형식체계 $\mathcal{L} = \mathcal{L}(\Alpha , \Omega , \Zeta, \Iota)$ 이다.
