# [ccss17.github.io](https://ccss17.github.io)

# 통계적 추정 

# 모집단과 표본 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 모집단(population) : 알고자 하는 전체 조사 대상이다.

  </blockquote>

  - 예시 

    한 학교의 학생들의 여론조사를 위하여 전교생들에 대한 설문조사를 진행한다고 하자.
    
    이때 그 학교의 모든 학생 집단은 모집단이다.

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 표본(sample) : 조사를 하기 위하여 모집단의 일부분을 추출한 것이다.

  </blockquote>

  - 설명 

    여론조사를 하기 위하여 한 국가의 전 국민에 대한 설문조사를 시행하려면 시간과 비용이 너무 많이 들어가서 어느 시점부터 여론조사를 하는 효용을 상쇄시키고 어느 시점부터는 손실이 더 커진다.

    따라서 모집단에서 국민 $1000$ 명을 추출하여 표본을 만들어 조사한다. 정확도를 약간 잃더라도 시간과 비용이 소모되는 것을 적당한 선에서 제한하는 것이다. 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 모집단의 크기 : 모집단에 속한 자료의 개수이다.

  </blockquote>

  - 예시 

    생산되는 전구 $10000$ 개에서 전구의 수명을 조사하려 한다. 

    이때 모집단의 크기는 $10000$ 이다.

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 표본의 크기 : 표본에 속한 자료의 개수이다.

  </blockquote>

  - 예시 

    생산되는 전구 $10000$ 개에서 $10$ 개를 추출하여 표본으로 삼고 전구의 수명을 조사하려 한다. 

    이때 표본의 크기는 $10$ 이다.

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 전수조사(total inspection) : 모집단 전체를 전부 다 조사하는 것이다.

  </blockquote>

  - 예시 

    한 학교의 학생들의 여론조사를 위하여 전교생들에 대한 설문조사를 진행한다고 하자.
    
    이때 이 설문조사는 전수조사가 된다. 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 표본조사(sample survey) : 모집단의 일부만, 즉 표본만 조사하는 것이다.

  </blockquote>

  - 설명 

    여론조사를 하기 위하여 한 국가의 전 국민에 대한 설문조사를 시행하려면 시간과 비용이 너무 많이 들어간다.

    따라서 모집단에서 국민 $1000$ 명을 추출하여 표본을 만들어 조사하는 것은 표본조사이다.

  - 표본조사의 목적은 모집단에서 얻은 표본으로부터 얻는 정보를 분석하여 최종적으로 모집단의 성질을 추측하는 것이다.

    아무리 표본을 조사한다고 하지만 결국에 관심있는 것은 모집단에 대한 정보임을 기억해야 한다. 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 추출(sampling) : 모집단으로부터 표본에 포함시킬 대상들을 뽑는 것이다.

  </blockquote>

  - 표본을 생성하기 위하여 모집단에서 대상을 추출하는데 표본조사의 목적은 결국에 모집단을 이해하기 위함이다.

    따라서 모집단으로부터 일부 대상을 추출할 때 모집단의 특성이 잘 반영되도록 대상들을 뽑아야 한다. 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 임의추출(random sampling) : 추출의 방법 중 하나로써 모집단에 속한 각 대상들을 같은 확률로 뽑는 방법이다.

  </blockquote>

  - 예시 

    제비뽑기나 난수 생성기로 표본을 추출하는 것이 임의추출이다. 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 임의표본(random sample) : 임의추출한 표본이다.

  </blockquote>

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 복원추출(sampling with replacement) : 추출한 것을 다시 넣고 다음을 추출하는 방법이다.

  </blockquote>

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 비복원추출(sampling without replacement) : 추출한 것을 다시 넣지 않고 다음을 추출하는 방법이다. 

  </blockquote>

  - 모집단의 크기가 충분히 크면 비복원추출도 복원추출로 볼 수 있다. 

# 표본평균의 평균, 분산, 표준편차

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 모집단의 확률분포 : 모집단에서 조사의 대상이 되는 특성을 나타내는 확률변수 $X$ 의 확률분포이다. 

  </blockquote>

  - 예시 

    모집단 $\{1,2,3\}$ 에서 하나의 숫자를 취할 확률변수를 $X$ 라 할 때 다음 표

    | $X$| $1$ | $2$ |$3$|
    |:---:|:---:|:---:|:---:|
    | $P(X=x)$| $\dfrac{1}{3}$  |$\dfrac{1}{3}$ |$\dfrac{1}{3}$ |

    를 모집단의 확률분포라고 할 수 있다. 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 모평균(population mean) : 모집단의 확률분포의 확률변수 $X$ 의 평균을 모평균 $\mu$ 라 한다.

  </blockquote>

  - 예시 

    "모집단의 확률분포" 의 예시의 모집단의 확률분포에서 모평균을 구해보면 

    $$ \therefore  \mu = 1 \times \dfrac{1}{3} + 2 \times \dfrac{1}{3} + 3 \times \dfrac{1}{3} = \dfrac{1+2+3}{3} = 2 $$

    이다. ■ 

    그러니까 이 값으로 "다음 시행에서 $2$ 라는 값이 나올 것을 기대할 수 있다" 또는 "평균적으로 값이 $2$ 를 취한다" 라고 해석할 수 있다. 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 모분산(population variance) : 모집단의 확률분포의 확률변수 $X$ 의 분산을 모분산 $\sigma ^{2}$ 라 한다.

  </blockquote>

  - 예시 

    "모집단의 확률분포" 의 예시의 모집단의 확률분포에서 모분산을 구해보면 

    $$ \therefore \sigma ^{2} = E(X ^{2}) - \mu ^{2} = \bigg (1 ^{2} \dfrac{1}{3}+2 ^{2}\dfrac{1}{3}+3 ^{2}\dfrac{1}{3}\bigg ) - 2^{2} = \dfrac{1+4+9}{3}- \dfrac{12}{3} = \dfrac{2}{3}  $$

    이다. ■ 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 모표준편차(population standard deviation) : 모집단의 확률분포의 확률변수 $X$ 의 분산을 모분산 $\sigma$ 라 한다.

  </blockquote>

  - 예시 

    "모집단의 확률분포" 의 예시의 모집단의 확률분포에서 모표준편차를 구해보면 

    $$ \therefore \sigma = \sqrt[]{\dfrac{2}{3}}  = \dfrac{\sqrt[]{6}}{3} $$

    이다. ■ 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 표본평균(sample mean) : 모집단에서 크기가 $n$ 인 표본 $X_1, X_2, \dots, X_n$ 을 임의추출했을 때 이들의 평균

  $$ \overline{X} = \dfrac{1}{n} \sum_{i=1}^{n}X_i $$

  이다.

  </blockquote>

  - 모평균 $\mu$ 이 고정된 상수임에 비해 표본평균 $\overline{X}$ 은 추출된 표본에 따라 여러 값을 가질 수 있는 확률변수이다.

  - 모집단의 확률분포가 정규분포이면 표본평균 $\overline{X}$ 는 $n$ 의 크기에 관계없이 정규분포

    $$ N \bigg (\mu , \dfrac{\sigma ^{2}}{n} \bigg ) $$

    를 따른다.

  - (중심극한정리) 모집단의 확률분포가 정규분포가 아니어도 $n$ 이 충분히 크면 표본평균 $\overline{X}$ 는 근사적으로 정규분포

    $$ N \bigg (\mu , \dfrac{\sigma ^{2}}{n} \bigg ) $$

    를 따른다.

    - 보통 $n$ 이 $30$ 이상이면 충분히 큰 표본으로 간주한다. 

  - 예시 

    "모집단의 확률분포" 의 예시의 모집단에서 크기가 $2$ 인 표본을 임의추출한 표본을 $X_1, X_2$ 라 하면 이 표본은 다음 중 하나로 될 수 있다. 

    | $X_1$| $1$ | $1$ |$1$|$2$ | $2$ |$2$|$3$ | $3$ |$3$|
    |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
    | $X_2$| $1$ | $2$ |$3$|$1$ | $2$ |$3$|$1$ | $2$ |$3$|

    이때 표본들의 표본평균 $\overline{X} = \dfrac{X_1+X_2}{2}$ 는 

    | $\overline{X}$| $1$ | $1.5$ |$2$|$1.5$ | $2$ |$2.5$|$2$ | $2.5$ |$3$|
    |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|

    위와 같은 값을 가질 수 있는 확률변수이다. ■ 

    그러니까 이 새로운 확률변수 $\overline{X}$(표본평균) 에 대한 평균, 분산, 표준편차를 구할 수 있는 것이다. 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 표본분산(sample variance) : 모집단에서 크기가 $n$ 인 표본 $X_1, X_2, \dots, X_n$ 을 임의추출했을 때 이들의 분산

  $$ S ^{2} = \dfrac{1}{n-1}\sum_{i=1}^{n}(X_i - \overline{X}) ^{2} $$

  이다.

  </blockquote>

  - 모분산과 달리 표본분산에서는 분산을 표본의 크기 $n$ 이 아닌 $n-1$ 로 나누어서 구하는데 이는 표본분산과 모분산의 차이를 줄이기 위해서이다. 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 표본표준편차(sample standard deviation) : 모집단에서 크기가 $n$ 인 표본 $X_1, X_2, \dots, X_n$ 을 임의추출했을 때 이들의 표준편차

  $$ S = \sqrt[]{S ^{2}} $$

  이다.

  </blockquote>

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 표본평균의 평균 : 모평균이 $\mu$, 모표준편차가 $\sigma$ 인 모집단에서 크기가 $n$ 인 표본을 임의추출 할 때 

  표본평균 $\overline{X}$ 들의 평균은 

  $$ E(\overline{X}) = \mu $$

  이다. 

  </blockquote>

  - 예시 

    "모집단의 확률분포" 의 예시의 모집단에서 크기가 $2$ 인 표본을 임의추출한 표본을 $X_1, X_2$ 이었을 때 이 표본의 평균 $\overline{X} = \dfrac{X_1+X_2}{2}$ 를 구하여 확률변수 $\overline{X}$ 의 평균을 구해보자. 

    "표본평균(sample mean)" 의 예시에서 확률변수 $\overline{X}$ 는 다음과 같은 값을 가질 수 있었음을 조사했으니까

    | $\overline{X}$| $1$ | $1.5$ |$2$|$1.5$ | $2$ |$2.5$|$2$ | $2.5$ |$3$|
    |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|

    표본평균 $\overline{X}$ 의 확률분포표는 다음과 같다. 

    | $\overline{X}$| $1$ | $1.5$ |$2$|$2.5$ | $3$ |
    |:---:|:---:|:---:|:---:|:---:|:---:|
    | $P(\overline{X}=x)$| $\dfrac{1}{9}$ | $\dfrac{2}{9}$ |$\dfrac{3}{9}$|$\dfrac{2}{9}$ | $\dfrac{1}{9}$ |

    이제 표본평균 $\overline{X}$ 의 평균을 구해보면

    $$ \therefore  E(\overline{X}) = 1 \times \dfrac{1}{9} + 1.5 \times \dfrac{2}{9} + 2 \times \dfrac{3}{9} + 2.5 \times \dfrac{2}{9} + 3 \times \dfrac{1}{9} = \dfrac{1 + 3 + 6 + 5 + 3}{9} = \dfrac{18}{9} = 2 $$

    임을 알 수 있다. ■ 

    한편 표본평균의 평균 $E(\overline{X})$ 는 모평균 $\mu$ 와 $E(\overline{X}) = \mu$ 의 관계를 갖는다는 점을 이용하여 "모평균(population mean)" 의 예시에서 $\mu = 2$ 였으므로 

    $$ \therefore E(\overline{X}) = \mu = 2 $$

    임을 알 수 있다. ■ 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 표본평균의 분산 : 모평균이 $\mu$, 모표준편차가 $\sigma$ 인 모집단에서 크기가 $n$ 인 표본을 임의추출 할 때 

  표본평균 $\overline{X}$ 들의 분산은 

  $$ V(\overline{X}) = \dfrac{\sigma ^{2}}{n} $$

  이다. 

  </blockquote>

  - 예시 

    "모집단의 확률분포" 의 예시의 모집단에서 크기가 $2$ 인 표본을 임의추출한 표본을 $X_1, X_2$ 이었을 때 이 표본의 평균 $\overline{X} = \dfrac{X_1+X_2}{2}$ 를 구하여 확률변수 $\overline{X}$ 의 분산을 구해보자. 

    "표본평균의 평균" 의 예시에서 표본평균 $\overline{X}$ 의 확률분포표는 다음과 같았고

    | $\overline{X}$| $1$ | $1.5$ |$2$|$2.5$ | $3$ |
    |:---:|:---:|:---:|:---:|:---:|:---:|
    | $P(\overline{X}=x)$| $\dfrac{1}{9}$ | $\dfrac{2}{9}$ |$\dfrac{3}{9}$|$\dfrac{2}{9}$ | $\dfrac{1}{9}$ |

    표본평균 $\overline{X}$ 의 평균은 $E(\overline{X}) = 2$ 이었다.

    따라서 표본평균의 분산 $V(\overline{X})$ 은 

    $$ \therefore  V(\overline{X}) = E(\overline{X} ^{2}) - \{E(\overline{X})\} ^{2} = \bigg (1 ^{2} \times \dfrac{1}{9} + 1.5 ^{2} \times \dfrac{2}{9} + 2 ^{2} \times \dfrac{3}{9} + 2.5 ^{2} \times \dfrac{2}{9} + 3 ^{2} \times \dfrac{1}{9} \bigg ) - 2 ^{2}= \dfrac{13}{3}-4 = \dfrac{1}{3} $$

    이다. ■ 

    한편 표본평균의 분산 $V(\overline{X})$ 는 모분산 $\sigma ^{2}$ 와 표본의 크기 $n$ 에 대하여 $V(\overline{X}) = \dfrac{\sigma ^{2}}{n}$ 의 관계를 갖는다는 점을 이용하여 "모분산(population variance)" 의 예시에서 $\sigma ^{2} = \dfrac{2}{3}$ 이고 표본의 크기는 $2$ 였으므로

    $$ \therefore V(\overline{X}) = \dfrac{\sigma ^{2}}{n} = \dfrac{\frac{2}{3}}{2} = \dfrac{1}{3} $$

    임을 알 수 있다. ■ 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 표본평균의 표준편차 : 모평균이 $\mu$, 모표준편차가 $\sigma$ 인 모집단에서 크기가 $n$ 인 표본을 임의추출 할 때 

  표본평균 $\overline{X}$ 들의 표준편차는

  $$ \sigma (\overline{X}) = \dfrac{\sigma }{\sqrt[]{n}} $$

  이다. 

  </blockquote>

  - 그러므로 모집단의 평균, 분산, 표준편차와 표본의 평균, 분산, 표준편차는 다음과 같은 관계를 가진다.

    ![캡처](https://user-images.githubusercontent.com/16812446/79965816-7684e280-84c7-11ea-8ec9-05f6175ca128.PNG)

  - 예시 

    "모집단의 확률분포" 의 예시의 모집단에서 크기가 $2$ 인 표본을 임의추출한 표본을 $X_1, X_2$ 이었을 때 이 표본의 평균 $\overline{X} = \dfrac{X_1+X_2}{2}$ 를 구하여 확률변수 $\overline{X}$ 의 표준편차 구해보자. 

    "표본평균의 분산" 의 예시에서 표본평균 $\overline{X}$ 의 분산은 $V(\overline{X}) = \dfrac{1}{3}$ 이었다.

    따라서 표본평균의 표준편차 $\sigma (\overline{X})$ 은 

    $$ \therefore  \sigma (\overline{X}) = \sqrt[]{\dfrac{1}{3}} = \dfrac{\sqrt[]{3}}{3}  $$

    이다. ■ 

    한편 표본평균의 표준편차 $\sigma(\overline{X})$ 는 모표준편차 $\sigma$ 와 표본의 크기 $n$ 에 대하여 $\sigma (\overline{X}) = \dfrac{\sigma }{\sqrt[]{n}}$ 의 관계를 갖는다는 점을 이용하여 "모표준편차(population variance)" 의 예시에서 $\sigma = \dfrac{\sqrt[]{6}}{3}$ 이고 표본의 크기는 $2$ 였으므로

    $$ \therefore \sigma (\overline{X}) = \dfrac{\sigma }{\sqrt[]{n}} = \dfrac{\frac{\sqrt[]{6}}{3}}{\sqrt[]{2}} = \dfrac{\sqrt[]{6}}{3 \sqrt[]{2}} = \dfrac{\sqrt[]{12}}{6} = \dfrac{\sqrt[]{3}}{3} $$

    임을 알 수 있다. ■ 

  - 예시 

    어떤 공장에서 생산한 건전지의 수명은 평균이 $200$ 시간이고 표준편차가 $10$ 시간인 정규분포 

    $$ N(200, 10 ^{2}) $$

    을 따른다고 하자. 이때 생산된 건전지 중에서 임의추출한 크기가 $25$ 인 표본의 표본평균을 $\overline{X}$ 라 할 때

    $$ P(199 \leq \overline{X} \leq 201) $$

    의 값을 구해보자. 

    모집단이 정규분포 $N(200, 10 ^{2})$ 를 따르므로 크기가 $25$ 인 표본평균 $\overline{X}$ 는 정규분포

    $$ N \bigg (200, \dfrac{10 ^{2}}{25}\bigg ) = N(200, 2 ^{2}) $$

    를 따른다. 이제 확률변수 $\overline{X}$ 를 표준화하여 표준정규분포의 확률변수 $Z = \dfrac{\overline{X} - \mu }{\sigma } = \dfrac{\overline{X} - 200}{2}$ 를 만들자. 그러면 

    $$ P(199 \leq \overline{X} \leq 201) = P \bigg (\dfrac{199 - 200}{2} \leq Z \leq \dfrac{201 - 200}{2} \bigg ) $$

    $$ = P(-0.5 \leq Z \leq 0.5) = 2 P(0 \leq Z \leq 0.5) $$

    $$ = 2 \times  (0.1915) = 0.383 $$

    이다. 그러므로 

    $$ \therefore  P(199 \leq \overline{X} \leq 201) = 0.383 $$

    이다. ■ 

    이 값은 "수명이 $199$ 이상이고 $201$ 인 건전지의 비율이 $38.3\%$ 이다" 또는 "어떤 건전지를 골랐는데 그 수명이 $199$ 이상이고 $201$ 이하일 확률이 $38.3\%$ 이다" 로 해석될 수 있다.

# 표본비율의 평균, 분산, 표준편차

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 모비율(population ratio) : 모집단에서 어떤 특성을 가지는 대상의 비율을 그 특성에 대한 모비율 $p$ 라 한다.

  </blockquote>

  - 기호 $p$ 는 proportion(비율) 의 앞글자를 딴 것이다. 

  - 예시 

    어느 도시의 청소년 $3482$ 명 중 흡연자가 $218$ 명이라고 하면 모집단에서 청소년 흡연자의 비율, 즉 모비율은 

    $$ \therefore  p = \dfrac{218}{3482} \approx 0.062 = 6.2\% $$

    이다. ■ 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 표본비율(sample ratio) : 모집단에서 임의추출한 크기가 $n$ 인 표본에서 이 특성을 가지는 대상의 수를 확률변수 $X$ 라 할 때

  그 특성에 대한 대상의 비율을 그 특성에 대한 표본비율 
  
  $$\hat{p} = \dfrac{X}{n}$$
  
  이라 한다.

  </blockquote>

  - 기호 $\hat{p}$ 는 "피햇" 으로 읽는다. 

  - 표본의 크기 $n$ 이 충분히 클 때 표본비율 $\hat{p}$ 는 근사적으로 정규분포 

    $$ N \bigg ( p, \dfrac{pq}{n} \bigg ) $$

    를 따른다. 

    - 증명 

      표본비율 $\hat{p} = \dfrac{X}{n}$ 에서 확률변수 $X$ 는 모집단에서 임의추출한 크기 $n$ 의 표본에서 어떤 특성을 가진 대상의 갯수이다.

      그러므로 크기 $n$ 의 표본에서 그 특성을 가진 대상들이 추출되었을 가짓수는 $0, 1, 2, \dots, n$ 이다.
      
      즉, 크기 $n$ 의 표본에 특성을 가진 대상이 아예 추출되지 않았을 수도 있고 
      
      단 $1$ 개의 특성을 가진 대상이 모집단에서 추출되어 속해있을 수도 있고

      특성을 가진 대상이 모집단에서 $2$ 개가 추출되어 속해있을 수도 있고

      특성을 가진 대상이 모집단에서 $n$ 개가 추출되어 속해있을 수도 있다.

      이때 모비율 $p$ 에 의하여 모집단에서 각각의 대상들이 그 특성을 가질 확률은 $p$ 이다. 또한 확률변수 $X$ 란 모집단에서 대상을 뽑는 독립시행을 $n$ 번 했을 때 특성을 갖는 대상들의 수이다.
      
      따라서 확률변수 $X$ 는 특성을 갖는 대상의 갯수 $x = 0, 1, 2, \dots, n$ 와 $q = 1-p$ 에 대하여 확률질량함수

      $$ P(X = x) = {}_{n}C_{x} p ^{x} q ^{n-x} $$

      를 가지며 이항분포의 정의에 의하여

      $$ B(n, p) $$

      를 따른다. 그러므로 확률변수 $X$ 의 평균과 분산은 

      $$ E(X) = np, V(X) = npq $$

      이다. 이때 이항분포에서 $n$ 이 충분히 크면 확률분포가 정규분포를 따르므로 확률변수 $X$ 는 근사적으로 정규분포를 따른다.
      
      그런데 표본비율 $\hat{p} = \dfrac{X}{n}$ 도 단지 확률변수 $X$ 를 $n$ 으로 나눈 것이므로 표본의 크기 $n$ 이 충분히 크면 평균 $E(\hat{p})$ 과 분산 $V(\hat{p})$ 에 대하여 근사적으로 정규분포

      $$ \therefore  N \bigg(E(\hat{p}) , V(\hat{p}) \bigg ) = N \bigg(p , \dfrac{pq}{n} \bigg ) $$

      를 따른다. ■ 

  - 예시 

    "모비율" 의 예시의 어느 도시의 청소년 $3482$ 명 중 흡연자가 $218$ 명이라고 하였다. 이때 모집단에서 $300$ 명을 임의추출했더니 그중에서 청소년 흡연자가 $31$ 명이었다. 그러면 표본에서 청소년 흡연자의 비율, 즉 표본비율은

    $$ \therefore  \hat{p} = \dfrac{31}{300} \approx 0.103 = 10.3\% $$

    이다. ■ 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 표본비율 $\hat{p}$ 의 평균 : 모비율이 $p$ 인 모집단에서 크기가 $n$ 인 표본을 임의추출 할 때 

  표본비율 $\hat{p}$ 에 대하여 평균은 

  $$ E(\hat{p}) = p $$

  이다.

  </blockquote>

  - 증명 

    "표본비율(sample ratio)" 의 $n$ 이 클 때 표본비율 $\hat{p}$ 이 정규분포를 따르는 것의 증명에서 확률변수 $X$ 는 이항분포 $B(n, p)$ 를 따르며 평균과 분산은 

    $$ E(X) = np, V(X) = npq $$

    이었다. 이에 따라 확률변수 $X$ 의 스칼라배 $\dfrac{1}{n}$ 인 표본비율 $\hat{p} = \dfrac{X}{n}$ 의 평균은 

    $$ \therefore  E(\hat{p}) = E \bigg (\dfrac{X}{n} \bigg ) = \dfrac{1}{n}E(X)=\dfrac{1}{n} np = p $$

    이다. ■ 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 표본비율 $\hat{p}$ 의 분산 : 모비율이 $p$ 인 모집단에서 크기가 $n$ 인 표본을 임의추출 할 때 

  표본비율 $\hat{p}$ 에 대하여 분산은 $q = 1 - p$ 에 대하여

  $$ V(\hat{p}) = \dfrac{pq}{n} $$

  이다.

  </blockquote>

  - 증명 

    "표본비율 $\hat{p}$ 의 평균" 의 증명에서 확률변수 $X$ 는 이항분포 $B(n, p)$ 를 따르며 확률변수 $X$ 의 평균과 분산은 $q = 1-p$ 에 대하여

    $$ E(X) = np, V(X) = npq $$

    이었다. 따라서 확률변수 $X$ 의 스칼라배 $\dfrac{1}{n}$ 인 표본비율 $\hat{p} = \dfrac{X}{n}$ 의 분산은

    $$ \therefore  V(\hat{p}) = V \bigg (\dfrac{X}{n} \bigg ) = \dfrac{1}{n ^{2}}V(X)=\dfrac{1}{n ^{2}} npq = \dfrac{pq}{n} $$

    이다. ■ 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 표본비율 $\hat{p}$ 의 표준편차 : 모비율이 $p$ 인 모집단에서 크기가 $n$ 인 표본을 임의추출 할 때 

  표본비율 $\hat{p}$ 에 대하여 표준편차는 $q = 1 - p$ 에 대하여

  $$ \sigma (\hat{p}) = \sqrt[]{\dfrac{pq}{n}} $$

  이다.

  </blockquote>

  - 증명 

    "표본비율 $\hat{p}$ 의 분산" 의 증명에서 확률변수 $X$ 의 스칼라배 $\dfrac{1}{n}$ 인 표본비율 $\hat{p} = \dfrac{X}{n}$ 의 분산은

    $$ V(\hat{p}) = \dfrac{pq}{n} $$

    이었다. 그러므로 표본비율 $\hat{p}$ 의 표준편차는 

    $$ \therefore  \sigma (\hat{p}) = \sqrt[]{\dfrac{pq}{n}} $$

    이다. ■ 
  
  - 예시 

    어떤 고등학교 학생 중 $40\%$ 가 졸업 후 대학에 진학하지 않고 바로 취직할 것으로 조사되었다.
    
    이 고등학교 학생 중에서 $96$ 명을 임의추출했을 때 바로 취직할 학생이 $46\%$ 이상 $50\%$ 이하일 확률을 구해보자. 

    대상의 특성을 "졸업 후 바로 취직하는 학생" 으로 두면 모집단에서 특성에 대한 모비율은 $p = 0.4$ 이다.
    
    임의추출한 $96$ 명의 표본에서 $96$ 을 $n$ 으로 두고 특성을 가지는 수를 $X$ 로 두면 표본비율을 $\hat{p} = \dfrac{X}{n}$ 로 볼 수 있고 이때 표본비율이

    $$ P(0.46 \leq \hat{p} \leq 0.5) $$

    일 확률을 구해야 한다. 

    표본비율의 평균, 분산, 표준편차는 $p = 0.4, q = 0.6, n = 94$ 이므로

    $$ E(\hat{p}) = p = 0.4 $$
    
    $$ V(\hat{p}) = \dfrac{pq}{n} = \dfrac{0.4 \times 0.6}{94} = \dfrac{1}{400} $$ 
    
    $$ \sigma (\hat{p}) = \sqrt[]{V(\hat{p})} = \sqrt[]{\dfrac{1}{400}} = \dfrac{1}{20} = 0.05$$

    이다. $n$ 이 $94$ 로 충분히 크므로 확률변수 $X$ 는 정규분포를 따르고 그것의 실수배인 확류변수 $\hat{p} = \dfrac{X}{n}$ 도 정규분포를 따른다. 그러므로 표준화하여 새로운 확률변수 $Z = \dfrac{\hat{p} - 0.4 }{0.05 }$ 를 만들면 

    $$ P(0.46 \leq \hat{p} \leq 0.5) = P \bigg ( \dfrac{0.46 - 0.4}{0.05}  \leq Z \leq \dfrac{0.5-0.4}{0.05} \bigg ) $$

    $$ = P(1.2 \leq Z \leq 2) = P(0 \leq Z \leq 2) - P(0 \leq Z \leq 1.2) $$

    $$ = 0.4772 - 0.3849 = 0.0923 $$

    이다. 따라서 이 고등학교 학생 중에서 $96$ 명을 임의추출했을 때 바로 취직할 학생이 $46\%$ 이상 $50\%$ 이하일 확률은

    $$ \therefore  P(0.46 \leq \hat{p} \leq 0.5)= 0.0923 $$

    이다. ■ 

    즉 $9.2\%$ 정도라고 생각할 수 있다. 

# 모평균의 추정 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 추정 : 표본에서 얻은 결과를 이용하여 모집단의 평균, 표준편차 등을 추측하는 것이다.

  </blockquote>

  - "표본평균과 표본비율의 평균, 분산, 표준편차" 에서는 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 신뢰도 : 표본평균의 분포로부터 모평균이 포함될 구간을 얻을 때 

  그 구간에 모평균이 포함될 확률이다. 

  </blockquote>

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 신뢰구간 : 모평균 $\mu$ 이 존재할 것으로 추정되는 구간이다.

  </blockquote>

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 모평균의 신뢰구간 : 정규분포 $N(\mu , \sigma ^{2})$ 을 따르는 모집단에서 임의추출한 크기가 $n$ 인 표본의 표본평균을 $\overline{X}$ 이라 할 때 

  모평균 $\mu$ 의 신뢰구간은 다음과 같다.

  1. 신뢰도 $95\%$ 의 신뢰구간

      $$ \bigg [ \overline{X} - 1.96 \dfrac{\sigma }{\sqrt[]{n}}, \overline{X} + 1.96 \dfrac{\sigma }{\sqrt[]{n}} \bigg ] \Leftarrow \overline{X} - 1.96 \dfrac{\sigma }{\sqrt[]{n}} \leq \mu \leq  \overline{X} + 1.96 \dfrac{\sigma }{\sqrt[]{n}} $$

  2. 신뢰도 $99\%$ 의 신뢰구간

      $$ \bigg [ \overline{X} - 2.58 \dfrac{\sigma }{\sqrt[]{n}}, \overline{X} + 2.58 \dfrac{\sigma }{\sqrt[]{n}} \bigg ] \Leftarrow \overline{X} - 2.58 \dfrac{\sigma }{\sqrt[]{n}} \leq \mu \leq  \overline{X} + 2.58 \dfrac{\sigma }{\sqrt[]{n}} $$

  </blockquote>

  - 모표준편차 $\sigma$ 가 주어지지 않은 경우 표본표준편차 $S$ 를 사용할 수 있다. 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 모평균의 신뢰구간 길이 : 모평균의 신뢰구간으로부터 모평균 $\mu$ 의 신뢰구간 길이는 다음과 같다. 

  1. 신뢰도 $95\%$ 의 신뢰구간 길이 : $\displaystyle 2 \times 1.96 \dfrac{\sigma }{\sqrt[]{n}}$

  2. 신뢰도 $99\%$ 의 신뢰구간 길이 : $\displaystyle 2 \times 2.58 \dfrac{\sigma }{\sqrt[]{n}}$

  </blockquote>

# 모비율의 추정 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 모비율의 신뢰구간 : 모집단에서 임의추출한 크기가 $n$ 인 표본의 표본비율을 $\hat{p}$ 이라 할 때

  $n$ 이 충분히 크면 $\hat{q} = 1 - \hat{p}$ 에 대하여 모비율 $p$ 의 신뢰구간은 다음과 같다.

  1. 신뢰도 $95\%$ 의 신뢰구간

      $$ \bigg [ \hat{p} - 1.96 \sqrt[]{\dfrac{\hat{p}\hat{q}}{n}}, \hat{p} + 1.96 \sqrt[]{\dfrac{\hat{p}\hat{q}}{n}} \bigg ] \Leftarrow \hat{p} - 1.96 \sqrt[]{\dfrac{\hat{p}\hat{q}}{n}} \leq p \leq  \hat{p} + 1.96 \sqrt[]{\dfrac{\hat{p}\hat{q}}{n}} $$

  2. 신뢰도 $99\%$ 의 신뢰구간

      $$ \bigg [ \hat{p} - 2.58 \sqrt[]{\dfrac{\hat{p}\hat{q}}{n}}, \hat{p} + 2.58 \sqrt[]{\dfrac{\hat{p}\hat{q}}{n}} \bigg ] \Leftarrow \hat{p} - 2.58 \sqrt[]{\dfrac{\hat{p}\hat{q}}{n}} \leq p \leq  \hat{p} + 2.58 \sqrt[]{\dfrac{\hat{p}\hat{q}}{n}}  $$

  </blockquote>

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 모비율의 신뢰구간 길이 : 모비율의 신뢰구간으로부터 모비율 $p$ 의 신뢰구간 길이는 다음과 같다.

  1. 신뢰도 $95\%$ 의 신뢰구간 길이 : $\displaystyle 2 \times 1.96 \sqrt[]{\dfrac{\hat{p}\hat{q}}{n}}$

  2. 신뢰도 $99\%$ 의 신뢰구간 길이 : $\displaystyle 2 \times 2.58 \sqrt[]{\dfrac{\hat{p}\hat{q}}{n}}$

  </blockquote>