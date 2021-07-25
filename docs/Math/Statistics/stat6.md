# 공분산과 상관계수

!!! tldr ""

    양의 관계 : 두 변수에 대하여 한 변수가 증가할 때 다른 변수가 증가하고 한 변수가 감소할 때 다른 변수도 감소하는 관계이다.



!!! tldr ""

    음의 관계 : 두 변수에 대하여 한 변수가 증가할 때 다른 변수가 감소하고 한 변수가 감소할 때 다른 변수가 증가하는 관계이다.



!!! tldr ""

    산점도(scatter plot, scatter graph, scatter chart, scattergram) : 직교 좌표계를 이용해 두 변수 간의 관계를 나타내는 방법이다.

- 예시 

    산점도는 다음과 같이 두 변수를 좌표계의 점으로 나타낸다. 

    ![](https://upload.wikimedia.org/wikipedia/ko/thumb/8/8a/Scatter_plot.png/240px-Scatter_plot.png) ![](https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Scatter_diagram_for_quality_characteristic_XXX.svg/330px-Scatter_diagram_for_quality_characteristic_XXX.svg.png)

    왼쪽 산점도는 두 변수가 양의 관계를 갖는다는 것을 알려준다. 이로써 두 변수 간의 관계서 선형적인지 비선형적인지 확인할 수 있다. 

    오른쪽 산점도의 선형성을 통해 두 변수가 음의 관계를 갖는다는 것을 알 수 있다. 

- 예시 

    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Scatter_plot.jpg/360px-Scatter_plot.jpg)

    위와 같은 공간좌표계에 산점도를 나타냄으로써 다변수에 대한 관계를 알 수 있다.

- 예시 

    <img src="https://user-images.githubusercontent.com/16812446/80305697-5e7bce80-87f9-11ea-8fd1-b19165bcdbaa.JPG" width="400" height="400"> 

    위 산점도는 선형적이지가 않아서 양의 관계인지 음의 관계인지 파악하기 힘들다.

!!! tldr ""

    공분산(covariance) : 두 가지 데이터의 직선관계가 어느 정도인지를 나타내는 통계값으로써 
    
    $n$ 개의 $2$-튜플 확률변수 
    
    $$ (X, Y) = \{(x_1, y_1),(x_2, y_2),(x_3, y_3),\dots, (x_n, y_n)\} $$
    
    가 있을 때 $X$ 의 평균 $\mu _{x}$, $Y$ 의 평균이 $\mu _{y}$ 에 대하여 
    
    $$ \text{Cov}(X, Y) = \dfrac{1}{n} \sum_{i=1}^{n}(x_i - \mu _{x})(y_i - \mu _{y}) = \dfrac{1}{n} \bigg  \{\sum_{i=1}^{n}x_iy_i - \dfrac{1}{n}\sum_{i=1}^{n}x_i \sum_{i=1}^{n}y_i \bigg \}  $$
    
    이다.

- 설명

    <img src=" https://user-images.githubusercontent.com/16812446/80305896-cbdc2f00-87fa-11ea-9953-4dc81538249e.PNG" width="200" height="200">

    <img src="https://user-images.githubusercontent.com/16812446/80305877-b23ae780-87fa-11ea-9069-67fa0ab80de0.PNG" width="200" height="200">

    위와 같은 각각 양의 관계와 음의 관계를 보여주는 산점도를 생각하자. 

    이때 변수의 직선관계가 위치에 따라서 변함이 없어야 하므로 그 직선관계를 변수 $x, y$ 의 평균 $\mu _{x}, \mu _{y}$ 를 기준으로 판단하는 것으로 한다.

    또한 양의 직선관계를 나타내는 왼쪽 그래프에서 그래프가 평균을 기준으로 데이터가 $1$ 사분면, $3$ 사분면에 많고 

    음의 직선관계를 나타내는 오른쪽 그래프에서 그래프가 평균을 기준으로 데이터가 $2$ 사분면, $4$ 사분면에 많다.

    또한 평균 $\mu _{x}, \mu _{y}$ 에서 멀어질수록 직선관계가 더욱 뚜렷해진다. 

    이런 것들을 고려해보면 변수 $x, y$ 와 평균 $\mu _{x}, \mu _{y}$ 의 차이를 곱한

    $$ (x_i - \mu _{x}) (y_i - \mu _{y}) $$

    가 직선관계를 가장 잘 나타내준다고 할 수 있다. 따라서 $i = 1, 2, 3, \dots, n$ 에 대한 데이터 $(x_i - \mu _{x}) (y_i - \mu _{y})$ 로 를 구하고 그 평균을 구하면 전체 데이터가 얼마나 직선관계를 갖는지 가늠할 수 있다.

    그러므로 이 방식으로 데이터의 직선관계를 수식으로 나타낼 수 있도록 고안된 방법이 공분산

    $$ \therefore  \text{Cov}(X, Y) = \dfrac{1}{n} \sum_{i=1}^{n}(x_i - \mu _{x})(y_i - \mu _{y}) $$

    이다. ■ 

    한편 공분산은 다음 공식으로 간편화되어 사용된다. 

    $$ \text{Cov}(X, Y) = \dfrac{1}{n} \sum_{i=1}^{n}(x_i - \mu _{x})(y_i - \mu _{y}) $$

    $$ = \dfrac{1}{n} \bigg  \{\sum_{i=1}^{n}(x_iy_i - \mu _{x}y_i+x_i \mu _{y} - \mu _{x} \mu _{y}) \bigg \}  $$

    $$ = \dfrac{1}{n} \bigg  \{\sum_{i=1}^{n}x_iy_i - \mu _{x}\sum_{i=1}^{n} y_i + \mu _{y} \sum_{i=1}^{n}x_i - \sum_{i=1}^{n} \mu _{x} \mu _{y} \bigg \}  $$

    이다. 이때 $\displaystyle \mu _{x} = \dfrac{1}{n} \sum_{i=1}^{n}x_i , \mu _{y} = \dfrac{1}{n} \sum_{i=1}^{n}y_i$ 이므로 $\displaystyle  \mu _{x}n = \sum_{i=1}^{n}x _{i}, \mu _{y}n = \sum_{i=1}^{n}y _{i}$ 임을 이용하면

    $$ = \dfrac{1}{n} \bigg  \{\sum_{i=1}^{n}x_iy_i - \mu _{x} \mu _{y}n + \mu _{y} \mu _{x}n - n \mu _{x} \mu _{y} \bigg \}  $$

    $$ = \dfrac{1}{n} \bigg  \{\sum_{i=1}^{n}x_iy_i - n \mu _{x} \mu _{y} \bigg \}  $$

    $$ = \dfrac{1}{n} \bigg  \{\sum_{i=1}^{n}x_iy_i - n \bigg ( \dfrac{1}{n}\sum_{i=1}^{n}x_i \bigg ) \bigg ( \dfrac{1}{n}\sum_{i=1}^{n}y_i \bigg ) \bigg \}  $$

    $$ = \dfrac{1}{n} \bigg  \{\sum_{i=1}^{n}x_iy_i - \dfrac{1}{n}\sum_{i=1}^{n}x_i \sum_{i=1}^{n}y_i \bigg \}  $$

    을 얻는다. 따라서

    $$ \therefore  \text{Cov}(X, Y) = \dfrac{1}{n} \bigg  \{\sum_{i=1}^{n}x_iy_i - \dfrac{1}{n}\sum_{i=1}^{n}x_i \sum_{i=1}^{n}y_i \bigg \}  $$

    이다.  ■ 

- 공분산이라는 말은 연산형태가 분산과 비슷한데 두 변수에 대한 연산이라는 것에서 착안하여 공분산이라는 이름이 붙혀졌다. 

- 공분산은 두 데이터의 상관관계를 조사해야 할 때 사용한다. 

    - 이때 단위가 전혀 다른 두 데이터에도 공분산을 구할 수 있다.

        가령 신장과 체중의 상관관계를 조사할 때에도 공분산을 구할 수 있다. 

- 공분산은 양수가 될 수도 있고 음수가 될 수도 있다. 

    - 공분산이 양수일 때 두 데이터가 양의 관계에 있다고 한다.

        이것은 두 데이터 중 어느 한쪽이 증가하거나 감소할 때 다른 데이터도 증가하거나 감소하는 관계이다. 

    - 공분산이 음수일 때 두 데이터가 음의 관계에 있다고 한다.

        이것은 두 데이터 중 어느 한쪽이 증가하거나 감소할 때 다른 데이터도 감소하거나 증가하는 관계이다. 

- 하지만 공분산의 절댓값이 양의 관계나 음의 관계의 강도를 나타내지는 않는다. 관계의 강도는 상관계수로 비교할 수 있다. 

- 예시 

    어떤 회사에서 고객들에 대한 매출량을 $6$ 개월동안 월별로 조사하여 다음 표를 만들었다. 

    |    | $1$ 월 | $2$ 월 | $3$ 월 | $4$ 월 | $5$ 월 | $6$ 월 | 합계 |
    |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
    | 고객 $A$ | $5000$ 원  |$5000$ 원  |$5000$ 원  |$5000$ 원  |$5000$ 원  |$5000$ 원  | $30000$ 원 | 
    | 고객 $B$ | $10000$ 원  |$3000$ 원  |$1000$ 원  |$1000$ 원  |$15000$ 원  |$0$ 원  |$30000$ 원 | 
    | 고객 $C$ | $3000$ 원  |$7000$ 원  |$2000$ 원  |$8000$ 원  |$4000$ 원  |$6000$ 원  |$30000$ 원 | 
    | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | 
    | 월매출 | $2500$ 만원  |$4000$ 만원  |$2000$ 만원  |$5500$ 만원  |$3500$ 만원  |$4500$ 만원  |$2$ 억 $2$ 천만원   |

    이때 고객 $A, B, C$ 의 $6$ 개월간의 매출액은 $30000$ 원으로써 평균 월 매출이 각각 $5000$ 원이다. 

    이제 고객 $B$ 의 매출과 와 월매출을 각각 확률변수 $X, Y$ 로 두고 공분산을 구해보자.

    $X$ 의 평균은 먼저 $\mu _{x} = 5000$ 이고 

    편의를 위해 월 매출 $Y$ 를 백만원 단위로 계산하여 $Y$ 의 평균은 $\mu _{y} = 22000 \div 6 = 36.666 \dots$ 이다. 

    그러면

    $$ Cov(X, Y) = \dfrac{1}{n} \sum_{i=1}^{n}(x_i - \mu _{x})(y_i - \mu _{y}) $$

    에서 

    $$ = \dfrac{1}{6}\{(10000 - 5000)(25 - 36.66 \dots) + (3000 - 5000)(40 - 36.66 \dots) + \dots\} $$

    $$ = -21667 $$

    임을 알 수 있다. ■ 

    같은 방식으로 고객 $A, B, C$ 에 대한 원 매출, 분산, 표준편차, 공분산을 구해보면 다음과 같다. 

    |    | 평균 매출 | 분산 $\sigma ^{2}$ | 표준편차 $\sigma$ | 공분산 | 
    |:---:|:---:|:---:|:---:|:---:|
    | 고객 $A$ | $5000$ 원  |$0$ 원 $^{2}$  |$0$ 원  |$0$|
    | 고객 $B$ | $5000$ 원  |$31,000,000$ 원 $^{2}$  |$5568$ 원  |$-21667$|
    | 고객 $C$ | $5000$ 원  |$4,666,667$ 원 $^{2}$  |$2160$ 원  |$24167$|
    | 평균 월 매출 | $3666. 66\dots$ 백만원  |$138.89$ 백만원 $^{2}$  | 약 $1200$ 백만원  ||

!!! tldr ""

    편차제곱의 합 표기 : 데이터 $x, y$ 와 그 각각의 평균 $\mu _{x}, \mu _{y}$ 에 대하여 편차제곱의 합을 일반적으로 $S _{ab}$ 의 형식으로 다음과 같이 표기한다.
    
    $$ S _{xx} = \sum_{i=1}^{n}(x_i - \mu _{x}  ) ^{2} = \sum_{i=1}^{n}x_i ^{2} - n \mu _{x} ^{2} $$
    
    $$ S _{yy} = \sum_{i=1}^{n}(y_i - \mu _{y}  ) ^{2} = \sum_{i=1}^{n}y_i ^{2} - n \mu _{y} ^{2} $$
    
    $$ S _{xy} = \sum_{i=1}^{n}(x_i - \mu _{x}  )(y_i - \mu _{y}  )  = \sum_{i=1}^{n}x_iy_i  - n \mu _{x}\mu _{y}  $$

- 증명 

    $$ S _{xx} = \sum_{i=1}^{n}(x_i - \mu _{x}  ) ^{2} = \sum_{i=1}^{n} (x_i ^{2} -2x_i \mu _{x} + \mu _{x} ^{2}) $$

    $$ = \sum_{i=1}^{n}x_i ^{2} - \sum_{i=1}^{n}2x_i \mu _{x} + \sum_{i=1}^{n} \mu _{x} ^{2} $$

    $$ = \sum_{i=1}^{n}x_i ^{2} - 2\mu _{x} \sum_{i=1}^{n}x_i + n \mu _{x} ^{2} $$

    이다. 이때 $\displaystyle \mu _{x} = \dfrac{1}{n} \sum_{i=1}^{n}x_i$ 이므로 $\displaystyle  \mu _{x}n = \sum_{i=1}^{n}x _{i}$ 임을 이용하면

    $$ = \sum_{i=1}^{n}x_i ^{2} - 2\mu _{x} \cdot \mu _{x}n + n \mu _{x} ^{2} = \sum_{i=1}^{n}x_i ^{2} - 2 n \mu _{x} ^{2} + n \mu _{x} ^{2} $$

    $$ = \sum_{i=1}^{n}x_i ^{2} - 2\mu _{x} \cdot \mu _{x}n + n \mu _{x} ^{2} = \sum_{i=1}^{n}x_i ^{2} - n \mu _{x} ^{2}$$

    을 얻는다. 즉, 

    $$ \therefore  S _{xx} = \sum_{i=1}^{n}(x_i - \mu _{x}  ) ^{2} = \sum_{i=1}^{n}x_i ^{2} - n \mu _{x} ^{2}$$

    이다. ■

!!! tldr ""

    상관계수(correlation coefficient) : 측정단위에 영향을 받아 선형관계의 강도를 명확히 알 수 없는 공분산의 단점을 해결하여 직선관계의 정도까지 나타내줄 수 있는 통계값으로써 
    
    확률변수 $X$ 와 $Y$ 의 분산이 양수일 때 각각의 표준편차 $\sigma _{y}, \sigma _{y}$ 와 공분산 $\sigma _{xy}$ 에 대한 무차원수
    
    $$ \rho = \dfrac{1}{n} \sum_{i=1}^{n} \bigg ( \dfrac{x_i - \mu _{x}}{\sigma _{x}} \bigg ) \bigg (\dfrac{y_i - \mu _{y}}{\sigma _{y}} \bigg ) = \dfrac{\sigma _{xy}}{\sigma _{x} \sigma _{y}} = \dfrac{S _{xy}}{\sqrt[]{S _{xx}} \sqrt[]{ S _{yy}} } $$
    
    이다.

- 설명 

    우리는 정규분포를 표준정규분포로 표준화할 때 확률변수 $X$ 에 평균 $\mu$ 를 빼고 표준편차 $\sigma$ 로 나누어 새로운 확률변수 $Z = \dfrac{X - \mu}{\sigma }$ 를 얻었다.

    이와 같은 방식으로 측정단위에 영향을 받는 공분산

    $$ \text{Cov}(X, Y) = \sigma _{xy} = \dfrac{1}{n} \sum_{i=1}^{n}(x_i - \mu _{x})(y_i - \mu _{y}) $$

    을 표준화하기 위하여 확률변수 $X$ 를 $\dfrac{X - \mu _{x}}{\sigma _{x}}$ 로 표준화하고 확률변수 $Y$ 를 $\dfrac{Y - \mu _{y}}{\sigma _{y}}$ 로 표준화할 수 있다.

    그러므로 공분산에서 데이터와 평균을 뺀 값 $x_i - \mu _{x}$ 를 표준편차 $\sigma _{x}$ 로 나누고 $y_i - \mu _{y}$ 도 표준편차 $\sigma _{y}$ 로 나누어주면

    $$ \therefore  \rho = \dfrac{1}{n} \sum_{i=1}^{n} \bigg ( \dfrac{x_i - \mu _{x}}{\sigma _{x}} \bigg ) \bigg (\dfrac{y_i - \mu _{y}}{\sigma _{y}} \bigg ) $$

    를 얻는다. ■ 

    이것을 상관계수이다. 바로 이 상관계수가 단위의 영향력을 없애버린 무차원 수로써 표준화가 된 값인 것이다.

    이때 공분산 $\displaystyle  \sigma _{xy} = \dfrac{1}{n} \sum_{i=1}^{n}(x_i - \mu _{x})(y_i - \mu _{y})$ 을 이용하여 수식을 더욱 간단히 표현하면 

    $$ \therefore  \rho = \dfrac{\sigma _{xy}}{\sigma _{x} \sigma _{y}} $$

    를 얻는다. ■ 

    그리고 표준편차 $\displaystyle \sigma _{x} = \sqrt[]{\dfrac{1}{n}\sum_{i=1}^{n}(x_i-\mu _{x}) ^{2}}, \sigma _{y}= \sqrt[]{\dfrac{1}{n}\sum_{i=1}^{n}(y_i-\mu _{y}) ^{2}}$ 를 이용하여 식을 풀고 편차 제곱의 합 표기 

    $$ S _{xx} = \sum_{i=1}^{n}(x_i - \mu _{x}  ) ^{2} , S _{yy} = \sum_{i=1}^{n}(y_i - \mu _{y}  ) ^{2} , S _{xy} = \sum_{i=1}^{n}(x_i - \mu _{x}  )(y_i - \mu _{y}  )  $$

    를 이용하면 

    $$ \therefore  \rho = \dfrac{\displaystyle \sum_{i=1}^{n}(x_i-\mu _{x})(y_i - \mu _{y})}{\sqrt[]{\displaystyle \sum_{i=1}^{n}(x_i - \mu _{x})^{2}} \sqrt[]{\displaystyle \sum_{i=1}^{n}(y_i -  \mu _{y})^{2}}} = \dfrac{S _{xy}}{\sqrt[]{S _{xx}} \sqrt[]{ S _{yy}} } $$ 

    를 얻는다. ■ 

- 상관계수 $\rho$ 는 $-1 \leq \rho \leq 1$ 의 범위 내에서 존재한다. 

    - 증명 

        코시-슈바르츠 부등식은 $\displaystyle \bigg ( \sum_{i=1}^{n}a_ib_i \bigg ) ^{2} \leq  \sum_{i=1}^{n}a_i ^{2} \sum_{i=1}^{n}b_i ^{2}$ 의 관계를 보증한다. 

        이때 상관계수의 정의

        $$ \rho = \dfrac{\displaystyle \sum_{i=1}^{n}(x_i-\mu _{x})(y_i - \mu _{y})}{\sqrt[]{\displaystyle \sum_{i=1}^{n}(x_i - \mu _{x})^{2}} \sqrt[]{\displaystyle \sum_{i=1}^{n}(y_i -  \mu _{y})^{2}}}  $$ 

        에서 $a_i = x_i - \mu _{x}, b_i = y_i - \mu _{y}$ 로 두면 

        $$ = \dfrac{\displaystyle \sum_{i=1}^{n}a_ib_i}{\sqrt[]{\displaystyle \sum_{i=1}^{n}a_i^{2}} \sqrt[]{\displaystyle \sum_{i=1}^{n}b_i^{2}}}  $$ 

        을 얻는다. 양변에 제곱을 취하면

        $$ \rho ^{2} = \dfrac{\bigg (\displaystyle \sum_{i=1}^{n}a_ib_i \bigg ) ^{2}}{\displaystyle \sum_{i=1}^{n}a_i^{2} \displaystyle \sum_{i=1}^{n}b_i^{2}} $$ 

        을 얻는데 코시-슈바르츠 부등식 $\displaystyle \bigg ( \sum_{i=1}^{n}a_ib_i \bigg ) ^{2} \leq  \sum_{i=1}^{n}a_i ^{2} \sum_{i=1}^{n}b_i ^{2}$ 에서

        $$ \rho ^{2} = \dfrac{\bigg (\displaystyle \sum_{i=1}^{n}a_ib_i \bigg ) ^{2}}{\displaystyle \sum_{i=1}^{n}a_i^{2} \displaystyle \sum_{i=1}^{n}b_i^{2}} \leq 1 $$

        임을 알 수 있다. 그러므로 $\rho ^{2} \leq 1$ 에서 

        $$ \therefore -1 \leq \rho \leq 1 $$

        이다. ■ 

    - 일반적으로 상관계수의 절댓값이 $0.7$ 보다 크면 "상관관계가 강하다" 고 말한다.

    - 상관계수가 $0$ 에 가까우면 상관관계가 약하거나 거의 없다고 볼 수 있다. 

    - 예시 

        상관계수가 $-0.9$ 라면 음의 상관관계가 강하다고 할 수 있다. 

        상관계수가 $0.8$ 라면 양의 상관관계가 강하다고 할 수 있다. 

- 상관계수로 공분산으로는 알 수 없었던 관계의 강도를 알 수 있다.

- 예시 

    어떤 회사에서 $6$ 개월간의 수입과 지출을 정리한 표가 다음과 같다고 하자. 

    |    | $1$ 월 | $2$ 월 | $3$ 월 | $4$ 월 | $5$ 월 | $6$ 월 | 평균 |
    |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
    | (수입) 월매출 | $2500$ 만원  |$4000$ 만원  |$2000$ 만원  |$5500$ 만원  |$3500$ 만원  |$4500$ 만원  |$3670$ 만원   |
    | (지출) 광고비 | $200$ 만원  |$100$ 만원  |$400$ 만원  |$300$ 만원  |$200$ 만원  |$200$ 만원  |$233$ 만원   |
    | $PV$(광고조회수) | $180$ 만회  |$270$ 만회  |$160$ 만회  |$620$ 만회  |$320$ 만회  |$390$ 만회  |$323$ 만회  |

    이때 월매출이 광고비나 $PV$(광고조회수) 와 관련이 있는지 예상이 되서 좀 더 엄밀하게 공분산을 구해보려 한다. 

    월매출을 $R$, 광고비를 $A$, $PV$ 를 $P$ 로 두고 공분산 $\text{Cov}(R,A), \text{Cov}(R,P)$ 를 계산해보자.

    먼저 각 데이터에 대한 편차를 구해놓아야 한다. 

    |    | $1$ 월 편차 | $2$ 월 편차 | $3$ 월 편차 | $4$ 월 편차 | $5$ 월 편차 | $6$ 월 편차 | 표준편차 |
    |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
    | $R$ | $-11.7$ |$3.3$ |$-16.7$ |$18.3$ |$-1.7$ |$8.3$ |$11.8$ |
    | $A$ | $-0.33$ |$-1.33$ |$1.67$ |$0.67$ |$-0.33$ |$-0.33$ |$0.943$ |
    | $P$ | $-143$ |$-53$ |$-163$ |$297$ |$-3$ |$67$ |$154$ |

    이를 바탕으로 공분산을 구해보면 

    $$ \text{Cov}(R,A) = \dfrac{1}{6}\{(-11.7) \times (-0.33) + 3.3 \times (-1.33) + \dots + 8.3 \times (-0.33)\} = -3.056 $$

    $$ \text{Cov}(R,P) = \dfrac{1}{6}\{(-11.7) \times (-143) + 3.3 \times (-53) + \dots + 8.3 \times 67\} = 1703 $$

    이다. 따라서 월매출과 광고비는 음의 관계이고 월매출과 광고조회수는 양의 관계임을 알 수 있다.

    그런데 이 상관관계가 얼마나 강한지는 알 수 없다. 왜냐하면 광고조회수의 데이터의 값이 단지 크기 때문에 $1703$ 이라는 큰 수가 계산된 것이기 때문이다. 

    따라서 이것으로 월매출과 광고비의 공분산 $-3.056$ 보다 상관관계의 강도가 크다고 말할 수 없다.

    그렇다면 월매출과 광고비의 상관계수 $\rho _{RA}$ 와 월매출과 광고조회수의 상관계수 $\rho _{RP}$ 를 구해보면

    $$ \therefore  \rho _{RA} = \dfrac{\text{Cov}(R,A)}{\sigma _{R} \sigma _{A}} = \dfrac{-3.056}{11.8 \times 0.943} = -0.2746 $$

    $$ \therefore  \rho _{RP} = \dfrac{\text{Cov}(R,P)}{\sigma _{R} \sigma _{P}} = \dfrac{1703}{11.8 \times 154} = 0.9372 $$

    이다. ■ 

    이에 따라 월매출과 광고조회수 $PV$ 가 강한 양의 상관관계에 있다고 생각할 수 있다. 

    또 월매출과 광고비는 약한 음의 상관관계를 갖는다고 볼 수 있다.

!!! tldr ""

    표본공분산(sample covariance) : 추출된 표본의 두 가지 데이터의 직선관계가 어느 정도인지를 나타내는 통계값으로써 
    
    $n$ 개의 $2$-튜플 확률변수 
    
    $$ (X, Y) = \{(x_1, y_1),(x_2, y_2),(x_3, y_3),\dots, (x_n, y_n)\} $$
    
    가 있을 때 $X$ 의 평균 $\mu _{x}$, $Y$ 의 평균이 $\mu _{y}$ 에 대하여 
    
    $$ \text{Cov}(X, Y) = \dfrac{1}{n-1} \sum_{i=1}^{n}(x_i - \mu _{x})(y_i - \mu _{y}) = \dfrac{1}{n-1} \bigg  \{\sum_{i=1}^{n}x_iy_i - \dfrac{1}{n}\sum_{i=1}^{n}x_i \sum_{i=1}^{n}y_i \bigg \}  $$
    
    이다.

- 공분산이 $n$ 으로 나눈 반면 표본공분산은 $n-1$ 로 나누었다는 것에 주의하자. 

- 증명 

    표본공분산은 다음 공식으로 간편화되어 사용된다. 

    $$ \text{Cov}(X, Y) = \dfrac{1}{n-1} \sum_{i=1}^{n}(x_i - \mu _{x})(y_i - \mu _{y}) $$

    $$ = \dfrac{1}{n-1} \bigg  \{\sum_{i=1}^{n}(x_iy_i - \mu _{x}y_i+x_i \mu _{y} - \mu _{x} \mu _{y}) \bigg \}  $$

    $$ = \dfrac{1}{n-1} \bigg  \{\sum_{i=1}^{n}x_iy_i - \mu _{x}\sum_{i=1}^{n} y_i + \mu _{y} \sum_{i=1}^{n}x_i - \sum_{i=1}^{n} \mu _{x} \mu _{y} \bigg \}  $$

    이다. 이때 $\displaystyle \mu _{x} = \dfrac{1}{n} \sum_{i=1}^{n}x_i , \mu _{y} = \dfrac{1}{n} \sum_{i=1}^{n}y_i$ 이므로 $\displaystyle  \mu _{x}n = \sum_{i=1}^{n}x _{i}, \mu _{y}n = \sum_{i=1}^{n}y _{i}$ 임을 이용하면

    $$ = \dfrac{1}{n-1} \bigg  \{\sum_{i=1}^{n}x_iy_i - \mu _{x} \mu _{y}n + \mu _{y} \mu _{x}n - n \mu _{x} \mu _{y} \bigg \}  $$

    $$ = \dfrac{1}{n-1} \bigg  \{\sum_{i=1}^{n}x_iy_i - n \mu _{x} \mu _{y} \bigg \}  $$

    $$ = \dfrac{1}{n-1} \bigg  \{\sum_{i=1}^{n}x_iy_i - n \bigg ( \dfrac{1}{n}\sum_{i=1}^{n}x_i \bigg ) \bigg ( \dfrac{1}{n}\sum_{i=1}^{n}y_i \bigg ) \bigg \}  $$

    $$ = \dfrac{1}{n-1} \bigg  \{\sum_{i=1}^{n}x_iy_i - \dfrac{1}{n}\sum_{i=1}^{n}x_i \sum_{i=1}^{n}y_i \bigg \}  $$

    을 얻는다. 따라서

    $$ \therefore  \text{Cov}(X, Y) = \dfrac{1}{n-1} \bigg  \{\sum_{i=1}^{n}x_iy_i - \dfrac{1}{n}\sum_{i=1}^{n}x_i \sum_{i=1}^{n}y_i \bigg \}  $$

    이다.  ■ 

- 예시 

    올림픽 육상 $100$ 미터 남자 우승기록에서 $1900$ 년부터 $2016$ 년까지의 표본은 다음과 같다. 

    | 번호 | $X$(연도) | $Y$(기록) | $XY$ |
    |:---:|:---:|:---:|:---:|
    | $1$ | $1900$ | $11$ | $20900$ |
    | $2$ | $1904$ | $11$ | $20944$ |
    | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ |
    | $27$ | $2016$ | $9.81$ | $19776.96$ |
    | 합계 | $52940$ | $276.76$ | $542291.2$ |

    연도와 기록에 대한 표본공분산은

    $$ \text{Cov}(X, Y) = \dfrac{1}{n-1} \bigg  \{\sum_{i=1}^{n}x_iy_i - \dfrac{1}{n}\sum_{i=1}^{n}x_i \sum_{i=1}^{n}y_i \bigg \}  $$

    에서

    $$ \therefore  \text{Cov}(X,Y) = \dfrac{1}{27 - 1}\bigg \{ 542291.2 - \dfrac{1}{27}(52940)(276.76) \bigg \} = -13.98 $$

    이다. ■ 

    즉 연도와 기록은 음의 관계를 갖고 연도가 높아질수록 기록이 줄어든다고 볼 수 있다. 

    또 한편 공분산은 측정 데이터의 단위에 영향을 받으므로 $-13.98$ 이 선형관계의 강도를 보여줄 수 있는 것은 아니다. 실제로 기록을 나타내는 확률변수 $Y$ 의 단위를 초에서 분으로 바꾸면 데이터들에 $\times \dfrac{1}{60}$ 연산을 해주어야 하는데 이때 

    $$ -13.98 \to -0.233 $$

    으로 공분산이 변한다. 따라서 공분산의 절댓값 크기에서 의미를 찾으려 들면 안된다!

!!! tldr ""

    표본상관계수(sample correlation coefficient) : 측정단위에 영향을 받아 선형관계의 강도를 명확히 알 수 없는 공분산의 단점을 해결하여 직선관계의 정도까지 나타내줄 수 있는 추출된 표본의 통계값으로써 
    
    확률변수 $X$ 와 $Y$ 의 분산이 양수일 때 각각의 표본표준편차 $\sigma _{x}, \sigma _{y}$ 와 표본공분산 $\sigma _{xy}$ 에 대한 무차원수
    
    $$ \rho = \dfrac{1}{n-1} \sum_{i=1}^{n} \bigg ( \dfrac{x_i - \mu _{x}}{\sigma _{x}} \bigg ) \bigg (\dfrac{y_i - \mu _{y}}{\sigma _{y}} \bigg ) = \dfrac{\sigma _{xy}}{\sigma _{x} \sigma _{y}} = \dfrac{S _{xy}}{\sqrt[]{S _{xx}} \sqrt[]{ S _{yy}} } $$
    
    이다.

- 표본상관계수도 마찬가지로 $-1$ 에서서 $1$ 의 값을 갖는다. 

    - $0$ 에 가까우면 직선상관관계가 없다고 볼 수 있다. 

- 그러나 두 변수가 직선관계가 있다고 해서 잠복변수의 존재에 의하여 인과관계를 갖는다고 할 수는 없다. 

    - 예시 

        휴대전화 보급률과 기대수명에 대한 선형상관관계는 매우 높다.

        그렇다면 수명을 늘리기 위해 휴대전화 보급을 늘려야 하는가? 이 두 변수는 인과관계가 없기 때문에 올바르지 않는 결론이다.

!!! tldr ""

    가능도(likelihood) :

**구체화 필요**

!!! tldr ""

    최대가능도추정(maximum likelihood estimation) :

**구체화 필요**