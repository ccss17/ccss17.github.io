# [ccss17.github.io](https://ccss17.github.io)

# Docker 메모 

## 시작 

- `ubuntu 18.04` 시작 

  ```shell
  docker run -it --name gbc ubuntu:18.04 /bin/bash
  ```

- `ubuntu 18.04` 시작(privileged mode)

  ```shell
  docker run -it --privileged --name gbc -w /root ubuntu:18.04 /usr/bin/zsh
  ```

- `gdb` 실습환경 시작(privileged mode)

  ```shell
  docker run -it --privileged --name gbc -w /root ccss17/security-tutorial
  ```

- `tensorflow` 시작 

  ```shell
  docker run -it -p 8888:8888 --name tf -v ${HOME}/repo/testrepo/tftest:/tf -u $(id -u):$(id -g) tensorflow/tensorflow:latest
  ```

- `pytorch notebook` 시작 
  
  ```shell
  docker run -d --name torch-notebook -p 8888:8888 -p 6006:6006 -v $PWD:/workspace ccss17/torch-notebook
  ```

  또는 윈도우에서 경로지정을 위하여 다음과 같이 실행할 수 있다. 

  ```shell
  docker run -d --name torch-notebook -p 8888:8888 -p 6006:6006 -v d:\repo\torch-test:/workspace ccss17/torch-notebook
  ```

## 관리

- 실행중인 컨테이너 중지 

  ```shell
  # 그냥 컨테이너 내부 쉘에서 exit 입력 
  exit
  ```
  
  또는 로컬 쉘에서 다음 명령어 입력 

  ```shell
  docker stop <container>
  ```

- 중지된 컨테이너 재시작

  ```shell
  docker start -ai <container>
  ```

- 변경된 컨테이너로부터 이미지 생성 

  ```shell
  docker commit <컨테이너> <새이미지이름>
  ```

  - 중지된 컨테이너로부터 이미지 생성하고 privileged mode 로 시작하기 위해 사용할 수도 있음. 

- `docker exec [OPTIONS] CONTAINER COMMAND [ARG...]` : 실행중인 컨테이너에 명령 실행 

  - `-d` : 백그라운드로 실행한다.

  - `-it` : `STDIN` 을 유지시키고 `pseudo-TTY` 를 허가하여 키보드 상호작용이 필요할 때 사용한다.

  - `--privileged` : 상승된 권한으로 실행한다. `ASLR` 을 꺼야하는 상황 등에서 유용하다.

  - `-w` : 명령어가 실행될 위치를 지정한다. 

  

## 상태

- 이미지 상태 보기

  ```shell
  docker images 
  ```

- 실행 중인 컨테이너 상태 보기

  ```shell
  docker ps 
  ```

- 중지된 컨테이너를 포함한 모든 컨테이너 상태 보기

  ```shell
  docker ps -a
  ```

## 삭제 

- 컨테이너 삭제 

  ```shell
  docker rm container
  ```

- 중지된 컨테이너 모두 삭제 

  ```shell
  docker rm -v $(docker ps -a -q -f status=exited)
  ```

## 빌드 

- 이미지 생성 

  ```shell
  docker build -t username/image .
  ```

  ```shell
  docker build -t app .
  ```

- 이미지 이름 변경 

  - `app` 에서 `username/image:1` 으로 (`버전 == 1`)

    ```shell
    docker tag app username/image:1
    ```

## 공유 

- 이미지 푸쉬 

  ```shell
  docker login
  docker push username/image
  ```
