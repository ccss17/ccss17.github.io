# Deep Learning from Scratch

[밑바닥부터 시작하는 딥러닝](https://book.naver.com/bookdb/book_detail.nhn?bid=11492334)의 개인 메모입니다.

# 경사 하강법 


!!! tldr ""

    경사법 : 기울기 벡터를 사용하여 손실함수 값을 최소로 만드는 방법을 찾는 알고리즘이다.

- 하지만 기울기가 가리키는 곳에 함수의 최솟값이 존재하는지 확신할 수 없다. 실제로 복잡한 함수에서는 기울기가 가르키는 방향에 최솟값이 없는 경우가 대부분이다. 또 복잡하고 찌그러진 함수에서 평평한 곳으로 파고들면 고원(plateau)이라고 하는 학습이 정체되는 공간에 수렴할 수도 있다.

    기울기의 방향이 반드시 최소값을 가르키는 것은 아니지만 일단 그 방향으로 가면 함수의 값을 줄일 수 있기 때문에 일단 기울기를 단서로 나아갈 방향을 정하는 것이다.
    
    경사법에서는 그 기울기 방향으로 일정 거리만큼 이동하여 또 기울기를 구한다. 그런데 기울어져 있으면 또 그방향으로 일정 거리 나아가본다. 이렇게 계속 기울기 방향으로 나아가서 손실 함수 값을 줄여보는 것이 경사법이다.

- 최솟값을 찾는다면 그것을 경사하강법(gradient descent method)이라고 하고, 최댓값을 찾는다면 경사 상승법(gradient ascent method)이라고한다.

- 경사법을 수식으로 나타내면 학습률 $\eta \in \mathbb{R}$ 과 가중치 벡터 $\mathbf{w} \in \mathbb{R} ^{n}$ 에 대하여

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

!!! tldr ""

    신경망 학습 알고리즘 : 신경망 학습 알고리즘은 다음의 1~3단계를 에폭만큼, 또는 수용가능 오차도가 산출될때까지 반복하여 가중치와 편향을 훈련 데이터에 적합하도록 조정하는 알고리즘이다.
    
    1. (미니배치) 훈련 데이터 중 일부를 무작위로 추출한다. 이 일부 데이터를 미니배치라고 하며, 이 미니배치의 손실 함수 값을 줄이는 것이 신경망 학습의 목표이다.
    
    2. (기울기 산출) 손실함수에 대한 가중치 행렬의 기울기를 구한다. 이 기울기 벡터로 손실함수 값을 줄이는 방향에 대한 단서를 얻는다. 
    
    3. (가중치 학습) 가중치 매개변수를 기울기 방향으로 학습률만큼 갱신한다.

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

- 오차역전파가 적용된 코드 구현

    ```python
    class TwoLayerNet:
        def __init__(self, input_size, hidden_size, output_size, weight_init_std = 0.01):
            # 가중치 초기화
            self.params = {}
            self.params['W1'] = weight_init_std * np.random.randn(input_size, hidden_size)
            self.params['b1'] = np.zeros(hidden_size)
            self.params['W2'] = weight_init_std * np.random.randn(hidden_size, output_size) 
            self.params['b2'] = np.zeros(output_size)

            # 계층 생성
            self.layers = OrderedDict()
            self.layers['Affine1'] = Affine(self.params['W1'], self.params['b1'])
            self.layers['Relu1'] = Relu()
            self.layers['Affine2'] = Affine(self.params['W2'], self.params['b2'])

            self.lastLayer = SoftmaxWithLoss()
            
        def predict(self, x):
            for layer in self.layers.values():
                x = layer.forward(x)
            
            return x
            
        # x : 입력 데이터, t : 정답 레이블
        def loss(self, x, t):
            y = self.predict(x)
            return self.lastLayer.forward(y, t)
        
        def accuracy(self, x, t):
            y = self.predict(x)
            y = np.argmax(y, axis=1)
            if t.ndim != 1 : t = np.argmax(t, axis=1)
            
            accuracy = np.sum(y == t) / float(x.shape[0])
            return accuracy
            
        # x : 입력 데이터, t : 정답 레이블
        def numerical_gradient(self, x, t):
            loss_W = lambda W: self.loss(x, t)
            
            grads = {}
            grads['W1'] = numerical_gradient(loss_W, self.params['W1'])
            grads['b1'] = numerical_gradient(loss_W, self.params['b1'])
            grads['W2'] = numerical_gradient(loss_W, self.params['W2'])
            grads['b2'] = numerical_gradient(loss_W, self.params['b2'])
            
            return grads
            
        def gradient(self, x, t):
            # forward
            self.loss(x, t)

            # backward
            dout = 1
            dout = self.lastLayer.backward(dout)
            
            layers = list(self.layers.values())
            layers.reverse()
            for layer in layers:
                dout = layer.backward(dout)

            # 결과 저장
            grads = {}
            grads['W1'], grads['b1'] = self.layers['Affine1'].dW, self.layers['Affine1'].db
            grads['W2'], grads['b2'] = self.layers['Affine2'].dW, self.layers['Affine2'].db

            return grads
    ```

    이 역전파를 사용하는 신경망 학습을 실제로 사용하는 코드는 다음과 같다. 

    ```python
    # coding: utf-8
    import sys, os
    sys.path.append(os.pardir)

    import numpy as np
    from dataset.mnist import load_mnist
    from two_layer_net import TwoLayerNet

    # 데이터 읽기
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

    network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

    iters_num = 10000
    train_size = x_train.shape[0]
    batch_size = 100
    learning_rate = 0.1

    train_loss_list = []
    train_acc_list = []
    test_acc_list = []

    iter_per_epoch = max(train_size / batch_size, 1)

    for i in range(iters_num):
        batch_mask = np.random.choice(train_size, batch_size)
        x_batch = x_train[batch_mask]
        t_batch = t_train[batch_mask]
        
        # 기울기 계산
        #grad = network.numerical_gradient(x_batch, t_batch) # 수치 미분 방식
        grad = network.gradient(x_batch, t_batch) # 오차역전파법 방식(훨씬 빠르다)
        
        # 갱신
        for key in ('W1', 'b1', 'W2', 'b2'):
            network.params[key] -= learning_rate * grad[key]
        
        loss = network.loss(x_batch, t_batch)
        train_loss_list.append(loss)
        
        if i % iter_per_epoch == 0:
            train_acc = network.accuracy(x_train, t_train)
            test_acc = network.accuracy(x_test, t_test)
            train_acc_list.append(train_acc)
            test_acc_list.append(test_acc)
            print(train_acc, test_acc)
    ```

# 오차역전파

!!! tldr ""

    오차역전파 : 신경망 학습에서 수치미분보다 효율적으로 기울기를 계산하는 방법이다.

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

!!! tldr ""

    $n$ 개의 독립변수와 $m$ 개의 매개변수에 대한 다변수 합성함수의 편도함수(chain rule) : 유한개의 매개변수 $x_1, x_2, \dots, x_m$ 에 대한 다변수 함수 $w = f(x_1, x_2, \dots, x_m)$ 가 미분가능하고,
    
    $n$ 개의 독립변수 $p_1, p_2, \dots, p_n$ 에 대한 함수 $x_1, x_2, \dots, x_m$ 도 미분가능하면,

    $w$ 가 미분가능하고 $p_1, p_2, \dots, p_n$ 에 대한 함수들도 미분가능하며

    각각의 독립변수에 대한 $w$ 의 편도함수는 다음과 같다. 

    $$ \frac{\partial  w}{\partial p_1} = \frac{\partial w}{\partial x_1}\frac{\partial  x_1}{\partial  p_1} + \frac{\partial w}{\partial x_2}\frac{\partial  x_2}{\partial  p_1} + \dots + \frac{\partial w}{\partial x_m}\frac{\partial  x_m}{\partial  p_1}$$

    $$ \frac{\partial  w}{\partial p_2} = \frac{\partial w}{\partial x_1}\frac{\partial  x_1}{\partial  p_2} + \frac{\partial w}{\partial x_2}\frac{\partial  x_2}{\partial  p_2} + \dots + \frac{\partial w}{\partial x_m}\frac{\partial  x_m}{\partial  p_2}$$

    $$ \vdots $$

    $$ \frac{\partial  w}{\partial p_n} = \frac{\partial w}{\partial x_1}\frac{\partial  x_1}{\partial  p_n} + \frac{\partial w}{\partial x_2}\frac{\partial  x_2}{\partial  p_n} + \dots + \frac{\partial w}{\partial x_m}\frac{\partial  x_m}{\partial  p_n}$$

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
    
        **즉, $n \in \mathbb{R}$ 개의 상위 노드로부터 전달된 미분 $\dfrac{\partial L}{\partial u_1},\dfrac{\partial L}{\partial u_2}, \dots, \dfrac{\partial L}{\partial u_n}$ 에 각각의 상위 노드에 대한 자신 $v$ 의 미분 $\dfrac{\partial u_1}{\partial v},\dfrac{\partial u_2}{\partial v}, \dots, \dfrac{\partial u_n}{\partial v}$ 를 곱하고 모두 더한 값**

        $$ \dfrac{\partial L}{\partial u_1}\dfrac{\partial u_1}{\partial v} +\dfrac{\partial L}{\partial u_2}\dfrac{\partial u_2}{\partial v} +\dots+\dfrac{\partial L}{\partial u_n}\dfrac{\partial u_n}{\partial v} $$

        **을 최종적으로 자신의 미분값, 즉 자신이 조금 변했을 때 손실함수가 얼마나 변하는지에 대한 단서로 삼아야 한다.**

!!! tldr ""

    기울기 확인(gradient check) : 오차역전파를 구현하고 제대로 구현했는지 확인하기 위하여 수치미분과 대조하는 것이다.

- **오차역전파는 수치미분의 느린 속도 때문에 개발되었으나 수치미분이 딥러닝에서 완전히 폐기되는 것은 아니다. 왜냐하면 수치 미분으로 오차역전파가 정확하게 구현되었는지 확인할 수 있기 때문이다.**

    수치미분은 구현하기가 상대적으로 쉬워서 코드에 버그가 있기 어려운 반면, 오차역전파의 구현은 다소 복잡해서 버그가 있을 수도 있다.

- 코드 구현 

    ```python
    # 데이터 읽기
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

    network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

    x_batch = x_train[:3]
    t_batch = t_train[:3]

    grad_numerical = network.numerical_gradient(x_batch, t_batch)
    grad_backprop = network.gradient(x_batch, t_batch)

    # 각 가중치의 절대 오차의 평균을 구한다.
    for key in grad_numerical.keys():
        diff = np.average( np.abs(grad_backprop[key] - grad_numerical[key]) )
        print(key + ":" + str(diff))
    ```

    위 코드의 출력이 

    ```python
    b1:9.7e-13
    W1:8.4e-13
    b2:1.1e-10
    W2:2.2e-13
    ```

    로 나왔다면 오차가 $0$ 에 수렴하므로 역전파가 잘 구현되어 있는 것이다.

!!! tldr ""

    덧셈 노드의 역전파 : 입력을 더하여 상위 연산 노드로 전달하는 덧셈 연산 노드의 역전파는 그 미분이 $1$ 이므로 상위 연산 노드에서 전달된 미분에 $1$ 을 곱하여 하위 연산 노드로 전달한다.

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

!!! tldr ""

    곱셈 노드의 역전파 : 입력을 곱하여 상위 연산 노드로 전달하는 곱셈 연산 노드의 역전파는 순전파 때의 그 입력을 제외한 나머지 입력을 곱한 것을 상위 노드에서 역전파된 미분에 곱하여 하위 노드로 전달한다.

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

        역전파 때 상위노드에서 미분 $2.7$ 을 전달했다면 

        $1$ 의 입력을 전달한 하위 노드에 $2.7 \times (2 \times 3 \times 4)$ 를 전달하고

        $2$ 의 입력을 전달한 하위 노드에 $2.7 \times (1 \times 3 \times 4)$ 를 전달하고

        $3$ 의 입력을 전달한 하위 노드에 $2.7 \times (1 \times 2 \times 4)$ 를 전달하고

        $4$ 의 입력을 전달한 하위 노드에 $2.7 \times (1 \times 2 \times 3)$ 를 전달하는 것이다.

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

!!! tldr ""

    나눗셈 노드의 역전파 : 입력 $x$ 의 곱셈의 역원 $\dfrac{1}{x}$ 을 상위 연산 노드로 전달하는 나눗셈 연산 노드의 역전파는 상위노드에 $-\dfrac{1}{x ^{2}}$ 를 곱하여 하류로 전달한다.

- 함수 $y = \dfrac{1}{x}$ 의 미분은 $\dfrac{dy}{dx} = -\dfrac{1}{x ^{2}}$ 이다. 그러므로 역전파 때 상위 노드에서 전달된 값에 $-\dfrac{1}{x ^{2}}$ 를 곱하여 하위 노드로 전달한다.

!!! tldr ""

    $\exp$ 노드의 역전파 : 입력 $x$ 에 대하여 $\exp(x)$ 를 상위 연산 노드로 전달하는 $\exp$ 연산 노드의 역전파는 상위노드에 $\exp (x)$ 를 곱하여 하류로 전달한다.

- 함수 $y = \exp (x)$ 의 미분은 $\dfrac{dy}{dx} = \exp (x)$ 이다. 그러므로 역전파 때 상위 노드에서 전달된 값에 $\exp (x)$ 를 곱하여 하위 노드로 전달한다.

!!! tldr ""

    표준 Sigmoid 활성화 함수의 역전파 : 표준 Sigmoid 함수 $y = \zeta (x) = \text{sigmoid}(x) =: \dfrac{1}{1 + \exp (-x)}$ 의 역전파는 상위노드에 $y(1-y)$ 를 곱하여 하류로 전달한다.

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

!!! tldr ""

    ReLU 활성화 함수의 역전파 : ReLU 함수 $y = \begin{cases} x &(x>0)\\ 0 &(x \leq 0)\\ \end{cases}$ 의 미분은 
    
    $$ \dfrac{dy}{dx} = \begin{cases} 1 &(x>0)\\ 0 &(x \leq 0)\\ \end{cases} $$
    
    이므로 순전파 때 입력 $x$ 가 $0$ 보다 크면 $1$ 을 곱하여 하위 노드로 전달하고 $0$ 이하면 $0$ 을 곱하여 하위 노드로 전달한다.

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

!!! tldr ""

    신경망 순전파 흐름 : $n, m \in \mathbb{N}$ 에 대한 $1 \times n$ 입력행렬 $X$, $n \times m$ 가중치행렬 $W$, $1 \times m$ 편향행렬 $B$ 에 대하여 $1 \times m$ 순입력행렬
    
    $$ Z = X W + B $$
    
    를 활성화 함수 $h:\mathbb{R} ^{m} \to \mathbb{R} ^{m}$ 에 입력하여 얻은 $1 \times m$ 출력행렬 $Y$ 를 다음 층으로 전달하는 것이다.

- 신경망 순전파의 행렬곱을 기하학에서 아핀 변환(affine transformation) 이라고 한다.

    > 아핀 기하학이 유클리드 기하학보다 논리적으로 선행한다는 것을 수학사에서 살펴본 적이 있다.

    - 그래서 아핀 변환(행렬곱)을 처리하는 레이어를 Affine 계층이라는 이름으로 구현한다.

!!! tldr ""

    Affine 변환의 역전파 : 입력 행렬 $\mathbf{X,W}$ 과 출력행렬 $\mathbf{Y} = \mathbf{XW}$ 를 갖는 Affine 레이어의 역전파는 손실값 $L$ 에 대한 $\mathbf{Y}$ 의 미분 $\dfrac{\partial L}{\partial \mathbf{Y}}$ 에 대하여 
    
    $$ \dfrac{\partial L}{\partial \mathbf{X}} = \dfrac{\partial L}{\partial \mathbf{Y}}\cdot \mathbf{W} ^{\intercal } $$
    
    $$ \dfrac{\partial L}{\partial \mathbf{W}} = \mathbf{X}^{\intercal } \dfrac{\partial L}{\partial \mathbf{Y}} $$
    
    이다.

- 아핀 변환 신경망 구성

    ![](https://cdn-ak.f.st-hatena.com/images/fotolife/m/msyksphinz/20170622/20170622015132.png)

- 코드 구현 

    행렬곱 연산과 행렬덧셈 연산을 하는 Affine 레이어는 다음과 같이 코드로 구현할 수 있다.

    ```python
    class Affine:
        def __init__(self, W, b):
            self.W = W
            self.b = b
            self.x = None
            self.dW = None
            self.db = None

        def forward(self, x):
            self.x = x
            out = np.dot(self.x, self.W) + self.b 
            return out

        def backward(self, dout):
            dx = np.dot(dout, self.W.T)
            self.dW = np.dot(self.x.T, dout)
            self.db = np.sum(dout, axis=0) # 살짝 이해 안됨.
            return dx
    ```

    다음 코드는 입력 데이터가 행렬이 아니라 텐서인 경우, 즉 4차원 데이터인 경우도 처리할 수 있도록 구현한 것이다.

    ```python
    class Affine:
        def __init__(self, W, b):
            self.W = W
            self.b = b
            self.x = None
            self.original_x_shape = None
            self.dW = None
            self.db = None

        def forward(self, x):
            # 텐서 대응
            self.original_x_shape = x.shape
            x = x.reshape(x.shape[0], -1) # 이 부분 이해 안됨.
            self.x = x
            out = np.dot(self.x, self.W) + self.b # 입력 행렬을 데이터별로 벡터로 만들고 행렬곱을 개별 가중치 벡터로 한다고? 이해 안됨.
            return out

        def backward(self, dout):
            dx = np.dot(dout, self.W.T)
            self.dW = np.dot(self.x.T, dout)
            self.db = np.sum(dout, axis=0)
            dx = dx.reshape(*self.original_x_shape)  # 입력 데이터 모양 변경(텐서 대응)
            return dx
    ```

- 행렬곱 미분 정리

    http://cs231n.stanford.edu/handouts/derivatives.pdf

    http://cs231n.stanford.edu/handouts/linear-backprop.pdf

    $n \times d$ 입력 행렬 $\mathbf{X}$, $d \times m$ 가중치 행렬 $\mathbf{W}$ 에 대한 $n \times m$ 행렬 $\mathbf{Y=XW}$ 과 손실함수 $l$ 에 대한 스칼라 $L=l(\mathbf{Y})$ 에 대하여 $\mathbf{X}$ 의 미분 (1) 은 

    $$ \dfrac{\partial L}{\partial \mathbf{X}} = \dfrac{\partial L}{\partial \mathbf{Y}}\dfrac{\partial \mathbf{Y}}{\partial \mathbf{X}} = \dfrac{\partial L}{\partial \mathbf{Y}}\mathbf{W}^{\intercal } $$

    이고, $\mathbf{W}$ 의 미분 (2) 은
    
    $$ \dfrac{\partial L}{\partial \mathbf{W}} = \dfrac{\partial L}{\partial \mathbf{Y}}\dfrac{\partial \mathbf{Y}}{\partial \mathbf{W}} = \mathbf{X}^{\intercal } \dfrac{\partial L}{\partial \mathbf{Y}}$$

    이다.

    - (1) 증명

        $n \times d$ 입력 행렬 $\mathbf{X}$, $d \times m$ 가중치 행렬 $\mathbf{W}$ 에 대한 행렬곱 $\mathbf{Y}$ 는 $n \times m$ 행렬

        $$ \mathbf{Y} = \mathbf{XW} = \begin{pmatrix} x _{11}&x _{12}&\dots&x _{1d}\\ x _{21}&x _{22}&\dots&x _{2d}\\ \vdots & \vdots & \ddots & \vdots \\ x _{n1}&x _{n2}&\dots&x _{nd}\\ \end{pmatrix} \begin{pmatrix} w _{11} & w _{12} &\dots & w _{1m} \\ w _{21} & w _{22} &\dots & w _{2m} \\ \vdots & \vdots & \ddots & \vdots \\ w _{d1} & w _{d2} &\dots & w _{dm} \\ \end{pmatrix} $$

        $$ = \begin{pmatrix} \displaystyle \sum_{k=1}^{d}x _{1k} w _{k1} & \displaystyle \sum_{k=1}^{d}x _{1k} w _{k2} & \dots & \displaystyle \sum_{k=1}^{d}x _{1k} w _{km} \\ \displaystyle \sum_{k=1}^{d}x _{2k} w _{k1} & \displaystyle \sum_{k=1}^{d}x _{2k} w _{k2} & \dots & \displaystyle \sum_{k=1}^{d}x _{2k} w _{km} \\ \vdots & \vdots & \ddots & \vdots \\ \displaystyle \sum_{k=1}^{d}x _{nk} w _{k1} & \displaystyle \sum_{k=1}^{d}x _{nk} w _{k2} & \dots & \displaystyle \sum_{k=1}^{d}x _{nk} w _{km} \\ \end{pmatrix} $$

        이다. 이 순전파 출력 $\mathbf{Y}$ 이 손실함수 $l$ 로 전달되어 최종적으로 스칼라 $L$ 이 되었다고 하면 

        $$ L = l(\mathbf{Y}) = l(\mathbf{XW}) $$

        이다.

        $L$ 이 스칼라고 $\mathbf{Y}$ 는 $n \times m$ 행렬이므로 $L$ 에 대한 $\mathbf{Y}$ 의 미분은 $n \times m$ 행렬 

        $$ \dfrac{\partial L}{\partial \mathbf{Y}} = \begin{pmatrix} \dfrac{\partial L}{\partial y _{11}}& \dfrac{\partial L}{\partial y _{12}}& \dots& \dfrac{\partial L}{\partial y _{1m}}\\ \dfrac{\partial L}{\partial y _{21}}& \dfrac{\partial L}{\partial y _{22}}& \dots& \dfrac{\partial L}{\partial y _{2m}}\\ \vdots & \vdots & \ddots & \vdots \\ \dfrac{\partial L}{\partial y _{n1}}& \dfrac{\partial L}{\partial y _{n2}}& \dots& \dfrac{\partial L}{\partial y _{nm}}\\ \end{pmatrix} $$

        이다. $\mathbf{Y}$ 는 $\mathbf{X, W}$ 에 대한 함수이므로 $L$ 에 대한 $\mathbf{X, W}$ 의 미분은 이독립변수와 일매개변수의 합성함수의 미분

        $$ \dfrac{\partial L}{\partial \mathbf{X}} = \dfrac{\partial L}{\partial \mathbf{Y}}\dfrac{\partial \mathbf{Y}}{\partial \mathbf{X}}, \dfrac{\partial L}{\partial \mathbf{W}} = \dfrac{\partial L}{\partial \mathbf{Y}}\dfrac{\partial \mathbf{Y}}{\partial \mathbf{W}} $$

        이다. 이때 $L$ 에 대한 $\mathbf{X}$ 의 미분은 행렬 미분의 정의에 의하여 야코비 행렬

        $$ \dfrac{\partial L}{\partial \mathbf{X}} = \begin{pmatrix} \dfrac{\partial L}{\partial x _{11}}& \dfrac{\partial L}{\partial x _{12}}& \dots& \dfrac{\partial L}{\partial x _{1d}}\\ \dfrac{\partial L}{\partial x _{21}}& \dfrac{\partial L}{\partial x _{22}}& \dots& \dfrac{\partial L}{\partial x _{2d}}\\ \vdots & \vdots & \ddots & \vdots \\ \dfrac{\partial L}{\partial x _{n1}}& \dfrac{\partial L}{\partial x _{n2}}& \dots& \dfrac{\partial L}{\partial x _{nd}}\\ \end{pmatrix} $$

        이다. 이때 $L$ 에 대한 $\mathbf{X}$ 의 $(1,1)$ 원소 $x_{11}$ 의 미분은
        
        $\mathbf{Y}$ 를 행렬이 아니라 매개변수의 나열로 본다면, $\dfrac{\partial L}{\partial x _{11}}$ 에 대한 매개변수를 갖는 합성함수의 편미분으로 나타낼 수 있으므로 스칼라

        $$ \dfrac{\partial L}{\partial x _{11}} = \sum_{i=1}^{n}\sum_{j=1}^{m}\dfrac{\partial L}{\partial y _{ij}}\dfrac{\partial y _{ij}}{\partial x _{11}} $$

        이다. 그런데 귀찮은 덧셈 연산을 피하기 위하여 모든 스칼라 $\dfrac{\partial L}{\partial y _{ij}}$ 들을 행렬 $\dfrac{\partial L}{\partial \mathbf{Y}}$ 로 쓰고, 모든 스칼라 $\dfrac{\partial y _{ij}}{\partial x _{11}}$ 들을 행렬 $\dfrac{\partial \mathbf{Y}}{\partial x _{11}}$ 로 쓰면 이것을 Frobenius 내적

        $$ = \bigg < \dfrac{\partial L}{\partial \mathbf{Y}} , \dfrac{\partial \mathbf{Y}}{\partial x _{11}} \bigg  > _{\mathbf{F}}$$

        으로 나타낼 수 있다. 이때 

        $$ \dfrac{\partial \mathbf{Y}}{\partial x _{11}} = \begin{pmatrix} w _{11}& w _{12}& \dots& w _{1m} \\ 0& 0& \dots& 0\\ \vdots & \vdots & \ddots & \vdots \\ 0& 0& \dots& 0\\ \end{pmatrix} $$

        이므로 

        $$ \bigg < \dfrac{\partial L}{\partial Y} , \dfrac{\partial Y}{\partial x _{11}} \bigg > _{\mathbf{F}} = \Bigg < \begin{pmatrix} \dfrac{\partial L}{\partial y _{11}}& \dfrac{\partial L}{\partial y _{12}}& \dots& \dfrac{\partial L}{\partial y _{1m}}\\ \dfrac{\partial L}{\partial y _{21}}& \dfrac{\partial L}{\partial y _{22}}& \dots& \dfrac{\partial L}{\partial y _{2m}}\\ \vdots & \vdots & \ddots & \vdots \\ \dfrac{\partial L}{\partial y _{n1}}& \dfrac{\partial L}{\partial y _{n2}}& \dots& \dfrac{\partial L}{\partial y _{nm}}\\ \end{pmatrix}, \begin{pmatrix} w _{11}& w _{12}& \dots& w _{1m} \\ 0& 0& \dots& 0\\ \vdots & \vdots & \ddots & \vdots \\ 0& 0& \dots& 0\\ \end{pmatrix}  \Bigg > _{\mathbf{F}} $$

        $$ = \dfrac{\partial L}{\partial y _{11}} w _{11} + \dfrac{\partial L}{\partial y _{12}} w _{12} + \dots+ \dfrac{\partial L}{\partial y _{1m}} w _{1m} = \sum_{k=1}^{m}\dfrac{\partial L}{\partial y _{1k}}w _{1k} $$

        이다. 즉, $\displaystyle \dfrac{\partial L}{\partial x _{11}} = \bigg < \dfrac{\partial L}{\partial \mathbf{Y}} , \dfrac{\partial \mathbf{Y}}{\partial x _{11}} \bigg  > _{\mathbf{F}}= \sum_{k=1}^{m}\dfrac{\partial L}{\partial y _{1k}}w _{1k}$ 이다. 마찬가지로 

        $$\displaystyle \dfrac{\partial L}{\partial x _{12}} = \bigg < \dfrac{\partial L}{\partial \mathbf{Y}} , \dfrac{\partial \mathbf{Y}}{\partial x _{12}} \bigg  > _{\mathbf{F}}= \sum_{k=1}^{m}\dfrac{\partial L}{\partial y _{1k}}w _{2k}$$
        
        $$\displaystyle \dfrac{\partial L}{\partial x _{21}} = \bigg < \dfrac{\partial L}{\partial \mathbf{Y}} , \dfrac{\partial \mathbf{Y}}{\partial x _{21}} \bigg  > _{\mathbf{F}}= \sum_{k=1}^{m}\dfrac{\partial L}{\partial y _{2k}}w _{1k}$$

        $$ \vdots $$
        
        $$\displaystyle \dfrac{\partial L}{\partial x _{ij}} = \bigg < \dfrac{\partial L}{\partial \mathbf{Y}} , \dfrac{\partial \mathbf{Y}}{\partial x _{ij}} \bigg  > _{\mathbf{F}}= \sum_{k=1}^{m}\dfrac{\partial L}{\partial y _{ik}}w _{jk}$$

        이다. 그렇다면 최종적으로 $L$ 에 대한 $\mathbf{X}$ 의 미분은 $n \times d$ 행렬

        $$ \therefore  \dfrac{\partial L}{\partial \mathbf{X}} = \begin{pmatrix} \displaystyle \sum_{k=1}^{m}\dfrac{\partial L}{\partial y _{1k}}w _{1k}& \displaystyle \sum_{k=1}^{m}\dfrac{\partial L}{\partial y _{1k}}w _{2k}& \dots& \displaystyle \sum_{k=1}^{m}\dfrac{\partial L}{\partial y _{1k}}w _{dk} \\ \displaystyle \sum_{k=1}^{m}\dfrac{\partial L}{\partial y _{2k}}w _{1k}& \displaystyle \sum_{k=1}^{m}\dfrac{\partial L}{\partial y _{2k}}w _{2k}& \dots& \displaystyle \sum_{k=1}^{m}\dfrac{\partial L}{\partial y _{2k}}w _{dk} \\ \vdots & \vdots & \ddots & \vdots \\ \displaystyle \sum_{k=1}^{m}\dfrac{\partial L}{\partial y _{nk}}w _{1k}& \displaystyle \sum_{k=1}^{m}\dfrac{\partial L}{\partial y _{nk}}w _{2k}& \dots& \displaystyle \sum_{k=1}^{m}\dfrac{\partial L}{\partial y _{nk}}w _{dk} \\ \end{pmatrix}$$

        $$ = \begin{pmatrix} \dfrac{\partial L}{\partial y _{11}}& \dfrac{\partial L}{\partial y _{12}}& \dots& \dfrac{\partial L}{\partial y _{1m}}\\ \dfrac{\partial L}{\partial y _{21}}& \dfrac{\partial L}{\partial y _{22}}& \dots& \dfrac{\partial L}{\partial y _{2m}}\\ \vdots & \vdots & \ddots & \vdots \\ \dfrac{\partial L}{\partial y _{n1}}& \dfrac{\partial L}{\partial y _{n2}}& \dots& \dfrac{\partial L}{\partial y _{nm}}\\ \end{pmatrix}\begin{pmatrix} w_{11}& w_{21}& \dots & w_{d1} \\ w_{12}& w_{22}& \dots & w_{d2} \\ \vdots & \vdots & \ddots & \vdots \\ w_{1m}& w_{2m}& \dots & w_{dm} \\ \end{pmatrix} $$

        $$ = \boxed{\dfrac{\partial L}{\partial \mathbf{Y}}\mathbf{W}^{\intercal } } $$

        이다. ■ 

    - (2) 증명

        마찬가지로 $L$ 에 대한 $\mathbf{W}$ 의 미분은 행렬 미분의 정의에 의하여 야코비 행렬

        $$ \dfrac{\partial L}{\partial \mathbf{W}} = \begin{pmatrix} \dfrac{\partial L}{\partial w_{11}}& \dfrac{\partial L}{\partial w_{12}}& \dots& \dfrac{\partial L}{\partial w_{1m}}\\ \dfrac{\partial L}{\partial w_{21}}& \dfrac{\partial L}{\partial w_{22}}& \dots& \dfrac{\partial L}{\partial w_{2m}}\\ \vdots & \vdots & \ddots & \vdots \\ \dfrac{\partial L}{\partial w_{d1}}& \dfrac{\partial L}{\partial w_{d2}}& \dots& \dfrac{\partial L}{\partial w_{dm}}\\ \end{pmatrix} $$

        인데 이때 $L$ 에 대한 $\mathbf{W}$ 의 $(1,1)$ 원소 $w _{11}$ 의 미분은 

        $\mathbf{Y}$ 를 행렬이 아니라 매개변수의 나열로 본다면, $\dfrac{\partial L}{\partial w _{11}}$ 에 대한 매개변수를 갖는 합성함수의 편미분으로 나타낼 수 있으므로 스칼라

        $$ \dfrac{\partial L}{\partial w_{11}} = \sum_{i=1}^{n}\sum_{j=1}^{m}\dfrac{\partial L}{\partial y _{ij}}\dfrac{\partial y _{ij}}{\partial w_{11}} $$

        이다. 이것도 마찬가지로 Frobenius 내적 

        $$ = \bigg < \dfrac{\partial L}{\partial \mathbf{Y}} , \dfrac{\partial \mathbf{Y}}{\partial w _{11}} \bigg  > _{\mathbf{F}}$$

        으로 나타낼 수 있다. 그러면 마찬가지로

        $$ \dfrac{\partial \mathbf{Y}}{\partial w _{11}} = \begin{pmatrix} x _{11}& 0& \dots& 0 \\ x _{21}& 0& \dots& 0\\ \vdots & \vdots & \ddots & \vdots \\ x _{n1}& 0& \dots& 0\\ \end{pmatrix} $$

        이므로

        $$ \bigg < \dfrac{\partial L}{\partial \mathbf{Y}} , \dfrac{\partial \mathbf{Y}}{\partial w _{11}} \bigg  > _{\mathbf{F}} = \Bigg < \begin{pmatrix} \dfrac{\partial L}{\partial y _{11}}& \dfrac{\partial L}{\partial y _{12}}& \dots& \dfrac{\partial L}{\partial y _{1m}}\\ \dfrac{\partial L}{\partial y _{21}}& \dfrac{\partial L}{\partial y _{22}}& \dots& \dfrac{\partial L}{\partial y _{2m}}\\ \vdots & \vdots & \ddots & \vdots \\ \dfrac{\partial L}{\partial y _{n1}}& \dfrac{\partial L}{\partial y _{n2}}& \dots& \dfrac{\partial L}{\partial y _{nm}}\\ \end{pmatrix}, \begin{pmatrix} x _{11}& 0& \dots& 0 \\ x _{21}& 0& \dots& 0\\ \vdots & \vdots & \ddots & \vdots \\ x _{n1}& 0& \dots& 0\\ \end{pmatrix} \Bigg > _{\mathbf{F}} $$

        $$ = \dfrac{\partial L}{\partial y _{11}}x _{11} + \dfrac{\partial L}{\partial y _{21}}x _{21} + \dots+ \dfrac{\partial L}{\partial y _{n1}}x _{n1}  = \sum_{k=1}^{n} \dfrac{\partial L}{\partial y _{k1}}x _{k1} $$

        이다. 즉, $\displaystyle \dfrac{\partial L}{\partial w _{11}} = \bigg < \dfrac{\partial L}{\partial \mathbf{Y}} , \dfrac{\partial \mathbf{Y}}{\partial w _{11}} \bigg  > _{\mathbf{F}}= \sum_{k=1}^{n}\dfrac{\partial L}{\partial y _{k1}}x _{k1}$ 이다. 마찬가지로 

        $$\displaystyle \dfrac{\partial L}{\partial w _{12}} = \bigg < \dfrac{\partial L}{\partial \mathbf{Y}} , \dfrac{\partial \mathbf{Y}}{\partial w _{12}} \bigg  > _{\mathbf{F}}= \sum_{k=1}^{n}\dfrac{\partial L}{\partial y _{k2}}x_{k1}$$

        $$\displaystyle \dfrac{\partial L}{\partial w _{21}} = \bigg < \dfrac{\partial L}{\partial \mathbf{Y}} , \dfrac{\partial \mathbf{Y}}{\partial w _{21}} \bigg  > _{\mathbf{F}}= \sum_{k=1}^{n}\dfrac{\partial L}{\partial y _{k1}}x_{k2}$$

        $$ \vdots $$

        $$\displaystyle \dfrac{\partial L}{\partial w _{ij}} = \bigg < \dfrac{\partial L}{\partial \mathbf{Y}} , \dfrac{\partial \mathbf{Y}}{\partial w _{ij}} \bigg  > _{\mathbf{F}}= \sum_{k=1}^{n}\dfrac{\partial L}{\partial y _{kj}}x_{ki}$$

        이다. 그렇다면 최종적으로 $L$ 에 대한 $\mathbf{W}$ 의 미분은 $d \times m$ 행렬

        $$ \therefore \dfrac{\partial L}{\partial \mathbf{W}} = \begin{pmatrix} \displaystyle \sum_{k=1}^{n}\dfrac{\partial L}{\partial y_{k1}}x_{k1}& \displaystyle \sum_{k=1}^{n}\dfrac{\partial L}{\partial y_{k2}}x_{k1}& \dots& \displaystyle \sum_{k=1}^{n}\dfrac{\partial L}{\partial y_{km}}x_{k1} \\ \displaystyle \sum_{k=1}^{n}\dfrac{\partial L}{\partial y_{k1}}x_{k2}& \displaystyle \sum_{k=1}^{n}\dfrac{\partial L}{\partial y_{k2}}x_{k2}& \dots& \displaystyle \sum_{k=1}^{n}\dfrac{\partial L}{\partial y_{km}}x_{k2} \\ \vdots & \vdots & \ddots & \vdots \\ \displaystyle \sum_{k=1}^{n}\dfrac{\partial L}{\partial y_{k1}}x_{kd}& \displaystyle \sum_{k=1}^{n}\dfrac{\partial L}{\partial y_{k2}}x_{kd}& \dots& \displaystyle \sum_{k=1}^{n}\dfrac{\partial L}{\partial y_{km}}x_{kd} \\ \end{pmatrix}$$

        $$ = \begin{pmatrix} x_{11}& x_{21}& \dots & x_{n1} \\ x_{12}& x_{22}& \dots & x_{n2} \\ \vdots & \vdots & \ddots & \vdots \\ x_{1d}& x_{2d}& \dots & x_{nd} \\ \end{pmatrix}\begin{pmatrix} \dfrac{\partial L}{\partial y _{11}}& \dfrac{\partial L}{\partial y _{12}}& \dots& \dfrac{\partial L}{\partial y _{1m}}\\ \dfrac{\partial L}{\partial y _{21}}& \dfrac{\partial L}{\partial y _{22}}& \dots& \dfrac{\partial L}{\partial y _{2m}}\\ \vdots & \vdots & \ddots & \vdots \\ \dfrac{\partial L}{\partial y _{n1}}& \dfrac{\partial L}{\partial y _{n2}}& \dots& \dfrac{\partial L}{\partial y _{nm}}\\ \end{pmatrix} $$

        $$ = \boxed{\mathbf{X}^{\intercal }\dfrac{\partial L}{\partial \mathbf{Y}}} $$

        이다. ■ 

- 행렬덧셈 미분 정리

    $n \times m$ 출력 행렬 $\mathbf{Y}$, $n \times m$ 편향 행렬 $\mathbf{B}$ 에 대한 $n \times m$ 순입력 행렬 $\mathbf{Z=Y + B}$ 과 손실함수 $l$ 에 대한 스칼라 $L=l(\mathbf{Y})$ 에 대하여 $\mathbf{Y}$ 의 미분 (1) 은 

    $$ \dfrac{\partial L}{\partial \mathbf{Y}} = \dfrac{\partial L}{\partial \mathbf{Z}} $$ 

    이고, $\mathbf{W}$ 의 미분 (2) 은
    
    $$ \dfrac{\partial L}{\partial \mathbf{B}} = \dfrac{\partial L}{\partial \mathbf{Z}} $$ 

    이다.

    - (1) 증명

        $n \times m$ 출력 행렬 $\mathbf{Y}$, $n \times m$ 편향 행렬 $\mathbf{B}$ 에 대한 행렬 $\mathbf{Z = Y + B}$ 는 $n \times m$ 행렬

        $$ \mathbf{Z} = \mathbf{Y + B} = \begin{pmatrix} y_{11}&y_{12}&\dots&y_{1m}\\ y_{21}&y_{22}&\dots&y_{2m}\\ \vdots & \vdots & \ddots & \vdots \\ y_{n1}&y_{n2}&\dots&y_{nm}\\ \end{pmatrix} + \begin{pmatrix} b_{11} & b_{12} &\dots & b_{1m} \\ b_{21} & b_{22} &\dots & b_{2m} \\ \vdots & \vdots & \ddots & \vdots \\ b_{n1} & b_{n2} &\dots & b_{nm} \\ \end{pmatrix} $$

        $$ = \begin{pmatrix} \displaystyle y_{11}+b_{11} & \displaystyle y_{12}+b_{12} & \dots & \displaystyle y_{1m}+b_{1m} \\ \displaystyle y_{21}+b_{21} & \displaystyle y_{22}+b_{22} & \dots & \displaystyle y_{2m}+b_{2m} \\ \vdots & \vdots & \ddots & \vdots \\ \displaystyle y_{n1}+b_{n1} & \displaystyle y_{n2}+b_{n2} & \dots & \displaystyle y_{nm}+b_{nm} \\ \end{pmatrix} $$

        이다. 이 $\mathbf{Z}$ 이 손실함수 $l$ 로 전달되어 최종적으로 스칼라 $L$ 이 되었다고 하면 

        $$ L = l(\mathbf{Z}) = l(\mathbf{Y + B}) $$

        이다.

        $L$ 이 스칼라고 $\mathbf{Z}$ 는 $n \times m$ 행렬이므로 $L$ 에 대한 $\mathbf{Z}$ 의 미분은 $n \times m$ 행렬 

        $$ \dfrac{\partial L}{\partial \mathbf{Z}} = \begin{pmatrix} \dfrac{\partial L}{\partial z_{11}}& \dfrac{\partial L}{\partial z_{12}}& \dots& \dfrac{\partial L}{\partial z_{1m}}\\ \dfrac{\partial L}{\partial z_{21}}& \dfrac{\partial L}{\partial z_{22}}& \dots& \dfrac{\partial L}{\partial z_{2m}}\\ \vdots & \vdots & \ddots & \vdots \\ \dfrac{\partial L}{\partial z_{n1}}& \dfrac{\partial L}{\partial z_{n2}}& \dots& \dfrac{\partial L}{\partial z_{nm}}\\ \end{pmatrix} $$

        이다. $\mathbf{Z}$ 는 $\mathbf{Y, B}$ 에 대한 함수이므로 $L$ 에 대한 $\mathbf{Y, B}$ 의 미분은 이독립변수와 일매개변수의 합성함수의 미분

        $$ \dfrac{\partial L}{\partial \mathbf{Y}} = \dfrac{\partial L}{\partial \mathbf{Z}}\dfrac{\partial \mathbf{Z}}{\partial \mathbf{Y}}, \dfrac{\partial L}{\partial \mathbf{B}} = \dfrac{\partial L}{\partial \mathbf{Z}}\dfrac{\partial \mathbf{Z}}{\partial \mathbf{B}} $$

        이다. 이때 $L$ 에 대한 $\mathbf{Y}$ 의 미분은 행렬 미분의 정의에 의하여 야코비 행렬

        $$ \dfrac{\partial L}{\partial \mathbf{Y}} = \begin{pmatrix} \dfrac{\partial L}{\partial y_{11}}& \dfrac{\partial L}{\partial y_{12}}& \dots& \dfrac{\partial L}{\partial y_{1m}}\\ \dfrac{\partial L}{\partial y_{21}}& \dfrac{\partial L}{\partial y_{22}}& \dots& \dfrac{\partial L}{\partial y_{2m}}\\ \vdots & \vdots & \ddots & \vdots \\ \dfrac{\partial L}{\partial y_{n1}}& \dfrac{\partial L}{\partial y_{n2}}& \dots& \dfrac{\partial L}{\partial y_{nm}}\\ \end{pmatrix} $$

        이다. 이때 $L$ 에 대한 $\mathbf{Y}$ 의 $(1,1)$ 원소 $y_{11}$ 의 미분은
        
        $\mathbf{Z}$ 를 행렬이 아니라 매개변수의 나열로 본다면, $\dfrac{\partial L}{\partial y_{11}}$ 에 대한 매개변수를 갖는 합성함수의 편미분으로 나타낼 수 있으므로 스칼라

        $$ \dfrac{\partial L}{\partial y_{11}} = \sum_{i=1}^{n}\sum_{j=1}^{m}\dfrac{\partial L}{\partial z _{ij}}\dfrac{\partial z _{ij}}{\partial y_{11}} $$

        이다. 그런데 귀찮은 덧셈 연산을 피하기 위하여 모든 스칼라 $\dfrac{\partial L}{\partial z _{ij}}$ 들을 행렬 $\dfrac{\partial L}{\partial \mathbf{Z}}$ 로 쓰고, 모든 스칼라 $\dfrac{\partial z _{ij}}{\partial y_{11}}$ 들을 행렬 $\dfrac{\partial \mathbf{Z}}{\partial y_{11}}$ 로 쓰면 이것을 Frobenius 내적

        $$ = \bigg < \dfrac{\partial L}{\partial \mathbf{Z}} , \dfrac{\partial \mathbf{Z}}{\partial y_{11}} \bigg  > _{\mathbf{F}}$$

        으로 나타낼 수 있다. 이때 

        $$ \dfrac{\partial \mathbf{Z}}{\partial y_{11}} = \begin{pmatrix} 1 & 0& \dots& 0 \\ 0& 0& \dots& 0\\ \vdots & \vdots & \ddots & \vdots \\ 0& 0& \dots& 0\\ \end{pmatrix} $$

        이므로 
        
        $$ \bigg < \dfrac{\partial L}{\partial \mathbf{Z}} , \dfrac{\partial \mathbf{Z}}{\partial y _{11}} \bigg  > _{\mathbf{F}} = \Bigg < \begin{pmatrix} \dfrac{\partial L}{\partial z_{11}}& \dfrac{\partial L}{\partial z_{12}}& \dots& \dfrac{\partial L}{\partial z_{1m}}\\ \dfrac{\partial L}{\partial z_{21}}& \dfrac{\partial L}{\partial z_{22}}& \dots& \dfrac{\partial L}{\partial z_{2m}}\\ \vdots & \vdots & \ddots & \vdots \\ \dfrac{\partial L}{\partial z_{n1}}& \dfrac{\partial L}{\partial z_{n2}}& \dots& \dfrac{\partial L}{\partial z_{nm}}\\ \end{pmatrix}, \begin{pmatrix} 1& 0& \dots& 0 \\ 0& 0& \dots& 0\\ \vdots & \vdots & \ddots & \vdots \\ 0& 0& \dots& 0\\ \end{pmatrix} \Bigg > _{\mathbf{F}} $$

        $$ = \dfrac{\partial L}{\partial z_{11}} $$

        이다. 즉, $\displaystyle \dfrac{\partial L}{\partial y _{11}} = \bigg < \dfrac{\partial L}{\partial \mathbf{Z}} , \dfrac{\partial \mathbf{Z}}{\partial y _{11}} \bigg  > _{\mathbf{F}}= \dfrac{\partial L}{\partial z _{11}}$ 이다. 마찬가지로 

        $$\displaystyle \dfrac{\partial L}{\partial y _{ij}} = \bigg < \dfrac{\partial L}{\partial \mathbf{Z}} , \dfrac{\partial \mathbf{Z}}{\partial y _{ij}} \bigg  > _{\mathbf{F}}= \dfrac{\partial L}{\partial z _{ij}}$$

        이다. 그러므로 $L$ 에 대한 $\mathbf{Y}$ 의 미분은 $n \times m$ 행렬 

        $$ \therefore \dfrac{\partial L}{\partial \mathbf{Y}} = \begin{pmatrix} \dfrac{\partial L}{\partial z _{11}}& \dfrac{\partial L}{\partial z _{12}}& \dots& \dfrac{\partial L}{\partial z _{1m}}\\ \dfrac{\partial L}{\partial z _{21}}& \dfrac{\partial L}{\partial z _{22}}& \dots& \dfrac{\partial L}{\partial z _{2m}}\\ \vdots & \vdots & \ddots & \vdots \\ \dfrac{\partial L}{\partial z _{n1}}& \dfrac{\partial L}{\partial z _{n2}}& \dots& \dfrac{\partial L}{\partial z _{nm}}\\ \end{pmatrix} = \dfrac{\partial L}{\partial \mathbf{Z}} $$ 

        이다. ■

!!! tldr ""

    CrossEntropyError 레이어 역전파 : 신경망의 출력벡터 $\mathbf{y} \in \mathbb{R} ^{k}$, 원-핫 인코딩된 정답 레이블 $\mathbf{t} \in \mathbb{R} ^{k}$ 에 대한 손실함수
    
    $$ E(\mathbf{t}, \mathbf{y}) = - \sum_{i}^{} t _{i}\ln_{} y _{i} $$
    
    CrossEntropyError 함수의 역전파는 상위 노드에서 역전파된 미분에 
    
    $$ - \dfrac{t_i}{y_i} $$
    
    를 곱하여 하위 노드로 역전파한다.

- 신경망의 출력벡터 $\mathbf{y}$ 는 CrossEntropyError 레이어의 입력 벡터임을 주의하자.

- CrossEntropyError 함수는 출력벡터 $\mathbf{y} \in \mathbb{R} ^{k}$, 정답벡터 $\mathbf{t} \in \mathbb{R} ^{k}$, $i$ 번째 뉴런 에 대하여 

    $$ E(\mathbf{t, y}) = - \sum_{i}^{}t_i \ln y_i $$

    이다. 이것의 미분은 

    $$ \dfrac{\partial E(\mathbf{t},\mathbf{o})}{\partial y_i} = \boxed{- \dfrac{t_i}{y_i}} $$

    이다. ■ 

- 그러므로 만약 정답 레이블이 아니라면 $t_i = 0$ 이므로 상위 노드에서 역전파된 미분에 $0$ 을 곱하여 하위 노드로 전달한다. 이는 가중치 조정이 $0$ 이 된다는 것이다.

- 이것은 곱셈 노드, 덧셈 노드, 로그 노드의 국소적 역전파로 구성될 수 있다.

!!! tldr ""

    Softmax 레이어 역전파 : $n \in \mathbb{N}$ 개의 입력 $a_1, \dots, a_n$ 에 대한 $k$ 번째 입력 $a_k$ 에 대하여 $k$ 번째 출력 $y_k$ 
    
    $$ y_k = \dfrac{\exp (a_k)}{\displaystyle \sum_{i=1}^{n}\exp (a_i)} $$
    
    을 갖는 Softmax 함수의 역전파는 상위 노드에서 역전파된 미분에
    
    $$ y_k(1 - y_k) $$
    
    를 곱하여 하위 노드로 전달한다.
    
    > $-y_ky_j$ 라는 미분 결과에 대해서도 처리할 수 있어야 하는데, 여러개의 역전파 값에 대하여 일반적인 역전파 정의를 다시 해야 할 듯.

- 증명 

    Softmax 함수는 $n \in \mathbb{N}$ 개의 입력 $a_1, \dots, a_n$ 에 대한 $k$ 번째 입력 $a_k$ 에 대하여 $k$ 번째 출력 $y_k$ 

    $$ y_k = \dfrac{\text{exp}( a_k)}{\displaystyle \sum_{i=1}^{n}\text{exp}(a_i)} $$

    을 갖는다. 이것의 미분은 

    $$ \dfrac{\partial y_k}{\partial a_j} = \dfrac{\partial }{\partial a_j}\bigg (\dfrac{\text{exp}( a_k)}{\sum_{i=1}^{n}\text{exp}(a_i)} \bigg ) $$

    이다. $k = j$ 일 경우 $\dfrac{\partial \text{exp}( a_k)}{\partial a_j} = \text{exp}( a_k)$ 이므로 분수함수의 미분에 의하여 

    $$ = \dfrac{\text{exp}( a_k)\sum_{i=1}^{n}\text{exp}(a_i) - \text{exp}( a_j)\text{exp}( a_k)}{\bigg (\displaystyle \sum_{i=1}^{n}\text{exp}(a_i)\bigg ) ^{2}} = \dfrac{\text{exp}( a_k)(\sum_{i=1}^{n}\text{exp}(a_i) - \text{exp}( a_j))}{\bigg (\displaystyle \sum_{i=1}^{n}\text{exp}(a_i)\bigg ) ^{2}} $$

    $$ = \dfrac{\text{exp}( a_k)}{\displaystyle \sum_{i=1}^{n}\text{exp}(a_i)}\times \dfrac{\displaystyle \sum_{i=1}^{n}\text{exp}(a_i) - \text{exp}( a_j)}{\displaystyle \sum_{i=1}^{n}\text{exp}(a_i)} = y_k(1 - y_j)= \boxed{y_k(1 - y_k)}  $$

    이다. ▲ 
    
    $k \neq j$ 일 경우 $\dfrac{\partial \text{exp}( a_k)}{\partial a_j} = 0$ 이므로 

    $$ \dfrac{\partial y_k}{\partial a_j} = \dfrac{0 - \text{exp}( a_j)\text{exp}( a_k)}{\bigg (\displaystyle \sum_{i=1}^{n}\text{exp}(a_i)\bigg ) ^{2}} = -\dfrac{\text{exp}( a_k)}{\displaystyle \sum_{i=1}^{n}\text{exp}(a_i)}\dfrac{\text{exp}( a_j)}{\displaystyle \sum_{i=1}^{n}\text{exp}(a_i)} = \boxed{-y_ky_j}  $$

    이다. ▲ 

    그러므로 Softmax 함수의 미분은 

    $$ \therefore \dfrac{\partial y_k}{\partial a_j} = \begin{cases} y_k(1 - y_k) &(j=k)\\ -y_ky_j &(j \neq k)\\ \end{cases} $$

    이다. ■ 

    또는 크로네커 델타 $\delta _{ij} = \begin{cases} 1 &(i=j)\\ 0 &(i\neq j)\\ \end{cases}$  를 사용하여 

    $$ \therefore \dfrac{\partial y_k}{\partial a_j} = y_k(\delta _{kj} - y_j) $$

    로 정의할 수도 있다.

!!! tldr ""

    Softmax-with-CrossEntropyError-Loss 레이어 역전파 : Softmax 함수로 입력을 정규화하고 CrossEntropyError 로 손실값까지 구해주는 레이어의 역전파는 상위노드에서 전달된 미분에 
    
    $$ y_k - t_k $$
    
    를 곱하여 하위노드로 전달한다.

- 출력층에서 사용하는 Softmax 레이어는 출력을 정규화해준다.

    신경망이 하는 일이란 학습과 추론인데, 추론할 때는 출력이 정규화되지 않아도 된다. 왜냐하면 그냥 가장 높은 값만 알면 되기 때문이다. 

    반면 학습할 때에는 Softmax 레이어로 출력을 정규화해주어야 한다.

    - 왜??

- 증명 

    Softmax 함수는 $n \in \mathbb{N}$ 개의 입력 $a_1, \dots, a_n$ 에 대한 $k$ 번째 입력 $a_k$ 에 대하여 $k$ 번째 출력 $y_k$ 

    $$ y_k = \dfrac{\exp (a_k)}{\displaystyle \sum_{i=1}^{n} \exp (a_i)} $$

    을 갖는다. 이 $y_k$ 는 정답 벡터 $\mathbf{t} \in \mathbb{R} ^{n}$ 에 대하여 CrossEntropyError 함수 

    $$ L = E(\mathbf{t, y}) := - \sum_{i=1}^{n}t_i \ln y_i $$

    로 전달되고 최종적으로 손실값 $L$ 이 계산된다. 이 $L$ 에 대한 입력 벡터 $\mathbf{a} \in \mathbb{R} ^{n}$ 의 $k$ 번째 입력 $a_k$ 의 미분은

    $$ \dfrac{\partial L}{\partial a_k} = - \sum_{i=1}^{n}t_i \dfrac{\partial \ln y_i}{\partial a_k}= - \sum_{i=1}^{n}t_i \dfrac{\partial \ln y_i}{\partial y_i}\dfrac{\partial y_i}{\partial a_k} = - \sum_{i=1}^{n}t_i \dfrac{1}{y_i}\dfrac{\partial y_i}{\partial a_k} $$

    $$ = -t_k(1-y_k)- \sum_{i \in \{1,\dots,(k-1),(k+1),\dots,n\}}^{}\dfrac{t_i}{y_i}(-y_iy_k) $$

    $$ = -t_k+t_ky_k+ \sum_{i \in \{1,\dots,(k-1),(k+1),\dots,n\}}^{}t_iy_k $$

    $$ = -t_k+y_k \bigg (t_k+ \sum_{i \in \{1,\dots,(k-1),(k+1),\dots,n\}}^{}t_i \bigg ) = -t_k+y_k \sum_{i =  1}^{n}t_i $$

    인데, 정답 벡터 $\mathbf{t} \in \mathbb{R} ^{n}$ 은 원-핫 인코딩되어 있으므로 $\sum_{k=1}^{n}t_k = 1$ 이다. 따라서

    $$ = -t_k+y_k  = \boxed{y_k - t_k} $$

    이다. ■ 

- 코드 구현 

    ```python
    class SoftmaxCrossEntropyError:
        def __init__(self):
            self.loss = None 
            self.y = None     # softmax 출력
            self.t = None     # 정답 레이블(원-핫 벡터)
        
        def forward(self, x, t):
            self.t = t
            self.y = softmax(x)
            slef.loss = cross_entropy_error(self.y, self.t)
            return self.loss
        
        def backward(self, dout = 1):
            batch_size = self.t.shape[0]
            if self.t.size == self.y.size: # 정답 레이블이 원-핫 벡터일 때
                dx = (self.y - self.t) / batch_size
            else:
                dx = self.y.copy()
                dx[np.arange(batch_size), self.t] -= 1 # 이해 안됨
                dx = dx / batch_size
            return dx
    ```

---

# affine layer 메모

  - $\dfrac{\partial L}{\partial \mathbf{Y}}$ 를 전달하는 이유는 최종적으로 $\dfrac{\partial L}{\partial \mathbf{X}}, \dfrac{\partial L}{\partial \mathbf{W}}$  를 계산하기 위함이다.
  
  - 마찬가지로 $L$ 이 스칼라므로 $\dfrac{\partial L}{\partial \mathbf{X}}$ 의 형상은 $\mathbf{X}$ 와 동일하게 $n \times d$ 이고, $\dfrac{\partial L}{\partial \mathbf{W}}$ 의 형상은 $\mathbf{W}$ 와 동일하게 $d \times m$ 이다.

  - 이미 잘 알고 있듯 $\dfrac{\partial \mathbf{Y}}{\partial \mathbf{X}}, \dfrac{\partial \mathbf{Y}}{\partial \mathbf{W}}$ 는 야코비안 행렬이다. 그런데 이것을 명시적으로 나타내기란 매우 어렵다. 통상적인 신경망에서 $n=64,m=d=4096$ 으로 둔다면 $\mathbf{X}$ 는 $n \times d =64 \times 4096$ 행렬이 되고, $\mathbf{Y}$ 는 $n \times m = 64 \times 4096$ 행렬이 되므로 $\dfrac{\partial \mathbf{Y}}{\partial  \mathbf{X}}$ 은 $64 \cdot 4096 \cdot 64 \cdot 4096$ 의 스칼라 값을 갖기 때문이다.

  - 만약 벡터 $\mathbf{v} \in \mathbb{R} ^{n}, \mathbf{w} \in \mathbb{R} ^{m}$ 에 대하여 $\mathbf{v}$ 가 $\mathbf{w}$ 에 종속되어 있다면 $\mathbf{v}$ 에 대한 $\mathbf{w}$ 의 미분은 $m \times n$ 야코비안 행렬이 된다.

      마찬가지로 스칼라($1 \times 1$ 행렬) $a$ 와 $n \times m$ 행렬 $\mathbf{A}$ 에 대하여 $\mathbf{A}$ 가 스칼라 $a$ 의 독립변수라면 $a$ 에 대한 $\mathbf{A}$ 의 미분은 $n \times m$ 야코비안 행렬이 된다.

      마찬가지로 $n \times m$ 행렬 $A$ 와 $s \times t$ 행렬 $B$ 가 서로 종속일 때 $A$ 에 대한 $B$ 의 미분으로 얻어진 야코비안 행렬의 원소 개수는 $n \times m \times s \times t$ 이다.

      - 증명 

        행렬 $A$ 의 $(i, j)$ 원소 $a _{ij}$ 를 행렬 $B$ 에 대하여 미분하면 야코비안 행렬

        $$ \dfrac{\partial a _{ij}}{\partial B} = \begin{pmatrix} \dfrac{\partial a _{ij}}{\partial b _{11}} & \dfrac{\partial a _{ij}}{\partial b _{12}} & \dots& \dfrac{\partial a _{ij}}{\partial b _{1t}}  \\ \dfrac{\partial a _{ij}}{\partial b _{21}} & \dfrac{\partial a _{ij}}{\partial b _{22}} & \dots& \dfrac{\partial a _{ij}}{\partial b _{2t}}  \\ \vdots & \vdots & \ddots & \vdots \\ \dfrac{\partial a _{ij}}{\partial b _{s1}} & \dfrac{\partial a _{ij}}{\partial b _{s2}} & \dots& \dfrac{\partial a _{ij}}{\partial b _{st}}  \\ \end{pmatrix} $$ 

        을 얻는다. 그러므로 행렬 $A$ 의 모든 원소에 대하여 $B$ 를 미분하면 야코비안 행렬을 부분행렬로 갖는 행렬 

        $$ \dfrac{\partial A}{\partial B} = \begin{pmatrix} \dfrac{\partial a _{11}}{\partial B}& \dfrac{\partial a _{12}}{\partial B}& \dots& \dfrac{\partial a _{1m}}{\partial B} \\ \dfrac{\partial a _{21}}{\partial B}& \dfrac{\partial a _{22}}{\partial B}& \dots& \dfrac{\partial a _{2m}}{\partial B} \\ \vdots & \vdots & \ddots & \vdots \\ \dfrac{\partial a _{n1}}{\partial B}& \dfrac{\partial a _{n2}}{\partial B}& \dots& \dfrac{\partial a _{nm}}{\partial B} \\ \end{pmatrix} $$

        이다. $s \times t$ 행렬이 $n \times m$ 행렬의 원소로 있으므로 모든 원소의 개수는 $(s \times t) n \times m$ 이다.

  - 하지만 다행히도 야코비안 행렬 $\dfrac{\partial \mathbf{Y}}{\partial \mathbf{X}}$ 를 명시적으로 표현하지 않고, 심지어 계산하지도 않고 식 $\dfrac{\partial \mathbf{Y}}{\partial \mathbf{X}}$ 을 다룰 수 있다. 

  ---

  에 대한 $1 \times m$ 행렬 $\mathbf{Y} = \mathbf{XW+B}$ 

  $$ \mathbf{Y} = \mathbf{XW}+\mathbf{B} = \begin{pmatrix} \displaystyle \sum_{k=1}^{n}x_kw _{k1} + b_1 & \displaystyle \sum_{k=1}^{n}x_kw _{k2} + b_2 & \dots & \displaystyle \sum_{k=1}^{n}x_kw _{km} + b_m \\ \end{pmatrix} $$

  이 존재한다. 스칼라 $L = Y \Psi$ 가 존재한다. ▲ 

  그러므로 $\mathbf{Y}$ 의 $i$번째 원소 $y_i = \displaystyle \sum_{k=1}^{n}x_kw _{ki}+b_i$ 에 대한 $x_j$ 의 미분은

  $$ \dfrac{\partial  y_i}{\partial x_j} = w _{ji} $$

  이다. 그렇다면 $\mathbf{Y}$ 에 대한 $\mathbf{X}$ 의 미분은 야코비행렬 

  $$ \dfrac{\partial \mathbf{Y}}{\partial \mathbf{X}} = \begin{pmatrix} \dfrac{\partial y_1}{\partial x_1} & \dfrac{\partial y_1}{\partial x_2} & \dots& \dfrac{\partial y_1}{\partial x_n} \\ \dfrac{\partial y_2}{\partial x_1} & \dfrac{\partial y_2}{\partial x_2} & \dots& \dfrac{\partial y_2}{\partial x_n} \\ \vdots & \vdots & \ddots & \vdots \\ \dfrac{\partial y_m}{\partial x_1} & \dfrac{\partial y_m}{\partial x_2} & \dots& \dfrac{\partial y_m}{\partial x_n} \\ \end{pmatrix} = \begin{pmatrix} w _{11} & w _{21}& \dots & w _{n1} \\ w _{12} & w _{22}& \dots & w _{n2} \\ \vdots & \vdots & \ddots & \vdots \\ w _{1m} & w _{2m}& \dots & w _{nm} \\ \end{pmatrix} = \mathbf{W} ^{\intercal } $$

  이다. ▲ 

- 신경망 순전파 때 사용되는 행렬곱을 기하학에서 어파인 변환(affine transformation) 이라고 한다.

---


  정리 6 (매개변수를 갖는 행렬방정식의 미분) "벡터 $\mathbf{y} \in \mathbb{R} ^{m}$($m \times 1$ 행렬), $\mathbf{x} \in \mathbb{R} ^{n}$($n \times 1$ 행렬) 와 $m \times n$ 행렬 $\mathbf{A}$ 이 존재할때 $\mathbf{x}$ 가 벡터 $\mathbf{z}$ 에 대한 함수라면 행렬방정식 $\mathbf{y} = \mathbf{Ax}$ 의 미분은 $\dfrac{\partial \mathbf{y}}{\partial \mathbf{z}} = \dfrac{\partial \mathbf{y}}{\partial \mathbf{x}}\dfrac{\partial \mathbf{x}}{\partial \mathbf{z}} = \mathbf{A}\dfrac{\partial \mathbf{x}}{\partial \mathbf{z}}$  이다." 에 의하여

  $1 \times 1$ 행렬 $L$ 

  $$ \dfrac{\partial L}{\partial \mathbf{X}} = 
  $$

  먼저 
  
  먼저 $L$ 을 $\mathbf{X}$ 의 $(i, j)$ 원소로 미분하면 $L = l(\mathbf{Y}) = l(\mathbf{XW})$ 이므로 매개변수 $\mathbf{Y}$ 에 대한 합성함수 미분, 즉 

  $$ \dfrac{\partial L}{\partial x _{ij}} = 
  $$

  $\dfrac{\partial L}{\partial \mathbf{X}} = \begin{pmatrix} \dfrac{\partial L}{\partial x _{11}}& \dfrac{\partial L}{\partial x _{12}}& \dots& \dfrac{\partial L}{\partial x _{1d}} \\ \dfrac{\partial L}{\partial x _{21}}& \dfrac{\partial L}{\partial x _{22}}& \dots& \dfrac{\partial L}{\partial x _{2d}}\\ \vdots & \vdots & \ddots & \vdots \\ \dfrac{\partial L}{\partial x _{n1}}& \dfrac{\partial L}{\partial x _{n2}}& \dots& \dfrac{\partial L}{\partial x _{nd}}\\ \end{pmatrix}$ 이다.

