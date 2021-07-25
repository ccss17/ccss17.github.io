
## **<div align="center"> ☀️ ️여기서부터 Day5   ☀️ </div>**

# Build System

C/C++ 소스코드를 컴파일하기 위해서는 

```shell
$ gcc main.c -o main
```

와 같은 명령어를 실행해야 합니다. 하지만 컴파일할 파일이 많아질 경우 이러한 컴파일 명령어가 매우 복잡해지는데, 이러한 고잡한 빌드 과정 자체를 관리하기 위하여 빌드 시스템이 개발되었죠.

기본적으로 Make 가 가장 기초적인 빌드 시스템인데, 이 빌드 시스템의 여러 단점을 보완하기 위하여 CMake, Maven, Bazel 같은 새로운 빌드 시스템들이 나왔습니다. 여기에서는 Make 의 기본적인 사용방법과 새로운 빌드 시스템 중 Bazel 의 사용법만 간단하게 살펴보겠습니다. 

!!! note

    여러 빌드 시스템이 많지만 각자 장단점이 있기 때문에 여러분의 프로젝트에 적절한 빌드 시스템을 선정하여서 사용하면 됩니다.

# Make

> 참고/출처 : https://makefiletutorial.com/

먼저 도커 컨테이너에서 다음 명령어를 통하여 빌드 시스템을 연습할 공간을 만들어 주세요.

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ mkdir build-test
$ cd build-test
$ touch main.c
$ touch Makefile
```

그리고 `main.c` 의 내용을 다음과 같이 채워넣으시면 됩니다. 

```c
#include <stdio.h>

int main(void)
{
    printf("Build system test\n");
    return 0;
}
```

그리고 `Makefile` 의 내용을 다음과 같이 채워넣어 주세요. 

```makefile
all:
    gcc main.c -o main
```

그리고 다음 명령어를 실행해봅시다. 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ make
```

그러면 컴파일이 완료되어서 `main` 이라는 실행파일이 생깁니다. 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ ./main
```

실행까지 해보죠. 이제 Makefile 에 대하여 알아보겠습니다.

## 일반 규칙 

`Makefile` 은 수 개의 규칙으로 구성되는데 규칙의 일반적 문법은 다음과 같습니다.

```make
targets : prerequisites 
    command
    command
    command
    ...
```

- ==**`targets` : 규칙 이름으로써 공백으로 구분되는 파일 이름들이다. 만들어질 파일 이름을 뜻한다. 보통 규칙 당 하나의 파일만 있다.**==

- ==**`commands` : `targets` 을 만드는 일련의 명령어들이다.**==

    - 이 부분은 공백이 아닌 탭으로 시작되어야만 한다.

- ==**`prerequisites` : 공백으로 구분되는 파일 이름들로써 `commands` 가 실행되기 위하여 필요한 의존성 파일 리스트를 뜻한다.**==

만약 이 `prerequisites` 의 파일들 중 하나가 존재하지 않는다면 먼저 그 파일 이름의 규칙을 찾아서 그 규칙을 실행하여 파일을 만들게 됩니다.

```make
blah: blah.o
cc blah.o -o blah

blah.o: blah.c
    cc -c blah.c -o blah.o

blah.c:
    echo "int main() { return 0; }" > blah.c

clean:
    rm -f blah.o blah
```

이러한 `Makefile` 의 경우 `blah` 가 첫번째 규칙이므로 디폴트 규칙이 되죠. `make` 명령을 인자 없이 실행하면 `Makefile` 의 첫번째 규칙이 실행됩니다. 일반적으로 첫번째 규칙을 `all` 로 정하는 국룰이 있죠. 

또한 통상적으로 Makefile 에 있는 `clean` 규칙은 컴파일된 바이너리를 삭제하는 용도로 사용됩니다. 이 `clean` 규칙을 실행하기 위해서는 

```shell
$ make clean
```

와 같이 규칙 이름(`clean`) 을 `make` 의 파라미터로 전달하여 실행하면 됩니다. 반면 파라미터를 전달하지 않고 단지 `make` 로 실행하면 가장 첫번째 규칙이 실행되는 것이죠.

!!! note

    `cc` 도 `gcc` 같은 컴파일러입니다.

`make` 는 규칙의 파일이 이미 존재할 경우 `"up to date"` 메시지를 출력하고 규칙을 실행하지 않습니다. 

## PHONY

`make` 는 효율성을 위하여 `targets` 파일이 이미 존재하면 규칙을 실행하지 않습니다. 그런데 `clean` 이나 `all` 같은 규칙은 실제 파일 이름을 지칭하지 않죠. 만약 실수로 `all` 파일이나 `clean` 파일을 생성하였을 경우 `all` 이나 `clean` 규칙이 실행되지 않을 수도 있습니다. 이것을 방지하기 위하여 `.PHONY` 에 `targets` 을 명시하면 `make` 는 파일이 존재하는지 검사하지 않고 규칙을 무조건 실행합니다. 

- ==**`.PHONY` : `targets` 이 실제 파일 이름이 아니라는 것을 명시한다.**==

    - 또한 파일 존재 검사를 하지 않기 때문에 `.PHONY` 를 사용하면 `make` 의 성능이 향상된다. 

다음과 같이 `.PHONY` 규칙에 `clean` 을 명시하여 실제 파일 이름이 아니라는 것을 알려주세요. 그러면 `clean` 파일이 있어도 규칙이 항상 실행됩니다. 

```make
one:
    touch one
clean:
    rm -f one
.PHONY: 
    clean
```

!!! note

    이렇게 매우 간단하게 Makefile 에 대하여 알아보았습니다. 더 많은 Makefile 정보를 알고 싶다면 다음 링크들을 참고해주세요.

    https://makefiletutorial.com/

    https://ccss17.github.io/Computer/makefile/

# Bazel

Bazel 은 Google 에서 만든 빌드 시스템입니다. Bazel 의 특징은 매우 큰 프로젝트에 적합하다는 것이죠. 왜냐하면 Bazel 은 프로젝트에서 수정된 일부분만 컴파일하는 기능을 제공하기 때문입니다. 이 기능은 조금만 더 큰 프로젝트를 다루다보면 매우 큰 장점이라는 것을 알 수 있습니다. 디버깅을 위해서는 프로젝트를 빌드하고 프로그램이 잘 돌아가나 확인해야 하는데, 이 과정에서 컴파일을 매번 해야 합니다. 이때 컴파일 속도가 빨라지면 작업 효율이 매우 올라가고 시간 절약이 많이 되죠. 

그리고 Bazel 은 C/C++ 뿐만 아니라 Java, Android, iOS, Go 같은 다양한 언어도 컴파일할 수 있게 해주고, Linux/Windows/MacOS 와 같은 모든 플랫폼에서 사용가능합니다. 

!!! note

    하지만 Bazel 빌드 시스템에 대한 단점과 비판도 있기 때문에 무조건 Bazel 로 프로젝트를 빌드해야겠다고 생각할 필요는 없습니다. 여러 빌드 시스템의 장단점을 미루어보고 자신의 프로젝트에 적절한 빌드 시스템을 선정해야 합니다.

## Bazel Tutorial 

> 참고/출처 : https://docs.bazel.build/versions/4.0.0/tutorial/cpp.html

먼저 도커 컨테이너에서 Bazel Tutorial 레포지토리를 클론합니다.

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ git clone https://github.com/bazelbuild/examples
```

이 레포지토리를 보면 여러가지 튜토리얼들이 많은데 C++ 프로젝트를 Bazel 로 빌드하는 튜토리얼을 따라해보겠습니다. `examples/cpp-tutorial/stage1` 으로 이동해주세요.

이곳은 Bazel 빌드 시스템을 연습해볼 수 있는 간단한 프로젝트가 있는 레포지토리입니다. `ls` 명령어로 디렉토리를 확인해보면 `WORKSPACE` 라는 파일과 `main` 이라는 C++ 소스코드를 담고 있는 디렉토리가 있습니다. 그리고 `main` 디렉토리 안에는 `BUILD` 라는 파일도 있죠. 다음 명령어로 C++ 소스코드를 가볍게 살펴보세요. 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ cat main/hello-world.cc
```

그러면 이제 Bazel 로 C++ 프로젝트를 빌드하고 실행해봅시다. 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ bazel build //main:hello-world
```

이 명령어가 Bazel 을 통해서 C++ 프로젝트를 빌드한 것입니다. 컴파일된 실행 파일은 `bazel-bin/main` 에 저장됩니다. 이제 컴파일된 실행 파일을 실행해보죠.

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ ./bazel-bin/main/hello-world
Hello world
Wed Feb 10 20:40:12 2021
```

이제 Bazel 에 대하여 알아보겠습니다. 

- ==**`WORKSPACE` : Bazel 빌드 시스템으로 빌드될 프로젝트임을 알려주는 파일이다.**==

    - 이 파일은 프로젝트의 최상층(root)에 위치해야 한다.

- ==**`BUILD` : Bazel 빌드 시스템이 프로젝트를 어떻게 컴파일해야 하는지 알려주는 파일이다.**==

    - 이 파일은 프로젝트의 하위 디렉토리에 하나 이상 존재하며, 이 파일을 갖고 있는 디렉토리가 하나의 package 가 된다.

이 프로젝트의 `WORKSPACE` 파일은 빈 파일입니다. 이렇게 빈 파일의 `WORKSPACE` 만 만들어두어도 Bazel 이 Bazel 빌드 시스템으로 빌드될 프로젝트임을 인식할 수 있습니다. 

`main/BUILD` 파일은 `main` 이라는 package 가 어떻게 컴파일되어야 하는지 Bazel 에게 알려줍니다. 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ cat main/BUILD
load("@rules_cc//cc:defs.bzl", "cc_binary")

cc_binary(
    name = "hello-world",
    srcs = ["hello-world.cc"],
)
```

이 `BUILD` 파일은 `hello-world` 라는 타켓을 `hello-world.cc` 라는 C++ 소스코드로 컴파일 하는 규칙을 명시합니다. `cc_binary` 는 Bazel 의 내장 규칙인데 이것으로 C++ 프로그램을 컴파일 할 수 있습니다.

이렇게 `BUILD` 파일을 가볍게 알아보는 것으로 Bazel 빌드 시스템을 마무리하겠습니다. stage2, stage3 과 더 자세한 Bazel 사용법은 관심 있으신 분들만 

https://docs.bazel.build/versions/4.0.0/tutorial/cpp.html

이곳에서 더 알아보시면 됩니다.

# make with VSCode

VSCode 를 사용하면서 make 로 C++ 을 빌드하는 방법을 간단하게 살펴보겠습니다. 새폴더를 만드시고 다음과 같이 파일을 세팅해주세요.

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ touch main.cc
$ touch makefile
$ mkdir .vscode
$ touch .vscode/tasks.json
```

그리고 `main.cc` 라는 C++ 프로그램을 다음과 같이 간단하게 채워봅시다.

```cpp
#include <iostream>
int main(){
    std::cout << "make with vscode!" << std::endl;
    return 0;
}
```

`makefile` 은 다음과 같이 채워주세요.

```makefile
all:
	g++ main.cc
clean:
	rm a.out
```

마지막으로 `.vscode/tasks.json` 을 다음과 같이 채워주세요.

```json
{
    "tasks": [
        {
            "label": "make and run",
            "type": "shell",
            "command": "make clean ; make && ./a.out",
            "args": [
                // "arg1"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            }
        }
    ]
}
```

그리고 VSCode 에서 <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>B</kbd> 를 누르면 빌드가 됩니다. 빌드 스크립트가 지금

```shell
$ make clean ; make && ./a.out
```

이렇게 되어있습니다. 먼저 기존에 컴파일된 바이너리를 `make clean` 으로 삭제하고 `make` 를 통해 빌드를 한 후 컴파일된 바이너리를 `./a.out` 으로 실행합니다. `make clean` 과 `make` 를 `;` 으로 이어준 이유는 컴파일된 바이너리가 없을 경우 `make clean` 명령이 실패하기 때문입니다. 만약 `&&` 로 이어졌다면 `&&` 는 이전 명령어가 성공적으로 종료되어야만 다음 명령어를 실행하기 때문에 빌드에 실패하게 되죠. 그렇기 때문에 `;` 으로 이어준 것입니다.

Make 뿐만 아니라 Grunt, Gulp, MSBuild, Rake, Bazel, Flutter, Android, iOS 등등 다양한 Task 들을 VSCode 와 연동하여 사용할 수 있습니다. 더 자세한 내용은 

https://code.visualstudio.com/docs/editor/tasks#vscode

이 링크를 참고해주시면 됩니다. 이 가이드의 목적은 이런 것들이 있다 정도만 가볍게 알려드리는 것이고, 여러분이 앞으로 각자의 분야에서 필요한 것들을 찾아서 이런 식으로 사용할 수 있겠다는 아이디어만 전달해드릴 수 있다면 저는 충분하다고 생각합니다.

## rust with VSCode 

> 참고/출처 : https://stackoverflow.com/a/46885479/15266921

아쉬우니까 나중에 Rust 공부하시는 분들을 위하여 Rust 프로젝트를 빌드하고 실행하는 `tasks.json` 만 알려드리고 마무리하겠습니다. 

```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "cargo run",
            "type": "shell",
            "command": "cargo",
            "args": [
                "run",
                // "--release",
                // "--",
                // "arg1"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            }
        }
    ]
}
```

## **<div align="center"> 🌜 ️여기까지 Day5     🌜️ </div>**
