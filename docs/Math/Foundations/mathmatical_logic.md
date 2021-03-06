!!! tldr ""

    수리 논리학 : 수학의 기호로 논리학에서 사용하는 명제를 표시하여 연구하는 학문이다.

- 수학에서 집합론과 더불어 수학 기초론을 이룬다. 

-  컴퓨터과학과 밀접하게 연관되어 있기에 컴퓨터공학과에서는 이산수학 교과로 일부를 다룬다.

- 일반적으로 연역논리만을 다루며 그 중에서도 표준논리만을 다룬다. 

- 역사 

    - 라이프니츠가 처음으로 논리학을 수학 기호로 전개할 수 있다는 것을 제안하였다.

    - 이후 부울이 진리값으로 논리를 대수처럼 계산하는 체계를 제시했다.

    - 프레게는 독립적으로 개념 또는 술어 수준에서 명제를 분석하는 양화 논리 체계를 개발했다.

    - 러셀은 모든 수학의 참인 명제를 논리학적 참으로 환원하는 논리주의를 제안했고 이는 수학 전체의 무모순적 공리 체계를 구축하려는 힐베르트의 형식주의에도 영향을 미쳤다.

    - 그러나 괴델의 불완전성 정리로 논리주의 및 형식주의의 초기 형태는 위기를 맞이하였고, 결국 괴델이 ZFC 공리계에서는 연속체 가설이 참이면서 동시에 거짓일 수 있음을 증명하였다.

    - 괴델의 불완전성 정리로 현대 수리논리학이 본격적으로 발전하였다.

!!! tldr ""

    명제와 조건의 부정 : 명제 또는 조건 $p$ 에 대하여 "$p 가 아니다$" 를 $p$ 의 부정이라 하고 기호로 $\sim p$ 로 나타낸다.

- 배중률에 의하여 $p$ 와 $\sim p$ 의 참, 거짓 관계는 항상 서로 반대된다. 

    - 예시 

        명제 $p$ 를 "독도는 한국땅이다." 라고 한다면 $p$ 의 부정 $\sim p$ 는 "독도는 한국땅이 아니다." 이다. 이때 반드시 두 명제 중 어느 것 하나만 참이고 다른 것은 거짓이다. 

- 전체집합을 $U$, 조건 $p$ 의 진리집합을 $P$ 라 하면 $\sim p$ 의 진리집합은 $P^C$ 이다. 

- $\sim(\sim p)$ 의 진리집합은 $(P^C)^C = P$ 이다.

    - 이에 따라 $\sim(\sim p) = p$ 이다.

!!! tldr ""

    명제 $p \to q$ : 명제 "$p 이면 q 이다.$" 를 기호로 $p \to q$ 로 나타낸다.

- $p$ 를 가정(hypothesis), $q$ 를 결론(conclusion)이라 한다. 

- 두 조건 $p, q$ 의 진리집합을 각각 $P, Q$ 라 할 때 다음이 성립한다.

    - $P \subset Q$ 이면 명제 $p \to q$ 는 참이다. : $(P \subset Q) \to (p \to q)$ 

    - $P \not \subset Q$ 이면 명제 $p \to q$ 는 거짓이다. : $(P \not \subset Q) \to \sim(p \to q)$ 

- 즉, 가정(조건 $p$)을 만족하는 모든 대상의 모임(집합)이 결론(조건 $q$)을 만족하는 모든 대상의 모임(집합)의 부분집합이라는 뜻이다. 

    - 다시 말해 가정(조건 $p$)을 만족하는 어떤 대상을 가져오더라도 반드시 결론(조건 $q$)을 만족한다는 것이다. 

    - 그러므로 이러한 명제가 참임을 증명하기 위해서는 가정(조건 $p$)을 만족하는 모든 대상이 항상 결론(조건 $q$)을 만족하는지 보이면 된다. 

- 반면 명제 $p \to q$ 가 거짓임을 보일 때 조건 $p$ 는 만족하지만 조건 $q$ 는 만족하지 않는 대상이 있다는 것을 보이면 된다. 

    - 그러한 대상을 반례(counter example)라고 한다. 

    - 예시 

        "모든 삼각형은 이등변삼각형이다" 라는 명제는 거짓이다. 삼각형이면서 이등변삼각형이 아닌 대상이 존재하기 때문이다. 

- 명제 $p \to q$ 가 참일 때 이것을 $p \implies q$ 라고 표현한다. 

- 명제 $p \to q$ 가 거짓일 때 이것을 $p \not \implies q$ 라고 표현한다. 

- 예시 

    "$x$ 가 $4$ 의 양의 배수이면 $x$ 는 $2$ 의 양의 배수이다" 라는 명제에서 "$p : x 는 4 의 양의 배수이다.$" 와 "$q : x 는 2 의 양의 배수이다.$" 는 두 조건 $p, q$ 를 추출하자. 그러면 $p, q$ 의 진리집합 $P, Q$ 는 다음과 같다. 

    $$ P = \{4, 8, 12, 16, \dots\} $$

    $$ Q = \{2, 4, 6, 8, 10, \dots\} $$

    이때 $P \subset Q$ 이다. 즉 $4$ 의 양의 배수는 전부 다 $2$ 의 양의 배수이므로 $p \to q$ 는 참이다. 이 예시로부터 명제 $(P \subset Q) \to (p \to q)$ 는 참임을 알 수 있다. 

- 예시 

    "$p : x 는 3 의 양의 배수이다.$" 와 "$q : x 는 6 의 양의 배수이다.$" 는 두 조건 $p, q$ 의 진리집합 $P, Q$ 는 다음과 같다. 

    $$ P = \{3, 6, 9, 12, \dots\} $$

    $$ Q = \{6, 12, 18, 24, \dots\} $$

    이때 $P$ 의 원소 $9$ 가 $Q$ 에 속하지 않으므로 $P \not \subset Q$ 이다. 즉 $3$ 의 양의 배수 중 $6$ 의 양의 배수가 아닌 것이 있으므로 $p \to q$ 는 거짓이다. **이처럼 명제 $p \to q$ 가 거짓임을 보일 때 가정 $p$ 를 만족하지만 결론 $q$ 를 만족하지 않는 예(반례, counter example)가 하나라도 있음을 보이면 된다.**

    이 예시로부터 명제 $(P \not \subset Q) \to \sim(p \to q)$ 는 참임을 알 수 있다.

!!! tldr ""

    명제 $p \to q$ 의 부정 : 명제 $p, q$ 의 진리값에 따른 명제 $p \to q$ 의 진리값은 다음과 같다.

- $p \to q$ 진리표 

    | $p$| $q$ | $p \to q$ |
    |:---:|:---:|:---:|
    | $T$  | $T$  |$T$|
    | $T$  | $F$  |$F$|
    | $F$  | $T$  |$T$|
    | $F$  | $F$  |$T$|

- 위 진리표에서 $p, q$ 가 각각 $T, T$ 이면 명제 $p \to q$ 가 $T$ 이고 $p, q$ 가 $T, F$ 이면 $p \to q$ 가 $F$ 인 것은 직관적으로 자명하지만 $p$ 가 $F$ 일 때 명제가 $T$ 가 되는 것은 직관적이지 않다. 

    - 그러나 논리학의 명제는 정의에 따라 반드시 참($T$)과 거짓($F$) 중 하나의 진리값을 가져야 한다. 그런데 전제($p$) 가 거짓일 경우 근본적으로 전제로부터 결론에 이르는 논증($p \to q$) 의 진리값을 판명할 수 없다. 그렇지만 이런 경우에도 진리값이 존재해야 $p \to q$ 를 명제로 다룰 수 있기 때문에 $p$ 가 $F$ 일 때 $p \to q$ 를 $T$ 로 정의하기로 약속한다. 이와 같은 $T$ 를 공진리(vacuous truth) 또는 항진이라고 한다.

- 집합의 포함관계의 관점에서 살펴보면 전제 $p$ 가 거짓일 때 $p$ 의 진리집합은 $P = \emptyset$ 이다. 따라서 결론 $q$ 의 진리집합 $Q$ 에 상관없이 관계 $P \subset Q$ 가 항상 성립한다. 따라서 가정 $p$ 가 거짓인 명제 $p \to q$ 는 항상 참(공진리)이다. 

- 예시 

    명제 "날씨가 맑으면 현장실습을 간다." 는 명제에서 전제와 결론이 진리값 $T, F$ 들을 가질 때 명제의 참거짓을 판명해보자. 

    - 전제 "날씨가 맑다." 를 $p$ 라고 하고 "현장실습을 간다." 를 $q$ 라고 하면 명제를 $p \to q$ 로 표현할 수 있다. 이때 날씨가 맑은데 현장실습을 나갔다면 $p \to q$ 는 참이다. 반면 날씨가 맑은데도 현장실습을 나가지 않았다면 $p \to q$ 는 자명하게 거짓이다.

    - 그런데 날씨가 맑지 않은 경우에 명제 $p \to q$ 의 참거짓을 어떻게 판명해야 하는가? 솔직히 말해서 이 경우 "날씨가 맑다" 는 전제 $p$ 부터가 거짓이기 때문에 명제 $p \to q$ 는 성립하지 않는다. 따라서 근본적으로 명제 $p \to q$ 의 참거짓을 논할 수 없다.

    - 전제가 거짓일 경우 $p \to q$ 의 참거짓을 밝힐 수 없으므로 결론이 어떻게 도출되든 관계 없다. 그런데 배중률에 따라 모든 명제는 $T$ 또는 $F$ 값을 가져야 한다. 따라서 이 경우 그냥 $p \to q$ 를 참(공진리)이라고 약속한다.

- 하지만 위 예시에서 전제가 거짓인 시점에서 우리가 가진 단서는 $\sim p$ 일 뿐이며 $p \to q$ 를 판명할 논거가 불충분하다. 그래서 엄밀하게는 $p \to q$ 는 결정불가능하다. 이는 형식논리(formal logic)가 배중률(명제는 반드시 참 또는 거짓이다)을 기본원리로 받아들이기 때문에 발생하는 문제다. 

- 이 문제는 브라우어의 직관주의 수학(intuitionistic mathematics) 에서도 비판한다. 직관주의 수학은 수학계에서 비주류이긴 하지만 $T, F$ 진리값을 확장한 다치논리가 발전되면 기존 수학에서 더 발전된 수학이 나올 수도 있을 거라는 주장이 있다.

!!! tldr ""

    조건부 명제의 참, 거짓 : 전체집합 $U$ 에 대하여 조건 $p$ 의 진리집합을 $P$ 라 할 때, 다음이 성립한다.

- 명제 "모든 $x$에 대하여 $p$ 이다." 는 $P=U$ 일 때 참이다. 즉 $p$ 를 참이되게 하는 원소가 모인 진리집합 $P$ 가 전체집합 $U$ 과 동일해야 한다. 

    - 이 명제의 부정은 "어떤 $x$ 에 대하여 $\sim p$ 이다." 이다.

    - 예시 

        명제 "모든 실수에 대하여 $x^2>0$ 이다." 는 "모든" 이라는 조건으로 때문에 $x$ 가 될 수 있는 전체집합의 모든 원소에 대하여 $x^2>0$ 이어야 참이다.

        하지만 실수 집합의 원소 $0$ 는 $x^2>0$ 를 만족하지 않는다. 따라서 이 명제는 거짓이다. 

    - 예시 

        명제 "모든 학생은 거짓말쟁이다." 를 부정하려 한다면 모든 학생 중에 거짓말쟁이가 아닌 학생이 하나라도 있다는 것을 보이면 된다. 즉 "어떤 학생은 거짓말쟁이가 아니다" 가 참이라는 것을 증명하면 된다. 

        이것을 일반화하면 "모든 $x$ 에 대하여 $p$ 이다." 라는 명제의 부정이 "어떤 $x$ 에 대하여 $\sim p$ 이다." 라는 것을 알 수 있다. 

- 명제 "어떤 $x$에 대하여 $p$ 이다." 는 $P\neq \emptyset$ 일 때 참이다. 즉 $p$ 를 참이되게 하는 원소가 모인 진리집합 $P$ 에 최소 $1$ 개 이상의 원소가 있으면 된다. 

    - 이 명제의 부정은 "모든 $x$ 에 대하여 $\sim p$ 이다." 이다.

    - 예시 

        명제 "어떤 실수에 대하여 $x^2>0$ 이다." 는 "어떤" 이라는 조건으로 때문에 $x$ 가 될 수 있는 전체집합 중에서 어느 한 원소만 $x^2>0$ 을 만족하면 참이다.

        실수 집합의 원소 $2$ 는 $x^2>0$ 를 만족한다. 따라서 이 명제는 참이다. 

    - 예시 

        명제 "어떤 학생은 거짓말쟁이다." 를 부정하려 한다면 모든 학생이 거짓말쟁이가 아니라는 것을 보이면 된다. 즉 "모든 학생은 거짓말쟁이가 아니다" 가 참이라는 것을 증명하면 된다. 

        이것을 일반화하면 "어떤 $x$ 에 대하여 $p$ 이다." 라는 명제의 부정이 "모든 $x$ 에 대하여 $\sim p$ 이다." 라는 것을 알 수 있다.

!!! tldr ""

    명제의 역(converse) : 명제 $p \to q$ 에 대하여 $q \to p$ 를 명제의 역이라 한다.

- 어떤 명제 $p$ 와 그것의 역의 진리치는 일정한 관계를 갖지 않는다. 

- 예시 

    '모든 사람은 포유류다' 는 참이지만 그 역인 '포유류는 모두 사람이다' 는 거짓이다. 

    '두 삼각형이 합동이면 대응하는 세 변의 길이가 각각 같다' 는 참이고 그 역인 '대응하는 세 변의 길이가 각각 같으면 두 삼각형은 합동이다' 도 참이다.

!!! tldr ""

    명제의 대우(contraposition) : 명제 $p \to q$ 에 대하여 $\sim q \to \sim p$ 를 명제의 대우라 한다.

- 어떤 명제 $p$ 와 그것의 대우는 항상 똑같은 진리치를 갖는다. 즉 $p$ 가 참이면 그것의 대우도 참이고 거짓이면 그것의 대우도 거짓이다. 다시 말해 명제와 그 대우는 동치이다. 

- $p \implies q$, 즉 명제 $p \to q$ 가 참이면 $P \subset Q$ 이다. 또한 이에 따라 $\sim q \to \sim p$ 이기에 $Q^C \subset P^C$ 도 참이다. 

- $p \not \implies q$, 즉 명제 $p \to q$ 가 거짓이면 $P \not \subset Q$ 이다. 또한 $Q^C \not \subset P^C$ 도 참이며 이에 따라 $\sim q \not \implies \sim p$ 이다. 

- 따라서 명제 $p \to q$ 를 증명할 때 $\sim q \to \sim p$ 를 증명해도 된다. 

- 예시(삼단논법) 

    "참을 깨달은 자는 배움이 있는 자이다. 책임의 소중함을 느끼는 자가 아니라면 겨레를 위해 희생을 각오한 자가 아니다. 진정한 지도자는 겨레를 위해 희생을 각오한 자이다." 로부터 "그러므로 진정한 지도자는 배움이 있는 자이다." 라는 결론이 도출되었다면 보충되어야할 전제가 무엇일까? 

    먼저 전제를 "$a \to b, \sim c \to \sim d, e \to d$" 라는 형식언어로 표현할 수 있고 결론을 $e \to b$ 로 표현할 수 있다. 전제와 결론을 선형적으로 정리하면 $e \to d \to c \dots a \to b$ 를 얻는다. 이것으로부터 명제 $c$ 와 $a$ 가 연결되지 않는다는 것을 알 수 있기 때문에 $1$ 차적으로는 보충되어야 할 전제를 $c \to a$ 라고 추측할 수 있다.

    즉 생략되어 보충되어야 할 전제란 "책임의 소중함을 느끼는 자는 참을 깨달은 자이다" 라고 말할 수 있다.

## 수리논리학의 증명법 및 논증법

!!! tldr ""

    수학에서의 증명 : 증명을 작성할 때 지켜야하는 규칙은 다음과 같다.
    
1. 증명되지 않은 명제를 사용하여 결론을 이끌어내서는 안된다.

    - 논증은 이미 참이라고 알려진 내용을 근거로 주장하는 바를 정립하는 것이기에 참거짓이 밝혀지지 않은 내용을 근거로 결론을 끌어내었다면 결론에 근거가 없는 것과 다름없기 때문이다. 

2. 논증에 쓰는 문장이 옳음을 표현하는 방법은 다음과 같다. 

    - "지금 증명하려는 정리의 가정에 의하여 ..."

    - "공리에 의하여 ..."

    - "앞에 증명된 정리에 의하여 ..."

    - "정의에 의하여 ..."

    - "이 증명중 이미 확립된 앞 단계에 의하여 ..."

    - "논리 규칙에 의하여 ..."

3. (귀류법) 명제 "$p$ 이면 $q$ 이다" 를 증명하기 위해서는 조건 '$q$' 가 성립하지 않으면 '$p$' 또는 '$p$' 로부터 연연되는 사실에 모순이 된다는 점을 보이면 된다.

    - 결론을 부정하는 것으로부터 시작하여 추론 끝에 얻은 명제가 가정과 모순된다는 것을 보이면 처음에 결론을 부정했던 것 또한 거짓임을 보일 수 있다는 것에서 착안한 증명법이다.

    - 이것은 대우명제를 증명하는 것과 같다. 

4. 조건 $p$ 의 부정을 $\sim p$ 로 쓰는데 이때 $\sim(\sim p)$ 는 $p$ 와 같다.

    - 즉, 어떤 조건의 부정을 부정하면 원래의 조건과 같아진다.

5. "$p$ 와 $q$ 가 동시에 성립한다" 는 조건의 부정은 "$p$ 와 $q$ 둘 중 최소한 하나는 성립하지 않는다" 이다. 

    - 예시 

    "내 자동차가 하얗고 튼튼하다" 는 명제를 부정하려면 자동차가 하얗지 않거나 하얗더라도 튼튼하지 않으면 된다. 

6. (한정기호, quantifier) "임의의 $x$ 에 관하여 조건 $p$ 가 성립한다" 의 부정은 "어떤 $x$ 에 대하여 조건 $p$ 가 성립하지 않는다" 또는 "조건 $p$ 를 부정하는 특정한 $x$ 가 존재한다" 이다. 

7. (한정기호, quantifier) "특정한 $x$ 에 대하여 조건 $p$ 가 성립한다" 의 부정은 "임의의 $x$ 에 대하여 조건 $p$ 가 부정된다 " 또는 "조건 $p$ 를 만족하는 $x$ 는 아예 없다" 이다. 

8. (배반공리, law of excluded middle) 임의의 조건 $p$ 가 있다고 하자. 그러면 임의의 대상을 가져오더라도 이 대상은 $p$ 를 만족하든지 $p$ 를 만족하지 않든지, 둘 중 하나만 성립한다.

    - 논리학에서 배중률로 설명되지만 배중률은 논리학계에서 다소 논란이 있다. 그러나 배반공리는 수학에서는 널리 사용된다. 

    - 예시 

        조건 $q_1, q_2, \dots, q_n$ 들이 서로 배반적(mutually exclusive, 이들 중 어느 두 조건도 동시에 만족하는 대상이 있을 수 없음) 이며 동시에 임의의 대상이 이들 조건 중 하나는 만족해야 한다는 완벽성(exhaustiveness) 을 갖추고 있다고 하자.

        이때 "$p$ 를 만족하면서 동시에 $q_k$ 를 만족하는 대상은 없다" 는 명제를 $k=1$ 부터 $k=n-1$ 까지 모두 증명하였다면 결국 "$p$ 이면 $q_n$ 이다" 를 증명하게 된 것이다. 이것을 "proof by cases" 라고 하는데 사실 귀류법을 여러번 사용한 것에 불과하다.

- 위와 같은 수학의 명제를 증명하는 논증에 사용되는 논리 규칙들보다 더 정확하고 자세한 내용을 형식논리학에서 알아볼 수 있다. 

- 정리의 증명에서 용어의 정의를 확실히 이해해야 한다. 왜냐하면 정리의 증명은 사실상 한 정의로부터 다른 정의로 논리적으로 옮겨가는 과정을 모아둔 것이기 때문이다.

!!! tldr ""

    직접증명법 : 명제 $p$ 가 참이라는 가정으로부터 $q$ 가 참이라는 결론에 도달하여 명제 $p \to q$ 가 참임을 증명하는 방법이다.

!!! tldr ""

    간접증명법 : 명제를 증명할 때 직접 증명하지 않고 간접적으로 증명하는 방법이다.

- 대우를 이용한 증명이나 귀류법이 이에 속한다.

!!! tldr ""

    대우를 이용한 증명법(proof by contraposition) : 주어진 명제의 대우가 참임을 보임으로써 그 명제가 참임을 보이는 것이다.

- $p \to q$ 를 증명하기 어려울 때 $\sim q \to \sim p$ 가 참임을 증명함으로써 원래의 명제를 증명하는 것이다.

!!! tldr ""

    귀류법 : 주어진 명제의 결론을 부정한 후 모순이 생기는 것을 보임으로써 결론을 부정하지 않는 명제가 참임을 증명하는 방법이다.

- 어떤 주장에 대해 함의하는 내용을 따라가다보면 모순에 도달한다는 것을 보여서 주장이 잘못된 것임을 보이는 증명법이다. 

- 수학에서도 자주 사용될 뿐아니라 논리학에서도 사용되는 증명법이다. 

    - 일상생활에서도 자주 볼 수 있는데 "당신의 말이 맞다고 칩시다. 그러면 이러이러한 문제가 발생합니다. 그러므로 당신의 주장은 틀렸습니다." 라는 식이다.

- 예시 

    학문의 시작이란 결과(현상, 대상 등)에 원인(근거)이 존재한다는 것이다. 부모에게 부모가 있고 그 부모에게는 또 다시 부모가 있듯이 그 원인에는 그 원인을 낳은 또 다른 원인이 있다. 자연현상에 대한 관찰을 시작으로 이와 같은 역추적 과정을 계속하는 것이 지식 발전의 과정이다. 그런데 부모의 부모를 무한히 거슬러 올라갈 수 없듯이 원인의 원인을 역추적 해나가다보면 언젠가 더 이상의 근거에 의지하여 존재하지 않고 스스로 존재하는 최초의 원인(혹은 사실, 대상)이 발견될 것이다. 논리적 사고와 추론을 통하여 진리를 탐구하고자 했던 데카르트는 귀류법으로 그러한 최초의 원인에 대한 자신의 결론에 도달하였다. 다음은 데카르트가 귀류법으로 최초의 원인에 대한 결론을 내리는 논증이다.

    "나는 생각한다."를 부정해보자. 그렇다면 "나는 생각하지 않는다." 이다. 그런데 이 순간 나는 "나는 생각하지 않는다." 라고 생각하는 셈이다. 이것은 모순이다. 따라서 "나는 생각한다." 를 부정할 수 없다. 그렇다면 생각을 하는 나의 존재 또한 부정할 수 없다. 그러므로 "나는 생각한다. 고로 존재한다(I think, therefore I am)." 는 더 이상 의심할 수 없고 부정할 수 없는 최초의 지식이다. 이것을 사유의 제 $1$ 원리로 삼고 모든 지식이 쌓일 토대로 삼아야 한다. 

- 예시 

    소수(prime number) 의 개수가 유한하다고 하자. 그러면 유한개의 소수를 작은 순서로 $p_1, p_2, \dots, p_n$ 로 나타낼 수 있다. 이제 다음과 같이 정의된 수 $P$ 를 생각하자.

    $$P = \prod_{k=1}^{n}p_k + 1$$

    $P$ 는 $p_1$ 로 나누었을 때 $1$ 이 남는다. 

    $P$ 는 $p_2$ 로 나누었을 때 $1$ 이 남는다. 

    $\vdots$

    $P$ 는 $p_n$ 로 나누었을 때 $1$ 이 남는다. 

    즉, $P$ 는 어떤 소수로 나누어도 나누어 떨어지지 않는다. 따라서 $P$ 는 모든 소수와 서로소이다. 이에 따라 $P$ 는 $p_1, p_2, \dots, p_n$ 와는 다른 소수라는 것을 알 수 있다. 그런데 이 결론은 소수가 유한개로써 $p_1, p_2, \dots, p_n$ 만 존재한다는 전제와 모순된다. 따라서 소수는 무한히 많다.

!!! tldr ""

    수학적 귀납법(mathematical induction) : 자연수 $k$ 에 대한 명제 $p(k)$ 이 $n$ 번째 명제를 표시한다고 하자. 이때 모든 자연수 $n$ 에 대하여 아래 두 조건
    
      1. $n=1$ 일 때 명제 $p(1)$ 이 성립한다. 
    
      2. $n=k-1$ 일 때 명제 $p(k-1)$ 이 성립하면 $n=k$ 일 때도 명제 $p(k)$ 이 성립한다.
    
    이 참이면, 명제 $p(n)$ 이 임의의 자연수 $n$ 에 대하여 참이다.

- 즉 수학적 귀납법도 "$p 이면 q 이다(p \to q)$" 형태이다. 

- 수학적 귀납법의 증명(귀류법)

    귀류법으로 증명하기 위하여 결론을 부정하여 명제 $p(k)$ 를 거짓이 되게 하는 자연수 $k$ 가 존재한다고 가정하자. 그리고 이 가정에 따라 생성된 집합 $A$ 를 

    $$ A = \{자연수 m | p(m) 은 거짓명제\} $$

    로 정의하자. 가정에 따라 $A$ 는 공집합이 아니다.

    $A$ 에 속한 원소 중 가장 작은 자연수를 $n$ 이라고 하자. 그렇다면 조건 1. 때문에 $n \geq 2$ 이다. 한편 $n-1$ 도 자연수인데 이것은 $n$ 보다 작기에 $A$ 에 속하지 않는다. 이에 따라 명제 $p(n-1)$ 는 참이다. 

    그런데 조건 2. 로 때문에 명제 $p(n-1)$ 이 참이면 $p(n)$ 도 참이다. $p(n)$ 은 배중률로 인하여 반드시 참이거나 거짓이어야 하는데 참이면서 동시에 거짓이게 되었다. 따라서 이것은 공리에 위배되며 그 원인은 $p(n)$ 이 거짓이라는 가정 $n \in A$ 때문이다.

    $\therefore$ 처음의 가정은 거짓이며 이로써 수학적 귀납법의 거짓을 주장하는 명제의 거짓이 증명되었다. 

- 일반적인 수학에서의 증명은 연역 논리에 의존한다. 그러나 귀납 논리로 수학 명제를 증명할 때도 있다. 귀납법이란 실존하는 모든 대상에 대하여 어떤 주장에 대한 반례가 없음을 보이는 것으로 자신의 주장이 참임을 증명하는 것이라고 이미 언급했다. 현실 세상에서는 이처럼 존재하는 모든 대상을 검증하여 주장하는 바가 참이라는 것을 증명할 수 없었다. 그러나 수학에서는 위와 같이 **이전의 대상이 참이라면 그 다음 대상도 참이라는 관계를 증명하는 것으로 무한히 많은 대상일지라도 모두 참이라는 것을 증명할 수 있다.**

!!! tldr ""

    충분조건(sufficiency) : $p \implies q$ 이면 $p$ 는 $q$ 이기 위한 충분조건이다.

- $P \subset Q$ 이면 $p \implies q$ 이기 때문에 $p$ 를 참이 되게하는 진리집합 $P$ 가 $q$ 를 참이 되게하는 진리집합 $Q$ 에 속한다. 따라서 $p$ 가 참이라는 것이 보장되면 진리집합이 $q$ 를 참이 되게하는 진리집합에 포함되므로 $q$ 도 참이라는 것이 충분히 보장된다. 쉽게 말해 $p \implies q$ 는 "$p$ 이면 무조건 $q$ 이다" 라는 것이기 때문에 $p$ 는 $q$ 가 참이 되기 위한 충분한 조건을 이미 충족한다. 따라서 $p \implies q$ 일 때, $p$ 를 $q$ 이기 위한 충분조건이라고 한다. 

- 예시 

    명제 $p:x^2-4=0$ 는 명제 $q:x^3-4x=0$ 에 대하여 어떤 조건인가?

    $p : x^2-4=0 = (x+2)(x-2)$ 에서 $x=-2$ 또는 $x=2$ 이므로 $P=\{-2, 2\}$ 이다. 

    한편 $q : x^3-4x=0 = x(x+2)(x-2)$ 에서 $x=0$ 또는 $x=-2$ 또는 $x=2$ 이므로 $Q=\{0, -2, 2\}$ 이다. 

    이때 각 명제의 진리집합 $P, Q$ 는 $P \subset Q$ 의 관계를 갖는다. 따라서 $p$ 는 $q$ 이기 위한 충분조건이다.

!!! tldr ""

    필요조건(necessity) : $p \implies q$ 이면 $q$ 는 $p$ 이기 위한 필요조건이다.

- $P \subset Q$ 이면 $p \implies q$ 이기 때문에 $p$ 를 참이 되게하는 진리집합 $P$ 가 $q$ 를 참이 되게하는 진리집합 $Q$ 에 속한다. 이는 $q$ 를 참이 되게 하는 진리집합이 반드시 $p$ 를 참이 되게 한다는 보장은 없지만 $p$ 를 참이 되게 하기 위해서는 필요하기는 한 조건임을 의미한다. 따라서 $q$ 를 $p$ 가 참이기 위한 필요조건이라 한다. (충분한 조건, 즉 충분 조건은 아닌 것이 $q$ 의 진리집합의 모든 원소가 $p$ 를 항상 만족하지 않기 때문이다.)

- 예시 

    두 조건 $p, q$ 의 진리집합을 $P, Q$ 가 다음과 같이 정의되었을 때 명제 $p$ 는 명제 $q$ 에 대하여 어떤 조건일까? 

    $$P=\{x|x<3\}, Q=\{x|-2 \leq x \leq 2\}$$

    두 진리집합 $P, Q$ 는 $Q \subset P$ 의 관계를 갖는다. 따라서 $p$ 는 $q$ 이기 위한 필요조건이다.

!!! tldr ""

    필요충분조건(necessity and sufficiency) : $p \implies q$ 이고 $q \implies p$ 이면 $p$ 는 $q$ 이기 위한 필요충분조건이다.

- 필요충분조건을 $p \iff q$ 라고 나타낸다. 

    - 또한 "if and only if" 로도 나타내고 줄임말로 "$iff$" 로 나타낸다.

- 필요충분조건은 두 명제의 진리집합이 동일함을 뜻하고 두 명제가 동치라는 것을 뜻한다. 

- 즉, $P \subset Q$ 이면 $p \implies q$ 이고 $Q \subset P$ 이면 $q \implies p$ 이므로 $P=Q$ 이며 이것을 $p \iff q$ 라고 표현한다.

!!! tldr ""

    수리 논리학의 논증 : 수리 논리학의 논증이란 특정한 명제 집합(전제)과 특정한 문장(결론)으로 구성된다.

- 문자의 조합으로 이루어진 문장은 무수히 많고 그 문장으로 이루어진 논증 또한 무수히 많지만, 그 무한 논증 집합 중 일부만이 타당한 논증이다. 

    - **만약 무수히 많은 문장 경우의 수를 기계학습으로 학습할 수 있다면 타당한 논증을 컴퓨터에게 가르칠 수 있을까?**

- 또한 그 타당성을 크게 의미론적 방식, 구문론적 방식으로 정의한다.

!!! tldr ""

    의미론적으로 타당한 논증 : 전제들이 모두 참일 경우 결론이 반드시 참인 논증이다.

- 전제들이 모두 참인데도 결론이 거짓이면 그 논증은 부당한 논증이다. 

- 전제들이 모두 참이면서 결론이 참이라고 해서 논증이 타당한 것이 아니다. 전제가 모두 참이라면 결론이 반드시 참이어야 그 논증은 타당하다. 

    - 예시 (타당한 논증 )

        만약 소크라테스가 철학자라면, 소크라테스는 지혜를 사랑한다. 소크라테스는 철학자다. 따라서 소크라테스는 지혜를 사랑한다.

    - 예시 (타당하지 않는 논증 )

        소크라테스는 철학자다. 고래는 포유류다. 따라서 박지성은 축구선수다.

- 논증이 의미론적으로 타당할 경우 그 결론은 전제의 논리적 귀결이이라 한다. 

    - 결론 $\phi$ 가 전제의 전체집합 $\Gamma$ 의 논리적 귀결이라는 것을 $\Gamma \models \phi$ 으로 표현한다. 

    - 전체집합 $\Gamma$ 가 공집합이면 논리적 귀결 $\phi$ 는 논리적 참이고 $\models \phi$ 로 표현한다.

!!! tldr ""

    구문론적으로 타당한 논증 : 전제나 결론의 참, 거짓을 따지지 않고 오직 주어진 추론규칙에 의거하여 전제들로부터 결론이 도출가능 또는 증명가능하면 타당하다고 보는 논증이다.

- 전제나 결론의 참, 거짓을 모른채로 논증의 타당성을 따진다.

- 결론 $\phi$ 가 집합 $\Gamma$ 로부터 도출가능하면 $\Gamma \vdash \phi$ 로 표현한다. 

- 증명 

    공리라고 불리는 일련의 명제와 전제의 전체 집합 $\Gamma$ 를 주어진 추론규칙을 적용하여 결론을 도출하는 연속된 문장들이다. 

## 메타 정리

!!! tldr ""

    메타 정리 : 논리 체계 내부에 대한 정리가 아닌 논리 체계 그 자체를 다루는 정리이다.

- 메타 정리들은 명제 논리와 1차 술어논리에서만 동시에 성립하며 2차 이상 논리체계에서는 동시에 성립할 수 없다.

- 건전성, 완전성, 일관성(무모순성)이 동시에 성립하는 1차 술어논리는 가장 기초적인 논리 체계가 된다고 할 수 있다.

    - 따라서 지금까지도 수학의 기초로 활용된다.

!!! tldr ""

    메타 정리의 성질

- 논리 체계의 건전성 : 문장집합 $\Gamma$ 로부터 명제 $\phi$ 가 도출되면 문장 $\phi$ 가 명제집합 $\Gamma$ 의 귀결이다.

    $$ \Gamma \vdash \phi \implies \Gamma \models \phi$$

- 논리 체계의 완전성 : 문장 $\phi$ 가 명제집합 $\Gamma$ 의 귀결이면 문장집합 $\Gamma$ 로부터 명제 $\phi$ 가 도출된다는 것이다.

    $$ \Gamma \models \phi\implies \Gamma \vdash \phi $$

    - 건정성과 완전성은 역 관계이며, 괴델의 완전성 정리에 의해 명제 논리와 1차 술어논리 체계에서 동치라는 것이 증명되었다. 

    - 명제 논리와 1차 술어논리에서 모형이론적 진리와 증명이론적 진리는 서로 같다는 것이다. 즉 타당한 문장은 증명될 수 있고 증명될 수 있는 명제는 타당하다. 

    $$ \Gamma \models \phi\iff  \Gamma \vdash \phi $$

- 논리 체계의 일관성(무모순성) : 공집합으로부터 모순이 도출되지 않는다.

    $$\emptyset \not\vdash \perp $$

    - 또한 표준 명제 논리와 1차 술어논리 체계는 일관적이고, 괴델의 완전성 정리에서 1차 논리가 일관성이 성립한다는 것이 증명되었다. 

- 콤팩트성 : 어떤 명제 $\phi$ 가 명제 집합 $\Gamma$ 의 귀결일 때, $\Delta \models \phi$ 를 만족시키는 $\Gamma$ 의 유한 부분집합 $\Delta$ 가 존재한다. 

    - 어떤 집합이 닫혀 있는 성질이라 할 수 있다. 

    - 콤팩트성 정리에 따르면 논리 체계의 일관성은 콤팩트성과 동치이다. 콤팩트성이 성립하는 논리체계는 일관성(무모순성)이 성립하고 일관성(무모순성)이 성립하는 논리체계는 콤팩트성이 성립한다. 

- 뢰벤하임-스콜렘 정리

  **구체화 필요**

- 괴델의 불완전성 정리 

  **구체화 필요**

!!! tldr ""

    명제 논리 
    
    **구체화 필요**



!!! tldr ""

    양화 논리

- 1차 술어논리

**구체화 필요**

!!! tldr ""

    양상 논리
    
    **구체화 필요**



!!! tldr ""

    수리 논리학의 기호 
    
    | 언어| 기호 |
    |:---:|:---:|
    | 그리고 | $\land$|
    | 또는 | $\lor$|
    | $A$ 이면 $B$ 이다. | $A \subset B, A \to B$|
    | 아니다 | $\neg$|



!!! tldr ""

    추론 형식 
    
    | 형식 | 구조 | 추론 |
    |:---:|:---:|:---:|
    | F1 | 전가언 3단논법 | 간접추론|
    | F2 | 혼합가언 전건긍정 3단논법(대전제 가언, 소전제 정언 명제) | 간접추론|
    | F3 | 혼합가언 후건부정 3단논법(대전제 가언, 소전에 정언) | 간접추론|
    | F4 | 혼합선언 부정3단논법(대전제 선언 명제, 소전제 정언)| 간접추론|
    | F5 | 드모르간의 법칙 | 직접추론|
    | F6 | 연언 명제 | 직접추론|
    | F7 | 연언 명제의 분리 | 직접추론|
    | F8 | 이중부정 | 직접추론|



!!! tldr ""

    고전 논리학의 자연언어를 수학적 기호로 추상화시킨 예시

- 전제1 - 만약 A가 B라면 C가 아니거나 D이다.

    $B \supset (-C \lor D)$

- 전제2 -	A는 E이거나 또는 C이다.

    $E \land C$

- 전제3 -	A는 B이다.

    $B$

- 전제4 -	A는 D가 아니다.

    $-D$

- 결론1 -	A는 C가 아니다.

    $-C$

- 결론2 -	A는 E이다.

    $E$

- 이처럼 수리논리학은 자연언어를 수학 기호로 격하한 다음 타당성 검증에 사용되는 추론 형식을 적용하여 연역 논증을 자동으로 전제들로부터 참과 거짓인 결론을 이끌어낼 수 있다는 가능성을 보여준다.

