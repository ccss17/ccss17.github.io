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

  - 그러므로 원래는 $n$ 차원 벡터 $x = \begin{bmatrix} x_1\\x_2\\\dots\\x_n\end{bmatrix}$ (입력) 의 전치와 $n$ 차원 벡터 $w = \begin{bmatrix} w_1\\w_2\\\dots\\w_n\end{bmatrix}$ (가중치) 의 행렬곱(순입력)

    $$ x ^{T}w = \sum_{i=1}^{n} w _{i} x _{i} = z $$

    이 $z > \theta$ 이면 $y=1$ 로, $z \leq  \theta$ 이면 $y=0$ 로 계산했었다.
  
  - 그러나 임계값 $\theta$ 를 편향 $b$ 로 바꾸어 표현한 모델에서는 입력 $x_0 = 1$ 와 가중치 $w_0 = b$ 를 추가하여 
  
    $x_0=1$ 에 대한 $n+1$ 차원 벡터 $x = \begin{bmatrix} x_0\\x_1\\x_2\\\dots\\x_n\end{bmatrix}$ (입력) 의 전치와 
    
    $w_0 = b$ 에 대한 $n+1$ 차원 벡터 $w = \begin{bmatrix} w_0 \\ w_1\\w_2\\\dots\\w_n\end{bmatrix}$ (가중치) 의 행렬곱(순입력)

    $$ x ^{T}w = b + \sum_{i=1}^{n} w _{i} x _{i} =  \sum_{i=0}^{n} w _{i} x _{i} = z (\because b = x_0w_0 = 1 \cdot b)$$

    이 $z > 0$ 이면 $y=1$ 로, $z \leq  0$ 이면 $y=0$ 로 계산한다.

- 퍼셉트론이란 1957년 프랑크 로젠블라트(Frank Rosenblatt) 가 논문 《The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain》  고안한 알고리즘이다.

- 이 퍼셉트론이 신경망(딥러닝)의 기원이 되는 알고리즘이다.

- 이 퍼셉트론을 **인공뉴런**, **단순 퍼셉트론**으로 부르지면 여기서는 단순히 **퍼셉트론**이라고 하자.

- 이 퍼셉트론 알고리즘으로 할 수 있는 일이란 입력을 직선으로(선형적으로) 두 가지로 분류하는 것이다.

  - 퍼셉트론 알고리즘으로 직선으로, 즉 선형적으로 분류가 가능한 다음과 같은 단순한 문제들을 풀 수 있다. 
  
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

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

퍼셉트론 학습 알고리즘(Perceptron Learning Algorithm) : 퍼셉트론을 통하여 선형 분리 가능 문제를 해결하기 위한 가중치를 수렴시키는 알고리즘(계산과정)이다.

</blockquote>

- 퍼셉트론 학습 알고리즘은 다음과 같다. 이때 퍼셉트론 알고리즘의 목적은 입력 벡터 $x$ 를 올바르게 선형 분리하는 가중치 벡터 $w$ 를 구하는 것임을 상기하자.

1. (공리)

    임의의 자연수 $m$ 과 $i \in \{1,\dots,m\}$ 에 대한 $m$ 개의 불변요소인 입력 벡터 $\mathbf{x}^{(i)} \in \R ^{n}$, 

    무작위 값으로 초기화된 가변요소인 가중치 벡터 $\mathbf{w} \in \R ^{n}$, 

    $m$ 개의 입력 벡터에 대응되는 $i \in \{1,\dots,m\}$ 에 대한 클래스 레이블 $y ^{(i)} \in \{0,1\}$, 
    
    학습률 $\eta \in \R$ 가 있다. 

2. (연역) 

    계단함수 $h: \R \to \{0,1\}$ 와 $i$ 번째 입력벡터 $\mathbf{x}^{(i)}$ 대하여 출력(예측값) 
    
    $$\hat{y} ^{(i)} = h(\mathbf{x} ^{(i)} \cdot \mathbf{w})$$
    
    을 계산할 수 있다. 

    그런데 출력 $\hat{y} ^{(i)}$ 이 클레스 레이블 $y ^{(i)}$ 과 다르면 가변요소 가중치 벡터 $\mathbf{w}$ 를 조정해야 한다. 이때 로젠블라트는 다음과 같은 규칙으로 가중치를 조정하기로 결정했다.

    > 근데 뭔가 너무 "되겠지?.." 하고 던지는 마인드이긴 하다. 원래 정확한 계산을 통하여 얼마나 조정해야 하는지 알아낸 다음 그만큼 조정해야 하잖아. CTF 풀 때 입력 바이트를 0바이트부터 1000바이트까지 때려넣는 거랑 약간 비슷하네.

3. 에폭(학습횟수)이 남았거나 종료 조건(출력이 실제값과 다른 허용할만한 정도)이 충족되지 않으면 가중치 벡터 $\mathbf{w}$ 를 다음과 같이 조정한다.

    $$ \mathbf{w} := \mathbf{w} + \eta (y ^{(i)} - \hat{y} ^{(i)})\mathbf{x}^{(i)} $$

    그러므로 자연수 $j \in \{1,\dots,n\}$ 에 대한 가중치 벡터의 $j$ 번째 원소 $w_j$ 는 $i$ 번째 입력벡터 $\mathbf{x}^{(i)}$ 의 $j$ 번째 원소 $x_j ^{(i)}$ 에 대하여

    $$ w_j := w_j + \eta (y ^{(i)} - \hat{y}^{(i)}) x_j ^{(i)} $$

    와 같이 조정된다. $\Delta w_j = \eta (y ^{(i)} - \hat{y}^{(i)}) x_j ^{(i)}$ 로 두면

    $$ w_j := w_j + \Delta w_j $$

    로 쓸 수 있다.

    - 만약 정답 레이블 $y ^{(i)}$ 와 출력(예측값) $\hat{y} ^{(i)}$ 가 같으면 $\Delta w_j = 0$ 이 되므로 가중치는 
    
      $$w_j := w_j + 0$$ 
      
      이 되어 조정되지 않는다.

    - 만약 정답 레이블 $y ^{(i)}$ 이 출력(예측값) $\hat{y} ^{(i)}$ 보다 크면 $\Delta w_j = \eta ( 1 - (-1) ) x _j ^{(i)} = 2\eta x _j ^{(i)}$ 이 되어 가중치가

      $$ w_j := w_j + 2 \eta x _j ^{(i)}$$

      로 조정되면서 $2 \eta x _j ^{(i)}$ 만큼 증가한다.
    
    - 만약 정답 레이블 $y ^{(i)}$ 이 출력(예측값) $\hat{y} ^{(i)}$ 보다 작으면 $\Delta w_j = \eta ( -1 - 1 ) x _{j}^{(i)} = -2\eta x _j ^{(i)}$ 이 되어 가중치가

      $$ w_j := w_j - 2 \eta x _j ^{(i)} $$

      로 조정되면서 $2 \eta x _{j}^{(i)}$ 만큼 감소한다.
  
- 이때 $i$ 번째 입력벡터 $\mathbf{x}^{(i)}$ 의 $0$ 번째 입력을 $x_0 = 1$, $0$ 번째 가중치를 $w_0 = b$ 로 두어 인공뉴런의 편향을 벡터의 내적 계산에 포함시켜서 편하게 계산하기도 한다.

  - 예시 
  
    $\R ^{3}$ 공간의 입력벡터 $\mathbf{x}$, 가중치벡터 $\mathbf{w}$ 를 학습시킨다면(가중치를 조정한다면)

    $$ \Delta w_0 = \eta (y ^{(i)} - \hat{y}^{(i)}) $$

    $$ \Delta w_1 = \eta (y ^{(i)} - \hat{y}^{(i)})x_1 ^{(i)} $$

    $$ \Delta w_2 = \eta (y ^{(i)} - \hat{y}^{(i)})x_2 ^{(i)} $$

    와 같이 조정된다는 것이다. $0$번째 입력 $x_0 ^{(i)}$ 은 편향 $w_0 = b$ 를 나타내기 위하여 항상 $1$ 이기 때문이다.

- 예시 

  학습을 통하여 $\R ^{5}$ 공간의 예측 벡터 $\hat{y}$ 가 출력되었는데, 정답 벡터 $y$ 가 다음과 같다고 하자.

  $$ \hat{y} = (\hat{y_1},\hat{y_2},\hat{y_3},\hat{y_4},\hat{y_5}) = (1,-1,1,1,-1) $$

  $$ y = (y_1,y_2,y_3,y_4,y_5) = (1,-1,-1,1,-1) $$

  그러면 $3$ 번째 샘플이 다르기 때문에 $3$ 번째 가중치만 조정(학습)된다.

  $$\Delta w_3 = \eta ( -1 - 1 ) x = -2\eta x$$

- 예시 

  편향을 나타내기 위한 고정된 입력 $x_0 = 1$ 과 편향 $w_0 = b$ 과 계단함수 $h(x)$ 와 학습률 $\eta =1$ 에 대하여

  퍼셉트론의 입력 벡터 $x = (x_0 = 1, x_1 = 2, x_2 = 1)$, 가중치 $w = (w_0 = -1, w_1 = 0.5, w_2 = 0.3)$ 에 대한 출력(예측값)은 

  $$ \hat{y} = h(x \cdot w) = h(-1 + 2 \cdot 0.5 + 1 \cdot 0.3) = h(0.3) = 1 $$

  이다. 그런데 정답이 $y = 0$ 이라면 가중치는 다음과 같이 조정(학습)된다.

  $$ w_j = w_j + \eta (y - \hat{y})x $$

  $$ w_0 = -1 + 1 \cdot (0 - 1) \cdot 1 = -2 $$
        
  $$ w_1 = 0.5 + 1 \cdot (0 - 1) \cdot 2 = -1.5 $$
        
  $$ w_2 = 0.3 + 1 \cdot (0 - 1) \cdot 1 = -0.7 $$
        
<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

퍼셉트론 수렴 정리(perceptron convergence theorem) : 퍼셉트론이 선형 분리 가능 문제들, 즉 직선으로 분류가 가능한 데이터를

유한번의 학습으로 데이터를 잘 분류하는 가중치를 수렴시킬 수 있다 는 정리이다.

</blockquote>

- 퍼셉트론 수렴 정리는 다시 말해 퍼셉트론 학습 알고리즘이 선형적으로 분리할 수 있는 데이터를 올바르게 분류할 수 있는 가중치 벡터를 반드시 수렴시킬 수 있다는 것이다.

  선형적으로 분리 가능하다는 것은 특징(features) 의 선형결합을 통하여 데이터를 분류할 수 있다는 것이다.

- 그러나 비선형 분리 문제는 퍼셉트론이 자동으로 학습할 수 없다.

- 정리 

  > 참고/출처 : https://nbviewer.jupyter.org/github/metamath1/ml-simple-works/blob/master/perceptron/perceptron.ipynb

  "$\|\mathbf{w} ^{*}\|=1$ 인 계수벡터 $\mathbf{w} ^{*}$ 와 $\forall k \in \{1, \dots, n\}$ 에 대한 $k$ 번째 입력벡터 $\mathbf{x}_{k}$ 와 $k$ 번째 출력값을 나타내는 번째 스칼라 $y_k \in \{-1,1\}$ 에 대하여 

  $y_k(\mathbf{x}_{k}\cdot \mathbf{w}^{*}) \geq \gamma > 0$ 을 만족하는 $\gamma \in \R$ 가 존재하고, 
  
  $\|\mathbf{x}_{k}\| \leq R$ 인 $R \in \R$ 이 존재하면,

  퍼셉트론 알고리즘의 에러 $y_k \neq \hat{y}_{k} = \mathbf{x}_{k}\cdot \mathbf{w}^{*}$ 에 대한 에러 발생횟수 $\epsilon$ 은 $\epsilon \leq \dfrac{R ^{2}}{\gamma ^{2}}$ 이다."

  - 정리의 이해

    먼저 여기에서는 활성화함수로 양극성 계단함수 $\displaystyle y = h(x) = \begin{cases} 1 &x > 0\\ -1 &x \leq 0\\ \end{cases}$ 를 사용한다. 퍼셉트론 수렴 정리를 한줄씩 풀어서 이해해보자.

    ![](https://nbviewer.jupyter.org/github/metamath1/ml-simple-works/blob/master/perceptron/fig1.png)

    위 그림에서 $\mathbf{w} ^{*}$ 에 의해 결정되는 직선의 방정식은 붉은선이다. 이 붉은선이 모든 데이터를 올바르게 선형 분리하는 선이라고 하자. 그 직선의 방정식을 편향을 나타내기 위한 $w_0 = b, x_0 = 1$ 와 자유변수 $x_1, x_2$ 에 대한 $\mathbf{x} = \big <1, x_1, x_2\big >$ 와 가중치 벡터 $\mathbf{w} ^{*}=\big <b, w_1, w_2\big >$ 에 대하여 $x_1x_2$ 평면 위의 직선의 방정식

    $$ \mathbf{w} ^{*}\cdot \mathbf{x} = b + w_1x_1 + w_2x_2 = 0 $$

    으로 나타낼 수 있다. 
    
    퍼셉트론 알고리즘은 이와같은 가중치 벡터 $\mathbf{w} ^{*}$ 를 찾는 것이다. 만약 가중치 벡터 $\mathbf{w} ^{*}$ 를 찾았다면 이것을 사용하여 $k$번째 입력벡터 $\mathbf{x}_{k}$ 에 대하여 $\mathbf{w} ^{*}\cdot \mathbf{x} _{k} > 0$ 이면 빨간 직선의 위쪽, $\mathbf{w} ^{*}\cdot \mathbf{x} _{k} < 0$ 이면 빨간 직선의 아래쪽에 위치한다고 판별할 수 있다.

    그렇다면 가중치 벡터 $\mathbf{w}^{*}$ 가 존재하여 $y_k(\mathbf{w}^{*}\cdot \mathbf{x}_{k}) = y_k \hat{y_k} \geq \gamma > 0$ 인 $\gamma$ 가 있다는 것은 $\mathbf{w}^{*}$ 가 데이터를 $2$개의 클래스로 잘 선형분리 하고 있다는 것이다.
    
    왜냐하면 $y_k$ 가 직선의 방정식 위쪽에 위치했다면 $y_k > 0$ 인데 예측값 $\hat{y_k} = \mathbf{w}^{*}\cdot \mathbf{x}_k$ 도 데이터가 위쪽에 있다고 판별했으면 $\hat{y_k} = \mathbf{w}^{*}\cdot \mathbf{x}_k > 0$ 이 되어 $y_k \hat{y_k} > 0$ 이 되고,

    $y_k$ 가 직선의 방정식 아래쪽에 위치했다면 $y_k < 0$ 인데 예측값 $\hat{y_k} = \mathbf{w}^{*}\cdot \mathbf{x}_k$ 도 데이터가 아래쪽에 있다고 판별했으면 $\hat{y_k} = \mathbf{w}^{*}\cdot \mathbf{x}_k < 0$ 이 되어 $y_k \hat{y_k} > 0$ 이 되기 때문에

    $\mathbf{w}^{*}$ 가 데이터를 잘 선형분리하고 있다면 항상 $y_k \hat{y_k} > 0$ 가 될 것이기 때문이다.

    이때 결과값, 즉 $\mathbf{w}^{*}\cdot \mathbf{x}_{k}$ 이 $0$ 에 가까울수록 직선의 방정식과의 거리가 가까워진다. 그러므로 $\gamma$ 는 아무리 커봤자 직선의 방정식과 거리가 가장 가까운 입력 벡터 $\mathbf{x}_{k}$ 와 직선의 방정식과의 거리이다. 

    또한 입력 벡터 $\mathbf{x}_{k}$ 의 크기, 즉 $\|\mathbf{x}_{k}\|$ 와 같거나 큰 $R \in \R$ 을 정할 수 있다.

    이 조건이 충족되면 퍼셉트론 알고리즘이 최대 $\dfrac{R ^{2}}{\gamma ^{2}}$ 번만에 데이터를 잘 선형분리하는 계수 벡터 $\mathbf{w}^{*}$ 를 찾을 수 있다. 

- 증명

  > 참고/출처 : https://nbviewer.jupyter.org/github/metamath1/ml-simple-works/blob/master/perceptron/perceptron.ipynb

  > 참고/출처 : 알고리즘 중심의 머신러닝 가이드Machine Learning: An Algorithmic Perspective, 2nd ed., 스티븐 마슬랜드

  > 참고/출처 : http://www.cs.columbia.edu/~mcollins/courses/6998-2012/notes/perc.converge.pdf

  $y_k(\mathbf{x}_{k}\cdot \mathbf{w}^{*}) \geq \gamma > 0$ 을 만족하는 $\gamma \in \R$ 가 존재하므로 데이터를 잘 선형분리시킬 수 있는 $\mathbf{w}^{*}$ 가 존재한다. 퍼셉트론 알고리즘은 가중치 학습을 반복하면서 $\mathbf{w} ^{*}$ 을 찾으려할텐데 이때 $t$번째 학습에서의 가중치 $\mathbf{w} ^{(t)}$ 가 $\mathbf{w}^{*}$ 와 평행하다면 두 벡터의 사이각이 $0$ 가 되어 $\mathbf{w}^{*}\cdot \mathbf{w} ^{(t)}$ 값이 최대가 된다.

  그러므로 매 학습마다 두 벡터 $\mathbf{w}^{*}, \mathbf{w} ^{(t)}$ 의 내적값이 증가함을 보이면 가중치가 수렴하고 있음을 보인느 것이 된다. 이때 두 벡터의 각도가 줄어듦으로써 내적값이 증가하는 것이 아니라 $\mathbf{w} ^{(t)}$ 의 값 자체가 커져서 내적값이 증가할 수도 있기 때문에 $\mathbf{w} ^{(t)}$ 의 크기 상한값도 함께 보여야 가중치가 수렴한다고 말할 수 있다.

  만약 $t$번째 반복에서 $k$번째 입력 벡터 $\mathbf{x}_{k}$ 와 그것의 클래스 레이블 $y _{k}$ 에 대하여 $y _{k}(\mathbf{w} ^{(t-1)} \cdot \mathbf{x}_{k}) < 0$ 이 되었다면 에러가 발생한 것이므로 가중치를 조정해야 한다. 퍼셉트론 알고리즘에서 가중치 조정은 

  $$ \mathbf{w} ^{(t)} := \mathbf{w}^{(t-1)} + \eta (y _{k} - \hat{y} _{k})\mathbf{x}_{k} $$

  와 같이 이루어졌다는 것을 기억하자. 이때 $\eta = 1$ 로 두고 퍼셉트론의 예측값 $\hat{y}_{k}$ 는 편의를 위하여 제거하자. 그렇게 해도 양이 어느정도 바뀔 뿐 부호는 바뀌지 않으므로 가중치 조정이 가능하기 때문이다. 그러면 가중치 조정은

  $$ \mathbf{w}^{(t)} := \mathbf{w}^{(t-1)} + y _{k}\mathbf{x}_{k} $$

  와 같이 이루어진다. 그러면 이때 두 벡터 $\mathbf{w}^{*}, \mathbf{w}^{(t)}$ 의 내적값을 계산해보면

  $$ \mathbf{w}^{*}\cdot \mathbf{w}^{(t)} = \mathbf{w}^{*}\cdot (\mathbf{w}^{(t-1)}+y _{k} \mathbf{x}_{k}) $$

  $$ = \mathbf{w}^{*}\cdot \mathbf{w}^{(t-1)}+y _{k} \mathbf{w}^{*}\cdot \mathbf{x}_{k} $$

  $$ \geq  \mathbf{w}^{*}\cdot \mathbf{w}^{(t-1)} + \gamma \ \ (\because y_k(\mathbf{x}_{k}\cdot \mathbf{w}^{*}) \geq \gamma ) $$

  이다. 즉, $\mathbf{w}^{*}\cdot \mathbf{w}^{(t)}- \mathbf{w}^{*}\cdot \mathbf{w}^{(t-1)} \geq  \gamma > 0$ 이므로 $\mathbf{w}^{*}\cdot \mathbf{w}^{(t)}$ 이 $\mathbf{w}^{*}\cdot \mathbf{w}^{(t-1)}$ 보다 $\gamma$ 이상 크다는 것이다. 이로써 매 학습마다 $\mathbf{w}^{*}\cdot \mathbf{w}^{(t)}$ 가 증가한다는 것이, 즉 가중치 벡터가 수렴되고 있다는 것이 증명되었다. ▲ 

  매 학습마다 내적 $\mathbf{w}^{*}\cdot \mathbf{w}^{(t)}$ 의 값이 최소 $\gamma$ 이상 증가하기 때문에 초기 가중치 벡터를 $\|\mathbf{w}^{0}\| = 0$ 로 두면 $t$번 학습 후 내적값이 

  $$ \mathbf{w}^{*}\cdot \mathbf{w}^{(t)} \geq t \gamma $$

  이라는 것 즉, 최소 $t \gamma$ 이상이라는 것을 알 수 있다. 그런데 코시-슈바르츠 부등식에 의해 

  $$ \|\mathbf{w}^{*}\|\|\mathbf{w}^{(t)}\| \geq \mathbf{w}^{*}\cdot \mathbf{w}^{(t)} $$ 

  인데 $\|\mathbf{w}^{*}\| = 1$ 이므로 $\|\mathbf{w}^{(t)}\| \geq \mathbf{w}^{*}\cdot \mathbf{w}^{(t)} \geq t \gamma$ 에서 

  $$\|\mathbf{w}^{(t)}\| \geq t \gamma$$

  이다. 그러므로 $t \gamma$ 가 $\|\mathbf{w}^{(t)}\|$ 의 최대하계, 즉 하한

  $$ \therefore \inf \| \mathbf{w}^{(t)}\| = t \gamma $$

  이 된다. ▲ 

  $t$번째 학습 이후 가중치 벡터 $\mathbf{w}^{(t)}$ 의 길이의 제곱은 

  $$ \|\mathbf{w}^{(t)}\|^{2} = \|\mathbf{w}^{(t-1)} + y _{k} \mathbf{x} _{k}\|^{2} $$

  $$ = \|\mathbf{w}^{(t-1)}\| ^{2} + y _{k} ^{2} \|\mathbf{x} _{k}\| ^{2} + 2y _{k} \mathbf{w}^{(t-1)}\cdot  \mathbf{x} _{k} $$

  인데 $y _{k} \in \{-1,1\}$ 이므로 $y _{k}^{2} = 1$ 이고 $\|x _{k}\| \leq R \implies \|x _{k}\|^{2}\leq R ^{2}$ 이고 예측값이 출력값과 틀렸으므로 $y _{k} \mathbf{w}^{(t-1)} \cdot \mathbf{x} = y _{k}\hat{y}_{k} < 0$ 이다. 따라서

  $$ \|\mathbf{w}^{(t)}\| ^{2} \leq  \|\mathbf{w}^{(t-1)}\| ^{2} + R ^{2} $$

  이다. 즉, $\|\mathbf{w}^{(t)}\| ^{2} - \|\mathbf{w}^{(t-1)}\| ^{2} \leq  R ^{2}$ 이므로 초기 가중치 벡터를 $\| \mathbf{w}^{0}\| = 0$ 로 두면 $t$ 번은 학습은 다음과 같이 이루어진다.

  $$ \|\mathbf{w}^{1}\|^{2} - \|\mathbf{w}^{0}\| ^{2} \leq R ^{2} $$

  $$ \|\mathbf{w}^{2}\|^{2} - \|\mathbf{w}^{1}\| ^{2} \leq R ^{2} $$

  $$ \dots $$

  $$ \|\mathbf{w}^{(t)}\|^{2} - \|\mathbf{w}^{(t-1)}\| ^{2} \leq R ^{2} $$

  이것들을 모두 더하면

  $$ \|\mathbf{w}^{(t)}\|^{2} \leq t R ^{2} $$

  을 얻는다. 이것이 $\|\mathbf{w}\|^{2}$ 의 최소상계, 즉 상한

  $$ \sup \|\mathbf{w}^{(t)}\| ^{2} = t R ^{2} $$
  
  이다. ▲ 

  상한과 하한을 같은 부등식에 쓰면 다음과 같다. 

  $$ (\inf \|\mathbf{w}^{(t)}\|) ^{2} \leq \|\mathbf{w}^{(t)}\|^{2} \leq \sup \|\mathbf{w}^{(t)}\|^{2} $$

  $$ \iff t ^{2} \gamma ^{2} \leq \|\mathbf{w}^{(t)}\|^{2} \leq t R ^{2} $$

  여기에서 

  $$ \iff t \leq \dfrac{R ^{2}}{\gamma ^{2}} $$

  를 얻는다. 이것은 곧 학습 횟수 $t$ 가 상계를 갖는다는 것이므로 
  
  결과적으로 선형분리 가능 데이터에 조건 $\eta =1, \|\mathbf{w}^{0}\| = 0$ 을 적용하면 퍼셉트론 알고리즘이 유한번의 학습으로, 즉 최대 $\dfrac{R ^{2}}{\gamma ^{2}}$ 번의 학습으로(에러로) 가중치 매개변수 $\mathbf{w}$ 를 최적의 가중치 벡터 $\mathbf{w}^{*}$ 로 수렴시킬 수 있다는 것이다. ■   

  - 이는 분류해야 하는 클래스간 거리가 가까울수록 알고리즘 반복 횟수(학습횟수, 에러횟수)는 늘어나지만 어쨌든 수렴은 한다는 것을 보여준다.

  > $\gamma$ 가 늘어날수록 학습횟수가 줄어들고, $R$ 이 늘어날수록 학습횟수가 많아지는구나.

  > 또한 그렇다면 이것은 선형분리가 불가능한 문제이더라도 좌표변환으로써 결국 선형분리 문제로 회귀시키면 비선형문제라도 잘 분류할 수 있는 가중치 벡터를 수렴시킬 수 있다는 뜻이구나. 가령 $XOR$ 문제를 좌표변환으로써 선형분리 문제로 사상시키는 것이다.

  > 벡터의 크기의 제곱의 연산에 대한 정리, 코시-슈바르츠 부등식의 벡터 표현 -> semi-inner-product , 하한의 제곱

  > 코시 슈바르츠 부등식 https://namu.wiki/w/%EC%BD%94%EC%8B%9C-%EC%8A%88%EB%B0%94%EB%A5%B4%EC%B8%A0%20%EB%B6%80%EB%93%B1%EC%8B%9D#toc , https://proofwiki.org/wiki/Cauchy-Bunyakovsky-Schwarz_Inequality

- **그러면 이로썬 선형분리 문제는 항상 가중치를 수렴시킬 수 있다는 것을 알게 되었다. 그러면 임의의 데이터가 선형분리되는지 판단할 수 있는 알고리즘은 존재할까?** 

  **만약 존재하지 않으면 레이어를 하나 더 추가하여 좌표변환(공간변환)을 해보고, 또 존재하지 않으면 레이어를 또 추가해서 공간변환을 또 해보고... 그렇게 자동으로 네트워크를 생성해볼 수 있으니까.**

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

    가령 입력 벡터를 $1 \times 2$ 행렬 $X = \begin{pmatrix} x_1&x_2 \end{pmatrix}$, 가중치를 $2 \times 3$ 행렬 $W=\begin{pmatrix} w _{11}&w _{21}&w _{31}\\w _{12}&w _{22}&w _{32} \end{pmatrix}$, 편향을 $1 \times 3$ 행렬 $B = \begin{pmatrix} b _{1}&b _{2} & b _{3}\\ \end{pmatrix}$ 으로 나타낸다면, 순입력 $Z = \begin{pmatrix} z_1&z_2&z_3\\ \end{pmatrix}$ 를 다음과 같이 계산할 수 있다. 

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

  에 임의의 정수 $C$ 를 분자와 분모에 곱하여

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

    # 앞의 두 반환값 _, _ 은 훈련 데이터와 훈련 정답 레이블이다. 여기서는 이미 훈련된 가중치로 추론, 즉 순전파만 테스트할 것이기 때문에 시험 데이터 x 와 시험 정답 레이블 t 만 가져온다.
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

과적합(overfitting) : 신경망이 특정 데이터셋에 과하게 최적화된 상태이다.

</blockquote>

# <a name="손실함수" href="#손실함수">손실함수</a>

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

손실함수(loss function) : 현재의 신경망이 데이터를 얼마나 처리하지 못하는지를 출력하는 함수이다.

</blockquote>

- 이 손실함수를 통하여 가중치 매개변수들을 얼마나 조정해야 하는지 알 수 있다.

- 손실함수로 임의의 함수를 사용할 수 있으나, 

  일반적으로 평균 제곱 오차와 교차 엔트로피 오차를 사용한다.

- 출력의 정확도라는 지표 대신 손실함수 값이라는 간접적인 지표를 사용하는 이유는 이렇다.

  신경망 학습에서는 최적의 매개변수(가중치, 편향(임계값)) 을 찾기 위하여 손실 함수 값을 최대한 적게 만드는 매개변수 값을 찾는다. 이때 매개변수의 미분(기울기)를 계산하여 그 미분값을 단서로 매개변수의 값을 서서히 갱신해나간다.

  즉, 어떤 신경망의 가중치 매개변수의 손실 함수의 미분이란 "이 가중치 매개변수를 아주 조금 변화시켰을 때, 손실 함수가 어떻게 변하는가" 에 대한 대답입니다.

  미분 값이 음수면 그 가중치를 양의 방향으로 변화시켜 손실함수 값을 줄이고, 
  
  미분 값이 양수면 그 가중치를 음의 반향으로 변화시켜 손실함수 값을 줄인다.

  그런데 미분 값이 $0$ 이면 가중치를 바꿔도 손실함수 값이 바뀌지 않으므로 가중치 갱신(학습) 이 끝난다.

  그런데 "출력의 정확도" 를 지표로 삼으면 미분 값이 대부분의 장소에서 $0$ 이 되어 매개변수를 제대로 갱싱할 수 없다.

  - "출력의 정확도" 를 지표로 매개변수의 미분을 구하면 대부분의 장소에서 $0$ 이 되는 이유는 이렇다.

    어떤 신경망이 $100$ 개의 훈련 데이터 중에서 $12$ 개만 제대로 인식한다고 가정하자. 이때의 정확도는 $12\%$ 이다. 만약 정확도가 지표였다면 가중치 매개변수의 값을 조금 조정해도 정확도는 여전히 $12\%$ 이다. 

    정확도가 개선된다고 하더라도 그 값이 $12.023\%$ 같은 연속적인 값이 아니라 $13\%$ 같은 불연속적인 값으로 변한다. 이에 따라 가중치를 조금 바꾸어도 정확도가 변하지 않는다는 결론이 나와버리는 것이다. 

    - 그리고 이것은 계단 함수를 활성화함수로 사용하지 않게 된 이유와도 같다.

      계단함수는 불연속적으로 갑자기 변하지만, 시그모이드 함수는 출력이 연속적으로 변하고 기울기도 연속적으로 변한다. 이에 따라 시그모이드 함수의 미분은 어느 장소에서도 $0$ 이 되지 않는다.

      기울기가 $0$ 이 되지 않아서 시그모이드 함수로 신경망이 올바르게 학습할 수 있는 것이다.

### <a name="**<center>아 이게 시그모이드 함수를 활성화 함수로 사용하는 이유구나.</center>**" href="#**<center>아 이게 시그모이드 함수를 활성화 함수로 사용하는 이유구나.</center>**">**<center>아 이게 시그모이드 함수를 활성화 함수로 사용하는 이유구나.</center>**</a>

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

교차 엔트로피 오차(cross entropy error, CEE) : 신경망의 출력 $y _{k}$, 원-핫 인코딩된 정답 레이블 $t _{k}$, 데이터의 차원 수 $k$ 에 대한 손실함수

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

  이처럼 데이터에 따라 같은 교차 엔트로피 오차 함수 계산을 할 때도 처리를 다르게 해주어야 한다.

  - `y[np.arange(batch_size), t]` 의 의미는 배치처리에서도 다음과 같다. 

    먼저 `np.arange(50)` 은 다음과 같이 $0$ 부터 $49$ 까지의 배열을 생성한다.
    
    ```python
    >>> np.arange(50)
    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
          17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
          34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49])
    ```

    이것을 `a = np.arange(50).reshape([25, 2])` 로 저장한다고 하자. 그러면 $25$ 행, $2$ 열인 행렬이 생성된다. 

    ```python
    >>> np.arange(50).reshape([25, 2])
    array([[ 0,  1],
          [ 2,  3],
          [ 4,  5],
          [ 6,  7],
          [ 8,  9],
          [10, 11],
          [12, 13],
          [14, 15],
          [16, 17],
          [18, 19],
          [20, 21],
          [22, 23],
          [24, 25],
          [26, 27],
          [28, 29],
          [30, 31],
          [32, 33],
          [34, 35],
          [36, 37],
          [38, 39],
          [40, 41],
          [42, 43],
          [44, 45],
          [46, 47],
          [48, 49]])
    ```

    이제 이 행렬에서 $0$ 행을 가져오자.

    ```python
    >>> np.arange(50).reshape([25, 2])[0]
    array([ 0,  1])
    ```

    이때 $0$ 행 $1$ 열을 가져오면 다음과 같다.

    ```python
    >>> np.arange(50).reshape([25, 2])[0, 1]
    1
    ```

    넘파이는 임의의 행을 가져올 수 있는 인덱싱 방식을 제공한다. $0$ 행과 $1$ 행을 가져와보자.

    ```python
    >>> np.arange(50).reshape([25, 2])[[0, 1]]
    array([[0, 1],
           [2, 3]])
    ```

    마찬가지로 다음과 같이 $0$ 행과 $5$ 행도 가져올 수 있다.

    ```python
    >>> np.arange(50).reshape([25, 2])[[0, 5]]
    array([[0, 1],
           [10, 11]])
    ```

    그러므로 다음 코드는 $0,1,2$ 행을 가져온다.

    ```python
    >>> np.arange(50).reshape([25, 2])[np.arange(3)]
    array([[0, 1],
           [2, 3],
           [4, 5]])
    ```

    이렇게 가져와진 $0,1,2$ 해에서 $0$ 열을 가져오면 다음과 같다.

    ```python
    >>> np.arange(50).reshape([25, 2])[np.arange(3), 0]
    array([0, 2, 4])
    ```

    다음과 같이 $1$ 열도 가져올 수 있다.

    ```python
    >>> np.arange(50).reshape([25, 2])[np.arange(3), 1]
    array([1, 3, 5])
    ```

    그런데 열을 가져오는 인덱싱에도 숫자가 아닌 배열을 전달하면 각각의 행에 부합하는 원소를 인덱싱할 수 있다. 다음과 같이 $0,1,2$ 행에 대하여 $0,1,1$ 열을 가져올 수 있다는 것이다.

    ```python
    >>> np.arange(50).reshape([25, 2])[np.arange(3), [0, 1, 1]]
    array([0, 3, 5])   
    ```

  - 그러므로 `y[np.arange(batch_size), t]` 의 의미는 `y` 에서 `0` 행부터 `batch_size-1` 행에서 `t` 열을 가져온 것이다. 
    
    그런데 `y` 는 출력이었고, `t` 는 손글씨의 정답 레이블로써 `[2,7,0,9,4]` 였다. 그러므로 결과적으로 출력층에서 정답에 해당하는 출력을 가져온 것이 된다.

    즉, `[y[0, 2], y[1, 7], y[2, 0], y[3, 9], y[4, 4]]` 인 배열을 생성한 것이 된다.
  
# <a name="미분 " href="#미분 ">미분 </a>

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

해석적 미분 : 수학에서의 미분으로써 한순간의 변화량을 표현한 것

$$ \dfrac{df(x)}{dx} = \lim_{h \to 0} \dfrac{f(x+h)-f(x)}{h} $$

이다.

</blockquote>

- 예시 

  달리기 선수가 $10$분에 $2$ km 를 뛰었다고 하자. 그러면 속도는 $\dfrac{2}{10} = 0.2$ [km/m] 그런데 이것은 평균 속도, 즉 평균 변화량이다. 
  
  우리는 $10$분이라는 시간을 $1$분동안 달린 거리, $1$초 동안 달린 거리, $0.1$초 동안 달린 거리, $\dots$ 로 줄여나가면서 순간적인 속도, 즉 순간 변화량을 구하려 한다.

  이것은 다음과 같이

  $$ \dfrac{df(x)}{dx} = \lim_{h \to 0} \dfrac{f(x+h)-f(x)}{h} $$

  시간 $x$ 의 아주 작은 변화량 $dx$ 에 따라서 거리 $f(x)$ 의 아주 작은 변화량 $df(x)$ 가 얼마나 변했는지 표현할 수 있다. 그리고 이것을 수식적으로 시간 $h$ 가 $0$ 에 수렴할 때 평균변화량 이 순간변화량이 되기 때문에

  $$ \lim_{h \to 0} \dfrac{f(x+h)-f(x)}{h} $$

  라고 표현할 수도 있다.

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

수치 미분(numerical differentiation) : 컴퓨터에서 미분을 계산할 때 실제로 $0$ 에 수렴하는 차분을 사용할 수 없으므로 매우 작은 차분을 사용하여 미분을 하는 것

$$ \lim_{h \to 0} \dfrac{f(x+h)-f(x-h)}{2h} $$

이다.

</blockquote>

- 해석적 미분의 달리기 선수 예시의 순간변화량을 코드로 

  ```python
  def df(f, x):
      h = 10e-50 # 거의 0 에 수렴하는 엄청 작은 값
      return (f(x + h) - f(x)) / h
  ```

  라고 구현하면 다음의 두 가지가 에러가 발생한다.
  
  1. 반올림 오차가 발생한다. 반올림 오차는 작은 값이 생략되어 최종 계산 결과에 오차가 생기게 되는 것이다.

      따라서 반올림 오차가 발생하지 않도록 너무 작은 값을 사용하는 것보다 $10 ^{-4}$ 정도의 값을 사용해야 한다.
  
  2. 수학에서 엄밀한 미분이란 $h$ 가 $0$ 에 진정으로 수렴하기 때문에 $x+h$ 와 $x$ 로 수식을 표현할 수 있었다.
  
      하지만 코드에서는 $h$ 를 $0$ 으로 수렴시키지 못하기 때문에 $x+h$ 와 $x$ 로 순간변화율을 구하는 것이 아니라 $x+h$ 와 $x-h$ 로 순간변화율을 구해야 한다.

- 그래서 이 두 가지 에러를 해결하여 

  ```python
  def df(f, x):
      h = 1e-4 #0.0001
      return (f(x+h) - f(x-h)) / (2*h)
  ```

  로 최종 미분 코드를 짤 수 있다.

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

반올림 오차 : 작은 값이 생략되어 최종 계산 결과에 오차가 생기게 되는 것이다.

</blockquote>

- 예시 

  아주 작은 값을 컴퓨터가 처리하기 어려워서 다음과 같이 오차가 생기는 것이다.

  ```python
  >>> np.float32(1e-50)
  0.0
  ```

- 컴퓨터로 미분할 때 엄청나게 작은 값을 사용하는 게 아니라 $10 ^{-4}$ 정도의 값을 사용하면 반올림 오차도 생기지 않고 적당히 좋은 결과를 얻는다는 사실이 알려져있다.

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

중심 차분(중앙 차분) : 미분 $\displaystyle \lim_{h \to 0} \dfrac{f(x+h)-f(x)}{h}$ 을 컴퓨터 코드로 구현할 때 $h$ 를 실제로 $0$ 에 수렴시키지 못하기 때문에

$$\displaystyle \lim_{h \to 0} \dfrac{f(x+h)-f(x-h)}{2h}$$

로 미분을 구하여 오차를 최소화시키는 방식이다.

</blockquote>

- 설명 

  수학에서의 원래 미분은 차분 $h$ 를 $0$ 에 수렴시킬 수 있기 때문에

  $$\displaystyle \dfrac{df(x)}{dx} = \lim_{h \to 0} \dfrac{f(x+h)-f(x)}{h}$$

  를 사용했었다. 이것은 두 점 $(x, f(x)), (x+h, f(x+h))$ 으로 생성된 직선을 $h$ 를 $0$ 으로 수렴시켜 접선으로 만들어 기울기를 구하는 것이었다.

  하지만 수치미분에서 기울기의 오차를 줄이기 위하여 두 점 $(x-h, f(x-h)), (x+h, f(x+h))$ 으로 생성된 직선의 기울기를 구한다. 따라서 

  $$ \dfrac{f(x+h) - f(x-h)}{(x+h) - (x-h)} = \dfrac{f(x+h)-f(x-h)}{2h} $$

  에서 $h$ 를 $0$ 으로 최대한 수렴시킨 

  $$\displaystyle \lim_{h \to 0} \dfrac{f(x+h)-f(x-h)}{2h}$$

  을 사용하는 것이다.

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

편미분 코드 구현

</blockquote>

- 먼저 이변수 함수 $f(x_0, x_1) = x _{0} ^{2} + x _{1} ^{2}$ 는 `numpy` 배열 `x` 에 대하여 다음과 같이 간단히 코드로 사상시킬 수 있다.

  ```python
  def f(x):
      return x[0]**2 + x[1]**2
      # return np.sum(x ** 2)
  ```

  - 이때 점 $(x _{0}, x _{1}) = (3, 4)$ 에서 $x _{0}$ 에 대한 편미분계수를 구해보자.

    이변수 함수 $f(x _{0}, x _{1})$ 를 $x _{0}$ 에 대하여 편미분 하면 

    $$ f _{x_0}(x _{0}, x _{1}) = \dfrac{\partial f(x _{0}, x _{1})}{\partial x _{0}} = 2 x _{0} $$

    이다. 이것은 변수 $x _{0}$ 에 따른, 곡면 $f(x _{0}, x _{1})$ 과 $x _{0}$ 축에 평행한 평면과의 교선의 접선의 기울기이다. 이것을 다음과 같이 간단히 코드로 구현할 수 있다.

    ```python
    def f1(x0, x1):
        return 2 * x0
    ```

    이변수니까 명목상 $x _{0}, x _{1}$ 을 입력으로 받지만 $x _{1}$ 는 편미분과정에서 사라져서 아무 처리를 받지 않는 것이다.

    그러면 그냥 단순히 `f1(3, 4)` 를 구하면 `6` 이 계산된다. 이것은 해석적 미분과 동일한 값이다.

  - 이제 수치미분으로 점 $(x _{0}, x _{1}) = (3, 4)$ 에서 $x _{0}$ 에 대한 편미분계수를 구해보자.

    수치 미분에서 완성한 코드

    ```python
    def df(f, x):
        h = 1e-4 #0.0001
        return (f(x+h) - f(x-h)) / (2*h)
    ```

    를 사용하자.

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

기울기 벡터 코드 구현

</blockquote>

- 예시  

  점 $P(x_0, x_1) = (3, 4)$ 에서 이변수 함수 $f$ 에 대한 기울기 $\bigg (\dfrac{\partial f}{\partial  x_0}, \dfrac{\partial f}{\partial x_1}\bigg )$ 을 계산해보자.

  ```python
  import numpy as np

  def numerical_gradient(f, x):
      h = 1e-4
      grad = np.zeros_like(x)

      for idx in range(x.size):
          tmp_val = x[idx]
          # f(x+h) 계산
          x[idx] = tmp_val+h
          fxh1 = f(x)

          # f(x-h) 계산
          x[idx] = tmp_val-h
          fxh2 = f(x)

          grad[idx] = (fxh1 - fxh2) / (2+h)
          x[idx] = tmp_val # 값 복원
      
      return grad
  ```

# <a name="경사 하강법 " href="#경사 하강법 ">경사 하강법 </a>

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

경사법 : 기울기 벡터를 사용하여 손실함수 값을 최소로 만드는 방법을 찾는 알고리즘이다.

</blockquote>

- 하지만 기울기가 가리키는 곳에 함수의 최솟값이 존재하는지 확신할 수 없다. 실제로 복잡한 함수에서는 기울기가 가르키는 방향에 최솟값이 없는 경우가 대부분이다. 또 복잡하고 찌그러진 함수에서 평평한 곳으로 파고들면 고원(plateau)이라고 하는 학습이 정체되는 공간에 수렴할 수도 있다.

  기울기의 방향이 반드시 최소값을 가르키는 것은 아니지만 일단 그 방향으로 가면 함수의 값을 줄일 수 있기 때문에 일단 기울기를 단서로 나아갈 방향을 정하는 것이다.
  
  경사법에서는 그 기울기 방향으로 일정 거리만큼 이동하여 또 기울기를 구한다. 그런데 기울어져 있으면 또 그방향으로 일정 거리 나아가본다. 이렇게 계속 기울기 방향으로 나아가서 손실 함수 값을 줄여보는 것이 경사법이다.

- 최솟값을 찾는다면 그것을 경사하강법(gradient descent method)이라고 하고, 최댓값을 찾는다면 경사 상승법(gradient ascent method)이라고한다.

- 경사법을 수식으로 나타내면 학습률 $\eta \in \R$ 과 가중치 벡터 $\mathbf{w} \in \R ^{n}$ 에 대하여

  > 학습률은 하이퍼파라미터이다. 이는 가중치와 편향 같은 신경망 내부에서 자동으로 결정되는 매개변수와는 달리 사람이 직접 설정해야 하는 매개변수이다.

  $$ \mathbf{w} := \mathbf{w} - \eta \dfrac{\partial f}{\partial \mathbf{w}} $$

  이다. 즉, 가중치 벡터 $\mathbf{w}$ 의 $k$번째 원소에 대하여

  $$ w_k := w_k - \eta \dfrac{\partial f}{\partial w_k} $$

  이다. 
  
  - 이것을 최적화하려는 함수 `f`, 초기값 `init_x`, 학습률 `lr`, 경사법 반복 회수 `epoch` 에 대하여 다음과 같이 코드로 간단히 구현할 수 있다. 

    ```python
    def gradient_descent(f, init_x, lr=0.01, epoch=100):
        x = init_x
        for _ in range(epoch):
            grad = numerical_gradient(f, x)
            x -= lr * grad
        return x
    ```

    이 함수로 극소값을 구할 수 있고, 운좋으면 최소값을 구할 수 있다.
  
- 신경망에서의 경사법은 손실함수 $L$ 에 대하여 가중치 행렬 $W$ 의 미분을 구하는 것이다.

  - 예시 

    $2 \times 3$ 행렬 $W$ 가 

    $$ W = \begin{pmatrix} w _{11}&w _{12}&w _{13}\\w _{21}& w _{22}& w _{23} \end{pmatrix} $$

    일 때 기울기는 

    $$ \dfrac{\partial L}{\partial W} = \begin{pmatrix} \dfrac{\partial L}{\partial w _{11}}& \dfrac{\partial L}{\partial w _{12}}& \dfrac{\partial L}{\partial w _{13}} \\ \dfrac{\partial L}{\partial w _{21}}& \dfrac{\partial L}{\partial w _{22}}& \dfrac{\partial L}{\partial w _{23}} \end{pmatrix} $$

    이다. 1행의 첫번째 원소 $\dfrac{\partial L}{\partial w _{11}}$ 는 $w _{11}$ 을 아주 조금 변경했을 때 손실함수값 $L$ 이 얼마나 변하는지를 나타내준다.
  
  - 코드 구현 

    신경망의 기울기를 구하는 코드를 실제로 구현해보자.

    ```python
    class simpleNet:
        def __init__(self):
            self.W = np.random.randn(2, 3)

        def predict(self, x):
            return np.dot(x, self.W)
        
        def loss(self, x, t):
            z = self.predict(x)
            y = softmax(z)
            loss = CEE(y, t)
            return loss
    
    
    net = simpleNet
    x = np.array([0.6, 0.9])  # 입력
    t = np.array([0, 0, 1])   # 정답 레이블
    p = net.predict(x)

    f = lambda w: net.loss(x, t)
    
    dW = numerical_gradient(f, net.W)
    print(dW) # 기울기 벡터 출력
    # [[0.21, 0.14, -0.36] 
    #  [0.32, 0.21, -0.54]]
    ```

    이를 통해 $\dfrac{\partial L}{\partial w _{11}} \approx 0.2$ 임을 알 수 있다. 이는 $w _{11}$ 을 $h$ 만큼 늘리면 손실함수 값은 $0.2h$ 만큼 증가한다는 것이다.

    또한 $\dfrac{\partial L}{\partial w _{23}} \approx -0.5$ 임을 알 수 있다. 이는 $w _{23}$ 을 $h$ 만큼 늘리면 손실함수 값은 $-0.5h$ 만큼 증가한다는 것이다.

    이로써 $w _{11}$ 는 음의 방향으로 갱신해야 손실함수 값이 감소하고, $w _{23}$ 은 양의 방향으로 조정해야 손실함수 값이 감소함을 알 수 있다. 

    또한 $\bigg |\dfrac{\partial L}{\partial w _{11}}\bigg | < \bigg |\dfrac{\partial L}{\partial w _{23}}\bigg |$ 이므로 $w _{23}$ 을 갱신할 때 $w _{11}$ 보다 손실함수 값이 더 예민하게 움직인다는 것을 알 수 있다.

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

신경망 학습 알고리즘 : 신경망 학습 알고리즘은 다음의 2단계와 3단계를 에폭만큼, 또는 수용가능 오차도가 산출될때까지 반복하여 가중치와 편향을 훈련 데이터에 적합하도록 조정하는 알고리즘이다.

1. (미니배치) 훈련 데이터 중 일부를 무작위로 추출한다. 이 일부 데이터를 미니배치라고 하며, 이 미니배치의 손실 함수 값을 줄이는 것이 신경망 학습의 목표이다.

2. (기울기 산출) 손실함수에 대한 가중치 행렬의 기울기를 구한다. 이 기울기 벡터로 손실함수 값을 줄이는 방향에 대한 단서를 얻는다. 

3. (가중치 학습) 가중치 매개변수를 기울기 방향으로 학습률만큼 갱신한다.

</blockquote>

- 이때 미니배치를 무작위로 선정하므로 확률적 경사 하강법(SGD, stochastic gradient descent)라고 한다.

- 코드 구현 

  ```python
  class TwoLayerNet:
      def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):
          # {params} 입력층의 뉴런수, 은닉층의 뉴런 수, 출력증의 뉴럭수
          # 가중치 초기화
          self.params = {}
          self.params['W1'] = weight_init_std * np.random.randn(input_size, hidden_size)
          self.params['b1'] = np.zeros(hidden_size)
          self.params['W2'] = weight_init_std * np.random.randn(hidden_size, output_size)
          self.params['b2'] = np.zeros(output_size)

      def predict(self, x):
          # 예측(추론)을 수행한다.
          W1, W2 = self.params['W1'], self.params['W2']
          b1, b2 = self.params['b1'], self.params['b2']
      
          a1 = np.dot(x, W1) + b1
          z1 = sigmoid(a1)
          a2 = np.dot(z1, W2) + b2
          y = softmax(a2)
          
          return y
          
      def loss(self, x, t):
          # {params} x : 입력 데이터, t : 정답 레이블
          # 손실함수 값을 계산한다.
          y = self.predict(x)
          
          return cross_entropy_error(y, t)
      
      def accuracy(self, x, t):
          # 정확도를 구한다.
          y = self.predict(x)
          y = np.argmax(y, axis=1)
          t = np.argmax(t, axis=1)
          
          accuracy = np.sum(y == t) / float(x.shape[0])
          return accuracy
          
      def numerical_gradient(self, x, t):
          # {params} x : 입력 데이터, t : 정답 레이블
          # 가중치 행렬의 기울기 벡터를 구한다.
          loss_W = lambda W: self.loss(x, t)
          
          grads = {}
          grads['W1'] = numerical_gradient(loss_W, self.params['W1'])
          grads['b1'] = numerical_gradient(loss_W, self.params['b1'])
          grads['W2'] = numerical_gradient(loss_W, self.params['W2'])
          grads['b2'] = numerical_gradient(loss_W, self.params['b2'])
          
          return grads
          
      def gradient(self, x, t):
          # 오차 역전파로 가중치 행렬의 기울기 벡터를 빠르게 구한다.
          W1, W2 = self.params['W1'], self.params['W2']
          b1, b2 = self.params['b1'], self.params['b2']
          grads = {}
          
          batch_num = x.shape[0]
          
          # forward
          a1 = np.dot(x, W1) + b1
          z1 = sigmoid(a1)
          a2 = np.dot(z1, W2) + b2
          y = softmax(a2)
          
          # backward
          dy = (y - t) / batch_num
          grads['W2'] = np.dot(z1.T, dy)
          grads['b2'] = np.sum(dy, axis=0)
          
          da1 = np.dot(dy, W2.T)
          dz1 = sigmoid_grad(a1) * da1
          grads['W1'] = np.dot(x.T, dz1)
          grads['b1'] = np.sum(dz1, axis=0)

          return grads
  
  def test_dummy():
      # 더미 데이터와 더미 정답 레이블로 학습해본다.
      net = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)
      x = np.random.rand(100, 784) # 더미 데이터 손글씨 사진 100장
      t = np.random.rand(100, 10)  # 더미 데이터 100장에 대한 더미 정답 레이블 
      grads = net.numerical_gradient(x, t)
      # ...

  def test_mnist():
      from dataset.mnist import load_mnist
      (x_train, t_train), (x_test, t_test) = \
          load_mnist(normalize=True, one_hot_label=True)
      
      train_loss_list = []
      epoch = 10000
      train_size = x_train.shape[0]
      batch_size = 100
      lr = 0.1
      net = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)
      # net = TwoLayerNet(input_size=784, hidden_size=100, output_size=10)
      train_acc_list = []
      test_acc_list = []

      for _ in range(epoch):
          batch_mask = np.random.choice(train_size, batch_size)
          x_batch = x_train[batch_mask]
          t_batch = t_train[batch_mask]

          grad = net.numerical_gradient(x_batch, t_batch)
          for key in ('W1', 'b1', 'W2', 'b2'):
              net.params[key] -= lr * grad[key]
          loss = net.loss(x_batch, t_batch)
          train_loss_list.append(loss)

          # 정확도 계산 
          train_acc = net.accuracy(x_train, t_train)
          test_acc = net.accuracy(x_test, t_test)
          train_acc_list.append(train_acc)
          test_acc_list.append(test_acc)
          print("tarin acc, test acc : ", train_acc, test_acc)


  if __name__ == '__main__':
      test_mnist()
  ```

  - 위 코드에서 `numerical_gradient(self, x, t)` 의 수치미분으로 가중치의 기울기를 계산하는데, 실제로는 오차역전파로 기울기 계산을 빠르게 수행한다.

# <a name="오차역전파 " href="#오차역전파 ">오차역전파 </a>

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

오차역전파 : 신경망 학습에서 수치미분보다 효율적으로 기울기를 계산하는 방법이다.

</blockquote>

- 오차역전파는 계산 그래프로 순전파를 계산한다.

  - 계산 그래프는 연산 노드(덧셈, 곱셈 등등)에 입력을 주고 출력을 상위 연산 노드로 전달하는 알고리즘이다.

  - 계산 그래프를 통한 중간 노드로 국소적 계산을 하면 여러 이점이 있다. 

    1. 네트워크가 아무리 복잡해도 각 노드에서는 단순한 국소적 계산만 하면 된다. 

    2. 중간 계산 과정을 저장할 수 있다. 

    3. 역전파를 통해 미분을 효율적으로 빠르게 계산할 수 있다.

- 계산 그래프의 역전파는 입력 $x$ 와 출력 $y$ 을 갖는 노드에 전달된 상위 노드에서 전달된 값 $E$ 에 대하여

  $$ E \dfrac{\partial y}{\partial x} $$

  을 이전 노드로 전달한다.

  - 이렇게 미분을 구하는 것이 가능한 이유는 합성함수의 미분, 즉 연쇄법칙 때문이다.

    - 예시 

      이독립변수와 일매개변수와 대한 합성함수

      $$ z = t ^{2} $$

      $$ t = x + y $$

      의 도함수는 $x$ 에 대한 미분

      $$ \dfrac{\partial z}{\partial x} = \dfrac{\partial z}{\partial t}\dfrac{\partial t}{\partial x} $$

      과 $y$ 에 대한 미분

      $$ \dfrac{\partial z}{\partial x} = \dfrac{\partial z}{\partial t}\dfrac{\partial t}{\partial x} $$

      이다.

      가장 상위 노드에서, 즉 출력층에서 이전 노드로 미분 $\dfrac{\partial z}{\partial z}$ 를 전달한다.

      그러면 이전 노드가 상위 노드의 미분 $\dfrac{\partial z}{\partial z}$ 을 받고 $z$ 에 대한 $t$ 의 미분 $\dfrac{\partial z}{\partial t}$ 를 곱하여 $\dfrac{\partial z}{\partial z}\dfrac{\partial z}{\partial t}$ 를 만들어서 또 이전 노드로 전달한다. 

      그러면 이전 노드가 상위 노드의 미분 $\dfrac{\partial z}{\partial z}\dfrac{\partial z}{\partial t}$ 을 받고 각각 $t$ 에 대한 $x$ 의 미분 
      과 $t$ 에 대한 $y$ 의 미분을 곱하여

      $$ \dfrac{\partial z}{\partial z}\dfrac{\partial z}{\partial t}\dfrac{\partial t}{\partial x} $$

      $$ \dfrac{\partial z}{\partial z}\dfrac{\partial z}{\partial t}\dfrac{\partial t}{\partial y} $$

      을 만든다. 그러면 이 결과는 곧

      $$ \dfrac{\partial z}{\partial z}\dfrac{\partial z}{\partial t}\dfrac{\partial t}{\partial x} = \dfrac{\partial z}{\partial x}$$

      $$ \dfrac{\partial z}{\partial z}\dfrac{\partial z}{\partial t}\dfrac{\partial t}{\partial y} = \dfrac{\partial z}{\partial y}$$

      가 되어 각각 $z$ 에 대한 $x$ 의 미분, $z$ 에 대한 $y$ 의 미분 결과값이 되는 것이다.

      이렇게 각각의 노드가 상위 노드에서 받은 미분값을 자신의 미분에 곱하기만 하면, 최종 손실함수가 자신의 변화에 대하여 얼마나 변하는지 보여주는 순간변화율, 즉 미분값을 구할 수 있는 것이다.

      > 모든 합성함수의 미분, 즉 연쇄법칙은 독립변수에 대한 미분이고, 전체함수 $f$ 를 매개변수로 미분하고, 매개변수를 독립변수로 미분한 것을 곱하면 된다. 다음의 다변수 합성함수의 편도함수를 보자.
      
      <blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

      $n$ 개의 독립변수와 $m$ 개의 매개변수에 대한 다변수 합성함수의 편도함수(chain rule) : 유한개의 매개변수 $x_1, x_2, \dots, x_m$ 에 대한 다변수 함수 $w = f(x_1, x_2, \dots, x_m)$ 가 미분가능하고,

      $n$ 개의 독립변수 $p_1, p_2, \dots, p_n$ 에 대한 함수 $x_1, x_2, \dots, x_m$ 도 미분가능하면,

      $w$ 가 미분가능하고 $p_1, p_2, \dots, p_n$ 에 대한 함수들도 미분가능하며

      각각의 독립변수에 대한 $w$ 의 편도함수는 다음과 같다. 

      $$ \frac{\partial  w}{\partial p_1} = \frac{\partial w}{\partial x_1}\frac{\partial  x_1}{\partial  p_1} + \frac{\partial w}{\partial x_2}\frac{\partial  x_2}{\partial  p_1} + \dots + \frac{\partial w}{\partial x_m}\frac{\partial  x_m}{\partial  p_1}$$

      $$ \frac{\partial  w}{\partial p_2} = \frac{\partial w}{\partial x_1}\frac{\partial  x_1}{\partial  p_2} + \frac{\partial w}{\partial x_2}\frac{\partial  x_2}{\partial  p_2} + \dots + \frac{\partial w}{\partial x_m}\frac{\partial  x_m}{\partial  p_2}$$

      $$ \vdots $$

      $$ \frac{\partial  w}{\partial p_n} = \frac{\partial w}{\partial x_1}\frac{\partial  x_1}{\partial  p_n} + \frac{\partial w}{\partial x_2}\frac{\partial  x_2}{\partial  p_n} + \dots + \frac{\partial w}{\partial x_m}\frac{\partial  x_m}{\partial  p_n}$$

      </blockquote>

    - 예시 

      이독립변수와 이매개변수에 대한 합성함수 

      $$ z = x + y $$

      $$ x = 2r s$$

      $$ y = r s$$

      의 도함수는 $r$ 에 대한 미분 

      $$ \dfrac{\partial z}{\partial r} = \dfrac{\partial z}{\partial x}\dfrac{\partial x}{\partial r} + \dfrac{\partial z}{\partial y}\dfrac{\partial y}{\partial r} $$

      과 $s$ 에 대한 미분

      $$ \dfrac{\partial z}{\partial s} = \dfrac{\partial z}{\partial x}\dfrac{\partial x}{\partial s} + \dfrac{\partial z}{\partial y}\dfrac{\partial y}{\partial s} $$

      이다.

      가장 상위 노드에서, 즉 출력층에서 이전 노드로 미분 $\dfrac{\partial z}{\partial z}$ 를 전달한다.

      그러면 이전 노드가 상위 노드의 미분 $\dfrac{\partial z}{\partial z}$ 을 받고 각각 $z$ 에 대한 $x$ 의 미분과 $z$ 에 대한 $y$ 의 미분을 곱하여
      
      $$\dfrac{\partial z}{\partial z}\dfrac{\partial z}{\partial x}$$

      $$\dfrac{\partial z}{\partial z}\dfrac{\partial z}{\partial y}$$

      를 전달한다. 그러면 이전 그 이전 노드는 각각 $x$ 에 대한 $r$ 의 미분을 $\dfrac{\partial z}{\partial z}\dfrac{\partial z}{\partial x}$ 에 곱한 것과 $y$ 에 대한 $r$ 의 미분을 $\dfrac{\partial z}{\partial z}\dfrac{\partial z}{\partial y}$ 에 곱한 것을 더하고

      $x$ 에 대한 $s$ 의 미분을 $\dfrac{\partial z}{\partial z}\dfrac{\partial z}{\partial x}$ 에 곱한 것과 $y$ 에 대한 $s$ 의 미분을 $\dfrac{\partial z}{\partial z}\dfrac{\partial z}{\partial y}$ 에 곱한 것을 더하여 

      $$\dfrac{\partial z}{\partial z}\dfrac{\partial z}{\partial x}\dfrac{\partial x}{\partial r} + \dfrac{\partial z}{\partial z}\dfrac{\partial z}{\partial y}\dfrac{\partial y}{\partial r}$$

      $$\dfrac{\partial z}{\partial z}\dfrac{\partial z}{\partial x}\dfrac{\partial x}{\partial s}  + \dfrac{\partial z}{\partial z}\dfrac{\partial z}{\partial y}\dfrac{\partial y}{\partial s}$$

      를 구할 수 있다.

      - **이로써 우리는 상위 노드로부터 전달된 모든 미분 값에 그 상위 노드에 대한 자신의 미분을 곱하고 모두 더해야 한다는 것을 알 수 있다.**
      
        **즉, $n \in \R$ 개의 상위 노드로부터 전달된 미분 $\dfrac{\partial L}{\partial u_1},\dfrac{\partial L}{\partial u_2}, \dots, \dfrac{\partial L}{\partial u_n}$ 에 각각의 상위 노드에 대한 자신 $v$ 의 미분 $\dfrac{\partial u_1}{\partial v},\dfrac{\partial u_2}{\partial v}, \dots, \dfrac{\partial u_n}{\partial v}$ 를 곱하고 모두 더한 값**

        $$ \dfrac{\partial L}{\partial u_1}\dfrac{\partial u_1}{\partial v} +\dfrac{\partial L}{\partial u_2}\dfrac{\partial u_2}{\partial v} +\dots+\dfrac{\partial L}{\partial u_n}\dfrac{\partial u_n}{\partial v} $$

        **을 최종적으로 자신의 미분값, 즉 자신이 조금 변했을 때 손실함수가 얼마나 변하는지에 대한 단서로 삼아야 한다.**
  
<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

덧셈 노드의 역전파 : 입력을 더하여 상위 연산 노드로 전달하는 덧셈 연산 노드의 역전파는 그 미분이 $1$ 이므로 상위 연산 노드에서 전달된 미분에 $1$ 을 곱하여 하위 연산 노드로 전달한다.

</blockquote>
  
- $n$ 개의 입력 $x_1, x_2, \dots, x_n$ 을 받아 상위 연산 노드로 전달하는 덧세 연산 노드는 함수 $y  = x_1+x_2+\dots+x_n$ 로 표현되는데 각 독립변수에 대한 미분은

  $$ \dfrac{\partial y}{\partial x_1} = 1, \dfrac{\partial y}{\partial x_2} = 1, \dots, \dfrac{\partial y}{\partial x_n} = 1 $$

  로써 모두 $1$ 이다.

  그러므로 덧셈 노드의 역전파는 단지 상위 노드에서 온 미분값에 $1$ 을 곱해주는 것이다. 그런데 $1$ 을 곱하는 것은 무의미하므로 그냥 전달된 값을 아무 연산 없이 그대로 다시 전달하면 된다.

  - **물론 상위 노드에서 $n$ 개의 미분이 전달되면 그것들에 상위 노드에 대한 자신의 미분을 곱하여 더해주어야 하기 때문에**

    **덧셈 노드의 경우 그냥 상위 노드에서 전달된 미분들을 더하기만 하면 된다는 것이다.**

- 예시 

  함수 $z = x+y$ 의 역전파를 조사하자. $z$ 의 미분은 다음과 같다. 

  $$ \dfrac{\partial z}{\partial x} = 1 $$

  $$ \dfrac{\partial z}{\partial y} = 1 $$

  그러므로 상류에서 전해진 미분 $\dfrac{\partial L}{\partial z}$ 에 단지 $1$ 을 곱하여 하류로 전달하면 된다. $L$ 은 손실함수를 뜻한다.

  - 코드 구현 

    이 예시를 다음과 같이 코드로 간단히 구현할 수 있다.

    ```python
    class AddLayer:
        def __init__(self):
            pass

        def forward(self, x, y):
            out = x + y

            return out

        def backward(self, dout):
            dx = dout * 1
            dy = dout * 1

            return dx, dy
    ```

- 예시 

  함수 $u = x+y+z+w$ 의 역전파를 조사하자. $u$ 의 미분은 다음과 같다. 

  $$ \dfrac{\partial u}{\partial x} = 1, \dfrac{\partial u}{\partial y} = 1, \dfrac{\partial u}{\partial z} = 1, \dfrac{\partial u}{\partial w} = 1 $$

  그러므로 상류에서 전해진 미분 $\dfrac{\partial L}{\partial u}$ 에 단지 $1$ 을 곱하여 하류로 전달하면 된다. $L$ 은 손실함수를 뜻한다.

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

곱셈 노드의 역전파 : 입력을 곱하여 상위 연산 노드로 전달하는 곱셈 연산 노드의 역전파는 순전파 때의 그 입력을 제외한 나머지 입력을 곱한 것을 상위 노드에서 역전파된 미분에 곱하여 하위 노드로 전달한다.

</blockquote>

- 예시 

  함수 $z = xy$ 에 대한 미분은 

  $$ \dfrac{\partial z}{\partial x} = y , \dfrac{\partial z}{\partial y} = x $$

  이다. 

  그러므로 우리는 순전파 때의 입력들을 서로 바꾼 값을 상위 노드에서 역전파된 미분에 곱하여 하위 노드로 전달하면 된다는 것을 알 수 있다.

  - 예시 

    곱셈 노드가 순전파때 입력 $10,5$ 를 받아 상위노드로 $50$ 을 전달했는데, 

    역전파 때 상위노드에서 미분 $1.3$ 을 전달했다면 

    $10$ 의 입력을 전달한 하위 노드에 $6.5$ 를 전달하고

    $5$ 의 입력을 전달한 하위 노드에 $13$ 를 전달하는 것이다.
  
  - 코드 구현 

    이 예시를 다음과 같이 간단하게 코드로 구현할 수 있다. 

    ```python
    class MulLayer:
        def __init__(self):
            self.x = None
            self.y = None

        def forward(self, x, y):
            self.x = x
            self.y = y                
            out = x * y

            return out

        def backward(self, dout):
            dx = dout * self.y  # x와 y를 바꾼다.
            dy = dout * self.x

            return dx, dy
    ```

    이 코드를 사용하여 사과 $100$ 원 짜리 사과를 $2$ 개 사고 $10\%$ 의 세금이 부과된 상황을 순전파로 구현하고, 역전파로 미분을 구해보자.

    ```python
    apple = 100
    apple_num = 2
    tax = 1.1

    mul_apple_layer = MulLayer()
    mul_tax_layer = MulLayer()

    # 순전파
    apple_price = mul_apple_layer.forward(apple, apple_num)
    price = mul_tax_layer.forward(apple_price, tax)

    # 역전파
    dprice = 1 # 최종 노드가 price 인데 price 에 대한 price 의 미분은 1 이다.
    dapple_price, dtax = mul_tax_layer.backward(dprice)
    dapple, dapple_num = mul_apple_layer.backward(dapple_price)
    ```

    역전파 `backward` 의 입력은 순전파의 출력에 대한 미분이라는 것을 기억하자.
  
- 예시 

  함수 $u = xyzw$ 에 대한 미분은 

  $$ \dfrac{\partial u}{\partial x} = yzw , \dfrac{\partial u}{\partial y} = xzw, \dfrac{\partial u}{\partial z} = xyw , \dfrac{\partial u}{\partial w} = xyz $$

  이다. 

  그러므로 우리는 순전파 때의 그 입력을 제외한 나머지 입력을 곱한 것을 상위 노드에서 역전파된 미분에 곱하여 하위 노드로 전달하면 된다는 것을 알 수 있다.

  - 예시 

    곱셈 노드가 순전파때 입력 $1,2,3,4$ 를 받아 상위노드로 $24$ 을 전달했는데, 

    역전파 때 상위노드에서 미분 $1$ 을 전달했다면 

    $1$ 의 입력을 전달한 하위 노드에 $24 \times (2 \times 3 \times 4)$ 를 전달하고

    $2$ 의 입력을 전달한 하위 노드에 $24 \times (1 \times 3 \times 4)$ 를 전달하고

    $3$ 의 입력을 전달한 하위 노드에 $24 \times (1 \times 2 \times 4)$ 를 전달하고

    $4$ 의 입력을 전달한 하위 노드에 $24 \times (1 \times 2 \times 3)$ 를 전달하는 것이다.

  - 코드 구현 

    이 예시를 다음과 같이 간단하게 코드로 구현할 수 있다. 

    ```python
    import numpy as np

    class MulLayer:
        def __init__(self):
            self.input = []

        def forward(self, input):
            self.input = input
            out = np.prod(self.input)

            return out

        def backward(self, dout):
            result = []
            for i, v in enumerate(self.input):
                tmp = self.input
                del tmp[i]
                result.append(dout * np.prod(tmp))

            return result
    ```

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

나눗셈 노드의 역전파 : 입력 $x$ 의 곱셈의 역원 $\dfrac{1}{x}$ 을 상위 연산 노드로 전달하는 나눗셈 연산 노드의 역전파는 상위노드에 $-\dfrac{1}{x ^{2}}$ 를 곱하여 하류로 전달한다.

</blockquote>

- 함수 $y = \dfrac{1}{x}$ 의 미분은 $\dfrac{dy}{dx} = -\dfrac{1}{x ^{2}}$ 이다. 그러므로 역전파 때 상위 노드에서 전달된 값에 $-\dfrac{1}{x ^{2}}$ 를 곱하여 하위 노드로 전달한다.

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

$\exp$ 노드의 역전파 : 입력 $x$ 에 대하여 $\exp(x)$ 를 상위 연산 노드로 전달하는 $\exp$ 연산 노드의 역전파는 상위노드에 $\exp (x)$ 를 곱하여 하류로 전달한다.

</blockquote>

- 함수 $y = \exp (x)$ 의 미분은 $\dfrac{dy}{dx} = \exp (x)$ 이다. 그러므로 역전파 때 상위 노드에서 전달된 값에 $\exp (x)$ 를 곱하여 하위 노드로 전달한다.

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

표준 Sigmoid 활성화 함수의 역전파 : 표준 Sigmoid 함수 $y = \zeta (x) = \text{sigmoid}(x) =: \dfrac{1}{1 + \exp (-x)}$ 의 역전파는 상위노드에 $y(1-y)$ 를 곱하여 하류로 전달한다.

</blockquote>

- 함수 $y = \zeta (x) =: \dfrac{1}{1+\exp (-x)}$ 의 미분은 $\{\zeta (x)\}' = \zeta (x)\{1-\zeta (x)\}$ 이다. 그러므로 역전파 때 상위 노드에서 전달된 값에 $y(1-y)$ 를 곱하여 하위 노드로 전달한다.

- 코드 구현 

  시그모이드 함수 레이어는 다음과 같이 간단하게 구현할 수 있다. 

  ```python
  class Sigmoid:
    def __init__(self):
        self.out = None

    def forward(self, x):
        out = sigmoid(x)
        self.out = out
        return out

    def backward(self, dout):
        dx = dout * (1.0 - self.out) * self.out

        return dx
  ```

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

ReLU 활성화 함수의 역전파 : ReLU 함수 $y = \begin{cases} x &(x>0)\\ 0 &(x \leq 0)\\ \end{cases}$ 의 미분은 

$$ \dfrac{dy}{dx} = \begin{cases} 1 &(x>0)\\ 0 &(x \leq 0)\\ \end{cases} $$

이므로 순전파 때 입력 $x$ 가 $0$ 보다 크면 $1$ 을 곱하여 하위 노드로 전달하고 $0$ 이하면 $0$ 을 곱하여 하위 노드로 전달한다.

</blockquote>

- 즉, 순전파 때 입력이 $0$ 보다 크면 상류의 값을 그대로 하류로 전달하고 

  $0$ 이하면 하류로 아무것도 전달하지 않는다.

- 코드 구현 

  ReLU 함수 레이어는 다음과 같이 간단하게 코드로 구현할 수 있다. 

  ```python
  class Relu:
      def __init__(self):
          self.mask = None

      def forward(self, x):
          self.mask = (x <= 0)
          out = x.copy()
          out[self.mask] = 0

          return out

      def backward(self, dout):
          dout[self.mask] = 0
          dx = dout

          return dx
  ```

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

신경망 순전파 흐름 : $n, m \in \N$ 에 대한 $1 \times n$ 입력행렬 $X$, $n \times m$ 가중치행렬 $W$, $1 \times m$ 편향행렬 $B$ 에 대하여 $1 \times m$ 순입력행렬

$$ Z = X W + B $$

를 활성화 함수 $h:\R ^{m} \to \R ^{m}$ 에 입력하여 얻은 $1 \times m$ 출력행렬 $Y$ 를 다음 층으로 전달하는 것이다.

</blockquote>

- 신경망 순전파의 행렬곱을 기하학에서 아핀 변환(affine transformation) 이라고 한다.

  > 아핀 기하학이 유클리드 기하학보다 논리적으로 선행한다는 것을 수학사에서 살펴본 적이 있다.

  - 그래서 아핀 변환(행렬곱)을 처리하는 레이어를 Affine 계층이라는 이름으로 구현한다.

<blockquote style="border: 2px solid; color:black; background:#E0E0E0;padding: 7px;">

Affine 변환의 역전파 : 

</blockquote>