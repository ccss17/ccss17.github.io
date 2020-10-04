
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
        
        형상이 된다. 

        어쩄든 이로써 입력 데이터의 형상이 끊임없이 줄어들어 언젠가 $(1, 1)$ 이 될 수도 있다. 이렇게 되면 더 이상 합성곱 연산을 적용할 수 없으므로 큰 문제가 된다. 따라서 패딩 $p$ 를 적용함으로써 형상을

        $$(n + 2p - m + 1, n + 2p - m + 1)$$ 

        로 확장해주는 것이다.
    
    !!! info "사소하고 어설픈 증명"
    
        $(n, n)$ 입력 데이터에 $(m, m)$ 커널을 몇번 적용할 수 있는지 조사하기 위하여 집합

        $$ A = \{x + (m - 1) | x \in \N,  x + (m - 1) \leq n\} $$
        
        을 정의해보자. 이 집합은 입력 데이터에 필터가 적용되는 마지막 좌표를 갖는다.
        
        가령 $(7, 7)$ 에 필터 $(3, 3)$ 을 적용하면 집합 $A$ 는 $1 + (m - 1) = m = 3$ 을 시작으로 $7$ 까지의 원소를 가지므로 $A = \{3, 4, 5, 6, 7\}$ 이다. 

        이 집합의 기수 자체가 필터가 적용되는 횟수이다. 그러므로 집합 $A$ 가 의존하는 독립변수 $x \in \N$ 를 조사하면

        $$  x + (m - 1) \leq n \iff  x \leq n - (m - 1) \iff x \leq n - m + 1 $$

        이다. 이는 $x$ 가 $1$ 부터 $n - m + 1$ 까지의 자연수라는 말이므로 집합 $|A| = n - m + 1$ 이고, 결과적으로 커널이 적용되는 횟수가 $n - m + 1$ 번이라는 것이다. 그러므로 $n - m + 1$ 개의 커널 적용 결과가 생성되고 이는 $y$ 축 방향으로도 마찬가지이므로 최종적으로 형상 $(n-m+1, n-m+1)$ 이 생성된다. 
        
- 지금까지 스트라이드stride 는 암묵적으로 $1$ 이 었다. 스트라이드란 필터를 적용하는 위치의 간격이다. 만약 스트라이드를 $2$ 로 하면 필터를 적용하는 윈도우가 두 칸씩 이동한다.

    ![](https://media.vlpt.us/post-images/dscwinterstudy/3084e940-4199-11ea-b8c9-7f7f97d846d5/fig-7-7.png)

    !!! note

        $n > m$ 인 $n, m \in \N$ 에 대하여 $(n, n)$ 입력 데이터에 $(m, m)$ 커널과 패딩 $p$ 와 스트라이드 $s$ 까지 적용하면 그 형상이
        
        $$ \bigg (\dfrac{n + 2p - m}{s} + 1, \dfrac{n + 2p - m }{s}+ 1  \bigg )$$ 

        가 된다. 따라서 이 분수값이 정수로 나누어 떨어져야 하는 것이 중요하다. 딥러닝 프레임워크들은 형상이 나누어떨어지지 않을 때 반올림을 하는 등 에러를 발생시키지 않고 그냥 진행하기도 한다.

    !!! info "사소하고 어설픈 증명"
    
        $(n, n)$ 입력 데이터에 스트라이드 $s$ 로 $(m, m)$ 커널을 몇번 적용할 수 있는지 조사하기 위하여 집합

        $$ A = \{s(x - 1) + m | x \in \N,  s(x - 1) + m \leq n\} $$

        을 정의하자. 이 집합은 입력 데이터에 필터가 적용되는 마지막 좌표를 갖는다.
        
        가령 $(7, 7)$ 에 스트라이드 $s = 2$ 로 필터 $(3, 3)$ 을 적용하면 집합 $A$ 는 $s(x - 1) + m = 2 \cdot 0 + m = 3$ 을 시작으로 $3, 5, 7$ 의 원소를 갖는다. 

        이 집합의 기수 자체가 필터가 적용되는 횟수이다. 그러므로 집합 $A$ 가 의존하는 독립변수 $x \in \N$ 를 조사하면

        $$  s(x - 1) + m \leq n \iff  x \leq \dfrac{n-m}{s} + 1 $$

        이는 $x$ 가 $1$ 부터 $\dfrac{n-m}{s} + 1$ 까지의 자연수라는 말이므로 집합 $|A| = \dfrac{n-m}{s} + 1$ 이고, 결과적으로 커널이 적용되는 횟수가 $\dfrac{n-m}{s} + 1$ 라는 것이다. 그러므로 $\dfrac{n-m}{s} + 1$ 개의 커널 적용 결과가 생성되고, 이는 $y$ 축 방향으로도 마찬가지이므로 최종적으로 형상 $\bigg (\dfrac{n-m}{s} + 1, \dfrac{n-m}{s} + 1\bigg )$ 이 생성된다.

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

- https://leonardoaraujosantos.gitbook.io/artificial-inteligence/machine_learning/deep_learning/convolution_layer/making_faster

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
    def im2col_no_stride_pad(input_data, filter_h, filter_w):
        N, C, H, W = input_data.shape
        out_h = (H - filter_h) + 1
        out_w = (W - filter_w) + 1

        img = np.pad(input_data, [(0,0), (0,0), (0, 0), (0, 0)], 'constant')
        col = np.zeros((N, C, filter_h, filter_w, out_h, out_w))

        for y in range(filter_h):
            y_max = y + out_h
            for x in range(filter_w):
                x_max = x + out_w
                col[:, :, y, x, :, :] = img[:, :, y:y_max:1, x:x_max:1]

        col = col.transpose(0, 4, 5, 1, 2, 3).reshape(N*out_h*out_w, -1)
        return col

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

- 예시 

    $4 \times 4 \times 3$ 형상의 입력에 $3 \times 3 \times 3$ 필터를 스트라이드 $s = 1$ 로 적용한다고 하자. 
    
    그러면 먼저 각 채널 마다, 즉 $3$ 개의 필터 적용 부분공간을 하나의 벡터로 만든다. 이 작업으로 $1$ 개의 벡터가 생성되는 것이다.

    그리고 그 다음 필터 적용 부분공간을 하나의 벡터로 만들고, 또 그 다음 필터 적용 부분공간을 하나의 벡터로 만든다.

    최종적으로 생성된 벡터들을 다음과 같이 하나의 행렬로 만든다. 

    ![](https://praisethemoon.org/wp-content/uploads/2019/04/im2col-3d-1024x510.png)

    ![](https://praisethemoon.org/wp-content/uploads/2019/04/im2col-3d1-1024x510.png)

    ![](https://praisethemoon.org/wp-content/uploads/2019/04/im2col-3d2-1024x510.png)

    ![](https://praisethemoon.org/wp-content/uploads/2019/04/im2col-3d3-1024x510.png)

    *https://praisethemoon.org/demystifying-the-math-and-implementation-of-convolutions-part-iii/*

    그런 다음 각 채널에 적용될 커널도 하나의 벡터로 만든다. 

    !!! note
    
        커널을 여러개 두었다면 행렬이 생성되겠지만, 여기에서는 단순한 예시이므로 하나의 벡터가 생성되었다. 하지만 실제로 이렇게 하면 입력 데이터의 차원이 계속 줄어드니까 안된다.

    ![](https://praisethemoon.org/wp-content/uploads/2019/04/im2col-filter-3d-1.png)

    *https://praisethemoon.org/demystifying-the-math-and-implementation-of-convolutions-part-iii/*

    마지막으로 단지 행렬곱을 하면 된다. 그리고 원래의 입력 형상을 복원해준다.

    ![](https://praisethemoon.org/wp-content/uploads/2019/04/conv-im2col-1-filter-3d-1024x351.png)

    *https://praisethemoon.org/demystifying-the-math-and-implementation-of-convolutions-part-iii/*

- 예시 

    $227 \times 227 \times 3$ 형상의 입력에 $11 \times 11 \times 3$ 필터가 스트라이드 $s = 4$ 와 패딩 $p = 0$ 으로 적용된다고 하자.
    
    그러면 우선 입력 데이터에 필터가 적용되는 $11 \times 11 \times 3$ 블록을 벡터로 쭉 늘어뜨리게 된다. 그러므로 늘어뜨린 벡터 크기는 $11 \times 11 \times 3 = 363$ 이 된다. 또 필터 적용 횟수는 곧 출력 데이터 형상 $\bigg (\dfrac{227 - 11}{4} + 1, \dfrac{227 - 11}{4} + 1\bigg ) = (55, 55)$ 에서 $55 \times 55 = 3025$ 와 같기 때문에 $363$ 사이즈 벡터가 $3025$ 개 생성된다. 그러므로 입력 데이터를 행렬로 바꾸면 $363 \times 3025$ 형상의 행렬이 생성된다.

    이제 필터를 행렬로 바꾸어야 한다. $11 \times 11 \times 3$ 필터를 $96$ 개를 적용한다고 하면 $4$ 차원 필터 $96 \times 11 \times 11 \times 3$ 을 적용하게 되는 것이다. 그러므로 $11 \times 11 \times 3$ 을 먼저 벡터로 바꾸어 $363$ 사이즈 벡터를 만들고 $96$ 개의 벡터로 행렬을 만들어서 최종적으로 $96 \times 363$ 의 행렬을 생성한다.

    이후 가중치 행렬 $96 \times 363$ 와 입력 데이터 행렬 $363 \times 3025$ 를 행렬곱을 하여 $96 \times 3025$ 의 행렬이 나온다. 이것이 합성곱 연산 결과와 같다. 이 행렬을 $55 \times 55 \times 96$ 형상으로 바꾸어 주기만 하면 된다. 이 바꾸는 연산은 `col2im` 함수로 할 수 있다.

    코드구현

    ```python
    def im2col(x,hh,ww,stride):
        """
        Args:
        x: image matrix to be translated into columns, (C,H,W)
        hh: filter height
        ww: filter width
        stride: stride
        Returns:
        col: (new_h*new_w,hh*ww*C) matrix, each column is a cube that will convolve with a filter
                new_h = (H-hh) // stride + 1, new_w = (W-ww) // stride + 1
        """

        c,h,w = x.shape
        new_h = (h-hh) // stride + 1
        new_w = (w-ww) // stride + 1
        col = np.zeros([new_h*new_w,c*hh*ww])

        for i in range(new_h):
            for j in range(new_w):
                patch = x[...,i*stride:i*stride+hh,j*stride:j*stride+ww]
                col[i*new_w+j,:] = np.reshape(patch,-1)
        return col
    ```

- 즉, `im2col` 연산은 다음과 같이 진행된다.

    ![](https://gblobscdn.gitbook.com/assets%2F-LvMRntv-nKvtl7WOpCz%2F-LvMRp9FltcwEeVxPYFs%2F-LvMRrx8aKg05MeAZ3ds%2FConv_Graph_Im2col.png?alt=media)

    *https://leonardoaraujosantos.gitbook.io/artificial-inteligence/machine_learning/deep_learning/convolution_layer/making_faster*

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

    **구체화 필요**

- 이렇게 1층 합성곱 계층에서는 엣지(색상이 바뀌는 경계선)와 블롭(국소적으로 덩어리진 영역) 등의 저수준 정보가 추출된다.

    그런데 CNN 층을 깊게 만들면 추출되는 정보들이 더 고차원적으로 추상화된다는 연구결과가 있다.

    AlexNet 이라는 8층 CNN 을 구성할 경우 1층에서 에지와 블롭, 3층에서 텍스쳐, 5층에서 사물의 일부, 마지막 완전연결 층에서는 사물의 클래스에 뉴런이 반응했다.

    즉, 층이 깊어지면 뉴런이 반응하는 대상이 단순한 모양(저차원적 대상) 에서 추상적인 정보로 변화해간다. 다시 말해 사물의 의미를 이해하도록 변화하는 것이다.

# 여러 CNN

CNN 네트워크를 어떻게 구성해야 할지에 대한 제안은 다양하다.

!!! tldr ""

    LeNet : 1998년에 제안된 손글씨 인식 CNN 네트워크이다.

- 합성곱 계층과 풀링 계층(원소를 줄이기만 하는 서브샘플링 계층)을 반복하다가 마지막에 완전연결 계층을 거치면서 결과를 출력한다.

- LeNet 은 현재의 CNN 과 차이가 있는데, 첫번째 차이는 Sigmoid 활성화 함수를 사용한다는 것이다. 현재는 주로 ReLU 를 사용한다.

    또 LeNet 은 서브샘플리을 하여 중간 데이터를 줄이지만, 현재는 맥스 풀링이 주류이다.

!!! tldr ""

    AlexNet : 2012년에 제안된 CNN 네트워크이다.

- LeNet 과 크게 다르지는 않다. AlexNet 도 합성곱 계층과 풀링 계층을 거듭하며 마지막에 완전연결 게층을 거쳐 결과를 출력한다.

- 다만 차이점은 활성화 함수로 ReLU 를 사용하고,

    LRN(Local Response Normalization) 이라는 국소적 정규화 계층을 사용하며,

    드롭아웃을 사용한다.

- 비록 20세기에 지안된 LeNet 과 큰 차이가 있지는 않지만 AlexNet 으로 인하여 딥러닝 열풍이 시작되었다.

# 정확도 향상 팁

!!! tldr ""

    What is the class of this image? : 다양한 데이터셋을 대상으로 논문 등에서 발표한 기법들의 정확도 순위를 보여주는 사이트이다.

- 이 사이트의 상위 기법들을 참고하면 정확도를 높일 수 있는 기술이나 힌트를 얻을 수 있다.

    !!! example
    
        앙상블 학습, 학습률 감소, 데이터 확장 등이 정확도 향상에 도움이 된다.

!!! tldr ""

    데이터 확장(data augmentation) : 입력 이미지를 인위적으로 확장한다.

- 이미지를 회전하거나 세로로 이동하는 등 미세한 변화를 주어 이미지 개수를 늘리는 것이다. 이는 데이터가 몇 개 없을 때 매우 효과적이다.

- 가령 이미지 일부를 잘라내는 **crop** 이나 좌우를 뒤집는 **flip** 등이 적용된다.

!!! tldr ""

    딥러닝 : 층을 깊게 한 신경망이다.

- 층을 깊게 하는 이유에 대한 논리적이고 수학적인 설명과 이론적 근거는 솔직히 아직 부족하다. 그러나 연구와 실험적으로 설명할 수 있는 것들은 몇 가지 있다.

    - ILSVRC 로 대표되는 대규모 이미지 인식 대회의 상위 기법들이 대부분 딥러닝이다. 그리고 그 경향은 층을 더 깊게 만드는 방향으로 가고 있다. 즉, 층의 깊이에 비례하여 정확도도 좋아진다는 추론을 할 수 있다.

    - 층을 깊게하면 신경망 매개변수가 줄어든다.

        층을 깊게한 신경망은 깊지 않은 경우보다 적은 매개변수로 같거나 뛰어난 표현력을 달성할 수 있다.

        !!! example
        
            가령 CNN 에서 $5 \times 5$ 필터를 사용하는 1개 층을 사용할 경우 $5 \times 5$ 영역을 $1 \times 1$ 출력 영역으로 계산하는데 $25$ 개 매개변수가 필요하다. 그러나 $3 \times 3$ 필터를 사용하는 2개 층을 사용할 경우 똑같은 $5 \times 5$ 영역을 $2$ 개의 층을 거쳐 $1 \times 1$ 출력 영역으로 계산하지만, $18$ 개의 매개변수가 필요하다.

            마찬가지로 $3 \times 3$ 합성곱 연산을 $3$ 회 반복하면 매개변수가 $27$ 개지만 같은 크기의 영역을 $1$ 회의 합성곱 연산으로 보기 위해서는 $7 \times 7$ 필터, 즉 매개변수 $49$ 개가 필요하다.
        
        이로써 적은 매개변수로 넓은 수용 영역(receptive field, 뉴런에 변화를 일으키는 국소 영역) 를 소화할 수 있다.

        또한 층 사이에 ReLU 활성화 함수를 끼워넣어 신경망 표현력을 개선시킬 수 있다. 왜냐하면 활성화 함수가 신경망에 비선형 힘을 가하고, 비선형 함수가 겹치면서 더 복잡한 것도 표현할 수 있게 되기 때문이다. 
    
    - 층을 깊게하면 학습 효율성도 높아진다. CNN 을 시각적으로 표현했을 때 층이 깊어질 수록 더 추상화되고 고차원적인 표현력이 이루어진다는 것을 알아보았기 때문이다.

!!! tldr ""

    ILSVRC(ImageNet Large Scale Visual Recongintion Challenge) : 딥러닝의 열풍을 일으킨 이미지 인식 대회이다.

- 2012년 AlexNet 이 압도적인 성적으로 우승하면서 딥러닝이 트렌드가 되었다.

- 이 대회에서는 ImageNet 이라는 100만장이 넘는 이미지 데이터셋을 사용하는데 이 거대한 데이터셋으로 신경망의 성능을 겨룬다.

- 2010 년 NEC America, 2011 년 Xerox, 2012년 AlexNet, 2013년 Clarifi, 2014년 VGG, 2015년 GoogLeNet, 2015년 ResNet 이 우승하였다.

    특히 ResNet 은 오류율을 3.5% 까지 낮췄는데 이는 인간의 인식 능력을 넘어선 것이다.

!!! tldr ""

    VGG : 합성곱 계층과 풀링 계층으로 구성되는 기본적인 CNN 이다.

- 비중이 있는 층(합성곱 계층, 완전연결 계층)을 16층 혹은 19층으로 심화한 것이 특징이다. 각각 VGG16, VGG19 로 구분한다.

- VGG 는 $3 \times 3$ 의 작은 필터로 합성곱 계층을 쌓는다. 

- VGG 는 2014 년 대회에서 2위에 올랐고 GoogLeNet 이 1위를 했지만 구성하기가 쉬워 널리 사용된다.

    ![](https://neurohive.io/wp-content/uploads/2018/11/vgg16-1-e1542731207177.png)

!!! tldr ""

    GoogLeNet : 세로 방향의 층을 깊게할 뿐 아니라 가로방향 층도 깊게한 CNN 신경망이다.

- GoogLeNet 은 가로 방향에 폭이 있다. 이것을 인셉션 구조라고 한다.

    ![](https://www.researchgate.net/publication/327249814/figure/fig4/AS:754608565678080@1556924110809/Image-of-GoogLeNet-architecture-17.jpg)

- 입센션 구조는 앞 계층의 입력을 받아서 $1 \times 1$ 합성곱, $3 \times 3$ 합성곱, $5 \times 5$ 합성곱, $3 \times 3$ 맥스 풀링으로 가로 층을 확장한다.

    ![](https://pytorch.org/assets/images/googlenet1.png)

    인셉션 구조는 다음과 같이 더욱 확장 및 응용될 수 있다. 

    ![](https://qph.fs.quoracdn.net/main-qimg-729049bf3f099a675d80c09eaf897e21)

    인셉션 구조는 위와 같이 크기가 다른 필터와 풀링을 여러 개 적용하고 그 결과를 결합한다. 이 인셉션 구조를 하나의 빌딩 블록(구성요소) 로 사용하는 것이 GoogLeNet 의 특징이다.

    또 $1 \times 1$ 크기 필터를 사용하는 합성곱 계층을 사용하기도 하는데 이는 채널 쪽 크기를 줄이는 것으로 매개변수 제거와 고속 처리에 기여한다. (Going Deeper With Convolutions(2015))

!!! tldr ""

    ResNet : MS 에서 개발한 CNN 네트워크이다.

- 층을 깊게 할 수 있는 특별한 장치를 도입한 것이 특징이다. 층을 깊게하면 성능이 향상되기는 하지만 층이 너무 깊으면 학습이 잘 되지 않고 오히려 성능이 떨어질 때도 있다.

    이를 해결하기 위해 ResNet 은 스킵 연결(skip connection) 을 도입했다. 이 구조가 층의 깊이에 비례해 성능을 향상시킬 수 있게 하는 장치이다. 물론 그래도 여전히 층을 깊게 하는 것에 한계는 존재한다.

- 스킵 연결이란 입력 데이터를 합성곱 계층을 건너뛰어 출력에 바로 더하는 구조이다.

    ![](https://miro.medium.com/max/1140/1*D0F3UitQ2l5Q0Ak-tjEdJg.png)

    weight layer 는 합성곱 계층을 뜻한다. 위 그림은 입력 $x$ 를 연속한 두 합성곱 계층을 건너뛰어 출력에 바로 연결한다. 단축 연결이 없었다면 출력이 $F(x)$ 가 되지만, 스킵 연결로 인하여 출력이 $F(x) + x$ 가 된다.

    이 스킵 연결이 층이 깊어져도 학습을 효율적으로 할 수 있게 해준다. 왜냐하면 역전파 때 스킵 연결이 신호 감쇠를 막아주기 때문이다. 스킵 연결은 입력 데이터를 그대로 흘려주는데 역전파 때도 상류의 기울기를 그대로 하류로 내보내준다. 그래서 기울기가 과도하게 작아지거나 커지지 않고 의미있는 기울기가 전달될 수 있다.

    즉, 스킵 연결이 실제로 하는 일이란 층을 깊게 할수록 기울기가 작아지는 소실 문제를 완화시켜주는 것이다.

- ResNet 은 다음과 같이 VGG 를 기반으로 스킵 연결을 도입하여 층을 깊게 만들 수 있었다.

    ![](https://kharshit.github.io/img/resnet_50.png)

    ResNet 은 위와 같이 합성곱 계층을 2개 층마나 스킵하면서 층을 깊게 만든다.

    실험결과 150층 이상으로 해도 정확도가 올랐다. 그리고 ILSVRC 대회에서 오류율이 3.5% 라는 경이로운 성과를 낼 수 있었다.

!!! tldr ""

    전이 학습(transfer learning) : 거대한 데이터셋을 학습한 가중치를 다른 신경망에 복사하여 그 상태에서 재학습을 수행하는 것이다.

- 가령 VGG 와 구성이 같은 신경망을 준비하고 미리 학습된 가중치를 초깃값으로 설정한 후, 새로운 데이터셋을 대상으로 재학습(fine tuning) 을 수행하는 것이다.

- 전이 학습은 데이터셋이 적을 때 유용하다.

# 딥러닝 고속화

!!! tldr ""

    GPU 고속화 : GPU 병렬 수치 연산으로 순전파를 효율적으로 처리하는 것이다.

- 딥러닝은 대량의 단일 곱셈-누산(혹은 큰 행렬곱)을 처리하는데 이는 GPU 의 특기다.

- CPU 로 40일 걸리는 연산을 GPU 로 6일만에 처리할 수 있다.

- 합성곱 계층의 im2col 연산은 큰 행렬의 곱으로 변환할 수 있는데 이는 GPU 가 최적으로 수행할 수 있다. GPU 는 작은 단위 연산보다 큰 덩어리의 연산에 유리하기 때문이다.

    im2col 의 큰 행렬곱을 GPU 가 한 번에 처리할 수 있다.

!!! tldr ""

    분산학습 : 딥러닝 학습을 다수의 GPU 로 분산하여 처리하는 것이다.

- GPU 로 딥러닝 처리를 고속화할 수 있지만, 여러 GPU 로 딥러닝 시간을 더욱 단축할 수 있다.

- 구글의 TensorFlow 나 MS 의 CNTK 가 분산학습에 중점을 두고 개발된 딥러닝 프레임워크이다.

- 7일짜리 연산을 GPU 100 개를 사용하여 3시간만에 끝낼 수 있다.

- 분산 학습 관련 기술은 TensorFlow 기술 논문 등을 참고할 수 이싿. 

    - 논문 : TensorFlow: Large-Scale Machine Learning on Heterogeneous Distributed Systems

!!! tldr ""

    메모리 절약 : 계산 능력 외에도 메모리 용량과 버스 대역폭 등이 딥러닝 고속화에 병목이 될 수 있기 때문에 메모리 용량을 최적화 시키는 것이다.

- 딥러닝은 대량의 가중치 매개변수를 저장해야 한다. 64비트나 32비트 부동소수점으로 실수를 표현할 수 있는데, 비트 수를 높일수록 정확도가 늘어나지만 그만큼 메모리 사용량이 늘고 버스대역폭에 부담이 간다.

    다행히 딥러닝은 높은 수치 정밀도를 요구하지 않는다. 왜냐하면 신경망은 견고성이라는 성질을 갖기 때문이다. 이는 입력에 노이즈가 좀 섞여도 출력이 잘 달라지지 않는다는 특징이다.

- 컴퓨터는 실수를 32비트 단정밀도(single-precision) 와 64비트 배정밀도(double-precision) 등으로 표현하지만, 지금까지의 실험으로는 16비트 반정밀도(half-precision) 만 사용해도 학습에 문제가 없다고 알려져 있다. (논문: Deep learning with limited numerical precision)

- 2016년부터 엔비디아의 GPU 인 파스칼 아키텍쳐부터 16비트 반정밀도를 지원하기 시작했다. 맥스웰 아키텍쳐도 반정밀도 스토리지를 지원하고는 있었지만 연산 자체를 16비트로 수행하지는 않았다. 그러나 파스칼 아키텍쳐가 연산도 16비트로 하기 시작하자 성능이 2배 정도 빨라졌다.

- 파이썬은 기본적으로 64비트 배정밀도 부동소수점을 사용하지만, NumPy 에서 16비트 반정밀도 부동소수점으로 딥러닝을 하면 정확도가 떨어지지 않는대신 속도는 올라간다는 것을 알 수 있다.

- 최근에는 가중치와 중간 데이터를 1비트로 표현하는 **Binarized Neural Networks** 라는 방법도 등장했다. (논문: Binarized Neural Network: Training Deep Neural Networks with Weights and Activations Constrained to+1 or-1)

- 메모리 절약은 딥러닝 고속화를 위하여 중요하게 생각해야 하며, 특히 임베디드 딥러닝에 있어서 매우 중요한 주제이다.

!!! tldr ""

    사물 검출 : 

!!! tldr ""

    분할(segmentation) :

!!! tldr ""

    이미지 생성 : 

!!! tldr ""

    강화학습 : 