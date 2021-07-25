
# The NumPy array: a structure for efficient numerical computation

> ref : https://arxiv.org/abs/1102.1523

numpy 는 다음 3가지 기법으로 Python 이라는 하이레벨 언어에서 효율적인 행렬 계산을 할 수 있도록 했다. 1) 벡터화 계산, 2) 메모리 복사 피하기, 3) 연산 횟수 줄이기. 먼저 numpy 행렬 구조를 소개하고 이 기법들에 대해서 소개한 후 마지막으로 행렬 데이터를 다른 라이브러리와 어떻게 공유할지 소개한다. 

Python 은 리스트와 딕셔너리를 제공하지만 이 자료구조들은 고성능 수치 계산에는 적합하지 않다. numpy 행렬은 다차원 행렬인데, 이는 원소의 타입과 형상에 의하여 구성된다.

## Basic usage

(numpy 사용법은 다들 잘 아니까 pass)

## The structure of a Numpy array: a view on memory

ndarray 라고 불리우는 numpy 행렬은 다음 성질로 사용하는 메모리를 설명한다. 

- Data pointer: 행렬의 첫번째 바이트의 메모리 주소이다.

- Data type description : 행렬의 원소의 타입이다. 가령 부동소수점이라든가 정수라든가.

- Shape : 행렬의 형상이다. 가령 (10, 10) 이라든가 (5,5,5) 라든가. 특히 (5,5,5) 는 x, y, z 축을 뜻한다.

- Strides : Strides 는 다음 원소를 지칭하기 위하여 몇 바이트를 넘어가야 하는지 말해준다. 가령 (10, 10) 의 바이트 행렬의 Strides 는 (10, 1) 이다. 이는 1바이트를 지나치면 다음 열로 갈 수 있고, 10바이트를 지나치면 다음 행으로 갈 수 있다는 것이다.

- Flags : 메모리를 수정할 수 있는지, 메모리 레이아웃이 C 스타일인지 Fortran 스타일인지 등등을 정한다.

numpy 행렬의 stride 는 메모리 복사를 피하게 하여 성능을 높혀준다. 가령 다음을 보자.

```python
In [1]: x = np.arange(9).reshape((3, 3))

In [2]: x
Out[2]: array([[0, 1, 2],[3, 4, 5],[6, 7, 8]])

In [3]: x.strides
Out[3]: (24, 8)
```

우리가 현재 대부분 사용하는 컴퓨터는 64비트(8바이트) 아키텍쳐이므로 stride 가 (24, 8) 이라는 것은 다음 행을 지칭하기 위하여 24바이트, 즉 3개의 정수를 건너뛰어야 한다는 것을 의미한다. 이때 다음과 같이 이 행렬의 2번째 원소들만으로 새로운 행렬을 만들어서 stride 를 살펴보자.

```python
In [4]: y = x[::2, ::2]

In [5]: y
Out[5]: array([[0, 2],[6, 8]])

In [6]: y.strides
Out[6]: (48, 16)
```

이때 행렬 y 의 stride 는 (48, 16) 이다. 이는 다음 원소를 지칭하기 위하여 정수 2개를 건너뛰어야 하고, 다음 행을 지칭하기 위하여 정수 8개를 건너뛰어야 한다는 말이다. 이것은 행렬을 복사한 것이 아니라 행렬 x 의 메모리 레이아웃에서 stride 만 바뀐 행렬 y 를 만들었기 때문이다. 즉 x 와 y 는 같은 메모리를 지칭하고 있다. 이로써 행렬 복사를 피할 수 있고 성능을 높힐 수 있다는 것이지.

같은 원리로 행렬의 전치(transpose) 연산이나 형상 변경(reshape)을 할 때도 행렬 복사가 아닌, stride 를 조작함으로써 zero-cost 계산을 할 수 있게 된다. 가령 다음을 보자.

```python
# Transpose the array, using the shorthand "T"
In [9]: xT = x.T

In [10]: xT
Out[10]:array([[0, 3, 6],[  1, 4, 7],[  2, 5, 8]])

In [11]: xT.strides
Out[11]: (8, 24)

# Change the shape of the array
In [12]: z = x.reshape((1, 9))
In [13]: z
Out[13]: array([[0, 1, 2, 3, 4, 5, 6, 7, 8]])

In [14]: z.strides
Out[14]: (72, 8)
# i.e., for the two-dimensional z, 9 * 8 bytes# to skip over a row of 9 uint8 elements,# 8 bytes to skip a single element
```

행렬 z 의 타입을 64비트 정수가 아니라 바이트로 바꾸어도 마찬가지로 stride 만 바꾼다. 다음을 보자.

```python
>>> z.dtype = np.dtype('uint8')
>>> z
array([[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0,
        0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0,
        0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 8, 0,
        0, 0, 0, 0, 0, 0]], dtype=uint8)
>>> z.shape
(1, 72)
>>> z.strides
(72, 1)
```

!!! note

    대박인데? 이게 가능한 이유가 뭐였고, 이런 방법을 찾을 수 있던 게 뭐였을까. 한 대상을 우리가 원하는 대상으로 사상시키려 할 때 여러가지 방법이 있다는 것을 규명한다. 메모리 복사도 가능할 것이고, 다른 방법도 존재하겠지만, 그 중에서 가장 비용이 낮은 것은 stride 를 바꾸는 것이다.

    근데 stride 라는 개념 자체를 정의해야 이런 아이디어를 얻을 수 있었을 것이다. 이런 개념을 어떻게 정의할 수 있었을까? 그것은 한 대상의 구조를 면밀하고 엄밀하게 분석하여 정의했기 때문인 것 같다. 여기에도 수학의 방식이 사용되었겠지. 시간을 들여서 어떤 대상의 구조를 수학적인 방식으로 심층적으로 분석하는 게 전혀 시간낭비가 아니구나.

## operations on arrays: vectorization and broadcasting

많은 프로그래밍 언어에서 무분별한 for 루프의 사용은 프로그램의 전체 성능을 매우 떨어뜨린다. 이 상황은 단순한 연산을 큰 데이터셋에 적용할 때 발생한다. numpy 는 vectorization 이라고 부르는 grouping element-wise operation 으로 이런 연산을 매우 빠르게 해낸다. 

벡터 a 에 3 을 곱해야 한다고 생각하자. 전통적인 for 루프로는 다음과 같이 해야 한다. 

```python
a = [1,3,5]
b = [3*x for x in a]
```

하지만 벡터화의 접근으로는 다음과 같이 한다. 

```python
a = np.array([1,3,5])
b = 3 * a
```

numpy 의 벡터화 연산은 C 언어에서 구현되어 있어서 매우 빠른 속도를 낼 수 있다. 이 연산은 스칼라와 행렬 사이에서만 가능한 게 아니다. 다음과 같이 행렬과 행렬 사이의 뺄셈 연산도 가능하다.

```python
b - a
```

!!! note

    벡터화 연산에 대한 구체적인 원리를 설명하지는 않는건가. 그럼 C 에서의 구현을 살펴봐야겠네. 아니면 그냥 C 로 for 문을 구현해서 빠르다는 것일 수도 있고.

numpy 는 두 행렬의 형상이 다를 때 한 행렬을 확장하여 연산을 완료한다. 다음을 보자.

```python
In [28]: m = np.arange(6).reshape((2,3))

In  [29]:m
Out [29]:array([[0, 1, 2],[3, 4, 5]])

In [30]: b + m
Out[30]:array([[ 3, 10, 17],[ 6, 13, 20]])
```

이것을 브로드캐스팅이라 하는데, 이러한 broadcasted 행렬 또한 물리적으로 생성되지 않고, stride 를 사용하여 이루어진다. 

## Broadcasting Rules

두 행렬을 브로드캐스팅 하기 전에 numpy 는 두 행렬의 형상이 맞춰질 수 있는지 검사한다. 가령 형상 (2, 4, 3) 과 (4, 1) 을 갖는 행렬 x, y 를 생각하면 z = x+y 의 형상을 다음과 같이 정한다. 

$$ \begin{array}{rl}
x&amp; (2, 4, 3) \\
y&amp; ( 4, 1 )\\
\hline z &amp; (2, 4, 3); 
\end{array} 
$$

## Vectorization and broadcasting examples

함수 f 에 행렬 x 를 입력하여 계산하고 싶다고 하자. 전통적인 for 루프로 짠다면 

```python
def f(x):
    return x+1

x = np.arange(1e5)
y = [f(i) for i in x]
```

와 같이 짤 것이다. 하지만 이는 약 0.5 초가 걸릴정도로 매우 비효율적이다. numpy 는 다음과 같이 벡터화된 루프를 사용하여 연산이 약 0.001 초가 걸릴정도로 매우 효율적으로 적용한다.

```python
y=f(x)
```

하지만 주의해야 할 점이 있다. 만약 다음과 같이 행렬 연산을 한다고 하자.

```python
a = x**2
b = 3*x
c = a - b
fx = c + 4
```

이렇게 하면 매번 임시 행렬이 생성되므로 비효율적이다. 그래서 in-place 연산을 다음과 같이 해야 한다.

```python
def g(x):
    # Allocate the output array with x-squared
    fx = x**2
    # In-place operations: no new memory allocated
    fx -= 3*x
    fx += 4
    return fx
```

이러면 한 자리에 임시 행렬이 생성되고 계속 연산을 한 다음 반환되서 성능이 2배 이상 효율적이다. 참고로 Cython, Theano, numexpr 같은 걸 쓰면 cache 사용을 극한으로 올려줘서 성능을 더욱 높힐 수 있다.

### Evaluating Functions

### Finite Differencing

pass

### Creating a grid using broadcasting

pass

### Computer Vision

(결국 벡터화를 하면 성능이 많이 좋아지는데, 그것이 어떻게 구현되었는지는 설명하지 않네.)

## Sharing data

pass

### Efficient I/O with memory mapping

pass

### The array interface for foreign blocks of memory

pass

### Structured data-types to expose complex data

pass

## Conclusion

pass
