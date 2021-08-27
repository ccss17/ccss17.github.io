!!! info "ref"

    https://www.tondering.dk/download/sur16.pdf

# 초현실수

!!! def "초현실수(surreal number)"

    초현실수는 초현실수 집합 $L, R$ 에 대하여 
    
    $$ \forall l \in L, \forall r \in R : r \not \leq l \tag{1.1} $$

    을 만족하는 집합 $\{L|R\}$ 이다.

- $L$ 과 $R$ 을 각각 초현실수를 구성하는 left set, right set 이라고 한다. 

- $(1.1)$ 에 의하여 초현실수를 구성하는 집합쌍을 $L$ 과 $R$ 이라고 할 때 $R$ 의 어떤 원소도 $L$ 의 원소보다 작거나 같지 않다. 

- It provide virtually all of the capabilities of ordinary real numbers.

- Conway used surreal numbers to describe various aspects of game theory.

- 초현실수 집합 $L, R$ 이 $(1.1)$ 을 만족하면 새로운 초현실수 $\{L|R\}$ 을 구성할 수 있다. 이제 $(1.1)$ 이 well-formed 된 집합 쌍을 특정짓는다고 하자. 그러면 오직 well-formed 된 집합 쌍만이 초현실수를 구성한다고 할 수 있다.

- 초현실수는 쉽게 말해서 left set 과 right set 이 공집합이 아닐 경우 아래에서 살펴볼 [정리 5](#c076cc283) 에 의하여 left set 의 최댓값보다 크고 right set 의 최소값보다 작은 어떤 값이라고 생각해도 된다. 

- 초현실수는 모든 실수와 초실수의 무한대와 무한소까지 포함하도록 구성된 집합이 아닌 전순서 모임(totally ordered proper class) 이다. 

    von Neumann–Bernays–Gödel 집합론에서 생각할 경우 초현실수 모임 $\mathbf{No}$ 는 유리수 $\mathbb{Q}$, 실수 $\R$, 초실수 $^{*}\R$ 등등 모든 순서체를 부분 체로 포함한다. 

    물론 모든 초한서수도 초현실수에 포함된다. 

    즉, 초현실수는 모든 순서체를 포함할 수 있으므로 가장 큰 순서체(ordered field) 이다. 

- 초현실수는 특유의 구성방법과 연산으로 인하여 전혀 다른 새로운 수가 정의된다. 가령 무한대 $\omega$ 도 하나의 수로 다룰 수 있고, 무한소 $\epsilon$ 과 $\dfrac{\epsilon }{2}$ 도 정의할 수 있다. 

    ![](https://upload.wikimedia.org/wikipedia/commons/4/49/Surreal_number_tree.svg)

    초실수(hyperreal number) 도 무한대와 무한소를 하나의 수로 정의하지만 초현실수는 집합이 아닌 전순서 모임이다.

    또한 초실수에서는 $0$ 과 무한소 $\epsilon$ 사이에 수가 존재하지 않지만, 초현실수에서는 $\dfrac{\epsilon }{2}$ 등 수많은 다른 수가 존재한다. 

- 아래 그림은 수 체계의 관계를 나타낸다. 

    ![](https://www.researchgate.net/profile/Tee-Jay-Dack/publication/328107970/figure/fig1/AS:678473026793478@1538771983490/The-universe-of-non-complex-numbers.jpg)

## $0$ 의 정의

!!! def "최초의 초현실수"

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

    으로 표기한다. 이때 처음 두 집합쌍은 초현실수가 되지만 마지막 집합쌍은 $0 \leq 0$ 이므로 초현실수가 될 수 없다. 그 대신 $\{0|0\}$ 같은 집합쌍을 pseudo number  라고 부른다. 

## 초현실수의 순서관계

!!! def "$\leq$ "

    초현실수 $x, y$ 와 $x$ 의 left set 인 $X_L$ 과 $y$ 의 right set 인 $Y_R$ 에 대하여 

    $$ x \leq y \iff  \lnot \exists x_L \in X_L : y \leq x_L \land \lnot \exists y_R \in Y_R : y_R \leq x \tag{1.4} $$

    이다.

- 즉, $x \leq y$ 라는 것은 $y$ 가 $x$ 의 left set 의 원소보다 작거나 같지 않고, $y$ 의 right set 이 $x$ 보다 작거나 같지 않다는 것이다.

- 다르게 말하면 

    $$ \forall x_L \in X_L : x_L < y \land \forall y_R \in Y_R : x < y_R $$

    이라고도 할 수 있을듯.

!!! def ""

    $$ \{|\} \leq \{|\} \tag{1.3} $$

- 증명 

    [$\leq$ 의 정의](#6c5b5ea1c)에 의하여

    $$ \lnot \exists x_L \in \varnothing : \{|\} \leq x_L \tag{1.5} $$

    와 

    $$ \lnot \exists y_R \in \varnothing : y_R \leq \{|\} \tag{1.6} $$

    를 증명하면 증명이 끝난다. 그런데 이 두 명제는 공집합 위에서 선언되었으므로 조건을 만족시킬 원소가 존재하지 않는다. 그러므로 $\leq$ 의 뜻을 모르더라도 $(1.5)$ 와 $(1.6)$ 이 거짓이 되지 않는다는 것을 알 수 있다. 그러므로 

    $$ \therefore \{|\} \leq \{|\} $$

    이다. ■ 

- 일반적으로 초현실수는 자기 자신에 대하여 작거나 같다.

!!! def ""

    $$ 0 \leq 0 $$

- 증명 

    $$ \because  \{|\} \leq \{|\} $$

!!! def ""

    $$ \{|\} \leq \{0|\} $$

- 증명 

    [$\leq$ 의 정의](#6c5b5ea1c)에 의하여 

    $$ \lnot \exists x_L \in \varnothing : \{0 | \} \leq x_L $$

    과 

    $$ \lnot \exists y_R \in \varnothing : y_R \leq \{|\} $$

    이 참이라면 증명이 끝난다. 그런데 이는 자명한 사실이다. 왜냐하면 공집합은 이 조건을 위배시킬 원소를 갖지 않기 때문이다. ■ 

!!! note

    "공집합이 조건을 위배시키는 원소를 갖지 않는다" 라고 말할 수도 있지만 "공집합이 조건을 만족시키는 원소를 갖지 않는다" 라고 말할 수도 있다. 왜 이론을 전개하기 유리한 방향으로 전자를 채택했을까? 

    가정이 성립하지 않으니까 Vacuous Truth 로써 참이라고 결론 내린거구나.

!!! def ""

    $$ \{0|\} \not \leq \{|\} \tag{1.10}  $$

- 증명

    $$ \exists x_L \in \{0\} : \{|\} \leq x_L \tag{1.11} $$

    또는 

    $$ \exists y_R \in \varnothing : y_R \leq \{0|\} $$

    이 참이면 증명이 끝난다. $(1.11)$ 은 [$(1.3)$](#ab60662a7) 에 의하여 $\{|\}\leq 0$ 이므로 참이다. ■ 

!!! def ""

    $$ \{0|\} \leq \{0|\} \tag{1.13} $$

- 증명 

    $$ \lnot \exists x_L \in \{0\} : \{0|\} \leq x_L \tag{1.14} $$

    과 

    $$ \lnot \exists y_R \in \varnothing : y_R \leq \{0|\} \tag{1.15} $$

    가 참이면 증명이 끝난다. $(1.15)$ 는 Vacuous Truth 이다. $(1.14)$ 는 $(1.10)$ 에서 $\{0|\}\not \leq 0$ 이므로 참이다. ■ 

!!! def ""

    $$ x \leq y \iff y \geq x $$

- 기호 $\geq$ 는 "보다 크거나 같다" 는 뜻이다. 

!!! def "$<$ "

    $$ x \leq y \land y \not \leq x \iff x < y $$

- 기호 $<$ 는 "보다 작다" 는 뜻이다. 

- 예시 

    $$ 0 < \{0|\} $$

    $$ \{|0\} < 0 $$

    $$ \{|0\} < \{0|\} $$

!!! def "서로 같은 초현실수"

    $$ x \leq y \land y \leq x \iff x = y $$

- 기호 $=$ 는 "같다" 는 뜻이다. 같지 않다를 뜻하는 $\neq$ 는 

    $$ x \not \leq y \lor y \not \leq x \iff x \neq y $$

    이다. 

- 예시 

    $$ 0 = 0 $$

    $$ \{|0\} = \{|0\} $$

!!! def ""

    $$ 1 \equiv \{0|\} $$

    $$ -1 \equiv \{|0\} $$

- 이제 $0 \equiv \{|\}$ 이외에 또 다른 축약기호를 만든다. 그것이 $1$ 과 $-1$ 이다. 

- 예시 

    $$ 0 < 1 $$

    $$ 1 = 1 $$

    $$ -1 < 0 $$

    $$ -1 = -1 $$

    $$ -1 < 1 $$

!!! def ""

    초현실수 생성법 : 기존에 존재하는 초현실수를 집합쌍 $\{L|R\}$ 의 $L$ 과 $R$ 의 자리에 대입하고, well-formed 인 집합쌍만을 추려내고, 기존의 초현실수와 값이 다른 초현실수를 가려낸다. 

- 기존에 존재하던 초현실수가 $x_1, x_2, \dots, x_n$ 라고 하자. 우선 이 초현실수가 left set $L$ 에 대입되는 경우의 수는 $2 ^{n}$ 이다. 마찬가지로 right set $R$ 에 대입되는 경우의 수도 $2 ^{n}$ 이다.

    이 방식으로 기존에 존재하던 초현실수 $n$ 개로 만들 수 있는 새로운 집합쌍은

    $$ 2 ^{n} \times 2 ^{n} = \boxed{2 ^{2n}} $$

    이다. 여기에서 well-formed 인 집합쌍만이 초현실수가 되고, 기존에 존재하던 초현실수와 다른 값을 가지는 초현실수들만이 새로 생성된 초현실수가 된다. 

- 우리는 지금까지 세 가지 초현실수 $-1, 0, 1$ 을 생성해내었다. 이것을 기반으로 새로운 $2 ^{2 \cdot 3} = 64$ 가지 집합쌍을 만들 수 있고 이 중 아래와 같은 $17$ 가지 집합쌍이 well-formed 된 초현실수가 된다.

    $$ \{-1|\}, \{|-1\} $$

    $$ \{1|\}, \{|1\} $$

    $$ \{-1, 0|\}, \{-1|0\}, \{|-1, 0\} $$

    $$ \{0, 1|\}, \{0|1\}, \{|0, 1\} $$

    $$ \{-1, 1|\}, \{-1|1\}, \{|-1, 1\} $$

    $$ \{-1, 0, 1|\}, \{-1, 0|1\}, \{-1|0, 1\}, \{|-1,0,1\} $$

!!! def ""

    $$ 2 \equiv \{1|\} $$

    $$ -2 \equiv \{|-1\} $$

- 다음을 증명하는 것은 매우 쉽다.

    $$ 1 < \{1|\} $$

    $$ \{|-1\} < -1 $$

    이 수를 각각 $2, -2$ 로 정의한다. 

!!! def ""

    $$ \dfrac{1}{2} \equiv \{0|1\} $$

    $$ -\dfrac{1}{2} \equiv \{-1|0\} $$

- 다음을 쉽게 증명할 수 있다. 

    $$ 0 < \{0|1\} < 1 $$

    $$ -1 < \{-1|0\} < 0 $$

    그러므로 이 수를 각각 $\dfrac{1}{2}, -\dfrac{1}{2}$ 로 정의한다. 

- 이 초현실수가 왜 $\dfrac{1}{3}$ 이나 $\dfrac{14}{17}$ 이 아닌 $\dfrac{1}{2}$ 로 정의될까? 그 이유는 아래에서 알게 될텐데 스포를 하자면 

    $$\{0|1\}+\{0|1\}=1$$ 
    
    로 정의되기 때문이다. 

!!! def ""

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

!!! def ""

    birthday of a surreal number : 초현실수의 생성순서관계를 나타내기 위한 개념이다.

- 우리는 최초로 초현실수 $0$ 을 생성했다. 그러므로 $0$ 이 day zero 에 태어났다고 할 수 있다. 

    그리고 $0$ 을 기반으로 $-1,1$ 을 생성했다. 그러므로 이 둘은 day one 에 태어났다고 할 수 있다. 

    이후에 $-1,0,1$ 을 기반으로 $-2,-\dfrac{1}{2}, \dfrac{1}{2},2$ 를 생성했으므로 이들은 day two 에 태어났다고 할 수 있다. 

## 음의 초현실수

!!! def "$-$ "

    $$ -x = \{-X_R | -X_L\} $$

- 초현실수의 음수를 이렇게 정의한다. 

## 초현실수의 성질

여기서부터 초현실수를 나타내기 위하여 소문자를 사용하고, 초현실수 집합을 나타내기 위하여 대문자를 사용한다. 또한 초현실수 $x$ 의 left set 을 나타내기 위하여 $X_L$ 를, right set 을 위하여 $X_R$ 을 사용한다.

!!! def "초현실수와 초현실수 집합의 비교"

    초현실수 집합 $A, B$ 와 초현실수 $c$ 에 대하여 다음과 같이 정의한다.

    $$ A \leq c \iff \forall a \in A : a \leq c $$

    $$ c \leq A \iff \forall a \in A : c \leq a $$

    $$ A \leq B \iff \forall a \in A \enspace \forall b \in B : a \leq b $$

- 이 정의에 의하여 임의의 초현실수 $b$ 에 대하여 

    $$ \varnothing \leq b, \varnothing \not \leq b, \varnothing > b, \dots $$

    등등이 Vacuous Truth 에 의하여 모든 부등식 관계기호에 대하여 참이 된다. 

- 예시 

    $$ \{1,3,5\} < \{6,7\} $$

    $$ \{3,5,6\} \not < 1 $$

- 이때 $\lnot (A \leq b) \not \equiv A \not \leq b$ 인 것에 주의하자. 

    - 예시 

        $\{3,5\} \leq 4$ 은 거짓인 반면 $\{3,5\} \not \leq 4$ 도 거짓이다. 
    
!!! def "서로 같은 초현실수 집합의 정의"

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

    [$\leq$ 의 정의](#6c5b5ea1c)를 정의하는 $(1.4)$ 도 다음과 같이 나타낼 수 있다.

    $$ x \leq y \iff y \not \leq X_L \land Y_R \not \leq x $$

!!! def "$\equiv$ "

    $$ \begin{equation}\begin{split} x \equiv y \iff &\forall x_L \in X_L : x_L \in Y_L \enspace \land \\ &\forall x_R \in X_R : x_R \in Y_R \enspace \land \\ &\forall y_L \in Y_L : y_L \in X_L \enspace \land \\ &\forall y_R \in Y_R : y_R \in X_R \end{split}\end{equation} \tag*{} $$

- 우리는 지금까지 $\equiv$ 이 단지 초현실수의 동등함을 나타낸다고 비형식적으로 정의했지만 이제 이것을 형식적으로 정의할 때가 되었다. 

!!! def ""

    parents : 초현실수의 left set 과 rigth set 의 원소들이다. 

- Conway 는 parents 대신 option 이라는 용어를 사용했다. 

- 초현실수의 정의는 재귀적으로 선언되어 모든 초현실수가 기존에 생성된 초현실수를 기반으로 생성됨을 말해준다.

    이는 모든 초현실수가 원시 초현실수인 $\{|\}$ 에 도달할 때까지 그들의 parents 를 역추적해나갈 수 있다는 것을 말해준다. 

!!! def "정리 증명 도구"

    정리의 증명을 위하여 다음을 사용할 것이다.

    1. $\{|\}$ 에 대하여 정리가 참이다.

    2. 초현실수 $x$ 의 parents 에 대하여 정리가 참이면 $x$ 에 대하여 정리가 참이다.

- 2) 를 사용하여 수학적 귀납법을 전개할 수 있다. 즉, $\varnothing$ 에 대하여 참임을 증명한 다음, 정리가 parents 에 대하여 참임을 가정하고 parents 로 구성된 초현실수에 대하여 참임을 증명하면 모든 초현실수에 대하여 정리가 참임을 증명할 수 있다. 

!!! def "$\not \leq$ "

    $$ x \not \leq y \iff \exists x_L \in X_L : y \leq x_L \lor \exists y_R \in Y_R : y_R \leq x \tag{2.5} $$

- 증명

    $$ \because  x \leq y \iff  \lnot \exists x_L \in X_L : y \leq x_L \land \lnot \exists y_R \in Y_R : y_R \leq x \tag{2.4} $$

    이는 $(1.4)$ 를 다시 가져온 것이다.

!!! def "정리 1"

    $x$ 가 초현실수이면 $x \leq x$ 이다.

- 증명 

    먼저 $0 \leq 0$ 은 [$(1.3)$](#ab60662a7) 에 의하여 이미 증명되었다. ▲ 
    
    이 정리가 $x$ 의 parents 에 대하여 참이라고 하자. 즉, $X_L \cup X_R$ 의 모든 원소에 대하여 참이라고 가정하는 것이다. 

    우선 $(2.4)$ 에 의하여 $x \leq x$ 는 다음과 동치이다. 

    $$ \lnot \exists x_L \in X_L : x \leq x_L \land \lnot \exists x_R \in X_R : x_R \leq x \tag{2.6} $$

    $(2.6)$ 의 왼쪽 명제는 $\forall x_L \in X_L : x \not \leq x_L$ 과 같다. 그러면 [$\not \leq$ 의 정의](#34f824094) 에 의하여 이는 

    $$ \forall x_L \in X_L : ( \exists a \in X_L : x_L \leq a \lor \exists b \in X _{LR} : b \leq x) \tag{2.7} $$

    와 같다. 그런데 우리는 $x$ 의 parents 에 대하여 이 정리가 성립한다고 가정했다. 그러므로 $x_L \leq x_L$ 이다. 

    그러면 $X_L$ 의 원소 $x_L$ 에 대하여 $a \equiv x_L$ 로 두면 왼쪽 명제가 참이 된다. $a$ 를 당연히 $x_L$ 로 둘 수 있는데 $a$ 는 $X_L$ 의 원소이기 때문이다. 그러므로 $X_L$ 의 원소 $x_L$ 이 정해질 때마다 $a \equiv x_L$ 로 두면 왼쪽 명제가 참이 되는 것이다. 그러므로 $(2.7)$ 명제 전체가 참이 된다. 이것으로 $(2.6)$ 의 왼쪽 명제를 증명하였다. ▲ 

    이제 $(2.6)$ 의 오른쪽 명제를 증명할 차례이다. $(2.6)$ 의 오른쪽 명제는 $\forall x_R \in X_R : x_R \not \leq x$ 와 같다. [$\not \leq$ 의 정의](#34f824094) 에 의하여 이는 

    $$ \forall x_R \in X_R : (\exists c \in X _{RL} : x \leq c \lor \exists d \in X_R : d \leq x_R) \tag{2.8} $$

    가 된다. $x$ 의 parents 에 대하여 이 정리가 참이므로 $x_R \leq x_R$ 이고 $d \equiv x_R$ 로 두면 $(2.8)$ 이 참이된다. 이로써 $(2.6)$ 의 오른쪽 명제가 증명되었다. ▲ 

    그러므로 $(2.6)$ 은 참이고, 모든 증명이 끝났다. ■ 

- 우리는 지금까지 이 정리를 초현실수가 well-formed 라는 가정 없이 증명했다는 것을 유의하라. 이 사실은 나중에 유용하게 사용된다.
    
!!! def "따름정리 2"

    $x$ 가 초현실수이면 $x = x$ 이다. 

- 증명 

    이 정리는 [서로 같은 초현실수의 정의](#9b1c5b42d)에 의하여 곧바로 도출된다. ■ 

!!! def "정리 3"

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

!!! def "정리 4"

    $$ A = A' \land B = B' \implies \{A|B\} = \{A'|B'\} $$

- 증명

    [서로 같은 초현실수 집합의 정의](#4922e884d) 에 의하여 $A = A'$ 는

    $$ \forall a \in A \exists a' \in A' : a = a' \land \forall a' \in A' \exists a \in A : a = a' $$

    을 뜻하고, [서로 같은 초현실수의 정의](#9b1c5b42d) 에 의하여 $a = a'$ 는

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

    $(2.14)$ 와 $(2.20)$ 과 [정리 3](#5587827c6) 에 의하여 

    $$ \{A|B\} \leq \{A'|B'\} \tag{2.22} $$

    를 얻고, $(2.17)$ 과 $(2.19)$ 와 [정리 3](#5587827c6) 에 의하여 

    $$ \{A'|B'\} \leq \{A|B\} \tag{2.23} $$

    을 얻는다. ▲ 

    그러므로 

    $$ \therefore \{A|B\} = \{A'|B'\} $$

    이다. ■ 

- 우리가 정리 3 과 정리 4 를 초현실수가 well-formed 라는 가정 없이 증명했다는 것에 유의하라.

!!! def "정리 5"

    초현실수는 그것의 left set 보다 크고, 그것의 right set 보다 작다. 즉, 

    $$ \begin{equation}\begin{split}   \forall a \in A : a < \{A|B\}&  \\ \forall b \in B : \{A|B\} < b &  \\ \end{split}\end{equation}\tag{2.24} $$

    이다. 집합 부등식으로 표현하면 

    $$ A < \{A|B\} \land \{A|B\} < B \tag{2.25} $$

    이다.

- 증명 

    $(2.24)$ 의 첫번째 명제를 증명하기 위하여 [$<$ 의 정의](#e9c1c7e5b) 에 따라 

    $$ \forall a \in A : a \leq \{A|B\} \tag{2.26} $$

    $$ \forall a \in A : \{A|B\}  \not \leq a \tag{2.27} $$

    를 증명해야 한다. ▲ 

    $(2.26)$ 을 귀납법으로 증명해보자(*$A_L \cup A_R$ 에 대하여 참임을 가정하고 $A$ 에 대하여 참이라는 것을 보이는 것이다*). $A= \varnothing$ 일 경우 자명하게 참이다. $(2.26)$ 은 [$\leq$ 의 정의](#6c5b5ea1c) 에 의하여 

    $$ \lnot \exists a_L \in A_L : \{A|B\} \leq a_L \land \lnot \exists b \in B : b \leq a \tag{2.28} $$

    이다. 그런데 $(2.28)$ 의 오른쪽 명제는 $\{A|B\}$ 가 well-formed 이므로 참이다. ▲ 
    
    $(2.28)$ 의 왼쪽 명제는 

    $$ \forall a_L \in A_L : \{A|B\} \not \leq a_L \tag{2.29} $$

    와 같고, [$\not \leq$ 의 정의](#34f824094) 에 의하여 

    $$ \forall a_L \in A_L : (\exists a' \in A : a_L \leq a' \lor \exists a _{LR} \in A _{LR} : a _{LR} \leq \{A|B\}) \tag{2.30} $$

    이다. $a' \equiv a$ 로 둔다면(*최초로 결정된 $A$ 의 원소 $a$ 에 대하여 $a'$ 을 $a$ 과 같게 설정한다는 말인 것 같다. 그리고 이는 충분히 가능한 일이긴하지.*) $(2.30)$ 의 왼쪽 명제를 

    $$ \forall a_L \in A_L : a_L \leq a \tag{2.31} $$

    로 바꿀 수 있는데, 이 명제의 형태는 이것들의 left set parents 에 의하여 변수가 치환된 것을 제외하고 $(2.26)$ 과 완전히 동일하다. 그런데 우리는 $A_L \cup A_R$ 에 대하여 $(2.26)$ 이 성립함을 가정했다. 그러므로 $(2.26)$ 의 [논의 영역](../Logic/FormalSystem/#5ad54ef60) $A$ 를 $A_L$ 로 치환한 $(2.31)$ 은 참이다. 그러므로 (*$(2.30)$ 도 참이고.. $(2.28)$ 도 참이니까..*) 결국 $(2.26)$ 의 증명이 끝났다. ▲ 

    $(2.27)$ 은 [$\not \leq$ 의 정의](#34f824094) 에 의하여 $A$ 의 모든 $a$ 에 대하여 

    $$ \exists a' \in A : a \leq a' \lor \exists a_R \in A_R : a_R \leq \{A|B\} \tag{2.32} $$

    이 참임을 증명하면 증명된다. 이것의 왼쪽 명제에서 $a' \equiv a$ 로 설정할 수 있는데, 이렇게 하면 $a \leq a$ 가 되어 [정리 1](#a65fcbfae) 에 의하여 참이 된다. ▲ 

    이로써 $(2.24)$ 의 첫번째 명제가 증명되었는데, 두번째 명제도 비슷한 방식으로 증명할 수 있다. ■ 

!!! def "정리 6"

    The transitive law : 초현실수 $x, y, z$ 에 대하여 

    $$ x \leq y \land y \leq z \implies x \leq z $$

    이다.

- 증명

    이 정리가 거짓이라고 하면 

    $$ x \leq y \land y \leq z \land x \not \leq z \tag{2.33} $$

    을 만족하는 초현실수 $x,y,z$ 가 존재한다. 이제 Boolean function $p(x,y,z)$ 를 다음과 같이 정의하자. 

    $$ p(x,y,z) \iff x \leq y \land y \leq z \land x \not \leq z \tag{2.34} $$

    $(2.33)$ 은 [$\leq$ 의 정의](#6c5b5ea1c) 와 [$\not \leq$ 의 정의](#34f824094) 에 의하여 

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

!!! def "정리 7"

    $$ x \not \leq y \implies y \leq x $$

- 이 정리는 모든 초현실수가 $\leq$ 관계로 연결 되어있음을 말해준다. 

- 증명 

    $x \not \leq y$ 은 [$\not \leq$ 의 정의](#34f824094) 에 의하여 

    $$ \exists x_L \in X_L : y \leq x_L \tag{2.45} $$

    $$ \exists y_R \in Y_R : y_R \leq x \tag{2.46} $$

    중 하나 이상이 반드시 참임을 주장하는 것이다. ▲ 

    $(2.45)$ 가 참이라고 하면 $y \leq x_L$ 을 만족하는 $x_L$ 을 잡을 수 있다. 또한 $(2.26)$ 에 의하여 $x_L \leq x$ 이므로 [The transitive law](#70892e5fd) 에 의하여 $y \leq x$ 을 얻는다. ▲ 

    $(2.46)$ 가 참이라고 하면 $y_R \leq x$ 을 만족하는 $y_R$ 을 잡을 수 있다. 또한 [정리 5](#c076cc283) 에 의하여 $y \leq y_R$ 이므로 [The transitive law](#70892e5fd) 에 의하여 $y \leq x$ 을 얻는다. ■ 
    
!!! def "단순화된 $<$ "

    $$ x < y \iff y \not \leq x \tag{2.48} $$

- 증명

    [정리 7](#630774eb4) 에 의하여 [$<$ 의 정의](#e9c1c7e5b) 

    $$ x \leq y \land y \not \leq x \iff x < y \tag{2.47} $$

    에서 $y \not \leq x$ 가 $x \leq y$ 를 함의하므로 

    $$ y \not \leq x \iff x < y  $$

    로 단순화시켜도 무방하다. ■  

!!! def "정리 8"

    $$ x<y \land y<z \implies x<z $$

- 증명

    이 정리가 거짓이면 

    $$ x < y \land y < z \land x \not < z \tag{2.49} $$

    가 참이고, 이것과 동치 명제인 

    $$ y \not \leq x \land z \not \leq y \land z \leq x \tag{2.50} $$

    도 참이다. [정리 6](#70892e5fd) 의 대우 명제는 임의의 초현실수 $b$ 에 대하여 

    $$ a \not \leq c \implies a \not \leq b \lor b \not \leq c \tag{2.51} $$

    임을 주장한다. $a \equiv y, b \equiv z, c \equiv x$ 라고 두고 $(2.51)$ 을 $(2.50)$ 의 $y \not \leq x$ 에 적용하면 

    $$ (y \not \leq z \lor z \not \leq x) \land z \not \leq y \land z \leq x \tag{2.52} $$

    를 얻는다. 그러나 이 명제는 참거짓이 서로 상반되는 두 명제를 동시에 주장하므로 모순이다. 그러므로 이 정리는 참이다. ■ 

!!! def "정리 9"

    초현실수 $x$ 에 대하여 $x$ 의 값을 보존하면서

    $$ \exists x_L \in X_L : \xi < x_L $$
    
    을 만족하는 임의의 left set 원소 $\xi$ 를 제거할 수 있고,

    $$ \exists x_R \in X_R : x_R < \eta $$
    
    을 만족하는 임의의 right set 원소 $\eta$ 를 제거할 수 있다. 

- 이 정리는 초현실수를 단순화시킬 수 있는 방법을 말해준다.

- 예시 

    $$ \{1,2,3|4,5,6\} = \{1,3|4,6\} = \{3|4\} $$

- 증명 

    이 정리의 첫번째 반쪽을 증명해보자. 초현실수 $x$ 에 대하여 

    $$ x = \{x_1, x_2, \dots | X_R\} $$

    이라고 하고 $x_1 < x_2$ 라고 하자. 증명해야 할 것은 $\{x_1,x_2, \dots|X_R\}=\{x_2, \dots|X_R\}$ 이다. ▲ 

    [$=$ 의 정의](#9b1c5b42d) 에 의하여 

    $$ \{x_1,x_2, \dots|X_R\} \leq \{x_2, \dots|X_R\} \land \{x_1,x_2, \dots|X_R\} \geq \{x_2, \dots|X_R\} $$

    을 증명해야 한다. 그런데 이 두 부등식은 모두 [정리 3](#5587827c6) 으로부터 도출된다. ▲ 

    나머지 반쪽도 비슷하게 증명가능하다. ■ 

!!! def "따름정리 10"

    $A$ 가 가장 큰 원소 $a _{\max}$ 를 가지면 

    $$ \{A|B\} = \{a _{\max} | B\} $$

    이다. $B$ 가 가장 작은 원소 $b _{\min}$ 을 가지면 

    $$ \{A|B\} = \{A | b _{\min}\} $$

    이다.

- 이 정리는 임의의 초현실수 $\{A|B\}$ 에 대하여 

    $$ \{A|B\} = \{a _{\max} | b _{\min}\} $$

    임을 말해준다.

- 이 정리에 의하여 초현실수의 정의를 바꾸어야 하지 않을까? 즉, 초현실수의 left set, right set 이 단 하나의 수만 포함하도록 정의를 수정할 수 있지 않느냐는 것이다. 

    하지만 그럴 수 없다. 이 정리는 초현실수의 left set, right set 이 가장 큰 원소와 가장 작은 원소를 가질 때만 유효하다. 

    만약 left set, right set 이 무한집합이면 가장 큰 원소, 가장 작은 원소가 존재하지 않는다.

- 증명 

    [정리 9](#7817bc62f) 로부터 바로 도출된다. ■ 

!!! def "정리 11"

    초현실수 $x$ 가 초현실수 집합 $A$ 의 모든 원소보다 크고, 초현실수 집합 $B$ 의 모든 원소보다 작으면 $x = \{X_L, A|X_R, B\}$ 이다. 즉, 

    $$ A < x < B \implies x = \{X_L, A | X_R, B\} \tag{2.53} $$

    이다.

- 예시 

    우리는 $-1 < 0 < 1$ 과 $0 = \{|\}$ 를 이미 증명했었는데 이 정리에 의하여 

    $$ 0 = \{-1 | 1\} $$

    이 된다. 이 사실 또한 이미 증명했었다.

- 증명 

    $x = \{X_L, A | X_R, B\}$ 를 증명하는 것은

    $$x \leq \{X_L, A | X_R, B\} \land \{X_L, A | X_R, B\} \leq x$$ 
    
    를 증명하는 것이다. 이는 [$\leq$ 의 정의](#6c5b5ea1c) 에 의하여 다음을 증명하는 것과 같다. 

    $$ \lnot \exists x_L \in X_L : \{X_L, A | X_R, B\} \leq x_L \tag{2.54} $$

    $$ \lnot \exists \beta  \in X_R \cup B : \beta \leq x \tag{2.55} $$

    $$ \lnot \exists \alpha \in X_L \cup A : x \leq \alpha \tag{2.56} $$

    $$ \lnot \exists x_R \in X_R : x_R \leq \{X_L,A|X_R,B\} \tag{2.57} $$

    $(2.54)$ 는 $\forall x_L \in X_L : x_L \leq \{X_L, A | X_R, B\}$ 와 같은데, [정리 5](#c076cc283) 에 의하여 $\{X_L, A | X_R, B\}$ 는 

    $$ \forall \gamma \in X_L \cup A : \gamma <\{X_L, A | X_R, B\} $$

    을 만족한다. 이는 $(2.54)$ 를 함의한다. ▲ 

    $(2.57)$ 는 $\forall x_R \in X_R : \{X_L, A | X_R, B\} \leq x_R$ 와 같은데, [정리 5](#c076cc283) 에 의하여 $\{X_L, A | X_R, B\}$ 는 

    $$ \forall \delta \in X_R \cup B : \{X_L, A | X_R, B\} < \delta $$

    을 만족한다. 이는 $(2.57)$ 를 함의한다. ▲ 

    $(2.55)$ 는 $\forall \beta \in X_R \cup B : x \leq \beta$ 와 같다.
    
    [정리 5](#c076cc283) 에 의하여 $\forall \beta \in X_R : x \leq \beta$ 는 자명하고, 
    
    $B$ 의 정의에 의하여 $\forall \beta \in B : x \leq \beta$ 도 자명하다. ▲ 

    $(2.56)$ 도 [정리 5](#c076cc283) 와 $A$ 의 정의에 의하여 자명하다. ■ 

!!! def "정리 12"

    day $m$ 에서 초현실수 

    $$ x_1 < x_2 < \dots < x_n $$

    이 존재했다면 day $m+1$ 에서 새로 생성된 초현실수는 

    $$ \{|x_1\}, \{x_1|x_2\}, \dots, \{x _{n-1} | x_n\}, \{x_n\} $$

    이다. 즉, day $m+1$ 에서의 초현실수는 

    $$ \{|x_1\} < x_1 < \{x_1|x_2\} < x_2 < \dots < \{x _{n-1} | x_n\} < x_n < \{x_n|\} \tag{2.58} $$

    이다.

- 최초의 초현실수 $0 = \{|\}$, 즉 day zero 에 태어난 초현실수 이후에 day one 에 태어난 초현실수는 

    $$ -1, 0, 1 $$

    이다. 이를 기반으로 day two 에 생성된 초현실수는 

    $$ -2, -1, - \dfrac{1}{2} , 0, \dfrac{1}{2}, 1, 2 $$

    이다. 이를 기반으로 day three 에 태어난 초현실수는

    $$ -3, -2, - \dfrac{3}{2}, -1, - \dfrac{3}{4}, - \dfrac{1}{2}, - \dfrac{1}{4}, 0 , \dfrac{1}{4}, \dfrac{1}{2}, \dfrac{3}{4}, 1, \dfrac{3}{2}, 2, 3 $$

    이다. 이로써 새로운 day 에 새로 생성되는 초현실수는 초현실수 리스트의 양끝과 초현실수들의 사이에 위치한다고 유추할 수 있다. 

    이것을 일반화하여 엄밀히 증명한 것이 이 정리이다. 

- 증명

    day $m+1$ 에 생성된 초현실수에 대하여 살펴보자. 

    1. $\{|x_1\}$ 와 $\{x_n|\}$ 는 day $m$ 에 존재하지 않았다. 

    2. $\{|x_j\}$ 에 대하여 $j>1$ 라면 이것은 day $m$ 에 존재했다. 

    3. $\{x_i|\}$ 에 대하여 $i<n$ 라면 이것은 day $m$ 에 존재했다. 

    4. $\{x_i|x_j\}$ 에 대하여 $i+1=j$ 라면 이것은 day $m$ 에 존재하지 않았다. 

    5. $\{x_i|x_j\}$ 에 대하여 $i+1 \neq j$ 라면 이것은 day $m$ 에 존재했다. ▲ 

    a) 의 증명:

    [정리 5](#c076cc283) 에 의하여 $\{|x_1\} < x_1$ 이고 $x_1$ 은 day $m$ 에서 가장 작은 초현실수이다. 그러므로 day $m+1$ 에서, 즉 [day $m$ 의 초현실수를 기반으로 생성할 수 있는 초현실 수](#3db1a67fe) 중 가장 작은 초현실수는 $\{|x_1\}$ 이다. 

    [정리 5](#c076cc283) 에 의하여 $x_n < \{x_n|\}$ 이고 $x_n$ 은 day $m$ 에서 가장 큰 초현실수이다. 그러므로 day $m+1$ 에서, 즉 [day $m$ 의 초현실수를 기반으로 생성할 수 있는 초현실 수](#3db1a67fe) 중 가장 큰 초현실수는 $\{x_n|\}$ 이다. ▲ 

    b) 의 증명:

    $x_k$ 를 $x_k \leq x _{j-1}$ 인 가장 오래된 초현실수라고 하자. 그렇다면 $x_k$ 보다 오래된 초현실수 $a$ 는 반드시 $a > x _{j-1}$ 이다. 그러므로 $x_k$ 의 parents 는 $x _{j-1}$ 보다 크다. 즉, 

    $$ x _{j-1} < {X_k}_R \tag{2.59} $$

    day $m$ 에서 $x _{j-1}$ 와 $x_j$ 사이에는 어떤 수도 존재하지 않으므로 ${X_k}_R \not < x_j$ 이고 결국 

    $$ x_j \leq {X_k}_R \tag{2.60} $$

    을 얻는다. [정리 5](#c076cc283) 에 의하여 

    $$ \{|x_j\} < x_j \tag{2.61} $$

    이므로 $(2.60)$ 과 $(2.61)$ 에 의하여 

    $$ \{|x_j\} < {X_k}_R \tag{2.62} $$

    를 얻는다. (*${X_k}_L < x_j$ 를 왜 증명하지 않고 정리 11 을 곧바로 적용하는걸까?*)

    c) 의 증명:

    b) 의 증명과 비슷하다. 

    d) 의 증명: 

    [정리 5](#c076cc283) 에 의하여 $x_i < \{x_i | x _{i+1}\} < x _{i+1}$ 인데 day $m$ 에서는 $x_i$ 와 $x _{i+1}$ 사이에 초현실수가 존재하지 않는다. 그러므로 $\{x_i|x _{i+1}\}$ 는 day $m+1$ 에 생성된 새로운 초현실수이다.

    e) 의 증명:

    $x_k$ 를 $x _{i+1} \leq x_k \leq x _{j-1}$ 를 만족하는 가장 오래된 초현실수라고 하자. 그러면 $x_k$ 의 parents 는 $x _{i+1}$ 보다 작거나 $x _{j-1}$ 보다 크다. 즉, 

    $$ {X_k}_{L} < x _{i+1} \land x _{j-1} \leq {X_k}_{R} \tag{2.65} $$

    이다. (*근데 이렇게 논의를 이어가려면 먼저 $x$ 보다 작은 초현실수 $y,z$ 로 이루어진 초현실수 $\{y,z\}$ 는 반드시 $x$ 보다 작다 라는 정리와 그 반대의 정리도 필요하잖아.*)

- 이 정리의 증명이 내 생각에는 약간 허술한 것 같다. 아무리 이해하려 해도 증명되지 않은 정리를 암묵적으로 사용하고 있는 것 같아서 이해되지 않는다. 이것을 이 이상 이해하려 하는 것은 비효율적인듯. 일단 넘어가는 게 효율적인듯하네. 

!!! def "따름정리 13"

    $x$ 가 $a$ 와 $b$ 사이에 있는 가장 오래된 초현실수이면 $\{a|b\} = x$ 이다. 

- 이 정리는 초현실수의 집합쌍이 어떤 값을 갖는지 알려준다. 

- 예시 

    우리는 $\{-1|1\} = 0$ 을 살펴보았는데 이는 $0$ 이 $-1$ 과 $1$ 사이에 있는 가장 오래된 초현실수라는 사실로부터도 도출된다. 

    비슷하게 이 정리를 통하여 $\bigg \{\dfrac{1}{4} | 2 \bigg \} = 1$ 과 $\bigg \{\dfrac{1}{4}|1 \bigg \} = \dfrac{1}{2}$ 같은 결론을 내릴 수 있다. 

!!! def "초현실수의 값"

    Dali function : $\R$ 을 $\mathbf{No}$ 로 보내는 다음과 같은 사상이다.

    $$ \delta (x) = \begin{cases} \{|\} & x = 0\\ \{\delta (x-1)|\} & x \in \mathbb{Z} ^{+} \\ \{|\delta (x+1)\} & x \in \mathbb{Z} ^{-} \\ \bigg \{\delta \bigg (\dfrac{j-1}{2^k}\bigg )\bigg |\delta \bigg (\dfrac{j+1}{2^k}\bigg )\bigg \} & x = \dfrac{j}{2^k} \text{ s.t. } j \in \mathbb{Z}, k \in \mathbb{Z} ^{+} \\ \end{cases} $$

- 이때 $\dfrac{j}{2^k}$ 는 기약분수(irreducible fraction)이다. 

- 지금까지 우리는 다양한 초현실수에 $0, 1, -\dfrac{1}{2}$ 같은 이름을 부여했다. 이제 초현실수에 어떤 수로 이름을 부여하는지 이 함수를 통하여 형식적으로 엄밀히 정의한다.

- 이 함수가 정의되었으니 $\{4|\}$ 를 쓰기 위하여 엄밀하게 $\{\delta (4)|\}$ 로 써야 하지만 편의상 전자의 방식을 고수한다. 

- 그러나 무리수를 초현실수로 보내는 경우가 Dali function 에서 정의되지 않았다. 이를 위해 이후에 Dali function 을 다시 다룰 것이다. 

!!! def ""

    Dali function 은 실수의 순서를 보존한다. 즉, 실수 $x,y$ 에 대하여 

    $$ x < y \iff \delta (x) < \delta (y) $$

    이라고 표현할 수 있다. 

- 즉, Dali function 으로 사상된 실수들의 순서는 초현실수의 순서와 같다.

- 증명

    [정리 5](#c076cc283) 와 Dali function 의 정의에 의하여 쉽게 증명된다. 

# 초현실수의 덧셈

!!! def "초현실수와 초현실수 집합의 덧셈"

    초현실수 $n$ 과 초현실수 집합 $S$ 에 대하여 

    $$ n+S = \{n + a : a \in S\} $$

    이다.

- $n-S$ 나 $S-n$ 도 동일한 방식으로 정의한다. $Sn$ 또한 동일하게 정의할 것이다. 

- 예시 

    $$ 6 + \{3,5,8\} = \{9,11,14\} $$

    $$ 6 - \{3,5,8\} = \{3,1,-2\} $$

    $$ \{3,5,8\} - 6 = \{-3,-1,2\} $$

    $$ 6 \times \{3,5,8\} = \{18,30,48\} $$

- 특히, 공집합에 대한 연산의 결과는 공집합으로 정의한다.

    - 예시 

        $$ n + \varnothing = \varnothing $$

        $$ n - \varnothing = \varnothing $$

        $$ n \varnothing = \varnothing $$

!!! def "초현실수 집합의 덧셈"

    초현실수 집합 $S, T$ 에 대하여 

    $$ S + T = \{s + t : s \in S, t \in T\} $$

    이다.

- 예시 

    $$ \{10,20\} + \{3,5,8\} = \{13,15,18,23,25,28\} $$

- 똑같은 집합이 집합 연산에 사용되면 다음과 같이 한다.(*이거 이해가 안되네*)

    - 예시 

        집합 $S = \{1,2\}, T = \{10, 20\}$ 에 대하여 

        $$ S + T + S = \{12,14,22,24\} $$

!!! def "초현실수의 덧셈"

    초현실수 $a, b$ 에 대하여

    $$ a + b = \begin{cases} \{A_L + b, a + B_L | A_R + b, a + B_R\}  & a \neq \varnothing \land  b \neq \varnothing \\ \varnothing  & a = \varnothing \lor b = \varnothing \\ \end{cases} $$

    이다. 

- 이제 초현실수의 덧셈이 well-formed 인 초현실수를 생성하는지 검증해야 하고, 덧셈의 정의가 make sense 한지 검증해야 한다. 

    그에 앞서 필요한 몇가지 정리들을 증명해보고, 덧셈의 well-formedness 와 make sense 를 검증해보자. 

- 예시 

    $1 + \dfrac{1}{2}$ 를 계산해보자. $1 \equiv \{0|\}, \dfrac{1}{2} \equiv \{0|1\}$ 이므로 먼저 

    $$ \begin{equation}\begin{split}   1 + \dfrac{1}{2} &=  \bigg \{0+\dfrac{1}{2}, 1 + 0 \bigg | \varnothing + \dfrac{1}{2}, 1 + 1\bigg \}\\ &= \bigg \{0 + \dfrac{1}{2} , 1 + 0 \bigg | 1 + 1\bigg \} \\ \end{split}\end{equation}\tag*{} $$

    이다. 
    
    $0 + \dfrac{1}{2}$ 를 계산해보자. $0 \equiv \{|\}$ 이므로 

    $$ \begin{equation}\begin{split}   0 + \dfrac{1}{2} &= \{\varnothing +\dfrac{1}{2}, 0 + 0 \bigg | \varnothing + \dfrac{1}{2}, 0 + 1\}  \\ &= \{0+0|0+1\} \\ \end{split}\end{equation}\tag*{} $$

    이다. 

    $0 + 0$ 을 계산해보자. 

    $$ \begin{equation}\begin{split}   0 + 0 &= \{\varnothing +0,0+\varnothing |\varnothing +0,0+\varnothing \} \\ &= \{|\} \\ &= 0 \\ \end{split}\end{equation}\tag*{} $$

    $0+1$ 을 계산해보자. 

    $$ \begin{equation}\begin{split}   0 + 1 &= \{\varnothing +1,0+0|\varnothing +1,0+\varnothing \}  \\ &= \{0|\} \\ &= 1 \\ \end{split}\end{equation}\tag*{} $$

    같은 방식으로 $1+0=1$ 임을 알 수 있다. 이로써 

    $$ \begin{equation}\begin{split}   0 + \dfrac{1}{2} &= \{0+0|0+1\}  \\ &= \{0|1\} \\ &= \dfrac{1}{2}\\ \end{split}\end{equation}\tag*{} $$

    라는 결론을 내릴 수 있다. 

    이제 $1+1$ 을 계산해보자. 

    $$ \begin{equation}\begin{split}   1 + 1 &= \{0+1,1+1|\varnothing +1,1+\varnothing \} \\ &= \{1|\} \\ &= 2 \\ \end{split}\end{equation}\tag*{} $$

    최종적으로 

    $$ \begin{equation}\begin{split}   1 + \dfrac{1}{2}&= \bigg \{0 + \dfrac{1}{2}, 1+0 \bigg |1+1\bigg \}  \\ &= \bigg \{\dfrac{1}{2}, 1 \bigg | 2\bigg \}\\ &= \{ 1 | 2\}\\ &= 1 \dfrac{1}{2} = \dfrac{3}{2} \\ \end{split}\end{equation}\tag*{} $$

    라는 것을 알 수 있다. 

!!! def ""

    초현실수 $a,b$ 에 대하여 

    $$ a+b = b+a $$

    이다.

- 증명

    $$ a + b = \{A_L + b, a + B_L | A_R + b, a + B_R\} = \{B_L + a, b + A_L | B_R + a, b + A_R\} = b + a $$

- 예시 

    $$ \begin{equation}\begin{split}   \dfrac{1}{2} + \dfrac{1}{2} &= \bigg \{0 + \dfrac{1}{2}, \dfrac{1}{2} + 0 \bigg | 1 + \dfrac{1}{2}, \dfrac{1}{2} + 1\bigg \}  \\ &= \bigg \{\dfrac{1}{2}\bigg |\dfrac{3}{2}\bigg \} \\ \end{split}\end{equation}\tag*{} $$

    - $\bigg \{\dfrac{1}{2}\bigg |\dfrac{3}{2}\bigg \}$ 의 값이 뭘까? [따름정리 13](#c9737ce31) 에 따르면 $\dfrac{1}{2}$ 과 $\dfrac{3}{2}$ 사이에 있는 가장 오래된 초현실수인 $1$ 이 그 값이 된다.

        그러므로 $\dfrac{1}{2} + \dfrac{1}{2} = 1$ 로 정의된다는 것이다. 이런 이유로 $\{0|1\} = \dfrac{1}{2}$ 로 정의한 것이다. 

## well-formedness

!!! def "정리 14"

    $$ x \leq x' \land y \leq y' \implies x + y \leq x'+y' $$

!!! def "정리 15"

    $$ x+y \geq x'+y' \land y \leq y' \implies x \geq x' $$

- 증명 

    정리 14 와 정리 15 를 같이 증명해보자. 이 둘을 Boolean function $p, q$ 로 정의한다. 

    $$ p(x,x',y,y') \iff (x \leq x' \land y \leq y' \implies x + y \leq x'+y') $$

    $$ q(x,x',y,y') \iff (x+y \geq x'+y' \land y \leq y' \implies x \geq x') $$

    사실 우리는 지금까지 초현실수의 덧셈이 well-formed 을 생성한다는 것을 증명하지 않았기 때문에 초현실수의 well-formedness 에 의존성이 있는 그 어떠한 정리도 사용할 수 없다. 즉, 우리는 정리 1, 3, 4, 6 만을 사용할 수 있다. (well-formedness 에 의존성이 없는 이 정리들이 나중에 유용할 것이라고 언급했었는데 바로 여기에서 유용하다는 것이다.)

    정리 14 의 $x + y \leq x' + y'$ 를 증명하기 위하여 

    $$ \lnot \exists \alpha \in \{X_L + y, x+Y_L\} : x'+y' \leq \alpha \land \lnot \exists \beta \in \{X'_R+y', x'+Y'_R\} : \beta \leq x+y \tag{3.14} $$

    를 증명해야 하는데 이는

    $$ \forall \alpha \in \{X_L + y, x+Y_L\} : x'+y' \not \leq \alpha \land \forall  \beta \in \{X'_R+y', x'+Y'_R\} : \beta \not \leq x+y \tag{3.14} $$

    이고

    $$ x + y = \{X_L + y, x+Y_L | X_R + y, x+Y_R\} $$

    $$ x' + y' = \{X'_L + y', x' + Y'_L | X'_R + y', x' + Y'_R\} $$

    이므로 $(3.14)$ 는 

    $$ x' + y' \not \leq X_L + y \tag{3.15} $$

    $$ x' + y' \not \leq x + Y_L \tag{3.16} $$

    $$ X'_R + y' \not \leq x + y \tag{3.17} $$

    $$ x' + Y'_R \not \leq x + y \tag{3.18} $$

    이 참일 때 참이 된다. ▲ 

    $(3.15)$ 가 거짓이라고 가정하자. 그러면 정리 14 의 조건부에서 $y \leq y'$ 가 참이므로 이를 연결하여 

    $$ X_l + y \geq x' + y' \land y \leq y' \tag{3.19} $$

    를 얻는다. 이는 Boolean function $q(X_L, x', y, y')$ 의 조건부와 같으므로 $X_L \geq x'$ 를 함의한다. 그러나 정리 5 에 의하여 $X_L < x$ 이고 정리 14 의 조건부에 의하여 $x \leq x'$ 이므로 $X_L < x'$ 이고, 이는 모순이다. Boolean function $q$ 가 참이라고 가정하면 $(3.15)$ 를 거짓이라고 가정한 것이 잘못되었음을 알 수 있다. 그러므로 $(3.15)$ 는 참이다. ▲ 

    비슷하게 $q(X_L, x', y, y')$ 가 참이라고 가정하면 $(3.16)$ 도 참이다. ▲ 

    비슷하게 $q(x, X'_R, y, y')$ 가 참이라고 가정하면 $(3.17)$ 도 참이다. ▲ 

    비슷하게 $q(y, Y'_R, x, x')$ 가 참이라고 가정하면 $(3.18)$ 도 참이다. ▲ 

    그러므로 $(3.14)$ 는 참이다. 이로써 정리 14 는 정리 15 를 가정하였을 때 참임이 증명되었다. ▲ 

    정리 15 의 조건부 $x + y \geq x'+y'$ 와 $\geq$ 의 정의로부터 다음이 참임을 알 수 있다.

    $$ X'_L + y' \not \geq x+y \tag{3.20} $$

    $$ x' + Y'_L \not \geq x+y \tag{3.21} $$

    $$ x' + y' \not \geq X_R+y \tag{3.22} $$

    $$ x' + y' \not \geq x+Y_R \tag{3.23} $$

    정리 15 가 틀렸다고 가정하면 조건부 $y \leq y'$ 와 부정된 결론부 $x \not \geq x'$ 를 얻는다. $x \not \geq x'$ 는 [$\not \leq$ 의 정의](#34f824094) 에 의하여

    $$ \exists x'_L \in X'_L : x \leq x'_L \lor \exists x_R \in X_R : x_R \leq x' \tag{3.24} $$

    와 동치이다. $(3.24)$ 의 왼쪽 명제 $x \leq x'_L$ 와 $y \leq y'$ 를 결합하면 $p(x, x'_L, y, y')$ 의 조건부를 얻는데 이는 곧 $x + y \leq x'_L + y'$ 를 함의한다. 그런데 이는 $(3.20)$ 과 모순이다. 그러므로 Boolean function $p$ 가 참임을 가정하면 정리 15 는 참이다. ▲ 

    비슷하게 $(3.24)$ 의 오른쪽 명제를 $y \leq y'$ 와 결합하면 $p(x_R, x', y, y')$ 의 조건부를 얻는데 이는 $x_R + y \leq x'+y'$ 를 함의한다. 그런데 이는 $(3.22)$ 와 모순이다. 그러므로 정리 14 를 가정하면 정리 15 가 참임을 알 수 있다. ▲ 

    그러므로 정리 14 와 정리 15 는 동치이다. 즉, 

    $$ p \iff q $$

    이다. 이제 정리 14 나 정리 15 둘 중 하나를 증명하면 모든 증명이 끝난다. ▲ 

    정리하자면, $p(x,y,x',y')$ 는 $q(X_L, x', y, y'), q(Y_l, y', x, x'), q(x, X'_R, y, y'), q(y, Y'_R, x, x')$ 를 가정하면 참이다.
    
    $q(x, x', y, y')$ 는 $p(x, x'_L, y, y'), p(x_R, x', y, y')$ 를 가정하면 참이다. 

    그러므로 $p(x, y, x', y')$ 는 다음을 가정하면 참이다. 

    $$ p(X_L, x'_L, y, y') \tag{3.25} $$

    $$ p(X _{LR}, x', y, y') \tag{3.26} $$

    $$ p(Y_L, y'_L, x, x') \tag{3.27} $$

    $$ p(Y _{LR}, y', x, x') \tag{3.28} $$

    $$ p(x, X' _{RL}, y, y') \tag{3.29} $$

    $$ p(x_R, X'_R, y, y') \tag{3.30} $$

    $$ p(y, Y' _{RL}, x, x') \tag{3.31} $$

    $$ p(y_R, Y'_R, x, x') \tag{3.32} $$

    그런데 이 명제들은 모두 다 $p(x, y, x', y')$ 의 첫번째와 두번째 파라미터를 그것의 parents 로 치환하였다. 이 사실은 $p(x, y, x', y')$ 가 결국 최초의 parents 를 파라미터로 갖는 $p$ 의 진리값에 의존한다는 것을 알려준다. 다시말해, $p(x, x', y, y')$ 는 

    $$ p(x, \varnothing , y, y') \tag{3.33} $$

    $$ p(\varnothing, x', y, y') \tag{3.34} $$

    이 참일 때 참이 된다. 이는 

    $$ x \leq \varnothing \land y \leq y' \implies x + y \leq \varnothing + y' \tag{3.35} $$

    $$ \varnothing \leq x' \land y \leq y' \implies \varnothing + y \leq x' + y' \tag{3.36} $$

    이 참일 때 정리 14 가 증명됨을 뜻한다. $\varnothing$ 과의 연산은 $\varnothing$ 이므로 $(3.35), (3.36)$ 의 결론부는 각각

    $$ x + y \leq \varnothing $$

    $$ \varnothing \leq x' + y' $$

    이 되고, [초현실수와 초현실수 집합의 비교]() 에 의하여 $\varnothing$ 과의 부등식 관계기호는 항상 참이므로 결국 $(3.35), (3.36)$ 이 참임을 알 수 있다. 그러므로 $(3.33), (3.34)$ 도 참이고 이로써 정리 14 가 증명되었다. 이로써 모든 증명이 끝났다. ■  

- 이 정리 또한 초현실수의 well-formedness 에 의존하지 않고 증명되었다. 

!!! def "따름정리 16"

    $$ x=x' \land y = y' \implies x+y = x' + y' $$

- 증명 

    정리 14 로부터 바로 증명된다. ■ 

- 이 정리로부터 만약 $2+3$ 을 계산했을 때 $2$ 나 $3$ 을 표현하는 어떤 초현실수를 택하더라도 그 결과가 항상 같은 값임을 보장받을 수 있다. 

!!! def "정리 17"

    $$ x < x' \land y \leq y' \implies x + y < x' + y' $$

- 증명 

    [$<$ 의 정의](#e9c1c7e5b) 에 의하여 $x < x'$ 는 $x \leq x', x \not \geq x'$ 를 뜻한다.
    
    (여기서 [단순화된 $<$ 의 정의](#d0af3b928) 도 사용할 수 없는데 이 정리가 초현실수의 well-formed 에 의존하기 때문이다. 우리는 아직 초현실수의 덧셈이 well-formed 초현실수를 생성한다는 것을 증명하지 않았다. )

    $x \leq x', y \leq y'$ 이므로 [정리 14](#19305c513) 로부터 

    $$ x + y \leq x'+y' \tag{3.37} $$

    을 얻는다. [정리 15](#6cef2829a) 의 대우 

    $$ x \not \geq x' \implies x + y \not \geq x'+y' \lor y \not \leq y' \tag{3.38} $$

    에서 $x \not \geq x'$ 이므로 $x + y \not \geq x'+y' \lor y \not \leq y'$ 인데 $y \leq y'$ 이므로 

    $$ x + y \not \geq x' + y' \tag{3.39} $$

    이다. $(3.37)$ 과 $(3.39)$ 와 [$<$ 의 정의](#e9c1c7e5b) 에 의하여 

    $$ \therefore x + y < x' + y' $$

    이다. ■ 

이제 초현실수의 덧셈이 well-formed 인 초현실수를 생성한다는 것을 증명할 수 있다. 

!!! def "정리 18"

    초현실수 $a, b$ 에 대하여 

    $$ a + b = \{A_L + b, a + B_L | A_R + b, a + B_R\} $$

    은 well-formed 이다. 

- 증명

    [well-formedness 의 정의](#06f455e4b) 에 의하여 

    $$ A_L + b < A_R + b \tag{3.40} $$

    $$ A_L + b < a + B_R \tag{3.41} $$

    $$ a + B_L < A_R + b \tag{3.42} $$

    $$ a + B_L < a + B_R \tag{3.43} $$

    이 증명되면 초현실수 덧셈이 well-formed 인 초현실수를 생성한다는 것이 증명된다. ▲ 

    $(3.40), (3,43)$ 은 초현실수 $a, b$ 의 well-formedness 를 정리 17 와 연결하면 곧바로 도출된다. 즉, $A_L < A_R$ 와 $b \leq b$ 에서 $A_L + b < A_R + b$ 가 도출되고 $(3.43)$ 도 비슷하게 증명된다. ▲ 

    $(3.41)$ 을 증명해보자. [정리 5](#c076cc283) 에 의하여 $A_L < a$ 이고 정리 17 에 의하여 

    $$ A_L + b < a + b \tag{3.44} $$

    이다. 같은 원리로 

    $$ a + b < a + B_R \tag{3.45} $$

    를 얻는다. $(3.44), (3.45)$ 와 [The transitive law](#70892e5fd) 에 의하여 $(3.41)$ 을 얻는다. ▲ 

    $(3.42)$ 도 비슷하게 증명된다. ■ 

- 이로써 초현실수 덧셈 연산이 well-formedness 를 만족한다는 것을 보장받았다. 이제 초현실수 덧셈이 make sense 한지 따져보기만 하면 된다. 

    그에 앞서 몇가지 대수학 이론을 살펴보자. 

## make sense

!!! def ""

    군(group) : 집합 $X$ 와 집합 $X$ 의 원소를 연산하는 대수적 연산자 $\star$ 에 대하여 

    - (associative law) $a,b,c \in X : (a \star b) \star c = a \star (b \star c)$

    - (neutral element) $\exists e \in X \text{ s.t. }\ \forall a \in X : a \star e = a \land e \star a = a$ 

    - (inverse element) $\exists \bar{a} \in X \text{ s.t. }\ \forall a \in X : a \star \bar{a} = e$

    이 성립하면 $(X, \star )$ 를 군이라고 한다.

!!! def ""

    가환군(commutative group), 아벨군(abelian group) : 집합 $X$ 와 집합 $X$ 의 원소를 연산하는 대수적 연산자 $\star$ 에 대하여 군의 조건이 성립되면서

    - (commutative law) $a \star b = b \star a$

    이 성립하면 $(X, \star )$ 를 아벨군이라 한다. 

- 예시 

    $(\R, +)$ 는 항등원 $0$ 와 $x$ 의 역원 $-x$ 를 갖는 가환군이다. 

    $(\R, \times )$ 는 군이 아닌데 항등원을 갖지만 모든 실수에 대한 역원이 존재하지는 않기 때문이다. 즉  $\not \exists  x \in \R \text{ s.t. }\ 0 \times x = 1$ 이다. 

!!! def "정리 19"

    $0$ 은 초현실수 덧셈의 항등원이다. 즉, $0 + x = x \land x + 0 = x$ 이다.

- 증명 

    명백하게 $0 + 0 = 0$ 이다. 이제 $x$ 에 대하여 $x$ 의 parents 에서 이 정리가 성립한다고 가정하자. 

    $$ \begin{equation}\begin{split} 0 + x& = \{\varnothing + x, 0 + X_L | \varnothing + x, 0 + X_R\}\\ & = \{0+X_L | 0 + X_R\} \end{split}\end{equation} \tag{3.46} $$

    인데 $x$ 의 parents 에 대하여 이 정리가 성립하므로 $0 + X_L = X_L \land 0 + X_R = X_R$ 이다. 따라서 

    $$ \{0 + X_L | 0 + X_R\} = \{X_L | X_R\} = x $$

    를 얻고, $0+x=x$ 가 증명된다. ▲ 

    $x+0=x$ 도 비슷하게 증명할 수 있다. ■ 

!!! def "정리 20"

    초현실수의 덧셈은 commutative law 를 만족한다. 즉, $x + y = y + x$ 이다. 

- 증명 

    $x, y$ 의 parents 에 대하여 commutative law 가 성립한다고 가정하면 [$+$ 의 정의에 의하여 $x, y$ 에 대하여 commutative law 가 성립함을 자명하게 알 수 있다.](#cf34e3c3f) 
    
    그러므로 귀납법을 쓰기 위하여 $0+x=x+0$ 만 증명하면 되는데 이는 정리 19 에 의하여 자명하게 참이다. ■ 

!!! def "정리 21"

    초현실수의 덧셈은 associative law 를 만족한다. 즉, $(x + y) + z = x + (y + z)$ 이다. 

- 증명

    $$ (x + y) + z = \{(x+y)_L + z, (x+y)+Z_L | (x+y)_R + z, (x+y)+Z_R\} $$

    $$ = \{(X_L + y) + z, (x + Y_L) + z, (x+y) + Z_L | (X_R+y) + z, (x+Y_R) + z, (x+y) + Z_R\} \tag{3.47} $$

    $$ x + (y + z) = \{X_L + (y+z), x+(y+z)L | X_R + (y+z), x+(y+z)_R\} $$

    $$ = \{X_L + (y+z), x+(Y_L+z), x+(y+Z_L) | X_R + (y+z), x+(Y_R+z), x+(y+Z_R)\} \tag{3.48} $$

    에서 $(3.47), (3.48)$ 이 $x, y, z$ 의 parents 에 대한 associative 가 성립함을 가정하면 성립한다는 것을 알 수 있다. 

    그러므로 parents 의 parents 를 거슬러 올라가면서 이 정리의 참거짓을 결정하게 된다. 그런데 이 초현실수가 $0$ 로 치환되면 참이므로 결국 참임을 알 수 있다. $0$ 는 최초의 초현실수이다. 그러므로 이 정리는 참이다. ■ 

!!! def "정리 22"

    임의의 초현실수 $x$ 는 $x + (-x) = 0$ 를 만족하는 덧셈의 역원 $-x$ 를 가진다. 

- 증명

    먼저 $-x$ 의 존재성, 즉 $-x$ 가 well-formed 인 초현실수임을 증명해야 한다. 그리고 $x + (-x) = 0$ 임을 증명하면 증명이 끝난다. 

    먼저 $(-X)_L = -X_R$ 이고 $(-X)_R = -X_L$ 이다.

    $-x$ 의 well-formedness 를 증명하기 위하여 $X_L < X_R$ 를 기반으로 

    $$ -X_R < -X_L \tag{3.49} $$

    를 증명해야 한다. 이는 결국 $a \leq b \iff -b \leq -a$ 의 증명을 요구한다. $a \leq b$ 는 

    $$ \lnot \exists \alpha \in A_L : b \leq \alpha \land \lnot \exists \beta \in B_R : \beta \leq a \tag{3.50} $$

    을 뜻하고 $-b \leq -a$ 는 

    $$ \lnot \exists \xi \in (-B)_L : -a \leq \xi \land \lnot \exists \eta \in (-A)_R : \eta \leq -b \tag{3.51} $$

    을 뜻한다. $(3.51)$ 은 

    $$ \lnot \exists \xi \in -B_R : -a \leq \xi \land \lnot \exists \eta \in -A_L : \eta \leq -b \tag{3.52} $$

    와 같다. 

    이때 $(3.50)$ 의 왼쪽 명제와 $(3.52)$ 의 오른쪽 명제를 $\alpha = - \eta$ 를 택하여 비교해보자. 

    $$ \lnot \exists -\eta \in A_L : b \leq - \eta , \lnot \exists \eta \in -A_L : \eta \leq -b $$
    
    또한 $(3.50)$ 의 오른쪽 명제와 $(3.52)$ 의 왼쪽 명제를 $\xi = - \beta$ 를 택하여 비교해보자. 

    $$ \lnot \exists \beta \in B_R : \beta \leq a , \lnot \exists - \beta \in -B_R : -a \leq - \beta $$
    
    그러면 $a,b$ 의 parents 에 대하여 참임을 가정하면 $a \leq b \iff -b \leq -a$ 가 참이 됨을 알 수 있다. (*근데 이것도 은연중에 가정하고 있는 전제가 있는 것 같은데. 즉 $- a \in A$ 와 $a \in -A$ 가 같다는 전제가 있는 것 같다.  $-$ 는 일단 초현실수의 덧셈의 역원으로 정의되었으니까, 지금 은연중에 가정하고 있는 건 초현실수 집합 $A$ 에 대하여 $-A$ 란 역원의 집합이라는 것이다. 어쨌든 $-a \in A \iff a \in -A$ 를 가정하고, $A_L, B_R$ 에 대하여 성립함을 가정하면 $a,b$ 에 대해서도 성립한다고 할 수 있지. 그렇게 되면 $0$ 에 대해서만 성립함을 보이면 귀납법에 의하여 증명되었다고 할 수 있고.*)

    비슷한 과정을 통하여 $a \leq 0 \iff 0 \leq  -a$ 가 $a$ 의 parents 에 대하여 성립하면 성립함을 보일 수 있다. 

    마지막으로 $0 \leq -0$ 는 자명하다. 그러므로 $-x$ 는 well-formed 이다. ▲ 

    이제 $x + (-x) = 0$ 을 증명해보자. $x = 0$ 이면 $-x = 0$ 임이 자명하므로 성립한다. 
    
    $x$ 의 parents 에 대하여 성립함을 가정하자.

    $$ x + (-x) = \{X_L + (-x), x+(-X_R) | X_R + (-x), x + (-X_L) \} \tag{3.53} $$

    에서 left set 의 첫번째 원소는 

    $$ X_L + (-x) = \{X _{LL} + (-x), X_L + (-X_R) | X _{LR} + (-x) , X_L + (-X_L)\} \tag{3.54} $$

    이다. $x$ 의 parents 에 대하여 성립하므로 $X_L + (-X_L) = 0$ 인데 [정리 5](#c076cc283) 에 의하여 초현실수는 right set 의 모든 원소보다 작으므로 

    $$ X_L + (-x) < 0 $$

    이다. $(3.53)$ 의 left set 의 두번째 원소는 

    $$ x + (-X_R) = \{X_L + (-X_R) , x + (-X _{RR}) | X_R + (-X_R), x + (-X _{RL})\} \tag{3.55} $$

    인데 또 다시 [정리 5](#c076cc283) 를 적용하여 
    
    $$x + (-X_R) < 0$$
    
    를 얻을 수 있다. 같은 방식으로 $X_R + (-x) > 0, x + (-X_L) > 0$ 를 얻을 수 있다. 즉, $(3.53)$ 의 left set 의 모든 원소가 $0$ 보다 작고, right set 의 모든 원소가 $0$ 보다 크다는 결론을 내릴 수 있다. 

    그러면 [따름정리 13](#c9737ce31) 에 의하여 left set 과 right set 사이의 가장 오래된 원소 $0$ 가 $x + (-x)$ 의 값이다. 그러므로

    $$ \therefore x + (-x) = 0 $$

    이다. ■ 

!!! def ""

    $$ a + (-b) \iff a - b $$

- 매우 쉽게 증명할 수 있다.

- 증명

!!! def ""

    준동형사상(homomorphism) : 집합 $A$ 와 $B$ 에서 정의된 항수 $k$ 를 갖는 연산 $\mu$ 에 대하여 사상 $f : A \to B$ 가 

    $$ \forall a_1, \dots, a_k \in A : f(\mu _A(a_1, \dots, a_k)) = \mu _B(f(a_1), \dots, f(a_k)) $$

    를 만족할 때 $f$ 를 준동형사상이라 한다. 

- 준동형사상은 두 대수 구조의 연산 구조를 보존하는 사상이다. 가령 이항 연산 $\cdot$ 이 두 집합 $A, B$ 에서 연산될 때 사상 $f : A \to B$ 가 

    $$ f(x \cdot y) = f(x) \cdot f(y) $$

    를 만족하면 $f$ 가 연산 구조를 보존한다고 말한다.

- 예시 

    실수 집합 $\R$ 은  덧셈과 곱셈이 정의된 환(ring)이다. $2 \times 2$ 행렬의 집합 $\R _{2 \times 2}$ 또한 덧셈과 곱셈이 정의된 환(ring)이다. 사상 $f: \R \to \R _{2 \times 2}$ 를 

    $$ f(r) = \begin{pmatrix} r&0\\ 0&r\\ \end{pmatrix} $$

    와 같이 정의하면 

    $$ f(r + s) = \begin{pmatrix} r+s&0\\ 0&r+s\\ \end{pmatrix} = \begin{pmatrix} r&0\\ 0&r\\ \end{pmatrix} + \begin{pmatrix} s&0\\ 0&s\\ \end{pmatrix} = f(r) + f(s) $$

    이고 

    $$ f(rs) = \begin{pmatrix} rs&0\\ 0&rs\\ \end{pmatrix} = \begin{pmatrix} r&0\\ 0&r\\ \end{pmatrix} \begin{pmatrix} s&0\\ 0&s\\ \end{pmatrix} = f(r) f(s) $$

    이므로 사상 $f$ 는 환 $\R$ 을 환 $\R _{2 \times 2}$ 로 보내면서 연산 구조를 보존한다. 그러므로 $f$ 는 실수집합환과 $2 \times 2$ 행렬집합환의 준동형사상이다.

- 전단사 준동형사상을 동형사상(isomorphism) 이라 한다. 

!!! def "정리 23"

    Dali function 은 $(\R, +)$ 을 $(\mathbf{No} , +)$ 로 보내는 준동형사상이다. 즉, 실수 $a, b$ 와 Dali function $\delta$ 에 대하여 

    $$ \delta (a + b) = \delta (a) + \delta (b) $$

    이다.

- 전자의 $+$ 는 실수의 $+$ 이고 후자의 $+$ 는 초현실수의 $+$ 이다.

- 이 정리는 Dali function 이 준동형사상이라는 것, 즉 실수의 연산 구조를 그대로 보존하여 초현실수로 보낸다는 것을 말해준다. 

- 증명

    $a = 0 \lor b = 0$:

    [정리 19](#820dbbc7f) 에 의하여 초현실수의 항등원은 $\{|\}$ 이고, 실수의 항등원은 $0$ 이다. 그러므로 

    $$ \delta (0+b) = \delta (b) = \{|\} + \delta (b) = \delta (0) + \delta (b) $$

    이다. ▲ 

    $a, b \in \mathbb{Z} _{+}$:

    [Dali function](#b3aed9bc1) 의 정의에 의하여 

    $$ \delta (a) = \{\delta (a-1)|\}, \delta (b) = \{\delta (b-1)|\}, \delta (a+b) = \{\delta (a+b-1)|\} $$

    이다. 또한 $a = 0, b = 0$ 에 대하여 이 정리가 성립함을 이미 증명했다. 이제 귀납법을 사용할텐데 지금까지처럼 parents 에 대하여 귀납법을 전개하는 것이 아니라 양의 정수에 대하여 귀납법을 전개할 것이다. 

    $a-1, b-1$ 에 대하여 정리가 성립함을 가정하면 

    $$ \delta (a-1+b) = \delta (a-1) + \delta (b) \tag{3.56} $$

    $$ \delta (a+b-1) = \delta (a) + \delta (b-1) \tag{3.57} $$

    이다. 그러므로 
    
    $$ \begin{equation}\begin{split} \delta (a) + \delta (b)& = \{\delta (a)_L + \delta (b), \delta (a) + \delta (b)_L | \delta (a)_R + \delta (b), \delta (a) + \delta (b)_R\} \\ & = \{\delta (a-1) + \delta (b), \delta (a) + \delta(b-1)| \}\\ & = \{\delta (a-1+b) , \delta (a+b-1)| \}\\ & = \delta (a+b) \end{split}\end{equation} \tag{3.58} $$

    이다. 이에 따라 귀납법에 의하여 이 경우가 증명되었다. ▲ 

    $a, b \in \mathbb{Z} _{-}$:

    [Dali function](#b3aed9bc1) 의 정의에 의하여 

    $$ \delta (a) = \{|\delta (a+1)\}, \delta (b) = \{|\delta (b+1)\}, \delta (a+b) = \{|\delta (a+b+1)\} $$

    이다. 또한 $a = 0, b = 0$ 에 대하여 이 정리가 성립함을 이미 증명했다. 이제 귀납법을 사용할텐데 지금까지처럼 parents 에 대하여 귀납법을 전개하는 것이 아니라 음의 정수에 대하여 귀납법을 전개할 것이다. 

    $a+1, b+1$ 에 대하여 정리가 성립함을 가정하면 

    $$ \delta (a+1+b) = \delta (a+1) + \delta (b) \tag{3.59} $$

    $$ \delta (a+b+1) = \delta (a) + \delta (b+1) \tag{3.60} $$

    이다. 그러므로 
    
    $$ \begin{equation}\begin{split} \delta (a) + \delta (b)& = \{\delta (a)_L + \delta (b), \delta (a) + \delta (b)_L | \delta (a)_R + \delta (b), \delta (a) + \delta (b)_R\} \\ & = \{|\delta (a+1) + \delta (b), \delta (a) + \delta(b+1) \}\\ & = \{|\delta (a+1+b) , \delta (a+b+1) \}\\ & = \delta (a+b) \end{split}\end{equation} \tag{3.61} $$

    이다. 이에 따라 귀납법에 의하여 이 경우가 증명되었다. ▲ 

    $a \in \mathbb{Z} _{+}, b \in \mathbb{Z} _{-}$:

    [Dali function](#b3aed9bc1) 의 정의에 의하여 $\delta (a) = \{\delta (a-1)|\}, \delta (b) = \{|\delta (b+1)\}$ 이다. 정리 [Dali function 은 실수의 순서를 보존한다]() 에 의하여

    $$ \delta (a+b-1) < \delta (a+b) < \delta (a+b+1) \tag{3.62} $$

    이다. $a+b$ 의 부호에 따라서 다음의 결과를 얻는다. 

    - $a+b>0$ 이면 $\delta (a+b) = \{\delta (a+b-1)|\}$ 이다. [정리 11](#6c1e1f527) 과 $(3.62)$ 에 의하여 $\delta (a+b) = \{\delta (a+b-1) | \delta (a+b+1)\}$

    - $a+b=0$ 이면 $\delta (a+b) = \{|\}$ 이다. [정리 11](#6c1e1f527) 과 $(3.62)$ 에 의하여 $\delta (a+b) = \{\delta (a+b-1) | \delta (a+b+1)\}$

    - $a+b<0$ 이면 $\delta (a+b) = \{|\delta (a+b+1)\}$ 이다. [정리 11](#6c1e1f527) 과 $(3.62)$ 에 의하여 $\delta (a+b) = \{\delta (a+b-1) | \delta (a+b+1)\}$

    그러므로 모든 경우에서 

    $$ \delta (a+b) = \{\delta (a+b-1) | \delta (a+b+1)\} \tag{3.63} $$

    를 얻는다. 이 정리가 $a = 0, b = 0$ 에서 성립한다는 것을 이미 증명했다. 이제 $a-1$ 과 $b+1$ 에서 이 정리가 성립한다고 가정하자. 즉, 

    $$ \delta (a-1+b) = \delta (a-1) + \delta (b) \tag{3.64} $$

    $$ \delta (a+b+1) = \delta (a) + \delta (b+1) \tag{3.65} $$

    를 가정한다. 이를 기반으로 

    $$ \begin{equation}\begin{split} \delta (a) + \delta (b)& = \{\delta (a)_L + \delta (b), \delta (a) + \delta (b)_L | \delta (a)_R + \delta (b), \delta (a) + \delta (b)_R\} \\ & = \{\delta (a-1)+\delta (b)|\delta (a) + \delta (b+1) \}\\ & = \{\delta (a-1+b)| \delta (a+b+1) \}\\ & = \delta (a+b) \end{split}\end{equation} \tag{3.66} $$

    를 얻는다. 이에 따라 귀납법에 의하여 이 경우가 증명되었다. ▲ 

    $a \in \mathbb{Z} _{+}, b = \dfrac{j}{2^k} \text{ s.t. }\ j \in \mathbb{Z} , k \in \mathbb{Z} _{+}$:

    (이때 $\dfrac{j}{2^k}$ 는 기약분수이다.)

    [Dali function](#b3aed9bc1) 의 정의에 의하여 $\delta (a) = \{\delta (a-1)|\}, \delta (b) = \bigg \{\delta \bigg (\dfrac{j-1}{2 ^{k}}\bigg )\bigg |\delta \bigg (\dfrac{j+1}{2^k}\bigg )\bigg \}$ 이다. 또한 

    $$ a+b = a+ \dfrac{j}{2^k} = \dfrac{2^ka + j}{2^k} \tag{3.67} $$

    이므로 [Dali function](#b3aed9bc1) 에 의하여

    $$ \delta (a+b) = \bigg \{\delta \bigg (\dfrac{2^ka+j-1}{2^k}\bigg )\bigg |\delta \bigg (\dfrac{2^ka+j+1}{2^k}\bigg )\bigg \} \tag{3.68} $$

    이다. 우리는 이 정리가 $a = 0$ 이고 $b$ 가 정수일 때, 즉 $k = 0$ 일 때 성립한다는 것을 이미 증명했다. 이제 이 정리가 $a - 1, k - 1$ 에서 성립한다고 가정하고 $a, k$ 에 대하여 성립함을 보이자. 그러면

    $$ \begin{equation}\begin{split} \delta (a) + \delta (b) & = \{\delta (a) _L + \delta (b), \delta (a) + \delta (b)_L | \delta (a)_R + \delta (b) , \delta (a) + \delta (b) _R\} \\ & = \bigg \{\delta (a-1) + \delta \bigg (\dfrac{j}{2^k}\bigg ), \delta (a) + \delta \bigg (\dfrac{j-1}{2^k}\bigg )\bigg |\delta (a) + \delta \bigg (\dfrac{j+1}{2^k}\bigg )\bigg \} \\ & = \bigg \{\delta \bigg (a - 1 + \dfrac{j}{2^k}\bigg ), \delta \bigg (a + \dfrac{j-1}{2^k}\bigg )\bigg |\delta \bigg (a + \dfrac{j+1}{2^k}\bigg )\bigg \} \end{split}\end{equation} \tag{3.69} $$

    가 성립한다. 마지막 연산이 가능한 이유는 $\dfrac{j-1}{2^k}, \dfrac{j+1}{2^k}$ 가 최소 $2$ 로 약분되므로 분모가 최대 $2 ^{k-1}$ 가 되기 때문이다. 더욱 단순화시켜보면 

    $$ \begin{equation}\begin{split} \delta (a) + \delta (b) & = \bigg \{\delta \bigg ( \dfrac{2^ka -2^k + j}{2^k}\bigg ), \delta \bigg (\dfrac{2^ka + j-1}{2^k}\bigg )\bigg |\delta \bigg (\dfrac{2^ka + j+1}{2^k}\bigg )\bigg \} \\ & = \bigg \{\delta \bigg (\dfrac{2^ka + j-1}{2^k}\bigg )\bigg |\delta \bigg (\dfrac{2^ka + j+1}{2^k}\bigg )\bigg \} \end{split}\end{equation} \tag{3.70} $$

    이 된다. 마지막 단순화는 $k \leq 0 \iff 2 ^{k} \geq 1$ 를 기반으로 [따름정리 10](#810bebedd) 에 의하여 이루어진다. $(3.70)$ 은 $(3.68)$ 과 같으므로 이 경우에서 $\delta (a)+\delta (b) = \delta (a+b)$ 가 증명되었다. ▲ 

    $a \in \mathbb{Z} _{-}, b = \dfrac{j}{2^k} \text{ s.t. }\ j \in \mathbb{Z} , k \in \mathbb{Z} _{+}$:

    (이때 $\dfrac{j}{2^k}$ 는 기약분수이다.)

    이전의 경우와 증명이 매우 비슷하므로 생략한다. ▲ 

    $a = \dfrac{j_a}{2 ^{k_a}} \text{ s.t. }\ j_a \in \mathbb{Z} , k_a \in \mathbb{Z} _{+} , b = \dfrac{j_b}{2 ^{k_b}} \text{ s.t. }\ j_b \in \mathbb{Z} , k_b \in \mathbb{Z} _{+}$:

    (이때 $\dfrac{j_a}{2^k_a}, \dfrac{j_b}{2^k_b}$ 는 기약분수이다.)

    [Dali function](#b3aed9bc1) 에 의하여 $\delta (a) = \bigg \{\delta \bigg (\dfrac{j_a-1}{2 ^{k_a}}\bigg )\bigg |\delta \bigg (\dfrac{j_a+1}{2 ^{k_a}}\bigg )\bigg \}$ 이고 $\delta (b) = \bigg \{\delta \bigg (\dfrac{j_b-1}{2 ^{k_b}}\bigg )\bigg |\delta \bigg (\dfrac{j_b+1}{2 ^{k_b}}\bigg )\bigg \}$ 이다. 일반성을 훼손하지 않고 $k_a \geq k_b$ 라고 가정할 수 있으며 이 경우 

    $$ \begin{equation}\begin{split} a + b & = \dfrac{j_a}{2 ^{k_a}} + \dfrac{j_b}{2 ^{k_b}}\\ & = \dfrac{j_a + 2 ^{k_a - k_b}j_b}{2 ^{k_a}} \end{split}\end{equation} \tag{3.71} $$

    이므로 

    $$ \delta (a+b) = \bigg \{\delta \bigg (\dfrac{j_a + 2 ^{k_a-k_b}j_b - 1}{2 ^{k_a}}\bigg ) \bigg | \delta \bigg (\dfrac{j_a + 2 ^{k_a-k_b}j_b+1}{2 ^{k_a}}\bigg )\bigg \} \tag{3.72} $$

    이다. 우리는 이미 이 정리가 $a, b$ 가 정수일 때, 즉 $k_a = 0, k_b = 0$ 일 때 성립한다는 것을 증명했다. 그러므로 이 정리가 $k_a - 1, k_b - 1$ 에서 성립한다는 것을 가정하고 $k_a, k_b$ 에서 성립함을 보이자. 

    $$ \begin{equation}\begin{split} \delta (a) + \delta (b) & = \{\delta (a)_L + \delta (b), \delta (a) + \delta (b)_L | \delta (a)_R + \delta (b), \delta (a) + \delta (b)_R\}\\ & = \bigg \{\delta \bigg (\dfrac{j_a-1}{2 ^{k_a}}\bigg )+\delta \bigg (\dfrac{j_b}{2 ^{k_b}}\bigg ), \delta \bigg (\dfrac{j_a}{2 ^{k_a}}\bigg ) + \delta \bigg (\dfrac{j_b-1}{2 ^{k_b}}\bigg )\bigg | \\ & \qquad \qquad  \delta \bigg (\dfrac{j_a+1}{2 ^{k_a}}\bigg )+\delta \bigg (\dfrac{j_b}{2 ^{k_b}}\bigg ), \delta \bigg (\dfrac{j_a}{2 ^{k_a}}\bigg ) + \delta \bigg (\dfrac{j_b+1}{2 ^{k_b}}\bigg )\bigg\} \\ & = \bigg \{\delta \bigg (\dfrac{j_a-1}{2 ^{k_a}} + \dfrac{j_b}{2 ^{k_b}}\bigg ), \delta \bigg (\dfrac{j_a}{2 ^{k_a}}+\dfrac{j_b-1}{2 ^{k_b}}\bigg )\bigg | \delta \bigg (\dfrac{j_a+1}{2 ^{k_a}} + \dfrac{j_b}{2 ^{k_b}}\bigg ), \delta \bigg (\dfrac{j_a}{2 ^{k_a}} + \dfrac{j_b+1}{2 ^{k_b}}\bigg )\bigg\} \\ \end{split}\end{equation} \tag*{} $$

    에서 마지막 연산은 $\dfrac{j_a-1}{2 ^{k_a}}$ 가 최소 $2$ 로 약분되서 분모가 최대 $2 ^{k_a-1}$ 로 바뀌기 때문이다. 더욱 단순화를 시켜보면

    $$ \begin{equation}\begin{split} \delta (a) + \delta (b) & = \bigg \{\delta \bigg( \dfrac{(j_a-1) + 2 ^{k_a-k_b}j_b}{2 ^{k_a}} \bigg ), \delta \bigg (\dfrac{j_a + (j_b -1) 2 ^{k_a-k_b}}{2 ^{k_a}}\bigg ) \bigg | \\ & \qquad \qquad  \delta \bigg (\dfrac{(j_a+1) + 2 ^{k_a-k_b}j_b}{2 ^{k_a}}\bigg ), \delta \bigg (\dfrac{j_a+(j_b + 1)2 ^{k_a-k_b}}{2 ^{k_a}}\bigg )\bigg \}\\ & = \bigg \{\delta \bigg( \dfrac{j_a + 2 ^{k_a-k_b}j_b}{2 ^{k_a}} -1 \bigg ), \delta \bigg (\dfrac{j_a +  2 ^{k_a-k_b}j_b - 2 ^{k_a-k_b}}{2 ^{k_a}}\bigg ) \bigg | \\ &\qquad \qquad \delta \bigg (\dfrac{j_a + 2 ^{k_a-k_b}j_b + 1}{2 ^{k_a}}\bigg ), \delta \bigg (\dfrac{j_a+2 ^{k_a-k_b}j_b + 2 ^{k_a-k_b}}{2 ^{k_a}}\bigg )\bigg \}\\ & = \bigg \{\delta \bigg( \dfrac{j_a + 2 ^{k_a-k_b}j_b}{2 ^{k_a}} -1 \bigg )\bigg | \delta \bigg (\dfrac{j_a + 2 ^{k_a-k_b}j_b + 1}{2 ^{k_a}}\bigg )\bigg \}\\ \end{split}\end{equation} \tag{3.74} $$

    이 된다. 마지막 단순화는 $k_a \geq k_b \iff 2 ^{k_a-k_b} \geq 1$ 를 기반으로 [따름정리 10](#810bebedd) 에 의하여 이루어진다. $(3.74)$ 은 $(3.72)$ 과 같으므로 이 경우에서 $\delta (a)+\delta (b) = \delta (a+b)$ 가 증명되었다. ▲ 

    이로써 가능한 모든 경우에서 증명이 끝났다. ■ 

!!! def "초현실수 덧셈의 make sense"

    초현실수 덧셈 $(\mathbf{No}, +)$ 은 다음을 만족한다.

    - $(\mathbf{No} , +)$ 이 가환군을 이룬다.

    - Dali function 이 실수 덧셈 $+_r$ 과 초현실수 덧셈 $+_s$ 에 대하여 $(\R, + _{r})$ 에서 $(\mathbf{No} , + _{s})$ 로 가는 준동형사상이다. 
    
- 이 정리는 초현실수 덧셈이 make sense 하다는 것을 말해준다. 초현실수 덧셈이 make sense 하다는 것은 쉽게 말해 덧셈이 우리가 예상한대로 행동한다는 것이다. 

- 증명 

    정리 19, 20, 21, 22 에 의하여 $(\mathbf{No} , +)$ 는 아벨군이다. ▲ 

    정리 22 에 의하여 [Dali function](#b3aed9bc1) 은 $(\R, +)$ 을 $(\mathbf{No} ,+)$ 로 보내는 준동형사상이다. ▲ 

    그러므로 초현실수 덧셈 연산은 make sense 하다. ■ 

- 초현실수 덧셈 $(\mathbf{No} , +)$ 이 아벨군을 이룬다는 것은 $(\R, +)$ 와 대수적으로 동일한 성질을 띈다는 것이다. 

- [Dali function](#b3aed9bc1) 이 $(\R, +_r)$ 를 $(\mathbf{No} , +_s)$ 로 보내는 준동형사상이라는 조건은 

    $$ \delta (a +_r b) = \delta (a) +_s \delta (b) $$

    을 만족한다는 것이다. 이 조건이 필요한 것은 [Dali function](#b3aed9bc1) 이 실수덧셈군의 구조를 보존하면서 두 수의 덧셈 연산을 초현실수덧셈군으로 보낼 수 있다는 것이다. 
    
    구조를 보존한다는 조건이 필요한 이유는 [Dali function](#b3aed9bc1) 이 초현실수에 $0, 1, 2$ 같은 이름을 부여했으므로 실수에서 $2 + 3 = 5$ 라는 결과를 내는 것과 같이 초현실수에서도 $2 + 3 = 5$ 가 되어야 하기 때문이다. 
    
    그러므로 $\delta (2 + 3) = \delta (5)$ 가 초현실수 $5$ 라는 이름을 부여받듯이 $\delta (2) + \delta (3)$ 가 초현실수 이름 $2$ 와 $3$ 을 부여받은 덧셈 결과 $5$ 로 연산되어야 한다는 것이다. 

# 초현실수의 곱셈

!!! def "초현실수의 곱셈"

    초현실수 $a, b$ 에 대하여 

    $$ \begin{equation}\begin{split} ab &= \{A_Lb+aB_L - A_LB_L, A_Rb+aB_R -A_RB_R |\\ & \qquad \qquad  A_Lb+aB_R-A_LB_R, A_Rb+aB_L-A_RB_L\} \end{split}\end{equation} \tag*{} $$

    라고 정의한다. 

- 덧셈에서와 같이 이 곱셈 연산이 올바른가, 즉 well-formed 인 초현실수를 생성하는가 물어보아야 한다. 또한 이 곱셈 연산이 make sense 한지 검증해야 한다. 

    그러나 곱셈의 well-formedness 에 대해서는 생략한다.

- 특히 $0$ 은 곱셈연산에서 특별한 역할을 한다. 

!!! def "정리 24"

    $$ 0 \times x = x \times  0 = 0 $$

- 증명 

    $$ \begin{equation}\begin{split} 0x & = \{\varnothing x + 0X_L - \varnothing X_L, \varnothing x + 0 X_R - \varnothing X_R | \varnothing x + 0X_R - \varnothing X_R, \varnothing x + 0X_L - \varnothing X_L\}\\ & = \{|\} \\ & 0 \end{split}\end{equation} \tag{4.2} $$

    $x0=0$ 또한 비슷하게 증명가능하다. ■ 

!!! def "정리 25"

    곱셈의 항등원은 $1$ 이다. 즉, $1 \times x = x \land x \times 1 = x$ 이다. 

- 증명

    $$ 
    \begin{equation}\begin{split}
    1x &= \{0x+1X_L -0X_L, \varnothing x +1X_R- \varnothing X_R | 0b+1X_R-00_R, \varnothing x+1X_L-\varnothing X_L\}\\
    & = \{1X_L|1X_R\}
    \end{split}\end{equation} \tag{4.3}
    $$

    $x$ 의 parents 에 대하여 이 정리가 성립한다고 하면 $\{1X_L|1X_R\} = x$ 이다. $x = 0$ 일 때 이 정리가 자명하게 성립하므로 $1x = x$ 이다. ▲ 

    $x1 = x$ 도 비슷하게 증명가능하다. ■ 

!!! def "정리 26"

    초현실수 곱셈은 commutative law 를 만족한다. 즉, $xy = yx$ 이다.

- 증명

    $x, y$ 의 parents 에 대하여 성립함을 가정하면 이는 곱셈의 정의에 의하여 자명하게 성립한다. ▲ 

    $0x = x0$ 의 증명은 정리 24 에 의하여 자명하다. ■ 

!!! def "정리 27"

    초현실수 곱셈은 associative law 를 만족한다. 즉, $(xy)z = x(yz)$

- 증명

!!! def "정리 28"

    초현실수 곱셈과 덧셈은 distributive law 를 만족한다. 즉, $x(y+z) = xy+xz$ 이다.
    
- 증명

!!! def "정리 29"

    $0$ 을 제외한 임의의 초현실수 $x$ 는 $x \times \dfrac{1}{x} = 1$ 을 만족하는 곱셈의 역원 $\dfrac{1}{x}$ 을 가진다. 

- 증명

- 이 정리의 증명은 다음 장에서 논의할 것이다. 그때까지 우리는 분모가 $2$ 의 배수인 분수만 다룰 것이다. 사실 우리는 아직 $\dfrac{1}{3}$ 같은 초현실수가 어떤 것인지 다루지 않았다. 

!!! def "정리 30"

    초현실수 $a, b$ 와 Dali function $\delta$ 에 대하여 $\delta (ab) = \delta (a)\delta (b)$ 이다.

- 증명

## make sense

!!! def "초현실수 곱셈의 make sense"

    초현실수 곱셈은 다음을 만족한다.

    - $(\mathbf{No} \setminus \{0\} , \times )$ 이 아벨군을 이룬다.

    - Dali function 은 실수 곱셈 $\times  _r$ 과 초현실수 곱셈 $\times  _s$ 에 대하여 $(\R , \times  _{r})$ 에서 $(\mathbf{No}  , \times  _{s})$ 로 가는 준동형사상이다. 
    
- 이 정리는 초현실수 곱셈이 make sense 하다는 것을 말해준다. 초현실수 곱셈이 make sense 하다는 것은 쉽게 말해 곱셈이 우리가 예상한대로 행동하느냐는 것이다. 

- 증명 

    정리 25, 26, 27, 29 에 의하여 $(\mathbf{No} \setminus \{0\} , \times )$ 은 아벨군을 이룬다. ▲ 

    정리 30 에 의하여 [Dali function](#b3aed9bc1) 은 $(\R, \times )$ 을 $(\mathbf{No} , \times )$ 로 보내는 준동형사상이다. ▲ 

    그러므로 초현실수 곱셈 연산은 make sense 하다. ■ 

!!! def ""

    환(ring) : 집합 $R$ 이 두 이항연산 $+, \cdot$ 에 대하여 다음을 만족하면 환이다.

    1. $R$ 은 덧셈 $+$ 에 대하여 아벨군이다. 

        - associative : $\forall a,b,c \in R : (a+b)+c=a+(b+c)$

        - commutative : $\forall a,b \in R : a+b=b+a$

        - additive identity : $\exists 0 \in R \text{ s.t. }\ \forall a \in R : a + 0 = a$

        - additive inverse : $\exists -a \in R \text{ s.t. }\ \forall a \in R : a + -a = 0$
    
    2. $R$ 은 곱셈 $\cdot$ 에 대하여 모노이드이다.

        - associative : $(a \cdot b) \cdot c = a \cdot (b \cdot c)$

        - multiplicative identity : $\exists 1 \in R \text{ s.t. }\ \forall a \in R : a \cdot 1 = a \land 1 \cdot a = a$
    
    3. 곱셉 $\cdot$ 이 덧셈 $\times$ 에 대한 결합법칙을 만족한다.

        - left distributivity : $\forall a, b, c \in R : a \cdot (b+c) = (a \cdot b) + (a \cdot c)$

        - right distributivity : $\forall a, b, c \in R : (b+c) \cdot a = (b \cdot a) + (c \cdot a)$

!!! def ""

    $(\mathbf{No}, +, \times)$ 는 환이다.

- 증명

    [초현실수 덧셈의 make sense](#def5835c5) 와 초현실수 곱셈의 make sense 에 의하여 초현실수의 덧셈 $+$ 과 곱셈 $\cdot$ 은 아벨군을 이룬다. 이로써 환의 조건 1), 2) 가 성립한다. ▲ 

    [정리 28](#d5f07d137) 에 의하여 환의 조건 3) 이 성립한다. ■ 

- 초현실수 곱셈 $(\mathbf{No} \setminus  \{0\} , \times )$ 이 아벨군을 이룬다는 것은 $(\R, +)$ 와 대수적으로 동일한 성질을 띈다는 것이다. 

# 무한, 그리고 그 너머로

!!! def ""

    정수 집합(set of integers) : 정수 집합 $\mathbb{Z}$ 를 다음과 같이 구성한다. 

    $$ 0 \in \mathbb{Z} $$

    $$ n \in \mathbb{Z} \implies \{n|\} \in \mathbb{Z} $$

    $$ n \in \mathbb{Z} \implies \{|n\} \in \mathbb{Z} $$

- 최초로 $0 = \{|\}$ 이 $\mathbb{Z}$ 에 포함되었으니까 $1 = \{0|\}, -1 = \{|0\}$ 도 $\mathbb{Z}$ 에 포함되고, 이를 기반으로 $2 = \{1|\}, -2 = \{|-1\}$ 도 포함된다.

- 이렇게 초현실수로 이루어진 정수 집합 $\mathbb{Z}$ 은 Dali function 에 평범한 정수들을 입력함으로써 평범한 정수 집합 $\mathbb{Z}$ 과 완전히 같아졌다. 

## 무한대의 정의

!!! def "무한대(unlimited)"

    $$ \omega \equiv \{\mathbb{Z} | \} $$

- $\mathbb{Z}$ 또한 명백히 초현실수 집합이므로 이를 기반으로 새로운 초현실수를 생성해낼 수 있다. 

    이렇게 생성된 초현실수 $\omega$ 는 명백히 초현실수이다. left set, right set 모두 초현실수 집합이고, well-formed 이기 때문이다. 

- 이 수는 [정리 5](#c076cc283) 에 의하여 모든 양의 정수보다 크다. 즉, $\omega$ 는 무한대(infinity)이다. 

    일반적인 실수체에는 무한대가 존재하지 않는다. 

- 그 표기법에서 예상할 수 있듯 $\omega$ 는 자연수를 서수로 이해할 때의 $\omega$ 와 매칭된다. 

    서수에 대한 이야기는 여기서 줄이겠지만, 존재하는 모든 서수를 초현실수로 표현할 수 있다는 것만 언급해둔다.

- 물론 $\omega$ 는 다른 표현을 가진다. 

    $$ \begin{equation}\begin{split} \omega & = \{\mathbb{Z} | \}\\ & = \{1,2,3, \dots|\}\\ & = \{2,4,6, \dots|\}\\ & = P\\ \end{split}\end{equation} \tag*{} $$

    $P$ 는 소수의 집합이다. [정리 9](#7817bc62f) 는 $\omega$ 의 left set 중에서 어떤 것보다 더 큰 원소를 남겨두기만 한다면 그 이외의 원소를 제거해도 된다는 것을 알려준다. 이로써 무수히 많은 $\omega$ 표현이 존재함을 알 수 있다. 

!!! def ""

    $$ \omega -1 = \{\mathbb{Z} | \omega \} $$

- 증명

    $$ \begin{equation}\begin{split} \omega - 1& = \omega + (-1) \\ & = \{\mathbb{Z} - 1| \omega -  0 \} \end{split}\end{equation} \tag*{} $$

!!! def ""

    $$ \omega + 1 = \{\omega | \} $$

- 증명 

    $$ \begin{equation}\begin{split} \omega + 1 & = \{\mathbb{Z} + 1, \omega + 0 | \}\\ & = \{\mathbb{Z} , \omega | \} \\ & = \{\omega | \} \end{split}\end{equation} \tag*{} $$

    (마지막 연산은 $\omega$ 가 모든 정수보다 크기 때문에 [따름정리 10](#810bebedd) 에 의하여 도출된다.)

!!! def ""

    $$ \omega + 2 = \{\omega + 1 | \} $$

    $$ \omega + 3 = \{\omega + 2 | \} $$

    $$ \omega - 2 = \{\mathbb{Z}  | \omega -1 \} $$

    $$ \omega - 3 = \{\mathbb{Z}  | \omega -2 \} $$

    $$ \omega + \omega = \{\omega + \mathbb{Z} | \} $$

- 증명 

    $\omega ,\omega + 1, \omega + 2, \omega - 1, \omega -2$ 의 정의로부터 다 쉽게 도출된다. 

!!! def ""

    $$ \omega + \mathbb{Z} = \{\dots, \omega -2, \omega -1, \omega , \omega +1, \omega +2, \dots\} $$

!!! def ""

    $$ 2 \omega = \{\omega + \mathbb{Z} |\} $$

    $$ 3 \omega = \{2\omega + \mathbb{Z} |\} $$

    $$ 4 \omega = \{3\omega + \mathbb{Z} |\} $$

    $$ \omega ^{2} = \{\omega , 2 \omega , 3 \omega , 4 \omega , \dots |\} $$

    $$ \omega ^{\omega } = \{\omega , \omega ^{2} , \omega ^{3} , \omega ^{4} , \dots |\} $$

    $$ \dfrac{\omega }{2} = \{\mathbb{Z} | \omega - \mathbb{Z} \} $$

    $$ \sqrt[]{\omega } = \{\mathbb{Z} | \omega , \dfrac{\omega }{2}, \dfrac{\omega }{3},\dfrac{\omega }{4}, \dots\} $$

    $$ - \omega  = \{| \mathbb{Z} \} $$

- 물론 이 수들도 다른 표현을 가진다. 

- 이로써 우리는 초현실수가 평범한 실수 이외의 수들도 포함할 수 있다는 것을 알았다. 

## 무한소의 정의

!!! def "무한소(infinitesimal)"

    $$ \varepsilon = \bigg \{0 \bigg | 1, \dfrac{1}{2}, \dfrac{1}{4}, \dfrac{1}{8}, \dfrac{1}{16}, \dots \bigg \} $$

- 이 수 또한 well-formed 이므로 엄연히 초현실수이다. 그런데 이 수는 [정리 5](#c076cc283) 에 의하여 $0$ 보다 크면서 모든 양의 분수보다 작다. 

    이러한 수를 무한소(infinitesimal) 라고 한다. 무한소는 보통 $0$ 이 아니면서 모든 양수보다 작은 수로 이해된다. 

    일반적인 실수체에는 무한소가 존재하지 않는다. 

- 이 수의 값을 살펴보면 $\varepsilon = \dfrac{1}{\omega }$ 인데 이로써 우리는 무한대의 역수를 얻는다. 

!!! def ""

    $$ \varepsilon + 1 = \bigg \{1\bigg |2, \dfrac{3}{2}, \dfrac{5}{4}, \dfrac{9}{8}, \dfrac{17}{16}, \dots \bigg \} $$

- 이 수는 $1$ 보다 크고 $1$ 보다 큰 모든 실수보다 작은 수이다. 

!!! def ""

    $$ 2 \varepsilon = \bigg \{\varepsilon \bigg | 1 + \varepsilon , \dfrac{1}{2} + \varepsilon , \dfrac{1}{4} + \varepsilon , \dfrac{1}{8} + \varepsilon , \dfrac{1}{16} + \varepsilon , \dots \bigg \} $$

    $$ \dfrac{\varepsilon }{2} = \{0 | \varepsilon \} $$

    $$ \sqrt[]{\varepsilon }=\bigg  \{\varepsilon ,2 \varepsilon , 3 \varepsilon , 4 \varepsilon , \dots\ \bigg |1, \dfrac{1}{2}, \dfrac{1}{4}, \dfrac{1}{8}, \dfrac{1}{16}, \dots\bigg \} $$

- 이렇게 초현실수가 무한대와 무한소를 포함하므로 초현실수의 미분이나 적분의 유용한 정의를 찾기가 어렵다. 가령 $x, y$ 가 무한소의 일부일 때 $\dfrac{dy}{dx}$ 를 정의하는 것은 쉽지 않다. 

!!! def ""

    dyadic : $j \in \mathbb{Z} , k \in \mathbb{Z} _{\geq 0}$ 에 대하여 $\dfrac{j}{2^k}$ 형태의 분수이다. 

- 우리가 지금까지 만들었던 초현실수 분수는 모두 다 dyadic 의 형태였다. 

## $\dfrac{1}{3}$ 의 정의

!!! def "$\dfrac{1}{3}$ "

    다음을 만족하는 초현실수 $t = \{T_L | T_R\}$ 를 $\dfrac{1}{3}$ 로 정의한다. 

    - $T_L$ 은 $3j < 2 ^{k}$ 를 만족하는 모든 dyadic $\dfrac{j}{2^k}$ 의 집합이다.

    - $T_R$ 은 $3j > 2 ^{k}$ 를 만족하는 모든 dyadic $\dfrac{j}{2^k}$ 의 집합이다.

## $\pi$ 의 정의

!!! def "$\pi$ "

    $\pi$ 보다 작은 모든 dyadic 의 집합 $L$ 과 $\pi$ 보다 큰 모든 dyadic 의 집합 $R$ 에 대하여

    $$\pi = \{L|R\}$$

    이다.

- 전자의 $\pi$ 는 $\R$ 에 있고 후자의 $\pi$ 는 $\mathbf{No}$ 에 있다. 

- $\dfrac{1}{3}$ 과 $\pi$ 같은 실수를 구성하는 방식은 데데킨트 절단을 연상시킨다. 

## 나눗셈의 정의

!!! def "나눗셈"

    초현실수 $x$ 와 조건

    - $0 \in L$

    - $\lambda \in L \implies \dfrac{1 + (X_R-x) \lambda }{X_R} \in L$
    
    - $\lambda \in L \implies \dfrac{1 + (X_L-x) \lambda }{X_L} \in R$
    
    - $\rho \in R \implies \dfrac{1 + (X_L-x) \rho  }{X_L} \in L$
    
    - $\rho \in R \implies \dfrac{1 + (X_R-x) \rho  }{X_R} \in R$
    
    을 만족하는 집합 $L, R$ 에 대하여 

    $$ \dfrac{1}{x} = \{L|R\} $$

    이다. 

- 증명

- 예시 

    초현실수 $\dfrac{1}{5}$ 를 표현해보자. $x = 5$ 에서 $X_L = \{4\}, X_R = \varnothing$ 이므로 
    
    $$ 0 \in L $$

    $$ \lambda \in L \implies \dfrac{1- \lambda }{4} \in R $$

    $$ \rho \in R \implies \dfrac{1- \rho }{4} \in L $$

    이다. 즉, $0 \in L, \dfrac{1}{4} \in R, \dfrac{3}{16} \in L, \dfrac{13}{64} \in R, \dots$ 이다. 

## $\exp (x)$ 

!!! def "$e^{x} $"

    함수 $f(y, n) = 1 + \dfrac{y}{1!} +\dfrac{y ^{2}}{2!} +\dfrac{y ^{3}}{3!} + \dots + \dfrac{y ^{n}}{n!}$ 에 대한

    - $T_1 = \exp (X_L)(f(x-X_L, n)) \quad \text{ n assumes all positive integer values }$

    - $T_2 = \exp (X_R)(f(x-X_R, n)) \quad \text{ n assumes all positive odd integer values }$

    - $T_3 = \dfrac{\exp (X_R)}{f(X_R - x, n)} \quad \text{ n assumes all positive integer values }$

    - $T_4 = \dfrac{\exp (X_L)}{f(X_L - x, n)} \quad \text{ n assumes all positive odd integer values }$

    을 만족하는 집합 $T_1,T_2,T_3,T_4$ 에 대하여

    $$\exp (x) = \{0, T_1, T_2, | T_3, T_4\}$$

    이다. 

- 증명 

# Surcomplex numbers

!!! def ""

    Surcomplex number : 초현실수 $a, b$ 와 $-1$ 의 제곱근 $i$ 에 대하여 $a + bi$ 형태의 수이다.
