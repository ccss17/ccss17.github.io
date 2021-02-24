# 연속확률분포

!!! tldr ""

    연속확률변수(continuous random variable) : 어떤 구간에 속하는 모든 실수의 값을 가지는 확률변수 $X$ 이다.

- 예시 

    신생아 $100$ 명의 몸무게를 측정할 때 측정값을 $X$ 로 두면 $X$ 값은 kg 단위로 다음과 같을 수 있다. 

    $$ X = 2.54, 3.1, 4.0, 2.9, \dots $$

    이 확률변수 $X$ 는 어떤 구간 내에서 모든 실수 값을 가지므로 연속확률변수이다.

!!! tldr ""

    확률밀도함수(probability density function) : 연속확률변수 $X$ 가 구간 $[\alpha , \beta ]$ 에 속하는 모든 실수 값을 가질 때
    
    $X$ 의 확률분포를 나타내는 함수 $f(x)$ 이다.

- 대표적인 확률밀도함수가 정규분포곡선이다.

!!! tldr ""

    연속확률분포(continuous probability distribution) : 확률밀도함수를 이용해 분포를 표현할 수 있는 확률분포이다.

- 연속확률분포에는 정규분포(normal distribution), 지수분포(exponential distribution), 스튜던트 $t$ 분포(Student's t-distribution), 파레토 분포(Pareto distribution), 로지스틱 분포(logistic distribution) 등이 있다. 

    한편 이산확률분포도 무한히 반복하면 연속확률분포 중 하나로 수렴한다.

!!! tldr ""

    확률밀도함수의 성질 : 구간 $[\alpha , \beta ]$ 에 속하는 모든 실수 값을 가지는 연속확률변수 $X$ 의 확률분포를 나타내는 확률밀도함수 $f(x)$ 는 다음 성질을 만족한다. 
    
    1. $f(x) \geq 0 (\alpha \leq x \leq \beta )$
    
    2. $\displaystyle \int_{\alpha }^{\beta }f(x)dx=1$
    
    3. $\displaystyle  P(a \leq X \leq b) = \int_{a}^{b}f(x)dx$
    
    4. $\displaystyle  P(a \leq X \leq b) = P(a < X \leq b) = P(a \leq X < b) = P(a < X < b)$

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

!!! tldr ""

    연속확률변수의 평균 : 연속확률변수 $X$ 의 확률밀도함수가 $f(x) (\alpha \leq x \leq \beta )$ 일 때
    
    평균은
    
    $$ \boxed{\mu = E(X) = \int_{\alpha }^{\beta }xf(x)dx}  $$
    
    이다.

- 설명 

    이산확률변수 $X$ 의 평균에서 변량과 확률을 곱한 것의 총합

    $$ \mu = E(X) = \sum_{i=1}^{n}x_i P(X=i) = \sum_{i=1}^{n}x_ip_i=x_1p_1 + x_2p_2 + \dots + x_n p_n$$

    으로써 평균을 구했듯이 연속확률변수 $X$ 의 평균도 다음과 같이 

    폐구간 $[\alpha , \beta ]$ 에서 정의된 확률질량함수 $f(x)$ 에 대하여 변량 $x$ 와 확률 $f(x)$ 을 곱한 것의 총합으로 평균을 구한다. 즉 평균은

    $$ \therefore \mu = E(X) = \int_{\alpha }^{\beta } xf(x)dx $$

    이다. ■

!!! tldr ""

    연속확률변수의 분산 : 연속확률변수 $X$ 의 확률밀도함수가 $f(x) (\alpha \leq x \leq \beta )$ 일 때
    
    분산은
    
    $$ \boxed{V(X) = E((X - \mu ) ^{2}) = \int_{\alpha }^{\beta }(x- \mu ) ^{2} f(x)dx = \int_{\alpha }^{\beta }x ^{2}f(x)dx - \mu ^{2} = E(X ^{2}) - \{E(X)\} ^{2}}  $$
    
    이다.

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

!!! tldr ""

    연속확률변수의 표준편차 : 연속확률변수 $X$ 의 확률밀도함수가 $f(x) (\alpha \leq x \leq \beta )$ 일 때
    
    표준편차는
    
    $$ \boxed{\sigma (X) = \sqrt[]{V(X)}}  $$
    
    이다.

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

!!! tldr ""

    연속확률변수의 평균, 분산, 표준편차의 성질 : 연속확률변수 $X$ 와 두 상수 $a, b(a \neq 0)$ 에 대하여 
    
    1. $E(aX+b) = aE(X) + b$
    
    2. $V(aX+b) = a ^{2} V(X)$
    
    3. $\sigma (aX+b) = |a| \sigma (X)$

- 이산확률변수의 평균, 분산, 표준편차의 성질이 그대로 적용된다. 

- 증명 

    연속확률변수 $X$ 의 확률밀도함수가 $f(x) (\alpha \leq x \leq \beta )$ 일 때

    $$ \therefore  E(aX + b) = \int_{\alpha }^{\beta }(ax + b) f(x)dx = a \int_{\alpha }^{\beta }xf(x)dx + b \int_{\alpha }^{\beta }f(x)dx = a E(X)+b $$

    $$ \therefore  V(aX+b) = \int_{\alpha }^{\beta }\{ax+b-(a \mu +b) ^{2} \}f(x)dx dx = a ^{2} \int_{\alpha }^{\beta }(x-m) ^{2}f(x)dx = a ^{2}V(X) $$

    $$ \therefore  \sigma (aX+b) = \sqrt[]{a ^{2} {V(X)}} = |a|\sigma (X) $$

    이다. ■ 

# 정규분포

!!! tldr ""

    정규분포(normal distribution) : 연속확률변수 $X$ 의 확률밀도함수 $f(x)$ 가 각각 평균과 표준편차를 나타내는 두 상수 $\mu , \sigma (\sigma >0)$ 에 대하여 
    
    개구간 $(-\infty , \infty )$ 에서 다음과 같이 정의될 때
    
    $$ f(x) = \dfrac{1}{\sqrt[]{2 \pi } \sigma } e ^{- \frac{(x- \mu )^{2}}{2 \sigma ^{2}}} $$
    
    확률변수 $X$ 의 확률분포를 정규분포
    
    $$ N(\mu , \sigma ^{2}) $$
    
    라 한다.

- 가우스가 처음 정립했기 때문에 가우스 분포(Gaussian distribution) 이라고도 한다.

- 이것을 확률변수 $X$ 가 정규분포 $N( \mu , \sigma ^{2})$ 를 따른다고 표현한다. 

- 자연 대상을 관찰하여 얻은 상대도수를 계급의 크기를 충분히 작게하여 히스토그램으로 나타내면

    ![](https://docs.scipy.org/doc/numpy-1.15.0/_images/numpy-random-normal-1.png)

    와 같이 종 모양의 곡선과 가까워진다. 이런 곡선이 확률변수 $X$ 의 평균, 표준편차 $\mu , \sigma$ 와 개구간 $(-\infty ,\infty )$ 대하여 확률밀도함수 

    $$ f(x) = \dfrac{1}{\sqrt[]{2 \pi } \sigma } e ^{- \frac{(x- \mu )^{2}}{2 \sigma ^{2}}} $$

    로 주어질 때 $X$ 의 확률분포를 정규분포라 하는 것이다.

!!! tldr ""

    정규분포곡선 : 확률변수 $X$ 의 확률분포가 정규분포일 때 확률밀도함수 $y = f(x)$ 의 그래프를 정규분포곡선이라 한다.

- 예시 

    다음 그래프는 정규분포 $N(1, 1)$ 을 따르는 확률변수 $X$ 의 확률밀도함수 

    $$ f(x) = \dfrac{1}{\sqrt[]{2 \pi } } e ^{- \frac{x^{2}}{2 }} $$

    의 정규분포곡선이다.

    ![desmos-graph](https://user-images.githubusercontent.com/16812446/79834513-2b47d280-83e8-11ea-8108-647d17728c38.png)

!!! tldr ""

    정규분포의 성질 : 연속확률변수 $X$ 의 확률밀도함수 $f(x)$ 가 각각 평균과 표준편차를 나타내는 두 상수 $\mu , \sigma (\sigma >0)$ 에 대하여 정규분포일 때 다음 성질을 갖는다.
    
    1. 그래프의 개형이 직선 $x=m$ 에 대하여 좌우 대칭인 종 모양 곡선이다.
    
    2. $f(x)$ 의 최댓값은 $x=m$ 에서 $\dfrac{1}{\sqrt[]{2 \pi }\sigma }$ 이다. 
    
    3. $x$ 축을 점근선으로 가진다.
    
    4. $x$ 축과 정규분포곡선 사이 넓이
    
        $$ \int_{-\infty }^{\infty }f(x)dx = 1 $$ 
    
        는 $1$ 이다.
    
    5. 표준편차 $\sigma$ 가 일정할 때 평균 $\mu$ 에 따라 대칭축의 위치는 바뀌지만 곡선의 모양은 불변한다.
    
    6. 평균 $\mu$ 가 일정할 때 표준편차 $\sigma$ 가 커지면 곡선의 가운데 부분이 낮아지면서 양쪽으로 퍼지고
    
        표준편차 $\sigma$  가 작아지면 곡선 가운데 부분이 높아지면서 좁아진다.

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

!!! tldr ""

    표준정규분포(standard normal distribution) : 평균과 표준편차가 $\mu=0, \sigma = 1$ 인 정규분포를 표준정규분포
    
    $$ N(0, 1) $$
    
    라 한다.

- 자연 대상을 관찰하여 정리하면 정규분포를 따른다는 것을 우리는 이미 알고 있다. 그런데 특정 자연 대상이 어떤 범위에 속한다는 것을 구하기 위하여 확률을 구해야 한다면 

    $$ f(x) = \dfrac{1}{\sqrt[]{2 \pi } \sigma } e ^{- \frac{(x- \mu )^{2}}{2 \sigma ^{2}}} $$

    또는

    $$ f(x) = \dfrac{1}{\sqrt[]{2 \pi } \sigma } e ^{-(1/2) \{(x- \mu )/ \sigma \} ^{2} } $$

    와 같이 복잡한 정규분포곡선을 항상 적분해야만 한다. 그런데 이것은 너무 귀찮다.

    따라서 평균과 표준편차가 $\mu=0, \sigma = 1$ 인 정규분포를 표준정규분포로 제정해서 표준정규분포의 확률밀도함수 

    $$ f(x) = \dfrac{1}{\sqrt[]{2 \pi } } e ^{- \frac{x^{2}}{2} } $$

    에 대한 적분값을 미리 계산해둔다. 그러면 모든 정규분포들을 표준정규분포로 표준화시켜서 미리 계산해둔 값을 사용할 수 있다.

    실제로 수학자들이 표준정규분포에 대한 적분 결과를 이미 표로 정리해두었으니 그것이 표준정규분포표이다. 

- 표준정규분포를 따르는 확률변수를 $Z$ 또는 $z$ 로 표기한다. 

- 확률변수 $Z$ 에 대한 표준정규분포의 확률밀도함수

    $$ f(z) = \dfrac{1}{\sqrt[]{2 \pi } } e ^{- z^{2}/2 } $$

    의 그래프개형은 다음과 같다. 

  ![desmos-graph(3)](https://user-images.githubusercontent.com/16812446/79836894-ab236c00-83eb-11ea-99f7-7d0fa630b574.png)

!!! tldr ""

    표준점수(standard score) : 표준정규분포를 따르는 확률변수로써 
    
    정규분포를 만드는 개개의 경우가 표준정규분포에서 어떤 위치를 차지하는지 보여주는 무차원 수로써 
    
    원수치 $x$ 와 모집단의 표준편차 $\sigma$ 와 모집단의 평균 $\mu$ 에 대하여
    
    $$ z = \dfrac{x - \mu }{\sigma } $$
    
    이다.

- 표준값, $z$ 값($z$ value), $z$ 점수($z$ score) 로도 표기한다. 

- 통상적으로 시험성적을 평가할 때 원점수로는 시험의 난이도를 알아볼 수 없다. 

    - 예시

        어떤 학생이 영어에서는 $80$ 점을 받았고 수학에서는 $50$ 점을 받았다면 정말로 수학보다 영어를 잘한 것일까? 

        그 학교의 학생들의 영어점수와 수학점수를 확률변수 $X_1, X_2$ 로 두고 조사했는데 두 확률변수가 각각 정규분포

        $$ N(95, 5 ^{2}), N(20, 2 ^{2}) $$

        를 따랐다고 하자.

        그러면 이 학생의 영어 표준점수와 수학 표준점수는 각각 

        $$ \therefore z _{1} = \dfrac{80 - 95}{5} = -3, z _{2} = \dfrac{50 - 20}{2} = 15 $$

        이다. 이로써 수학을 영어보다 훨씬 잘했다는 것을 알 수 있다. 

    위 예시에서 알 수 있듯이 원수치의 상대적 위치를 알기 위하여 표준점수를 사용한다.

!!! tldr ""

    편차치 : 표준점수에서 음수가 나오는 것을 극복하기 위한 점수로써 표준점수 $z$ 에 대하여 
    
    $$ t = 10 z + 50 $$
    
    이다.

- $T$ 점수($T$ score) 라고도 표기한다.

!!! tldr ""

    표준정규분포표 : 표준정규분포 $N(0, 1)$ 를 따르는 확률변수 $Z$ 와 양수 $a$ 에 대한 확률 
    
    $$ P(0 \leq Z \leq a) = \int_{0}^{a} f(z)dz $$

    의 적분값들을 수학자들이 미리 정리해둔 표이다.

- 수학자들이 표준정규분포표로 정리해두었으니 우리는 그 표를 갖다 쓰면 된다. 

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

!!! tldr ""

    정규분포의 표준화(standardization) : 정규분포를 표준정규분포로 변환하는 것으로써 확률변수 $X$ 가 정규분포 $N(\mu , \sigma ^{2})$ 를 따를 때 
    
    확률변수 $X$ 를 확률변수 $Z = \dfrac{X - \mu }{\sigma }$ 로 변환하여 표준정규분포 $N(0, 1)$ 를 따르게 하는 것이다.

- 설명

    다양한 정규분포의 계산을 쉽게 할라고 표준정규분포를 만든 것을 이해하였으니

    이제 실제로 정규분포를 표준정규분포로 변환하여 사용하는 법을 알아봐야 한다. 

    임의의 값을 갖는 평균과 표준편차 $\mu , \sigma$ 에 대하여 확률변수 $X$ 의 확률분포가 정규분표

    $$ N(\mu , \sigma ^{2}) $$

    를 따른다고 하자. 이제 확률변수 $Z$ 를

    $$ Z = \dfrac{X - \mu }{\sigma } $$

    로 정의하자. 그러면 확률변수 $Z$ 의 평균과 분산은

    $$ E(Z) = E \bigg (\dfrac{X - \mu }{\sigma } \bigg ) = E \bigg (\dfrac{1}{\sigma }X - \dfrac{\mu }{\sigma } \bigg ) = \dfrac{1}{\sigma}E(X) - \dfrac{\mu }{\sigma } = \dfrac{\mu }{\sigma } - \dfrac{\mu }{\sigma } = 0 $$

    $$ Z(Z) = Z \bigg (\dfrac{X - \mu }{\sigma } \bigg ) = V \bigg (\dfrac{1}{\sigma }X - \dfrac{\mu }{\sigma } \bigg ) = \dfrac{1}{\sigma ^{2}}V(X) = \dfrac{\sigma ^{2}}{\sigma ^{2}} = 1 $$

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

        $$ P(\mu \leq X \leq \mu + \sigma ) = \int_{\mu }^{\mu + \sigma } \dfrac{1}{\sqrt[]{2 \pi } \sigma }e ^{- \frac{(x-\mu )^{2}}{2 \sigma ^{2}}}dx $$

        $$ = \int_{0 }^{\sigma } \dfrac{1}{\sqrt[]{2 \pi } \sigma }e ^{- \frac{x^{2}}{2 \sigma ^{2}}}dx $$

        에서 $\dfrac{x}{\sigma } = z$ 로 치환하면 치환적분법에 의해 

        $$ = \int_{0}^{1} \dfrac{1}{\sqrt[]{2 \pi }}e ^{-\frac{z ^{2}}{2}}dz = P(0 \leq Z \leq 1) $$

        이다. 

        즉 표준화를 해도 구간에 대한 확률밀도함수의 넓이가, 즉 확률이

        $$ \therefore  P(\mu \leq X \leq \mu + \sigma ) = P(\dfrac{\mu -\mu }{\sigma } \leq Z \leq \dfrac{\mu +\sigma - \mu }{\sigma }) = P(0 \leq Z \leq 1) $$

        와 같이 동일하다.

- 예시 

    확률변수 $X$ 가 정규분포 $N(10, 2 ^{2})$ 를 따르고 표준정규분포표가 다음과 같을 때 $P(12 \leq X \leq 14)$ 를 구하자.

    | $z$| $P(0 \leq Z \leq z)$ |
    |:---:|:---:|
    | $1.0$  | $0.3413$  |
    | $2.0$  | $0.4772$  |

    정규분포를 확률변수 $Z = \dfrac{X - \mu }{\sigma }$ 를 이용하여 표준정규분포로 표준화하면

    $$ P(12 \leq X \leq 14) = P \bigg ( \dfrac{12-10}{2} \leq \dfrac{X-10}{2} \leq \dfrac{14-10}{2} \bigg ) = P(1 \leq Z \leq 2) = P(0 \leq Z \leq 2) - P(0 \leq Z \leq 1) $$

    이므로

    $$ = 0.4772 - 0.3413 = 0.1359 $$

    이다. 따라서 

    $$ \therefore P(12 \leq X \leq 14) = 0.1359 $$

    이다. ■ 

    이로써 확률을 약 $13.5\%$ 로 생각할 수 있다.

- 표준화의 이점은 분포상태가 다른 변량끼리의 비교를 할 수 있게 해준다는 것이다.

    - 예시 

        한 학교의 학생들의 영어점수와 수학점수를 확률변수 $X_1, X_2$ 로 두고 조사했는데 두 확률변수가 각각 

        $$ N(70, 5 ^{2}), N(50, 2 ^{2}) $$

        를 따랐다.

        이때 학생 $A$ 의 영어 점수와 수학 점수가 각각 $80, 60$ 이었다. 그래서 직관적으로 학생 $A$ 가 영어를 수학보다 더 잘한다고 생각했다. 

        그러나 학생들의 영어점수와 수학점수 $X_1, X_2$ 를 표준화시켜 $N(0, 1)$ 을 따르게 하면 

        학생 $A$ 의 영어 점수와 수학 점수가 각각

        $$ Z_1 = \dfrac{80 - 70}{5} = 2, Z_2 = \dfrac{60 - 50}{2} = 5 $$

        가 된다. 이로써 학생 $A$ 는 수학 성적이 오히려 영어 성적보다 높았다는 것을 알게 되었다. 

- 예시 

    한 회사에서 신입 사원 $60$ 명을 모집하는데 $500$ 명이 지원했다고 하자. 지원자들의 입사 시험 점수의 평균이 $74$ 점이고 표준편차가 $10$ 점인 정규분포 

    $$ N(74, 10 ^{2}) $$

    를 따른다고 하자.

    이때 회사에 입사하기 위한 최저 점수를 구해보자.

    먼저 지원자의 시험 점수를 확률변수 $X$ 로 두면 이것은 정규분포 $N(74, 10 ^{2})$ 를 따르고

    입사할 확률(비율)이 $\dfrac{60}{500} = 0.12$ 이므로 입사 최저 점수를 $a$ 로 두면 확률변수 $X$ 가 $a$ 보다 클 확률(또는 $a$ 보다 큰 $X$ 들의 비율) 은

    $$ P(X \geq a) = 0.12 $$

    이다. 그러므로 정규분포를 표준화하여 새로운 확률변수 $Z = \dfrac{X - \mu }{ \sigma } = \dfrac{X - 74}{10}$ 를 만들면 이것은 표준정규분포 $N(0, 1)$ 를 따른다. 

    따라서 

    $$ P(X \geq a) = P \bigg ( \dfrac{X-74}{10} \geq \dfrac{a-74}{10} \bigg ) = P \bigg ( Z \geq \dfrac{a-74}{10} \bigg ) $$

    $$ = 0.5 - P \bigg ( 0 \leq Z \leq \dfrac{a-74}{10} \bigg ) = 0.12 $$

    에서 

    $$ P \bigg ( 0 \leq Z \leq \dfrac{a-74}{10} \bigg ) = 0.38 $$

    임을 알 수 있다. 그런데 표준정규분포표에 따라 확률값 $0.38$ 은 $z$ 값이 $1.2$ 일 때 해당한다.

    그러므로 $\dfrac{a-74}{10}=1.2$ 에서 

    $$ \therefore  a = 86 $$

    을 얻는다. ■ 

    이로써 입사 최저 점수를 $86$ 점이라고 예측할 수 있다.

!!! tldr ""

    이항분포와 정규분포의 관계 : 확률변수 $X$ 가 이항분포 $B(n, p)$ 를 따를 때 
    
    $n$ 이 충분히 크면 큰 수의 법칙에 의하여 $X$ 는 근사적으로 $q=1-p$ 에 대한 정규분포
    
    $$ N(np, npq) $$
    
    를 따른다.

- 설명

    이산확률변수 $X$ 가 이항분포 $B(n, p)$ 를 따를 때 시행 횟수 $n$ 이 조금만 커지면 확률을 계산하는 것이 쉽지 않다.

    그런데 이때 시행횟수 $n$ 을 충분히 크게하면 큰 수의 법칙에 의하여 확률변수 $X$ 가 근사적으로 평균과 분산과 표준편차가 각각 $q = 1-p$ 에 대하여

    $$\mu = np, V(X) = npq, \sigma (X)= \sqrt[]{npq}$$

    인 정규분포 

    $$ N(np,npq) $$

    를 따른다. 따라서 $n$ 이 충분히 클 때 이항분포를 정규분포에 근사시킨 후 표준정규분포로 정규화시키면 확률을 매우 쉽게 구할 수 있다.

- 예시 

    안타를 칠 확률이 $40\%$ 인 야구선수가 $150$ 번의 타석에서 $75$ 개 이상의 안타를 칠 확률을 구해보자. 

    안타수를 확률변수 $X$ 로 두면 안타를 칠 확률이 $40\% = \dfrac{2}{5}$ 이므로 $X$ 는 이항분포

    $$ B \bigg (150, \dfrac{2}{5} \bigg ) $$

    를 따른다. $150$ 의 시행이 충분히 크다고 한다면 이 확률분포를 정규분포

    $$ N(np, npq) = N \bigg (150 \times \dfrac{2}{5}, 150 \times \dfrac{2}{5} \times \dfrac{3}{5} \bigg ) = N(60, 6 ^{2}) $$

    에 근사시킬 수 있다. 

    그러므로 이 정규분포를 표준화하여 표준정규분포로 만들면 

    $$ P(X \geq 75) = P \bigg (\dfrac{X-60}{6} \geq \dfrac{75-60}{6} \bigg ) = P(Z \geq 2.5) = 0.5 - P(0 \leq Z \leq 2.5) = 0.5 - 0.4938 = 0.0062 $$

    이다. 따라서 구하고자 하는 확률은 근사적으로

    $$ \therefore  P(X \geq 75) = 0.0062 $$

    이다. ■