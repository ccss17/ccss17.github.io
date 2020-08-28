# Deep Learning from Scratch

[밑바닥부터 시작하는 딥러닝](https://book.naver.com/bookdb/book_detail.nhn?bid=11492334)의 개인 메모입니다.

# 가중치 최적화 


!!! tldr ""

    최적화(optimization) : 신경망 학습의 목적, 즉 손실 함수의 값을 최대한 낮추기 위하여 최적의 가중치 매개변수를 찾는 것이다.

- 가중치 매개변수 공간은 매우 넓고 복잡해서 수식을 풀어 단번에 손실함수의 최소값을 구하는 방법은 존재하지 않는다. 

    - 증명 

        **구체화 필요**

- SGD, 모멘텀, AdaGrad, Adam 등 최적화 기법이 존재하지만 모든 문제에서 항상 최고의 성능을 보이는 최적화 기법은 아직까지 존재하지 않는다. 문제와 상황에 따라서 좋은 성능을 보이는 최적화 기법이 각각 따로 존재한다. 

    - 아직까지 많은 연구에서 SGD 를 사용하며, 최근에는 Adam 으로 좋은 성과가 많이 나오기도 한다.

    - 하지만 일반적으로 거칠게 말해서 SGD 보다 모멘텀, AdaGrad, Adam 등이 학습이 더 빠르고 최종 정확도도 더 높다.

    - 증명

        **구체화 필요**

!!! tldr ""

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

!!! tldr ""

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

!!! tldr ""

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

!!! tldr ""

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

!!! tldr ""

    가중치 초기값 : 초기에 설정되는 가중치로써 신경망 학습에 중요한 영향을 끼친다.

- 가중치 초기값이 $0$ 인 경우 

    과적합이 발생하는 것을 방지하지 위하여 가중치 값을 작게 만들 수 있다. 따라서 최대한 작은 가중치 값으로 학습을 시작하는 것도 좋은 방법이라고 할 수 있다. 

    그러나 가중치가 $0$ 이면 학습이 제대로 이루어지지 않는다. 역전파 때 모든 가중치 값들이 똑같이 갱신되기 때문이다. 

    - 예시 

        2층 신경망에서 첫번째, 두번째 층의 가중치가 $0$ 이면 순전파 때 가중치가 $0$ 이므로 같은 값($0$)이 다음 레이어로 전달된다. 이것은 가중치가 모두 똑같이 갱신된다는 의미이다. 

        이로써 가중치를 여러개 둔 의미도, 층을 깊게 한 의미도 사라진다.

!!! tldr ""

    은닉층의 활성화값 분포 :  활성화 함수의 출력 데이터이다.

- 이것을 관찰하면 가중치 초깃값에 따라 활성화값들이 어떻게 변화하는지 관찰할 수 있다.

- 표준편차가 1 인 정규분포인 가중치 사용

    ```python
    input_data = np.random.randn(1000, 100)  # 1000개의 데이터
    node_num = 100  # 각 은닉층의 노드(뉴런) 수
    hidden_layer_size = 5  # 은닉층이 5개
    activations = {}  # 이곳에 활성화 결과를 저장

    x = input_data

    for i in range(hidden_layer_size):
        if i != 0:
            x = activations[i-1]

        w = np.random.randn(node_num, node_num) * 1
        a = np.dot(x, w)
        z = sigmoid(a)
        activations[i] = z

    for i, a in activations.items():
        plt.subplot(1, len(activations), i+1)
        plt.title(str(i+1) + "-layer")
        if i != 0: plt.yticks([], [])
        plt.hist(a.flatten(), 30, range=(0,1))
    plt.show()
    ```

    ![image](https://user-images.githubusercontent.com/16812446/91309429-8a30b480-e7eb-11ea-89bc-937f452e1076.png)

    여기에서 시그모이드 함수는 출력이 $0$ 또는 $1$ 에 가까워지자 미분이 $0$ 에 다가간다.

    그래서 데이터가 $0$ 과 $1$ 에 치우쳐 분포하면 기울기가 작아지다가 사라진다. 이것이 기울시 소실gradient vanishing 문제이다.

- 표준편차가 $0.01$ 인 정규분포인 가중치 사용

    ```python
    w = np.random.randn(node_num, node_num) * 0.01
    ```

    ![image](https://user-images.githubusercontent.com/16812446/91309782-fca19480-e7eb-11ea-90e5-1660e21c2cf9.png)


    이번에는 $0.5$ 부근에 활성화 값이 집중되어 기울기 소실 문제는 일어나지 않지만 활성화 값이 너무 치우쳐서 표현력에 문제가 생긴다. 즉 대부분의 뉴런이 같은 값을 출력하고 있기에 뉴런을 여러개를 둔 의미가 없어지는 것이다.

!!! tldr ""

    Xavier 초깃값 : Xavier Glorot 의 논문에서 권장하는 가중치 초깃값으로써 앞 계층의 노드 $n$ 에 대하여 표준편차가 $\dfrac{1}{\sqrt[]{n}}$ 인 분포를 사용하면 활성화값들이 광범위하게 분포된다는 초깃값이다.

- Xavier 분포인 가중치 사용

    ![image](https://user-images.githubusercontent.com/16812446/91311152-b51c0800-e7ed-11ea-8a2d-a486e72582db.png)

    층이 깊어질수록 형태가 다소 일그러지지만 확실히 넓게 분포되었다.

    이 일그러짐은 sigmoid 함수 대신 tanh 함수를 사용하면 말끔한 종 모양으로 분포되어 개선된다. tanh 함수가 원점 $(0,0)$ 에서 대칭인 반면 sigmoid 는 $(0,0.5)$ 에서 대칭이다. 활성화 함수용으로는 원점에서 대칭인 함수를 사용하는 것이 더 낫다고 알려져 있다. 

- Xavier 분포인 가중치와 tanh 함수 사용

    ![image](https://user-images.githubusercontent.com/16812446/91311702-586d1d00-e7ee-11ea-8c26-7d89068f1bc1.png)

!!! tldr ""

    He 초깃값 : 앞 계층의 노드가 $n$ 일 때 표준편차가 $\sqrt[]{\dfrac{2}{n}}$ 인 정규분포를 사용하는 가중치 분포이다.

- Xavier 초깃값은 활성화 함수가 선형일 때 유용하다. sigmoid 와 tanh 는 좌우 대치잉라 중앙 부근이 선형인 함수로 볼 수 있다. 반면 ReLU 를 사용할 때 특화된 초깃값은 He 초깃값이다. 

- ReLU 는 음의 영역이 $0$ 이라 더 넓기 분포시키기 위하여 $2$ 배의 계수가 필요하다고 볼 수 있다.

- ReLU 함수를 표준편차가 $0.01$ 인 정규분포를 가중치 초깃값으로 사용한 경우

    ![image](https://user-images.githubusercontent.com/16812446/91312302-0d9fd500-e7ef-11ea-9d99-86db07198fc5.png)

    활성화값들이 매우 작은 값으로 흐르고 있다. 이는 역전파 때 기울기도 작아진다는 것으로 학습도 거의 이루어지지 않는다.

- ReLU 함수를 Xavier 분포 가중치 초깃값으로 사용한 경우

    ![image](https://user-images.githubusercontent.com/16812446/91312539-4fc91680-e7ef-11ea-871d-2b1198f00f9c.png)

    층이 깊어지면서 치우침이 커진다. 이는 기울기 소실 문제를 일으킨다.

- ReLU 함수를 He 분포 가중치 초깃값으로 사용한 경우

    ![image](https://user-images.githubusercontent.com/16812446/91312708-7d15c480-e7ef-11ea-8700-bb20e59cdd7a.png)

    활성화값이 균일하게 분포되었다. 역전파 때도 적절한 값이 나올 것이다.

- 이로써 ReLU 를 사용할 때는 He 초깃값을 사용하고, sigmoid 나 tanh 등의 S자 모양 곡선을 활성화 함수로 사용하면 Xavier 초깃값을 사용하는 것이 좋다고 할 수 있다.

- MNIST 데이터셋으로 뉴런 수가 $100$ 개인 $5$ 층 신경망에서 ReLU 를 활성화 함수로 사용했을 때 가중치 분포에 따른 활성화 값 관찰

    ![image](https://user-images.githubusercontent.com/16812446/91388093-9d866300-e871-11ea-8e51-919b61a12ebc.png)

    표준편차가 $0.01$ 일 때 학습이 전혀 이루어지지 않는다. 앞의 실험에서와 같이 순전파 때 너무 작은 값, 즉 $0$ 에 가까운 값이 흐르기 때문이다. 이 때문에 역전파 때의 기울기도 작아져서 가중치가 거의 갱신되지 않는다.

    Xavier 도 학습이 잘 되지만 He 가 학습이 더 빠르게 잘 된다.

!!! tldr ""

    배치 정규화(Batch Normalization) : 학습 시 미니배치 단위로 데이터 분포가 정규분포가 되도록 정규화시키는 것이다.

- 가중치의 초깃값을 적절히 설정함으로써 각 층의 활성화값 분포가 적당히 퍼지도록 하여 학습이 원활하게 진행되도록 했다. 여기에서 착안하여 각 층의 활성화 값을 강제로 퍼뜨려보는 것이다.

- 2015년에 제안된 신생 기술인데 많은 연구자들이 사용하고 있다.

- 장점 

    - 학습 속도가 빨라진다.

    - 초깃값 의존도가 사라진다. 

    - 오버피팅을 억제한다.(드롭아웃 필요성 감소)

- 배치 정규화 층 예시 

    ![](https://t1.daumcdn.net/cfile/tistory/997AE03A5AAAA64C2A?download)

    위와 같이 배치 정규화를 사용한다. 
    
- 배치 정규화는 우선 $m \in \N$ 개의 입력 데이터 집합 미니배치 $B = \{x_1, x_2, \dots, x_m\}$ 에 대하여 평균과 분산

    $$ \mu _{B} := \dfrac{1}{m}\sum_{i=1}^{m}x_i $$

    $$ \sigma ^{2} _{B} := \dfrac{1}{m}\sum_{i=1}^{m}(x_i - \mu _{B}) ^{2} $$

    을 구한다. 그리고 이를 통하여 입력 데이터 $x_i$ 를 다음과 같이 정규화한다.

    $$ \hat{x}_{i} := \dfrac{x_i - \mu _{B}}{\sqrt[]{\sigma ^{2}_{B}+ \epsilon }} $$

    $\epsilon$ 은 매우 작은 값, 가령 $10 \text{e} -7$ 이다. 이는 $0$ 으로 나누어지는 사고를 예방한다.

    - 결국에 배치 정규화란 입력 데이터 집합 $\{x_1, x_2, \dots, x_m\}$ 을 정규분포를 따르는 집합 $\{\hat{x_1}, \hat{x_2}, \dots, \hat{x_m}\}$ 으로 사상시키는 함수

        $$ f: \R ^{m} \to \R ^{m}, x \mapsto \hat{x} $$

        이다.

    - 배치 정규화층을 활성화 함수 앞 또는 뒤에 삽입합으로써 데이터 분포가 덜 치우치게 할 수 있다.

        - 활성화 함수 앞에 넣을 것인지 뒤에 넣을 것인지에 대한 논의와 실험은 지금도 진행중이다.(arxiv:1502.03167, arxiv:1511.06422)

    그리고 최종적으로 배치 정규화 계층은 정규화된 데이터에 고유한 확대(scale) 와 이동(shift) 변환을 수행한다.

    $$ y_i := \gamma \hat{x}_{i}+\beta $$

    $\gamma$ 가 확대를 하고 $\beta$ 가 이동을 한다. 이 값의 초깃값은 $\gamma = 1, \beta = 0$ 이고, 학습하면서 적절한 값으로 조정해나간다.

- 배치 정규화의 역전파

    https://kratzert.github.io/2016/02/12/understanding-the-gradient-flow-through-the-batch-normalization-layer.html

    https://kevinzakka.github.io/2016/09/14/batch_normalization/

- 배치 정규화를 사용하지 않으면 가중치 초깃값이 잘 분포되어 있지 않으면 학습이 잘 되지 않는다. 

    ![image](https://user-images.githubusercontent.com/16812446/91393412-2eab0900-e875-11ea-9015-fb8edb359323.png)

    또 위와 같이 실험 결과 배치 정규화를 사용하면 가중치 초깃값에 크게 의존하지 않아도 된다는 것이 밝혀졌다.

!!! tldr ""

    과적합(overfitting) : 신경망이 훈련데이터에 지나치게 적응되어 다른 데이터에 제대로 대응하지 못하는 상태이다.

- 오버피팅은 다음 두 경우 발생한다.

    1. 매개변수가 많고 표현력이 높은 모델일 때

    2. 훈련 데이터가 적을 때

- 오버피팅을 일부러 발생시키기 위하여 다음의 코드로 실험해보자. 오버피팅 조건을 충족시키기 위하여 60000개의 MNIST 의 데이터셋을 300개만 사용하고, 7층의 네트워크를 사용해 복잡도가 높은 네트워크를 사용한다.

    ```python
    ...
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True)
    # 오버피팅을 재현하기 위해 학습 데이터 수를 줄임
    x_train = x_train[:300]
    t_train = t_train[:300]

    network = MultiLayerNet(input_size=784, hidden_size_list=[100, 100, 100, 100, 100, 100], output_size=10, weight_decay_lambda=weight_decay_lambda)
    optimizer = SGD(lr=0.01) # 학습률이 0.01인 SGD로 매개변수 갱신

    max_epochs = 201
    train_size = x_train.shape[0]
    batch_size = 100

    train_loss_list = []
    train_acc_list = []
    test_acc_list = []

    iter_per_epoch = max(train_size / batch_size, 1)
    epoch_cnt = 0

    for i in range(1000000000):
        batch_mask = np.random.choice(train_size, batch_size)
        x_batch = x_train[batch_mask]
        t_batch = t_train[batch_mask]

        grads = network.gradient(x_batch, t_batch)
        optimizer.update(network.params, grads)

        if i % iter_per_epoch == 0:
            train_acc = network.accuracy(x_train, t_train)
            test_acc = network.accuracy(x_test, t_test)
            train_acc_list.append(train_acc)
            test_acc_list.append(test_acc)

            print("epoch:" + str(epoch_cnt) + ", train acc:" + str(train_acc) + ", test acc:" + str(test_acc))

            epoch_cnt += 1
            if epoch_cnt >= max_epochs:
                break
    ```

    결과는 다음과 같다.

    ![image](https://user-images.githubusercontent.com/16812446/91396736-433bd100-e876-11ea-91d4-dd4f01ca6358.png)

    훈련 정확도는 매우 높지만 시험 데이터의 정확도는 낮다. 훈련 데이터에 너무 적응(fitting) 되어 버렸기 때문이다.

!!! tldr ""

    가중치 감소(weight decay) : 가중치를 감소시켜 오버피팅을 억제하는 기법이다.

- 가중치 $\mathbf{W}$ 에 대하여 L2 노름에 따른 가중치 감소는 $\dfrac{1}{2}\lambda \mathbf{W}^{2}$ 이 된다. 

    $\lambda$ 는 정규화의 세기를 조절하는 하이퍼 파라미터이다. $\dfrac{1}{2}$ 은 미분의 결과를 편의상 조정하는 상수이다. 
    
    가중치 감소는 모든 가중치 가각의 손실함수에 $\dfrac{1}{2}\lambda \mathbf{W}^{2}$ 를 더한다. 즉 가중치의 기울기를 구하는 계산에서 역전파 법에 따라 정규화항에 미분한 $\lambda \mathbf{W}$ 을 더한다.

    !!! note
    
        정규화항으로 L2 노름, L1 노름, L $\infty$ 노름을 사용할 수 있다. L2 노름은 각 원소의 제곱을 더한 것에 제곱근을 취한다. 가령 가중치가 $\mathbf{W} = (w_1, w_2, \dots, w_n)$ 이었다면 L2 노름에서는 $\sqrt[]{w_1 ^{2} + w_2 ^{2} + \dots + w_n ^{2}}$ 으로 계산할 수 있다.

        L1 노름은 절댓값의 합, $|w_1| + |w_2| + \dots + |w_n|$ 이다. L $\infty$ 노름은 Max 노름으로써 각 원소의 절댓값중 가장 큰 것이다.

        일반적으로 L2 노름을 자주 쓴다.

- 오버피팅은 가중치 매개변수의 값이 커서 발생하는 경우가 많기 때문에 가중치 감소를 사용하기도 한다.

- 손실 함수에 가중치의 L2 노름을 더한 가중치 감소를 적용한 실험 결과

    ![image](https://user-images.githubusercontent.com/16812446/91395674-f0fab000-e875-11ea-989d-226fc14cb6f2.png)

    오버피팅이 그나마 억제되었다.

!!! tldr ""

    드롭아웃(Dropout) : 뉴런을 무작위로 삭제하면서 학습하는 방법이다.

- 신경망 모델이 복잡해지면 가중치 감소만으로 오버피팅을 억제하기 힘들어진다. 이럴 때 드롭아웃을 사용한다.

- 드롭아웃은 훈련 때 삭제할 뉴런을 무작위로 선택하고, 검증 때 모든 뉴런에 신호를 전달한다.

    단, 시험 때 각 뉴런의 출력에 훈련 때 삭제한 비율을 곱하여 출력한다.

    그런데 실제 딥러닝 프레임워크들은 삭제한 비율을 곱하지 않기도 한다. 효율적인 구현에 대해서는 chainer.org 의 드롭아웃 구현을 참고하면 좋다.

!!! tldr ""

    앙상블 학습(ensemble learning) : 개별적으로 학습시킨 여러 모델의 출력의 평균을 내어 추론하는 방식이다.

- 앙상블 학습을 사용하면 신경망의 정확도가 몇% 개선된다고 실험적으로 알려져 있다.

- 가령 같거나 비슷한 구조의 모델을 5개를 따로 학습시키고 5개의 출력의 평균을 내어 답을 내는 것이다.

!!! tldr ""

    하이퍼파라미터 : 뉴런의 개수, 배치의 크기, 매개변수 갱신 학습률 등의 변수들이다.

- 하이퍼파라미터 성능을 평가할 때는 시험 데이터를 사용하면 안된다. 하이퍼파라미터를 시험 데이터로 조정하면 시험 데이터에 오버피팅 되기 때문이다.

    따라서 하이퍼파라미터 전용 데이터를 따로 두고 이것을 검증 데이터라고 부른다. 

    !!! note
    
        그러므로 데이터를 다음과 같이 분류할 수 있다. 

        - 훈련 데이터 : 매개변수(가중치, 편향) 학습용

        - 검증 데이터 : 하이퍼파라미터 성능 평가용

        - 시험 데이터 : 신경망 전반 성능 평가용

- 보통 훈련 데이터의 20% 정도를 검증 데이터로 분리시켜 학습한다.

!!! tldr ""

    하이퍼파라미터 최적화 : 하이퍼파라미터를 최적화 시킬 때는 최적값이 존재하는 범위를 조금씩 줄여나간다.

- 가령 하이퍼파라미터를 $0.001$ 에서 $1000$ 사이의 $10$ 의 거듭제곱 단위 범위로 정하고 학습을 시켜보면서 정확도를 평가한다.

    이때 하이퍼파라미터를 최적화시킬 때 시간이 매우 오래 걸린다. 따라서 아닌 것 같은 값은 일찍 포기해야 하고, 에폭을 작게하여 1회 평가 시간을 단축시켜야 한다.

- 물론 이 방식은 과학이라기보다 실용, 지혜, 직관에 의존한다. 더 세련된 기법을 소개하자면 베이즈 최적화가 있다. 이는 베이즈 정리를 기반으로 더 엄밀하고 효율적인 최적화를 수행한다.
