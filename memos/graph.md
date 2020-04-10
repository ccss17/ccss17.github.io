# [ccss17.github.io](https://ccss17.github.io)

# 도형의 방정식 

- 함수의 그래프 : $x$ 축을 독립변수로 하고 각각의 $x$값에 대응하는 $y$ 값의 모든 순서쌍 $(x, y)$ 을 좌표평면에서 시각적으로 나타낸 것이다. 

  - 함수 $f$ 의 그래프 $G$ 는 엄밀하게 다음과 같이 정의된다.
  
    - 함수 $f: X \to Y$ 에서 정의역 $X$ 의 원소 $x$ 와 이에 대응하는 함숫값 $f(x)$ 의 순서쌍 전체의 집합 $G = \{(x, f(x)) | x \in X\}$ 를 함수 $f$ 의 그래프 $G$ 라 한다. 

  - 예시

    - 다음은 함수 $f(x) = 2x+1$ 의 그래프를 $\Re^2$(2차원 좌표계) 에서 시각화한 것이다. 

      ![desmos-graph](https://user-images.githubusercontent.com/16812446/75017426-52f5e980-54d0-11ea-9e69-e8a8e3df403d.png)

- 직선의 방정식 : 직선의 방정식은 좌표평면에서 두 점을 곧게 이은 선분을 양 끝으로 무한히 늘린 직선을 나타내는 함수이다. 

  - 직선은 두 점으로 유일하게 특정될 뿐 아니라 한 점과 기울기로도 유일하게 특정되므로 직선의 방정식은 다음과 같이 정의된다. 

    - 한 점과 기울기로 정의 : 좌표평면에 한 점 $A(x_1, y_1)$ 과 기울기 $m$ 이 주어졌다고 하자. 이때 기울기는 직선 위의 어떤 점으로 구해도 일정하므로 직선 위의 임의의 점 $P(x, y)$ 에 대하여 $m = \frac{y-y_1}{x-x_1}$ 이 성립한다. 따라서 직선의 방정식은 $y = mx - mx_1 + y_1$ 으로써 $f(x) = y = mx + a$ 의 꼴이 된다.

    - 두 점으로 정의 : 좌표평면에 두 점 $A(x_1, y_1)$ 과 $B(x_2, y_2)$ 이 주어졌다고 하자. 이때 기울기는 $m = \frac{y_2-y_1}{x_2-x_1}$ 이다. 따라서 다시 한 점과 기울기로 직선을 특정하는 정의로 회귀하여 임의의 점 $P(x, y)$ 에 대하여 직선의 방정식은 $y = mx + a$ 이다. 

      - 두 점이 $y_1 = y_2$ 의 관계를 가질 경우 : 기울기 $m$ 이 $0$ 가 되어 직선의 방정식이 $y = a$ 가 된다.

      - 두 점이 $x_1 = x_2$ 의 관계를 가질 경우 : 기울기를 정의할 수 없지만 이러한 직선 위의 모든 점은 같은 $x$ 좌표를 갖는다는 유일한 성질을 사용하여 직선의 방정식을 $x=x_1$ 로 정의한다. 

  - 이로부터 모든 직선의 방정식을 대표하는 일차방정식 $ax + by + c = 0$ 를 얻는다. (단, $a \neq 0 또는 b \neq 0$)

- 원의 방정식 : 중심이 $C(a, b)$ 이고 반지름의 길이가 $r(r>0)$ 인 원의 방정식은 $(x-a)^2 + (y-b)^2 = r^2$ 이다. 

  - 원이란 중심을 기준으로 일정한 거리에 있는 점들의 모임이다. 이 정의에 따라 중심 $C(a, b)$ 로부터 $r$ 만큼 떨어진 임의의 점 $(x, y)$ 을 피타고라스의 정리를 통하여 $(x-a)^2 + (y-b)^2 = r^2$ 로 표현할 수 있다. 

- 점의 평행이동 : 좌표평면 위의 한 점 $P(x, y)$ 를 $x$ 축의 방향으로 $a$ 만큼, $y$ 축의 방향으로 $b$ 만큼 평행이동한 점 $Q$ 의 좌표는 $Q(x+a, y+b)$ 이다. 

- 도형의 평행이동 : 방정식 $f(x, y) = 0$ 이 나타내는 도형을 $x$ 축의 방향으로 $a$ 만큼, $y$ 축의 방향으로 $b$ 만큼 평행이동한 도형의 방정식은 $f(x-a, y-b) = 0$ 이다. 

  - 도형 위의 임의의 점을 $P(x, y)$ 라 할 때 도형을 $x$ 축의 방향으로 $a$ 만큼, $y$ 축의 방향으로 $b$ 만큼 평행이동하면 도형 위의 임의의 점 $P$ 도 평행이동한다. 그 결과 점 $P$ 가 $P'(X, Y)$ 가 되었다고 하면 다음이 성립한다. 

    $$ X = x+a $$

    $$ Y = y+b $$
  
    이때 $x, y$ 는 도형의 방정식 $f(x, y) = 0$ 을 만족하는 미지수이므로 $x = X-a, y = Y-b$ 를 도형의 방정식에 대입하면 $f(X-a, Y-b) = 0$ 이 된다. 그런데 이것은 임의의 점 $P'(X, Y)$ 가 $f(X-a, Y-b) = 0$ 를 항상 만족하는 것을 의미하기 때문에 이 방정식이 평행이동한 도형의 방정식이 된다. 

    한편 도형의 방정식을 일반적으로 $x, y$ 를 통하여 나타내기 때문에 $X, Y$ 를 $x, y$ 를 고쳐 최종적으로 평행이동한 도형의 방정식 $f(x-a, y-b)=0$ 를 얻는다. 

- 대칭 : 중심선을 기준으로 양 측이 동일한 대상이다. 
  
- 점의 대칭이동 : 좌표평면 위의 임의의 한 점 $(x, y)$ 를 대칭이동한 결과는 다음과 같다. 

  - 원점에 대하여 대칭이동한 점의 좌표 : $(-x, -y)$

  - $x$축에 대하여 대칭이동한 점의 좌표 : $(x, -y)$

  - $y$축에 대하여 대칭이동한 점의 좌표 : $(-x, y)$

  - 직선 $y=x$에 대하여 대칭이동한 점의 좌표 : $(y, x)$

- 도형의 대칭이동 : 도형의 방정식 $f(x, y) = 0$ 이 나타내는 도형을 대칭이동한 결과는 다음과 같다. 

  - 원점에 대하여 대칭이동한 도형의 방정식 : $f(-x, -y)=0$

  - $x$축에 대하여 대칭이동한 도형의 방정식 : $f(x, -y)=0$

  - $y$축에 대하여 대칭이동한 도형의 방정식 : $f(-x, y)=0$

  - 직선 $y=x$에 대하여 대칭이동한 도형의 방정식 : $f(y, x)=0$

# 여러가지 함수 

- 항등함수 : 함수 $f: X \to Y$ 에서 정의역 $X$ 의 각 원소가 자기 자신으로 대응되는 함수를 항등함수라 한다.

  - 즉 $f: X \to Y, x \mapsto x$ 인 함수 $f(x) = x$ 를 항등함수라 한다.

  - 예시 

    - 파이썬 프로그래밍 언어로 정의된 함수 `def f(x): return x` 는 항등함수이다. 

- 상수함수 : 함수 $f: X \to Y$ 에서 정의역 $X$ 의 모든 원소가 공역의 단 하나의 원소로 대응되는 함수, 즉 $f(x) = c$ ($c$ 는 상수) 인 함수 $f$ 를 상수함수라 한다. 

  - 예시 
  
    $f(x) = 5$

- 합성함수(composite function) : 두 함수 $f: X \to Y, g: Y \to Z$ 가 주어졌을 때, 두 함수 $f$ 와 $g$ 를 통하여 집합 $X$ 의 임의의 원소 $x$ 에 집합 $Z$ 의 원소 $g(f(x))$ 를 대응시킨 새로운 함수를 $f$ 와 $g$ 의 합성함수라 한다. 

  - 합성함수를 기호로 $g \circ f: X \to Z$ 로 표현한다.

  - $X$ 의 임의의 원소 $x$ 에 대하여 $(g \circ f)(x) = g(f(x))$ 이 성립한다. 

  - 일반적인 경우에 두 함수 $f, g$ 로 이룰 수 있는 합성함수는 교환법칙이 성립하지 않는다.
  
    - 즉, $g \circ f \neq f \circ g$ 이다. 

  - 일반적인 경우에 세 함수 $f, g, h$ 로 이룰 수 있는 합성함수는 결합법칙이 성립한다. 
  
    - 즉, $(h \circ g) \circ f = h \circ (g \circ f)$ 이다. 

  - 함수가 두 자연대상의 관계를 추상화하여 수학적 형식언어로 명확하게 표현할 수 있었다. 즉 단순한 "원인에 대한 결과" 라는 인과관계를 표현할 수 있었다. 한편 합성함수는 셋 이상의 자연 대상의 복합관계를 표현할 수 있게 해준다. 즉 "원인에 대한 결과, 그리고 그 결과로부터 영향을 받아 발생한 또 다른 현상" 과 같은 복잡한 인과관계를 표현할 수 있다. 

    - **뉴런이 서로에게 미치는 영향을 합성합수로 효과적으로 표현할 수 있어서 인간의 뇌를 구성하는 뉴런의 네트워크를 함수로 표현할 수 있다. 수학의 형식언어로 표현된 것은 코드로 쉽게 변환할 수 있기에 인간의 뇌가 이루는 지능을 합성함수를 통하여 자동화할 수 있는 가능성이 있다.**
  
  - 예시 
    
    거시경제학은 통화정책에 관하여 "통화공급량이 증가하면 국민소득이 증가한다." 라고 말한다. 이 명제를 $p \to q$ 라고 표현하고 $p$ 를 참이되게 하는 진리집합과 $q$ 를 참이되게 하는 진리집합을 각각 $P, Q$ 라 하자. 그리고 $P$ 의 원소 $x$ 가 $Q$ 의 원소 $y$ 로 대응되는 이항관계를 함수 $f$ 라 하고 $f: P \to Q, x \mapsto y$ 로 표현한다. 즉 "통화공급량의 증가" 와 "국민소득 증가" 라는 자연대상 사이의 관계를 추상화하여 함수라는 수학적 형식 언어로 격하시킨 것이다. 

    그런데 경제학자들은 함수 $f$ 를 좀 더 세부적으로 분석하여 함수 $f$ 가 내부적으로 더 작은 함수들의 복합관계로 이루어졌다는 것을 밝혀내었다. 즉, 경제학자들은 "통화공급량이 증가하면 이자율이 하락하고 이자율이 하락하면 기업의 투자가 증가하고 기업의 투자가 증가하면 총수요가 증가하며 총수요가 증가하면 결과적으로 국민소득이 증가한다." 라는 것을 밝혀내었다. 

    "통화공급량이 증가하면 이자율이 하락한다" 는 명제를 함수 $f_1: X_1 \to X_2, x_1 \mapsto x_2$ 로 나타내자. 
    
    "이자율이 하락하면 기업의 투자가 증가한다" 는 명제를 함수 $f_2: X_2 \to X_3, x_2 \mapsto x_3$ 로 나타내자. 
    
    "기업의 투자가 증가하면 총수요가 증가한다" 는 명제를 함수 $f_3: X_3 \to X_4, x_3 \mapsto x_4$ 로 나타내자. 
    
    "총수요가 증가하면 국민소득이 증가한다" 는 명제를 함수 $f_4: X_4 \to X_5, x_4 \mapsto x_5$ 로 나타내자. 

    그러면 결과적으로 함수 $f$ 는 $f=f_4 \circ f_3 \circ f_2 \circ f_1$ 이라는 합성함수였음을 알 수 있다. 또한 이 시점에서 합성함수 $f$ 를 구성하고 있는 함수들 $f_n$ 들 또한 더 세부적인 함수로 나뉘어질 수도 있다는 가능성을 볼 수 있다.
    
    합성함수란 이처럼 수로 표현할 수 있는 셋 이상의 임의의 자연대상들의 복합적 인과관계를 수학적 추상 대상물로 격하시킬 수 있게 해주는 효과적인 도구이다. 
  
  - 예시 

    세 함수 $f(x) = 2x, g(x) = x+1, h(x) = x^2$ 로 합성함수와 교환법칙과 결합법칙에 관하여 실험해보자. 

    - 교환법칙 실험 

      $(g \circ f)(x) = g(f(x)) = g(2x) = 2x + 1$ 인데 비해
      
      $(f \circ g)(x) = f(g(x)) = f(x+1)=2(x+1) = 2x+2$ 이다. 
      
      따라서 교환법칙은 성립하지 않는다. 

    - 결합법칙 실험 

      $(h \circ (g \circ f))(x) = h((g \circ f)(x)) = h(2x+1) = (2x+1)^2$ 이다.
      
      그런데 $((h \circ g) \circ f)(x) = (h \circ g)(f(x)) = (h \circ g)(2x) = (2x+1)^2$ 이다.

      $\because (h \circ g)(x) = h(g(x)) = h(x+1) = (x+1)^2$
      
      따라서 결합법칙이 성립한다. 

- 역함수(inverse function) : 함수 $f: X \to Y$ 가 일대일대응이면 집합 $Y$ 의 임의의 원소 $y$ 에 $f(x) = y$ 인 집합 $X$ 의 원소 $x$ 를 대응시킨 함수 $f^{-1}: Y \to X$ 이다.

  - 함수 $f$ 의 역함수를 $f^{-1}$ 로 표현한다. 

  - 역함수에 관한 연구는 자연대상의 원인, 뿌리에 관한 역추적(궁극적으로는 모든 것의 토대를 향한 역추적)과 비슷하다. 자연대상의 원인에 대한 의문과 분석은 자주 보이는 사유의 방식 중 하나이고 이 사유의 방식에 해당하는 수학 대상물이 역함수이다.

    - "주가가 폭등한 나라는 하나같이 실물경기가 불안하다." 는 명제의 원인을 역추적하면 "일정 수익을 올리면 털고 떠나는 단기자금이 하루에도 수십조 원씩 초 단위로 세계 주식시장을 넘나든다." 는 명제를 밝힐 수 있다. 

  - 역함수로부터 다음의 관계가 발견되었다. 

    - $y=f(x) \Leftrightarrow x=f^{-1}(y)$

    - $(f^{-1})^{-1} = f$

    - $(g\circ f)^{-1} = f^{-1} \circ g ^{-1}$

    - $f ^{-1} \circ f = I_X$

    - $f \circ f ^{-1} = I_Y$

      - 집합 $X$ 에서의 항등함수를 $I_X$ 로, 집합 $Y$ 에서의 항등함수를 $I_Y$ 로 표기한다. 
    
    - 함수 $f: \Re \to \Re$ 에 대하여 $y=f(x)$ 의 그래프와 그 역함수 $y = f ^{-1}(x)$ 의 그래프는 직선 $y=x$ 에 대하여 서로 대칭이다.

      - $y=f(x)$ 그래프에서 $y=f ^{-1}(x)$ 를 구하기 위해서 $y$ 축을 정의역으로 취급하고 $x$ 축을 공역으로 취급하기 때문이다. 
  
  - 역함수 구하기 : 함수 $y = f(x)$ 의 역함수는 다음과 같이 구한다.

    1. $y=f(x)$ 를 $x$ 에 대하여 풀어 $x=f ^{-1}(y)$ 를 얻는다. 

    2. $x=f ^{-1}(y)$ 에서 $x$ 와 $y$ 를 서로 바꿔서 $y=f ^{-1}(x)$ 를 얻는다. 
  
  - 예시 

    - 함수 $f(x) = y = 3x-2$ 의 역함수는 무엇인가. 함수 $f$ 를 $x$ 에 대하여 풀면 $x = \frac{1}{3}y + \frac{2}{3}$ 이므로 역함수는 $f ^{-1}(x) = \frac{1}{3}x+\frac{2}{3}$ 이다. 
  
- 양함수(explicit function) : 하나의 변수 $y$ 가 다른 한 변수 $x$ 에 대한 식으로 제시된 함수일 때, $y$ 를 $x$ 의 양함수라 한다. 

  - 지금까지 살펴본 대부분의 함수가 양함수이다. 

  - 예시 

    $y = x + 3$

- 음함수(implicit function) : $x$ 에 대한 함수 $y$ 가 두 변수 $x, y$ 의 항을 모두 좌변으로 이항하여 $f(x, y) = 0$ 꼴로 주어질 때 $y$ 를 $x$ 의 음함수라 한다. 

  - 양함수는 항상 음함수로 바꿀 수 있다. 

  - 예시 

    $$y = 2x-1 \Rightarrow 2x-y-1 = 0$$
 
  - 예시
 
    $$ x ^{2} + 2xy + y ^{3} = 0 $$
  
  - 예시 

    원의 방정식 $x ^{2}+y ^{2}-1=0$ 같은 음함수는 함수가 아니다. $x$ 의 값에 $2$ 개의 $y$ 값이 대응되어 함수의 정의에 어긋나기 때문이다. 그러나 $x, y$ 값의 범위를 적절히 설정하면 함수가 되기 때문에 음함수도 함수로 쳐준다. 

    가령 이 원의 방정식의 $y$ 값의 범위를 $y \geq 0$ 와 $y \leq 0$ 로 정한다. 그러면 

    $y \geq 0$ 일 때, $y = \sqrt[]{1-x^2}$ 이고 

    $y \leq 0$ 일 때, $y = -\sqrt[]{1-x^2}$ 이다. 

    이것들은 모두 폐구간 $[-1, 1]$ 에서 $x$ 에 대한 함수가 된다. 

- 초월함수(transcendental function) : 계수가 유리수인 다항함수의 사칙연산(거듭제곱근 연산을 포함)을 유한번 이내에서 아무리 적용하여도 만들 수 없는 함수이다. 

  - 예시 

    지수함수 $y = 2 ^{x}$ 는 초월함수이다. 

    로그함수 $y = \log_{4} x$ 는 초월함수이다. 

    삼각함수 $y = \sin x$ 는 초월함수이다. 

## 다항함수 

- 다항함수(polynomial function) : 다음과 같은 꼴의 함수 $f(x)$ 를 $x$ 에 대한 $n$ 차 다항함수(nth degree polynomial function)라 한다. 

  $$ f(x) = \sum_{k=0}^{n}a _{k}x ^{k} = a_nx^n + a _{n-1}x ^{n-1} + a _{n-2}x ^{n-2} + \dots + a _{0}x ^{0}  (단, a _{n} \neq 0, n 은 자연수, a _{i}(0 \leq i \leq n) 는 상수) $$

- 이차함수 

  **구체화 필요**

- 삼차함수 

  **구체화 필요**

- 사차함수 

  **구체화 필요**

- 함수의 최대값 : 어떤 함수의 모든 함수값 중에서 가장 큰 값을 함수의 최대값이라 한다. 

- 함수의 최소값 : 어떤 함수의 모든 함수값 중에서 가장 작은 값을 함수의 최소값이라 한다. 

- 이차함수의 최대값과 최소값

  **구체화 필요**

- 홀함수(기함수, odd function) : 원점에 대하여 대칭인 함수이다.

  - 즉, $f(-x) = -f(x)$ 가 성립하는 함수이다.

  - 단어 그대로 홀수차항만 있는 다항함수가 홀함수이다. 

  - 예시 
  
    - $y = 2x$

    - $y = x^3 - 2x$

      ![desmos-graph(7)](https://user-images.githubusercontent.com/16812446/75110012-f3ccdc00-566b-11ea-801b-97894c2b66c0.png)

- 짝함수(우함수, even function) : $y$ 축에 대하여 대칭인 함수이다.

  - 즉, $f(-x) = f(x)$ 가 성립하는 함수이다. 

  - 단어 그대로 짝수차항만 있는 다항함수가 홀함수이다. 

  - 예시 

    - $y=1$

    - $y=x^2-2$
  
    - $y=x^2-x$ 는 짝수차항과 홀수차항이 모두 있기 때문에 홀함수도 아니고 짝함수도 아니다.

- 매개변수 방정식(parameter equation) : 점 $P(x, y)$ 에 대하여 $x=g(t), y=h(t)$ 이면 함수 $f: \Re \to \Re ^{2}, t \mapsto (x, y)$ 를 생각할 수 있다. 이때 $x=g(t), y=h(t)$ 를 $t$ 를 매개변수로 하는 도형의 매개변수 방정식이라 한다. 

## 유리함수

- 유리함수(rational function) : 함수 $y=f(x)$ 에서 $f(x)$ 가 $x$ 에 대한 유리식일 때, 이 함수를 유리함수라 한다.

  - $f(x)$ 가 $x$ 에 대한 다항식이면 다항함수(polynomial function)라 하는 것이다. 

  - $f(x)$ 가 $x$ 에 대한 분수식이면 분수함수(fractional function)라 하는 것이다. 

    - 다항함수와 분수함수의 차이점은 다항함수의 정의역이 실수 전체 집합인데 비해 분수함수의 정의역은 분모를 $0$ 이 되게 하는 실수를 제외한 실수 전체 집합이라는 것이다. 

- 유리함수의 그래프 : $y = \frac{ax+b}{cx+d}$(단, $ad-bc \neq 0, c \neq 0$)의 그래프는 함수 $y = \frac{k}{x-p}+q$(단, $k \neq 0$) 의 꼴로 변형할 수 있으므로 다음이 성립한다. 

  - $y = \frac{k}{x}$ 의 그래프를 $x$ 축 방향으로 $p$ 만큼, $y$ 축 방향으로 $q$ 만큼 평행이동한 것이다.

  - 정의역 : $\{x|x \neq p 인 실수\}$, 치역 : $\{y|y \neq q 인 실수\}$

  - 점근선은 두 직선 $x=p, y=q$ 이다.

  - 점 $(p, q)$ 에 대하여 대칭이고, 점 $(p, q)$ 를 지나고 기울기가 $1$ 또는 $-1$ 인 두 직선에 대하여도 대칭인 쌍곡선이다. 

  - 예시 
  
    $y = \frac{2}{x}$ 의 그래프이다. $y = \frac{k}{x-p}+q$(단, $k \neq 0$) 의 꼴 유리함수는 이와 같은 꼴에서 $x$ 축으로 $p$ 만큼, $y$ 축으로 $q$ 만큼 평행이동한 것이다.

    ![desmos-graph](https://user-images.githubusercontent.com/16812446/75099281-255d8d00-5603-11ea-98fd-89c968af8de2.png)

## 무리함수

- 무리함수 : 함수 $y=f(x)$ 에서 $f(x)$ 가 $x$ 에 대한 무리식일 때, 이 함수를 무리함수라 한다. 

- 무리함수의 그래프 : $y = \sqrt[]{ax+b}+c$(단, $a \neq 0$) 의 그래프는 $y=\sqrt[]{a(x-p)}+c$ 로 변형할 수 있으므로 다음이 성립한다. 

  - $y=\sqrt[]{ax}$ 의 그래프를 $x$ 축의 방향으로 $p$ 만큼, $y$ 축의 방향으로 $q$ 만큼 평행이동한 것이다.

  - 정의역 : $a>0$ 일 때 $\{x|x \geq p 인 실수\}$, $a<0$ 일 때 $\{x|x \leq p 인 실수\}$

    - 즉, 무리함수의 정의역은 근호 안의 식의 값이 $0$ 또는 양수가 되게 하는 모든 실수 집합이다. 

  - 치역 : $\{y|y \geq q 인 실수\}$

  - 점 $(p,q)$ 가 그래프의 시작점이다. 

  - 예시 
  
    다음은 $y=\sqrt[]{ax}$ 꼴의 무리함수이다. $y=\sqrt[]{a(x-p)}+q$ 는 이 꼴에서 $x$ 축으로 $p$ 만큼, $y$ 축으로 $q$ 만큼 평행이동한 것이다.
  
    - 차례로 $y = \sqrt[]{2x}$ 와 $y = \sqrt[]{-2x}$ 의 그래프이다. 


      ![desmos-graph](https://user-images.githubusercontent.com/16812446/75109533-ab132400-5667-11ea-8468-c25c60012256.png) ![desmos-graph(2)](https://user-images.githubusercontent.com/16812446/75109563-da299580-5667-11ea-981c-50847527be13.png)

    - 차례로 $y = -\sqrt[]{2x}$ 와 $y = -\sqrt[]{-2x}$ 의 그래프이다. 

      ![desmos-graph(3)](https://user-images.githubusercontent.com/16812446/75109568-f3cadd00-5667-11ea-80f9-c5fa4b9a8055.png) ![desmos-graph(4)](https://user-images.githubusercontent.com/16812446/75109577-09d89d80-5668-11ea-829e-5ed51029ae00.png)
      
    - 차례로 $y = \sqrt[]{3^2-x^2}$ 와 $y = -\sqrt[]{3^2-x^2}$ 의 그래프이다. 

      ![desmos-graph(5)](https://user-images.githubusercontent.com/16812446/75109648-9c793c80-5668-11ea-8542-9369bc611610.png) ![desmos-graph(6)](https://user-images.githubusercontent.com/16812446/75109660-b87cde00-5668-11ea-897c-4eaf836d5a0b.png)

## 지수함수 

- 지수함수 : $a$ 가 $1$ 이 아닌 양수일 때, 임의의 실수 $x$ 에 $a^x$ 를 대응시킨 함수 $y = a^x$ 이다. 

  - 지수함수의 그래프는 $a > 1$ 일 때와 $0 < a < 1$ 일 때 달라진다. 

  - 밑이 무리수 $e$ 인 지수함수 $y = e^x$ 를

    $$ y = \exp x $$

    또는

    $$ y = \exp (x) $$

    로 표현하기도 한다.

  - $a > 1$ 일 때, $y = 2^x$

    ![desmos-graph(1)](https://user-images.githubusercontent.com/16812446/73837365-a9b6be80-4854-11ea-8d3b-d1e3d3972bdc.png)

  - $0 < a < 1$ 일 때, $y = (1/2)^x$

    ![desmos-graph(2)](https://user-images.githubusercontent.com/16812446/73837415-c652f680-4854-11ea-8eac-410e5f17204b.png)

- 지수방정식(exponential equation) : 지수에 미지수를 포함하고 있는 방정식이다. 

  - 예시 
  
    $x^{x+3} = x^{2x-1}$

- 지수부등식(exponential inequality) : 지수에 미지수를 포함하고 있는 부등식이다. 

  - 지수부등식의 밑이 $a$ 일때, 밑의 범위가 $a > 1$ 인지 $0 < a <1$ 인지에 따라 지수의 대수 관계가 바뀌므로 주의해야 한다. 

  - 예시 
  
    $2^{x^2-4} \geq 8^x$

## 로그함수

- 로그함수 : $a$ 가 $1$ 이 아닌 양수일 때, 임의의 양의 실수 $x$ 에 $\log_{a} x$ 를 대응시키는 함수 $y = \log_{a} x$ 를 $a$ 를 밑으로 하는 로그함수라 한다. 

  - 로그함수 $y = \log_{a} x(a>0, a \neq 1)$ 은 지수함수 $y = a^x(a>0, a \neq 1)$ 의 역함수이다. 

    - 예시 
    
      지수함수 $y = 2^x$ 의 역함수 $x = 2^y$ 를 $y$ 에 대하여 풀면 $y = \log_{2} x$ 이다. 

  - 따라서 로그함수는 지수함수와 직선 $y=x$ 에 대하여 대칭이다. 이에따라 지수함수와 마찬가지로 $a > 1$ 일 때와 $0 < a < 1$ 일 때 달라진다. 

  - $a > 1$ 일 때, $y = \log_{2} x$

    ![desmos-graph(4)](https://user-images.githubusercontent.com/16812446/73849124-b2b38a00-486c-11ea-9385-7b2aff924a78.png)

  - $0 < a < 1$ 일 때, $y = (1/2)^x$

    ![desmos-graph(5)](https://user-images.githubusercontent.com/16812446/73849242-f0b0ae00-486c-11ea-8587-58a29b4e4606.png)

- 로그방정식(logarithm equation) : 로그의 진수($value$) 또는 밑($base$)에 미지수를 포함하고 있는 방정식이다. 

  - 예시 
  
    $\log_{2} (x+2) = \log_{2} 2x$

- 로그부등식(logarithm inequality) : 로그의 진수 또는 밑에 미지수를 포함하고 있는 부등식이다. 

  - 로그부등식의 밑이 $a$ 일때, 밑의 범위가 $a > 1$ 인지 $0 < a <1$ 인지에 따라 지수의 대수 관계가 바뀌므로 주의해야 한다. 

  - 예시 
  
    $\log_{3} (x^2-2x) > \log_{3} (2-x)+1$

## 특별한 함수 

- 가우스 함수 : 실수 $x$ 에 대하여 $x$ 보다 크지 않은 최대의 정수를 대응시키는 함수이다. 

  - $f(x) = [x]$ 로 표기한다. 

  - 한 마디로 $x$ 를 정수부, 소수부로 쪼개고 소수부를 버리는 함수이다. 이때 소수부란 $0$ 보다 크거나 같고 $1$ 보다 작은 수이다. 

  - 예시 
  
    $[1.23] = 1, [-1.23] = -2$ 

  - 이 함수를 가우스 함수라 부르는 것은 대한민국을 제외하면 보편적이지 않으니 주의해야 한다. 버림함수 또는 바닥함수라고도 불리운다. 

- 주기함수 : $y = f(x)$ 의 정의역에 속하는 모든 실수 $x$ 에 대하여 $f(x+p) = f(x)$ 를 만족시키는 $0$ 이 아닌 상수 $p$ 가 존재할 때 이 함수를 주기함수라 한다. 

  - 또한 이러한 상수 $p$ 중에서 최소인 양수를 그 함수의 주기라고 한다. 

  - 두 함수 $f(x), g(x)$ 가 주기함수라면 $f(x) + g(x)$ 도 주기함수고 그 주기는 $f(x)$ 의 주기와 $g(x)$ 의 주기의 최소공배수이다. 

  - 예시 
  
    $y = \sin x$ 는 주기가 $2 \pi$ 인 주기함수이다. 즉 모든 실수 $x$ 에 대하여 관계 $\sin x = \sin(x + 2\pi)$ 가 성립한다.

  - 예시 
  
    $y = \tan x$ 는 주기가 $\pi$ 인 주기함수이다. 모든 실수 $x$ 에 대하여 관계 $\tan x = \tan(x + \pi)$ 가 성립한다.

- 뉴턴의 다항식 보간법(polynomial interpolation) : $(n+1)$ 개의 점을 지나는 $n$ 차 다항함수의 정확한 식을 얻는 방법이다.

  - 이 예시 뉴턴의 다항식 보간법을 사용하지 않고 연립방정식으로 구하는 방법이다. 

    - 예시 
    
      세 점 $(1, 7), (-1, 5), (-2, -5)$ 를 지나는 포물선을 그래프로 하는 이차함수 $ax^2 +bx+c$ 를 구하여라.

        $$
        \begin{cases}
        5 = a-b+c&\text{}\\
        7 = a+b+c&\text{}\\
        -5 = 4a-2b+c&\text{}\\
        \end{cases} 
        $$

      위 연립방정식을 풀어서 $a, b, c$ 를 얻으면 이차함수가 $y=-3x ^{2}+x+9$ 라는 것을 알 수 있다. 
  
  - 예시 
  
    함수 $f(x) = ax^2 + bx+c$ 가 $f(2.17)=7$, $f(3.17)=1$, $f(4.17)=3$ 을 만족시킬 때 $a$ 값을 구해보자. 

    먼저 두 점 $(2.17, 7), (3.17,1)$ 을 지나는 직선을 그래프로 하는 일차함수 식을 구하자. 

      $$ g(x) = -6(x-3.17)+1 $$
    
    그런데 이 직선의 그래프 $g(x)$ 와 $f(x)$ 와의 교점은 $(2.17, 7), (3.17,1)$ 이므로 이 두 점에서 두 함수의 함수값은 같다. 따라서 이 두 점에서 두 함수의 차이는 $0$ 이어야 한다. 따라서 다항식 $f(x)-g(x)$ 은 다음과 같이 인수분해된다. 

      $$ f(x)-g(x)=a(x-2.17)(x-3.17) $$
    
    그런데 $g(x)$ 를 이미 알고 있으므로 $g(x)$ 를 소거할 수 있다.

      $$ f(x)+6(x-3.17)= + a(x-2.17)(x-3.17) $$
    
    이제 이 이차함수 $f(x)$ 가 $(4.17, 3)$ 을 지나는 것을 이용하여 마지막 미지수 $a$ 가 $4$ 라는 것을 밝힐 수 있다. 

- 시그모이드 함수(sigmoid function) : 다음과 같이 표현되는 함수를 시그모이드 함수라 한다. 

  $$ \zeta _a(x) = \frac{1}{1+\exp(-ax)} $$

  또는

  $$ \zeta _a(x) = \frac{1}{1+ e ^{-ax} } $$

  - $a$ 를 게인(gain) 이라 한다.

  - 시그모이드 함수는 다음의 특성을 갖는다.
  
    - 점근선 $y = 0, y = 1$ 을 갖는다.

    - $$x = 0 \to \zeta _a(0) = \frac{1}{2}$$ 

- 표준 시그모이드 함수 : $a=1$ 일 때의 시그모이드 함수, 즉

  $$ \zeta (x) = \frac{1}{1+\exp (-x)} $$

  또는

  $$ \zeta (x) = \frac{1}{1+e ^{-x}} $$

  를 표준 시그모이드 함수라 한다. 

- 밑이 무리수 $e$ 인 지수함수의 그래프 연구 k

  - 다음 그래프에서 빨간 곡선이 $y = e^x$, 파란 곡선이 $y=e^{-x}$ 를 나타낸다. 

    ![desmos-graph(5)](https://user-images.githubusercontent.com/16812446/77422130-51da1400-6e10-11ea-8468-7ab5610f410b.png)

  - 다음 그래프에서 빨간 곡선이 $y = \frac{1}{e^x}$, 파란 곡선이 $y= \frac{1}{e^{-x}}$ 를 나타낸다. 

    ![desmos-graph](https://user-images.githubusercontent.com/16812446/77422280-88b02a00-6e10-11ea-98e3-6cee1b599740.png)
  
    - $y = e ^{x} = \frac{1}{e ^{-x}}$ 를 알 수 있다. 

  - 다음 그래프는 
  
    $$y = \frac{1}{1+e ^{-x}}$$
    
    이다. 

    ![desmos-graph](https://user-images.githubusercontent.com/16812446/77422864-87333180-6e11-11ea-8200-6f070e22c6d9.png)

    - 함수값의 경계가 $(0, 1)$ 임을 알 수 있다. 

  - 다음 그래프는 
  
    $$y = \frac{1}{\frac{1}{2}+e ^{-x}}$$
    
    이다. 

    ![desmos-graph(1)](https://user-images.githubusercontent.com/16812446/77423021-d8432580-6e11-11ea-94fa-92cdd15ef17a.png)

    - 함수값의 경계가 $(0, 2)$ 임을 알 수 있다. 

  - 다음 그래프는 
  
    $$y = \frac{1}{\frac{1}{4}+e ^{-x}}$$
    
    이다. 

    ![desmos-graph(2)](https://user-images.githubusercontent.com/16812446/77423171-13455900-6e12-11ea-94c9-84ae6d46ff38.png)

    - 함수값의 경계가 $(0, 4)$ 임을 알 수 있다. 
  
  - 여기까지의 그래프 연구를 통하여 

    $$ y = \frac{1}{\frac{1}{n}+e ^{-x}} $$

    의 함수값의 경계가 $(0, n)$ 이라는 귀납적 가설을 세울 수 있다.

  - 다음 그래프는 
  
    $$y = \frac{1}{1+e ^{-5x}}$$
    
    이다. 

    ![desmos-graph(3)](https://user-images.githubusercontent.com/16812446/77423392-72a36900-6e12-11ea-80e0-b3baf537b86b.png)

    - 게인 $a$ 의 값을 $1$ 에서 $5$ 로 높혔더니 함수의 휘어지는 정도가 커졌다는 것을 알 수 있다. $x$ 축을 압축시켰다고도 할 수 있다.

# 벡터 

- 양 : 어떤 물체의 크기이다.

  - 측정 가능한 양(물리량)과 측정 불가능한 양(비물리량)으로 나눌 수 있다.

- 물리량 : 측정 가능한 양이다.

  - 벡터와 스칼라로 나눌 수 있다. 

- 비물리량 : 측정 불가능한 양이다. 

  - 예시 

    "$A$ 의 키는 $180$ cm 이다." 에서 $180$ cm 의 키는 측정 가능한 물리량이다.

    반면 "$A$ 가 $B$ 보다 더 리더십이 있다." 에서 리더십의 비교는 측정이 불가능한 비물리량이다. 

    > 그러나 리더십이라는 대상에 대한 단순화 및 집합으로의 환원을 거쳐서 측정하능하게 만들 수 있다는 가능성을 볼 수 있다. 여기에서 더 나아가 철학적 관념 또한 단순화와 수학적 모델링을 거쳐서 측정가능한 수로 격하시킬 수 있는 가능성도 엿볼 수 있다. 

- 스칼라(scala) : 크기만 있고 방향성이 없는 물리량이다. 

  - 길이, 넓이, 부피 등이 스칼라량에 속한다. 

  - 예시 

    "$A$ 는 $20$ 분을 뛰었다" 에서 $20$ 은 스칼라량이다. 

- 벡터(vector) : 크기와 방향성이 동시에 있는 물리량이다. 

  - 스칼라량으로는 방향에 대한 정보가 부족하기에 방향에 대한 정보를 덧붙힌 것이 벡터이다. 

  - 예시 

    "$A$ 는 $20$ 분을 뛰었다" 를 "$A$ 는 동쪽으로 $20$ 분을 뛰었다" 로 바꾸면 방향성이 추가되었기 때문에 벡터량이다. 

  - 역사 
  
    물체에 두 힘을 동시에 가했을 때 물체의 힘의 크기를 나타내는 $2$ 개의 선분이 이루는 평행사변형의 대각선을 그릴 수 있다. 이 대각선의 방향으로 그 물체가 움직이게 되는데 이러한 벡터의 합성을 스테빈(1548), 갈릴레오(1546) 가 발견했다. 

    뉴턴(1642)은 속도, 힘 등을 방향이 있는 선분으로 나타내어 벡터의 기초를 만들었다. 

    가우스(1777)는 복소수평면을 생각하여 복소평면에서 벡터를 나타낼 수 있게 하였다.

    해밀턴(1805)은 벡터에 좌표를 결합하여 벡터공간의 기초를 만들었다.

    그리스만(1809)은 벡터의 내적과 외적을 정의하였다.

    라플라스(1749)는 벡터해석학에 기여했다.

    기브스(1849), 헤비사이드(1850) 는 벡터해석학을 완성했다. 

    이 벡터해석학은 19세기 물리학을 대표하는 전자기학의 필수적인 수학적 도구가 되었다. 또 현대에 와서는 의학과 공학에도 널리 쓰이는 중요한 개념이 되었다. 

  - 다음과 같이 점 $A$ 에서 점 $B$ 로 방향이 주어진 선분 $AB$ 를 벡터 $AB$ 라 한다.

    ![](https://t1.daumcdn.net/cfile/tistory/267BE245539F79880C)

    - 이것을 형식언어로 $\overrightarrow{AB}$ 로 표현한다. 

  - 다음과 같이 벡터를 시점과 종점이 아닌 단일 문자로 나타낼 수도 있다. 

    $$ \overrightarrow{a}, \overrightarrow{b}, \overrightarrow{c}, \dots $$

  - **벡터는 행렬과 같이 수와 다른 개념이므로 행렬에서처럼 연산법칙, 항등원, 역원, 단위(수에서 $1$) 등을 새로 정의해야 한다.**

- 벡터의 시점(initial point) : 다음과 같이 점 $A$ 에서 점 $B$ 로 방향이 주어진 선분 $AB$ 를 벡터 $AB$ 에서

    ![](https://t1.daumcdn.net/cfile/tistory/267BE245539F79880C)

    점 $A$ 를 벡터의 시점이라 한다. 

- 벡터의 종점(terminal point) : 다음과 같이 점 $A$ 에서 점 $B$ 로 방향이 주어진 선분 $AB$ 를 벡터 $AB$ 에서

    ![](https://t1.daumcdn.net/cfile/tistory/267BE245539F79880C)

    점 $B$ 를 벡터의 종점이라 한다. 

- 스칼라 함수(scalar function) : 실숫값 함수와 같이 어떤 점을 하나의 스칼라에 대응시키는 함수이다.

  - 즉 여러 독립변수에 대응하는 하나의 함수 값이 스칼라가 된다. 

  - 지금까지 살펴본 함수들이 스칼라 함수에 해당한다. 

  - 실숫값 함수의 정의처럼 공역이 실수 집합 $\Re$ 인 함수 

    $$ f: X \to \Re $$

    이다. 

  - 예시 

    $$ y = x ^{2}, y = \sin x, y = \ln x \dots $$

- 벡터 함수(vector function) : 어떤 점을 하나의 벡터에 대응시키는 함수이다. 

  - 여러 독립변수를 하나의 함수값, 즉 벡터에 대응시키는 함수이다. 

  - 예시 

    $$ r(t) = \bigg < f(t), g(t), h(t) \bigg > = f(t)i + g(t)j+h(t)k $$

- 장(field) : 공간에서 위치, 시간 등에 따라 그 성질을 다르게 나타내는 물리량이다. 

  - 공간 내 점의 위치와 시간에 따라 다른 값을 가진다.

  - 공간의 모든 점에서 정의되는 물리량이다. 

    - 물리량이므로 스칼라량, 벡터량을 지닌다. 

- 스칼라 장(scalar field) : 공간 내 각 점의 위치, 시간 등에 따라 결정되는 크기를 갖는 스칼라를 나타내는 분포이다.

  - 즉 공간 내 각 점에 물리적으로 스칼라 값을 대응시키는 스칼라 함수이다. 

  - 예시 

    대기의 각 점의 온도, 밀도, 압력 
  
  - 예시 

    전하가 있는 공간에서의 전위의 분포 

- 벡터 장(vector field) : 공간 내 각 점의 위치, 시간 등에 따라 결정되는 크기와 방향을 갖는 벡터를 나타내는 분포이다. 

  - 예시 

    속도장, 역장(力場)은 크기 뿐만 아니라 방향을 가지므로 벡터장에 해당한다. 

    - 속도장은 각 점에서 속도 벡터를 대응시킨 것으로 해류 속도장, 풍속 속도장 등이 있다. 

    - 역장은 각 점에서 힘 벡터를 대응시킨 것으로써 중력장, 전기장, 자기장 등이 있다.

      - 일례로 중력장은 중력이 미치는 공간 내 각 점에 중력 벡터를 대응시킨 벡터 함수이다. 

## 여러가지 벡터 

- 영벡터(zero vector) : 임의의 점 $A$ 에 대하여 $\overrightarrow{AA}$ 와 같이 시점과 종점이 일치하는 벡터를 영벡터라 한다. 

  - 기호로 $\overrightarrow{0}$ 으로 나타낸다.

  - 영벡터는 크기가 $0$ 고 방향은 없다고 정의한다. 

  - 실수연산에서 항등원 역할을 한다.

- 역벡터(inverse vector) : 벡터 $\overrightarrow{AB}$ 에 대하여 크기는 같고 방향이 반대인 벡터 $\overrightarrow{BA}$ 를 벡터 $\overrightarrow{AB}$ 의 역벡터라 한다. 

  - $\overrightarrow{AB}$ 역벡터를 $-$ 를 붙혀서 $-\overrightarrow{AB}$ 로 나타낸다.

    $$ \overrightarrow{BA} = -\overrightarrow{AB} $$

  - 실수연산에서 역원 역할을 한다.

- 단위벡터(unit vector) : 크기가 $1$ 인 벡터이다. 

  - 실수연산에서 $1$ 의 역할을 한다.

- 평면벡터(plane vector) : 평면에서 정의된 벡터이다. 

- 공간벡터(space vector) : 공간에서 정의된 벡터이다. 

## 벡터 대수 

실수에서 했던 연산들을 벡터에 대하여 재정의하고 있는 것이다. 

- 벡터의 크기 : 벡터 $\overrightarrow{AB}$ 에서 선분 $AB$ 의 길이를 벡터의 크기라 한다.

  - 형식언어로 $|\overrightarrow{AB}|$ 로 나타낸다. 

  - 다음과 같이 벡터의 크기를 시점과 종점이 아닌 단일 문자로 나타낼 수도 있다. 

    $$ |\overrightarrow{a}|, |\overrightarrow{b}|, |\overrightarrow{c}|, \dots $$

- 두 벡터가 같다 : 시점과 종점의 위치에 관계 없이 두 벡터 $\overrightarrow{a}, \overrightarrow{b}$ 의 크기와 방향이 같으면 두 벡터 $\overrightarrow{a}, \overrightarrow{b}$ 를 같다고 한다.

  - 두 벡터 $\overrightarrow{a}, \overrightarrow{b}$ 가 각각 선분 $\overline{AB}, \overleftrightarrow{CD}$ 로 구성되었을 때 이 둘이 같다는 것을

    $$ \overrightarrow{a} = \overrightarrow{b} \Leftrightarrow \overrightarrow{AB} = \overrightarrow{CD} $$

    로 표현한다. 
  
  - 예시 

    ![unnamed](https://user-images.githubusercontent.com/16812446/79002706-fd62c280-7b8b-11ea-8a50-45ca181784e1.gif)

    위 세 벡터는 같은 방향과 같은 길이를 지니므로 모두 같다.

    즉, 왼쪽부터 차례로 $\overrightarrow{AB}, \overrightarrow{CD}, \overrightarrow{OP}$ 라고 한다면 

    $$ \overrightarrow{AB}= \overrightarrow{CD}= \overrightarrow{OP} $$

    이다. 

- 벡터의 덧셈 : 벡터의 덧셈은 다음 두 경우로 정의된다. 

  - 삼각형에서의 덧셈 : 두 벡터 $\overrightarrow{u} = \overrightarrow{AB}, \overrightarrow{v} = \overrightarrow{BC}$ 에 대하여 벡터 $\overrightarrow{w} = \overrightarrow{AC}$ 를 두 벡터 $\overrightarrow{u}, \overrightarrow{v}$ 의 합이라 한다.

    - 이것을 기호로 다음과 같이 나타낸다. 

      $$ \overrightarrow{u}+\overrightarrow{v}= \overrightarrow{AB} + \overrightarrow{BC} = \overrightarrow{AC} = \overrightarrow{w} $$ 

    - 그림

      ![캡처](https://user-images.githubusercontent.com/16812446/77826567-90930580-7153-11ea-98d2-da447edd015a.PNG)

  - 평행사변형에서의 덧셈 : 두 벡터 $\overrightarrow{a} = \overrightarrow{AB}, \overrightarrow{b} = \overrightarrow{AC}$ 에 대하여 평행사변형 $ABDC$ 를 만들 때, 벡터 $\overrightarrow{AD}$ 를 두 벡터 $\overrightarrow{a}, \overrightarrow{b}$ 의 합이라 한다.

    - 이것을 기호로 다음과 같이 나타낸다. 

      $$ \overrightarrow{a}+\overrightarrow{b}= \overrightarrow{AB} + \overrightarrow{AC} = \overrightarrow{AD} $$ 
  
    - 그림

      ![](https://i.ytimg.com/vi/gdWfqihMW14/maxresdefault.jpg)

- 벡터 덧셈의 성질 

  임의의 세 벡터 $\overrightarrow{a}, \overrightarrow{b}, \overrightarrow{c}$ 와 영벡터 $\overrightarrow{0}$ 에 대하여 다음이 성립한다.

  - 교환법칙 : $\overrightarrow{a}+\overrightarrow{b}=\overrightarrow{b}+\overrightarrow{a}$

  - 결합법칙 : $(\overrightarrow{a}+\overrightarrow{b})+\overrightarrow{c}=\overrightarrow{a}+(\overrightarrow{b}+\overrightarrow{c})$

  - 항등원 : $\overrightarrow{a}+\overrightarrow{0}=\overrightarrow{0}+\overrightarrow{a} = \overrightarrow{a}$

  - 역원 : $\overrightarrow{a}+(-\overrightarrow{a})=-\overrightarrow{a}+\overrightarrow{a} = \overrightarrow{0}$

- 벡터의 뺄셈 : 두 벡터 $\overrightarrow{OA}, \overrightarrow{OB}$ 에 대하여 $\overrightarrow{a}$ 와 $\overrightarrow{-b}=\overrightarrow{BO}$ 의 합 

  $$ \overrightarrow{a}+(-\overrightarrow{b}) = \overrightarrow{OA}+\overrightarrow{BO} = \overrightarrow{BO} + \overrightarrow{OA} = \overrightarrow{BA} $$

  를 벡터 $\overrightarrow{a}$ 를 벡터 $\overrightarrow{b}$ 에서 뺀 차라고 한다.

  - 이것을 기호로 다음과 같이 나타낸다. 

    $$ \overrightarrow{a}-\overrightarrow{b}= \overrightarrow{OA} - \overrightarrow{OB} = \overrightarrow{BA} $$ 

  - 그림 
  
    ![](https://i.ytimg.com/vi/kOCTTK3Cnto/maxresdefault.jpg)
  
- 벡터의 실수배(스칼라배) : 임의의 실수 $k$ 와 벡터 $\overrightarrow{a}$ 의 곱 $k \overrightarrow{a}$ 를 벡터 $\overrightarrow{a}$ 의 실수배라 하고 다음과 같이 정의한다.

  - $\overrightarrow{a} \neq \overrightarrow{0}$ 인 경우 

    - $k>0$ 이면 $k \overrightarrow{a}$ 는 $\overrightarrow{a}$ 와 방향이 같고 크기가 $k |\overrightarrow{a}|$ 인 벡터이다. 

    - $k<0$ 이면 $k \overrightarrow{a}$ 는 $\overrightarrow{a}$ 와 방향이 반대이고 크기가 $|k| |\overrightarrow{a}|$ 인 벡터이다. 

    - $k=0$ 이면 $k \overrightarrow{a} = \overrightarrow{0}$ 이다.

  - $\overrightarrow{a} = \overrightarrow{0}$ 인 경우, 실수 $k$ 에 대하여 $k \overrightarrow{a}=\overrightarrow{0}$ 이다. 

- 벡터의 실수배의 성질 : 두 실수 $k, l$ 과 두 벡터 $\overrightarrow{a}, \overrightarrow{b}$ 에 대하여 다음이 성립한다.

  - 벡터의 실수배의 결합법칙 : $k(l \overrightarrow{a}) = (kl)\overrightarrow{a}$

  - 벡터의 실수배의 분배법칙 
  
    $(k+l) \overrightarrow{a} = k\overrightarrow{a}+l \overrightarrow{a}$

    $k(\overrightarrow{a}+\overrightarrow{b}) = k\overrightarrow{a}+k \overrightarrow{b}$

- 두 벡터의 평행조건 : 다음 두 경우에서 두 벡터는 평행한다고 정의한다. 

  - 영벡터가 아닌 두 벡터 $\overrightarrow{a}, \overrightarrow{b}$ 와 $0$ 이 아닌 실수 $k$ 에 대하여 

    $$ \overrightarrow{a}//\overrightarrow{b} \Leftrightarrow \overrightarrow{b} = k \overrightarrow{a} $$

- 세 점이 한 직선 위에 있을 조건 : 서로 다른 세점 $A, B, C$ 가 한 직선 위에 존재하기 위한 필요충분조건은 $0$ 이 아닌 실수 $k$ 에 대하여

  $$ \overrightarrow{AC} = k \overrightarrow{AB} $$

  이다.

## 위치벡터 

- 위치벡터 : 평면 또는 공간에서 한 점 $O$ 를 고정할 때 임의의 한 점 $A$ 에 대하여 $O$ 를 시점으로 하고 $A$ 를 종점으로 하는 유일한 벡터 $\overrightarrow{OA}$ 를 점 $O$ 에 대한 점 $A$ 의 위치벡터라 한다. 

  - 점 $O$ 에 대한 점 $A$ 의 위치벡터를 간단하게 점 $A$ 의 위치벡터로 부른다.

  - 점 $O$ 의 위치벡터는 $\overrightarrow{0}$ 이다.

  - 두 점 $A, B$ 의 위치벡터가 각각 $\overrightarrow{a}, \overrightarrow{b}$ 일 때 

    $$ \overrightarrow{AB} = \overrightarrow{OB} - \overrightarrow{OA} = \overrightarrow{b} - \overrightarrow{a} $$

    이다. 

**구체화 필요**

## 평면벡터 

- 평면벡터 : 위치벡터의 개념을 좌표평면 위로 옮겨서 시점을 원점 $O(0, 0)$ 으로 고정시킨 벡터이다.

  - 종점의 좌표 $2-$튜플을 평면벡터를 대표하는 값으로 삼는다. 

- 평면벡터 성분 표현 : 임의의 평면벡터 $\overrightarrow{a}$ 에 대하여 $\overrightarrow{a} = \overrightarrow{OA}$ 의 종점이 점이 $A(a_1, a_2)$ 일 때, 두 점 $E_1(1, 0), E_2(0, 1)$ 의 위치벡터 $\overrightarrow{e_1}, \overrightarrow{e_2}$ 를 이용하여 벡터 $\overrightarrow{a}$ 를 다음과 같이 나타낼 수 있다. 

  $$ \overrightarrow{a} = \overrightarrow{OA} = \overrightarrow{OA_1} + \overrightarrow{OA_2} = a_1\overrightarrow{e_1} + a_2 \overrightarrow{e_2} $$

  - 이때 두 실수 $a_1, a_2$ 를 평면벡터 $\overrightarrow{a}$ 의 성분이라 한다. 

  - 또 성분만을 이용해서 평면벡터 $\overrightarrow{a}$ 를 두 수의 순서쌍($2-$튜플)

    $$ \overrightarrow{a} = (a_1,a_2) $$

    로 나타낼 수 있다. 

- 평면벡터의 크기 : $\overrightarrow{a} = (a_1,a_2)$  의 크기는 

  $$ |\overrightarrow{a}| = \sqrt[]{a^{2}_{1}+a^{2}_{2}} $$

- 평면벡터의 같음 : $\overrightarrow{a} = (a_1,a_2),\overrightarrow{b} = (b_1,b_2)$  가 같을 조건은

  $$ \overrightarrow{a} = \overrightarrow{b} \Leftrightarrow a_1=b_1, a_2 = b_2 $$

  이다. 

- 평면벡터의 연산 : $\overrightarrow{a} = (a_1,a_2),\overrightarrow{b} = (b_1,b_2)$ 에 대하여

  - 덧셈 : $\overrightarrow{a}+\overrightarrow{b}=(a_1+b_1, a_2+b_2)$

  - 뺄셈 : $\overrightarrow{a}-\overrightarrow{b}=(a_1-b_1, a_2-b_2)$

  - 실수배 : $k\overrightarrow{a}=(ka_1, ka_2)$

- 두 점에 대한 평면벡터의 성분 : 좌표평면 위의 두 점 $A(a_1,a_2),B(b_1,b_2)$ 에 대하여 

  $$ \overrightarrow{AB} = \overrightarrow{OB}-\overrightarrow{OA}=(b_1,a_1, b_2-a_2) $$

  이다. 

- 두 점에 대한 평면벡터의 크기 : 좌표평면 위의 두 점 $A(a_1,a_2),B(b_1,b_2)$ 에 대하여 

  $$ |\overrightarrow{AB}| = \sqrt[]{(b_1-a_1)^{2}+(b_2-a_2)^{2}} $$

  이다. 

- 두 평면벡터의 평행 : 영벡터가 아닌 두 평면벡터 $\overrightarrow{a} = (a_1,a_2),\overrightarrow{b} = (b_1,b_2)$ 에 대하여

  $$ \overrightarrow{a}//\overrightarrow{b} \Leftrightarrow \overrightarrow{b} = k \overrightarrow{a} \Leftrightarrow \begin{cases} b_1 = ka_1 &\text{}\\ b_2=ka_2 &\text{}\\ \end{cases} $$

## 공간벡터 

**구체화 필요**
