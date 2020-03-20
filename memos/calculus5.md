# [ccss17.github.io](https://ccss17.github.io)

# Calculus5 Memo

# 여러 가지 함수의 부정적분 

- $n$ 차 단항 함수 $y=x^n$ 의 부정적분 : $n \neq 1$ 인 실수일 때

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

    $$
    \int_{}^{}\sqrt[]{x}dx = \int_{}^{}x ^{\frac{1}{2}}dx = \frac{1}{\frac{1}{2}+1}x ^{}
    $$

## 지수함수의 부정적분
  
- 지수함수 $y = e^x$ 의 부정적분 : 

  $$ \int_{}^{}e ^{x}dx=e ^{x}+C $$

  - 증명 

    밑이 $e$ 인 지수함수의 미분법에서 $(e ^{x})'=e ^{x}$ 이므로 부정적분의 정의에 의하여 

    $$ \int_{}^{}e ^{x}dx=e ^{x}+C $$

    이다.
  
  - 예시 

    $$ \int_{}^{}e ^{x+2}dx = \int_{}^{}e ^{2} \circ e ^{x}dx=e ^{2}\int_{}^{}e ^{x}dx = e ^{2} \circ e ^{x}+C = e ^{x+2}+C $$

- 지수함수 $y = a^x$ 의 부정적분 : 

  $$ \int_{}^{}a ^{x}dx= \frac{a ^{x}}{\ln a}+C $$

  - 증명 

    지수함수 $y = a ^{x}$ 의 미분법에서 $(a ^{x})' = a ^{x}\ln a$ 이므로 

    $$ (\frac{a ^{x}}{\ln a})' = a ^{x} $$

    이다. 따라서 부정적분의 정의에 의하여 

    $$ \int_{}^{}a ^{x}dx = \frac{a ^{x}}{\ln a}+C $$

    이다.
  
  - 그런데 미분해서 $\ln x, \log_{a} x$ 가 나오는 식이 없으므로 이것들을 적분하면 어떤 식이 나오는지 알 수 없을 것만 같다. 그러나 부분적분법이라는 특수한 적분법으로 적분을 할 수 있게 되었다.

  - 예시 

    $$ \int_{}^{}3 ^{x-2}dx = \int_{}^{}3 ^{x} \circ 3 ^{-2}dx = \frac{1}{9}\int_{}^{}3 ^{x}dx = \frac{3 ^{x}}{9 \ln 3}+C = \frac{3 ^{x-2}}{\ln 3}+C $$

## 삼각함수의 부정적분
  
- 삼각함수의 부정적분 : 

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

- 탄젠트함수의 부정적분 : 

  $$ \int_{}^{}\tan xdx=- \ln |\cos x|+C $$

  - 증명 

    $$ \int_{}^{}\tan xdx = \int_{}^{}\frac{\sin x}{\cos x}dx $$

    이다. 그런데 $(\cos x)' = -\sin x$ 이므로 

    $$ = -\int_{}^{} \frac{(\cos x)' }{\cos x} dx $$

    이다. 이때 피적분함수가 $\frac{f'(x)}{f(x)}$ 꼴인 경우의 치환적분법에 의하여 

    $$ = -\int_{}^{} \frac{(\cos x)' }{\cos x} dx = -\ln |\cos x|+C$$

    이다. 그러므로 

    $$ \therefore \int_{}^{}\tan xdx = - \ln |\cos x|+C $$

# 치환적분법 

- 적분변수의 치환(역연쇄법칙, anti chain rule) : 적분변수 $x$ 를 새로운 변수 $t$ 로 바꾸는 것이다.

  - 부연설명
  
    함수 $f(x)$ 에서 변수 $x$ 를 다른 변수 $t$ 에 대한 미분가능한 함수 $x=g(t)$ 로 생각하면

    $$ f(x) = f(g(t)), \frac{dx}{dt} = g'(t) $$

    이므로 

    $$ \int_{}^{}f(x)dx = \int_{}^{}f(x)\frac{dt}{dt}dx$$

    에서 적분변수를 $x \to t$ 로 변경하면

    $$ = \int_{}^{}f(x)\frac{dx}{dt}dt = \int_{}^{}f(g(t))g'(t)dt $$ 

    이다. 그러므로

    $$ \therefore \int_{}^{}f(x)dx = \int_{}^{}f(g(t))g'(t)dt $$ $$

    가 된다.
  
    - 합성함수의 미분법, 즉 연쇄법칙에서 미분기호를 

      $$ \frac{dy}{dx} = \frac{dy}{dt} \circ \frac{dt}{dx} $$

      와 같이 분수처럼 계산할 수 있었다.
    
    - $\int_{}^{}$ 안에서 $\frac{dt}{dt}$ 에 대한 곱하기, 약분, 결합법칙을 자유롭게 적용할 수 있다.

  - 증명 

    함수 $f(x)$ 의 한 부정적분을 $F(x)$ 라 하면 

    $$ \int_{}^{}f(x)dx = F(x)+C $$

    이다. $x$ 를 $t$ 에 대한 미분가능한 함수 $x=g(t)$ 로 두면 $F(x)=F(g(t))$ 이므로 $F(x)$ 를 $t$ 에 대하여 미분하면 합성함수의 미분법에 의하여 

    $$ \frac{d}{dt}F(x)=\frac{d}{dx}F(x)\circ \frac{dx}{dt}=f(x)g'(t)=f(g(t))g'(t) $$

    이다. 따라서 부정적분의 정의에 의하여 

    $$ \therefore  \int_{}^{}f(g(t))g'(t)dt = F(x)+C = \int_{}^{}f(x)dx $$

    이다.

- 치환적분법(integration by substitution) : 적분변수의 치환을 이용하여 합성함수 형태의 적분식을 쉬운 적분식으로 변환하여 적분하는 방법이다. 

  - 부연설명 
  
    미분가능한 함수 $g(t)$ 에 대하여 $x=g(t)$ 로 놓으면

    $$ \int_{}^{}f(x)dx = \int_{}^{}f(g(t))g'(t)dt $$

    이다. 
  
  - 예시 

    $$ \int_{}^{}(3x+2) ^{2}dx $$

    에서 $3x+2=t$ 로 두면 $x = \frac{t-2}{3}$ 이고 양변을 $t$ 에 대하여 미분하면 

    $$ \frac{dx}{dt} = \frac{1}{3} $$

    이다. $\int_{}^{}$ 안에서 $dx, dt$ 를 자유롭게 약분, 곱셈 등을 할 수 있으므로 

    $$ dx = \frac{1}{3}dt $$

    이다. 따라서

    $$ \int_{}^{}(3x+2)^{2}dx = \int_{}^{}t ^{2} \circ \frac{1}{3}dt $$

    이므로

    $$ = \frac{1}{3} \int_{}^{}t ^{2}dt = \frac{1}{3} \circ \frac{1}{3} t ^{3}+C = \frac{1}{9} (3x+2) ^{3}+C$$

    이다.

## 치환적분법을 이용한 부정적분 계산 

피적분함수의 형태에 따라 다음의 경우로 나누어 정의한다.

- 피적분함수가 $f(g(x))g'(x)$ 꼴인 경우 : 함수 $f(x)$ 의 한 부정적분이 $F(x)$ 이고 $g(x) = t$ 라고 하면

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

    $$ \int_{}^{}x(x ^{2}+1)^{5}dx = \frac{1}{2} \int_{}^{}(x ^{2}+1) ^{5} \circ 2xdx = \frac{1}{2} \int_{}^{}f(g(x)) \circ g'(x)dx = \frac{1}{2} \circ \frac{1}{6}t ^{6} + C = \frac{1}{12}t ^{6}+C $$

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

    $$ \int_{}^{}x(x ^{2}+1)^{5}dx = \frac{1}{2} \int_{}^{}(x ^{2}+1) ^{5} \circ 2xdx = \frac{1}{2} \int_{}^{} t ^{5}dt = \frac{1}{12}t ^{6}+C $$

    이다. 그러므로

    $$ \therefore \int_{}^{}x(x ^{2}+1)^{5}dx = \frac{1}{12}(x ^{2}+1)^{6}+C $$

    이다.

- 피적분함수가 $\frac{f'(x)}{f(x)}$ 꼴인 경우 : 

  $$ \int_{}^{}\frac{f'(x)}{f(x)} = \ln |f(x)|+C $$

  - 증명 

    $f(x)=t$ 로 두면 

    $$ f'(x) = \frac{dt}{dx} \Rightarrow  f'(x)dx = dt $$

    이다. 따라서

    $$ \int_{}^{}\frac{f'(x)}{f(x)}dx = \int_{}^{}\frac{1}{t}dt = \ln |t|+C = \ln |f(x)|+C $$

    이다. 
  
  - 예시 

    $$ \int_{}^{}\frac{x^2}{x^3-4}dx $$

    에서 $(x ^{3}-4)'=3x ^{2}$ 이므로 

    $$ \int_{}^{}\frac{x^2}{x^3-4}dx = \frac{1}{3} \int_{}^{}\frac{3x^2}{x^3-4}dx=\frac{1}{3}\ln |x ^{3}-4|+C $$

## 유리함수의 부정적분 

피적분함수가 $\frac{f'(x)}{f(x)}$ 꼴이 아닌 유리함수의 부정적분은 분모, 분자의 차수에 따라 다음과 같이 구한다.

- (분자의 차수) $<$ (분모의 차수) 이고 분모가 인수분해되는 경우 : 피적분함수를 부분분수로 변형하여 부정적분을 구한다.

- (분자의 차수) $\geq$ (분모의 차수) 인 경우 : 분자를 분모로 나누어 몫