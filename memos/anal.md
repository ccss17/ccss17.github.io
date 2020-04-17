# [ccss17.github.io](https://ccss17.github.io)

# 해석

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;"

- 해석학 : 

**구체화 필요**

  </blockquote>

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;"

- 유클리드 공간 : 유클리드 기하학의 공리가 성립하는 $n$ 차원의 공간이다. 

  </blockquote>

  - 유클리드가 연구했던 길이와 평면과 공간에 좌표계를 도입하여 임의 차원의 공간으로 일반화한 것이다. 직선은 1차원 유클리드 공간, 평면은 2차원 유클리드 공간, 공간은 3차원 유클리드 공간이다. 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;"

- 좌표평면(직교 좌표계, rectangular coordinate system) : 임의 차원의 유클리드 공간을 나타내는 좌표계 중 하나이다. 

  </blockquote>

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;"

- 튜플(tuple) : 셀 수 있는 수량의 순서있는 열거이다. 

  </blockquote>

  - $n$ 개의 요소를 가진 튜플을 $n$-튜플이라 한다.

  - 가령 $5$-튜플은 $(2, 4, 7, 1, 7)$ 와 같다. 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;"

- 순서쌍(2-튜플, ordered pair) : 두 개의 수학적 대상을 순서를 정하여 나타낸 쌍이다.

  </blockquote>

  - 예시 

    두 대상 $a, b$ 를 $(a, b)$ 로 나타낸다. 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;"

- 이항관계(binary relation) : 순서쌍들로 이루어지는 집합이다. 

  </blockquote>

  - 예시 

    집합 $A = \{a, b\}$ 의 원소를 집합 $B = \{c\}$ 로 대응시키는 모든 순서쌍은 집합 $R = \{(a, c), (b, c)\}$ 이다.

## 구간 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;"

- 구간(interval) : 두 실수 $a, b(a<b)$ 에 대하여 실수의 집합 

  $$\{x \in \Re |a \leq x \leq b\}, \{x \in \Re |a < x < b\}, \{x \in \Re  | a \leq x < b\}, \{x \in \Re |a<x \leq b\}$$

  를 구간이라 한다. 

  </blockquote>

  - 기호로 각각 $[a,b], (a,b), [a,b), (a,b]$ 라 한다.

  - 구간은 수로 그 특성 혹은 존재자체를 수로 추상화할 수 있는 자연의 모든 대상의 집합을 마찬가지로 수로 격하될 수 있는 자연의 어떤 대상을 기준으로 하여 나눈 것에 대응된다.

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;"

- 폐구간(닫힌구간, closed interval) : $[a,b]$ 를 닫힌구간이라 한다. 

  </blockquote>

  - $[a,b] = \{x \in \Re | a \leq x \leq b\}$ 이다. 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;"

- 개구간(열린구간, open interval) : $(a,b)$ 를 열린구간이라 한다. 

  </blockquote>

  - $(a,b) = \{x \in \Re | a < x < b\}$ 이다. 

  - 특히 실수 전체의 집합도 하나의 구간으로 보고 개구간 $(-\infty, \infty)$ 로 나타낸다. 

    - $\infty$ 는 특정한 값이 아니고 "한없이 커지고 있는 상태" 를 나타내기 때문에 $[-\infty, \infty]$ 나 $(a, \infty]$ 와 같이 $\infty$ 를 폐구간과 엮지 않는다. 실수 $x$ 의 값이 한없이 커질 수는 있어도 $x = \infty$ 라는 값을 가질 수는 없기 때문이다. 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;"

- 반열린구간(반개구간 또는 반폐구간, half open interval 또는 half closed interval) : $(a,b]$ 또는 $[a,b)$ 를 반열린구간이라 한다. 

  </blockquote>

  - $(a,b] = \{x \in \Re | a < x \leq b\}$ 이다. 

  - $[a,b) = \{x \in \Re | a \leq x < b\}$ 이다. 

  - $(-\infty,b] = \{x \in \Re | x \leq b\}$ 이다. 

  - $[a,+\infty) = \{x \in \Re | a \leq x\}$ 이다. 

## 1차원 좌표계

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;"

- 수직선(number line) : 다음과 같은 규칙으로 실수를 한 점에 일대일 대응시키는 직선이다. 

  1. 원점 $O$ 는 $0$ 이다.

  2. $x(x>0)$ 는 원점 $O$ 에서 양의 방향으로 $x$단위만큼 떨어진 점이다.

  3. $-x(x>0)$ 는 원점 $O$ 에서 음의 방향으로 $x$단위만큼 떨어진 점이다.

  </blockquote>

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;"

- 좌표(coordinate) : 수직선 위의 점에 대응하는 실수이다.

  </blockquote>

  - 일대일 대응이기에 좌표는 그 점을 유일하게 특정할 수 있다.

  - 좌표가 $a$ 인 점 $P$ 를 $P(a)$ 로 표기한다. 

## 2차원 좌표계

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;"

- 좌표평면(coordinate plane) : 서로 직교하는 수직선을 $x$축과 $y$축으로 두고 다음과 같은 규칙으로 평면 위의 실수 순서쌍 좌표를 정의하는 $xy$ 좌표평면이다. 

  1. 원점 $O$ 는 $(0, 0)$ 이다. 

  2. 점 $P$ 는 점 $P$ 에서 두 수직선($x$축, $y$축)으로 수산의 발을 내렸을 때 각 수직선에서의 수선의 발의 좌표의 순서쌍 $(n, m)$ 이다. 

  </blockquote>

  - 이렇게 얻은 실수 순서쌍 $(n, m)$ 를 그 점의 좌표라 하고 $n$ 와 $m$ 를 각각 그 점에서의 $x$ 좌표, $y$ 좌표라 한다. 

      ![2-coor](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Cartesian-coordinate-system.svg/354px-Cartesian-coordinate-system.svg.png)

  - 좌표평면을 통하여 평면 위의 모든 점은 유일한 실수 순서쌍에 대응된다. 

  - 좌표평면을 통하여 평면 위에서 정의되었던 논증기하학의 도형들을 좌표위에 나타낼 수 있게 되어 대수학적 문제로 변환할 수 있게 된다. 역으로 대수학적 수식 또한 기하학적으로 나타낼 수 있다. 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;"

- 절편 : 좌표평면 상의 함수의 그래프가 $x$ 축과 $y$ 축과 만나는 좌표를 통틀어서 이르는 말이다. 

  </blockquote>

  - $x$ 절편 : $x$ 축과 만나는 $x$ 좌표이다. 

  - $y$ 절편 : $y$ 축과 만나는 $y$ 좌표이다. 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;"

- 사분면(quadrant) : 좌표평면의 직교좌표축으로 구분되는 $4$ 가지 영역을 다음과 같이 특정하는 방법이다.

  </blockquote>

  - $1$사분면 : $x$ 좌표와 $y$ 좌표가 모두 양수인 좌표평면 영역을 칭한다. 

  - $2$사분면 : $x$ 좌표가 음수이고 $y$ 좌표가 양수인 좌표평면 영역을 칭한다. 

  - $3$사분면 : $x$ 좌표와 $y$ 좌표가 모두 음수인 좌표평면 영역을 칭한다. 

  - $4$사분면 : $x$ 좌표가 양수이고 $y$ 좌표가 음수인 좌표평면 영역을 칭한다. 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;"

- 좌표평면에서의 직선 : 서로 다른 두 좌표가 주어지면 두 점을 지나는 유일한 직선이 결정되며 그 직선은 다음 $3$ 가지 중 하나에 속한다. 

  </blockquote>

  - 수직선(vertical line) : $x$ 축과 수직인 직선이다. 

  - 수평선(horizontal line) : $x$ 축과 평행인 직선이다. 

  - 수직선 또는 수평선이 아닌 직선. 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;"

- 직선의 기울기 : 직선의 방향을 유일하게 특정할 수 있는 방법으로 다음과 같이 정의된다. 

  </blockquote>

  - 기울기 $m$ 은 서로 다른 두 점 $A(x_1, y_1), B(x_2, y_2)$ 를 지나는 직선에 대하여 다음과 같이 정의된다. 

    - 직선이 수직선인 경우 : 기울기 $m$ 를 정의하지 않는다. 

    - 직선이 수직선이 아닐 경우 : $m = \frac{\Delta y}{\Delta x} = \frac{y_2-y_1}{x_2-x_1}$ (단 $\Delta x$ 는 유일한 직선을 특정하는 두 점 $A(x_1, y_1), B(x_2, y_2)$ 의 $x$ 좌표 변화량, $\Delta y$ 는 $y$ 좌표 변화량이다.)

  - 어떤 직선이 $y$ 축에 대하여 얼마나 기울었는지 나타내는 방법이기도 하다. 

  - 쉽게 말해 기울기란 어떤 직선이 $y$ 축에 기운 정도인데, 그것을 그 직선을 특정하는 두 $x$ 좌표가 일정량 변했을 때 두 $y$ 좌표가 일정량 변한 정도의 비율로 나타내겠다는 것이다. (수직선일 때는 $y$ 축에 전혀 기울지 않았다고 생각하면 되려나?)

## 두 점의 거리 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;"

- 거리 : 두 대상이 서로 떨어진 정도를 수치로 나타낸 것이다. 

  </blockquote>

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;"

- 유클리드 거리(Euclidean distance) : 두 점 사이의 거리를 계산할 때 쓰이는 방법이다. 

  </blockquote>

  - 이 거리로 유클리드 공간을 정의할 수 있다. 

  - 이 거리에 대응하는 노름(norm) 을 유클리드 노름(Euclidean norm) 이라 한다. 

  - $1$ 차원 유클리드 거리 : 점 $A(a_1)$ 와 점 $B(a_2)$ 의 거리는 

    $$ |a_1 - a_2| $$

    이다. 

  - $2$ 차원 유클리드 거리 : 점 $A(a_1, b_1)$ 와 점 $B(a_2, b_2)$ 의 거리는 

    $$ \sqrt[]{(a_1 - b_1) ^{2} + (a_2 - b_2) ^{2}} $$

    이다. 

  - $3$ 차원 유클리드 거리 : 점 $A(a_1, b_1, c_1)$ 와 점 $B(a_2, b_2, c_2)$ 의 거리는 

    $$ \sqrt[]{(a_1 - a_2) ^{2} + (b_1 - b_2) ^{2} + (c_1 - c_2)^2} $$

    이다. 

  - 특히 점 $A$ 와 원점 사이의 거리를 

    $$ ||A|| $$

    로 표현하고 점 $A$ 와 점 $B$ 사이의 거리를

    $$ ||A-B|| $$

    로 표현한다. 

  - 예시 

    인공지능에서 데이터가 정해진 카테고리에 속하는지 알기 위해 벡터 공간상에 위치시킨 후 더 가까운 카테고리를 유클리드 거리로 판단한다. 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;"

- 두 점의 거리의 의미 : 논증기하학이 측정으로부터 비롯된 학문이기 때문에 두 대상과의 관계의 기본은 거리이다. 그런데 해석기하학으로 두 점과의 거리를 좌표사이의 거리로 계산할 수 있게 되었다. 

  </blockquote>

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;"

- 수직선에서 두 점의 거리 : 수직선 위의 두 점 $P(x), Q(y)$ 의 거리 $\overline{PQ}$ 는 $|x - y|$ 이다. 

  </blockquote>

  - 좌표가 원점으로부터 단위거리만큼 떨어진 실수에 일대일 대응되는 위치로 정의되었기 때문에 유일하게 특정된 원점을 기준으로 한 위치를 기반으로 대상이 서로 떨어진 정도를 측정할 수 있다. 

  - 점 $P$ 가 좌표값 $P(x)$ 를, 점 $Q$ 가 좌표값 $Q(y)$ 를 가지고 점 $P$ 와 점 $Q$ 가 $d$ 만큼 떨어져있다고 하자. 

    - $x>0, y>0, x<y$ : 거리의 정의와 조건에 따라 원점으로부터 점 $Q(y)$ 까지의 거리는 $x + d$ 이다. 그런데 $Q(y)$ 가 원점으로부터 떨어진 정도는 $y$ 이기 때문에 $x+d = y$ 이다. 따라서 $d = y - x$ 이다.

    - $x>0, y>0, x>y$ : 거리의 정의와 조건에 따라 원점으로부터 점 $P(x)$ 까지의 거리는 $y + d$ 이다. 그런데 $P(x)$ 가 원점으로부터 떨어진 정도는 $x$ 이기 때문에 $y+d = x$ 이다. 따라서 $d = x - y$ 이다.

    - $x<0, y<0, x>y$ : 거리의 정의와 조건에 따라 원점으로부터 점 $Q(y)$ 까지의 거리는 $-x + d$ 이다. 그런데 $Q(y)$ 가 원점으로부터 떨어진 정도는 $-y$ 이기 때문에 $-x+d = -y$ 이다. 따라서 $d = -y + x$ 이다.

    - $x<0, y<0, x<y$ : 거리의 정의와 조건에 따라 원점으로부터 점 $P(x)$ 까지의 거리는 $-y + d$ 이다. 그런데 $P(x)$ 가 원점으로부터 떨어진 정도는 $-x$ 이기 때문에 $-y+d = -x$ 이다. 따라서 $d = -x + y$ 이다.

    - $x>0, y<0$ : 점 $P(x)$ 가 원점에서부터 $x$ 만큼 떨어져 있고 점 $Q(y)$ 가 원점으로부터 $-y$ 만큼 떨어져 있다. 따라서 거리의 정의와 조건에 따라 $d = x + (-y)$ 이다. 

    - $x<0, y>0$ : 점 $P(x)$ 가 원점에서부터 $-x$ 만큼 떨어져 있고 점 $Q(y)$ 가 원점으로부터 $y$ 만큼 떨어져 있다. 따라서 거리의 정의와 조건에 따라 $d = (-x) + y$ 이다. 

  - 이로부터 모든 경우를 대표하는 $d = |x - y|$ 을 얻는다. 

  - 원점과 점 $P(x)$ 와의 거리는 $|x|$ 이다. 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;"

- 좌표평면에서 두 점의 거리 : 좌표평면에서 두 점 $P(x_1, y_1), Q(x_2, y_2)$ 의 거리 $\overline{AB}$ 는 $\sqrt[]{(x_2-x_1)^2 + (y_2-y_1)^2}$ 이다. 

  </blockquote>

## 3차원 좌표계

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;"

- 공간 좌표 : 

  **구체화 필요**

  </blockquote>

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;"

- 3차원 좌표계 : 서로 직교하는 $x$축, $y$축, $z$축으로 정의하여 $xy$, $xz$, $yz$ 평면으로 이루어진 좌표계이다. 

  ![3-coor](https://res.cloudinary.com/eightcruz/image/upload/v1543400108/hmxzjj3qbay9o3zh4w7m.png)

  </blockquote>

## 함수 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;"

- 대응 : 공집합이 아닌 두 집합 $X, Y$ 에 대하여 $X$ 의 원소를 $Y$ 의 원소에 짝짓는 것을 $X$ 에서 $Y$ 로의 대응이라 한다. 

  </blockquote>

  - 집합 $X$ 의 원소 $x$ 가 집합 $Y$ 의 원소 $y$ 에 대응하는 것을 $x \to y$ 로 표현한다. 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;"

- 함수(function) 또는 사상(mapping) : 집합 $X, Y$ 에 대하여 집합 $X$ 의 임의의 한 원소 $x \in X$ 를 집합 $Y$ 의 오직 한 원소 $y \in Y$ 에 대응시키는 이항관계이다. 

  </blockquote>

  - 집합 $X$ 를 정의역이라 하고 집합 $Y$ 를 공역이라 한다. 

  - 정의역 원소 $x$ 에 대응되는 공역 원소 $y$ 를 $x$의 함수값 또는 상(image) 이라 한다.

    - 정의역 원소 $x$ 의 상을 $f(x)$ 로 표기한다. 

  - 모든 상(함수값) 를 포함하는 집합을 치역(range) 이라 한다. 

    - 집합 $\{f(x) | x \in X\}$ 로 표현한다.

    - 치역을 종종 $f(X)$ 로도 표기한다. 

  - 즉 함수는 정의역의 각 원소를 반드시 하나의 공역 원소에 대응시켜야만 성립한다. 

  - 함수는 다음과 같은 형식언어로 표기된다.

    - 함수를 $f : X \to Y$ 로 표기하면 함수 $f$ 가 정의역 $X$, 공역 $Y$ 를 갖는다는 뜻이다. 

    - 함수를 $f : x \mapsto y$ 로 표기하면 정의역 원소 $x$ 가 상 $y$ 에 대응된다는 것이다.

    - 함수 $f$ 에 의하여 정의역 $X$ 의 원소 $x$ 가 공역 $Y$ 의 원소 $y$ 로 대응될 때 

      $$y=f(x)$$

      로 표현한다.

    - $f(x) | _{x=a}$ 라고 하면 $f(x)$ 에 $x=a$ 를 대입한 값이다. 

  - 컴퓨터 공학적으로는 어떤 입력에 대하여 하나의 결과를 출력하는 것이라고 할 수 있다.

    > 프로그래밍에서는 함수의 개념이 수에서 확장되어 문자열, 참거짓, 객체 등을 입력과 출력으로 취급한다. 물론 내부적으로 모두 수이므로 수를 대응시키는 함수 관계라는 점은 변함이 없다. 

  - 예시

    어떤 가족의 구성원을 정의역 $X$, 날짜의 집합을 공역 $Y$ 으로 하여 각 구성원 $x$ 를 그 생년월일 $f(x)$ 로 대응시키는 관계 $f$ 는 함수이다.

    사람이 서로 다른 두 날에 태어났을 수는 없기 때문이다. 

  - 예시

    실수를 그 제곱에 대응시키는 대응 관계 $f: \Re \to \Re, x \mapsto x^2$ 는 함수이다. 

  - 함수는 자연대상의 인과관계를 수학 대상물로 추상화 시킨 것이다.

    - 따라서 세상에 존재하는 모든 인과관계는 함수로 격하(변환)될 가능성을 갖는다. 

    - 모리스 클라인(Morris Kline)은 이렇게 말했다. "함수는 단순한 기호적 수식이 아니다. 함수는 우주의 법칙이고 가장 작은 모래알부터 가장 먼 거리에 있는 거대한 별들의 동작까지 포괄한다." 

    - 정의역을 인과관계의 원인들에 해당하는 원인집합이라 할 수 있고 공역을 인과관계의 결과들에 해당하는 결과집합이라 할 수 있다. 그리고 함수의 이항관계를 원인과 결과 간의 관계라 할 수 있다. 

    - 예시 

      경제학이 창시된 이래 고전경제학자들은 "공급이 수요를 만든다." 라는 세이의 법칙(Say's law) 을 참이라 여겼다. 그러나 1930년 대공황이 발생하고 수많은 사람들이 실업하고 자살하기 시작했다. 그때 케인즈(Keynes) 가 "수요가 공급을 만든다." 라고 하며 정부가 재정 지출을 늘려 총수요를 증가시켜야 한다고 주장했다. 그리고 이렇게 기존의 잘못 파악된 인과관계를 제대로 고친 것이 대공황을 극복하는 게기가 되었다.

      이렇듯 사건의 인과관계를 올바르게 파악하는 것은 매우 중요하며, 올바르게 인과관계를 파악할 수 있는 최선의 방법 중 하나는 자연 대상을 함수로 추상화시켜 수학적으로 엄밀하게 다루는 것이다. 

    - 일반적으로 함수 $f$ 의 정의역의 임의의 두 원소 $x_1, x_2$ 에 대하여 다음의 관계가 성립한다. 

      $$ x_1 = x_2 (원인이 같다.) \Rightarrow f(x_1) = f(x_2) (결과도 같다.) $$

      또한 대우도 성립한다.

      $$ f(x_1) \neq f(x_2) (결과가 다르다.) \Rightarrow x_1 \neq x_2 (원인도 다르다.) $$

      그런데 수학에서는 원인들의 집합에 해당하는 정의역과 결과들의 집합에 해당하는 공역이 수체계의 집합으로 본다. 그러므로 만약 임의의 자연대상을 수로 변환하여 집합으로 묶을 수 있다면 정의역과 공역으로 삼을 수 있고 수로 격하된 자연대상들의 관계 또한 연산으로 표현할 수 있다면 함수라는 형식 언어로 표현할 수 있다. 

      **따라서 수와 연산으로 격하될 수 있는 모든 자연대상과 그것들의 관계는 함수로 표현 가능하다. 그런데 수학의 형식언어는 모두 코드로 변환될 수 있기 때문에 수와 연산으로 격하될 수 있는 임의의 자연대상은 모두 다 프로그램으로 자동화 할 수 있다. 그리고 이것은 역사적으로 거듭되어온 기술의 자연대상 대체가 가속화되다가 언젠가는 초지능이 탄생 할 수도 있다는 기술적 특이점의 가능성을 시사한다.**

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;"

- 정의역(domain) : 함수 $f: X \to Y$ 에서 집합 $X$ 를 $f$ 의 정의역이라 한다.

  </blockquote>

  - 즉 정의역은 함수의 모든 입력값의 집합이다.

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;"

- 공역(codomain) : 함수 $f: X \to Y$ 에서 집합 $Y$ 를 $f$ 의 공역이라 한다.

  </blockquote>

  - 모든 $y \in Y$ 에 대하여 $f(x) = y$ 인 $x \in X$ 가 존재할 필요는 없다.

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;"

- 상(image) 또는 함수값 : 함수 $f: X \to Y$ 에서 정의역 $X$ 의 원소 $x \in X$ 에 대응하는 공역 $Y$ 의 원소 $y \in Y$ 이다.

  </blockquote>

  - 즉 상은 함수 $f: X \to Y$ 의 정의역의 원소 $x \in X$ 에 대한 공역의 원소 

    $$ f(x) \in Y $$

    이다. 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;"

- 원상(preimage) 또는 역상(inverse image) : 함수 $f: X \to Y$ 에서 공역 $Y$ 의 원소 $y \in Y$ 에 대응하는 정의역 $X$ 의 원소 $x \in X$ 이다. 

  </blockquote>

  - 즉 원상은 함수 $f: X \to Y$ 의 공역의 원소 $y \in Y$ 에 대한 정의역의 원소 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;"

- 치역(range) : 함수 $f: X \to Y$ 에서 모든 상(함수값)의 집합 $\{f(x): x \in X\}$ 을 $f$ 의 치역이라 한다.

  </blockquote>

  - 즉 치역은 함수의 모든 함수값의 집합이다.

    > 컴퓨터공학에서 모든 출력값의 집합이라고 할 수 있다. 

  - 정의역의 상(image) 이라고도 부른다. 

  - 치역은 다음과 같은 형식언어로 표현된다. 

    $$ ran f = f(X) = \{f(x) : x \in X\} $$

    - 또한 치역은 공역의 부분집합이므로 

      $$ \{f(x) : x \in X\} \subset Y $$

      이다.

## 함수의 분류 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;"

- 단사함수(injection function) 또는 일대일 함수(one-to-one function) : 정의역의 서로 다른 원소를 공역의 서로 다른 원소로 대응시키는 함수이다.

  </blockquote>

  - 즉 단사함수에서 공역의 각 원소는 정의역의 원소 중 최대 한 원소의 상이다. 

  - 단사함수는 두 집합 $X, Y$ 사이의 함수 $f: X \to Y$ 에 대하여 다음 동치 조건들을 만족시킨다.

    - 임의의 $x, x' \in X$ 에 대하여 $f(x) = f(x') \Rightarrow x = x'$ 이다.

    - 임의의 $x, x' \in X$ 에 대하여 $x \neq x' \Rightarrow f(x) \neq f(x')$ 이다.

  - 단사함수는 다음 두 집합 대응관계의 추상화 그림으로 설명된다. 

    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Injection.svg/330px-Injection.svg.png)

  - 예시 

    $g: \Re \to \Re, x \to x ^{2}$ 로 정의된 함수 $f(x) = x ^{2}$ 는 단사함수가 아니다.

    왜냐하면 $f(1)=1=f(-1)$ 이기 때문이다. 

  - 예시 

    무리수 $e$ 를 밑으로 하는 지수함수 $exp: \Re \to \Re, x \mapsto e ^{x}$ 는 단사함수이다.

    한편 음수에서는 상이 존재하지 않으므로 전사함수는 아니다. 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;"

- 전사함수(onto function, surjection function) : 공역과 치역이 같은 함수이다.

  </blockquote>

  - 전사함수에서 두 집합 $X, Y$ 사이의 함수 $f: X \to Y$ 에 대하여 다음 조건들이 성립하며 서로 동치이다. 

    - 임의의 $y \in Y$ 에 대하여 $f(x) = y$ 인 $x \in X$ 가 존재한다.

    - 공역과 치역이 같다. 즉, $Y=f(X)$ 이다. 

  - 전사함수는 다음 두 집합 대응관계의 추상화 그림으로 설명된다. 

    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Surjection.svg/330px-Surjection.svg.png)

  - 예시 

    실수 집합 $\Re$ 에서 실수 집합 $\Re$ 로 가는 함수 $f$ 가 

    $$ f: \Re \to \Re $$

    $$ f:x \mapsto x ^{2} $$

    로 정의되었다고 하자. 이때 $f$ 의 공역은 $\Re$, $f$ 의 치역은 반개구간 $[0, \infty)$ 이다.

    따라서 $f$ 는 전사함수가 아니다. 

  - 예시 

    실수 집합 $\Re$ 에서 실수 집합 $\Re$ 로 가는 함수 $f$ 가 

    $$ f: \Re \to \Re $$

    $$ f:x \mapsto 2x $$

    로 정의되었다고 하자. 이때 $f$ 의 공역과 치역이 둘 다 $\Re$ 이다.

    따라서 $f$ 는 전사함수이다. 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;"

- 전단사 함수(bijection, bijective function) 또는 일대일 대응 : 두 집합 사이를 중복 없이 모두 일대일 대응시키는 이항관계를 갖는 함수이다.

  </blockquote>

  - 전단사함수에서 두 집합 $X, Y$ 사이의 함수 $f: X \to Y$ 에 대하여 다음 조건들이 성립하며 서로 동치이다. 

    - 전사 함수이면서 단사 함수이다. 

    - 임의의 $y \in Y$ 에 대하여 $f(x) = y$ 인 유일한 $x \in X$ 가 존재한다. 

  - 전단사함수는 다음 두 집합 대응관계의 추상화 그림으로 설명된다. 

    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Bijection.svg/330px-Bijection.svg.png)

  - 예시 

    모든 항등함수는 전단사함수이다. 

  - 예시 

    $f: \Re \to \Re, x \mapsto 2x+1$ 로 정의된 함수 $f(x) = 2x+1$ 는 전단사함수이다. 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;"

- 서로 같은 함수 : 두 함수 $f: X \to Y$, $g: X' \to Y'$ 에 대하여 다음 두 조건이 성립하면 두 함수 $f, g$ 를 서로 같다고 한다. 

  1. 두 함수의 정의역과 공역이 같다. $X = X', Y = Y'$

  2. 정의역의 모든 원소 $x$ 에 대하여 두 함수의 함수값이 같다. $f(x) = g(x)$

  </blockquote>

  - 두 함수가 서로 같다는 것을 $f=g$ 라고 표현한다. 

## 특별한 정의역과 공역을 갖는 함수 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;"

- 실변수 함수(function of a real variable) : 정의역이 실수 집합 $\Re$ 인 함수 

  $$ f: \Re \to X $$

  를 실변수 함수라 한다.

  </blockquote>

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;"

- 실숫값 함수(real-valued function) 또는 실함수(real function) : 공역이 실수 집합 $\Re$ 인 함수 

  $$ f: X \to \Re  $$

  를 실숫값 함수라 한다.

  </blockquote>

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;"

- 복소변수 함수(function of a complex variable) : 정의역이 복소수 집합 $\mathbb{C}$ 인 함수 

  $$ f: \mathbb{C} \to X  $$

  를 복소변수 함수라 한다.

  </blockquote>

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;"

- 복소 함수(complex function) : 공역이 복소수 집합 $\mathbb{C}$ 인 함수 

  $$ f: X \to \mathbb{C}  $$

  를 복소 함수라 한다.

  </blockquote>

## 다변수 함수 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;"

- 다변수함수(multivariate function) : 둘 이상의 독립변수를 갖는 함수이다.

  </blockquote>

  - 일반적으로 다변수 실함수와 다변수 복소함수를 뜻한다. 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;"

- 다변수 실함수 : 다변수 실함수는 $n(n \geq 2)$ 개의 실수 독립 변수들을 오직 하나의 실수값에 대응시키는 규칙이다.

  </blockquote>

  - 즉, 다변수 실함수 $f$ 는 $y,x_1, x_2, \dots, x_n \in \Re$ 에 대하여 $n-$튜플 $(x_1, x_2, \dots, x_n)$ 을 오직 하나의 함수값

    $$ y = f(x_1, x_2, \dots, x_n) $$

    로 대응시키는 규칙이다.

  - 유클리드 공간 $\Re ^{n}$(또는 그 부분집합) 을 정의역으로 갖는 실수값 함수

    $$ f: \Re ^{n} \to \Re $$

    로 정의할 수도 있다. 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;"

- 다변수 복소함수 : 다중 복소수 독립 변수에 대한 복소수 값 함수

  $$ w = f(z_1, z_2, \dots, z_n) $$

  이다.

  </blockquote>

  - 복소수 곱공간 $C ^{n}$(또는 그 부분집합) 을 정의역으로 갖는 복소수 값 함수 

    $$ f: C ^{n} \to C $$

    로 정의할 수도 있다. 

