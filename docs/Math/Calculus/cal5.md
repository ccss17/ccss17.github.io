# 여러 가지 함수의 부정적분 

!!! tldr ""

    $n$ 차 단항 함수 $y=x^n$ 의 부정적분 : $n \neq 1$ 인 실수일 때
    
    $$ \int_{}^{}x ^{n} dx = \frac{1}{n+1}x ^{n+1}+C $$
    
    이고, $n = 1$ 일 때 
    
    $$ \int_{}^{} \frac{1}{x} dx = \ln |x| + C $$
    
    이다.

- 증명 

    $n \neq -1$ 일 때, 함수 $y= x ^{n}$ 의 미분법에서 

    $$ \bigg( \frac{1}{n+1}x ^{n+1}\bigg)' = x ^{n} $$

    이므로 부정적분의 정의에 의하여 

    $$ \therefore  \int_{}^{}x ^{n} dx = \frac{1}{n+1}x ^{n+1}+C $$

    이고, $n = -1$ 일 때 로그함수의 미분법에서 $(\ln |x|)' = \frac{1}{x}$ 이므로 부정적분의 정의에 의하여

    $$ \therefore \int_{}^{} \frac{1}{x} dx = \ln |x| + C $$

    이다. 

- 예시 

    $$ \int_{}^{}\frac{1}{x^2}dx = \int_{}^{}x ^{-2}dx = \frac{1}{-2+1}x ^{-2+1}+C = -\frac{1}{x}+C $$

    $$ \int_{}^{}\sqrt[]{x}dx = \int_{}^{}x ^{\frac{1}{2}}dx = \frac{1}{\frac{1}{2}+1}x ^{} $$

## 지수함수의 부정적분

!!! tldr ""

    지수함수 $y = e^x$ 의 부정적분 : 
    
    $$ \int_{}^{}e ^{x}dx=e ^{x}+C $$

- 증명 

    밑이 $e$ 인 지수함수의 미분법에서 $(e ^{x})'=e ^{x}$ 이므로 부정적분의 정의에 의하여 

    $$ \int_{}^{}e ^{x}dx=e ^{x}+C $$

    이다.

- 예시 

    $$ \int_{}^{}e ^{x+2}dx = \int_{}^{}e ^{2} \cdot e ^{x}dx=e ^{2}\int_{}^{}e ^{x}dx = e ^{2} \cdot e ^{x}+C = e ^{x+2}+C $$

!!! tldr ""

    지수함수 $y = a^x$ 의 부정적분 : 
    
    $$ \int_{}^{}a ^{x}dx= \frac{a ^{x}}{\ln a}+C $$

- 증명 

    지수함수 $y = a ^{x}$ 의 미분법에서 $(a ^{x})' = a ^{x}\ln a$ 이므로 

    $$ (\frac{a ^{x}}{\ln a})' = a ^{x} $$

    이다. 따라서 부정적분의 정의에 의하여 

    $$ \int_{}^{}a ^{x}dx = \frac{a ^{x}}{\ln a}+C $$

    이다.

- 그런데 미분해서 $\ln x, \log_{a} x$ 가 나오는 식이 없으므로 이것들을 적분하면 어떤 식이 나오는지 알 수 없을 것만 같다. 그러나 부분적분법이라는 특수한 적분법으로 적분을 할 수 있게 되었다.

- 예시 

    $$ \int_{}^{}3 ^{x-2}dx = \int_{}^{}3 ^{x} \cdot 3 ^{-2}dx = \frac{1}{9}\int_{}^{}3 ^{x}dx = \frac{3 ^{x}}{9 \ln 3}+C = \frac{3 ^{x-2}}{\ln 3}+C $$

## 삼각함수의 부정적분

!!! tldr ""

    삼각함수의 부정적분 : 
    
    $$ \int_{}^{}\sin xdx=-\cos x+C $$
    
    $$ \int_{}^{}\cos xdx=\sin x+C $$
    
    $$ \int_{}^{}\sec ^{2}xdx=\tan x+C $$
    
    $$ \int_{}^{}\csc ^{2}xdx=-\cot x+C $$
    
    $$ \int_{}^{}\sec x \tan xdx=\sec x+C $$
    
    $$ \int_{}^{}\csc x \cot xdx=-\csc x+C $$

- 증명

    삼각함수의 미분법에 의하여 

    $$ (\cos x)'=-\sin x$$ 

    $$(\sin x)'=\cos x $$

    $$ (\tan x)' = \sec ^{2}x$$ 

    $$(\cot x)'=-\csc ^{2}x $$

    $$ (\sec x)'=\sec x \tan x$$ 

    $$(\csc x)' = -\csc x \cot x $$

    이므로 부정적분의 정의에 의하여 각각의 부정적분이 증명된다.

- 그런데 미분하여 $\tan x$ 가 나오는 식이 없기에 $\tan x$ 를 적분하면 어떤 식이 나오는지 알 수 없을 것 같다. 하지만 치환적분법이라는 특수한 적분법으로 적분을 할 수 있게 된다. 

    - $\cot x, \sec x, \csc x$ 의 적분도 치환적분법으로 구한다. 

- 예시 

    $$ \int_{}^{}(3 \sin x-\cos x)dx = -3 \cos x-\sin x+C $$

!!! tldr ""

    함수 $\tan x$ 의 부정적분 : 
    
    $$ \int_{}^{}\tan xdx=- \ln |\cos x|+C $$

- 증명 

    $$ \int_{}^{}\tan xdx = \int_{}^{}\frac{\sin x}{\cos x}dx $$

    이다. 그런데 $(\cos x)' = -\sin x$ 이므로 

    $$ = -\int_{}^{} \frac{(\cos x)' }{\cos x} dx $$

    이다. 이때 피적분함수가 $\frac{f'(x)}{f(x)}$ 꼴인 경우의 치환적분법에 의하여 

    $$ = -\int_{}^{} \frac{(\cos x)' }{\cos x} dx = -\ln |\cos x|+C$$

    이다. 그러므로 

    $$ \therefore \int_{}^{}\tan xdx = - \ln |\cos x|+C $$

!!! tldr ""

    함수 $\cot x$ 의 부정적분 : 
    
    $$ \int_{}^{}\cot xdx = \ln |\sin x| +C $$



!!! tldr ""

    함수 $\sec x$ 의 부정적분 : 
    
    $$ \int_{}^{}\sec xdx = \ln |\sec x+\tan x|+C $$



!!! tldr ""

    함수 $\csc xdx$ 의 부정적분 :
    
    $$ \int_{}^{}\csc xdx = -\ln |\csc x+\cot x| $$

# 치환적분법

!!! tldr ""

    적분변수의 치환(역연쇄법칙, anti chain rule) : 적분변수 $x$ 를 새로운 변수 $t$ 로 바꾸는 것이다.

- 설명

    함수 $f(x)$ 에서 변수 $x$ 를 다른 변수 $t$ 에 대한 미분가능한 함수 $x=g(t)$ 로 생각하면 $f(x) = f(g(t)), \dfrac{dx}{dt} = g'(t)$ 이므로 

    $$ \int_{}^{}f(x)dx = \int_{}^{}f(x)\frac{dt}{dt}dx$$

    에서 적분변수를 $x \to t$ 로 변경하면

    $$ = \int_{}^{}f(x)\frac{dx}{dt}dt = \int_{}^{}f(g(t))g'(t)dt $$ 

    이다. 그러므로

    $$ \therefore \int_{}^{}f(x)dx = \int_{}^{}f(g(t))g'(t)dt $$

    가 된다.

    - 합성함수의 미분법, 즉 연쇄법칙에서 미분기호를 

        $$ \frac{dy}{dx} = \frac{dy}{dt} \cdot \frac{dt}{dx} $$

        와 같이 분수처럼 계산할 수 있었다.

    - $\displaystyle \int_{}^{}$ 안에서 $\dfrac{dt}{dt}$ 에 대한 곱하기, 약분, 결합법칙을 자유롭게 적용할 수 있다.

!!! tldr ""

    치환적분법(integration by substitution) : 적분변수의 치환을 이용하여 합성함수 형태의 적분식을 쉬운 적분식으로 변환하여 적분하는 방법으로써 
    
    함수 $f(x)$ 의 한 부정적분을 $F(x)$ 라 하고 미분가능한 함수 $g(t)$ 에 대하여 $x=g(t)$ 로 놓으면
    
    $$ \int_{}^{}f(x)dx = \int_{}^{}f(g(t))g'(t)dt = F(g(t)) + C $$
    
    이다.

- 증명 

    함수 $f(x)$ 의 한 부정적분을 $F(x)$ 라 하면 

    $$ \int_{}^{}f(x)dx = F(x)+C $$

    이다. $x$ 를 $t$ 에 대한 미분가능한 함수 $x=g(t)$ 로 두면 $F(x)=F(g(t))$ 이므로 $F(x)$ 를 $t$ 에 대하여 미분하면 합성함수의 미분법에 의하여 

    $$ \frac{d}{dt}F(x)=\frac{d}{dx}F(x)\cdot \frac{dx}{dt}=f(x)g'(t)=f(g(t))g'(t) $$

    이다. 따라서 부정적분의 정의에 의하여 

    $$ \therefore  \int_{}^{}f(g(t))g'(t)dt = F(x)+C = \int_{}^{}f(x)dx $$

    이다.

- 예시 

    $$ \int_{}^{}(3x+2) ^{2}dx $$

    에서 $3x+2=t$ 로 두면 $x = \dfrac{t-2}{3}$ 이고 양변을 $t$ 에 대하여 미분하면 

    $$ \frac{dx}{dt} = \frac{1}{3} $$

    이다. $\int_{}^{}$ 안에서 $dx, dt$ 를 자유롭게 약분, 곱셈 등을 할 수 있으므로 

    $$ dx = \frac{1}{3}dt $$

    이다. 따라서

    $$ \int_{}^{}(3x+2)^{2}dx = \int_{}^{}t ^{2} \cdot \frac{1}{3}dt $$

    이므로

    $$ = \frac{1}{3} \int_{}^{}t ^{2}dt = \frac{1}{3} \cdot \frac{1}{3} t ^{3}+C = \frac{1}{9} (3x+2) ^{3}+C$$

    이다.

## 치환적분법을 이용한 부정적분 계산 

피적분함수의 형태에 따라 다음의 경우로 나누어 정의한다.

!!! tldr ""

    피적분함수가 $f(g(x))g'(x)$ 꼴인 경우 : 함수 $f(x)$ 의 한 부정적분이 $F(x)$ 이고 $g(x) = t$ 라고 하면
    
    $$ \int_{}^{}f(g(x))g'(x)dx = F(t)+C $$
    
    이다.

- 증명

    $g(x) = t$ 로 놓으면 

    $$ g'(x) = \frac{dt}{dx} $$

    이므로 $F(t)$ 가 $f(t)$ 의 한 부정적분일 때

    $$ \int_{}^{}f(g(x))g'(x)dx = \int_{}^{}f(t) \frac{dt}{dx} dx$$ 

    에서 $dx$ 를 약분하여

    $$ =\int_{}^{}f(t)dt = F(t)+C=F(g(x))+C $$

    이다.

- 예시 

    $$ \int_{}^{}x(x ^{2}+1)^{5}dx $$

    에서 $(x ^{2}+1)'=2x$ 이므로 $x^2+1=g(x)=t$ 로 두고 $t ^{5} = f(t)$ 로 두면,

    $$ \int_{}^{}x(x ^{2}+1)^{5}dx = \frac{1}{2} \int_{}^{}(x ^{2}+1) ^{5} \cdot 2xdx = \frac{1}{2} \int_{}^{}f(g(x)) \cdot g'(x)dx = \frac{1}{2} \cdot \frac{1}{6}t ^{6} + C = \frac{1}{12}t ^{6}+C $$

    이다. 그러므로 

    $$ \therefore \int_{}^{}x(x ^{2}+1)^{5}dx = \frac{1}{12}(x ^{2}+1)^{6}+C $$

    이다.

- 예시 

    $$ \int_{}^{}x(x ^{2}+1)^{5}dx $$

    에서 $(x ^{2}+1)'=2x$ 이므로 $x^2+1=t$ 로 두면,

    $$ \frac{dt}{dx}=2x $$

    에서 

    $$ dt = 2xdx $$

    이므로

    $$ \int_{}^{}x(x ^{2}+1)^{5}dx = \frac{1}{2} \int_{}^{}(x ^{2}+1) ^{5} \cdot 2xdx = \frac{1}{2} \int_{}^{} t ^{5}dt = \frac{1}{12}t ^{6}+C $$

    이다. 그러므로

    $$ \therefore \int_{}^{}x(x ^{2}+1)^{5}dx = \frac{1}{12}(x ^{2}+1)^{6}+C $$

    이다.

!!! tldr ""

    피적분함수가 $\frac{f'(x)}{f(x)}$ 꼴인 경우 : 
    
    $$ \int_{}^{}\frac{f'(x)}{f(x)} = \ln |f(x)|+C $$

- 증명 

    $f(x)=t$ 로 두면 

    $$ f'(x) = \frac{dt}{dx} \implies  f'(x)dx = dt $$

    이다. 따라서

    $$ \int_{}^{}\frac{f'(x)}{f(x)}dx = \int_{}^{}\frac{1}{t}dt = \ln |t|+C = \ln |f(x)|+C $$

    이다. 

- 예시 

    $$ \int_{}^{}\frac{x^2}{x^3-4}dx $$

    에서 $(x ^{3}-4)'=3x ^{2}$ 이므로 

    $$ \int_{}^{}\frac{x^2}{x^3-4}dx = \frac{1}{3} \int_{}^{}\frac{3x^2}{x^3-4}dx=\frac{1}{3}\ln |x ^{3}-4|+C $$

## 유리함수의 부정적분 

피적분함수가 $\frac{f'(x)}{f(x)}$ 꼴이 아닌 유리함수의 부정적분은 분모, 분자의 차수에 따라 다음과 같이 구한다.

!!! tldr ""

    (분자의 차수) $<$ (분모의 차수) 이고 분모가 인수분해되는 경우 : 피적분함수를 부분분수로 변형하여 부정적분을 구한다.
    
    (**구체화 필요**)

!!! tldr ""

    (분자의 차수) $\geq$ (분모의 차수) 인 경우 : 분자를 분모로 나누어 몫과 나머지의 꼴로 나타내어 부정적분을 구한다.
    
    (**구체화 필요**)

## 부분적분법

!!! tldr ""

    부분적분법(integration by parts) : 두 함수 $f(x),g(x)$ 가 미분가능할 때 
    
    $$ \int_{}^{}f(x)g'(x)dx = f(x)g(x)-\int_{}^{}f'(x)g(x)dx \Leftarrow \int_{}^{}uv'dx = uv-\int_{}^{}u'vdx $$
    
    을 활용하여 곱셈 꼴인 함수를 쉽게 적분하는 방법이다.

- 적분상수를 생략한 것은 우변의 적분이 아직 완료되지 않았기 때문이다. 

- 증명 

    미분가능한 두 함수 $f(x), g(x)$ 의 곱 $f(x)g(x)$ 를 미분하면 

    $$ \{f(x)g(x)\}' = f(x)g'(x) + f'(x)g(x) $$

    이므로 도함수의 역연산인 부정적분은 

    $$ \int_{}^{}\{f(x)g'(x)+f'(x)g(x)\}dx = f(x)g(x)+C $$

    이고

    $$ \int_{}^{}f(x)g'(x)dx + \int_{}^{} f'(x)g(x)dx = f(x)g(x)+C $$

    에서 

    $$ \therefore  \int_{}^{}f(x)g'(x)dx = f(x)g(x) - \int_{}^{} f'(x)g(x)dx $$

    이다. 

- 예시 

    $y = x e ^{x}$ 의 부정적분은 $x, e^x$ 에 대한 미분으로도 구할 수 없고 치환적분법도 사용할 수 없다. 하지만 부분적분법을 사용하여 $f(x) = x, g'(x) = e^x$ 로 두면 $f'(x) = 1, g(x) = e^x$ 이므로 

    $$ \int_{}^{}f(x)g'(x)dx = f(x)g(x) - \int_{}^{} f'(x)g(x)dx $$

    에서 

    $$ \int_{}^{}x e ^{x}dx = x \cdot e ^{x}- \int_{}^{}1 \cdot e ^{x}dx $$

    이다. 그러므로

    $$ \therefore  \int_{}^{}x e ^{x}dx = xe ^{x}- e ^{x} + C$$

    이다.

!!! tldr ""

    부분적분법의 활용

- 피적분함수가 두 함수의 곱의 꼴로 주어지고 치환적분법을 이용하기 어려운 경우 부분적분법을 고려한다.

    - 특히 상수도 함수로 함수로 취급할 수도 있다는 것을 알아야 한다. 

- 미분하면 간단해지는 것을 $u = f(x)$, 적분하기 쉬운 것을 $v' = g'(x)$ 로 둔다.

    - 보통 로그함수, 다항함수, 삼각함수, 지수함수 순으로 $f(x)$ 를 택하고 남은 함수를 $g'(x)$ 로 택한다. 

    - 예시 

        $$ \int_{}^{}x \cos xdx $$

        의 부정적분을 구하는 경우 $u, v'$ 을 택할 수 있는 경우를 나누어볼 수 있다. 

        $$(i) u=1, v'=x \cos x$$

        $$(ii) u=x, v'=\cos x$$

        $$(iii) u=\cos x, v'=x $$

        $$(iv) u=x \cos x, v'=1 $$

        $(i)$ 의 경우 $v$ 자체를 구하는 게 문제의 목적이므로 무의미하다. $(iii), (iv)$ 는 우변의 $\int_{}^{}u'vdx$ 가 너무 복잡해진다. 그러므로 $(ii)$ 의 경우를 택하면

        $$ \int_{}^{}u'vdx = \int_{}^{}\sin xdx $$

        로 둘 수 있다. 그러므로 

        $$ \int_{}^{}uv'dx = uv-\int_{}^{}u'vdx $$

        에서

        $$ \therefore \int_{}^{}x \cos xdx = x \sin x + \cos x + C $$

        이다.

        요지는 공식의 우변의

        $$ \int_{}^{}u'vdx  $$

        를 최대한 간단하게 할 수 있는 $u, v'$ 를 택하면 된다는 것이다. 그러므로 일반적으로 미분하면 간단해지는 것을 $u$ 로 두고 나머지 것들을 $v'$ 로 택한다. 또한 일반적으로 미분하면 간단해지는 함수의 우선순위는 로그함수, 다항함수, 삼각함수, 지수함수이다.

!!! tldr ""

    자연로그함수 $\ln x$ 의 부정적분 : 
    
    $$ \int_{}^{}\ln xdx=x \ln x - x +C $$

- 증명 

    $$ \int_{}^{}uv'dx = uv - \int_{}^{}u'vdx $$

    에서 $u = \ln x, v'=1$ 로 두면 

    $$ \int_{}^{}\ln x \cdot 1 dx = \ln x \cdot x - \int_{}^{} \frac{1}{x} \cdot x dx $$

    이다. 그러므로 

    $$ \int_{}^{}\ln xdx = x \ln x - \int_{}^{}dx $$

    에서 

    $$ \therefore \int_{}^{}\ln xdx = x \ln x - x + C $$

    이다.

!!! tldr ""

    로그함수 $\log_{a} x$ 의 부정적분 : 
    
    $$ \int_{}^{}\log_{a}  xdx=x \ln x - x +C $$

- 증명 

    $$ \int_{}^{}uv'dx = uv - \int_{}^{}u'vdx $$

    에서 $u = \log_{a} x, v'=1$ 로 두면 

    $$ \int_{}^{}\log_{a} x \cdot 1 dx = \log_{a} x \cdot x - \int_{}^{} \frac{1}{x \ln a} \cdot x dx $$

    이다. 그러므로 

    $$ \int_{}^{}\log_{a}  xdx = x \log_{a}  x - \frac{1}{\ln a} \int_{}^{} dx $$

    에서 

    $$ \therefore \int_{}^{}\log_{a}  xdx = x \log_{a}  x - \frac{x}{\ln a} + C $$

    이다.

## 치환적분법, 부분적분법으로의 정적분

!!! tldr ""

    치환적분법으로의 정적분 : 폐구간 $[a,b]$ 에서 연속인 함수 $f(x)$ 에 대하여 미분가능한 함수 $x=g(t)$ 의 도함수 $g'(t)$ 가 폐구간 $[\alpha, \beta]$ 에서 연속이고 $x=g(t)$ 가 적분 구간에서 일대일대응이며 $a= g(\alpha), b = g(\beta)$ 이면 
    
    $$ \int_{a}^{b}f(x)dx = \int_{\alpha }^{\beta }f(g(t))g'(t)dt $$
    
    이다.

- 증명 

    폐구간 $[a, b]$ 에서 연속인 함수 $f(x)$ 의 한 부정적분을 $F(x)$ 라 하면 

    $$ \int_{a}^{b}f(x)dx = \bigg[F(x)\bigg]^{b} _{a} = F(b) - F(a) $$

    이다. 

    한편 $x$ 를 $t$ 에 대하여 미분가능한 함수 $x=g(t)$ 로 치환하면 치환적분법에 의하여 

    $$ \int_{}^{}f(x)dx = \int_{}^{}f(g(t))g'(t)dx = F(g(t))+C $$

    이다. 이때 $x=g(t)$ 가 적분구간에서 일대일대응이므로 

    $$ a=g(\alpha), b=g(\beta) $$

    를 만족하는 $\alpha, \beta$ 는 유일하게 결정된다. 따라서 적분구간 $[a,b]$ 를 $[\alpha, \beta]$ 로 바꿀 수 있다. 그러면 치환적분법으로 얻은 부정적분을 적분구간 $[\alpha, \beta]$ 에 대하여 정적분해보면 

    $$ \int_{\alpha }^{\beta }f(g(t))g'(t)dt = \bigg[F(g(t))\bigg]^{\beta }_{\alpha } = F(g(\beta )) - F(g(\alpha )) = F(b)-F(a) $$

    이다. 그러므로 

    $$ \int_{a}^{b}f(x)dx = F(b) - F(a) = \int_{\alpha }^{\beta }f(g(t))g'(t)dt $$

    에서 

    $$ \therefore  \int_{a}^{b}f(x)dx = \int_{\alpha }^{\beta }f(g(t))g'(t)dt $$

    이다.

- 예시 

    $$ \int_{0}^{4}\sqrt[]{2x+1}dx $$

    에서 $t = (2x+1)$ 로 두면 $x = \frac{t-1}{2}$ 에서 $\frac{dx}{dt}=\frac{1}{2}$ 이다. 따라서 

    $$ dx = \frac{1}{2}dt $$

    이다. 또한 $x=0 \to t=1, x=4 \to t=9$ 이므로 

    $$ \int_{0}^{4}\sqrt[]{2x+1}dx = \int_{1}^{9}\sqrt[]{t} \frac{1}{2}dt = \frac{1}{2} \int_{1}^{9}t ^{\frac{1}{2}}dt = \frac{1}{2}\bigg[\frac{2}{3}t ^{\frac{3}{2}}\bigg]^{9}_{1} =\frac{1}{3}(27-1)=\frac{26}{3} $$

    이다.

!!! tldr ""

    부분적분법으로의 정적분 : 폐구간 $[a,b]$ 에서 두 함수 $f(x), g(x)$ 가 미분가능하고 $f'(x), g'(x)$ 가 연속일 때 
    
    $$ \int_{a}^{b}f(x)g'(x)dx = \bigg[f(x)g(x)\bigg]^{b}_{a}-\int_{a}^{b}f'(x)g(x)dx $$
    
    $$ \iff $$
    
    $$ \int_{a}^{b}uv'dx = \bigg[uv\bigg]^{b}_{a}-\int_{a}^{b}u'vdx $$
    
    이다.

- 증명 

    폐구간 $[a,b]$ 에서 두 함수 $f(x), g(x)$ 가 미분가능하고 $f'(x), g'(x)$ 가 연속일 때 함수의 곱의 미분법에서 

    $$ \{f(x)g(x)\}' = f'(x)g(x)+f(x)g'(x) $$

    이므로 $f(x)g(x)$ 는 $f'(x)g(x)+f(x)g'(x)$ 의 한 부정적분이다. 그러므로 정적분의 정의에 의하여 

    $$ \int_{a}^{b}\{f'(x)g(x)+f(x)g'(x)\}dx = \bigg[f(x)g(x)\bigg]^{b}_{a} $$

    이다. 여기에서 

    $$ \int_{a}^{b}f'(x)g(x)+ \int_{a}^{b} f(x)g'(x)dx = \bigg[f(x)g(x)\bigg]^{b}_{a} $$

    이므로

    $$ \therefore  \int_{a}^{b}f(x)g'(x)= \bigg[f(x)g(x)\bigg]^{b}_{a} - \int_{a}^{b} f'(x)g(x)dx $$

    이다.

- 예시 

    $$ \int_{0}^{1}xe ^{x}dx $$

    에서 $u=x, v'=e^x$ 로 두면 

    $$ \int_{a}^{b}uv'dx = \bigg[uv\bigg]^{b}_{a}-\int_{a}^{b}u'vdx $$

    에서 

    $$ \int_{0}^{1}x e ^{x}dx = \bigg[xe^x\bigg]^{1}_{0} - \int_{0}^{1}e^xdx $$

    이다. 따라서 

    $$ \therefore  \int_{0}^{1}x e ^{x}dx = (e - 0) - \bigg[e^x\bigg]^{1}_{0} = e - (e - 1) = 1$$

    이다.

# 속도와 거리

!!! tldr ""

    정적분으로 구하는 속도 및 거리 
    
    **구체화 필요**

# 역함수의 부정적분과 정적분

!!! tldr ""

    역함수의 부정적분 : 함수 $f(x)$ 의 역함수 $y=f ^{-1}(x)$ 에 대하여 $f ^{-1}(x)$ 의 부정적분은 
    
    $$ \int_{}^{}f ^{-1}(x)dx = xf ^{-1}(x)-\int_{}^{}f(y)dy $$
    
    이다.

- 증명 

    함수 $f(x)$ 의 역함수 $y= f ^{-1}(x)$ 에 대하여 역함수의 정의에 따라 $f(y)=x$ 이고 역함수 미분법에 의하여 $\{f ^{-1}(x)\}' = \frac{1}{f'(y)}$ 이다.

    그러므로 부분적분법을 이용하여

    $$ \int_{}^{}f ^{-1}(x)dx $$

    에서 $u = f ^{-1}(x), v' = 1$ 로 두면 $u'=\frac{1}{f'(y)}, v=x$ 이므로 

    $$ \int_{}^{}f ^{-1}(x)dx = xf ^{-1}(x) - \int_{}^{}\frac{x}{f'(y)}dx $$

    이다. 이때 $x = f(y)$ 에서 $\frac{dx}{dy}=f'(y)$ 이므로 

    $$ dx = f'(y)dy $$

    이다. 따라서 

    $$ \int_{}^{}f ^{-1}(x)dx = xf ^{-1}(x) - \int_{}^{}\frac{f(y)}{f'(y)}f'(y)dy $$

    이다. 그러므로

    $$ \therefore \int_{}^{}f ^{-1}(x)dx = xf ^{-1}(x) - \int_{}^{}f(y)dy $$

    이다.

!!! tldr ""

    역함수의 정적분 : 
    
    **구체화 필요**

# 미분방정식

!!! tldr ""

    미분방정식(differential equation) : 함수와 그 도함수의 관계를 나타내는 방정식이다.

- 예시 

    $$ \frac{dy}{dx} = xy $$

- 예시 

    $$ y' = xy ^{2}+2xy $$

- 예시 

    $$ \frac{f'(x)}{f(x)} = 1 $$

    에서 $y=f(x)$ 로 나타내면 

    $$ \frac{dy}{dx} \cdot \frac{1}{y}=1 $$

    이므로 

    $$ \frac{dy}{dx}=y $$

    라는 미분방정식으로 나타낼 수 있다.