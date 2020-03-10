# [ccss17.github.io](https://ccss17.github.io)

# Calculus4 Memo

# 지수함수와 로그함수의 극한

- 지수함수 $y=a ^{x}(a>0, a \neq 1)$ 의 극한 : 다음과 같이 $x$ 가 상수에 한없이 가까워지는 경우와 무한대로 발산하는 경우로 나누어서 생각할 수 있다. 

  - $x$ 가 상수에 한없이 가까워질 때

    $$ \lim_{x \to r} a ^{x} = a ^{r} $$

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
        
        다음은 $y = \frac{1}{2} ^{x}$ 의 그래프이다. 그래프를 통해 각각의 경우의 지수함수 극한을 확인해보자. 

          ![desmos-graph(1)](https://user-images.githubusercontent.com/16812446/76310427-21737f80-6312-11ea-9c9f-7b2b231a7d09.png)

        그래프에서 

          $$ \lim_{x \to 1} \frac{1}{2}^{x} = \frac{1}{2} $$

        임을 알 수 있다. 또 그래프에서 

          $$ \lim_{x \to \infty } (\frac{1}{2})^{x} = 0 $$

        임을 알 수 있다. 또 그래프에서 

          $$ \lim_{x \to -\infty } (\frac{1}{2})^{x} = \infty $$

        임을 알 수 있다.

- 로그함수 $y= \log_{a} x(a>0, a \neq 1)$ 의 극한 : 다음과 같이 $x$ 가 $0$ 이 아닌 상수에 한없이 가까워지는 경우와 무한대로 발산하는 경우 또는 $0$ 에 한없이 가까워지는 경우로 나누어서 생각할 수 있다. 

  - $x$ 가 상수에 한없이 가까워질 때

    $$ \lim_{x \to r} \log_{a} x = \log_{a} r (단, r > 0) $$

  - $x$ 가 무한대로 발산하거나 $0$ 에 한없이 가까워지는 경우 때 $a$ 의 값의 범위를 나누어 다음과 같이 단순화된 경우로 구분한다. 

    - $a>1$ 일 때 

      $$ \lim_{x \to \infty} \log_{a} x = \infty, \lim_{x \to 0+} \log_{a} x = - \infty $$

    - $0<a<1$ 일 때 

      $$ \lim_{x \to \infty} \log_{a} x = - \infty, \lim_{x \to 0+} \log_{a} x = \infty $$

## 무리수 $e$ 와 자연로그 

- 무리수 $e$ : 무리수 $e$ 는 다음과 같이 정의한다. 

  $$ \lim_{x \to 0} (1+x) ^{\frac{1}{x}} = e $$
  
  $$ \lim_{x \to \infty} (1+\frac{1}{x}) ^{x} = e $$

- 자연로그 : 무리수 $e$ 를 밑으로 하는 로그 $\log_{e} x$ 를 $x$ 의 자연로그라 한다. 

  - 종종 자연로그 $\log_{e} x$ 를 간단히 $\ln x$ 로 나타낸다. 

- 무리수 $e$ 를 이용한 지수함수와 로그함수의 극한 : $a>0, a \neq 0$ 일 때 다음이 성립한다. 

  1. $$ \lim_{x \to 0} \frac{\ln (1+x)}{x} = 1 $$

  2. $$ \lim_{x \to 0} \frac{e ^{x}-1}{x} = 1 $$

  3. $$ \lim_{x \to 0} \frac{\log_{a} (1+x)}{x} = \frac{1}{\ln a} $$

  4. $$ \lim_{x \to 0} \frac{a ^{x}-1}{x} = \ln a $$

# 지수함수와 로그함수의 미분 
