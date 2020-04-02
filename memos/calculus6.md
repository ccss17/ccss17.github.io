# [ccss17.github.io](https://ccss17.github.io)

# Calculus6 Memo

# 이변수 함수의 극한 

- 이변수 함수의 극한 : 함수 $f(x, y)$ 에서 $(x, y)$ 이 $(x_0, y_0)$ 에 한없이 다가갈 때 함수값이 극한값 $L$ 로 다가가는 것은 

  임의의 양수 $\epsilon > 0$ 에 대하여 적당한 양수 $\delta > 0$ 가 존재하여 정의역의 모든 $(x, y)$ 에 대하여 다음을 만족하는 것이다. 

    $$ 0 < \sqrt[]{(x-x_0) ^{2} + (y - y_0) ^{2}} < \delta \Rightarrow  |f(x, y) - L| < \epsilon $$

  - 기호로 다음과 같이 표현한다. 

    $$ \lim_{(x, y) \to (x_0, y_0)} f(x, y) = L $$

- 이변수 함수의 극한의 성질 : 실수 $L, M, k$ 에 대하여 

  $$ \lim_{(x, y) \to (x_0, y_0)} f(x, y) = L\\ \lim_{(x, y) \to (x_0, y_0)} g(x, y) = M $$

  일 때 다음이 성립한다. 

  - 합의 법칙 : $\lim_{(x, y) \to (x_0, y_0)} (f(x, y)+g(x, y)) = L + M$

  - 차의 법칙 : $\lim_{(x, y) \to (x_0, y_0)} (f(x, y)-g(x, y)) = L - M$

  - 실수배 법칙 : $\lim_{(x, y) \to (x_0, y_0)} kf(x, y) = kL$

  - 곱의 법칙 : $\lim_{(x, y) \to (x_0, y_0)} (f(x, y)\cdot g(x, y)) = L \cdot M$

  - 몫의 법칙 : $\lim_{(x, y) \to (x_0, y_0)} \frac{f(x, y)}{g(x, y)} = \frac{L}{M}, M \neq 0$

  - 제곱 법칙 : $n \in \mathbb{Z}, n > 0, \lim_{(x, y) \to (x_0, y_0)} [f(x, y)] ^{n} = L ^{n}$

  - 제곱근 법칙 : $n \in \mathbb{Z}, n > 0, \lim_{(x, y) \to (x_0, y_0)} \sqrt[n]{f(x, y)} = L ^{\frac{1}{n}}$

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

## 여러가지 편도함수 

- 이계 편도함수(second-order partial derivative) : 이변수 함수 $f(x, y)$ 를 두번 미분한 것으로 다음 $4$ 가지 경우로 정의된다. 

  - $x$ 에 대하여 두번 미분할 경우 

    $$ \frac{\partial ^{2} f}{\partial x ^{2}} = \frac{\partial }{\partial x }(\frac{\partial f}{\partial x}) = (f_x)_x = f _{xx} $$

  - $x$ 에 대하여 미분하고 $y$ 에 대하여 미분할 경우

    $$ \frac{\partial ^{2} f}{\partial y \partial x } = \frac{\partial }{\partial y}(\frac{\partial f}{\partial x}) = (f_x)_y = f _{xy} $$

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