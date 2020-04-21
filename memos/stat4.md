# [ccss17.github.io](https://ccss17.github.io)

# 연속확률변수

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 연속확률변수(continuous random variable) : 어떤 구간에 속하는 모든 실수의 값을 가지는 확률변수 $X$ 이다. 

  </blockquote>

  - 예시 

    신생아 $100$ 명의 몸무게를 측정할 때 측정값을 $X$ 로 두면 $X$ 값은 kg 단위로 다음과 같을 수 있다. 

    $$ X = 2.54, 3.1, 4.0, 2.9, \dots $$

    이 확률변수 $X$ 는 어떤 구간 내에서 모든 실수 값을 가지므로 연속확률변수이다. 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 확률밀도함수(probability density function) : 연속확률변수 $X$ 가 구간 $[\alpha , \beta ]$ 에 속하는 모든 실수 값을 가질 때

  $X$ 의 확률분포를 나타내는 함수 $f(x)$ 이다. 

  </blockquote>

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 확률밀도함수의 성질 : 구간 $[\alpha , \beta ]$ 에 속하는 모든 실수 값을 가지는 연속확률변수 $X$ 의 확률분포를 나타내는 확률밀도함수 $f(x)$ 는 다음 성질을 만족한다. 

  1. $f(x) \geq 0 (\alpha \leq x \leq \beta )$

  2. $\displaystyle \int_{\alpha }^{\beta }f(x)dx=1$

  3. $\displaystyle  P(a \leq X \leq b) = \int_{a}^{b}f(x)dx$

  4. $\displaystyle  P(a \leq X \leq b) = P(a < X \leq b) = P(a \leq X < b) = P(a < X < b)$

  </blockquote>

  - 증명 

    "확률질량함수의 성질" 에서 이산확률변수 $X$ 의 확률질량함수가 $P(X = x_i) = p_i(i = 1, 2, 3, \dots, n)$ 일 때 다음이 성립함을 우리는 이미 알고 있다. 

    1. $0 \leq P(x) \leq 1$

    2. $\displaystyle \Sigma P(x)= 1$

    3. $\displaystyle P(x_i \leq X \leq x_j) = \sum_{k=i}^{j}P(X=x_k) = \sum_{k=i}^{j}p_k$ (단, $i, j = 1, 2, 3, \dots, n$ 이고 $i < j$)

    이 성질들은 전사건 $S$ 과 임의의 사건 $A$ 에 대한 확률의 기본 성질
    
    1. $0 \leq P(A) \leq 1$

    2. $P(S) = 1$

    3. $P(\emptyset ) = 0$

    로부터 온 것으로써 확률질량함수가 어떤 사건의 확률을 나타내는 함수이기 때문에 성립하는 것이었다.

    첫번째 성질

    1. $f(x) \geq 0 (\alpha \leq x \leq \beta )$

    또한 $0 \leq  P(x) \leq 1$ 에서 온 것으로써 폐구간 $[\alpha, \beta ]$ 위에 있는 $x$ 에 대응하는 함수값이 양수임을 보장함으로써 폐구간 $[\alpha , \beta ]$ 에 속하는 $a < b$ 인 $a, b$ 에 대하여
    
    $$ 0 \leq \int_{a}^{b} f(x) dx \leq 1 $$

    임을 보장해준다. 이것은 확률질량함수의 첫번째 성질 $0 \leq P(X) \leq 1$ 와 같다. ■ 

    두번째 성질

    2. $\displaystyle \int_{\alpha }^{\beta }f(x)dx=1$

    은 확률질량함수의 두번째 성질 $\displaystyle \Sigma P(x)= 1$ 와 같다. ■ 

    세번째 성질

    3. $\displaystyle P(a \leq X \leq b) = \int_{a}^{b}f(x)dx$

    도 확률질량함수의 세번째 성질 $i, j = 1, 2, 3, \dots, n$ 이고 $i < j$ 에 대하여 $\displaystyle P(x_i \leq X \leq x_j) = \sum_{k=i}^{j}P(X=x_k) = \sum_{k=i}^{j}p_k$ 와 같다. ■ 

    가령 $X$ 가 각각 이산확률변수이고 연속확률변수일 때 $P(1 \leq X \leq 3)$ 은 확률의 합으로써

    $$ P(1 \leq X \leq 3) = P(X=1) + P(X=2) + P(X=3)  = \sum_{i=1}^{3}p_i $$

    $$ P(1 \leq X \leq 3) = \int_{1}^{3}f(x)dx $$

    인 것이다. 

    네번째 성질 

    4. $\displaystyle  P(a \leq X \leq b) = P(a < X \leq b) = P(a \leq X < b) = P(a < X < b)$

    은 연속확률변수 $X$ 가 하나의 값 $a$ 을 가질 확률이 $F'(x) =f(x)$ 에 대하여

    $$ P(X = a) = P(a \leq X \leq a) = \int_{a}^{a}f(x)dx = F(a)-F(a) = 0 $$

    이라는 것으로부터 기인했다. ■ 
  
  - 예시 

    연속확률변수 $X$ 의 확률밀도함수 $f(x) = \dfrac{2}{9}x$ 가 폐구간 $[0, 3]$ 에서 정의되었다고 하자.

    확률변수 $X$ 가 $1 \leq X \leq 2$ 일 확률 $P(1 \leq X \leq 2)$ 을 구해보자.

    $P(1 \leq X \leq 2)$ 는

    $$ \therefore  P(1 \leq X \leq 2) = \int_{1}^{2}\dfrac{2}{9}x dx = \bigg [ \dfrac{1}{9}x ^{2} \bigg ] ^{2} _{1} = \dfrac{3}{9} = \dfrac{1}{3} $$

    이다. ■ 

    확률변수 $X$ 가 $X \geq \dfrac{5}{2}$ 일 확률 $P \bigg  (X \geq \dfrac{5}{2} \bigg  )$ 을 구해보자.

    $P \bigg  (X \geq \dfrac{5}{2} \bigg  )$ 는

    $$ \therefore P \bigg  (X \geq \dfrac{5}{2} \bigg  ) = P \bigg  (\dfrac{5}{2} \leq X \leq 3 \bigg  ) = \int_{5/2}^{3} \dfrac{2}{9}x dx = \bigg [ \dfrac{1}{9}x ^{2} \bigg ] ^{3} _{5/2} = 1 - \dfrac{25}{36} = \dfrac{11}{36} $$

    이다. ■ 

## 연속확률변수 평균, 분산, 표준편차(산포도 측정)

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 연속확률변수의 평균 : 연속확률변수 $X$ 의 확률밀도함수가 $f(x) (\alpha \leq x \leq \beta )$ 일 때

  평균은

  $$ \boxed{\mu = E(X) = \int_{\alpha }^{\beta }xf(x)dx}  $$

  이다.

  </blockquote>

  - 설명 

    이산확률변수 $X$ 의 평균에서 변량과 확률을 곱한 것의 총합

    $$ \mu = E(X) = \sum_{i=1}^{n}x_i P(X=i) = \sum_{i=1}^{n}x_ip_i=x_1p_1 + x_2p_2 + \dots + x_n p_n$$

    으로써 평균을 구했듯이 연속확률변수 $X$ 의 평균도 다음과 같이 

    폐구간 $[\alpha , \beta ]$ 에서 정의된 확률질량함수 $f(x)$ 에 대하여 변량 $x$ 와 확률 $f(x)$ 을 곱한 것의 총합으로 평균을 구한다. 즉 평균은

    $$ \therefore \mu = E(X) = \int_{\alpha }^{\beta } xf(x)dx $$

    이다. ■ 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 연속확률변수의 분산 : 연속확률변수 $X$ 의 확률밀도함수가 $f(x) (\alpha \leq x \leq \beta )$ 일 때

  분산은

  $$ \boxed{V(X) = E((X - \mu ) ^{2}) = \int_{\alpha }^{\beta }(x- \mu ) ^{2} f(x)dx = \int_{\alpha }^{\beta }x ^{2}f(x)dx - \mu ^{2} = E(X ^{2}) - \{E(X)\} ^{2}}  $$

  이다.

  </blockquote>

  - 증명 

    이산확률변수 $X$ 의 분산을 구할 때처럼 분산은 본질적으로 편차 제곱의 평균이다. 

    그러므로 폐구간 $[\alpha , \beta ]$ 에서 정의된 확률질량함수 $f(x)$ 에 대한 연속확률변수 $X$ 의 분산은 다음과 같다.

    $$ V(X) = E((X - \mu ) ^{2}) = \int_{\alpha }^{\beta }(x - \mu ) ^{2}f(x)dx $$

    $$ = \int_{\alpha }^{\beta } \{ x ^{2}f(x) - 2x \mu f(x) + \mu ^{2} f(x) \} dx $$

    $$ = \int_{\alpha }^{\beta } x ^{2}f(x) dx -2 \mu  \int_{\alpha }^{\beta } x f(x) dx + \mu ^{2}  \int_{\alpha }^{\beta } f(x) dx $$

    에서 $\displaystyle \int_{\alpha }^{\beta }f(x) dx = 1$ 이므로 

    $$ = \int_{\alpha }^{\beta } x ^{2}f(x) dx -2 \mu \cdot \mu  + \mu ^{2} \cdot 1 $$
    
    $$ = \int_{\alpha }^{\beta } x ^{2}f(x) dx - \mu ^{2} = E(X ^{2}) - \{E(X)\} ^{2} $$

    이다. 따라서 

    $$ \therefore V(X) = E(X ^{2}) - \{E(X)\} ^{2} $$

    이다. ■ 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 연속확률변수의 표준편차 : 연속확률변수 $X$ 의 확률밀도함수가 $f(x) (\alpha \leq x \leq \beta )$ 일 때

  표준편차는

  $$ \boxed{\sigma (X) = \sqrt[]{V(X)}}  $$

  이다.

  </blockquote>

  - 예시 

    연속확률변수 $X$ 의 확률밀도함수가 $\displaystyle f(x) = \dfrac{4}{9} - kx(-1 \leq x \leq 2)$ 라고 하자.

    그러면 먼저 $k$ 값은 $\displaystyle \int_{-1}^{2} f(x)dx = 1$ 이므로 

    $$ \int_{-1}^{2} \bigg ( \dfrac{4}{9} - kx \bigg ) dx = \bigg [ \dfrac{4}{9}x - \dfrac{k}{2}x ^{2} \bigg ] ^{2} _{-1} =\dfrac{4}{3}-\dfrac{3}{2}k = 1 $$

    에서 $k = \dfrac{2}{9}$ 이다. 

    이때 확률변수 $X$ 의 평균, 분산, 표준편차를 구해보자.

    $X$ 의 평균은 

    $$ \therefore  \mu = E(X) =  \int_{-1}^{2}xf(x)dx = \int_{-1}^{2}x \bigg ( \dfrac{4}{9}-\dfrac{2}{9}x \bigg )dx = \int_{-1}^{2} \bigg (\dfrac{4}{9}x - \dfrac{2}{9}x ^{2} \bigg )dx = \bigg [ \dfrac{2}{9}x ^{2} - \dfrac{2}{27}x ^{3} \bigg ] ^{2}_{-1} = \dfrac{2}{3}-\dfrac{2}{3}=0 $$

    이다. ■ 

    $X$ 의 분산은 

    $$  V(X) = E(X ^{2}) - \{E(X)\} ^{2} = \int_{-1}^{2}x ^{2}f(x)dx - 0 ^{2} $$

    $$ = \int_{-1}^{2} \bigg ( \dfrac{4}{9}x ^{2}-\dfrac{2}{9}x ^{3} \bigg ) dx = \bigg [ \dfrac{4}{27}x ^{3} - \dfrac{1}{18}x ^{4} \bigg ] ^{2} _{-1} = \dfrac{1}{2} $$

    이므로 

    $$ \therefore  V(X) = \dfrac{1}{2} $$

    이다. ■

    $X$ 의 표준편차는 

    $$ \therefore \sigma (X) = \sqrt[]{V(X)} = \sqrt[]{\dfrac{1}{2}} $$

    이다. ■ 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 연속확률변수의 평균, 분산, 표준편차의 성질 : 연속확률변수 $X$ 와 두 상수 $a, b(a \neq 0)$ 에 대하여 

  1. $E(aX+b) = aE(X) + b$

  2. $V(aX+b) = a ^{2} V(X)$

  3. $\sigma (aX+b) = |a| \sigma (X)$

  </blockquote>

  - 이산확률변수의 평균, 분산, 표준편차의 성질이 그대로 적용된다. 

  - 증명 

    연속확률변수 $X$ 의 확률밀도함수가 $f(x) (\alpha \leq x \leq \beta )$ 일 때

    $$ \therefore  E(aX + b) = \int_{\alpha }^{\beta }(ax + b) f(x)dx = a \int_{\alpha }^{\beta }xf(x)dx + b \int_{\alpha }^{\beta }f(x)dx = a E(X)+b $$

    $$ \therefore  V(aX+b) = \int_{\alpha }^{\beta }\{ax+b-(a \mu +b) ^{2} \}f(x)dx dx = a ^{2} \int_{\alpha }^{\beta }(x-m) ^{2}f(x)dx = a ^{2}V(X) $$

    $$ \therefore  \sigma (aX+b) = \sqrt[]{a ^{2} {V(X)}} = |a|\sigma (X) $$

    이다. ■ 

# 정규분포 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 정규분포(normal distribution) : 연속확률변수 $X$ 의 확률밀도함수 $f(x)$ 가 각각 평균과 표준편차를 나타내는 두 상수 $\mu , \sigma (\sigma >0)$ 에 대하여 

  개구간 $(-\infty , \infty )$ 에서 다음과 같이 정의될 때

  $$ f(x) = \dfrac{1}{\sqrt[]{2 \pi } \sigma } e ^{- \frac{(x- \mu )^{2}}{2 \sigma ^{2}}} $$

  확률변수 $X$ 의 확률분포를 정규분포

  $$ N(\mu , \sigma ^{2}) $$
  
  라 한다. 

  </blockquote>

  - 가우스가 처음 정립했기 때문에 가우스 분포(Gaussian distribution) 이라고도 한다.

  - 이것을 확률변수 $X$ 가 정규분포 $N( \mu , \sigma ^{2})$ 를 따른다고 표현한다. 

  - 자연 대상을 관찰하여 얻은 상대도수를 계급의 크기를 충분히 작게하여 히스토그램으로 나타내면

    ![](https://docs.scipy.org/doc/numpy-1.15.0/_images/numpy-random-normal-1.png)

    와 같이 종 모양의 곡선과 가까워진다. 이런 곡선이 확률변수 $X$ 의 평균, 표준편차 $\mu , \sigma$ 와 개구간 $(-\infty ,\infty )$ 대하여 확률밀도함수 

    $$ f(x) = \dfrac{1}{\sqrt[]{2 \pi } \sigma } e ^{- \frac{(x- \mu )^{2}}{2 \sigma ^{2}}} $$

    로 주어질 때 $X$ 의 확률분포를 정규분포라 하는 것이다. 
    
- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 정규분포곡선 : 확률변수 $X$ 의 확률분포가 정규분포일 때 확률밀도함수 $y = f(x)$ 의 그래프를 정규분포곡선이라 한다. 

  </blockquote>

  - 예시 

    다음 그래프는 정규분포 $N(1, 1)$ 을 따르는 확률변수 $X$ 의 확률밀도함수 

    $$ f(x) = \dfrac{1}{\sqrt[]{2 \pi } } e ^{- \frac{x^{2}}{2 }} $$

    의 정규분포곡선이다.

    ![desmos-graph](https://user-images.githubusercontent.com/16812446/79834513-2b47d280-83e8-11ea-8108-647d17728c38.png)

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 정규분포의 성질 : 연속확률변수 $X$ 의 확률밀도함수 $f(x)$ 가 각각 평균과 표준편차를 나타내는 두 상수 $\mu , \sigma (\sigma >0)$ 에 대하여 정규분포일 때 다음 성질을 갖는다.

  1. 그래프의 개형이 직선 $x=m$ 에 대하여 좌우 대칭인 종 모양 곡선이다.

  2. $f(x)$ 의 최댓값은 $x=m$ 에서 $\dfrac{1}{\sqrt[]{2 \pi }\sigma }$ 이다. 

  3. $x$ 축을 점근선으로 가진다.

  4. $x$ 축과 정규분포곡선 사이 넓이

      $$ \int_{-\infty }^{\infty }f(x)dx = 1 $$ 
      
      는 $1$ 이다.

  5. 표준편차 $\sigma$ 가 일정할 때 평균 $\mu$ 에 따라 대칭축의 위치는 바뀌지만 곡선의 모양은 불변한다.

  6. 평균 $\mu$ 가 일정할 때 표준편차 $\sigma$ 가 커지면 곡선의 가운데 부분이 낮아지면서 양쪽으로 퍼지고

      표준편차 $\sigma$  가 작아지면 곡선 가운데 부분이 높아지면서 좁아진다. 

  </blockquote>

  - 증명 

    1. 그래프의 개형이 직선 $x=m$ 에 대하여 좌우 대칭인 종 모양 곡선이다.

    은 그냥 그래프 개형에서 직관적으로 알 수 있다.

    2. $f(x)$ 의 최댓값은 $x=m$ 에서 $\dfrac{1}{\sqrt[]{2 \pi }\sigma }$ 이다. 

    도 일단은 그래프 개형에서 직관적으로 알 수 있다.

    3. $x$ 축을 점근선으로 가진다.

    은 확률밀도함수의 성질 $f(x) \geq 0$ 에서 곡선이 항상 $x$ 축 위에 있다는 것에서 도출된다. 

    4. $x$ 축과 정규분포곡선 사이 넓이는 $1$ 이다.

    은 확률밀도함수의 성질

    $$ \int_{-\infty }^{\infty }f(x)dx = 1 $$ 

    에서 도출된다.

    5. 표준편차 $\sigma$ 가 일정할 때 평균 $\mu$ 에 따라 대칭축의 위치는 바뀌지만 곡선의 모양은 불변한다.

    은 각각 정규분포 $N \bigg (0, \dfrac{1}{3} \bigg ), N \bigg (1, \dfrac{1}{3} \bigg ), N \bigg (2, \dfrac{1}{3} \bigg )$ 을 따르는 그래프

    $$ y = \dfrac{3}{\sqrt[]{2 \pi }}e ^{-9 \frac{x ^{2}}{2}} , y = \dfrac{3}{\sqrt[]{2 \pi }}e ^{-9 \frac{(x-1) ^{2}}{2}} , y = \dfrac{3}{\sqrt[]{2 \pi }}e ^{-9 \frac{(x-2) ^{2}}{2}} $$

    를 다음과 같이 그려봄으로써 알 수 있다. 순서대로 빨간선, 파란선, 초록선이다.

    ![desmos-graph(1)](https://user-images.githubusercontent.com/16812446/79835459-b83f5b80-83e9-11ea-9aeb-3714281dc266.png)

    6. 평균 $\mu$ 가 일정할 때 표준편차 $\sigma$ 가 커지면 곡선의 가운데 부분이 낮아지면서 양쪽으로 퍼지고 표준편차 $\sigma$  가 작아지면 곡선 가운데 부분이 높아지면서 좁아진다. 

    도 각각 정규분포 $N \bigg (0, \dfrac{1}{3} \bigg ), N \bigg (0, \dfrac{1}{2} \bigg ), N (0, 1)$ 을 따르는 그래프 

    $$ y = \dfrac{3}{\sqrt[]{2 \pi }}e ^{-9 \frac{x ^{2}}{2}} , y = \dfrac{2}{\sqrt[]{2 \pi }}e ^{-2 x ^{2}} , y = \dfrac{1}{\sqrt[]{2 \pi }}e ^{- \frac{x ^{2}}{2}} $$

    를 다음과 같이 그려봄으로써 알 수 있다. 순서대로 빨간선, 파란선, 초록선이다.

    ![desmos-graph(2)](https://user-images.githubusercontent.com/16812446/79835764-37349400-83ea-11ea-801e-3854af430f1d.png)

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 표준정규분포(standard normal distribution) : 평균과 표준편차가 $\mu=0, \sigma = 1$ 인 정규분포를 표준정규분포

  $$ N(0, 1) $$

  라 한다. 

  </blockquote>

  - 자연 대상을 관찰하여 정리하면 정규분포를 따른다는 것을 우리는 이미 알고 있다. 그런데 특정 자연 대상이 어떤 범위에 속한다는 것을 구하기 위하여 확률을 구해야 한다면 

    $$ f(x) = \dfrac{1}{\sqrt[]{2 \pi } \sigma } e ^{- \frac{(x- \mu )^{2}}{2 \sigma ^{2}}} $$

    와 같이 복잡한 정규분포곡선을 항상 적분해야만 한다. 그런데 이것은 너무 귀찮다.

    따라서 평균과 표준편차가 $\mu=0, \sigma = 1$ 인 정규분포를 표준정규분포로 제정해서 표준정규분포의 확률밀도함수 
    
    $$ f(x) = \dfrac{1}{\sqrt[]{2 \pi } } e ^{- \frac{x^{2}}{2} } $$

    에 대한 적분값을 미리 계산해둔다. 그러면 모든 정규분포들을 표준정규분포로 표준화시켜서 미리 계산해둔 값을 사용할 수 있다.

    - 확률변수 $Z$ 에 대한 표준정규분포의 확률밀도함수

      $$ f(z) = \dfrac{1}{\sqrt[]{2 \pi } } e ^{- \frac{z^{2}}{2} } $$

      의 그래프개형은 다음과 같다. 

      ![desmos-graph(3)](https://user-images.githubusercontent.com/16812446/79836894-ab236c00-83eb-11ea-99f7-7d0fa630b574.png)
    
  - 이때 확률변수 $Z$ 에 대한 표준정규분포에서 양수 $a$ 에 대한 확률 

    $$ P(0 \leq Z \leq a) = \int_{0}^{a} f(z)dz $$

    의 적분값들을 수학자들이 표준정규분포표로 정리해두었으니 우리는 그 표를 갖다 쓰면 된다. 

    - 예시 

      표준정규분포를 따르는 확률분포에서 확률 $\displaystyle  P(0 \leq Z \leq 1.76) = \int_{0}^{1.76}\dfrac{1}{\sqrt[]{2 \pi } } e ^{- \frac{z^{2}}{2} }$ 은 다음과 같은 표준정규분포표

      | $z$ | $0.00$ | $\dots$ |$0.06$|
      |:---:|:---:|:---:|:---:|
      | $\vdots$ | | | |
      | $1.7$ | |  | $0.4608$|

      에서 $0.4608$ 임을 알 수 있다. 
    
    - 이 표준정규분포표를 통하여 모든 경우의 구간에 대한 확률을 구할 수 있다.

      즉, $0 < a \leq b$ 에 대하여 

      $$ P(a \leq Z \leq b) = P(0 \leq Z \leq b) - P(0 \leq Z \leq a) $$

      $$ P(-a \leq Z \leq b) = P(0 \leq Z \leq b) + P(0 \leq Z \leq a) $$

      $$ P(-a \leq Z \leq a) = 2P(0 \leq Z \leq a) $$

      $$ P(Z \geq a) = 0.5 - P(0 \leq Z \leq a) $$

      $$ P(Z \leq a) = 0.5 + P(0 \leq Z \leq a) $$

      인 것을 활용하여 구간을 적절히 변환시켜 표준정규분포표를 사용하게 할 수 있다. 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 정규분포의 표준화(standardization) : 정규분포를 표준정규분포로 변환하는 것으로써 확률변수 $X$ 가 정규분포 $N(\mu , \sigma ^{2})$ 를 따를 때 

  확률변수 $X$ 를 확률변수 $Z = \dfrac{X - \mu }{\sigma }$ 로 변환하여 표준정규분포 $N(0, 1)$ 를 따르게 하는 것이다.

  </blockquote>

  - 설명

    다양한 정규분포의 계산을 쉽게 할라고 표준정규분포를 만든 것을 이해하였으니
  
    이제 실제로 정규분포를 표준정규분포로 변환하여 사용하는 법을 알아봐야 한다. 

    임의의 값을 갖는 평균과 표준편차 $\mu , \sigma$ 에 대하여 확률변수 $X$ 의 확률분포가 정규분표

    $$ N(\mu , \sigma ^{2}) $$

    를 따른다고 하자. 이제 확률변수 $Z$ 를

    $$ Z = \dfrac{X - \mu }{\sigma } $$

    로 정의하자. 그러면 확률변수 $Z$ 의 평균과 분산은

    $$ E(Z) = E(\dfrac{X - \mu }{\sigma }) = E(\dfrac{1}{\sigma }X - \dfrac{\mu }{\sigma }) = \dfrac{1}{\sigma}E(X) - \dfrac{\mu }{\sigma } = \dfrac{\mu }{\sigma } - \dfrac{\mu }{\sigma } = 0 $$

    $$ Z(Z) = Z(\dfrac{X - \mu }{\sigma }) = V(\dfrac{1}{\sigma }X - \dfrac{\mu }{\sigma }) = \dfrac{1}{\sigma ^{2}}V(X) = \dfrac{\sigma ^{2}}{\sigma ^{2}} = 1 $$

    이 된다. 따라서 확률변수 $Z$ 는 표준정규분포 

    $$ N(0, 1) $$

    를 따르게 된다. ■ 
    
  - 확률변수 $X$ 를 표준정규분포로 변환하였으니 $X$ 의 확률을 구할 때 일일이 적분할 필요 없이 확률도
  
    $$\displaystyle P(a \leq X \leq b) = P \bigg (\dfrac{a- \mu }{\sigma } \leq Z \leq \dfrac{b- \mu }{\sigma } \bigg )$$

    로 변환하여 표준정규분포표를 사용하면 된다. 

    - 증명

      $$\displaystyle P(a \leq X \leq b) = \displaystyle P(\dfrac{a - \mu }{\sigma } \leq \dfrac{X- \mu }{\sigma } \leq \dfrac{b- \mu }{\sigma }) = P \bigg (\dfrac{a- \mu }{\sigma } \leq Z \leq \dfrac{b- \mu }{\sigma } \bigg )$$
  
  - 정규분포를 표준화하여 확률을 구해도 그 값이 불변하기 때문에 이렇게 할 수 있는 것이다.

    - 증명 

      **구체화 필요**

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 이항분포와 정규분포의 관계 : 확률변수 $X$ 가 이항분포 $B(n, p)$ 를 따를 때 

  $n$ 이 충분히 크면 $X$ 는 근사적으로 $q=1-p$ 에 대한 정규분포

  $$ N(np, npq) $$

  를 따른다.

  </blockquote>