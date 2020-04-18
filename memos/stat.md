# [ccss17.github.io](https://ccss17.github.io)

# 통계

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 통계학(statistics) : 산술적 방법으로 다량의 데이터를 관찰하고 분석하는 수학의 분야이다. 

  </blockquote>

  - 통계학 statistics 의 어원은 라틴어 status 인데 이는 국가를 의미한다. 즉 통계학은 국가를 지배하는데에 필요한 학문으로써 발달하였다. 

    - 통계학을 쉽게 말해서 데이터와 자료를 연구하는 학문으로 볼 수 있다. 

    - 통계학은 국가에서 수집된 다량의 데이터를 수집하고 분석하여 국가를 잘 지배할 수 있도록 최선의 결론을 도출하는 학문인 것이다.

  - 역사 

    케틀레(1796) 는 천문학에서 쓰이던 확률론을 사회 데이터에 적용하려 했다. 

    그런데 프랑스 통계를 기초로 범죄 같은 사회적 현상이 마치 물리학 법칙처럼 규칙적으로 발생한다는 사실을 알아 내었다.

    그는 통계학으로써 사회의 법칙을 알아낼 수 있다고 생각하였다. 

    > 이렇게 얻어낸 사회의 법칙은 사회를 지배하는데에 쓰일 수 있다. 

  - 통계학을 배우는 목적을 자료로부터 필요한 정보를 찾고 그것으로부터 필요한 결론을 추론하여 내는 결정 능력을 기르는 것으로 삼으면 좋을 것이다. 

## 기초 용어

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 자료(data, 데이터) : 수, 영상, 단어 등의 형태로 된 의미 단위이다.

  </blockquote>

  - 보통 연구의 바탕이 되는 재료를 뜻하고 자료를 의미있게 정리하면 정보가 된다. 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 질적 자료(qualitative data, 정성적 자료) : 수치로 측정이 불가능한 자료이다.

  </blockquote>

  - 예시

    전화번호, 성별, 종교분류 등이 있다. 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 양적 자료(quantitative data, 정량적 자료) : 수치로 측정이 가능한 자료이다.

  </blockquote>

  - 예시 

    온도, 지능지수, 매출액 등이 있다. 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 정보(information) : 특정 목적의 의사결정을 위하여 의미있게 자료를 가공한 것이다. 

  </blockquote>

  - 정보는 판단을 위하여 존재하기 때문에 목적적합성과 신뢰성, 적시성이 중요하다. 목적적합성이 없다면 판단하는데 있어 의미있는 자료가 되지 못한다. 신뢰성이 없다면 판단할 때 사용할 수 없다. 적시성이 없으면 판단할 때가 이미 지나버려 무의미하게 된다. 

  - 비교적 장기간 사용할 수 있는 정보를 지식으로 취급하기도 한다.

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 지식(knowledge) : 일반적으로 사용할 수 있는 정보, 또는 어떤 대상에 관하여 알고 있는 이해이다. 

  </blockquote>

## 기초 통계학 용어

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 변량(variate) : 자료를 수량으로 나타낸 것이다.

  </blockquote>

  - 예시 

    학생들의 수학 점수를 숫자로 환원하여 나열한 것 

    $$ 92, 84, 88, 45, 12, 29, 39, \dots $$

    은 변량이다.

  - 예시 

    각 국가별 행복도를 수치로 환원하여 나열한 것

    $$ 15, 82, 10, 99, 28, \dots $$

    은 변량이다.

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 계급(class) : 변량을 일정한 간격으로 나눈 구간이다. 

  </blockquote>

  - 예시 

    학생들의 수학 점수를 나열한 변량 

    $$ 92, 84, 88, 45, 12, 29, 39, \dots $$

    에 대하여 
    
    $10$ 점대 $x_1$ 명,

    $20$ 점대 $x_2$ 명,

    $\vdots$

    $80$ 점대 $x _{n-1}$ 명,

    $90$ 점대 $x_n$ 명

    와 같이 일정 구간으로 나눈 것은 계급이라 한다.

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 계급의 크기(class interval) : 변량을 나눈 간격이다.

  </blockquote>

  - 예시 

    학생들의 수학 점수를 $0 \sim 10$, $10 \sim 20$ 와 같이 나누었다면 

    계급의 크기는 $10$ 이다. 

### 대표값

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 대표값(representative value) : 어떤 데이터를 대표하는 값이다. 

  </blockquote>

  - 예시 

    대표값에는 대표적으로 계급값, 중앙값, 평균, 최빈값이 있다. 

    또한 백분위수, 사분위수, 절사평균 등의 대표값이 존재한다. 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 계급값(class mark) : 계급을 대표하는 값으로써 계급의 중앙값이다.

  </blockquote>

  - 예시 

    학생들의 수학 점수를 $0 \sim 10$, $10 \sim 20$ 와 같이 나누었다면 

    계급값은 각각 $5, 15$ 이다. 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 평균(mean) : 데이터를 모두 더한 것을 데이터의 개수로 나눈 값이다. 

  </blockquote>

  - 일반적으로 평균이라고 부르는 것은 통계학에서 산술평균이라고 하는 것이다. 

  - 예시 

    $4$ 명의 한 달 소득이 만 원 단위로

    $$ 100, 200, 128, 328 $$

    라면 이것의 평균은 

    $$ \therefore  \dfrac{100+200+128+328}{4} = 189 $$

    이다. ■ 

    그러니까 평균적으로 사람들이 $189$ 만원을 벌고 있다고 생각할 수 있는 것이다. 

    이렇게 단순하게 생각할 수 있게 해주는 것이 대표값의 장점이다. 

### 도수분포

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 도수(frequency) : 각 계급에 속하는 변량의 개수이다. 

  </blockquote>

  - 예시 

    학생들의 수학 점수를 나열한 변량 

    $$ 92, 84, 88, 45, 12, 29, 39$$

    에서 $80$ 점대($80 \sim 99$) 계급에 속하는 변량의 개수는 $2$ 이므로 
    
    도수가 $2$ 이다.

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 도수분포표(frequency distribution) : 자료를 몇 개의 계급으로 나누고 각 계급의 도수를 정리한 표다.

  </blockquote>

  - 예시

    학생들에게 책을 멀리 던지라고 시키고 그 거리를 측정하여 변량으로 만든 후 그 변량을 거리에 따라 계급으로 나누었다고 하자.
    
    그러면 그 계급에 속하는 도수를 표로 정리하면 다음과 같은 도수분포표가 된다. 

    | 거리(m) | 도수(명) |
    |:--:|:--:| 
    | 0 ~ 10 | 2 | 
    | 10 ~ 20 | 6 | 
    | 20 ~ 30 | 10 |

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 히스토그램(histogram) : 도수분포표의 각 계급의 끝값을 가로축에 표시하고 도수를 세로축에 표시하여 직사각형으로 나타낸 그래프이다. 

  </blockquote>

  - 예시 

    다음 도수분포표를 생각하자.

    | Bin | Count |
    |:--:|:--:|
    | $-3.5$ | $23$ |
    | $-2.5$ | $32$ |
    | $-1.5$ | $109$ |
    | $-0.5$ | $180$ |
    | $0.5$ | $132$ |
    | $1.5$ | $34$ |
    | $2.5$ | $4$ |
    | $3.5$ | $90$ |

    이에 대한 히스토그램은 다음과 같다. 

    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Example_histogram.png/220px-Example_histogram.png)
  
  - 예시 

    히스토그램의 또 다른 예시는 다음과 같다. 

    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Histogram_of_arrivals_per_minute.svg/614px-Histogram_of_arrivals_per_minute.svg.png)

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 상대도수(relative frequency) : 전체 도수에 대한 각 계급의 도수의 비율

  $$ \boxed{(\text{계급의 상대도수}) = \dfrac{(\text{계급의 도수})}{(\text{도수의 총합})} } $$

  이다. 

  </blockquote>

  - 즉 전체 도수가 $1$ 일 때 그 계급의 도수의 값을 뜻한다. 

  - 예시 

    학생들의 수학점수에 대한 상대도수를 구하여 도수분포표에 추가해보면 다음과 같다. 

    | 점수 | 학생 수(명) | 상대도수 |
    |:--:|:--:|:--:| 
    | $61 \sim 70$ | $1$ | $\dfrac{1}{20} = 0.05$ |
    | $71 \sim 80$ | $3$ | $\dfrac{3}{20} = 0.15$ |
    | $81 \sim 90$ | $10$ | $\dfrac{10}{20} = 0.5$ |
    | $91 \sim 100$ | $6$ | $\dfrac{16}{20} = 0.3$ |


- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 편차 : 자료의 한 변량에서 평균을 뺀 값이다. 

  </blockquote>

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 분산 : 편차의 제곱의 합을 전체 변량의 개수로 나눈 값이다.

  </blockquote>

  - 즉 편차 제곱의 평균이다. 

  - $(분산) = \frac{(편차)^2의 총합}{(변량)의 개수}$

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 표준편차 : 분산의 양의 제곱근이다.

  </blockquote>

  - $(표준편차) = \sqrt[]{(분산)}$

## 이산확률변수와 확률분포 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 확률변수(random variable) : 어떤 시행에서 조건에 의해 표본공간의 각 원소(근원사건)에 하나의 실수 $x$ 를 대응시킨 변수

  $$ X = x $$

  이다.

  </blockquote>

  - 확률변수를 사용하면 표본공간을 수량화하여 여러 사건들의 확률을 수학적으로 동시에 다룰 수 있다.

  - 확률이 특정 사건이 일어날 확률을 구하는 것이 목적이었다면 

    확률변수와 이 분야의 개념들은 표본공간 안의 모든 사건들의 확률을 구하여 그 분포를 해석함으로써 다른 사건의 확률을 추정하는 것이 목적이다. 
  
  - 예시 

    $1$ 개의 동전을 $2$ 번 던지는 시행에서 표본공간을 조건 "앞면이 나온 횟수" 로 분할하자.
    
    그러면 분할된 각 사건과 그 확률의 대응관계는 앞면 $H$, 뒷면 $T$ 에 대하여 다음과 같다.

    | 표본공간 | $(T,T)$ | $(H,T), (T, H)$ | $(H,H)$ | 
    |:---:|:---:|:---:|:---:|
    | 앞면이 나온 횟수  | $0$  | $1$ | $2$ |
    | 확률  | $\dfrac{1}{4}$  | $\dfrac{2}{4}=\dfrac{1}{2}$ | $\dfrac{1}{4}$ |

    이때 "앞면이 나온 횟수" 를 $X$ 로 두면 각 사건을 

    $$ X=0, X=1, X=2 $$

    로 표현할 수 있다. ■ 

    이러한 $X$ 들을 표본공간의 각각의 원소, 즉 근원사건에 실수를 대응시킨 것을 확률변수라 한다. 

    이 확률변수로 각각의 사건들이 특정되므로 $X=x$ 로 표현할 수 있다. 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 확률변수로의 확률 표기 : 확률변수 $X$ 에 대하여 어떤 사건 $X = x$ 가 일어날 확률을 

  $$ P(X = x) $$

  로 표기하고 $X$ 가 $a$ 이상, $b$ 이하의 값을 취할 확률을

  $$ P(a \leq  X \leq b) $$

  로 표기한다. 

  </blockquote>

  - 어떤 사건이 일어날 확률을 $P(A)$ 로 표기할 수 있으나 어차피 표본공간 내 모든 근원사건을 확률변수 $X=x$ 로 특정할 수 있기 때문에 
  
    전체 사건(표본공간)에 대한 일관적인 표기를 위하여 $P(X) = x$ 로 표기하는 것이 좋다. 

  - 예시 

    "확률변수의 정의" 의 $1$ 개의 동전을 $2$ 번 던지는 시행에서 표본공간의 근원사건을 "앞면이 나온 횟수" 로 특정하는 예시에서 
    
    각각의 사건들을 확률변수

    $$ X=0, X=1, X=2 $$

    로 표현할 수 있었다. 그러면 이제 이 사건들이 일어날 각각의 확률들을 

    $$ P(X=0) = \dfrac{1}{4}, P(X=1) = \dfrac{1}{2}, P(X=2) = \dfrac{1}{4} $$

    로 일관되게 표현할 수 있다. ■ 

    한편 $X$ 가 $1$ 이상, $2$ 이하의 값을 가질 확률, 즉 앞면이 $1$ 번이나 $2$ 번이 나올 사건이 일어날 확률을 

    $$P(1 \leq X \leq 2) = \dfrac{1}{2} + \dfrac{1}{4} = \dfrac{3}{4}$$

    로 표현할 수 있다. ■ 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 확률분포(probability distribution) : 확률변수 $X$ 가 가질 수 있는 모든 값과 $X$ 가 그 값을 취할 확률의 대응 관계(함수)를

  확률변수 $X$ 의 확률분포라 한다. 

  </blockquote>

  - 예시 

    "확률변수의 정의" 의 $1$ 개의 동전을 $2$ 번 던지는 시행에서 표본공간의 근원사건을 "앞면이 나온 횟수" 로 특정하는 예시에서 
    
    확률변수 $X$ 의 확률분포는 다음과 같다. 

    | $X$ | $0$  | $1$ | $2$ |
    |:---:|:---:|:---:|:---:|
    | $P(X=x)$  | $\dfrac{1}{4}$  | $\dfrac{1}{2}$ | $\dfrac{1}{4}$ |
  
  - 위 예시처럼 확률분포는 확률분포표로 나타낼 수도 있고 좌표계에 확률분포 그래프로 나타낼 수도 있다. 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 이산확률변수(discrete random variable) : 확률변수 $X$ 가 가질 수 있는 값들이 유한개이거나, 또는 자연수나 정수와 같이 셀 수 있을 때 $X$ 를 이산확률변수라 한다. 

  </blockquote>

  - 예시 

    "확률변수의 정의" 의 $1$ 개의 동전을 $2$ 번 던지는 시행에서 표본공간의 근원사건을 "앞면이 나온 횟수" 로 특정하는 예시에서 

    확률변수 $X$ 는 $0, 1, 2$ $3$ 개의 값을 가질 수 있다.

    따라서 $X$ 는 이산확률변수이다. 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 확률질량함수(probability mass function) : 이산확률변수 $X$ 가 가질 수 있는 값이 $x_1, x_2, x_3, \dots, x_n$ 일 때

  $X$ 의 각 값에 $X$ 가 그 값을 취할 확률 $p_1, p_2, p_3, \dots, p_n$ 을 대응시킨 함수 

  $$ P(X = x_i) = p_i (i= 1, 2, 3, \dots, n) $$

  를 $X$ 의 확률질량함수라고 한다. 

  </blockquote>

  - 예시 

    남학생 $4$ 명, 여학생 $3$ 명 중에서 임원 $2$ 명을 뽑으려 할 때 뽑힌 여학생의 수를 확률변수 $X$ 라 하자.

    $X$ 의 확률질량함수를 구해보자. 

    먼저 여학생이 $x$ 명 뽑혔고 남학생이 $y$ 명뽑혔다고 할 때 $x, y$ 는 

    $$ x+ y =2 $$

    의 관계를 갖는다. 그러므로 $y = 2 -x$ 이므로 확률변수 $X = x$ 에 따른 각 사건들의 확률을 $x$ 에 대하여 정리할 수 있다. 

    이제 확률을 구해보자. 확률은 $7$ 명 중에서 $2$ 명을 뽑는 경우의 수와 여학생이 $x$ 명 뽑히는 경우의 수의 비 

    $$ \dfrac{{}_{3}C_{x} \times {}_{4}C_{2-x}}{{}_{7}C_{2}} $$

    이다. 이것은 확률변수 $X = x$ 에 대한 함수와 같으므로 $x = 0, 1, 2$ 에 대한 확률질량함수 

    $$ P(X = x) = \dfrac{{}_{3}C_{x} \times {}_{4}C_{2-x}}{{}_{7}C_{2}} $$ 

    로 표현할 수 있다. ■ 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 확률질량함수의 성질 : 이산확률변수 $X$ 의 확률질량함수가 $P(X = x_i) = p_i(i = 1, 2, 3, \dots, n)$ 일 때 다음이 성립한다. 

  1. $0 \leq P(X = x_i) \leq 1$

  2. $\displaystyle \sum_{i=1}^{n}P(X=x_i)= \sum_{i=1}^{n}p_i = p_1+p_2+p_3+\dots+p_n=1$

  3. $\displaystyle P(x_i \leq X \leq x_j) = \sum_{k=i}^{j}P(X=x_k) = \sum_{k=i}^{j}p_k$ (단, $i, j = 1, 2, 3, \dots, n$ 이고 $i < j$)

  </blockquote>

  - 설명 

    확률질량함수는 어떤 사건에 대한 확률을 나타내는 함수이므로 다음의 확률의 기본 성질이 성립한다. 

    전사건 $S$ 과 임의의 사건 $A$ 에 대하여 다음이 성립한다. 

    1. $\boxed{ 0 \leq P(A) \leq 1}$

    2. $\boxed{ P(S) = 1}$

    3. $\boxed{ P(\emptyset ) = 0}$
  
  - 위의 첫번째, 두번째 성질을 더욱 간단하게 다음과 같이 표기하기도 한다. 

    1. $\displaystyle 0 \leq P(x) \leq 1$

    2. $\displaystyle \Sigma P(x) = 1$

### 이산확률변수의 기댓값, 분산, 표준편차 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 기댓값(expectation, expected value) 또는 이산확률변수의 평균(mean of a discrete random variable) : 이산확률변수 $X$ 의 확률질량함수가 $P(X=x_i) = p_i(i=1,2,3, \dots, n)$ 일 때 

  기댓값은 확률변수($x_1, x_2, \dots, x_n$) 에 그 확률($p_1, p_2, \dots, p_n$)을 곱하여 더한 값

  $$E(X) = \sum_{i=1}^{n}x_ip_i=x_1p_1 + x_2p_2 + \dots + x_n p_n$$

  또는

  $$ \mu = \sum_{i=1}^{n}x_ip_i=x_1p_1 + x_2p_2 + \dots + x_n p_n$$

  이다.

  </blockquote>

  - 더욱 간단하게 확률변수를 소문자 $x$ 로 두고

    $$E(x) = \Sigma  xP(x)$$

    또는

    $$ \mu = \Sigma xP(x)$$

    로 표기하기도 한다.

  - 기대값은 매 시행마다 예측되는 값이다.

    - 예시 

      자동차 판매원이 매 주마다 평균적으로 $2.4$ 대의 자동차를 팔 것을 예측할 수 있다. 
    
  - 예시 

    어떤 기계가 일주일 동안 고장날 횟수를 $20$ 주 동안 관찰하여 얻은 도수분포표가 다음과 같다고 하자. 

    | 변량(고장횟수) | 도수 |
    |:---:|:---:|
    | $0$ | $3$ |
    | $1$ | $4$ |
    | $2$ | $7$ |
    | $3$ | $6$ |

    어떤 기계가 일주일 동안 고장날 횟수 $x$ 와 확률 $P(x)$ 를 정리한 확률분포표가 다음과 같다고 하자.

    | 확률변수 $x$ (고장횟수) | 확률 $P(x)$ |
    |:---:|:---:|
    | $0$ | $.15$ |
    | $1$ | $.20$ |
    | $2$ | $.35$ |
    | $3$ | $.30$ |

    기계가 일주일 동안 고장날 기대값(평균)을 구해보자. 

    확률분포표에 $xP(x)$ 을 추가한 표를 만들어보자.

    | $x$ | $P(x)$ | $xP(x)$ |
    |:---:|:---:|:---:|
    | $0$ | $.15$ | $0(.15) = .00$ |
    | $1$ | $.20$ |$1(.20) = .20$ |
    | $2$ | $.35$ |$2(.35) = .70$ |
    | $3$ | $.30$ |$3(.30) = .90$ |

    그러면 기대값은 

    $$ \therefore \mu = \Sigma xP(x) = 1.80 $$

    이다. ■ 

    이는 기계가 일주일이 $1.8$ 번 고장날 것으로 예상된다는 것이다.


  - 설명 

    학생들 $10$ 명 이 갖고 있는 자전거 개수에 대한 도수분포표(단, $2$ 개 이상은 $2$ 개로 취급함)

    | 변량 | $0$ 개 | $1$ 개 | $2$ 개 |
    |:---:|:---:|:---:|:---:|
    | 도수(명) | $3$ | $5$ | $2$ |

    에서 변량의 평균을 구해보자. 

    $$ \dfrac{0 \times 3 + 1 \times 5 + 2 \times 2}{3 + 5 + 2} = \dfrac{9}{10} $$


    확률변수 $X$ 의 확률분포가 다음과 같다고 하자. 

    | $X$ | $2$  | $4$ | $6$ |
    |:---:|:---:|:---:|:---:|
    | $P(X=x)$  | $\dfrac{1}{4}$  | $\dfrac{1}{2}$ | $\dfrac{1}{4}$ |

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 분산(variance) : 이산확률변수 $X$ 의 확률질량함수가 $P(X=x_i) = p_i(i=1,2,3, \dots, n)$ 일 때 분산은

  $$V(X) = \sum_{i=1}^{n} (x_i- m) ^{2} p_i = E(X ^{2}) - \{E(X)\}^{2} $$

  이다.

  </blockquote>

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 표준편차(standard deviation) : 이산확률변수 $X$ 의 확률질량함수가 $P(X=x_i) = p_i(i=1,2,3, \dots, n)$ 일 때 표준편차는

  $$\sigma (X) = \sqrt[]{V(X)} $$

  이다.

  </blockquote>

### 이산확률변수의 기댓값, 분산, 표준편차 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 평균 : 이산확률변수 $X$ 와 두 상수 $a, b(a \neq 0)$ 에 대하여 평균은 다음 성질을 갖는다. 

  $$ E(aX+b) = aE(X)+b $$

  </blockquote>

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 분산 : 이산확률변수 $X$ 와 두 상수 $a, b(a \neq 0)$ 에 대하여 분산은 다음 성질을 갖는다. 

  $$ V(aX+b) = a ^{2}V(X) $$

  </blockquote>

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 표준편차 : 이산확률변수 $X$ 와 두 상수 $a, b(a \neq 0)$ 에 대하여 표준편차은 다음 성질을 갖는다. 

  $$ \sigma (aX+b) = |a|\sigma (X) $$

