# [ccss17.github.io](https://ccss17.github.io)

---

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

  $n=1$ 일 때 $n$-공간에서 함수 $f(x)$ 가 점 $p$ 에서 미분가능하다는 것은 $x=p$ 에서 미분계수 $f'(p)$ 가 존재한다는 것

  기하학적으로 함수 $f$ 의 그래프가 점 $(p, f(p))$ 에서 접선을 가진다는 것이었다.

  점 $(p, f(p))$ 를 지나는 직선의 방정식은 

  $$ y = f(p)+a(x-p) $$

  이었고, 이 직선이 $x=p$ 일 때
