# 도형 


!!! tldr ""

    점 : (원론) 쪼갤 수 없는 것이다.



!!! tldr ""

    선 : (원론) 폭이 없이 길이만 있는 것이다.



!!! tldr ""

    직선 : 곧게 뻗은 선을 추상화한 개념이다. (원론) 점들이 곧게 있는 것이다.



!!! tldr ""

    선분 : 양쪽에 끝나는 점이 있는 직선의 부분이다.



!!! tldr ""

    면 : (원론) 길이와 폭만 있는 것이다.



!!! tldr ""

    둘레(경계) : 도형의 경계의 길이를 뜻한다. (원론) 어떤 것의 끝이다.



!!! tldr ""

    도형 : 점(0), 선(1), 면(2), 입체(3), 초입방체(n) 의 집합이다. (원론) 둘레나 둘레들에 둘러싸인 것이다.



!!! tldr ""

    반직선 : 점 하나에서 시작하여 한 방향으로 무한히 뻗어 나가는 선이다.

## 각

!!! tldr ""

    각 : 같은 끝점을 갖는 두 반직선이 이루는 도형이다.

- 즉 반직선과 반직선이 맞붙었을 때 꼭짓점(맞붙은 점) 안팎에서 생기는 공간이다.

!!! tldr ""

    각도 : 각을 이루는 두 반직선이 서로 기운 정도이다.

- 즉 반직선과 반직선 사이에 생긴 공간의 크기이다. 

- 가장 큰 각 : 두 반직선 사이의 공간을 계속 늘리면 두 반직선이 언젠가 맞닿게 되는데 그때 생긴 각이 가장 큰 각이다.

!!! tldr ""

    육십분법 : 가장 큰 각을 $360$ 등분하여 얻은 각도를 $1\degree$($1$도) 라 부르는 각 크기 표현 방식이다.

- 가장 일반적으로 각의 크기를 표현할 때 사용하는 방식이다.

!!! tldr ""

    직각 : 크기가 $90\degree$ 인 각이다.

- (원론) 직선에 다른 직선을 세웠을 때 이웃한 각의 크기가 같으면 그 각을 직각이라 부른다.

!!! tldr ""

    예각 : 크기가 $0\degree$ 보다 크고 $90\degree$ 보다 작은 각이다.

- (원론) 직각보다 작은 각이다.

!!! tldr ""

    둔각 : 크기가 $90\degree$ 보다 크고 $180\degree$ 보다 작은 각이다.

- (원론) 직각보다 큰 각이다. 

## 다각형

!!! tldr ""

    다각형 : 직선들로 둘러싼 도형이다.



!!! tldr ""

    삼각형 : 세 개의 직선으로 둘러싼 도형이다.



!!! tldr ""

    사각형 : 네 개의 직선으로 둘러싼 도형이다.



!!! tldr ""

    넓이(면적) : 영역의 크기를 추상적으로 표현하는 양이다.

## 원

!!! tldr ""

    원 : (원론) 어떤 선에 둘러싸인 도형이 있어서, 한 점에서 그 도형으로 직선을 그었을 때 직선이 모두 같으면 그 도형을 원이라 한다.



!!! tldr ""

    지름 : 원의 중심을 지나는 직선이다.



!!! tldr ""

    반지름 : 원의 중심으로부터 경계에 이르는 선분이다. 지름의 절반이다.



!!! tldr ""

    원주 : 원의 둘레를 뜻한다.

- 원주율의 정의에 따라 원주 $C$ 는 $C=d\pi=2r\pi$ 이다. ($r$ 은 반지름)

!!! tldr ""

    원주율($\pi$) : 원주와 지름의 비율이다. 즉 원의 지름에 대한 원의 둘레의 비율이다.

- 약 $3.141592653589793238...$ 의 수이다.

- 원의 지름을 기준으로 했을 때 원의 둘레의 크기의 정도는 $3.141592653589793238...$ 라는 것이다. 

- 이 비율은 항상 동일하다. 

- $\pi$ 라 표기하며 정의에 따라 원주를 $C$ 원의 지름을 $d$ 라 하면 $\pi=\frac{C}{d}$ 이다.

!!! tldr ""

    원의 넓이 : 원의 크기를 나타내며 $r^2\pi$ 이다. ($r$ 은 반지름)

## 부채꼴 원

!!! tldr ""

    호($arc$) : 이차원 평면 위의 미분가능한 곡선에서 닫힌 부분이다.



!!! tldr ""

    원호($circular arc$) : 원둘레의 일부분이다.



!!! tldr ""

    부채꼴($circular sector$) : 원에서 두 개의 반지름과 하나의 호로 둘러싸인 영역이다. 
    
    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Circle_arc.svg/300px-Circle_arc.svg.png)



!!! tldr ""

    부채꼴의 호의 길이 : 원의 반지름을 $r$, 부채꼴의 중심각을 $\theta$ 라 하면 부채꼴의 호의 길이 $l$ 은 $l = r \theta$ 이다.

- 증명 

    부채꼴의 중심각을 $\theta$ 라디안이라 하고 부채꼴의 호의 길이를 $l$ 이라고 하자. 

    부채꼴의 호의 길이 $l$ 는 중심각의 크기 $\theta$ 에 비례하므로 원의 둘레 $2 \pi r$ 과의 비례식은 

    $$ 2 \pi : 2 \pi r = \theta : l $$

    이다. 그러므로 호의 길이 $l$ 는

    $$ \therefore  l = r \theta $$

    이다.

!!! tldr ""

    부채꼴의 넓이 : 부채꼴의 크기를 나타내며 $\frac{1}{2} r ^{2} \theta$ 이다.

- 증명 

    부채꼴의 중심각을 $\theta$ 라디안이라 하고 원의 반지름을 $r$ 이라 하자.

    부채꼴의 넓이 $S$ 도 중심각 $\theta$ 에 비례하므로 원의 넓이 $\pi r ^{2}$ 와의 비례식은 

    $$ 2 \pi : \pi r ^{2} = \theta : S $$

    이다. 그러므로 부채꼴의 넓이 $S$ 는 

    $$ \therefore S = \frac{\pi r ^{2} \theta }{2 \pi } = \frac{1}{2} r ^{2} \theta $$

    이다.

!!! tldr ""

    반원 : 위 그림에서 중심각 $\theta$ 가 $180 \degree$ 인 부채꼴이다.



!!! tldr ""

    육십분법 : 가장 큰 각을 $360$ 등분하여 얻은 각도를 $1\degree$($1$도) 라 부르는 각 크기 표현 방식이다.



!!! tldr ""

    호도법($Radian$) : 반지름에 대한 호의 비율을 각으로 표현하는 각 크기 표현 방식이다.

- 반지름 $r$ 인 원에 어떤 부채꼴이 있을 때 이 부채꼴의 중심각 $\theta$ 이 마주보는 호의 길이를 $l$ 이라고 하자. 그러면 중심각 $\theta$ 의 라디안 값은 반지름에 대한 호의 비율 $l/r$ 이다. 

  ![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Circle_radians.gif/220px-Circle_radians.gif)

- 반지름의 길이 $r$ 과 같은 호의 길이 $r$ 로 이루어진 부채꼴의 중심각 $\theta$ 가 $1$ 라디안이 된다.

- $360 \degree$ 는 반지름에 대한 원둘레의 비율이므로 $2 \pi$ 라디안이다. 

- $1 \degree$ 는 $2 \pi$ 라디안을 $360$ 등분한 것이므로 $(\pi/180)$ 라디안이다. 

- $1$ 라디안은 $360 \degree$ 를 $2\pi$ 등분한 것이므로 $(180/\pi) \degree$ 이다. 

- 라디안은 길이와 길이의 비율로 정의되므로 무차원 수이며, 이에 따라 단위(차원)가 없는 순수한 수로 표현할 수 있기 때문에 수학적 기술이 용이해져 육십분법보다 자주 쓰인다. 

- 원주율의 단위도 라디안이다.

!!! tldr ""

    새로운 원주율($\tau$) : 라디안을 사용할 때 현재 사용하고 있는 원주율($\pi$) 가 라디안의 정의와 $\frac{1}{2}$ 차이가 나서 부자연스럽기 때문에 $\pi$ 에 $2$ 를 곱한 값을 사용하자고 주장된 원주율 $\tau$(타우) 이다.

- 라디안은 **반지름**에 대한 호의 비로 정의되는데 원주율 $\pi$ 은 **지름**에 대한 원주의 비로 정의되기에 부자연스럽다. 

- $\tau = 2 \pi = 6.283185...$ 의 값이다. 

- 타우 $\tau$ 를 사용하면 원주의 길이가 $\tau r$, 원의 넓이가 $\frac{1}{2}\tau r^2$ 이 되고 이것이 훨씬 더 직관적이다. 

- 라디안에서 타우 $\tau$ 를 사용하면 한 바퀴가 $\tau$ 가 되고 삼각함수 $\sin, \cos$ 의 한 주기도 $\tau$ 가 된다. 

> 하지만 원주율 $\pi$ 를 새로운 원주율 $\tau$ 로 바꾸는 효용보다 비용이 더 커서 아마 바뀌지 않을 거라고 예상된다. 사람은 최대이익과 최소비용의 방향으로 행동을 택하기 때문이다. 물론 $\tau$ 를 사용함에 있어서 그 효용이 막대하게 커지는 요인이 발생한다면 이야기는 달라질 것이다. 

## 삼각비

!!! tldr ""

    삼각법(trigonometry) : 삼각형의 변과 각 사이의 관계에 따른 여러가지 도형을 연구하는 수학의 한 분과이다.



!!! tldr ""

    삼각비(trigonometric ratio) : 직각삼각형의 두 변의 길이의 비례 관계를 나타내는 값이다.

- 삼각비는 직각삼각형의 빗변은 항상 밑변, 높이와 일정 비율을 유지하고 있음을 보여준다. 

- 삼각법을 통해 각도만으로 변의 길이를 비교 계산할 수 있는 편리함이 있었기에 고대로부터 개발되었다. (**수학의 발전 이유 중 하나는 관계에 관한 연구를 계속하는 것으로 한 요소를 밝혀내는 것으로 다른 요소를 알 수 있는 편리함이 있기 때문이다.**)

- 삼각비의 정의역은 $0 \degree < x < 90 \degree$ 이다. 따라서 $0 \degree$ 와 $90 \degree$ 에서는 정의되지 않는다. 

![](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Trigonometry_triangle.svg/225px-Trigonometry_triangle.svg.png)

!!! tldr ""

    주어진 각을 기준으로 직각삼각형의 특정 부분을 칭하는 방법

- 밑변 : 주어진 각을 기준으로 직각삼각형의 직각으로 향하는 선분이다. 

- 빗변 : 주어진 각을 기준으로 직각삼각형의 직각으로 향하지 않는 선분이다. 

- 높이 : 주어진 각을 기준으로 그 각과 마주보는 선분이다.

!!! tldr ""

    사인($sine$) : 직각 삼각형의 빗변에 대한 높이의 비율이다.

- 위 그림에서 $\sin A = \frac{a}{h}$ 이다.

!!! tldr ""

    코사인($cosine$) : 직각 삼각형의 빗변에 대한 밑변의 비율이다.

- 위 그림에서 $\cos A = \frac{b}{h}$ 이다.

!!! tldr ""

    탄젠트($tangent$) : 직각 삼각형의 밑변에 대한 높이의 비율이다.

- 위 그림에서 $\tan A = \frac{a}{b}$ 이다.

!!! tldr ""

    코시컨트($cosecant$) : 직각 삼각형의 높이에 대한 빗변의 비율이다.

- $sin A$ 의 역수이다. 

- 위 그림에서 $\csc A = \frac{h}{a}$ 이다.

!!! tldr ""

    시컨트($secant$) : 직각 삼각형의 밑변 대한 빗변의 비율이다.

- $cos A$ 의 역수이다. 

- 위 그림에서 $\csc A = \frac{h}{b}$ 이다.

!!! tldr ""

    코탄젠트($cotangent$) : 직각 삼각형의 높이에 대한 밑변의 비율이다.

- $tan A$ 의 역수이다. 

- 위 그림에서 $\cot A = \frac{b}{a}$ 이다.

## 삼각함수

!!! tldr ""

    단위원(Unit circle) : 은 반지름의 길이가 $1$ 인 원이다.

- 해석기하학에서는 원점 $(0, 0)$ 을 중심으로 하는 반지름이 $1$ 인 원을 뜻한다.

!!! tldr ""

    삼각함수(trigonometric functions) : 각의 크기를 삼각비로 나타내는 함수이다.

- 삼각비는 직각삼각형의 세 변의 길이가 각에 대하여 일정한 비율을 유지하는 것을 보여준다. 이러한 각과 비율의 관계를 함수로 나타낸 것이 삼각함수이다. 

- 하지만 삼각비에서 육십분법을 사용하는 것과 달리 삼각함수는 라디안으로 나타낸 각을 사용한다.

- 또한 삼각비의 정의역이 $0 \degree < x < 90 \degree$ 인 것에 비해 삼각함수의 정의역은 실수집합이 된다.

!!! tldr ""

    삼각함수의 단위원을 통한 정의 : 반지름 $r$ 의 길이가 $1$ 인 단위원 위의 점 A $(x, y)$ 가 있다고 하자. 이때 $x$ 축과 점 $A$ 와 원점을 잇는 직선과의 각을 $\theta$ 라고하면 삼각함수를 다음과 같이 정의할 수 있다. 
    
    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Circle-trig6.svg/255px-Circle-trig6.svg.png)

- 사인함수($sin\theta$) : $sin\theta = \frac{y}{r}$

- 코사인함수($cos\theta$) : $cos\theta = \frac{x}{r}$

    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Sine_function001.svg/500px-Sine_function001.svg.png)

- 탄젠트함수($tan\theta$) : $tan\theta = \frac{sin \theta}{cos \theta} = \frac{y}{x}$

    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Tangent.svg/350px-Tangent.svg.png)

- 코시컨트함수($csc\theta$) : $csc\theta = \frac{1}{\sin \theta} = \frac{r}{y}$

    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Csc_drawing_process.gif/350px-Csc_drawing_process.gif)

- 시컨트함수($sec\theta$) : $sec\theta = \frac{1}{\cos \theta} = \frac{r}{x}$

- 코탄젠트함수($cot\theta$) : $cot\theta = \frac{1}{\tan \theta} = \frac{x}{y}$

    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Trigonometric_functions.svg/744px-Trigonometric_functions.svg.png)

## 삼각함수의 특수각

!!! tldr ""

    삼각함수의 특수각 : 삼각함수는 특수한 각에 대하여 다음의 값을 갖는다. 
    
    |  |$0 \degree$ |$\frac{\pi }{6}(30 \degree)$|$\frac{\pi }{4}(45 \degree)$|$\frac{\pi }{3}(60 \degree)$|$\frac{\pi }{2}(90 \degree)$|
    |:---:|:---:|:---:|:---:|:---:|:---:|
    | $\sin \theta$  | $0$ | $\frac{1}{2}$ | $\frac{1}{\sqrt[]{2}}$ | $\frac{\sqrt[]{3}}{2}$ | $1$ |
    | $\cos \theta$  | $1$ | $\frac{\sqrt[]{3}}{2}$ | $\frac{1}{\sqrt[]{2}}$ | $\frac{1}{2}$ | $0$ |
    | $\tan \theta$  | $0$ | $\frac{1}{\sqrt[]{3}}$ | $1$ | $\sqrt[]{3}$ | $undefined, \pm \infty$ |
    | $\csc \theta$  | $undefined$ | $2$ | $\sqrt[]{2}$ | $\frac{2}{\sqrt[]{3}}$ | $1$ |
    | $\sec \theta$  | $1$ | $\frac{2}{\sqrt[]{3}}$ | $\sqrt[]{2}$ | $2$ | $undefined$ |
    | $\cot \theta$  | $undefined$ | $\sqrt[]{3}$ | $1$ | $\frac{1}{\sqrt[]{3}}$ | $0$ |

## 삼각함수의 성질

!!! tldr ""

    삼각함수 사이의 관계

- $\tan \theta = \dfrac{\sin \theta }{\cos \theta }$

- $\sin ^2 \theta  + \cos ^2 \theta = 1$

    - 증명 

        반지름 길이가 $r$ 인 원에서 사인함수는 $\sin \theta = \frac{y}{r}$ 이고 코사인함수는 $\cos \theta  = \frac{x}{r}$ 이다. 이때 원의 방정식 $x^2 + y^2 = r^2$ 의 $x, y$ 를 각각 사인과 코사인에 대하여 풀면 $r^2 \sin \theta + r^2 \cos \theta = r^2$ 이므로 

        $$ \therefore  \sin ^2 \theta  + \cos ^2 \theta = 1$$ 

        이다.

- $1 + \tan ^{2} \theta = \sec ^{2} \theta$

    - 증명 

        $$\sin ^2 \theta  + \cos ^2 \theta = 1 $$

        $$ \iff $$

        $$\frac{1}{\cos ^{2} \theta}(\sin ^2 \theta  + \cos ^2 \theta) = \frac{1}{\cos ^{2} \theta} $$

        $$ \iff $$

        $$ \therefore \tan ^{2} \theta + 1 = \sec ^{2} \theta$$

- $1 + \cot ^{2} \theta = \csc ^{2} \theta$

    - 증명 

        $$\sin ^2 \theta  + \cos ^2 \theta = 1 $$

        $$ \iff $$

        $$\frac{1}{\sin ^{2} \theta}(\sin ^2 \theta  + \cos ^2 \theta) = \frac{1}{\sin ^{2} \theta} $$

        $$ \iff $$

        $$ \therefore 1 + \cot ^{2} \theta = \csc ^{2} \theta$$

### 삼각함수의 주기와 대칭성 

임의의 자연수 $n$ 에 대하여 다음이 성립한다.

!!! tldr ""

    $2n \pi  + \theta$

- $\sin (2n \pi + \theta) = \sin \theta$

- $\cos (2n \pi + \theta) = \cos \theta$

- $\tan (2n \pi + \theta) = \tan (n \pi + \theta) = \tan \theta$

!!! tldr ""

    $-\theta$

- $\sin (-\theta) = -\sin \theta$

- $\cos (-\theta) = \cos \theta$

- $\tan (-\theta) = -\tan \theta$

!!! tldr ""

    $\pi \pm \theta$

- $\sin (\pi + \theta) = -\sin \theta$

- $\cos (\pi + \theta) = -\cos \theta$

- $\tan (\pi + \theta) = \tan \theta$

- $\sin (\pi - \theta) = \sin \theta$

- $\cos (\pi - \theta) = -\cos \theta$

- $\tan (\pi - \theta) = -\tan \theta$

!!! tldr ""

    $\frac{\pi}{2} \pm \theta$

- $\sin (\frac{\pi}{2} + \theta) = \cos \theta$

- $\cos (\frac{\pi}{2} + \theta) = -\sin \theta$

- $\tan (\frac{\pi}{2} + \theta) = -\frac{1}{\tan \theta}$

- $\sin (\frac{\pi}{2} - \theta) = \cos \theta$

- $\cos (\frac{\pi}{2} - \theta) = \sin \theta$

- $\tan (\frac{\pi}{2} - \theta) = \frac{1}{\tan \theta}$

## 삼각방정식과 삼각부등식

!!! tldr ""

    삼각방정식 : 각의 크기에 미지수가 있는 삼각함수를 포함하는 방정식이다.

- 예시 

    $\sin x = \frac{1}{2}$

!!! tldr ""

    삼각부등식 : 각의 크기에 미지수가 있는 삼각함수를 포함하는 부등식이다.

- 예시 

    $\cos x > \frac{\sqrt[]{3}}{2}$

## 삼각형과 삼각함수와의 관계

!!! tldr ""

    삼각형과 삼각함수와의 관계 : 다음의 삼각형이 있을 때 삼각형과 삼각함수와의 일관된 관계가 존재한다. 
    
    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Acute_Triangle.svg/330px-Acute_Triangle.svg.png)



!!! tldr ""

    사인법칙(Law of sines) : 삼각형 $ABC$ 의 외접원의 반지름의 길이를 $R$ 이라 하면 삼각형 $ABC$ 의 세 변의 길이와 세 각의 크기 사이에 다음 관계가 존재하고 이를 사인법칙이라 한다.
    
    $$ \frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C} = 2R $$

- 증명 

    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Law_of_sines_proof.svg/400px-Law_of_sines_proof.svg.png" width="50%" height="auto">

    삼각형 $ABC$ 의 변 $c$ 위의 높이를 $h$ 라고 하면 $\sin A$ 는 빗변 $b$ 에 대한 높이 $h$ 의 비율 $\sin A = \dfrac{h}{b}$ 이다. 그러므로 

    $$ h = b \sin A $$

    인데, 이에따라 삼각형 $ABC$ 의 넓이 $K$ 는 

    $$ K = \dfrac{1}{2}ch=\dfrac{1}{2}bc \sin A $$

    이다. 그러므로 $2K = bc \sin A$ 인데 마찬가지의 방법으로 

    $$ 2K = bc \sin A = ac \sin B = ab \sin C $$

    를 얻는다. 이것을 $abc$ 로 나누면 $\dfrac{\sin A}{a} =\dfrac{\sin B}{b} =\dfrac{\sin C}{c}$ 을 얻고 이것의 역수를 취하면 사인법칙

    $$\dfrac{a}{\sin A} =\dfrac{b}{\sin B} =\dfrac{c}{\sin C}$$

    을 얻는다. ■ 

- 그리고 이 관계로부터 다음의 관계들이 도출된다. 

- $\sin A = \frac{a}{2R}$

- $\sin B = \frac{b}{2R}$ 

- $\sin C = \frac{c}{2R}$

- $a = 2R \sin A$

- $b = 2R \sin B$

- $c = 2R \sin C$

!!! tldr ""

    코사인법칙(Law of cosines) : 삼각형 $ABC$ 의 세 변의 길이와 세 각의 크기 사이에 다음의 관계가 존재하고 이를 코사인법칙이라 한다. 
    
    $$a^2 = b^2 + c^2 -2bc \cos A$$
    
    $$b^2 = c^2 + a^2 -2ca \cos B$$
    
    $$c^2 = a^2 + b^2 -2ab \cos C$$

- 코사인 법칙은 시점이 같은 두 벡터 $u, v$ 와 두 벡터가 이루는 각 $\theta$ 와 두 벡터의 종점을 이은 벡터 $w = u-v$ 에 대하여서도 적용된다.

    <img src="https://user-images.githubusercontent.com/16812446/86887866-392e0980-c134-11ea-9889-3e42cf40f31a.png" width="50%" height="auto">

    > 출처 : [Thomas' CALCULUS](https://www.amazon.com/Thomas-Calculus-Early-Transcendentals-13th/dp/0321884078) Figure12.21

    이때 벡터들의 길이 $|u|, |v|, |w|$ 와 $u,v$ 가 이루는 각 $\theta$ 에 대하여 코사인 법칙 

    $$ |w| ^{2} = |u|^{2}+|v|^{2}-2|u||v|\cos \theta $$

    가 성립한다.

- 증명 

    <img src="https://w.namu.la/s/8cdb7e58c9045a93487b9344d5c293f6dbd4490cbcecd8bee4e150402bdde278e491b4d20d72ca08f27c2dedcc9f2e08a18bddaa4c0bda69db51fe80f13b8c8aa8b46e373b790be34442adff9d35034756944778474f7b75dd3f6246bfa1c09f" width="50%" height="auto">

    위 삼각형에서 각각의 각 $A,B,C$ 와 마주보는 변의 길이를 $a,b,c$ 라고 하자.

    삼각형 $\Delta ABC$ 에 대하여 $\cos B = \dfrac{\overline{BH}}{c}, \cos C = \dfrac{\overline{CH}}{b}$ 이므로

    $$ a = \overline{BH}+\overline{CH} = c \cos B + b \cos C $$

    이 성립한다. 마찬가지의 방식으로

    $$ a = c \cos B + b \cos C $$

    $$ b = a \cos C + c \cos A $$

    $$ c = a \cos B + b \cos A $$

    을 얻는다. 이 세 등식에 각각 $a,b,c$ 를 곱하면

    $$ a ^{2} = ac \cos B + ab \cos C $$

    $$ b ^{2} = ab \cos C + bc \cos A $$

    $$ c ^{2} = ac \cos B + bc \cos A $$

    을 얻는다. 이때 첫째 등식에 둘째 등식과 셋째 등식을 빼면 $a ^{2}-b ^{2}- c ^{2}=-2bc \cos A$ 이므로

    $$ \therefore  a^2 = b^2 + c^2 -2bc \cos A$$

    을 얻는다. ■ 

    마찬가지의 방식으로 나머지 코사인 법칙도 쉽게 유도할 수 있다. ■ 

- 코사인 법칙으로부터 다음의 따름법칙을 쉽게 유도할 수 있다.

    $$\cos A = \frac{b^2+c^2-a^2}{2bc}$$

    $$\cos B = \frac{c^2+a^2-b^2}{2ca}$$

    $$\cos C = \frac{a^2+b^2-c^2}{2ab}$$

!!! tldr ""

    삼각형의 넓이와 삼각함수와의 관계 : 삼각형 $ABC$ 의 넓비를 $S$ 라 하고 삼각형 $ABC$ 의 외접원의 반지름을 $R$, 내접원의 반지름을 $r$ 이라 하면 다음의 관계가 존재한다.

- $S = \frac{1}{2}bc \sin A = \frac{1}{2} ca \sin B = \frac{1}{2} ab \sin C$

- $S = \frac{abc}{4R} = 2R^2 \sin A \sin B \sin C$

- $S = \frac{1}{2}r(a+b+c)$

- $S = \sqrt[]{s(s-a)(s-b)(s-c)}$ (단, $s = \frac{a+b+c}{2}$)

### 사각형과 삼각함수와의 관계

!!! tldr ""

    사각형의 넓이 : 두 대각선 $AC, BD$ 의 길이와 두 대각선이 이루는 각 $\theta$의 크기가 주어진 사각형 $ABCD$ 의 넓이 $S$ 는 다음과 같다.
    
    $$ S = \frac{1}{2} \times \overline{AC} \times \overline{BD} \times \sin \theta $$



!!! tldr ""

    평행사변형의 넓이 : 이웃하는 두변 $AB, BC$ 의 길이와 그 끼인각 $\theta$ 의 크기가 주어진 평행사변형 $ABCD$ 의 넓이 $S$ 는 다음과 같다.
    
    $$ S = \overline{AB} \times \overline{BC} \times \sin \theta $$

## 삼각함수의 덧셈정리

!!! tldr ""

    삼각함수의 덧셈정리 : 두 각 $\alpha, \beta$ 에 대하여 $\alpha + \beta, \alpha - \beta$ 의 삼각함수를 $\alpha, \beta$ 의 삼각함수로 다음과 같이 나타낼 수 있다.

- 사인함수의 덧셈정리 

    - $\sin(\alpha +\beta) = \sin \alpha \cos \beta + \cos \alpha \sin \beta$

    - $\sin (\alpha - \beta ) = \sin \alpha \cos \beta - \cos \alpha \sin \beta$

- 코사인함수의 덧셈정리 

    - $\cos (\alpha + \beta) = \cos \alpha \cos \beta - \sin \alpha \sin \beta$

    - $\cos (\alpha - \beta ) = \cos \alpha \cos \beta + \sin \alpha \sin \beta$

- 탄젠트함수의 덧셈정리 

    - $$\tan (\alpha + \beta) = \frac{\tan \alpha + \tan \beta }{1 - \tan \alpha \tan \beta }$$

    - $$\tan (\alpha - \beta) = \frac{\tan \alpha - \tan \beta }{1 + \tan \alpha \tan \beta }$$

- 우리는 특수각에 대한 삼각함수 값만을 알고 있었지만 이 덧셈정리들로 일반적인 각에 대한 삼각함수 값을 비교적 쉽게 구할 수 있게 되었다.

- 이 덧셈정리는 삼각함수의 미분과 적분에 활용된다. 

- 증명 

    ![](https://ww.namu.la/s/25287916f70ebb1ca9f932f4eb1edf48a08497c7bcb48cd58da722ebf3c5d4a7b86694ff5126861296b0642f3bd55f0db9aab0301cd1413a26c38641bffeb18ee6796941a31dff1b70d77a0f79e576c3d0e2422f7c553dc2953e8ceef220aedd)

    위 그림에서 양의 $x$ 축을 시초선으로하고 각의 크기가 $\beta$ 인 동경이 단위원과 만나는 점을 $B$, 각의 크기가 $\alpha$ 인 동경이 단위원과 만나는 점을 $C$ 라 하자. 

    그러면 각각의 좌표는 $B(\cos \beta, \sin \beta), C(\cos \alpha, \sin \alpha)$ 이다. 

    이때 두 점 사이의 거리는 

    $$ \overline{BC} ^{2} = (\cos \beta - \cos \alpha) ^{2} + (\sin \beta -\sin \alpha ) ^{2} = (\cos ^{2} \alpha + \sin ^{2} \alpha ) + (\cos ^{2} \beta + \sin ^{2} \beta ) - 2(\cos \alpha \cos \beta + \sin \alpha \sin \beta ) $$

    $$ = 1 + 1 - 2(\cos \alpha \cos \beta + \sin \alpha \sin \beta ) $$

    $$ = 2 - 2(\cos \alpha \cos \beta + \sin \alpha \sin \beta ) $$

    이다. 그런데 삼각형의 세 변의 길이와 한 각의 크기 사이의 관계를 보여주는 코사인 법칙에 의하여 

    $$ \overline{BC} ^{2} = 1 ^{2} + 1 ^{2} - 2 \circ 1 \circ 1 \cos (\alpha -\beta ) $$

    $$ = 2 - 2 \cos (\alpha -\beta ) $$

    이다. 따라서 

    $$ 2 - 2 \cos (\alpha -\beta ) = 2 - 2(\cos \alpha \cos \beta + \sin \alpha \sin \beta ) $$

    $$ \iff $$

    $$ \therefore  \cos (\alpha -\beta ) = \cos \alpha \cos \beta + \sin \alpha \sin \beta $$

    이다. 이 결론은 임의의 두 각 $\alpha, \beta$ 에 대하여 성립하므로 $\beta$ 를 $- \beta$ 로 두면 

    $$ \therefore  \cos (\alpha +\beta ) = \cos \alpha \cos \beta - \sin \alpha \sin \beta $$

    이다. 한편 $\sin \theta = \cos (\frac{\pi}{2} - \theta)$ 이므로

    $$ \sin (\alpha + \beta) = \cos \{\frac{\pi}{2} - (\alpha + \beta)\}= \cos \{(\frac{\pi}{2} - \alpha) - \beta\} $$

    $$ = \cos (\frac{\pi}{2}-\alpha)\cos \beta  + \sin (\frac{\pi}{2}-\alpha) \sin \beta $$

    그런데 $\sin (\frac{\pi }{2} - \theta) = \cos \theta,\cos (\frac{\pi }{2} - \theta ) = \sin \theta$ 이므로 

    $$ \therefore \sin (\alpha + \beta) = \sin \alpha\cos \beta  + \cos \alpha \sin \beta $$

    이다. 이 결론은 임의의 두 각 $\alpha, \beta$ 에 대하여 성립하므로 $\beta$ 를 $- \beta$ 로 두면 

    $$ \therefore \sin (\alpha - \beta) = \sin \alpha\cos \beta  - \cos \alpha \sin \beta $$

    한편 $\tan \theta = \frac{\sin \theta }{\cos \theta }$ 이므로 

    $$ \tan (\alpha + \beta ) = \frac{\sin (\alpha + \beta )}{\cos (\alpha + \beta)} = \frac{\sin \alpha\cos \beta  + \cos \alpha \sin \beta }{\cos \alpha \cos \beta - \sin \alpha \sin \beta } $$

    $$ = \frac{(\sin \alpha\cos \beta  + \cos \alpha \sin \beta )}{(\cos \alpha \cos \beta - \sin \alpha \sin \beta )} \frac{ \div \cos \alpha \cos \beta }{\div \cos \alpha \cos \beta } $$

    $$ \iff $$

    $$ \therefore \tan (\alpha + \beta ) = \frac{\tan \alpha - \tan \beta }{1 + \tan \alpha \tan \beta } $$

    이다. 이 결론은 임의의 두 각 $\alpha, \beta$ 에 대하여 성립하므로 $\beta$ 를 $- \beta$ 로 두면 

    $$ \therefore \tan (\alpha - \beta ) = \frac{\tan \alpha + \tan \beta }{1 - \tan \alpha \tan \beta } $$

    > 증명 방향을 보면 알 수 있지만 한 각을 두 각으로 나눌 수 있게끔 하는 관계를 유도하는 것이 증명의 목표이다. 이처럼 증명과 그것에 따라 정립되는 수식은 목적에 따라 움직인다. 

- 예시 

    $$ \sin 75 \degree = \sin (45 \degree + 30 \degree) = \sin 45 \degree \cos 30 \degree + \cos 45 \degree \sin 30 \degree = \frac{\sqrt[]{2}}{2} \circ \frac{\sqrt[]{3}}{2} + \frac{\sqrt[]{2}}{2}\circ \frac{1}{2} = \frac{\sqrt[]{6}+\sqrt[]{2}}{4} $$

    $$ \cos 75 \degree = \cos (45 \degree + 30 \degree) = \cos 45 \degree \cos 30 \degree - \sin 45 \degree \sin 30 \degree = \frac{\sqrt[]{2}}{2} \circ \frac{\sqrt[]{3}}{2} - \frac{\sqrt[]{2}}{2}\circ \frac{1}{2} = \frac{\sqrt[]{6}-\sqrt[]{2}}{4} $$

    $$ \tan 15 \degree = \tan(45 \degree - 30 \degree ) = \frac{\tan 45 \degree - \tan 30  \degree }{1 + \tan 45 \degree \tan 30 \degree } = \frac{1 - \frac{1}{\sqrt[]{3}}}{1 + 1 \circ \frac{1}{\sqrt[]{3}}} = \frac{\sqrt[]{3}-1}{\sqrt[]{3}+1} = 2 - \sqrt[]{3} $$

!!! tldr ""

    배각의 공식 : 삼각함수의 덧셈정리로부터 다음의 파생 관계를 얻을 수 있다.

- $\sin 2 \alpha = 2 \sin \alpha \cos \alpha$

    - 증명 

        사인함수의 덧셈정리

        $$\sin(\alpha +\beta) = \sin \alpha \cos \beta + \cos \alpha \sin \beta$$

        는 임의의 두 각 $\alpha, \beta$ 에 대하여 성립하므로 $\beta = \alpha$ 로 두면 

        $$ \therefore \sin 2 \alpha = 2 \sin \alpha \cos \alpha $$

        이다. 

- $\cos 2 \alpha = \cos ^{2} \alpha - \sin ^{2} \alpha = 2 \cos ^{2} \alpha -1 = 1 - 2 \sin ^{2} \alpha$

    - 증명 

        코사인함수의 덧셈정리

        $$\cos (\alpha + \beta) = \cos \alpha \cos \beta - \sin \alpha \sin \beta$$

        는 임의의 두 각 $\alpha, \beta$ 에 대하여 성립하므로 $\beta = \alpha$ 로 두면 

        $$ \therefore \cos 2 \alpha = \cos ^{2}\alpha - \sin ^{2} \alpha  $$

        그런데 $\sin ^{2}\theta  + \cos ^{2} \theta  = 1$ 이므로 $\sin ^{2}\theta  = 1 - \cos ^{2} \theta$ 에서

        $$ \therefore \cos 2 \alpha = 2\cos ^{2}\alpha - 1  $$

        이고 $\cos ^{2} \theta  = 1 - \sin ^{2} \theta$ 에서

        $$ \therefore \cos 2 \alpha = 1 - 2\sin ^{2}\alpha $$

        이다. 

- $\tan 2 \alpha = \frac{2 \tan \alpha }{1 - \tan ^{2}\alpha }$

    - 증명 

        탄젠트 함수의 덧셈정리

        $$\tan (\alpha + \beta) = \frac{\tan \alpha + \tan \beta }{1 - \tan \alpha \tan \beta }$$

        는 임의의 두 각 $\alpha, \beta$ 에 대하여 성립하므로 $\beta = \alpha$ 로 두면 

        $$ \therefore  \tan 2\alpha = \frac{2\tan \alpha}{1 - \tan ^{2} \alpha}$$

        이다.

- 이 공식은 차수가 $2$ 인 식과 차수가 $1$ 인 식이 갖는 관계를 보여주므로 차수를 변환시키면 유용한 상황에서 사용된다. 

    > 따라서 임의의 차수를 원하는 차수로 변환하기 위한 목적으로 공식을 더 유용하게 변환할 수 있다. 

    - 삼각방정식, 적분법 등에서 사용된다. 

    - 배각의 공식 뿐만 아니라 $3$ 배각의 공식, $4$ 배각의 공식, $n$ 배각의 공식이 존재한다.

!!! tldr ""

    반각의 공식 : 배각의 공식에서 다음의 파생관계를 얻을 수 있다.

- $\sin ^{2} \frac{\alpha }{2} = \frac{1 - \cos \alpha }{2}$

    - 증명 

        $\cos 2 \alpha = 1 - 2 \sin ^{2} \alpha$ 에서

        $$ \sin ^{2} \alpha  = \frac{1 - \cos 2 \alpha }{2} $$

        를 얻는다. 이때 $\alpha$ 대신 $\frac{\alpha }{2}$ 를 대입하면

        $$ \therefore  \sin ^{2} \frac{\alpha }{2} = \frac{1 - \cos \alpha }{2} $$

        이다.

- $\cos ^{2}\frac{\alpha }{2} = \frac{1+\cos \alpha }{2}$

    - 증명 

        $\cos 2 \alpha = 2 \cos ^{2} \alpha -1$ 에서 

        $$ \cos ^{2} \alpha = \frac{1 + \cos 2 \alpha}{2} $$

        를 얻는다. 이때 $\alpha$ 대신 $\frac{\alpha }{2}$ 를 대입하면

        $$ \therefore  \cos ^{2}\frac{\alpha }{2} = \frac{1+\cos \alpha }{2} $$

        이다.

- $\tan ^{2} \frac{\alpha }{2} = \frac{1-\cos \alpha }{1+\cos \alpha }$

    - 증명 

        탄젠트는 코사인 값에 대한 사인 값의 비이므로 

        $$ \tan ^{2} \frac{\alpha }{2} = \frac{\sin ^{2} \frac{\alpha }{2}}{\cos ^{2} \frac{\alpha }{2}} = \frac{\frac{1-\cos \alpha }{2}}{\frac{1+\cos \alpha }{2}} $$ 

        에서

        $$ \therefore  \tan ^{2} \frac{\alpha }{2} = \frac{\sin ^{2} \frac{\alpha }{2}}{\cos ^{2} \frac{\alpha }{2}} = \frac{\frac{1-\cos \alpha }{2}}{\frac{1+\cos \alpha }{2}} = \frac{1-\cos \alpha }{1+\cos \alpha } $$

        이다. 

- 반각의 공식은 모든 식이 $\cos \alpha$ 로 표현된다. 

    - 즉 이 관계 덕분에 $\cos \alpha$ 값만 알면 $\sin ^{2} \frac{\alpha }{2}, \cos ^{2} \frac{\alpha }{2}, \tan ^{2} \frac{\alpha }{2}$ 를 알 수 있다. 

## 삼각함수의 합성

삼각함수의 합성 

**구체화 필요**
