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

시그모이드 함수(sigmoid function) : 정의역 $(- \infty , \infty )$ 과 치역 $(0, 1)$ 을 가지는 함수로써 

입력 $x$ 에 대하여 다음의 출력 $y$ 를 계산하는 함수이다.

$$ y = \zeta (x) = \dfrac{1}{1+e ^{-x}} $$

또는

$$ y = \zeta (x) =\dfrac{1}{1+\text{exp}(-x)} $$

</blockquote>

- 편의상 표준 시그모이드 함수를 단순히 시그모이드 함수라고 부르는 것이다.

- 음의 무한대 $- \infty$ 에 가까울 수록 $0$ 에 수렴하고,

  양의 무한대 $\infty$ 에 가까울 수록 $1$ 에 수렴하고,

  그 중간인 $0$ 이면 $\dfrac{1}{2}$ 을 출력한다.

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

# <a name="신경망" href="#신경망">신경망</a>

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

신경망(neural network) : 퍼셉트론이 사용하는 계단함수를 일반적인 활성화 함수로 일반화 시키고, 

퍼셉트론의 가중치 매개변수를 수동으로 입력하는 것이 아니라 데이터로부터 자동으로 결정하게 하는 알고리즘이다.

</blockquote>

- 퍼셉트론이 활성화 함수로 계단 함수를 사용하는 것과 달리 신경망에서는 시그모이드 함수나 ReLU 함수 등을 사용하여 출력 신호를 변환한다.

  - 계단함수가 $0, 1$ 의 값만 출력하는 반면 시그모이드 함수는 매끄러운 모양새로 개구간 $(0, 1)$ 의 실수($0.731, 0.880$ 등)를 반환한다.

    시그모이드 함수의 이 매끄러움이 신경망 학습에서 중요한 역할을 한다.

  - 즉, 퍼셉트론에서는 $0, 1$ 이 흘렀다면, 신경망에서는 시그모이드 함수로 인해 개구간 $(0,1)$ 의 연속적인 실수가 흐른다.

> 퍼셉트론이 처음 제시되었을 때 암묵적으로 채택되었던 "활성화 함수" 인 "계단 함수" 를 일반적인 "활성화 함수" 로 일반화시킴으로써 더욱 강력한 추상 구조인 신경망이 탄생하였다. 그렇다면 다른 구성 요소도 일반화시켜서 더 광범위한 계산 능력을 가진 추상 모델을 만들 수 있는 가능성을 볼 수 있다. 

- 퍼셉트론에서 입력과 가중치를 벡터의 내적으로 표현했었는데, 

  신경망에서는 다층 퍼셉트론의 수많은 계산을 수행해야 하기 때문에 가장 간소하게 표현할 수 있는 행렬 연산으로 표현하면 좋다.

  - 예시 

    가령 입력 벡터를 $1 \times 2$ 행렬 $X = \begin{pmatrix} x_1\\x_2 \end{pmatrix}$, 가중치를 $2 \times 3$ 행렬 $W=\begin{pmatrix} w _{11}&w _{21}&w _{31}\\w _{12}&w _{22}&w _{32} \end{pmatrix}$, 편향을 $1 \times 3$ 행렬 $B = \begin{pmatrix} b _{1}&b _{2} & b _{3}\\ \end{pmatrix}$ 으로 나타낸다면, 순입력 $Z = \begin{pmatrix} z_1&z_2&z_3\\ \end{pmatrix}$ 를 다음과 같이 계산할 수 있다. 

    $$ Z = XW + B $$

    이 순입력 $Z$ 에 활성화 함수로 시그모이드 함수를 적용한 코드는 다음과 같다.

    - 코드 

      ```python
      import numpy as np
      def sigmoid(x):
          return 1 / (1 + np.exp(-x))
      X = np.array([1.0, 0.5])
      W = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
      B = np.array([0.1, 0.2, 0.3])

      Z = np.dot(X, W) + B
      A = sigmoid(Z)
      ```
  
- 신경망은 분류와 회귀 모두에 이용할 수 있다. 

  이때 어떤 문제이냐에 따라 출력층에서 사용하는 활성화 함수가 달라진다.

  - 보통 회귀 문제에서 항등 함수를 사용하고, 분류에서 소프트맥스 함수를 사용한다.

    - 분류란 데이터가 어느 클래스에 속하느냐는 문제이다.

    - 회귀는 입력 데이터에서 수치를 예측하는 문제이다. 
    
      가령 사진 속 인물의 몸무게를 맞추는 문제이다.

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

소프트맥스 함수(softmax function) : 분류에서 사용되는 함수

$$ y _{k} = \dfrac{\exp (a _{k})}{\displaystyle \sum_{i=1}^{n} \exp (a _{i})} $$

이다.

</blockquote>

- 코드

  ```python
  import numpy as np
  def softmax(a):
      return np.exp(a) / np.sum(np.exp(a))
  ```

- 소프트맥스의 출력은 모든 입력신호로부터 영향을 받는다.

- 소프트맥스 함수는 지수함수를 사용하는데 지수함수는 매우 쉽게 커진다. 가령 $e ^{100}$ 은 $0$ 이 $40$ 개가 넘는 큰 값이다. 이로인해 오버플로우가 쉽게 발생한다. 그런데 소프트맥스 함수는 어차피 비율을 계산하는 것이므로 다음과 같이 수식을 개선할 수 있다. 

  먼저

  $$ y _{k} = \dfrac{\exp (a _{k})}{\displaystyle \sum_{i=1}^{n} \exp (a _{i})}  $$

  에 임의의 정수 $C$ 를 분바와 분모에 곱하여

  $$ = \dfrac{C\exp (a _{k})}{\displaystyle C\sum_{i=1}^{n} \exp (a _{i})} $$

  를 얻고 $C$ 를 지수함수로 옮겨 $\log_{} C$ 로 만들면 다음을 얻는다.

  $$ = \dfrac{\exp (a _{k} + \log_{} C)}{\displaystyle \sum_{i=1}^{n} \exp (a _{i} + \log_{} C)} $$

  이때 $\log_{} C = C'$ 로 두면

  $$ = \dfrac{\exp (a _{k} + C')}{\displaystyle \sum_{i=1}^{n} \exp (a _{i} + C')} $$

  을 얻는데, 이것은 소프트맥스 함수에 임의의 $C'$ 를 분자와 분모에 더해도 관계없다는 뜻이 된다.

  따라서 오버플로우를 방지하기 위하여 입력값에 임의의 수를 빼줄 수 있는 것이다. 일반적으로 임의의 수로 입력 신호 중 최댓값을 채택한다. 가령 가장 큰 입력값이 $a_m$ 이라면 

  $$ \dfrac{\exp (a _{k} - a_m)}{\displaystyle \sum_{i=1}^{n} \exp (a _{i} - a_m)} $$

  을 사용하는 것이다.

  - 따라서 가령 다음과 같은 코드처럼 소프트맥스 함수를 개선할 수 있다.

    ```python
    import numpy as np
    def softmax(a):
        c = np.max(a)
        exp_a = np.exp(a - c)
        return exp_a / np.sum(exp_a)
    ```

- 신경망을 이용한 분류에서 일반적으로 가장 큰 출력을 내는 뉴런(노드)에 해당하는 클래스만 인식한다.

  그런데 소프트맥스는 단조증가함수이므로 출력이 가장 큰 뉴런의 위치는 달라지지 않는다. 

  그러므로 신경망 분류에서 소프트맥스 함수를 생략해도 관계없다.

  - 기계학습 문제풀이는 학습과 추론 두 단계로 이뤄진다. 학습 단계에서 모델을 학습하고, 추론 단계에서 미지의 데이터를 분류(추론) 한다.

    신경망을 학습시킬 때에는 출력층에서 소프트맥스를 사용한다.
  
<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

단조증가함수 : 정의역 원소 $a, b$ 가 $a \leq b$ 일 때, $f(a) \leq f(b)$ 가 성립하는 함수이다.

</blockquote>

# <a name="순전파" href="#순전파">순전파</a>

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

순전파(forward propagation) : 신경망의 학습과 추론 두 단계 중 추론과정이다.

</blockquote>

- 기계학습과 마찬가지로 신경망도 두 단계로 문제를 해결한다. 
   
  먼저 훈련데이터로 학습하며 가중치 매개변수를 결정하고, 

  추론 단계에서 학습한 매개변수를 사용해 입력 데이터를 분류한다.

- 이미 학습된 가중치 매개변수로 MNIST 같은 데이터셋을 테스트해볼 수 있다.

  - `sample_weight.pkl` 에 이미 학습된 가중치가 있다. 이 가중치는 은닉층 2개로 숫자 0 부터 숫자 9 를 분류하는 신경망이다.

    첫번째 은닉층에서는 50개의 뉴런을 배치하고, 두번째 뉴런에서는 100개의 뉴런을 배치한다. 

    최초의 입력층은 28x28 픽셀의 손글씨 이미지이므로 784 크기의 벡터이다. 그렇다면 다음과 같이 코드를 짤 수 있다. 

    ```python
    def predict(network, x):
        W1, W2, W3 = network['W1'], network['W2'], network['W3']
        b1, b2, b3 = network['b1'], network['b2'], network['b3']

        a1 = np.dot(x, W1) + b1
        z1 = sigmoid(a1)
        a2 = np.dot(z1, W2) + b2
        z2 = sigmoid(a2)
        a3 = np.dot(z2, W3) + b3
        y = softmax(a3)
        return y

    _, _, x, t = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
    accuracy_cnt = 0
    for i in range(len(x)):
        y = predict(network, x[i])
        p = np.argmax(y) # 확률이 가장 높은 원소의 인덱스를 얻는다.
        if p == t[i]:
            accuracy_cnt += 1

    print("Accuracy:" + str(float(accuracy_cnt) / len(x)))
    ```

    이 코드는 학습과정은 건너뛰고 이미 학습된 가중치를 불러와서 추론과정(순전파)만 수행해본다.

    그리고 정확도를 측정해서 출력한다.

  - 하지만 위 코드를 적당한 단위로 묶어서 다음과 같이 한번에 처리해주는 배치(batch) 처리를 할 수 있다.

    ```python
    x, t = get_data()
    network = init_network()

    batch_size = 100 # 배치 크기
    accuracy_cnt = 0

    for i in range(0, len(x), batch_size):
        x_batch = x[i:i+batch_size]
        y_batch = predict(network, x_batch)
        p = np.argmax(y_batch, axis=1)
        accuracy_cnt += np.sum(p == t[i:i+batch_size])

    print("Accuracy:" + str(float(accuracy_cnt) / len(x)))

    ```

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

배치(batch) : 입력 데이터를 하나로 묶은 것이다.

</blockquote>

- 입력 데이터를 배치로 처리하면 다음과 같은 여러 이점이 있다.

  - 이미지 1장당 처리 시간을 대폭 줄여준다.

  - 수치 계산 라이브러리(numpyu, pytorch 등) 대부분이 큰 배열을 효율적으로 처리할 수 있도록 고도로 최적화되어있다.

  - 큰 신경망에서는 데이터 병목이 자주 발생하는데, 배치 처리를 함으로써 I/O 버스에 부하를 줄여줄 수 있다.

    - 더 정확히 말하면 느린 I/O 를 통해 데이터를 읽는 횟수를 줄여서, 빠른 CPU 나 GPU 의 순수계산 비율을 높이는 것이다.

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

원-핫 인코딩(one-hot encoding) : 정답을 뜻하는 원소만 $1$ 로, 나머지는 모두 $0$ 인 배열로 저장하는 방식이다.

</blockquote>

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

전처리(pre-processing) : 신경망의 입력 데이터에 특정 변환을 가하는 것이다.

</blockquote>

- 이 전처리는 활발히 사용되는데, 입력 데이터에 적절한 변환을 가함으로써 식별 능력을 개선하고 학습 속도를 높일 수 있기 때문이다.

- 예시 

  데이터 전체 평균과 표준편차를 이용하여 데이터들이 $0$ 을 중심으로 분포하도록 이동한다. 

  데이터의 확산 범위를 제한하는 정규화를 수행한다. 

  전체 데이터를 균일하게 분포시키는 데이터 백색화(whitening) 를 진행한다.

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

정규화(normalization) : 전처리 과정 중 하나로 입력 데이터를 특정 범위로 변환하는 것이다.

</blockquote>

- 예시 

  폐구간 $[0, 255]$ 에 존재하는 정수 데이터를 폐구간 $[0, 1]$ 에 존재하는 실수로 변환한다.

# <a name="기계학습" href="#기계학습">기계학습</a>

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

학습(learning) : 신경망 학습에서 학습이란, 

손실함수의 값을 가장 작게 만드는 가중치 매개변수의 최적값을 훈련 데이터로부터 자동으로 찾는 것이다.

</blockquote>

- 손실 함수의 값을 작게만드는 기법 중 하나로 함수의 기울기를 활용하는 경사법이 있다.

- 신경망은 데이터에서 자동으로 학습하는데, 이는 수천만개의 가중치를 수작업으로 조정할 필요 없이 자동으로 조정할 수 있다는 뜻이다.

  - 퍼셉트론도 선형 분리 가능 문제들, 즉 직선으로 분류가 가능한 데이터는 데이터로부터 자동으로 학습할 수 있다. 이것이 퍼셉트론 수렴 정리(perceptron convergence theorem) 이다.

    그러나 퍼셉트론은 XOR 게이트 같은 비선형 분리 문제는 자동으로 학습할 수 없다.

- 위에서 순전파로 이미 학습된 가중치로 MNIST 손글씨 데이터를 추론했었다.

  이제 실제로 숫자 $5$ 를 인식하는 프로그램을 만들어보아야 한다.

  그런데 대체 어떻게 만들어야할까? $5$ 를 인식하는 알고리즘을 밑바닥부터 짜는 것보다 이미지에서 특징(feature) 를 추출하고 그 특징의 패턴을 기계학습으로 가중치에 학습시키는 것이 좋다.

  - 여기서 말한 특징(feature)이란 입력 데이터(이미지) 에서 본질적인 데이터(중요한 데이터) 를 추출한 변환기이다.

  - 이미지의 특징은 보통 벡터로 표현한다.

  - 컴퓨터 비전에서는 SIFT, SURF, HOG 등의 특징을 많이 사용한다.

    이 특징을 사용하여 이미지를 벡터로 변환하고, 
    
    변환된 벡터를 가지고 지도 학습 방식의 대표 분류 기법인 SVM, KNN 등으로 학습할 수 있다.
  
  - 하지만 이 특징 기법의 단점은 특징까지는 여전히 사람이 설계하기 때문에 문제에 적합한 특징을 쓰지 않으면 좋은 결과를 얻을 수 없다는 것이다.

    |유형|입력 데이터 | 알고리즘 | 출력 데이터|
    |:---:|:---:|:---:|:---:|
    |1|손글씨 $5$|사람이 명시한 규칙(알고리즘)|결과|
    |2|손글씨 $5$|사람이 생각한 특징(SIFT, HOG 등) &rarr; 기계학습(SVM, KNN 등)|결과|
    |3|손글씨 $5$|신경망(딥러닝)|결과|

    유형 1 은 순수하게 사람이 제작한 알고리즘으로 손글씨 $5$ 를 5 라고 판단하는 것이고,

    유형 2 은 사람이 생각한 특징을 기반으로 기계학습을 하여 손글씨 $5$ 를 5 라고 판단하는 것이고,

    유형 3 은 순수하게 컴퓨터가 딥러닝으로 손글씨 $5$ 를 5 라고 판단하는 것이다.

- 위의 이유 때문에 딥러닝을 종단간 기계학습(end-to-end machine learning) 이라고도 한다.

  이것은 "처음부터 끝까지" 사람의 개입없이 결과를 얻는다는 뜻을 갖고 있다.

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

퍼셉트론 수렴 정리(perceptron convergence theorem) : 퍼셉트론이 선형 분리 가능 문제들, 즉 직선으로 분류가 가능한 데이터는 

항상 데이터로부터 자동으로 학습할 수 있다는 정리이다.

</blockquote>

- 그러나 비선형 분리 문제는 퍼셉트론이 자동으로 학습할 수 없다.

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

과적합(overfitting) : 신경망이 특정 데이터셋에 과하게 최적화된 상태이다.

</blockquote>

# <a name="손실함수" href="#손실함수">손실함수</a>

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

손실함수(loss function) : 현재의 신경망이 데이터를 얼마나 처리하지 못하는지를 출력하는 함수이다.

</blockquote>

- 이 손실함수를 통하여 가중치 매개변수들을 얼마나 조정해야 하는지 알 수 있다.

- 손실함수로 임의의 함수를 사용할 수 있으나, 

  일반적으로 평균 제곱 오차와 교차 엔트로피 오차를 사용한다.

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

평균 제곱 오차(mean squared error, MSE) : 신경망의 출력 $y _{k}$, 정답 레이블 $t _{k}$, 데이터의 차원 수 $k$ 에 대한 손실함수

$$ E = \dfrac{1}{2}  \sum_{k}^{}(y _{k} - t _{k}) ^{2} $$

이다.

</blockquote>

- 가장 자주 쓰이는 손실 함수이다.

- 예시 

  손글씨 숫자 인식 MNIST 데이터셋 테스트에서 신경망의 출력층의 소프트맥스 함수의 출력 $y _{k}$ 를

  ```python
  y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
  ```

  이라고 하자. 출력 $y _{k}$ 는 손글씨가 각각의 숫자일 확률이다. 그래서 이미지가 $0$ 일 확률은 $0.1$ 로 계산한 것이다. 따라서 신경망이 손글씨가 $2$ 일 확률이 $60\%$ 로 가장 높다고 판단한 것이다.
  
  원핫인코딩으로 인코딩된 정답을 가르키는 정답 레이블 $t _{k}$ 를 

  ```python
  t = [0,0,1,0,0,0,0,0,0,0]
  ```

  이라고 하자. 
  
  이때 평균 제곱 오차는 각 원소의 출력(추정값)과 정답 레이블의 차($y _{k} - t _{k})$ 를 제곱한 후 그 총합을 구하는 것이다. 따라서 
  
  ```python
  def MSE(y, t):
      return 0.5 * np.sum((y - t) ** 2)
  ```

  로 간단히 구현할 수 있다. 출력과 정답의 평균오차제곱을 구해보면 $2$ 를 가장 높은 확률로 추론했으므로 다음과 같이 손실값이 작게 나온다.

  ```python
  print(MSE(np.array(y), np.array(t)))
  # 0.0975...
  ```

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

교차 엔트로피 오차(cross entropy error, CEE) : 신경망의 출력 $y _{k}$, 정답 레이블 $t _{k}$, 데이터의 차원 수 $k$ 에 대한 손실함수

$$ E = - \sum_{k}^{} t _{k}\ln_{} y _{k} $$

이다.

</blockquote>

- 교차 엔트로피 오차 함수에서 정답레이블의 $t _{k}$ 는 원-핫 인코딩된 레이블이다. 따라서 정답 인덱스만 $1$ 이고 나머지는 $0$ 이다.

  그런데 정답 레이블와 출력을 곱하고 있으므로 정답에 해당하는 출력 이외의 값들은 $0$ 과 곱해져서 $0$ 이 된다. 즉, 정답이 아닌 출력은 손실함수에 영향을 끼지지 않는다.

- 예시 

  손글씨 숫자가 어떤 숫자인지 추정할 때 정답이 $2$ 였는데, $2$ 에 해당하는 출력값이 $0.6$ 이었다고 하자. 즉 $2$ 일 확률이 $60\%$ 라고 추론한 것이다.

  이때 교차 엔트로피 함수는 단순히 

  $$ E = - \ln_{} (0.6) = 0.51 $$

  이 된다. 반면 $2$ 에 해당하는 출력값이 $0.1$ 이었다면

  $$ E = - \ln_{} (0.1) = 2.30 $$

  이 되어 손실값이 커지게 된다.

- 교차 엔트로피 오차함수는 다음과 같이 코드로 간단히 구현할 수 있다.

  ```python
  def CEE(y, t):
      delta = 1e-7
      return -np.sum(t * np.log(y + delta))
  ```

  그런데 위 코드를 보면 원래의 수식 

  $$ E = - \sum_{k}^{} t _{k}\ln_{} y _{k} $$

  으로 오차를 계산하는 것이 아니라

  $$ E = - \sum_{k}^{} t _{k}\ln_{} (y _{k} + 0.00000001) $$

  로 계산하는 것을 알 수 있다.

  이것은 $\log_{}$ 함수에 $0$ 을 입력하면 음의 무한대가 되기 때문에 절대 $0$ 이 되지 않도록 아주 작은 값을 더해주는 가벼운 트릭이다.

- 그러나 손실함수는 실제로 하나의 훈련 데이터만을 계산하는 것이 아니라,

  모든 훈련 데이터를 대상으로 손실 함수 값을 구해야만 한다. 

  쉽게 말해 훈련 데이터가 100개면 이것을 기반으로 100개의 손실 함수 값의 합을 가중치 매개변수 조정의 기준으로 삼아야 한다는 것이다.

  - 교차엔트로피 함수의 훈련 데이터 모두에 대한 손실함수의 합은 

    $N$ 개의 데이터, 데이터의 차원 수 $k$, $n$ 번째 데이터의 $k$ 번째 데이터의 정답 레이블 $t _{nk}$, 신경망의 출력 $y _{nk}$ 에 대하여

    $$ E = - \dfrac{1}{N}\sum_{n}^{}\sum_{k}^{}t _{nk}\log_{} y _{nk} $$

    이다.

    수식이 복잡해보여도 단순히 교차 엔트로피 함수를 $N$ 개의 데이터에 대하여 확장했을 뿐이다! 마지막에는 $N$ 으로 나누어 값을 정규화시켰다.

  - 이렇게 $N$ 을 나눔으로써 "평균 손실 함수", 즉 손실 함수의 평균값이 구해지는 것이다.

  - 우리는 이로써 훈련 데이터의 개수에 관계없이 언제나 통일되고 일관된 손실함수 지표를 얻을 수 있게 되었다. 

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

미니배치 학습(mini-batch) : 실제로 수없이 많은 모든 데이터를 대상으로 손실함수의 합을 구하기에는 시간이 걸리기 때문에,

훈련 데이터의 일부만 추려서 "근사치" 로 손실함수를 계산하며 학습하는 과정이다.

</blockquote>

- 만약 데이터가 $20,0000$ 개가 있다면 이 모든 데이터에 대한 손실함수의 합의 평균을 구하면 너무 좋겠지만, 

  매번 그렇게 하기에 시간이 너무 오래걸린다. 
  
  따라서 가령 $100$ 개를 적절히 추출하여 그것에 대한 손실함수의 합의 평균으로 가중치 매개변수를 조정함으로써 학습하는 것이다.

- 예시 

  무작위로 100개의 데이터를 추출하는 미니배치 과정을 다음과 같이 간단히 구현할 수 있다. 

  위에서 계속 사용했었던 MNIST 손글씨 인식 코드의 맥락에서 작성된 코드이다.

  ```python
  train_size = x_train.shape[0]
  batch_size = 100
  batch_mask = np.random.choice(train_size, batch_size)
  x_batch = x_train[batch_mask]
  t_batch = t_train[batch_mask]
  ```

  가령 `np.random.choice(100, 3)` 은 $0 \sim 99$ 에서 $3$ 개의 무작위 수를 반환한다.

- 예시 

  미니배치를 했을 때 교차 엔트로피 오차를 구하는 코드는 다음과 같다. 교차 엔트로피의 원래 코드에서처럼 신경망의 출력 `y`, 정답 레이블 `t` 에 대한 코드이다. 
  
  만약 `y` 가 1차원이면, 즉 배치가 없다면, 즉, 데이터 하나당 교차 엔트로피 오차를 구하는 경우, `reshape` 함수로 데이터의 형상을 바꾸어 준다.

  계산이 다 되면 `batch_size` 로 나누어 정규화해줌으로써 이미지 1장당 평균 교차 엔트로피 오차, 즉 입력 하나 당 평균 교차 엔트로피 오차를 계산한다.

  ```python
  def CEE(y, t):
      if y.ndim == 1:
          t = t.reshape(1, t.size)
          y = y.reshape(1, y.size)
      batch_size = y.shape[0]
      return -np.sum(t * np.log(y + 1e-7)) / batch_size
  ```

- 예시

  반면 교차 엔트로피 오차 함수에 정답 레이블이 원-핫 인코딩이 아닌 숫자 $2$, 또는 $7$ 로 주어졌다면 다음과 같이 구현해야 한다.

  ```python
  def CEE(y, t):
      if y.ndim == 1:
          t = t.reshape(1, t.size)
          y = y.reshape(1, y.size)
      batch_size = y.shape[0]
      return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size
  ```