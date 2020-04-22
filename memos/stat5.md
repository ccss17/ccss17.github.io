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

    모집단 $\{1,2,3,4\}$ 에서 하나의 숫자를 취할 확률변수를 $X$ 라 할 때 다음 표

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

  - 모집단의 확률분포가 정규분포가 아니어도 $n$ 이 충분히 크면 표본평균 $\overline{X}$ 는 근사적으로 정규분포

    $$ N \bigg (\mu , \dfrac{\sigma ^{2}}{n} \bigg ) $$

    를 따른다.

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

  표본평균 $\overline{X}$ 에 대한 평균은 

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
    | $P(\overline{X}=x)$| $\dfrac{1}{9}$ | $\dfrac{2}{9}$ |$\dfrac{3}{9}=\dfrac{1}{3}$|$\dfrac{2}{9}$ | $\dfrac{1}{9}$ |

    이제 표본평균 $\overline{X}$ 의 평균을 구해보면

    $$ \therefore  E(\overline{X}) = 1 \times \dfrac{1}{9} + 1.5 \times \dfrac{2}{9} + 2 \times \dfrac{1}{3} + 2.5 \times \dfrac{2}{9} + 3 \times \dfrac{1}{9} = \dfrac{1 + 3 + 6 + 5 + 3}{9} = \dfrac{18}{9} = 2 $$

    임을 알 수 있다. ■ 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 표본평균의 분산 : 모평균이 $\mu$, 모표준편차가 $\sigma$ 인 모집단에서 크기가 $n$ 인 표본을 임의추출 할 때 

  표본평균 $\overline{X}$ 에 대한 분산은 

  $$ V(\overline{X}) = \dfrac{\sigma ^{2}}{n} $$

  이다. 

  </blockquote>

  - 예시 

    "모집단의 확률분포" 의 예시의 모집단에서 크기가 $2$ 인 표본을 임의추출한 표본을 $X_1, X_2$ 이었을 때 이 표본의 평균 $\overline{X} = \dfrac{X_1+X_2}{2}$ 를 구하여 확률변수 $\overline{X}$ 의 분산을 구해보자. 

    "표본평균의 평균" 의 예시에서 표본평균 $\overline{X}$ 의 확률분포표는 다음과 같았고

    | $\overline{X}$| $1$ | $1.5$ |$2$|$2.5$ | $3$ |
    |:---:|:---:|:---:|:---:|:---:|:---:|
    | $P(\overline{X}=x)$| $\dfrac{1}{9}$ | $\dfrac{2}{9}$ |$\dfrac{3}{9}=\dfrac{1}{3}$|$\dfrac{2}{9}$ | $\dfrac{1}{9}$ |

    표본평균 $\overline{X}$ 의 평균은 $E(\overline{X}) = 2$ 이었다.

    따라서 표본평균의 분산 $V(\overline{X})$ 은 

    $$ \therefore  V(\overline{X}) = E(\overline{X} ^{2}) - \{E(\overline{X})\} ^{2} = \bigg (1 ^{2} \times \dfrac{1}{9} + 1.5 ^{2} \times \dfrac{2}{9} + 2 ^{2} \times \dfrac{1}{3} + 2.5 ^{2} \times \dfrac{2}{9} + 3 ^{2} \times \dfrac{1}{9} \bigg ) - 2 ^{2}= \dfrac{13}{3}-4 = \dfrac{1}{3} $$

    이다. ■ 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 표본평균의 표준편차 : 모평균이 $\mu$, 모표준편차가 $\sigma$ 인 모집단에서 크기가 $n$ 인 표본을 임의추출 할 때 

  표본평균 $\overline{X}$ 에 대한 표준편차

  $$ \sigma (\overline{X}) = \dfrac{\sigma }{\sqrt[]{n}} $$

  이다. 

  </blockquote>

  - 예시 

    "모집단의 확률분포" 의 예시의 모집단에서 크기가 $2$ 인 표본을 임의추출한 표본을 $X_1, X_2$ 이었을 때 이 표본의 평균 $\overline{X} = \dfrac{X_1+X_2}{2}$ 를 구하여 확률변수 $\overline{X}$ 의 표준편차 구해보자. 

    "표본평균의 분산" 의 예시에서 표본평균 $\overline{X}$ 의 분산은 $V(\overline{X}) = \dfrac{1}{3}$ 이었다.

    따라서 표본평균의 표준편차 $\sigma (\overline{X})$ 은 

    $$ \therefore  \sigma (\overline{X}) = \sqrt[]{\dfrac{1}{3}} = \dfrac{\sqrt[]{3}}{3}  $$

    이다. ■ 

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

- 모비율 : 모집단에서 어떤 특성을 가지는 대상의 비율을 그 특성에 대한 모비율 $p$ 라 한다.

  </blockquote>

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 표본비율 : 모집단에서 임의추출한 크기가 $n$ 인 표본에서 이 특성을 가지는 대상의 수를 확률변수 $X$ 라 할 때

  그 특성에 대한 대상의 비율을 그 특성에 대한 표본비율 
  
  $$\hat{p} = \dfrac{X}{n}$$
  
  이라 한다.

  </blockquote>

  - 표본의 크기 $n$ 이 충분히 클 때 표본비율 $\hat{p}$ 는 근사적으로 정규분포 

    $$ N \bigg ( p, \dfrac{pq}{n} \bigg ) $$

    를 따른다. 

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 표본비율 $\hat{p}$ 의 평균 : 모비율이 $p$ 인 모집단에서 크기가 $n$ 인 표본을 임의추출 할 때 

  표본비율 $\hat{p}$ 에 대하여 평균은 

  $$ E(\hat{p}) = p $$

  이다.

  </blockquote>

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 표본비율 $\hat{p}$ 의 분산 : 모비율이 $p$ 인 모집단에서 크기가 $n$ 인 표본을 임의추출 할 때 

  표본비율 $\hat{p}$ 에 대하여 분산은 $q = 1 - p$ 에 대하여

  $$ V(\hat{p}) = \dfrac{pq}{n} $$

  이다.

  </blockquote>

- <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;

- 표본비율 $\hat{p}$ 의 표준편차 : 모비율이 $p$ 인 모집단에서 크기가 $n$ 인 표본을 임의추출 할 때 

  표본비율 $\hat{p}$ 에 대하여 표준편차는 $q = 1 - p$ 에 대하여

  $$ \sigma (\hat{p}) = \sqrt[]{\dfrac{pq}{n}} $$

  이다.

  </blockquote>
