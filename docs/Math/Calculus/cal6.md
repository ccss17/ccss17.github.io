# 이변수 함수의 극한 


!!! tldr ""

    이변수함수 : 두 개의 변수에 의존하는 함수이다.

- 예시 

    수직선 $\mathbb{R}$ 의 두 점 $x,y$ 에 대하여 이들 사이의 거리를 재는 함수 

    $$ d(x, y) := |x - y| $$

    는 정의역이 실수쌍 $(x, y)$ 전체로 이루어진 집합, 즉 좌표평면 $\mathbb{R} ^{2}$ 이다.

!!! tldr ""

    다변수함수 또는 $n$변수 함수 : $n$-공간의 부분집합 $U$ 에서 $U$ 의 각 점 $X = (x_1, x _{2}, \dots, x _{n})$ 을 실수 $f(x) = f(x_1, x _{2}, \dots, x _{n})$ 에 대응시키는 함수
    
    $$ f : U \to \mathbb{R} $$
    
    이다.

- $n$-공간의 부분집합 $U$ 에서 정의된 다변수함수 $f$ 를 이해하는 방법 중 하나는 그래프를 그려보는 것인데, $f$ 의 그래프는 

    $$ \{(x_1, x_2, \dots, x_n, z) \in R ^{n+1} | (x_1, x_2, \dots, x_n) \in U, z = f(x_1, x_2, \dots, x_n)\} $$

    이다.

    - 예시 

        이변수함수 $f(x, y) = x^2+ y ^{2}$ 의 그래프는 방정식 $z = x^2+ y ^{2}$ 으로 표현되는 다음과 같은 회전포물변이다.

        ![image](https://user-images.githubusercontent.com/16812446/86470649-cc52f200-bd76-11ea-9347-5421db411de9.png)

!!! tldr ""

    이변수 함수의 극한 : 함수 $f(x, y)$ 에서 $(x, y)$ 이 $(x_0, y_0)$ 에 한없이 다가갈 때 함수값이 극한값 $L$ 로 다가가는 것은 
    
    임의의 양수 $\epsilon > 0$ 에 대하여 적당한 양수 $\delta > 0$ 가 존재하여 정의역의 모든 $(x, y)$ 에 대하여 다음을 만족하는 것이다. 
    
    $$  0 < \sqrt[]{(x-x_0) ^{2} + (y - y_0) ^{2}} < \delta \implies  |f(x, y) - L| < \epsilon $$

- 기호로 다음과 같이 표현한다. 

    $$ \lim_{(x, y) \to (x_0, y_0)} f(x, y) = L $$

!!! tldr ""

    일변수 함수의 일차함수의 기울기 : 일변수 함수의 일차함수 $y = ax + b$ 의 기울기는
    
    $$ \dfrac{\Delta y}{\Delta x} = \dfrac{(a(x+\Delta x)+b) - (ax + b)}{\Delta x} = a $$
    
    이다.



!!! tldr ""

    이변수함수의 일차함수의 기울기 : 이변수 함수의 일차함수 
    
    $$ z = z(x, y) = ax + by + c $$
    
    의 기울기는 $x$ 축 방향 기울기와 $y$ 축 방향 기울기로 이루어진 벡터
    
    $$ (a, b) = ai + bj $$
    
    이다.

- 설명 

    $$ \int_{-\infty }^{\infty }f(x)
    $$

    이변수 함수의 일차함수 

    $$ z = z(x, y) = ax + by + c $$
    
    에 대하여 $xy$-평면에서 $x$ 축과 나란한 직선 위에서의 기울기는 

    $$ \dfrac{z(x+\Delta x, y) - z(x, y)}{\Delta x} = \dfrac{(a(x+\Delta x)+by+c) - (ax + by + c)}{\Delta x} = a $$

    이고 $y$ 축과 나란한 직선 위에서의 기울기는

    $$ \dfrac{z(x, y + \Delta y) - z(x, y)}{\Delta y} = b $$

    이다. 그러므로 이것을 일반화하여 임의의 방향에 대한 기울기를 벡터

    $$ (a, b) = ai+bj $$

    로 표현한다.

!!! tldr ""

    이변수 일차함수의 기울기 벡터 : 이변수 함수의 일차함수 $z = z(x, y) = ax + by + c$ 의 기울기를 나타내는 벡터
    
    $$ (a, b) = ai+bj $$
    
    이다.

- 예시 

    함수 $z = 1 - x - y$ 의 $x$ 축 방향, $y$ 축 방향의 기울기는 모두 $-1$ 이므로 기울기 벡터는

    $$ (-1, -1) $$

    이다.

!!! tldr ""

    $n$변수 일차함수의 기울기 : 벡터 $a = (a_1, \dots, a_n), x = (x_1, \dots, x_n)$ 와 단위벡터 $v = (v_1, \dots, v_n)$ 와 실수 $c$ 에 대한  $n$변수 함수
    
    $$ z = z(x) = a \cdot x = a_1x_1 + \dots + a_nx_n + c = a \cdot x + c $$
    
    의 $v-$방향 기울기는
    
    $$ a \cdot v = a_1v_1 + \dots + a_n v_n $$
    
    이다.

- 설명 

    벡터 $a = (a_1, \dots, a_n), x = (x_1, \dots, x_n), e_1 = (1, \dots, 0)$ 와 실수 $c$ 에 대한  $n$변수 함수

    $$ z = z(x) = a_1x_1 + \dots + a_nx_n + c = a \cdot x + c $$

    의 첫번째 축 방향의 기울기는 

    $$ \dfrac{z(x + te_1) - z(x)}{t} = \dfrac{(a \cdot (x + te_1) + c) - (a \cdot x+c)}{t} = a \cdot e_1 = a_1 $$

    이다.

    이 기울기는 함수의 그래프를 $x_1z$-평면에서 살펴본 직선의 기울기이다. 마찬가지로 $x_nz$-평면에서 살펴본 직선의 기울기, 즉 마지막 축 방향의 기울기는 $a_n$ 이다.

!!! tldr ""

    이변수 함수의 극한의 성질 : 실수 $L, M, k$ 에 대하여 
    
    $$ \lim_{(x, y) \to (x_0, y_0)} f(x, y) = L\\ \lim_{(x, y) \to (x_0, y_0)} g(x, y) = M $$
    
    일 때 다음이 성립한다.

- 합의 법칙 

    $$ \lim_{(x, y) \to (x_0, y_0)} (f(x, y)+g(x, y)) = L + M $$

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

!!! tldr ""

    이변수 함수의 연속 : 이변수 함수 $f(x, y)$ 가 점 $(x_0, y_0)$ 에서 연속이라는 것은 다음 조건과 동치이다.
    
    1. $f$ 가 $(x_0, y_0)$ 에서 정의되어 있다. 
    
    2. $\displaystyle \lim_{(x, y) \to (x_0, y_0)} f(x, y)$ 극한값이 존재한다.
    
    3. $\displaystyle \lim_{(x, y) \to (x_0, y_0)} f(x, y) = f(x_0, y_0)$



!!! tldr ""

    이변수 합성함수의 연속 : 이변수 함수 $f$ 가 $(x_0, y_0)$ 에서 연속이고 일변수 함수 $g$ 가 $x$ 축 상의 점 $f(x_0, y_0)$ 에서 연속일 때,
    
    $h(x, y) = g(f(x, y))$ 로 정의된 이변수 합성함수 $h = g \circ f$ 는 연속이다.

- 예시 

    합성함수 $e ^{x-y}, \cos \frac{xy}{x^2+1}, \ln (1+x ^{2}y ^{2})$ 는 개구간 $(-\infty , \infty)$ 에서 연속이다.

!!! tldr ""

    다변수 함수의 극한과 연속 : 이변수 함수의 극한과 연속의 정의와 비슷하다.

- 예시 

    $P$ 가 $(x, y, z)$ 를 뜻할 때

    $$ \lim_{P \to (1,0,-1)} \frac{e ^{x+z}}{z ^{2}+\cos \sqrt[]{xy}} = \frac{e ^{1-1}}{(-1)^{2}+\cos 0} = \frac{1}{2} $$

    이다. 

# 상미분과 편미분 

실제로 많은 함수들이 하나의 독립 변수에 의존하는 것이 아니라 두 개 이상의 독립 변수에 종속되기 때문에 많은 경우 일변수 함수에 대한 미분을 다변수 함수로 확장한 미분이 필요하다.

!!! tldr ""

    상미분(ordinary derivative) : 변수가 하나만 있는 함수에 대한 미분이다.

- 지금까지 해오던 미분이 바로 상미분이다.

!!! tldr ""

    $x$ 에 대한 편미분계수 : 이변수 함수 $z = f(x, y)$ 의 점 $(x_0, y_0)$ 에서의 $x$ 에 대한 편미분계수는 
    
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

!!! tldr ""

    $y$ 에 대한 편미분계수 : 이변수 함수 $z = f(x, y)$ 의 점 $(x_0, y_0)$ 에서의 $y$ 에 대한 편미분계수는 
    
    $$ \frac{\partial f}{\partial y} \bigg | _{(x_0, y_0)} = \frac{d}{dy}f(x_0, y) \bigg | _{y=y_0} =  \lim_{h \to 0} \frac{f(x_0, y_0+h)-f(x_0,y_0)}{h} $$
    
    이다.



!!! tldr ""

    편도함수(partial derivative) : 이변수 함수 $z = f(x, y)$ 의 편도함수는 다음과 같이 정의된다.
    
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

    $$ f_x(x, y) = 3x ^{2} + 2xy ^{3} \implies f_x(2, 1) = 16 $$

    $$ f_y(x, y) = 3x ^{2}y ^{2} - 4y \implies f_x(2, 1) = 8 $$

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

!!! tldr ""

    편도함수의 기하학적 의미 : 이변수 함수 $f(x, y)$ 에 대하여 편도함수의 기하학적 의미는 각각 다음과 같다. 
    
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

!!! tldr ""

    이계 편도함수(second-order partial derivative) : 이변수 함수 $f(x, y)$ 를 두번 미분한 것으로 다음 $4$ 가지 경우로 정의된다.

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

!!! tldr ""

    혼합 편미분(mixed derivative) : 이변수 함수 $f(x, y)$ 에 대하여 서로 다른 두 변수에 대한 편미분이다.

- 이계 편도함수에서 $x$ 에 대하여 미분하고 $y$ 에 대하여 미분한 경우

    $$ \frac{\partial ^{2} f}{\partial y \partial x } = \frac{\partial }{\partial y}(\frac{\partial f}{\partial x}) = (f_x)_y = f _{xy} $$

    와 $y$ 에 대하여 미분하고 $x$ 에 대하여 미분한 경우

    $$ \frac{\partial ^{2} f}{\partial x \partial y } = \frac{\partial }{\partial x}(\frac{\partial f}{\partial y}) = (f_y)_x = f _{yx} $$

    를 뜻한다.

!!! tldr ""

    혼합 편미분 정리(mixed derivative theorem) : 이변수 함수 $f(x, y)$ 와 그 편미분 $f_x, f_y, f _{xy}, f _{yx}$ 가 점 $(a, b)$ 를 포함하는 개구간에서 정의되어 있고 점 $(a, b)$ 에서 연속이라면 
    
    $$ f _{xy}(a, b) = f _{yx}(a, b) $$
    
    이다.

- 예시 

    이계 편도함수의 예시에서 이변수 함수 $f(x, y) = x \cos y + y e ^{x}$ 의 혼합 편미분의 변수 순서가 다른 두 결과

    $$ \frac{\partial ^{2}f}{\partial y \partial x} = \frac{\partial }{\partial y}(\frac{\partial f}{\partial x}) = -\sin y + e ^{x} $$

    $$ \frac{\partial ^{2}f}{\partial x \partial y} = \frac{\partial }{\partial x}(\frac{\partial f}{\partial y}) = -\sin y + e ^{x} $$

    가 동일한 것은 우연의 일치가 아니다. 혼합 편미분 정리에 의하여 이 둘이 같은 것이다. 

# 다변수 합성 함수의 미분

## 선형근사

!!! tldr ""

    선형화(linearization) : 함수 $f$ 가 $x=a$ 에서 미분가능할 때 $x=a$ 에서의 접선의 방정식
    
    $$ L(x) = f'(a)(x-a) + f(a) $$
    
    를 함수 $f$ 의 선형화라고 한다.

- 다음 그래프는 $y = x^2, y = 2x-1$ 이다. 그런데 $x=1$ 지점에서 그래프를 더 확대해보면 다음과 같다. 

    <img src="https://user-images.githubusercontent.com/16812446/79032028-2b70f280-7bde-11ea-84c5-a63f705c0906.png" width="30%" height="auto"> <img src="https://user-images.githubusercontent.com/16812446/79032042-43e10d00-7bde-11ea-94f6-9056afab3f22.png" width="30%" height="auto"> <img src="https://user-images.githubusercontent.com/16812446/79032074-991d1e80-7bde-11ea-9a8f-3e636d9bb31b.png" width="30%" height="auto">

    그러면 거의 두 함수를 분간할 수가 없다. 

    이것은 원함수의 임의의 점 $x=a$ 에서의 접선을 그렸을 때 $x=a$ 를 중심으로 그래프를 끝없이 확대해보면 원함수와 접선이 거의 똑같아지는 것을 의미한다.

- 이 현상을 이용하여 $x=a$ 에서 원래의 함수를 선형 근사시킬 수 있는 방법을 $x=a$ 에서의 접선 

    $$ L(x) = f'(a)(x-a) + f(a) $$

    을 구하는 것이라 할 수 있다. 

- 예시 

    $y = \sqrt[]{1+x}$ 을 $x = 0$ 에서 선형근사시켜보면 다음과 같다.

    $$ \sqrt[]{1+x} \approx 1 + \frac{x}{2} $$

!!! tldr ""

    표준 선형 근사(standard linear approximation) : 선형화의 정의에서 $x=a$ 에서 함수 $f$ 의 함수 $L$ 에 의한 근사
    
    $$ f(x) \approx L(x) $$
    
    를 표준 선형 근사라한다.

- 이때 $x=a$ 를 근사의 중심이라 한다. 

## 미분(differential)

!!! tldr ""

    미분(differential) : $y = f(x)$ 를 미분가능한 함수이고 미분 $dx$ 가 독립변수일 때 미분 $dy$ 는 
    
    $$ dy = f'(x)dx $$
    
    이다.

- $dx$ 와 $x$ 가 독립변수인 반면 $dy$ 는 종속변수이다. 즉, $dy$ 는 $x, dx$ 에 의해 결정된다.

- 가끔 $dy = f'(x)dx$ 를 다음과 같이 미분 $f$ 로도 표현한다.

    $$ df = f'(x)dx $$

- 미분은 서로 다른 두 개념인 differentiation(미분) 과 differential(미분) 으로 동시에 쓰인다. 전자는 도함수를 얻는다는 뜻의 differentiate 의 명사형이다. 후자 differential 은 원함수의 선형근사함수를 뜻한다.

    가령 함수 $f(x)$ 의 한 점 $a$ 에서의 미분(differential) 은 

    $$ df(\Delta x) = f'(a)\Delta x $$

    로 표현되는 선형근사함수이다. 

- 기하학적 의미 

    ![image](https://user-images.githubusercontent.com/16812446/86736612-a11a1c80-c06e-11ea-8b4f-20ed5748ea3c.png)

    > 출처 : [Thomas' CALCULUS](https://www.amazon.com/Thomas-Calculus-Early-Transcendentals-13th/dp/0321884078) Figure3.55

    기하학적 의미는 이렇다.
    
    위 그림에서 $x = a, dx = \Delta x$ 로 두자. $x$ 의 증분 $\Delta x$ 는 $x = a$ 에서 $x = a + \Delta x$ 의 거리

    $$ \Delta x = (\Delta x + a) - (a) $$

    로 두자. 
    
    $x$ 증분에 따른 $y=f(x)$ 의 변화는 $\Delta y = f(a + dx) - f(a)$ 이다. 
    
    $x$ 증분에 따른 접선 $L(x) = f'(a)(x-a) + f(a)$ 의 변화는 
    
    $$\Delta L = L(a + dx) - L(a)$$

    $$ = f'(a)\{(a+dx)-a\} +f(a) -f(a) $$

    $$ = f'(a)dx $$

    이다.

    이것의 의미는 $\Delta L = f'(a)dx = dy$ 이므로 $f$ 의 선형화(접선 $L$)의 변화가 정확하게 $x=a, dx = \Delta x$ 일때 미분(differential) $dy$ 와 똑같다는 것이다.

    그러므로 우리는 $dx = \Delta x$ 일때 미분(differential) $dy$ 가 정확하게 접선의 변화량을 나타내준다는 것을 알 수 있다.

    만약 $dx \neq 0$ 이라면 다음과 같이 미분(differential) $dy$ 를 $dx$ 로 나누어 얻은 것이 도함수 $f'(x)$ 와 정확하게 일치한다는 것을 알 수 있다.

    $$ dy \div dx = \dfrac{f'(x)dx}{dx} = f'(x) = \dfrac{dy}{dx} $$

- 예시 

    $y = x ^{5} + 37x$ 에서의 $dy$ 를 찾자. 

    $$ dy = (5x ^{4} + 37)dx $$

    이때 $x=1,dx=0.1$ 에서 $dy$ 값을 찾으면

    $$ dy = (5 \cdot 1   ^{4} + 37)(0.2) = 8.4 $$

    이다. ■ 

- 예시 

    합성함수 미분법(Chain Rule) 과 다른 미분법을 함께 사용할 수 있다. 

    먼저 일반적인 미분(differentiation) 의 관점에서 $(\tan x)' = \sec ^{2}x$ 이므로 $(\tan 2x)'$ 에서 $2x = t$ 로 두면 

    $$ \dfrac{d \tan 2x}{dx} = \dfrac{d \tan t}{dx} = \dfrac{d \tan t}{dt}\cdot \dfrac{d2x}{dx} = \sec ^{2}t \cdot 2 = 2 \sec ^{2}(2x) $$

    이다.

    이제 미분(differential) 의 관점에서

    $$ d (\tan  2x) = \sec ^{2}(2x)d(2x) $$ 

    에서 $d(2x)$ 을 함수 $y = 2x$ 를 $x$ 에 대하여 하는 미분(differential) 으로 보면 $d(2x) = (2x)'dx = 2dx$ 이므로

    $$ d (\tan 2x) = 2 \sec ^{2} (2x) dx $$

    이다. 

## 미분 추정

!!! tldr ""

    미분의 추정(estimating with differentials) : 함수 $f(x)$ 가 $x = a$ 에서 미분가능할 때 $x = a$ 의 근방 $x = a + dx$ 에서 함수값이 변하는 정도 $f(a + dx)$ 는 근사적으로
    
    $$ f(a + dx) \approx f(a) + dy $$
    
    이다.

- $y$ 의 증분은 $\Delta y = f(a + \Delta x) - f(a)$ 이다. 이때 $dx= \Delta x$ 가 충분히 작으면 $y$ 의 증분 $\Delta y$ 는 미분 $dy$ 와 거의 똑같아진다. 왜냐하면 함수 $f$ 의 접선 $L$ 의 증분 $\Delta L = f'(a)dx = dy$ 이 $x = a$ 의 근방에서 함수 $f$ 의 증분 $\Delta y$ 와 거의 똑같아지기 때문이다. 그러므로 $x = a$ 근방에서 

    $$ f'(a)dx = dy \approx \Delta y $$

    라 할 수 있고, 이에 따라

    $$ f(a + dx) = f(a) + \Delta y $$

    를 근사적으로 

    $$ f(a + dx) \approx  f(a) + dy $$

    로 쓸 수 있다. 

- 예시 

    $7.97 ^{\frac{1}{3}}$ 을 추산해보자. 

    $f(x) = x ^{\frac{1}{3}}$ 의 미분(differential)은 $dy = \dfrac{1}{3x ^{\frac{2}{3}}}dx$ 이다. 이때 $a = 8$ 로 둔다면 $7.97$ 을 $x = a$ 근방의 함수 $f$ 의 접선의 함수값으로 생각할 수 있다. 그렇다면 $dx = -0.03$ 으로 둘 때 $x = a$ 에서의 함수값 $f(7.97)$ 을 다음과 같이 근사시킬 수 있다. 

    $$ f(7.97) = f(a + dx) \approx f(a) + dy $$

    그러면 $f(a) + dy = f(a) + f'(a)dx$ 에서 $f'(x) = \frac{1}{3x ^{\frac{2}{3}}}$ 이고 $dx = -0.03$ 으로 두었으므로

    $$ = 8 ^{\frac{1}{3}} + \frac{1}{3(8)^{\frac{2}{3}}}(-0.03) = 1.9975 $$

    이다. 따라서 

    $$ \therefore  7.97 ^{\frac{1}{3}} \approx 1.9975 $$

    이다. ■ 

- 예시

    원의 반지름 $r$ 이 $a=10$ 에서 $a=10.1$ 로 변했을 때 원의 넓이 $A$ 를 추정해보자.

    먼저 원의 정확한 넓이는 $A = \pi r ^{2}$ 이고 $a=10, dr = 0.1$ 이므로 미분(differential) 을 구하여

    $$ dA = A'(a)dr = 2 \pi adr = 2 \pi (10)(0.1) = 2 \pi $$

    을 얻는다.

    그런데 $A(r + \Delta r) \approx A(r)+dA$ 이므로 

    $$ A(10 + 0.1) \approx A(10)+2 \pi = \pi (10)^{2}+2 \pi =102 \pi $$

    를 얻는다. 그러므로 반지름 $r=10.1$ 일 때 원의 넓이를 미분 추정해보면 $102 \pi$ 이다. ■ 

    실제 넓이는 $A(10.1) = \pi (10.1) ^{2} = 102.01 \pi$ 이므로 오차는 $\Delta A - dA = 0.01 \pi$ 이다.

!!! tldr ""

    미분근사의 오차(error in differential approximation) : 함수 $y=f(x)$ 가 $x=a$ 에서 미분가능하고 $x$ 가 $a$ 에서 $a+\Delta x$ 로 변할 때 함수 $y$ 의 변화량 $\Delta y$ 은
    
    $\Delta x \to 0 \implies \epsilon \to 0$ 인 오차량 $\epsilon = \dfrac{f(a+\Delta x) - f(a)}{\Delta x} - f'(a)$ 에대하여
    
    $$ \Delta y = f'(a) = f'(a)\Delta x+\epsilon \Delta x $$
    
    이다.

- 설명 

    함수 $f(x)$ 가 $x=a$ 에서 미분가능하다고 하고 $x$ 의 변화량을 $dx = \Delta x$ 라고 하자.

    그러면 $x$ 가 $a$ 에서 $a+ \Delta x$ 변할 때 함수 $f$ 의 변화를 표현하는 두 가지 방법이 있다.

    1. 진짜 변화량 : $\Delta f = f(a+\Delta x)-f(a)$

    2. 미분 추정량 : $df = f'(a)\Delta x$

    이때 미분 추정량 $df$ 는 진짜 변화량 $\Delta f$ 와 얼마나 차이가 날까? 이것은 단순히 $\Delta f$ 로부터 $df$ 를 빼보면 알 수 있다.

    그러므로 추정오차량은

    $$ \text{(추정오차량)} = \Delta f - df = \Delta f - f'(a)\Delta x $$

    $$ = f(a+\Delta x)-f(a)-f'(a)\Delta x $$

    $$ = \bigg ( \dfrac{f(a+\Delta x) - f(a)}{\Delta x} - f'(a) \bigg )\cdot \Delta x $$

    인데 오차량을 $\epsilon = \bigg ( \dfrac{f(a+\Delta x) - f(a)}{\Delta x} - f'(a) \bigg )$ 로 두면

    $$ = \epsilon \cdot \Delta x $$

    이다.

    그런데 $\Delta x \to 0$ 일 때 미분계수의 정의에 따라 $\dfrac{f(a+\Delta x) - f(a)}{\Delta x} \to f'(a)$ 이다. 그러므로 실질적으로 $\epsilon$ 은 매우 작은양으로 줄어든다. 즉,

    $$ \Delta x \to 0 \implies \epsilon \to 0 $$

    이다. 따라서 $\Delta x$ 가 매우 작으면 오차량 $\epsilon$ 도 함께 매우 작아진다. 이때 $\Delta f - df = \epsilon \cdot \Delta x$ 이므로 $\Delta f = df + \epsilon \Delta x$ 즉,

    $$ \underbrace{\Delta f}_{\text{true change}} = \underbrace{f'(a)\Delta x}_{\text{estimated change}} + \underbrace{\epsilon \Delta x}_{error} $$

    를 얻는다.

- 예시

    원의 반지름 $r$ 이 $a=10$ 에서 $a=10.1$ 로 변했을 때 원의 넓이 $A$ 를 추정해보고 오차를 조사하자.

    먼저 원의 정확한 넓이는 $A = \pi r ^{2}$ 이고 $a=10, dr = 0.1$ 이므로 미분(differential) 을 구하여

    $$ dA = A'(a)dr = 2 \pi adr = 2 \pi (10)(0.1) = 2 \pi $$

    을 얻는다.

    그런데 $A(r + \Delta r) \approx A(r)+dA$ 이므로 

    $$ A(10 + 0.1) \approx A(10)+2 \pi = \pi (10)^{2}+2 \pi =102 \pi $$

    를 얻는다. 그러므로 반지름 $r=10.1$ 일 때 원의 넓이를 미분 추정해보면 $102 \pi$ 이다. 

    실제 넓이는 $A(10.1) = \pi (10.1) ^{2} = 102.01 \pi$ 이므로 
    
    $$ \Delta A = (102.01 - 100) \pi = (\underbrace{2 \pi}_{dA}  + \underbrace{0.01 \pi}_{\text{error}}) $$
    
    에서 $\Delta A - dA = \epsilon \Delta r = 0.01 \pi$ 이다. 따라서 최종적으로 오차량 
    
    $$\epsilon = \dfrac{0.01 \pi}{\Delta r} = \dfrac{0.01 \pi }{0.1} = 0.1 \pi$$ 
    
    을 얻는다. ■ 

## 이변수함수의 미분가능성

!!! tldr ""

    이변수함수의 미분가능 : 점 $(x_0,y_0)$ 에 대한 이변수함수 $z=f(x,y)$ 의 편미분 $f_x(x_0, y_0), f_y(x_0,y_0)$ 이 존재하고 함수 $z$ 의 변화량 $\Delta z$ 가 
    
    $\Delta x, \Delta y \to 0 \implies \epsilon _1, \epsilon _2 \to 0$ 에 대한 방정식
    
    $$ \Delta z = f_x(x_0,y_0)\Delta x+f_y(x_0,y_0)\Delta y+\epsilon _1 \Delta x+\epsilon _2 \Delta y $$
    
    을 만족하면 $f$ 는 모든 정의역에서 미분가능하다.

- 그리고 미분가능한 이변수함수의 그래프를 매끄러운 곡면(smooth surface)이라고 한다.

!!! tldr ""

    일독립변수와 이매개변수에 대한 도함수 : 이변수 함수 $w = f(x, y)$ 가 미분가능하고 $t$ 에 대한 함수 $x = x(t), y = y(t)$ 가 미분가능하면
    
    $t$ 에 대한 이변수 합성함수 $w = f(x(t), y(t))$ 는 미분가능하며 그 도함수는 
    
    $$ \frac{dw}{dt} = f_x(x(t), y(t)) \cdot x'(t) + f_y(x(t), y(t)) \cdot y'(t) $$
    
    또는 
    
    $$ \frac{dw}{dt} = \frac{\partial w}{\partial x}\frac{dx}{dt} + \frac{\partial w}{\partial y}\frac{dy}{dt} $$
    
    이다.

- 증명 

    증명은 $x,y$ 가 $t=t_0$ 에서 미분가능하면 $w$ 도 $t_0$ 에서 미분가능하고 

    점 $P_0 = (x(t_0),y(t_0))$ 에 대하여

    $$ \bigg (\dfrac{dw}{dt}\bigg )_{t_0} = \bigg (\dfrac{\partial w}{\partial x}\bigg )_{P_0} \bigg (\dfrac{d x}{d t}\bigg )_{t_0} +\bigg (\dfrac{\partial w}{\partial y}\bigg )_{P_0} \bigg (\dfrac{d y}{d t}\bigg )_{t_0} $$

    가 성립함을 보임으로써 완성된다.

    먼저 $\Delta x, \Delta y, \Delta w$ 를 $t$ 가 $t_0$ 에서 $t_0 + \Delta t$ 로 변할때의 증분이라고 하자. 이변수함수 $f$ 가 미분가능하다고 가정했으므로

    $\Delta x,y \to 0 \implies \epsilon _{1}, \epsilon _{2} \to 0$ 에 대하여

    $$ \Delta w =  \bigg (\dfrac{\partial w}{\partial x}\bigg )_{P_0}\Delta x+ \bigg (\dfrac{\partial w}{\partial y}\bigg )_{P_0} \Delta y+\epsilon _1 \Delta x+\epsilon _2 \Delta y $$

    이 성립한다.

    이 식을 $\Delta t$ 로 나누면

    $$ \dfrac{\Delta w}{\Delta t}  =  \bigg (\dfrac{\partial w}{\partial x}\bigg )_{P_0} \dfrac{\Delta x}{\Delta t} + \bigg (\dfrac{\partial w}{\partial y}\bigg )_{P_0} \dfrac{\Delta y}{\Delta t}+\epsilon _1  \dfrac{\Delta x}{\Delta t}+\epsilon _2 \dfrac{\Delta y}{\Delta t} $$

    를 얻는다. 이때 $\Delta t \to 0$ 이면

    $$ \lim_{\Delta t \to 0} \dfrac{\Delta w}{\Delta t}  =  \bigg (\dfrac{\partial w}{\partial x}\bigg )_{P_0} \bigg (\dfrac{dx}{dt}\bigg )_{t_0} + \bigg (\dfrac{\partial w}{\partial y}\bigg )_{P_0} \bigg (\dfrac{dy}{dt}\bigg ) _{t_0}+0 \cdot  \dfrac{\Delta x}{\Delta t}+0 \cdot \dfrac{\Delta y}{\Delta t} $$


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

!!! tldr ""

    일독립변수와 삼매개변수에 대한 함성함수의 도함수(chain rule) : 삼변수 함수 $w = f(x, y, z)$ 가 미분가능하고 $t$ 에 대한 함수 $x = x(t), y = y(t), z = z(t)$ 가 미분가능하면
    
    $t$ 에 대한 삼변수 합성함수 $w = f(x(t), y(t), z(t))$ 도 미분가능하며 그 도함수는 
    
    $$ \frac{dw}{dt} = \frac{\partial w}{\partial x}\frac{dx}{dt} + \frac{\partial w}{\partial y}\frac{dy}{dt} + \frac{\partial w}{\partial z}\frac{dz}{dt}$$
    
    이다.

- 증명 

    일독립변수와 이매개변수에 대한 도함수의 증명과 동일하다.

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

!!! tldr ""

    이독립변수와 삼매개변수에 대한 함성함수의 편도함수(chain rule) : 삼변수 함수 $w = f(x, y, z)$ 가 미분가능하고 $r, s$ 에 대한 함수 $x = x(r, s), y = y(r, s), z = z(r, s)$ 가 미분가능하면,
    
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

!!! tldr ""

    이독립변수와 이매개변수에 대한 함성함수의 편도함수(chain rule) : 이변수 함수 $w = f(x, y)$ 가 미분가능하고 $r, s$ 에 대한 함수 $x = x(r, s), y = y(r, s)$ 가 미분가능하면,
    
    이 $3$ 가지 함수는 모두 미분 가능하고 $w$ 는 $r$ 과 $s$ 에 대하여 각각 다음의 편도함수를 가진다. 
    
    $$ \frac{\partial  w}{\partial  r} = \frac{\partial w}{\partial x}\frac{\partial  x}{\partial  r} + \frac{\partial w}{\partial y}\frac{\partial  y}{\partial  r} $$
    
    $$ \frac{\partial  w}{\partial  s} = \frac{\partial w}{\partial x}\frac{\partial  x}{\partial  s} + \frac{\partial w}{\partial y}\frac{\partial  y}{\partial  s} $$



!!! tldr ""

    $1$ 개의 독립변수와 $m$ 개의 매개변수에 대한 다변수 합성함수의 편도함수(chain rule) : 유한개의 매개변수 $x_1, x_2, \dots, x_m$ 에 대한 다변수 함수 $w = f(x_1, x_2, \dots, x_m)$ 가 미분가능하고,
    
    $1$ 개의 독립변수 $p$ 에 대한 함수 $x_1, x_2, \dots, x_m$ 도 미분가능하면,
    
    $w$ 가 미분가능하고 $p$ 에 대한 함수들도 미분가능하며
    
    독립변수 $p$ 에 대한 편도함수는 다음과 같다. 
    
    $$ \frac{\partial  w}{\partial p} = \frac{\partial w}{\partial x_1}\frac{\partial  x_1}{\partial  p} + \frac{\partial w}{\partial x_2}\frac{\partial  x_2}{\partial  p} + \dots + \frac{\partial w}{\partial x_m}\frac{\partial  x_m}{\partial  p} = \sum_{k=1}^{m}\dfrac{\partial  w}{\partial x_k}\dfrac{\partial  x_k}{\partial p}$$



!!! tldr ""

    $n$ 개의 독립변수와 $1$ 개의 매개변수에 대한 다변수 합성함수의 편도함수(chain rule) : $1$ 개의 매개변수 $x$ 에 대한 일변수 함수 $w = f(x)$ 가 미분가능하고,
    
    $n$ 개의 독립변수 $p_1, p_2, \dots, p_n$ 에 대한 다변수 함수 $x$ 도 미분가능하면,
    
    $w$ 가 미분가능하고 $p_1, p_2, \dots, p_n$ 에 대한 함수 $x$ 도 미분가능하며
    
    각각의 독립변수에 대한 $w$ 의 편도함수는 다음과 같다. 
    
    $$ \frac{\partial  w}{\partial p_1} = \frac{\partial w}{\partial x}\frac{\partial  x}{\partial  p_1} $$
    
    $$ \frac{\partial  w}{\partial p_2} = \frac{\partial w}{\partial x}\frac{\partial  x}{\partial  p_2} $$
    
    $$ \vdots $$
    
    $$ \frac{\partial  w}{\partial p_n} = \frac{\partial w}{\partial x}\frac{\partial  x}{\partial  p_n} $$



!!! tldr ""

    $n$ 개의 독립변수와 $m$ 개의 매개변수에 대한 다변수 합성함수의 편도함수(chain rule) : 유한개의 매개변수 $x_1, x_2, \dots, x_m$ 에 대한 다변수 함수 $w = f(x_1, x_2, \dots, x_m)$ 가 미분가능하고,
    
    $n$ 개의 독립변수 $p_1, p_2, \dots, p_n$ 에 대한 함수 $x_1, x_2, \dots, x_m$ 도 미분가능하면,
    
    $w$ 가 미분가능하고 $p_1, p_2, \dots, p_n$ 에 대한 함수들도 미분가능하며
    
    각각의 독립변수에 대한 $w$ 의 편도함수는 다음과 같다. 
    
    $$ \frac{\partial  w}{\partial p_1} = \frac{\partial w}{\partial x_1}\frac{\partial  x_1}{\partial  p_1} + \frac{\partial w}{\partial x_2}\frac{\partial  x_2}{\partial  p_1} + \dots + \frac{\partial w}{\partial x_m}\frac{\partial  x_m}{\partial  p_1}= \sum_{k=1}^{m}\dfrac{\partial  w}{\partial x_k}\dfrac{\partial  x_k}{\partial p_1}$$
    
    $$ \frac{\partial  w}{\partial p_2} = \frac{\partial w}{\partial x_1}\frac{\partial  x_1}{\partial  p_2} + \frac{\partial w}{\partial x_2}\frac{\partial  x_2}{\partial  p_2} + \dots + \frac{\partial w}{\partial x_m}\frac{\partial  x_m}{\partial  p_2}= \sum_{k=1}^{m}\dfrac{\partial  w}{\partial x_k}\dfrac{\partial  x_k}{\partial p_2}$$
    
    $$ \vdots $$
    
    $$ \frac{\partial  w}{\partial p_n} = \frac{\partial w}{\partial x_1}\frac{\partial  x_1}{\partial  p_n} + \frac{\partial w}{\partial x_2}\frac{\partial  x_2}{\partial  p_n} + \dots + \frac{\partial w}{\partial x_m}\frac{\partial  x_m}{\partial  p_n}= \sum_{k=1}^{m}\dfrac{\partial  w}{\partial x_k}\dfrac{\partial  x_k}{\partial p_n}$$

# 기울기 벡터와 방향도함수

!!! tldr ""

    스칼라장(scalar field) : 공간 상의 모든 점에 스칼라가 대응되어 있는 분포이다.

- 유클리드 공간 $\mathbb{R} ^{n}$ 에서 스칼라장은 

    $$ F: A \in \mathbb{R} ^{n} \to \mathbb{R}, (a_1, a_2, \dots, a_n) \mapsto a $$

    으로 정의되는 사상(함수) 로써 정의역 $A$ 의 모든 원소 $x \in A$ 에 스칼라(실수), 즉 $F(x)$ 를 대응시킨다. 

- 예시 

    공간 상의 온도 분포는 스칼라장의 일종이다.

    호수의 수압 분포도 스칼라장의 일종이다. 

    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Scalar_field.png/330px-Scalar_field.png)

    위 그림은 스칼라장의 일종으로 색채에 대응하는 숫자를 색으로 표현한 것이다.

!!! tldr ""

    이변수함수의 $u$-방향미분계수, 또는 $u$-방향 순간변화율 : 데카르트 공간 $\mathbb{R} ^{3}$ 에서 정의된 이변수함수 $f(x,y)$ 와 한 점 $P_0(x_0,y_0)$ 와 단위벡터 $u = u_1i+u_2j$ 에 대한 극한값
    
    $$ (D_uf)_{P_0} := \bigg (\dfrac{df}{ds}\bigg )_{u,P_0} = \lim_{s \to 0} \dfrac{f(x_0+su_1, y_0 + su_2)-f(x_0,y_0)}{s} $$
    
    이다.

- 다음과 같이 표기하기도 한다.

    $$ D_uf(P_0) := \bigg (\dfrac{df}{ds}\bigg )_{u,P_0} = \lim_{s \to 0} \dfrac{f(x_0+su_1, y_0 + su_2)-f(x_0,y_0)}{s} $$

- $s$ 는 점 $P_0$ 에서 $u$ 방향으로의 곡선의 길이를 뜻한다. 

    그러므로 $\dfrac{df}{ds}$ 를 계산함으로써 $P_0$ 에서의 이변수함수 $f$ 의 순간변화율을 계산할 수 있는 것이다.

- 편미분계수 $f_x(x_0, y_0), f_y(x_0, y_0)$ 은 각각 점 $P_0$ 에 대한 $i$-방향미분계수, $j$-방향미분계수 였던 것이다.

    일변수 함수에서는 방향이 오직 하나였지만, 다변수 함수에서는 방향이 무한하므로 벡터 $u$ 를 통하여 미분 방향, 즉 변화율을 조사할 방향을 설정해야 한다.

- 기하학적 의미 

    <img src="https://user-images.githubusercontent.com/16812446/86775439-57dbc400-c092-11ea-94ea-ed93c3413888.png" width="70%" height="auto">

    > 출처 : [Thomas' CALCULUS](https://www.amazon.com/Thomas-Calculus-Early-Transcendentals-13th/dp/0321884078) Figure14.28

    위 그림과 같이 이변수 함수 $z=f(x,y)$ 는 곡면 $S$ 를 그린다.
    
    $z_0=f(x_0,y_0)$ 으로 곡면 $S$ 위에 위치한 점 $P(x_0,y_0,z_0)$ 에서 수직평면 $C$ 가 벡터 $u = u_1i+u_2j$ 방향으로 곡면 $S$ 를 가로지르고 있다.

    벡터 $u$ 방향으로의 $f$ 의 변화율은 접평면 $C$ 가 점 $P$ 와 만나는 지점에서 $u$ 방향으로의 변화율을 뜻하는 것이다.

    만약 $u=i$ 라면 점 $P_0$ 에서의 방향미분계수, 즉 순간변화율은 $\dfrac{\partial f}{\partial x} \bigg | _{(x_0, y_0)}$ 과 같게 되는 것이다. 즉 $x$ 축 방향 벡터 $u$ 로의 $f$의 순간변화율인 것이다.

    만약 $u=j$ 라면 점 $P_0$ 에서의 방향미분계수, 즉 순간변화율은 $\dfrac{\partial f}{\partial y} \bigg | _{(x_0, y_0)}$ 과 같게 되는 것이다. 즉 $y$ 축 방향 벡터 $u$ 로의 $f$의 순간변화율인 것이다.

    방향미분계수는 이것을 일반화하여 임의의 방향 벡터 $u$ 로의 $f$의 순간변화율을 계산할 수 있게 해주는 것이다.

    - 한편 곡면 $S$ 의 점 $P_0(x_0,y_0)$ 에서 벡터 $u$ 방향으로의 직선을 $xy$ 평면에서 표현해보면 다음과 같다.

        <img src="https://user-images.githubusercontent.com/16812446/86777767-865a9e80-c094-11ea-8374-29a5d45204db.png" width="50%" height="auto">

        > 출처 : [Thomas' CALCULUS](https://www.amazon.com/Thomas-Calculus-Early-Transcendentals-13th/dp/0321884078) Figure14.27

        이 직선을 독립변수 $s$ 와 벡터 $u=u_1i+u_2j$ 에 대한 매개변수 방정식

        $$ x = x_0+su_1, y = y_0 + su_2 $$

        으로 표현할 수 있다.

- 예시 

    이변수함수 $f(x,y) = x ^{2}+xy$ 의 점 $P_0(1,2)$ 에서 벡터 $u = (1/\sqrt[]{2})i+(1/\sqrt[]{2})j$ 방향의 순간변화율을 구해보자.

    방향미분계수의 정의에 따라

    $$ \bigg (\dfrac{df}{ds}\bigg )_{u,P_0} = \lim_{s \to 0} \dfrac{f(x_0+su_1, y_0 + su_2)-f(x_0,y_0)}{s} $$

    $$ = \lim_{s \to 0} \dfrac{f(1+s \cdot \dfrac{1}{\sqrt[]{2}}, 2 + s \cdot \dfrac{1}{\sqrt[]{2}})-f(1,2)}{s} $$

    $$ = \lim_{s \to 0} \dfrac{\bigg (1+s \cdot \dfrac{1}{\sqrt[]{2}} \bigg ) ^{2}+\bigg (1+s \cdot \dfrac{1}{\sqrt[]{2}} \bigg )\bigg (2 + s \cdot \dfrac{1}{\sqrt[]{2}}\bigg ) -3}{s} $$

    $$ = \lim_{s \to 0} \dfrac{\dfrac{5s}{\sqrt[]{2}}+s ^{2}}{s} = \lim_{s \to 0} \bigg (\dfrac{5}{\sqrt[]{2}}+s\bigg ) = \dfrac{5}{\sqrt[]{2}}$$

    이다. ■

!!! tldr ""

    이변수함수의 방향도함수 : 데카르트 공간 $\mathbb{R} ^{3}$ 에서 정의된 이변수함수 $f(x,y)$ 단위벡터 $u = u_1i+u_2j$ 에 대하여
    
    $f$ 의 정의역의 각 원소를 $u$-방향미분계수에 대응시켜 만든 함수
    
    $$ D_uf := \bigg (\dfrac{df}{ds}\bigg )_{u} = \lim_{s \to 0} \dfrac{f(x+su_1, y+ su_2)-f(x,y)}{s} $$
    
    이다.

- 이때 $x, y$ 를 벡터 $u = u_1i+u_2j$ 방향으로 향하는 직선

    $$ x = x_0 + su_1, y = y_0 + su_2 $$

    으로 한정시키자. 그래도 이변수 함수 $f(x,y)$ 의 벡터 $u$ 방향으로의 순간변화율을 구하기에 충분하다. 그러면 $f$ 의 $u$ 방향으로의 순간변화율은 독립변수 $s$ 에 의존하는 $x,y$ 를 변수로 갖는 이독립변수 일매개변수의 합성함수 미분으로 구할 수 있게 된다. 그러므로 

    $$ \bigg (\dfrac{df}{ds}\bigg )_{u} = \bigg (\dfrac{\partial f}{\partial x}\bigg )\dfrac{dx}{ds}+\bigg (\dfrac{\partial f}{\partial y}\bigg )\dfrac{dy}{ds} $$

    인데 $x = x_0 + su_1$ 를 $s$ 에 대하여 미분하면 $\dfrac{dx}{ds} = u_1$ 이고 $y = y_0 + su_2$ 를 $s$ 에 대하여 미분하면 $\dfrac{dy}{ds} = u_2$ 이므로

    $$ = \bigg (\dfrac{\partial f}{\partial x}\bigg )u_1+\bigg (\dfrac{\partial f}{\partial y}\bigg )u_2 $$

    인데 이것을 벡터 $\bigg <\dfrac{\partial f}{\partial x}, \dfrac{\partial f}{\partial y}\bigg >$ 와 벡터 $\big <u_1,u_2\big >$ 내적으로 표현하면

    $$ = \bigg[ \bigg (\dfrac{\partial f}{\partial x}\bigg )i+\bigg (\dfrac{\partial f}{\partial y}\bigg )j \bigg ]\cdot \bigg [u_1i+u_2j\bigg ] = \nabla f \cdot u = \text{grad}\ f \cdot u $$

    이다.

    - 이것은 다변수함수 $f$ 의 $u$ 방향의 미분이 벡터 $u$ 와 기울기벡터의 내적임을 알려준다.

!!! tldr ""

    방향도함수의 계산 : 단위벡터 $u$ 방향의 방향도함수의 계산은 기울기 벡터 $\nabla f$ 와 벡터 $u$ 와 두 벡터가 이루는 각 $\theta$ 에 대하여
    
    $$ \bigg (\dfrac{df}{ds}\bigg )_{u} = D_uf = \nabla f \cdot u = |\nabla f|\cos \theta $$
    
    이다.

- 증명

    $$ \bigg (\dfrac{df}{ds}\bigg )_{u} = D_uf = \nabla f \cdot u $$

    을 유도하는 과정은 이변수함수의 방향도함수에서 이미 다루었다.

    두 벡터 $u, v$ 가 이루는 코사인 유사도 $\cos  \theta = \dfrac{u \cdot v}{|u||v|}$ 에 두 벡터 $\nabla f, u$ 를 적용하면

    $$ \cos \theta = \dfrac{\nabla f \cdot u}{|\nabla f||u|} $$

    이므로 

    $$ \nabla f \cdot u = |\nabla f||u| \cos \theta $$

    를 얻는다. 따라서

    $$ D_uf = \nabla f \cdot u = |\nabla f||u| \cos \theta $$

    에서 $u$ 는 단위벡터이므로 $|u|=1$ 을 이용하여

    $$ \therefore D_uf = |\nabla f| \cos \theta $$

    를 얻는다. ■ 

- **가장 급격하게 변화하는 방향으로의 방향도함수**

    방향도함수가 결국 

    $$ \bigg (\dfrac{df}{ds}\bigg )_{u} = |\nabla f|\cos \theta $$

    이므로 방향도함수의 방향을 나타내는 벡터 $u$ 와 기울기 벡터 $\nabla f$ 가 이루는 각 $\theta$ 가 $0$ 일때 방향도함수 값이 최대가 된다. 즉, 다변수 함수의 변화율이 최대가 된다. 

    왜냐하면 $\cos \theta$ 함수값은 폐구간 $[-1, 1]$ 에서 존재하는데, 최댓값 $1$ 을 내기 위해서는 $\theta = 0$ 이어야 하기 때문이다. 

    이는 곧 방향도함수의 방향 $u$ 가 기울기벡터 $\nabla f$ 와 이루는 각이 $0 \degree$, 즉 두 벡터가 동일할 때 다변수함수의 변화율이 가장 크다는 뜻이다.

    이것은 기울기벡터 $\nabla f = \text{grad}\ f$ 는 다변수 함수의 최대변화율의 방향을 나타내고 있다는 것이다.

- **가장 급격하게 감소하는 방향으로의 방향도함수**

    반대로 다변수 함수 $f$ 가 가장 급격하게 감소하는 방향벡터 $u$ 를 구해보자. 마찬가지로 방향도함수의 계산이 

    $$ \bigg (\dfrac{df}{ds}\bigg )_{u} = |\nabla f|\cos \theta $$

    인데 $\cos \theta$ 이 폐구간 $[-1, 1]$ 에 존재하므로 $\cos \theta = -1$ 을 내기 위하여 방향벡터 $u$ 가 기울기 벡터 $\nabla f$ 와 이루는 각이 $\theta=\pi$ 가 되어야 한다.

    즉, 방향벡터 $u$ 가 기울기벡터와 정반대방향을 향하면 방향도함수가

    $$ \bigg (\dfrac{df}{ds}\bigg )_{u} = -|\nabla f|$$

    가 되어 가장 급격하게 감소하는 방향으로의 변화율을 구할 수 있게 된다.

- **변하지않는 방향으로의 방향도함수**

    다변수 함수 $f$ 가 변하지 않는 방향으로의 방향벡터 $u$ 를 구해보자. 방향도함수의 계산이 

    $$ \bigg (\dfrac{df}{ds}\bigg )_{u} = |\nabla f|\cos \theta $$

    인데 $\cos \theta$ 이 폐구간 $[-1, 1]$ 에 존재하므로 $\cos \theta = 0$ 이면 즉, 방향벡터 $u$ 가 기울기벡터와 직교하면 방향도함수가

    $$ \bigg (\dfrac{df}{ds}\bigg )_{u} = |\nabla f| \cdot 0$$

    이 되어 변하지 않는 방향으로의 방향벡터 $u$ 를 구할 수 있게 된다. 이 조건은 $\theta= \dfrac{\pi }{2} = 90 \degree$ 이므로 결국 방향벡터 $u$ 와 기울기벡터 $\nabla f$ 가 직교하는 방향으로 향할 때 변하지 않는 방향으로의 변화율을 구할 수 있는 것이다.

- 예시

    이변수함수 $f(x, y) = xe ^{y}+\cos (xy)$ 의 벡터 $v = 3i-4j$ 방향의 방향도함수의 점 $(2,0)$ 에서의 방향미분계수를 구해보자.

    먼저 벡터 $v$ 를 단위벡터로 바꾸면 $u = \dfrac{v}{|v|}=\dfrac{v}{5}=\dfrac{3}{5}i-\dfrac{4}{5}j$, 즉 $\bigg <\dfrac{3}{5},-\dfrac{4}{5}\bigg >$ 이다.

    또 기울기 벡터는 

    $$ \bigg <\dfrac{\partial  f}{\partial x},\dfrac{\partial f}{\partial y}\bigg > = \big < e ^{y}-y \sin (xy), x e ^{y}-x \sin (xy) \big > $$

    이다.

    그러므로 방향도함수는 

    $$ D_uf = \big < e ^{y}-y \sin (xy), x e ^{y}-x \sin (xy) \big > \cdot \bigg <\dfrac{3}{5},-\dfrac{4}{5}\bigg >$$ 

    $$ = \dfrac{3}{5}(e ^{y}-y \sin (xy))-\dfrac{4}{5}(x e ^{y}-x \sin (xy)) $$

    이다. 따라서 점 $(2,0)$ 에서 벡터 $v$ 방향으로의 방향미분계수는

    $$ D_uf \bigg | _{(2,0)} = \dfrac{3}{5}(e ^{0}-0 \cdot \sin (2 \cdot 0))-\dfrac{4}{5}(2 \cdot e ^{0}- 2 \sin (2 \cdot 0)) $$

    $$ = \dfrac{3}{5}(1 - 0) - \dfrac{4}{5}(2 - 0) = \dfrac{3-8}{5} = -1 $$

    이다. ■ 
    
# 삼각함수로 정의한 방향도함수

!!! tldr ""

    삼각함수로 정의한 이변수 함수의 방향도함수(directional derivative) : 스칼라 함수 $f(x, y)$ 에 대하여 단위벡터 $u = \big < \cos \theta , \sin \theta \big >$ 방향의 방향도함수는 
    
    함수 $f$ 의 벡터 $u$ 방향으로의 순간변화율로써
    
    $$ D _{u} f(x, y) = \lim_{h \to 0} \frac{f(x + h \cos \theta , y + h \sin \theta )-f(x, y)}{h}  $$
    
    이다.

- 위 정의는 다음 그림과 같이

    ![캡처](https://user-images.githubusercontent.com/16812446/79028349-9a445080-7bca-11ea-8ac9-596994fdd522.PNG)

    https://www.youtube.com/watch?v=ehrGmxqQsjo&t=98s

    단위벡터 $u = \big < \cos \theta , \sin \theta \big >$ 의 방향이 $x$ 축과 이루는 각이 $\theta$ 이고 두 점 $P, Q$ 와 의 거리를 $h$ 로 두었을 때

    $$ D _{u} f(x, y) = \lim_{h \to 0} \frac{f(x + h \cos \theta , y + h \cos (\frac{\pi }{2}-\theta) )-f(x, y)}{h} $$

    와 같이 정의된 방향도함수에서 

    $$ \cos \bigg  (\frac{\pi }{2} - \theta \bigg ) = \sin \theta $$

    를 사용하여 간단하게 만든 것이다. 

- 증명

    위 그래프의 점 $P, Q$ 의 거리를 $h$ 라 하고 두 점을 $xy$ 평면으로 내려 떨어뜨리면

    ![캡처](https://user-images.githubusercontent.com/16812446/79028367-ae884d80-7bca-11ea-9268-0e46b10e1dd6.PNG)

    https://www.youtube.com/watch?v=ehrGmxqQsjo&t=98s

    이와 같이 되는 것을 생각하자. 노란선이 단위 벡터 $u$ 의 방향을 나타내며 지금 우리의 목적은 이 방향으로의 함수 $f$ 의 변화율을 구하는 것이다. 

    이제 기존의 도함수의 정의

    $$ \lim_{h \to 0} \frac{f(x + \Delta x, y + \Delta y )-f(x, y)}{h} $$

    에서 $\Delta x, \Delta y$ 를 푸는 것이 목적이다. 

    단위벡터 $u$ 의 방향이 $x$ 축으로부터 $\theta$ 만큼 벌어져있기 때문에 위 그림처럼 한 각을 $\theta$ 로 하고 밑변과 높이의 길이를 $\Delta x, \Delta y$ 로 하는 직각 삼각형을 생각할 수 있다. 위 그림에서 빨간색 직각삼각형이 그것이다. 

    이 직각삼각형의 빗변의 길이는 두 점 $P, Q$ 와의 거리와 같으므로 $h$ 이다. 

    이때 이 직각삼각형의 한 각 $\theta$ 에서 $\cos \theta$ 는 $\theta$ 를 기준으로 빗변에 대한 밑변의 비율이기 때문에

    $$ \cos \theta = \frac{\Delta x}{h} $$

    에서

    $$ \therefore \Delta x = h \cdot \cos \theta $$

    이다. 또한 이 직각삼각형의 한 각 $\theta$ 에서 $\sin \theta$ 는 $\theta$ 를 기준으로 빗변에 대한 높이의 비율이기 때문에

    $$ \sin \theta = \frac{\Delta y}{h} $$

    에서

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

- $\dfrac{\partial f}{\partial x}$ 의 기하학적 의미를 기억하자. 

    ![2v](https://user-images.githubusercontent.com/16812446/78995906-63e0e400-7b7e-11ea-9f1e-76382bc9c548.jpg)

    그것은 위 그림의 왼쪽 그래프와 같이 곡면 $f(x, y)$ 와 $x$ 축에 평행한 평면과의 교선의 접선의 기울기였다. 

    그러한 교선은 수없이 많은데 $y$ 에 따라 점 $P(x_0, y_0)$ 가 상주하고 있는 교선을 얻었다고 하자.

    이제 이 교선에서 $x$ 에 따라 점 $P$ 가 결정되어서 이 $P$ 에서 $x$ 축에 평행한 접선의 기울기가 편미분계수 

    $$ \frac{\partial f}{\partial x} \bigg | _{(x_0, x_0)} $$

    의 의미였다. 

    그리고 그러한 특수한 점 $P(x_0, y_0)$ 을 일반화하여 일반적인 점 $P(x, y)$ 로 만들자. 이 독립변수 $x, y$ 로 결정되는 점 $P$ 에 따른 기울기를 함수로 표현한 것이 

    $$ \frac{\partial f}{\partial x} $$

    의 의미였고 이것을 $x$ 에 관한 편도함수라고 불렀다. 

    그런데 $\dfrac{\partial f}{\partial x}$ 을 벡터의 관점에서 표현하면 "함수 $f$ 의 표준 단위 벡터 $i$ 방향으로의 변화율" 이라고 표현 할 수 있다. 

    - 표준 단위 벡터 $i$ 는 $\big <1, 0, 0 \big >$ 이었고 이것은 $x$ 축 상의 단위벡터 였다.

        그런데 $x$ 에 관한 편도함수는 곡면을 $x$ 축과 평행하도록 잘라서 교선을 얻어서 그 위의 기울기를 구하는 것과 같다. 

        또한 편도함수는 도함수의 일종이고 도함수는 함수의 변화율을 나타내는 것임을 기억하자.

        그렇다면 결론적으로 

        $$\frac{\partial f}{\partial x}$$

        를 "$x$ 축과 평행하도록 교선을 만든다" 고 할 수 있고 

        이것을 다시 "함수 $f$ 의 벡터 $i$ 방향으로의 변화율" 을 구한다고 표현할 수 있다. 

    - 따라서 $\dfrac{\partial f}{\partial x}$ 을 또 다시 방향도함수의 정의에 따라서 "함수 $f$ 의 벡터 $i$ 방향의 방향도함수" 라고도 표현할 수 있다. 

        즉 함수 $f$ 의 $x$ 에 대한 편도함수는 방향도함수의 벡터 $i$ 방향으로의 아주 특수한 경우라고 할 수 있다. 

    - 그러면 $\dfrac{\partial f}{\partial y}$ 도 마찬가지로 방향도함수의 정의에 따라서 "함수 $f$ 의 벡터 $j$ 방향의 방향도함수" 라고도 표현할 수 있다. 

        표준 단위 벡터 $j$ 는 $\big <0, 1, 0 \big >$ 이었고 이것은 $y$ 축 상의 단위벡터 였다.

        즉 함수 $f$ 의 $y$ 에 대한 편도함수는 방향도함수의 벡터 $j$ 방향으로의 아주 특수한 경우라고 할 수 있다. 

- 예시 

    $\theta = 0$ 일 때, 즉 $u = i = \big < 1, 0\big >$ 일 때, 그러니까 단위벡터 $u$ 의 방향이 $x$ 축 일때,

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

    $\theta = \frac{\pi}{2}$ 일 때, 즉 $u = j = \big < 0, 1\big >$ 일 때, 그러니까 단위벡터 $u$ 의 방향이 $y$ 축일 때,

    함수 $f(x, y)$ 의 방향도함수는

    $$ D _{u} f(x, y) = \lim_{h \to 0} \frac{f(x + h \cos \theta , y + h \sin \theta )-f(x, y)}{h} $$

    에서

    $$ D _{u} f(x, y) = \lim_{h \to 0} \frac{f(x , y + h )-f(x, y)}{h} $$

    가 된다. 

    이것은 이변수 함수의 $x$ 에 대한 편도함수

    $$ \frac{\partial f}{\partial y} $$

    의 정의와 같다.

!!! tldr ""

    기울기 벡터(gradient vector, gradient) : 스칼라 함수 $f(x, y)$ 의 기울기는 벡터함수 
    
    $$ \text{grad} f = \nabla f = \frac{\partial f}{\partial x}i + \frac{\partial f}{\partial y}j =  \bigg <\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}\bigg > $$
    
    이다.

- 다음과 같이 표기하기도 한다.

    $$  \nabla f(x, y) = \bigg < f_x(x, y), f_y(x, y) \bigg > $$

- 기울기 벡터는 함수의 증가율이 최대가 되는 방향, 즉 스칼라장의 최대 증가율을 나타내는 벡터장이다. 

    - 증명

        방향도함수는 한 지점에서 함수의 무수히 많은 방향으로의 순간변화율을 알려준다. 지금의 목표는 방향도함수 값이 최대가 되는 방향의 단위벡터를 찾는 것이다. 그러면 그 방향으로의 순간변화율이 함수를 가장 많이 변화시키는 방향이 된다. 

        임의의 방향의 단위 벡터 $v$ 에 대한 이 방향도함수의 계산은 다음과 같았다.

        $$ D _{u}f (x, y) = \nabla f \cdot v $$

        이때 두 벡터 $\nabla f, v$ 가 이루는 각이 $\theta$ 일 때 두 벡터가 이루는 각을 이용한 내적의 계산법에 의하여

        $$ \nabla f \cdot v = |\nabla f||v| \cos \theta $$

        이다. 

        그런데 $\cos \theta$ 는 폐구간 $[-1, 1]$ 에서 정의되므로 방향도함수 값이 최대가 되려면 

        $$ \cos \theta = 1 \to \theta = 0 $$

        이어야 한다. 

        이것은 곧 두 벡터 $\nabla f, v$ 가 이루는 각이 $0$ 일 때, 즉 두 벡터가 똑같을 때 방향도함수 값이 최대가 됨을 뜻한다. 

        다시말해서 임의의 방향으로의 단위벡터 $v$ 가 기울기 벡터 $\nabla f$ 의 방향과 같을 때 방향도함수 값을 최대가 되고, 그 방향으로의 순간변화율이 함수를 가장 많이 변화시킨다. 

        그러므로 기울기 벡터 $\nabla f$ 의 방향이 함수의 증가율이 최대가 되는 방향을 가르킨다. 

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

- 예시 

    $f(x, y, z) = xy ^{2} + 2x ^{2} + z ^{3}$ 일 때 $\nabla f(1, 2, 3)$ 를 구해보자. 

    먼저 기울기 벡터는 

    $$ \nabla f = \bigg < \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z} \bigg > $$

    에서 

    $$ = \bigg < y ^{2}+4x, 2xy, 3z ^{2} \bigg > $$

    이다. 그러므로 

    $$ \therefore \nabla f(1, 2, 3) = \big < 8, 4, 27\big > $$

!!! tldr ""

    기울기 벡터 방향의 단위벡터 : 기울기 벡터 $\nabla f$ 방향으로의 단위벡터는
    
    $$ \frac{\nabla f}{|\nabla f|} $$

    이다.

- 증명

    임의의 벡터 $v$ 방향으로의 단위벡터는

    $$ \frac{v}{|v|} $$

    이므로 기울기 벡터 $\nabla f$ 방향으로의 단위벡터는

    $$ \therefore \frac{\nabla f}{|\nabla f|} $$

    이다.

- 방향도함수에서 최대증가율을 의미하는 기울기벡터를 사용하여 함수가 최대로 변화는 방향을 알고 싶다고 하자.

    그런데 기울기벡터에는 그것이 단위벡터라는 보장이 없다. 하지만 방향도함수는 단위 벡터를 사용해야 한다. 

    따라서 기울기 벡터를 단위벡터로 만들어주는 정규화과정을 거쳐야 한다. 

- 예시 

    삼변수함수 $f(x,y,z) = x ^{2}yz$ 의 점 $(1, 1, 1)$ 에서 변화율이 최대인 방향을 가르키는 단위벡터 $\overrightarrow{u}$ 를 구하자. 

    먼저 기울기 벡터 

    $$ \nabla f(x, y, z) = \big < 2xyz, x ^{2}z, x ^{2}y \big > $$

    에서

    $$ \therefore \overrightarrow{u} = \frac{\nabla f(1, 1, 1)}{|\nabla f(1, 1, 1)|} = \frac{\big < 2, 1, 1 \big > }{\bigg |\big < 2, 1, 1 \big > \bigg |} = \frac{\big <2, 1, 1 \big >}{\sqrt[]{6}} $$

    이다.

!!! tldr ""

    방향도함수의 계산 : 이변수 함수 $z = f(x, y)$ 가 $x, y$ 에 관한 편도함수를 각각 가지면 임의의 단위벡터 $u = \big < \cos \theta, \sin \theta \big >$ 에 대하여 
    
    $$ D _{u}f(x, y) = f_x(x, y) \cos \theta + f_y(x, y) \sin \theta $$
    
    또는 
    
    $$ D _{u}f(x, y) = \frac{\partial f}{\partial x} \cos \theta + \frac{\partial f}{\partial y} \sin \theta $$
    
    이다.

- 이 관계식은 기울기벡터의 정의 

    $$ \text{grad} f = \nabla f =  \bigg <\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}\bigg > $$

    와 단위벡터 $u = \big < \cos \theta, \sin \theta \big >$ 의 내적을 이용하여 더욱 간단하게 

    $$ D _{u}f(x, y) = \text{grad} f \cdot u = \nabla f \cdot u =  \bigg <\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}\bigg > \cdot u $$

    으로 표현할 수 있다. 

- 증명 

    함수 $g(t) = f(x + t \cos \theta, y + t \sin \theta)$ 를 정의하자. 그리고 편의상 $A = x + t \cos \theta, B = y + t \sin \theta$ 로 두자. 그러면 

    $$ g(t) = f(A, B) $$

    이다. 이제 함수 $g(t)$ 를 미분하자. $g(t)$ 는 일독립변수 $t$ 와 이매개변수 $A, B$ 에 대한 합성함수이므로 

    $$ g'(t) = \frac{d}{dt}f(A, B) = \frac{\partial }{\partial A}f(A, B) \frac{dA}{dt} + \frac{\partial }{\partial B}f(A,B)\frac{dB}{dt} $$

    이다. 그런데 

    $$ \frac{dA}{dt} = \frac{d}{dt}(x+t \cos \theta) = \cos \theta$$

    $$ \frac{dB}{dt} = \frac{d}{dt}(y+t \sin \theta) = \sin \theta$$

    이므로 

    $$ g'(t) = \frac{\partial }{\partial A}f(A, B) \cos \theta + \frac{\partial }{\partial B}f(A,B) \sin \theta $$

    이다. 이때 

    $$ t = 0 \to A = x, B = y $$

    이므로 

    $$ g'(0) = \frac{\partial }{\partial x}f(x, y) \cos \theta + \frac{\partial }{\partial y}f(x,y) \sin \theta \tag{1} $$

    이다. 

    한편 도함수의 정의에 의한 $g(t)$ 의 도함수

    $$ g'(t) = \lim_{h \to 0} \frac{g(t+h)-g(t)}{h} $$

    에서

    $$ g'(0) = \lim_{h \to 0} \frac{g(h)-g(0)}{h} = \lim_{h \to 0} \frac{f(x + h \cos \theta, y + h \sin \theta)-f(x , y)}{h} $$

    인데 방향도함수의 정의

    $$ D _{u} f(x, y) = \lim_{h \to 0} \frac{f(x + h \cos \theta , y + h \sin \theta )-f(x, y)}{h} $$

    에 의하여 

    $$ g'(0) = D _{u}f(x, y) $$

    이다. 그러므로 (1) 에 의하여 최종적으로 

    $$ \therefore D _{u}f(x, y) = \frac{\partial }{\partial x}f(x, y) \cos \theta + \frac{\partial }{\partial y}f(x,y) \sin \theta $$

    이다. 

- 예시 

    이변수 함수 $f(x, y) = x ^{2}y$ 의 점 $(3, 4)$ 에서 벡터 $u = \bigg < \dfrac{1}{\sqrt[]{5}}, \dfrac{2}{\sqrt[]{5}}\bigg >$ 방향으로의 방향도함수는

    $$ f_x(3, 4) = 2xy \bigg  | _{(3, 4)} = 24 $$ 

    $$ f_y(3, 4) =x ^{2} \bigg  | _{(3, 4)} = 9 $$

    에서 

    $$ \therefore  D_u f(3, 4) = \nabla f \cdot u \bigg | _{(3, 4)} = \frac{24}{\sqrt[]{5}} + \frac{18}{\sqrt[]{5}} = \frac{42}{\sqrt[]{5}} $$

    이다.

!!! tldr ""

    삼변수 함수의 방향도함수 : 삼변수 함수 $f(x, y, z)$ 에 대하여 단위벡터 $u = \big < \cos \alpha , \cos \beta , \cos \gamma  \big >$ (단, $\cos ^{2}\alpha +\cos ^{2}\beta +\cos ^{2}\gamma =1$) 방향으로의 방향도함수는
    
    $$ D _{u}f(x,y,z) = \lim_{h \to 0} \frac{f(x+h \cos \alpha , y + h \cos \beta , z + h \cos \gamma )-f(x,y,z)}{h} $$
    
    이다.

- 이때 $\alpha$ 는 단위벡터 $u$ 가 $x$ 축과 이루는 각,

    $\beta$ 는 단위벡터 $u$ 가 $y$ 축과 이루는 각,

    $\gamma$ 는 단위벡터 $u$ 가 $z$ 축과 이루는 각이다.

- $\cos ^{2}\alpha +\cos ^{2}\beta +\cos ^{2}\gamma =1$ 의 조건은 단위벡터 $u$ 의 길이 $|u|$ 가 $1$ 임을 보장한다. 

- 즉 $x, y, z$ 의 증분을 각각 다음과 같이 정의한 것이다. 

    $$ \Delta x = h \cos \alpha , \Delta y = y + h \cos \beta , \Delta z= z + h \cos \gamma $$

!!! tldr ""

    삼변수 함수의 기울기 벡터(gradient vector) : 스칼라 함수 $w = f(x, y, z)$ 의 기울기는 벡터함수 
    
    $$ \text{grad} f = \nabla f = \frac{\partial f}{\partial x}i + \frac{\partial f}{\partial y}j + \frac{\partial f}{\partial z} k=  \bigg <\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z}\bigg > $$
    
    또는 
    
    $$ \nabla f(x, y, z) = \bigg < f_x(x, y, z), f_y(x, y, z), f_z(x, y, z) \bigg > $$
    
    로써 스칼라장의 최대 증가율을 나타내는 벡터장이다.



!!! tldr ""

    삼변수 함수의 방향도함수 계산 : 삼변수 함수 $w = f(x, y, z)$ 가 $x, y, z$ 에 관한 편도함수를 각각 가지면 임의의 단위벡터 $u$ 에 대하여 
    
    $$ D _{u}f(x, y, z) = \text{grad} f \cdot u = \nabla f \cdot u =  \bigg <\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z}\bigg > \cdot u $$
    
    이다.



!!! tldr ""

    열린집합 : 위상수학에서 열린집합은 스스로의 경계를 포함하지 않는 위상 공간의 부분집합이다.

- 예시

    양수 $r$ 에 대하여 $n$-공간의 한 점 $P$ 를 중심으로 반지름이 $r$ 인 열린공

    $$ \mathbb{B} ^{n}(P, r) := \{X \in \mathbb{R} ^{n} \Big ||X-P| < r\} $$

    은 열린 집합이다.

    다음은 2차원 열린 공으로써, 열린 원판 $\mathbb{B} ^{2}$ 이다.

    ![](https://mblogthumb-phinf.pstatic.net/20141228_119/dydrogud22_1419762043201Uk8cC_JPEG/2.jpg?type=w2)

# 선형화

!!! tldr ""

    선형화(linearization) : 함수 $f$ 가 $x=a$ 에서 미분가능할 때 $x=a$ 에서의 접선의 방정식
    
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

!!! tldr ""

    표준 선형 근사(standard linear approximation) : 선형화의 정의에서 $x=a$ 에서 함수 $f$ 의 함수 $L$ 에 의한 근사
    
    $$ f(x) \approx L(x) $$
    
    를 표준 선형 근사라한다.

- 이때 $x=a$ 를 근사의 중심이라 한다. 

## 미분

!!! tldr ""

    미분(differential) : $y = f(x)$ 를 미분가능한 함수이고 미분 $dx$ 가 독립변수일 때 미분 $dy$ 는 
    
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

!!! tldr ""

    미분의 추정(estimating with differentials) : 함수 $f(x)$ 가 $x = a$ 에서 미분가능할 때 $x = a$ 의 근방 $x = a + dx$ 에서 함수값이 변하는 정도 $f(a + dx)$ 는 근사적으로
    
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

!!! tldr ""

    접평면(tangent plane) : $3$ 차원 곡면의 한 접점에 존재하는 무수히 많은 접선들이 동시에 상주하고 있는 평면이다.
    
    ![index](https://user-images.githubusercontent.com/16812446/79077468-ec0ce800-7d3c-11ea-8d57-3c992ab66d6e.jpg)

- 위 그림과 같이 어떤 곡면에는 접선이 무수히 많고 그 접선들이 상주하는 평면이 곡면의 접평면이다.

!!! tldr ""

    법선벡터(normal vector) : 접평면에 직교하는 벡터이다.
    
    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Surface_normal_illustration.svg/220px-Surface_normal_illustration.svg.png)

- 즉 법선벡터는 위 그림의 화살표 벡터와 같이 $3$ 차원 곡면의 한 접점에서의 모든 접선과 직교한다.

!!! tldr ""

    이변수 함수 선형화 또는 접평면(tangent plane) : $f$ 의 연속인 편도함수들이 존재할 때 점 $P(x_0, y_0, z_0)$ 에서 곡면 $z = f(x, y)$ 에 대한 접평면의 방정식은 
    
    $$ z - z_0 = f_x(x_0, y_0)(x- x_0) + f_y(x_0, y_0)(y - y_0) $$
    
    또는 
    
    $$ L(x, y) = f(x_0, y_0) + f_x(x_0, y_0)(x-x_0) + f_y(x_0, y_0)(y - y_0) $$
    
    이고 이것은 이변수 함수 $f(x, y)$ 의 선형화이다.

- 또한 점 $P(x_0, y_0, z_0)$ 근방에서 

    $$ f(x, y) \approx L(x, y) $$

    이 성립한다.

    일변수 함수 $f$ 를 $x=a$ 에서 끝없이 확대했을 때 $x=a$ 에서 접선과 거의 똑같아지는 것과 같이 이변수 함수 $f$ 를 끝없이 확대하면 접평면의 방정식과 거의 똑같아지기 때문이다.

!!! tldr ""

    이변수 함수 미분 또는 전미분(total differential) : 점 $(x_0, y_0)$ 에서 점 $(x_0 + dx, y_0 + dy)$ 로 움직였을 때의 변화량 
    
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