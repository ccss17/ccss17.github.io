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

# 1. Introduction

# 2. Related work

# 3. The proposed approachd

## 3.1. The triplet loss

## 3.2. The quadruplet loss

## 3.3. Margin-based online hard negative mining

# 4. Relationships of different losses

# 5. Experiment

## 5.1. Implementation and Datasets

## 5.2. Results of Quadruplet Network

## 5.3. Comparison with the state of the arts

# 6. Conclusion
