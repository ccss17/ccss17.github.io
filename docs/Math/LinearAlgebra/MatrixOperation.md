
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

- 이 정리는 가역행렬에 대한 행렬곱 연산이 행렬의 랭크를 보존한다는 것을 말해준다.

    선형변환의 랭크를 찾는 문제는 행렬의 랭크를 찾는 문제로 귀결되는데, 이 정리가 유용한 도구를 제공해준다.

- 증명

    1:

    [$Q$ 가 가역이므로 $\mathbf{L}_{Q}$ 는 동형사상](../LinearTransformation/#80bc2f76a)이다. 따라서 다음을 얻는다.

    $$ \mathbf{R} (\mathbf{L}_{AQ})  = \mathbf{R} (\mathbf{L}_A \mathbf{L}_{Q}) = \mathbf{L}_{A}\mathbf{L}_{Q}(\mathbf{F} ^{n}) = \mathbf{L}_{A}(\mathbf{L}_{Q}(\mathbf{F} ^{n})) = \mathbf{L}_{A}(\mathbf{F} ^{n}) = \mathbf{R} (\mathbf{L}_A) $$

    그러므로 $AQ$ 의 랭크는 행렬의 랭크의 정의에 의하여 다음과 같다.

    $$ \text{rank} (AQ) = \text{rank} (A) \tag*{▲} $$

    2: 

    $\mathbf{L}_{PA} = \mathbf{L}_{P}\mathbf{L}_{A}$ 에서 $\mathbf{R} (\mathbf{L}_A)$ 은 $\mathbf{F} ^{m}$ 의 부분공간이므로 [이 정리](../LinearTransformation/#1e331034c) 에 의하여 다음이 성립한다.

    $$ \dim (\mathbf{R} (\mathbf{L}_A) ) = \dim (\mathbf{L}_{P}(\mathbf{R} (\mathbf{L}_A) )) = \dim (\mathbf{R} (\mathbf{L}_{P}\mathbf{L}_{A}) ) = \dim (\mathbf{R} (\mathbf{L}_{PA})) $$

    그러므로 $\text{rank} (A) = \text{rank} (PA)$ 이다. ▲ 

    3:

    $$ \text{rank} (PAQ) = \text{rank} (AQ) = \text{rank} (A) \tag*{■} $$

!!! tldr "정리 3.4 따름정리"

    행렬의 기본행[열]연산은 랭크를 보존한다.

- 증명

    행렬에 기본행[열]연산을 적용하는 것은 정리 3.2 에 의하여 기본행렬에 대한 행렬곱을 취하는 것이다. 기본행렬은 가역이므로 정리 3.4 에 의하여 랭크가 보존된다. ■ 

- 우리는 행렬의 랭크를 보존하는 행렬연산 하나를 밝혀내었다. 따라서 랭크를 구하기 쉽게 변형된 행렬을 알아본다. 

!!! tldr "정리 3.5"

    임의의 행렬의 랭크는 일차독립인 열들의 최대 개수이다.

    행렬의 랭크는 그 열들에 의해 생성된 부분공간의 차원이다.

- 보통 행렬 $A$ 의 랭크를 구할 때 $A$ 에 기본행[열]연산을 적용하여 일차독립인 열의 개수를 구할 수 있도록 만든 다음 이 정리를 사용한다.

    기본연산을 적용하여 일차독립인 열을 어떻게 구할 수 있게 하냐면, 그냥 $0$ 인 성분이 최대한 많이 나오게 하면 된다.

    - 예시 

        행렬 $A = \begin{pmatrix} 1&2&1\\ 1&0&3\\ 1&1&2\\ \end{pmatrix} \implies \begin{pmatrix} 1&0&0\\ 0&-2&2\\ 0&-1&1\\ \end{pmatrix}$ 이므로 $\text{rank} (A) = 2$ 이다.

- 증명

    $A \in \mathbf{M}_{m \times n}(\mathbf{F} )$ 에 대하여 다음이 성립한다. 

    $$ \text{rank} (A) = \text{rank} (\mathbf{L}_{A})  = \dim (\mathbf{R} (\mathbf{L}_A) ) $$

    $\mathbf{F} ^{n}$ 의 표준 순서기저 $\beta$ 는 $\mathbf{F} ^{n}$ 를 생성한다. [정리 2.2](../LinearTransformation/#f380ab529) 에 의하여 다음이 성립한다. 

    $$ \mathbf{R} (\mathbf{L}_A) = \text{span } (\mathbf{L}_{A}(\beta ))  = \text{span } (\{\mathbf{L}_{A}(e_1, \mathbf{L}_{A}(e_2), \dots, \mathbf{L}_{A}(e_n)\}) $$

    [정리 2.13 - 2](../LinearTransformation/#546d2897f) 에 의하여 $A$ 의 $j$ 열 $a_j$ 에 대하여 $\mathbf{L}_{A}(e_j) = Ae_j = a_j$ 이다. 따라서 다음이 성립한다.
    
    $$ \text{rank} (A) = \mathbf{R} (\mathbf{L}_A) = \dim (\text{span } (\{a_1, a_2, \dots, a_n \})) \tag*{■} $$
    
- 예시 

    행렬 $A = \begin{pmatrix} 1&0&1\\ 0&1&1\\ 1&0&1\\ \end{pmatrix}$ 의 1열과 2열은 일차독립이고 3열은 두 열의 일차결합이다. 그러므로 다음이 성립한다. 

    $$ \text{rank} (A) = \dim \Bigg (\text{span } \Bigg (\Bigg \{\begin{pmatrix} 1\\ 0\\ 1\\ \end {pmatrix}, \begin{pmatrix} 0\\ 1\\ 0\\ \end{pmatrix}, \begin{pmatrix} 1\\ 1\\ 1\\ \end{pmatrix} \Bigg \}\Bigg ) \Bigg ) = 2 $$

!!! tldr ""

    행렬 $A \in \mathbf{M}_{m \times n}(\mathbf{F})$ 에 대하여 다음이 성립한다.

    $$ \text{rank} (A) = 0 \iff A = O $$

- 증명

    $\text{rank} (A) = 0$ 을 가정하면 $A$ 의 열들은 모두 서로 일차종속이다. 이는 $c_j \neq 0$ 인 $c_j$ 가 하나 이상 존재함을 의미한다. 

    $$ c_1a_1 + c_2a_2 + \dots + c_na_n = 0$$

    $$ c_ja_j = 0 \implies a_j = 0 $$



!!! tldr "정리 3.6"

    
