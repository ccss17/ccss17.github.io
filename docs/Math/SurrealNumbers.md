!!! info "ref"

    https://www.tondering.dk/download/sur16.pdf

# 초현실수 개론

!!! tldr "초현실수의 정의"

    초현실수(surreal number) : 초현실수 집합 $L, R$ 에 대하여 
    
    $$ \forall l \in L, \forall r \in R : r \not \leq l \tag{1.1} $$

    을 만족하는 집합 $\{L|R\}$ 이다.

- $L$ 과 $R$ 을 각각 초현실수를 구성하는 left set, right set 이라고 한다. 

- $(1.1)$ 에 의하여 초현실수를 구성하는 집합쌍을 $L$ 과 $R$ 이라고 할 때 $R$ 의 어떤 원소도 $L$ 의 원소보다 작거나 같지 않다. 

- It provide virtually all of the capabilities of ordinary real numbers.

- Conway used surreal numbers to describe various aspects of game theory.

- 초현실수 집합 $L, R$ 이 $(1.1)$ 을 만족하면 새로운 초현실수 $\{L|R\}$ 을 구성할 수 있다. 이제 $(1.1)$ 이 well-formed 된 집합 쌍을 특정짓는다고 하자. 그러면 오직 well-formed 된 집합 쌍만이 초현실수를 구성한다고 할 수 있다.

- 초현실수는 실수를 비롯하여 

!!! tldr "최초의 초현실수"

    $$ 0 \equiv \{|\} $$

- 최초의 초현실수를 구성하기 위하여 $L, R$ 을 공집합 $\varnothing$ 으로 두면 최초의 초현실수는 $\{\varnothing | \varnothing \}$ 이 된다. 이때 이 초현실수의 $\varnothing$ 을 관례상 생략하여 더욱 편하게

    $$ \{ | \} $$

    라고 표기한다. 

- 이 초현실수를 구성하는 집합 쌍은 well-formed 이다. 왜냐하면 두 집합 쌍이 모두 공집합이므로 조건 $(1.1)$ 을 위배하는 원소가 존재하지 않기 때문이다. 

- 우리는 $\{|\}$ 을 영이라고 부르기로 하고 앞으로 이 초현실수를 기호 $0$ 로 표기하기로 한다. 

    $$ 0 \equiv \{|\} \tag{1.2} $$

- 기호 $\equiv$ 을 두 대상이 동등하다는 것을 나타낼 때 사용하자. $0$ 은 단지 $\{|\}$ 의 축약이다. $\equiv$ 는 $=$ 와 같지 않다. 우리는 아직 초현실수의 $=$ 를 정의하지 않았다. 

- 이제 우리는 집합 $\varnothing$ 과 $\{0\}$ 을 기반으로 $\{\{0\} | \varnothing \} ,\{\varnothing  | \{0\}\} ,\{\{0\} | \{0\} \}$ 와 같은 새로운 집합쌍을 생성할 수 있다.

    이때 $L = \{0\}, R = \varnothing$ 으로 구성된 집합쌍 $\{L | R\} = \{\{0\} | \varnothing \}$ 를 편의상 $\{0|\}$ 으로 표기한다. 그러므로 결국에 새로운 세 가지 집합쌍을 

    $$ \{0|\}, \{|0\}, \{0|0\} $$

    으로 표기한다. 이때 처음 두 집합쌍은 초현실수가 되지만 마지막 집합쌍은 $0 \leq 0$ 이므로 초현실수가 될 수 없다. 그 대신 $\{0|0\}$ 같은 집합쌍을 거짓수(pseudo number) 라고 부른다. 

!!! tldr "초현실수의 비교"

    초현실수 $x, y$ 와 $x$ 의 left set 인 $X_L$ 과 $y$ 의 right set 인 $Y_R$ 에 대하여 

    $$ x \leq y \iff  \lnot \exists x_L \in X_L : y \leq x_L \land \lnot \exists y_R \in Y_R : y_R \leq x \tag{1.4} $$

    이다.

- 즉, $x \leq y$ 라는 것은 $y$ 가 $x$ 의 left set 의 원소보다 작거나 같지 않고, $y$ 의 right set 이 $x$ 보다 작거나 같지 않다는 것이다.

- 다르게 말하면 

    $$ \forall x_L \in X_L : x_L < y \land \forall y_R \in Y_R : x < y_R $$

    이라고도 할 수 있을듯.

!!! tldr ""

    $$ \{|\} \leq \{|\} \tag{1.3} $$

- 증명 

    [초현실수의 비교의 정의]()에 의하여

    $$ \lnot \exists x_L \in \varnothing : \{|\} \leq x_L \tag{1.5} $$

    와 

    $$ \lnot \exists y_R \in \varnothing : y_R \leq \{|\} \tag{1.6} $$

    를 증명하면 증명이 끝난다. 그런데 이 두 명제는 공집합 위에서 선언되었으므로 조건을 만족시킬 원소가 존재하지 않는다. 그러므로 $\leq$ 의 뜻을 모르더라도 $(1.5)$ 와 $(1.6)$ 이 거짓이 되지 않는다는 것을 알 수 있다. 그러므로 

    $$ \therefore \{|\} \leq \{|\} $$

    이다. ■ 

- 일반적으로 초현실수는 자기 자신에 대하여 작거나 같다.

!!! tldr ""

    $$ 0 \leq 0 $$

- 증명 

    $$ \because  \{|\} \leq \{|\} $$

!!! tldr ""

    $$ \{|\} \leq \{0|\} $$

- 증명 

    [초현실수의 비교의 정의]()에 의하여 

    $$ \lnot \exists x_L \in \varnothing : \{0 | \} \leq x_L $$

    과 

    $$ \lnot \exists y_R \in \varnothing : y_R \leq \{|\} $$

    이 참이라면 증명이 끝난다. 그런데 이는 자명한 사실이다. 왜냐하면 공집합은 이 조건을 위배시킬 원소를 갖지 않기 때문이다. ■ 

!!! note

    "공집합이 조건을 위배시키는 원소를 갖지 않는다" 라고 말할 수도 있지만 "공집합이 조건을 만족시키는 원소를 갖지 않는다" 라고 말할 수도 있다. 왜 이론을 전개하기 유리한 방향으로 전자를 채택했을까? 

    가정이 성립하지 않으니까 Vacuous Truth 로써 참이라고 결론 내린거구나.

!!! tldr ""

    $$ \{0|\} \not \leq \{|\} \tag{1.10}  $$

- 증명

    $$ \exists x_L \in \{0\} : \{|\} \leq x_L \tag{1.11} $$

    또는 

    $$ \exists y_R \in \varnothing : y_R \leq \{0|\} $$

    이 참이면 증명이 끝난다. $(1.11)$ 은 $(1.3)$ 에 의하여 $\{|\}\leq 0$ 이므로 참이다. ■ 

!!! tldr ""

    $$ \{0|\} \leq \{0|\} \tag{1.13} $$

- 증명 

    $$ \lnot \exists x_L \in \{0\} : \{0|\} \leq x_L \tag{1.14} $$

    과 

    $$ \lnot \exists y_R \in \varnothing : y_R \leq \{0|\} \tag{1.15} $$

    가 참이면 증명이 끝난다. $(1.15)$ 는 Vacuous Truth 이다. $(1.14)$ 는 $(1.10)$ 에서 $\{0|\}\not \leq 0$ 이므로 참이다. ■ 

!!! tldr ""

    $$ x \leq y \iff y \geq x $$

- 기호 $\geq$ 는 "보다 크거나 같다" 는 뜻이다. 

!!! tldr "$<$ 의 정의"

    $$ x \leq y \land y \not \leq x \iff x < y $$

- 기호 $<$ 는 "보다 작다" 는 뜻이다. 

- 예시 

    $$ 0 < \{0|\} $$

    $$ \{|0\} < 0 $$

    $$ \{|0\} < \{0|\} $$

!!! tldr "서로 같은 초현실수의 정의"

    $$ x \leq y \land y \leq x \iff x = y $$

- 기호 $=$ 는 "같다" 는 뜻이다. 같지 않다를 뜻하는 $\neq$ 는 

    $$ x \not \leq y \lor y \not \leq x \iff x \neq y $$

    이다. 

- 예시 

    $$ 0 = 0 $$

    $$ \{|0\} = \{|0\} $$

!!! tldr ""

    $$ 1 \equiv \{0|\} $$

    $$ -1 \equiv \{|0\} $$

- 이제 $0 \equiv \{|\}$ 이외에 또 다른 축약기호를 만든다. 그것이 $1$ 과 $-1$ 이다. 

- 예시 

    $$ 0 < 1 $$

    $$ 1 = 1 $$

    $$ -1 < 0 $$

    $$ -1 = -1 $$

    $$ -1 < 1 $$

- 이렇게 우리는 세 가지 초현실수 $-1, 0, 1$ 을 생성해내었다. 이것을 기반으로 새로운 60 가지 집합쌍을 만들 수 있고 이 중 아래와 같은 17 가지 집합쌍이 well-formed 된 초현실수가 된다.

    $$ \{-1|\}, \{|-1\} $$

    $$ \{1|\}, \{|1\} $$

    $$ \{-1, 0|\}, \{-1|0\}, \{|-1, 0\} $$

    $$ \{0, 1|\}, \{0|1\}, \{|0, 1\} $$

    $$ \{-1, 1|\}, \{-1|1\}, \{|-1, 1\} $$

    $$ \{-1, 0, 1|\}, \{-1, 0|1\}, \{-1|0, 1\}, \{|-1,0,1\} $$

!!! tldr ""

    $$ 2 \equiv \{1|\} $$

    $$ -2 \equiv \{|-1\} $$

- 다음을 증명하는 것은 매우 쉽다.

    $$ 1 < \{1|\} $$

    $$ \{|-1\} < -1 $$

    이 수를 각각 $2, -2$ 로 정의한다. 

!!! tldr ""

    $$ \dfrac{1}{2} \equiv \{0|1\} $$

    $$ -\dfrac{1}{2} \equiv \{-1|0\} $$

- 다음을 쉽게 증명할 수 있다. 

    $$ 0 < \{0|1\} < 1 $$

    $$ -1 < \{-1|0\} < 0 $$

    그러므로 이 수를 각각 $\dfrac{1}{2}, -\dfrac{1}{2}$ 로 정의한다. 

- 이 초현실수가 왜 $\dfrac{1}{3}$ 이나 $\dfrac{14}{17}$ 이 아닌 $\dfrac{1}{2}$ 로 정의될까? 그 이유는 아래에서 알게 될텐데 스포를 하자면 $\{0|1\}+\{0|1\}=1$ 로 정의되기 때문이다. 

!!! tldr ""

    $$ \{-1|1\} = \{|\} $$

- 증명 

    $$ \lnot \exists x_L \in \{-1\} : \{|\} \leq x_L \tag{1.38} $$

    과 

    $$ \lnot \exists y_R \in \varnothing : y_R \leq \{-1|1\} \tag{1.39} $$

    이 참임을 증명하자. $0 \not \leq -1$ 이고 $(1.39)$ 는 Vacuous Truth 이다. ▲ 

    같은 방식으로 

    $$ \{|\} \leq \{-1|1\} $$ 

    임을 쉽게 증명할 수 있다. ▲ 

    그러므로 증명이 끝났다. ■ 

- 이때 $\equiv$ 가 아닌 $=$ 기호를 사용했다는 것을 주목하자. $\{-1|1\}$ 과 $\{|\}$ 의 구성요소는 전혀 다르다. 그러므로 이 둘은 동등하지 않다($\not \equiv$). 하지만 이 둘은 $0$ 이라는 같은 값을 가진다($=$). 

    $$ \{-1|1\} \not \equiv \{|\} \land \{-1|1\} = \{|\} $$

    그러므로 우리는 $\{|\}$ 과 $\{-1|1\}$ 이 $0$ 을 다른 방식으로 표현함을 알 수 있다. 

    - 같은 방식으로 우리는 다음을 증명할 수 있다. 

        $$ 0 = \{-1|\} = \{|1\} $$

        $$ 1 = \{-1,0|\} $$

        $$ -2 = \{|-1,0\} = \{|-1, 1\} = \{|-1,0,1\} $$

        $$ 2 = \{0,1|\} = \{-1,1|\} = \{-1,0,1|\} $$

        $$ -1 = \{|0,1\} $$

        $$ \dfrac{1}{2} = \{-1,0|1\} $$

        $$ -\dfrac{1}{2} = \{-1|0,1\} $$

        그러므로 이것들은 우리에게 새로운 값의 초현실수를 생성해주지 못한다.
    
    - 위 초현실수의 패턴을 포착했다면 초현실수의 값을 유추할 때 left set 의 가장 높은 값과 right set 의 가장 낮은 값만을 고려하면 된다는 것을 알 수 있을 것이다. 이 사실 또한 곧이어 증명할 것이다. 

- 이제 우리는 초현실수 $-2, -1, -\dfrac{1}{2}, 0, \dfrac{1}{2}, 1, 2$ 를 알게 되었다. 그러므로 이 초현실수를 바탕으로 아래와 같은 또 다른 초현실수를 생성할 수 있다.

    $$ -3 \equiv \{|-2\} $$

    $$ -1 \dfrac{1}{2} \equiv \{-2|-1\} $$

    $$ -\dfrac{3}{4} \equiv \{-1|-\dfrac{1}{2}\} $$

    $$ -\dfrac{1}{4} \equiv \{-\dfrac{1}{2}|0\} $$
    
    $$ \dfrac{1}{4} \equiv  \{0|\dfrac{1}{2}\} $$

    $$ \dfrac{3}{4} \equiv \{\dfrac{1}{2}|1\} $$

    $$ 1 \dfrac{1}{2} \equiv \{1|2\} $$

    $$ 3 \equiv \{2|\} $$

    또 이를 기반으로 기존의 초현실수의 다른 표현을 발견할 수 있다. 

    $$ \{-2, \dfrac{1}{2} | 2\} = 1, \quad \{-2|1\} = 0 $$

!!! tldr ""

    birthday of a surreal number : 초현실수의 생성순서관계를 나타내기 위한 개념이다.

- 우리는 최초로 초현실수 $0$ 을 생성했다. 그러므로 $0$ 이 day zero 에 태어났다고 할 수 있다. 

    그리고 $0$ 을 기반으로 $-1,1$ 을 생성했다. 그러므로 이 둘은 day one 에 태어났다고 할 수 있다. 

    이후에 $-1,0,1$ 을 기반으로 $-2,-\dfrac{1}{2}, \dfrac{1}{2},2$ 를 생성했으므로 이들은 day two 에 태어났다고 할 수 있다. 

# 초현실수의 성질

여기서부터 초현실수를 나타내기 위하여 소문자를 사용하고, 초현실수 집합을 나타내기 위하여 대문자를 사용한다. 또한 초현실수 $x$ 의 left set 을 나타내기 위하여 $X_L$ 를, right set 을 위하여 $X_R$ 을 사용한다.

!!! tldr ""

    초현실수 집합 $A, B$ 와 초현실수 $c$ 에 대하여 다음과 같이 정의한다.

    $$ A \leq c \iff \forall a \in A : a \leq c $$

    $$ c \leq A \iff \forall a \in A : c \leq a $$

    $$ A \leq B \iff \forall a \in A \enspace \forall b \in B : a \leq b $$

- 이 정의에 의하여 임의의 초현실수 $b$ 에 대하여 

    $$ \varnothing \leq b, \varnothing \not \leq b, \varnothing > b, \dots $$

    등등이 모든 부등식 관계기호에 대하여 성립한다.

- 예시 

    $$ \{1,3,5\} < \{6,7\} $$

    $$ \{3,5,6\} \not < 1 $$

- 이때 $\lnot (A \leq b) \not \equiv A \not \leq b$ 인 것에 주의하자. 

    - 예시 

        $\{3,5\} \leq 4$ 은 거짓인 반면 $\{3,5\} \not \leq 4$ 도 거짓이다. 
    
!!! tldr "서로 같은 초현실수 집합의 정의"

    초현실수 집합 $A, B$ 에 대하여 다음과 같이 정의한다.

    $$ A = B \iff \forall a \in A \enspace  \exists b \in B : a = b \land \forall b \in B \exists a \in A : a = b $$

- $A=B$ 란 결국 두 집합의 원소가 서로 같다는 것이다. 

- 예시 

    $\{|\} = \{-1|1\}$ 이고 $\{1|\} = \{-1,0,1|\}$ 이므로 다음이 성립한다. 

    $$ \{\{|\}, \{1|\}\} = \{\{-1|1\}, \{|\}, \{-1,0,1|\}\} $$

- 또한 이제부터 공집합은 생략하고 집합을 콤마로 구분하자. 가령 left set 이 $\{a,b\} \cup C \cup D$ 이고 right set 이 $\varnothing$ 이면 

    $$ \{\{a,b\}\cup C \cup D|\varnothing \} $$

    이라고 쓰는 것이 아니라

    $$ \{a,b,C,D|\} $$

    라고 편하게 쓰도록 한다. 

- 지금까지 정의한 표기 규칙에 의하여 well-formedness 조건 $(1.1)$ 을 다음과 같이 더욱 간략하게 나타낼 수 있다.

    $x$ 가 초현실수라면 

    $$ X_R \not \leq X_L. \tag{2.1} $$

    초현실수의 비교를 정의하는 $(1.4)$ 도 다음과 같이 나타낼 수 있다.

    $$ x \leq y \iff y \not \leq X_L \land Y_R \not \leq x $$

!!! tldr "$\equiv$ 의 정의"

    $$ \begin{equation}\begin{split} x \equiv y \iff &\forall x_L \in X_L : x_L \in Y_L \quad \land \\ &\forall x_R \in X_R : x_R \in Y_R \quad \land \\ &\forall y_L \in Y_L : y_L \in X_L \quad \land \\ &\forall y_R \in Y_R : y_R \in X_R \end{split}\end{equation} \tag*{} $$

- 우리는 지금까지 $\equiv$ 이 단지 초현실수의 동등함을 나타낸다고 비형식적으로 정의했지만 이제 이것을 형식적으로 정의할 때가 되었다. 

!!! tldr ""

    parents : 초현실수의 left set 과 rigth set 의 원소들이다. 

- Conway 는 parents 대신 option 이라는 용어를 사용했다. 

- 초현실수의 정의는 재귀적으로 선언되어 모든 초현실수가 기존에 생성된 초현실수를 기반으로 생성됨을 말해준다.

    이는 모든 초현실수가 원시 초현실수인 $\{|\}$ 에 도달할 때까지 그들의 parents 를 역추적해나갈 수 있다는 것을 말해준다. 

!!! tldr "정리 증명 도구"

    정리의 증명을 위하여 다음을 사용할 것이다.

    1. $\{|\}$ 에 대하여 정리가 참이다.

    2. 초현실수 $x$ 의 parents 에 대하여 정리가 참이면 $x$ 에 대하여 정리가 참이다.

- 2) 를 사용하여 수학적 귀납법을 전개할 수 있다. 즉, $\varnothing$ 에 대하여 참임을 증명한 다음, 정리가 parents 에 대하여 참임을 가정하고 parents 로 구성된 초현실수에 대하여 참임을 증명하면 모든 초현실수에 대하여 정리가 참임을 증명할 수 있다. 

!!! tldr "$\not \leq$ 의 정의"

    $$ x \not \leq y \iff \exists x_L \in X_L : y \leq x_L \lor \exists y_R \in Y_R : y_R \leq x \tag{2.5} $$

- 증명

    $$ \because  x \leq y \iff  \lnot \exists x_L \in X_L : y \leq x_L \land \lnot \exists y_R \in Y_R : y_R \leq x \tag{2.4} $$

    이는 $(1.4)$ 를 다시 가져온 것이다.

!!! tldr "정리 1"

    $x$ 가 초현실수이면 $x \leq x$ 이다.

- 증명 

    먼저 $0 \leq 0$ 은 [$(1.3)$]() 에 의하여 이미 증명되었다. ▲ 
    
    이 정리가 $x$ 의 parents 에 대하여 참이라고 하자. 즉, $X_L \cup X_R$ 의 모든 원소에 대하여 참이라고 가정하는 것이다. 

    우선 $(2.4)$ 에 의하여 $x \leq x$ 는 다음과 동치이다. 

    $$ \lnot \exists x_L \in X_L : x \leq x_L \land \lnot \exists x_R \in X_R : x_R \leq x \tag{2.6} $$

    $(2.6)$ 의 왼쪽 명제는 $\forall x_L \in X_L : x \not \leq x_L$ 과 같다. 그러면 [$\not \leq$ 의 정의]() 에 의하여 이는 

    $$ \forall x_L \in X_L : ( \exists a \in X_L : x_L \leq a \lor \exists b \in X _{LR} : b \leq x) \tag{2.7} $$

    와 같다. 그런데 우리는 $x$ 의 parents 에 대하여 이 정리가 성립한다고 가정했다. 그러므로 $x_L \leq x_L$ 이다. 

    그러면 $X_L$ 의 원소 $x_L$ 에 대하여 $a \equiv x_L$ 로 두면 왼쪽 명제가 참이 된다. $a$ 를 당연히 $x_L$ 로 둘 수 있는데 $a$ 는 $X_L$ 의 원소이기 때문이다. 그러므로 $X_L$ 의 원소 $x_L$ 이 정해질 때마다 $a \equiv x_L$ 로 두면 왼쪽 명제가 참이 되는 것이다. 그러므로 $(2.7)$ 명제 전체가 참이 된다. 이것으로 $(2.6)$ 의 왼쪽 명제를 증명하였다. ▲ 

    이제 $(2.6)$ 의 오른쪽 명제를 증명할 차례이다. $(2.6)$ 의 오른쪽 명제는 $\forall x_R \in X_R : x_R \not \leq x$ 와 같다. [$\not \leq$ 의 정의]() 에 의하여 이는 

    $$ \forall x_R \in X_R : (\exists c \in X _{RL} : x \leq c \lor \exists d \in X_R : d \leq x_R) \tag{2.8} $$

    가 된다. $x$ 의 parents 에 대하여 이 정리가 참이므로 $x_R \leq x_R$ 이고 $d \equiv x_R$ 로 두면 $(2.8)$ 이 참이된다. 이로써 $(2.6)$ 의 오른쪽 명제가 증명되었다. ▲ 

    그러므로 $(2.6)$ 은 참이고, 모든 증명이 끝났다. ■ 

- 우리는 지금까지 이 정리를 초현실수가 well-formed 라는 가정 없이 증명했다는 것을 유의하라. 이 사실은 나중에 유용하게 사용된다.
    
!!! tldr "따름정리 2"

    $x$ 가 초현실수이면 $x = x$ 이다. 

- 증명 

    이 정리는 [서로 같은 초현실수의 정의]()에 의하여 곧바로 도출된다. ■ 

!!! tldr "정리 3"

    초현실수 집합 $A,A',B,B'$ 에 대하여

    $$ \forall a \in A \exists a' \in A' : a \leq a' \land \forall b' \in B' \exists b \in B : b \leq b' $$

    이면 

    $$ \{A|B\} \leq \{A'|B'\} \tag{2.9} $$

    이다. 

- 증명 

    $(2.9)$ 를 증명하려면 $(2.4)$ 에 의하여 

    $$ \lnot \exists a \in A : \{A'|B'\} \leq a \land \lnot \exists b' \in B' : b' \leq \{A|B\} \tag{2.10} $$

    을 증명하면 증명이 끝난다. ▲ 

    $\exists a \in A : \{A'|B'\} \leq a$ 라고 가정하면 또 다시 $(2.4)$ 에 의하여 

    $$ \lnot \exists a' \in A' : a \leq a' \land \lnot \exists a_R \in A_R : a_R \leq \{A'|B'\} \tag{2.11} $$

    이다. 그러므로 $(2.11)$ 의 왼쪽 명제는 결국 항상 $a' < a$ 이라고 말하는 것이다. 그런데 이는 가정의 왼쪽 명제와 모순된다. 그러므로 $(2.11)$ 은 모순이고 $(2.10)$ 의 왼쪽 명제는 참이다. ▲ 

    $\exists b' \in B' : b' \leq \{A|B\}$ 라고 가정하면 $(2.4)$ 에 의하여 

    $$ \lnot \exists b'_l \in B'_L : \{A|B\} \leq b'_L \land \lnot \exists b \in B:b \leq b' \tag{2.12} $$

    이다. $(2.12)$ 의 오른쪽 명제는 결국 항상 $b' < b$ 이라고 말하는 것이다. 하지만 이는 가정의 오른쪽 명제와 모순된다. 그러므로 $(2.12)$ 는 모순이고 $(2.10)$ 의 오른쪽 명제는 참이다. ▲ 

    그러므로 $(2.10)$ 는 참이고 모든 증명이 끝났다. ■ 

    - 이 증명도 $\{A|B\}$ 가 well-formed 된 초현실수라는 가정이 없네. 이러면 전체 이론이 불안정해지지 않을까? 왜 strict 한 가정 없이 이론을 전개하는거지. 

!!! tldr "정리 4"

    $$ A = A' \land B = B' \implies \{A|B\} = \{A'|B'\} $$

- 증명

    [서로 같은 초현실수 집합의 정의]() 에 의하여 $A = A'$ 는

    $$ \forall a \in A \exists a' \in A' : a = a' \land \forall a' \in A' \exists a \in A : a = a' $$

    을 뜻하고, [서로 같은 초현실수의 정의]() 에 의하여 $a = a'$ 는

    $$ a \leq a' \land a' \leq a $$

    을 뜻한다. 그러므로 우리는 

    $$ \forall a \in A \exists a' \in A' : a \leq a' \tag{2.14} $$

    $$ \forall a \in A \exists a' \in A' : a' \leq a \tag{2.15} $$

    $$ \forall a' \in A' \exists a \in A : a \leq a' \tag{2.16} $$

    $$ \forall a' \in A' \exists a \in A : a' \leq a \tag{2.17} $$

    을 얻는다. ▲ 

    같은 방식으로 $B = B'$ 로부터 

    $$ \forall b \in B \exists b' \in B' : b \leq b' \tag{2.18} $$

    $$ \forall b \in B \exists b' \in B' : b' \leq b \tag{2.19} $$

    $$ \forall b' \in B' \exists b \in B : b \leq b' \tag{2.20} $$

    $$ \forall b' \in B' \exists b \in A : b' \leq b \tag{2.21} $$

    을 얻는다. ▲ 

    $(2.14)$ 와 $(2.20)$ 과 [정리 3]() 에 의하여 

    $$ \{A|B\} \leq \{A'|B'\} \tag{2.22} $$

    를 얻고, $(2.17)$ 과 $(2.19)$ 와 [정리 3]() 에 의하여 

    $$ \{A'|B'\} \leq \{A|B\} \tag{2.23} $$

    을 얻는다. ▲ 

    그러므로 

    $$ \therefore \{A|B\} = \{A'|B'\} $$

    이다. ■ 

- 우리가 정리 3 과 정리 4 를 초현실수가 well-formed 라는 가정 없이 증명했다는 것에 유의하라.

!!! tldr "정리 5"

    초현실수는 그것의 left set 보다 크고, 그것의 right set 보다 작다. 즉, 

    $$ \begin{equation}\begin{split}   \forall a \in A : a < \{A|B\}&  \\ \forall b \in B : \{A|B\} < b &  \\ \end{split}\end{equation}\tag{2.24} $$

    이다. 집합 부등식으로 표현하면 

    $$ A < \{A|B\} \land \{A|B\} < B \tag{2.25} $$

    이다.

- 증명 

    $(2.24)$ 의 첫번째 명제를 증명하기 위하여 [$<$ 의 정의]() 에 따라 

    $$ \forall a \in A : a \leq \{A|B\} \tag{2.26} $$

    $$ \forall a \in A : \{A|B\}  \not \leq a \tag{2.27} $$

    를 증명해야 한다. ▲ 

    $(2.26)$ 을 귀납법으로 증명해보자(*$A_L \cup A_R$ 에 대하여 참임을 가정하고 $A$ 에 대하여 참이라는 것을 보이는 것이다*). $A= \varnothing$ 일 경우 자명하게 참이다. $(2.26)$ 은 [초현실수의 비교]() 에 의하여 

    $$ \lnot \exists a_L \in A_L : \{A|B\} \leq a_L \land \lnot \exists b \in B : b \leq a \tag{2.28} $$

    이다. 그런데 $(2.28)$ 의 오른쪽 명제는 $\{A|B\}$ 가 well-formed 이므로 참이다. ▲ 
    
    $(2.28)$ 의 왼쪽 명제는 

    $$ \forall a_L \in A_L : \{A|B\} \not \leq a_L \tag{2.29} $$

    와 같고, [$\not \leq$ 의 정의]() 에 의하여 

    $$ \forall a_L \in A_L : (\exists a' \in A : a_L \leq a' \lor \exists a _{LR} \in A _{LR} : a _{LR} \leq \{A|B\}) \tag{2.30} $$

    이다. $a' \equiv a$ 로 둔다면(*최초로 결정된 $A$ 의 원소 $a$ 에 대하여 $a'$ 을 $a$ 과 같게 설정한다는 말인 것 같다. 그리고 이는 충분히 가능한 일이긴하지.*) $(2.30)$ 의 왼쪽 명제를 

    $$ \forall a_L \in A_L : a_L \leq a \tag{2.31} $$

    로 바꿀 수 있는데, 이 명제의 형태는 이것들의 left set parents 에 의하여 변수가 치환된 것을 제외하고 $(2.26)$ 과 완전히 동일하다. 그런데 우리는 $A_L \cup A_R$ 에 대하여 $(2.26)$ 이 성립함을 가정했다. 그러므로 $(2.26)$ 의 [논의 영역]() $A$ 를 $A_L$ 로 치환한 $(2.31)$ 은 참이다. 그러므로 (*$(2.30)$ 도 참이고.. $(2.28)$ 도 참이니까..*) 결국 $(2.26)$ 의 증명이 끝났다. ▲ 

    $(2.27)$ 은 [$\not \leq$ 의 정의]() 에 의하여 $A$ 의 모든 $a$ 에 대하여 

    $$ \exists a' \in A : a \leq a' \lor \exists a_R \in A_R : a_R \leq \{A|B\} \tag{2.32} $$

    이 참임을 증명하면 증명된다. 이것의 왼쪽 명제에서 $a' \equiv a$ 로 설정할 수 있는데, 이렇게 하면 $a \leq a$ 가 되어 [정리 1]() 에 의하여 참이 된다. ▲ 

    이로써 $(2.24)$ 의 첫번째 명제가 증명되었는데, 두번째 명제도 비슷한 방식으로 증명할 수 있다. ■ 

!!! tldr "정리 6"

    The transitive law : 초현실수 $x,y,z$ 에 대하여

    $$ x \leq y \land y \leq z \implies x \leq z $$

    이다.

- 증명

    이 정리가 거짓이라고 하면 

    $$ x \leq y \land y \leq z \land x \not \leq z \tag{2.33} $$

    을 만족하는 초현실수 $x,y,z$ 가 존재한다. 이제 Boolean function $p(x,y,z)$ 를 다음과 같이 정의하자. 

    $$ p(x,y,z) \iff x \leq y \land y \leq z \land x \not \leq z \tag{2.34} $$

    $(2.33)$ 은 [초현실수의 비교]() 와 [$\not \leq$ 의 정의]() 에 의하여 

    $$ \lnot \exists x_L \in X_L : y \leq x_L \tag{2.35} $$

    $$ \lnot \exists y_R \in Y_R : y_R \leq x \tag{2.36} $$

    $$ \lnot \exists y_L \in Y_L : z \leq y_L \tag{2.37} $$

    $$ \lnot \exists z_R \in Z_R : z_R \leq y \tag{2.38} $$

    $$ \exists x_L \in X_L : z \leq x_L \lor \exists z_R \in Z_R : z_R \leq x \tag{2.39} $$

    이 참이면 참이 된다. ▲ 

    먼저 $(2.39)$ 의 왼쪽 명제가 참이라고 하자. $(2.35)$ 는 

    $$ \forall x_L \in X_L : y \not \leq x_L \tag{2.40} $$

    과 동치이다. 이때 $(2.40)$ 의 $x_L$ 을 $(2.39)$ 의 왼쪽 명제의 $x_L$ 과 동일하게 잡으면 이 명제들을 $(2.33)$ 의 $y \leq z$ 와 결합하여 

    $$ y \leq z \land z \leq x_L \land y \not \leq x_L \tag{2.41} $$

    을 얻을 수 있는데, 이는 

    $$ p(y, z, x_L) $$

    과 동치이다. ▲ 

    $(2.39)$ 의 오른쪽 명제가 참이라고 하자. $(2.38)$ 은

    $$ \forall z_R \in Z_R : z_R \not \leq y \tag{2.42} $$

    와 동치이다. 이때 $(2.42)$ 의 $z_R$ 을 $(2.39)$ 의 오른쪽 명제의 $z_R$ 과 동일하게 잡으면 이 명제들을 $(2.33)$ 의 $x \leq y$ 와 결합하여 

    $$ z_R \leq x \land x \leq y \land z_R \not \leq y \tag{2.43} $$

    을 얻을 수 있는데, 이는 

    $$ p(z_R, x, y) $$

    과 동치이다. ▲ 

    그러므로 

    $$ p(x, y, z) \implies \exists x_L \in X_L : p(y, z, x_L) \lor \exists z_R \in Z_R : p(z_R, x, y) \tag{2.44} $$

    이다. $x_L, z_R$ 은 각각 $x, z$ 의 parents 이므로 우리는 $x, z$ 의 parents 를 거슬러 올라가다보면 최초의 초현실수 $\{|\}$ 에 도달하게 된다. 그러나 $\{|\}$ 의 parents 는 존재하지 않으므로 $(2.44)$ 가 거짓이 된다. 이는 최초의 가정인 $(2.33)$ 도 거짓임을 말해주고, 결국 이 정리가 참이라는 것을 알 수 있다. ■ 

- 이 정리도 초현실수가 well-formed 라는 가정없이 증명되었다. 

!!! tldr "정리 7"

    $$ x \not \leq y \implies y \leq x $$

- 이 정리는 모든 초현실수가 $\leq$ 관계로 연결 되어있음을 말해준다. 

- 증명 

    $x \not \leq y$ 은 [\not \leq 의 정의]() 에 의하여 

    $$ \exists x_L \in X_L : y \leq x_L \tag{2.45} $$

    $$ \exists y_R \in Y_R : y_R \leq x \tag{2.46} $$

    중 하나 이상이 반드시 참임을 주장하는 것이다. ▲ 

    $(2.45)$ 가 참이라고 하면 $y \leq x_L$ 을 만족하는 $x_L$ 을 잡을 수 있다. 또한 $(2.26)$ 에 의하여 $x_L \leq x$ 이므로 [The transitive law]() 에 의하여 $y \leq x$ 을 얻는다. ▲ 

    $(2.46)$ 가 참이라고 하면 $y_R \leq x$ 을 만족하는 $y_R$ 을 잡을 수 있다. 또한 [정리 5]() 에 의하여 $y \leq y_R$ 이므로 [The transitive law]() 에 의하여 $y \leq x$ 을 얻는다. ■ 
    
!!! tldr "단순화된 $<$ 의 정의"

    $$ x < y \iff y \not \leq x \tag{2.48} $$

- 증명

    [정리 7]() 에 의하여 [$<$ 의 정의]() 

    $$ x \leq y \land y \not \leq x \iff x < y \tag{2.47} $$

    에서 $y \not \leq x$ 가 $x \leq y$ 를 함의하므로 

    $$ y \not \leq x \iff x < y  $$

    로 단순화시켜도 무방하다. ■  

!!! tldr "정리 8"

    $$ x<y \land y<z \implies x<z $$

- 증명

    이 정리가 거짓이면 

    $$ x < y \land y < z \land x \not < z \tag{2.49} $$

    가 참이고, 이것과 동치 명제인 

    $$ y \not \leq x \land z \not \leq y \land z \leq x \tag{2.50} $$

    도 참이다. [정리 6]() 의 대우 명제는 임의의 초현실수 $b$ 에 대하여 

    $$ a \not \leq c \implies a \not \leq b \lor b \not \leq c \tag{2.51} $$

    임을 주장한다. $a \equiv y, b \equiv z, c \equiv x$ 라고 두고 $(2.51)$ 을 $(2.50)$ 의 $y \not \leq x$ 에 적용하면 

    $$ (y \not \leq z \lor z \not \leq x) \land z \not \leq y \land z \leq x \tag{2.52} $$

    를 얻는다. 그러나 이 명제는 참거짓이 서로 상반되는 두 명제를 동시에 주장하므로 모순이다. 그러므로 이 정리는 참이다. ■ 

!!! tldr "정리 9"

    초현실수 $x$ 에 대하여 $x$ 의 값을 보존하면서

    $$ \exists x_L \in X_L : x_L < \xi $$
    
    을 만족하는 임의의 left set 원소 $\xi$ 를 제거할 수 있고,

    $$ \exists x_R \in X_R : \eta < x_R $$
    
    을 만족하는 임의의 right set 원소 $\eta$ 를 제거할 수 있다. 

- 이 정리는 초현실수를 단순화시킬 수 있는 방법을 말해준다.

- 예시 

    $$ \{1,2,3|4,5,6\} = \{1,3|4,6\} = \{3|4\} $$

- 증명 

    이 정리의 첫번째 반쪽을 증명해보자. 초현실수 $x$ 에 대하여 

    $$ x = \{x_1, x_2, \dots | X_R\} $$

    이라고 하고 $x_1 < x_2$ 라고 하자. 증명해야 할 것은 $\{x_1,x_2, \dots|X_R\}=\{x_2, \dots|X_R\}$ 이다. ▲ 

    [$=$ 의 정의]() 에 의하여 

    $$ \{x_1,x_2, \dots|X_R\} \leq \{x_2, \dots|X_R\} \land \{x_1,x_2, \dots|X_R\} \geq \{x_2, \dots|X_R\} $$

    을 증명해야 한다. 그런데 이 두 부등식은 모두 [정리 3]() 으로부터 도출된다.(*$\dots$ 에 대한 언급이 너무 모호한 것 같은데, 왜 이 증명만 이렇게 허술할까? 좀 더 엄밀해야 할 것 같은데*) ▲ 

    나머지 반쪽도 비슷하게 증명가능하다. ■ 

!!! tldr "따름정리 10"

    $A$ 가 가장 큰 원소 $a _{\max}$ 를 가지면 

    $$ \{A|B\} = \{a _{\max} | B\} $$

    이다. $B$ 가 가장 작은 원소 $b _{\min}$ 을 가지면 

    $$ \{A|B\} = \{A | b _{\min}\} $$

    이다.

- 증명 

    [정리 9]() 로부터 바로 도출된다. ■ 