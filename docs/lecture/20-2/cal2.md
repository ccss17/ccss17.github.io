# 역삼각함수

!!! tldr ""

    역함수(inverse function) : 함수 $f: A \to B$ 에 대해 함수 $g: B \to A$ 가 있어서 $\forall a \in A, g(f(a)) = a \land \forall \in B f(g(b)) = b$ 이면 $g$ 를 $f$ 의 역함수라고 한다.

- $f$ 의 역함수를 $f ^{-1}$ 라고 표시한다.

- 어떤 함수가 역함수를 가지려면 일대일 대응이어야 한다. 

!!! tldr ""

    역사인함수(arcsine) : 정의역 $\bigg [- \dfrac{\pi }{2}, \dfrac{\pi }{2}\bigg ]$ 을 갖는 사인함수 $f:\bigg [-\dfrac{\pi }{2},\dfrac{\pi }{2}\bigg ] \to [-1, 1], x \mapsto \sin x$ 의 역함수 
    
    $$f ^{-1}: [-1, 1] \to \bigg [- \dfrac{\pi }{2}, \dfrac{\pi }{2}\bigg ], x \mapsto \arcsin x = \sin ^{-1}x$$
    
    이다.

- 역함수는 일대일 대응이므로 특별한 언급이 없는 한 역사인함수를 정의하기 위하여 사인함수의 정의역을 $\bigg [- \dfrac{\pi }{2}, \dfrac{\pi }{2}\bigg ]$ 로 한다.

- 예시 

    $$ \arcsin 1 = \dfrac{\pi }{2}, \sin ^{-1} \dfrac{1}{2} = \dfrac{\pi }{6} $$

!!! tldr ""

    역코사인함수(arccosine) : 정의역 $[0, \pi]$ 을 갖는 코사인함수 $y = f(x) = \cos x$ 의 역함수 

    $$f ^{-1}: [-1, 1] \to [0, \pi], x \mapsto \arccos x = \cos ^{-1}x$$
    
    이다.

- 다음 그림을 보자.

    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Arcsine_Arccosine.svg/252px-Arcsine_Arccosine.svg.png)
    
!!! tldr ""

    역탄젠트함수(arctangent) : 정의역 $\bigg (-\dfrac{\pi }{2}, \dfrac{\pi }{2}\bigg )$ 을 갖는 탄젠트함수 $y = f(x) = \tan x$ 의 역함수 

    $$f ^{-1}: \R \to \bigg (-\dfrac{\pi }{2}, \dfrac{\pi }{2}\bigg ), x \mapsto \arctan x = \tan ^{-1}x$$
    
    이다.

!!! tldr ""

    역코탄젠트함수(arccotangent) : 정의역 $[0, \pi]$ 을 갖는 코탄젠트함수 $y = f(x) = \cot x$ 의 역함수 

    $$ f ^{-1}: \R \to (0, \pi), x \mapsto \operatorname{arccot} x = \cot ^{-1} x $$
    
    이다.

- 다음 그림을 보자.

    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Arctangent_Arccotangent.svg/441px-Arctangent_Arccotangent.svg.png)

!!! tldr ""

    역시컨트함수(arcsecant) : 시컨트함수 $y = f(x) = \sec x$ 의 역함수 

    $$ f ^{-1}: (\infty, -1] \cup [1, \infty) \to \bigg [- \dfrac{\pi }{2}, 0 \bigg ) \cup \bigg (0,\dfrac{\pi }{2}\bigg], x \mapsto \operatorname{arcsec} x = \sec ^{-1} x $$
    
    이다.

!!! tldr ""

    역코시컨트함수(arcsecant) : 코시컨트함수 $y = f(x) = \csc x$ 의 역함수 

    $$ f ^{-1}: (\infty, -1] \cup [1, \infty) \to \bigg [0, - \dfrac{\pi }{2}\bigg ) \cup \bigg (\dfrac{\pi }{2}, \pi \bigg], x \mapsto \operatorname{arccsc} x = \csc ^{-1} x $$
    
    이다.

- 다음 그림을 보자.

    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Arcsecant_Arccosecant.svg/441px-Arcsecant_Arccosecant.svg.png)

# 역삼각함수 미분

!!! tldr ""

    역사인함수의 미분 : $y = \arcsin x$ 의 미분은 

    $$ (\arcsin x)' = \dfrac{1}{\sqrt[]{1-x ^{2}}} $$

    이다.

- 증명

    함수 $y = \arcsin x$ 에 대하여 $\sin y = \sin (\arcsin x) = x$ 이다. 양변을 $x$ 로 미분하면 합성함수의 미분에 의하여 

    $$ \cos y \dfrac{dy}{dx} = 1 $$

    이다. 그러므로 $\cos y \neq 0$ 일 때 

    $$ \dfrac{dy}{dx} = \dfrac{1}{\cos y} = \dfrac{1}{\pm \sqrt[]{1 - \sin ^{2}y}} = \dfrac{1}{\pm \sqrt[]{1- x ^{2}}}   $$

    이다. 그런데 $y = \arcsin x$ 의 치역이 $- \pi /2 \leq y \leq \pi /2$ 이므로 $\cos y \geq 0$ 이다. 그러므로 

    $$ \therefore \dfrac{d}{dx}\arcsin x = \dfrac{1}{\pm \sqrt[]{1- x ^{2}}} , |x| < 1$$

    이다.

!!! tldr ""

    역코사인함수의 미분 : $y = \arccos x$ 의 미분은 

    $$ (\arccos x)' = - \dfrac{1}{\sqrt[]{1-x ^{2}}} $$

    이다.

!!! tldr ""

    역탄젠트함수의 미분 : $y = \arctan x$ 의 미분은 

    $$ (\arctan x)' = \dfrac{1}{\sqrt[]{1+x ^{2}}} $$

    이다.

- 증명 

    $$ y = \arctan x \implies \tan y = x $$

    $$ \implies \dfrac{d \tan y}{dx} = \sec ^{2}y \dfrac{dy}{dx}=1 $$

    $$ \therefore \dfrac{dy}{dx} = \dfrac{1}{\sec ^{2}y} = \dfrac{1}{1+x ^{2}} $$

!!! tldr ""

    역코탄젠트함수의 미분 : $y = \operatorname{arccot}  x$ 의 미분은 

    $$ (\operatorname{arccot}  x)' = -\dfrac{1}{\sqrt[]{1+x ^{2}}} $$

    이다.

# 쌍곡함수(hyperbolic function)

!!! tldr ""

    쌍곡사인함수(hyperbolic sine) : $\sinh x = \dfrac{e ^{x} - e ^{-x}}{2}$

!!! tldr ""

    쌍곡코사인함수(hyperbolic cosine) : $\cosh x = \dfrac{e ^{x} + e ^{-x}}{2}$

- 쌍곡함수를 $x = \cosh u, y = \sinh u$ 로 두면

    $$ x ^{2} - y ^{2} = \cosh ^{2}u - \sinh ^{2}u = \dfrac{1}{4}(e ^{2u} + 2 + e ^{-2u}) - \dfrac{1}{4}(e ^{2u} - 2 + e ^{-2u}) =  1 $$

    이 되어 쌍곡선에 대한 적절한 매개화(parametrization) 이 가능하게 되어 쌍곡 함수라는 이름이 붙었다.
    
    다음 그래프는 쌍곡선을 이루는 $x ^{2} - y ^{2} = 1$ 의 그래프이다.

    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Hyperbolic_functions-2.svg/465px-Hyperbolic_functions-2.svg.png)

!!! tldr ""

    쌍곡탄젠트함수(hyperbolic tangent) : $\tanh x = \dfrac{\sinh x}{\cosh x} = \dfrac{e ^{x} - e ^{-x}}{e ^{x}+e ^{-x}}$

- 그래프 

    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Sinh_cosh_tanh.svg/450px-Sinh_cosh_tanh.svg.png)

!!! tldr ""

    쌍곡코시컨트함수(hyperbolic cosecant) : $\operatorname{csch} x = \dfrac{1}{\sinh x} = \dfrac{2}{e ^{x} - e ^{-x}}$

!!! tldr ""

    쌍곡시컨트함수(hyperbolic secant) : $\operatorname{csch} x = \dfrac{1}{\cosh x} = \dfrac{2}{e ^{x} + e ^{-x}}$

!!! tldr ""

    쌍곡코탄젠트함수(hyperbolic cotangent) : $\coth  x = \dfrac{\cosh  x}{\sinh  x} = \dfrac{e ^{x} + e ^{-x}}{e ^{x}-e ^{-x}}$

!!! tldr ""

    쌍곡함수 성질 : 쌍곡함수에 관해 다음 성질이 성립한다.

- $\cosh ^{x} - \sinh ^{2}x = 1$

- $1 - \tanh ^{2} = \operatorname{sech} ^{2}x$

- $\coth ^{2}x -1 = \operatorname{csch} ^{2}x$

- $\cosh x$ 는 짝함수이다.

    $$ \because \cosh (-x) = \dfrac{e ^{-x} + e ^{-(-x)}}{2} = \dfrac{e ^{-x} + e ^{x}}{2} = \cosh x $$

- $\sinh x$ 는 홀함수이다.

    $$ \because \sinh (-x) = \dfrac{e ^{-x} - e ^{-(-x)}}{2} = - \bigg (\dfrac{e ^{-x} - e ^{x}}{2}\bigg ) = -\sinh x $$

- $\sinh (x+y) = \sinh x \cosh y + \cosh x \sinh y \implies  \sinh 2x = 2 \sinh x \cosh x$

    $$ \because \sinh x \cosh y + \cosh x \sinh y = \dfrac{e ^{x}-e ^{-x}}{2}\dfrac{e ^{y}+e ^{-y}}{2} +  \dfrac{e ^{x}+e ^{-x}}{2}\dfrac{e ^{y}-e ^{-y}}{2} $$

    $$ = \dfrac{1}{4}(e ^{x+y}+e ^{x-y}-e ^{-x+y}- e ^{-x-y} + e ^{x+y}-e ^{x-y}+e ^{-x+y} - e ^{-x-y}) $$

    $$ \dfrac{2}{4}(e ^{x+y} - e ^{-(x+y)}) = \sinh (x+y) $$

- $\cosh  (x+y) = \cosh  x \cosh y + \sinh  x \sinh y \implies  \cosh  2x = \cosh ^{2} x + \sinh ^{2} x$

!!! tldr ""

    쌍곡사인함수의 미분 : $(\sinh x)' = \cosh x$

- 증명

    $$\dfrac{d}{dx}\sinh x = \dfrac{d}{dx} \dfrac{e ^{x}-e ^{-x}}{2} = \dfrac{e ^{x} + e ^{-x}}{2} = \cosh x$$

!!! tldr ""

    쌍곡코사인함수의 미분 : $(\cosh x)' = \sinh x$

- 증명

    $$\dfrac{d}{dx}\cosh x = \dfrac{d}{dx} \dfrac{e ^{x}+e ^{-x}}{2} = \dfrac{e ^{x} - e ^{-x}}{2} = \sinh x$$

!!! tldr ""

    쌍곡탄젠트함수의 미분 : $(\tanh  x)' = \operatorname{sech} ^{2} x$

- 증명

    $$\dfrac{d}{dx}\tanh  x = \dfrac{d}{dx} \dfrac{\sinh x}{\cosh x} = \dfrac{\cosh x \cosh x - \sinh x \sinh x}{\cosh ^{2}x} = \operatorname{sech} ^{2} x$$

# 쌍곡함수의 적분

!!! tldr ""

    쌍곡사인함수의 부정적분 : $\displaystyle \int_{}^{}\sinh x dx = \cosh x + C$

- 예시 

    $$ \int_{}^{}\sinh ^{2}xdx = \int_{}^{}\bigg (\dfrac{e ^{x} - e ^{-x}}{2}\bigg )^{2}dx = \int_{}^{}\dfrac{e ^{2x} + e ^{-2x} -2}{4}dx $$

    $$ \dfrac{1}{8} ( e ^{2x} - e ^{-2x}) - \dfrac{1}{2}x + C = \dfrac{\sinh 2x}{4} - \dfrac{x}{2} + C $$

!!! tldr ""

    쌍곡코사인함수의 부정적분 : $\displaystyle \int_{}^{}\cosh  x dx = \sinh x + C$

!!! tldr ""

    쌍곡시컨트 제곱함수의 부정적분 : $\displaystyle \int_{}^{}\operatorname{sech} ^{2} x dx = \tanh  x + C$

!!! tldr ""

    쌍곡코탄젠트함수의 부정적분 : $\displaystyle \int_{}^{}\operatorname{coth} x dx = \ln |\sinh x|+ C$

- 증명 

    $\int_{}^{}\coth x dx = \int_{}^{}\dfrac{\cosh x}{\sinh x}dx$ 이므로 $u = \sinh x, du = \cosh x dx$ 로 두면

    $$ \therefore \int_{}^{}\dfrac{du}{u} = ln|u| + C = \ln |\sinh x|+C $$

    이다.

# 역쌍곡함수

!!! tldr ""

    역쌍곡사인함수 : 쌍곡사인함수 $y = \sinh x$ 의 역함수는

    $$ y = \sinh ^{-1} x = \ln (x + \sqrt[]{x ^{2} + 1}) $$

    이다.

- $y = \sinh x$ 는 일대일 대응이므로 역함수를 갖는다.

- 증명

    $y = \sinh ^{-1} x$ 에서 $\sinh y = x$ 이므로 $\sinh y = \dfrac{e ^{y} - e ^{-y}}{2} = x$ 을 얻는다. 양변에 $2 e ^{y}$ 를 곱하여

    $$ e ^{2y} - 2x e ^{y} - 1 = 0 $$

    를 얻고 이에 따라 

    $$ e ^{y} = \dfrac{2x \pm \sqrt[]{4 x ^{2} + 4}}{2} = x \pm \sqrt[]{x ^{2} + 1} $$

    을 얻는데, $e ^{y}$ 는 항상 양수이므로 

    $$ e ^{y} = x + \sqrt[]{x ^{2} + 1} $$

    이다. 그러므로 

    $$ \therefore y = \ln (x + \sqrt[]{x ^{2} + 1}) $$

    이다.

!!! tldr ""

    역쌍곡코사인함수 : 쌍곡코사인함수 $y = \cosh x$ 의 역함수는 정의역 $x \geq 1$ 에서

    $$ y = \cosh ^{-1} x = \ln (x + \sqrt[]{x ^{2} - 1}) $$

    이다.

- 증명

    $y = \cosh ^{-1} x$ 에서 $\cosh y = x$ 이므로 $\cosh y = \dfrac{e ^{y} + e ^{-y}}{2} = x$ 을 얻는다. 양변에 $2 e ^{y}$ 를 곱하여

    $$ e ^{2y} - 2x e ^{y} + 1 = 0 $$

    를 얻고 이에 따라 

    $$ e ^{y} = \dfrac{2x \pm \sqrt[]{4 x ^{2} - 4}}{2} = x \pm \sqrt[]{x ^{2} - 1} \qquad (x \geq 1) $$

    을 얻는다. 이때 $y \geq 0$ 이므로 $e ^{y} \geq 1$ 인데 $x > 1$ 일 때 $x - \sqrt[]{x ^{2} - 1}$ 이므로

    $$ e ^{y} = x + \sqrt[]{x ^{2} - 1} $$

    이다. 그러므로 

    $$ \therefore y = \ln (x + \sqrt[]{x ^{2} - 1}) $$

    이다.

!!! tldr ""

    역쌍곡탄젠트함수 : 쌍곡탄젠트함수 $y = \tanh x$ 의 역함수는 정의역 $|x| < 1$ 에서

    $$ y = \tanh ^{-1} x = \dfrac{1}{2} \ln \dfrac{1+x}{1-x} $$

    이다.

- 증명

    $-1 < \tanh y < 1$ 이므로 $|x| < 1$ 이다. $\tanh y = \dfrac{e ^{y} - e ^{-y}}{e ^{y} + e ^{-y}} = x$ 에 $e ^{y}$ 를 곱하면

    $$ \dfrac{e ^{2y} - 1}{e ^{2y} + 1} = x $$

    을 얻는다. 이로부터

    $$ e ^{2y} - 1 = x e ^{2y} + x \implies (1 - x) e ^{2y} = x + 1 \implies e ^{2y} = \dfrac{1+x}{1-x} $$ 
    
    $$ \therefore y = \dfrac{1}{2}\ln \bigg (\dfrac{1+x}{1-x}\bigg ) \quad (|x| < 1) $$

    을 얻는다.

# 역쌍곡함수 미분

!!! tldr ""

    역쌍곡사인함수 미분 : $\displaystyle \frac{d}{dx} (\sinh ^{-1} x) = \dfrac{1}{\sqrt[]{x^2 + 1}}$

- 역쌍곡함수들의 미분은 로그함수를 이용한 역함수 표현법을 사용하면 쉽게 구할 수 있다.

!!! tldr ""

    역쌍곡코사인함수 미분 : $\displaystyle \frac{d}{dx} (\cosh ^{-1} x) = \dfrac{1}{\sqrt[]{x ^{2} -1 }} \quad (x > 1)$

!!! tldr ""

    역쌍곡탄젠트함수 미분 : $\displaystyle \frac{d}{dx} (\tanh ^{-1} x) = \dfrac{1}{1 - x ^{2}} \quad (|x| < 1)$

- 증명

    $$ \frac{d}{dx}  (\tanh ^{-1} x) = \dfrac{1}{2}\dfrac{d}{dx} (\ln (1+x) - \ln (1-x)) = \dfrac{1}{2} \bigg (\dfrac{1}{1+x}+\dfrac{1}{1-x}\bigg ) $$

    $$ \dfrac{1}{2}\bigg (\dfrac{2}{1 - x ^{2}}\bigg ) = \dfrac{1}{1-x ^{2}} $$

!!! tldr ""

    역쌍곡코탄젠트함수 미분 : $\displaystyle \frac{d}{dx} (\coth ^{-1} x) = \dfrac{1}{1 - x ^{2}} \quad (|x| > 1)$

!!! tldr ""

    역쌍곡시컨트함수 미분 : $\displaystyle \frac{d}{dx} (\operatorname{sech} ^{-1} x) = \dfrac{1}{x \sqrt[]{1 - x ^{2}} } \quad (0 < x < 1)$

!!! tldr ""

    역쌍곡코시컨트함수 미분 : $\displaystyle \frac{d}{dx} (\operatorname{csch} ^{-1} x) = \dfrac{1}{|x| \sqrt[]{1 + x ^{2}} } \quad (x \neq 0)$

# 미분 방정식

!!! tldr ""

    미분 방정식 : 미분이 들어간 방정식이다.

- 예시

    $\dfrac{dy}{dx} = e ^{x}$ 는 미분이 들어간 방정식이다. 이 방정식을 푼다는 것은 $y$ 가 무엇인지 구하는 것이다. 따라서 적분을 하면 미분방정식의 해 $y = e ^{x} + C$ 를 얻는다.

    $\dfrac{dy}{dt} = \sinh t$ 는 변수 $t$ 에 대한 미분방정식이다. 이 방정식을 풀면 미분방정식의 해 $y = \cosh t + C$ 를 얻는다.

- 예시 

    $\dfrac{dy}{dt} = 3y$ 의 해는 $y = e ^{3t}$ 가 될 수도 있고, $y = 5e ^{3t}$ 가 될 수도 있다. 그러므로 이 해들을 일반적으로 $y = C e ^{3t}$ 라고 표현하고 이것을 일반해라고 한다.

    이때 초깃값을 가령 $y(0) = 1$ 로 주면 $y(0) = C e ^{0} = C$ 가 되어 $C = 1$ 을 얻는다. 이렇게 초깃값이 주어지면 초깃값 문제라고 한다.

    이 미분방정식을 적분을 통하여 풀 수도 있다. 좌변에 모두 $y$ 가 있게 하고 우변에 모두 독립변수 $t$ 가 있게 하면

    $$ \dfrac{dy}{dt} = 3y \iff \dfrac{1}{y}dy = 3dt $$

    인데, 좌변과 우변을 적분하면 

    $$ \int_{}^{}\dfrac{1}{y}dy = \int_{}^{}3dt \iff \ln |y| = 3t + C$$

    를 얻는다. 명시하지는 않았지만 이 미분방정식은 인구 비례 형태를 나타내는 것이므로 $y$ 가 양수이다. 따라서 

    $$ \ln y = 3t + C \iff y = e ^{3t + C} = e ^{C} \cdot e ^{3t} $$

    을 얻는데 $e ^{C}$ 는 상수이므로 그냥 $C$ 로 표현하면 

    $$ \therefore  y = C e ^{3t} $$

    를 얻는다.

!!! tldr ""

    1계 미분방정식 : $\dfrac{dy}{dt} = y'$ 로 두었을 때 방정식에 $y', y$ 가 있는 방정식이다.

- 예시 

    $10 + t ^{2}\sin t + e ^{t}y' = 0$ 은 1계 미분방정식이다.

!!! tldr ""

    2계 미분방정식 : $\bigg (\dfrac{d ^{2}y}{d t ^{2}}, \dfrac{dy}{dt}, y\bigg ) = (y'', y', y)$ 로 두었을 때 방정식에 $y'',y',y$ 가 있는 방정식이다.

- 예시 

    $(\ln t) ^{2}y + y' + y'' = 3$ 은 2계 미분방정식이다.

!!! tldr ""

    선형 1계 미분방정식 : $y', y$ 와 $t$ 에 대한 함수 $A(t), B(t), C(t)$ 대하여 1차식 

    $$ A(t) y' + B(t) y + C(t) = 0 $$

    꼴로 주어진 미분방정식이다.

- 보통 $A(t) y' + B(t) y + C(t) = 0$ 꼴을 편의상 $y' + P(t) y = Q(t)$ 로 고쳐서 사용한다.

- 예시 

    1계 선형 미분방정식 $y' = \dfrac{1}{t} y = t \quad (t> 0)$ 를 풀어보자.

    $$ ty' + y = t ^{2} $$

!!! tldr ""

    1계 미분방정식의 해 : 미분방정식 $\dfrac{dy}{dt} + P(t)y = Q(t)$ 에 대하여 적분인자(integrating factor) 

    $$ \mu = \pm e ^{\int_{}^{}P(t)dt} $$

    를 양변에 곱하면 미분방정식의 해를 간단히 구할 수 있다.

- 예시

    미분방정식 $\dfrac{dy}{dt} + \dfrac{1}{t}y = t \quad (t > 0)$ 의 일반해를 구해보자. 양변에 $t$ 를 곱하면 

    $$ t \dfrac{dy}{dt} + y = t ^{2} $$

    이다. 이때 좌변은 $ty$ 를 $t$ 에 대하여 합성함수의 미분한 결과

    $$ \dfrac{d}{dt}(ty) = t'y + ty' = y + t \dfrac{dy}{dt} = t \dfrac{dy}{dt} + y $$

    와 같다. 그러므로 미분방정식을 

    $$ \dfrac{d}{dt}(ty) = t ^{2} $$

    로 쓸 수 있다. 이때 양변을 $t$ 에 대하여 적분하면

    $$ \int_{}^{}\dfrac{d}{dt}(ty) dt = \int_{}^{} t ^{2}dt $$

    $$ \iff ty = \dfrac{1}{3}t ^{3} + C $$

    를 얻는다. 따라서 일반해는

    $$ \therefore \dfrac{1}{3}t ^{2} + \dfrac{C}{t} \quad (t > 0) $$

    이다.

- 증명 

    1계 미분방정식 
    
    $$\dfrac{dy}{dt} + P(t)y = Q(t)$$ 
    
    의 해를 구하는 방법을 살펴보자. 먼저 위 예시로 우리가 알 수 있는 것은 미분방정식에 적당한 함수 $\mu (t)$ 를 곱하면 좌변이 어떤 함수의 미분 꼴이 되어 양변을 적분하여 간단히 해를 구할 수 있게 된다는 것이다. 이것을 식으로 표현하면 

    $$ \mu (t) \bigg (\dfrac{dy}{dt} + P(t)y\bigg ) = \mu (t)Q(t) $$

    인데, 우리가 원하는 것은 결과적으로 

    $$ \mu (t) \bigg (\dfrac{dy}{dt} + P(t)y\bigg ) = \dfrac{d}{dt}(\mu (t) y) $$

    이 되는 $\mu (t)$ 이다. 이 식을 전개해보면

    $$ \iff \mu y' + \mu P(t)y = \mu y' + \mu ' y $$

    $$ \iff \mu P(t) y = \mu ' y \iff \mu ' = \mu P(t) $$

    $$ \iff \dfrac{d \mu }{dt} = \mu P(t) \iff \dfrac{1}{\mu }d \mu = P(t) dt $$

    이다. 이것을 그대로 적분하면

    $$ \int_{}^{}\dfrac{1}{\mu }d \mu = \int_{}^{}P(t)dt $$

    $$ \ln |\mu | = \int_{}^{}P(t)dt $$

    $$ \therefore \mu = \pm e ^{\int_{}^{}P(t)dt} $$

    를 얻는다.

    즉, 1계 선형 미분방정식에서 $y$ 의 계수인 함수 $P(t)$ 를 적분하여 $e$ 의 지수함수에 올린 형태 $\mu = \exp \bigg (\int_{}^{}P(t)dt\bigg )$ 를 곱하면 미분방정식의 해를 간단히 구할 수 있다. 

- 예시 

    미분방정식 $t \dfrac{dy}{dt} = t ^{2} + 3y \quad (t > 0)$ 의 일반해를 구해보자. 먼저 방정식을 표준형으로 쓰면

    $$ \dfrac{dy}{dt} - \dfrac{3}{t}y = t $$

    이다. 이때 적분인자는 

    $$ e ^{- \int_{}^{}\dfrac{3}{t}dt} = e ^{-3 \ln t} = e ^{\ln t ^{-3}} = t ^{-3} \quad (t > 0) $$

    이다. 이 적분인자를 미분방정식 양변에 곱하면

    $$ t ^{-3}(y'-\dfrac{3}{t}y) = t ^{-2} \iff \dfrac{d}{dt}(t ^{-3}y) = t ^{-2} $$

    를 얻는다. 양변을 적분하면 일반해는 

    $$ \int_{}^{} \dfrac{d}{dt}(t ^{-3}y) = \int_{}^{} t ^{-2} $$

    $$ \iff t ^{-3}y = \int_{}^{}t ^{-2}dt = - \dfrac{1}{t} + C $$

    $$ \iff y = -t ^{2} + C t ^{3} \quad (t > 0) $$

    이다.
    
# 수열의 수렴

!!! tldr ""

    수열의 수렴 : $n \in \N$ 에 대하여 수열 $a_n$ 이 수렴한다는 것은 어떤 실수 $L \in \R$ 이 존재하여 임의의 양수 $\epsilon$ 에 대하여

    $n > N _{\epsilon }$ 이기만 하면 $|a_n -L | < \epsilon$ 이 성립하도록 하는 양수 $N _{\epsilon }$ 이 존재한다는 것이다.

- 증명

    (중복)

!!! tldr ""

    유계 증가수열 원리(Monotonic Sequence Principle) : 대한 수열 $a_n$ 이 
    
    $$\forall n \in \N, a_n \leq a _{n+1} \land \exists M \in \R, \forall n \in \N, a_n \leq M$$

    이면 수열 $a_n$ 은 반드시 수렴한다.

- 이는 실수의 완비성이라 부르는 실수 체계의 공리이다.

- 증명

    **구체화 필요**

- 예시 

    $$ \lim_{n \to \infty} \sqrt[m]{a_n} = \sqrt[m]{l} $$

!!! tldr ""

    수렴하는 수열의 성질 : 수렴하는 두 수열 $\{a_n\},\{b_n\}$ 에 대하여 $\displaystyle \lim_{n \to \infty} a_n = l, \lim_{n \to \infty} b_n = l'$ 일 때 다음 성질이 성립한다.

1. $\displaystyle \lim_{n \to \infty} (a_n + b_n) = l + l'$

2. $\displaystyle \lim_{n \to \infty} (a_n \cdot b_n) = l \cdot  l'$

3. 상수 $c$ 에 대하여 $\displaystyle \lim_{n \to \infty} ca_n = cl$

4. $f$ 가 $\R$ 위에서 정의된 연속함수라면 $\displaystyle  \lim_{n \to \infty}f(a_n) = f(l)$ 이다.

5. 수열 $\{c_n\}$ 이 있어서 어떤 양수 $N$ 보다 큰 모든 $n$ 에 대해 $\displaystyle  a_n \leq c_n \leq b_n \land l=l' \implies \lim_{n \to \infty} c_n =l$ 이다.


# 무한급수 수렴판정

!!! tldr ""

    무한급수 (infinite series) : 무한수열의 합이다.

- 수열 $\{a_n\}$ 에 대한 무한급수는 $\displaystyle \sum_{n=1}^{\infty} a_n$ 이다.

    이 수열의 부분합은 $\displaystyle  k \in \N, S_k = \sum_{n=1}^{k}a_n$ 인데, 무한급수가 수렴한다는 것은 수열 $\{S_k\}$ 가 수렴한다는 것, 즉 $\displaystyle \exists L \in \R, \lim_{k \to \infty} S_k = \sum_{n=1}^{\infty} a_n = L$ 라는 것이다.

- 예시 

    $\displaystyle \sum_{n=2}^{\infty}\dfrac{1}{n(n-1)} = \sum_{n=2}^{\infty}\bigg (\dfrac{1}{n-1}-\dfrac{1}{n}\bigg )$ 은 수렴한다. 왜냐하면

    $$ S_n = 1 - \dfrac{1}{n} \implies  \lim_{n \to \infty}S_n = 1 \implies  \sum_{n=2}^{\infty}\dfrac{1}{n(n-1)}=1 $$

    이기 때문이다.

!!! tldr ""

    수렴하는 급수의 성질 : 수렴하는 두 급수 $\displaystyle \sum_{n=1}^{\infty}a_n, \sum_{n=1}^{\infty} b_n$ 에 대하여 다음 성질이 성립한다.

1. 상수 $A$ 에 대해 $\displaystyle \sum_{n=1}^{\infty}Aa_n = A \sum_{n=1}^{\infty}a_n$

2. $\displaystyle \sum_{n=1}^{\infty}a_n + \sum_{n=1}^{\infty}b_n = \sum_{n=1}^{\infty}(a_n + b_n)$

!!! tldr ""

    일반항 판정법(n-th term test) : 일반항 $a_n$ 이 $\displaystyle  n \to \infty \implies \lim_{n \to \infty} a_n \neq 0$ 이면 급수 $\displaystyle \sum_{n=1}^{\infty}a_n$ 이 발산한다.

- 예시 

    무한급수 $\displaystyle \sum_{n=1}^{\infty}\dfrac{n ^{2}}{4 + 2 n ^{2}}$ 가 수렴하는지 조사하자.

    $\displaystyle \lim_{n \to \infty} \dfrac{n ^{2}}{4 + 2 n ^{2}} = \lim_{n \to \infty}\dfrac{1}{4/n ^{2} + 2}  = \dfrac{1}{2}$ 이므로 일반항이 $0$ 으로 수렴하지 않는다. 그러므로 급수가 발산한다.

!!! tldr ""

    등비급수(geometric series) 의 수렴 : $a \neq 0$ 와 공비(ratio) $r \in \R$ 에 대한 등비급수

    $$ S = a + ar + ar ^{2} + ar ^{3} + \dots + a r ^{n} + \dots = \sum_{k=0}^{\infty}a r ^{k} $$ 

    는 $r = 1$ 인 경우 부분합이 $S_k = ka$ 이 되어 발산하고,

    $r \neq 1$ 인 경우 부분합이 $S_k = \dfrac{a(1-r ^{k})}{1-r}$ 이 되므로 $|r|<1$ 일 때 $\displaystyle \lim_{k \to \infty} S_k = \dfrac{a}{1-r}$ 이 되어 수렴하고, $|r| > 1$ 일 때는 발산한다.

- 부분합 $S_k$ 는 다음과 같이 얻는다.

    $$ rS_k = ar + \dots + ar ^{k} $$

    $$ S_k - rS_k = (1-r)S_k = a - ar ^{k}  \iff S_k = \dfrac{a(1-r ^{k})}{1-r} $$

- 예시 

    등비급수 $\displaystyle \sum_{k=1}^{\infty}\bigg (\dfrac{1}{2}\bigg )^{k}$ 의 수렴을 조사하자.

    공비가 $\dfrac{1}{2}$ 이므로 수렴한다.

!!! tldr ""

    비교판정법(comparison test) : 모든 $n$ 에 대해 $0 \leq a_n \leq b_n$ 이면

    1. $\displaystyle \sum_{n=1}^{\infty} b_n$ 이 수렴하면 $\displaystyle \sum_{n=1}^{\infty} a_n$ 도 수렴한다.

    2. $\displaystyle \sum_{n=1}^{\infty} b_n$ 이 발산하면 $\displaystyle \sum_{n=1}^{\infty} a_n$ 도 발산한다.

- 1 증명 

   $\displaystyle \sum_{n=1}^{\infty} b_n = M$ 으로 두면 

   $$ \sum_{n=1}^{k} a_n \leq \sum_{n=1}^{k} b_n \leq \sum_{n=1}^{\infty} b_n = M $$

   이 되어 유계 증가수열의 원리에 의해 $\displaystyle \sum_{n=1}^{\infty} a_n$ 이 수렴한다.

- 2 증명 

    (1 의 증명과 비슷하게 할 수 있다.)

- 예시 

    $\displaystyle \sum_{n=1}^{\infty}\dfrac{1}{n ^{2}}$ 은 비교 판정법에 의하여 수렴한다.
    
    왜냐하면 $n \geq 2$ 일 때 $\dfrac{1}{n ^{2}} < \dfrac{1}{n(n-1)}$ 이고 $\sum_{n=2}^{\infty} = 1$ 이기 때문이다. 

- 예시 

    조화급수 $\displaystyle \sum_{n=1}^{\infty}\dfrac{1}{n}$ 은 비교 판정법에 의하여 발산한다.

    왜냐하면 

    $$ 1 + \dfrac{1}{2} + \dfrac{1}{3} + \dots > 1 + \dfrac{1}{2} + \bigg (\dfrac{1}{4} + \dfrac{1}{4} \bigg ) + \dots $$

    $$ = 1 + \dfrac{1}{2} + 2 \times \dfrac{1}{4} + 4 \times \dfrac{1}{8} = 1 + \dfrac{1}{2} + \dfrac{1}{2} + \dots = \infty $$

    이기 때문이다.

!!! tldr ""

    극한 비교판정법(limit comparison test) : $\forall n \in \N, a_n > 0, b_n > 0$ 일 때 $\displaystyle \lim_{n \to \infty} \dfrac{a_n}{b_n} = c \land c > 0$ 이면 $\sum a_n, \sum b_n$ 은 둘 다 수렴하거나 둘 다 발산한다.

- 증명 

    극한 $\displaystyle \lim_{n \to \infty} \dfrac{a_n}{b_n}$ 이 유한값 $c$ 라고 하면 극한의 정의에 따라 조건 $n \geq N$ 을 만족하는 $\forall n \in \N$ 에 대하여 부등식

    $$ a_n \leq (c+1) b_n $$

    이 항상 성립하게 하는 자연수 $N$ 이 존재하게 된다. 그러면

    $$ \sum_{n=1}^{\infty} a_n = \sum_{n=1}^{N-1}a_n + \sum_{n=N}^{\infty}a_n \leq \sum_{n=1}^{N-1}a_n + (c+1) \sum_{n=N}^{\infty}b_n $$

    이다. 그러므로 $\sum b_n$ 이 수렴하면 $\sum a_n$ 이 수렴한다.

    $\sum b_n$ 이 발산한다고 가정하면, 극한의 정의에 따라 조건 $n \geq N_1$ 을 만족하는 임의의 자연수 $n$ 에 대하여 부등식 

    $$ \dfrac{c}{2}b_n \leq a_n $$

    이 항상 성립하게 하는 자연수 $N_1$ 이 존재하게 된다 그러면 

    $$ \sum_{n=N_1}^{\infty} \dfrac{c}{2}b_n \leq \sum_{n=N_1}^{\infty} a_n $$

    의 좌변이 발산하므로 $\sum a_n$ 은 발산한다.

    (이해 안 됨 강의 봐야할듯)

- 예시 

    $\displaystyle \sum_{n=1}^{\infty}\dfrac{2 n ^{2} + 3n}{\sqrt[]{5 + n ^{5}}}$ 가 수렴하는지 조사하자.

    $a_n = \dfrac{2 n ^{2} + 3n}{\sqrt[]{5 + n ^{5}}}, b_n = \dfrac{2 n ^{2}}{n ^{5/2}} = \dfrac{2}{\sqrt[]{2}}$ 라고 하면 

    $$ \lim_{n \to \infty} \dfrac{a_n}{b_n} = \lim_{n \to \infty}  \dfrac{2 n ^{2} + 3n}{\sqrt[]{5 + n ^{5}}}\dfrac{n ^{1/2}}{2} = \lim_{n \to \infty}  \dfrac{n ^{5/2} + \dfrac{3}{2} n ^{3/2}}{\sqrt[]{5 + n ^{5}}} $$

    $$ = \lim_{n \to \infty} \dfrac{1 + \dfrac{3}{2}n ^{3/2-5/2}}{\sqrt[]{\dfrac{5+n ^{5}}{n ^{5}}}} = \lim_{n \to \infty} \dfrac{1 + \dfrac{3}{2}n ^{-1}}{\sqrt[]{1+5 /n ^{5}}} = 1 $$

    이므로 극한 비교판정법을 사용할 수 있다.

    $\displaystyle \sum_{n=1}^{\infty} \dfrac{2}{\sqrt[]{n}}$ 이 발산하므로 극한 비교판정법에 의하여 처음의 급수도 발산한다.

!!! tldr ""

    비율 판정법(raio test) : $\forall n \in \N, a_n > 0$ 에 대하여 극한값

    $$ r = \lim_{m \to \infty} \dfrac{a _{m+1}}{a_m} $$

    이 존재할 때 $r < 1$ 이면 급수 $\displaystyle \sum_{n=1}^{\infty}a_n$ 가 수렴하고,

    $r > 1$ 이면 급수 $\displaystyle \sum_{n=1}^{\infty}a_n$ 가 발산한다.

- 증명

    ㅇㅇ 
    (이해 안 됨 강의 봐야할듯)

- 예시 

    $\displaystyle \sum_{n=0}^{\infty} \dfrac{n}{3 ^{n}}$ 이 수렴하는지 조사하자.

    $$ \lim_{n \to \infty} \dfrac{\dfrac{n+1}{3 ^{n+1}}}{\dfrac{n}{3 ^{n}}}  = \lim_{n \to \infty} \dfrac{n+1}{n} \dfrac{3 ^{n}}{3 ^{n+1}} = \dfrac{1}{3} $$

    이므로 주어진 급수는 비율 판정법에 의하여 수렴한다.

!!! tldr ""

    거듭제곱근 판정법(root test) : $\displaystyle \forall n \in \N, a_n>0 \land \exists r \in \R, r = \lim_{m \to \infty} (a_m) ^{1/m} \implies r < 1$ 이면 급수 $\displaystyle \sum_{n=1}^{\infty}a_n$ 이 수렴하고, $r>1$ 이면 발산한다.

- 증명

    **구체화 필요**

- $r=1$ 일 경우 수렴, 발산에 대한 결론을 얻을 수 없다는 단점이 있다. 이런 경우 다음에 소개할 적분판정법을 사용할 수 있다.

- 예시 

    $\displaystyle \sum_{n=2}^{\infty}\dfrac{1}{(\ln n) ^{n}}$ 이 수렴하는지 조사하자.

    $$ \lim_{n \to \infty} \sqrt[n]{\dfrac{1}{(\ln n) ^{n}}}  = \lim_{n \to \infty} \dfrac{1}{\ln n}  = 0 $$ 

    이므로 거듭제곱근 판정법에 의해 수렴한다.

!!! tldr ""

    단조감소함수 : 다음 조건을 만족하는 함수 $f(x)$ 를 단조감수함수라고 한다.

    $$ x_1 < x_2 \to f(x_1) > f(x_2) $$

!!! tldr ""

    적분판정법(integral test) : $x>0$ 에서 정의된 단조감소함수 $f(x)$ 와 수열 $a_n$ 에 대하여 $f(x) \geq 0 \land \forall n \in \N, a_n = f(n)$ 일 때 극한

    $$ \lim_{R \to \infty}\int_{1}^{R}f(x)dx $$

    가 수렴하면 급수 $\displaystyle \sum_{n=1}^{\infty}a_n$ 도 수렴하고,

    무한대로 발산하면 급수 $\displaystyle \sum_{n=1}^{\infty}a_n$ 도 발산한다.

- 증명 

    **구체화 필요**

- 예시 

    $\exists p \in \R$ 에 대하여 급수 $\displaystyle \sum_{n=1}^{\infty}\dfrac{1}{n^p}$ 는 $p \leq 1$ 이면 발산하고, $p>1$ 이면 수렴하는데, 이 사실을 증명해보자.

    먼저 수열 $a_n = \dfrac{1}{n^p}$ 에 대하여 $p \leq 0$ 이면 $\forall n \in \N, a_n > 1$ 이므로 급수가 무조건 발산하므로, $p > 0$ 인 경우만 상정하자.

    함수 $f(x) = x ^{-p}$ 에 대하여
    
    $$p \neq 1 \implies \int_{1}^{R}x ^{-p}dx = \bigg [\dfrac{1}{1-p}x ^{1-p}\bigg ] ^{R} _{1} = \dfrac{1}{1-p}(R ^{1-p} - 1) $$ 

    이다. 이때 

    $$ p>1 \iff 1-p<0 \implies \lim_{R \to \infty} \int_{1}^{R}x ^{-p}dx = \lim_{R \to \infty} \dfrac{1}{1-p}(R ^{1-p} - 1) = \dfrac{1}{p-1} $$

    이므로 이 값은 유한하다. 그러므로 $p>1$ 이면 $\sum \dfrac{1}{n^p}$ 는 수렴한다. ■ 

    한편, 

    $$ 0 < p < 1 \implies \lim_{R \to \infty} \int_{1}^{R} x ^{-p}dx \to \infty  $$

    이므로 $0<p<1$ 이면 $\sum \dfrac{1}{n^p}$ 는 발산한다. ■ 

    또

    $$ p = 1 \implies \lim_{R \to \infty} \int_{1}^{R}x ^{-1}dx = \lim_{R \to \infty}  \ln R \to \infty $$

    이다. 그러므로 $p=1$ 이면 $\sum \dfrac{1}{n^p}$ 는 발산한다. ■ 

!!! tldr ""

    절대수렴(converges absolutely) : 임의의 급수 $\displaystyle \sum_{n=1}^{\infty}a_n$ 이 주어졌을 때, 급수 $\displaystyle \sum_{n=1}^{\infty}|a_n|$ 이 수렴하면, 급수 $\displaystyle \sum_{n=1}^{\infty}a_n$ 이 절대수렴한다.

!!! tldr ""

    절대수렴판정법(absolute convergence test) : 절대수렴하는 급수는 수렴한다.

- 증명

    **구체화 필요**

!!! tldr ""

    교대급수(alternating series) : $\forall n \in \N, a_n > 0 \implies \sum(-1) ^{n+1} a_n$ 꼴의 급수이다.

- 예시 

    $$ 1 - \dfrac{1}{2} + \dfrac{1}{3} - \dfrac{1}{4} + \dots $$

!!! tldr ""

    교대급수 판정법(alternating series test) : $\forall n \in \N, a_n > 0 \land a_n \geq a _{n+1}$ 이면 $\sum (-1) ^{n+1} a_n$ 은 수렴한다. 

- 증명

    **구체화 필요**

- 예시 

    $1 - \dfrac{1}{2} + \dfrac{1}{3} - \dfrac{1}{4} + \dots$ 은 교대급수판정법에 의하여 수렴한다.

# 멱급수와 수렴반경

!!! tldr ""

    멱급수(power series) : 변수 $x$ 에 대하여

    $$ \sum_{n=0}^{\infty}a_n x ^{n} = a_0 + a_1x + a_2 x ^{2} + \dots $$

    이다.

- 멱급수의 수렴 조사

    비율판정법을 사용하여 

    $$ r = \lim_{n \to \infty} \dfrac{| a _{n+1} x ^{n+1}|  }{|a_n x ^{n}} $$

    을 생각해보면 $r<1$ 인 경우 멱급수 $\sum a_n x ^{n}$ 가 절대 수렴한다. 따라서 부등식

    $$ \lim_{n \to \infty} \dfrac{| a _{n+1} x ^{n+1}|  }{|a_n x ^{n}} < 1 $$

    을 풀어서

    $$ |x| < \lim_{n \to \infty} \dfrac{| a _{n} |  }{|a _{n+1}| }  $$

    을 얻으면, 우변의 극한이 존재할 경우 $R = \displaystyle \lim_{n \to \infty} \dfrac{| a _{n} |  }{|a _{n+1}| }$ 을 얻는데, 조건 $|x| < R$ 을 만족하는 범위에서 멱급수 $\sum a_n x ^{n}$ 가 수렴(절대수렴) 한다는 것을 알 수 있다.
