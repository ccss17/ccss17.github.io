# [ccss17.github.io](https://ccss17.github.io)

# Makefile Memo

## 튜토리얼 

- https://makefiletutorial.com/ : Command line arguments and override (Section 6.7)

- http://www.cs.colby.edu/maxwell/courses/tutorials/maketutor/

## 일반 규칙 

- `Makefile` 은 수 개의 규칙으로 구성되는데 규칙의 일반적 문법은 다음과 같다.

  ```make
  targets : prerequisites 
    command
    command
    command
    ...
  ```

  - `targets` : 규칙 이름으로써 공백으로 구분되는 파일 이름들이다. 만들어질 파일 이름을 뜻한다. 보통 규칙 당 하나의 파일만 있다. 

  - `commands` : `targets` 을 만드는 일련의 명령어들이다. 이 부분은 공백이 아닌 탭으로 시작되어야만 한다. 

  - `prerequisites` : 공백으로 구분되는 파일 이름들로써 `commands` 가 실행되기 위하여 필요한 의존성 파일 리스트를 뜻한다. 

    - **만약 이 파일들 중 하나가 존재하지 않는다면 먼저 그 파일 이름의 규칙을 찾아서 그 규칙을 실행하여 파일을 만든다.**

      ```make
      blah: blah.o
      cc blah.o -o blah
      
      blah.o: blah.c
        cc -c blah.c -o blah.o
      
      blah.c:
        echo "int main() { return 0; }" > blah.c
      
      clean:
        rm -f blah.o blah.c blah
      ```

      이러한 `Makefile` 의 경우 `blah` 가 첫번째 규칙이므로 디폴트 규칙이 된다. 

- `make` 명령을 인자 없이 실행하면 `Makefile` 의 첫번째 규칙이 실행된다. 일반적으로 첫번째 규칙을 `all` 로 정하는 국룰이 있다. 

- 통상적으로 `CC` 에 컴파일러를, `CFLAGS` 에 컴파일 옵션을 저장하여 규칙에 삽입한다. 

- `make` 는 규칙의 파일이 이미 존재할 경우 `"up to date"` 메시지를 출력하고 규칙을 실행하지 않는다. 

  - 예시

    ```make
    some_file:
      touch some_file
    ```

    처음 실행할 때는 규칙이 실행 되지만 한번 더 실행하면 규칙이 실행되지 않는다. 

## 축약규칙 

- 위 예제의 `Makefile` 은 다음과 같이 축약할 수 있다. 

```make
some_file:; touch some_file
```

## PHONY

- `.PHONY` : `targets` 이 실제 파일 이름이 아니라는 것을 명시한다.

  - `make` 는 효율성을 위하여 `targets` 파일이 이미 존재하면 규칙을 실행하지 않는다. 그런데 `clean` 이나 `all` 같은 규칙은 실제 파일 이름을 지칭하지 않는다. 만약 실수로 `all` 파일이나 `clean` 파일을 생성하였을 경우 `all` 이나 `clean` 규칙이 실행되지 않을 수도 있다. 이것을 방지하기 위하여 `.PHONY` 에 `targets` 을 명시하면 `make` 는 파일이 존재하는지 검사하지 않고 규칙을 무조건 실행한다. 

  - 또한 파일 존재 검사를 하지 않기 때문에 `.PHONY` 를 사용하면 `make` 의 성능이 향상된다. 

  - 예시

    ```make
    one:; touch one
    clean:; rm -f one
    ```

    위 예제의 `clean` 규칙은 파일 `one` 을 삭제하기로 되어있다. 그런데 만약 `clean` 이라는 이름을 가진 파일이 존재하면 `make clean` 으로 규칙을 실행한다 해도 `make: 'clean' is up to date.` 라는 메세지가 출력되고 규칙이 실행되지 않는다. 

    ```make
    one:; touch one
    clean:; rm -f one
    .PHONY: clean
    ```

    따라서 `.PHONY` 에 `clean` 을 명시하여 실제 파일 이름이 아니라는 것을 명시해준다. 그러면 `clean` 파일이 있어도 규칙이 항상 실행된다. 

## 변수 

- 문자열을 변수에 저장하고 `${}` 나 `$()` 로 사용할 수 있다.

  - 예시

    ```make
    files = file1 file2
    some_file: $(files)
      echo "Look at this variable: " $(files)
      touch some_file
    
    file1:
      touch file1
    file2:
      touch file2
    
    clean:
      rm -f file1 file2 some_file
    ```

### 변수 할당 

- `var = value` : 지연된 할당으로써 변수가 사용될 때 그 값들이 재귀적으로 할당된다. 

  - 예시
    
    ```make
    foo = $(bar)
    bar = $(ugh)
    ugh = Huh?

    all:;echo $(foo)
    ```

    이때 `foo` 에 할당되는 `bar` 는 `foo` 가 선언되는 시점에서 정의되지 않았기 때문에 컴파일 에러가 날 것 같다. 하지만 `=` 는 지연된 할당으로서 `foo` 가 실질적으로 사용될 때 참조된 모든 변수들을 재귀적으로 찾아가며 할당한다. 

- `var := value` : 즉시 할당으로써 변수가 선언될 때 그 값들이 재귀적으로 할당된다. 

  - 예시

    ```make
    foo := $(bar)
    bar := $(ugh)
    ugh := Huh?

    all:;echo $(foo)
    ```

    이전 예제와는 달리 이 코드는 아무것도 출력하지 않는다. `foo` 가 선언되는 시점에서 `bar` 는 정의되지 않았기 때문이다. 

    ```make
    ugh := Huh?
    bar := $(ugh)
    foo := $(bar)

    all:;echo $(foo)
    ```

    즉시 할당된 변수를 제대로 출력되게 하기 위해서는 위와 같이 선언 순서를 바꾸어 주어야 한다. 즉시 할당과 지연 할당을 섞어서 쓰면 다음과 같이 순서를 배치하는 것 또한 가능하다. 

    ```make
    bar = $(ugh)
    ugh := Huh?
    foo := $(bar)

    all:;echo $(foo)
    ```

    이렇게 해도 된다. 

    ```make
    foo = $(bar)
    ugh := Huh?
    bar := $(ugh)

    all:;echo $(foo)
    ```
  
  - 예시

    ```make
    one = one ${later_variable}
    two := two ${later_variable}

    later_variable = later

    .PHONY: all
    all: 
      echo $(one)
      echo $(two)
    ```

    위 예시에서 `one` 에는 `later_variable` 이 할당되지만 `two` 는 `:=` 으로 즉시할당을 사용했기 때문에 `later_variable` 이 할당되지 않는다. 

- `var ?= value` : 만약 `var` 이 할당되어 있지 않으면 `value` 로 할당한다. 

  - 예시

    ```make
    one = hello
    one ?= will not be set
    two ?= will be set

    .PHONY: all
    all: 
      echo $(one)
      echo $(two)
    ```

    위 예시에서 `?=` 로 `one` 과 `two` 를 할당하는데 `two` 만 할당된다. 

- 변수 확장 : 단순히 변수를 이어붙히는 것으로 변수 확장을 할 수 있다. 

  - 예시

    ```make
    one = hello
    one := ${one} there
    all: 
      echo $(one)
    ```

    위 예시에서 즉시할당 `:=` 를 지연할당 `=` 으로 바꾼다면 무한루프 에러가 발생한다. 

- `+=` 변수 확장 : `+=` 연산자로도 변수 확장을 할 수 있다. 

  - 예시

    ```make
    one = hello
    one += there
    all: 
      echo $(one)
    ```

    위 예시는 `hello there` 를 출력한다. 

- 할당되지 않은 변수 : 할당되지 않은 변수를 다른 변수에 할당하면 스페이스 하나가 할당된다. 

  - 예시

    ```make
    with_spaces = hello   # with_spaces has many spaces after "hello"                    
    after = $(with_spaces)there

    nullstring =                              
    space = $(nullstring) # Make a variable with a single space.

    .PHONY: all 
    all: 
        @echo "$(after)"
        @echo start"$(nullstring)"end
        @echo start"$(space)"end
    ```

    위 예시의 출력은 다음과 같다. 

    ```shell
    $ make
    hello   there
    startend
    start end
    ```

- 변수 치환 : `$(var:a=b)` 로 변수 `var` 의 `a` 가 `b` 로 치환된다.

  - 예시

    ```make
    foo := a.o b.o c.o
    bar := $(foo:.o=.c)
    all: ; echo $(bar)
    ```

    위 예시는 `a.c b.c c.c` 를 출력한다. 

- 패턴 변수 치환 : `%` 를 사용한 패턴을 포함하여 변수 치환을 할 수도 있다. 

  - 예시

    ```make
    foo := a.o b.o c.c
    bar := $(foo:%.o=%)
    all: ; echo $(bar)
    ```

    위 예시는 `a b c.c` 를 출력한다. 


## 함축 규칙 

- `Makefile` 은 다음과 같이 함축 규칙을 지원한다. 

  ```make
  # blah.o 규칙 안에 주석을 달면 함축 규칙이 실행되지 않는다. 
  # Implicit command of: "cc blah.o -o blah"
  blah:
  
  # Implicit command of: "cc -c blah.c -o blah.o"
  blah.o:
  
  blah.c:
  	echo "int main() { return 0; }" > blah.c
  
  clean:
  	rm -f blah.o blah blah.c
  ```

## 특수 문자 

- 와일드카드 `*` : 와일드카드 `*` 는 `targets`, `prerequisites`, `commands` 에서 사용 가능하다.

  ```make 
  some_file: *.c
	# create the binary
  
  *.c:
  	touch f1.c
  	touch f2.c
   
  clean:
  	rm -f *.c
  ```

  - 이 `Makefile` 은 `.c` 파일이 단 하나라도 있으면 `*.c` 규칙이 실행되지 않는다. 와일드카드 `*` 는 어떤 문자열이라도 해당되기에 `make` 가 `*.c` 라는 의존성이 해결 된 것으로 판단하기 때문이다. 

- 와일드카드 `*` 함수 : 와일드카드 `*` 를 `targets`, `prerequisites`, `commands` 에서밖에 사용하지 못하기 때문에 변수할당이나 함수인자 전달 시에는 와일드카드 함수를 사용해야 한다. 

  ```make
  wrong = *.o # Wrong
  objects := $(wildcard *.c) # Right

  some_binary: 
      touch f1.c
      touch f2.c
      echo $(wrong)
      echo $(objects)

  clean:
      rm -f *.c
  ```

- `%` 는 모든 파일 이름을 뜻한다.

  - `%.c` 라고 하면 모든 `.c` 파일을 뜻한다. 

- `$@` 는 규칙의 `:` 왼쪽 부분이다. 

- `$<` 는 규칙의 `:` 오른쪽 부분의 첫번째 아이템이다. 

- `$^` 는 규칙의 `:` 오른쪽 부분이다. 

## 다중 타겟

- `targets` 에 여러 파일이 선언되어 사용할 수도 있다. 

  - 예시

    ```make
    all: f1.o f2.o
    f1.o f2.o:
      echo $@
    ```

    위 예시에서 규칙 `all` 에서 `f1.o` 와 `f2.o` 를 지정하였는데 각각 `f1.o f2.o` 규칙을 실행하게 된다. 이때 실행 명령 `echo $@` 의 `$@` 에는 각각 맥락에 따라 `f1.o` 와 `f2.o` 가 대입된다. 

- `targets` 에 와일드카드 `%` 로 일반적인 파일을 선언하여 사용할 수 있다. 

  - 예시

    ```make
    all: f1.o f2.o
    %.o:
      echo $@
    ```

    이 경우 `%.o` 규칙으로 인해 `.o` 확장자를 가진 모든 파일이 이 규칙으로 생성된다. 

    ```make
    all: f1.o f2.o
    %.o:
      echo $@
    f1.o:
      echo TEST
    ```

    하지만 위와 같이 `f1.o` 의 규칙을 따로 지정해줄 경우 `f1.o` 를 생성할 때 `make` 는 `%.o` 규칙이 아니라 `f1.o` 규칙을 실행한다. 

## vpath 

- `vpath` : `prerequisites` 를 찾는 경로를 현재 디렉토리와 더불어서 추가한다. 

  - 기본적으로 `make` 는 `prerequisites` 를 현재 디렉토리에서 찾는다. 그런데 `vpath` 로 특정 `prerequisites` 의 탐색경로를 현재 디렉토리에 더불어서 추가할 수 있다. 
  
  - 형식 : `vpath <pattern> <directories, space/colon seperated>`

  - `<pattern>` 에서 특수문자 `%` 를 사용할 수 있다. 

  - `VPATH` 환경변수에도 경로를 추가하여 사용할 수 있다.

  - 예시 

    ```make
    vpath %.h ../headers ../other-directory

    some_binary: ../headers blah.h
      touch some_binary

    ../headers:
      mkdir ../headers

    blah.h:
      touch ../headers/blah.h
    ```

    위 예시의 `vpath` 때문에 `.h` 확장자를 가진 파일을 현재 디렉토리 뿐만 아니라 `../headers` 디렉토리와 `../other-directory` 에서도 찾는다. 이에 따라 만약 `vpath` 가 포함된 라인을 지우고 `make` 를 실행해보면 파일 `blah.h` 를 찾지 못하여 규칙 `blah.h:` 를 항상 실행하게 된다.
  
## Static Pattern Rules

- static pattern : 패턴에 맞는 `targets` 을 자동으로 `prerequisites` 으로 변환해주는 규칙이다.

  - `targets ...: target-pattern: prereq-patterns ...` 의 형식으로 사용된다. `target-pattern` 에 매칭된 `target` 을 `prereq-pattern` 으로 변환해준다.

  - 예시

    ```make
    objects = foo.o bar.o
    $(objects): %.o: %.c
      echo "Call gcc to generate $@ from $<"
    ```

    위 규칙은 다음의 규칙과 동일하다.

    ```make
    foo.o: foo.c
      echo "Call gcc to generate $@ from $<"

    bar.o: bar.c
      echo "Call gcc to generate bar.o from bar.c"
    ```

## Static Pattern Rules and Filter

- static pattern with Filter : static pattern 의 `targets` 을 패턴으로 필터링해서 매칭되지 않는 `target` 은 규칙에 적용시키지 않는 규칙이다. 

  - 예시

    ```make
    objects = foo.o bar.o f1.c
    $(objects): %.o: %.c
      echo "Call gcc to generate $@ from $<"
    ```

    위 규칙에서 `f1.c` 는 분명 static pattern 에 해당되지 않는 예외이다. 이 규칙은 다음의 규칙과 동일한 기능을 하게 된다. 

    ```make
    foo.o: foo.c
      echo "Call gcc to generate $@ from $<"

    bar.o: bar.c
      echo "Call gcc to generate bar.o from bar.c"

    f1.c:
      echo "Call gcc to generate f1.c from"
    ```

    따라서 이러한 예외는 규칙에 적용시키지 않기 위하여 다음과 같이 필터링을 걸 수 있다. 

    ```make
    objects = foo.o bar.o f1.c
    $(filter %.o $(objects)): %.o: %.c
      echo "Call gcc to generate $@ from $<"
    ```

    위 규칙은 `objects` 에서 `.o` 로 끝나는 파일만 규칙에 적용시킨다. 

## Double-Colon

- Double-Colon : (이 규칙은 흔히 쓰이지 않음) Double-Colon 으로 시작되는 규칙이 여러번 정의되어도 그것들을 모두 실행하게 해준다. 

  - 예시 

    ```make
    all: blah
    blah::
      echo "hello"
    blah::
      echo "hello again"
    ```

    위 규칙에서 `blah` 가 Double-Colon 으로 시작되는데 Single-Colon 으로 바꾸면 에러가 발생하면서 마지막 규칙만 실행된다. 

# 명령 실행 관련 

## Command Echoing/Silencing

- Command Echoing/Silencing : 명령어 앞에 `@` 를 붙히면 명령어가 출력되지 않는다. 

  - `make -s` 로 실행하면 모든 명령어에 `@` 를 붙혀서 실행한 효과를 얻을 수 있다. 

  - 예시 

    ```make
    all: 
      @echo "hello"
      echo "hello again"
    ```

    위 예시의 출력은 다음과 같다. 
    
    ```shell
    $ make
    hello
    echo "hello again"
    hello again
    ```

## Command Execution

- Command Execution : 각각의 명령어는 항상 새로운 쉘에서 실행되는 것과 같다. 

  - 따라서 `make` 에서 명령어들을 실행하기 위하여 보통 `; \` 로 명령어를 이어준다. 

  - 예시

    ```make
    all: 
      cd ..
      echo `pwd`
      cd ..;echo `pwd`
      cd ..; \
      echo `pwd`
    ```

    위 예시의 출력은 다음과 같다. 

    ```shell
    $ make
    cd ..
    echo `pwd`
    /home/ccsss/repo/csrepo/ccss17.github.io/maketest
    cd ..;echo `pwd`
    /home/ccsss/repo/csrepo/ccss17.github.io
    cd ..; \
    echo `pwd`
    /home/ccsss/repo/csrepo/ccss17.github.io
    ```

## Default Shell

- Default Shell : `make` 가 명령어를 실행하는 기본 쉘은 `/bin/sh` 인데 `SHELL` 변수를 바꿈으로써 기본 쉘을 변경할 수 있다. 

  - 예시

    ```make
    all:
      echo "current shell: $$0"
    ```

    위 예시가 `/bin/sh` 을 출력하는데 비해 다음 예시는 `/bin/bash` 를 출력한다. 

    ```make
    SHELL=/bin/bash
    all:
      echo "current shell: $$0"
    ```

## DELETE_ON_ERROR

- `DELETE_ON_ERROR` : `make` 는 규칙이 `nonzero` 종료 코드를 반환하면 전체 실행을 중단하는데, `.DELETE_ON_ERROR` 가 설정되면 이때 `nonzero` 반환값을 반환한 규칙의 `target` 파일을 삭제한다. 

  - 대부분의 경우에 `.DELETE_ON_ERROR` 를 설정하는 것이 좋다. 

  - 예시

    ```make
    all: one

    one:
      touch one
      false
    ```

    위 예시는 `false` 가 `nonzero` 종료코드를 반환하기에 전체실행이 중단되지만 파일 `one` 이 사라지지 않는다. 하지만 다음 예시는 파일 `one` 이 자동으로 삭제된다. 

    ```make
    .DELETE_ON_ERROR
    all: one

    one:
      touch one
      false
    ```
  
## 에러 처리 

- `-k` 옵션 : `make` 를 이 옵션으로 실행하면 에러가 발생해도 실행을 중단하지 않고 끝까지 실행한다.

  - 모든 에러를 한번에 확인하고 싶을 때 유용하다.

- `-i` 옵션 : `make` 를 이 옵션으로 실행하면 모든 에러를 무시한다. 

  - 예시 

    ```make
    .DELETE_ON_ERROR:
    all: one 
    
    one:
        touch one
        false
        touch one-post
    ```

    위 예시를 `make -k` 로 실행하면 파일 `one` 생성되었다가 `false` 에서 전체 실행이 중단되고 `one` 이 삭제된다.

    반면 `make -i` 로 실행하면 `false` 가 반환하는 `nonzero` 리턴값을 무시하고 파일 `one` 과 파일 `one-post` 가 생성된다.

- `-` : 명령어 앞에 `-` 를 붙히면 `nonzero` 종료코드가 반환되어도 전체 실행이 중단되지 않고 무시된다.

  - 예시

    ```make
    one:
        -false
        touch one
    ```

    위 예시에서 에러가 무시되고 파일 `one` 이 잘 실행된다. 

# Recursive make 

- `make -C <directory>` : `<directory>` 를 `make` 한다. 

  - 예시 

    ```make
    new_contents = "hello:;touch inside_file"                                            
    all:
        mkdir -p subdir
        echo $(new_contents) > subdir/makefile
        make -C subdir
    ```

    위 예시는 `subdir` 디렉토리를 만들고 `subdir/makefile` 을 `make` 한다. 

- `export <variable>` : 재귀적으로 호출된 하위 `make` 에서 상위 `make` 의 변수를 사용할 수 있게 한다. 

  - 예시

    ```make
    new_contents = "hello:;echo \$$(cooly)"

    all:
        mkdir -p subdir
        echo $(new_contents) | sed -e 's/^ //' > subdir/makefile
        make -C subdir
    cooly = "The subdirectory can see me!"
    export cooly
    ```

    위 예시의 `export cooly` 로 생성된 `subdir/makefile` 에서 `cooly` 변수를 사용할 수 있게 된다.

- `EXPORT_ALL_VARIABLES` : `.EXPORT_ALL_VARIABLES:` 를 선언하면 모든 변수가 `export` 된다. 

  - 예시 

    ```make
    .EXPORT_ALL_VARIABLES:
    new_contents = "hello:\n\techo \$$(cooly)"

    cooly = "The subdirectory can see me!"
    # This would nullify the line above: unexport cooly

    all:
      mkdir -p subdir
      echo $(new_contents) | sed -e 's/^ //' > subdir/makefile
      @echo "---MAKEFILE CONTENTS---"
      @cd subdir && cat makefile
      @echo "---END MAKEFILE CONTENTS---"
      cd subdir && $(MAKE)
    ```