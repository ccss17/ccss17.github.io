# CUDA 메모

- **CPU** 를 **host** , **GPU** 를 **device** 라고 한다.

- `__global__` 키워드를 함수 선언 맨 앞에 쓰면 함수가 **device**  에서 실행된다.

  - **device**  에서 실행되는 함수를 **kernel**  이라고 한다.

- **kernel** 은 **GPU** 에서 실행되는데 **GPU** 는 **CPU** 와 독립된 메모리 공간을 갖는다. 

  - **CPU** 의 메모리 공간을 **host memory**, **GPU** 의 메모리 공간을 **device memory** 라고 한다.

  - **CPU** 의 메모리 공간을 가르키는 포인터를 **host pointer**, **GPU** 의 메모리 공간을 가르키는 포인터를 **device pointer** 라고 한다.

  - device memory 가 host memory 와 독립되어 있기 때문에 host memory 의 데이터를 device memory 로 옮겨주어야만 GPU 가 데이터를 처리할 수 있다. 그러므로 CUDA 프로그램은 다음과 같은 실행흐름을 갖는다.

    1. host memory 를 할당하고, 데이터를 초기화한다.

    2. device memory 를 할당한다.

    3. host memory 의 데이터를 device memory 로 옮긴다.

    4. kernel 을 실행한다.

    5. kernel 실행 결과를 device memory 에서 host memory 로 옮긴다.

    - host memory 할당/해제는 malloc()/free() 또는 new/delete 로 할 수 있다. 
    
    - device memory 할당/해제는 cudaMalloc()/cudaFree() 로 할 수 있다.

    - host memory 에서 device memory 로, 또는 device memory 에서 host memory 로 데이터를 옮기는 것은 cudaMemcpy() 로 할 수 있다.

- 이름 `func` 을 갖는 **kernel**  은 `func<<<GRID, THREADS>>>(...)` 와 같이 호출된다.

  - `THREADS` 는 스레드 블록이 갖는 스레드 개수를 뜻한다.

  - `GRID` 는 스레드 블록의 개수를 뜻한다.

  - **CUDA** 가 `<<<GRID, THREADS>>>` 로써 **kernel** 을 자동으로 GPU 의 병렬 스레드로 호출해준다. 그러므로 각각의 스레드가 **kernal** 의 작업을 공평하게 배분받을 수 있도록 해야 한다. 

    - 스레드에 작업을 공평하게 분배하기 위하여 스레드 인덱스와 스레드 개수, 스레드 블록 인덱스, 스레드 블록 개수 정보가 필요하다. 이를 위하여 다음과 같이 **kernel** 내부에서 사용할 수 있는 변수들이 존재한다.

    - `threadIdx.x` : 스레드 블록 내부에서 현재의 스레드의 인덱스이다.

    - `blockDim.x` : 스레드 블록 내부의 스레드 개수이다.

    - `blockIdx.x` : 스레드 블록 인덱스이다.

    - `gridDim.x` : 스레드 블록의 개수이다.

- `nvprof` 로 CUDA 프로그램의 실행결과를 자세히 분석할 수 있다.
