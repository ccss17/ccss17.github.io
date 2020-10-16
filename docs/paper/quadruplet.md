# Quadruplet 사전지식

# (Translation) Beyond triplet loss : One shot learning experiments with quadruplet loss (by Eric Craeymeersch)

*References*: 

:   https://medium.com/@crimy/beyond-triplet-loss-one-shot-learning-experiments-with-quadruplet-loss-16671ed51290

## The "QuadLoss" paper

이 논문은 **FaceNet** 이후 2년 후에 나온 논문으로써 서로 다른 감시 카메라가 한 사람을 추적하는 관점에서의 재식별(re-identification) 을 연구한다. 가령 카메라 1 로 어떤 사람을 추적하다가, 카메라 2 가 같은 사람을 찍었을 때 똑같은 사람인지 어떻게 인식하게 할 것인가? 이 문제는 두 카메라가 다른 포즈, 다른 각도, 다른 명조로 동일 인물을 촬영하므로 생각보다 어려운 문제다.

이 논문은 4 파트로 요약된다.

- triplet loss 함수 개선

- Learned metric

- Mining strategy

- Extensive loss functions study

### triplet loss 함수 개선

원래 triplet loss 함수는 다음과 같았다. $[z] _{+} = \max (z, 0)$ 와 입력 이미지 $f(x_i), f(x_j), f(x_k)$ 와 하이퍼파라미터 $\alpha _{trp}$ 에 대하여

$$ L _{trp} = \sum_{i,j,k}^{N} [\|f(x_i) - f(x_j)\| ^{2} _{2} - \|f(x_i) - f(x_k)\|^{2}_{2} + \alpha _{trp}]_{+} \tag{1} $$

이때 $x_i$ 가 anchor, $x_j$ 가 positive, $x_k$ 가 negative 를 뜻한다. 하지만 이 논문에서는 anchor 라는 단어를 사용하지 않고 reference 혹은 ref 를 사용한다. 논문에서는 이 함수를 다음과 같이 개선한다. learned metric 을 사용하는 $f(x_i) - f(x_j)$ 인 $g(x_i, x_j)$ 에 대하여 

![image](https://user-images.githubusercontent.com/16812446/96069879-14d38d00-0eda-11eb-913b-b650cd8fd981.png)

이 손실함수는 triplet loss 함수와 동일하게 Anchor-Positive 거리와 Anchor-Negative 거리의 차이값을 포함하지만, 단지 Anchor-Positive 거리와 Negative-AnotherNegative 거리의 차이값도 계산하고 있다. 이에 따라 새로운 하이퍼파라미터 $\alpha _{2}$ 가 추가되었다. AnotherNegative 란 기존의 negative 와 다른 클래스에서 가져온 negative 샘플이다.

그러므로 이것을 계산하기 위하여 Anchor(A), Positive(P), Negative(N), Negative2(N2) 가 필요하다. 이제 Anchor 와 Positive 의 거리를 AP 라고 하고 Negative 와 Negative2 의 거리를 NN 이라고 하자. 그러면 triplet loss 와 quadruplet loss 를 단순하게 다음과 같이 쓸 수 있다.

:   Triplet loss = AP - AN + alpha1

:   Quadruplet loss = AP - AN + alpha1 + AP - NN + alpha2

이 논문은 위 수식의 항들을 편의상 다음과 같이 부른다.

:   "AP - AN + alpha1" 를 "strong" push (alpha1 = 1) 라고 부른다.

:   "AP - NN + alpha2" 를 "weak" push (alpha1 < 0.5) 라고 부른다.

### Learned metric

원래의 손실함수에서는 거리를 계산할 때 L2 거리

$$ \text{L2dist} (a, b) = (a - b) ^{2} $$

로 계산했다. 하지만 이 논문에서는 L2 거리를 neural network 로 대체했다. learned metrics 에 대한 자료는 매우 많으므로 생략하겠다.

### Training architecture

![](https://miro.medium.com/max/1313/1*9QVFD-io7Ods-o9CFL9gMw.png)

:   논문에서 설명된 학습 구조. 분홍생 파트가 FaceNet 구조에서 새롭게 추가된 파트이다.

학습 구조는 세 파트로 진행된다.

- 첫번째 파트는 4가지 이미지를 받아서 동일한 conv 계층을 통해 벡터로 변환한다. 

- 그런 다음 벡터를 AP(ref-pos), AN(ref-neg), NN(neg-neg2) 로 그룹화한다. 

- 그리고 기존에 이 페어의 L2 거리를 계산하는 것과 다르게 learned metric network 로 보낸다. 그리고 최종적으로 binary softmax 로 보내서 같은 사람인지, 다른 사람인지 두 가지 값만을 출력하게 한다. 후자의 값만이 거리 표시기 또는 비유사도 표시기로 작동한다.

- 마지막으로 3 개의 softmax 로 손실 함수를 계산한다.

### Mining strategy

마이닝은 말 그대로 학습할 샘플을 선택하는 것이다. 우리는 샘플이 얼마나 hard 하냐는 것을 샘플이 생성하는 손실값이 얼마나 되느냐로 말할 것이다.

- easy 샘플이란 손실값이 작거나 없는 것이다. 가령 anchor 와 매우 가까운 positive 이거나 anchor 와 매우 먼 negative 가 easy sample 이라고 할 수 있다.

- hard 샘플이란 손실값을 매우 크게 배출하는 샘플이다. 가령 anchor 와 매우 먼 positive 이거나 anchor 와 매우 가까운 negative 가 easy sample 이라고 할 수 있다.

- 이 중간에, 마진을 뜻하는 alpha1 과 alpha2 의 경계에 있는 semi-hard 샘플이 존재한다.

easy 샘플을 선택해서 학습하는 건 전체 시스템에 별 도움이 안된다. **따라서 마이닝이란 hard 샘플 혹은 semi-hard 샘플을 빠르게 찾아서 시스템의 학습이 빠르게 진행될 수 있도록 하는 것이다.** 

이 논문은 배치에서 선택될 hard 샘플을 가려내는 dynamic threshold 를 기반으로 하는 aggressive mining strategy 를 소개한다. 이것에 관해서 여기에서는 자세히 설명하지 않을 것이다.

### Extensive loss functions study

그러고나서 이 논문은 다른 종류의 손실함수의 차이점에 대하여 분석한다. 만약 이 주제에 대하여 더 알고 싶고, 아카데믹한 설명을 이해하는데에 거부감이 없다면 이 파트도 읽어보길 바란다.

## Our Challenge

이 포스트에서 우리는 두 이미지가 서로 기호를 뜻하는지 같은 기호를 뜻하는지 One shot learning system 으로 판별해볼 것이다. OMNIGLOT 데이터셋을 사용할 건데, 이 데이터셋은 50 개의 다른 알파벳에서 온 1623 개의 손글씨 문자를 갖고 있다. MNIST 가 10 개의 클래스에 클래스 당 6000 개의 샘플을 갖고 있는 것과 달리 우리는 1623 클래스와 클래스 당 20 개의 샘플을 갖고 있는 이 데이터셋을 사용할 것이다.

![](https://miro.medium.com/max/1313/1*FhHGYU4S5xnW5s5rl3JcEA.jpeg)

:   omnigplot 데이터셋 

이 데이터셋을 964 개의 훈련용 클래스와 659 개의 시험용 클래스로 분할할 수 있다. 이는 시험용 데이터셋에 샘플들만 있는 것이 아니라 훈련 때 사용되지 않은 전혀 새로운 클래스도 포함되어 있다는 것이다. 이것이 MNIST 와 가장 다른 차이점이다. 

우리는 기존의 triplet loss 를 사용해서 학습을 해보고, quadruplet loss 사용해서 학습을 해볼 것이다. 그리고 이 두 시스템을 다음과 같이 최대한 동일한 환경으로 학습시켜볼 것이다. 

- 동일한 데이터를 동일한 시간으로 동일한 에폭으로 동일한 mining strategy 로 학습시킨다.

- 인코더(사진을 벡터로 변환하는 계층) 파트를 동일한 neural network 구조를 사용할 것이다. 두 인코더가 완전히 똑같은 파라미터와 동일한 크기(여기에서는 20)를 갖도록 할 것이다.

하지만 quadruplet 시스템에는 다음의 기능을 추가하게 된다.

- quadruplet loss 함수에는 dist(A, P)-dist(N, N2) 가 더해진다.

- L2 거리 대신 learned metric 을 사용한다. 이것은 모델에 또 다른 neural network 를 더함으로써 이루어진다.

즉, triplet loss 시스템(3x) 과 quadruplet loss + learned metric system(4x) 을 비교해보는 것이다.

### 데이터셋 준비

먼저 OMNIGLOT 을 다운로드 받아서 그레이스케일로 변환하고, $0-255$ 의 값을 $0-1$ 로 정규화한다. 그러고나서 데이터셋을 다음의 자료구조로 저장한다.

- X 에 모든 이미지를 저장한다. Y 에 true labels (class 번호들) 을 저장한다. 

- dataset_train 이라는 자료구조를 정의한다. 가령 dataset_train[0] 에는 모든 class 0 을 갖는 이미지 (?, 105, 105, 1) 들이 저장되어 있다. 이렇게 하면 나중에 특정 클래스에 대한 샘플링(quadruplet (A, P, N, N2) 를 만드는 것)을 할 때 편하다.

### Mining Strategy

4x 에 대한 mining strategy 는 단순하게 할 것이다.

- 100 개의 quadruplet 을 한 배치로 만든다.

- 16 개의 hardest quadruplet 을 택한다. 

- 16 개의 랜덤 quadruplet 을 택하여 32 개의 샘플을 만든다.

![](https://miro.medium.com/max/1313/1*_Ar5aeP-dPgXwNoWznddeQ.png)

:   hard quadruplet 예시

3x 는 triplet 을 사용하기 때문에 다음과 같다.

- 4x 에서 준비한 100 개의 quadruplet 에서 APN 를 구성하기 위한 첫 3 개의 이미지들을 추출하여 100 개의 triplet 을 한 배치로 만든다. 

- 16 개의 hardest triplet 을 선택한다. 

- 16 개의 무작위 triplet 을 선택하여 32 개의 샘플로 이루어진 배치를 만든다. 

![](https://miro.medium.com/max/1313/1*w15NaxvjlIx81hdtqIFkZw.png)

:   hard triplet 예시 

## Keras 로 모델 만들기

### The encoder

논문에서는 pretrained Resnet 을 사용했지만, 여기에서는 그것이 유용하지 않으니 (conv/pool) * 3 + fc 조합을 사용하겠다. 마지막 계층은 embedding 값이 full range 를 갖도록 하기 위하여 어떤 활성화함수도 가지면 안된다.

```python
def build_network(input_shape, embeddingsize):
    '''
    Define the neural network to learn image similarity
    Input : 
            input_shape : shape of input images
            embeddingsize : vectorsize used to encode our picture   
    '''
    # Convolutional Neural Network
    network = Sequential()
    network.add(Conv2D(128, (7,7), activation='relu',padding='same',
                     input_shape=input_shape,
                     kernel_initializer='he_uniform',
                     kernel_regularizer=l2(2e-4)))
    network.add(MaxPooling2D())
    network.add(Conv2D(128, (5,5), activation='relu', kernel_initializer='he_uniform',padding='same',
                     kernel_regularizer=l2(2e-4)))
    network.add(MaxPooling2D())
    network.add(Conv2D(64, (5,5), activation='relu', kernel_initializer='he_uniform',padding='same',
                     kernel_regularizer=l2(2e-4)))
    network.add(Flatten())
    network.add(Dense(2048, activation='relu',
                   kernel_regularizer=l2(1e-3),
                   kernel_initializer='he_uniform'))
    network.add(Dense(embeddingsize, activation=None,
                   kernel_regularizer=l2(1e-3),
                   kernel_initializer='he_uniform'))
    #Force the encoding to live on the d-dimentional hypershpere
    network.add(Lambda(lambda x: K.l2_normalize(x,axis=-1)))
    return network
```

### The learned metric

4x 시스템을 위해서 두 embedding 을 받아서 거리를 출력해주는 neural network 를 만들어야 한다. 우리는 3 개의 fc 와 논문에서와 같이 binary softmax 를 사용할 것이다. 우리는 두 embedding 이 유사하지 않은 확률을 뜻하는 거리를 표현하는 숫자 하나만 필요하기 때문에 softmax 의 출력 하나만을 취할 것이다. 

이때 두 embedding 을 연결하여 첫번째 계층에 입력할 것이다.

```python
def build_metric_network(single_embedding_shape):
    '''
    Define the neural network to learn the metric
    Input : 
            single_embedding_shape : shape of input embeddings or feature map. Must be an array
    '''
    #compute shape for input
    input_shape = single_embedding_shape
    #the two input embeddings will be concatenated    
    input_shape[0] = input_shape[0]*2
     # Neural Network
    network = Sequential(name="learned_metric")
    network.add(Dense(10, activation='relu',
                   input_shape=input_shape, 
                   kernel_regularizer=l2(1e-3),
                   kernel_initializer='he_uniform'))
    network.add(Dense(10, activation='relu',                   
                   kernel_regularizer=l2(1e-3),
                   kernel_initializer='he_uniform'))  
    network.add(Dense(10, activation='relu',                   
                   kernel_regularizer=l2(1e-3),
                   kernel_initializer='he_uniform'))
    #Last layer : binary softmax
    network.add(Dense(2, activation='softmax'))
    #Select only one output value from the softmax
    network.add(Lambda(lambda x: x[:,0]))
    return network
```

### Loss functions

3x 시스템을 위해서 A, P, N 을 입력받아서 triplet loss 함수 정의대로 L2 거리를 계산하고 모두 더하는 클래스를 정의해준다. 

```python
class TripletLossLayer(Layer):
    def __init__(self, alpha, **kwargs):
        self.alpha = alpha
        super(TripletLossLayer, self).__init__(**kwargs)
    
    def triplet_loss(self, inputs):
        anchor, positive, negative = inputs
        p_dist = K.sum(K.square(anchor-positive), axis=-1)
        n_dist = K.sum(K.square(anchor-negative), axis=-1)
        return K.sum(K.maximum(p_dist - n_dist + self.alpha, 0), axis=0)
    
    def call(self, inputs):
        loss = self.triplet_loss(inputs)
        self.add_loss(loss)
        return loss
```

4x 시스템을 위해서 learned metric 으로 이미 학습된 AP, AN, NN 을 입력받아서 마찬가지로 quadruplet loss 함수 정의대로 계산해준다.

```python
class QuadrupletLossLayer(Layer):
    def __init__(self, alpha, beta, **kwargs):
        self.alpha = alpha
        self.beta = beta
        self.debugeric = 1
        super(QuadrupletLossLayer, self).__init__(**kwargs)
    
    def quadruplet_loss(self, inputs):
        ap_dist,an_dist,nn_dist = inputs
        ap_dist2 = K.square(ap_dist)
        an_dist2 = K.square(an_dist)
        nn_dist2 = K.square(nn_dist)
        return K.sum(K.maximum(ap_dist2 - an_dist2 + self.alpha, 0), axis=0) + K.sum(K.maximum(ap_dist2 - nn_dist2 + self.beta, 0), axis=0)
    
    def call(self, inputs):
        loss = self.quadruplet_loss(inputs)
        self.add_loss(loss)
        return loss
```

### Assembling our Keras models

이제 3x 시스템 전체를 만들 수 있다.

```python
def build_model3(input_shape, network, margin=0.2):
    '''
    Define the Keras Model for training 
        Input : 
            input_shape : shape of input images
            network : Neural network to train outputing embeddings
            margin : minimal distance between Anchor-Positive and Anchor-Negative for the lossfunction (alpha)
    
    '''
     # Define the tensors for the three input images
    anchor_input = Input(input_shape, name="anchor_input")
    positive_input = Input(input_shape, name="positive_input")
    negative_input = Input(input_shape, name="negative_input") 
    # Generate the encodings (feature vectors) for the three images
    encoded_a = network(anchor_input)
    encoded_p = network(positive_input)
    encoded_n = network(negative_input)
    #TripletLoss Layer
    loss_layer = TripletLossLayer(alpha=margin,name='3xLoss')([encoded_a,encoded_p,encoded_n])
    # Connect the inputs with the outputs
    network_train = Model(inputs=[anchor_input,positive_input,negative_input],outputs=loss_layer)
    # return the model
    return network_train
```

![](https://miro.medium.com/max/1313/1*VpRE32TwrTM3nfGAuXuoBw.png)

또 4x 전체 시스템도 AP, AN, NN 을 metric network 로 계산하고 QuadrupletLossLayer 로 입력하는 방식으로 만들 수 있다.

```python
def build_model4(input_shape, network, metricnetwork,margin=0.1, margin2=0.01):
    '''
    Define the Keras Model for training 
        Input : 
            input_shape : shape of input images
            network : Neural network to train outputing embeddings
            metricnetwork : Neural network to train the learned metric
            margin : minimal distance between Anchor-Positive and Anchor-Negative for the lossfunction (alpha1)
            margin2 : minimal distance between Anchor-Positive and Negative-Negative2 for the lossfunction (alpha2)
    
    '''
     # Define the tensors for the four input images
    anchor_input = Input(input_shape, name="anchor_input")
    positive_input = Input(input_shape, name="positive_input")
    negative_input = Input(input_shape, name="negative_input") 
    negative2_input = Input(input_shape, name="negative2_input")
    # Generate the encodings (feature vectors) for the four images
    encoded_a = network(anchor_input)
    encoded_p = network(positive_input)
    encoded_n = network(negative_input)
    encoded_n2 = network(negative2_input)
    #compute the concatenated pairs
    encoded_ap = Concatenate(axis=-1,name="Anchor-Positive")([encoded_a,encoded_p])
    encoded_an = Concatenate(axis=-1,name="Anchor-Negative")([encoded_a,encoded_n])
    encoded_nn = Concatenate(axis=-1,name="Negative-Negative2")([encoded_n,encoded_n2])
    #compute the distances AP, AN, NN
    ap_dist = metricnetwork(encoded_ap)
    an_dist = metricnetwork(encoded_an)
    nn_dist = metricnetwork(encoded_nn)
    #QuadrupletLoss Layer
    loss_layer = QuadrupletLossLayer(alpha=margin,beta=margin2,name='4xLoss')([ap_dist,an_dist,nn_dist])
    # Connect the inputs with the outputs
    network_train = Model(inputs=[anchor_input,positive_input,negative_input,negative2_input],outputs=loss_layer)
    # return the model
    return network_train
```

![](https://miro.medium.com/max/1313/1*1BZht07yu6SvnTkq4u1Bdg.png)

## 실제 학습하기

(생략)

## Discussion

실제로 학습해보니 4x 가 3x 에 비하여 논문에서 보여주는 뛰어난 성능이 나오지는 않았다. 그래서 우리는 좀 더 근본적인 이야기를 할 필요가 있어 보인다. 즉 정말로 두 시스템을 완벽하게 비교할 수 있는가? 

- 두 시스템의 하이퍼파라미터를 완벽히 동일하게 설정한다면, 4x 시스템의 성능이 떨어지는 것 같지 않은가?

- mining strategy 가 생각보다 더 중요한 것 같지 않은가? 논문에서는 hardest 샘플을 가져왔지만, 우리는 로컬 배치에서의 hard 샘플을 가져왔다. 이게 국소적인 최적화를 낳은 것이 아닐까? 

- metric network 구조가 잘못되었을까? 계층 3 개를 두는 것이 충분해보였다. 계층을 더 두면 과적합이 일어날 것 같았다. 이 생각이 틀렸을까? 

- encoder 모델이 너무 단순해서 quadruplet loss 또는 learned metric 의 잠재성이 드러나지 않은 걸까? 논문에서 저자들은 우리가 사용한 모델보다 더 크고 복잡한 Resnet 을 사용했었다. 

- 우리가 사용한 OMNIGLOT 데이터셋이 이 모델에 부적합한 게 아니었을까?

- 어쩌면 QuadrupletLoss 논문 자체가 [A Metric Learning Reality Check](https://deepai.org/publication/a-metric-learning-reality-check) 에서처럼 기술적인 결함을 갖고 있던 게 아닐까? [A Metric Learning Reality Check](https://deepai.org/publication/a-metric-learning-reality-check) 논문에서는 저자가 지난 몇년동안 Deep metric learning 이 과대평가되었다고 결론내린다. 

## Summary

- learned metric 과 quadloss 는 상당히 흥미로운 아이디어이다. 하지만 나의 실험에서는 quadloss 의 효능을 보지 못했다. quadloss 는 아마 다른 상황에서 뛰어난 성능을 보이는 것 같다. 

- 논문의 저자들은 4x 시스템이 일반적인 상황에서 더 낫다는 증명을 충분히 보이지 않았다. 이는 논문을 평가할 때 건전한 회의론을 갖는 것이 필요해 보인다.

---

# 《Beyond triplet loss: a deep quadruplet network for person re-identification》 

!!! info 

    2017년 4월 6일에 나온 논문.

# Abstract

우리는 triplet loss 보다 더 성능이 좋은 quadruplet loss 를 소개할 것이다. 4x 시스템은 margin-based online hard negative mining 을 사용한다.

# 1. Introduction

triplet loss 가 널리 사용되고 있지만, 사람의 재인식이라는 관점에서는 테스트 데이터셋에 사람의 신원이 보이지 않거나, 훈련 데이터셋과 겹치는 부분이 없기도 하다. triplet loss 는 큰 내부 클래스 변동에 대한 학습을 한다. 이것은 내부 클래스의 변동를 줄이고 외부 클래스 간의 변동를 높이면 에러율이 높아짐을 의미한다.

이에 따라 우리는 triplet loss 가 테스트 셋에서 보이는 성능을 높이기 위하여 내부 클래스 간 변동을 줄이고 외부 클래스 간의 변동을 높이는 연구를 했다. 그 연구 결과가 quadruplet ranking loss 이다. 이 시스템은 두 가지 기능을 한다. 

1. positive 들을 서로 가깝게 만든다. 

2. negative 페어를 positive 페어로부터 밀어낸다.

첫번째 기능은 triplet loss 에서 소개된 기능과 같다. 하지만 두번째 기능은 외부 클래스 간 변이를 줄이고 내부 클래스 간 변이를 최소화시키게 해준다.

이 두 기능의 밸런스는 2 개의 마진을 어떻게 설정하느냐에 따라 달라진다. 주의할점은 두번째 기능은 훈련 데이터셋에 대하여 모델이 좋은 성능을 내는데에 필요하지는 않다. 하지만 이 기능은 훈련 데이터셋과 테스트 데이터셋에 대한 일반적인 능력을 향상시키는데에 도움이 된다. 파트 5 에서 이 디자인 설계가 외부 클래스 간 변이를 높이고, 내부 클래스 간 변이를 줄이는 실험을 보여줄 것이다.

한편, 몇몇 사람 재인식 딥러닝 모델들은 학습을 위하여 binary classification loss 를 채택하기도 했다. 우리는 우리의 방법을 정당화하기 위하여 quadruplet loss, triplet loss, binary classification loss 를 이론적으로 비교해 볼 것이다.

또한 quadruplet loss 를 사용하는 quadruplet deep network 를 소개할 것이다. 이 모델은 입력으로 quadruplet 을 받게 된다. 실제 실험을 진행하게 되면 작은 데이터셋에 대해서도 이 시스템은 매우 많은 quadruplet sample 을 생성하게 되므로, 어떻게 적합한 샘플링을 할지가 중요한 문제이다. 우리는 샘플링 전략으로 margin-based online hard negative mining 을 택하여 모델을 학습하기 위해 hard sample 들을 추출하도록 했다. 

우리는 알고리즘을 학습된 모델에 따라 적응적으로 margin threshold 를 설정하도록 만들었고, 이 margin threshold 가 hard 샘플들을 자동으로 선택하도록 만들었다. 

정리하자면 우리는 다음 4 가지 성과를 냈다. 

1. strong push 와 weak push 전략을 사용하는 quadruplet loss

2. margin-based online hard negative mining 전략을 사용하는 quadruplet deep network 모델

3. 통합된 관점에서 다른 손실들을 주는 이론적이고 통찰력있는 loss 관계 분석

4. 대표적인 데이터셋(CUHK03, CUHK01, VIPeR)에 대한 뛰어난 성능(기존의 모델보다 더 뛰어난 성능)

# 2. Related work

(생략)

# 3. The proposed approachd

## 3.1. The triplet loss

triplet loss 는 같은 사람 $x_i, x_j$ 와 다른 사람 $x_k$ 에 대한 triplet $\{x_i, x_j, x_k\}$ 들로 학습을 한다. triplet 시스템은 $x_i$ 를 $x_k$ 보다 $x_j$ 에 가깝게 만든다. 이는 $[z] _{+} = \max (z, 0)$ 와 입력 이미지 $f(x_i), f(x_j), f(x_k)$ 와 하이퍼파라미터 $\alpha _{trp}$ 에 대하여

$$ L _{trp} = \sum_{i,j,k}^{N} [\|f(x_i) - f(x_j)\| ^{2} _{2} - \|f(x_i) - f(x_k)\|^{2}_{2} + \alpha _{trp}]_{+} \tag{1} $$ 

으로 표현할 수 있다. image feature $f$ 는 학습이 진행되면서 정규화된다. threshold $\alpha _{trp}$ 는 positive 와 negative 에서 강제되는 여백이다. 또 triplet loss 는 얼굴 유사도를 표현하기 위하여 유클리드 거리를 채택했다.

하지만 우리는 유클리드 거리를 learned metric $g(x_i, x_j)$ 로 대체할 것이다. 이는 기존의 유클리드 거리에 비하여 여러 카메라 사진에 대한 훨씬 견고한 유사도 측정을 제공하게 된다. learned metric 에 의한 loss 함수는 다음과 같다.

$$ L _{trp} = \sum_{i, j, k}^{N} [g(x_i, x_j) ^{2} - g(x_i, x_k) ^{2} + \alpha _{trp}]_{+} \tag{2} $$

방정식 $(1)$ 에서 $f(x_i)$ 는 잘 정규화되고, $\|f(x_i) - f(x_j)\| _{2} \in [0, 1]$ 를 유지하게 된다. 하지만 방정식 $(2)$ 의 $g(x_i, x_j)$ 는 벡터가 아니라 스칼라이다. 이에 따라 $g(x_i, x_j)$ 의 값이 폐구간 $[0, 1]$ 을 유지할 없게 되고, 부분적으로 margin threshold $\alpha _{trp}$ 을 무효화시킨다. 가령 $\alpha _{trp}$ 이 아무리 커도 모델이 지속적으로 $g(x_i, x_j)$ 을 $g(x_i, x_k)$ 와 곱한다. 그래서 3.2 파트에서 triplet loss 를 업그레이드 한 quadruplet loss 를 소개한다.

## 3.2. The quadruplet loss

![image](https://user-images.githubusercontent.com/16812446/96235604-f81c7f80-0fd5-11eb-88df-4644714296b4.png)

:   Figure 2. 세 모딜의 서로 다른 loss 시스템. (a) 는 유클리드 거리를 사용하는 triplet loss 이다. (b) 는 learned metric 을 사용하는 triplet loss 이다. (c) 는 정규화가 포함된 우리가 향상시킨 triplet loss 이다.

먼저 Fig 2 (b) 를 뜻하는 정규화가 필요한 방정식 $(2)$ 를 보완해보자. Fig 2 (c) 는 2 차원 출력을 갖는 fc 계층을 추가하여 정규화를 한 모습을 보여준다. $g(x_i, x_j)$ 의 값이 클수록 두 이미지가 유사하지 않다는 것을 뜻한다. 그러므로 fc 계층의 2 차원 중 하나가 두 이미지의 비유사도를 보여주어야 한다. 이때 2 차원 출력을 정규화하기 위하여 softmax 를 사용했다. 그러면 한 차원(Fig 2 (c) 의 빨간점)은 두 이미지의 비유사도를 표현하는데, loss 에 보내지고 학습이 될 $g(x_i, x_j)$ 의 역할을 한다. 그 결과 $g(x_i, x_j)$ 가 margin threshold $\alpha _{trp}$ 가 효과를 가지도록 폐구간 $[0, 1]$ 로 정규화된다.

또 우리는 마지막 fc 계층 이후에 softmax 계층을 넣어서 두가지 출력이 유사도와 비유사도의 확률을 나타내도록 했다. 이것의 영향력을 파트 5.2 에서 Triplet(Improved w/o sfx) 와 Triplet(Improved) 와 비교해본다. 

방정식 (2) 에서 triplet loss 가 positive 와 negative 사이의 거리를 기반으로 학습한다는 것을 알 수 있다. 우리의 quadruplet loss 는 새로운 제약을 추가했다. 이 제약은 negative 페어를 positive 페어로부터 멀리 민다. quadruplet loss 는 두 margin 을 뜻하는 $\alpha _1, \alpha _2$ 와 이미지 $x_i$ 의 신원 ID 를 뜻하는 $s_i$ 에 대하여 다음과 같다.

$$ L _{quad} = \sum_{i,j,k}^{N} [g(x_i, x_j) ^{2} - g(x_i, x_k) ^{2} + \alpha _{1}] _{+} \\ + \sum_{i,j,k,l}^{N} [g(x_i, x_j) ^{2} - g(x_l, x_k) ^{2} + \alpha _{2}] _{+} \\ s_i = s_j, s_l \neq s_k, s_i \neq s_l, s_i \neq s_k \tag{3} $$

첫번째 항은 positive 와 negative 의 상대적 거리를 계산하는 방정식 (2) 와 같다. 두번째 항이 새롭게 추가되었는데, 이는 서로 다른 이미지에 대한 positive 와 negative 의 거리를 제약한다. 이 제약 덕분에 외부 클래스 간 최소 거리가 내부 클래스 간 최대 거리보다 커진다.

우리는 이 두 항이 손실에 미치는 영향력을 조정하기 위하여 두 margin threshold 를 도입했다. 이때 $\alpha _1$ 이 주된 제약(첫번째 항)을 이룰 수 있도록 충분히 커야 한다. 두번째 항의 $\alpha _2$ 는 두번째 항의 제약이 첫번째 항의 제약보다 약하도록 충분히 작아야 한다. 그러므로 우리의 시스템은 $\alpha _1 > \alpha _2$ 가 되어야 한다.

![image](https://user-images.githubusercontent.com/16812446/96238455-74649200-0fd9-11eb-9e10-25c0ee0ae7ad.png)

:   Figure 3. quadruplet deep network. 빨간 그림자가 씌워진 부분이 Fig 2 (c) 에서 새롭게 추가된 제약이다.

위 그림에서 빨간 그림자를 제외하면 Fig 2 (c) 와 동일하다. 빨간 그림자가 새롭게 추가된 제약을 뜻한다. 이 제약을 통하여 triplet network 가 quadruplet network 로 된다. quadruplet network 는 positive 와 negative 만을 다루는 것(same probe images)이 아니라 different probe images 도 서로 멀어지게 한다. same probe 에 대해서는 positive 와 negative 에 strong push 를 하고, different probe 에 대해서는 상대적으로 약한 weaker push 를 하여 외부 클래스 간 변이를 줄인다.

## 3.3. Margin-based online hard negative mining

방정식 (1) 에서는 margin threshold 보다 짧은 거리를 갖는 샘플을 선택하는 online hard negative mining 을 사용했다. 하지만 이는 적합한 margin threshold 를 미리 정의하기에 어렵다. 작은 threshold 의 결과는 작은 hard samples 들이다. hard sample 들이 모델 학습에 기여하기 때문에, 작은 hard samples 들은 모델의 수렴을 느리게 만들고 모델이 차선의 해답을 내게 만든다. 반면 너무 큰 threshold 는 너무 많은 htard sample 들을 발생시켜서 과적합을 발생시킨다.

따라서 우리의 알고리즘은 학습된 모델에 대한 margin threshold 를 적응적으로 설정한다. 그리고 이렇게 설정된 threshold 로 hard sample 들을 샘플링한다. 적응적인 margin 의 메인 아이디어는 과대하게, 혹은 과소하게 hard smaple 들이 샘플링되는 것을 방지하는 것이다.

adaptive margin threshold 는 실질적으로 서로 다른 두 분포의 평균 거리를 표현하는데에 사용된다. 서로 다른 두 분포란 positive pair 의 거리 분포와 negative pair 거리 분포를 뜻한다. 이에 따라 우리는 서로다른 두 분포에 대한 거리의 평균을 적응적으로 설정하는 margin threshold 로 설정했다.

그러므로 adaptive margin threshold 는 두 거리 분포의 평균을 뜻하는 $\mu _{p}, \mu _{n}$ 과 positive pair 의 개수 $N_p$, negative pair 의 개수 $N_n$ 과 상관 계수 $w$ 에 대하여 

$$ \alpha = w(\mu _{n} - \mu _{p})\\ = w \bigg (\dfrac{1}{N_n} \sum_{i,k}^{N}g(x_i, x_k) ^{2} - \dfrac{1}{N_p}\sum_{i,j}^{N}g(x_i, x_j) ^{2}\bigg ) \\ s_i = s_j, s_i \neq s_k \tag{4} $$

이다. 우리는 방정식 (3) 의 $\alpha _{1}$ 에 대하여 $w = 1$ 로, $\alpha _{2}$ 에 대하여 $w = 0.5$ 로 설정했다.

실제로 구현할 때 두 거리 분포를 매 iteration 마다 구하는 것은 시간이 많이 걸린다. 따라서 각 배치마다의 두 분포의 평균을 대신 사용한다. 배치 크기를 $M$ 이라고 하면 $N_p, N_n$ 은 $M, 2M$ 으로 각각 설정된다. 최적화에는 SGD 를 사용했고, 우리의 손실 함수의 역전파 기울기 미분은

$\mu = \mu _n - \mu _p$ 와 $\iota[a] = \begin{cases} 1 & a = \text{true}\\ 0 & a = \text{false}\\ \end{cases}$ 에 대하여 

$$ \dfrac{\partial L _{quad}}{\partial g(x_i, x_j)} = \bigg (2 - \dfrac{2}{M} \bigg )g(x_i, x_j) \iota [g(x_i, x_k) ^{2} - g(x_i, x_j) ^{2} < \max (\mu , 0)] + \\ \bigg (2 - \dfrac{1}{M} \bigg )g(x_i, x_j) \iota \bigg [g(x_i, x_k) ^{2} - g(x_i, x_j) ^{2} < \dfrac{\max (\mu , 0)}{2} \bigg ] \\ \dfrac{\partial L _{quad}}{\partial g(x_i, x_k)} = \bigg (-2 + \dfrac{3}{2M} \bigg )g(x_i, x_j) \iota [g(x_i, x_k) ^{2} - g(x_i, x_j) ^{2} < \max (\mu , 0)] \\ \dfrac{\partial L _{quad}}{\partial g(x_l, x_k)} = \bigg (-2 + \dfrac{3}{2M} \bigg )g(x_i, x_j) \iota \bigg [g(x_i, x_k) ^{2} - g(x_i, x_j) ^{2} < \dfrac{\max (\mu , 0)}{2} \bigg ] \\ s_i = s_j, s_l \neq s_k , s_i \neq s_l, s_i \neq s_k \tag{5} $$

이다.

결과적으로 매 iteration 마다 margin 이 자동으로 두 거리 분포에 대하여 적응하게 된다. 

# 4. Relationships of different losses

(생략)

Quadruplet vs Triplet: quadruplet 의 방정식의 두번째 항은 different probe images 에 대해서도 모델이 학습하게 하여 외부 클래스 간 변이를 높이고 테스트 데이터셋에 대한 성능을 높혀준다.

# 5. Experiment

![image](https://user-images.githubusercontent.com/16812446/96247670-661c7300-0fe5-11eb-8344-62a849a2dd70.png)

:   Figure 5. 데이터셋 CUHK03 의 훈련 데이터를 여러 모델로 학습한 후 내부 클래스와 외부 클래스 간 거리 분포 그래프이다. 빨간선이 내부 클래스 거리 분포, 파란선이 외부 클래스 거리 분포이다.

우리는 두 가지 실험을 진행하였다. 

1. 다른 loss 와 성능을 비교해보기

2. 현재 제안된 state-of-the-art 모델과 비교해보기

## 5.1. Implementation and Datasets

우리는 Caffe 로 모델을 구현했고, 모든 이미지를 $227 \times 227$ 로 재조정한 다음 모델에 입력했다. 학습율은 $10 ^{-3}$ 으로, 배치 사이즈는 $128$ 로 설정했다. 모든 데이터셋에 대하여 이미지를 수평으로 복사하여 데이터셋 크기를 $4$ 배로 늘렸다.

margin-based hard negative mining 방식을 사용하지 않을 때는 margin threshold 를 각각 $\alpha _1 = 1, \alpha _2 = 0.5$ 로 설정했다. 왜냐하면 margin-based hard negative mining 이 막 시작될 때에는 두 거리 분포가 혼돈 상태라서 두 거리 분포의 평균이 무의미하기 때문이다. 그래서 처음 시작할 때 수렴을 가속화하기 위하여 미리 학습된 네트워크와 고정된 margin threshold 를 사용했다. ImageNet 에서 미리 학습된 AlexNet 모델로 처음 두 합성곱 계층의 커널 가중치를 초기화시켰다. 

![image](https://user-images.githubusercontent.com/16812446/96249267-eb088c00-0fe7-11eb-9fb3-515d34510710.png)

## 5.2. Results of Quadruplet Network

Triplet 과 Quadruplet 시스템을 비교한 부분이 위 표의 아랫부분에 있다. MargOHNM 이 적응적인 margin threshold 방식을 사용한 것이다. 이게 성능이 제일 좋더라.

## 5.3. Comparison with the state of the arts

위 표의 상단부분에서 18 개의 다른 알고리즘과 비교해봤는데, 역시 우리게 제일 성능이 좋더라고 ㅋㅋ 

# 6. Conclusion

하여튼 간에 margin-based online hard negative mining 을 샘플링 방식으로 사용하는 quadruplet loss 가 겁나 좋으니까 이거 써라 ㅇㅋ?