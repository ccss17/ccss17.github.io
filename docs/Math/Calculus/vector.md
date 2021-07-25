# 매개변수 방정식 

곡선을 두 독립변수 $x, y$ 로 나타내는 것이 아니라 매개변수를 통한 방정식으로 나타내면 훨씬 더 일반적인 곡선을 표현할 수 있다. 

!!! tldr ""

    매개변수 방정식(parametric equations) : $x, y$ 가 각각 구간 $I$ 의 $t$ 에 대한 함수 
    
    $$ x = f(t), y = g(t) $$
    
    일 때, 위 방정식을 곡선의 매개변수 방정식이라 한다.

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

!!! tldr ""

    매개변수 곡선(parametric curve) : 매개변수 방정식의 정의에서 매개변수 방정식으로 정의된 점들의 집합 $(x, y) = (f(t), g(t))$ 을 매개변수 곡선이라 한다.

!!! tldr ""

    매개변수 구간(parametric interval) : 매개변수 방정식의 정의에서 정의역 $I$ 를 매개변수 구간이라 한다.

!!! tldr ""

    시점(initial point) : 매개변수 방정식의 정의에서 $I$ 가 폐구간이고 $t$ 가 $a \leq t \leq b$ 로 정의되었을 때 점 $(f(a), g(a))$ 를 곡선의 시점이라 한다.

!!! tldr ""

    종점(terminal point) : 매개변수 방정식의 정의에서 $I$ 가 폐구간이고 $t$ 가 $a \leq t \leq b$ 로 정의되었을 때 점 $(f(b), g(b))$ 를 곡선의 종점이라 한다.

# 벡터

!!! tldr ""

    평행이동 사상 : 좌표공간 $\mathbb{R} ^{n}$ 의 한 점 $v$ 에 대한 함수 
    
    $$ T _{v}: \mathbb{R} ^{n} \to \mathbb{R} ^{n}, T _{v}(X) := X+v $$
    
    이다.

- 일반적으로 두 점 $v, w \in \mathbb{R} ^{n}$ 에 대한 평행이동 $T _{v}, T _{w}$ 의 합성은 평행이동이고,

    $$ T _{v} \circ T _{w} = T _{v+w} = T _{w} \circ T _{v} $$

    가 성립한다.

- 원점 $O$ 에 대한 평행이동 $T _{O}$ 은 항등사상 $id: \mathbb{R} ^{n}\to \mathbb{R} ^{n}$ 와 같다.

- $T _{-v} = T _{v} ^{-1}$ 이다.

- 예시 

    좌표평면에서 사상 

    $$ (x,y) \mapsto (x+1, y+2) $$

    은 각 점을 오른쪽으로 $1$, 위쪽으로 $2$ 만큼 평행이동시키는 사상이다.

!!! tldr ""

    양 : 어떤 물체의 크기이다.

- 측정 가능한 양(물리량)과 측정 불가능한 양(비물리량)으로 나눌 수 있다.

!!! tldr ""

    물리량 : 측정 가능한 양이다.

- 벡터와 스칼라로 나눌 수 있다.

!!! tldr ""

    비물리량 : 측정 불가능한 양이다.

- 예시 

    "$A$ 의 키는 $180$ cm 이다." 에서 $180$ cm 의 키는 측정 가능한 물리량이다.

    반면 "$A$ 가 $B$ 보다 더 리더십이 있다." 에서 리더십의 비교는 측정이 불가능한 비물리량이다. 

    > 그러나 리더십이라는 대상에 대한 단순화 및 집합으로의 환원을 거쳐서 측정하능하게 만들 수 있다는 가능성을 볼 수 있다. 여기에서 더 나아가 철학적 관념 또한 단순화와 수학적 모델링을 거쳐서 측정가능한 수로 격하시킬 수 있는 가능성도 엿볼 수 있다.

!!! tldr ""

    평행이동 : 좌표공간, 즉 데카르트 공간 $\mathbb{R} ^{n}$ 의 한 점 $v$ 과 임의의 점 $X$ 에 대하여 함수
    
    $$ T_v : \mathbb{R} ^{n} \to \mathbb{R} ^{n}, T_v(X) := X+v $$
    
    를 $v$ 만큼 평행이동하는 사상이라고 한다.

- 예시 

    좌표평면에서 사상

    $$ (x, y) \mapsto (x+1, y+2) $$

    은 각 점들을 오른쪽으로 $1$, 위쪽으로 $2$ 만큼 평행이동하는 사상이다.

!!! tldr ""

    스칼라(scala) : 크기만 있고 방향성이 없는 물리량이다.

- 길이, 넓이, 부피 등이 스칼라량에 속한다. 

- 그냥 단순히 실수로 생각하면 된다! 

- 예시 

    "$A$ 는 $20$ 분을 뛰었다" 에서 $20$ 은 스칼라량이다.

!!! tldr ""

    벡터(vector) 또는 유향선분(directed segment) : 유클리드 공간 속 두 점 $A,B$ 를 잇는 유향선분 
    
    $$ \overrightarrow{AB} $$
    
    이다.

- 크기와 방향성이 있는 자연대상을 수학적 추상대상물로 추상화한 것으로 볼 수 있을 것 같다. 

    데카르트가 점들을 대수화했듯이 라그랑주가 힘, 속도, 가속도 등을 벡터로 대수화한 것이다.
  
- $A$ 를 시점, $B$ 를 종점이라 한다.

- 평행이동 사상 $T$ 는 점들을 이동시킬 뿐 아니라 유향선분도 이동시킨다. 즉,

    $$ T(A)=A', T(B)=B' $$

    이면,

    $$ T(\overrightarrow{AB})=\overrightarrow{A'B'} $$

    이다.

    - 만약 유향선분 $\overrightarrow{AB}$ 를 평행이동하여 유향선분 $\overrightarrow{A'B'}$ 를 얻으면 두 유향선분을 동등하다고 하고,

        $$ \overrightarrow{AB} \equiv \overrightarrow{A'B'} $$

        라고 쓴다.

- 서로 동등한 유향선분을 대표하는 것을 벡터(vector) 로 정의하는 의견도 있다.

    - 즉, 유향선분은 시점과 종점을 가진 방향성이 있는 선분이다. 하지만 벡터는 그 모든 선분을 대표하는 추상대상물인 것이다.

        이 정의에 의하면 벡터를 시점을 원점 $(0, 0)$ 으로 하는 유향선분으로 이해해야 하지만, 시점과 종점은 존재하지 않는다.

    - 이 정의에 의하면 임의의 유향선분은 원점을 시점으로 하는 유향선분과 동등하기 때문에, 벡터 전체 집합은 원점을 시점으로 하는 유향선분 전체의 집합과 같다. 

    - 원점을 시점으로 한 유향선분의 종점은 $\mathbb{R} ^{n}$ 의 한 점이므로, $\mathbb{R} ^{n}$ 의 한 점을 벡터로 볼 수 있다.

        즉, $\mathbb{R} ^{n}$ 의 벡터의 전체 집합은 $\mathbb{R} ^{n}$ 과 일대일 대응이다.
    
    - 이 관점에서 유향선분 $\overrightarrow{AB}$ 가 표현하는 벡터는 점 $B-A$ 에 대응된다.

- 다음과 같이 점 $A$ 에서 점 $B$ 로 방향이 주어진 선분 $AB$ 를 벡터 $AB$ 라 한다.

    ![](https://t1.daumcdn.net/cfile/tistory/267BE245539F79880C)

    - 이것을 형식언어로 $\overrightarrow{AB}$ 로 표현한다. 

- 다음과 같이 벡터를 시점과 종점이 아닌 단일 문자로 나타낼 수도 있다. 

    $$ \overrightarrow{a}, \overrightarrow{b}, \overrightarrow{c}, \dots $$

- **벡터는 행렬과 같이 수와 다른 개념이므로 행렬에서처럼 연산법칙, 항등원, 역원, 단위(수에서 $1$) 등을 새로 정의해야 한다.**

- 크기와 방향성이 동시에 있는 물리량이다. 

    > 크기와 방향성이 있는 자연대상을 수학적 추상대상물로 추상화한 것으로 볼 수 있을 것 같다. 

    - 스칼라량으로는 방향에 대한 정보가 부족하기에 방향에 대한 정보를 덧붙힌 것이 벡터이다. 

        그래서 방향성이 있는 선분 "유향선분" 이라고도 부른다.

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

!!! tldr ""

    벡터의 시점(initial point) : 다음과 같이 점 $A$ 에서 점 $B$ 로 방향이 주어진 선분 $AB$ 를 벡터 $AB$ 에서
    
    ![](https://t1.daumcdn.net/cfile/tistory/267BE245539F79880C)
    
    점 $A$ 를 벡터의 시점이라 한다.

!!! tldr ""

    벡터의 종점(terminal point) : 다음과 같이 점 $A$ 에서 점 $B$ 로 방향이 주어진 선분 $AB$ 를 벡터 $AB$ 에서
    
    ![](https://t1.daumcdn.net/cfile/tistory/267BE245539F79880C)
    
    점 $B$ 를 벡터의 종점이라 한다.

!!! tldr ""

    스칼라 함수(scalar function) : 실숫값 함수와 같이 어떤 점을 하나의 스칼라에 대응시키는 함수이다.

- 즉 여러 독립변수에 대응하는 하나의 함수 값이 스칼라가 된다. 

- 지금까지 살펴본 함수들이 스칼라 함수에 해당한다. 

- 실숫값 함수의 정의처럼 공역이 실수 집합 $\mathbb{R}$ 인 함수 

    $$ f: X \to \mathbb{R} $$

    이다. 

- 예시 

    $$ y = x ^{2}, y = \sin x, y = \ln x \dots $$

!!! tldr ""

    벡터 함수(vector function) : 어떤 점을 하나의 벡터에 대응시키는 함수이다.

- 여러 독립변수를 하나의 함수값, 즉 벡터에 대응시키는 함수이다. 

- 예시 

    $$ r(t) = \bigg < f(t), g(t), h(t) \bigg > = f(t)i + g(t)j+h(t)k $$

!!! tldr ""

    장(field) : 공간에서 위치, 시간 등에 따라 그 성질을 다르게 나타내는 물리량이다.

- 공간 내 점의 위치와 시간에 따라 다른 값을 가진다.

- 공간의 모든 점에서 정의되는 물리량이다. 

    - 물리량이므로 스칼라량, 벡터량을 지닌다.

!!! tldr ""

    스칼라 장(scalar field) : 공간 내 각 점의 위치, 시간 등에 따라 결정되는 크기를 갖는 스칼라를 나타내는 분포이다.

- 즉 공간 내 각 점에 물리적으로 스칼라 값을 대응시키는 스칼라 함수이다. 

- 예시 

    대기의 각 점의 온도, 밀도, 압력 

- 예시 

    전하가 있는 공간에서의 전위의 분포

!!! tldr ""

    벡터 장(vector field) : 공간 내 각 점의 위치, 시간 등에 따라 결정되는 크기와 방향을 갖는 벡터를 나타내는 분포이다.

- 예시 

    속도장, 역장(力場)은 크기 뿐만 아니라 방향을 가지므로 벡터장에 해당한다. 

    - 속도장은 각 점에서 속도 벡터를 대응시킨 것으로 해류 속도장, 풍속 속도장 등이 있다. 

    - 역장은 각 점에서 힘 벡터를 대응시킨 것으로써 중력장, 전기장, 자기장 등이 있다.

        - 일례로 중력장은 중력이 미치는 공간 내 각 점에 중력 벡터를 대응시킨 벡터 함수이다. 

## 여러가지 벡터

!!! tldr ""

    영벡터(zero vector) : 임의의 점 $A$ 에 대하여 $\overrightarrow{AA}$ 와 같이 시점과 종점이 일치하는 벡터를 영벡터라 한다.

- 기호로 $\overrightarrow{0}$ 으로 나타낸다.

- 영벡터는 크기가 $0$ 고 방향은 없다고 정의한다. 

- 실수연산에서 항등원 역할을 한다.

!!! tldr ""

    역벡터(inverse vector) : 벡터 $\overrightarrow{AB}$ 에 대하여 크기는 같고 방향이 반대인 벡터 $\overrightarrow{BA}$ 를 벡터 $\overrightarrow{AB}$ 의 역벡터라 한다.

- $\overrightarrow{AB}$ 역벡터를 $-$ 를 붙혀서 $-\overrightarrow{AB}$ 로 나타낸다.

    $$ \overrightarrow{BA} = -\overrightarrow{AB} $$

- 실수연산에서 역원 역할을 한다.

- 예시

    $\overrightarrow{a}+\overrightarrow{-a} = \overrightarrow{0}$

!!! tldr ""

    단위벡터(unit vector) : 크기가 $1$ 인 벡터이다.

- 실수연산에서 $1$ 의 역할을 한다.

!!! tldr ""

    평면벡터(plane vector) : 평면에서 정의된 벡터이다.



!!! tldr ""

    공간벡터(space vector) : 공간에서 정의된 벡터이다.

## 벡터 대수 

실수에서 했던 연산들을 벡터에 대하여 재정의하고 있는 것이다.

!!! tldr ""

    벡터의 크기 : 벡터 $\overrightarrow{AB}$ 에서 선분 $AB$ 의 길이를 벡터의 크기라 한다.

- 형식언어로 $|\overrightarrow{AB}|$ 로 나타낸다. 

- 다음과 같이 벡터의 크기를 시점과 종점이 아닌 단일 문자로 나타낼 수도 있다. 

    $$ |\overrightarrow{a}|, |\overrightarrow{b}|, |\overrightarrow{c}|, \dots $$

!!! tldr ""

    벡터의 상등 : 두 벡터 $\overrightarrow{AB}, \overrightarrow{CD}$ 에 대하여 한 벡터를 평행이동 사상하여 다른 벡터를 얻을 수 있으면,
    
    두 벡터가 동등하다고 한다.

- 시점과 종점의 위치에 관계 없이 두 벡터 $\overrightarrow{a}, \overrightarrow{b}$ 의 크기와 방향이 같으면 두 벡터 $\overrightarrow{a}, \overrightarrow{b}$ 를 같다고 한다.

- 두 벡터 $\overrightarrow{a}, \overrightarrow{b}$ 가 각각 선분 $\overline{AB}, \overleftrightarrow{CD}$ 로 구성되었을 때 이 둘이 같다는 것을

    $$ \overrightarrow{a} \equiv \overrightarrow{b} \iff \overrightarrow{AB} \equiv \overrightarrow{CD} $$

    로 표현한다. 

- 예시 

    ![unnamed](https://user-images.githubusercontent.com/16812446/79002706-fd62c280-7b8b-11ea-8a50-45ca181784e1.gif)

    위 세 벡터는 같은 방향과 같은 길이를 지니므로 모두 같다.

    즉, 왼쪽부터 차례로 $\overrightarrow{AB}, \overrightarrow{CD}, \overrightarrow{OP}$ 라고 한다면 

    $$ \overrightarrow{AB} \equiv \overrightarrow{CD} \equiv \overrightarrow{OP} $$

    이다.

!!! tldr ""

    벡터의 덧셈 : 벡터의 덧셈은 다음 두 경우로 정의된다.

- 삼각형에서의 덧셈 : 두 벡터 $\overrightarrow{u} = \overrightarrow{AB}, \overrightarrow{v} = \overrightarrow{BC}$ 에 대하여 벡터 $\overrightarrow{w} = \overrightarrow{AC}$ 를 두 벡터 $\overrightarrow{u}, \overrightarrow{v}$ 의 합이라 한다.

    - 이것을 기호로 다음과 같이 나타낸다. 

        $$ \overrightarrow{u}+\overrightarrow{v}= \overrightarrow{AB} + \overrightarrow{BC} = \overrightarrow{AC} = \overrightarrow{w} $$ 

    - 그림

        ![캡처](https://user-images.githubusercontent.com/16812446/77826567-90930580-7153-11ea-98d2-da447edd015a.PNG)

- 평행사변형에서의 덧셈 : 두 벡터 $\overrightarrow{a} = \overrightarrow{AB}, \overrightarrow{b} = \overrightarrow{AC}$ 에 대하여 평행사변형 $ABDC$ 를 만들 때, 벡터 $\overrightarrow{AD}$ 를 두 벡터 $\overrightarrow{a}, \overrightarrow{b}$ 의 합이라 한다.

    - 이것을 기호로 다음과 같이 나타낸다. 

        $$ \overrightarrow{a}+\overrightarrow{b}= \overrightarrow{AB} + \overrightarrow{AC} = \overrightarrow{AD} $$ 

    - **하지만 정말 벡터의 덧셈이 이 두 가지 경우로 따로 정의된 것이 아니다. 실제로 삼각형에서의 덧셈과 평행사변형에서의 덧셈은 본질적으로 동일하다.**

        ![](https://i.ytimg.com/vi/gdWfqihMW14/maxresdefault.jpg)

        왜냐하면 위 그림에서 벡터 $\overrightarrow{AC}$ 를 벡터 $\overrightarrow{BD}$ 로 옮겨도 두 벡터가 방향과 크기가 같으므로 동일하기 때문이다. 그러므로 평행사변형에서의 덧셈도 결국 삼각형에서의 덧셈 $\overrightarrow{AB} + \overrightarrow{BD} = \overrightarrow{AD}$ 으로 변환할 수 있다.

        마찬가지의 방법으로 삼각형에서의 덧셈도 평행사변형에서의 덧셈으로 변환할 수 있다. 

- 임의의 세 벡터 $\overrightarrow{a}, \overrightarrow{b}, \overrightarrow{c}$ 와 영벡터 $\overrightarrow{0}$ 에 대하여 다음이 성립한다.

    - 교환법칙 : $\overrightarrow{a}+\overrightarrow{b}=\overrightarrow{b}+\overrightarrow{a}$

    - 결합법칙 : $(\overrightarrow{a}+\overrightarrow{b})+\overrightarrow{c}=\overrightarrow{a}+(\overrightarrow{b}+\overrightarrow{c})$

    - 항등원 : $\overrightarrow{a}+\overrightarrow{0}=\overrightarrow{0}+\overrightarrow{a} = \overrightarrow{a}$

    - 역원 : $\overrightarrow{a}+(-\overrightarrow{a})=-\overrightarrow{a}+\overrightarrow{a} = \overrightarrow{0}$

!!! tldr ""

    벡터의 뺄셈 : 두 벡터 $\overrightarrow{OA}, \overrightarrow{OB}$ 에 대하여 $\overrightarrow{a}$ 와 $\overrightarrow{-b}=\overrightarrow{BO}$ 의 합 
    
    $$ \overrightarrow{a}+(-\overrightarrow{b}) = \overrightarrow{OA}+\overrightarrow{BO} = \overrightarrow{BO} + \overrightarrow{OA} = \overrightarrow{BA} $$
    
    를 벡터 $\overrightarrow{a}$ 를 벡터 $\overrightarrow{b}$ 에서 뺀 차라고 한다.

- 이것을 기호로 다음과 같이 나타낸다. 

    $$ \overrightarrow{a}-\overrightarrow{b}= \overrightarrow{OA} - \overrightarrow{OB} = \overrightarrow{BA} $$ 

- 벡터의 뺄셈은 다음 그림으로 설명된다. 즉, 종점과 종점을 이은 벡터가 뺄셈의 결과이다.

    ![](https://i.ytimg.com/vi/kOCTTK3Cnto/maxresdefault.jpg)

    위 그림에서는 $\overrightarrow{OA} - \overrightarrow{OB} = \overrightarrow{BA}$ 의 연산결과를 살펴보았다. 그런데 방향이 다른 벡터를 얻기 위하여

    $$\overrightarrow{OB} - \overrightarrow{OA} = \overrightarrow{AB}$$

    를 연산하면된다.

    - 설명 

        벡터 $\overrightarrow{a}, \overrightarrow{b}$ 뺄셈 $\overrightarrow{a}-\overrightarrow{b}$ 은 벡터 $\overrightarrow{a}$ 와 벡터 $\overrightarrow{b}$ 의 역벡터의 합으로 볼 수 있다. 즉, 

        ![](https://t1.daumcdn.net/cfile/tistory/99845F335A03C4D528)

        > https://waraccc.tistory.com/11

        에서 벡터의 뺄셈 $\overrightarrow{a}-\overrightarrow{b}$ 을 다음과 같이 $\overrightarrow{a}+(-\overrightarrow{b})$ 로 볼 수 있다는 것이다.

        ![](https://t1.daumcdn.net/cfile/tistory/996A6F335A03CBC129)

        > https://waraccc.tistory.com/11

        그러면 벡터의 덧셈은 이미 알고있는대로 다음과 같이 진행된다.

        ![](https://t1.daumcdn.net/cfile/tistory/99454C335A03CC0719)

        > https://waraccc.tistory.com/11

        그런데 벡터는 평행이동 사상이 존재하면 동일한 것이므로 다음과 같이 원래의 벡터 $\overrightarrow{b},\overrightarrow{a}$ 의 종점을 이은 벡터를 뺄셈 결과로 볼 수 있는 것이다.

        ![](https://t1.daumcdn.net/cfile/tistory/998675335A03CC1A06)

        > https://waraccc.tistory.com/11

        마찬가지로 $\overrightarrow{b}-\overrightarrow{a}$ 의 연산결과는 다음과 같은 빨간 벡터가 된다.

        ![](https://t1.daumcdn.net/cfile/tistory/99D4A7335A03CC2C45)

        > https://waraccc.tistory.com/11

!!! tldr ""

    벡터의 실수배(스칼라배) : 임의의 실수 $k$ 와 벡터 $\overrightarrow{a}$ 의 곱 $k \overrightarrow{a}$ 를 벡터 $\overrightarrow{a}$ 의 실수배라 하고 다음과 같이 정의한다.

- $\overrightarrow{a} \neq \overrightarrow{0}$ 인 경우 

    - $k>0$ 이면 $k \overrightarrow{a}$ 는 $\overrightarrow{a}$ 와 방향이 같고 크기가 $k |\overrightarrow{a}|$ 인 벡터이다. 

    - $k<0$ 이면 $k \overrightarrow{a}$ 는 $\overrightarrow{a}$ 와 방향이 반대이고 크기가 $|k| |\overrightarrow{a}|$ 인 벡터이다. 

    - $k=0$ 이면 $k \overrightarrow{a} = \overrightarrow{0}$ 이다.

- $\overrightarrow{a} = \overrightarrow{0}$ 인 경우, 실수 $k$ 에 대하여 $k \overrightarrow{a}=\overrightarrow{0}$ 이다. 

- 벡터의 실수배의 성질 

    두 실수 $k, l$ 과 두 벡터 $\overrightarrow{a}, \overrightarrow{b}$ 에 대하여 다음이 성립한다.

    - 벡터의 실수배의 결합법칙 : $k(l \overrightarrow{a}) = (kl)\overrightarrow{a}$

    - 벡터의 실수배의 분배법칙 

        $(k+l) \overrightarrow{a} = k\overrightarrow{a}+l \overrightarrow{a}$

        $k(\overrightarrow{a}+\overrightarrow{b}) = k\overrightarrow{a}+k \overrightarrow{b}$

!!! tldr ""

    벡터의 평행 : 다음 두 경우에서 두 벡터는 평행한다고 정의한다.

- 영벡터가 아닌 두 벡터 $\overrightarrow{a}, \overrightarrow{b}$ 와 $0$ 이 아닌 실수 $k$ 에 대하여 

    $$ \overrightarrow{a}//\overrightarrow{b} \iff \overrightarrow{b} = k \overrightarrow{a} $$

!!! tldr ""

    세 점이 한 직선 위에 있을 조건 : 서로 다른 세점 $A, B, C$ 가 한 직선 위에 존재하기 위한 필요충분조건은 $0$ 이 아닌 실수 $k$ 에 대하여
    
    $$ \overrightarrow{AC} = k \overrightarrow{AB} $$
    
    이다.

## 위치벡터

!!! tldr ""

    위치벡터 : 원점 $O$ 를 시점으로 하고 임의의 한 점 $A$ 를 종점으로 하는 벡터 $\overrightarrow{OA}$ 를 
    
    점 $O$ 에 대한 점 $A$ 의 위치벡터라 한다.

- 그냥 좌표공간에서 점을 벡터로 이해할 때 그것을 위치벡터라고 부르는 것이다.

- 점 $O$ 에 대한 점 $A$ 의 위치벡터를 간단하게 점 $A$ 의 위치벡터로 부른다.

- 점 $O$ 의 위치벡터는 $\overrightarrow{0}$ 이다.

- 두 점 $A, B$ 의 위치벡터가 각각 $\overrightarrow{a}, \overrightarrow{b}$ 일 때 

    $$ \overrightarrow{AB} = \overrightarrow{OB} - \overrightarrow{OA} = \overrightarrow{b} - \overrightarrow{a} $$

    이다. 

## 평면벡터

!!! tldr ""

    평면벡터 : 위치벡터의 개념을 좌표평면 위로 옮겨서 시점을 원점 $O(0, 0)$ 으로 고정시킨 벡터이다.

- 종점의 좌표 $2-$튜플을 평면벡터를 대표하는 값으로 삼는다. 

- 평면벡터 성분 표현 

    임의의 평면벡터 $\overrightarrow{a}$ 에 대하여 $\overrightarrow{a} = \overrightarrow{OA}$ 의 종점이 점이 $A(a_1, a_2)$ 일 때, 두 점 $E_1(1, 0), E_2(0, 1)$ 의 위치벡터 $\overrightarrow{e_1}, \overrightarrow{e_2}$ 를 이용하여 벡터 $\overrightarrow{a}$ 를 다음과 같이 나타낼 수 있다. 

    $$ \overrightarrow{a} = \overrightarrow{OA} = \overrightarrow{OA_1} + \overrightarrow{OA_2} = a_1\overrightarrow{e_1} + a_2 \overrightarrow{e_2} $$

    - 이때 두 실수 $a_1, a_2$ 를 평면벡터 $\overrightarrow{a}$ 의 성분이라 한다. 

    - 또 성분만을 이용해서 평면벡터 $\overrightarrow{a}$ 를 두 수의 순서쌍($2-$튜플)

        $$ \overrightarrow{a} = (a_1,a_2) $$

        로 나타낼 수 있다.

!!! tldr ""

    평면벡터의 크기 : $\overrightarrow{a} = (a_1,a_2)$  의 크기는 
    
    $$ |\overrightarrow{a}| = \sqrt[]{a^{2}_{1}+a^{2}_{2}} $$



!!! tldr ""

    평면벡터의 같음 : $\overrightarrow{a} = (a_1,a_2),\overrightarrow{b} = (b_1,b_2)$  가 같을 조건은
    
    $$ \overrightarrow{a} = \overrightarrow{b} \iff a_1=b_1, a_2 = b_2 $$
    
    이다.



!!! tldr ""

    평면벡터의 연산 : $\overrightarrow{a} = (a_1,a_2),\overrightarrow{b} = (b_1,b_2)$ 에 대하여

- 덧셈 : $\overrightarrow{a}+\overrightarrow{b}=(a_1+b_1, a_2+b_2)$

- 뺄셈 : $\overrightarrow{a}-\overrightarrow{b}=(a_1-b_1, a_2-b_2)$

- 실수배 : $k\overrightarrow{a}=(ka_1, ka_2)$

!!! tldr ""

    두 점에 대한 평면벡터의 성분 : 좌표평면 위의 두 점 $A(a_1,a_2),B(b_1,b_2)$ 에 대하여 
    
    $$ \overrightarrow{AB} = \overrightarrow{OB}-\overrightarrow{OA}=(b_1,a_1, b_2-a_2) $$
    
    이다.



!!! tldr ""

    두 점에 대한 평면벡터의 크기 : 좌표평면 위의 두 점 $A(a_1,a_2),B(b_1,b_2)$ 에 대하여 
    
    $$ |\overrightarrow{AB}| = \sqrt[]{(b_1-a_1)^{2}+(b_2-a_2)^{2}} $$
    
    이다.



!!! tldr ""

    두 평면벡터의 평행 : 영벡터가 아닌 두 평면벡터 $\overrightarrow{a} = (a_1,a_2),\overrightarrow{b} = (b_1,b_2)$ 에 대하여
    
    $$ \overrightarrow{a}//\overrightarrow{b} \iff \overrightarrow{b} = k \overrightarrow{a} \iff \begin{cases} b_1 = ka_1 &\text{}\\ b_2=ka_2 &\text{}\\ \end{cases} $$

## 공간벡터 

**구체화 필요**

# 벡터 해석학

과학 공학, 금융, 의학, 더 높은 수준의 수학 같은 현실 세계에서는 일변수 함수가 아닌 다변수 함수가 훨씬 자주 쓰인다. 이 파트는 다변수 함수의 미적분을 소개하기 위한 사전 지식을 가르친다.

!!! tldr ""

    표준점(standard point) 에 위치한 벡터 : 시점이 원점에 위치한 벡터이다.

- 벡터의 속성은 크기와 방향이다. 즉, 위치는 벡터의 속성이 아니다. 이때 벡터를 정확하게 대수적으로 기술하기 위하여 시점을 원점에 위치시킨 다음 종점의 좌표로 벡터를 특정한다.

    - 이것을 표준점에 위치한 벡터라고 한다.

!!! tldr ""

    벡터 성분 표기(component form) : $2$ 차원, $3$ 차원일 경우 각각 다음과 같이 정의된다.

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

!!! tldr ""

    벡터의 성분(component) : 벡터 성분 표기에서 $v_1, v_2, v_3$ 을 벡터의 성분이라 한다.



!!! tldr ""

    영 벡터(zero vector) : 길이가 $0$ 인 벡터로써 
    
    $$ \big<0, 0 \big> $$
    
    또는 
    
    $$ \big< 0,0,0 \big > $$
    
    이다.



!!! tldr ""

    $2$ 차원 벡터의 길이(magnitude or length of vector) : $2$ 차원 공간에서 정의된 임의의 벡터 $\overrightarrow{PQ}$ 를 표준점에 위치시켜서 그 성분을
    
    $$ v = \big<x_2-x_1, y_2-y_1\big> $$
    
    로 표기할 수 있다면 벡터의 길이는 
    
    $$ |v| = ||v|| = \sqrt[]{v _{1} ^{2} + v _{2} ^{2} } = \sqrt[]{(x _{2} - x _{1}) ^{2} + (y _{2} - y _{1}) ^{2} } $$
    
    이다.



!!! tldr ""

    $3$ 차원 벡터의 길이(magnitude or length of vector) : $3$ 차원 공간에서 정의된 임의의 벡터 $\overrightarrow{PQ}$ 를 표준점에 위치시켜서 그 성분을
    
    $$ v = \big<x_2-x_1, y_2-y_1, z_2-z_1 \big> $$
    
    로 표기할 수 있다면 벡터의 길이는 
    
    $$ |v| = ||v|| = \sqrt[]{v _{1} ^{2} + v _{2} ^{2} + v _{3} ^{2}} = \sqrt[]{(x _{2} - x _{1}) ^{2} + (y _{2} - y _{1}) ^{2} + (z _{2} - z _{1}) ^{2}} $$
    
    이다.

- 벡터 $v$ 의 길이를 $|v|$ 또는 $||v||$ 로 표기한다.

!!! tldr ""

    $n$-공간의 벡터의 크기, 길이, 또는 절댓값 : 유향선분 $\overrightarrow{AB}$ 에 대하여 
    
    $$ |\overrightarrow{AB}| := |B-A| $$
    
    또는 좌표 $(v_1, \dots, v_n)$ 으로 표현한 벡터 $v$ 에 대하여
    
    $$ |v| = \sqrt[]{v_1 ^{2}+\dots+v_n ^{2}} $$
    
    이다.

## 노름 거리

!!! tldr ""

    $L_1$ 노름(norm) 거리 또는 맨해튼 거리 : 벡터 $a$ 에 대한 $L_1$ 노름은 
    
    $$ ||a|| _{1} = |a_1| + |a_2| + |a_3| + \dots + |a_n| = \sum_{i=1}^{n}|a_i| $$
    
    이다.

- 예시

    벡터 $a = (4, 3)$ 에 대한 $L_1$ 노름은 오른쪽으로 $4$, 위로 $3$ 움직인 것과 같이 $7$ 이다.

    이처럼 $L_1$ 노름은 

    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Manhattan_distance.svg/300px-Manhattan_distance.svg.png)

    와 같이 바둑판 모양으로 움직인 최단거리를 뜻한다.

!!! tldr ""

    $L_2$ 노름(norm) 거리 또는 유클리드 거리 : 벡터 $a$ 에 대한 $L_2$ 노름은 벡터의 크기에서의 정의와 동일하게 
    
    $$ ||a|| _{2} = \sqrt[]{\sum_{i=1}^{n}a _ i ^{2}} = \sqrt[]{a_1 ^{2}+a_2 ^{2}+\dots+a_n ^{2}} $$
    
    이다.

- $L_2$ 노름은 유클리드 기하학에서 사용하던 거리와 똑같고 

    우리가 일상생활에서 직관적으로 생각하던 거리와 동일하다!

- $L_1, L_2$ 노름은 선형회귀 모델의 정규화 항에서 사용된다.

!!! tldr ""

    $L_p$ 노름 : 점 $(x_1, x_2, \dots, x_n)$ 과 점 $(y_1, y_2, \dots, y_n)$ 의 $L_p$ 노름 거리는 다음과 같이 정의된다. 
    
    $$ \Bigg ( \sqrt[]{\sum_{i=1}^{n}|x_i - y_i| ^{p}} \Bigg ) ^{1/p} $$

- $L_1$ 노름 거리가 

    $$ \sum_{i=1}^{n}|x_i - y_i| ^{p} $$

    로 정의되고 $L_2$ 노름 거리가 

    $$ \Bigg ( \sqrt[]{\sum_{i=1}^{n}|x_i - y_i| ^{2}} \Bigg ) ^{1/2} $$

    로 정의된 것에서 일반화 된 것이다.

!!! tldr ""

    무한 $L _{\infty }$ 노름 : 점 $(x_1, x_2, \dots, x_n)$ 과 점 $(y_1, y_2, \dots, y_n)$ 의 $L _{\infty }$ 노름 거리는 다음과 같이 정의된다. 
    
    $$ \lim_{p \to \infty}  \Bigg ( \sqrt[]{\sum_{i=1}^{n}|x_i - y_i| ^{p}} \Bigg ) ^{1/p} $$

    또는

    $$ = \max (|x_1 -y_1|, |x_2 - y_2|, \dots, |x_n - y_n|) $$

- 보통 $L_1$ 노름거리과 $L_2$ 노름거리, 무한 노름거리 외에는 잘 사용되지 않는다. 

- 무한노름거리는 체비쇼프 거리(chebyshev distance) 거리로도 불린다. 

## 벡터 대수 연산 

(스칼라는 단순히 실수로 생각하면 된다.)

!!! tldr ""

    벡터 덧셈 : $u = \big <u_1, u_2, u_3 \big >, v = \big < v_1, v_2, v_3 \big >$ 인 벡터 $u, v$ 에 대하여 
    
    $$u + v = \big <u_1+v_1, u_2+v_2 + u_3+v_3 \big >$$
    
    이다.

- 예시 

    해석기학적인 벡터 덧셈은 논증기하적으로 벡터 덧셈을 정의했을 때와 같이 

    벡터 $u, v$ 를 더해 벡터 $w$ 가 나오는데, 각각

    삼각형의 형태로 덧셈이 이루어지는 경우

    ![캡처](https://user-images.githubusercontent.com/16812446/79008020-73205b80-7b97-11ea-9e2a-b085f47baf47.PNG)

    와 평행사변형의 형태로 덧셈이 이루어지는 경우

    ![캡처](https://user-images.githubusercontent.com/16812446/79008186-c5617c80-7b97-11ea-8f0a-4bba658bd881.PNG)

    와 같다. 

- 특히 위 예시에서 덧셈의 결과인 $w$ 를 합 벡터(resultant vector) 라 한다.

!!! tldr ""

    벡터 스칼라배 : $u = \big <u_1, u_2, u_3 \big >, v = \big < v_1, v_2, v_3 \big >$ 인 벡터 $u, v$ 에 대하여 
    
    $$ku = \big <ku_1, ku_2, ku_3 \big >$$
    
    이다.

- 벡터 $u$ 에 스칼라배를 하면 벡터가 늘어날 수도 있고 줄어들 수도 있다.

- 특히 스칼라 $k$ 가 음수면 벡터의 방향이 바뀐다.

!!! tldr ""

    스칼라배 벡터의 길이 : 벡터 $u$ 에 스칼라배 $k$ 를 한 벡터 $ku$ 의 길이 $|ku|$ 는 
    
    $$ |ku| = \sqrt[]{(ku_1) ^{2}+(ku_2) ^{2}+(ku_3)^{2}} = \sqrt[]{k ^{2}(u_1 ^{2}+u_2 ^{2}+u_3 ^{2})} $$
    
    $$ = \sqrt[]{k ^{2}}\sqrt[]{u_1 ^{2}+u_2 ^{2}+u_3 ^{2}} = |k||u| $$
    
    이다.

- 즉, $ku$ 의 길이는 벡터 $u$ 의 길이에 정확히 $k$ 배한 길이와 같다. 

- 특히 벡터 $u$ 에 $-1$ 스칼라를 곱한 벡터 $-u$ 는 같은 길이에 정반대 방향을 가르킨다.

!!! tldr ""

    단위 벡터(unit vector) : 길이가 $1$ 인 벡터이다.

- 즉 단위 벡터란 벡터

    $$ v = \big<x_2-x_1, y_2-y_1, z_2-z_1 \big> $$

    에 대한 벡터 길이

    $$ |v| = \sqrt[]{(x _{2} - x _{1}) ^{2} + (y _{2} - y _{1}) ^{2} + (z _{2} - z _{1}) ^{2}} = 1 $$

    을 만족하는 모든 벡터를 뜻한다.

!!! tldr ""

    $3$차원 공간에서의 표준 단위 벡터(standard unit vector) : 표준 단위 벡터는 길이가 $1$ 인 다음의 특수한 $3$ 가지 경우의 벡터를 뜻한다. 
    
    $$ i := \big <1, 0, 0 \big >, j := \big <0, 1, 0 \big >, k := \big <0, 0, 1 \big > $$

- 벡터 $i,j,k$ 는 사원수체에서 허수부의 기저이다.

- 그 어떠한 벡터도 표준 단위 벡터의 선형결합으로 표현될 수 있다. 그러므로 표준 단위 벡터는 모든 벡터를 생성한다. 

- 예시

    즉, 임의의 벡터 $v = \big <v_1,v_2, v_3 \big >$ 는 다음과 같이 표준 단위 벡터의 선형 결합으로 표현될 수 있다. 

    $$ v = \big <v_1,v_2, v_3 \big > = \big <v_1,0,0\big > + \big <0,v_2,0\big > + \big <0,0,v_3\big > $$

    $$ = v_1\big <1,0,0\big > + v_2\big <0,1,0\big > + v_3\big <0,0,1\big > $$

    $$ = v_1i + v_2j + v_3k $$

!!! tldr ""

    벡터의 $i$ 성분(i-component) : 표준 단위 벡터의 예시에서 스칼라 $v_1$ 을 벡터 $v$ 의 $i$ 성분이라한다.

- 즉 $i$ 성분은 $(1, 0, 0)$ 또는 $\big < 1, 0, 0 \big >$ 이다.

- 또 $i$ 벡터를 $x$ 축 상의 단위벡터라고도 한다.

!!! tldr ""

    벡터의 $j$ 성분(j-component) : 표준 단위 벡터의 예시에서 스칼라 $v_2$ 을 벡터 $v$ 의 $j$ 성분이라한다.

- 즉 $j$ 성분은 $(0, 1, 0)$ 또는 $\big < 0, 1, 0 \big >$ 이다.

- 또 $j$ 벡터를 $y$ 축 상의 단위벡터라고도 한다.

!!! tldr ""

    벡터의 $k$ 성분(k-component) : 표준 단위 벡터의 예시에서 스칼라 $v_3$ 을 벡터 $v$ 의 $k$ 성분이라한다.

- 즉 $k$ 성분은 $(0, 0, 1)$ 또는 $\big < 0, 0, 1 \big >$ 이다.

- 또 $k$ 벡터를 $z$ 축 상의 단위벡터라고도 한다.

!!! tldr ""

    벡터의 $i,j,k$ 성분으로의 벡터 표기 : 점 $P_1(x_1, y_1, z_1)$ 에서 점 $P_2(x_2, y_2, z_2)$ 으로 이어져있는 벡터는 
    
    $$ \overrightarrow{P_1P_2} = (x_2 - x_1)i + (y_2-y_1)j+(z_2-z_1)k $$
    
    로 표기할 수 있다.

- 따라서

    $$ \overrightarrow{P_1P_2} = \big <x_2 - x_1 , y_2-y_1,z_2-z_1 \big >  = (x_2 - x_1)i + (y_2-y_1)j+(z_2-z_1)k $$

    이다.

!!! tldr ""

    $n$-공간에서의 표준단위벡터 : $n$-공간에서 벡터
    
    $$ e_1 := (1,0,0,\dots,0) $$
    
    $$ e_2 := (0,1,0,\dots,0) $$
    
    $$ \vdots $$
    
    $$ e_n := (0,0,0,\dots,1) $$
    
    를 표준단위벡터라고 한다.



!!! tldr ""

    나란한 벡터 : 영벡터가 아닌 두 벡터 $v, w$ 에 대하여 
    
    $$ v = tw $$
    
    인 실수 $t$ 가 존재하면, $v, w$ 를 나란하다고 한다.

- 이때 $t>0$ 이면 $v,w$ 는 같은 방향이라 하고,

    $t<0$ 이면 $v,w$ 는 반대 방향이라 한다.

- 영벡터는 모든 벡터와 나란하다고 정의한다.

- 예시 

    벡터 $v = (1,2,3)$ 과 같은 방향의 단위벡터를 구해보자.

    $v$ 의 절댓값(크기)를 $t$ 라고 하고 $v$ 와 같은 방향의 단위벡터를 $a$ 라고 하자. 그러면 

    $$ \sqrt[]{1 ^{2}+2 ^{2}+3 ^{3}} = t $$

    이고 

    $$ (1,2,3) = ta $$

    이다. 따라서 

    $$ a = \dfrac{1}{t}(1,2,3) = \dfrac{1}{\sqrt[]{14}}(1,2,3) $$

    이다.

    - 벡터 $v$ 방향으로의 단위벡터는 다음의 정의에서 좀 더 구체적으로 살펴보자.

!!! tldr ""

    벡터 방향으로의 단위 벡터 : 영벡터가 아닌 벡터 $v \neq 0$ 와 길이 $|v|$ 에 대하여 
    
    $$ \frac{v}{|v|} $$
    
    가 벡터 $v$ 방향으로의 단위 벡터이다.

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

## 내적, 외적

!!! tldr ""

    내적(inner product) : $n$-공간 의 두 벡터 $u ,v$ 가 $u = \big < u_1, u_2, u_3, \dots, u_n \big >, v = \big  <v_1, v_2, v_3, \dots, v_n \big  >$ 일 때, 
    
    두 벡터 $u, v$ 의 내적은 두 벡터 $u, v$ 가 이루는 각 $\theta$ 에 대하여 스칼라
    
    $$ u \cdot v := u_1v_1+u_2v_2+u_3v_3+\dots+u_nv_n = \sum_{i=1}^{n}u_iv_i = |u||v|\cos \theta $$
    
    이다.

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
    
- 내적의 성질 : 임의의 벡터 $u, v, w$ 와 스칼라 $c$ 에 대하여 다음이 성립한다. 

    1. $u \cdot v = v \cdot u$

    2. $(cu)\cdot v = u \cdot (cv) = c(u \cdot v)$

    3. $u \cdot (v + w) = u \cdot v + u \cdot w$

    4. $u \cdot u = |u| ^{2}$

    5. $0 \cdot u = 0$

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

!!! tldr ""

    정사영(orthogonal projection) : 영이 아닌 벡터 $a$ 와 임의의 벡터 $b$ 에 대하여, 벡터 $b$ 에서 직선 $\{ta|t \in \mathbb{R}\}$ 에 내린 수선의 발
    
    $$ P _{a}(b) = \text{proj} _{a}b =  \dfrac{a \cdot b}{a \cdot a}a $$
    
    
    을 $a$ 에 대한 $b$ 의 정사영이라 한다.

- 실수(스칼라) $\dfrac{a \cdot b}{a \cdot a}$ 를 벡터 $b$ 의 $a$ 성분이라고 한다.

    - $a$ 가 단위벡터라면 

        $$ a \cdot b $$

        가 $b$ 의 $a$ 성분이다.

- 즉, $a$ 에 대한 $b$ 의 정사영은 영이 아닌 벡터 $a$ 와 임의의 벡터 $b$ 에 대하여, $a$ 와 나란한 벡터 중 $b$ 와의 거리가 가장 가까운 벡터인 것이다.

    ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAARwAAACyCAMAAACnS4D4AAAAw1BMVEX///+/AADu0dHa2toAAAAvLy/m5ubp6ent7e2/v7+oqKi4uLj8/Pzw8PDf39/j4+NBQUGqAAD39/fFxcVra2vWu7vPz89XV1ezs7OWlpZSUlJJSUnLy8uGhoZEREQ8PDwpKSmhoaEjIyN5eXmYmJgUFBRWVlaOjo41NTVjY2N1dXWCgoJmZmYREREoLS3/3t7/mZn/0dHEqKhTHBzyra3zKyvyWlrympqUAADPAADDDQ0QGBj/Li7/PT3/dHT/qan/6up/IHvnAAAF3UlEQVR4nO2da4OqNhCG03K/agNF7qjoAu5ut9v2tD29//9fVRT3HG8gIggJ83xxAWXHGGcykzcRIQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgIGDhb4tGC4Oy6Zi30YMFIvNmfVtxUBxto3Dqn2bMUykbdtM+7ZimNjuOm8cpm8zhojiTiPenuG+7RggjDf1pnLfVgyVLPRMhFStbzuGiMKFUT7Ckby+DRkgi6Wl2fmjAaOcMwJOL/6Q3H4NGSBm+OFqMCQPx2B3BoPiEoRo8/XAN/szZIAwy+TgSAKHfICxPhr5gUM+QF4bR8e81JMhAySZQ5pZRjw9rYrqkF4V4OzpLAUHn1MgehfCtvT0eEMGCJMmF85al06ODn++6NuEwWIvlYvnNf3BhgyQFWddvgD1HBREZR1k9PUc1XRLCxNjz620p5eKGYZxFy8m0+eqy6NuHItbVV02skcZMkCkuV15fcwOWeaM6ieMOLdK0msVCnGsJQx144FuqwScZddFAiNNPHkvrhGmx1myuFyhOGOUDtmY16t/MiMsZNhzmFXIuTiOccoqFGcIV8ZBhKL61hYjPr/0HE7q3oVSn6MyDKPruhWcxiT8Mqsv16K4ZMHg86+V6Jo3ZNoGvUKCGX92So+CHgwZIuf1BuvGSQaVWqUtnvonBQmlZJKhFHoL7JKNjt/bYu7feAt66zkBj9Kj4/TmWShKQ3mOo8kHPUU1vdvVj/QuRlOlg56C3WzUxfIq+OjCUPk6fqNXEQYzdxq9bgz1nBMZZH3odchfOJVB1mdy47iIPEAGWc4mar6AQa+e8yMddXbPSkS6fY4Y3lV0oDpa6dx9FQqrUoJBNv5yhLMHNbHX90ZirXa1mTRWy7qTDKVQW895ju7/2Cmt56gvbgtrwunsOZr7AhWKEiYRxTH4Tqx5pQyyPhRO6ilXZJD1oc8h3z7JUAp1udV1GWR9xLtHSoNC3TSYZBgJeFZDBlkfplnpeZjwYbvTBTSVLJi05U+aIodcVwZZH3oEkzIHMsgynLT9uCu0NmLql7i+DLI+dPgcnN0gg6wPFbmV6G46qVDQIJhkonGubqmDz3UVcckXTNrzzqb7iR8hL7ju4i3p9ZzyvRZagOwCe9VeCy1AtGCyeq+FcXNlr4X7IVhIcGWvhRYgN1pJy851V8TmVvKy+zWGpAomEw5kkGVswkdE2QmJgkl8lwyyPiT6HDHcXH9SGxCYPhzsteB324FsNpx+QIZvVtgvizcTsdtlLZKr7JEyIja4ddjgIw+3Fqhbp6B4olCgmSQ0TszaWJ4XRdFM67hxZJbfI5LQODPWEHnNKyxNLbnb5Ed+FchpHMyxlsjzgsJtjzQTJd3urCq/ktNzBDad7D5KrfA6Me54fwHJJabnWKwrFMaK8U4xwHQ9gJWeiGgcRhEN1tT2pgr2Y+qX9lrsrHFUqa3EOdj+9l+i7eOqIBo/tHTjy7z9+L6Nh2L46oith3Jb3jpKIX9DXCv303c/Gvn9V376+dsu+eXTp0+//vYeTb31SioGgbNEZ1pBj6MoipWn7TtqpVi3+9FI9vfvDvimSz5//mP78GcYTtkP1lw7pGvXC6N0d89WUkRte6dlG3eqx9tff//z7xsy5xF7vgfPvSSpFyjizlG0k68Zeds8cLP4/96Lx8VzB//U2mll1Cx3om3dkr4pGFi5AlBGQ/mgSpfc/xJOkqS3ujC+GKQ4lCgoq7hdlDQx/BwroFfNKxcBwmmYCVgaprjj7ActcjPPEeOYpnlERTB4rGgSRryRN4y1b5yN0aR1bBmZFA22fCNGL76sLARmhTaqoWYI44mGPDVpIOhOeGSSrGU6ZcGgJXrJ/5gjlGE0SZBgLSYTB8UNsgJLkgKatkfOkB7s5idSpM7yL4aPdMtHloIaTWRiugb8ni8jcatRVoxtoMr7UIBlhGUZVjqerJaS8sbRbNum6uNvzuqocRxZy9tLgF/JAwAAAAAAAAAAAAAAAAAAAAAAAIAm/A9OZ1YJp/cf9AAAAABJRU5ErkJggg==)

- 증명

    벡터 $a$ 와 나란한 벡터 $ta$ 중에서 $b$ 와 거리가 가장 가까운 것을 구하면 된다.

    벡터 $b$ 와 $ta$ 사이의 거리의 제곱은 

    $$ f(x) = |ta-b| ^{2} = (ta-b)\cdot (ta-b) $$

    $$ = (a \cdot a) t^{2} - 2(a \cdot b)t+b \cdot b $$

    이다. 그러면 $f(t)$ 는 임의의 실수 $t$ 에 대한 $2$차 다항함수이고, 최고차 항의 계수가 양수이다.

    그러므로 $f(t)$ 는 

    $$ 0 = f'(t) = 2(a \cdot a)t - 2(a \cdot b) $$

    일 때, 즉 

    $$ t = \dfrac{a \cdot b}{a \cdot a} $$

    일 때 최솟값을 가진다.

    $\therefore$ 그러므로 벡터 $b$ 와 거리가 가장 가까운 벡터 $ta$ 는 $\dfrac{a \cdot b}{a \cdot a} a$ 이다. ■

!!! tldr ""

    두 벡터의 각도(angle between two vectors) : 시점이 같은 영벡터가 아닌 두 벡터 $u, v$ 가 $u = \big < u_1, u_2, u_3 \big >, v = \big  <v_1, v_2, v_3 \big  >$ 일 때, 
    
    두 벡터 $u ,v$ 가 이루는 각 $0 \leq  \theta \leq \pi$ 는 
    
    $$ \theta = \cos ^{-1} \bigg ( \frac{u \cdot v}{|u||v|} \bigg ) $$
    
    이다.

- 다음과 같이 쓸 수도 있다.

    $$ \theta = \cos ^{-1} \bigg ( \frac{u_1v_1+u_2v_2+u_3v_3}{|u||v|} \bigg ) $$

- 증명 

    시점이 같은 임의의 두 벡터 $u = \big <u_1,u_2,u_3\big >, v=\big <v_1,v_2,v_3\big >$ 가 이루는 각 $0 \leq \theta \leq \pi$ 를 구해보자. 

    <img src="https://user-images.githubusercontent.com/16812446/86887866-392e0980-c134-11ea-9889-3e42cf40f31a.png" width="50%" height="auto">

    > 출처 : [Thomas' CALCULUS](https://www.amazon.com/Thomas-Calculus-Early-Transcendentals-13th/dp/0321884078) Figure12.21

    두 벡터의 크기 $|u|, |v|$ 와 두 벡터의 뺄셈으로 얻은 벡터 
    
    $$w = u-v=\big <u_1-v_1,u_2-v_2,u_3-v_3\big >$$
    
    에 대하여 코사인 법칙

    $$ |w| ^{2} = |u|^{2}+|v|^{2}-2|u||v|\cos \theta $$

    $$ 2|u||v|\cos \theta= |u|^{2}+|v|^{2} - |w| ^{2} $$

    이 성립한다. 이때 벡터 $u, v, w$ 의 크기 제곱은

    $$ |u| ^{2} = \bigg (\sqrt[]{u_1 ^{2}+u_2 ^{2}+u_3 ^{2}} \bigg )^{2}=u_1 ^{2}+u_2 ^{2}+u_3 ^{2} $$
    
    $$ |v| ^{2} = v_1 ^{2}+v_2 ^{2}+v_3 ^{2} $$
    
    $$ |w| ^{2} = (u_1-v_1) ^{2}+(u_2 - v_2) ^{2}+(u_3 - v_3) ^{2} $$

    $$ = u_1 ^{2}-2u_1v_1 + v_1 ^{2} +u_2 ^{2}-2u_2v_2 + v_2 ^{2} +u_3 ^{2}-2u_3v_3 + v_3 ^{2} $$

    이므로 
    
    $$ |u|^{2}+|v|^{2} - |w| ^{2} = 2(u_1v_1+u_2v_2+u_3v_3) $$

    이다. 그러므로

    $$ 2|u||v|\cos \theta= |u|^{2}+|v|^{2} - |w| ^{2} = 2(u_1v_1+u_2v_2+u_3v_3) $$

    $$ \cos \theta = \dfrac{u_1v_1+u_2v_2+u_3v_3}{|u||v|} $$

    이다. 그런데 $\theta$ 가 두 벡터가 이루는 각이므로 $0 \leq 0 < \pi$ 이다. 따라서 최종적으로 두 벡터 $u,v$ 가 이루는 각 $\theta$ 는

    $$ \therefore \theta = \cos ^{-1}\bigg ( \dfrac{u_1v_1+u_2v_2+u_3v_3}{|u||v|} \bigg ) = \cos ^{-1}\bigg ( \dfrac{u \cdot v}{|u||v|} \bigg ) $$

    이다. ■ 

- 예시 

    두 벡터 

    $$ u = i - 2j - 2k, v = 6i + 3j + 2k $$

    가 이루는 각을 구해보자.

    $$ u \cdot v = (1)(6)+(-2)(3)+(-2)(2) = -4 $$

    $$ |u| = \sqrt[]{(1)^{2}+(-2)^{2}+(-2)^{2}} = \sqrt[]{9} = 3 $$

    $$ |v| = \sqrt[]{(6)^{2}+(3)^{2}+(2)^{2}} = \sqrt[]{49} = 7 $$

    에서 

    $$ \theta = \cos ^{-1} \bigg ( \frac{u \cdot v}{|u||v|} \bigg ) = \cos ^{-1} \bigg ( \frac{-4}{3 \cdot 7} \bigg ) \approx 100.98 \degree $$

!!! tldr ""

    코사인 유사도(cosine similarity) : 영벡터가 아닌 두 벡터 $u, v$ 가 $u = \big < u_1, u_2, \dots, u_n \big >, v = \big  <v_1, v_2, \dots, v_n \big  >$ 일 때, 
    
    $$ \cos  \theta = \frac{u \cdot v}{|u||v|} $$
    
    또는 
    
    $$ \cos  (u, v) := \frac{u \cdot v}{|u||v|} $$
    
    를 코사인 유사도라고 정의한다.

- 증명 

    코사인 유사도 $\cos  \theta = \dfrac{u \cdot v}{|u||v|}$ 는 두 벡터의 각도 $\theta = \cos ^{-1} \bigg ( \dfrac{u \cdot v}{|u||v|} \bigg )$ 에서 

    $$ \therefore  \cos \theta = \frac{u \cdot v}{|u||v|} $$

    와 같이 쉽게 유도된다. 

- 다음의 기호로도 표기할 수 있다. 

    $$ \cos \theta = \frac{u \cdot v }{||u|| \cdot  ||v||} = \frac{ \displaystyle \sum_{i=1}^{n}a_ib_i}{ \displaystyle \sqrt[]{\sum_{i=1}^{n}a_i ^{2}} \sqrt[]{\sum_{i=1}^{n}b_i ^{2}}} $$

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

!!! tldr ""

    벡터의 직교(orthogonal vectors) : 두 벡터 $u, v$ 가 직교하는 조건은
    
    $$ u \cdot v = 0 $$
    
    이다.

- 두 벡터가 이루는 각이 $90 \degree$ 일 때 직교한다고 한다. 

- 증명 

    $$ \cos \bigg ( \frac{\pi }{2} \bigg ) = 0 , \cos ^{-1} 0 = \frac{\pi }{2} $$

    이므로 벡터 $u, v$ 가 이루는 각이 $90 \degree = \dfrac{\pi }{2}$ 라면

    $$ \theta = \cos ^{-1} \bigg ( \frac{u \cdot v}{|u||v|} \bigg ) $$

    에서 

    $$ \frac{\pi }{2}  = \cos ^{-1} 0 = \cos ^{-1} \bigg ( \frac{u \cdot v}{|u||v|} \bigg ) $$

    $$ 0 = \frac{u \cdot v}{|u||v|} $$

    이다. 그러므로

    $$ \therefore u \cdot v = 0 $$

    이다. ■

!!! tldr ""

    외적(outer product) : 벡터 $u, v$ 가 이루는 각이 $\theta$ 이고 벡터 $u, v$ 가 이루는 평면에 수직한 단위 벡터 $n$ 에 대하여 
    
    벡터 $u, v$ 의 외적은 벡터 
    
    $$ u \times v = (|u||v| \sin \theta) n $$
    
    이다.

- 교차곱(cross product), 벡터곱(vector product), 텐서곱(tensor product) 으로도 불린다. 

- 내적의 결과가 스칼라인 반면 외적의 결과는 벡터이다. 

    - 이로 인해 외적은 벡터곱(vector product) 이라고 불리기도 한다. 

- 벡터의 외적 $u \times v$ 는 $u, v$ 에 직교(orthogonal) 한다. 

    ![](https://www.sharetechnote.com/image/EngMath_Matrix_CrossProduct_01.png)

    - 왜냐하면 위 그림과같이 외적이란 벡터 $n$ 의 스칼라배에 불과하기 때문이다. 

    - 위 그림의 빨간선이 벡터 $u, v$ 가 이루는 평면에 직교하는 단위벡터 $n$ 이다! 

- 외적의 성질 : 임의의 벡터 $u, v, w$ 와 임의의 스칼라 $r, s$ 에 대하여 다음이 성립한다. 

    1. $(ru) \times (sv) = (rs)(u \times v)$

    2. $u \times (v + w) = u \times v + u \times w$

    3. $v \times u = -(u \times v)$

    4. $(v+w)\times u = v \times u + w \times u$

    5. $0 \times u=0$

    6. $u \times (v \times w) = (u \cdot w)v - (u \cdot v)w$

!!! tldr ""

    외적의 크기 : 벡터 $u, v$ 의 외적의 크기는 
    
    $$ |u \times v| = |u||v| \sin \theta $$
    
    이다.

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

!!! tldr ""

    평행 벡터(parallel vectors) : 두 벡터 $u, v$ 가 평행인 것은
    
    $$ u \times v = 0 $$
    
    와 동치이다.

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

# 일차독립과 일차종속

!!! tldr ""

    $3$차원 좌표공간의 표준단위벡터의 일차결합(linear combination) : $3$차원 좌표공간의 임의의 벡터 
    
    $$ v = (v_1, v_2, v_3) $$
    
    은 표준단위벡터 $i = (1,0,0),j = (1,0,0),k = (1,0,0)$ 에 의하여 
    
    $$ a = a_1i + a_2j + a_3 k $$
    
    로 표현할 수 있는데, 이와 같은 표현을 벡터 $i,j,k$ 의 일차결합이라 한다.

- 예시 

    $2$차원 좌표평면에서의 벡터 $i, j$ 를 $1$시방향 벡터 

    $$ h_1 := (\cos 60 \degree , \sin 60 \degree ) = \dfrac{1}{2}(1, \sqrt[]{3}) $$

    와 $5$시방향 벡터

    $$ h_5 := (\cos 60 \degree , -\sin 60 \degree ) = \dfrac{1}{2}(1, -\sqrt[]{3}) $$

    의 일차결합으로 표현하면

    $$ i = h_1+h_5, j = \dfrac{1}{\sqrt[]{3}}h_1 - \dfrac{1}{\sqrt[]{3}}h_5 $$

    이다.

!!! tldr ""

    일차결합 또는 선형결합(linear combination) : 임의의 자연수 $k$ 에 대한 임의의 실수 $t_1, \dots, t_k$ 에 대하여 벡터 
    
    $$ t_1a_1 + \dots + t_ka_k $$
    
    를 $a_1, \dots, a_k$ 의 일차결합이라 한다.



!!! tldr ""

    일차종속 또는 선형종속(linearly dependent) : 일차결합의 정의에서 $a_1, \dots, a_k$ 중 어느 벡터 $a_i$ 가 나머지 벡터들의 일차결합이면 $a_1, \dots, a_k$ 를 일차종속이라 한다.

- 예시 

    $a_1, \dots, a_k$ 에서 $a_1$ 이 $a_2, \dots, a_k$ 의 일차결합이면 $a_1, \dots, a_k$ 는 일차종속이다.

- 예시 

    벡터 $a=(1,2,3),b=(2,4,6)$ 에서 $b=2a$ 이므로 이들은 일차종속이다.

!!! tldr ""

    일차독립 또는 선형독립(linearly independent) : 일차결합의 정의에서 $a_1, \dots, a_k$ 가 일차종속이 아니면 $a_1, \dots, a_k$ 을 일차독립이라 한다.

- 어떤 벡터 $a$ 가 일차독립이라는 것은 $a \neq 0$ 임을 뜻한다.

- 자연수 $k$ 에 대한 벡터 $a_1, \dots, a_k$ 가 일차독립일 필요충분조건은 방정식 

    $$ x_1a_1 + x_2a_2 + \dots + x_ka_k = 0 $$

    의 해가 자명한 해 즉, $x_1=x_2=\dots=x_k=0$ 뿐인 것이다.

    - 증명 

        이 명제의 대우를 증명하려 해보자. 즉, 귀류법을 사용하자. 그러면 방정식

        $$ x_1a_1 + x_2a_2 + \dots + x_ka_k = 0 $$

        은 자명하지 않은 해 $(x_1, \dots, x_k)$ 를 갖는다. 즉, 어떤 $i \in \{1, \dots, k\}$ 에 대하여 $x_i \neq 0$ 이다. 그러므로 

        $$ a_i = -\dfrac{x_1}{x_i}a_1 - \dots -\dfrac{x _{i-1}}{x_i}a _{i-1}-\dfrac{x _{i+1}}{x_i}a _{i+1} - \dots - -\dfrac{x _{k}}{x_i}a _{k} $$

        인데 이것은 곧 $a_1, \dots, a_k$ 가 일차종속이라는 것이다.

        가정과 모순이므로 벡터 $a_1, \dots, a_k$ 가 일차독립이면 방정식

        $$ x_1a_1 + x_2a_2 + \dots + x_ka_k = 0 $$

        은 자명한 해만을 갖는다.

# $3$차원 좌표공간의 기저

!!! tldr ""

    $3$차원 좌표공간의 생성 : $3$차원 좌표공간에서 실수 $v_1, v_2, v_3 \in \mathbb{R}$ 에 대한 벡터 $v=(v_1, v_2, v_3)$ 는 표준단위벡터 $i,j,k$ 의 일차결합인데,
    
    이때 $i,j,k$ 가 $3$차원 좌표공간을 생성한다고 한다.



!!! tldr ""

    $n$-공간의 생성 : $n$-공간의 모든 벡터가 벡터 $a_1,\dots,a_n$ 의 일차결합이면,
    
    $a_1,\dots,a_n$ 는 $n$-공간을 생성한다.

- 좌표평면에서는 $i,j$ 가 평면을 생성한다.

- 예시 

    $n$-공간의 임의의 벡터 $a=(a_1,\dots,a_n)$ 는 표준단위벡터들의 일차결합이다. 즉, 

    $$ a=a_1e_1+a_2e_2+\dots+a_ne_n $$

    이다. 그러므로 표준단위벡터 $e_1, \dots, e_n$ 는 $n$-공간을 생성한다.

!!! tldr ""

    $n$-공간의 기저(basis) : 일차독립이면서 $n$-공간을 생성하는 벡터 집합을 $n$-공간의 기저라고 한다.

- 예시 

    $n$-공간의 임의의 벡터 $a=(a_1,\dots,a_n)$ 는 표준단위벡터들의 일차결합이다. 즉, 

    $$ a=a_1e_1+a_2e_2+\dots+a_ne_n $$

    이다. 그러므로 표준단위벡터 $e_1, \dots, e_n$ 는 $n$-공간을 생성한다.

    그런데 벡터 $e_2, \dots, e_n$ 의 어떤 일차결합도 첫번째 성분이 $0$ 이 되므로 $e_1$ 의 일차결합이 될 수 없다. 같은 원리로 $e_i$ 는 $e_1, \dots, e _{i-1},e _{i+1}, \dots,e_n$ 의 일차결합일 수 없다. 그러므로 표준단위벡터 $e_1, \dots, e_n$ 은 서로 일차독립이다.

    표준단위벡터는 일차독립이면서 $n$-공간을 생성한다. 따라서 표준단위벡터는 $n$-공간의 기저이다. ■ 

# 벡터공간과 차원

!!! tldr ""

    벡터공간(vector space) : $\mathbb{R} ^{n}$ 처럼 원소의 합과 상수배가 정의되어 있는 집합, 즉 대수구조이다.

- 선형대수학이란 벡터공간을 연구하는 학문이다.

- 이 집합의 원소를 벡터라고 한다.

- 좌표공간에서처럼 일반적인 벡터공간 $V$ 에서도 기저를 보일 수 있다.

!!! tldr ""

    차원(dimension) : 벡터공간 $V$ 과 자연수 $n, k$ 에 대한 임의의 두 기저
    
    $$ v_1, \dots, v_n $$
    
    $$ w_1, \dots, w_k $$
    
    에 대하여 항상 $n=k$ 인데, 
    
    이 $n$ 을 $V$ 의 차원이라고 한다.

- 증명 

    벡터 $v_1, \dots, v_n$ 는 벡터공간 $V$ 의 기저이므로 $V$ 를 생성한다. 그러므로 벡터공간 $V$ 의 모든 벡터를 $v_1, \dots, v_n$ 의 일차결합으로 나타낼 수 있다. 

    따라서 $i \in \{1, \dots, k\}, j \in \{1,\dots,n\}$ 에 대한 임의의 실수 $a _{ij}$ 에 대하여

    $$ w _{i} = \sum_{j=1}^{n}a _{ij}v _{j} $$

    로 나타낼 수 있다.

    한편 이때 방정식

    $$ x_1w_1 + x_2w_2 + \dots + x_kw_k = 0 $$

    은 

    $$ \sum_{i=1}^{k}x_iw_i = x_1w_1 +x_2w_2+\dots +x_kw_k $$

    $$ = x_1(a _{11}v_1 + a _{12}v_2 + a _{1n}v_n) + $$

    $$   x_2(a _{21}v_1 + a _{22}v_2 + a _{2n}v_n) + $$

    $$ \vdots $$

    $$   x_k(a _{k1}v_1 + a _{k2}v_2 + a _{kn}v_n) $$

    이다. 이것은 $x_1a_{11}v_1$ 에서 $x_ka_{kn}v_n$ 까지 더한 것이므로 

    $$ = \sum_{j=1}^{n}\bigg (\sum_{i=1}^{k}x_ia_{ij}\bigg )v_j $$

    이다. 그런데 이 방정식은 $w_1, \dots, w_k$ 가 기저이고, 이에따라 일차독립이므로 자명한 해 $x_1 = x_2 = \dots = x_k = 0$  만 가진다.

    그러므로 

    $$ (a _{11}v_1, a _{12}v_2, a _{1n}v_n), \dots, (a _{k1}v_1, a _{k2}v_2, a _{kn}v_n) $$

    는 일차독립이다.

    그러므로 

    $$ (a _{11}, a _{12}, a _{1n}), \dots, (a _{k1}, a _{k2}, a _{kn}) $$

    는 일차독립이다.

    **??????? 벡터공간의 차원 정리에 대한 다른 증명을 찾아보자..**

- 예시 

    $\mathbb{R} ^{n}$ 의 차원은 $n$ 이다.

# 좌표계

!!! tldr ""

    좌표(coordinates) : $n$-공간의 의 벡터 $b_1, \dots, b_n$ 와 $n$-공간의 한 기저 $\mathcal{B}:= (b_1, \dots, b_n)$ 에 대하여 임의의 벡터 $v \in \mathbb{R} ^{n}$ 을 $\mathcal{B}:= (b_1, \dots, b_n)$ 로 표현하는 방법은
    
    $$ v = c_1b_1 + c_2b_2 + \dots + c_nb_n $$
    
    로써 유일한데, 이때 $(c_1, \dots, c_n) \in \mathbb{R} ^{n}$ 을 기저 $\mathcal{B}:= (b_1, \dots, b_n)$ 에 대한 벡터 $v$ 의 좌표라고 한다.

- 지금까지 줄곧 사용하던 좌표평면의 좌표 $(a,b)$ 와 좌표공간의 좌표 $(a,b,c)$ 을 일반화한 것이다.

    - 우리가 일반적으로 사용해왔던 좌표평면의 기저는 $\bigg (\begin{bmatrix} 1\\0 \end{bmatrix}, \begin{bmatrix} 0\\1 \end{bmatrix}\bigg )$ 이고, 좌표공간의 기저는 $\bigg ( \begin{bmatrix} 1\\0\\0 \end{bmatrix}, \begin{bmatrix} 0\\1\\0 \end{bmatrix}, \begin{bmatrix} 0\\0\\1 \end{bmatrix} \bigg )$ 인 것이다.

# 행렬

!!! tldr ""

    행렬곱 : $m \times n$ 행렬 $A=(a_{ij})$ 와 $n \times l$ 행렬 $B = (b _{jk})$ 에 대한 곱 $AB$ 는
    
    $m \times l$ 행렬 $A \times B = C = (c _{ik})$ 로써 $(i, k)$ 항이 $A$ 의 $i$번째 행 벡터와 $B$ 의 $k$ 번째 열 벡터의 내적 
    
    $$ \sum_{j=1}^{n}a _{ij}b _{jk} $$
    
    이다.



!!! tldr ""

    정사각행렬, or 정방행렬(square matrix), or $n$차 정사각행렬 : 행의 수와 열의 수가 $n$ 으로 같은 행렬이다.



!!! tldr ""

    $n$차 단위 행렬, or 항등행렬 : 대각선의 항들, 즉 $(i,i)$ 항이 모두 $1$ 이고 나머지 항은 $0$ 인 $n$차 정사각행렬 $I_n$ 이다.

- 혹은 간단히 $I$ 로도 표기한다.

!!! tldr ""

    선형사상(linear map) : $\forall x, y \in \mathbb{R} ^{n}$ 와 $t \in \mathbb{R}$ 에 대한 사상 $L$ 이 
    
    $$ L(\mathbf{x}+\mathbf{y}) = L(\mathbf{x}) + L(\mathbf{y}), L(t \mathbf{x}) = tL(\mathbf{x}) $$
    
    이면 $L$ 을 선형사상이라 한다.

- 예시 

    항등사상(identity map)

    $$ \text{id}:\mathbb{R} ^{n}\to \mathbb{R} ^{n}, \text{id}(\mathbf{x}):=\mathbf{x} $$

    은 선형사상이다.

- 예시 

    점대칭변환

    $$ -\text{id}:\mathbb{R} ^{n}\to \mathbb{R} ^{n}, \mathbf{x}\mapsto -x$$

    은 선형사상이다.

- 예시 

    $a_1, \dots, a_n \in \mathbb{R}$ 와 $(x_1, \dots, x_n) \in \mathbb{R} ^{n}$ 대한 함수 

    $$ l(x_1, \dots, x_n) := a_1x_1 + \dots+a_nx_n $$

    은 선형사상이다.

!!! tldr ""

    선형사상으로 정의하는 행렬 : $m \times n$ 행렬 $A$ 는 벡터 $\mathbf{x}\in \mathbb{R} ^{n}, A \mathbf{x}\in \mathbb{R} ^{m}$ 에 대한 사상
    
    $$ L_A : \mathbb{R} ^{n} \to \mathbb{R} ^{m}, \mathbf{x} \mapsto A \mathbf{x} $$
    
    이다.

- 설명 

    $n$-공간의 원소 열벡터 $\begin{pmatrix} x_1\\ \vdots \\x_n \end{pmatrix}$ 를 $m \times n$ 행렬 $A = (a _{ij})$ 와 곱하여 $m$-공간의 원소, 즉 벡터를 얻는다. 즉, 

    $$ \begin{pmatrix} a _{11} & \dots & a _{1n}\\ \vdots & \ddots & \vdots \\ a _{m1} & \dots & a _{mn}\\ \end{pmatrix} \begin{pmatrix} x_1\\\vdots \\x_n \end{pmatrix} = \begin{pmatrix} a _{11}x_1 + \dots + a _{1n}x_n\\ \vdots \\ a _{m1}x_1 + \dots + a _{mn}x_n\\ \end{pmatrix} \in \mathbb{R} ^{m} $$

    이다. 그러므로 $m \times n$ 행렬 $A$ 는 벡터 $\mathbf{x}\in \mathbb{R} ^{m}$ 에 대한 사상

    $$ L_A := A \mathbf{x} $$

    으로 정의할 수 있다.

!!! tldr ""

    치환(permutation) : $n \in \mathbb{N}$ 에 대한 집합 $\{1,2,\dots,n\}$ 에서 집합 $\{1,2,\dots,n\}$ 으로 가는 전단사 사상을 $n$-치환이라고 한다.

- 예시 

    항등치환 $id$ 는 

    $$ \text{id}(k) = k $$

    이고, 치환이다.

- $\sigma$ 가 $n$-치환일 때 $n$-치환을

    $$ \begin{pmatrix} 1&2&3&\dots&n\\ \sigma(1)& \sigma(2)& \sigma(3)& \dots& \sigma(n) \end{pmatrix} $$

    로 나타낸다.

    - 예시 

        $$ \begin{pmatrix} 1&2&3&4&5\\ 5& 4& 3& 2& 1 \end{pmatrix} $$

        은 $1,2,3,4,5$ 를 $5,4,3,2,1$ 로 보내는 치환이다.

!!! tldr ""

    항등치환 $\varepsilon$ : 항등치환은 
    
    $$ \varepsilon = \begin{pmatrix} 1&2&3&\dots&n\\ 1&2&3&\dots&n\\ \end{pmatrix} $$
    
    이다.



!!! tldr ""

    치환의 부호 : 치환 $\sigma$ 를 항등치환 $\varepsilon$ 으로 바꾸기 위한 조작횟수 $N(\sigma )$ 에 대하여 치환의 부호는
    
    $$ \text{sgn}(\sigma ) = (-1) ^{N(\sigma )} $$
    
    이다.

- 예시 

    치환 $\sigma = \begin{pmatrix} 1&2&3\\3&2&1 \end{pmatrix}$ 을 항등치환으로 바꾸기 위한 조작 횟수 $N(\sigma )$ 은 두번째 행의 $3$ 과 $1$ 을 $1$번 바꾸면 되기 때문에 

    $$ N(\sigma ) = 1 $$

    이다. 그러므로 치환의 부호는 

    $$ \text{sgn} (\sigma ) = (-1) ^{N(\sigma )} = (-1) ^{1} = -1 $$

    이다.

- 예시 

    치환 $\sigma = \begin{pmatrix} 1&2&3\\2&3&1 \end{pmatrix}$ 을 항등치환으로 바꾸기 위한 조작 횟수 $N(\sigma )$ 은 두번째 행의 $3$ 과 $1$ 을 $1$번 바꾸고 $1$ 과 $2$ 를 바꾸어야 하므로

    $$ N(\sigma ) = 2 $$

    이다. 그러므로 치환의 부호는 

    $$ \text{sgn} (\sigma ) = (-1) ^{N(\sigma )} = (-1) ^{2} = 1 $$

    이다.