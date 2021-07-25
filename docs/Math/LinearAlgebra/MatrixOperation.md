
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

    $\text{rank} (A) = 0$ 을 가정하자. $A$ 의 $j$ 번째 열벡터 $a_j$ 에 대하여 $a_j \neq 0$ 이면 스칼라 $c$ 에 대하여 $ca_j = 0$ 가 되기 위해서는 반드시 $c = 0$ 이어야 한다. 그러면 일차독립의 정의에 의하여 집합 $\{a_j\}$ 은 일차독립이다. 그러나 정리 3.5 에 의하여 [극대 일차독립 집합의 기수](../VectorSpace/#c298b6300)가 $0$ 이므로 이는 모순이다. 따라서 $a_j = 0$ 이다. 이는 $A = O$ 임을 뜻한다. ▲  

    $A = O$ 을 가정하면 극대 일차독립 집합이 공집합이므로 $\text{rank} (A) = 0$ 이 바로 나온다. ■ 
    
!!! tldr ""

    다음 행렬 $B$ 에 대하여 $\text{rank} (B) = r \implies \text{rank} (B') = r-1$ 이다.

    $$ B = \left(\begin{array}{c|ccc} 0 & 0 & \dots & 0 \\ \hline 0 & & & \\ \vdots  & & B' & \\ 0 & & & \\ \end{array}\right) $$

- 증명



!!! tldr "정리 3.6"

    $A \in \mathbf{M}_{m \times n}$ 에 대하여 $\text{rank} (A) = r$ 이면 다음이 성립한다.

    1. $r \leq m, r \leq n$

    2. 유한 번의 기본행[열]연산으로 항등행렬 $I_r$ 영행렬 $O_1, O_2, O_3$ 에 대하여 $A$ 를 행렬 $D = \begin{pmatrix} I_r&O_1\\ O_2&O_3\\ \end{pmatrix}$ 로 바꿀 수 있다.

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

    [정리 3.4 따름정리](#108500177) 와 정리 3.5 에 의하여 $\text{rank} (A) = 1$ 이다. ▲ 

    $m > 1$ 일 때 $m - 1$ 에 대하여 성립한다는 것을 가정하자. $A$ 가 $m \times  m$ 행렬이라고 하자. $n = 1$ 이면 $m = 1$ 일 때의 증명과 비슷하게 증명이 끝난다. ▲ 

    $n > 1$ 을 가정하자. $A \neq O$ 이므로 어떤 $i, j$ 에 대하여 $A _{ij} \neq 0$ 이다. 따라서 기본행연산 1형과 기본열연산 1형을 최대 한 번 적용하여 1행 1열을 $0$ 이 아닌 성분으로 만들 수 있다. 그러므로 기본연산 2형을 통하여 1행 1열의 성분을 $1$ 로 만들 수 있다. 

    그러면 기본행연산 3형과 기본열연산 3형을 통하여 1행과 1열에서 1행 1열 성분을 제외하고 모두 다 $0$ 으로 만들 수 있다. 즉, $A \neq O$ 에 기본연산을 유한번 적용하여 다음 행렬 $B$ 를 얻는다. 
    
    $$ B = \left(\begin{array}{c|ccc} 1 & 0 & \dots & 0 \\ \hline 0 &   & & \\ \vdots  & & B' & \\ 0 & & & \\ \end{array}\right) $$