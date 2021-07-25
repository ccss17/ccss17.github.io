
> metadata pass

# 기본행렬연산과 기본행렬

!!! tldr ""

    기본행[열]연산(elementary row[column] operation) : 체 $\mathbf{F}$ 에서 성분을 가져온 $m \times n$ 행렬 $A$ 와 스칼라 $a \in \mathbf{F}$ 에 대하여 $A$ 의 행[열] 에 대한 다음 세 연산이다. 

    1. $A$ 의 두 행[열]을 교환하는 것

    2. $A$ 의 한 행[열]에 영이 아닌 스칼라 $a$ 를 곱하는 것

    3. $A$ 의 한 행[열]에 다른 행[열]의 스칼라 $a$ 배를 더하는 것

- 행연산과 열연산을 기본연산(elementary operation)이라 한다. 또한 기본연산 1), 2), 3) 을 1형(type), 2형, 3형이라 한다.

!!! tldr ""

    $n \times n$ 기본행렬(elementary matrix) : 항등행렬 $I_n$ 에 기본연산을 적용하여 얻은 행렬이다.

- $I_n$ 에 1형, 2형, 3형 연산을 하여 얻은 행렬을 각각 1형, 2형, 3형이라 한다.

- 예시 

    $I_3$ 의 1행, 2행을 교환하여 다음 기본행렬을 얻는다.

    $$ E = \begin{pmatrix} 0&1&0\\ 1&0&0\\ 0&0&1\\ \end{pmatrix} $$

!!! tldr ""

    기본행[열]역연산(elementary row[column] inverse operation) : 체 $\mathbf{F}$ 에서 성분을 가져온 $m \times n$ 행렬 $A$ 와 스칼라 $a \in \mathbf{F}$ 에 대하여 $A$ 의 기본행[열]연산 에 대한 다음 세 연산이다. 

    1. $A$ 의 두 행[열]을 교환하는 것

    2. $A$ 의 한 행[열]에 영이 아닌 스칼라 $\dfrac{1}{a}$ 를 곱하는 것

    3. $A$ 의 한 행[열]에 다른 행[열]의 스칼라 $-a$ 배를 더하는 것

- 교환연산은 역연산이 동일하다.

- $I_n$ 에 기본연산을 적용하여 기본행렬 $E$ 를 얻었다면, $E$ 에 기본역연산을 적용하여 다시 $I_n$ 을 얻을 수 있다.

!!! tldr "정리 3.1"

    행렬 $A \in \mathbf{M}_{m \times n}(\mathbf{F} )$ 에 기본행[열]연산을 하여 행렬 $B$ 를 얻었다면, $B = EA[B = AE]$ 가 되는 $m \times m[n \times n]$ 기본행렬 $E$ 가 존재한다. 이때 $A$ 에서 $B$ 를 얻은 기본행[열]연산을 $I_m[I_n]$ 에 똑같이 적용하면 행렬 $E$ 가 된다. 

    역으로 $E$ 가 $m \times m[n \times n]$ 기본행렬일 때, $I_m[I_n]$ 에서 $E$ 를 얻은 기본행[열]연산을 $A$ 에 똑같이 적용하면 $EA[AE]$ 가 된다.

- 이 정리는 어떤 행렬에 기본행연산을 가하는 것이 그 행렬에 적절한 기본행렬을 곱하는 것과 같다는 것을 말해준다.

    첫번째, 두번째 명제는 기본연산에 대응되는 기본행렬이 항상 존재한다는 것과 그 기본행렬을 구하는 방법을 말해준다. 세번째 명제는 기본행렬이 존재할 때 그것이 기본연산과 대응된다는 것을 말해준다.

- 증명

    1형, 2형, 3형 기본행연산에 대하여 정리가 참임을 증명한 다음 전치행렬으로 열연산을 행연산으로 바꾸면 기본열연산에 대한 증명도 끝난다.

!!! tldr "정리 3.2"

    기본행렬은 가역이다.

    기본행렬의 역행렬도 같은 형(type)의 기본행렬이다.

- 증명

    $E$ 를 $n \times n$ 기본행렬이라 하면 기본행렬의 정의에 의하여 $I_n$ 에 기본행연산을 적용하여 $E$ 를 얻을 수 있다. 

    이 기본행연산에 대한 기본행역연산을 적용하여 $E$ 로부터 $I_n$ 을 얻을 수 있다. 이는 동일한 형(type) 의 행연산에 의하여 $E$ 를 $I_n$ 로 변환할 수 있다는 것이다.

    $E$ 를 $I_n$ 으로 바꾸는 기본행연산은 정리 3.1 에 의하여 행렬 $\bar{E}$ 로 표현할 수 있다. 그러므로 $\bar{E}E = I_n$ 인 기본행렬 $\bar{E}$ 가 존재한다. 

    [행렬곱 결과가 항등행렬인 두 정사각행렬은 모두 가역](../LinearTransformation/#0d6999da9)이므로 $E$ 는 가역이고, $E ^{-1} = \bar{E}$ 이다. ■ 

# 행렬의 랭크와 역행렬

!!! tldr "행렬의 랭크"

    행렬 $A \in \mathbf{M}_{m \times n}(\mathbf{F} )$ 와 $\mathbf{L}_{A} : \mathbf{F} ^{n} \to \mathbf{F} ^{m}$ 에 대하여 다음과 같이 정의한다.

    $$ \text{rank} (A) := \text{rank} (\mathbf{L}_{A}) $$

- 선형변환의 랭크에 대한 성질을 기반으로 행렬의 랭크에 대한 많은 정보를 얻을 수 있다. 

!!! tldr ""

    $n \times n$ 행렬이 가역이기 위한 필요충분조건은 행렬의 랭크가 $n$ 인 것이다. 

- 증명 

    $n \times n$ 행렬 $A$ 와 $\mathbf{L}_{A}: \mathbf{F} ^{n} \to \mathbf{F} ^{n}$ 는 [정리 2.18 따름정리 2](../LinearTransformation/#80bc2f76a) 에 의하여 $A$ 가 가역인 것과 $\mathbf{L}_{A}$ 가 가역인 것은 동치이다. [$\mathbf{L}_{A}$ 가 가역인 것과 $\text{rank} (\mathbf{L}_{A}) = \dim (\mathbf{F} ^{n}) = n$ 인 것은 동치이다](../LinearTransformation/#87356d7a4). 그러므로 행렬의 랭크의 정의에 의하여 $\text{rank} (A) = n$ 인 것과 $A$ 가 가역인 것은 동치이다. ■ 

!!! tldr "정리 3.3"

    유한차원 벡터공간 사이에서 정의된 선형변환 $\mathbf{T} : \mathbf{V} \to \mathbf{W}$ 와 $\mathbf{V} , \mathbf{W}$ 의 순서기저 $\beta , \gamma$ 에 대하여 $\text{rank} (\mathbf{T} ) = \text{rank} ([\mathbf{T} ]^{\gamma}_{\beta} )$ 이다.

- 증명

    [이 정리](../LinearTransformation/#cf9e1b36c) 에 의하여 증명이 끝난다. ■ 

!!! tldr "정리 3.4"

    $m \times n$ 행렬 $A$, $m \times m$ 가역행렬 $P$, $n \times n$ 가역행렬 $Q$ 에 대하여 다음이 성립한다. 

    1. $\text{rank} (AQ)  = \text{rank} (A)$

    2. $\text{rank} (PA)  = \text{rank} (A)$

    3. $\text{rank} (PAQ)  = \text{rank} (A)$

- 증명

    [$Q$ 가 가역이므로 $\mathbf{L}_{Q}$ 는 동형사상](../LinearTransformation/#80bc2f76a)이다. 따라서 다음을 얻는다.

    $$ \mathbf{R} (\mathbf{L}_{AQ})  = \mathbf{R} (\mathbf{L}_A \mathbf{L}_{Q}) = \mathbf{L}_{A}\mathbf{L}_{Q}(\mathbf{F} ^{n}) = \mathbf{L}_{A}(\mathbf{L}_{Q}(\mathbf{F} ^{n})) = \mathbf{L}_{A}(\mathbf{F} ^{n}) = \mathbf{R} (\mathbf{L}_A) $$

    그러므로 $AQ$ 의 랭크는 행렬의 랭크의 정의에 의하여 다음과 같다.

    $$ \text{rank} (AQ) = \text{rank} (A) \tag*{▲} $$