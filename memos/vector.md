# [ccss17.github.io](https://ccss17.github.io)

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

## <a name="**미적분 메모**" href="#**미적분 메모**">**미적분 메모**</a>

**[극한 메모](https://ccss17.github.io/calculus.html)**

**[미분 메모](https://ccss17.github.io/calculus2.html)**

**[적분 메모](https://ccss17.github.io/calculus3.html)**

**[미분2 메모](https://ccss17.github.io/calculus4.html)**

**[적분2 메모](https://ccss17.github.io/calculus5.html)**

**[벡터해석학 메모](https://ccss17.github.io/vector.html)**

**[미적분 메모](https://ccss17.github.io/calculus6.html)**

</blockquote>

# <a name="벡터해석학 메모" href="#벡터해석학 메모">벡터해석학 메모</a>

---

# <a name="매개변수 방정식 " href="#매개변수 방정식 ">매개변수 방정식 </a>

곡선을 두 독립변수 $x, y$ 로 나타내는 것이 아니라 매개변수를 통한 방정식으로 나타내면 훨씬 더 일반적인 곡선을 표현할 수 있다. 

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

매개변수 방정식(parametric equations) : $x, y$ 가 각각 구간 $I$ 의 $t$ 에 대한 함수 

$$ x = f(t), y = g(t) $$

일 때, 위 방정식을 곡선의 매개변수 방정식이라 한다. 

</blockquote>

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

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

매개변수 곡선(parametric curve) : 매개변수 방정식의 정의에서 매개변수 방정식으로 정의된 점들의 집합 $(x, y) = (f(t), g(t))$ 을 매개변수 곡선이라 한다. 

</blockquote>

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

매개변수 구간(parametric interval) : 매개변수 방정식의 정의에서 정의역 $I$ 를 매개변수 구간이라 한다. 

</blockquote>

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

시점(initial point) : 매개변수 방정식의 정의에서 $I$ 가 폐구간이고 $t$ 가 $a \leq t \leq b$ 로 정의되었을 때 점 $(f(a), g(a))$ 를 곡선의 시점이라 한다.

</blockquote>

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

종점(terminal point) : 매개변수 방정식의 정의에서 $I$ 가 폐구간이고 $t$ 가 $a \leq t \leq b$ 로 정의되었을 때 점 $(f(b), g(b))$ 를 곡선의 종점이라 한다.

</blockquote>

# <a name="벡터 " href="#벡터 ">벡터 </a>

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

양 : 어떤 물체의 크기이다.

</blockquote>

- 측정 가능한 양(물리량)과 측정 불가능한 양(비물리량)으로 나눌 수 있다.

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

물리량 : 측정 가능한 양이다.

</blockquote>

- 벡터와 스칼라로 나눌 수 있다. 

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

비물리량 : 측정 불가능한 양이다. 

</blockquote>

- 예시 

  "$A$ 의 키는 $180$ cm 이다." 에서 $180$ cm 의 키는 측정 가능한 물리량이다.

  반면 "$A$ 가 $B$ 보다 더 리더십이 있다." 에서 리더십의 비교는 측정이 불가능한 비물리량이다. 

  > 그러나 리더십이라는 대상에 대한 단순화 및 집합으로의 환원을 거쳐서 측정하능하게 만들 수 있다는 가능성을 볼 수 있다. 여기에서 더 나아가 철학적 관념 또한 단순화와 수학적 모델링을 거쳐서 측정가능한 수로 격하시킬 수 있는 가능성도 엿볼 수 있다. 

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

스칼라(scala) : 크기만 있고 방향성이 없는 물리량이다. 

</blockquote>

- 길이, 넓이, 부피 등이 스칼라량에 속한다. 

- 그냥 단순히 실수로 생각하면 된다! 

- 예시 

  "$A$ 는 $20$ 분을 뛰었다" 에서 $20$ 은 스칼라량이다. 

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

벡터(vector) 또는 유향선분(directed segment) : 크기와 방향성이 동시에 있는 물리량이다. 

</blockquote>

> 크기와 방향성이 있는 자연대상을 수학적 추상대상물로 추상화한 것으로 볼 수 있을 것 같다. 

- 스칼라량으로는 방향에 대한 정보가 부족하기에 방향에 대한 정보를 덧붙힌 것이 벡터이다. 

  - 그래서 방향성이 있는 선분 "유향선분" 이라고도 부른다.

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

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

벡터의 시점(initial point) : 다음과 같이 점 $A$ 에서 점 $B$ 로 방향이 주어진 선분 $AB$ 를 벡터 $AB$ 에서

![](https://t1.daumcdn.net/cfile/tistory/267BE245539F79880C)

점 $A$ 를 벡터의 시점이라 한다. 

</blockquote>

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

벡터의 종점(terminal point) : 다음과 같이 점 $A$ 에서 점 $B$ 로 방향이 주어진 선분 $AB$ 를 벡터 $AB$ 에서

![](https://t1.daumcdn.net/cfile/tistory/267BE245539F79880C)

점 $B$ 를 벡터의 종점이라 한다. 

</blockquote>

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

스칼라 함수(scalar function) : 실숫값 함수와 같이 어떤 점을 하나의 스칼라에 대응시키는 함수이다.

</blockquote>

- 즉 여러 독립변수에 대응하는 하나의 함수 값이 스칼라가 된다. 

- 지금까지 살펴본 함수들이 스칼라 함수에 해당한다. 

- 실숫값 함수의 정의처럼 공역이 실수 집합 $\R$ 인 함수 

  $$ f: X \to \R $$

  이다. 

- 예시 

  $$ y = x ^{2}, y = \sin x, y = \ln x \dots $$

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

벡터 함수(vector function) : 어떤 점을 하나의 벡터에 대응시키는 함수이다. 

</blockquote>

- 여러 독립변수를 하나의 함수값, 즉 벡터에 대응시키는 함수이다. 

- 예시 

  $$ r(t) = \bigg < f(t), g(t), h(t) \bigg > = f(t)i + g(t)j+h(t)k $$

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

장(field) : 공간에서 위치, 시간 등에 따라 그 성질을 다르게 나타내는 물리량이다. 

</blockquote>

- 공간 내 점의 위치와 시간에 따라 다른 값을 가진다.

- 공간의 모든 점에서 정의되는 물리량이다. 

  - 물리량이므로 스칼라량, 벡터량을 지닌다. 

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

스칼라 장(scalar field) : 공간 내 각 점의 위치, 시간 등에 따라 결정되는 크기를 갖는 스칼라를 나타내는 분포이다.

</blockquote>

- 즉 공간 내 각 점에 물리적으로 스칼라 값을 대응시키는 스칼라 함수이다. 

- 예시 

  대기의 각 점의 온도, 밀도, 압력 

- 예시 

  전하가 있는 공간에서의 전위의 분포 

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

벡터 장(vector field) : 공간 내 각 점의 위치, 시간 등에 따라 결정되는 크기와 방향을 갖는 벡터를 나타내는 분포이다. 

</blockquote>

- 예시 

  속도장, 역장(力場)은 크기 뿐만 아니라 방향을 가지므로 벡터장에 해당한다. 

  - 속도장은 각 점에서 속도 벡터를 대응시킨 것으로 해류 속도장, 풍속 속도장 등이 있다. 

  - 역장은 각 점에서 힘 벡터를 대응시킨 것으로써 중력장, 전기장, 자기장 등이 있다.

    - 일례로 중력장은 중력이 미치는 공간 내 각 점에 중력 벡터를 대응시킨 벡터 함수이다. 

## <a name="여러가지 벡터 " href="#여러가지 벡터 ">여러가지 벡터 </a>

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

영벡터(zero vector) : 임의의 점 $A$ 에 대하여 $\overrightarrow{AA}$ 와 같이 시점과 종점이 일치하는 벡터를 영벡터라 한다. 

</blockquote>

- 기호로 $\overrightarrow{0}$ 으로 나타낸다.

- 영벡터는 크기가 $0$ 고 방향은 없다고 정의한다. 

- 실수연산에서 항등원 역할을 한다.

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

역벡터(inverse vector) : 벡터 $\overrightarrow{AB}$ 에 대하여 크기는 같고 방향이 반대인 벡터 $\overrightarrow{BA}$ 를 벡터 $\overrightarrow{AB}$ 의 역벡터라 한다. 

</blockquote>

- $\overrightarrow{AB}$ 역벡터를 $-$ 를 붙혀서 $-\overrightarrow{AB}$ 로 나타낸다.

  $$ \overrightarrow{BA} = -\overrightarrow{AB} $$

- 실수연산에서 역원 역할을 한다.

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

단위벡터(unit vector) : 크기가 $1$ 인 벡터이다. 

</blockquote>

- 실수연산에서 $1$ 의 역할을 한다.

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

평면벡터(plane vector) : 평면에서 정의된 벡터이다. 

</blockquote>

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

공간벡터(space vector) : 공간에서 정의된 벡터이다. 

</blockquote>

## <a name="벡터 대수 " href="#벡터 대수 ">벡터 대수 </a>

실수에서 했던 연산들을 벡터에 대하여 재정의하고 있는 것이다. 

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

벡터의 크기 : 벡터 $\overrightarrow{AB}$ 에서 선분 $AB$ 의 길이를 벡터의 크기라 한다.

</blockquote>

- 형식언어로 $|\overrightarrow{AB}|$ 로 나타낸다. 

- 다음과 같이 벡터의 크기를 시점과 종점이 아닌 단일 문자로 나타낼 수도 있다. 

  $$ |\overrightarrow{a}|, |\overrightarrow{b}|, |\overrightarrow{c}|, \dots $$

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

벡터의 상등 : 시점과 종점의 위치에 관계 없이 두 벡터 $\overrightarrow{a}, \overrightarrow{b}$ 의 크기와 방향이 같으면 두 벡터 $\overrightarrow{a}, \overrightarrow{b}$ 를 같다고 한다.

</blockquote>

- 두 벡터 $\overrightarrow{a}, \overrightarrow{b}$ 가 각각 선분 $\overline{AB}, \overleftrightarrow{CD}$ 로 구성되었을 때 이 둘이 같다는 것을

  $$ \overrightarrow{a} = \overrightarrow{b} \iff \overrightarrow{AB} = \overrightarrow{CD} $$

  로 표현한다. 

- 예시 

  ![unnamed](https://user-images.githubusercontent.com/16812446/79002706-fd62c280-7b8b-11ea-8a50-45ca181784e1.gif)

  위 세 벡터는 같은 방향과 같은 길이를 지니므로 모두 같다.

  즉, 왼쪽부터 차례로 $\overrightarrow{AB}, \overrightarrow{CD}, \overrightarrow{OP}$ 라고 한다면 

  $$ \overrightarrow{AB}= \overrightarrow{CD}= \overrightarrow{OP} $$

  이다. 

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

벡터의 덧셈 : 벡터의 덧셈은 다음 두 경우로 정의된다. 

</blockquote>

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

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

벡터 덧셈의 성질 

임의의 세 벡터 $\overrightarrow{a}, \overrightarrow{b}, \overrightarrow{c}$ 와 영벡터 $\overrightarrow{0}$ 에 대하여 다음이 성립한다.

</blockquote>

- 교환법칙 : $\overrightarrow{a}+\overrightarrow{b}=\overrightarrow{b}+\overrightarrow{a}$

- 결합법칙 : $(\overrightarrow{a}+\overrightarrow{b})+\overrightarrow{c}=\overrightarrow{a}+(\overrightarrow{b}+\overrightarrow{c})$

- 항등원 : $\overrightarrow{a}+\overrightarrow{0}=\overrightarrow{0}+\overrightarrow{a} = \overrightarrow{a}$

- 역원 : $\overrightarrow{a}+(-\overrightarrow{a})=-\overrightarrow{a}+\overrightarrow{a} = \overrightarrow{0}$

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

벡터의 뺄셈 : 두 벡터 $\overrightarrow{OA}, \overrightarrow{OB}$ 에 대하여 $\overrightarrow{a}$ 와 $\overrightarrow{-b}=\overrightarrow{BO}$ 의 합 

$$ \overrightarrow{a}+(-\overrightarrow{b}) = \overrightarrow{OA}+\overrightarrow{BO} = \overrightarrow{BO} + \overrightarrow{OA} = \overrightarrow{BA} $$

를 벡터 $\overrightarrow{a}$ 를 벡터 $\overrightarrow{b}$ 에서 뺀 차라고 한다.

</blockquote>

- 이것을 기호로 다음과 같이 나타낸다. 

  $$ \overrightarrow{a}-\overrightarrow{b}= \overrightarrow{OA} - \overrightarrow{OB} = \overrightarrow{BA} $$ 

- 그림 

  ![](https://i.ytimg.com/vi/kOCTTK3Cnto/maxresdefault.jpg)

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

벡터의 실수배(스칼라배) : 임의의 실수 $k$ 와 벡터 $\overrightarrow{a}$ 의 곱 $k \overrightarrow{a}$ 를 벡터 $\overrightarrow{a}$ 의 실수배라 하고 다음과 같이 정의한다.

</blockquote>

- $\overrightarrow{a} \neq \overrightarrow{0}$ 인 경우 

  - $k>0$ 이면 $k \overrightarrow{a}$ 는 $\overrightarrow{a}$ 와 방향이 같고 크기가 $k |\overrightarrow{a}|$ 인 벡터이다. 

  - $k<0$ 이면 $k \overrightarrow{a}$ 는 $\overrightarrow{a}$ 와 방향이 반대이고 크기가 $|k| |\overrightarrow{a}|$ 인 벡터이다. 

  - $k=0$ 이면 $k \overrightarrow{a} = \overrightarrow{0}$ 이다.

- $\overrightarrow{a} = \overrightarrow{0}$ 인 경우, 실수 $k$ 에 대하여 $k \overrightarrow{a}=\overrightarrow{0}$ 이다. 

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

벡터의 실수배의 성질 : 두 실수 $k, l$ 과 두 벡터 $\overrightarrow{a}, \overrightarrow{b}$ 에 대하여 다음이 성립한다.

</blockquote>

- 벡터의 실수배의 결합법칙 : $k(l \overrightarrow{a}) = (kl)\overrightarrow{a}$

- 벡터의 실수배의 분배법칙 

  $(k+l) \overrightarrow{a} = k\overrightarrow{a}+l \overrightarrow{a}$

  $k(\overrightarrow{a}+\overrightarrow{b}) = k\overrightarrow{a}+k \overrightarrow{b}$

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

두 벡터의 평행조건 : 다음 두 경우에서 두 벡터는 평행한다고 정의한다. 

</blockquote>

- 영벡터가 아닌 두 벡터 $\overrightarrow{a}, \overrightarrow{b}$ 와 $0$ 이 아닌 실수 $k$ 에 대하여 

  $$ \overrightarrow{a}//\overrightarrow{b} \iff \overrightarrow{b} = k \overrightarrow{a} $$

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

세 점이 한 직선 위에 있을 조건 : 서로 다른 세점 $A, B, C$ 가 한 직선 위에 존재하기 위한 필요충분조건은 $0$ 이 아닌 실수 $k$ 에 대하여

$$ \overrightarrow{AC} = k \overrightarrow{AB} $$

이다.

</blockquote>

## <a name="위치벡터 " href="#위치벡터 ">위치벡터 </a>

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

위치벡터 : 평면 또는 공간에서 한 점 $O$ 를 고정할 때 임의의 한 점 $A$ 에 대하여 $O$ 를 시점으로 하고 $A$ 를 종점으로 하는 유일한 벡터 $\overrightarrow{OA}$ 를 점 $O$ 에 대한 점 $A$ 의 위치벡터라 한다. 

</blockquote>

- 점 $O$ 에 대한 점 $A$ 의 위치벡터를 간단하게 점 $A$ 의 위치벡터로 부른다.

- 점 $O$ 의 위치벡터는 $\overrightarrow{0}$ 이다.

- 두 점 $A, B$ 의 위치벡터가 각각 $\overrightarrow{a}, \overrightarrow{b}$ 일 때 

  $$ \overrightarrow{AB} = \overrightarrow{OB} - \overrightarrow{OA} = \overrightarrow{b} - \overrightarrow{a} $$

  이다. 

**구체화 필요**

## <a name="평면벡터 " href="#평면벡터 ">평면벡터 </a>

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

평면벡터 : 위치벡터의 개념을 좌표평면 위로 옮겨서 시점을 원점 $O(0, 0)$ 으로 고정시킨 벡터이다.

</blockquote>

- 종점의 좌표 $2-$튜플을 평면벡터를 대표하는 값으로 삼는다. 

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

평면벡터 성분 표현 : 임의의 평면벡터 $\overrightarrow{a}$ 에 대하여 $\overrightarrow{a} = \overrightarrow{OA}$ 의 종점이 점이 $A(a_1, a_2)$ 일 때, 두 점 $E_1(1, 0), E_2(0, 1)$ 의 위치벡터 $\overrightarrow{e_1}, \overrightarrow{e_2}$ 를 이용하여 벡터 $\overrightarrow{a}$ 를 다음과 같이 나타낼 수 있다. 

$$ \overrightarrow{a} = \overrightarrow{OA} = \overrightarrow{OA_1} + \overrightarrow{OA_2} = a_1\overrightarrow{e_1} + a_2 \overrightarrow{e_2} $$

</blockquote>

- 이때 두 실수 $a_1, a_2$ 를 평면벡터 $\overrightarrow{a}$ 의 성분이라 한다. 

- 또 성분만을 이용해서 평면벡터 $\overrightarrow{a}$ 를 두 수의 순서쌍($2-$튜플)

  $$ \overrightarrow{a} = (a_1,a_2) $$

  로 나타낼 수 있다. 

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

평면벡터의 크기 : $\overrightarrow{a} = (a_1,a_2)$  의 크기는 

$$ |\overrightarrow{a}| = \sqrt[]{a^{2}_{1}+a^{2}_{2}} $$

</blockquote>

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

평면벡터의 같음 : $\overrightarrow{a} = (a_1,a_2),\overrightarrow{b} = (b_1,b_2)$  가 같을 조건은

$$ \overrightarrow{a} = \overrightarrow{b} \iff a_1=b_1, a_2 = b_2 $$

이다. 

</blockquote>

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

평면벡터의 연산 : $\overrightarrow{a} = (a_1,a_2),\overrightarrow{b} = (b_1,b_2)$ 에 대하여

</blockquote>

- 덧셈 : $\overrightarrow{a}+\overrightarrow{b}=(a_1+b_1, a_2+b_2)$

- 뺄셈 : $\overrightarrow{a}-\overrightarrow{b}=(a_1-b_1, a_2-b_2)$

- 실수배 : $k\overrightarrow{a}=(ka_1, ka_2)$

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

두 점에 대한 평면벡터의 성분 : 좌표평면 위의 두 점 $A(a_1,a_2),B(b_1,b_2)$ 에 대하여 

$$ \overrightarrow{AB} = \overrightarrow{OB}-\overrightarrow{OA}=(b_1,a_1, b_2-a_2) $$

이다. 

</blockquote>

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

두 점에 대한 평면벡터의 크기 : 좌표평면 위의 두 점 $A(a_1,a_2),B(b_1,b_2)$ 에 대하여 

$$ |\overrightarrow{AB}| = \sqrt[]{(b_1-a_1)^{2}+(b_2-a_2)^{2}} $$

이다. 

</blockquote>

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

두 평면벡터의 평행 : 영벡터가 아닌 두 평면벡터 $\overrightarrow{a} = (a_1,a_2),\overrightarrow{b} = (b_1,b_2)$ 에 대하여

$$ \overrightarrow{a}//\overrightarrow{b} \iff \overrightarrow{b} = k \overrightarrow{a} \iff \begin{cases} b_1 = ka_1 &\text{}\\ b_2=ka_2 &\text{}\\ \end{cases} $$

</blockquote>

## <a name="공간벡터 " href="#공간벡터 ">공간벡터 </a>

**구체화 필요**

# <a name="벡터 해석학" href="#벡터 해석학">벡터 해석학</a>

과학 공학, 금융, 의학, 더 높은 수준의 수학 같은 현실 세계에서는 일변수 함수가 아닌 다변수 함수가 훨씬 자주 쓰인다. 이 파트는 다변수 함수의 미적분을 소개하기 위한 사전 지식을 가르친다. 

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

표준점(standard poitn) 에 위치한 벡터 : 시점이 원점에 위치한 벡터이다. 

</blockquote>

- 벡터의 속성은 크기와 방향이다. 즉, 위치는 벡터의 속성이 아니다. 이때 벡터를 정확하게 대수적으로 기술하기 위하여 시점을 원점에 위치시킨 다음 종점의 좌표로 벡터를 특정한다.

  - 이것을 표준점에 위치한 벡터라고 한다. 

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

벡터 성분 표기(component form) : $2$ 차원, $3$ 차원일 경우 각각 다음과 같이 정의된다. 

</blockquote>

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

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

벡터의 성분(component) : 벡터 성분 표기에서 $v_1, v_2, v_3$ 을 벡터의 성분이라 한다. 

</blockquote>

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

영 벡터(zero vector) : 길이가 $0$ 인 벡터로써 

$$ \big<0, 0 \big> $$

또는 

$$ \big< 0,0,0 \big > $$

이다. 

</blockquote>

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

$2$ 차원 벡터의 길이(magnitude or length of vector) : $2$ 차원 공간에서 정의된 임의의 벡터 $\overrightarrow{PQ}$ 를 표준점에 위치시켜서 그 성분을

$$ v = \big<x_2-x_1, y_2-y_1\big> $$

로 표기할 수 있다면 벡터의 길이는 

$$ |v| = ||v|| = \sqrt[]{v _{1} ^{2} + v _{2} ^{2} } = \sqrt[]{(x _{2} - x _{1}) ^{2} + (y _{2} - y _{1}) ^{2} } $$

이다. 

</blockquote>

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

$3$ 차원 벡터의 길이(magnitude or length of vector) : $3$ 차원 공간에서 정의된 임의의 벡터 $\overrightarrow{PQ}$ 를 표준점에 위치시켜서 그 성분을

$$ v = \big<x_2-x_1, y_2-y_1, z_2-z_1 \big> $$

로 표기할 수 있다면 벡터의 길이는 

$$ |v| = ||v|| = \sqrt[]{v _{1} ^{2} + v _{2} ^{2} + v _{3} ^{2}} = \sqrt[]{(x _{2} - x _{1}) ^{2} + (y _{2} - y _{1}) ^{2} + (z _{2} - z _{1}) ^{2}} $$

이다. 

</blockquote>

- 벡터 $v$ 의 길이를 $|v|$ 또는 $||v||$ 로 표기한다. 

## <a name="노름 거리" href="#노름 거리">노름 거리</a>

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

$L_1$ 노름(norm) 거리 또는 맨해튼 거리 : 벡터 $a$ 에 대한 $L_1$ 노름은 

$$ ||a|| _{1} = |a_1| + |a_2| + |a_3| + \dots + |a_n| = \sum_{i=1}^{n}|a_i| $$

이다. 

</blockquote>

- 벡터 $a = (4, 3)$ 에 대한 $L_1$ 노름은 오른쪽으로 $4$, 위로 $3$ 움직인 것과 같이 $7$ 이다.

  이처럼 $L_1$ 노름은 

  ![](https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Manhattan_distance.svg/300px-Manhattan_distance.svg.png)

  와 같이 바둑판 모양으로 움직인 최단거리를 뜻한다. 

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

$L_2$ 노름(norm) 거리 또는 유클리드 거리 : 벡터 $a$ 에 대한 $L_2$ 노름은 벡터의 크기에서의 정의와 동일하게 

$$ ||a|| _{2} = \sqrt[]{\sum_{i=1}^{n}a _ i ^{2}} = \sqrt[]{a_1 ^{2}+a_2 ^{2}+\dots+a_n ^{2}} $$

이다.

</blockquote>

- $L_2$ 노름은 유클리드 기하학에서 사용하던 거리와 똑같고 

  우리가 일상생활에서 직관적으로 생각하던 거리와 동일하다!

- $L_1, L_2$ 노름은 선형회귀 모델의 정규화 항에서 사용된다.

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

$L_p$ 노름 : 점 $(x_1, x_2, \dots, x_n)$ 과 점 $(y_1, y_2, \dots, y_n)$ 의 $L_p$ 노름 거리는 다음과 같이 정의된다. 

$$ \Bigg ( \sqrt[]{\sum_{i=1}^{n}|x_i - y_i| ^{p}} \Bigg ) ^{1/p} $$

</blockquote>

- $L_1$ 노름 거리가 

  $$ \sum_{i=1}^{n}|x_i - y_i| ^{p} $$

  로 정의되고 $L_2$ 노름 거리가 

  $$ \Bigg ( \sqrt[]{\sum_{i=1}^{n}|x_i - y_i| ^{2}} \Bigg ) ^{1/2} $$

  로 정의된 것에서 일반화 된 것이다. 

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

무한 $L _{\infty }$ 노름 : 점 $(x_1, x_2, \dots, x_n)$ 과 점 $(y_1, y_2, \dots, y_n)$ 의 $L _{\infty }$ 노름 거리는 다음과 같이 정의된다. 

  $$ \lim_{p \to \infty}  \Bigg ( \sqrt[]{\sum_{i=1}^{n}|x_i - y_i| ^{p}} \Bigg ) ^{1/p} $$

  또는

  $$ = \max (|x_1 -y_1|, |x_2 - y_2|, \dots, |x_n - y_n|) $$

</blockquote>

- 보통 $L_1$ 노름거리과 $L_2$ 노름거리, 무한 노름거리 외에는 잘 사용되지 않는다. 

- 무한노름거리는 체비쇼프 거리(chebyshev distance) 거리로도 불린다. 

## <a name="벡터 대수 연산 " href="#벡터 대수 연산 ">벡터 대수 연산 </a>

(스칼라는 단순히 실수로 생각하면 된다.)

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

벡터 덧셈 : $u = \big <u_1, u_2, u_3 \big >, v = \big < v_1, v_2, v_3 \big >$ 인 벡터 $u, v$ 에 대하여 

$$u + v = \big <u_1+v_1, u_2+v_2 + u_3+v_3 \big >$$

이다.

</blockquote>

- 예시 

  해석기학적인 벡터 덧셈은 논증기하적으로 벡터 덧셈을 정의했을 때와 같이 

  벡터 $u, v$ 를 더해 벡터 $w$ 가 나오는데, 각각

  삼각형의 형태로 덧셈이 이루어지는 경우

  ![캡처](https://user-images.githubusercontent.com/16812446/79008020-73205b80-7b97-11ea-9e2a-b085f47baf47.PNG)

  와 평행사변형의 형태로 덧셈이 이루어지는 경우

  ![캡처](https://user-images.githubusercontent.com/16812446/79008186-c5617c80-7b97-11ea-8f0a-4bba658bd881.PNG)

  와 같다. 

- 특히 위 예시에서 덧셈의 결과인 $w$ 를 합 벡터(resultant vector) 라 한다. 

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

벡터 스칼라배 : $u = \big <u_1, u_2, u_3 \big >, v = \big < v_1, v_2, v_3 \big >$ 인 벡터 $u, v$ 에 대하여 

$$ku = \big <ku_1, ku_2, ku_3 \big >$$

이다.

</blockquote>

- 벡터 $u$ 에 스칼라배를 하면 벡터가 늘어날 수도 있고 줄어들 수도 있다.

- 특히 스칼라 $k$ 가 음수면 벡터의 방향이 바뀐다.

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

스칼라배 벡터의 길이 : 벡터 $u$ 에 스칼라배 $k$ 를 한 벡터 $ku$ 의 길이 $|ku|$ 는 

$$ |ku| = \sqrt[]{(ku_1) ^{2}+(ku_2) ^{2}+(ku_3)^{2}} = \sqrt[]{k ^{2}(u_1 ^{2}+u_2 ^{2}+u_3 ^{2})} = \sqrt[]{k ^{2}}\sqrt[]{u_1 ^{2}+u_2 ^{2}+u_3 ^{2}} = |k||u| $$

이다. 

</blockquote>

- 즉, $ku$ 의 길이는 벡터 $u$ 의 길이에 정확히 $k$ 배한 길이와 같다. 

- 특히 벡터 $u$ 에 $-1$ 스칼라를 곱한 벡터 $-u$ 는 같은 길이에 정반대 방향을 가르킨다.

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

단위 벡터(unit vector) : 길이가 $1$ 인 벡터이다. 

</blockquote>

- 즉 단위 벡터란 벡터

  $$ v = \big<x_2-x_1, y_2-y_1, z_2-z_1 \big> $$

  에 대한 벡터 길이

  $$ |v| = \sqrt[]{(x _{2} - x _{1}) ^{2} + (y _{2} - y _{1}) ^{2} + (z _{2} - z _{1}) ^{2}} = 1 $$

  을 만족하는 모든 벡터를 뜻한다. 

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

표준 단위 벡터(standard unit vector) : 표준 단위 벡터는 길이가 $1$ 인 다음의 특수한 $3$ 가지 경우의 벡터를 뜻한다. 

$$ i = \big <1, 0, 0 \big >, j = \big <0, 1, 0 \big >, k = \big <0, 0, 1 \big > $$

</blockquote>

- 그 어떠한 벡터도 표준 단위 벡터의 선형결합으로 표현될 수 있다. 그러므로 표준 단위 벡터는 모든 벡터를 생성한다. 

  - 예시

    즉, 임의의 벡터 $v = \big <v_1,v_2, v_3 \big >$ 는 다음과 같이 표준 단위 벡터의 선형 결합으로 표현될 수 있다. 

    $$ v = \big <v_1,v_2, v_3 \big > = \big <v_1,0,0\big > + \big <0,v_2,0\big > + \big <0,0,v_3\big > $$

    $$ = v_1\big <1,0,0\big > + v_2\big <0,1,0\big > + v_3\big <0,0,1\big > $$

    $$ = v_1i + v_2j + v_3k $$

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

벡터의 $i$ 성분(i-component) : 표준 단위 벡터의 예시에서 스칼라 $v_1$ 을 벡터 $v$ 의 $i$ 성분이라한다.

</blockquote>

- 즉 $i$ 성분은 $(1, 0, 0)$ 또는 $\big < 1, 0, 0 \big >$ 이다.

- 또 $i$ 벡터를 $x$ 축 상의 단위벡터라고도 한다. 

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

벡터의 $j$ 성분(j-component) : 표준 단위 벡터의 예시에서 스칼라 $v_2$ 을 벡터 $v$ 의 $j$ 성분이라한다.

</blockquote>

- 즉 $j$ 성분은 $(0, 1, 0)$ 또는 $\big < 0, 1, 0 \big >$ 이다.

- 또 $j$ 벡터를 $y$ 축 상의 단위벡터라고도 한다. 

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

벡터의 $k$ 성분(k-component) : 표준 단위 벡터의 예시에서 스칼라 $v_3$ 을 벡터 $v$ 의 $k$ 성분이라한다.

</blockquote>

- 즉 $k$ 성분은 $(0, 0, 1)$ 또는 $\big < 0, 0, 1 \big >$ 이다.

- 또 $k$ 벡터를 $z$ 축 상의 단위벡터라고도 한다. 

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

벡터의 $i,j,k$ 성분으로의 벡터 표기 : 점 $P_1(x_1, y_1, z_1)$ 에서 점 $P_2(x_2, y_2, z_2)$ 으로 이어져있는 벡터는 

$$ \overrightarrow{P_1P_2} = (x_2 - x_1)i + (y_2-y_1)j+(z_2-z_1)k $$

로 표기할 수 있다. 

</blockquote>

- 따라서

  $$ \overrightarrow{P_1P_2} = \big <x_2 - x_1 , y_2-y_1,z_2-z_1 \big >  = (x_2 - x_1)i + (y_2-y_1)j+(z_2-z_1)k $$

  이다.

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

벡터 방향으로의 단위 벡터 : 영벡터가 아닌 벡터 $v \neq 0$ 와 길이 $|v|$ 에 대하여 

$$ \frac{v}{|v|} $$

가 벡터 $v$ 방향으로의 단위 벡터이다. 

</blockquote>

- 증명

  단위 벡터는 어떤 방향이든지 길이가 $1$ 인 벡터인 것을 기억하자.

  그러면 임의의 벡터 $u$ 에 그것의 길이 $|u|$ 의 역수 $|\frac{1}{u}|$ 을 스칼라배 한다면 벡터 $u$ 의 길이는 $1$ 이 된다.

  $$ \because  \bigg | \frac{1}{|v|}v \bigg | = \frac{1}{|v|}|v| = 1 $$

  이기 때문이다. 

  1. $\bigg | \frac{1}{|v|}v \bigg |$ 는 벡터 $v$ 에 스칼라배 $\frac{1}{|v|}$ 를 한 길이를 뜻한다.

      - 기호 $||$ 의 의미를 기억하자!

  2. 그리고 임의의 벡터 $u$ 에 스칼라배 $k$ 를 한 벡터 $ku$ 의 길이 $|ku|$ 는 

      $$ |ku| = |k||u| $$

      임을 기억하자. 이 정리에서

      $$ k = \frac{1}{|v|}, u = v $$

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

## <a name="내적, 외적" href="#내적, 외적">내적, 외적</a>

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

내적(inner product) : 두 벡터 $u ,v$ 가 $u = \big < u_1, u_2, u_3 \big >, v = \big  <v_1, v_2, v_3 \big  >$ 일 때, 두 벡터 $u, v$ 의 내적은 스칼라

$$ u \cdot v = u_1v_1+u_2v_2+u_3v_3 $$

이다. 

</blockquote>

- 내적은 두 벡터 $u, v$ 가 이루는 각에 대한 관계식

  $$ \theta = \cos ^{-1} \bigg ( \frac{u \cdot v}{|u||v|} \bigg ) $$

  을 이용하여 두 벡터의 각이 $\theta$ 일 때 

  $$ u \cdot v = |u||v| \cos \theta $$

  으로 정의할 수도 있다. 

  - 증명  

    $$ \theta = \cos ^{-1} \bigg ( \frac{u \cdot v}{|u||v|} \bigg ) $$

    에서 

    $$ \cos \theta = \frac{u \cdot v}{|u||v|} $$

    이므로

    $$ \therefore  u \cdot v = |u||v| \cos \theta $$

    이다.

- 내적은 두 벡터

  $$ a = \begin{bmatrix} a_1\\a_2\\\vdots \\a_n \end{bmatrix}, b = \begin{bmatrix} b_1\\b_2\\\vdots \\b_n \end{bmatrix} $$

  에 대하여 

  $$ \big< a, b \big > = a_1b_1 + a_2b_2 + \dots + a_n b_n = \sum_{i=1}^{n}a_ib_i $$

  로 표기할 수도 있다. 

  - $\big < \big >$ 기호를 벡터 표기가 아닌 내적 표기로 사용할 수도 있다는 것에 주의하자. 

- 점곱(dot product), 스칼라곱(scalar product), 영사곱(projection product) 으로도 불린다. 

- 예시 

  $$ \big < 1, -2, 1\big > \cdot \big < -6, 2, -3\big > = (1)(-6)+(-2)(2)+(-1)(-3) = -7 $$

- 예시 

  $$ \bigg ( \frac{1}{2}i + 3j + k \bigg ) \cdot (4i-j+2k) = \bigg (\frac{1}{2}\bigg )(4)+(3)(-1)+(1)(2) = 1 $$

- 예시 

  $$ a = \begin{bmatrix} 1\\2\\3 \end{bmatrix}, b=\begin{bmatrix} 4\\5\\6 \end{bmatrix} $$

  에 대한 내적은

  $$ \big < a, b \big > = (1)(4)+(2)(5)+(3)(6)=4+10+18=32 $$

  이다. 

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

내적의 성질 : 임의의 벡터 $u, v, w$ 와 스칼라 $c$ 에 대하여 다음이 성립한다. 

1. $u \cdot v = v \cdot u$

2. $(cu)\cdot v = u \cdot (cv) = c(u \cdot v)$

3. $u \cdot (v + w) = u \cdot v + u \cdot w$

4. $u \cdot u = |u| ^{2}$

5. $0 \cdot u = 0$

</blockquote>

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

두 벡터의 각도(angle between two vectors) : 영벡터가 아닌 두 벡터 $u, v$ 가 $u = \big < u_1, u_2, u_3 \big >, v = \big  <v_1, v_2, v_3 \big  >$ 일 때, 두 벡터 $u ,v$ 가 이루는 각 $\theta$ 는 

$$ \theta = \cos ^{-1} \bigg ( \frac{u \cdot v}{|u||v|} \bigg ) $$

또는

$$ \theta = \cos ^{-1} \bigg ( \frac{u_1v_1+u_2v_2+u_3v_3}{|u||v|} \bigg ) $$

이다. 

</blockquote>

- 증명 

  **구체화 필요** 

- 예시 

  두 벡터 

  $$ u = i - 2j - 2k, v = 6i + 3j + 2k $$

  가 이루는 각을 구해보자.

  $$ u \cdot v = (1)(6)+(-2)(3)+(-2)(2) = -4 $$

  $$ |u| = \sqrt[]{(1)^{2}+(-2)^{2}+(-2)^{2}} = \sqrt[]{9} = 3 $$

  $$ |v| = \sqrt[]{(6)^{2}+(3)^{2}+(2)^{2}} = \sqrt[]{49} = 7 $$

  에서 

  $$ \theta = \cos ^{-1} \bigg ( \frac{u \cdot v}{|u||v|} \bigg ) = \cos ^{-1} \bigg ( \frac{-4}{(3)(7)} \bigg ) \approx 100.98 \degree $$

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

코사인 유사도(cosine similarity) : 영벡터가 아닌 두 벡터 $u, v$ 가 $u = \big < u_1, u_2, \dots, u_n \big >, v = \big  <v_1, v_2, \dots, v_n \big  >$ 일 때, 

$$ \cos  \theta = \frac{u \cdot v}{|u||v|} $$

또는 

$$ \cos  (u, v) = \frac{u \cdot v}{|u||v|} $$

를 코사인 유사도라고 정의한다.

</blockquote>

- 증명 

  코사인 유사도

  $$ \cos  \theta = \frac{u \cdot v}{|u||v|} $$

  는 두 벡터의 각도

  $$ \theta = \cos ^{-1} \bigg ( \frac{u \cdot v}{|u||v|} \bigg ) $$

  에서 

  $$ \therefore  \cos \theta = \frac{u \cdot v}{|u||v|} $$

  와 같이 쉽게 유도된다. 

- 다음의 기호로도 표기할 수 있다. 

  $$ \cos \theta = \frac{\big < u ,v \big >}{||u|| \cdot  ||v||} = \frac{ \displaystyle \sum_{i=1}^{n}a_ib_i}{ \displaystyle \sqrt[]{\sum_{i=1}^{n}a_i ^{2}} \sqrt[]{\sum_{i=1}^{n}b_i ^{2}}} $$

- 코사인 유사도는 폐구간 $[-1, 1]$ 에 존재한다. 

  즉 $-1 \leq \cos (u, v) \leq 1$ 이다.

  - 코사인 유사도가 $-1$ 일 때 두 벡터가 서로 반대방향이다.

  - 코사인 유사도가 $0$ 일 때 두 벡터가 직교한다.

  - 코사인 유사도가 $1$ 일 때 두 벡터가 서로 같은 방향으로 평행이 된다. 

- 이와 같이 코사인 유사도가 높다는 것은 두 벡터가 더 비슷하다는 것이다. 

  > 인공지능이 자연어를 처리할 때 단어와 문장을 벡터로 처리하는데 벡터로 환원된 단어와 문장의 관계성을 파악할 때 코사인 유사도가 사용된다. 코사인 유사도가 높을수록 해당 단어와 문장이 더 가까운 관계라는 것이다. 

  > 벡터 해석학으로 격하된 자연대상은 벡터 해석학의 법칙에 순응하기 때문이다. 

  > 이것은 수학 사상사에서 배웠던 수학적 추상대상물로 환원된 자연대상을 수학의 추상 법칙으로 다룰 수 있다는 것의 논거 및 개별 대상이 될 수 있다. 

- 예시 

  두 벡터 $a = (1, 2, 3), b = (6, 5, 4)$ 의 코사인 유사도를 구해보자. 

  $$ a \cdot b = (1)(6)+(2)(5)+(3)(4) = 28 $$

  $$ |a| = \sqrt[]{1^2+2^2+3^2} = \sqrt[]{14} $$

  $$ |b| = \sqrt[]{6^2+5^2+4^2} = \sqrt[]{77} $$

  이므로 코사인 유사도 $\cos (a, b)$ 는

  $$ \therefore \cos (a, b) = \frac{28}{\sqrt[]{14} \sqrt[]{77}} = \frac{2 \sqrt[]{22}}{11} \approx 0.8528 $$

  이다. 

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

벡터의 직교(orthogonal vectors) : 두 벡터 $u, v$ 가 직교하는 조건은

$$ u \cdot v = 0 $$

이다. 

</blockquote>

- 두 벡터가 이루는 각이 $90 \degree$ 일 때 직교한다고 한다. 

- 증명 

  $$ \cos \bigg ( \frac{\pi }{2} \bigg ) = 0 $$

  $$ \cos ^{-1} 0 = \frac{\pi }{2} $$

  이므로 벡터 $u, v$ 가 이루는 각이 $90 \degree = \dfrac{\pi }{2}$ 라면

  $$ \theta = \cos ^{-1} \bigg ( \frac{u \cdot v}{|u||v|} \bigg ) $$

  에서 

  $$ \frac{\pi }{2}  = \cos ^{-1} 0 = \cos ^{-1} \bigg ( \frac{u \cdot v}{|u||v|} \bigg ) $$

  $$ 0 = \frac{u \cdot v}{|u||v|} $$

  이다. 그러므로

  $$ \therefore u \cdot v = 0 $$

  이다. 

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

외적(outer product) : 벡터 $u, v$ 가 이루는 각이 $\theta$ 이고 벡터 $u, v$ 가 이루는 평면에 수직한 단위 벡터 $n$ 에 대하여 

벡터 $u, v$ 의 외적은 벡터 

$$ u \times v = (|u||v| \sin \theta) n $$

이다. 

</blockquote>

- 교차곱(cross product), 벡터곱(vector product), 텐서곱(tensor product) 으로도 불린다. 

- 내적의 결과가 스칼라인 반면 외적의 결과는 벡터이다. 

  - 이로 인해 외적은 벡터곱(vector product) 이라고 불리기도 한다. 

- 벡터의 외적 $u \times v$ 는 $u, v$ 에 직교(orthogonal) 한다. 

  ![](https://www.sharetechnote.com/image/EngMath_Matrix_CrossProduct_01.png)

  - 왜냐하면 위 그림과같이 외적이란 벡터 $n$ 의 스칼라배에 불과하기 때문이다. 

  - 위 그림의 빨간선이 벡터 $u, v$ 가 이루는 평면에 직교하는 단위벡터 $n$ 이다! 

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

외적의 성질 : 임의의 벡터 $u, v, w$ 와 임의의 스칼라 $r, s$ 에 대하여 다음이 성립한다. 

1. $(ru) \times (sv) = (rs)(u \times v)$

2. $u \times (v + w) = u \times v + u \times w$

3. $v \times u = -(u \times v)$

4. $(v+w)\times u = v \times u + w \times u$

5. $0 \times u=0$

6. $u \times (v \times w) = (u \cdot w)v - (u \cdot v)w$

</blockquote>

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

외적의 크기 : 벡터 $u, v$ 의 외적의 크기는 

$$ |u \times v| = |u||v| \sin \theta $$

이다. 

</blockquote>

- 증명 

  외적의 정의

  $$ u \times v = (|u||v| \sin \theta) n $$

  에서 $n$ 은 단위벡터이므로 크기가 $1$ 이다. 따라서 외적의 크기는 

  $$ |u \times v| = |u||v| |\sin \theta| |n| $$

  에서

  $$ \therefore  |u \times v| = |u||v| \sin \theta $$

  이다. 

- 외적의 크기는 벡터 $u, v$ 가 이루는 평행사변형(parallogram)의 크기와 같다. 

  - 증명 

    평행사변형의 밑변이 $|u|$ 이 되고 높이가 $|v||\sin \theta|$ 가 되므로 외적의 크기 

    $$ |u \times v| = |u||v| \sin \theta $$

    는 두 벡터 $u, v$ 가 이루는 평행사변형의 넓이와 같다. 

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

평행 벡터(parallel vectors) : 두 벡터 $u, v$ 가 평행인 것은

$$ u \times v = 0 $$

와 동치이다. 

</blockquote>

- 증명 

  $\sin \theta$ 에서 $\theta$ 가 $0, \pi$ 일 때 $0$ 이므로 두 벡터 $u, v$ 가 평행할 때 

  $$u \times v = 0$$

  이다. 이것의 역도 성립한다.

  - 두 벡터 $u, v$ 중 하나가 영벡터라면 역시 

    $$u \times v = 0$$

    이다.

- 즉 $u \times v = 0$ 은 평행일 필요충분조건이다. 

- 형식언어로

  $$ u // v \iff u \times v $$

  로 표현할 수 있다. 




