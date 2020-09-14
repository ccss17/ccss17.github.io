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

- 코드 구현

    다음과 같이 하이퍼파라미터를 로그 스케일 범위에서 무작위로 추출하는 코드를 간단히 짤 수 있다.

    ```python
    weight_decay = 10 ** np.random.uniform(-8, -4)
    lr = 10 ** np.random.uniform(-6, -2)
    ```

    이렇게 균등분포로 하이퍼파라미터를 무작위로 추출하고 학습하여 정확도 순으로 그래프를 그려보면 다음과 같다.

    ![image](https://user-images.githubusercontent.com/16812446/91628211-83c35800-e9f8-11ea-97c7-6c229af1645e.png)

    이때 상위 5개의 하이퍼파라미터를 추출하면 그 결과가 다음과 같다.

    ```shell
    val acc:0.06 | lr:2.1046950927191495e-06, weight decay:2.3489822114211226e-06
    =========== Hyper-Parameter Optimization Result ===========
    Best-1(val acc:0.79) | lr:0.008855979078312936, weight decay:2.9750325705175363e-08
    Best-2(val acc:0.78) | lr:0.008001814164776825, weight decay:2.5759378936377233e-07
    Best-3(val acc:0.78) | lr:0.0066928694143954985, weight decay:9.585002121120948e-07
    Best-4(val acc:0.77) | lr:0.006031604802007462, weight decay:1.3351736344247978e-06
    Best-5(val acc:0.76) | lr:0.005313421478478791, weight decay:3.0638643452015215e-05
    ```

    그러면 좁혀진 이 범위 내에서 또 다시 균등분포를 통해 하이퍼파라미터를 뭐 100 개 쯤 추출하고 똑같은 작업을 반복하는 것이다.

# 합성곱 신경망 CNN

!!! tldr ""

    완전연결, fully-connected, 전결합 : 인접하는 계층의 모든 뉴런이 결합되어 있는 신경망이다.

- 완전 연결 신경망을 Affine 계층으로 구현했었다.

- 완전 연결 신경망(Affine)은 모든 데이터셋을 1차원 데이터로 평탄화하기 때문에 고차원 데이터의 형상과 구조에 담겨있는 패턴과 의미를 포착할 수 없다.

    !!! note
    
        고차원 데이터의 구조와 형상에 의미와 패턴이 있다고 전제하고 있다. 그러나 이것에 대한 엄말한 논의가 필요하다.


!!! tldr ""

    합성곱 신경망, convolutional neural network, CNN : 합성곱 계층으로 이루어진 신경망이다.

- 이미지 인식, 음성 인식 등 다양한 곳에서 사용되는데 특히 이미지 분야에서의 딥러닝은 거의 다 CNN 을 기초로 한다.

- 합성곱은 공학과 물리학에서 널리 쓰이는 수학적 개념이다. 수학적으로 "두 함수 중 하나를 반전(reverse), 이동(shift) 시켜가며 함수와의 곱을 연이어 적분한다" 고 정의할 수 있다.

- Affine 계층을 사용했을 때 가령 신경망을 다음과 같이 이룰 수 있었다.

    ![](https://cdn-ak.f.st-hatena.com/images/fotolife/m/msyksphinz/20170622/20170622015132.png)

    ![](https://t1.daumcdn.net/cfile/tistory/997AE03A5AAAA64C2A?download)

    CNN 구조는 다음과 같이 구성할 수 있다.

    ![](https://media.vlpt.us/post-images/dscwinterstudy/118fa610-4199-11ea-9e80-2dba9507cf00/fig-7-2.png)

    이처럼 CNN 에서는 합성곱 계층 Conv 와 풀링 계층 Pooling 이 추가된다. 지금까지의 [Affine-ReLU] 연결이 [Conv-ReLU-(Pooling)] 연결로 바뀐 것이다. Pooling 은 생략되기도 한다.

- Affine 계층으로 이루어진 신경망은 가령 MNIST 데이터셋의 형상 $1 \times 28 \times 28$ 을 1차원 형상 $1 \times 1 \times 784$ 로 평탄화시켰다. 그러나 합성곱 계층은 데이터의 형상을 유지한다. 이미지도 3차원으로 받고 다음 계층에도 3차원 데이터로 전달한다.

    이로써 엄밀히 증명된 것은 아니지만 CNN 이 이미지 형상을 제대로 이해할 것 같다.

- CNN 에서 합성곱 계층의 입출력 데이터를 특징 맵feature map 이라고 한다.

    합성곱 계층의 입력 데이터를 입력 특징 맵input feature map, 출력 데이터를 출력 특징 맵output feature map 이라고 한다.

- 합성곱 계층에서는 다음과 같이 합성곱 연산을 수행하는데 이는 이미지 처리에서 필터 연산과도 같다.

    왼쪽 행렬($4 \times 4$)이 입력 데이터이고 가운데 행렬($3 \times 3$)이 필터(or 커널 kernel) 이며 오른쪽 행렬($2 \times 2$)이 출력이다.

    ![](https://media.vlpt.us/post-images/dscwinterstudy/1d4ed9d0-4199-11ea-8bd7-d9eb4a57ded4/fig-7-4.png)

    합성곱 연산은 위와 같이 필터의 윈도우(window) 를 일정 간격으로 이동해가면 단일 곱셈-누산(fused multiply-add, FMA) 를 연산하고 그 결과를 출력에 저장한다.

    **그리고 $1 \times 1$ 형상의 편향 bias 를 모든 출력에 더해준다!**

    !!! note
    
        이 합성곱 연산을 과학용 파이썬 라이브러리 SciPy 의 2차원 합성곱 함수(`scipy.signal.convolve2d`) 로 수행하면 결과가 다르게 나온다. 교차상관(cross-correlation) 함수인 `scipy.signal.correlate2d` 를 사용해야 결과가 똑같이 나온다. 

        이는 딥러닝에서 합성곱과 교차상관을 잘 구분하지 않기 때문이다. 주어진 필터를 flipping 하면 합성곱이 되고 하지 않으면 교차상관이 되기 때문이다.

        flipping 이란 행렬의 원소를 좌우, 상하로 한 번씩 뒤집는 것이다. 딥러닝 라이브러리들의 합성곱 함수들은 flipping 을 하지 않거나 flipping 여부를 파라미터로 받는다.

- 합성곱 연산을 수행하기 전 입력 데이터의 주변을 $0$ 으로 채워서 확장하여 패딩을 만들기도 한다.

    ![](https://media.vlpt.us/post-images/dscwinterstudy/282b27a0-4199-11ea-8bd7-d9eb4a57ded4/fig-7-6.png) 

    위 사진은 $(4, 4)$ 크기의 입력 데이터에 폭이 $1$ 인 패딩을 적용여 $(6, 6)$ 으로 만든 것이다.

    !!! note
    
        패딩은 출력 크기를 조정할 목적으로 사용된다. 
        
        $n > m$ 인 $n, m \in \N$ 에 대하여 $(n, n)$ 입력 데이터에 $(m, m)$ 커널을 적용하면 
        
        $$(n - m + 1, n - m + 1)$$ 
        
        형상이 된다. 이로써 입력 데이터의 형상이 끊임없이 줄어들어 언젠가 $(1, 1)$ 이 될 수도 있다. 이렇게 되면 더 이상 합성곱 연산을 적용할 수 없으므로 큰 문제가 된다. 따라서 패딩 $p$ 를 적용함으로써 형상을

        $$(n + 2p - m + 1, n + 2p - m + 1)$$ 

        로 확장해주는 것이다.

- 지금까지 스트라이드stride 는 암묵적으로 $1$ 이 었다. 스트라이드란 필터를 적용하는 위치의 간격이다. 만약 스트라이드를 $2$ 로 하면 필터를 적용하는 윈도우가 두 칸씩 이동한다.

    ![](https://media.vlpt.us/post-images/dscwinterstudy/3084e940-4199-11ea-b8c9-7f7f97d846d5/fig-7-7.png)

    !!! note

        $n > m$ 인 $n, m \in \N$ 에 대하여 $(n, n)$ 입력 데이터에 $(m, m)$ 커널과 패팅 $p$ 와 스트라이드 $s$ 까지 적용하면 그 형상이
        
        $$ \bigg (\dfrac{n + 2p - m}{s} + 1, \dfrac{n + 2p - m }{s}+ 1  \bigg )$$ 

        가 된다. 따라서 이 분수값이 정수로 나누어 떨어져야 하는 것이 중요하다. 딥러닝 프레임워크들은 형상이 나누어떨어지지 않을 때 반올림을 하는 등 에러를 발생시키지 않고 그냥 진행하기도 한다.

- 일반적으로 입력 데이터 $(H, W)$, 커널 $(FH, FW)$, 출력 데이터 $(OH, OW)$, 패딩 $P$, 스트라이드 $S$ 는 다음의 관계를 갖는다.

    $$ (OH, OW) = \bigg ( \dfrac{H+2P-FH}{S} + 1, \dfrac{W + 2P - FW}{S} + 1\bigg ) $$

    !!! example
    
        입력 $(28, 31)$, 패딩 $2$, 스트라이드 $3$, 필터 $(5, 5)$ 에 대한 출력은 

        $$ \bigg (\dfrac{28 + 2 \cdot 2 - 5}{3} + 1, \dfrac{31 + 2 \cdot 2 - 5}{3} + 1\bigg ) = (10, 11) $$

        이다.

!!! tldr ""

    $3$ 차원 데이터 합성곱 연산 : $(H, W)$ 형상에서 채널 축이 추가된 $(C, H, W)$ 형상에 대한 합성곱 연산으로써 각각의 필터의 합성곱 연산을 수행하고 그 결과를 더하여 하나의 출력을 계산한다.

- 이때 물론 입력 데이터의 채널 수와 필터의 채널 수가 같아야 한다.

- 예시 

    다음과 같이 각각의 필터에 대하여 합성곱 연산을 수행하고 그 결과를 모두 더하여 하나의 출력으로 계산한다.

    ![](https://media.vlpt.us/post-images/dscwinterstudy/4d744a50-4199-11ea-8bd7-d9eb4a57ded4/fig-7-9.png)

    위의 예시는 입력 데이터의 채널 수와 필터의 채널 수가 $3$ 으로 일치한다.

- 이러한 3차원 합성곱 연산을 직육면체 블록으로 추상화 시키면 생각하기 쉽다.

    ![](https://3.bp.blogspot.com/-vwlVvtTGnSE/WYJsaj5E2EI/AAAAAAAALNs/qlHKYaW6R0AukJ3qKdReTkuiugqkFfUWgCK4BGAYYCw/s400/o11.PNG)

    !!! note
    
        $3$ 차원 데이터를 다차원 배열로 나타낼 때 여기에서는 (channel, height, width) 순서로 쓴다.

    이렇게 $3$ 차원 입력 데이터에 $3$ 차원 필터로 합성곱 연산을 하면 $2$ 차원 특징 맵이 출력된다. 그런데 이렇게 차원 수가 줄어들게 되면 언젠가 $1$ 차원이 되어버리고 신경망을 깊게 만들 수 없다. 

    따라서 필터를 $4$ 차원으로 하여 출력 특징 맵이 $2$ 차원이 아니라 $3$ 차원으로 나올 수 있도록 할 수 있다.

    ![](https://3.bp.blogspot.com/-Sd2tEjB9ZLQ/WYJtnAea0LI/AAAAAAAALN4/7BFnDCofuusdoPYPB88xUWWIlC5qZzcawCK4BGAYYCw/s400/o12.PNG)

    위와 같이 $4$ 차원 필터를 적용하면 $FN$ 개 채널을 가지는 출력 데이터가 연산된다.

- 마지막으로 다음과 같이 합성곱 연산을 끝낸 후 편향 블록을 더해줌으로써 최종 출력 데이터를 만들어낸다.

    ![](https://1.bp.blogspot.com/-O60db3qXQws/WYJw8NMcTzI/AAAAAAAALOI/7oF6RD68VV08XcOSHdd1vyzfuwTwRiZtwCK4BGAYYCw/s400/o13.PNG)

    위 그림과 같이 편향은 채널 하나 당 하나의 값으로 구성된다.

- 완전연결 신경망에서 매번 하나의 데이터만을 연산하니까 속도가 너무 느려서 배치 처리를 했었다. 같은 이유로 합성곱 연산에서도 배치 처리가 필요하다. 합성곱 연산에서의 배치처리는 단순히 입력 데이터의 차원을 하나 더 늘려서 $4$ 차원 데이터를 만드는 것이다. 

    즉, (channel, height, width) 형상을 (데이터 개수, channel, height, width) 로 바꾸는 것이다.

    ![](https://1.bp.blogspot.com/-O60db3qXQws/WYJw8NMcTzI/AAAAAAAALOI/7oF6RD68VV08XcOSHdd1vyzfuwTwRiZtwCK4BGAYYCw/s400/o13.PNG)

!!! tldr ""

    풀링(Pooling) : 세로, 가로 방향의 공간을 줄이는 연산이다.

- 풀링에서의 윈도우 크기와 스트라이드는 같은 값으로 설정하는 것이 일반적이다.

    !!! example
    
        풀링 윈도우가 $3 \times 3$ 이면 스트라이드를 $3$ 으로, 풀링 윈도우가 $4 \times 4$ 이면 스트라이드를 $4$ 로 정한다.

!!! tldr ""

    최대 풀링(max pooling) : 풀링 윈도우에서 최댓값을 구하여 새로운 데이터 원소로 정하는 연산이다.


- 다음 그림은 $2 \times 2$ 최대 풀링을 스트라이드 $2$ 로 처리하는 과정을 보여준다.

    ![](https://media.vlpt.us/post-images/dscwinterstudy/590eb800-4199-11ea-8bd7-d9eb4a57ded4/fig-7-14.png)

    단순히 $2 \times 2$ 영역에서 가장 큰 값을 새로운 데이터의 원소로 정한다.

!!! tldr ""

    평균 풀링(average pooling) : 풀링 윈도우에서 평균을 구하여 새로운 데이터 원소로 정하는 연산이다.

- 하지만 이미지 인식 분야에서는 보통 max pooling 을 사용한다.

!!! tldr ""

    최소 풀링(min pooling) : 풀링 윈도우에서 최소값을 구하여 새로운 데이터 원소로 정하는 연산이다.

- 하지만 이미지 인식 분야에서는 보통 max pooling 을 사용한다.

!!! tldr ""

    풀링 계층 : 풀링 연산을 하는 신경망 계층이다.

- 풀링 계층에서는 가중치 매개변수가 없고, 학습해야할 것도 없다.

- 풀링 계층을 지나쳐도 채널 수는 변하지 않는다.

- 입력 데이터가 조금 변해도 풀링의 결과는 잘 변하지 않는다.


!!! tldr ""

    im2col : CNN 의 $4$ 차원 데이터를 $2$ 차원 행렬로 변형시키고 $4$ 차원 필터도 $2$ 차원 행렬로 변환시켜서 합성곱 연산을 행렬곱으로 단순화시키는 트릭이다.

- im2col 은 입력 데이터에서 필터를 적용하는 3차원 블록 영역을 한 줄로 늘어뜨린다. 이것을 필터가 적용되는 모든 영역에서 수행한다.

- 다음 그림은 그냥 보기 좋게끔 필터의 적용 영역이 겹치지 않도록 스트라이드를 적절히 설정하여 im2col 을 전개한 모습이다.

    ![](https://petewarden.files.wordpress.com/2015/04/im2col_corrected.png?w=550&h=252)

    *출처: https://petewarden.com/2015/04/20/why-gemm-is-at-the-heart-of-deep-learning/*

    그러나 실제로는 영역이 겹치는 경우가 대부분이다. 따라서 필터 적용 영역이 중복될 때 im2col 을 전개하면 원소 수가 원래의 블록의 원소 보다 많아진다. 이로써 메모리가 낭비된다.

    그럼에도 im2col 을 사용하는 것은 컴퓨터 자체가 큰 행렬을 묶어서 계산하는데 탁월하기 때문이다. 행렬 계산 라이브러리, 선형 대수 라이브러리 등은 큰 행렬을 빠르게 계산할 수 있도록 최적화되어 있다. 

- 입력 데이터를 im2col 로 전개한 다음에 필터(가중치)를 1열로 전개하고 두 행렬곱을 계산하면 된다.

    ![](https://petewarden.files.wordpress.com/2015/04/im2colmult_corrected1.png?w=550&h=331)

    *출처: https://petewarden.com/2015/04/20/why-gemm-is-at-the-heart-of-deep-learning/*

    위 그림과 같이 입력 데이터가 행으로 변환된 행렬이 되었고, 커널이 열로 변환된 행렬이 되었다. 합성곱을 수행하는 것이 이제 행렬곱이 되었다!

- **이 행렬곱 연산의 결과는 $2$ 차원 출력 데이터가 된다.** ^^CNN 은 데이터를 $4$ 차원 배열로 저장하기 때문에 이것을 다시 $4$ 차원으로 reshape 해주는 것으로 합성곱 계층의 구현이 마무리된다.^^

- 코드 구현 

    ```python
    def im2col(input_data, filter_h, filter_w, stride=1, pad=0):
        """
        input_data : 4차원 배열 형태의 입력 데이터(이미지 수, 채널 수, 높이, 너비)
        filter_h : 필터의 높이
        filter_w : 필터의 너비
        stride : 스트라이드
        pad : 패딩
        """
        N, C, H, W = input_data.shape
        out_h = (H + 2*pad - filter_h)//stride + 1
        out_w = (W + 2*pad - filter_w)//stride + 1

        img = np.pad(input_data, [(0,0), (0,0), (pad, pad), (pad, pad)], 'constant')
        col = np.zeros((N, C, filter_h, filter_w, out_h, out_w))

        for y in range(filter_h):
            y_max = y + stride*out_h
            for x in range(filter_w):
                x_max = x + stride*out_w
                col[:, :, y, x, :, :] = img[:, :, y:y_max:stride, x:x_max:stride]

        col = col.transpose(0, 4, 5, 1, 2, 3).reshape(N*out_h*out_w, -1)
        return col


    def col2im(col, input_shape, filter_h, filter_w, stride=1, pad=0):
        """
        col : 2차원 배열(입력 데이터)
        input_shape : 원래 이미지 데이터의 형상（예：(10, 1, 28, 28)）
        filter_h : 필터의 높이
        filter_w : 필터의 너비
        stride : 스트라이드
        pad : 패딩
        """
        N, C, H, W = input_shape
        out_h = (H + 2*pad - filter_h)//stride + 1
        out_w = (W + 2*pad - filter_w)//stride + 1
        col = col.reshape(N, out_h, out_w, C, filter_h, filter_w).transpose(0, 3, 4, 5, 1, 2)

        img = np.zeros((N, C, H + 2*pad + stride - 1, W + 2*pad + stride - 1))
        for y in range(filter_h):
            y_max = y + stride*out_h
            for x in range(filter_w):
                x_max = x + stride*out_w
                img[:, :, y:y_max:stride, x:x_max:stride] += col[:, :, y, x, :, :]

        return img[:, :, pad:H + pad, pad:W + pad]
    ```

!!! tldr ""

    합성곱 계층 구현 : `im2col` 을 사용하면 합성곱 계층을 간단하게 구현할 수 있다. 

- 합성곱 순전파 구현

    ```python linenums="1" hl_lines="14-17"
    class Convolution:
        def __init__(self, W, b, stride=1, pad=0):
            self.W = W
            self.b = b
            self.stride = stride
            self.pad = pad
            
        def forward(self, x):
            FN, C, FH, FW = self.W.shape
            N, C, H, W = x.shape
            out_h = 1 + int((H + 2*self.pad - FH) / self.stride)
            out_w = 1 + int((W + 2*self.pad - FW) / self.stride)

            col = im2col(x, FH, FW, self.stride, self.pad)
            col_W = self.W.reshape(FN, -1).T
            out = np.dot(col, col_W) + self.b
            out = out.reshape(N, out_h, out_w, -1).transpose(0, 3, 1, 2)

            self.x = x
            self.col = col
            self.col_W = col_W

            return out
    ```

    결국 14~17 이 합성곱 계층의 핵심이다. 4차원 데이터를 2차원 데이터로 평탄화 시킨 후 단지 행렬곱으로 합성곱을 효율적으로 수행한 후 다시 데이터를 원래 형상으로 바꾸어 준다. 마지막으로 `transpose` 함수로 축 순서를 변경하여 `(N, H, W, C)` 형상을 `(N, C, H, W)` 로 되돌려 준다.

- 합성곱 역전파 구현

    CNN 순전파가 행렬곱으로 이루어진 탓에 Affine 계층과 순전파가 비슷하고 역전파도 비슷하다. 단, `im2col` 연산을 역으로 처리해주어야 한다. 이는 `col2im` 함수를 이용하면 된다. `col2im` 을 사용한다는 점만 제외하면 Affine 계층과 역전파가 똑같다.

    ```python
    class Convolution:
        def __init__(self, W, b, stride=1, pad=0):
            self.W = W
            self.b = b
            self.stride = stride
            self.pad = pad
            
            # 중간 데이터（backward 시 사용）
            self.x = None   
            self.col = None
            self.col_W = None
            
            # 가중치와 편향 매개변수의 기울기
            self.dW = None
            self.db = None

        def forward(self, x):
            ...

        def backward(self, dout):
            FN, C, FH, FW = self.W.shape
            dout = dout.transpose(0,2,3,1).reshape(-1, FN)

            self.db = np.sum(dout, axis=0)
            self.dW = np.dot(self.col.T, dout)
            self.dW = self.dW.transpose(1, 0).reshape(FN, C, FH, FW)

            dcol = np.dot(dout, self.col_W.T)
            dx = col2im(dcol, self.x.shape, FH, FW, self.stride, self.pad)

            return dx
    ```

!!! tldr ""

    풀링 계층 구현 : `im2col` 을 사용해 입력 데이터를 전개하는 식으로 구현하면 된다.

- 입력 데이터를 다음과 같이 전개하면 행렬에서 행별 최댓값을 구할 수 있다.

    ![](https://images4.programmersought.com/849/18/180c55f02633bec41d7daa3c2a20ba81.png)

    풀링 계층은 위와 같이 채널을 독립적으로 `im2col` 을 전개한다. 그리고 다음과 같이 형상을 다시 맞춰준다. 

    ![](https://media.vlpt.us/post-images/dscwinterstudy/943b08c0-4199-11ea-9479-ad3ff669a3cd/fig-7-22.png)

- 코드 구현 

    ```python linenums="1" hl_lines="16 17"
    class Pooling:
        def __init__(self, pool_h, pool_w, stride=1, pad=0):
            self.pool_h = pool_h
            self.pool_w = pool_w
            self.stride = stride
            self.pad = pad
            
            self.x = None
            self.arg_max = None

        def forward(self, x):
            N, C, H, W = x.shape
            out_h = int(1 + (H - self.pool_h) / self.stride)
            out_w = int(1 + (W - self.pool_w) / self.stride)

            col = im2col(x, self.pool_h, self.pool_w, self.stride, self.pad)
            col = col.reshape(-1, self.pool_h*self.pool_w)

            arg_max = np.argmax(col, axis=1)
            out = np.max(col, axis=1)
            out = out.reshape(N, out_h, out_w, C).transpose(0, 3, 1, 2)

            self.x = x
            self.arg_max = arg_max

            return out

        def backward(self, dout):
            dout = dout.transpose(0, 2, 3, 1)
            
            pool_size = self.pool_h * self.pool_w
            dmax = np.zeros((dout.size, pool_size))
            dmax[np.arange(self.arg_max.size), self.arg_max.flatten()] = dout.flatten()
            dmax = dmax.reshape(dout.shape + (pool_size,)) 
            
            dcol = dmax.reshape(dmax.shape[0] * dmax.shape[1] * dmax.shape[2], -1)
            dx = col2im(dcol, self.x.shape, self.pool_h, self.pool_w, self.stride, self.pad)
            
            return dx
    ```

    풀링 계층의 구현은 위에서 강조한 코드가 핵심이다. 행별 맥스 풀링을 구하고 형상을 원래대로 되돌려 준다.

- 역전파

    풀링 계층의 역전파는 ReLU 계층을 구현할 때 사용한 max 의 역전파와 비슷하다.

!!! tldr ""

    CNN 구현 : CNN 구현은 보통 [Conv(합성곱)-ReLU-Pooling] - [Conv(합성곱)-ReLU-Pooling] - ... - [Conv(합성곱)-ReLU-Pooling] - [Fc(완전연결 Affine)-ReLu] - [Fc - Softmax] 로 이루어진다.

- Simple CNN 코드 구현 

    ```python linenums="1"
    class SimpleConvNet:
        """단순한 합성곱 신경망
        
        conv - relu - pool - affine - relu - affine - softmax
        
        Parameters
        ----------
        input_size : 입력 크기（MNIST의 경우엔 784）
        hidden_size_list : 각 은닉층의 뉴런 수를 담은 리스트（e.g. [100, 100, 100]）
        output_size : 출력 크기（MNIST의 경우엔 10）
        activation : 활성화 함수 - 'relu' 혹은 'sigmoid'
        weight_init_std : 가중치의 표준편차 지정（e.g. 0.01）
            'relu'나 'he'로 지정하면 'He 초깃값'으로 설정
            'sigmoid'나 'xavier'로 지정하면 'Xavier 초깃값'으로 설정
        """
        def __init__(self, input_dim=(1, 28, 28), 
                    conv_param={'filter_num':30, 'filter_size':5, 'pad':0, 'stride':1},
                    hidden_size=100, output_size=10, weight_init_std=0.01):
            filter_num = conv_param['filter_num']
            filter_size = conv_param['filter_size']
            filter_pad = conv_param['pad']
            filter_stride = conv_param['stride']
            input_size = input_dim[1]
            conv_output_size = (input_size - filter_size + 2*filter_pad) / filter_stride + 1
            pool_output_size = int(filter_num * (conv_output_size/2) * (conv_output_size/2))
    ```

    합성곱 계층의 하이퍼파라미터를 받아서 저장하고 합성곱 계층의 출력 크기를 계산한다.

    ```python linenums="1"
            # 가중치 초기화
            self.params = {}
            self.params['W1'] = weight_init_std * \
                                np.random.randn(filter_num, input_dim[0], filter_size, filter_size)
            self.params['b1'] = np.zeros(filter_num)
            self.params['W2'] = weight_init_std * \
                                np.random.randn(pool_output_size, hidden_size)
            self.params['b2'] = np.zeros(hidden_size)
            self.params['W3'] = weight_init_std * \
                                np.random.randn(hidden_size, output_size)
            self.params['b3'] = np.zeros(output_size)
    ```

    학습에 필요한 매개변수는 첫번째 층의 합성곱 계층 (`self.params['W1'], self.params['b1']`) 과 나머지 두 완전연결(Fc, Affine) 계층의 가중치와 편향(`self.params['W2'], self.params['b2'], self.params['W3'], self.params['b3']`)이다.

    ```python linenums="1"
            # 계층 생성
            self.layers = OrderedDict()
            self.layers['Conv1'] = Convolution(self.params['W1'], self.params['b1'],
                                            conv_param['stride'], conv_param['pad'])
            self.layers['Relu1'] = Relu()
            self.layers['Pool1'] = Pooling(pool_h=2, pool_w=2, stride=2)
            self.layers['Affine1'] = Affine(self.params['W2'], self.params['b2'])
            self.layers['Relu2'] = Relu()
            self.layers['Affine2'] = Affine(self.params['W3'], self.params['b3'])

            self.last_layer = SoftmaxWithLoss()
    ```

    정의된 하이퍼파라미터와 가중치를 통해 계층을 Simple Convolution Network 를 생성한다.

    ```python linenums="1"
        def predict(self, x):
            for layer in self.layers.values():
                x = layer.forward(x)
            return x

        def loss(self, x, t):
            y = self.predict(x)
            return self.last_layer.forward(y, t)
    ```

    추론을 수행하는 `predict` 와 손실값을 구하는 `loss` 를 구현한다. `x` 로 입력 데이터를 받고 `t` 로 정답 레이블을 전달 받는다. `loss` 가 `predict` 를 내부적으로 호출한다.

    ```python linenums="1"
        def gradient(self, x, t):
            # forward
            self.loss(x, t)

            # backward
            dout = 1
            dout = self.last_layer.backward(dout)

            layers = list(self.layers.values())
            layers.reverse()
            for layer in layers:
                dout = layer.backward(dout)

            # 결과 저장
            grads = {}
            grads['W1'], grads['b1'] = self.layers['Conv1'].dW, self.layers['Conv1'].db
            grads['W2'], grads['b2'] = self.layers['Affine1'].dW, self.layers['Affine1'].db
            grads['W3'], grads['b3'] = self.layers['Affine2'].dW, self.layers['Affine2'].db

            return grads
    ```

    오차역전파법으로 기울기를 구하는 메소드 `gradient` 를 구현한다. `x` 로 입력 데이터를 받고 `t` 로 정답 레이블을 받는다. 이 메소드가 `loss` 메소드를 내부적으로 호출하고 있다.

    ```python linenums="1"
        def accuracy(self, x, t, batch_size=100):
            if t.ndim != 1 : t = np.argmax(t, axis=1)
            
            acc = 0.0
            
            for i in range(int(x.shape[0] / batch_size)):
                tx = x[i*batch_size:(i+1)*batch_size]
                tt = t[i*batch_size:(i+1)*batch_size]
                y = self.predict(tx)
                y = np.argmax(y, axis=1)
                acc += np.sum(y == tt) 
            
            return acc / x.shape[0]

        def numerical_gradient(self, x, t):
            """기울기를 구한다（수치미분）.

            Parameters
            ----------
            x : 입력 데이터
            t : 정답 레이블

            Returns
            -------
            각 층의 기울기를 담은 사전(dictionary) 변수
                grads['W1']、grads['W2']、... 각 층의 가중치
                grads['b1']、grads['b2']、... 각 층의 편향
            """
            loss_w = lambda w: self.loss(x, t)

            grads = {}
            for idx in (1, 2, 3):
                grads['W' + str(idx)] = numerical_gradient(loss_w, self.params['W' + str(idx)])
                grads['b' + str(idx)] = numerical_gradient(loss_w, self.params['b' + str(idx)])

            return grads

        def save_params(self, file_name="params.pkl"):
            params = {}
            for key, val in self.params.items():
                params[key] = val
            with open(file_name, 'wb') as f:
                pickle.dump(params, f)

        def load_params(self, file_name="params.pkl"):
            with open(file_name, 'rb') as f:
                params = pickle.load(f)
            for key, val in params.items():
                self.params[key] = val

            for i, key in enumerate(['Conv1', 'Affine1', 'Affine2']):
                self.layers[key].W = self.params['W' + str(i+1)]
                self.layers[key].b = self.params['b' + str(i+1)]
    ```

    편의 함수를 구현한다. `accuracy` 메소드로 모델의 정확도를 측정하고 `numerical_gradient` 로 기울기가 잘 구해지는지 비교해볼 수 있다. `save_params` 과 `load_params` 로 긴 학습시간을 반복하지 않도록 가중치를 저장하고 불러올 수 있다.

- 이 Simple Convolution Network 로 MNIST 를 학습하면 훈련데이터의 정확도가 99.82% 가 나오고 시험데이터의 정확도가 98.96% 가 나온다. 층을 더욱 깊게 만들면 정확도를 99% 로 만들 수 있다.

!!! tldr ""

    CNN 시각화 : CNN 이 실제로 이미지 데이터에서 무엇을 학습하는지 알 수 있게 해주는 기법이다.

- 위에서 구현한 Simple Convolution Network 의 첫번째 계층, 즉 합성곱 계층의 가중치가 무엇을 학습하는지 알아보자. 가중치 형상은 `(1,5,5)` 에 `30` 개 필터라서 형상이 `(30, 1, 5, 5)` 였다.

    ![](https://media.vlpt.us/post-images/dscwinterstudy/b0d98ab0-4199-11ea-bed1-737062fffe57/fig-7-24.png)

    학습 전에는 왼쪽 그림과 같이 가중치가 불규칙하게 설정되어 있지만 학습 후에는 오른쪽 그림과 같이 규칙성 있는  이미지가 되었다. 가중치의 숫자가 `0` 에 가까울수록 검은색으로 `255` 에 가까울수록 흰색으로 표현했다.

    왼쪽 절반이 흰색이고 오른쪽 절반이 검은색인 필터는 세로 방향의 테두리에 반응하고

    아래쪽 절반이 흰색이고 위쪽 절반이 검은색인 필터는 가로 방향의 테두리에 반응한다.