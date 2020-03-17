# [ccss17.github.io](https://ccss17.github.io)

# Calculus4 Memo

# 지수함수와 로그함수의 극한

- 지수함수 $y=a ^{x}(a>0, a \neq 1)$ 의 극한 : 다음과 같이 $x$ 가 상수에 한없이 가까워지는 경우와 무한대로 발산하는 경우로 나누어서 생각할 수 있다. 

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

- 로그함수 $y= \log_{a} x(a>0, a \neq 1)$ 의 극한 : 다음과 같이 $x$ 가 $0$ 이 아닌 상수에 한없이 가까워지는 경우와 무한대로 발산하는 경우 또는 $0$ 에 한없이 가까워지는 경우로 나누어서 생각할 수 있다. 

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

- 무리수 $e$ : 무리수 $e$ 는 다음과 같이 정의한다. 

  $$ \lim_{x \to 0} (1+x) ^{\frac{1}{x}} = e $$

  - 위의 정의에서 $\frac{1}{x} = t$ 로 놓으면 $x \to 0+ \Rightarrow t \to \infty$ 이다. 따라서
  
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

- 자연로그 : 무리수 $e$ 를 밑으로 하는 로그 $\log_{e} x$ 를 $x$ 의 자연로그라 한다. 

  - 자연로그 $\log_{e} x$ 를 간단히 $\ln x$ 로 나타낸다. 

  - 자연이라는 수식어는 자연로그의 도함수를 도출하는 과정에서 밑이 동시에 자연스럽게 정의된다는 점이나, 자연로그의 밑을 지수의 밑으로 하는 지수함수의 미분 등에서 아주 깔끔한 결과가 얻어지는 데서 유래했다. (나무위키)

  - 다음과 같은 관계가 성립한다. 

    - $\ln e = \log_{e} e = 1$

    - $\ln 1 = \log_{e} 1 = 0$

- 무리수 $e$ 를 이용한 지수함수와 로그함수의 극한 : $a>0, a \neq 0$ 일 때 다음이 성립한다. 

  1. $$ \lim_{x \to 0} \frac{\log_{a} (1+x)}{x} = \frac{1}{\ln a} $$

      - 증명 

        $$ \lim_{x \to 0} \frac{\log_{a} (1+x)}{x} = \lim_{x \to 0} \log_{a} (1+x) ^{\frac{1}{x}} = \log_{a} e = \frac{1}{\ln a} $$

      - 그러므로 $a = e$ 일 때 

        $$ \lim_{x \to 0} \frac{\ln (1+x)}{x} = 1 $$

        이다. 

  2. $$ \lim_{x \to 0} \frac{a ^{x}-1}{x} = \ln a $$

      - 증명 

        $a ^{x} -1 = t$ 로 두면 $x \to 0 \Rightarrow t \to 0$ 이고 $a ^{x} = 1+t$ 에서 

          $$ \therefore x = \log_{a} (1+t) $$
        
        이다. 따라서 

          $$ \lim_{x \to 0} \frac{a ^{x}-1}{x} = \lim_{t \to 0} \frac{t}{\log_{a} (1+t)} = \lim_{t \to 0} \frac{1}{\frac{\log_{a} (1+t)}{t}} $$

          $$ = \lim_{t \to 0} \frac{1}{\log_{a} (1+t) ^{\frac{1}{t}}} = \frac{1}{\log_{a} e} = \ln a $$

      - 그러므로 $a = e$ 일 때 

        $$ \lim_{x \to 0} \frac{e ^{x}-1}{x} = e $$

        이다. 

## 지수함수와 로그함수의 미분 

- 지수함수 $y=a ^{x}$ 의 도함수 : 지수함수 $y=a ^{x}$ 의 도함수는 

  $$ (a ^{x})' = a ^{x} \ln a $$

  이다.

  - 증명 

    도함수의 정의에 따라 지수함수 $y=a ^{x}(a>0, a \neq 1)$ 의 도함수는 

      $$ y' = \lim_{h \to 0} \frac{f(a+h)-f(a)}{h} = \lim_{h \to 0} \frac{a ^{x+h}-a ^{x}}{h}  $$

      $$ = \lim_{h \to 0} \frac{a ^{x}(a ^{h}-1)}{h} = a ^{x} \lim_{h \to 0} \frac{a ^{h}-1}{h} = a ^{x} \ln a $$
    
    이다. 그러므로 

      $$
      (a ^{x})' = a ^{x}\ln a
      $$

- $y = e ^{x}$ 의 도함수 : 지수함수 도함수의 정의에 따라 밑이 $e$ 일 때, 즉 $a=e$ 일 때 지수함수 $y = e ^{x}$ 의 도함수는 

    $$ (e ^{x})' = e ^{x} $$

    이다. 

- 로그함수 $y = \log_{a} x$ 의 도함수 : 로그함수 $y = \log_{a} x(a>0, a \neq 1)$ 의 도함수는 

  $$ (\log_{a} x)' = \frac{1}{x \ln a} $$

  이다.

  - 증명 

    도함수의 정의에 따라 로그함수 $y=\log_{a} x(a>0, a \neq 1)$ 의 도함수를 구해보자.

      $$ y' = \lim_{h \to 0} \frac{f(a+h)-f(a)}{h} = \lim_{h \to 0} \frac{\log_{a} (x+h)-\log_{a} x}{h} = \lim_{h \to 0} \frac{1}{h} \log_{a} \frac{x+h}{x} $$

      $$ = \lim_{h \to 0} \frac{1}{x} \circ \frac{x}{h} \log_{a} (1+\frac{h}{x}) = \frac{1}{x} \lim_{h \to 0} \log_{a} (1+\frac{h}{x}) ^{\frac{x}{h}} $$

      이때 $\frac{h}{x} = t$ 로 두면 $h \to 0 \Rightarrow t \to 0$ 이므로

      $$ = \frac{1}{x} \lim_{t \to 0} \log_{a} (1 + t)^{\frac{1}{t}} = \frac{1}{x}\log_{a} e $$

      최종적으로

      $$ \therefore (\log_{a} x)' = \frac{1}{x\ln a} $$

      이다. 

- 자연로그함수 $y = \ln x$ 의 도함수 : 로그함수 도함수의 정의에 따라 밑이 $e$ 일 때, 즉 $a=e$ 일 때 자연로그함수 $y = \ln x$ 의 도함수는 

  $$ (\ln x)' = \frac{1}{x} $$

  이다. 

## 정의역이 확장된 로그함수의 미분

지금까지의 로그함수의 미분은 정의역이 양의 실수 집합에서만 성립한다. 그러나 이제 정의역을 확장해보자. 

- 로그함수 $y = \ln |x|$ 의 도함수 : 로그함수 $y = \ln |x|$ 의 도함수는 

  $$ (\ln |x|)' = \frac{1}{x} $$

  이다. 

  - 증명 

    $x$ 의 범위를 축소시켜 상황을 단순화시켜보자. 

    $x>0$ 일 때 $y = \ln |x| = \ln x$ 이므로 $y'=\frac{1}{x}$ 이다. 

    $x<0$ 일 때 $y = \ln |x| = \ln (-x)$ 이므로 $y'=\frac{(-x)'}{-x}=\frac{-1}{-x}=\frac{1}{x}$ 이다. 

    그러므로 단순화된 상황을 다시 일반화하면

    $$ \therefore (\ln |x|)' = \frac{1}{x} $$

    이다. 

- 로그함수 $y = \log_{a} |x|$ 의 도함수 : 로그함수 $y = \log_{a} |x|$ 의 도함수는 

  $$ (\log_{a} |x|)' = \frac{1}{x \ln a} $$

  이다. 

  - 증명 

    로그함수 $y = \ln |x|$ 의 도함수를 이용하여

    $$y' = (\log_{a} |x|)' = (\frac{\ln |x|}{\ln a})' = \frac{(\ln |x|)'}{\ln a} = \frac{1}{x} \circ \frac{1}{\ln a} = \frac{1}{x \ln a}$$

    이다. 그러므로

    $$ \therefore (\log_{a} |x|) = \frac{1}{x \ln a} $$
  
  - 그런데 정의역이 양의 실수로 국한된 로그함수의 도함수와 절대값 연산으로 정의역이 확장된 로그함수의 도함수가 서로 같으므로 로그함수의 도함수를 구할 때 절대값을 무시할 수 있다. 

# 삼각함수의 극한

- 삼각함수의 극한 : 임의의 실수 $a$ 에 대하여 삼각함수의 극한은 다음과 같다. 

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

- 함수 $\frac{\sin x}{x}, \frac{\tan x}{x}$ 의 극한 : $x$ 가 라디안일 때 다음이 성립한다. 

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

      $$ \lim_{x \to 0} \frac{\tan x}{x} = \lim_{x \to 0} \frac{\sin x}{x \cos x} = \lim_{x \to 0} (\frac{\sin x}{x} \circ \frac{1}{\cos x}) $$

      $$ = \lim_{x \to 0} \frac{\sin x}{x} \circ \lim_{x \to 0} \frac{1}{\cos x} = 1 \circ 1 = 1 $$

      그러므로 

      $$ \therefore \lim_{x \to 0} \tan x = 1 $$

      이다. 다음 그래프 $y=\frac{\tan x}{x}$ 에서도 $x \to 0 \Rightarrow \tan x \to 1$ 임을 확인할 수 있다. 물론 다음 그래프도 $x=0$ 에서 함수값은 정의되어있지 않다. 

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

- 함수 $y = \sin x$ 의 도함수 : $y' = \cos x$ 이다. 

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

- 함수 $y = \cos x$ 의 도함수 : $y' = -\sin x$ 이다. 

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

- 함수 $y = \tan x$ 의 도함수 : $y' = \sec ^{2} x$ 이다. 

  - 증명 

    $\tan x = \frac{\sin x}{\cos x}$ 이므로 몫의 미분을 사용하면 

      $$ (\tan x)' = (\frac{\sin x}{\cos x})' = \frac{(\sin x)'\cos x - \sin x(\cos x)'}{\cos ^{2}x} $$

- 함수 $y = \sec x$ 의 도함수 : $y' = \sec x \tan x$ 이다. 

  - 증명 

    $\sec x = \frac{1}{\cos x}$ 이므로 몫의 미분을 사용하면 

      $$ (\sec x)' = (\frac{1}{\cos x})' = -\frac{(\cos x)'}{\cos ^{2}x}= \frac{\sin x}{\cos ^{2}x} = \frac{1}{\cos x} \circ \frac{\sin x}{\cos x} $$
    
    이다. 따라서 최종적으로 

      $$ \therefore  (\sec x)' = \sec x \tan x $$
    
    이다.

- 함수 $y = \csc x$ 의 도함수 : $y' = -\csc x \cot x$ 이다. 

  - 증명 

    $\csc x = \frac{1}{\sin x}$ 이므로 몫의 미분을 사용하면 

      $$ (\csc x)' = (\frac{1}{\sin x})' = -\frac{(\sin x)'}{\sin ^{2}x}= -\frac{\cos x}{\sin ^{2}x} = -\frac{1}{\sin x} \circ \frac{\cos x}{\sin x} $$
    
    이다. 따라서 최종적으로 

      $$ \therefore  (\csc x)' = - \csc x \cot x $$
    
    이다.

- 함수 $y = \cot x$ 의 도함수 : $y' = -\csc ^{2} x$ 이다. 

  - 증명 

    $\cot x = \frac{\cos x }{\sin x}$ 이므로 분수함수 미분을 사용하면 

      $$ (\cot x)' = (\frac{\cos x}{\sin x})' = \frac{(\cos x)'\sin x - \cos x(\sin x)'}{\sin ^{2}x} = \frac{-\sin ^{2} x - \cos ^{2} x}{\sin ^{2}x} = -\frac{1}{\sin ^{2}x} $$
    
    이다. 따라서 최종적으로 

      $$ \therefore  (\cot x)' = - \csc ^{2}x $$
    
    이다.

## 복잡한 함수의 도함수 

- 로그함수 $y = \ln |f(x)|$ 의 도함수 : 함수 $f(x)$ 가 미분가능하고 $f(x) \neq 0$ 일 때 로그함수 $y = \ln |f(x)|$ 의 도함수는

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

- 로그함수 $y = \log_{a} |f(x)|(a>0, a \neq 1)$ 의 도함수 : 함수 $f(x)$ 가 미분가능하고 $f(x) \neq 0$ 일 때 로그함수 $y = \ln |f(x)|$ 의 도함수는

  $$\{\ln |f(x)|\}' = \frac{f'(x)}{f(x)\ln a}$$ 
  
  이다.

  - 증명 

    로그함수 $y = \ln |f(x)|$ 의 도함수를 이용하여 로그함수 $y = \log_{a} |f(x)|(a>0, a \neq 1)$ 의 도함수를 구해보자. 

      $$ y' = (\log_{a} |f(x)|)' = (\frac{\ln |f(x)|}{\ln a})' = \frac{(\ln |f(x)|)'}{\ln a} = \frac{f'(x)}{f(x)} \circ \frac{1}{\ln a} = \frac{f'(x)}{f(x)\ln a} $$
    
    그러므로 

      $$ \therefore  (\log_{a} |f(x)|)' = \frac{f'(x)}{f(x)\ln a} $$

    이다.

- 로그미분법 : 밑과 지수에 변수가 포함되어 있는 함수나 복잡한 분수함수는 다음과 같이 미분하면 편할 때가 있다. 

  1. $y=f(x)$ 양 변에 절대값을 취한다.

      $$ |y| = |f(x)| $$
  
  2. 양변에 자연로그를 취한다. 

      $$ \ln |y| = \ln |f(x)| $$
  
  3. 양변을 $x$ 에 대하여 미분한다. 

      $$ \frac{y'}{y} = \frac{f'(x)}{f(x)} $$
  
  4. $y'$ 에 대하여 정리한다. 

      $$ y' = y \circ \frac{f'(x)}{f(x)} $$
  
  - 예시 

    함수 $f(x) = x ^{\sin x}(x>0)$ 의 도함수를 구해보자.

    함수 $f(x)$ 의 함수값은 항상 양수이니 양변에 자연로그를 취하면 

      $$ y = x ^{\sin x} $$

    에서 

      $$ \ln y = \ln x ^{\sin x} $$

    이다. 이때 양변을 $x$ 에 대하여 미분하면 

      $$ \frac{y'}{y} = (\sin x)'\ln x + \sin x(\ln x)' = \cos x \circ \ln x + \sin x \circ \frac{1}{x} $$

      $$ y' = y(\cos x \circ \ln x + \sin x \circ \frac{1}{x}) $$

    에서 

    $$ \therefore y' = x ^{\sin x}(\cos x \circ \ln x + \frac{\sin x}{x}) $$

    이다. 

- 함수 $y = x ^{n}$ 의 도함수 : $n$ 이 실수일 때, $y' = f'(x) = nx ^{n-1}$ 

  - 증명 

    우리는 앞서 정수 $n$ 에 대하여 $n$차 단항 함수 $y = x ^{n}$ 의 도함수가 $y' = n x ^{n-1}$ 임을 알아보았었다. 이제 로그미분법으로 $n$ 이 실수일 때 함수 $y= x ^{n}$ 의 도함수를 구해보자.

    $y = x ^{n}$ 의 양변의 절대값에 자연로그를 취하면 

    $$ \ln |y| = \ln |x ^{n}| $$

    $$ \ln |y| = n\ln |x| $$

    이다. 이때 양변을 $x$ 에 대하여 미분하면 

    $$ \frac{y'}{y} = n \circ \frac{1}{x} $$

    $$ y' = y \circ n \circ \frac{1}{x} $$

    $$ y' = x ^{n} \circ n \circ \frac{1}{x} $$

    에서 

    $$ \therefore y' = n x ^{n-1} $$

    이다. 
  
  - 예시 

    $y = x ^{\sqrt[]{3}}$ 의 도함수는 $y' = \sqrt[]{3} x ^{\sqrt[]{3}-1}$ 이다. 

  - 예시 

    $y = x ^e$ 의 도함수는 $y'=ex^{e-1}$ 이다.

## 매개변수로 나타낸 함수의 미분 

- 매개변수(parameter)로 나타낸 함수 : 두 변수 $x, y$ 사이의 관계를 변수 $t$ 를 매개로 

    $$ x = f(t), y = g(t) $$
  
  꼴로 나타낼 때, 변수 $t$ 를 매개변수라 하고 위 식을 매개변수로 나타낸 함수라 한다. 

- 매개변수로 나타낸 함수의 미분법 : 두 함수 $x=f(t),y=g(t)$ 에서 $f(t),g(t)$ 가 각각 $t$ 에 대하여 미분가능하고 $f'(t) \neq 0$ 일 때 

  $$ \frac{dy}{dx} = \frac{\frac{dy}{dt}}{\frac{dx}{dt}} = \frac{g'(t)}{f'(t)} $$

  - 증명 

    두 함수 $x=f(t), y=g(t)$ 가 각각 $t$ 에 대하여 미분가능하고 $f'(t) \neq 0$ 라고하자. 그러면 $x = f(t)$ 의 역함수가 존재하고 $t$ 는 $x$ 에 대한 함수이므로 $y=g(t)$ 도 $x$ 에 대한 함수로 볼 수 있다. 또 매개변수 $t$ 의 증분 $\Delta t$ 에 대한 $x$ 의 증분을 $\Delta x$, $y$ 의 증분을 $\Delta y$ 라 하자.

    그러면 $x$ 가 $t$ 에 대해서 미분가능하기 때문에 
    
    $$ \lim_{\Delta x \to 0}  \frac{\Delta t}{\Delta x} $$

    의 값이 존재한다. 그런데 분모가 $0$ 에 한없이 다가가는데도 그 값이 존재하므로 분자도 $0$ 에 다가간다. 따라서

    $$ \Delta x \to 0 \Rightarrow \Delta t \to 0 $$

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
