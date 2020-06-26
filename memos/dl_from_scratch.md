# <a name="Deep Learning from Scratch" href="#Deep Learning from Scratch">Deep Learning from Scratch</a>

[밑바닥부터 시작하는 딥러닝](https://book.naver.com/bookdb/book_detail.nhn?bid=11492334)의 개인 메모입니다.

# <a name="퍼셉트론 Perceptron" href="#퍼셉트론 Perceptron">퍼셉트론 Perceptron</a>

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

계단 함수(step function) : 입력 $x$ 가 $0$ 을 넘으면 $y = 1$ 을 출력하고, $0$ 과 같거나 작으면 $y = 0$ 을 출력하는 함수

$$ y = \begin{cases} 1\ (x > 0) &\text{}\\ 0\ (x \leq 0) &\text{}\\ \end{cases} $$

이다.

</blockquote>

- 코드로도 간단하게 구현할 수 있다.

  ```python
  def step_function(x):
      return int(x > 0)
  ```

  위 코드는 `numpy` 의 행렬(배열)을 인수로 받을 수 없다. 따라서 다음과 같이 고칠 수 있다.

  ```python
  import numpy as np
  def step_function(x):
      y = x > 0
      return y.astype(np.int)
  ```

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

시그모이드 함수(sigmoid function) : 입력 $x$ 에 대하여 다음의 출력 $y$ 를 계산하는 함수이다.

$$ y = \zeta (x) = \dfrac{1}{1+e ^{-x}} $$

또는

$$ y = \zeta (x) =\dfrac{1}{1+\text{exp}(-x)} $$

</blockquote>

- 편의상 표준 시그모이드 함수를 단순히 시그모이드 함수라고 부르는 것이다.

- 시그모이드라는 이름 **sigmoid** 는 단순히 함수가 "S자 모양" 이라는 뜻이다. 계단 함수처럼 함수의 개형을 보고 이름을 붙힌 것이다. 

  그러니까 시그모이드 함수라고 하면 그냥 **"S자 모양 함수이다."** 라고 이해하면 된다. 
  
  - 다음과 같이 표준 시그모이드 함수는 S 자 모양을 그린다.

    ![desmos-graph](https://user-images.githubusercontent.com/16812446/77422864-87333180-6e11-11ea-8200-6f070e22c6d9.png)

- 시그모이드 함수는 다음과 같이 간단히 코드로 구현할 수 있다.

  ```python
  import numpy as np
  def sigmoid(x):
      return 1 / (1 + np.exp(-x))
  ```

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

퍼셉트론(perceptron) 또는 인공뉴런 : 임의의 자연수 $n$ 에 대하여 $n$ 개의 실수 $x$(입력) 와 그 입력에 각각 대응되는 실수 $w$(가중치) 를 곱한 것을 모두 더한 실수 $z$(순입력) 가

실수 $\theta$(임계값) 보다 크면 $y=0$ 을 계산(출력)하고, 같거나 작으면 $y=1$ 을 계산(계단함수)하는 알고리즘(계산과정)이다.

$$ y = \begin{cases} 1\ \bigg (\displaystyle z = \sum_{i=1}^{n}w _{i} x _{i} > \theta \bigg ) &\text{}\\ 0\ \bigg (\displaystyle z = \sum_{i=1}^{n}w _{i} x _{i} \leq \theta \bigg ) &\text{}\\ \end{cases} $$

</blockquote>

- 또는 $b = -\theta$ 에 대하여

  $$ y = \begin{cases} 1\ \bigg (\displaystyle b + \sum_{i=1}^{n}w _{i} x _{i} > 0 \bigg ) &\text{}\\ 0\ \bigg (\displaystyle b + \sum_{i=1}^{n}w _{i} x _{i} \leq 0 \bigg ) &\text{}\\ \end{cases} $$

  로 표현할 수 있다.

  - 이때 $b$ 를 편향(bias) 라고 한다.

  - 그러므로 원래는 $n$ 차원 벡터 $x = \begin{bmatrix} x_1\\x_2\\\dots\\x_n\end{bmatrix}$ (입력) 의 전치와 $n$ 차원 벡터 $w = \begin{bmatrix} w_1\\w_2\\\dots\\w_n\end{bmatrix}$ (가중치) 의 내적(순입력)

    $$ x ^{T}w = \sum_{i=1}^{n} w _{i} x _{i} = z $$

    이 $z > \theta$ 이면 $y=1$ 로, $z \leq  \theta$ 이면 $y=0$ 로 계산했었다.
  
  - 그러나 임계값 $\theta$ 를 편향 $b$ 로 바꾸어 표현한 모델에서는 입력 $x_0$ 와 가중치 $w_0 = b$ 를 추가하여 
  
    $x_0=1$ 에 대한 $n+1$ 차원 벡터 $x = \begin{bmatrix} x_0\\x_1\\x_2\\\dots\\x_n\end{bmatrix}$ (입력) 의 전치와 
    
    $w_0 = b$ 에 대한 $n+1$ 차원 벡터 $w = \begin{bmatrix} w_0 \\ w_1\\w_2\\\dots\\w_n\end{bmatrix}$ (가중치) 의 내적(순입력)

    $$ x ^{T}w = b + \sum_{i=1}^{n} w _{i} x _{i} =  \sum_{i=0}^{n} w _{i} x _{i} = z (\because b = x_0w_0 = 1 \cdot b)$$

    이 $z > 0$ 이면 $y=1$ 로, $z \leq  0$ 이면 $y=0$ 로 계산한다.

- 퍼셉트론이란 1957년 프랑크 로젠블라트(Frank Rosenblatt) 가 논문 《The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain》  고안한 알고리즘이다.

- 이 퍼셉트론이 신경망(딥러닝)의 기원이 되는 알고리즘이다.

- 이 퍼셉트론을 **인공뉴런**, **단순 퍼셉트론**으로 부르지면 여기서는 단순히 **퍼셉트론**이라고 하자.

- 이 퍼셉트론 알고리즘으로 할 수 있는 일이란 입력을 직선으로(선형적으로) 두 가지로 분류하는 것이다.

  - 퍼셉트론 알고리즘으로 직선으선형적으 분류가 가능한 다음과 같은 단순한 문제들을 풀 수 있다. 
  
    이것은 퍼셉트론 알고리즘이 매개변수(가중치 $w$, 임계값 $\theta$)를 조정하는 것으로써 다양한 알고리즘(AND 게이트, OR 게이트, NAND 게이트)로 사상될 수 있다는 것을 의미한다.

  - 예시 
  
    **AND 게이트**는 다음과 같이 $2$ 개의 입력에 대하여 $1$ 개의 출력을 계산한다.

    |$x_1$|$x_2$|$y$|
    |:---:|:---:|:---:|
    |$0$|$0$|$0$|
    |$1$|$0$|$0$|
    |$0$|$1$|$0$|
    |$1$|$1$|$1$|

    퍼셉트론으로 AND 게이트를 표현하려 한다. 그렇다면 $2$ 개의 입력 $x$ 와 그에 대응되는 가중치 $w$ 를 곱한 것을 모두 더한 $y$ 가 임계값 $\theta$ 보다 클 때 $1$, 같거나 작을 때 $0$ 을 출력하게 하면 된다. 
    
    입력 $x$ 는 임의의 수 $0, 1$ 이고 이것을 가중치 $w$ 로 계산하고 임계값 $\theta$ 와 비교하므로 결국 **가중치 $w$ 와 임계값 $\theta$ 을 조정하는 것으로 퍼셉트론을 특정해주어야** 한다.

    이 경우 $(w _{1}, w _{2}, \theta) = (0.5, 0.5, 0.7)$ 로 설정하면 퍼셉트론이 AND 게이트와 같은 출력(계산결과)를 낼 수 있다.

    > 그런데 이로써 어떤 대상에게는 불변요소(변하지 않는 요소, 변하지만 우리가 임의로 조작할 수 없는 요소 등)와 가변요소(우리가 임의로 조작할 수 있는 요소) 가 있다는 것을 알 수 있다. 실제로 우리는 모든 대상을 불변 혹은 가변이라는 기준으로 분석할 수 있다. 그런데 이 대상은 물론 계산 가능하다는 범주 안에 포함되어야만 한다. 이 분류가 이루어진다면, 위의 퍼셉트론 알고리즘 또한 이 모델로 추상화가 가능하다. 그리고 추상화된 모델로써 그 안에 포함된 모든 알고리즘(계산과정) 모델을 단번에 다룰 수 있다. 이것의 효용은 우리가 광범위한 알고리즘 모델을 또 다시 추상화시켜서 수없이 많은 대상을 자동화할 수 있다는 것이다.

  - 예시 
  
    **NAND 게이트**는 다음과 같이 $2$ 개의 입력에 대하여 $1$ 개의 출력을 계산한다.

    |$x_1$|$x_2$|$y$|
    |:---:|:---:|:---:|
    |$0$|$0$|$1$|
    |$1$|$0$|$1$|
    |$0$|$1$|$1$|
    |$1$|$1$|$0$|

    퍼셉트론으로 NAND 게이트를 표현하려 한다. 이 경우 $(w _{1}, w _{2}, \theta) = (-0.5, -0.5, -0.7)$ 로 설정하면  된다.

  - 예시 
  
    **OR 게이트**는 다음과 같이 $2$ 개의 입력에 대하여 $1$ 개의 출력을 계산한다.

    |$x_1$|$x_2$|$y$|
    |:---:|:---:|:---:|
    |$0$|$0$|$0$|
    |$1$|$0$|$1$|
    |$0$|$1$|$1$|
    |$1$|$1$|$1$|

    퍼셉트론으로 OR 게이트를 표현하려 한다. 이 경우 $(w _{1}, w _{2}, \theta) = (1, 1, 0.8)$ 로 설정하면 된다.
  
  이것은 퍼셉트론으로 데이터를 분류하는 직선을 생성하는(선형 이진 분류기) 것과 같다. 다음과 같이 AND 게이트를 퍼셉트론이 분류하는 것이다.

  ![](https://miro.medium.com/max/1914/1*Tc8UgR_fjI_h0p3y4H9MwA.png) 

  하지만 XOR 게이트는 직선으로 분류할 수 없으므로 퍼셉트론으로 XOR 게이트를 표현할 수 없다.

- 퍼셉트론의 기하학적 의미

  퍼셉트론의 기하학적 의미를 이해하는 것은 중요한 의미를 갖는다.

  ![](https://miro.medium.com/max/764/1*C5LeL8JDfoGbkUg0cu1M-w.png)

  퍼셉트론의 n개의 입력과 n개의 가중치는 n차원 공간에서의 벡터로 볼 수 있고, 그것을 각각 곱하여 합한 것은 내적으로 볼 수 있다.

  또 퍼셉트론은 최종적으로 데이터를 2 종류로 분류할 수 있는 직선을 표현하는 가중치, 즉 직선의 기울기를 찾아내는 것이다. 

  **이렇게 퍼셉트론의 구성요소를 대수학과 벡터해석학 등의 수학으로 해석하면 수학적 의미를 찾아낼 수 있어서 많은 효용을 얻을 수 있다.**

- 퍼셉트론은 계산 가능하므로 코드로 자동화시킬 수 있다.

  - 예시 

    **구체화 필요**

    ```python
    def AND(x1, x2):
        w1, w2, theta = 0.5, 0.5, 0.7
        return int(x1*w1 + x2*w2 > theta)
    ```
  
  - 퍼셉트론 코드를 다음과 같이 일반적으로 나타낼 수 있다.

    **구체화 필요**

    ```python
    import numpy as np

    def perceptron(X, y, w = None):
        for xi, yi in zip(X, y):
          xi = xi
        return
    ```

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

다층 퍼셉트론(multi-layer perceptron) : 퍼셉트론을 여러개 쌓은 것이다.

</blockquote>

- 퍼셉트론으로 XOR 게이트를 표현할 수 없었지만 AND 게이트, NAND 게이트, OR 게이트를 표현한 퍼셉트론을 연결하면 XOR 게이트를 표현할 수 있다. 이렇게 연결된 퍼셉트론(인공뉴런)을 다층 퍼셉트론이라고 한다.

  - 퍼셉트론은 직교좌표계에서 단일 직선을 의미했다. 하지만 다층 퍼셉트론은 두 개의 출력을 냄으로써 두 개의 직선을 만든다.

    ![](https://t1.daumcdn.net/cfile/tistory/266ECC42535A2A2A1E)

    > https://roboticist.tistory.com/492

    그리고 이 두 직선을 기반으로 영역을 나누면 XOR 게이트를 분류할 수 있게 된다. 
    
    이 새로운 두 직선을 기반으로 좌표계를 변환해보면 XOR 게이트를 선형분류 문제로 환원시키는 것으로 볼 수도 있다는 것을 알 수 있다.

    ![](https://t1.daumcdn.net/cfile/tistory/265AA236535A2A2B2C)

    > https://roboticist.tistory.com/492

- 이 다층 퍼셉트론을 활용하여 모든 논리 회로를 표현할 수 있다. 왜냐하면 모든 논리 게이트를 표현할 수 있게 되었기 때문이다.

  여기서 알 수 있는 중요한 의의는 이에 따라 퍼셉트론이 모든 튜링기계와 만능기계(컴퓨터) 까지도 표현가능하다는 것이다. 왜냐하면 NAND 게이트 만으로도 현대의 최신 보편만능기계(컴퓨터) 도 구현 가능한데, 퍼셉트론으로 NAND 게이트를 구성할 수 있기 때문이다.

  - 2층 퍼셉트론, 정확히는 시그모이드 함수를 활성화 함수로 사용한다면 2층 퍼셉트론 구조로 임의의 함수를 표현할 수 있다는 사실이 증명되었다. 

    AND 게이트와 OR 게이트로 반가산기와 전가산기를 만들고, 그것으로 산술 논리 연산 장치(ALU)를 만들고 이것으로 CPU 를 만들 수 있다.
  
<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

활성화 함수(activate function) : n차원 벡터 입력 $x$ 와 n차원 벡터 가중치 $x$ 의 내적인 순입력 $z$ 를 

계산하여 뉴런(노드)의 출력을 결정하는 함수이다.

</blockquote>

- 퍼셉트론은 활성화 함수로써 계단함수를 채택하였다.

  - 하지만 퍼셉트론 알고리즘에서 계단함수를 임의의 활성화 함수로 일반화시켜야 신경망으로 나아갈 수 있다.

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

ReLU 함수 : 입력이 $0$ 을 넘으면 입력을 그대로 출력하고, $0$ 이하면 $0$ 을 출력하는 함수이다.

$$ y = \begin{cases}
x\ (x>0) &\text{}\\
0\ (x \leq 0) &\text{}\\
\end{cases} 
$$

</blockquote>

- 전통적으로 기계학습에서 학습을 위해 시그모이드 함수를 사용했으나 최근에는 이 ReLU 함수를 주로 사용하는 추세이다.

- ReLU 란 Rectified 란 뜻으로 "정류된" 이라는 말이다. 이것은 반파정류회로(half-wave rectification circuit) 가 $+/-$ 가 반복되는 교류에서 $-$ 흐름을 차단하여 정류시키는 것에서 유래되었다.

- 코드로 쉽게 구현할 수 있다.

  ```python
  import numpy as np
  def relu(x):
      return np.maximum(0, x)
  ```

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

신경망(neural network) : 퍼셉트론이 사용하는 계단함수를 일반적인 활성화 함수로 일반화 시키고, 

퍼셉트론의 가중치 매개변수를 수동으로 입력하는 것이 아니라 데이터로부터 자동으로 결정하게 하는 알고리즘이다.

</blockquote>

> 퍼셉트론이 처음 제시되었을 때 암묵적으로 채택되었던 "활성화 함수" 인 "계단 함수" 를 일반적인 "활성화 함수" 로 일반화시킴으로써 더욱 강력한 추상 구조인 신경망이 탄생하였다. 그렇다면 다른 구성 요소도 일반화시켜서 더 광범위한 계산 능력을 가진 추상 모델을 만들 수 있는 가능성을 볼 수 있다. 

- 퍼셉트론에서 입력과 가중치를 벡터의 내적으로 표현했었는데, 

  신경망에서는 다층 퍼셉트론의 수많은 계산을 수행해야 하기 때문에 가장 간소하게 표현할 수 있는 행렬 연산으로 표현하면 좋다.

  - 예시 

    가령 입력 벡터를 $1 \times 2$ 행렬 $X = \begin{pmatrix} x_1\\x_2 \end{pmatrix}$, 가중치를 $2 \times 3$ 행렬 $W=\begin{pmatrix} w _{11}&w _{21}&w _{31}\\w _{12}&w _{22}&w _{32} \end{pmatrix}$, 편향을 $1 \times 3$ 행렬 $B = \begin{pmatrix} b _{1}&b _{2} & b _{3}\\ \end{pmatrix}$ 으로 나타낸다면, 순입력 $Z = \begin{pmatrix} \\ \end{pmatrix}$