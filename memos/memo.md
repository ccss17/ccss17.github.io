# <a name="trivial memo " href="#trivial memo ">trivial memo </a>

## <a name="Colab 에서 TensorBoard 사용하기 " href="#Colab 에서 TensorBoard 사용하기 ">Colab 에서 TensorBoard 사용하기 </a>

1. 코드 셀 하나를 만들고 다음 두 줄 코드 실행 

  ```
  !wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
  !unzip ngrok-stable-linux-amd64.zip
  ```

    - 그리고 주석처리하거나 셀을 삭제해서 모든 셀 실행 시 다시 실행되지 않도록 합니다. 

2. TensorBoard 로그를 생성한다. 

  ```python
  import torchvision
  import torchvision.transforms as transforms
  # transforms
  transform = transforms.Compose(
    [transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))])
  # datasets
  trainset = torchvision.datasets.FashionMNIST('./data',
    download=True,
    train=True,
    transform=transform)
  trainloader = torch.utils.data.DataLoader(trainset, batch_size=4,
                                        shuffle=True, num_workers=2)
  # get some random training images
  dataiter = iter(trainloader)
  images, labels = dataiter.next()
  # create grid of images
  img_grid = torchvision.utils.make_grid(images)
  from torch.utils.tensorboard import SummaryWriter
  # default `log_dir` is "runs" - we'll be more specific here
  writer = SummaryWriter('runs/fashion_mnist_experiment_1')
  # write to tensorboard
  writer.add_image('four_fashion_mnist_images', img_grid)
  ```

    - 이 경우 `runs` 디렉토리가 로그가 저장되는 경로이다. 

3. 또 코드 셀을 하나 만들고 tensorboard 를 실행한다. 이때 `runs` 디렉토리에 로그가 저장되어 있다고 가정한다. 

  ```python
  LOG_DIR = './runs'
  get_ipython().system_raw(
  'tensorboard --logdir {} --host 0.0.0.0 --port 6006 &'
  .format(LOG_DIR)
  )
  ```
   
4. ngrok 로 외부에서 내부 tensorboard 로 연결할 수 있는 터널링 프록시를 만든다. 

  ```python
  get_ipython().system_raw('./ngrok http 6006 &')
  ```

5. 마지막으로 만들어진 터널의 public URL 을 얻어서 브라우저로 접속하면 된다. 

  ```shell
  ! curl -s http://localhost:4040/api/tunnels | python3 -c \
    "import sys, json; print(json.load(sys.stdin)['tunnels'][0]['public_url'])"
  ```


