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

- 벡터의 $j$ 성분(j-component) : 표준 단위 벡터의 예시에서 스칼라 $v_2$ 을 벡터 $v$ 의 $j$ 성분이라한다.

- 벡터의 $k$ 성분(k-component) : 표준 단위 벡터의 예시에서 스칼라 $v_3$ 을 벡터 $v$ 의 $k$ 성분이라한다.

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

## 기울기 벡터 

- 기울기 벡터(gradient vector) : 스칼라 함수 $f(x, y)$ 의 기울기는 벡터함수 

  $$ \text{grad} f = \nabla f = \frac{\partial f}{\partial x}i + \frac{\partial f}{\partial y}j =  \bigg <\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}\bigg > $$

  이다. 
