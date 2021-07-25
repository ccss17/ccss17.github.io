# 지수함수와 로그함수의 극한


!!! tldr ""

    지수함수 $y=a ^{x}(a>0, a \neq 1)$ 의 극한 : 다음과 같이 $x$ 가 상수에 한없이 가까워지는 경우와 무한대로 발산하는 경우로 나누어서 생각할 수 있다.

- $x$ 가 상수에 한없이 가까워질 때

    $$ \lim_{x \to r} a ^{x} = a ^{r} $$

    - 증명 

        지수함수의 그래프에서 모든 실수에 대하여 함수가 연속임을 알 수 있다. 

        즉, 모든 실수에 대하여 극한값과 함수값이 같다. 그러므로 

        $$ \therefore \lim_{x \to r} a ^{x} = a ^{r} $$

        이다. 

- $x$ 가 무한대로 발산할 때 $a$ 의 값의 범위를 나누어 다음과 같이 단순화된 경우로 구분한다. 

    - $a>1$ 일 때 

        $$ \lim_{x \to \infty} a ^{x} = \infty , \lim_{x \to -\infty} a ^{x} = 0 $$

        - 예시

            다음은 $y = 2 ^{x}$ 의 그래프이다. 그래프를 통해 각각의 경우의 지수함수 극한을 확인해보자. 

            ![desmos-graph](https://user-images.githubusercontent.com/16812446/76310253-c93c7d80-6311-11ea-9deb-290f84400ed6.png)

            그래프에서 

            $$ \lim_{x \to 1} 2 ^{x} = 2 ^{1} $$

            임을 알 수 있다. 또 그래프에서 

            $$ \lim_{x \to \infty } 2 ^{x} = \infty $$

            임을 알 수 있다. 또 그래프에서 

            $$ \lim_{x \to -\infty } 2 ^{x} = 0 $$

            임을 알 수 있다.

    - $0<a<1$ 일 때 

        $$ \lim_{x \to \infty} a ^{x} = 0, \lim_{x \to -\infty} a ^{x} = \infty $$

        - 예시

            다음은 $y = (\frac{1}{2})^{x}$ 의 그래프이다. 그래프를 통해 각각의 경우의 지수함수 극한을 확인해보자. 

            ![desmos-graph(1)](https://user-images.githubusercontent.com/16812446/76310427-21737f80-6312-11ea-9c9f-7b2b231a7d09.png)

            그래프에서 

            $$ \lim_{x \to 1} (\frac{1}{2})^{x} = \frac{1}{2} $$

            임을 알 수 있다. 또 그래프에서 

            $$ \lim_{x \to \infty } (\frac{1}{2})^{x} = 0 $$

            임을 알 수 있다. 또 그래프에서 

            $$ \lim_{x \to -\infty } (\frac{1}{2})^{x} = \infty $$

            임을 알 수 있다.

!!! tldr ""

    로그함수 $y= \log_{a} x(a>0, a \neq 1)$ 의 극한 : 다음과 같이 $x$ 가 $0$ 이 아닌 상수에 한없이 가까워지는 경우와 무한대로 발산하는 경우 또는 $0$ 에 한없이 가까워지는 경우로 나누어서 생각할 수 있다.

- $x$ 가 상수에 한없이 가까워질 때

    $$ \lim_{x \to r} \log_{a} x = \log_{a} r (단, r > 0) $$

    - 증명 

        로그함수의 그래프를 보면 모든 양의 실수에서 연속임을 알 수 있다. 

        따라서 모든 양의 실수에 대하여 극한값이 함수값과 같다. 그러므로 

        $$ \therefore \lim_{x \to r} \log_{a} x = \log_{a} r $$ 

        임을 알 수 있다. 

- $x$ 가 무한대로 발산하거나 $0$ 에 한없이 가까워지는 경우 때 $a$ 의 값의 범위를 나누어 다음과 같이 단순화된 경우로 구분한다. 

    - $a>1$ 일 때 

        $$ \lim_{x \to \infty} \log_{a} x = \infty, \lim_{x \to 0+} \log_{a} x = - \infty $$

        - 예시 

            다음은 $y = \log_{2} x$ 의 그래프이다. 그래프를 통해 각각의 경우의 로그함수 극한을 확인해보자. 

            ![desmos-graph(2)](https://user-images.githubusercontent.com/16812446/76377726-fbd88b80-638e-11ea-8fa0-b82d86c712bc.png)

            그래프에서 

            $$ \lim_{x \to 2} \log_{2} x = 1 $$

            임을 알 수 있다. 또 그래프에서 

            $$ \lim_{x \to \infty } \log_{2}x = \infty $$

            임을 알 수 있다. 또 그래프에서 

            $$ \lim_{x \to 0+ } \log_{2}x = -\infty $$

            임을 알 수 있다.

    - $0<a<1$ 일 때 

        $$ \lim_{x \to \infty} \log_{a} x = - \infty, \lim_{x \to 0+} \log_{a} x = \infty $$

        - 예시 

            다음은 $y = \log_{\frac{1}{2}} x$ 의 그래프이다. 그래프를 통해 각각의 경우의 로그함수 극한을 확인해보자. 

            ![desmos-graph(3)](https://user-images.githubusercontent.com/16812446/76377927-7bfef100-638f-11ea-8f49-23185fc87ab3.png)

            그래프에서 

            $$ \lim_{x \to \frac{1}{2}} \log_{\frac{1}{2}} x = 1 $$

            임을 알 수 있다. 또 그래프에서 

            $$ \lim_{x \to \infty } \log_{\frac{1}{2}}x = -\infty $$

            임을 알 수 있다. 또 그래프에서 

            $$ \lim_{x \to 0+ } \log_{\frac{1}{2}}x = \infty $$

            임을 알 수 있다.

## 무리수 $e$ 와 자연로그

!!! tldr ""

    무리수 $e$ : 무리수 $e$ 는 다음과 같이 정의한다. 
    
    $$ \lim_{x \to 0} (1+x) ^{\frac{1}{x}} = e $$

- 위의 정의에서 $\frac{1}{x} = t$ 로 놓으면 $x \to 0+ \implies t \to \infty$ 이다. 따라서

    $$ \lim_{t \to \infty} (1+\frac{1}{t}) ^{t} = e $$

    즉,

    $$ \lim_{x \to \infty} (1+\frac{1}{x}) ^{x} = e $$

    와 같이 정의할 수도 있다. 

    - 급수를 통하여 다음과 같이 정의할 수도 있다. 

        $$ e = \sum_{n=0}^{\infty}\frac{1}{n!} $$

- 무리수에 속하며 초월수로 알려져 있다. 

    - 그 값은 $e=2.718281 \dots$ 로 알려져 있다. 

    - $\pi, 1, 0, i$ 와 함께 $e$ 는 수학에서 가장 중요한 상수로 여겨진다. 

- $1618$ 년 네이피어가 로그 계산 과정에서 나온 간단한 결과값으로 $e$ 를 다루었지만 상수로 취급하지는 않았다. 이후 오트리드가 네이피어의 로그표로 로그 계산자를 만들었으나 $e$ 를 특별한 상수로 여기지는 않았다. 

    - 복리이자 계산

        단리 이자는 원금에 대하여 이자가 붙는 규칙이고 복리 이자는 원금에 붙은 이자를 합한 금액에서 이자를 계산하는 방식이다. 가령 이자가 $3%$ 에 원금이 $1000$ 만원이면 단리 이자는 매달 $30$ 만원의 이자가 발생하나 복리 이자는 첫째달 $30(1000 \times 0.03)$ 만원, 둘째달 $30.9(1030 \times 0.03)$ 만원, 셋째달 $31.827(1060.9 \times 0.03)$ 만원인 식이다. 

        이것을 정리하여 원금을 $a$, $n$ 번째 달 원리금을 $a_n$, 이자율을 $b$ 라고 하면 

        $$a_1 = a$$

        $$a_2 = a_1 + a_1 \times \frac{b}{100} = a_1(1+\frac{b}{100}) = a(1+\frac{b}{100})$$

        $$a_3 = a_2 + a_2 \times \frac{b}{100} = a_2(1+\frac{b}{100}) = a(1+\frac{b}{100}) ^{2}$$

        이므로 $n$ 번째 달 원리금은 

        $$ a_n = a _{n-1} + a _{n-1} \times \frac{b}{100} = a _{n-1}(1+\frac{b}{100}) = a (1+\frac{b}{100}) ^{n-1} $$

        이다. 

    이후에 야코프 베르누이가 위와 같은 복리 이자의 계산에서 기간을 $n$ 으로 두었을 때 이자율을 $\frac{1}{n}$ 으로 두면 복리이자가 다음과 같이 특정한 비율로 점근한다는 것을 발견하였다.

    $$ \lim_{n \to \infty} (1+\frac{1}{n}) ^{n} = 2.71823 \dots = e$$

    라이프니츠는 $1691$ 년에 베르누이가 정리한 이 급수를 최초로 상수 $b$ 로 표현했다. $1727$ 년 오일러는 비로소 이 상수를 $e$ 로 표현하고 사용하기 시작했다. 

- 예시 

    $$ \lim_{x \to 0} (1+3x) ^{\frac{1}{x}} = \lim_{x \to 0} \{(1+3x)^{\frac{1}{3x}}\} ^{3} = e ^{3} $$

    $$ \lim_{x \to \infty} (1+\frac{2}{x}) ^{x} = \lim_{x \to \infty} \{(1+\frac{2}{x})^{\frac{x}{2}}\} ^{2} = e ^{2} $$

!!! tldr ""

    자연로그 : 무리수 $e$ 를 밑으로 하는 로그 $\log_{e} x$ 를 $x$ 의 자연로그라 한다.

- 자연로그 $\log_{e} x$ 를 간단히 $\ln x$ 로 나타낸다. 

- 자연이라는 수식어는 자연로그의 도함수를 도출하는 과정에서 밑이 동시에 자연스럽게 정의된다는 점이나, 자연로그의 밑을 지수의 밑으로 하는 지수함수의 미분 등에서 아주 깔끔한 결과가 얻어지는 데서 유래했다. (나무위키)

- 다음과 같은 관계가 성립한다. 

    - $\ln e = \log_{e} e = 1$

    - $\ln 1 = \log_{e} 1 = 0$

!!! tldr ""

    무리수 $e$ 를 이용한 지수함수와 로그함수의 극한 : $a>0, a \neq 0$ 일 때 다음이 성립한다. 
    
    1. $\displaystyle \lim_{x \to 0} \frac{\log_{a} (1+x)}{x} = \frac{1}{\ln a}$
    
    2. $\displaystyle \lim_{x \to 0} \frac{a ^{x}-1}{x} = \ln a$

- $1$ 의 증명 

    $$ \lim_{x \to 0} \frac{\log_{a} (1+x)}{x} = \lim_{x \to 0} \log_{a} (1+x) ^{\frac{1}{x}} = \log_{a} e = \frac{1}{\ln a} $$

- 그러므로 $a = e$ 일 때 

    $$ \lim_{x \to 0} \frac{\ln (1+x)}{x} = 1 $$

    이다. 

- $2$ 의 증명 

    $a ^{x} -1 = t$ 로 두면 $x \to 0 \implies t \to 0$ 이고 $a ^{x} = 1+t$ 에서 

    $$ \therefore x = \log_{a} (1+t) $$

    이다. 따라서 

    $$ \lim_{x \to 0} \frac{a ^{x}-1}{x} = \lim_{t \to 0} \frac{t}{\log_{a} (1+t)} = \lim_{t \to 0} \frac{1}{\frac{\log_{a} (1+t)}{t}} $$

    $$ = \lim_{t \to 0} \frac{1}{\log_{a} (1+t) ^{\frac{1}{t}}} = \frac{1}{\log_{a} e} = \ln a $$

- 그러므로 $a = e$ 일 때 

    $$ \lim_{x \to 0} \frac{e ^{x}-1}{x} = e $$

    이다. 

## 지수함수와 로그함수의 미분

!!! tldr ""

    지수함수 $y=a ^{x}$ 의 도함수 : 지수함수 $y=a ^{x}$ 의 도함수는 
    
    $$ (a ^{x})' = a ^{x} \ln a $$
    
    이다.

- 증명 

    도함수의 정의에 따라 지수함수 $y=a ^{x}(a>0, a \neq 1)$ 의 도함수는 

    $$ y' = \lim_{h \to 0} \frac{f(a+h)-f(a)}{h} = \lim_{h \to 0} \frac{a ^{x+h}-a ^{x}}{h}  $$

    $$ = \lim_{h \to 0} \frac{a ^{x}(a ^{h}-1)}{h} = a ^{x} \lim_{h \to 0} \frac{a ^{h}-1}{h} = a ^{x} \ln a $$

    이다. 그러므로 

    $$ (a ^{x})' = a ^{x}\ln a $$

!!! tldr ""

    $y = e ^{x}$ 의 도함수 : 지수함수 도함수의 정의에 따라 밑이 $e$ 일 때, 즉 $a=e$ 일 때 지수함수 $y = e ^{x}$ 의 도함수는 
    
      $$ (e ^{x})' = e ^{x} $$
    
      이다.

!!! tldr ""

    로그함수 $y = \log_{a} x$ 의 도함수 : 로그함수 $y = \log_{a} x(a>0, a \neq 1)$ 의 도함수는 
    
    $$ (\log_{a} x)' = \frac{1}{x \ln a} $$
    
    이다.

- 증명 

    도함수의 정의에 따라 로그함수 $y=\log_{a} x(a>0, a \neq 1)$ 의 도함수를 구해보자.

    $$ y' = \lim_{h \to 0} \frac{f(a+h)-f(a)}{h} = \lim_{h \to 0} \frac{\log_{a} (x+h)-\log_{a} x}{h} = \lim_{h \to 0} \frac{1}{h} \log_{a} \frac{x+h}{x} $$

    $$ = \lim_{h \to 0} \frac{1}{x} \cdot \frac{x}{h} \log_{a} (1+\frac{h}{x}) = \frac{1}{x} \lim_{h \to 0} \log_{a} (1+\frac{h}{x}) ^{\frac{x}{h}} $$

    이때 $\frac{h}{x} = t$ 로 두면 $h \to 0 \implies t \to 0$ 이므로

    $$ = \frac{1}{x} \lim_{t \to 0} \log_{a} (1 + t)^{\frac{1}{t}} = \frac{1}{x}\log_{a} e $$

    최종적으로

    $$ \therefore (\log_{a} x)' = \frac{1}{x\ln a} $$

    이다.

!!! tldr ""

    자연로그함수 $y = \ln x$ 의 도함수 : 로그함수 도함수의 정의에 따라 밑이 $e$ 일 때, 즉 $a=e$ 일 때 자연로그함수 $y = \ln x$ 의 도함수는 
    
    $$ (\ln x)' = \frac{1}{x} $$
    
    이다.

## 정의역이 확장된 로그함수의 미분

지금까지의 로그함수의 미분은 정의역이 양의 실수 집합에서만 성립한다. 그러나 이제 정의역을 확장해보자.

!!! tldr ""

    로그함수 $y = \ln |x|$ 의 도함수 : 로그함수 $y = \ln |x|$ 의 도함수는 
    
    $$ (\ln |x|)' = \frac{1}{x} $$
    
    이다.

- 증명 

    $x$ 의 범위를 축소시켜 상황을 단순화시켜보자. 

    $x>0$ 일 때 $y = \ln |x| = \ln x$ 이므로 $y'=\frac{1}{x}$ 이다. 

    $x<0$ 일 때 $y = \ln |x| = \ln (-x)$ 이므로 $y'=\frac{(-x)'}{-x}=\frac{-1}{-x}=\frac{1}{x}$ 이다. 

    그러므로 단순화된 상황을 다시 일반화하면

    $$ \therefore (\ln |x|)' = \frac{1}{x} $$

    이다.

!!! tldr ""

    로그함수 $y = \log_{a} |x|$ 의 도함수 : 로그함수 $y = \log_{a} |x|$ 의 도함수는 
    
    $$ (\log_{a} |x|)' = \frac{1}{x \ln a} $$
    
    이다.

- 증명 

    로그함수 $y = \ln |x|$ 의 도함수를 이용하여

    $$y' = (\log_{a} |x|)' = (\frac{\ln |x|}{\ln a})' = \frac{(\ln |x|)'}{\ln a} = \frac{1}{x} \cdot \frac{1}{\ln a} = \frac{1}{x \ln a}$$

    이다. 그러므로

    $$ \therefore (\log_{a} |x|) = \frac{1}{x \ln a} $$

- 그런데 정의역이 양의 실수로 국한된 로그함수의 도함수와 절대값 연산으로 정의역이 확장된 로그함수의 도함수가 서로 같으므로 로그함수의 도함수를 구할 때 절대값을 무시할 수 있다. 

# 삼각함수의 극한

!!! tldr ""

    삼각함수의 극한 : 임의의 실수 $a$ 에 대하여 삼각함수의 극한은 다음과 같다.

- $\lim_{x \to a} \sin x = \sin a$

- $\lim_{x \to a} \cos x = \cos a$

- $\lim_{x \to a} \tan x = \tan a$ (단, $a \neq n \pi  + \frac{\pi }{2}$, $n$ 은 정수)

    - 증명 

        $\sin, \cos, \tan$ 함수에서 알 수 있듯이 삼각함수는 연속함수이다. 즉, 임의의 실수 $a$ 에 대하여 $x \to a$ 에서의 극한값은 $x=a$ 에서의 함수값과 같으므로 

        $$ \lim_{x \to a} \sin x = a, \lim_{x \to a} \cos x = a $$

        이다.

        그런데 $\tan$ 함수는 임의의 정수 $n$ 에 대하여 $x= (\frac{1 }{2} + n)\pi$ 에 대하여 불연속이고 나머지 구간에서는 연속이다. 그러므로 $a \neq (\frac{1}{2}+n) \pi$ 인 임의의 실수 $a$ 에 대하여 $x \to a$ 일 때 극한값이 $x=a$ 에서의 함수값과 같으므로 

        $$ \lim_{x \to a} \tan x = a $$

        이다.

        $a = (\frac{1}{2}+n) \pi$ 인 임의의 실수 $a$ 에서는 

        $$ \lim_{x \to a-} \tan x = \infty , \lim_{x \to a+} \tan x = - \infty $$

        가 되어 극한값이 존재하지 않는다.

!!! tldr ""

    함수 $\frac{\sin x}{x}, \frac{\tan x}{x}$ 의 극한 : $x$ 가 라디안일 때 다음이 성립한다.

- $\lim_{x \to 0} \frac{\sin x}{x} = 1$

  - 증명 

    중심각 $\theta$ 를 갖는 부채꼴과 부채꼴에 내접한 삼각형, 외접한 삼각형의 넓이의 관계 부등식으로부터 부채꼴의 중심각이 $0$ 에 한없이 가까워질 때 세 넓이가 같아지는 것(샌드위치 정리)을 이용하여 

    $$ \lim_{x \to 0} \frac{\sin x}{x} = 1 $$

    를 증명할 수 있다. 하지만 단순하게 $y = \frac{\sin x}{x}$ (단, $x \neq 0$) 그래프를 그려보자.

    ![desmos-graph(4)](https://user-images.githubusercontent.com/16812446/76512654-6b866d80-6498-11ea-8e90-9c0e89854eb6.png)

    그러면 그래프가 위와 같은데, 물론 $x=0$ 에서 함수값은 정의되지 않지만 $x \to 0$ 에서의 극한값은 $1$ 이기 때문에

    $$ \therefore  \lim_{x \to 0} \frac{\sin x}{x} = 1 $$

    임을 알 수 있다. 

- $\lim_{x \to 0} \frac{\tan x}{x} = 1$

    - 증명 

        $$ \lim_{x \to 0} \frac{\tan x}{x} = \lim_{x \to 0} \frac{\sin x}{x \cos x} = \lim_{x \to 0} (\frac{\sin x}{x} \cdot \frac{1}{\cos x}) $$

        $$ = \lim_{x \to 0} \frac{\sin x}{x} \cdot \lim_{x \to 0} \frac{1}{\cos x} = 1 \cdot 1 = 1 $$

        그러므로 

        $$ \therefore \lim_{x \to 0} \tan x = 1 $$

        이다. 다음 그래프 $y=\frac{\tan x}{x}$ 에서도 $x \to 0 \implies \tan x \to 1$ 임을 확인할 수 있다. 물론 다음 그래프도 $x=0$ 에서 함수값은 정의되어있지 않다. 

        ![desmos-graph(5)](https://user-images.githubusercontent.com/16812446/76512834-b56f5380-6498-11ea-8ebb-40991579d7e4.png)

- $\lim_{x \to 0} \frac{\cos x}{x}$ 는 발산한다. 

    - 증명 

        $$ \lim_{x \to 0+} \cos x = 1, \lim_{x \to 0+} \frac{1}{x} = \infty $$

        이므로

        $$ \lim_{x \to 0+} \frac{\cos x}{x} = \infty $$

        인데 반해 

        $$ \lim_{x \to 0-} \cos x = 1, \lim_{x \to 0-} \frac{1}{x} = -\infty $$

        이므로

        $$ \lim_{x \to 0-} \frac{\cos x}{x} = -\infty $$

        이다. 

        즉, $\frac{\cos x}{x}$ 는 $x=0$ 에서 우극한과 좌극한이 같지 않다. 따라서 $x=0$ 에서 극한값은 존재하지 않는다. 함수 $y = \frac{\cos x}{x}$ 의 그래프는 다음과 같다. 

        ![desmos-graph(6)](https://user-images.githubusercontent.com/16812446/76513437-a4731200-6499-11ea-87ae-a6646df7cc60.png)

# 삼각함수의 도함수

!!! tldr ""

    함수 $y = \sin x$ 의 도함수 : $y' = \cos x$ 이다.

- 증명 

    삼각함수 $y = \sin x$ 의 도함수는 도함수의 정의에 의하여 

    $$ y' = \lim_{h \to 0} \frac{f(x+h)-f(x)}{h} = \lim_{h \to 0} \frac{\sin (x+h)-\sin x}{h} $$

    이다. 이때 사인함수의 덧셈정리에 의하여 

    $$ = \lim_{h \to 0} \frac{\sin x\cos h + \cos x \sin h -\sin x}{h} $$

    $$ = \lim_{h \to 0} \frac{\sin x(\cos h -1) + \cos x \sin h }{h} $$

    $$ = \sin x \lim_{h \to 0} \frac{(\cos h - 1)}{h} + \cos x \lim_{h \to 0} \frac{\sin h}{h} $$

    이다. 그런데 $\lim_{x \to 0} \frac{\sin x}{x} = 1$ 이므로 

    $$ = \sin x \times 0 + \cos x \times 1 $$

    이다. 따라서 최종적으로 

    $$ \therefore (\sin x)' = \cos x $$

    이다.

!!! tldr ""

    함수 $y = \cos x$ 의 도함수 : $y' = -\sin x$ 이다.

- 증명 

    삼각함수 $y = \cos x$ 의 도함수는 도함수의 정의에 의하여 

    $$ y' = \lim_{h \to 0} \frac{f(x+h)-f(x)}{h} = \lim_{h \to 0} \frac{\cos (x+h)-\cos x}{h} $$

    이다. 이때 코사인함수의 덧셈정리에 의하여 

    $$ = \lim_{h \to 0} \frac{\cos x\cos h - \sin x \sin h -\cos x}{h} $$

    $$ = \lim_{h \to 0} \frac{\cos x(\cos h -1) - \sin x \sin h }{h} $$

    $$ = \cos x \lim_{h \to 0} \frac{(\cos h - 1)}{h} - \sin x \lim_{h \to 0} \frac{\sin h}{h} $$

    이다. 그런데 $\lim_{x \to 0} \frac{\sin x}{x} = 1$ 이므로 

    $$ = \cos x \times 0 - \sin x \times 1 $$

    이다. 따라서 최종적으로 

    $$ \therefore (\cos x)' = -\sin x $$

    이다.

!!! tldr ""

    함수 $y = \tan x$ 의 도함수 : $y' = \sec ^{2} x$ 이다.

- 증명 

    $\tan x = \frac{\sin x}{\cos x}$ 이므로 몫의 미분을 사용하면 

    $$ (\tan x)' = (\frac{\sin x}{\cos x})' = \frac{(\sin x)'\cos x - \sin x(\cos x)'}{\cos ^{2}x} $$

    $$ \frac{\cos x \cdot \cos x - \sin x \cdot (- \sin x)}{\cos ^{2}x} = \frac{\cos ^{2}x + \sin ^{2}x}{\cos ^{2}x} = \frac{1}{\cos ^{2}x} = \sec ^{2} x$$

!!! tldr ""

    함수 $y = \sec x$ 의 도함수 : $y' = \sec x \tan x$ 이다.

- 증명 

    $\sec x = \frac{1}{\cos x}$ 이므로 몫의 미분을 사용하면 

    $$ (\sec x)' = (\frac{1}{\cos x})' = -\frac{(\cos x)'}{\cos ^{2}x}= \frac{\sin x}{\cos ^{2}x} = \frac{1}{\cos x} \cdot \frac{\sin x}{\cos x} = \sec x \tan x$$

    이다. 따라서 

    $$ \therefore  (\sec x)' = \sec x \tan x $$

    이다.

!!! tldr ""

    함수 $y = \csc x$ 의 도함수 : $y' = -\csc x \cot x$ 이다.

- 증명 

    $\csc x = \frac{1}{\sin x}$ 이므로 몫의 미분을 사용하면 

    $$ (\csc x)' = (\frac{1}{\sin x})' = -\frac{(\sin x)'}{\sin ^{2}x}= -\frac{\cos x}{\sin ^{2}x} = -\frac{1}{\sin x} \cdot \frac{\cos x}{\sin x} = - \csc x \cot x$$

    이다. 따라서 

    $$ \therefore  (\csc x)' = - \csc x \cot x $$

    이다.

!!! tldr ""

    함수 $y = \cot x$ 의 도함수 : $y' = -\csc ^{2} x$ 이다.

- 증명 

    $\cot x = \frac{\cos x }{\sin x}$ 이므로 분수함수 미분을 사용하면 

    $$ (\cot x)' = (\frac{\cos x}{\sin x})' = \frac{(\cos x)'\sin x - \cos x(\sin x)'}{\sin ^{2}x} = \frac{-\sin ^{2} x - \cos ^{2} x}{\sin ^{2}x} = -\frac{1}{\sin ^{2}x} = - \csc ^{2}x$$

    이다. 따라서 

    $$ \therefore  (\cot x)' = - \csc ^{2}x $$

    이다.

## 복잡한 함수의 도함수

!!! tldr ""

    로그함수 $y = \ln |f(x)|$ 의 도함수 : 함수 $f(x)$ 가 미분가능하고 $f(x) \neq 0$ 일 때 로그함수 $y = \ln |f(x)|$ 의 도함수는
    
    $$\{\ln |f(x)|\}' = \frac{f'(x)}{f(x)}$$ 
    
    이다.

- 증명 

    함수 $f(x)$ 가 미분가능하고 $f(x) \neq 0$ 일 때 로그함수 $y = \ln |f(x)|$ 의 도함수를 구해보자. 먼저 로그가 정의되도록 $f(x)$ 의 값의 범위를 나누어서 절대값 연산을 풀자.

    $f(x) > 0$ 일 때 $|f(x)| = f(x)$ 이므로 

    $$ y' = \{\ln |f(x)|\}' = \{\ln f(x)\}' = \frac{f'(x)}{f(x)} $$

    이다.

    $f(x) < 0$ 일 때 $|f(x)| = -f(x)$ 이므로 

    $$ y' = \{\ln |f(x)|\}' = \{\ln -f(x)\}' = \frac{-f'(x)}{-f(x)} = \frac{f'(x)}{f(x)}$$

    이다. 

    단순화된 상황을 일반적인 상황으로 병합하면

    $$ \{\ln |f(x)|\}' = \frac{f'(x)}{f(x)} $$

    이다.

!!! tldr ""

    로그함수 $y = \log_{a} |f(x)|(a>0, a \neq 1)$ 의 도함수 : 함수 $f(x)$ 가 미분가능하고 $f(x) \neq 0$ 일 때 로그함수 $y = \ln |f(x)|$ 의 도함수는
    
    $$\{\ln |f(x)|\}' = \frac{f'(x)}{f(x)\ln a}$$ 
    
    이다.

- 증명 

    로그함수 $y = \ln |f(x)|$ 의 도함수를 이용하여 로그함수 $y = \log_{a} |f(x)|(a>0, a \neq 1)$ 의 도함수를 구해보자. 

    $$ y' = (\log_{a} |f(x)|)' = (\frac{\ln |f(x)|}{\ln a})' = \frac{(\ln |f(x)|)'}{\ln a} = \frac{f'(x)}{f(x)} \cdot \frac{1}{\ln a} = \frac{f'(x)}{f(x)\ln a} $$

    그러므로 

    $$ \therefore  (\log_{a} |f(x)|)' = \frac{f'(x)}{f(x)\ln a} $$

    이다.

!!! tldr ""

    로그미분법 : 밑과 지수에 변수가 포함되어 있는 함수나 복잡한 분수함수는 다음과 같이 미분하면 편할 때가 있다. 
    
    1. $y=f(x)$ 양 변에 절대값을 취한다.
    
        $$ |y| = |f(x)| $$
    
    2. 양변에 자연로그를 취한다. 
    
        $$ \ln |y| = \ln |f(x)| $$
    
    3. 양변을 $x$ 에 대하여 미분한다. 
    
        $$ \frac{y'}{y} = \frac{f'(x)}{f(x)} $$
    
    4. $y'$ 에 대하여 정리한다. 
    
        $$ y' = y \cdot \frac{f'(x)}{f(x)} $$

- 예시 

    함수 $f(x) = x ^{\sin x}(x>0)$ 의 도함수를 구해보자.

    함수 $f(x)$ 의 함수값은 항상 양수이니 양변에 자연로그를 취하면 

    $$ y = x ^{\sin x} $$

    에서 

    $$ \ln y = \ln x ^{\sin x} $$

    이다. 이때 양변을 $x$ 에 대하여 미분하면 

    $$ \frac{y'}{y} = (\sin x)'\ln x + \sin x(\ln x)' = \cos x \cdot \ln x + \sin x \cdot \frac{1}{x} $$

    $$ y' = y(\cos x \cdot \ln x + \sin x \cdot \frac{1}{x}) $$

    에서 

    $$ \therefore y' = x ^{\sin x}(\cos x \cdot \ln x + \frac{\sin x}{x}) $$

    이다.

!!! tldr ""

    함수 $y = x ^{n}$ 의 도함수 : $n$ 이 실수일 때, $y' = f'(x) = nx ^{n-1}$

- 증명 

    우리는 앞서 정수 $n$ 에 대하여 $n$차 단항 함수 $y = x ^{n}$ 의 도함수가 $y' = n x ^{n-1}$ 임을 알아보았었다. 이제 로그미분법으로 $n$ 이 실수일 때 함수 $y= x ^{n}$ 의 도함수를 구해보자.

    $y = x ^{n}$ 의 양변의 절대값에 자연로그를 취하면 

    $$ \ln |y| = \ln |x ^{n}| $$

    $$ \ln |y| = n\ln |x| $$

    이다. 이때 양변을 $x$ 에 대하여 미분하면 

    $$ \frac{y'}{y} = n \cdot \frac{1}{x} $$

    $$ y' = y \cdot n \cdot \frac{1}{x} $$

    $$ y' = x ^{n} \cdot n \cdot \frac{1}{x} $$

    에서 

    $$ \therefore y' = n x ^{n-1} $$

    이다. 

- 예시 

    $y = x ^{\sqrt[]{3}}$ 의 도함수는 $y' = \sqrt[]{3} x ^{\sqrt[]{3}-1}$ 이다. 

- 예시 

    $y = x ^e$ 의 도함수는 $y'=ex^{e-1}$ 이다.

## 매개변수로 나타낸 함수의 미분

!!! tldr ""

    매개변수(parameter)로 나타낸 함수 : 두 변수 $x, y$ 사이의 관계를 변수 $t$ 를 매개로 
    
    $$ x = f(t), y = g(t) $$
    
    꼴로 나타낼 때, 변수 $t$ 를 매개변수라 하고 위 식을 매개변수로 나타낸 함수라 한다.

!!! tldr ""

    매개변수로 나타낸 함수의 미분법 : 두 함수 $x=f(t),y=g(t)$ 에서 $f(t),g(t)$ 가 각각 $t$ 에 대하여 미분가능하고 $f'(t) \neq 0$ 일 때 
    
    $$ \frac{dy}{dx} = \frac{\frac{dy}{dt}}{\frac{dx}{dt}} = \frac{g'(t)}{f'(t)} $$

- 증명 

    두 함수 $x=f(t), y=g(t)$ 가 각각 $t$ 에 대하여 미분가능하고 $f'(t) \neq 0$ 라고하자. 그러면 $x = f(t)$ 의 역함수가 존재하고 $t$ 는 $x$ 에 대한 함수이므로 $y=g(t)$ 도 $x$ 에 대한 함수로 볼 수 있다. 또 매개변수 $t$ 의 증분 $\Delta t$ 에 대한 $x$ 의 증분을 $\Delta x$, $y$ 의 증분을 $\Delta y$ 라 하자.

    그러면 $x$ 가 $t$ 에 대해서 미분가능하기 때문에 

    $$ \lim_{\Delta x \to 0}  \frac{\Delta t}{\Delta x} $$

    의 값이 존재한다. 그런데 분모가 $0$ 에 한없이 다가가는데도 그 값이 존재하므로 분자도 $0$ 에 다가간다. 따라서

    $$ \Delta x \to 0 \implies \Delta t \to 0 $$

    이다. 또 이것으로 도함수의 정의에 의한 $x$ 에 대한 $y$ 의 미분

    $$ \frac{dy}{dx} = \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x} $$

    을

    $$ \lim_{\Delta t \to 0} \frac{\frac{\Delta y}{\Delta t}}{\frac{\Delta x}{\Delta t}} $$

    로 쓸 수 있다. 즉,

    $$ \frac{dy}{dx} = \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x} = \lim_{\Delta t \to 0} \frac{\frac{\Delta y}{\Delta t}}{\frac{\Delta x}{\Delta t}} $$

    이다. 이때

    $$ \Delta x = f(t+\Delta t) - f(t), \Delta y = g(t+\Delta t) - g(t) $$

    이므로 

    $$ \lim_{\Delta t \to 0} \frac{\frac{\Delta y}{\Delta t}}{\frac{\Delta x}{\Delta t}} = \frac{\lim_{\Delta t \to 0} \frac{\Delta y}{\Delta t}}{\lim_{\Delta t \to 0} \frac{\Delta x}{\Delta t}} = \frac{\lim_{\Delta t \to 0} \frac{g(t+\Delta t) - g(t)}{\Delta t} }{\lim_{\Delta t \to 0} \frac{f(t+\Delta t)-f(t)}{\Delta t}} = \frac{\frac{dy}{dt}}{\frac{dx}{dt}} = \frac{g'(t)}{f'(t)} $$

    이다. 그러므로 

    $$ \therefore \frac{dy}{dx} = \frac{g'(t)}{f'(t)} $$

    이다.

- 예시 

    매개변수로 나타낸 함수 $x=\frac{1+t}{1-t}, y=\frac{3t}{1+t}$ 에서 $\frac{dy}{dx}$ 를 구하자. 

    $$\frac{dx}{dt}=\frac{1-t+(1+t)}{(1-t)^2}=\frac{2}{(1-t)^2}, \frac{dy}{dt}=\frac{3(1+t)-3t}{(1+t)^2}=\frac{3}{(1+t)^2}$$

    $$ \therefore \frac{dy}{dx} = \frac{\frac{dy}{dt}}{\frac{dx}{dt}} = \frac{\frac{3}{(1+t)^{2}}}{\frac{2}{(1-t)^2}} = \frac{3(1-t)^2}{2(1+t)^2} $$

!!! tldr ""

    음함수의 미분 : $x$ 에 대한 함수 $y$ 가 음함수 $f(x,y)=0$ 꼴로 주어질 때, $y$ 를 $x$ 에 대한 함수로 보고 각항을 $x$ 에 대하여 미분하여 $\frac{dy}{dx}$ 를 구한다.

- $y$ 가 포함된 항을 미분할 때 $x$ 에 대한 함수로 보고 합성함수의 미분법을 적용한다.

- 예시 

    $x ^{2}+ y ^{2}-1=0$ 의 각 항을 $x$ 에 대하여 미분하자. 

    $$ \frac{d}{dx}(x ^{2}) + \frac{d}{dx} (y ^{2}) - \frac{d}{dx}(1) = 0 $$

    에서 

    $$ \frac{d}{dx} x ^{2} = 2x, \frac{d}{dx} y ^{2} = 2y \cdot \frac{dy}{dx}, \frac{d}{dx}(1)=0 $$

    이므로 

    $$ 2x + 2y \cdot \frac{dy}{dx} - 0 = 0 $$

    이다. 따라서

    $$ \therefore \frac{dy}{dx} = - \frac{x}{y} $$

    이다. (단, $y \neq 0$)

!!! tldr ""

    역함수의 도함수 : 미분가능한 함수 $f(x)$ 의 역함수 $f ^{-1}(x)$ 가 존재하고 미분가능할 때 , 함수 $y = f ^{-1}(x)$ 의 도함수는 
    
    $$ (f ^{-1})'(x) = \frac{1}{f'(y)} $$
    
    또는 
    
    $$ \frac{dy}{dx} = \frac{1}{\frac{dx}{dy}} $$
    
    이다. (단, $f'(y) \neq 0, \frac{dx}{dy} \neq 0$)

- 증명

    함수 $f(x)$ 의 $x=a$ 에서의 미분계수란 함수 $f(x)$ 위의 점 $(a, b)$ 와 직선의 방정식 $g(x)$ 위의 임의의 점 $(c, d)$ 로 정의된 기울기 $f'(a) = \frac{d-b}{c-a}$ 이다.

    한편 직선을 $y=x$ 에 대하여 대칭시킨 역함수의 미분계수 $(f^{-1})'(b)$ 는 점 $(b, a)$ 와 점 $(d, c)$ 의 기울기 $(f^{-1})'(b) = \frac{c-a}{d-b}$ 이다. 따라서 함수 $f(x)$ 위의 점 $(a, b)$ 에 대하여 다음의 관계를 갖는다. 

    $$ f'(a) \cdot (f ^{-1})'(b) = 1 $$

    이제 점 $(a, b)$ 를 그것이 속한 집합으로 회귀시키자. 즉 이것을 일반화하여 함수 $f(x)$ 위의 임의의 점 $(x, y)$ 에서 

    > 이것 또한 추상화를 기계적으로 할 수 있는 방법의 예시이다. 즉 추상화와 일반화를 물질적 수준으로 끌어내려 자동적으로 할 수 있게끔 하는 방법을 계속 고민중인 것이다. 메타 수학명제를 수학명제로 끌어내려서 수학의 논리체계에서 적용되는 연산이 적용가능하게끔 한것처럼 말이다. 

    > 한편, "그렇다면 어떤 자연 대상을 수로 끌어내릴 수 있는가?" 라는 질문과 "수로 격하된 자연 대상을 어떻게 코드로 자동화 할 수 있는가?" 가 주요한 질문이 될 것이다. 

    $$ f'(x) \cdot (f ^{-1})'(y) = 1 $$

    가 성립한다. 한편 함수 $f ^{-1}(x)$ 위의 임의의 점 $(x, y)$, 즉 $y=f ^{-1}(x)$ 을 만족하는 $x, y$ 에 대하여서는 

    $$ f'(y) \cdot (f ^{-1})'(x) = 1 $$

    가 성립하여

    $$ \therefore (f^{-1})'(x)  = \frac{1}{f'(y)}  $$

    이다. 그런데 함수 $y= f ^{-1}(x)$ 를 $x$ 에 대하여 미분하면 

    $$ \frac{dy}{dx} = (f ^{-1})'(x) $$

    이고, 그 역함수 $x=f(y)$ 를 $y$ 에 대하여 미분하면 

    $$ \frac{dx}{dy}=f'(y) $$

    이므로 종전의

    $$ (f^{-1})'(x)  = \frac{1}{f'(y)}  $$

    를

    $$ \therefore  \frac{dy}{dx} = \frac{1}{\frac{dx}{dy}} $$

    로 표현할 수 있다. 

- 증명 (합성함수)

    함수 $f(x)$ 의 역함수를 $y = f ^{-1}(x)$ 라 하자. 그러면 역함수의 정의에 따라 

    $$ (f \cdot f ^{-1})(x) = x \iff f(f ^{-1}(x)) = x $$

    이고 합성합수의 미분을 적용하면 

    $$ f'(f ^{-1}(x)) \cdot \{f ^{-1}(x)\}' = 1 $$

    에서 

    $$ \therefore f ^{-1}(x) = \frac{1}{f'(f ^{-1}(x))} = \frac{1}{f'(y)} $$

    이다. 

- 예시 

    함수 $y = \sqrt[3]{x+1}$ 을 미분하자. 

    함수에 세제곱을 하여 $x$ 에 대하여 정리하면 $x = y ^{3}-1$ 이므로 $y$ 에 대하여 미분하면 

    $$ \frac{dx}{dy} = 3 y ^{2} $$

    이다. 그러므로 

    $$ \therefore \frac{dy}{dx} = \frac{1}{\frac{dx}{dy}} = \frac{1}{3y ^{2}} = \frac{1}{3 \sqrt[3]{(x+1) ^{2}}} $$

!!! tldr ""

    이계도함수(second order derivatives) : 함수 $f(x)$ 의 도함수 $f'(x)$ 가 미분가능할 때 $f'(x)$ 의 도함수
    
    $$ \lim_{\Delta x \to 0} \frac{f'(x+\Delta x)-f'(x)}{\Delta x} $$
    
    를 함수 $f(x)$ 의 이계도함수라 한다.

- 기호로

    $$f''(x) = y'' = \frac{d ^{2}y}{d x ^{2}} = \frac{d ^{2}}{d x ^{2}} f(x) $$

    라고 표현한다. 

    - 기호 

        $$\frac{d ^{2}y}{d x ^{2}}$$

        는 

        $$ \frac{d}{dx}(\frac{d}{dx}y) $$

        를 간결하게 표현한 것이다. 

- 예시 

    함수 $f(x) = x ^{3}-2x$ 의 이계도함수는 $f'(x) = 3 x ^{2} - 2$ 이므로 

    $$ \therefore  f''(x) = 6x $$

    이다.

!!! tldr ""

    고계도함수(higher order derivatives) : 함수 $f(x)$ 를 $2$ 번 이상 미분함 함수이다.

- 삼계도 함수 : 함수 $f(x)$ 를 $3$ 번 미분한 함수로써 

    $$ f'''(x) = \frac{d ^{3}y}{dx ^{3}} = \frac{d ^{3}}{dx ^{3}} f(x) $$

    로 표현한다. 

- $n$ 계도 함수 : 함수 $f(x)$ 를 $n$ 번 미분한 함수로써 

    $$ f ^{(n)} (x) = \frac{d ^{n}y}{dx ^{n}} = \frac{d ^{n}}{dx ^{n}} f(x) $$

    로 표현한다. 

- 예시 

    $$ f(x) = e ^{x} \implies f ^{(n)}(x) = e ^{x} $$

- 예시 

    $$ f(x) = \sin x \implies f ^{(n)}(x) =\sin (x+\frac{n \pi }{2}) $$

- 예시 

    $$ f(x) = \cos x \implies f ^{(n)}(x) =\cos (x+\frac{n \pi }{2}) $$

## 함수의 그래프 개형

!!! tldr ""

    곡선의 오목과 볼록의 판정 : 함수 $f(x)$ 가 어떤 구간에서 
    
    $f''(x) > 0$ 이면 곡선 $y=f(x)$ 는 이 구간에서 아래로 볼록(convex upward)하고, 
    
    $f''(x) < 0$ 이면 곡선 $y=f(x)$ 는 이 구간에서 위로 볼록(convex downward)하다.

- 증명 

    파란색 선이 구간 $[a, b]$ 에서의 직선일 때 이 구간에서 증가하는 곡선 $y=f(x)$ 를 그리면 다음과 같은 두 유형의 곡선을 그릴 수 있다. 

    ![desmos-graph](https://user-images.githubusercontent.com/16812446/77049717-ed801480-6a0b-11ea-8a42-37c3acaa1301.png) ![desmos-graph(1)](https://user-images.githubusercontent.com/16812446/77049675-da6d4480-6a0b-11ea-8219-a4206952234a.png)

    왼쪽 그래프와 같이 곡선이 선분 아래에 있을 때, 곡선 $y=f(x)$ 가 이 구간에서 아래로 볼록하다고 한다. 이 경우 접선의 기울기가 증가하는 것을 알 수 있다. 

    한편 오른쪽 그래프와 같이 곡선이 선분 위에 있을 때, 곡선 $y=f(x)$ 가 이 구간에서 위로 볼록하다고 한다. 이 경우 접선의 기울기가 감소하는 것을 알 수 있다. 

    그런데 이것은 그 역도 성립하여 $f'(x)$ 가 증가하면 곡선은 아래로 볼록하고 $f'(x)$ 가 감소하면 곡선은 위로 볼록하다. 그런데 이계도함수에서 $f''(x)>0$ 이면 $f'(x)$ 는 증가하고 $f''(x)<0$ 이면 $f'(x)$ 가 감소한다는 것을 이미 살펴보았다. 

    $\therefore f''(x) > 0$ 이면 곡선 $y=f(x)$ 는 이 구간에서 아래로 볼록하고, 

    $\therefore f''(x) < 0$ 이면 곡선 $y=f(x)$ 는 이 구간에서 위로 볼록하다.

- 예시 

    $y = x ^{3} - 3 x ^{2}$ 의 오목 구간과 볼록 구간을 알아보자. 

    $f(x) =x ^{3} - 3 x ^{2}$ 에서 $f'(x) = 3 x ^{2} - 6x$ 이고 $f''(x) = 6x-6=6(x-1)$

    이므로

    $$f''(1)=0$$ 

    이다. 그러므로 

    $\therefore f''(x) > 0$ 일 때 즉, $x > 1$ 인 개구간 $(1, \infty )$ 에서 아래로 볼록하고 

    $\therefore f''(x) < 0$ 일 때 즉, $x < 1$ 인 개구간 $(-\infty , 1)$ 에서 위로 볼록하다.

    실제로 다음과 같이 곡선의 그래프를 살펴보면 $x=1$ 를 기준으로 위로 볼록과 아래로 볼록이 바뀌는 것을 확인할 수 있다. 

    ![desmos-graph(2)](https://user-images.githubusercontent.com/16812446/77051638-f6261a00-6a0e-11ea-84ae-4b9472dcbf7e.png)

!!! tldr ""

    변곡점(inflection point) : 곡선 $y=f(x)$ 위의 점 $(a, f(a))$ 에 대하여 $x=a$ 의 좌우에서 곡선의 모양이 아래로 볼록에서 위로 볼록으로 바뀌거나 위로 볼록에서 아래로 볼록으로 바뀔 때, 이 점을 곡선 $y=f(x)$ 의 변곡점이라 한다.

- 예시 

    바로 위의 예시에서 살펴보았듯이 곡선 $y = x ^{3} - 3 x ^{2}$ 의 변곡점은 $x=1$ 이다.

!!! tldr ""

    변곡점의 판정 : 함수 $f(x)$ 에서 $f''(a)=0$ 이고 $x=a$ 의 좌우에서 $f''(x)$ 의 부호가 바뀌면 점 $(a, f(a))$ 는 곡선 $y=f(x)$ 의 변곡점이다.

- 증명

    점 $(a, f(a))$ 가 변곡점이면 $f''(a) = 0$ 이다. 

    하지만 그 역은 일반적으로 성립하지 않는다. 즉, $f''(a)=0$ 이어도 점 $(a,f(a))$ 가 변곡점이 아닐 수도 있다. 왜냐하면 $f''(a) = 0$ 일 지라도 $x=a$ 좌우에서 $f''(x)$ 의 부호가 바뀌지 않을 수도 있기 때문이다. 

    $\therefore$ 변곡점을 확인하기 위하여 $f''(a)=0$ 인 점 좌우에서 $f''(x)$ 의 부호가 바뀌는지 확인해야 한다.

!!! tldr ""

    점근선(asymptote) : 곡선 위의 점이 특정 방향으로 진행하면서 일정한 직선에 한없이 가까워지지만 만나지는 않을 때 그 직선을 곡선의 점근선이라 한다.

- 수직점근선(vertical asymptote) : $x$ 축에 수직인 점근선($y$축과 평행한 점근선) 이다. 

    - 함수 $f(x)$ 의 그래프에서 

        $$ \lim_{x \to a+} f(x) = \pm \infty $$

        또는 

        $$ \lim_{x \to a-} f(x) = \pm \infty $$

        이면 $f(x)$ 의 그래프는 수직점근선 $x=a$ 을 갖는다. 

    -  일반적으로 분수함수 $f(x)$ 의 분모를 $0$ 으로 만드는 값 $a$ 에 대하여 곡선 $f(x)$ 는 수직점근선 $x=a$ 을 갖는다. 

    - 예시 

        함수 $y = \frac{1}{x-1}$ 은 다음의 그래프에서 볼 수 있듯이 점근선 $x=1$ 을 갖는다. 

        ![desmos-graph(3)](https://user-images.githubusercontent.com/16812446/77053127-338ba700-6a11-11ea-8a0f-cd4fe1b076e3.png)

- 수평점근선(horizontal asymptote) : $x$축에 평행한 점근선($y$축에 수직인 점근선)이다. 

    - 함수 $f(x)$ 의 그래프에서 

        $$ \lim_{x \to \infty } f(x) = a $$

        또는 

        $$ \lim_{x \to -\infty } f(x) = a $$

        이면 $f(x)$ 의 그래프는 수평점근선 $x=a$ 을 갖는다. 

- 사선점근선(oblique asymptote) : 직선 $y=x$ 에 평행한 점근선($y$축에 수직인 점근선)이다.

!!! tldr ""

    곡선의 추적 : 함수 $f(x)$ 의 그래프 개형을 다음의 요소를 통하여 추적할 수 있다. 
    
    1. 함수의 정의역과 치역 
    
    2. 그래프의 대칭성과 주기
    
    3. 좌표축과 교점($x$절편, $y$절편)
    
    4. 함수의 증가와 감소, 극대와 극소
    
    5. 곡선의 오목과 볼록, 변곡점
    
    6. $\lim_{x \to \infty} f(x), \lim_{x \to -\infty}$, 점근선
    
    7. 불연속인 점이나 미분가능하지 않은 점

# 로피탈의 정리 

**구체화 필요**

# 테일러 급수

!!! tldr ""

    테일러 전개(Taylor's Expansion) : 어떤 함수를 이해하고자 할 때 그 함수를 직접적으로 관찰하는 것이 어려울 경우 그 함수를 다항함수로 근사시켜서 쉽게 관찰하여 이해하고자 하는 방법이다.

- 테일러 전개란 함수를 다항함수로 근사시키는 것이라 하였다. 따라서 함수을 멱급수로 표현하게 되는데 그때 표현되는 급수를 테일러 급수라고 한다. 

- 테일러 전개는 복잡한 함수를 이산적 계산만 가능한 컴퓨터에서 계산할 수 있도록 다항함수로 근사시킬 수 있다는 효용도 가지고 있다.

    - 다항함수는 덧셈, 뺄셈으로만 계산 가능하기 때문이다.

!!! tldr ""

    매끄러운 함수(smooth function) : 무한 번 미분 가능한 함수이다.

- $C ^{\infty}$ 함수로 표기하기도 한다.

!!! tldr ""

    테일러 급수(Taylor's Series) : $f(x)$ 가 무한 번 미분가능한 함수라 할 때 
    
    $$ f(x) = f(a) + \frac{f'(a)}{1!}(x-a) + \frac{f''(a)}{2!}(x-a) ^{2} + \dots + \frac{f ^{(n)}(a)}{n!}(x-a) ^{n} + \dots$$
    
    $$ = \sum_{n=0}^{\infty} \frac{f ^{(n)}(a)}{n!}(x-a) ^{n} $$
    
    라는 다항함수로 표현할 수 있고, 이를 $a$ 에서 $f(x)$ 의 테일러 급수라 한다.

- 증명 

    매끄러운 함수 $f(x)$ 를 생각하자. 그러면 미적분학의 제 $2$ 기본정리로부터 

    $$ \int_{a}^{x}f'(t)dt = f(x)-f(a) $$

    이다. 이 식을 다음과 같이 변형하자. 

    $$ \int_{a}^{x}f'(t)dt = \int_{a}^{x}(-1)(-f'(t))dt $$

    이제 부분적분을 시행하여 $-1$ 를 적분할 함수, $-f'(t)$ 를 미분할 함수로 잡자. $f(t)$ 가 무한번 미분가능하면 부분적분을 무한번 시행할 수 있으므로 다음과 같이 무한히 시행하여 보면 

    $$ \int_{a}^{x}(-1)(-f'(t))dt = f(x) - f(a) = \bigg[ -(x-t)f'(t)-\frac{(x-t)^2}{2}f''(t) - \frac{(x-t)^3}{6}f'''(t)- \dots \bigg] ^{x} _a $$

    이다. 단, $-1$ 을 계속 적분할 때 $-1$ 의 한 부정적분을 구해서 쓰면 되는데 적분변수 $t$ 와 관계없는 값 $x$ 를 상수취급하여 $x-t$ 를 부정적분으로써 구한다. 

    이제 위 식을 풀면 

    $$ f(x) - f(a) = (x-a)f'(a)+\frac{(x-a)^2}{2!}f''(t) + \frac{(x-a)^3}{3!}f'''(t)+ \dots $$

    이다. 그러므로 매끄러운 함수 $f(x)$ 에 대하여 

    $$ \therefore  f(x) = f(a) + (x-a)f'(a)+\frac{(x-a)^2}{2!}f''(t) + \frac{(x-a)^3}{3!}f'''(t)+ \dots $$

    이다.

!!! tldr ""

    매클로린 급수(Maclaurin Series) : 테일러 급수에서 $a=0$ 일 때, 즉 
    
    $$ f(x) = f(0) + \frac{f'(0)}{1!}x + \frac{f''(0)}{2!}x ^{2} + \dots + \frac{f ^{(n)}(0)}{n!}x ^{n} + \dots $$
    
    을 매클로린 급수라 한다.

- 예시 

    함수 $f(x) = \sin x$ 의 $a=0$ 에서의 테일러 급수는 

    $$ f(x) = f(0) + \frac{f'(0)}{1!}x + \frac{f''(0)}{2!}x ^{2} + \frac{f'''(0)}{3!}x ^{3} + \dots + \frac{f ^{(n)}(0)}{n!}x ^{n} + \dots $$

    이다. 그런데 사인함수의 $n$ 계도 함수는 

    $$ (\sin x)^{(n)} = \sin (x + \frac{n \pi }{2}) $$

    이다. 따라서

    $$ (\sin 0)^{(4n)} = 0, (\sin 0)^{(4n+1)} = 1, (\sin 0)^{(4n+2)} = 0, (\sin 0)^{(4n+3)} = -1 $$ 

    이다. 그러므로 이것을 테일러급수에 대입하여 

    $$ \therefore \sin x = \frac{x}{1!} - \frac{x ^{3}}{3!} + \frac{x ^{5}}{5!} - \frac{x ^{7}}{7!} + \dots = \sum_{n=1}^{\infty} \frac{(-1) ^{n}x ^{2n+1}}{(2n+1)!} $$

    를 얻는다. 

- 예시 

    코사인함수의 $n$ 계도 함수는 

    $$ (\cos x)^{(n)} = \cos (x + \frac{n \pi }{2}) $$

    이다. 따라서 

    $$ (\cos 0)^{(4n)} = 1, (\cos 0)^{(4n+1)} = 0, (\cos 0)^{(4n+2)} = -1, (\cos 0)^{(4n+3)} = 0 $$ 

    이고 위 예시와 비슷한 방식으로 

    $$ \therefore \cos x = 1 - \frac{x ^{2}}{2!} + \frac{x ^{4}}{4!} - \frac{x ^{6}}{6!} + \dots = \sum_{n=0}^{\infty} \frac{(-1) ^{n}x ^{2n}}{(2n)!} $$

    를 얻을 수 있다. 

    또한 코사인함수의 테일러 전개식은 위 예시의 사인함수의 테일러 급수를 미분함으로써 얻을 수도 있다. 즉,

    $$ (\sin x)' = (\frac{x}{1!} - \frac{x ^{3}}{3!} + \frac{x ^{5}}{5!} - \frac{x ^{7}}{7!} + \dots)' = (\sum_{n=0}^{\infty} \frac{(-1) ^{n}x ^{2n+1}}{(2n+1)!})' $$

    에서

    $$ \therefore \cos x = 1 - \frac{x ^{2}}{2!} + \frac{x ^{4}}{4!} - \frac{x ^{6}}{6!} + \dots = \sum_{n=0}^{\infty} \frac{(-1) ^{n}x ^{2n}}{(2n)!} $$

    를 얻는다. 

- 예시 

    함수 $f(x) = e^x$ 의 $a=0$ 에서의 테일러 급수는 

    $$ e ^{x} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots = \sum_{n=0}^{\infty} \frac{x^n}{n!} $$

    이다. 그런데 $x=1$ 을 대입하면 

    $$ e = 1 + 1 + \frac{1}{2!}+\frac{1}{3!}+\frac{1}{4!}+\dots = \sum_{n=0}^{\infty} \frac{1}{n!}$$

    이므로 우변을 계속 더하면 $e$ 의 근사값을 얻을 수 있다.

!!! tldr ""

    $n$차 테일러 다항식(nth Taylor Polynomial) : 함수 $f(x)$ 에 대하여 
    
    $$ T_n(x) = f(a) + \frac{f'(a)}{1!}(x-a) + \frac{f''(a)}{2!}(x-a) ^{2} + \dots + \frac{f ^{(n)}(a)}{n!}(x-a) ^{n} $$
    
    를 $a$ 에서 $f(x)$ 의 $n$ 차 테일러 다항식이라 한다.

- 테일러 급수는 원래의 함수를 근사시킨 것이기에 오차가 존재한다. 그러면 몇 번 미분해야 

    $$ f(x) = \sum_{n=0}^{\infty}\frac{f ^{(n)}(a)}{n!}(x-a) ^{n} $$

    이 성립하는가? 우변은 급수이므로 부분합의 극한으로 생각하자. 그러면 $f(x)$ 는 부분합으로 이루어진 수열의 극한이다. 여기에서 

    $$ f(x) = \lim_{n \to \infty}  \sum_{k=0}^{n}\frac{f ^{(k)}(a)}{k!}(x-a) ^{k} $$

    의 

    $$ \sum_{k=0}^{n}\frac{f ^{(k)}(a)}{k!}(x-a) ^{k} $$

    을 $n$ 차 테일러 다항식이라 한다. 이 $n$ 를 차츰차츰 늘려가면 원래의 함수에 근사하게 된다. 

- 예시 

    함수 $f(x) = e^x$ 에 대하여 $a=0$ 에 대한 $T_1(x), T_2(x), T_3(x), T_4(x)$ 을 그래프로 그려보며 어떻게 근사하는지 살펴보자. 

    ![desmos-graph(3)](https://user-images.githubusercontent.com/16812446/77070917-7e67e780-6a2e-11ea-9928-d4d298a8b0ea.png)

    위 그래프에서 빨간색이 원래 함수 $f(x)=e^x$ 이다.

    파란색이 $T_1(x) = 1+x$, 

    초록색이 $T_2(x) = 1+x+\frac{x^2}{2!}$, 

    보라색이 $T_3(x) = 1+x+\frac{x^2}{2!}+\frac{x^3}{3!}$ 이다.

    ![desmos-graph(4)](https://user-images.githubusercontent.com/16812446/77071308-25e51a00-6a2f-11ea-88eb-9032f9ec39b9.png)

    위 그래프에서 빨간색이 원래 함수 $f(x)=e^x$ 이다.

    파란색이 $T_4(x) = 1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\frac{x^4}{4!}$, 

    초록색이 $T_5(x) = 1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\frac{x^4}{4!}+\frac{x^5}{5!}$, 

    보라색이 $T_6(x) = 1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\frac{x^4}{4!}+\frac{x^5}{5!}+\frac{x^6}{6!}$ 이다.

    $n$차 테일러 다항식이 점차 원래 함수 $f(x)=e ^{x}$ 로 근사되는 것을 알 수 있다. 

# 특수 함수의 미분

!!! tldr ""

    시그모이드 함수의 도함수 : 시그모이드 함수
    
    $$ \zeta _{a} (x) = \frac{1}{1 + \exp(-ax)} $$
    
    또는 
    
    $$ \zeta (x) = \frac{1}{1 + e ^{-ax}} $$
    
    의 도함수는 
    
    $$ \{\zeta _{a} (x)\}' = a\zeta _{a} (x)\{1 - \zeta _{a} (x)\} $$
    
    이다.

- 간단하게 시그모이드 함수 $\zeta (x)$ 를 $s(x)$ 로 표현하여 

    $$ y' = s(x)(1-s(x)) $$

    로 기억해도 좋다. 

- 증명 

    $$ \zeta _{a}(x) = \frac{1}{1+e ^{-ax}} $$

    에서 

    $$ u = 1 + e ^{v}, v = -ax $$

    로 두면 $\zeta _{a}(x) = \frac{1}{u}$ 가 되므로 합성함수의 미분

    $$ \frac{d}{dx}\zeta _{a}(x) = \frac{d}{du}\zeta _{a}(x) \cdot \frac{du}{dv} \cdot \frac{dv}{dx} $$

    에서 

    $$ = \frac{d u ^{-1}}{du} \cdot \frac{d}{dv} (1 + e ^{v}) \cdot \frac{d}{dx} (-ax) $$

    $$ = (-1)u ^{-2} \cdot e ^{v} \cdot (-a) $$

    $$ = (1+ e ^{v}) ^{-2} \cdot e ^{-ax} \cdot (a) $$

    $$ = a (1+ e ^{-ax}) ^{-2} \cdot e ^{-ax}$$

    이다. 이것은 곧 

    $$ = a \frac{1}{(1+ e ^{-ax}) ^{2}} e ^{-ax}$$

    $$ = a \frac{1}{(1+ e ^{-ax}) } \frac{e ^{-ax}}{(1+ e ^{-ax})} $$

    $$ = a \frac{1}{(1+ e ^{-ax}) } \bigg \{ \frac{(1+ e ^{-ax})}{(1+ e ^{-ax})} - \frac{1}{(1+ e ^{-ax})}\bigg \}  $$

    $$ = a \frac{1}{(1+ e ^{-ax}) } \bigg \{ 1 - \frac{1}{(1+ e ^{-ax})}\bigg \}  $$

    이므로 시그모이드 함수의 도함수는 

    $$ \therefore \{\zeta _{a}(x)\}' = a \zeta _{a}(x)\{1-\zeta _{a}(x)\} $$

    이다.

!!! tldr ""

    표준 시그모이드 함수의 도함수 : 시그모이드 함수의 도함수의 정의로부터 $a=1$ 일 때 
    
    $$ \{\zeta (x)\}' = \zeta (x) \{1 - \zeta (x)\} $$
    
    이다.

- 표준 시그모이드 함수의 도함수는 

    ![](https://taewanmerepo.github.io/2017/09/sigmoid/differential_sigmoid.jpg)

    와 같이 그려진다. 최대값이 $0.25$ 이다.

!!! tldr ""

    시그모이드 함수의 이계도함수 : 시그모이드 함수
    
    $$ \zeta (x) = \frac{1}{1 + \exp(-x)} $$
    
    또는 
    
    $$ \zeta (x) = \frac{1}{1 + e ^{-x}} $$
    
    의 이계도함수는 
    
    $$ \{\zeta (x)\}'' = a ^{2} \zeta _{a}(x) \{1 - \zeta _{a}(x)\}\{1 - 2 \zeta _{a}(x)\}$$
    
    이다.

- 증명 

    시그모이드 함수의 이계도함수

    $$ \frac{d ^{2} \zeta _{a}(x)}{d x ^{2}} $$

    는 시그모이드 함수의 도함수와 곱의 미분법으로 구할 수 있다. 

    $$ \frac{d ^{2} \zeta _{a}(x)}{d x ^{2}} $$

    에서

    $$ \frac{d}{dx} \cdot \frac{d}{dx} \zeta _{a}(x) = \frac{d}{dx} \bigg [ a \zeta _{a}(x)\{1 - \zeta _{a}(x)\} \bigg ] $$

    $$ = a \{\zeta _{a}(x)\}'\{1 - \zeta _{a}(x)\} + a \zeta _{a}(x)\{1-\zeta _{a}(x)\}' $$

    $$ = a \{\zeta _{a}(x)\}'\{1 - \zeta _{a}(x)\} - a \zeta _{a}(x)\{\zeta _{a}(x)\}' $$

    이다. 이때 $a \{\zeta _{a}(x)\}$ 로 묶을 수 있으므로 

    $$ = a \{\zeta _{a}(x)\}'\{1 - 2\zeta _{a}(x)\} $$

    $$ = a \zeta _{a}(x)\{1 - \zeta _{a}(x)\} \{1 - 2\zeta _{a}(x)\} $$

    이다. 

    그러므로 시그모이드 함수의 이계도함수는 

    $$ \{\zeta (x)\}'' = a ^{2} \zeta _{a}(x) \{1 - \zeta _{a}(x)\}\{1 - 2 \zeta _{a}(x)\}$$

    이다. 

- 시그모이드 함수는 인공지능에서 활성화 함수의 일종으로 신경망의 표현력을 높일 때 사용된다.

!!! tldr ""

    ReLU 함수 : ReLU 함수는 다음과 같이 정의된다. 
    
    $$ \phi (x) = \max (0, x) = \begin{cases} x &(x>0)\text{}\\ 0 &(x \leq 0)\text{}\\ \end{cases} $$

- ReLU 함수는 인공지능에서 시그모이드 함수와 같이 활성화 함수로 사용된다.

!!! tldr ""

    ReLU 함수의 도함수 : ReLU 함수의 도함수는 
    
    $$ \phi ' (x) = \begin{cases} 1 &(x>0)\text{}\\ 0 &(x \leq 0)\text{}\\ \end{cases} $$
    
    이다.

- 인공지능에서 오차역전파를 할 때 표준 시그모이드 함수의 미분의 최대값이 $0.25$ 라서 오차 전파가 어려운 경우가 있다. 이 상황을 기울기 소실(vanishing gradient) 문제라 한다. 

    이때 ReLU 함수를 사용하면 되는데 ReLU 함수의 미분은 $0$ 또는 $1$ 의 값을 갖기 때문이다. 이는 기울기 소실 문제를 해결하는데 도움을 준다.