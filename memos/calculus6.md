# [ccss17.github.io](https://ccss17.github.io)

# Calculus6 Memo

# 매개변수 방정식 

곡선을 두 독립변수 $x, y$ 로 나타내는 것이 아니라 매개변수를 통한 방정식으로 나타내면 훨씬 더 일반적인 곡선을 표현할 수 있다. 

- 매개변수 방정식(parametric equations) : $x, y$ 가 각각 구간 $I$ 의 $t$ 에 대한 함수 

  $$ x = f(t), y = g(t) $$

  일 때, 위 방정식을 곡선의 매개변수 방정식이라 한다. 

- 매개변수 곡선(parametric curve) : 매개변수 방정식의 정의에서 매개변수 방정식으로 정의된 점들의 집합 $(x, y) = (f(t), g(t))$ 을 매개변수 곡선이라 한다. 

- 매개변수 구간(parametric interval) : 매개변수 방정식의 정의에서 정의역 $I$ 를 매개변수 구간이라 한다. 

- 시점(initial point) : 매개변수 방정식의 정의에서 $I$ 가 폐구간이고 $t$ 가 $a \leq t \leq b$ 로 정의되었을 때 점 $(f(a), g(a))$ 를 곡선의 시점이라 한다.

- 종점(terminal point) : 매개변수 방정식의 정의에서 $I$ 가 폐구간이고 $t$ 가 $a \leq t \leq b$ 로 정의되었을 때 점 $(f(b), g(b))$ 를 곡선의 종점이라 한다.

- 매개변수 방정식 예시 

  개구간 $(-\infty , \infty )$ 에서 정의된 $t$ 에 대한 함수 

  $$ x = t ^{2}, y = t+1 $$

  로 정의된 매개변수 방정식의 곡선을 그려보자. 

  $t$ 값에 따라 결정되는 $x, y$ 의 값을 살펴보면 다음과 같다.

  | t | x | y |
  |:---:|:---:|:---:|
  | -3  | 9 | -2 |
  | -2  | 4 | -1 |
  | -1  | 1 | 0 |
  | 0  | 0 | 1 |
  | 1  | 1 | 2 |
  | 2  | 4 | 3 |
  | 3  | 9 | 4 |

  따라서 $xy$ 평면에 그래프를 그려보면 아래와 같다. 

  ![desmos-graph](https://user-images.githubusercontent.com/16812446/79000371-73185f80-7b87-11ea-946b-6f1c94583fb4.png)

  이 그래프는 매개변수 방정식을 $t$ 에 대하여 풀어서 

  $$ x = y ^{2} - 2y +1 $$

  를 얻음으로써 그릴 수도 있다. 

# 이변수 함수의 극한 

- 이변수 함수의 극한 : 함수 $f(x, y)$ 에서 $(x, y)$ 이 $(x_0, y_0)$ 에 한없이 다가갈 때 함수값이 극한값 $L$ 로 다가가는 것은 

  임의의 양수 $\epsilon > 0$ 에 대하여 적당한 양수 $\delta > 0$ 가 존재하여 정의역의 모든 $(x, y)$ 에 대하여 다음을 만족하는 것이다. 

    $$ 0 < \sqrt[]{(x-x_0) ^{2} + (y - y_0) ^{2}} < \delta \Rightarrow  |f(x, y) - L| < \epsilon $$

  - 기호로 다음과 같이 표현한다. 

    $$ \lim_{(x, y) \to (x_0, y_0)} f(x, y) = L $$

- 이변수 함수의 극한의 성질 : 실수 $L, M, k$ 에 대하여 

  $$ \lim_{(x, y) \to (x_0, y_0)} f(x, y) = L\\ \lim_{(x, y) \to (x_0, y_0)} g(x, y) = M $$

  일 때 다음이 성립한다. 

  - 합의 법칙 

    $$\lim_{(x, y) \to (x_0, y_0)} (f(x, y)+g(x, y)) = L + M$$

  - 차의 법칙 

    $$\lim_{(x, y) \to (x_0, y_0)} (f(x, y)-g(x, y)) = L - M$$

  - 실수배 법칙 

    $$\lim_{(x, y) \to (x_0, y_0)} kf(x, y) = kL$$

  - 곱의 법칙 

    $$\lim_{(x, y) \to (x_0, y_0)} (f(x, y)\cdot g(x, y)) = L \cdot M$$

  - 몫의 법칙 

    $$\lim_{(x, y) \to (x_0, y_0)} \frac{f(x, y)}{g(x, y)} = \frac{L}{M}, M \neq 0$$

  - 제곱 법칙 

    $$n \in \mathbb{Z}, n > 0, \lim_{(x, y) \to (x_0, y_0)} [f(x, y)] ^{n} = L ^{n}$$

  - 제곱근 법칙 

    $$n \in \mathbb{Z}, n > 0, \lim_{(x, y) \to (x_0, y_0)} \sqrt[n]{f(x, y)} = L ^{\frac{1}{n}}$$

  - 증명 

    (생략)

- 이변수 함수의 연속 : 이변수 함수 $f(x, y)$ 가 점 $(x_0, y_0)$ 에서 연속이라는 것은 다음 조건과 동치이다.

  1. $f$ 가 $(x_0, y_0)$ 에서 정의되어 있다. 

  2. $\lim_{(x, y) \to (x_0, y_0)} f(x, y)$ 극한값이 존재한다.

  3. $\lim_{(x, y) \to (x_0, y_0)} f(x, y) = f(x_0, y_0)$

- 이변수 합성함수의 연속 : 이변수 함수 $f$ 가 $(x_0, y_0)$ 에서 연속이고 일변수 함수 $g$ 가 $x$ 축 상의 점 $f(x_0, y_0)$ 에서 연속일 때,

  $h(x, y) = g(f(x, y))$ 로 정의된 이변수 합성함수 $h = g \circ f$ 는 연속이다. 

  - 예시 

    합성함수 $e ^{x-y}, \cos \frac{xy}{x^2+1}, \ln (1+x ^{2}y ^{2})$ 는 개구간 $(-\infty , \infty)$ 에서 연속이다. 

- 다변수 함수의 극한과 연속 : 이변수 함수의 극한과 연속의 정의와 비슷하다.

  - 예시 

    $P$ 가 $(x, y, z)$ 를 뜻할 때

    $$ \lim_{P \to (1,0,-1)} \frac{e ^{x+z}}{z ^{2}+\cos \sqrt[]{xy}} = \frac{e ^{1-1}}{(-1)^{2}+\cos 0} = \frac{1}{2} $$

    이다. 

# 상미분과 편미분 

실제로 많은 함수들이 하나의 독립 변수에 의존하는 것이 아니라 두 개 이상의 독립 변수에 종속되기 때문에 많은 경우 일변수 함수에 대한 미분을 다변수 함수로 확장한 미분이 필요하다.

- 상미분(ordinary derivative) : 변수가 하나만 있는 함수에 대한 미분이다.

  - 지금까지 해오던 미분이 바로 상미분이다. 

- $x$ 에 대한 편미분계수 : 이변수 함수 $z = f(x, y)$ 의 점 $(x_0, y_0)$ 에서의 $x$ 에 대한 편미분계수는 

  $$ \frac{\partial f}{\partial x} \bigg | _{(x_0, y_0)} = \frac{d}{dx}f(x, y_0) \bigg | _{x=x_0} =  \lim_{h \to 0} \frac{f(x_0 + h, y_0)-f(x_0,y_0)}{h} $$

  이다. 

  - 기하학적 의미 

    ![캡처](https://user-images.githubusercontent.com/16812446/79021815-7deae880-7bb7-11ea-9ab7-4ed19accc346.PNG)

    https://www.youtube.com/watch?v=ehrGmxqQsjo&t=98s

    위와 같은 곡면의 그래프가 있을 때 $x$ 에 대한 편미분계수 

    $$ \lim_{h \to 0} \frac{f(x_0 + h, y_0)-f(x_0,y_0)}{h} $$

    의 의미는 다음과 같다. 

    먼저 점 $P(x_0, y_0)$ 가 상주하고 있는 교선 위의 또 다른 점 $Q(x_0+h,y_0)$ 를 생각하자. 그러면 점 $P$ 와 점 $Q$ 를 잇는 직선의 기울기는 

    $$ \frac{f(x_0 + h, y_0)-f(x_0,y_0)}{h} $$

    와 같다. $y$ 는 고정되어 있기 때문에 두 점에서의 $y$ 좌표는 $y_0$ 으로 동일하다. 

    이때 $h$ 를 $0$ 에 한없이 가깝게 만들어서 $P$ 와 $Q$ 를 거의 같게 만들면 두 점을 잇는 직선은 곧 곡면의 접선이 되고,

    그때의 기울기는 곧 접선의 기울기가 되는 것이다. 

- $y$ 에 대한 편미분계수 : 이변수 함수 $z = f(x, y)$ 의 점 $(x_0, y_0)$ 에서의 $y$ 에 대한 편미분계수는 

  $$ \frac{\partial f}{\partial y} \bigg | _{(x_0, y_0)} = \frac{d}{dy}f(x_0, y) \bigg | _{y=y_0} =  \lim_{h \to 0} \frac{f(x_0, y_0+h)-f(x_0,y_0)}{h} $$

  이다. 

- 편도함수(partial derivative) : 이변수 함수 $z = f(x, y)$ 의 편도함수는 다음과 같이 정의된다.

  1. $x$ 에 대한 편도함수는 

      $$ f_x(x, y) = \frac{\partial z}{\partial x} = \lim_{h \to 0} \frac{f(x+h, y)-f(x, y)}{h} $$

      이다. 

  2. $y$ 에 대한 편도함수는 

      $$ f_y(x, y) = \frac{\partial z}{\partial y} = \lim_{h \to 0} \frac{f(x, y+h)-f(x, y)}{h} $$

      이다. 

  - 이변수 함수 $f(x, y)$ 의 편미분할 변수를 제외한 나머지 변수를 상수로 취급하여 미분하면 된다.

  - 변수 $x$ 에 대한 다변수 함수 $f(x, y, \dots)$ 의 편미분을 

    $$ f'_x, f_x, \partial _x f, \frac{\partial }{\partial x}f, \frac{\partial f}{\partial x} $$

    등의 형식 언어로 표기한다.

    - 혹은 함수로서 편미분이 종속되는 변수를 강조하기 위해 

      $$ f'_x(x, y, \dots), \frac{\partial f}{\partial x}(x, y, \dots) $$

      로 표기할 수도 있다. 
  
  - 예시 
  
    이변수 함수 $f(x) = x ^{3}+x ^{2}y ^{3}-2y ^{2}$ 일 때 

    $$ f_x(x, y) = 3x ^{2} + 2xy ^{3} \Rightarrow f_x(2, 1) = 16 $$

    $$ f_y(x, y) = 3x ^{2}y ^{2} - 4y \Rightarrow f_x(2, 1) = 8 $$

    이다.

    기하학적으로 각각 곡면 $z = f(x, y)$ 과 평면 $y = 1$ 과 교선 위의 점 $(2, 1, 10)$ 에서의 접선의 기울기가 $16$ 이고 

    곡면 $z = f(x, y)$ 과 평면 $x = 2$ 과 교선 위의 점 $(2, 1, 10)$ 에서의 접선의 기울기가 $8$ 이라는 뜻이다. 

  - 예시 

    밑면의 반지름이 $r$, 높이가 $h$ 인 원뿔의 부피 $V$ 는 

    $$ V = \frac{\pi r ^{2}h}{3} $$

    으로써 두 독립변수 $r, h$ 에 의존하는 종속변수이다.
    
    이 $V$ 를 다변수 함수로 보고 $r$ 에 대해 편미분하면

    $$ \frac{\partial V}{\partial r} = \frac{2 \pi rh}{3} $$

    이고 $h$ 에 대해 편미분하면

    $$ \frac{\partial V}{\partial h} = \frac{\pi r ^{2}}{3} $$

    이다.

- 편도함수의 기하학적 의미 : 이변수 함수 $f(x, y)$ 에 대하여 편도함수의 기하학적 의미는 각각 다음과 같다. 

  ![2v](https://user-images.githubusercontent.com/16812446/78995906-63e0e400-7b7e-11ea-9f1e-76382bc9c548.jpg)

  1. $x$ 에 대한 편도함수 

      $$ f_x(x, y) = \frac{\partial z}{\partial x} = \lim_{h \to 0} \frac{f(x+h, y)-f(x, y)}{h} $$

      의 기하학적 의미 : 곡면 $f(x, y)$ 와 $x$ 축에 평행한 평면과의 교선의 접선의 기울기이다. 

      - 위 그림의 왼쪽의 그래프의 곡면에서 $xy$ 평면에서 수직으로, $x$ 축과 평행하게 곡면을 자르게 되면 여러 개의 교선을 얻을 수 있다. 

      - 그 교선 중 하나가 왼쪽 그래프의 점 $P$ 가 상주하고 있는 곡선이다.

        - 만약 그 곡선보다 좀 더 오른쪽에서 곡면을 자르면 더 짧은 교선을 얻을 수 있고 더 왼쪽에서 곡면을 자르면 더 긴 교선을 얻을 수 있을 것이다. 
      
      - 이 교선에서 어떤 점 $P$ 를 잡아서 접선을 그었을 때 그 접선의 기울기가 편미분계수이다. 

      - 그리고 그 기울기들에 대한 함수가 $x$ 에 대한 편도함수이다. 

  2. $y$ 에 대한 편도함수

      $$ f_y(x, y) = \frac{\partial z}{\partial y} = \lim_{h \to 0} \frac{f(x, y+h)-f(x, y)}{h} $$

      의 기하학적 의미 : 곡면 $f(x, y)$ 와 $y$ 축에 평행한 평면과의 교선의 접선의 기울기

      - 위 그림의 오른쪽의 그래프의 곡면에서 $xy$ 평면에서 수직으로, $y$ 축과 평행하게 곡면을 자르게 되면 여러 개의 교선을 얻을 수 있다. 

      - 그 교선 중 하나가 왼쪽 그래프의 점 $P$ 가 상주하고 있는 곡선이다.
      
      - 이 교선에서 어떤 점 $P$ 를 잡아서 접선을 그었을 때 그 접선의 기울기가 편미분계수이다. 

      - 그리고 그 기울기들에 대한 함수가 $y$ 에 대한 편도함수이다. 

  - 그러면 $x$ 축 방향으로 평행하지도 않고 $y$ 축 방향으로 평행하지도 않고 
  
    $x$ 축으로부터 $60 \degree$ 벌어진 단위 벡터 $u$ 의 방향으로 교선을 잘라서 기울기를 구하는 상황도 생각할 수 있다.

    이것을 단위벡터 $u$ 의 방향도함수라 한다. 

## 여러가지 편도함수 

- 이계 편도함수(second-order partial derivative) : 이변수 함수 $f(x, y)$ 를 두번 미분한 것으로 다음 $4$ 가지 경우로 정의된다. 

  - $x$ 에 대하여 두번 미분할 경우 

    $$ \frac{\partial ^{2} f}{\partial x ^{2}} = \frac{\partial }{\partial x }(\frac{\partial f}{\partial x}) = (f_x)_x = f _{xx} $$

  - $y$ 에 대하여 두번 미분할 경우

    $$ \frac{\partial ^{2} f}{\partial y ^{2}} = \frac{\partial }{\partial y ^{2}}(\frac{\partial f}{\partial y}) = (f_y)_y = f _{yy} $$

  - $y$ 에 대하여 미분하고 $x$ 에 대하여 미분할 경우

    $$ \frac{\partial ^{2} f}{\partial x \partial y } = \frac{\partial }{\partial x}(\frac{\partial f}{\partial y}) = (f_y)_x = f _{yx} $$
  
  - 예시 

    이변수 함수 $f(x, y) = x \cos y + y e ^{x}$ 의 이계 편도함수를 각각 구해보자.

    먼저 일계 편도함수를 구해놓자. 

    $$ \frac{\partial f}{\partial x} = \frac{\partial }{\partial x}(x \cos y + y e ^{x}) = \cos y + y e ^{x} $$

    $$ \frac{\partial f}{\partial y} = \frac{\partial }{\partial y}(x \cos y + y e ^{x}) = -x\sin y + e ^{x} $$

    그러면 이계 편도함수는 다음과 같다. 

    $$ \frac{\partial ^{2}f}{\partial y \partial x} = \frac{\partial }{\partial y}(\frac{\partial f}{\partial x}) = -\sin y + e ^{x} $$

    $$ \frac{\partial ^{2}f}{\partial x \partial y} = \frac{\partial }{\partial x}(\frac{\partial f}{\partial y}) = -\sin y + e ^{x} $$

    $$ \frac{\partial ^{2}f}{\partial x ^{2}} = \frac{\partial }{\partial x}(\frac{\partial f}{\partial x}) = y e ^{x} $$

    $$ \frac{\partial ^{2}f}{\partial y ^{2}} = \frac{\partial }{\partial y}(\frac{\partial f}{\partial y}) = -x \cos y $$

- 혼합 편미분(mixed derivative) : 이변수 함수 $f(x, y)$ 에 대하여 서로 다른 두 변수에 대한 편미분이다.

  - 이계 편도함수에서 $x$ 에 대하여 미분하고 $y$ 에 대하여 미분한 경우

    $$ \frac{\partial ^{2} f}{\partial y \partial x } = \frac{\partial }{\partial y}(\frac{\partial f}{\partial x}) = (f_x)_y = f _{xy} $$

    와 $y$ 에 대하여 미분하고 $x$ 에 대하여 미분한 경우

    $$ \frac{\partial ^{2} f}{\partial x \partial y } = \frac{\partial }{\partial x}(\frac{\partial f}{\partial y}) = (f_y)_x = f _{yx} $$

    를 뜻한다.

- 혼합 편미분 정리(mixed derivative theorem) : 이변수 함수 $f(x, y)$ 와 그 편미분 $f_x, f_y, f _{xy}, f _{yx}$ 가 점 $(a, b)$ 를 포함하는 개구간에서 정의되어 있고 점 $(a, b)$ 에서 연속이라면 

  $$ f _{xy}(a, b) = f _{yx}(a, b) $$

  이다.

  - 예시 
  
    이계 편도함수의 예시에서 이변수 함수 $f(x, y) = x \cos y + y e ^{x}$ 의 혼합 편미분의 변수 순서가 다른 두 결과
  
    $$ \frac{\partial ^{2}f}{\partial y \partial x} = \frac{\partial }{\partial y}(\frac{\partial f}{\partial x}) = -\sin y + e ^{x} $$

    $$ \frac{\partial ^{2}f}{\partial x \partial y} = \frac{\partial }{\partial x}(\frac{\partial f}{\partial y}) = -\sin y + e ^{x} $$

    가 동일한 것은 우연의 일치가 아니다. 혼합 편미분 정리에 의하여 이 둘이 같은 것이다. 

- 이변수 함수의 미분가능성 : 

**구체화 필요**

- 이변수 함성함수의 도함수(chain rule) : 이변수 함수 $w = f(x, y)$ 가 미분가능하고 $t$ 에 대한 함수 $x = x(t), y = y(t)$ 가 미분가능하면

  $t$ 에 대한 이변수 합성함수 $w = f(x(t), y(t))$ 는 미분가능하며 그 도함수는 

  $$ \frac{dw}{dt} = f_x(x(t), y(t)) \cdot x'(t) + f_y(x(t), y(t)) \cdot y'(t) $$

  또는 

  $$ \frac{dw}{dt} = \frac{\partial w}{\partial x}\frac{dx}{dt} + \frac{\partial w}{\partial y}\frac{dy}{dt} $$

  이다. 

  - 증명 

    (생략)**구체화 필요**
  
  - 예시 

    $t$ 에 대한 함수 $x = \cos t, y = \sin t$ 에 에 대한 이변수 합성함수 $w = xy$ 의 도함수를 구해보자.
    
    $$ \frac{dw}{dt} = \frac{\partial w}{\partial x}\frac{dx}{dt} + \frac{\partial w}{\partial y}\frac{dy}{dt} $$

    에서 

    $$ = \frac{\partial (xy)}{\partial x} \cdot \frac{d}{dt}(\cos t) + \frac{\partial (xy)}{\partial y} \cdot \frac{d}{dt}(\sin t) $$

    $$ = (y)(-\sin t) + (x)(\cos t) $$

    $$ = (\sin t)(-\sin t) + (\cos t)(\cos t) $$

    $$ =  -\sin ^{2}t+\cos ^{2}t$$

    $$ = \cos 2t $$

    이다. 

    이 결과는 더욱 $w$ 를 $t$ 에 대한 함수로 풀어서 구할 수도 있다. 

    $$ w = xy = \cos t \sin t = \frac{1}{2}\sin 2t $$

    에서 

    $$ \frac{dw}{dt} = \frac{d}{dt}(\frac{1}{2}\sin 2t) = \frac{1}{2}\cdot 2 \cos 2t = \cos 2t $$

    이다. 

- 일독립변수와 삼매개변수에 대한 함성함수의 도함수(chain rule) : 삼변수 함수 $w = f(x, y, z)$ 가 미분가능하고 $t$ 에 대한 함수 $x = x(t), y = y(t), z = z(t)$ 가 미분가능하면

  $t$ 에 대한 삼변수 합성함수 $w = f(x(t), y(t), z(t))$ 도 미분가능하며 그 도함수는 

  $$ \frac{dw}{dt} = \frac{\partial w}{\partial x}\frac{dx}{dt} + \frac{\partial w}{\partial y}\frac{dy}{dt} + \frac{\partial w}{\partial z}\frac{dz}{dt}$$

  이다. 

  - 증명 

    (생략)**구체화 필요**
  
  - 예시 

    다음과 같이 함수가 주어졌을 때 

    $$w = xy + z, x = \cos t, y = \sin t, z = t$$

    $dw/dt$ 를 구해보자. 

    $$ \frac{dw}{dt} = \frac{\partial f}{\partial x}\frac{dx}{dt} + \frac{\partial f}{\partial y}\frac{dy}{dt} + \frac{\partial w}{\partial z}\frac{dz}{dt}$$

    에서 

    $$ = (y)(-\sin t) + (x)(\cos t)+(1)(1) $$

    $$ = (\sin t)(-\sin t) + (\cos t)(\cos t)+1 $$

    $$ = -\sin ^{2} t + \cos ^{2} t+1 $$

    $$ = 1+\cos 2t $$

    이므로 

    $$ \therefore \frac{dw}{dt} = 1+\cos 2t $$

    이다. 

- 이독립변수와 삼매개변수에 대한 함성함수의 편도함수(chain rule) : 삼변수 함수 $w = f(x, y, z)$ 가 미분가능하고 $r, s$ 에 대한 함수 $x = x(r, s), y = y(r, s), z = z(r, s)$ 가 미분가능하면,

  이 $4$ 가지 함수는 모두 미분 가능하고 $w$ 는 $r$ 과 $s$ 에 대하여 각각 다음의 편도함수를 가진다. 

  $$ \frac{\partial  w}{\partial  r} = \frac{\partial w}{\partial x}\frac{\partial  x}{\partial  r} + \frac{\partial w}{\partial y}\frac{\partial  y}{\partial  r} + \frac{\partial w}{\partial z}\frac{\partial  z}{\partial  r}$$

  $$ \frac{\partial  w}{\partial  s} = \frac{\partial w}{\partial x}\frac{\partial  x}{\partial  s} + \frac{\partial w}{\partial y}\frac{\partial  y}{\partial  s} + \frac{\partial w}{\partial z}\frac{\partial  z}{\partial  s}$$

  - 증명 

    첫번째 편도함수는 $s$ 를 고정시킴으로써 $r$ 을 일독립변수와 삼매개변수에 대한 함성함수의 도함수의 $t$ 처럼 다룸으로써 얻을 수 있다. 

    두번째 편도함수도 $r$ 를 고정시킴으로써 $s$ 을 일독립변수와 삼매개변수에 대한 함성함수의 도함수의 $t$ 처럼 다룸으로써 얻을 수 있다. 
  
  - 예시 

    $$ w = x + 2y + z ^{2}, x = \frac{r}{s}, y = r ^{2} + \ln s, z = 2r $$

    일때, $\frac{\partial w}{\partial r}$ 과 $\frac{\partial w}{\partial s}$ 을 구해보자. 

    $$ \frac{\partial  w}{\partial  r} = \frac{\partial w}{\partial x}\frac{\partial  x}{\partial  r} + \frac{\partial w}{\partial y}\frac{\partial  y}{\partial  r} + \frac{\partial w}{\partial z}\frac{\partial  z}{\partial  r}$$

    에서 

    $$ = (1)(\frac{1}{s}) + (2)(2r) + (2z)(2) $$

    $$ = \frac{1}{s} + 4r + (4r)(2) = \frac{1}{s} + 12r $$

    이다. 
    
    그리고

    $$ \frac{\partial  w}{\partial  s} = \frac{\partial w}{\partial x}\frac{\partial  x}{\partial  s} + \frac{\partial w}{\partial y}\frac{\partial  y}{\partial  s} + \frac{\partial w}{\partial z}\frac{\partial  z}{\partial  s}$$

    에서 

    $$ = (1)(-\frac{r}{s^2}) + (2)(\frac{1}{s}) + (2z)(0) = \frac{2}{s} - \frac{r}{s^2} $$

    이다.

- 이독립변수와 이매개변수에 대한 함성함수의 편도함수(chain rule) : 이변수 함수 $w = f(x, y)$ 가 미분가능하고 $r, s$ 에 대한 함수 $x = x(r, s), y = y(r, s)$ 가 미분가능하면,

  이 $3$ 가지 함수는 모두 미분 가능하고 $w$ 는 $r$ 과 $s$ 에 대하여 각각 다음의 편도함수를 가진다. 

  $$ \frac{\partial  w}{\partial  r} = \frac{\partial w}{\partial x}\frac{\partial  x}{\partial  r} + \frac{\partial w}{\partial y}\frac{\partial  y}{\partial  r} $$

  $$ \frac{\partial  w}{\partial  s} = \frac{\partial w}{\partial x}\frac{\partial  x}{\partial  s} + \frac{\partial w}{\partial y}\frac{\partial  y}{\partial  s} $$

- $n$ 개의 독립변수와 $m$ 개의 매개변수에 대한 다변수 합성함수의 편도함수(chain rule) : 유한개의 매개변수 $x_1, x_2, \dots, x_m$ 에 대한 다변수 함수 $w = f(x_1, x_2, \dots, x_m)$ 가 미분가능하고,

  $n$ 개의 독립변수 $p_1, p_2, \dots, p_n$ 에 대한 함수 $x_1, x_2, \dots, x_m$ 도 미분가능하면,

  $w$ 가 미분가능하고 $p_1, p_2, \dots, p_n$ 에 대한 함수들도 미분가능하며

  각각의 독립변수에 대한 $w$ 의 편도함수는 다음과 같다. 

  $$ \frac{\partial  w}{\partial p_1} = \frac{\partial w}{\partial x_1}\frac{\partial  x_1}{\partial  p_1} + \frac{\partial w}{\partial x_2}\frac{\partial  x_2}{\partial  p_1} + \dots + \frac{\partial w}{\partial x_m}\frac{\partial  x_m}{\partial  p_1}$$

  $$ \frac{\partial  w}{\partial p_2} = \frac{\partial w}{\partial x_1}\frac{\partial  x_1}{\partial  p_2} + \frac{\partial w}{\partial x_2}\frac{\partial  x_2}{\partial  p_2} + \dots + \frac{\partial w}{\partial x_m}\frac{\partial  x_m}{\partial  p_2}$$

  $$ \vdots $$

  $$ \frac{\partial  w}{\partial p_n} = \frac{\partial w}{\partial x_1}\frac{\partial  x_1}{\partial  p_n} + \frac{\partial w}{\partial x_2}\frac{\partial  x_2}{\partial  p_n} + \dots + \frac{\partial w}{\partial x_m}\frac{\partial  x_m}{\partial  p_n}$$

# 벡터 해석학

과학 공학, 금융, 의학, 더 높은 수준의 수학 같은 현실 세계에서는 일변수 함수가 아닌 다변수 함수가 훨씬 자주 쓰인다. 이 파트는 다변수 함수의 미적분을 소개하기 위한 사전 지식을 가르친다. 

- 표준점(standard poitn) 에 위치한 벡터 : 시점이 원점에 위치한 벡터이다. 

  - 벡터의 속성은 크기와 방향이다. 즉, 위치는 벡터의 속성이 아니다. 이때 벡터를 정확하게 대수적으로 기술하기 위하여 시점을 원점에 위치시킨 다음 종점의 좌표로 벡터를 특정한다.

    - 이것을 표준점에 위치한 벡터라고 한다. 
  
- 벡터 성분 표기(component form) : $2$ 차원, $3$ 차원일 경우 각각 다음과 같이 정의된다. 

  - 벡터 $v$ 가 $2$ 차원 평면에서 정의된 벡터이고 그 시점을 원점에 위치했을 때 종점의 좌표 $(v_1, v_2)$ 라고 하면 

    벡터 $v$ 의 성분을 실수 순서쌍(2-튜플)

    $$ \big < v_1, v_2 \big > $$

    로 표기한다. 
  
  - 벡터 $v$ 가 $3$ 차원 공간에서 정의된 벡터이고 그 시점을 원점에 위치했을 때 종점의 좌표 $(v_1, v_2, v_3)$ 라고 하면 

    벡터 $v$ 의 성분을 실수 순서쌍(3-튜플)

    $$ \big < v_1, v_2, v_3 \big > $$

    로 표기한다. 
  
  - 이때 $v_1, v_2, v_3$ 을 벡터의 성분(component) 이라 한다. 

  - 예시 

    $3$ 차원 공간에서 정의된 벡터 $v$ 의 시점이 $P(x_1, y_1, z_1)$ 이고 종점이 $Q(x_2, y_2, z_2)$ 라 하자. 
    
    이 벡터 $v$ 의 성분은 시점을 원점에 위치시킨 후의 종점의 좌표이기 때문에

    $$ v_1 = x_2 - x_1, v_2 = y_2 - y_1, v_3 = z_2 - z_1 $$

    이다. 따라서 

    $$ v = \big<x_2-x_1, y_2-y_1, z_2-z_1 \big> $$

    이다.

- 벡터의 성분(component) : 벡터 성분 표기에서 $v_1, v_2, v_3$ 을 벡터의 성분이라 한다. 
  
- 벡터의 길이(magnitude or length of vector) : $2$ 차원, $3$ 차원일 경우 각각 다음과 같이 정의된다. 

  - $2$ 차원 공간에서 정의된 임의의 벡터 $\overrightarrow{PQ}$ 를 표준점에 위치시켜서 그 성분을

    $$ v = \big<x_2-x_1, y_2-y_1\big> $$

    로 표기할 수 있다면 벡터의 길이는 

    $$ |v| = ||v|| = \sqrt[]{v _{1} ^{2} + v _{2} ^{2} } = \sqrt[]{(x _{2} - x _{1}) ^{2} + (y _{2} - y _{1}) ^{2} } $$

    이다. 

  - $3$ 차원 공간에서 정의된 임의의 벡터 $\overrightarrow{PQ}$ 를 표준점에 위치시켜서 그 성분을

    $$ v = \big<x_2-x_1, y_2-y_1, z_2-z_1 \big> $$

    로 표기할 수 있다면 벡터의 길이는 

    $$ |v| = ||v|| = \sqrt[]{v _{1} ^{2} + v _{2} ^{2} + v _{3} ^{2}} = \sqrt[]{(x _{2} - x _{1}) ^{2} + (y _{2} - y _{1}) ^{2} + (z _{2} - z _{1}) ^{2}} $$

    이다. 
  
  - 벡터 $v$ 의 길이를 $|v|$ 또는 $||v||$ 로 표기한다. 
  
- 영 벡터(zero vector) : 길이가 $0$ 인 벡터로써 

  $$ \big<0, 0 \big> $$

  또는 

  $$ \big< 0,0,0 \big > $$

  이다. 

## 벡터 대수 연산 

(스칼라는 단순히 실수로 생각하면 된다.)

- 벡터 대수 연산 : 벡터 $u, v$ 를 다음과 같이 정의했을 때 덧셈과 스칼라배가 다음과 같이 정의된다. 

  $$ u = \big <u_1, u_2, u_3 \big >, v = \big < v_1, v_2, v_3 \big > $$

  - 벡터 덧셈 : $u + v = \big <u_1+v_1, u_2+v_2 + u_3+v_3 \big >$

    - 예시 

      해석기학적인 벡터 덧셈은 논증기하적으로 벡터 덧셈을 정의했을 때와 같이 

      벡터 $u, v$ 를 더해 벡터 $w$ 가 나오는데, 각각

      삼각형의 형태로 덧셈이 이루어지는 경우

      ![캡처](https://user-images.githubusercontent.com/16812446/79008020-73205b80-7b97-11ea-9e2a-b085f47baf47.PNG)

      와 평행사변형의 형태로 덧셈이 이루어지는 경우

      ![캡처](https://user-images.githubusercontent.com/16812446/79008186-c5617c80-7b97-11ea-8f0a-4bba658bd881.PNG)

      와 같다. 
    
    - 특히 위 예시에서 덧셈의 결과인 $w$ 를 합 벡터(resultant vector) 라 한다. 

  - 스칼라배 : $ku = \big <ku_1, ku_2, ku_3 \big >$

    - 벡터 $u$ 에 스칼라배를 하면 벡터가 늘어날 수도 있고 줄어들 수도 있다.

    - 특히 스칼라 $k$ 가 음수면 벡터의 방향이 바뀐다.

- 스칼라배 벡터의 길이 : 벡터 $u$ 에 스칼라배 $k$ 를 한 벡터 $ku$ 의 길이 $|ku|$ 는 

  $$ |ku| = \sqrt[]{(ku_1) ^{2}+(ku_2) ^{2}+(ku_3)^{2}} = \sqrt[]{k ^{2}(u_1 ^{2}+u_2 ^{2}+u_3 ^{2})} = \sqrt[]{k ^{2}}\sqrt[]{u_1 ^{2}+u_2 ^{2}+u_3 ^{2}} = |k||u| $$

  이다. 

  - 즉, $ku$ 의 길이는 벡터 $u$ 의 길이에 정확히 $k$ 배한 길이와 같다. 

  - 특히 벡터 $u$ 에 $-1$ 스칼라를 곱한 벡터 $-u$ 는 같은 길이에 정반대 방향을 가르킨다.

- 단위 벡터(unit vector) : 길이가 $1$ 인 벡터이다. 

  - 즉 단위 벡터란 벡터

    $$ v = \big<x_2-x_1, y_2-y_1, z_2-z_1 \big> $$

    에 대한 벡터 길이

    $$ |v| = \sqrt[]{(x _{2} - x _{1}) ^{2} + (y _{2} - y _{1}) ^{2} + (z _{2} - z _{1}) ^{2}} = 1 $$

    을 만족하는 모든 벡터를 뜻한다. 

- 표준 단위 벡터(standard unit vector) : 표준 단위 벡터는 길이가 $1$ 인 다음의 특수한 $3$ 가지 경우의 벡터를 뜻한다. 

  $$ i = \big <1, 0, 0 \big >, j = \big <0, 1, 0 \big >, k = \big <0, 0, 1 \big > $$

  - 그 어떠한 벡터도 표준 단위 벡터의 선형결합으로 표현될 수 있다. 그러므로 표준 단위 벡터는 모든 벡터를 생성한다. 

    - 예시
    
      즉, 임의의 벡터 $v = \big <v_1,v_2, v_3 \big >$ 는 다음과 같이 표준 단위 벡터의 선형 결합으로 표현될 수 있다. 

      $$ v = \big <v_1,v_2, v_3 \big > = \big <v_1,0,0\big > + \big <0,v_2,0\big > + \big <0,0,v_3\big > $$

      $$ = v_1\big <1,0,0\big > + v_2\big <0,1,0\big > + v_3\big <0,0,1\big > $$

      $$ = v_1i + v_2j + v_3k $$
  
- 벡터의 $i$ 성분(i-component) : 표준 단위 벡터의 예시에서 스칼라 $v_1$ 을 벡터 $v$ 의 $i$ 성분이라한다.

  - 즉 $i$ 성분은 $(1, 0, 0)$ 또는 $\big < 1, 0, 0 \big >$ 이다.
  
  - 또 $i$ 벡터를 $x$ 축 상의 단위벡터라고도 한다. 

- 벡터의 $j$ 성분(j-component) : 표준 단위 벡터의 예시에서 스칼라 $v_2$ 을 벡터 $v$ 의 $j$ 성분이라한다.

  - 즉 $j$ 성분은 $(0, 1, 0)$ 또는 $\big < 0, 1, 0 \big >$ 이다.
  
  - 또 $j$ 벡터를 $y$ 축 상의 단위벡터라고도 한다. 

- 벡터의 $k$ 성분(k-component) : 표준 단위 벡터의 예시에서 스칼라 $v_3$ 을 벡터 $v$ 의 $k$ 성분이라한다.

  - 즉 $k$ 성분은 $(0, 0, 1)$ 또는 $\big < 0, 0, 1 \big >$ 이다.
  
  - 또 $k$ 벡터를 $z$ 축 상의 단위벡터라고도 한다. 

- 벡터의 $i,j,k$ 성분으로의 벡터 표기 : 점 $P_1(x_1, y_1, z_1)$ 에서 점 $P_2(x_2, y_2, z_2)$ 으로 이어져있는 벡터는 

  $$ \overrightarrow{P_1P_2} = (x_2 - x_1)i + (y_2-y_1)j+(z_2-z_1)k $$

  로 표기할 수 있다. 

  - 따라서

    $$ \overrightarrow{P_1P_2} = \big <x_2 - x_1 , y_2-y_1,z_2-z_1 \big >  = (x_2 - x_1)i + (y_2-y_1)j+(z_2-z_1)k $$

    이다.

- 벡터 방향으로의 단위 벡터 : 영벡터가 아닌 벡터 $v \neq 0$ 와 길이 $|v|$ 에 대하여 

  $$ \frac{v}{|v|} $$

  가 벡터 $v$ 방향으로의 단위 벡터이다. 

  - 단위 벡터는 어떤 방향이든지 길이가 $1$ 인 벡터인 것을 기억하자.
  
    그러면 임의의 벡터 $u$ 에 그것의 길이 $|u|$ 의 역수 $|\frac{1}{u}|$ 을 스칼라배 한다면 벡터 $u$ 의 길이는 $1$ 이 된다.

    $$ \bigg | \frac{1}{|v|}v \bigg | = \frac{1}{|v|}|v| = 1 $$

    이기 때문이다. 

    1. $\bigg | \frac{1}{|v|}v \bigg |$ 는 벡터 $v$ 에 스칼라배 $\frac{1}{|v|}$ 를 한 길이를 뜻한다.
    
        - 기호 $||$ 의 의미를 기억하자!
    
    2. 그리고 벡터 $u$ 에 스칼라배 $k$ 를 한 벡터 $ku$ 의 길이 $|ku|$ 는 

        $$ |ku| = |k||u| $$

        임을 기억하자. 
        
        그러면 

        $$ k = \bigg | \frac{1}{|v|}v \bigg |, u = v $$

        로 두면

        $$ \bigg | \frac{1}{|v|}v \bigg | = \frac{1}{|v|}|v| $$

        임을 알 수 있다.
    
    3. 마지막으로 $|v|$ 와 $\frac{1}{|v|}$ 는 단지 스칼라, 즉 실수이므로 우리가 너무 잘 아는 실수의 곱을 적용하여 

        $$ \frac{1}{|v|}|v| = 1$$

        이 된다. 

  - 예시 

    점 $P_1(1,0,1)$ 에서 점 $P_2(3,2,0)$ 로 이어진 벡터 $v$ 방향으로의 단위벡터 $u$ 를 찾자.

    $$ \overrightarrow{P_1P_2} = (3-1)i+(2-0)j+(0-1)k = 2i+2j-k $$

    $$ |\overrightarrow{P_1P_2}| = \sqrt[]{2 ^{2} + 2 ^{2} +(-1)^{2}} = \sqrt[]{4+4+1} = \sqrt[]{9} = 3 $$

    이므로

    $$ \therefore  u = \frac{\overrightarrow{P_1P_2}}{|\overrightarrow{P_1P_2}|} = \frac{2i+2j-k}{3} = \frac{2}{3}i + \frac{2}{3}j - \frac{1}{3}k $$

    이다.

# 기울기 벡터와 방향도함수

- 스칼라장(scalar field) : 공간 상의 모든 점에 스칼라가 대응되어 있는 분포이다.

  - 유클리드 공간 $\Re ^{n}$ 에서 스칼라장은 

    $$ F: A \in \Re ^{n} \to \Re, (a_1, a_2, \dots, a_n) \mapsto a $$

    으로 정의되는 사상(함수) 로써 정의역 $A$ 의 모든 원소 $x \in A$ 에 스칼라(실수), 즉 $F(x)$ 를 대응시킨다. 

  - 예시 

    공간 상의 온도 분포는 스칼라장의 일종이다.

    호수의 수압 분포도 스칼라장의 일종이다. 

    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Scalar_field.png/330px-Scalar_field.png)

    위 그림은 스칼라장의 일종으로 색채에 대응하는 숫자를 색으로 표현한 것이다. 

- 기울기 벡터(gradient vector) : 스칼라 함수 $f(x, y)$ 의 기울기는 벡터함수 

  $$ \text{grad} f = \nabla f = \frac{\partial f}{\partial x}i + \frac{\partial f}{\partial y}j =  \bigg <\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}\bigg > $$

  로써 스칼라장의 최대 증가율을 나타내는 벡터장이다. 

  - 다음 그림에서

    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Gradient2.svg/450px-Gradient2.svg.png)

    회색의 밝기가 큰 스칼라를 나타낸다. 이때 화살표는 기울기, 즉 스칼라장에서 최대 증가율을 나타낸다.

  - 형렬적 표기로

    $$ \nabla f(x, y) = \begin{bmatrix} \dfrac{\partial f}{\partial x}\\ \\ \dfrac{\partial f}{\partial y} \end{bmatrix} $$

    로 쓸 수 있고 표준 단위 벡터 $i = \big <1, 0 \big >, j = \big < 0, 1\big >$ 를 각각 다음의 행렬로 표기할 수 있다. 

    $$ \begin{bmatrix} 1\\0 \end{bmatrix} , \begin{bmatrix} 0\\1 \end{bmatrix} $$

    이 행렬의 스칼라배로써 

    $$ \nabla f = \frac{\partial f}{\partial x}i + \frac{\partial f}{\partial y}j $$

    의 표기가 나온 것이다.

  - $\frac{\partial f}{\partial x}$ 의 기하학적 의미를 기억하자. 

    ![2v](https://user-images.githubusercontent.com/16812446/78995906-63e0e400-7b7e-11ea-9f1e-76382bc9c548.jpg)

    그것은 위 그림의 왼쪽 그래프와 같이 곡면 $f(x, y)$ 와 $x$ 축에 평행한 평면과의 교선의 접선의 기울기였다. 

    그러한 교선은 수없이 많은데 $y$ 에 따라 점 $P(x_0, y_0)$ 가 상주하고 있는 교선을 얻었다고 하자.

    이제 이 교선에서 $x$ 에 따라 점 $P$ 가 결정되어서 이 $P$ 에서 $x$ 축에 평행한 접선의 기울기가 편미분계수 

    $$ \frac{\partial f}{\partial x} \bigg | _{(x_0, x_0)} $$

    의 의미였다. 

    그리고 그러한 특수한 점 $P(x_0, y_0)$ 을 일반화하여 일반적인 점 $P(x, y)$ 로 만들자. 이 독립변수 $x, y$ 로 결정되는 점 $P$ 에 따른 기울기를 함수로 표현한 것이 

    $$ \frac{\partial f}{\partial x} $$

    의 의미였고 이것을 $x$ 에 관한 편도함수라고 불렀다. 
  
  - 그런데 $\frac{\partial f}{\partial x}$ 을 벡터의 관점에서 표현하면 "함수 $f$ 의 표준 단위 벡터 $i$ 방향으로의 변화율" 이라고 표현 할 수 있다. 

    - 표준 단위 벡터 $i$ 는 $\big <1, 0, 0 \big >$ 이었고 이것은 $x$ 축 상의 단위벡터 였다.
    
      그런데 $x$ 에 관한 편도함수는 곡면을 $x$ 축과 평행하도록 잘라서 교선을 얻어서 그 위의 기울기를 구하는 것과 같다. 

      또한 편도함수는 도함수의 일종이고 도함수는 함수의 변화율을 나타내는 것임을 기억하자.

      그렇다면 결론적으로 
      
      $$\frac{\partial f}{\partial x}$$

      를 "$x$ 축과 평행하도록 교선을 만든다" 고 할 수 있고 
      
      이것을 다시 "함수 $f$ 의 벡터 $i$ 방향으로의 변화율" 을 구한다고 표현할 수 있다. 
  
  - 그런데 $\frac{\partial f}{\partial x}$ 을 또 다시 방향도함수의 정의에 따라서 "함수 $f$ 의 벡터 $i$ 방향의 방향도함수" 라고도 표현할 수 있다. 

    - 즉 함수 $f$ 의 $x$ 에 대한 편도함수는 방향도함수의 벡터 $i$ 방향으로의 아주 특수한 경우라고 할 수 있다. 

  - 그러면 $\frac{\partial f}{\partial y}$ 도 마찬가지로 방향도함수의 정의에 따라서 "함수 $f$ 의 벡터 $j$ 방향의 방향도함수" 라고도 표현할 수 있다. 

    - 표준 단위 벡터 $j$ 는 $\big <0, 1, 0 \big >$ 이었고 이것은 $y$ 축 상의 단위벡터 였다.

    - 즉 함수 $f$ 의 $y$ 에 대한 편도함수는 방향도함수의 벡터 $j$ 방향으로의 아주 특수한 경우라고 할 수 있다. 
  
  - 예시 

    $f(x, y, z) = xy ^{2} + 2x ^{2} + z ^{3}$ 일 때 $\nabla f(1, 2, 3)$ 를 구해보자. 

    먼저 기울기 벡터는 

    $$ \nabla f = \bigg < \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z} \bigg > $$

    에서 

    $$ = \bigg < y ^{2}+4x, 2xy, 3z ^{2} \bigg > $$

    이다. 그러므로 

    $$ \therefore \nabla f(1, 2, 3) = \big < 8, 4, 27\big > $$
  
  - 기울기 벡터 값의 의미 

    이러한 기울기 벡터값은 함수의 증가율이 최대가 되는 방향을 가르키는 벡터이다! 

- 방향도함수(directional derivative) : 스칼라 함수 $f(x, y)$ 에 대하여 단위벡터 $u = \big < \cos \theta , \sin \theta \big >$ 방향의 방향도함수는 

  $$ D _{u} f(x, y) = \lim_{h \to 0} \frac{f(x + h \cos \theta , y + h \sin \theta )-f(x, y)}{h} $$

  이다. 

  - 위 정의는 다음 그림과 같이

    ![캡처](https://user-images.githubusercontent.com/16812446/79028349-9a445080-7bca-11ea-8ac9-596994fdd522.PNG)

    https://www.youtube.com/watch?v=ehrGmxqQsjo&t=98s

    단위벡터 $u = \big < \cos \theta , \sin \theta \big >$ 의 방향이 $x$ 축과 이루는 각이 $\theta$ 일 때 

    $$ D _{u} f(x, y) = \lim_{h \to 0} \frac{f(x + h \cos \theta , y + h \cos (\frac{\pi }{2}-\theta) )-f(x, y)}{h} $$

    와 같이 정의된 방향도함수에서 

    $$ \cos \bigg  (\frac{\pi }{2} - \theta \bigg ) = \sin \theta $$

    를 사용하여 간단하게 만든 것이다. 
    
    $h$ 는 두 점 $P, Q$ 와의 거리이다. 

    - 위 그래프의 점 $P, Q$ 의 거리를 $h$ 라 하고 두 점을 $xy$ 평면으로 내려 떨어뜨리면

      ![캡처](https://user-images.githubusercontent.com/16812446/79028367-ae884d80-7bca-11ea-9268-0e46b10e1dd6.PNG)

      https://www.youtube.com/watch?v=ehrGmxqQsjo&t=98s

      이와 같이 되는데 기존의 도함수의 정의

      $$ \lim_{h \to 0} \frac{f(x + \Delta x, y + \Delta y )-f(x, y)}{h} $$

      에서 $\Delta x, \Delta y$ 를 푸는 것이 목적이다. 

      단위벡터 $u$ 의 방향이 $x$ 축으로부터 $\theta$ 만큼 벌어져있기 때문에 위 그림처럼 한 각을 $\theta$ 로 하고 밑변과 높이의 길이를 $\Delta x, \Delta y$ 로 하는 직각 삼각형을 생각할 수 있다. 

      이 직각삼각형의 빗변의 길이는 두 점 $P, Q$ 와의 거리와 같으므로 $h$ 이다. 

      이때 이 직각삼각형의 한 각 $\theta$ 에서 $\cos \theta$ 는 $\theta$ 를 기준으로 빗변에 대한 밑변의 비율이기 때문에

      $$ \cos \theta = \frac{\Delta x}{h} $$

      이다. 그러므로 

      $$ \therefore \Delta x = h \cdot \cos \theta $$

      이다. 또한 이 직각삼각형의 한 각 $\theta$ 에서 $\sin \theta$ 는 $\theta$ 를 기준으로 빗변에 대한 높이의 비율이기 때문에

      $$ \sin \theta = \frac{\Delta y}{h} $$

      이다. 그러므로

      $$ \therefore \Delta y = h \cdot \sin \theta $$

      이다.

      따라서 최종적으로 단위벡터 $u = \big < \cos \theta , \sin \theta \big >$ 의 방향에서 점 $Q$ 가 점 $P$ 에 한없이 다가갈 때, 즉 두 점의 거리 $h$ 가 $0$ 에 한없이 다가갈 때 일반적인 도함수의 정의는

      $$ \lim_{h \to 0} \frac{f(x + \Delta x, y + \Delta y )-f(x, y)}{h} $$

      으로부터

      $$ \therefore  D _{u} f(x, y) = \lim_{h \to 0} \frac{f(x + h \cos \theta , y + h \sin \theta )-f(x, y)}{h} $$

      가 된다.

  - 따라서 $x$ 축과 이루는 각이 $\alpha$ 이고 $y$ 축과 이루는 각이 $\beta$ 일 때 

    $$ D _{u} f(x, y) = \lim_{h \to 0} \frac{f(x + h \cos \alpha  , y + h \cos  \beta  )-f(x, y)}{h} $$

    라고 하기도 한다. 
  
  - 예시 

    $\theta = 0$ 일 때, 즉 $u = i = \big < 1, 0, 0\big >$ 일 때, 그러니까 단위벡터 $u$ 의 방향이 $x$ 축 일때,

    함수 $f(x, y)$ 의 방향도함수는

    $$ D _{u} f(x, y) = \lim_{h \to 0} \frac{f(x + h \cos \theta , y + h \sin \theta )-f(x, y)}{h} $$

    에서

    $$ D _{u} f(x, y) = \lim_{h \to 0} \frac{f(x + h , y )-f(x, y)}{h} $$

    가 된다. 

    이것은 이변수 함수의 $x$ 에 대한 편도함수

    $$ \frac{\partial f}{\partial x} $$
    
    의 정의와 같다.
    
    그러므로 $x$ 에 대한 편도함수는 방향도함수의 매우 특수한 경우인 것이다. 

  - 예시 

    $\theta = \frac{\pi}{2}$ 일 때, 즉 $u = j = \big < 0, 1, 0\big >$ 일 때, 그러니까 단위벡터 $u$ 의 방향이 $y$ 축일 때,

    함수 $f(x, y)$ 의 방향도함수는

    $$ D _{u} f(x, y) = \lim_{h \to 0} \frac{f(x + h \cos \theta , y + h \sin \theta )-f(x, y)}{h} $$

    에서

    $$ D _{u} f(x, y) = \lim_{h \to 0} \frac{f(x , y + h )-f(x, y)}{h} $$

    가 된다. 

    이것은 이변수 함수의 $x$ 에 대한 편도함수

    $$ \frac{\partial f}{\partial y} $$
    
    의 정의와 같다.
    
    그러므로 $y$ 에 대한 편도함수는 방향도함수의 매우 특수한 경우인 것이다. 

- 삼독립변수에 대한 방향도함수 : 삼변수 함수 $f(x, y, z)$ 에 대하여 단위벡터 $u = \big < \cos \alpha , \cos \beta , \cos \gamma  \big >$ (단, $\cos ^{2}\alpha +\cos ^{2}\beta +\cos ^{2}\gamma =1$) 방향으로의 방향도함수는

  $$ D _{u}f(x,y,z) = \lim_{h \to 0} \frac{f(x+h \cos \alpha , y + h \cos \beta , z + h \cos \gamma )-f(x,y,z)}{h} $$

  이다. 

  - 이때 $\alpha$ 는 단위벡터 $u$ 가 $x$ 축과 이루는 각,
  
    $\beta$ 는 단위벡터 $u$ 가 $y$ 축과 이루는 각,
    
    $\gamma$ 는 단위벡터 $u$ 가 $z$ 축과 이루는 각이다.

  - $\cos ^{2}\alpha +\cos ^{2}\beta +\cos ^{2}\gamma =1$ 의 조건은 단위벡터 $u$ 의 길이 $|u|$ 가 $1$ 임을 보장한다. 


  - 즉 $x, y, z$ 의 증분을 각각 다음과 같이 정의한 것이다. 

    $$ \Delta x = h \cos \alpha , \Delta y = y + h \cos \beta , \Delta z= z + h \cos \gamma $$

- 방향도함수의 계산 

**구체화 필요** 

# 선형화

- 선형화(linearization) : 함수 $f$ 가 $x=a$ 에서 미분가능할 때 $x=a$ 에서의 접선의 방정식

  $$ L(x) = f'(a)(x-a) + f(a) $$

  를 함수 $f$ 의 선형화라고 한다.

  - 다음 그래프는 $y = x^2, y = 2x-1$ 이다.

    ![desmos-graph(1)](https://user-images.githubusercontent.com/16812446/79032028-2b70f280-7bde-11ea-84c5-a63f705c0906.png)

    그런데 $x=1$ 지점에서 그래프를 더 확대해보면 다음과 같다. 

    ![desmos-graph(2)](https://user-images.githubusercontent.com/16812446/79032042-43e10d00-7bde-11ea-94f6-9056afab3f22.png)

    여기에서 더 확대해보자. 

    ![desmos-graph(3)](https://user-images.githubusercontent.com/16812446/79032074-991d1e80-7bde-11ea-9a8f-3e636d9bb31b.png)

    그러면 거의 두 함수를 분간할 수가 없다. 

    이것은 원함수의 임의의 점 $x=a$ 에서의 접선을 그렸을 때 $x=a$ 를 중심으로 그래프를 끝없이 확대해보면 원함수와 접선이 거의 똑같아지는 것을 의미한다.

  - 이 현상을 이용하여 $x=a$ 에서 원래의 함수를 선형 근사시킬 수 있는 방법을 $x=a$ 에서의 접선 

    $$ L(x) = f'(a)(x-a) + f(a) $$

    을 구하는 것이라 할 수 있다. 
  
  - 예시 

    $y = \sqrt[]{1+x}$ 을 $x = 0$ 에서 선형근사시켜보면 다음과 같다.

    $$ \sqrt[]{1+x} \approx 1 + \frac{x}{2} $$

- 표준 선형 근사(standard linear approximation) : 선형화의 정의에서 $x=a$ 에서 함수 $f$ 의 함수 $L$ 에 의한 근사

  $$ f(x) \approx L(x) $$

  를 표준 선형 근사라한다.

  - 이때 $x=a$ 를 근사의 중심이라 한다. 

## 미분 

- 미분(differential) : $y = f(x)$ 를 미분가능한 함수이고 미분 $dx$ 가 독립변수일 때 미분 $dy$ 는 

  $$ dy = f'(x)dx $$

  이다. 

  - 가끔 $dy = f'(x)dx$ 를 다음과 같이 미분 $f$ 로도 표현한다.

    $$ df = f'(x)dx $$

  - 미분은 서로 다른 두 개념인 differentiation(미분) 과 differential(미분) 으로 동시에 쓰인다. 전자는 도함수를 얻는다는 뜻의 differentiate 의 명사형이다. 후자 differential 은 원함수의 선형근사함수를 뜻한다.

    가령 함수 $f(x)$ 의 한 점 $a$ 에서의 미분(differential) 은 

    $$ df(\Delta x) = f'(a)\Delta x $$

    로 표현되는 선형근사함수이다. 
  
  - 기하학적 의미 

    $x = a, dx = \Delta x$ 로 두자. $x$ 의 증분 $\Delta x$ 는 $x = a$ 에서 $x = a + \Delta x$ 의 거리

    $$ \Delta x = (\Delta x + a) - (a) $$

    로 두자.
    
    그러면 우선 $y$ 의 증분 

    $$ \Delta y = f(a + \Delta x) - f(a) $$

    은

    $$ \Delta y = f(a + dx) - f(a) $$

    이다. 한편 $x = a$ 에서 접선은 

    $$ L(x) = f'(a)(x-a) + f(a) $$

    이므로 $x = a$ 근방에서 접선의 변화를 

    $$ \Delta L = L(a + dx) - L(a) $$

    에서

    $$ = f'(a)\{(a+dx)-a\} +f(a) -f(a) $$

    $$ = f'(a)dx $$

    이므로 

    $$ \Delta L = f'(a)dx = dy $$

    이다. 

    이것은 함수 $f$ 의 $x=a$ 에서 선형근사함수 $L(x)$ 의 변화가 $x = a$ 이고 $dx = \Delta x$ 일 때 $dy$ 과 정확히 일치한다는 것이다. 
  
  - 예시 

    $y = x ^{5} + 37x$ 에서의 $dy$ 를 찾자. 

    $$ dy = (5x ^{4} + 37)dx $$
  
  - 예시 

    합성함수 미분법(Chain Rule) 과 다른 미분법을 함께 사용할 수 있다. 

    $$ d (\tan  2x) = \sec ^{2}(2x)d(2x) $$ 

    에서 

    $$ d(2x) = (2x)'dx = 2dx $$

    이므로
    
    $$ d (\tan 2x) = 2 \sec ^{2} 2x dx $$

    이다. 

- 미분의 추정(estimating with differentials) : 함수 $f(x)$ 가 $x = a$ 에서 미분가능할 때 $x = a$ 의 근방 $x = a + dx$ 에서 함수값이 변하는 정도 $f(a + dx)$ 는 근사적으로

  $$ f(a + dx) \approx f(a) + dy $$

  이다. 

  - $y$ 의 증분은 

    $$ \Delta y = f(a + \Delta x) - f(a) $$

    이다. 이때 $dx= \Delta x$ 가 충분히 작으면 $y$ 의 증분 $\Delta y$ 는 미분 $dy$ 와 거의 똑같아진다. 왜냐하면 함수 $f$ 의 접선 $L$ 의 증분 

    $$ \Delta L = f'(a)dx = dy$$

    가 $x = a$ 의 근방에서 함수 $f$ 의 증분 $\Delta y$ 와 거의 똑같아지기 때문이다. 그러므로 $x = a$ 근방에서 

    $$ f'(a)dx = dy \approx \Delta y $$

    라 할 수 있고, 이에 따라

    $$ f(a + dx) = f(a) + \Delta y $$

    를 근사적으로 

    $$ f(a + dx) \approx  f(a) + dy $$

    로 쓸 수 있다. 

  - 예시 

    $7.97 ^{\frac{1}{3}}$ 을 추산해보자. 

    $f(x) = x ^{\frac{1}{3}}$ 의 미분은 

    $$ dy = \frac{1}{3x ^{\frac{2}{3}}}dx $$

    이다. 
    
    이때 $a = 8$ 로 둔다면 $7.97$ 을 $x = a$ 근방의 함수 $f$ 의 접선의 함수값으로 생각할 수 있다. 

    그렇다면 $dx = -0.03$ 으로 둘 때 $x = a$ 에서의 함수값 $f(7.97)$ 을 다음과 같이 근사시킬 수 있다. 

    $$ f(7.97) = f(a + dx) \approx f(a) + dy $$

    그러면

    $$ f(a) + dy = f(a) + f'(a)dx $$

    에서 $f'(x) = \frac{1}{3x ^{\frac{2}{3}}}$ 이고 $dx = -0.03$ 으로 두었으므로

    $$ = 8 ^{\frac{1}{3}} + \frac{1}{3(8)^{\frac{2}{3}}}(-0.03) $$

    $$ = 1.9975 $$

    이다. 따라서 

    $$ \therefore  7.97 ^{\frac{1}{3}} \approx 1.9975 $$

    이다.

## 이변수 함수 선형화

- 이변수 함수 선형화 또는 접평면(tangent plane) : $f$ 의 연속인 편도함수들이 존재할 때 점 $P(x_0, y_0, z_0)$ 에서 곡면 $z = f(x, y)$ 에 대한 접평면의 방정식은 

  $$ z - z_0 = f_x(x_0, y_0)(x- x_0) + f_y(x_0, y_0)(y - y_0) $$

  또는 

  $$ L(x, y) = f(x_0, y_0) + f_x(x_0, y_0)(x-x_0) + f_y(x_0, y_0)(y - y_0)
  $$

  이고 이것은 이변수 함수 $f(x, y)$ 의 선형화이다. 

  - 또한 점 $P(x_0, y_0, z_0)$ 근방에서 

    $$ f(x, y) \approx L(x, y) $$

    이 성립한다.
    
    일변수 함수 $f$ 를 $x=a$ 에서 끝없이 확대했을 때 $x=a$ 에서 접선과 거의 똑같아지는 것과 같이 이변수 함수 $f$ 를 끝없이 확대하면 접평면의 방정식과 거의 똑같아지기 때문이다. 

- 이변수 함수 미분 또는 전미분(total differential) : 점 $(x_0, y_0)$ 에서 점 $(x_0 + dx, y_0 + dy)$ 로 움직였을 때의 변화량 

  $$ df = f_x(x_0, y_0)dx + f_y (x_0, y_0)dy $$

  또는

  $$ df = \frac{\partial f}{\partial x} dx + \frac{\partial f}{\partial y} dy $$

  을 함수 $f$ 의 전미분이라 한다. 

  - $y = f(x, y)$ 가 미분가능한 함수이면 점 $(x_0, y_0)$ 에서 편미분계수가 존재한다. 이 점에서 조금 움직인 점 $(x_0+\Delta x, y_0+\Delta y)$ 를 생각할 수 있고 이때의 함수 $f$ 의 변화량

    $$ \Delta f =f(x_0+\Delta x, y_0+\Delta y)- f(x_0, y_0) $$

    을 생각할 수 있다. 

    이때 접평면의 변화량 

    $$ \Delta L = L(x_0 + \Delta x, y_0 + \Delta y) - L(x_0, y_0) $$

    을 접평면의 방정식을 사용하여 풀면

    $$ = f_x(x_0, y_0)\Delta x + f_y(x_0, y_0)\Delta y $$

    이다. 

    이때 $dx, dy$ 는 독립변수이므로 임의의 값을 대입할 수 있다. 또한 우리는 보통

    $$ dx = \Delta x = x - x_0, dy = \Delta y = y - y_0 $$

    으로 정의한다.
  
  - 편미분이 변수 하나에 대한 함수의 변화량을 생각했다면 전미분은 모든 변수에 대한 변화량에 따라 함수가 얼마나 변하는지를 측정한다. 

  - 예시 

    반지름이 $r = 1$ 이고 높이가 $h = 5$ 인 원통이 있다고 하자. 이때 반지름과 높이를 변화시켜서 

    $$ dr = +0.03, dh = -0.1 $$

    가 되게 한다고 하자. 이때 부피의 변화량을 구해보자. 

    먼저 부피 $V$ 는 다음과 같은 이변수 함수다.

    $$ V = V(r, h) = \pi r ^{2}h $$

    $V$ 를 선형 근사시키면(전미분하면)

    $$ \Delta V \approx dV = V_r(r_0, h_0)dr + V_h(r_0, h_0)dh $$

    이다.

    $$ V_r = 2 \pi rh, V_h = \pi r ^{2} $$

    이므로

    $$ dV = 2 \pi r_0h_0dr + \pi r_0 ^{2}dh = 2 \pi 1 \cdot 5 \cdot (0.03) + \pi (1) ^{2}(-0.1) = 0.3 \pi - 0.1 \pi = 0.2 \pi \approx 0.63 cm ^{3} $$

    을 얻는다. 

  - 예시 

    $2.5m$ 높이와 $0.5m$ 반지름의 원뿔형 물탱크의 부피가 반지름과 높이의 변화에 얼마나 민감하게 변하는지 조사하려 한다.

    먼저 부피 $V$ 는 

    $$ V = \pi r ^{2} h $$

    이며, 각 변수에 대한 전미분은 다음과 같다. 

    $$ dV = V_r(0.5, 2.5)dr + V_h(0.5,2.5)dh $$
    
    $$ =(2 \pi rh)_{(0.5, 2.5)} dr + (\pi r ^{2})_{(0.5,2.5)}dh $$

    $$ = 2.5 \pi dr + 0.25 \pi dh $$

    따라서 반지름 $r$ 의 단위 $1$ 변화는 전체 부피 $V$ 를 $2.5 \pi$ 변하게 하고

    높이 $h$ 의 단위 $1$ 변화는 전체 부피 $V$ 를 $0.25\pi$ 변하게 한다.

    이로보아 반지름이 변할 때 물탱크의 전체 부피가 훨씬 더 민감하게 변한다는 것을 알 수 있다. 

