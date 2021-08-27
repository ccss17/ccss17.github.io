!!! info "ref"

    Stephen H. Friedberg, Linear Algebra, 4th Edition

> metadata pass

# Elementary Operation

!!! tldr "기본행[열]연산(elementary row[column] operation)"

    체 $\mathbf{F}$ 에서 성분을 가져온 $m \times n$ 행렬 $A$ 와 스칼라 $a \in \mathbf{F}$ 에 대하여 $A$ 의 행[열] 에 대한 다음 세 연산이다. 

    1. $A$ 의 두 행[열]을 교환하는 것

    2. $A$ 의 한 행[열]에 영이 아닌 스칼라 $a$ 를 곱하는 것

    3. $A$ 의 한 행[열]에 다른 행[열]의 스칼라 $a$ 배를 더하는 것

- 행연산과 열연산을 기본연산(elementary operation)이라 한다. 또한 기본연산 1), 2), 3) 을 1형(type), 2형, 3형이라 한다.

## Elementary Matrix

!!! tldr "기본행렬(elementary matrix)"

    항등행렬에 기본연산을 적용하여 얻은 행렬이다.

- $I_n$ 에 1형, 2형, 3형 연산을 하여 얻은 행렬을 각각 1형, 2형, 3형이라 한다.

- 예시 

    $I_3$ 의 1행, 2행을 교환하여 다음 기본행렬을 얻는다.

    $$ E = \begin{pmatrix} 0&1&0\\ 1&0&0\\ 0&0&1\\ \end{pmatrix} $$

!!! tldr "기본행[열]역연산(elementary row[column] inverse operation)"

    체 $\mathbf{F}$ 에서 성분을 가져온 $m \times n$ 행렬 $A$ 와 스칼라 $a \in \mathbf{F}$ 에 대하여 $A$ 의 기본행[열]연산 에 대한 다음 세 연산이다. 

    1. $A$ 의 두 행[열]을 교환하는 것

    2. $A$ 의 한 행[열]에 영이 아닌 스칼라 $\dfrac{1}{a}$ 를 곱하는 것

    3. $A$ 의 한 행[열]에 다른 행[열]의 스칼라 $-a$ 배를 더하는 것

- 교환연산은 역연산이 동일하다.

- $I_n$ 에 기본연산을 적용하여 기본행렬 $E$ 를 얻었다면, $E$ 에 기본역연산을 적용하여 다시 $I_n$ 을 얻을 수 있다.

## Properties of Elementary Operation, Elementary Matrix

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

    [행렬곱 결과가 항등행렬인 두 정사각행렬은 모두 가역](../LinearTransformation/#068bf6124)이므로 $E$ 는 가역이고, $E ^{-1} = \bar{E}$ 이다. ■ 

# Matrix Rank 

!!! tldr "행렬의 랭크(matrix rank)"

    행렬 $A \in \mathbf{M}_{m \times n}(\mathbf{F} )$ 와 $\mathbf{L}_{A} : \mathbf{F} ^{n} \to \mathbf{F} ^{m}$ 에 대하여 다음과 같이 정의한다.

    $$ \text{rank} (A) := \text{rank} (\mathbf{L}_{A}) $$

- 선형변환의 랭크에 대한 성질을 기반으로 행렬의 랭크에 대한 많은 정보를 얻을 수 있다. 

## Properties of Matrix Rank

!!! tldr ""

    $$ A \in \mathbf{M}_{n \times n}(\mathbf{F}) : A \text{ is invertible } \iff \text{rank} (A) = n $$

- 증명 

    $n \times n$ 행렬 $A$ 와 $\mathbf{L}_{A}: \mathbf{F} ^{n} \to \mathbf{F} ^{n}$ 는 [정리 2.18 따름정리 2](../LinearTransformation/#80bc2f76a) 에 의하여 $A$ 가 가역인 것과 $\mathbf{L}_{A}$ 가 가역인 것은 동치이다. [$\mathbf{L}_{A}$ 가 가역인 것과 $\text{rank} (\mathbf{L}_{A}) = \dim (\mathbf{F} ^{n}) = n$ 인 것은 동치이다](../LinearTransformation/#87356d7a4). 그러므로 행렬의 랭크의 정의에 의하여 $\text{rank} (A) = n$ 인 것과 $A$ 가 가역인 것은 동치이다. ■ 

- "$n \times n$ 가역행렬의 랭크는 $n$ 이다" 의 증명

    $A$ 가 $n \times n$ 가역행렬이면 다음이 성립한다. 

    $$ A ^{-1}A = A ^{-1}A = I_n $$

    [정리 3.4](#802aee216) 는 임의의 행렬에 가역행렬을 곱하는 것이 행렬의 랭크를 보존한다는 것을 말해준다. 이는 역으로 가역행렬이 곱해진 행렬곱에 가역행렬을 제거해도 행렬의 랭크가 보존됨을 뜻한다. 따라서 다음이 성립한다.

    $$ \text{rank} (I_n) = \text{rank} (A ^{-1}A) = \text{rank} (A) $$

    항등행렬 $I_n$ 의 랭크는 $n$ 이다. ■ 

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

    임의의 행렬의 랭크는 열들로 구성된 극대 일차독립 집합의 기수이다.

    행렬의 랭크는 그 열들에 의해 생성된 부분공간의 차원이다.

- 보통 행렬 $A$ 의 랭크를 구할 때 $A$ 에 기본행[열]연산을 적용하여 일차독립인 열의 개수를 구할 수 있도록 만든 다음 이 정리를 사용한다.

    기본연산을 적용하여 일차독립인 열을 어떻게 구할 수 있게 하냐면, 그냥 $0$ 인 성분이 최대한 많이 나오게 하면 된다.

    - 예시 

        행렬 $A = \begin{pmatrix} 1&2&1\\ 1&0&3\\ 1&1&2\\ \end{pmatrix} \implies \begin{pmatrix} 1&0&0\\ 0&-2&2\\ 0&-1&1\\ \end{pmatrix}$ 이므로 $\text{rank} (A) = 2$ 이다.

- 증명

    $A \in \mathbf{M}_{m \times n}(\mathbf{F} )$ 에 대하여 다음이 성립한다. 

    $$ \text{rank} (A) = \text{rank} (\mathbf{L}_{A})  = \dim (\mathbf{R} (\mathbf{L}_A) ) $$

    $\mathbf{F} ^{n}$ 의 표준 순서기저 $\beta$ 는 $\mathbf{F} ^{n}$ 를 생성한다. [정리 2.2](../LinearTransformation/#f380ab529) 에 의하여 다음이 성립한다. 

    $$ \mathbf{R} (\mathbf{L}_A) = \text{span} (\mathbf{L}_{A}(\beta ))  = \text{span} (\{\mathbf{L}_{A}(e_1), \mathbf{L}_{A}(e_2), \dots, \mathbf{L}_{A}(e_n)\}) $$

    [정리 2.13 - 2](../LinearTransformation/#546d2897f) 에 의하여 $A$ 의 $j$ 열 $a_j$ 에 대하여 $\mathbf{L}_{A}(e_j) = Ae_j = a_j$ 이다. 따라서 다음이 성립한다.
    
    $$ \text{rank} (A) = \dim (\mathbf{R} (\mathbf{L}_A)) = \dim (\text{span} (\{a_1, a_2, \dots, a_n \})) \tag*{■} $$
    
- 예시 

    행렬 $A = \begin{pmatrix} 1&0&1\\ 0&1&1\\ 1&0&1\\ \end{pmatrix}$ 의 1열과 2열은 일차독립이고 3열은 두 열의 일차결합이다. 그러므로 다음이 성립한다. 

    $$ \text{rank} (A) = \dim \Bigg (\text{span} \Bigg (\Bigg \{\begin{pmatrix} 1\\ 0\\ 1\\ \end {pmatrix}, \begin{pmatrix} 0\\ 1\\ 0\\ \end{pmatrix}, \begin{pmatrix} 1\\ 1\\ 1\\ \end{pmatrix} \Bigg \}\Bigg ) \Bigg ) = 2 $$

!!! tldr ""

    행렬 $A \in \mathbf{M}_{m \times n}(\mathbf{F})$ 에 대하여 다음이 성립한다.

    $$ \text{rank} (A) = 0 \iff A = O $$

- 증명

    $\text{rank} (A) = 0$ 을 가정하자. $A$ 의 $j$ 번째 열벡터 $a_j$ 에 대하여 $a_j \neq 0$ 이면 스칼라 $c$ 에 대하여 $ca_j = 0$ 가 되기 위해서는 반드시 $c = 0$ 이어야 한다. 그러면 일차독립의 정의에 의하여 집합 $\{a_j\}$ 은 일차독립이다. 그러나 정리 3.5 에 의하여 [극대 일차독립 집합의 기수](../VectorSpace/#c298b6300)가 $0$ 이므로 이는 모순이다. 따라서 $a_j = 0$ 이다. 이는 $A = O$ 임을 뜻한다. ▲  

    $A = O$ 을 가정하면 극대 일차독립 집합이 공집합이므로 $\text{rank} (A) = 0$ 이 바로 나온다. ■ 
    
## Finding Matrix Rank

!!! tldr ""

    다음 행렬 $B$ 에 대하여 $\text{rank} (B) = r \implies \text{rank} (B') = r-1$ 이다.

    $$ B = \left(\begin{array}{c|ccc} 1 & 0 & \dots & 0 \\ \hline 0 & & & \\ \vdots  & & B' & \\ 0 & & & \\ \end{array}\right) $$

- 증명

    다음과 같은 행렬 $B$ 의 1열은 다른 1열의 일차결합으로 표현될 수 없으므로 극대 일차독립 집합에 포함된다. 

    $$ B = \begin{pmatrix} 1&0&\dots&0\\ 0&B_{22}&\dots&B_{2n}\\ \vdots& \vdots& \ddots& \vdots \\ 0&B_{n2}&\dots&B_{nn}\\ \end{pmatrix} $$

    따라서 행렬 $B$ 의 랭크는 다음 행렬 $B'$ 의 극대 일차독립 집합의 기수에 $1$ 을 더한 것이다. 즉, $1 + \text{rank} (B') = \text{rank} (B)$ 이다.

    $$ B' = \begin{pmatrix} B_{22}&\dots&B_{2n}\\ \vdots& \ddots& \vdots \\ B_{n2}&\dots&B_{nn}\\ \end{pmatrix} $$

    그러므로 $\text{rank} (B) = r \implies \text{rank} (B') = r-1$ 이다.

!!! tldr ""

    다음과 같은 $m \times n$ 행렬 $B'$ 와 $D$, 그리고 $(m + 1) \times (n + 1)$ 행렬 $B$ 와 $D$ 에 대하여 $B'$ 에 기본연산을 유한 번 적용하여 그것을 $D'$ 로 변환할 수 있으면, $B$ 에 기본연산을 유한 번 적용하여 그것을 $D$ 로 변환할 수 있다.

    $$ B = \left(\begin{array}{c|ccc} 1 & 0 & \dots & 0 \\ \hline 0 & & & \\ \vdots & & B' & \\ 0 & & & \\ \end{array}\right), D = \left(\begin{array}{c|ccc} 1 & 0 & \dots & 0 \\ \hline 0 & & & \\ \vdots & & D' & \\ 0 & & & \\ \end{array}\right) $$

- 증명

    $B'$ 를 $D'$ 로 바꾸는 기본연산을 $B$ 에 동일하게 적용해도 $B$ 의 1행과 1열은 각각 보존된다. 그러므로 $B$ 에 기본연산을 유한번 적용하여 $D$ 로 변환할 수 있다.

    더 나아가서 그 기본연산은 $B'$ 을 $D'$ 으로 변환시키는 기본연산과 같다.

!!! tldr "정리 3.6"

    $A \in \mathbf{M}_{m \times n}$ 에 대하여 $\text{rank} (A) = r$ 이면 다음이 성립한다.

    1. $r \leq m, r \leq n$

    2. 유한 번의 기본행[열]연산으로 항등행렬 $I_r$ 영행렬 $O_1, O_2, O_3$ 에 대하여 $A$ 를 행렬 $D = \begin{pmatrix} I_r&O_1\\ O_2&O_3\\ \end{pmatrix}$ 로 바꿀 수 있다.

    3. $\text{rank} (A) = \text{rank} (D)$

- 지금 정리 3.5 로부터 계속 하고 있는 일은 행렬의 랭크를 쉽게 구할 수 있도록 행렬의 랭크를 보존하면서 변형시킬 수 있는 방법들을 정리하는 것이다.

- 다음 예시는 $A$ 를 $D$ 로 변형시키는 과정이 먼저 1행을 항등행렬의 1행과 같이 만들고, 2행을 항등행렬의 2행과 같이 만들기를 반복하는 것임을 말해준다.

- 예시 

    다음과 같은 행렬 $A$ 를 $D$ 로 변형시켜보자. 

    $$ A = \begin{pmatrix} 0&2&4&2&2\\ 4&4&4&8&2\\ 8&2&0&10&2\\ 6&3&2&9&1\\ \end{pmatrix} $$

    다음은 $A$ 에 기본행[열]연산을 계속 적용하여 $D$ 를 얻는 과정을 보여준다.

    $$ \begin{pmatrix} 0&2&4&2&2\\ 4&4&4&8&2\\ 8&2&0&10&2\\ 6&3&2&9&1\\ \end{pmatrix} \to \begin{pmatrix} 4&4&4&8&2\\ 0&2&4&2&2\\ 8&2&0&10&2\\ 6&3&2&9&1\\ \end{pmatrix} \to \begin{pmatrix} 1&1&1&2&0\\ 0&2&4&2&2\\ 8&2&0&10&2\\ 6&3&2&9&1\\ \end{pmatrix} \to \begin{pmatrix} 1&1&1&2&0\\ 0&2&4&2&2\\ 0&-6&-8&-6&2\\ 0&-3&-4&-3&1\\ \end{pmatrix} \to $$

    $$ \begin{pmatrix} 1&0&0&0&0\\ 0&2&4&2&2\\ 0&-6&-8&-6&2\\ 0&-3&-4&-3&1\\ \end{pmatrix} \to \begin{pmatrix} 1&0&0&0&0\\ 0&1&2&1&1\\ 0&-6&-8&-6&2\\ 0&-3&-4&-3&1\\ \end{pmatrix} \to \begin{pmatrix} 1&0&0&0&0\\ 0&1&2&1&1\\ 0&0&4&0&8\\ 0&0&2&0&4\\ \end{pmatrix} \to \begin{pmatrix} 1&0&0&0&0\\ 0&1&0&0&0\\ 0&0&4&0&8\\ 0&0&2&0&4\\ \end{pmatrix} \to $$

    $$ \begin{pmatrix} 1&0&0&0&0\\ 0&1&0&0&0\\ 0&0&1&0&2\\ 0&0&2&0&4\\ \end{pmatrix} \to \begin{pmatrix} 1&0&0&0&0\\ 0&1&0&0&0\\ 0&0&1&0&2\\ 0&0&0&0&0\\ \end{pmatrix} \to \begin{pmatrix} 1&0&0&0&0\\ 0&1&0&0&0\\ 0&0&1&0&0\\ 0&0&0&0&0\\ \end{pmatrix} = D $$

    그러면 [정리 3.4 따름정리](#108500177)로부터 $\text{rank} (A) = \text{rank} (D) = 3$ 이다.

- 증명

    [$A = O$ 이면 $r = 0$](#4f37a0785) 이므로 $D = A$ 가 되고 더 이상 증명할 것이없다. ▲ 

    $A \neq O$ 일 때 $r = \text{rank} (A) > 0$ 이다. $A$ 의 행의 개수 $m$ 에 대하여 수학적 귀납법을 사용하자. 

    $m = 1$ 일 때 $A_{11} \neq 0$ 일 경우 기본열연산 2형으로 $A_{11} \to 1$ 로 만들 수 있다. $A_{11} = 0$ 일 경우 기본열연산 1형과 2형으로 $A_{11} \to 1$ 로 만들 수 있다. 그러면 기본열연산 3형을 통하여 $A$ 를 다음과 같이 만들 수 있다.

    $$ A \to \begin{pmatrix} 1&0&\dots&0\\ \end{pmatrix} = D = \begin{pmatrix} I_1&O_1\\ \end{pmatrix} $$

    [정리 3.4 따름정리](#108500177) 와 [정리 3.5](#0ce821e3f) 에 의하여 $\text{rank} (A) = 1$ 이다. ▲ 

    $m > 1$ 일 때 $m - 1$ 에 대하여 성립한다는 것을 가정하자. $A$ 가 $m \times  m$ 행렬이라고 하자. $n = 1$ 이면 $m = 1$ 일 때의 증명과 비슷하게 증명이 끝난다. ▲ 

    $n > 1$ 을 가정하자. $A \neq O$ 이므로 어떤 $i, j$ 에 대하여 $A _{ij} \neq 0$ 이다. 따라서 기본행연산 1형과 기본열연산 1형을 최대 한 번 적용하여 1행 1열을 $0$ 이 아닌 성분으로 만들 수 있다. 그러므로 기본연산 2형을 통하여 1행 1열의 성분을 $1$ 로 만들 수 있다. 

    그러면 기본행연산 3형과 기본열연산 3형을 통하여 1행과 1열에서 1행 1열 성분을 제외하고 모두 다 $0$ 으로 만들 수 있다. 즉, $A \neq O$ 에 기본연산을 유한번 적용하여 다음 행렬 $B$ 를 얻는다. 
    
    $$ B = \left(\begin{array}{c|ccc} 1 & 0 & \dots & 0 \\ \hline 0 &   & & \\ \vdots  & & B' & \\ 0 & & & \\ \end{array}\right) $$

    그러면 [$\text{rank} (B') = \text{rank} (B) - 1 = \text{rank} (A) - 1 = r - 1$ 이다](#fa846233d). 
    
    $m - 1$ 에 대하여 본 정리가 성립한다는 가정에 의하여 $r - 1 \leq m - 1, r - 1 \leq n - 1$ 이므로 $r \leq m, r \leq n$ 이다.

    $m - 1$ 에 대하여 본 정리가 성립한다는 가정에 의하여 $(m - 1) \times (n - 1)$ 행렬인 $B'$ 에 대하여 본 정리가 성립하므로 $B'$ 를 영행령 $O_4, O_5, O_6$ 에 대하여 다음과 같은 행렬로 바꿀 수 있다. 

    $$ D' = \begin{pmatrix} I _{r-1} & O_4\\ O_5 & O_6\\ \end{pmatrix} $$

    이때 행렬 $D$ 를 다음과 같이 두자. 

    $$ D = \left(\begin{array}{c|ccc} 1 & 0 & \dots & 0 \\ \hline 0 & & & \\ \vdots & & D' & \\ 0 & & & \\ \end{array}\right) $$

    $B$ 에 기본연산을 유한번 적용하여 $D$ 를 얻을 수 있다면 증명이 끝난다. 본 정리가 $m - 1$ 에 대해서는 성립하므로 [$B'$ 에 기본연산을 유한 번 적용하여 그것을 $D'$ 으로 바꿀 수 있다. 그러므로 $B$ 에 기본연산을 유한번 적용하여 $D$ 로 바꿀 수 있다](#bb65cc453).

    $A$ 에 기본연산을 적용하여 그것을 $B$ 로 변환할 수 있으므로 결국 $A$ 에 기본연산을 적용하여 그것을 $D$ 로 바꿀 수 있다. ▲ 

    3) 은 [정리 3.4 따름정리](#108500177) 에서 바로 나온다. ■ 

!!! tldr "정리 3.6 따름정리 1"

    $A \in \mathbf{M}_{m \times n}, \text{rank} (A) = r$ 인 행렬 $A$ 에 대하여 다음을 만족하는 $m \times m$ 가역행렬 $B$ 와 $n \times n$ 가역행렬 $C$ 가 존재한다. 

    $$ D = \begin{pmatrix} I_r&O_1\\ O_2&O_3\\ \end{pmatrix} = BAC $$

- 증명

    정리 3.6 은 $A$ 에 기본연산을 적용하여 그것을 $D$ 로 변환시킬 수 있음을 말해준다. 이때 [정리 3.1](#1c860f354) 에 의하여 기본행연산은 $A$ 의 우측에 곱해지는 행렬곱으로, 기본열연산은 $A$ 의 좌측에 곱해지는 행렬곱으로 표현가능하다. 즉, $m \times m$ 기본행렬 $E_1, E_2, \dots, E_p$ 와 $n \times n$ 기본행렬 $G_1, G_2, \dots, G_q$ 에 대하여 다음이 성립한다. 

    $$ D = E_p E _{p-1} \dots E_2 E_1 A G_1 G_2 \dots G_q $$

    [문제 2.4 - 4](../LinearTransformation/#843e52544) 에 의하여 다음과 같은 행렬 $B, C$ 는 가역이다.

    $$ B = E_p E _{p-1} \dots E_2 E_1 $$

    $$ C = G_1 G_2 \dots G_q $$

    또한 $D = BAC$ 이다. ■ 

!!! tldr "정리 3.6 따름정리 2"

    $m \times n$ 행렬 $A$ 에 대하여 다음이 성립한다.

    1. $\text{rank} (A ^{t}) = \text{rank} (A)$

    2. 임의의 행렬의 랭크는 행들로 구성된 극대 일차독립 집합의 기수이다. 행렬의 랭크는 그 행에 의해 생성된 부분공간의 차원이다.

    3. 임의의 행렬의 행과 열은 차원이 같은 부분공간을 생성한다. 차원은 행렬의 랭크와 같다.

- 증명

    정리 3.6 따름정리 1 에 의하여 $D = BAC$ 인 가역행렬 $B, C$ 가 존재한다. 이 행렬의 전치는 다음과 같다. 

    $$ D ^{t} = (BAC) ^{t} = C ^{t}A ^{t}B ^{t} $$

    [문제 2.4-5](../LinearTransformation/#a3809d4dc) 에 의하여 $B ^{t}, C ^{t}$ 는 가역이다. [정리 3.4](#802aee216) 에 의하여 다음이 성립한다. 

    $$ \text{rank} (A ^{t}) = \text{rank} (C ^{t}A ^{t}B ^{t}) = \text{rank} (D ^{t}) $$

    $\text{rank} (A) = r$ 이라고 하자. $D ^{t}$ 는 $n \times m$ 행렬로써 $D$ 의 전치이므로 영행렬 $O, O', O''$ 에 대하여 다음의 꼴이다.

    $$ D ^{t} = \begin{pmatrix} I_r&O\\ O'&O''\\ \end{pmatrix} $$

    정리 3.6 에 의하여 $\text{rank} (A) = r = \text{rank} (D)$ 인데 $D$ 의 전치는 $I_r$ 을 보존하므로 [정리 3.5](#0ce821e3f) 에 의하여 $\text{rank} (D) = \text{rank} (D ^{t})$ 이다. 따라서 다음이 성립한다. 

    $$ \text{rank} (A ^{t}) = \text{rank} (D ^{t}) = r = \text{rank} (A) $$

    이로써 1) 이 증명되었다. ▲ 

    2) 는 행렬의 열에 대한 극대 일차독립 집합에 대한 [정리 3.5](#0ce821e3f) 를 단지 행에 대한 극대 일차독립 집합에 대한 명제로 바꾼 것이다. 정리 3.5 와 1) 이 참이라면 2) 는 1) 에서 바로 나온다. ▲ 

    3) 은 정리 3.5 와 2) 에서 바로 나온다. ■ 

!!! tldr "정리 3.6 따름정리 3"

    가역행렬은 기본행렬의 곱이다.

- 증명

    $n \times n$ 가역행렬 $A$ 의 랭크는 $n$ 이다. 정리 3.6 따름정리 1 은 $A$ 를 $D$ 로 변환했을 때 $D = I_n$ 임을 말해준다. 그러면 $I_n = BAC$ 인 가역행렬 $B, C$ 가 존재한다.

    정리 3.6 따름정리 1 의 증명과정에 의하면 가역행렬 $B, C$ 은 다음과 같은 기본행렬의 곱이다.

    $$ B = E_p E _{p-1} \dots E_2 E_1 $$

    $$ C = G_1 G_2 \dots G_q $$

    따라서 $A = B ^{-1}I_n C ^{-1} = B ^{-1}C ^{-1}$ 이고, [문제 2.4-4](../LinearTransformation/#e53147e37) 에 의하여 다음이 성립한다. 

    $$ A = E_1 ^{-1} E _2  ^{-1}\dots E_p  ^{-1} G_q ^{-1} G _{q-1}  ^{-1}\dots G_1  ^{-1} $$

    [정리 3.2](#c576bf96c) 에 의하여 기본행렬의 역행렬도 기본행렬이다. 그러므로 $A$ 는 기본행렬의 곱이다. ■ 

## Rank of Matrix Multiplication

!!! tldr "정리 3.7"

    유한차원 벡터공간 $\mathbf{V} , \mathbf{W} , \mathbf{Z}$ 사이에 정의 된 선형변환 $\mathbf{T} : \mathbf{V} \to \mathbf{W} , \mathbf{U} : \mathbf{W} \to \mathbf{Z}$ 와 행렬곱 $AB$ 이 정의된 두 행렬 $A, B$ 에 대하여 다음이 성립한다. 

    1. $\text{rank} (\mathbf{U} \mathbf{T} ) \leq \text{rank} (\mathbf{U} )$

    2. $\text{rank} (\mathbf{U} \mathbf{T} ) \leq \text{rank} (\mathbf{T} )$

    3. $\text{rank} (AB ) \leq \text{rank} (A)$

    4. $\text{rank} (AB ) \leq \text{rank} (B)$

- 이제 [정리 3.4 따름정리](#108500177), [정리 3.5](#0ce821e3f), [정리 3.6](#71b0f55b7), [정리 3.6 따름정리 2](#a2df8a4e7) 을 기반으로 임의의 행렬의 랭크를 쉽게 구할 수 있는 많은 도구들이 마련되었다.

    이 도구들을 통하여 기본연산을 행렬에 적용하여 $0$ 을 최대한 많이 가지도록 변형시키고 그 행렬의 극대 일차독립 집합의 기수를 파악하면 랭크를 쉽게 구할 수 있다. 

    - 예시 

        행렬 $A = \begin{pmatrix} 1&2&1&1\\ 1&1&-1&1\\ \end{pmatrix}$ 의 1행과 2행의 집합은 일차독립이므로 $\text{rank} (A) = 2$ 이다.
    
    - 예시 

        행렬 $A = \begin{pmatrix}
        1&2&3&1\\
        2&1&1&1\\
        1&-1&1&0\\
        \end{pmatrix}$ 에 기본연산을 적용하여 다음과 같이 변형할 수 있다.

        $$ A \to \begin{pmatrix} 1&2&3&1\\ 0&-3&-5&-1\\ 0&-3&-2&-1\\ \end{pmatrix} \to \begin{pmatrix} 1&2&3&1\\ 0&-3&-5&-1\\ 0&0&3&0\\ \end{pmatrix} $$

        3개의 행이 일차독립이므로 $\text{rank} (A) = 3$ 이다.
    
    위 예시에서 알 수 있듯이 굳이 [정리 3.6](#71b0f55b7) 이 말하는 $D = \begin{pmatrix} I&O\\ O&O\\ \end{pmatrix}$ 을 얻을 때까지 기본연산을 하는 것이 아니라 일차독립인 행 또는 열들의 최대 갯수가 명확히 보일 때까지 기본연산을 해도 된다.

- 증명

    1:

    $\mathbf{R} (\mathbf{T}) \subseteq \mathbf{W}$ 이므로 다음이 성립한다. 

    $$ \mathbf{R} (\mathbf{U}\mathbf{T} ) = \mathbf{U} \mathbf{T} (\mathbf{V} ) = \mathbf{U} (\mathbf{T} (\mathbf{V} )) = \mathbf{U} (\mathbf{R} (\mathbf{T}) ) \subseteq \mathbf{U} (\mathbf{W} ) = \mathbf{R} (\mathbf{U}) $$

    따라서 $\text{rank} (\mathbf{U} \mathbf{T} )$ 는 다음과 같다. 

    $$ \text{rank} (\mathbf{U} \mathbf{T} )  = \dim (\mathbf{R} (\mathbf{U}\mathbf{T} ) )\leq \dim (\mathbf{R} (\mathbf{U}) ) = \text{rank} (\mathbf{U} ) $$

    3:

    이제 1) 을 가정할 수 있으므로 $\text{rank} (AB)$ 는 다음과 같다. 

    $$ \text{rank} (AB) = \text{rank} (\mathbf{L}_{AB})  = \text{rank} (\mathbf{L}_{A}\mathbf{L}_{B})  \leq \text{rank} (\mathbf{L}_{A}) = \text{rank} (A) $$

    4:

    이제 3) 을 가정할 수 있으므로 3) 과 [정리 3.6 따름정리 2](#a2df8a4e7) 에 의하여 다음이 성립한다. 

    $$ \text{rank} (AB) = \text{rank} ((AB)^{t})  = \text{rank} (B ^{t}A ^{t})  \leq \text{rank} (B ^{t})  = \text{rank} (B) $$

    2:

    이제 4) 를 가정할 수 있다.

    $\mathbf{V} , \mathbf{W} , \mathbf{Z}$ 의 순서기저 $\alpha , \beta , \gamma$ 에 대하여 $A' = [\mathbf{U} ]^{\gamma}_{\beta} , B' = [\mathbf{T} ] ^{\beta }_{\alpha }$ 라 하면 [정리 2.11](../LinearTransformation/#2fc8f26aa) 에 의하여 $A'B' = [\mathbf{U} \mathbf{T} ] ^{\gamma}_{\alpha }$ 이다. 

    [정리 3.3](#af5c5b8cd) 과 4) 에 의하여 다음이 성립한다. 

    $$ \text{rank} (\mathbf{U} \mathbf{T} )  = \text{rank} (A'B')  \leq \text{rank} (B') = \text{rank} (\mathbf{T} ) \tag*{■} $$

# Finding Inverse Matrix

!!! tldr "첨가행렬(augmented matrix)"

    $m \times n$ 행렬 $A$ 와 $m \times p$ 행렬 $B$ 에 대한 첨가행렬 $(A|B)$ 는 $m \times (n + p)$ 행렬 $(AB)$ 이다.

    $(AB)$ 는 처음 $n$ 개 열이 $A$ 의 열이고, 나머지 $p$ 개 열이 $B$ 의 열인 행렬이다.

!!! tldr "문제 3.2-15"

    $n$ 개의 행을 가지는 행렬 $A, B$ 와 $m \times n$ 행렬 $M$ 에 대하여 다음이 성립한다. 

    $$ M(A|B) = (MA|MB) $$

- 증명

    $A$ 의 열을 $p$, $B$ 의 열을 $q$ 라고 하면 $A$ 는 $n \times p$ 행렬, $B$ 는 $n \times q$ 행렬이다. 
    
    또한 $(A|B)$ 는 $n \times (p + q)$ 행렬, $M(A|B)$ 는 $m \times (p + q)$ 행렬이다. 다음이 성립한다.

    $$ \begin{equation}\begin{split} M(A|B)&= \begin{pmatrix} M_{11}&M_{12}&\dots&M_{1n}\\ M_{21}&M_{22}&\dots&M_{2n}\\ \vdots& \vdots& \ddots& \vdots \\ M_{m1}&M_{m2}&\dots&M_{mn}\\ \end{pmatrix} \left(\begin{array}{cccc|cccc} A_{11} & A_{12} & \dots & A_{1p} & B_{11} & B_{12} & \dots & B_{1q} \\ A_{21} & A_{22} & \dots & A_{2p} & B_{21} & B_{22} & \dots & B_{2q} \\ \vdots & \vdots & \ddots & \vdots & \vdots& \vdots& \ddots& \vdots \\ A_{n1} & A_{n2} & \dots & A_{np} & B_{n1} & B_{n2} & \dots & B_{nq} \\ \end{array}\right) \\ &= \begin{pmatrix} \sum_{i=1}^{n}M_{1i}A_{i1}& \dots& \sum_{i=1}^{n}M_{1i}A_{ip}& \sum_{i=1}^{n}M_{1i}B_{i1}& \dots& \sum_{i=1}^{n}M_{1i}B_{iq}& \\ \sum_{i=1}^{n}M_{2i}A_{i1}& \dots& \sum_{i=1}^{n}M_{2i}A_{ip}& \sum_{i=1}^{n}M_{2i}B_{i1}& \dots& \sum_{i=1}^{n}M_{2i}B_{iq}& \\ \vdots& \ddots& \vdots& \vdots & \ddots & \vdots& \\ \sum_{i=1}^{n}M_{mi}A_{i1}& \dots& \sum_{i=1}^{n}M_{mi}A_{ip}& \sum_{i=1}^{n}M_{mi}B_{i1}& \dots& \sum_{i=1}^{n}M_{mi}B_{iq}& \\ \end{pmatrix} \end{split}\end{equation} \tag*{} $$

    $m \times p$ 행렬 $MA$ 와 $m \times q$ 행렬 $MB$ 는 다음과 같다.

    $$ \begin{equation}\begin{split} MA &= \begin{pmatrix} M_{11}&M_{12}&\dots&M_{1n}\\ M_{21}&M_{22}&\dots&M_{2n}\\ \vdots& \vdots& \ddots& \vdots \\ M_{m1}&M_{m2}&\dots&M_{mn}\\ \end{pmatrix} \begin{pmatrix} A_{11}&A_{12}&\dots&A_{1p}\\ A_{21}&A_{22}&\dots&A_{2p}\\ \vdots& \vdots& \ddots& \vdots \\ A_{n1}&A_{n2}&\dots&A_{np}\\ \end{pmatrix} \\ &= \begin{pmatrix} \sum_{i=1}^{n}M_{1i}A_{i1}& \dots& \sum_{i=1}^{n}M_{1i}A_{ip} \\ \sum_{i=1}^{n}M_{2i}A_{i1}& \dots& \sum_{i=1}^{n}M_{2i}A_{ip} \\ \vdots& \ddots& \vdots& \\ \sum_{i=1}^{n}M_{mi}A_{i1}& \dots& \sum_{i=1}^{n}M_{mi}A_{ip}\\ \end{pmatrix} \end{split}\end{equation} \tag*{} $$

    $$ \begin{equation}\begin{split} MB &=  \begin{pmatrix} M_{11}&M_{12}&\dots&M_{1n}\\ M_{21}&M_{22}&\dots&M_{2n}\\ \vdots& \vdots& \ddots& \vdots \\ M_{m1}&M_{m2}&\dots&M_{mn}\\ \end{pmatrix} \begin{pmatrix} B_{11}&B_{12}&\dots&B_{1q}\\ B_{21}&B_{22}&\dots&B_{2q}\\ \vdots& \vdots& \ddots& \vdots \\ B_{n1}&B_{n2}&\dots&B_{nq}\\ \end{pmatrix} \\ &= \begin{pmatrix} \sum_{i=1}^{n}M_{1i}B_{i1}& \dots& \sum_{i=1}^{n}M_{1i}B_{iq} \\ \sum_{i=1}^{n}M_{2i}B_{i1}& \dots& \sum_{i=1}^{n}M_{2i}B_{iq} \\ \vdots& \ddots& \vdots& \\ \sum_{i=1}^{n}M_{mi}B_{i1}& \dots& \sum_{i=1}^{n}M_{mi}B_{iq}\\ \end{pmatrix} \end{split}\end{equation} \tag*{} $$

    따라서 다음이 성립한다.

    $$ M(A|B) = (MA|MB) \tag*{■} $$

!!! tldr ""

    $n \times n$ 가역행렬 $A$ 와 첨가행렬 $(A|I_n)$ 에 대하여 다음이 성립한다.
    
    1. $(A|I_n)$ 에 유한 번의 기본행연산을 적용하여 첨가행렬 $(I_n|B)$ 을 얻을 수 있다면, $A$ 의 역행렬이 존재하고 $B = A ^{-1}$ 이다.

    2. $(A|I_n)$ 에 유한 번의 기본행연산을 적용하여 첨가행렬 $(I_n|B)$ 을 얻을 수 없다면, $A$ 의 역행렬이 존재하지 않고 처음 $n$ 개의 성분이 모두 $0$ 인 행을 가진 행렬을 얻는다. 

- 증명

    1:

    $n \times n$ 가역행렬 $A$ 에 대하여 $n \times 2n$ 첨가행렬 $C = (A|I_n)$ 을 가정하자. [문제 3.2-15]() 에 의하여 다음이 성립한다. 

    $$ A ^{-1}C = (A ^{-1}A|A ^{-1}I_n) = (I_n | A ^{-1}) $$

    [정리 3.6 따름정리 3](#18150efeb) 에 의하여 $A ^{-1}$ 은 기본행렬의 곱이다. $A ^{-1} = E_p \dots E_1$ 으로 두면 다음이 성립한다. 

    $$ A ^{-1}C = E_p \dots E_1 C = E_p \dots E_1 (A|I_n) = (I_n | A ^{-1}) $$

    기본행렬을 좌측에 곱하는 것은 기본행연산을 적용하는 것이므로 이 결과를 다음과 같이 정리할 수 있다. 

    **$A$ 가 $n \times n$ 가역행렬이면 행렬 $(A|I_n)$ 에 기본행연산을 유한 번 적용하여 $(I_n|A ^{-1})$ 으로 변형할 수 있다.** ▲ 

    역으로 가역행렬 $A$ 에 대하여 $(A|I_n)$ 에 기본행연산을 유한 번 적용하여 $(I_n|B)$ 로 변형할 수 있는 $n \times n$ 행렬 $B$ 가 존재한다고 하면, [정리 3.1](#1c860f354) 에 의하여 기본행연산들을 기본행렬 $E_1, \dots, E_p$ 로 나타낼 수 있으므로 다음이 성립한다. 

    $$ E_p \dots E_1 (A|I_n) = (I_n | B) $$

    $M = E_p \dots E_1$ 로 두면 [문제 3.2-15]() 에 의하여 다음이 성립한다. 

    $$ M(A|I_n) = (MA|M) = (I_n | B) $$

    따라서 [$MA = I_n, M = B$ 이므로 $M = B = A ^{-1}$](../LinearTransformation/#068bf6124) 이다. 이 결과를 다음과 같이 정리할 수 있다. 

    **$n \times n$ 가역행렬 $A$ 에 대하여 첨가행렬 $(A|I_n)$ 에 기본행연산을 유한번 적용하여 $(I_n|B)$ 로 변형할 수 있으면 $B = A ^{-1}$ 이다.** ■ 

    2:

    [$A$ 가 가역이 아니면 $\text{rank} (A) < n$ 이다](#f94f2d598). 또한 기본행연산으로 $(A|I_n)$ 을 $(I_n|B)$ 로 변형할 수 없다. [기본행연산은 행렬의 랭크를 보존하므로](#108500177) $\text{rank} (A) = n$ 이 되는데 이는 모순이기 때문이다. 이때 $A$ 를 변형하면 모든 성분이 $0$ 인 행을 포함하는 행렬을 얻는다. 

    아래의 예시를 살펴보자. 

- 예시 

    행렬 $A = \begin{pmatrix} 0&2&4\\ 2&4&2\\ 3&3&1\\ \end{pmatrix}$ 에 대하여 $(A|I_n)$ 을 $(I_n|A ^{-1})$ 로 변형시켜보자. 

    $$ \begin{pmatrix} 0&2&4&1&0&0\\ 2&4&2&0&1&0\\ 3&3&1&0&0&1\\ \end{pmatrix} \to \begin{pmatrix} 2&4&2&0&1&0\\ 0&2&4&1&0&0\\ 3&3&1&0&0&1\\ \end{pmatrix} \to \begin{pmatrix} 1&2&1&0&\frac{1}{2}&0\\ 0&2&4&1&0&0\\ 3&3&1&0&0&1\\ \end{pmatrix} \to $$ 

    $$ \begin{pmatrix} 1&2&1&0&\frac{1}{2}&0\\ 0&2&4&1&0&0\\ 0&-3&-2&0&-\frac{3}{2}&1\\ \end{pmatrix} \to \dots \to \begin{pmatrix} 1&0&0&\frac{1}{8}&-\frac{1}{8}&\frac{3}{4}\\ 0&1&0&-\frac{1}{4}&\frac{3}{4}&-\frac{1}{2}\\ 0&0&1&\frac{3}{8}&-\frac{3}{8}&\frac{1}{4}\\ \end{pmatrix} $$

    따라서 $A$ 의 역행렬은 다음과 같다. 

    $$ A ^{-1} = \begin{pmatrix} \frac{1}{8}&-\frac{1}{8}&\frac{3}{4}\\ -\frac{1}{4}&\frac{3}{4}&-\frac{1}{2}\\ \frac{3}{8}&-\frac{3}{8}&\frac{1}{4}\\ \end{pmatrix} $$

- 예시 

    행렬 $A = \begin{pmatrix} 1&2&1\\ 2&1&-1\\ 1&5&4\\ \end{pmatrix}$ 에 대하여 $(A|I_n)$ 을 $(I_n|A ^{-1})$ 로 변형시켜보자. 

    $$ \begin{pmatrix} 1&2&1&1&0&0\\ 2&1&-1&0&1&0\\ 1&5&4&0&0&1\\ \end{pmatrix} \to \dots \to \begin{pmatrix} 1&2&1&1&0&0\\ 0&-3&-3&-2&1&0\\ 0&0&0&-3&1&1\\ \end{pmatrix} $$ 

    마지막 행렬의 3행의 앞쪽 $n = 3$ 개의 성분이 모두 $0$ 인 행을 가진 행렬을 얻었다. 따라서 $A$ 의 역행렬은 존재하지 않는다.

- 이 정리로써 행렬이 가역인지 판단하고, 가역이면 역행렬을 구할 수 있다. 그런데 [정리 2.18](../LinearTransformation/#b7bc62d0d) 로써 선형변환의 가역성과 행렬의 가역성이 연결되었었다. 따라서 이 정리를 기반으로 선형변환의 가역성과 역변환도 밝힐 수 있다.

    - 예시 

        선형변환 $\mathbf{T} : \mathbf{P}_{2}(\R) \to \mathbf{P}_{2}(\R)$ 이 다음과 같이 정의되었다고 하자. 

        $$ \mathbf{T} (f(x)) = f(x) + f'(x) + f''(x) $$

        $\mathbf{P}_{2}(\R)$ 의 표준 순서기저를 $\beta = \{1, x, x ^{2}\}$ 라고 하면 [선형변환의 행렬표현](../LinearTransformation/#c16bc5e5b) 에 의하여 다음이 성립한다.

        $$ f(1) = 1 = 1 \cdot 1 + 0 \cdot x + 0 \cdot x ^{2} $$

        $$ f(x) = 1 = 1 \cdot 1 + 1 \cdot x + 0 \cdot x ^{2} $$

        $$ f(x ^{2}) = 1 = 2 \cdot 1 + 2 \cdot x + 1 \cdot x ^{2} $$

        $$ [\mathbf{T} ]_{\beta } = \begin{pmatrix} 1&1&2\\ 0&1&2\\ 0&0&1\\ \end{pmatrix} $$

        본 정리의 방법을 사용하여 $([\mathbf{T} ] _{\beta }|I_3)$ 를 $(I_3 | ([\mathbf{T} ]_{\beta } )^{-1})$ 으로 변형하면 다음을 얻는다.

        $$ ([\mathbf{T} ]_{\beta }) ^{-1} = \begin{pmatrix} 1&-1&0\\ 0&1&-2\\ 0&0&1\\ \end{pmatrix} $$

        즉, $([\mathbf{T} ]_{\beta }) ^{-1}$ 는 가역이다. 그러면 [정리 2.18 따름정리 1](../LinearTransformation/#b7bc62d0d) 에 의하여 $\mathbf{T}$ 도 가역이고 $([\mathbf{T} ]_{\beta }) ^{-1} = [\mathbf{T} ^{-1}] _{\beta }$ 이다.

        그러면 스칼라 $a_0, a_1, a_2$ 와 [정리 2.14](../LinearTransformation/#93b3bc7a2) 에 의하여 다음을 얻는다. 

        $$ [\mathbf{T} ^{-1}(a_0 + a_1x + a_2 x ^{2})] _{\beta } = \begin{pmatrix} 1&-1&0\\ 0&1&-2\\ 0&0&1\\ \end{pmatrix} \begin{pmatrix} a_0\\ a_1\\ a_2\\ \end{pmatrix} = \begin{pmatrix} a_0-a_1\\ a_1-2a_2\\ a_2\\ \end{pmatrix} $$

        따라서 다음과 같이 $\mathbf{T}$ 의 역변환까지 알 수 있다.

        $$ \mathbf{T} ^{-1}(a_0 + a_1x + a_2x ^{2}) = (a_0 - a_1) + (a_1 - 2a_2)x + a_2 x ^{2} $$

!!! tldr ""

    $u, v \in \mathbf{F} ^{2}$ 에 대한 $\{u, v\}$ 와 행렬 $\begin{pmatrix} u\\ v\\ \end{pmatrix}$ 에 대하여 다음이 성립한다.

    1. $\{u, v\}$ 가 일차독립이면 행렬 $\begin{pmatrix} u\\ v\\ \end{pmatrix}$ 은 가역이다.

    2. $\{u, v\}$ 가 일차종속이면 행렬 $\begin{pmatrix} u\\ v\\ \end{pmatrix}$ 은 가역이 아니다.

- 증명

    1:

    $u = (a_1, a_2), v = (b_1, b_2), A = \begin{pmatrix} a_1&a_2\\ b_1&b_2\\ \end{pmatrix}$ 라고 하자. $\{u, v\}$ 가 일차독립이라는 가정으로부터 다음이 성립한다.

    $$ c_1(a_1, a_2) + c_2(b_1, b_2) = 0 \implies c_1 = c_2 = 0 $$

    이는 다음이 성립함을 뜻한다. 
    
    $$a_1 \neq 0 \land b_1 \neq 0$$ 
    
    $$a_2 \neq 0 \land b_2 \neq 0$$ 

    그러므로 다음이 성립한다.

    $$ \begin{pmatrix} a_1&a_2\\ b_1&b_2\\ \end{pmatrix} \to \begin{pmatrix} a_1b_1&a_2b_1\\ a_1b_1&a_1b_2\\ \end{pmatrix} \to \begin{pmatrix} a_1b_1&a_2b_1\\ 0&a_1b_2 - a_1b_1\\ \end{pmatrix} \to \begin{pmatrix} 1& \frac{a_2b_1}{a_1b_1} \\ 0&1\\ \end{pmatrix} \to I_2 $$

    [유한번의 기본행연산으로 $A$ 를 항등행렬로 변환하였으므로 $A$ 는 가역이다](MatrixOperation/#01cc5fcfe). 

    2:

    $\{u, v\}$ 가 일차종속이라는 가정으로부터 다음이 성립한다.

    $$ v = cu $$

    그러므로 다음이 성립한다.

    $$ A = \begin{pmatrix} a_1&a_2\\ b_1&b_2\\ \end{pmatrix}  =\begin{pmatrix} a_1&a_2\\ ca_1&ca_2\\ \end{pmatrix} \to \begin{pmatrix} a_1&a_2\\ 0&0\\ \end{pmatrix} $$

    [$A$ 를 항등행렬로 변환할 수 없으므로 $A$ 는 가역이 아니다](MatrixOperation/#01cc5fcfe). 

# System of Linear Equation

!!! tldr "연립일차방정식(system of linear equation)"

    $1 \leq i \leq m, 1 \leq j \leq n$ 에 대하여 스칼라 $a _{ij}, b_i \in \mathbf{F}$ 와 변수 $x_j \in \mathbf{F}$ 에 대한 다음의 연립방정식을 체 $\mathbf{F}$ 위 $n$ 개의 미지수와 $m$ 개의 일차방정식으로 이루어진 연립일차방정식으로 정의한다. 

    $$ a _{11}x_1 + a _{12}x_2 + \dots + a _{1n}x_n = b_1 $$

    $$ a _{21}x_1 + a _{22}x_2 + \dots + a _{2n}x_n = b_2 $$

    $$ \vdots $$

    $$ a _{m1}x_1 + a _{m2}x_2 + \dots + a _{mn}x_n = b_m $$

!!! tldr "계수행렬(coefficient matrix)"

    $n$ 개의 미지수와 $m$ 개의 일차방정식으로 이루어진 연립일차방정식의 계수로 구성된 다음의 $m \times n$ 행렬이다.

    $$ A = \begin{pmatrix} a_{11}&a_{12}&\dots&a_{1n}\\ a_{21}&a_{22}&\dots&a_{2n}\\ \vdots& \vdots& \ddots& \vdots \\ a_{m1}&a_{m2}&\dots&a_{mn}\\ \end{pmatrix} $$

- $n$ 개의 미지수와 $m$ 개의 일차방정식에 대한 계수행렬은 $m \times n$ 행렬이다. 이는 선형변환 $\mathbf{L}_{A}: \mathbf{F} ^{n} \to \mathbf{F} ^{m}$ 에 대응된다. 

!!! tldr "연립일차방정식의 행렬표현"

    계수행렬 $A$ 와 $x = \begin{pmatrix} x_{1}\\ x_{2}\\ \vdots\\ x_{n}\\ \end{pmatrix}, b = \begin{pmatrix} b_{1}\\ b_{2}\\ \vdots\\ b_{n}\\ \end{pmatrix}$ 에 대한 연립일차방정식의 행렬표현은 다음과 같다. 

    $$ Ax = b $$

!!! tldr "해(solution) "

    연립일차방정식의 해는 $Ax = b$ 에 대하여 $As = b$ 를 만족하는 $n$순서쌍 $s = \begin{pmatrix} s_{1}\\ s_{2}\\ \vdots\\ s_{n}\\ \end{pmatrix} \in \mathbf{F} ^{n}$ 이다.

- 해는 존재할 수도 있고 존재하지 않을 수도 있다. 해가 존재한다면 유일할 수도 있고 유일하지 않을 수도 있다.

!!! tldr "해집합(solution set) "

    연립일차방정식의 모든 해들의 집합이다.

!!! tldr "연립일차방정식의 무모순성"

    연립일차방정식의 해집합이 공집합이면 모순이 있다(inconsistent) 또는 해가 존재하지 않는다고 한다. 반면 해집합이 공집합이 아니면 모순이 없다(consistent) 또는 해가 존재한다고 한다.

- 그러므로 연립일차방정식을 풀기 위하여 해가 존재하는지 살펴보고, 존재하는 모든 해를 구할 수 있어야 한다.

!!! tldr "동차(homogeneouse) 와 비동차(nonhomogeneouse) "

    $n$ 개의 미지수와 $m$ 개의 일차방정식으로 이루어진 연립일차방정식 $Ax = b$ 는 $b = 0$ 일 때 동차라고 하고, $b \neq 0$ 이면 비동차라고 한다.

## Properties of System of Linear Equation

!!! tldr "정리 3.8"

    체 $\mathbf{F}$ 에서 $n$ 개의 미지수와 $m$ 개의 일차방정식으로 이루어진 동차 연립일차방정식 $Ax = 0$ 와 해집합 $\mathbf{K}$ 에 대하여 $\mathbf{K} = \mathbf{N} (\mathbf{L}_A)$ 이다. 즉, 다음이 성립한다. 

    1. $\mathbf{K}$ 는 $\mathbf{F} ^{n}$ 의 부분공간이다.

    2. $\dim (\mathbf{K} ) = n - \text{rank} (\mathbf{L}_{A}) = n - \text{rank} (A)$

- 증명

    $\mathbf{K} = \{s \in \mathbf{F} ^{n} : As = 0\} = \mathbf{N} (\mathbf{L}_A)$ 인 것과 [차원정리](../LinearTransformation/#6187a9f9c) 와 [행렬의 랭크의 정의](#50228784b) 의하여 증명이 끝난다. ■ 

- 예시 

    다음과 같은 연립일차방정식이 존재한다. 

    $$ x_1 + 2x_2 + x_3 = 0 $$

    $$ x_1 - x_2 - x_3 = 0 $$

    계수행렬 $A = \begin{pmatrix} 1&2&1\\ 1&-1&-1\\ \end{pmatrix}$ 에 대하여 $\text{rank} (A)  = 2$ 이다. 해집합 $\mathbf{K}$ 에 대하여 $\dim (\mathbf{K} ) = 3 - 2 = 1$ 이므로 영벡터가 아닌 임의의 해가 $\mathbf{K}$ 의 기저가 된다. 가령 $\begin{pmatrix} 1\\ -2\\ 3\\ \end{pmatrix}$ 이 해이므로 $\text{span} \Bigg \{\begin{pmatrix} 1\\ -2\\ 3\\ \end{pmatrix}\Bigg \} = \mathbf{K}$ 이다.

!!! tldr "정리 3.8 따름정리"

    $m < n$ 이면 연립방정식 $Ax = 0$ 은 영벡터가 아닌 해가 있다.

- 이 정리는 일차방정식보다 미지수가 많으면 영이 아닌 벡터가 해로 존재한다는 것을 말해준다. 

- 증명

    $m < n$ 을 가정하고 $\mathbf{K} = \mathbf{N} (\mathbf{L}_A)$ 으로 두자.

    연립일차방정식이 $n$ 개의 미지수와 $m$ 개의 일차방정식을 가지므로 $A$ 는 $m \times n$ 계수행렬이다. 그러므로 [$\mathbf{L}_{A}$ 는 $\mathbf{F} ^{n} \to \mathbf{F} ^{m}$ 위에서 정의된 좌측 곱 변환](../LinearTransformation/#78c54c688)이다. [$\mathbf{L}_{A}$ 의 상공간은 $\mathbf{F} ^{m}$ 의 부분공간](../LinearTransformation/#eb957cbf0)이다. [정리 1.11](../VectorSpace/#26f9238cb) 와 [행렬의 랭크의 정의](#50228784b) 에 의하여 다음이 성립한다.
    
    $$ \text{rank} (A) = \text{rank} (\mathbf{L}_{A}) \leq m $$

    정리 3.8 에 의하여 다음이 성립한다. 

    $$ \dim (\mathbf{K} ) = n - \text{rank} (\mathbf{L}_{A})  \geq n - m > 0 $$

    이는 $\mathbf{K} \neq \{0\}$ 임을 뜻하고, 이에따라 영이 아닌 벡터 $s \in \mathbf{K}$ 가 존재한다. ■ 

!!! tldr ""

    $Ax = 0$ 을 $Ax = b$ 에 대응하는 동차 연립일차방정식이라 한다.

!!! tldr "정리 3.9"

    모순이 없는 연립일차방정식 $Ax = b$ 의 해집합 $\mathbf{K}$, 대응하는 연립일차방정식 $Ax = 0$ 의 해집합 $\mathbf{K} _{\mathbf{H} }$, $Ax = b$ 의 임의의 해 $s \in \mathbf{K}$ 에 대하여 다음이 성립한다.

    $$ \mathbf{K} = \{s\} + \mathbf{K} _{\mathbf{H} } = \{s + k : k \in \mathbf{K} _{\mathbf{H} }\} $$

- 이 정리는 비동차 연립일차방정식의 해집합을 동차 연립일차방정식의 해집합과 연결시켜준다.

- 증명

    $Ax + b$ 의 임의의 해 $s \in \mathbf{K}$ 를 택하자.

    $w \in \mathbf{K}$ 를 가정하면 $Aw = b$ 이다. 그러면 $A(w-s) = Aw-As = b-b = 0 \implies w-s \in \mathbf{K} _{\mathbf{H} }$ 이다. $w - s = k \in \mathbf{K} _{\mathbf{H} }$ 로 두자. 그러면 $w = s + k \in \{s\} + \mathbf{K} _{\mathbf{H} }$ 이다. 이는 어떤 원소가 $\mathbf{K}$ 에 속하면 반드시 $\{s\} + \mathbf{K} _{\mathbf{H} }$ 에 속함을 뜻한다. 그러므로 다음이 성립한다.

    $$ \mathbf{K} \subseteq \{s\} + \mathbf{K} _{\mathbf{H} } \tag*{▲} $$

    $w \in \{s\} + \mathbf{K} _{\mathbf{H} }$ 를 가정하면 $w = s + k$ 를 만족하는 $k \in \mathbf{K} _{\mathbf{H} }$ 가 존재한다. 그러므로 다음이 성립한다. 

    $$ Aw = A(s+k) = As + Ak = b + 0 = b $$
    
    즉, $w \in \mathbf{K}$ 이므로 $\{s\} + \mathbf{K} _{\mathbf{H} } \subseteq \mathbf{K}$ 이다. ▲ 
    
    따라서 $\mathbf{K} = \{s\} + \mathbf{K} _{\mathbf{H}}$ 이다. ■ 

- 예시 

    다음 연립일차방정식의 해는 $s = \begin{pmatrix} 1\\ 1\\ 4\\ \end{pmatrix} \in \mathbf{K}$ 이다.

    $$ x_1 + 2x_2 + x_3 = 7 $$

    $$ x_1 - x_2 - x_3 = -4 $$

    대응하는 동차 연립일차방정식의 해는 $k = \begin{pmatrix} 1\\ -2\\ 3\\ \end{pmatrix} \in \mathbf{K} _{\mathbf{H} }$ 이고 $\dim (\mathbf{K} _{\mathbf{H} }) = 1$ 이므로 $\mathbf{K} _{\mathbf{H} }= \{tk : t \in \R\}$ 이다. 그러므로 다음이 성립한다. 

    $$ \mathbf{K} = \{s + tk : t \in \R\} $$

!!! tldr "정리 3.10"

    $n$ 개의 미지수와 $n$ 개의 일차방정식으로 이루어진 연립일차방정식 $Ax = b$ 에 대하여 $A$ 가 가역이면 이 방정식은 유일한 해 $A ^{-1}b$ 를 가진다.

    역으로 연립일차방정식의 해가 유일하면 계수행렬은 가역이다.

- 이 정리는 가역인 정사각행렬을 계수행렬로 가지는 연립일차방정식의 해를 쉽게 구할 수 있는 방법을 알려준다.

- 증명

    $A$ 가 가역이면 역행렬 $A ^{-1}$ 가 존재하므로 $A(A ^{-1}b) = (AA ^{-1})b = b$ 가 성립한다. 그러므로 $A ^{-1}b$ 는 해이다. 이로써 존재성 증명이 끝났다. 
    
    이제 유일성을 증명하기 위하여 임의의 해 $s$ 에 대하여 $As = b$ 로 두면 $A ^{-1}As = A ^{-1}b \iff s = A ^{-1}b$ 가 성립한다. ▲ 

    방정식의 유일한 해를 $s$ 로 두면 대응하는 동차 연립일차방정식 $Ax = 0$ 의 해집합 $\mathbf{K} _{\mathbf{H} }$ 에 대하여 [정리 3.9](#932b55b12) 에 의하여 $\mathbf{K} = \{s\} = \{s\} + \mathbf{K} _{\mathbf{H}} \iff \mathbf{K} _{\mathbf{H} } = \{0\}$ 이다. [정리 3.8](#b7b9c78d0) 에 의하여 $\mathbf{K} _{\mathbf{H} } = \{0\} = \mathbf{L}_{A}$ 이고, $\dim (\mathbf{K} _{\mathbf{H} }) = n - \text{rank} (\mathbf{L}_{A}) = 0 \iff \text{rank} (\mathbf{L}_{A}) = n$ 이므로 [$\text{rank} (A) = n$ 이다. 그러므로 $A$ 는 가역이다](#8252ffa8b).

## Existence of Solution of Linear Equation System

!!! tldr "연립일차방정식의 첨가행렬"

    연립일차방정식 $Ax = b$ 의 첨가행렬은 $(A|b)$ 이다.

!!! tldr "문제 3.3-9"

    연립일차방정식 $Ax = b$ 의 해가 있는 것과 $b \in \mathbf{R} (\mathbf{L}_A)$ 인 것은 동치이다.

- 증명

    해가 존재하면 $As = b$ 를 만족하는 $s$ 가 존재한다. 그러므로 $\mathbf{L}_{A}(s) = b \in \mathbf{R} (\mathbf{L}_A)$ 이다. ▲ 

    $b \in \mathbf{R} (\mathbf{L}_A)$ 이면 $\mathbf{L}_{A}(s) = As = b$ 를 만족하는 $s$ 가 존재한다. 그러므로 연립일차방정식의 해가 존재한다. ■ 

!!! tldr "정리 3.11"

    연립일차방정식 $Ax = b$ 에 모순이 없는 것과 $\text{rank} (A) = \text{rank} (A|b)$ 인 것은 동치이다.

- 증명

    [정리 3.5](#0ce821e3f) 의 증명과정은 행렬 $A$ 의 $j$열 $a_j$ 에 대하여 $\mathbf{R} (\mathbf{L}_A)=\text{span} (\{a_1, a_2, \dots, a_n \})$ 임을 말해준다. 문제 3.3-9 에 의하여 $Ax = b$ 가 해가 있는 것은 $b \in \mathbf{R} (\mathbf{L}_A)$ 와 동치이다. 그러므로 $Ax = b$ 의 해가 있기 위하여 다음이 성립해야 한다. 

    $$ b \in \text{span} (\{a_1, a_2, \dots, a_n \}) $$

    그러므로 다음이 성립한다. 

    $$ \text{span} (\{a_1, a_2, \dots, a_n \}) = \text{span} (\{a_1, a_2, \dots, a_n, b \}) $$

    따라서 $\dim (\text{span} (\{a_1, a_2, \dots, a_n \}) )= \dim (\text{span} (\{a_1, a_2, \dots, a_n, b \}))$ 이다. [정리 3.5](#0ce821e3f) 에 의하여 다음이 성립한다.

    $$ \text{rank} (A) = \text{rank} (A|b) \tag*{■} $$

- 예시 

    다음 연립방정식에 대하여 $A = \begin{pmatrix} 1&1\\ 1&1\\ \end{pmatrix}, (A|b) = \begin{pmatrix} 1&1&0\\ 1&1&1\\ \end{pmatrix}$ 이다.

    $$ x_1 + x_2 = 0 $$

    $$ x_1 + x_2 = 1 $$

    그러므로 $\text{rank} (A) = 1, \text{rank} (A|b) = 2$ 이다. 정리에 의하여 이 방정식의 해가 없다.
