# Deep Learning from Scratch

[밑바닥부터 시작하는 딥러닝](https://book.naver.com/bookdb/book_detail.nhn?bid=11492334)의 개인 메모입니다.

# 가중치 최적화 


!!! note ""

    최적화(optimization) : 신경망 학습의 목적, 즉 손실 함수의 값을 최대한 낮추기 위하여 최적의 가중치 매개변수를 찾는 것이다.

- 가중치 매개변수 공간은 매우 넓고 복잡해서 수식을 풀어 단번에 손실함수의 최소값을 구하는 방법은 존재하지 않는다. 

  - 증명 

    **구체화 필요**

- SGD, 모멘텀, AdaGrad, Adam 등 최적화 기법이 존재하지만 모든 문제에서 항상 최고의 성능을 보이는 최적화 기법은 아직까지 존재하지 않는다. 문제와 상황에 따라서 좋은 성능을 보이는 최적화 기법이 각각 따로 존재한다. 

  - 아직까지 많은 연구에서 SGD 를 사용하며, 최근에는 Adam 으로 좋은 성과가 많이 나오기도 한다.

  - 하지만 일반적으로 거칠게 말해서 SGD 보다 모멘텀, AdaGrad, Adam 등이 학습이 더 빠르고 최종 정확도도 더 높다.

  - 증명

    **구체화 필요**

!!! note ""

    확률적 경사 하강법(SGD, Stochastic Gradient Descent) : 최적화(최적의 매개변수 찾기)를 위하여 미분을 사용하여 매개변수 기울기 $\dfrac{\partial L}{\partial \mathbf{W}}$ 를 구하고, 기울기 방향으로 매개변수 $\mathbf{W}$ 를 
    
    $$ \mathbf{W} := \mathbf{W} - \eta \dfrac{\partial L}{\partial \mathbf{W}} $$
    
    와 같이 갱신하는 일을 에폭 만큼, 또는 설정된 정확도가 나올 때까지 반복하는 최적화 기법이다.

- 이 SGD 를 지금까지 한 것이다.

- SGD 는 단순하지만 강력하다. 하지만 단점도 존재한다. 따라서 상황에 따라 다른 최적화 기법을 적용해야만 한다.

  - SGD 의 단점 

    SGD 의 단점이란 지도가 없는 장님이 광활한 산맥에서 가장 낮은 골짜기를 찾으려는 것과 똑같다. 
    
    지도가 없다는 것은 가장 낮은 골짜기가 정확히 어딘지 모른다는 것이고,

    장님이라는 것은 단서가 오로지 현재 서있는 땅의 기울기밖에 없다는 것이다.

    학습률 $\eta$ 란 기울기 방향으로 얼만큼 발걸음을 옮기느냐 이고, 

    에폭이란 이 지랄을 몇 번 반복할 것이냐 이다.

    이 무식한 방법으로 "운 좋으면" 가장 낮은 골짜기를 찾을 수 있을 것이다.

- 코드 구현 

  SGD 는 다음과 같이 간단히 구현할 수 있다.

  ```python
  class SGD:
      def __init__(self, lr = 0.01):
          self.lr = lr
      def update(self, params, grads):
          for key in params. keys():
              params[key] -= self.lr * grads[key]
  ```

  이 코드를 다음과 같이 간단히 사용할 수 있다. 

  ```python
  network = TwoLayerNet(...)
  optimizer = SGD()

  for i in range(10000):
      ...
      x_batch, t_batch = get_mini_batch(...)
      grads = network.gradient(x_batch, t_batch)
      params = network.params
      optimizer.update(params, grads)
      ...
  ```

!!! note ""

    모멘텀(momentum) : 최적화(최적의 매개변수 찾기)를 위하여 미분을 사용하여 매개변수 기울기 $\dfrac{\partial L}{\partial \mathbf{W}}$ 를 구하고, 속도 $\mathbf{v}$ 에 대하여 기울기 방향으로 매개변수 $\mathbf{W}$ 를 
    
    $$ \mathbf{v} := \alpha \mathbf{v} - \eta \dfrac{\partial L}{\partial \mathbf{W}} $$
    
    $$ \mathbf{W} := \mathbf{W} + \mathbf{v} $$
    
    와 같이 갱신하는 일을 에폭 만큼, 또는 설정된 정확도가 나올 때까지 반복하는 최적화 기법이다.

- $\alpha \mathbf{v}$ 는 물체가 아무런 힘을 받지 않을 때 서서히 하강시키는 역할을 한다. 

  $\alpha = 0.9$ 로 설정하는 것이 일반적이다.

- 코드 구현 

  ```python
  class Momentum:
      def __init__(self, lr=0.01, momentum=0.9):
          self.lr = lr
          self.momentum = momentum
          self.v = None
          
      def update(self, params, grads):
          if self.v is None:
              self.v = {}
              for key, val in params.items():                                
                  self.v[key] = np.zeros_like(val)
                  
          for key in params.keys():
              self.v[key] = self.momentum*self.v[key] - self.lr*grads[key] 
              params[key] += self.v[key]

  ```

  속도벡터 $\mathbf{v}$ 는 처음에는 영벡터로 시작하여 첫 가중치 업데이트 때 매개변수 데이터를 저장하고 

  $$ \mathbf{v} := \alpha \mathbf{v} - \eta \dfrac{\partial L}{\partial \mathbf{W}} $$

  $$ \mathbf{W} := \mathbf{W} + \mathbf{v} $$

  의 수식에 따라 가중치 업데이트를 진행한다.

- **모멘텀이 SGD 보다 왜 더 좋은지, 수식을 기반으로 좀 더 구체화 필요**

!!! note ""

    AdaGrad : 가중치 행렬 $\mathbf{W}$, 학습률 $\eta$, 손실함수 출력 스칼라 $L$ 에 대하여
    
    $$ \mathbf{h} := \mathbf{h} + \dfrac{\partial L}{\partial \mathbf{W}} \odot \dfrac{\partial L}{\partial \mathbf{W}} $$
    
    $$ \mathbf{W} := \mathbf{W} - \eta \dfrac{1}{\sqrt[]{\mathbf{h}}}\dfrac{\partial L}{\partial \mathbf{W}}
    $$
    
    와 같이 처음에는 큰 학습률로 학습하다가 점차 작은 학습률로 매개변수 가중치를 조정하는 최적화 기법이다.

- 기호 $\odot$ 은 행렬의 원소별 곱셈을 뜻한다. 그러므로 $\dfrac{\partial L}{\partial \mathbf{W}} \odot \dfrac{\partial L}{\partial \mathbf{W}}$ 는 행렬 $\dfrac{\partial L}{\partial \mathbf{W}}$ 의 원소별 제곱을 의미한다.

  이에 따라 $\mathbf{h}$ 에는 $\dfrac{\partial L}{\partial \mathbf{W}}$ 의 제곱이 계속 더해진다. 그리고 학습률을 $\eta := \dfrac{\eta }{\sqrt[]{h}}$ 로 줄여준다.

  - 이것은 매개변수 가중치 행렬에서 많이 갱신된 원소일수록 학습률을 낮추어준다는 의미이다.

    즉, 매개변수 가중치 행렬의 원소마다 학습률 감소를 다르게 적용하겠다는 의미이다.

- AdaGrad 는 이전 가중치 매개변수 행렬의 원소를 제곱하여 더해주므로 학습이 진행될 수록 학습률이 낮아진다. 이는 학습률 $\eta$ 가 $0$ 에 수렴하게 될 수도 있다는 것을 의미한다. 즉, 더 이상 학습이 되지 않는 상태에 도달할 수도 있다는 것이다. 

  - 이를 해결하기 위하여 **RMSProp** 기법이 개발되었다. 이는 과거의 모든 기울기에 대한 학습률을 균일하게 낮추는 것이 아니라, 먼 과거의 기울기는 서서히 잊고 새로운 기울기 정보를 크게 반영하는 최적화 기법이다.

    이를 지수이동평균(EMA, Exponential Moving Average) 라고 하여 과거 기울기 반영 규모를 기하급수적으로 감소시킨다.

- 코드 구현 

  ```python
  class AdaGrad:

      """AdaGrad"""

      def __init__(self, lr=0.01):
          self.lr = lr
          self.h = None
          
      def update(self, params, grads):
          if self.h is None:
              self.h = {}
              for key, val in params.items():
                  self.h[key] = np.zeros_like(val)
              
          for key in params.keys():
              self.h[key] += grads[key] * grads[key]
              params[key] -= self.lr * grads[key] / (np.sqrt(self.h[key]) + 1e-7)
    ```

    수식을 그냥 코드로 구현한 것이다. 다만 `1e-7` 을 더해주어 최악의 상황에서 $0$ 으로 나누어지는 것을 방지한다.

    - 이 값 `1e-7` 은 딥러닝 프레임워크에서는 파라미터로 직접 설정할 수 있다.

!!! note ""

    Adam : 거칠게 말해서 모멘텀과 AdaGrad 를 융합하여 만들어진 최적화 기법이다.

- Adam 은 직관적으로는 모멘텀과 AdaGrad 를 융합하고, 하이퍼파라미터(학습률 $\alpha$, 일차 모멘텀 계수 $\beta _{1}$, 이차 모멘텀 계수 $\beta _{2}$)의 편향 보정이 적용하여 가중치 매개변수를 갱신한다.

- Adam 의 실제 이론은 논문을 참조하자.

  - 논문에 따르면 기본 설정값을 $\beta _{1} =0.9, \beta _{2} = 0.999$ 로 설정했다. 대부분의 경우 이 기본값을 따르면 좋은 결과를 얻을 수 있다.

- 코드 구현 

  ```python
  class Adam:

      """Adam (http://arxiv.org/abs/1412.6980v8)"""

      def __init__(self, lr=0.001, beta1=0.9, beta2=0.999):
          self.lr = lr
          self.beta1 = beta1
          self.beta2 = beta2
          self.iter = 0
          self.m = None
          self.v = None
          
      def update(self, params, grads):
          if self.m is None:
              self.m, self.v = {}, {}
              for key, val in params.items():
                  self.m[key] = np.zeros_like(val)
                  self.v[key] = np.zeros_like(val)
          
          self.iter += 1
          lr_t  = self.lr * np.sqrt(1.0 - self.beta2**self.iter) / (1.0 - self.beta1**self.iter)         
          
          for key in params.keys():
              #self.m[key] = self.beta1*self.m[key] + (1-self.beta1)*grads[key]
              #self.v[key] = self.beta2*self.v[key] + (1-self.beta2)*(grads[key]**2)
              self.m[key] += (1 - self.beta1) * (grads[key] - self.m[key])
              self.v[key] += (1 - self.beta2) * (grads[key]**2 - self.v[key])
              
              params[key] -= lr_t * self.m[key] / (np.sqrt(self.v[key]) + 1e-7)
              
              #unbias_m += (1 - self.beta1) * (grads[key] - self.m[key]) # correct bias
              #unbisa_b += (1 - self.beta2) * (grads[key]*grads[key] - self.v[key]) # correct bias
              #params[key] += self.lr * unbias_m / (np.sqrt(unbisa_b) + 1e-7)
  ```

# 가중치 초기값

!!! note ""

    가중치 초기값 : 초기에 설정되는 가중치로써 신경망 학습에 중요한 영향을 끼친다.

- 가중치 초기값이 $0$ 인 경우 

  과적합이 발생하는 것을 방지하지 위하여 가중치 값을 작게 만들 수 있다. 따라서 최대한 작은 가중치 값으로 학습을 시작하는 것도 좋은 방법이라고 할 수 있다. 

  그러나 가중치가 $0$ 이면 학습이 제대로 이루어지지 않는다. 역전파 때 모든 가중치 값들이 똑같이 갱신되기 때문이다. 

  - 예시 

    2층 신경망에서 첫번째, 두번째 층의 가중치가 $0$ 이면 순전파 때 가중치가 $0$ 이므로 같은 값($0$)이 다음 레이어로 전달된다. 이것은 가중치가 모두 똑같이 갱신된다는 의미이다. 

    이로써 가중치를 여러개 둔 의미도, 층을 깊게 한 의미도 사라진다.

