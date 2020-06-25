# <a name="Deep Learning from Scratch" href="#Deep Learning from Scratch">Deep Learning from Scratch</a>

[밑바닥부터 시작하는 딥러닝](https://book.naver.com/bookdb/book_detail.nhn?bid=11492334)의 개인 메모입니다.

# <a name="퍼셉트론 Perceptron" href="#퍼셉트론 Perceptron">퍼셉트론 Perceptron</a>

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

퍼셉트론(perceptron) 또는 인공뉴런 : 임의의 자연수 $n$ 에 대하여 $n$ 개의 실수 $x$(입력) 와 그 입력에 각각 대응되는 실수 $w$(가중치) 를 곱한 것을 모두 더한 실수 $z$(순입력) 가

실수 $\theta$(임계값) 보다 크면 $y=0$ 을 계산(출력)하고, 같거나 작으면 $y=1$ 을 계산(출력)하는 알고리즘(계산과정)이다.

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

- 퍼셉트론은 계산 가능하므로 코드로 자동화시킬 수 있다.

  - 예시 

    ```python
    def AND(x1, x2):
        w1, w2, theta = 0.5, 0.5, 0.7
        return int(x1*w1 + x2*w2 > theta)
    ```
  
  - 퍼셉트론 코드를 다음과 같이 일반적으로 나타낼 수 있다.

    ```python
    import numpy as np

    def perceptron(X, y, w = None):
        for xi, yi in zip(X, y):
          xi = xi
        return
    ```
