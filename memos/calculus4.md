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

# 지수함수와 로그함수의 미분 

- 지수함수의 도함수 : 지수함수 $y=a ^{x}$ 의 도함수는 다음과 같다. 

  $$ y' = a ^{x} \ln a $$

  - 증명 

    도함수의 정의에 따라 지수함수 $y=a ^{x}(a>0, a \neq 1)$ 의 도함수는 

      $$ y' = \lim_{h \to 0} \frac{f(a+h)-f(a)}{h} = \lim_{h \to 0} \frac{a ^{x+h}-a ^{x}}{h}  $$

      $$ = \lim_{h \to 0} \frac{a ^{x}(a ^{h}-1)}{h} = a ^{x} \lim_{h \to 0} \frac{a ^{h}-1}{h} = a ^{x} \ln a $$
  
  - 그러므로 밑이 $e$ 일 때, 즉 $a=e$ 일 때 지수함수 $y = e ^{x}$ 의 도함수는 

    $$ y' = e ^{x} $$

    이다. 

- 로그함수의 도함수 : 로그함수 $y = \log_{a} x$ 의 도함수는 다음과 같다. 

  $$ y' = \frac{1}{x \ln a} $$

  - 증명 

    도함수의 정의에 따라 로그함수 $y=\log_{a} x(a>0, a \neq 1)$ 의 도함수를 구해보자.

      $$ y' = \lim_{h \to 0} \frac{f(a+h)-f(a)}{h} = \lim_{h \to 0} \frac{\log_{a} (x+h)-\log_{a} x}{h} = \lim_{h \to 0} \frac{1}{h} \log_{a} \frac{x+h}{x} $$

      $$ = \lim_{h \to 0} \frac{1}{x} \circ \frac{x}{h} \log_{a} (1+\frac{h}{x}) = \frac{1}{x} \lim_{h \to 0} \log_{a} (1+\frac{h}{x}) ^{\frac{x}{h}} $$

      이때 $\frac{h}{x} = t$ 로 두면 $h \to 0 \Rightarrow t \to 0$ 이므로

      $$ = \frac{1}{x} \lim_{t \to 0} \log_{a} (1 + t)^{\frac{1}{t}} = \frac{1}{x}\log_{a} e $$

      최종적으로

      $$ \therefore y' = \frac{1}{x\ln a} $$

      이다. 