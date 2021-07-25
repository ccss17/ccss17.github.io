# 미분(differential)

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

# 방향미분과 편미분의 일반적인 정의

!!! tldr ""

    **다변수함수의 변화율 조사와 일변수 함수의 변화율 조사의 차이점** : 일변수 함수의 미분에서는 변수가 변할 수 있는 방향이 본질적으로 하나뿐(변수가 증가하는 방향) 이지만 
    
    다변수 함수의 경우 변수의 변화의 방향이 무수히 많은데, 이 방향을 보통 단위벡터로 결정한다.

- 예시 

    우리에게 익숙한 일변수 함수 $y = f(x)$ 의 변화율을 조사할 때 변수 $x$ 의 변화에 관한 $y$ 의 변화율만 조사하면 되었었다.

    그런데 독립변수가 $2$ 개인 다변수 함수 $z = f(x, y)$ 의 변화율을 조사할 때는 변수 $x$ 의 변화에 관한 $z$ 의 변화율만 조사하는 것이 아니라 
    
    변수 $x$ 와 변수 $y$ 가 변하는 방향을 먼저 정의하고 $z$ 의 변화율을 조사해야 한다.

!!! tldr ""

    열린집합 또는 개집합(open set) : 위상수학에서 열린집합은 스스로의 경계를 포함하지 않는 위상 공간의 부분집합이다.

- 함수의 변화를 조사하려 할 때, 함수가 한 점에서 정의될 뿐 아니라 그 점의 근방에서 정의되어야 하는 것이 요구된다. 왜냐하면 그래야만 그 함수의 그 점에서의 변화를 조사하기에 용이하기 때문이다.

    따라서 미분법에서 함수의 정의역이 한 점을 포함하면, 그 점의 근방이 정의역에 포함되기를 바라는데 이런 집합을 열린 집합이라고 한다.

- 예시

    양수 $r$ 에 대하여 $n$-공간의 한 점 $P$ 를 중심으로 반지름이 $r$ 인 열린공

    $$ \mathbb{B} ^{n}(P, r) := \{X \in \mathbb{R} ^{n} \Big ||X-P| < r\} $$

    은 열린 집합이다.

    다음은 2차원 열린 공으로써, 열린 원판 $\mathbb{B} ^{2}$ 이다.

    ![](https://mblogthumb-phinf.pstatic.net/20141228_119/dydrogud22_1419762043201Uk8cC_JPEG/2.jpg?type=w2)

!!! tldr ""

    $v$-방향미분계수, 또는 $v$-방향 순간변화율 : $n$-공간의 열린 집합 $U$ 에서 정의된 함수 
    
    $$ f: U \to \mathbb{R} $$
    
    와 $U$ 의 한 점 $P$ 와 벡터 $v$ 에 대하여 극한값
    
    $$ D_vf(P) := \lim_{t \to 0} \dfrac{f(P+tv)-f(P)}{t}=\dfrac{d}{dt}\bigg | _{0}f(P+tv) $$
    
    이 존재하면 이 값을 점 $P$ 에서 $f$ 의 $v$-방향미분계수 또는 $v$-방향 순간변화율이라 한다.

- $t$ 는 점 $P$ 에서 벡터 $v$ 방향으로의 함수 $f$ 의 곡선의 길이를 뜻한다. 

    그러므로 $\dfrac{df}{dt}$ 를 계산함으로써 $v$ 방향으로의 순간변화율을 계산할 수 있는 것이다.

- 이때 벡터 $v$ 란 점 $P$ 를 시점으로 하는 벡터를 뜻한다. 이런 벡터를 점 $P$ 에서의 접벡터(tangent vector) 라 한다. 

    이 벡터는 함수를 그 방향으로 미분하도록 유도한다.

    - 일변수 함수에서는 방향이 오직 하나였지만, 다변수 함수에서는 방향이 무한하므로 벡터 $v$ 를 통하여 미분 방향, 즉 조사할 변화의 방향을 설정해야 한다.

    - 현대적인 미분기하학에서는 벡터와 미분작용소를 같은 것으로 본다.

    - 이처럼 개념을 그 자체로 정의하는 것이 아니라 행렬을 선형사상으로 보고, 공간의 기저를 좌표계로 볼 수 있듯이 
    
        다른 개념과의 관계로 그것을 정의하기도 한다.
  
- 단위벡터 $v$ 에 대한 $v$-방향미분계수의 기하학적 의미는 

    함수 $f$ 의 그래프를 직선 $P+tv$ 위에 한정하여 그렸을 때, 

    점 $(P, f(P))$ 에서 $f$ 의 그래프의 기울기를 뜻한다.

- 예시

    함수 $f(x,y) = x^2+y^2$ 에 대하여 점 $P=(0,1)$ 에서 $(2,3)$-방향미분계수를 구하면 

    $$ \dfrac{d}{dt}\bigg | _{0}f((0,1) + t(2,3)) = \dfrac{d}{dt}\bigg | _{0}f((2t,3t+1)) = \dfrac{d}{dt}\bigg | _{0}f(2t,3t+1) = $$

    $$ = \dfrac{d}{dt}\bigg | _{0}((2t) ^{2}+(3t+1) ^{2}) = (20t+6) \bigg | _{0} = 6 $$

    이다. ■ 

    즉, 함수 $f(x,y) = x^2+y^2$ 의 점 $P=(0,1)$ 에서 $(2,3)$ 방향으로의 순간변화율이 $6$ 이라는 것이다.

!!! tldr ""

    편미분계수 : $n$-공간의 $n$개의 축 방향의 단위벡터인 표준단위벡터 
    
    $$ e_1 := (1,0,\dots,0), \dots, e_n := (0,0,\dots,1), $$
    
    에 대하여 점 $P = (p_1, \dots,p_n)$ 에서 함수 $f: U \to \mathbb{R}$ 의 $e_k$-방향미분계수 
    
    $$D _{k}f(P) = \dfrac{\partial f(P)}{\partial x_k} = \dfrac{d}{dt}\bigg | _{0}f(p_1, \dots,p_k+t,\dots,p_n)$$
    
    를 점 $P$ 에서 $f$ 의 $k$번째 편미분계수라고 한다.

- 점 $P = (p_1, \dots,p_n)$ 에서 $f$ 의 $k$번째 편미분계수는 $P = (p_1, \dots,p_n)$ 의 $k$ 번째 성분만 변화시켜서 얻은 $f$ 의 변화율이다.

- 함수 $f$ 의 $k$번째 편미분계수 $\dfrac{\partial f}{\partial x_k}$ 는 $k$번째 성분만을 변수로 하고, 나머지 변수는 상수로 취급하여 얻은 미분계수이다.

- $\dfrac{df}{dx}$ 는 함수 $f$ 가 변수 $x$ 에 따라 변할 때 쓰는 기호였다. 

    하지만 함수 $f$ 가 일변수 $x$ 에만 의존하는 것이 아니라 
    
    다변수에 의존한다면 $\partial$ 을 사용하여 미분을 $\dfrac{\partial f}{\partial x}$ 로 표현한다.

- 예시 

    점 $P=(1,2,3)$ 에서 함수 $f(x,y,z) = x ^{2} y ^{3} + z$ 의 편미분계수들은 

    $$ D_1f(P) = \dfrac{\partial f}{\partial x}(P) = 2xy ^{3}(P) = 16 $$

    $$ D_2f(P) = \dfrac{\partial f}{\partial y}(P) = 3x ^{2} y ^{2}(P) = 12 $$

    $$ D_3f(P) = \dfrac{\partial f}{\partial z}(P) = 1 $$

    이다.

!!! tldr ""

    편도함수 : 함수 $f$ 가 점 $P = (p_1, \dots,p_n)$ 에 대하여 정의역 $U$ 의 모든 점에 대하여 $k$번째 편미분계수를 가지면 함수 
    
    $$ D_kf:U \to \mathbb{R}, P \mapsto D_kf(P) $$
    
    를 $f$의 $k$번째 편도함수라고 한다.

- 예시 

    함수 $r(x_1, \dots,x_n) := \sqrt[]{x_1 ^{2}+ \dots+x_n ^{2}}$ 의 편도함수를 구해보자. 
    
    $x_i$ 에 대하여 편미분하면 

    $$ \dfrac{\partial r}{\partial x_i} = \dfrac{\partial }{\partial x_i}\sqrt[]{x_1 ^{2}+ \dots+x_n ^{2}} = \dfrac{\partial }{\partial x_i}(x_1 ^{2}+ \dots+x_n ^{2})^{\frac{1}{2}} $$

    이다. $t = x_1 ^{2}+ \dots+x_n ^{2}$ 라고 두면,

    $$ = \dfrac{\partial }{\partial x_i}t^{\frac{1}{2}} = \dfrac{d t ^{\frac{1}{2}} }{d t} \dfrac{\partial t}{\partial x_i} = \dfrac{d t ^{\frac{1}{2}} }{d t} \dfrac{\partial (x_1 ^{2}+ \dots+x_n ^{2})}{\partial x_i} $$

    $$ = \dfrac{1}{2}t ^{\frac{1}{2}-1}(2x_i) = \dfrac{1}{t^{\frac{1}{2}} }(x_i) = \dfrac{x_i}{\sqrt[]{t}} $$

    이다. 그런데 $\sqrt[]{t} = \sqrt[]{x_1 ^{2}+ \dots+x_n ^{2}} = r$ 이므로

    $$ = \dfrac{x_i}{r} $$

    이다. ■ 

## 기울기 벡터의 일반적인 정의

!!! tldr ""

    편미분 가능 : $n$변수함수 $f$ 의 모든 편미분계수가 점 $P$ 에서 존재할 때, $f$ 는 점 $P$ 에서 편미분 가능하다.



!!! tldr ""

    기울기벡터(gradient vector) : $n$변수함수 $f$ 가 점 $P$ 에서 편미분가능할 때 벡터
    
    $$ \text{grad}\ f(P) := (D_1f(P), \dots, D_nf(P)) $$
    
    를 점 $P$ 에서 $f$ 의 기울기 벡터라고 한다.

- 기울기 벡터를 다음과 같이 표기하기도 한다.

    $$ \text{grad}\ f(P) := \Big < D_1f(P), \dots, D_nf(P) \Big > $$

    $$ \nabla f(P) := \bigg ( \dfrac{\partial f(P)}{\partial x_1}, \dots, \dfrac{\partial f(P)}{\partial x_n} \bigg ) = \bigg < \dfrac{\partial f(P)}{\partial x_1}, \dots, \dfrac{\partial f(P)}{\partial x_n} \bigg > $$

    - 다 같은 표기법이다.

    - $\nabla f$ 는 나블라 $f$ 또는 델 $f$ 라고 읽는다.

- 일변수함수 $f(x)$ 에서 접선의 기울기가 $f'(x)$ 인 것처럼, 

    다변수함수 $f(X)$ 의 그래프에서 접평면의 기울기 벡터가 $\text{grad} \ f(P)$ 이다.

- 예시 

    원점 $O = (0,0,0)$ 에서 함수 

    $$ f(x,y,z) = \exp (x+yz) $$

    의 기울기 벡터를 구해보자.

    $$ D_1f(x,y,z)=\dfrac{\partial \exp (x+yz)}{\partial x} = $$ 

    에서 상수배 함수 $y=cf(x)$ 의 도함수는 $y'=cf'(x)$ 이고, 함수 $y=e^x$ 의 도함수는 $y'=e^x$ 이므로
    
    $$ = \dfrac{\partial e ^{x+yz}}{\partial x} = e ^{x+yz} =f(x,y,z) $$

    이다. $\\blacktriangle$ 

    $$ D_2f(x,y,z) = \dfrac{\partial e ^{x+yz}}{\partial y} = $$

    에서 지수함수 $y=  a^x$ 의 도함수는 $y' = a^x \ln a$ 이므로 

    $$ = e ^{x}\dfrac{\partial (e ^{z})^{y}}{\partial y} = e ^{x}(e ^{z})^{y}\ln e ^{z} = e ^{x+zy} \cdot z = zf(x,y,z) $$

    이다. $\\blacktriangle$ 
    
    마찬가지로 

    $$ D_3f(x,y,z) = yf(x,y,z) $$

    이다. $\\blacktriangle$ 

    그런데 $f(O) = e^{0+0 \cdot 0} = 1$ 이므로 

    $$ D_1f(O) = 1, D_2f(O) =1 \cdot  0 = 0, D_3f(O) = 1 \cdot  0 = 0 $$

    이고, 이에따라 원점 $O$ 에서의 $f$ 의 기울기 벡터 

    $$ \therefore \text{grad}\ f(O) = (1,0,0) $$

    을 얻는다. ■ 

## 미분 가능의 일반적인 정의

!!! tldr ""

    **$n$-공간의 열린 집합에서 정의된 함수 $f$ 의 미분 가능** :

- 이 개념은 점 $P$ 에서 모든 벡터 $v$ 에 대한 방향미분계수 $D_vf(P)$ 가 존재한다는 것이 아니다.

    모든 방향미분계수가 존재하지만 연속함수가 아닐 수 있다. 

    하지만 미분가능함수는 항상 연속함수이다.

- 설명 

    $n=1$ 일 때 $n$-공간에서 함수 $f(x)$ 가 점 $p$ 에서 미분가능하다는 것은 $x=p$ 에서 미분계수 $f'(p)$ 가 존재한다는 것, 즉 평균변화율의 우극한과 좌극한이 같다는 것이었다. 이는 다시 말해 $x=p$ 에서 좌미분계수와 우미분계수가 같다는 것이다.

    기하학적으로 함수 $f$ 의 그래프가 점 $(p, f(p))$ 에서 접선을 가진다는 것이었다.

    점 $(p, f(p))$ 를 지나는 직선의 방정식은 어떤 실수 $a$ 에 대하여

    $$ y = f(p)+a(x-p) $$

    이었고, 이 직선이 $x=p$ 일 때 $y=f(x)$ 와 접한다는 것은 

    **(무슨 이유인지 모르겠지만)** $f(x)$ 와 $f(p) + a(x-p)$ 의 차가 $0$ 에 접근하는 것이 $x$ 가 $p$ 의 차가 $0$ 에 접근하는 것보다 훨씬 빠르다 **(이게 대체 무슨말일까?)** 는 뜻, 즉

    $$ \lim_{x \to p} \dfrac{f(x) - f(p) -a(x-p)}{x-p} = 0 $$

    이라고 한다. 

    그러므로 $n$-공간에서도 함수 $f$ 가

    **(책이 정말 어렵다..)**

!!! tldr ""

    일급함수 : $n$-공간의 열린 집합에서 정의된 함수 $f(x_1, \dots, x_n)$ 의 각 편도함수 
    
    $$ \dfrac{\partial f}{\partial x_1}, \dots,\dfrac{\partial f}{\partial x_n} $$
    
    가 연속이면, $f$ 를 일급함수 또는 $\mathcal{C} ^{1}$ 라고 한다.

# 다변수 벡터함수

!!! tldr ""

    함수의 분류 : 함수는 정의역과 공역의 차원을 기준으로 다음 $4$ 가지로 분류된다. 
    
    1. 실함수(real valued functions) : 다음과 같이 $1$차원에서 $1$차원으로 가는 함수이다.
    
        $$ \mathbb{R} \to \mathbb{R} $$
    
    2. 매개화된 곡선(parametrized curves) : 다음과 같이 $1$차원에서 $n$차원으로 가는 함수이다.
    
        $$ \mathbb{R} \to \mathbb{R} ^{n}$$
    
    3. 다변수 함수(functions of several variables) : 다음과 같이 $n$차원에서 $1$차원으로 가는 함수이다.
    
        $$ \mathbb{R} ^{n} \to \mathbb{R} $$
    
    4. 다변수 벡터함수(vector valued functions of several variables) : 다음과 같이 $n$차원에서 $m$차원으로 가는 함수이다.
    
        $$ \mathbb{R} ^{n} \to \mathbb{R} ^{m} $$

- 지금까지 실함수와 다변수함수의 미분을 살펴봤는데, 이제 다변수 벡터함수의 미분을 살펴본다. 

    다변수 벡터함수의 미분은 야코비 행렬로 표현된다. 정의역과 공역의 차원이 같은 함수, 즉 

    $$ R ^{n} \to R ^{n} $$

    는 야코비 행렬의 행렬식을 구할 수 있고, 이 값의 절대값은 부피변화율을 나타내는 것임을 알아볼 것이다.

!!! tldr ""

    다변수 벡터함수(vector valued functions of several variables) : $n$-공간의 한 부분집합에서 정의된 벡터함수
    
    $$ F: \mathbb{R} ^{n} \to \mathbb{R} ^{m} $$
    
    는 $F$ 의 성분함수 $f_1, \dots, f_m$ 에 대하여
    
    $$ F(x_1, \dots,x_n) = (f_1(x_1, \dots,x_n), \dots, f_m(x_1, \dots,x_n)) $$
    
    이다.

- 예시 

    함수 $F(x, y) = (e ^{x}\cos y, e ^{x}\sin y, x+y)$ 는 다변수 벡터함수이다.

!!! tldr ""

    야코비 행렬(jacobian matrix) : 열린집합 $U \subset \mathbb{R} ^{n}$ 에서 정의된 함수 벡터함수 $f: U \to \mathbb{R} ^{m}$ 가 $F = (f_1, \dots, f_m)$ 가 점 $P \in U$ 에서 미분가능하면 
    
    $f'_1(P) = \text{grad}\ f_1(P)$ 를 첫번째 행,
    
    $f'_2(P) = \text{grad}\ f_2(P)$ 를 두번째 행,
    
    $f'_m(P) = \text{grad}\ f_m(P)$ 를 마지막 행으로 하는 행렬
    
    $$ F'(P) := \dfrac{\partial (f_1, \dots, f_m)}{\partial (x_1, \dots, x_n)}(P) := \begin{pmatrix} \dfrac{\partial f_1}{\partial x_1}(P)&\dfrac{\partial f_1}{\partial x_2}(P)&\dots&\dfrac{\partial f_1}{\partial x_n}(P)\\ \dfrac{\partial f_2}{\partial x_1}(P)&\dfrac{\partial f_2}{\partial x_2}(P)&\dots&\dfrac{\partial f_2}{\partial x_n}(P)\\ \vdots &\ddots &\cdots&\vdots \\ \dfrac{\partial f_m}{\partial x_1}(P)&\dfrac{\partial f_m}{\partial x_2}(P)&\dots&\dfrac{\partial f_m}{\partial x_n}(P)\\ \end{pmatrix} $$
    
    을 점 $P$ 에서 $F$ 의 야코비 행렬이라고 한다.

- 예시 

    $F: \mathbb{R} ^{2} \to \mathbb{R} ^{3}$ 로 정의된 다변수 벡터함수 $F(x, y) = (e ^{x}\cos y, e ^{x}\sin y, x+y)$ 의 야코비행렬은 

    $$ F'(x, y) = \begin{pmatrix} e ^{x}\cos y&-e ^{x}\sin y\\ e ^{x}\sin y&e ^{x}\cos y\\ 1&1\\ \end{pmatrix} $$

    이다.

# 행렬 미분

> 출처/참고 : https://atmos.washington.edu/~dennis/MatrixCalculus.pdf

- 행렬 표기 

    $i \in \{1,2,\dots,m\}$, $j \in \{1,2,\dots,n\}$ 에 대한 $a _{ij}\in \mathbb{R}$ 에 대하여 행렬 

    $$ \mathbf{A}= \begin{bmatrix} a _{11} & a _{12} & \dots & a _{1n} \\ a _{21} & a _{22} & \dots & a _{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a _{m1} & a _{m2} & \dots & a _{mn} \\ \end{bmatrix} $$

    을 $m \times n$ 행렬이라 한다.

    - 이 행렬을 $i \in \{1,2,\dots,m\}$, $j \in \{1,2,\dots,n\}$ 에 대하여 

        $$ \mathbf{A} = [a _{ij}] $$

        라고 한다.
    
    - 이 행렬의 원소를 $a _{ij}$ 라고 한다.

    - $a _{jk}$ 는 $j$번째 행과 $k$번째 열의 원소를 말한다.

- 행렬곱 정의

    $m \times n$ 행렬 $\mathbf{A}$, $n \times p$ 행렬 $\mathbf{B}$ 에 대한 행렬곱은 $m \times p$ 행렬 $\mathbf{AB} = \mathbf{C}$ 이고, 

    $\mathbf{C}$ 의 $i \in \{1,\dots,m\}, j \in \{1,\dots,p\}$ 항 $(i,j)$ 는 

    $$ c _{ij} = \sum_{k=1}^{n}a _{ik}b _{kj} $$

    이다.

    - $\displaystyle \sum_{k=1}^{n}a _{ik}$ 는 $\mathbf{A}$ 의 $(i, 1), (i, 2), \dots, (i, n)$ 까지의 항을 뜻하므로 $\mathbf{A}$ 의 한 행의 모든 항을 뜻한다.

    - $\displaystyle \sum_{k=1}^{n}b _{kj}$ 는 $\mathbf{B}$ 의 $(1, j), (2, j), \dots, (n, j)$ 까지의 항을 뜻하므로 $\mathbf{B}$ 의 한 열의 모든 항을 뜻한다.

- 정리 1 

    - $m \times n$ 행렬 $\mathbf{A}$ 와 $n \times 1$ 행렬 $\mathbf{x} \in \mathbb{R} ^{n}$, 즉 벡터 $\mathbf{x}$ 에 대하여 

        $$ \mathbf{z} = \mathbf{Ax} $$

        는 $m \times 1$ 행렬, 즉 벡터 $\mathbf{z}\in \mathbb{R} ^{m}$ 이다.

        벡터 $\mathbf{z}$ 의 원소 $z_i$ 는 $a _{ik} \in \mathbf{A}, x_k \in \mathbf{x}$ 에 대하여 다음과 같이 결정된다. 

        $$ z_i = \sum_{k=1}^{n}a _{ik}x _{k} $$
    
    - 한편 $m \times 1$ 행렬 $\mathbf{y} \in \mathbb{R} ^{m}$ 에 대하여

        $$ \mathbf{z}^{T}=\mathbf{y}^{T}\mathbf{A} $$

        는 $n \times 1$ 행렬, 즉 벡터 $\mathbf{z} \in \mathbb{R} ^{n}$ 이다.

        - 이는 $(1 \times n) = (1 \times m)(m \times n)$ 의 결과이다.
    
    - 마지막으로 스칼라 $\alpha = \mathbf{y}^{T}\mathbf{Ax}$ 는 

        $$ \alpha = \sum_{j=1}^{m}\sum_{k=1}^{n}a _{jk}y_jx_k $$

        이다.
  
- 정리 2 

    $m \times n$ 행렬 $\mathbf{A}$, $n \times p$ 행렬 $\mathbf{B}$ 에 대한 행렬곱은 행렬 $\mathbf{C} = \mathbf{AB}$ 인데 이것의 전치행렬은 

    $$ \mathbf{C}^{\intercal }=\mathbf{B}^{\intercal }\mathbf{A}^{\intercal } $$

    이다.

    - 증명 

- 정리 3 

    $n \times n$ 가역행렬 $\mathbf{A,B}$ 에 대한 행렬곱 $\mathbf{C = AB}$ 에 대하여

    $$ \mathbf{C} ^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1} $$

    이다. 

    - 증명 

        $$ \mathbf{C B ^{-1}A ^{-1} = AB B ^{-1}A ^{-1} = I} $$

        이므로 $\mathbf{C}$ 의 역행렬은 $\mathbf{B ^{-1}A ^{-1}}$ 이다.

- 다변수벡터함수의 미분(야코비 행렬)

    - 벡터 $\mathbf{y} \in \mathbb{R} ^{m}$ 와 $\mathbf{x} \in \mathbb{R} ^{n}$ 에 대하여 다변수벡터함수

        $$ \mathbf{y} = \Psi (\mathbf{x}) $$

        가 존재한다. 이때 $\mathbf{y}$ 에 대한 $\mathbf{x}$ 의 미분은 다변수벡터함수의 미분, 즉 야코비 행렬 

        $$ \dfrac{\partial \mathbf{y}}{\partial \mathbf{x}} = \begin{bmatrix} \dfrac{\partial y_1}{\partial x_1} && \dfrac{\partial y_1}{\partial x_2} && \dots && \dfrac{\partial y_1}{\partial x_n} \\ \dfrac{\partial y_2}{\partial x_1} && \dfrac{\partial y_2}{\partial x_2} && \dots && \dfrac{\partial y_2}{\partial x_n} \\ \vdots && \vdots && \ddots && \vdots \\ \dfrac{\partial y_m}{\partial x_1} && \dfrac{\partial y_m}{\partial x_2} && \dots && \dfrac{\partial y_m}{\partial x_n} \end{bmatrix} $$

        이다.

        - 이 행렬을 변환 $\Psi ()$ 의 야코비 행렬이라고 한다.

- 정리 5 (다변수벡터함수 미분)

    벡터 $\mathbf{y} \in \mathbb{R} ^{m}$($m \times 1$ 행렬), $\mathbf{x} \in \mathbb{R} ^{n}$($n \times 1$ 행렬) 와 $m \times n$ 행렬 $\mathbf{A}$ 에 대한 행렬방정식 $\mathbf{y} = \mathbf{Ax}$ 의 미분은 

    $$ \dfrac{\partial \mathbf{y}}{\partial \mathbf{x}}=\mathbf{A} $$

    이다.

    - 증명 

        $\mathbf{y}$ 에 대한 $\mathbf{x}$ 의 미분은 다변수벡터함수의 미분, 즉 야코비행렬

        $$ \dfrac{\partial \mathbf{y}}{\partial \mathbf{x}} = \begin{bmatrix} \dfrac{\partial y_1}{\partial x_1} && \dfrac{\partial y_1}{\partial x_2} && \dots && \dfrac{\partial y_1}{\partial x_n} \\ \dfrac{\partial y_2}{\partial x_1} && \dfrac{\partial y_2}{\partial x_2} && \dots && \dfrac{\partial y_2}{\partial x_n} \\ \vdots && \vdots && \ddots && \vdots \\ \dfrac{\partial y_m}{\partial x_1} && \dfrac{\partial y_m}{\partial x_2} && \dots && \dfrac{\partial y_m}{\partial x_n} \end{bmatrix} $$

        이다. 그런데 $\mathbf{y}$ 의 $i$ 번째 원소는 $\displaystyle  y_i = \sum_{k=1}^{n}a _{ik}x_k$ 이므로 $y_i$ 에 대한 $x_j$ 의 미분은 

        $$ \dfrac{\partial y_i}{\partial x_j} = \dfrac{\partial }{\partial x_j}\bigg (\sum_{k=1}^{n}a _{ik}x_k \bigg ) = a _{ij} $$

        이다. 그러므로

        $$ \therefore  \dfrac{\partial \mathbf{y}}{\partial \mathbf{x}} = \begin{bmatrix} \dfrac{\partial y_1}{\partial x_1} && \dfrac{\partial y_1}{\partial x_2} && \dots && \dfrac{\partial y_1}{\partial x_n} \\ \dfrac{\partial y_2}{\partial x_1} && \dfrac{\partial y_2}{\partial x_2} && \dots && \dfrac{\partial y_2}{\partial x_n} \\ \vdots && \vdots && \ddots && \vdots \\ \dfrac{\partial y_m}{\partial x_1} && \dfrac{\partial y_m}{\partial x_2} && \dots && \dfrac{\partial y_m}{\partial x_n} \end{bmatrix} =  \begin{bmatrix} a_{11} && a_{12} && \dots && a_{1n} \\ a_{21} && a_{22} && \dots && a_{2n} \\ \vdots && \vdots && \ddots && \vdots \\ a_{m1} && a_{m2} && \dots && a_{mn} \end{bmatrix} = \mathbf{A} $$

        이다. ■ 
    
- 정리 6 (매개변수를 갖는 행렬방정식의 미분)

    벡터 $\mathbf{y} \in \mathbb{R} ^{m}$($m \times 1$ 행렬), $\mathbf{x} \in \mathbb{R} ^{n}$($n \times 1$ 행렬) 와 $m \times n$ 행렬 $\mathbf{A}$ 이 존재할때 $\mathbf{x}$ 가 벡터 $\mathbf{z}$ 에 대한 함수라면 행렬방정식 $\mathbf{y} = \mathbf{Ax}$ 의 미분은 

    $$ \dfrac{\partial \mathbf{y}}{\partial \mathbf{z}} = \dfrac{\partial \mathbf{y}}{\partial \mathbf{x}}\dfrac{\partial \mathbf{x}}{\partial \mathbf{z}} = \mathbf{A}\dfrac{\partial \mathbf{x}}{\partial \mathbf{z}} $$ 

    이다.

    - 증명 

        $\mathbf{y}$ 의 $i$ 번째 원소는 $\displaystyle y_i = \sum_{k=1}^{n}a _{ik}x _{k}$ 이다. 또 $\mathbf{x} \in \mathbb{R} ^{n}$ 는 독립변수 $\mathbf{z} \in \mathbb{R} ^{n}$ 를 $\mathbf{y} \in \mathbb{R} ^{m}$ 로 잇는 매개변수이다. 그러므로 $y_i$ 에 대한 $z_j$ 의 미분은 $1$ 개의 독립변수와 $n$ 개의 매개변수에 대한 일변수 합성함수에 대한 미분이다. 따라서 $y_i$ 에 대한 $z_j$ 의 미분은 

        $$ \dfrac{\partial y_i}{\partial z_j} = \dfrac{\partial y_i}{\partial  x_1}\dfrac{\partial x_1}{\partial z_j} +\dfrac{\partial y_i}{\partial  x_2}\dfrac{\partial x_2}{\partial z_j} +\dots +\dfrac{\partial y_i}{\partial  x_n}\dfrac{\partial x_n}{\partial z_j} = \sum_{k=1}^{n}\dfrac{\partial y_i}{\partial x_k}\dfrac{\partial x_k}{\partial z_j} = \sum_{k=1}^{n}a _{ik}\dfrac{\partial x_k}{\partial z_j} $$

        이다. 

        그렇다면 $\mathbf{y}$ 에 대한 $\mathbf{z}$ 의 미분은 일독립변수와 $n$매개변수를 갖는 다변수벡터 합성함수의 미분, 즉 다변수벡터 합성함수의 야코비 행렬
        
        $$ \dfrac{\partial \mathbf{y}}{\partial \mathbf{z}} = \begin{bmatrix} \dfrac{\partial y_1}{\partial z_1} & \dfrac{\partial y_1}{\partial z_2} & \dots& \dfrac{\partial y_1}{\partial z_n}  \\ \dfrac{\partial y_2}{\partial z_1} & \dfrac{\partial y_2}{\partial z_2} & \dots& \dfrac{\partial y_2}{\partial z_n}  \\ \vdots  & \vdots &\ddots &\vdots \\ \dfrac{\partial y_m}{\partial z_1} & \dfrac{\partial y_m}{\partial z_2} & \dots& \dfrac{\partial y_m}{\partial z_n}  \\ \end{bmatrix} = \begin{bmatrix} \displaystyle\sum_{k=1}^n a_{1k}\dfrac{\partial x_k}{\partial z_1} && \displaystyle\sum_{k=1}^n a_{1k}\dfrac{\partial x_k}{\partial z_2} && \dots && \displaystyle\sum_{k=1}^n a_{1k}\dfrac{\partial x_k}{\partial z_n} \\ \displaystyle\sum_{k=1}^n a_{2k}\dfrac{\partial x_k}{\partial z_1} && \displaystyle\sum_{k=1}^n a_{2k}\dfrac{\partial x_k}{\partial z_2} && \dots && \displaystyle\sum_{k=1}^n a_{2k}\dfrac{\partial x_k}{\partial z_n} \\ \vdots && \vdots && \ddots && \vdots \\ \displaystyle\sum_{k=1}^n a_{mk}\dfrac{\partial x_k}{\partial z_1} && \displaystyle\sum_{k=1}^n a_{mk}\dfrac{\partial x_k}{\partial z_2} && \dots && \displaystyle\sum_{k=1}^n a_{mk}\dfrac{\partial x_k}{\partial z_n} \end{bmatrix} $$

        이다. 그런데 $m \times n$ 행렬 $\mathbf{A} = \begin{bmatrix} a _{11} & a _{12} & \dots & a _{1n} \\ a _{21} & a _{12} & \dots & a _{1n} \\ \vdots & \vdots & \ddots & \vdots \\ a _{m1} & a _{m2} & \dots & a _{mn} \\ \end{bmatrix}$ 와
        
        다변수벡터함수 $\mathbf{x}$ 에 대한 벡터 $\mathbf{z}$ 의 미분, 즉 $n \times n$ 야코비 행렬 $\dfrac{\partial \mathbf{x}}{\partial \mathbf{z}} = \begin{bmatrix} \dfrac{\partial x_1}{\partial z_1} & \dfrac{\partial x_1}{\partial z_2} & \dots & \dfrac{\partial x_1}{\partial z_n}  \\ \dfrac{\partial x_2}{\partial z_1} & \dfrac{\partial x_2}{\partial z_2} & \dots & \dfrac{\partial x_2}{\partial z_n}  \\ \vdots & \vdots & \ddots & \vdots \\ \dfrac{\partial x_n}{\partial z_1} & \dfrac{\partial x_n}{\partial z_2} & \dots & \dfrac{\partial x_n}{\partial z_n}  \\ \end{bmatrix}$ 의 행렬곱 $\mathbf{A}\dfrac{\partial \mathbf{x}}{\partial \mathbf{z}}$ 은

        $$ \mathbf{A}\dfrac{\partial \mathbf{x}}{\partial \mathbf{z}} = \begin{bmatrix} \displaystyle\sum_{k=1}^n a_{1k}\dfrac{\partial x_k}{\partial z_1} && \displaystyle\sum_{k=1}^n a_{1k}\dfrac{\partial x_k}{\partial z_2} && \dots && \displaystyle\sum_{k=1}^n a_{1k}\dfrac{\partial x_k}{\partial z_n} \\ \displaystyle\sum_{k=1}^n a_{2k}\dfrac{\partial x_k}{\partial z_1} && \displaystyle\sum_{k=1}^n a_{2k}\dfrac{\partial x_k}{\partial z_2} && \dots && \displaystyle\sum_{k=1}^n a_{2k}\dfrac{\partial x_k}{\partial z_n} \\ \vdots && \vdots && \ddots && \vdots \\ \displaystyle\sum_{k=1}^n a_{mk}\dfrac{\partial x_k}{\partial z_1} && \displaystyle\sum_{k=1}^n a_{mk}\dfrac{\partial x_k}{\partial z_2} && \dots && \displaystyle\sum_{k=1}^n a_{mk}\dfrac{\partial x_k}{\partial z_n} \end{bmatrix} $$

        이다. 그러므로

        $$ \therefore  \dfrac{\partial \mathbf{y}}{\partial \mathbf{z}} = \mathbf{A}\dfrac{\partial \mathbf{x}}{\partial \mathbf{z}} $$

        이다. ■ 

    - 이는 $\dfrac{\partial \mathbf{y}}{\partial \mathbf{z}}= \dfrac{\partial \mathbf{y}}{\partial \mathbf{x}}\dfrac{\partial \mathbf{x}}{\partial \mathbf{z}}= \mathbf{A}\dfrac{\partial \mathbf{x}}{\partial \mathbf{z}}$  의 결과로도 얻을 수 있다. 그러므로 행렬미분에서도 합성함수의 편미분, 즉 연쇄법칙이 동일하게 적용된다는 추론을 내릴 수 있다. 그러나 이것에는 증명이 필요하다.

- 정리 7 (이독립변수를 갖는 행렬방정식의 미분)

    $m \times 1$ 행렬 $\mathbf{y}$, $n \times 1$ 행렬 $\mathbf{x}$, $m \times n$ 행렬 $\mathbf{A}$ 가 존재하고, $\mathbf{A}$ 가 $\mathbf{x}, \mathbf{y}$ 와 독립적일 때 스칼라
    
    $$\alpha = \mathbf{y}^{\intercal }\mathbf{Ax}$$

    를 정의할 수 있다. 그러면 $\alpha$ 에 대한 $\mathbf{x}$ 의 미분은 

    $$ \dfrac{\partial \alpha }{\partial \mathbf{x}} = \mathbf{y}^{\intercal }\mathbf{A} $$

    이고, $\alpha$ 에 대한 $\mathbf{y}$ 의 미분은 

    $$ \dfrac{\partial \alpha }{\partial \mathbf{y}} = \mathbf{x}^{\intercal }\mathbf{A} $$

    이다.

    - 증명 

        $1 \times n$ 행렬 $\mathbf{w}^{\intercal }=\mathbf{y}^{\intercal }\mathbf{A}$ 을 정의하자. 그러면 $\alpha = \mathbf{w}^{\intercal }\mathbf{x}$ 이다. 
        
        그렇다면 정리 5 "벡터 $\mathbf{y} \in \mathbb{R} ^{m}$($m \times 1$ 행렬), $\mathbf{x} \in \mathbb{R} ^{n}$($n \times 1$ 행렬) 
        와 $m \times n$ 행렬 $\mathbf{A}$ 에 대한 행렬방정식 $\mathbf{y} = \mathbf{Ax}$ 의 미분은 $\dfrac{\partial \mathbf{y}}{\partial \mathbf{x}}=\mathbf{A}$ 이다." 에서 $m = 1$ 로 두면

        "스칼라 $y \in \mathbb{R}$($1 \times 1$ 행렬), $\mathbf{x} \in \mathbb{R} ^{n}$($n \times 1$ 행렬) 와 $1 \times n$ 행렬 $\mathbf{A}$ 에 대한 행렬방정식 $y = \mathbf{Ax}$ 의 미분은 $\dfrac{\partial y}{\partial \mathbf{x}}=\mathbf{A}$ 이다." 이므로 

        $$ \dfrac{\partial \alpha }{\partial \mathbf{x}} = \mathbf{w}^{\intercal } = \mathbf{y}^{\intercal }\mathbf{A} $$

        이다. ■ 

        한편 $\alpha$ 는 스칼라이므로 $\alpha = \alpha ^{\intercal }$ 이다. 그러므로 

        $$ \alpha = \alpha ^{\intercal } = \mathbf{x}^{\intercal }\mathbf{A}^{\intercal }\mathbf{y} $$

        이다. 그렇다면 마찬가지로 정리 5 에 의하여

        $$ \dfrac{\partial \alpha }{\partial \mathbf{y}} = \mathbf{x}^{\intercal }\mathbf{A}^{\intercal } $$

        이다. ■ 

- 정리 8 (일독립변수와 그것의 전치로 구성된 행렬방정식의 미분)

    $n \times 1$ 행렬 $\mathbf{x}$, $n \times n$ 행렬 $\mathbf{A}$ 에 대하여 $\mathbf{A}$ 가 $\mathbf{x}$ 에 독립적일 때 스칼라

    $$ \alpha = \mathbf{x}^{\intercal }\mathbf{Ax} $$

    가 존재한다. 이때 $\alpha$ 에 대한 $\mathbf{x}$ 의 미분은 

    $$ \dfrac{\partial \alpha }{\partial \mathbf{x}} = \mathbf{x}^{\intercal }(\mathbf{A}+\mathbf{A}^{\intercal }) $$

    이다.

    - 증명

        먼저 $\mathbf{Ax} = \begin{pmatrix} a _{11} & a _{12} & \dots & a _{1n} \\ a _{21} & a _{22} & \dots & a _{2n} \\ \vdots & \vdots  & \ddots & \vdots \\ a _{n1} & a _{n2} & \dots & a _{nn} \\ \end{pmatrix} \begin{pmatrix} x _{1}\\ x _{2}\\ \vdots \\ x _{n}\\ \end{pmatrix}= \begin{pmatrix} \displaystyle \sum_{i=1}^{n} a _{1i} x_i\\ \displaystyle\sum_{i=1}^{n} a _{2i} x_i\\ \vdots \\ \displaystyle\sum_{i=1}^{n} a _{ni} x_i\\ \end{pmatrix}$ 이다. 그러므로 

        $$ \alpha = \mathbf{x}^{\intercal }\mathbf{Ax} = \begin{pmatrix} x_1 & x_2 & \dots & x_n \\ \end{pmatrix} \begin{pmatrix} \displaystyle \sum_{i=1}^{n} a _{1i} x_i\\ \displaystyle\sum_{i=1}^{n} a _{2i} x_i\\ \vdots \\ \displaystyle\sum_{i=1}^{n} a _{ni} x_i\\ \end{pmatrix} = x_1 \sum_{i=1}^{n}a _{1i}x _i + x_2 \sum_{i=1}^{n}a _{2i}x _i +\dots + x_n \sum_{i=1}^{n}a _{ni}x _i $$

        $$ = \sum_{j=1}^{n} x_j \sum_{i=1}^{n}a _{ji}x_i = \sum_{j=1}^{n} \sum_{i=1}^{n}a _{ij}x_i x_j $$

        이다. 이 $\alpha$ 에서 $k \in \{1,2,\dots,n\}$ 에 대하여 $x_k$ 에 종속된 수식만 생각하면 $j=k, i \neq k$ 일때

        $$ \sum_{i \in \{1,\dots,(k-1),(k+1),\dots,n\}}a _{ik}x_i x_k $$

        이고, $i=k , j \neq k$ 일때

        $$ \sum_{j \in \{1,\dots,(k-1),(k+1),\dots,n\}}a _{kj}x_k x_j $$

        이고, $i=j=k$ 일때

        $$ a _{kk}x_k ^{2} $$

        이다. 그렇다면 $\alpha$ 를 $x_k$ 에 대하여 미분하면

        $$ \dfrac{\partial \alpha }{\partial x_k} = \sum_{i \in \{1,\dots,(k-1),(k+1),\dots,n\}}a _{ik}x_i + \sum_{j \in \{1,\dots,(k-1),(k+1),\dots,n\}}a _{kj}x_j + 2a _{kk}x_k = $$ 

        $$=  \sum_{i=1}^{n} a _{ik}x_i + \sum_{j=1}^{n}a _{kj}x_j $$

        이다. 그런데 $1 \times 1$ 행렬 $\alpha$ 에 대한 $n \times 1$ 행렬 $\mathbf{x}$ 의 미분은 다변수벡터함수의 미분, 즉 야코비행렬

        $$ \dfrac{\partial \alpha }{\partial \mathbf{x}} = \begin{pmatrix} \dfrac{\partial \alpha }{\partial x_1}& \dfrac{\partial \alpha }{\partial x_2}& \dots & \dfrac{\partial \alpha }{\partial x_n} \end{pmatrix} = $$ 
        
        $$ = \begin{pmatrix} \displaystyle \sum_{i=1}^{n} a _{i1}x_i + \sum_{j=1}^{n}a _{1j}x_j & \displaystyle \sum_{i=1}^{n} a _{i2}x_i + \sum_{j=1}^{n}a _{2j}x_j & \dots& \displaystyle \sum_{i=1}^{n} a _{in}x_i + \sum_{j=1}^{n}a _{nj}x_j \\ \end{pmatrix} $$

        이다.

        한편 $n \times 1$ 행렬 $\mathbf{Ax} = \begin{pmatrix} \displaystyle \sum_{i=1}^{n} a _{1i} x_i\\ \displaystyle\sum_{i=1}^{n} a _{2i} x_i\\ \vdots \\ \displaystyle\sum_{i=1}^{n} a _{ni} x_i\\ \end{pmatrix}$ 에 대한 전치는 $1 \times n$ 행렬

        $$\mathbf{x ^{\intercal }A ^{\intercal }} = \begin{pmatrix} \displaystyle \sum_{i=1}^{n} a _{1i} x_i& \displaystyle\sum_{i=1}^{n} a _{2i} x_i& \dots & \displaystyle\sum_{i=1}^{n} a _{ni} x_i \end{pmatrix}$$

        이고,

        $$\mathbf{x ^{\intercal }A } = \begin{pmatrix} \displaystyle \sum_{i=1}^{n} a _{i1} x_i& \displaystyle\sum_{i=1}^{n} a _{i2} x_i& \dots & \displaystyle\sum_{i=1}^{n} a _{in} x_i \end{pmatrix}$$

        이다. 따라서 $\sum$ 의 매개변수 $j$ 는 $i$ 로 표기해도 관계없으므로 편의상 $j$ 를 $i$ 로 바꾸면 

        $$ \begin{pmatrix} \displaystyle \sum_{i=1}^{n} a _{i1}x_i + \sum_{j=1}^{n}a _{1j}x_j & \displaystyle \sum_{i=1}^{n} a _{i2}x_i + \sum_{j=1}^{n}a _{2j}x_j & \dots& \displaystyle \sum_{i=1}^{n} a _{in}x_i + \sum_{j=1}^{n}a _{nj}x_j \\ \end{pmatrix} $$

        $$ = \begin{pmatrix} \displaystyle \sum_{i=1}^{n} a _{1i} x_i& \displaystyle\sum_{i=1}^{n} a _{2i} x_i& \dots & \displaystyle\sum_{i=1}^{n} a _{ni} x_i \end{pmatrix} + \begin{pmatrix} \displaystyle \sum_{i=1}^{n} a _{i1} x_i& \displaystyle\sum_{i=1}^{n} a _{i2} x_i& \dots & \displaystyle\sum_{i=1}^{n} a _{in} x_i \end{pmatrix} $$

        $$ = \mathbf{x ^{\intercal }A ^{\intercal }} + \mathbf{x ^{\intercal }A} = \mathbf{x ^{\intercal }(A ^{\intercal }+ A)} $$

        이다. 그러므로 최종적으로

        $$ \therefore \dfrac{\partial \alpha }{\partial \mathbf{x}} = \mathbf{x ^{\intercal }A ^{\intercal }} + \mathbf{x ^{\intercal }A} = \mathbf{x ^{\intercal }(A ^{\intercal }+ A)} $$

        이다. ■   

- 정리 9 (일독립변수와 그것의 전치로 구성된 대칭행렬의 행렬방정식의 미분)

    $n \times 1$ 행렬 $\mathbf{x}$, $n \times n$ 대칭 행렬 $\mathbf{A}$ 에 대하여 $\mathbf{A}$ 가 $\mathbf{x}$ 에 독립적일 때 스칼라

    $$ \alpha = \mathbf{x}^{\intercal }\mathbf{Ax} $$

    가 존재한다. 이때 $\alpha$ 에 대한 $\mathbf{x}$ 의 미분은 

    $$ \dfrac{\partial \alpha }{\partial \mathbf{x}} = 2\mathbf{x}^{\intercal }(\mathbf{A}) $$

    이다.

    - 증명 

        정리 8 과 동일하다. 

    - 대칭행렬(symmetric matrix) 는 $\mathbf{A} = \mathbf{A ^{\intercal }}$ 인 행렬이다.

- 정리 10 (일독립변수와 이매개변수를 갖는 행렬의 미분)

    $n \times 1$ 행렬 $\mathbf{y}$, $n \times 1$ 행렬 $\mathbf{x}$ 이 벡터 $\mathbf{z}$ 의 함수일 때 스칼라 

    $$ \alpha = \mathbf{y}^{\intercal }\mathbf{x} $$

    가 존재한다. 이때 $\alpha$ 에 대한 $\mathbf{z}$ 에 대한 미분은 

    $$ \dfrac{\partial \alpha  }{\partial \mathbf{z}} = \mathbf{x}^{\intercal }\dfrac{\partial \mathbf{y}}{\partial \mathbf{z}}+\mathbf{y}^{\intercal }\dfrac{\partial \mathbf{x}}{\partial \mathbf{z}} $$

    이다.

    - 증명 

        $\displaystyle \alpha = \sum_{j=1}^{n}x_jy_j$ 이다. 이는 일독립변수와 $n$매개변수를 갖는 다변수 합성함수의 미분을 구하는 것과 같다. 그러므로 각각의 매개변수로 $\alpha$ 를 미분한 것에 매개변수에 대한 독립변수의 미분을 곱하면 된다.
        따라서 $\mathbf{z}$ 의 $k$ 번째 원소에 대한 미분은 

        $$ \dfrac{\partial \alpha }{\partial z_k} = \sum_{j=1}^{n} \bigg (\dfrac{\partial \alpha }{\partial x_j}\dfrac{\partial x_j}{\partial z_k}+\dfrac{\partial \alpha  }{\partial y_j}\dfrac{\partial y_j}{\partial z_k}\bigg ) = \sum_{j=1}^{n}\bigg (x_j \dfrac{\partial y_j}{\partial z_k}+y_j \dfrac{\partial x_j}{\partial z_k}\bigg ) $$

        이다. 그런데 $1 \times 1$ 행렬 $\alpha$ 에 대한 벡터 $\mathbf{z}$ 의 미분은 매개변수 $\mathbf{x, y}$ 를 갖는 다변수벡터함수에 대한 미분, 즉 야코비행렬

        $$ \dfrac{\partial \alpha }{\partial \mathbf{z}} = \begin{bmatrix} \dfrac{\partial \alpha  }{\partial z_1} & \dfrac{\partial \alpha  }{\partial z_2} & \dots& \dfrac{\partial \alpha  }{\partial z_n} \\ \end{bmatrix} $$

        $$ = \begin{bmatrix} \displaystyle \sum_{j=1}^{n}\bigg (x_j \dfrac{\partial y_j}{\partial z_1}+y_j \dfrac{\partial x_j}{\partial z_k}\bigg ) & \displaystyle \sum_{j=1}^{n}\bigg (x_j \dfrac{\partial y_j}{\partial z_2}+y_j \dfrac{\partial x_j}{\partial z_k}\bigg ) & \dots& \displaystyle \sum_{j=1}^{n}\bigg (x_j \dfrac{\partial y_j}{\partial z_n}+y_j \dfrac{\partial x_j}{\partial z_k}\bigg )  \\ \end{bmatrix} $$ 

        이다. ▲ 

        그런데 $\mathbf{x} ^{\intercal }$ 와 $\dfrac{\partial \mathbf{y}}{\partial \mathbf{z}}$ 의 행렬곱 $\mathbf{x}^{\intercal }\dfrac{\partial \mathbf{y}}{\partial \mathbf{z}}$ 은 

        $$ \mathbf{x}^{\intercal }\dfrac{\partial \mathbf{y}}{\partial \mathbf{z}} = \begin{bmatrix} x_1 & x_2 & \dots & x_n \\ \end{bmatrix} \begin{bmatrix} \dfrac{\partial y_1}{\partial z_1}& \dfrac{\partial y_1}{\partial z_2}& \dots & \dfrac{\partial y_1}{\partial z_n} \\ \dfrac{\partial y_2}{\partial z_1}& \dfrac{\partial y_2}{\partial z_2}& \dots & \dfrac{\partial y_2}{\partial z_n} \\ \vdots & \vdots & \ddots & \vdots \\ \dfrac{\partial y_n}{\partial z_1}& \dfrac{\partial y_n}{\partial z_2}& \dots & \dfrac{\partial y_n}{\partial z_n} \\ \end{bmatrix} $$

        $$ = \begin{bmatrix} \displaystyle \sum_{j=1}^{n} x_j \dfrac{\partial y_j}{\partial z_1} & \displaystyle \sum_{j=1}^{n} x_j \dfrac{\partial y_j}{\partial z_2} & \dots& \displaystyle \sum_{j=1}^{n} x_j \dfrac{\partial y_j}{\partial z_n} \\ \end{bmatrix} $$

        이고, $\mathbf{y} ^{\intercal }$ 와 $\dfrac{\partial \mathbf{x}}{\partial \mathbf{z}}$ 의 행렬곱 $\mathbf{y}^{\intercal }\dfrac{\partial \mathbf{x}}{\partial \mathbf{z}}$ 은 
        
        $$ \mathbf{y}^{\intercal }\dfrac{\partial \mathbf{x}}{\partial \mathbf{z}} = \begin{bmatrix} y_1 & y_2 & \dots & y_n \\ \end{bmatrix} \begin{bmatrix} \dfrac{\partial x_1}{\partial z_1}& \dfrac{\partial x_1}{\partial z_2}& \dots & \dfrac{\partial x_1}{\partial z_n} \\ \dfrac{\partial x_2}{\partial z_1}& \dfrac{\partial x_2}{\partial z_2}& \dots & \dfrac{\partial x_2}{\partial z_n} \\ \vdots & \vdots & \ddots & \vdots \\ \dfrac{\partial x_n}{\partial z_1}& \dfrac{\partial x_n}{\partial z_2}& \dots & \dfrac{\partial x_n}{\partial z_n} \\ \end{bmatrix} $$

        $$ = \begin{bmatrix} \displaystyle \sum_{j=1}^{n} y_ j \dfrac{\partial x_j}{\partial z_1} & \displaystyle \sum_{j=1}^{n} y_ j \dfrac{\partial x_j}{\partial z_2} & \dots& \displaystyle \sum_{j=1}^{n} y_ j \dfrac{\partial x_j}{\partial z_n} \\ \end{bmatrix} $$

        이다. 그러므로 최종적으로

        $$ \therefore  \dfrac{\partial \alpha  }{\partial \mathbf{z}} = \mathbf{x}^{\intercal }\dfrac{\partial \mathbf{y}}{\partial \mathbf{z}}+\mathbf{y}^{\intercal }\dfrac{\partial \mathbf{x}}{\partial \mathbf{z}} $$

        이다. ■ 
  
- 정리 11 (일독립변수와 이매개변수, 즉 매개변수와 그것의 전치인 매개변수를 갖는 행렬의 미분)

    $n \times 1$ 행렬 $\mathbf{x}$ 가 벡터 $\mathbf{z}$ 에 대한 함수일 때 스칼라 

    $$ \alpha = \mathbf{x}^{\intercal }\mathbf{x} $$
    
    가 존재한다. 이때 $\alpha$ 에 대한 $\mathbf{z}$ 의 미분은 

    $$ \dfrac{\partial \alpha }{\partial \mathbf{z}} = 2 \mathbf{x}^{\intercal }\dfrac{\partial \mathbf{x}}{\partial \mathbf{z}} $$

    이다.

    - 증명 

        정리 10 의 증명과 동일하다. ■ 

- 정리 12 (이독립변수를 갖는 행렬의 미분)

    $m \times 1$ 행렬 $\mathbf{y}$, $n \times 1$ 행렬 $\mathbf{x}$, $m \times n$ 행렬 $\mathbf{A}$ 에 대하여 $\mathbf{y,x}$ 가 벡터 $\mathbf{z}$ 의 함수이고 $\mathbf{A}$ 가 $\mathbf{z}$ 에 독립적일 때, 스칼라 

    $$ \alpha = \mathbf{y}^{\intercal }\mathbf{Ax} $$

    가 존재한다. $\alpha$ 에 대한 $\mathbf{z}$ 의 미분은 

    $$ \dfrac{\partial \alpha }{\partial \mathbf{z}} = \mathbf{x}^{\intercal }\mathbf{A}^{\intercal }\dfrac{\partial \mathbf{y}}{\partial \mathbf{z}}+\mathbf{y}^{\intercal }\mathbf{A}\dfrac{\partial \mathbf{x}}{\partial \mathbf{z}} $$

    이다. 

    - 증명 

        $\mathbf{w}^{\intercal } = \mathbf{y}^{\intercal }\mathbf{A}$ 로 두자. 그러면 $\alpha  = \mathbf{w}^{\intercal }\mathbf{x}$ 이다. 그렇다면 정리 10 "일독립변수와 이매개변수를 갖는 행렬의 미분" 에 의하여

        $$ \dfrac{\partial \alpha }{\partial \mathbf{z}} = \mathbf{x}^{\intercal }\dfrac{\partial \mathbf{w}}{\partial \mathbf{z}} + \mathbf{w}^{\intercal }\dfrac{\partial \mathbf{x}}{\partial \mathbf{z}} $$

        이다. 이때 $\mathbf{w}^{\intercal }$ 을 원래대로 치환하면

        $$ \therefore  \dfrac{\partial \alpha }{\partial \mathbf{z}} = \dfrac{\partial \alpha }{\partial \mathbf{y}}\dfrac{\partial \mathbf{y}}{\partial \mathbf{z}}+\dfrac{\partial \alpha }{\partial \mathbf{x}}\dfrac{\partial \mathbf{x}}{\partial \mathbf{z}} = \mathbf{x}^{\intercal }\mathbf{A}^{\intercal }\dfrac{\partial \mathbf{y}}{\partial \mathbf{z}}+\mathbf{y}^{\intercal }\mathbf{A}\dfrac{\partial \mathbf{x}}{\partial \mathbf{z}} $$

        을 얻는다. ■ 

- 정리 13 (이독립변수, 즉 독립변수와 그것의 전치인 독립변수를 갖는 행렬의 미분)

    $n \times 1$ 행렬 $\mathbf{x}$, $m \times n$ 행렬 $\mathbf{A}$ 에 대하여 $\mathbf{x}$ 가 벡터 $\mathbf{z}$ 의 함수이고 $\mathbf{A}$ 가 $\mathbf{z}$ 에 독립적일 때, 스칼라 

    $$ \alpha = \mathbf{x}^{\intercal }\mathbf{Ax} $$

    가 존재한다. $\alpha$ 에 대한 $\mathbf{z}$ 의 미분은 

    $$ \dfrac{\partial \alpha }{\partial \mathbf{z}} = \mathbf{x}^{\intercal }(\mathbf{A}  +\mathbf{A}^{\intercal })\dfrac{\partial \mathbf{x}}{\partial \mathbf{z}} $$

    이다. 

    - 증명 

        정리 12 의 증명과 동일하다.

- 정리 14 (이독립변수, 즉 독립변수와 그것의 전치인 독립변수를 갖는 행렬의 미분)

    $n \times 1$ 행렬 $\mathbf{x}$, $m \times n$ 대칭 행렬 $\mathbf{A}$ 에 대하여 $\mathbf{x}$ 가 벡터 $\mathbf{z}$ 의 함수이고 $\mathbf{A}$ 가 $\mathbf{z}$ 에 독립적일 때, 스칼라 

    $$ \alpha = \mathbf{x}^{\intercal }\mathbf{Ax} $$

    가 존재한다. $\alpha$ 에 대한 $\mathbf{z}$ 의 미분은 

    $$ \dfrac{\partial \alpha }{\partial \mathbf{z}} = 2\mathbf{x}^{\intercal }\mathbf{A}\dfrac{\partial \mathbf{x}}{\partial \mathbf{z}} $$

    이다. 

    - 증명 

        정리 13 의 증명과 동일하다.

- 정리 15 (행렬곱 미분)

    스칼라 $\alpha$ 의 함수를 원소로 갖는 $n \times n$ 행렬 $\mathbf{A, B}$ 에 대하여 행렬곱 $\mathbf{AB}$ 에 대한 스칼라 $\alpha$ 의 미분은 

    $$ \dfrac{\partial \mathbf{AB}}{\partial \alpha } = \dfrac{\partial \mathbf{A}}{\partial \alpha }\mathbf{B} + \mathbf{A}\dfrac{\partial \mathbf{B}}{\partial \alpha } $$

    이다. 

    - 증명

        먼저 $m \times n$ 함수 행렬 $\mathbf{F}$ 의 모든 원소가 스칼라 $\alpha$ 를 입력받는 함수들로 구성되어 있으면, $\mathbf{F}$ 에 대한 $\alpha$ 의 미분은 $m \times n$ 야코비 행렬 

        $$ \dfrac{\partial \mathbf{F}}{\partial \alpha }= \begin{pmatrix} \dfrac{\partial f_{11}}{\partial \alpha}& \dfrac{\partial f_{12}}{\partial \alpha}& \dots& \dfrac{\partial f_{1n}}{\partial \alpha} \\ \dfrac{\partial f_{21}}{\partial \alpha}& \dfrac{\partial f_{22}}{\partial \alpha}& \dots& \dfrac{\partial f_{2n}}{\partial \alpha} \\ \vdots & \vdots & \ddots & \vdots \\ \dfrac{\partial f_{m1}}{\partial \alpha}& \dfrac{\partial f_{m2}}{\partial \alpha}& \dots& \dfrac{\partial f  _{mn}}{\partial \alpha} \\ \end{pmatrix} $$

        인 것을 기억하자.

        그렇다면 행렬곱 $\mathbf{AB}$ 는

        $$ \mathbf{AB} = \begin{pmatrix} \displaystyle \sum_{k=1}^{n}a _{1k}b _{k1} & \displaystyle \sum_{k=1}^{n}a _{1k}b _{k2} & \dots& \displaystyle \sum_{k=1}^{n}a _{1k}b _{kn} \\ \displaystyle \sum_{k=1}^{n}a _{2k}b _{k1} & \displaystyle \sum_{k=1}^{n}a _{2k}b _{k2} & \dots& \displaystyle \sum_{k=1}^{n}a _{2k}b _{kn} \\ \vdots & \vdots & \ddots & \vdots \\ \displaystyle \sum_{k=1}^{n}a _{nk}b _{k1} & \displaystyle \sum_{k=1}^{n}a _{nk}b _{k2} & \dots& \displaystyle \sum_{k=1}^{n}a _{nk}b _{kn} \\ \end{pmatrix} $$

        이므로 $(i, j)$ 원소에 대한 스칼라 $\alpha$ 의 미분은 

        $$ \dfrac{\partial }{\partial \alpha }\sum_{k=1}^{n}a _{ik}b _{kj} = \sum_{k=1}^{n}\bigg (\dfrac{\partial a _{ik}}{\partial \alpha }b _{kj} + a _{ik}\dfrac{\partial  b_{kj}}{\partial \alpha }\bigg ) $$

        이다. 그러므로 행렬곱 $\mathbf{AB}$ 에 대한 스칼라 $\alpha$ 의 미분은 야코비 행렬

        $$ \dfrac{\partial }{\partial \alpha }\mathbf{AB} = \begin{pmatrix} \displaystyle \dfrac{\partial }{\partial \alpha}\sum_{k=1}^{n}a _{1k}b _{k1} & \displaystyle \dfrac{\partial }{\partial \alpha}\sum_{k=1}^{n}a _{1k}b _{k2} & \dots& \displaystyle \dfrac{\partial }{\partial \alpha}\sum_{k=1}^{n}a _{1k}b _{kn} \\ \displaystyle \dfrac{\partial }{\partial \alpha}\sum_{k=1}^{n}a _{2k}b _{k1} & \displaystyle \dfrac{\partial }{\partial \alpha}\sum_{k=1}^{n}a _{2k}b _{k2} & \dots& \displaystyle \dfrac{\partial }{\partial \alpha}\sum_{k=1}^{n}a _{2k}b _{kn} \\ \vdots & \vdots & \ddots & \vdots \\ \displaystyle \dfrac{\partial }{\partial \alpha}\sum_{k=1}^{n}a _{nk}b _{k1} & \displaystyle \dfrac{\partial }{\partial \alpha}\sum_{k=1}^{n}a _{nk}b _{k2} & \dots& \displaystyle \dfrac{\partial }{\partial \alpha}\sum_{k=1}^{n}a _{nk}b _{kn} \\ \end{pmatrix} $$

        $$ = \begin{pmatrix} \displaystyle \sum_{k=1}^{n}\bigg(\dfrac{\partial a _{1k}}{\partial \alpha}b _{k1} + a_{1k} \dfrac{\partial b_{k1}}{\partial \alpha}\bigg) & \displaystyle \sum_{k=1}^{n}\bigg(\dfrac{\partial a _{1k}}{\partial \alpha}b _{k2} + a_{1k} \dfrac{\partial b_{k2}}{\partial \alpha}\bigg) & \dots& \displaystyle \sum_{k=1}^{n}\bigg(\dfrac{\partial a _{1k}}{\partial \alpha}b _{kn} + a_{1k} \dfrac{\partial b_{kn}}{\partial \alpha}\bigg) \\ \displaystyle \sum_{k=1}^{n}\bigg(\dfrac{\partial a _{2k}}{\partial \alpha}b _{k1} + a_{2k} \dfrac{\partial b_{k1}}{\partial \alpha}\bigg) & \displaystyle \sum_{k=1}^{n}\bigg(\dfrac{\partial a _{2k}}{\partial \alpha}b _{k2} + a_{2k} \dfrac{\partial b_{k2}}{\partial \alpha}\bigg) & \dots& \displaystyle \sum_{k=1}^{n}\bigg(\dfrac{\partial a _{2k}}{\partial \alpha}b _{kn} + a_{2k} \dfrac{\partial b_{kn}}{\partial \alpha}\bigg) \\ \vdots & \vdots & \ddots & \vdots \\ \displaystyle \sum_{k=1}^{n}\bigg(\dfrac{\partial a _{nk}}{\partial \alpha}b _{k1} + a_{nk} \dfrac{\partial b_{k1}}{\partial \alpha}\bigg) & \displaystyle \sum_{k=1}^{n}\bigg(\dfrac{\partial a _{nk}}{\partial \alpha}b _{k2} + a_{nk} \dfrac{\partial b_{k2}}{\partial \alpha}\bigg) & \dots& \displaystyle \sum_{k=1}^{n}\bigg(\dfrac{\partial a _{nk}}{\partial \alpha}b _{kn} + a_{nk} \dfrac{\partial b_{kn}}{\partial \alpha}\bigg) \\ \end{pmatrix} $$

        이다. 그런데 이것은 

        $$ \dots $$

        이므로 최종적으로

        $$ \therefore \dfrac{\partial \mathbf{AB}}{\partial \alpha } = \dfrac{\partial \mathbf{A}}{\partial \alpha }\mathbf{B} + \mathbf{A}\dfrac{\partial \mathbf{B}}{\partial \alpha } $$

        이다. ■ 

- 정리 16

    그렇다면 $m \times m$ 가역행렬 $\mathbf{A}$ 의 모든 원소가 스칼라 $\alpha$ 를 입력받는 함수들로 구성되어 있다고 하자. 이때 $\mathbf{A}^{-1}$ 에 대한 $\alpha$ 의 미분은 

    $$ \dfrac{\partial \mathbf{A}^{-1}}{\partial \alpha } = - \mathbf{A}^{-1}\dfrac{\partial \mathbf{A}}{\partial \alpha }\mathbf{A}^{-1} $$

    이다.

    - 증명 

        $\mathbf{A}^{-1}\mathbf{A}=  \mathbf{I}$ 이므로 이것을 $\alpha$ 에 대하여 미분하면 정리 15 에 의하여 

        $$ \mathbf{A}^{-1}\dfrac{\partial \mathbf{A}}{\partial \alpha } + \dfrac{\partial \mathbf{A}^{-1}}{\partial \alpha }\mathbf{A} = \mathbf{0} $$

        이다. 그런데 이것은 곧 

        $$  \iff \dfrac{\partial \mathbf{A}^{-1}}{\partial \alpha }\mathbf{A} = - \mathbf{A}^{-1}\dfrac{\partial \mathbf{A}}{\partial \alpha } $$

        $$  \iff \dfrac{\partial \mathbf{A}^{-1}}{\partial \alpha } = - \mathbf{A}^{-1}\dfrac{\partial \mathbf{A}}{\partial \alpha }\mathbf{A}^{-1} $$

        이다. ■ 

- 연쇄법칙(chain rule)에 관하여 

    https://en.wikipedia.org/wiki/Chain_rule#Multivariable_case

    https://en.wikipedia.org/wiki/Total_derivative#The_total_derivative_as_a_linear_map

    - 일변수 실함수의 연쇄법칙 $\mathbb{R} \to \mathbb{R}$

        - 가장 단순한 형태

        일변수 실함수 $u = g(x)$ 가 점 $c$ 에서 미분가능하고(미분계수 $g'(c)$ 가 존재하고) 함수 $y = f(u)$  가 $g(c)$ 에서 미분가능하면 합성함수 $f \circ g$ 도 $c$ 에서 미분가능하고 그 미분은

        $$ (f \circ g)'(c) = f'(g(c))\cdot g'(c) $$

        이며 이것을 일반적으로 

        $$ (f \circ g)' = (f' \circ g) \cdot g' $$

        라고 쓴다.
        
        이것은 라이프니츠의 표기법으로 $f$ 를 독립변수 $u = g(x)$ 를 갖는 함수로 표현하여

        $$ \dfrac{dy}{dx}=\dfrac{dy}{du}\cdot \dfrac{du}{dx} $$

        로 쓸 수 있다.
        
        - 일반적인 형태 

        $n$ 개의 함수들 $f_1, \dots, f_n$ 의 합성함수 $f_1 \circ (f_2 \circ \dots (f _{n-1} \circ f_n ))$ 가 각각의 매개함수 $f_i$ 의 매개입력에서 미분가능할 때 그 미분은 

        $$ \dfrac{df_1}{dx}=\dfrac{df_1}{df_2}\dfrac{df_2}{df_3}\dots\dfrac{df_n}{dx} $$

        이다.

    - 다변수 함수의 연쇄법칙 $\mathbb{R} ^{n} \to \mathbb{R}$

        함수 $y = f(g_1(x), \dots, g_k(x))$ 의 연쇄법칙에는 $f$ 에 대한 $k$ 번째 인자에 대한 편미분이 필요한데, $f$ 를 $k$ 번째 인자에 대하여 미분한 것을

        $$ D_i f $$

        라고 한다. 이때 함수 $f$ 에 대한 $x$ 의 미분은 

        $$ \dfrac{d}{dx}f(g_1(x),\dots,g_k(x)) = \sum_{i=1}^{k}\bigg (\dfrac{d}{dx}g_i(x)\bigg )D_i f(g_1(x),\dots,g_k(x)) = \sum_{i=1}^{k} \dfrac{\partial f}{\partial g_i}\dfrac{\partial g_i}{\partial x} $$

        이다.
    
    - 다변수 벡터함수의 연쇄법칙 $\mathbb{R} ^{n} \to \mathbb{R} ^{m}$

        함수 $f: \mathbb{R} ^{m}\to \mathbb{R} ^{k}$ 와 $g: \mathbb{R} ^{n}\to \mathbb{R} ^{m}$ 이 $\mathbf{a} \in \mathbb{R} ^{n}$ 에서 미분가능할 때 $D _{\mathbf{a}} g$ 를 $\mathbf{a}$ 에서의 $g$ 의 전미분이라고 하고, $D _{g(\mathbf{a})} = f$ 를 점 $g(\mathbf{a})$ 에서의 $f$ 의 전미분이라고 하자. 그러면 이들은 각각 선형변환 $\mathbb{R} ^{n}\to \mathbb{R} ^{m}, \mathbb{R} ^{m}\to \mathbb{R} ^{k}$ 이므로 합성할 수 있다. 그러므로

        $$ D _{\mathbf{a}}(f \circ g) = D _{g(\mathbf{a})}\circ D _{\mathbf{a}}g $$

        이다. 이것을 간결하게

        $$ D(f \circ g) = Df \circ Dg $$
        
        로 쓸 수 있다.

        전미분은 선형변환이기에 그 결과를 행렬로 쓸 수 있는데 그 행렬을 야코비안 행렬이라 한다. 그러므로 다변수 벡터함수의 연쇄법칙을 야코비안행렬로 

        $$ J _{f \circ g}(\mathbf{a}) = J_f(g(\mathbf{a}))J_g(\mathbf{a}) $$

        나타낼 수 있고 더욱 간결하게 

        $$ J _{f \circ g} = (J_f \circ g)J_g $$

        로 쓸 수 있다.

- 정리 17 

    $n \times m$ 행렬 $\mathbf{X}$, $m \times d$ 행렬 $\mathbf{Y}$ 의 행렬곱 $\mathbf{XY}$ 은 $n \times d$ 행렬 $\mathbf{Z}$ 이다. 이때 $1 \times n$ 행렬 $\mathbf{V}$, $d \times 1$ 행렬 $\mathbf{W}$ 에 대하여 스칼라

    $$ \alpha = \mathbf{VZW} = \mathbf{VXYW} $$

    를 얻는다. 이때 $\alpha$ 에 대한 $\mathbf{X}$ 의 미분은 

    $$ \dfrac{\partial \alpha }{\partial \mathbf{X}}= \mathbf{V}^{\intercal }\mathbf{W}^{\intercal }\mathbf{Y} ^{\intercal } = (\mathbf{YWV})^{\intercal } $$

    이다.

    - 증명
    
        행렬 $\mathbf{Z}$ 는 다음과 같다.
    
        $$\mathbf{Z} = \begin{pmatrix} z _{11} & z _{12} & \dots & z _{1d} \\ z _{21} & z _{22} & \dots & z _{2d} \\ \vdots & \vdots & \ddots & \vdots \\ z _{n1} & z _{n2} & \dots & z _{nd} \\ \end{pmatrix} = \begin{pmatrix} x _{11}& x _{12}& \dots& x _{1m} \\ x _{21}& x _{22}& \dots& x _{2m} \\ \vdots & \vdots & \ddots & \vdots \\ x _{n1}& x _{n2}& \dots& x _{nm} \\ \end{pmatrix}\begin{pmatrix} y _{11} & y _{12} & \dots & y _{1d} \\ y _{21} & y _{22} & \dots & y _{2d} \\ \vdots & \vdots & \ddots & \vdots \\ y _{m1} & y _{m2} & \dots & y _{md} \\ \end{pmatrix}$$

        $$ = \begin{pmatrix} \displaystyle\sum_{k=1}^{m}x _{1k}y _{k1}& \displaystyle\sum_{k=1}^{m}x _{1k}y _{k2}& \dots& \displaystyle\sum_{k=1}^{m}x _{1k}y _{kd} \\ \displaystyle\sum_{k=1}^{m}x _{2k}y _{k1}& \displaystyle\sum_{k=1}^{m}x _{2k}y _{k2}& \dots& \displaystyle\sum_{k=1}^{m}x _{2k}y _{kd} \\ \vdots & \vdots & \ddots & \vdots \\ \displaystyle\sum_{k=1}^{m}x _{nk}y _{k1}& \displaystyle\sum_{k=1}^{m}x _{nk}y _{k2}& \dots& \displaystyle\sum_{k=1}^{m}x _{nk}y _{kd} \\ \end{pmatrix} $$

        그러므로 

        $$ \mathbf{VZ} = \begin{pmatrix} v_1& v_2& \dots& v_n \\ \end{pmatrix} \begin{pmatrix} \displaystyle\sum_{k=1}^{m}x _{1k}y _{k1}& \displaystyle\sum_{k=1}^{m}x _{1k}y _{k2}& \dots& \displaystyle\sum_{k=1}^{m}x _{1k}y _{kd} \\ \displaystyle\sum_{k=1}^{m}x _{2k}y _{k1}& \displaystyle\sum_{k=1}^{m}x _{2k}y _{k2}& \dots& \displaystyle\sum_{k=1}^{m}x _{2k}y _{kd} \\ \vdots & \vdots & \ddots & \vdots \\ \displaystyle\sum_{k=1}^{m}x _{nk}y _{k1}& \displaystyle\sum_{k=1}^{m}x _{nk}y _{k2}& \dots& \displaystyle\sum_{k=1}^{m}x _{nk}y _{kd} \\ \end{pmatrix} $$

        $$ = \begin{pmatrix} \displaystyle \sum_{t=1}^{n}v_t \sum_{k=1}^{m}x _{tk}y _{k1}& \displaystyle \sum_{t=1}^{n}v_t \sum_{k=1}^{m}x _{tk}y _{k2}& \dots& \displaystyle \sum_{t=1}^{n}v_t \sum_{k=1}^{m}x _{tk}y _{kd}\\ \end{pmatrix} $$

        이고, 

        $$ \mathbf{VZW} = \begin{pmatrix} \displaystyle \sum_{t=1}^{n}v_t \sum_{k=1}^{m}x _{tk}y _{k1}& \displaystyle \sum_{t=1}^{n}v_t \sum_{k=1}^{m}x _{tk}y _{k2}& \dots& \displaystyle \sum_{t=1}^{n}v_t \sum_{k=1}^{m}x _{tk}y _{kd}\\ \end{pmatrix}\begin{pmatrix} w _1\\ w _2\\ \vdots \\ w _d\\ \end{pmatrix} $$

        $$ = w_1 \sum_{t=1}^{n}v_t \sum_{k=1}^{m}x _{tk}y _{k1}+ w_2 \sum_{t=1}^{n}v_t \sum_{k=1}^{m}x _{tk}y _{k2}+ \dots+ w_d \sum_{t=1}^{n}v_t \sum_{k=1}^{m}x _{tk}y _{kd} $$

        $$ = \sum_{s=1}^{d}w_s \sum_{t=1}^{n}v_t \sum_{k=1}^{m}x _{tk}y _{ks} = \alpha $$

        이다. ▲ 

        그러므로 $\mathbf{X}$ 의 $(i,j)$ 번째 원소 $x _{ij}$ 에 대한 $\alpha$ 의 미분은 $t = i, k = j$ 일 때 $\displaystyle \sum_{s=1}^{d}w_s \sum_{t=1}^{n}v_t \sum_{k=1}^{m}x _{tk}y _{ks}$ 가 $\displaystyle \sum_{s=1}^{d}w_sv_i x _{ij}y _{js}=v_i x _{ij}\sum_{s=1}^{d}w_sy _{js}$ 가 되므로

        $$ \dfrac{\partial \alpha }{\partial x _{ij}} = v_i\sum_{s=1}^{d}w_sy _{js} $$

        이다.

        행렬 미분의 정의에 따라 

        $$ \dfrac{\partial \alpha }{\partial \mathbf{X}} = \begin{pmatrix} \dfrac{\partial \alpha }{\partial x _{11}}& \dfrac{\partial \alpha }{\partial x _{12}}& \dots & \dfrac{\partial \alpha }{\partial x _{1m}} \\ \dfrac{\partial \alpha }{\partial x _{21}}& \dfrac{\partial \alpha }{\partial x _{22}}& \dots & \dfrac{\partial \alpha }{\partial x _{2m}} \\ \vdots & \vdots & \ddots & \vdots \\ \dfrac{\partial \alpha }{\partial x _{n1}}& \dfrac{\partial \alpha }{\partial x _{n2}}& \dots & \dfrac{\partial \alpha }{\partial x _{nm}} \\ \end{pmatrix} $$

        $$ = \begin{pmatrix} v_1 \displaystyle  \sum_{s=1}^{d}w_s y_{1s}& v_1 \displaystyle  \sum_{s=1}^{d}w_s y_{2s}& \dots& v_1 \displaystyle  \sum_{s=1}^{d}w_s y_{ms} \\ v_2 \displaystyle  \sum_{s=1}^{d}w_s y_{1s}& v_2 \displaystyle  \sum_{s=1}^{d}w_s y_{2s}& \dots& v_2 \displaystyle  \sum_{s=1}^{d}w_s y_{ms} \\ \vdots & \vdots & \ddots & \vdots \\ v_n \displaystyle  \sum_{s=1}^{d}w_s y_{1s}& v_n \displaystyle  \sum_{s=1}^{d}w_s y_{2s}& \dots& v_n \displaystyle  \sum_{s=1}^{d}w_s y_{ms} \\ \end{pmatrix} $$

        이다. ▲ 
        
        이것은 $\mathbf{Y}$ 와 $\mathbf{W}$ 의 행렬곱 $m \times 1$ 행렬

        $$ \mathbf{Y}\mathbf{W} = \begin{pmatrix} y _{11} & y _{12} & \dots & y _{1d} \\ y _{21} & y _{22} & \dots & y _{2d} \\ \vdots & \vdots & \ddots & \vdots \\ y _{m1} & y _{m2} & \dots & y _{md} \\ \end{pmatrix} \begin{pmatrix} w_1\\ w_2\\ \vdots\\ w_d\\ \end{pmatrix}  = \begin{pmatrix} \displaystyle \sum_{s=1}^{d}y _{1s}w _{s}\\ \displaystyle \sum_{s=1}^{d}y _{2s}w _{s}\\ \dots\\ \displaystyle \sum_{s=1}^{d}y _{ms}w _{s}\\ \end{pmatrix}$$

        의 역행렬 $1 \times m$ 행렬
        
        $$ (\mathbf{YW}) ^{\intercal } = \begin{pmatrix} \displaystyle \sum_{s=1}^{d}y _{1s}w _{s}& \displaystyle \sum_{s=1}^{d}y _{2s}w _{s}& \dots& \displaystyle \sum_{s=1}^{d}y _{ms}w _{s} \end{pmatrix}$$ 

        과 $\mathbf{V}$ 의 역행렬 $n \times 1$ 행렬 $\mathbf{V}^{\intercal } = \begin{pmatrix} v_1\\v_2\\\vdots\\v_n \\ \end{pmatrix}$ 의 행렬곱

        $$ \mathbf{V}^{\intercal }(\mathbf{YW})^{\intercal } = \begin{pmatrix} v_1\\v_2\\\vdots\\v_n \\ \end{pmatrix}\begin{pmatrix} \displaystyle \sum_{s=1}^{d}y _{1s}w _{s}& \displaystyle \sum_{s=1}^{d}y _{2s}w _{s}& \dots& \displaystyle \sum_{s=1}^{d}y _{ms}w _{s} \end{pmatrix} $$ 

        과 같다. ▲ 

        그러므로 최종적으로

        $$ \therefore  \dfrac{\partial \alpha }{\partial \mathbf{X}} = \mathbf{V}^{\intercal }(\mathbf{YW})^{\intercal } = \mathbf{V}^{\intercal }\mathbf{W}^{\intercal }\mathbf{Y} ^{\intercal } = (\mathbf{YWV})^{\intercal } $$

        이다. ■ 
    
    - $\mathbf{Z}$ 에 관하여
    
        $$ = \begin{pmatrix} \displaystyle \sum_{t=1}^{n}v_t \sum_{k=1}^{m}z _{k1}& \displaystyle \sum_{t=1}^{n}v_t \sum_{k=1}^{m}z _{k2}& \dots& \displaystyle \sum_{t=1}^{n}v_t \sum_{k=1}^{m}z _{kd}\\ \end{pmatrix} $$

        $$ = \sum_{s=1}^{d}w_s \sum_{t=1}^{n}v_t \sum_{k=1}^{m}z _{ks} = \alpha $$

        그러므로 $\mathbf{Z}$ 의 $(i,j)$ 번째 원소 $z _{ij}$ 에 대한 $\alpha$ 의 미분은 $k=i, s = j$ 일 때 $\displaystyle \sum_{s=1}^{d}w_s \sum_{t=1}^{n}v_t \sum_{k=1}^{m}z _{ks}$ 가 $\displaystyle w_j z _{ij} \sum_{t=1}^{n}v_t$ 가 되므로 

        $$ \dfrac{\partial \alpha }{\partial z _{ij}} = w_j \sum_{t=1}^{n}v_t $$

        행렬 미분의 정의에 따라 $\alpha$ 에 대한 $\mathbf{Z}$ 의 미분은 $n \times d$ 행렬

        $$ \dfrac{\partial \alpha }{\partial \mathbf{Z}} = \begin{pmatrix} \dfrac{\partial \alpha }{\partial z_{11}}& \dfrac{\partial \alpha }{\partial z_{12}}& \dots & \dfrac{\partial \alpha }{\partial z_{1d}} \\ \dfrac{\partial \alpha }{\partial z_{21}}& \dfrac{\partial \alpha }{\partial z_{22}}& \dots & \dfrac{\partial \alpha }{\partial z_{2d}} \\ \vdots & \vdots & \ddots & \vdots \\ \dfrac{\partial \alpha }{\partial z_{n1}}& \dfrac{\partial \alpha }{\partial z_{n2}}& \dots & \dfrac{\partial \alpha }{\partial z_{nd}} \\ \end{pmatrix} $$

        $$ = \begin{pmatrix} w _1 \displaystyle  \sum_{t=1}^{n}v_{t}& w _2 \displaystyle  \sum_{t=1}^{n}v_{t}& \dots& w _d \displaystyle  \sum_{t=1}^{n}v_{t} \\ w _1 \displaystyle  \sum_{t=1}^{n}v_{t}& w _2 \displaystyle  \sum_{t=1}^{n}v_{t}& \dots& w _d \displaystyle  \sum_{t=1}^{n}v_{t} \\ \vdots & \vdots & \ddots & \vdots \\ w _1 \displaystyle  \sum_{t=1}^{2}v_{t}& w _2 \displaystyle  \sum_{t=1}^{n}v_{t}& \dots& w _d \displaystyle  \sum_{t=1}^{n}v_{t} \\ \end{pmatrix} $$

        이다. ▲ 

        이것은 $n \times 1$ 행렬 $\begin{pmatrix} \displaystyle\sum_{t=1}^{n}v_t\\\displaystyle\sum_{t=1}^{n}v_t\\\vdots\\\displaystyle\sum_{t=1}^{n}v_t \\ \end{pmatrix}$ 과 $1 \times d$ 행렬 $\mathbf{W} ^{\intercal } = \begin{pmatrix} w_1& w_2& \dots& w_d\\ \end{pmatrix}$ 의 행렬곱

        $$ \begin{pmatrix} \displaystyle\sum_{t=1}^{n}v_t\\\displaystyle\sum_{t=1}^{n}v_t\\\vdots\\\displaystyle\sum_{t=1}^{n}v_t \\ \end{pmatrix} \begin{pmatrix} w_1& w_2& \dots& w_d\\ \end{pmatrix} =
        \begin{pmatrix} \displaystyle\sum_{t=1}^{n}v_t\\\displaystyle\sum_{t=1}^{n}v_t\\\vdots\\\displaystyle\sum_{t=1}^{n}v_t \\ \end{pmatrix} \mathbf{W}^{\intercal }$$

        이다. 그런데 이것을 또 다시 $n \times n$ 일행렬 $\mathbf{J}$ 와 $n \times 1$ 행렬 $\mathbf{V}^{\intercal }$ 의 행렬곱

        $$ \mathbf{J} \mathbf{V}^{\intercal j} = \begin{pmatrix} 1& 1& \dots& 1 \\ 1& 1& \dots& 1 \\ \vdots & \vdots & \ddots & \vdots \\ 1& 1& \dots& 1 \\ \end{pmatrix} \begin{pmatrix} v_1\\v_2\\\vdots\\v_n \\ \end{pmatrix} =  \begin{pmatrix} \displaystyle\sum_{t=1}^{n}v_t\\\displaystyle\sum_{t=1}^{n}v_t\\\vdots\\\displaystyle\sum_{t=1}^{n}v_t \\ \end{pmatrix}$$
        
        을 사용하여 최종적으로 

        $$ \therefore \dfrac{\partial \alpha }{\partial \mathbf{Z}} = \mathbf{JV}^{\intercal }\mathbf{W}^{\intercal } $$

        로 표현할 수 있다.

    - 행렬곱 $\mathbf{Z = XY}$ 에 대한 $\mathbf{X}$ 의 미분 

        행렬 $\mathbf{Z}$ 는 다음과 같다.
    
        $$\mathbf{Z} = \begin{pmatrix} z _{11} & z _{12} & \dots & z _{1d} \\ z _{21} & z _{22} & \dots & z _{2d} \\ \vdots & \vdots & \ddots & \vdots \\ z _{n1} & z _{n2} & \dots & z _{nd} \\ \end{pmatrix} = \begin{pmatrix} x _{11}& x _{12}& \dots& x _{1m} \\ x _{21}& x _{22}& \dots& x _{2m} \\ \vdots & \vdots & \ddots & \vdots \\ x _{n1}& x _{n2}& \dots& x _{nm} \\ \end{pmatrix}\begin{pmatrix} y _{11} & y _{12} & \dots & y _{1d} \\ y _{21} & y _{22} & \dots & y _{2d} \\ \vdots & \vdots & \ddots & \vdots \\ y _{m1} & y _{m2} & \dots & y _{md} \\ \end{pmatrix}$$

        $$ = \begin{pmatrix} \displaystyle\sum_{k=1}^{m}x _{1k}y _{k1}& \displaystyle\sum_{k=1}^{m}x _{1k}y _{k2}& \dots& \displaystyle\sum_{k=1}^{m}x _{1k}y _{kd} \\ \displaystyle\sum_{k=1}^{m}x _{2k}y _{k1}& \displaystyle\sum_{k=1}^{m}x _{2k}y _{k2}& \dots& \displaystyle\sum_{k=1}^{m}x _{2k}y _{kd} \\ \vdots & \vdots & \ddots & \vdots \\ \displaystyle\sum_{k=1}^{m}x _{nk}y _{k1}& \displaystyle\sum_{k=1}^{m}x _{nk}y _{k2}& \dots& \displaystyle\sum_{k=1}^{m}x _{nk}y _{kd} \\ \end{pmatrix} $$

        그러므로 $\mathbf{Z}$ 의 $(i,j)$ 번째 원소 $z _{ij}$ 에 대한 $x _{st}$ 의 미분은 

        $$ \dfrac{\partial z _{ij}}{\partial x _{st}} = \dfrac{\partial }{\partial x _{st}}\sum_{k=1}^{m}x _{ik}y _{kj} = $$