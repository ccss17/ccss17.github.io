# [ccss17.github.io](https://ccss17.github.io)

---

# <a name="미분(differential)" href="#미분(differential)">미분(differential)</a>


## <a name="이변수 함수 선형화" href="#이변수 함수 선형화">이변수 함수 선형화</a>

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

접평면(tangent plane) : $3$ 차원 곡면의 한 접점에 존재하는 무수히 많은 접선들이 동시에 상주하고 있는 평면이다.

![index](https://user-images.githubusercontent.com/16812446/79077468-ec0ce800-7d3c-11ea-8d57-3c992ab66d6e.jpg)

</blockquote>

- 위 그림과 같이 어떤 곡면에는 접선이 무수히 많고 그 접선들이 상주하는 평면이 곡면의 접평면이다. 

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

법선벡터(normal vector) : 접평면에 직교하는 벡터이다.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Surface_normal_illustration.svg/220px-Surface_normal_illustration.svg.png)

</blockquote>

- 즉 법선벡터는 위 그림의 화살표 벡터와 같이 $3$ 차원 곡면의 한 접점에서의 모든 접선과 직교한다.

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

이변수 함수 선형화 또는 접평면(tangent plane) : $f$ 의 연속인 편도함수들이 존재할 때 점 $P(x_0, y_0, z_0)$ 에서 곡면 $z = f(x, y)$ 에 대한 접평면의 방정식은 

$$ z - z_0 = f_x(x_0, y_0)(x- x_0) + f_y(x_0, y_0)(y - y_0) $$

또는 

$$ L(x, y) = f(x_0, y_0) + f_x(x_0, y_0)(x-x_0) + f_y(x_0, y_0)(y - y_0)

$$

이고 이것은 이변수 함수 $f(x, y)$ 의 선형화이다. 

</blockquote>

- 또한 점 $P(x_0, y_0, z_0)$ 근방에서 

  $$ f(x, y) \approx L(x, y) $$

  이 성립한다.

  일변수 함수 $f$ 를 $x=a$ 에서 끝없이 확대했을 때 $x=a$ 에서 접선과 거의 똑같아지는 것과 같이 이변수 함수 $f$ 를 끝없이 확대하면 접평면의 방정식과 거의 똑같아지기 때문이다. 

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

이변수 함수 미분 또는 전미분(total differential) : 점 $(x_0, y_0)$ 에서 점 $(x_0 + dx, y_0 + dy)$ 로 움직였을 때의 변화량 

$$ df = f_x(x_0, y_0)dx + f_y (x_0, y_0)dy $$

또는

$$ df = \frac{\partial f}{\partial x} dx + \frac{\partial f}{\partial y} dy $$

을 함수 $f$ 의 전미분이라 한다. 

</blockquote>

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

# <a name="방향미분과 편미분의 일반적인 정의" href="#방향미분과 편미분의 일반적인 정의">방향미분과 편미분의 일반적인 정의</a>

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

**다변수함수의 변화율 조사와 일변수 함수의 변화율 조사의 차이점** : 일변수 함수의 미분에서는 변수가 변할 수 있는 방향이 본질적으로 하나뿐(변수가 증가하는 방향) 이지만 

다변수 함수의 경우 변수의 변화의 방향이 무수히 많은데, 이 방향을 보통 단위벡터로 결정한다.

</blockquote>

- 예시 

  우리에게 익숙한 일변수 함수 $y = f(x)$ 의 변화율을 조사할 때 변수 $x$ 의 변화에 관한 $y$ 의 변화율만 조사하면 되었었다.

  그런데 독립변수가 $2$ 개인 다변수 함수 $z = f(x, y)$ 의 변화율을 조사할 때는 변수 $x$ 의 변화에 관한 $z$ 의 변화율만 조사하는 것이 아니라 
  
  변수 $x$ 와 변수 $y$ 가 변하는 방향을 먼저 정의하고 $z$ 의 변화율을 조사해야 한다.

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

열린집합 또는 개집합(open set) : 위상수학에서 열린집합은 스스로의 경계를 포함하지 않는 위상 공간의 부분집합이다.

</blockquote>

- 함수의 변화를 조사하려 할 때, 함수가 한 점에서 정의될 뿐 아니라 그 점의 근방에서 정의되어야 하는 것이 요구된다. 왜냐하면 그래야만 그 함수의 그 점에서의 변화를 조사하기에 용이하기 때문이다.

  따라서 미분법에서 함수의 정의역이 한 점을 포함하면, 그 점의 근방이 정의역에 포함되기를 바라는데 이런 집합을 열린 집합이라고 한다.

- 예시

  양수 $r$ 에 대하여 $n$-공간의 한 점 $P$ 를 중심으로 반지름이 $r$ 인 열린공

  $$ \mathbb{B} ^{n}(P, r) := \{X \in \R ^{n} \Big ||X-P| < r\} $$

  은 열린 집합이다.

  다음은 2차원 열린 공으로써, 열린 원판 $\mathbb{B} ^{2}$ 이다.

  ![](https://mblogthumb-phinf.pstatic.net/20141228_119/dydrogud22_1419762043201Uk8cC_JPEG/2.jpg?type=w2)

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

$v$-방향미분계수, 또는 $v$-방향 순간변화율 : $n$-공간의 열린 집합 $U$ 에서 정의된 함수 

$$ f: U \to \R $$

와 $U$ 의 한 점 $P$ 와 벡터 $v$ 에 대하여 극한값

$$ D_vf(P) := \lim_{t \to 0} \dfrac{f(P+tv)-f(P)}{t}=\dfrac{d}{dt}\bigg | _{0}f(P+tv) $$

이 존재하면 이 값을 점 $P$ 에서 $f$ 의 $v$-방향미분계수 또는 $v$-방향 순간변화율이라 한다.

</blockquote>

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

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

편미분계수 : $n$-공간의 $n$개의 축 방향의 단위벡터인 표준단위벡터 

$$ e_1 := (1,0,\dots,0), \dots, e_n := (0,0,\dots,1), $$

에 대하여 점 $P = (p_1, \dots,p_n)$ 에서 함수 $f: U \to \R$ 의 $e_k$-방향미분계수 

$$D _{k}f(P) = \dfrac{\partial f(P)}{\partial x_k} = \dfrac{d}{dt}\bigg | _{0}f(p_1, \dots,p_k+t,\dots,p_n)$$

를 점 $P$ 에서 $f$ 의 $k$번째 편미분계수라고 한다.

</blockquote>

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

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

편도함수 : 함수 $f$ 가 점 $P = (p_1, \dots,p_n)$ 에 대하여 정의역 $U$ 의 모든 점에 대하여 $k$번째 편미분계수를 가지면 함수 

$$ D_kf:U \to \R, P \mapsto D_kf(P) $$

를 $f$의 $k$번째 편도함수라고 한다.

</blockquote>

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

## <a name="기울기 벡터의 일반적인 정의" href="#기울기 벡터의 일반적인 정의">기울기 벡터의 일반적인 정의</a>

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

편미분 가능 : $n$변수함수 $f$ 의 모든 편미분계수가 점 $P$ 에서 존재할 때, $f$ 는 점 $P$ 에서 편미분 가능하다.

</blockquote>

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

기울기벡터(gradient vector) : $n$변수함수 $f$ 가 점 $P$ 에서 편미분가능할 때 벡터

$$ \text{grad}\ f(P) := (D_1f(P), \dots, D_nf(P)) $$

를 점 $P$ 에서 $f$ 의 기울기 벡터라고 한다.

</blockquote>

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

  이다. □ 

  $$ D_2f(x,y,z) = \dfrac{\partial e ^{x+yz}}{\partial y} = $$

  에서 지수함수 $y=  a^x$ 의 도함수는 $y' = a^x \ln a$ 이므로 

  $$ = e ^{x}\dfrac{\partial (e ^{z})^{y}}{\partial y} = e ^{x}(e ^{z})^{y}\ln e ^{z} = e ^{x+zy} \cdot z = zf(x,y,z) $$

  이다. □ 
  
  마찬가지로 

  $$ D_3f(x,y,z) = yf(x,y,z) $$

  이다. □ 

  그런데 $f(O) = e^{0+0 \cdot 0} = 1$ 이므로 

  $$ D_1f(O) = 1, D_2f(O) =1 \cdot  0 = 0, D_3f(O) = 1 \cdot  0 = 0 $$

  이고, 이에따라 원점 $O$ 에서의 $f$ 의 기울기 벡터 

  $$ \therefore \text{grad}\ f(O) = (1,0,0) $$

  을 얻는다. ■ 

## <a name="미분 가능의 일반적인 정의" href="#미분 가능의 일반적인 정의">미분 가능의 일반적인 정의</a>

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

**$n$-공간의 열린 집합에서 정의된 함수 $f$ 의 미분 가능** : 

</blockquote>

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

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

일급함수 : $n$-공간의 열린 집합에서 정의된 함수 $f(x_1, \dots, x_n)$ 의 각 편도함수 

$$ \dfrac{\partial f}{\partial x_1}, \dots,\dfrac{\partial f}{\partial x_n} $$

가 연속이면, $f$ 를 일급함수 또는 $\mathcal{C} ^{1}$ 라고 한다.

</blockquote>

# <a name="다변수 벡터함수" href="#다변수 벡터함수">다변수 벡터함수</a>

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

함수의 분류 : 함수는 정의역과 공역의 차원을 기준으로 다음 $4$ 가지로 분류된다. 

1. 실함수(real valued functions) : 다음과 같이 $1$차원에서 $1$차원으로 가는 함수이다.

    $$ \R \to \R $$

2. 매개화된 곡선(parametrized curves) : 다음과 같이 $1$차원에서 $n$차원으로 가는 함수이다.

    $$ \R \to \R ^{n}$$

3. 다변수 함수(functions of several variables) : 다음과 같이 $n$차원에서 $1$차원으로 가는 함수이다.

    $$ \R ^{n} \to \R $$

4. 다변수 벡터함수(vector valued functions of several variables) : 다음과 같이 $n$차원에서 $m$차원으로 가는 함수이다.

    $$ \R ^{n} \to \R ^{m} $$

</blockquote>

- 지금까지 실함수와 다변수함수의 미분을 살펴봤는데, 이제 다변수 벡터함수의 미분을 살펴본다. 

  다변수 벡터함수의 미분은 야코비 행렬로 표현된다. 정의역과 공역의 차원이 같은 함수, 즉 

  $$ R ^{n} \to R ^{n} $$

  는 야코비 행렬의 행렬식을 구할 수 있고, 이 값의 절대값은 부피변화율을 나타내는 것임을 알아볼 것이다.

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

다변수 벡터함수(vector valued functions of several variables) : $n$-공간의 한 부분집합에서 정의된 벡터함수

$$ F: \R ^{n} \to \R ^{m} $$

는 $F$ 의 성분함수 $f_1, \dots, f_m$ 에 대하여

$$ F(x_1, \dots,x_n) = (f_1(x_1, \dots,x_n), \dots, f_m(x_1, \dots,x_n)) $$

이다.

</blockquote>

- 예시 

  함수 $F(x, y) = (e ^{x}\cos y, e ^{x}\sin y, x+y)$ 는 다변수 벡터함수이다.

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

야코비 행렬(jacobian matrix) : 열린집합 $U \subset \R ^{n}$ 에서 정의된 함수 벡터함수 $f: U \to \R ^{m}$ 가 $F = (f_1, \dots, f_m)$ 가 점 $P \in U$ 에서 미분가능하면 

$f'_1(P) = \text{grad}\ f_1(P)$ 를 첫번째 행,

$f'_2(P) = \text{grad}\ f_2(P)$ 를 두번째 행,

$f'_m(P) = \text{grad}\ f_m(P)$ 를 마지막 행으로 하는 행렬

$$ F'(P) := \dfrac{\partial (f_1, \dots, f_m)}{\partial (x_1, \dots, x_n)}(P) := \begin{pmatrix} \dfrac{\partial f_1}{\partial x_1}(P)&\dfrac{\partial f_1}{\partial x_2}(P)&\dots&\dfrac{\partial f_1}{\partial x_n}(P)\\ \dfrac{\partial f_2}{\partial x_1}(P)&\dfrac{\partial f_2}{\partial x_2}(P)&\dots&\dfrac{\partial f_2}{\partial x_n}(P)\\ \vdots &\ddots &\cdots&\vdots \\ \dfrac{\partial f_m}{\partial x_1}(P)&\dfrac{\partial f_m}{\partial x_2}(P)&\dots&\dfrac{\partial f_m}{\partial x_n}(P)\\ \end{pmatrix} $$

을 점 $P$ 에서 $F$ 의 야코비 행렬이라고 한다.

</blockquote>

- 예시 

  $F: \R ^{2} \to \R ^{3}$ 로 정의된 다변수 벡터함수 $F(x, y) = (e ^{x}\cos y, e ^{x}\sin y, x+y)$ 의 야코비행렬은 

  $$ F'(x, y) = \begin{pmatrix} e ^{x}\cos y&-e ^{x}\sin y\\ e ^{x}\sin y&e ^{x}\cos y\\ 1&1\\ \end{pmatrix} $$

  이다.

# <a name="행렬 미분" href="#행렬 미분">행렬 미분</a>

- 행렬 표기 

  $i \in \{1,2,\dots,m\}$, $j \in \{1,2,\dots,n\}$ 에 대한 $a _{ij}\in \R$ 에 대하여 행렬 

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

  - $m \times n$ 행렬 $\mathbf{A}$ 와 $n \times 1$ 행렬 $\mathbf{x} \in \R ^{n}$, 즉 벡터 $\mathbf{x}$ 에 대하여 

    $$ \mathbf{z} = \mathbf{Ax} $$

    는 $m \times 1$ 행렬, 즉 벡터 $\mathbf{z}\in \R ^{m}$ 이다.

    벡터 $\mathbf{z}$ 의 원소 $z_i$ 는 $a _{ik} \in \mathbf{A}, x_k \in \mathbf{x}$ 에 대하여 다음과 같이 결정된다. 

    $$ z_i = \sum_{k=1}^{n}a _{ik}x _{k} $$
  
  - 한편 $m \times 1$ 행렬 $\mathbf{y} \in \R ^{m}$ 에 대하여

    $$ \mathbf{z}^{T}=\mathbf{y}^{T}\mathbf{A} $$

    는 $n \times 1$ 행렬, 즉 벡터 $\mathbf{z} \in \R ^{n}$ 이다.

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

  - 벡터 $\mathbf{y} \in \R ^{m}$ 와 $\mathbf{x} \in \R ^{n}$ 에 대하여 다변수벡터함수

    $$ \mathbf{y} = \Psi (\mathbf{x}) $$

    가 존재한다. 이때 $\mathbf{y}$ 에 대한 $\mathbf{x}$ 의 미분은 다변수벡터함수의 미분, 즉 야코비 행렬 

    $$ \dfrac{\partial \mathbf{y}}{\partial \mathbf{x}} = \begin{bmatrix} \dfrac{\partial y_1}{\partial x_1} && \dfrac{\partial y_1}{\partial x_2} && \dots && \dfrac{\partial y_1}{\partial x_n} \\ \dfrac{\partial y_2}{\partial x_1} && \dfrac{\partial y_2}{\partial x_2} && \dots && \dfrac{\partial y_2}{\partial x_n} \\ \vdots && \vdots && \ddots && \vdots \\ \dfrac{\partial y_m}{\partial x_1} && \dfrac{\partial y_m}{\partial x_2} && \dots && \dfrac{\partial y_m}{\partial x_n} \end{bmatrix} $$

    이다.

    - 이 행렬을 변환 $\Psi ()$ 의 야코비 행렬이라고 한다.

- 정리 5 (다변수벡터함수 미분)

  벡터 $\mathbf{y} \in \R ^{m}$($m \times 1$ 행렬), $\mathbf{x} \in \R ^{n}$($n \times 1$ 행렬) 와 $m \times n$ 행렬 $\mathbf{A}$ 에 대한 행렬방정식 $\mathbf{y} = \mathbf{Ax}$ 의 미분은 

  $$ \dfrac{\partial \mathbf{y}}{\partial \mathbf{x}}=\mathbf{A} $$

  이다.

  - 증명 

    $\mathbf{y}$ 의 $i$ 번째 원소는 $\displaystyle  y_i = \sum_{k=1}^{n}a _{ik}x_k$ 이다. 그러므로 $y_i$ 에 대한 $x_j$ 의 미분은 

    $$ \dfrac{\partial y_i}{\partial x_j} = \dfrac{\partial }{\partial x_j}\sum_{k=1}^{n}a _{ik}x_k = a _{ij} $$

    이다. 그렇다면 $i \in \{1,2,\dots,m\}$, $j \in \{1,2,\dots,n\}$ 에서 $\mathbf{y}$ 에 대한 $\mathbf{x}$ 의 미분은 다변수벡터함수의 미분, 즉 야코비행렬

    $$ \dfrac{\partial \mathbf{y}}{\partial \mathbf{x}} = \begin{bmatrix} \dfrac{\partial y_1}{\partial x_1} && \dfrac{\partial y_1}{\partial x_2} && \dots && \dfrac{\partial y_1}{\partial x_n} \\ \dfrac{\partial y_2}{\partial x_1} && \dfrac{\partial y_2}{\partial x_2} && \dots && \dfrac{\partial y_2}{\partial x_n} \\ \vdots && \vdots && \ddots && \vdots \\ \dfrac{\partial y_m}{\partial x_1} && \dfrac{\partial y_m}{\partial x_2} && \dots && \dfrac{\partial y_m}{\partial x_n} \end{bmatrix} =  \begin{bmatrix} a_{11} && a_{12} && \dots && a_{1n} \\ a_{21} && a_{22} && \dots && a_{2n} \\ \vdots && \vdots && \ddots && \vdots \\ a_{m1} && a_{m2} && \dots && a_{mn} \end{bmatrix} = \mathbf{A} $$

    이다.

- 정리 6 (매개변수를 갖는 행렬방정식의 미분)

  벡터 $\mathbf{y} \in \R ^{m}$($m \times 1$ 행렬), $\mathbf{x} \in \R ^{n}$($n \times 1$ 행렬) 와 $m \times n$ 행렬 $\mathbf{A}$ 이 존재할때 $\mathbf{x}$ 가 벡터 $\mathbf{z}$ 에 대한 함수라면 행렬방정식 $\mathbf{y} = \mathbf{Ax}$ 의 미분은 

  $$ \dfrac{\partial \mathbf{y}}{\partial \mathbf{z}} = \dfrac{\partial \mathbf{y}}{\partial \mathbf{x}}\dfrac{\partial \mathbf{x}}{\partial \mathbf{z}} = \mathbf{A}\dfrac{\partial \mathbf{x}}{\partial \mathbf{z}} $$ 

  이다.

  - 증명 

    $\mathbf{y}$ 의 $i$ 번째 원소는 $\displaystyle y_i = \sum_{k=1}^{n}a _{ik}x _{k}$ 이다. 또 $\mathbf{x} \in \R ^{n}$ 는 독립변수 $\mathbf{z} \in \R ^{n}$ 를 $\mathbf{y} \in \R ^{m}$ 로 잇는 매개변수이다. 그러므로 $y_i$ 에 대한 $z_j$ 의 미분은 $1$ 개의 독립변수와 $n$ 개의 매개변수에 대한 일변수 합성함수에 대한 미분이다. 그러므로 
    
    <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

    $1$ 개의 독립변수와 $m$ 개의 매개변수에 대한 다변수 합성함수의 편도함수(chain rule) : 유한개의 매개변수 $x_1, x_2, \dots, x_m$ 에 대한 다변수 함수 $w = f(x_1, x_2, \dots, x_m)$ 가 미분가능하고,

    $1$ 개의 독립변수 $p$ 에 대한 함수 $x_1, x_2, \dots, x_m$ 도 미분가능하면,

    $w$ 가 미분가능하고 $p$ 에 대한 함수들도 미분가능하며

    독립변수 $p$ 에 대한 $w$ 의 편도함수는 다음과 같다. 

    $$ \frac{\partial  w}{\partial p} = \frac{\partial w}{\partial x_1}\frac{\partial  x_1}{\partial  p} + \frac{\partial w}{\partial x_2}\frac{\partial  x_2}{\partial  p} + \dots + \frac{\partial w}{\partial x_m}\frac{\partial  x_m}{\partial  p} = \sum_{k=1}^{m}\dfrac{\partial  w}{\partial x_k}\dfrac{\partial  x_k}{\partial p}$$

    </blockquote>

    에 의하여 $y_i$ 에 대한 $z_j$ 의 미분은 

    $$ \dfrac{\partial y_i}{\partial z_j} = \dfrac{\partial y_i}{\partial  x_1}\dfrac{\partial x_1}{\partial z_j} +\dfrac{\partial y_i}{\partial  x_2}\dfrac{\partial x_2}{\partial z_j} +\dots +\dfrac{\partial y_i}{\partial  x_n}\dfrac{\partial x_n}{\partial z_j} = \sum_{k=1}^{n}\dfrac{\partial y_i}{\partial x_k}\dfrac{\partial x_k}{\partial z_j} = \sum_{k=1}^{n}a _{ik}\dfrac{\partial x_k}{\partial z_j} $$

    이다. 
    
    그렇다면 $i \in \{1,2,\dots,m\}, j \in \{1,2,\dots,n\}$ 에 대하여 $\displaystyle \sum_{k=1}^{n}a _{ik}\dfrac{\partial x_k}{\partial z_j}$ 를 $\mathbf{A}\dfrac{\partial \mathbf{x}}{\partial \mathbf{z}}$ 로 일반화시킬 수 있고, 이에따라 $\mathbf{y}$ 에 대한 $\mathbf{z}$ 의 미분은 

    $$ \dfrac{\partial \mathbf{y}}{\partial \mathbf{z}}= \dfrac{\partial \mathbf{y}}{\partial \mathbf{x}}\dfrac{\partial \mathbf{x}}{\partial \mathbf{z}}= \mathbf{A}\dfrac{\partial \mathbf{x}}{\partial \mathbf{z}} $$

    이다.

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
    
    그렇다면 정리 5 "벡터 $\mathbf{y} \in \R ^{m}$($m \times 1$ 행렬), $\mathbf{x} \in \R ^{n}$($n \times 1$ 행렬) 
    와 $m \times n$ 행렬 $\mathbf{A}$ 에 대한 행렬방정식 $\mathbf{y} = \mathbf{Ax}$ 의 미분은 $\dfrac{\partial \mathbf{y}}{\partial \mathbf{x}}=\mathbf{A}$ 이다." 에서 $m = 1$ 로 두면

    "스칼라 $y \in \R$($1 \times 1$ 행렬), $\mathbf{x} \in \R ^{n}$($n \times 1$ 행렬) 와 $1 \times n$ 행렬 $\mathbf{A}$ 에 대한 행렬방정식 $y = \mathbf{Ax}$ 의 미분은 $\dfrac{\partial y}{\partial \mathbf{x}}=\mathbf{A}$ 이다." 이므로 

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

    이다. 그런데 $n \times 1$ 행렬 $\mathbf{Ax} = \begin{pmatrix} \displaystyle \sum_{i=1}^{n} a _{1i} x_i\\ \displaystyle\sum_{i=1}^{n} a _{2i} x_i\\ \vdots \\ \displaystyle\sum_{i=1}^{n} a _{ni} x_i\\ \end{pmatrix}$ 에 대한 전치는 $1 \times n$ 행렬

    $$\mathbf{x ^{\intercal }A ^{\intercal }} = \begin{pmatrix} \displaystyle \sum_{i=1}^{n} a _{1i} x_i& \displaystyle\sum_{i=1}^{n} a _{2i} x_i& \dots & \displaystyle\sum_{i=1}^{n} a _{ni} x_i \end{pmatrix}$$

    이고,

    $$\mathbf{x ^{\intercal }A } = \begin{pmatrix} \displaystyle \sum_{i=1}^{n} a _{i1} x_i& \displaystyle\sum_{i=1}^{n} a _{i2} x_i& \dots & \displaystyle\sum_{i=1}^{n} a _{in} x_i \end{pmatrix}$$

    이다.

    그러므로 $\forall k \in \{1,2,\dots,n\}$ 에 대하여 

    $$ \dfrac{\partial \alpha }{\partial \mathbf{x}} = \mathbf{x ^{\intercal }A ^{\intercal }} + \mathbf{x ^{\intercal }A} = \mathbf{x ^{\intercal }(A ^{\intercal }+ A)} $$

    이다. ■   