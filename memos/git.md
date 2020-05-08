# [ccss17.github.io](https://ccss17.github.io)

# git 메모 

https://git-scm.com/book/en/v2

# Version Control

VCS(Version Control System) 이란 파일의 변화를 추적하여 기록하는 프로그램이다. 이것을 사용하면 몇 가지 장점이 있는데 파일들을 버전으로 관리하여 복원할 때 편리하고 버전들을 쉽게 비교할 수 있다는 것이다. 

# git 

- 여러 VCS 프로그램이 있지만 git 이 그것들과 다른 점이 있다.

  - 여타 VCS 는 버전을 관리할 때 파일이 변경된 것을 중심으로 기록한다. 

  - 하지만 git 은 그 프로젝트 전체 파일의 스냅샷으로 버전을 관리한다. 물론 파일이 동일할 경우 이전 스냅샷에 단지 연결함으로써 용량을 아낀다! 

## git 이 파일을 관리하는 세 가지 상태

- git 은 다음 상태로 파일을 관리한다. 

  - untracked 상태 : `git` 이 변경사항을 추적하지 않는 파일이다.

  - modified 상태 : 파일을 변경했지만 아직 스테이징되지 않은 상태이다.

  - staged 상태 : 변경된 파일을 커밋이 될 리스트에 포함시킨 상태이다.

  - commited 상태 : `git` 데이터베이스에 하나의 버전으로 저장된 상태이다.

## git 프로젝트의 세 가지 영역 

- 이 세 가지 상태는 프로젝트를 working tree, staging area, git database 라는 세 가지 영역으로 나눈다. 

![](https://git-scm.com/book/en/v2/images/areas.png)

  - working tree : 프로젝트의 특정 버전의 파일들이 있는 영역이다. 
  
    - 최신 버전일 수도 있고 git database 에서 옛날 버전을 가져온 것일 수도 있다. 

  - staging area : 다음 버전, 즉 다음 커밋이 예정된 파일들이 있는 영역이다. 

  - git database : 프로젝트의 모든 버전을 데이터베이스로 관리하는 영역이다.
  
    - .git 디렉토리에 저장되어 있다. 

## git 프로젝트 기본 작업 흐름

1. working tree 의 파일을 수정한다.

2. 수정된 파일들 중 커밋하고 싶은 파일을 staging area 에 포함한다. 

3. 커밋하여 git database 에 스냅샷으로 남긴다. 또 하나의 버전을 생선한 것이다. 

# git 사용법 

## 설치 후 초기 설정 

git 을 설치한 후 가장 먼저 `user.name` 과 `user.email` 을 설정해주어야 한다. 커밋할 때 매번 이 정보가 사용되어야 하기 때문이다. 

```shell
git config --global user.name "NAME"
git config --global user.email "EMAIL"
```

- `git config --list` : 설정들을 확인한다. 

---

# 레포지토리 관리 

### 레포지토리 생성 

- `git init` : 레포지토리를 `git` 프로젝트로 초기화한다. 

  - 예시

    ```shell
    cd /path/to/my_project
    git init
    ```

### 파일 staging 하기

파일을 staging 영역에 올리는 것을 "staging 한다" 고 한다.

- `git add <file>` : 파일을 git 이 추적하도록 한다.

  - 파일 수정이 모두 끝났을 때 staging 해서 커밋 예정 리스트에 등록하는 것이다. 

  - 예시

    ```shell
    git add readme.md
    git add *.c
    ```

### 커밋 하기 

- `git commit -m 'init'` : 커밋을 하여 staging 된 파일들의 스냅샷을 찍고 데이터베이스에 하나의 버전으로 저장한다. 

- `git commit -a -m 'init'` : `-a` 옵션에 따라 `git` 이 스테이징 과정을 건너뛰고 모든 파일을 커밋한다. 

### 추적 금지하기 

- `.gitignore` : 이 파일에 파일 이름을 넣으면 `git` 이 변경사항을 더 이상 추적하지 않는다. 

- 예시 

  ```shell
  # ignore all .a files
  *.a
  # but do track lib.a, even though you're ignoring .a files above
  !lib.a
  # only ignore the TODO file in the current directory, not subdir/TODO
  /TODO
  # ignore all files in any directory named build
  build/
  # ignore doc/notes.txt, but not doc/server/arch.txt
  doc/*.txt
  # ignore all .pdf files in the doc/ directory and any of its subdirectories
  doc/**/*.pdf
  ```

## 파일 삭제 

- `git rm <file>` : 파일을 삭제하고 파일의 삭제를 스테이징한다. 

  -  스테이징된 파일을 삭제하려면 다음 명령어를 입력해야 한다. 

- `git rm -f <file>` : 스테이징된 파일을 삭제하고 로컬에서도 삭제한다. 

- `git rm --cached <file>` : 스테이징된 파일을 삭제한다. 로컬에서 삭제하지는 않는다. 

---

# 레포지토리 분석

### 레포지토리 상태 보기 

- `git status` : 파일들이 추적되고 있는지 추적되고 있지 않은지, 또는 커밋이 된 상태인지를 볼 수 있다. 

- `git status -s` : 상태를 간단히 출력한다. 

## 변경 사항 비교하기 

- `git diff` : 아직 스테이징 되지 않은 파일의 변경사항을 마지막 커밋과 비교하여 출력한다. 

- `git diff --staged` : 스테이징된 파일의 변경사항을 마지막 커밋과 비교하여 출력한다. 

- `git diff --cached` : `git diff --staged` 와 동일하다. 

## 커밋 기록 보기 

- `git log` : 커멋 기록을 출력한다.

  - `git log -2` : 커멋 기록을 2개만 출력한다.

- `git log -p` : 변경 사항도 출력하면서 커멋 기록을 출력한다.

  - `git log -p -2` : 변경 사항도 출력하면서 커멋 기록을 2개만 출력한다.

- `git log --stat` : 변경 사항을 간략히 출력하면서 커멋 기록을 출력한다.

- `git log --pretty=oneline` : 커멋 기록을 한줄로 출력한다.

  - `--graph` 와 함께 쓰여 `merge` 기록을 한 눈에 살펴보기 편하다. 

- `git log --since=<dat>` : 지난 2주간의 커밋 기록을 출력한다. 

  - `git log --since=2.weeks` : 지난 2주간의 커밋 기록을 출력한다. 

  - `git log --since=2008-1-15` : 2008 년 1월 15부터의 커밋 기록을 출력한다. 

- `git log -S <string>` : `<string>` 이 레포지토리에 추가되거나 삭제된 커밋 기록을 출력한다. 

  - 어떤 함수나 클래스가 추가되고 삭제된 기록을 살펴볼 때 편하다. 

---

# 원격 레포지토리 

### 원격 레포지토리 가져오기 

- `git clone <URL>` : 원격 레포지토리를 가져오기 위하여 다음 명령어를 입력한다. 

  - 예시 
  
    `git clone https://github.com/libgit2/libgit2`

  - `git` 은 `https` 프로토콜 뿐만 아니라 다음과 같이 `ssh` 프로토콜도 지원한다. 

    ```shell
    git clone git://user@server:path/to/repo.git
    ```

### 원격 레포지토리 리스트 관리

- `git remote -v` : 원격 레포지토리들을 본다. 

  - 예시  
  
    다음의 출력 결과를 보자. 이 중 어느 곳에서부터든지 프로젝트를 업데이트 할 수 있다.

    ```shell
    $ git remote -v
    bakkdoor  https://github.com/bakkdoor/grit (fetch)
    bakkdoor  https://github.com/bakkdoor/grit (push)
    cho45     https://github.com/cho45/grit (fetch)
    cho45     https://github.com/cho45/grit (push)
    defunkt   https://github.com/defunkt/grit (fetch)
    defunkt   https://github.com/defunkt/grit (push)
    koke      git://github.com/koke/grit.git (fetch)
    koke      git://github.com/koke/grit.git (push)
    origin    git@github.com:mojombo/grit.git (fetch)
    origin    git@github.com:mojombo/grit.git (push)
    ```

- `git remote show <remote>` : 특정 원격 레포지토리들을 본다. 

  - 예시 
  
    `git remote show origin` 

- `git remote add <shortname> <url>` : 원격 레포지토리를 추가한다. 

  - 예시 
  
    `git remote add pb https://github.com/paulboone/ticgit`

- `git remote remove <remote>` : 원격 레포지토리를 삭제한다. 

  - `git remote rm` 으로도 삭제할 수 있다. 

  - 예시 
    
    `git remote remove paul`

- `git remote rename <remote> <new>` : 원격 레포지토리의 이름을 바꾼다. 

  - 예시 
  
    `git remote rename pb paul`

### 원격 레포지토리로부터 업데이트하기 

- `git fetch <remote>` : 원격 레포지토리의 변경사항을 가져온다. 

  - `git fetch` 는 원격 레포지토리의 데이터를 가져오기는 하지만 프로젝트를 업데이트하지는 않는다. 따라서 프로그래머가 스스로 가져온 내용을 병합해야 한다. 

  - 예시 
  
    `git fetch pb`

- `git pull <remote> <branch>` : 원격 레포지토리의 변경사항을 가져온 후 자동으로 병합한다. 

  - 예시 
  
    `git pull origin master`

### 원격 레포지토리를 업데이트하기 

- `git push <remote> <branch>` : 원격 레포지토리로 변경사항을 업데이트한다. 

  - 만약 A 와 B 가 원격 레포지토리를 동시에 `clone` 하고 A 가 변경사항을 `push` 했다고 하자. 그러면 B 는 곧 바로 `push` 하지 못한다. B 는 먼저 A 가 업데이트 한 내용을 `fetch` 하고 병합한 후에야 `push` 할 수 있다. 

  - 예시 
  
    `git push origin master`

---

# 복원하기 

**이 명령어들은 `git` 이 재복원을 지원하지 않는 몇 안되는 기능들이니 아주 조심히 사용해야 한다. 더 이상의 재복원은 없다.**

### 마지막 커밋 수정하기 

- `git commit --amend` : 스테이징된 파일을 마지막 커밋에 포함시킨다. 

  - 만약 스테이징된 파일이 없다면 단순히 마지막 커밋 메시지를 수정하게 되는 것이다.

### 스테이징된 파일을 내리기 

- `git reset HEAD <file>` : 스테이징된 파일을 언스테이징한다. 

  - 만약 스테이징된 파일이 없다면 단순히 마지막 커밋 메시지를 수정하게 되는 것이다.

### 파일 복원하기 

- `git restore <file>` : 스테이징되지 않은 변경된 파일을 마지막 커밋 버전으로 복원한다. 

  - 스테이징 된 파일은 먼저 `git restore --staged <file>` 로 언스테이징을 한 후에야 복원할 수 있다. 

  - `git checkout -- <file>` 과 동일하다. 

---

# Tagging

`git` 특정 커밋에 태그를 부여해서 릴리즈 포인트를 정한다. 

- `git tag` : 모든 태그를 출력한다. 

  - `git tag -l "v1.8.5*` : `1.8.5` 버전의 모든 하위 버전을 출력한다. 

## 태그 생성 

`git` 은 `lightweight` 태그와 `annotated` 태그를 지원한다. `lightweight` 는 단순히 특정 커밋을 가르키는 포인터 역할을 하지만, `annotated` 태그는 태그 이름, 이메일, 태그 메시지 등을 포함하며 GPG 로 사인되어 커밋 오브젝트에 포함된다.

일반적으로 `annotated` 태그를 다는 것이 좋다. 하지만 임시적인 태그를 달거나 별도의 이유로 추가 정보를 저장하기 싫다면 `lightweight` 도 써도 좋다. 

### 마지막 커밋에 annotated 태그 부여 

- `git tag -a <VERSION> -m "MESSAGE"` : 마지막 커밋에 `annotated` 태그를 생성한다. 

  - `-a` 에 버전을 명시한다. 

  - `-m` 에 태그 메시지를 전달한다. 

  - 예시 
  
    `git tag -a v1.4 -m "my version 1.4"`

- `git show v1.4` : `1.4` 태그의 정보와 그것에 딸린 커밋 정보를 본다. 

### 마지막 커밋에 lightweight 태그 부여 

- `git tag <VERSION>` : 마지막 커밋에 `lightweight` 태그를 생성한다. 

  - `lightweight` 태그는 단지 커밋의 해쉬값만 저장한다. 

  - 예시 
  
    `git tag v1.4-lw`

  - `git show v1.4-lw` 로 태그 정보를 보면 커밋 해쉬만 볼 수 있다. 

### 특정 커밋에 lightweight 태그 부여 

- `git tag -a <VERSION> <COMMIT>` : 특정 커밋에 `annotated` 태그를 생성한다. 

  - 커밋의 해쉬를 특정할 수 있을만큼 헥사값을 전달하면 된다. 

  - 예시  
  
    `git tag -a v1.2 9fceb02`

### 특정 버전의 레포지토리 살펴보기 

- `git checkout <VERSION>` : 특정 버전일 때의 시점으로 레포지토리를 바꾼다. 

  - 예시 
  
    `git checkout 2.0.0`
  
  - 만약 특정 버전으로 되돌아가서 어떤 버그를 수정하고 커밋을 한다면, 그 커밋이 해당 태그를 바꾸는 것이 아니다. 그 커밋은 어떤 브랜치에도 속하지 않은 동떨어진 상태이다. 일반적으로 이런 경우에 다음의 명령어로 새로운 브랜치를 만들게 된다. 

    ```shell
    git checkout -b version2 v2.0.0
    ```

### 원격 레포지토리에 태그 공유 

`git push` 는 원격 레포에 태그까지 공유해주지는 않는다. 따라서 명시적으로 태그를 `push` 해주어야 한다. 

- `git push origin <VERSION>` : 특정 태그를 원격 레포에 푸쉬한다. 

  - 예시 
  
    `git push origin v1.5`

- `git push origin --tags` : 원격 레포에는 없는 모든 버전을 푸쉬한다.

  - 푸쉬할 태그가 너무 많을 때 유용한다. 

### 원격 레포지토리에 태그 공유 

- `git tag -d <VERSION>` : 특정 태그를 삭제한다. 

  - 예시 
   
    `git tag -d v1.4-lw` : 특정 태그를 삭제한다. 

  - 그러나 원격 레포의 태그까지 삭제하지는 않는다. 

- `git push origin --delete <VERSION>` : 원격 레포의 특정 태그를 삭제한다. 

---

# Branching 

프로젝트를 개발할 때 확실하게 정해진 파일들을 수정하지 않은 채 개발적이고 실험적인 내용들을 추가하며 파일들을 수정해야 한다. 그런데 이 작업은 매우 귀찮다. 원본 프로젝트를 복사하여 훼손되지 않도록 백업한 후 복사본을 고치는 과정을 반복해야 하기 때문이다. 

이 작업을 자동화해주기 위하여 `git` 은 브랜치 기능을 제공한다. `git` 은 메인 프로젝트를 곧 바로 수정하지 말고 브랜치를 만들어서 실험적이고 개발적인 아이디어를 반영한 후 메인 프로젝트로 병합하라고 권장한다. 즉 **브랜치를 만들고 병합하는 작업 과정을 자주 하라고 권장하는 것이다.**

`git` 이 제공하는 브랜치 기능을 잘 이해하면 당신의 개발 과정이 아주 강력하고 안정적으로 완전히 변할 것이다. 

## About Git Branching

먼저 `git` 이 다른 VCS 와는 달리 각각의 커밋들을 파일의 변경기록으로 저장하는 것이 아니라 레포지토리의 전체 스냅샷으로 저장하는 것을 기억하자. 당신이 커밋을 하면 커밋 오브젝트는 스테이징된 파일들, 커미터의 이름과 이메일, 그리고 부모 커밋들을 포인팅 한다. 

스테이징된 파일들 각각의 체크섬 해쉬값이 커밋에 저장되는데 이것을 `blobs` 오브젝트라 한다. 또한 `git` 은 디렉토리들의 체크섬을 계산하여 그 해쉬값을 `tree` 오브젝트로 저장한다. `tree` 오브젝트는 그 디렉토리에 저장되어있는 `blobs` 들의 리스트 정보를 지니고 있는 것이다. 그러면 `git` 은 최종적으로 메타데이터(날짜, 작성자 등)와 루트 디렉토리의 `tree` 오브젝트를 가르키는 `commit` 오브젝트를 만들며 커밋을 완료한다. 이 `commit` 오브젝트가 지금까지 해오던 커밋의 실체인 것이다. 

## 예시 

만약 3 개의 파일을 만든 후 스테이징 하고 커밋했다고 하자. 그러면 이 시점에서 5 개의 오브젝트가 생성된다. 3 개의 `blobs` 오브젝트와 루트 디렉토리를 가르키는 1 개의 `tree` 오브젝트, 그리고 1 개의 `commit` 오브젝트가 그것이다. 다음 그림이 지금 상황을 시각적으로 보여준다. 

![](https://git-scm.com/book/en/v2/images/commit-and-tree.png)

그리고 변경사항을 커밋할 때마다 커밋은 부모 커밋, 즉 이전 커밋을 다음과 같이 포인팅한다.

![](https://git-scm.com/book/en/v2/images/commits-and-parents.png)

`git` 은 `master` 라는 기본 브랜치를 갖고 있다. `master` 브랜치는 항상 마지막 커밋을 포인팅한다. 즉 커밋을 할 때마다 자동으로 마지막 커밋으로 포인팅을 변경해주는 것이다. 

## 브랜치 생성 

`branch` 를 생성한다는 것은 새로운 포인터를 만든다는 것이다. 

- `git branch <name>` : 새로운 브랜치를 만든다. 

  - 예시 
  
    `git branch testing` 현재 커밋에 `testing` 이라는 새로운 포인터를 만든다. 
  
  - 이제 현재 커밋에는 `master` 와 `testing` 이 포인팅하고 있는 것이다.

![](https://git-scm.com/book/en/v2/images/two-branches.png)

그런데 지금 내가 어떤 브랜치에 있는지 어떻게 알 수 있을까? `HEAD` 라는 특별한 포인터로 알 수 있다. 

- `HEAD` : 현재 상주하고 있는 브랜치를 가르키는 포인터이다. 

  - 지금 `HEAD` 는 아직 `matser` 를 가르키고 있다. 

![](https://git-scm.com/book/en/v2/images/head-to-master.png)

- `git log --oneline --decorate` : 현재 어떤 브랜치에 상주하고 있는지 확인한다. 

## 브랜치 이주 

- `git checkout <name>` : 브랜치를 이주한다. 

  - 예시 
  
    `git checkout testing` 는 `testing` 브랜치로 이주하게 한다. 즉 `HEAD` 가 `testing` 를 포인팅하게 하는 것이다. 

- `git checkout -b <name>` : 브랜치를 생성하면서 이주한다. 

  - 일반적으로 이 형태가 자주 쓰인다. 

![](https://git-scm.com/book/en/v2/images/head-to-testing.png)

이제 새로운 아이디어를 실험하고 마음껏 개발한 후 커밋하자. 다음 그림을 보자. 

![](https://git-scm.com/book/en/v2/images/advance-testing.png)

`testing` 브랜치는 마지막 커밋을 포인팅하기 위하여 앞으로 나아갔으나 `master` 브랜치는 가만히 멈추어 있다. 

```shell
git checkout master
```

그러면 위 명령어로 `master` 로 되돌아가보자. 

![](https://git-scm.com/book/en/v2/images/checkout-master.png)

이 명령어는 2 가지 일을 했다. `HEAD` 를 `master` 를 포인팅하게 했고 파일들을 `master` 가 포인팅하는 커밋의 시점으로 되돌려놓았다. 

그러고 나서 또 다시 파일을 변경하고 커밋했다고 하자. 다음 그림이 현 시점에서 상황을 보여준다. 

![](https://git-scm.com/book/en/v2/images/advance-master.png)

이 상황은 또한 `log` 명령어로 볼 수 있다.

- `git log --oneline --decorate --graph --all` : 브랜치 상황을 그래프로 시각적으로 보여준다. 

## Branching Management

- `git checkout -b <name>` : 브랜치 생성과 동시에 이주한다. 

- `git branch` : 현재 브랜치를 출력한다. 

  - `*` 가 표시되어 있는 브랜치가 현재 상주하고 있는, 즉 `HEAD` 가 포인팅하고 있는 브랜치이다. 

- `git branch -v` : 더 자세하게 출력한다. 

- `git branch --merged` : 현재 상주하고 있는 브랜치에 이미 병합된 브랜치를 출력한다. 

  - 이미 병합해서 삭제해도 되는 브랜치를 출력할 때 유용한다. 

- `git branch --no-merged` : 현재 상주하고 있는 브랜치에 병합되지 않은 브랜치를 출력한다. 

  - 이 명령어로 출력된 브랜치를 `git branch -d <name>` 으로 삭제하려하면 병합되지 않았다는 에러가 출력되며 삭제되지 않는다. 하지만 `-d` 옵션을 `-D` 로 바꾸어 강제로 삭제 할 수도 있다.

- `git branch -d <name>` : 브랜치를 삭제한다. 

- `git branch -D <name>` : 병합되지 않은 브랜치도 강제로 삭제한다. 

## 기본적인 브랜칭과 병합 시나리오 예시 

```shell
git checkout -b iss53
# branch[iss53] modify files and commit
git checkout master
git checkout -b hotfix
# branch[hotfix] modify files and commit
git checkout master
git merge hotfix
git branch -d hotfix 
git checkout iss53
# branch[iss53] modify files and commit
git checkout master
git merge iss53
# resolve merge conflicts and commit
git branch -d iss53
```
이제 한 웹개발자가 어떤 유저의 이슈를 해결하던 중 매우 급한 에러를 해결해야 하는 상황을 상상하자.

현재 상황:

![](https://git-scm.com/book/en/v2/images/basic-branching-1.png)

이제 웹개발자가 유저의 이슈를 받고 그 이슈를 `#53` 라 이름지었다고 하자. 그는 이 이슈를 해결하기 위하여 새로운 브랜치를 생성하고 이주한다.

### iss53 을 해결하러 가기 

```shell
git checkout -b iss53
```

현재 상황:

![](https://git-scm.com/book/en/v2/images/basic-branching-2.png)

그리고 웹개발자는 이슈를 해결하기 위해 `index.html` 을 수정하고 커밋했다. 


```shell
git commit -a -m 'added a new footer [issue 53]'
```

현재 상황:

![](https://git-scm.com/book/en/v2/images/basic-branching-3.png)

### 급히 해결해야 하는 에러 hotfix 를 보고받아서 그것부터 해결하러 하기 

그런데 웹개발자가 지금 즉시 해결해야만 하는 매우 급한 에러인 `hotfix` 를 보고받아서 `master` 브랜치로 되돌아가야 한다. 그런데 `git` 은 브랜치를 변경하기 전에 커밋되지 않은 파일들이 있다면 브랜치 변경을 허용하지 않기 때문에 모두 다 커밋이 완료된 상태여야 한다. (하지만 `Stashing` 을 사용하면 가능하기는 하다!)

```shell
git checkout master
```

이제 `hotfix` 를 해결하기 위해 새로운 브랜치를 만든다. 

```shell
git checkout -b hotfix
```

현재 상황:

![](https://git-scm.com/book/en/v2/images/basic-branching-4.png)

그리고 `hotfix` 를 다 해결한 후 커밋을 하였다. 다시 `master` 브랜치로 되돌아간 후 최종적으로 병합을 진행한다. 

```shell
git checkout master
git merge hotfix
```

이때 **Fast-forward** 로 병합을 진행하는데 변경된 커밋이 단순히 `master` 브랜치의 커밋의 앞에 있는 커밋이기 때문이다. 그래서 `git` 은 단순히 `HEAD` 포인터와 `master` 브랜치의 포인터를 앞으로 옮길 뿐이다. 실질적인 병합 과정이라고 할 것도 없는 이 병합을 **Fast-forward** 라 한다. 

현재 상황:

![](https://git-scm.com/book/en/v2/images/basic-branching-5.png)

### 다시 iss53 로 되돌아와서 작업하기 

이제 웹개발자는 다시 `#53` 이슈로 되돌아가서 하던 일을 마무리 하려 한다. 그런데 `hotfix` 브랜치는 더 이상 필요 없으니 먼저 삭제를 한 후 `#53` 이슈를 해결하러 돌아가자. 

```shell
git branch -d hotfix # hotfix 를 삭제한다. 
git checkout iss53
```

그는 `git branch -d` 로 `hotfix` 브랜치를 삭제한 후 `iss53` 브랜치로 되돌아가 작업을 마무리하고 커밋을 하였다.

현재 상황:

![](https://git-scm.com/book/en/v2/images/basic-branching-6.png)

이제 `master` 브랜치로 되돌아가서 해결된 `#53` 이슈를 병합해야한다.

```shell
git checkout master
git merge iss53
```

현재 상황:

![](https://git-scm.com/book/en/v2/images/basic-merging-1.png)

그런데 지금은 `hotfix` 를 병합할 때와 달리 단순히 포인터를 옮기는 것으로 병합이 되지 않는다. `git` 을 이런 상황에서 병합을 하기 위해 두 커밋의 변경사항을 모두 반영하는 새로운 `merge commit` 을 생성한다. 이 `merge commit` 은 여타 커밋과는 달리 부모 커밋을 2 개 갖고 있다.

현재 상황:

![](https://git-scm.com/book/en/v2/images/basic-merging-2.png)

이제 최종적으로 필요없어진 `iss53` 브랜치도 삭제해준다. 

```shell
git branch -d iss53
```

## 병합 충돌 

병합 충돌이란 두 커밋이 동일한 파일을 다른 내용으로 수정하여 병합할 수 없는 상황을 말한다. 위 상황에서 만약 병합 충돌이 일어났다면 어떻게 해야 할까? 

```shell
$ git merge iss53
Auto-merging index.html
CONFLICT (content): Merge conflict in index.html
Automatic merge failed; fix conflicts and then commit the result.
```

먼저 병합 충돌은 `git merge` 명령어를 실행할 때 에러 메시지가 출력되는 것을 보고 알 수 있다.

`git merge` 는 `merge commit` 을 자동으로 생성하며 병합을 진행한다. 하지만 이 경우 `merge commit` 을 자동적으로 생성하지 않고 개발자가 병합 충돌을 고친 후 스스로 커밋하도록 한다. 

일단 병합 충돌을 해결하기 위해 `git status` 명령으로 어떤 파일이 충돌되었는지 확인해야 한다. 

```
$ git status
On branch master
You have unmerged paths.
  (fix conflicts and run "git commit")

Unmerged paths:
  (use "git add <file>..." to mark resolution)

    both modified:      index.html

no changes added to commit (use "git add" and/or "git commit -a")
```

`index.html` 파일에서 충돌이 발생하였으므로 열어본다. 열어보면 파일에는 이미 `git` 이 다음과 같은 충돌 영역을 표시해둔다. 

```shell
<<<<<<< HEAD:index.html
<div id="footer">contact : email.support@github.com</div>
=======
<div id="footer">
 please contact us at support@github.com
</div>
>>>>>>> iss53:index.html
```

충돌 영역은 `=======` 로 구분되어 `HEAD` 가 가르키는 브랜치의 변경사항과 `iss53` 브랜치의 변경사항을 비교하여 보여준다. 당신은 두 변경사항 중 하나를 택하거나 둘 다 택하여 `<<<<<<<` 와 `=======`, 그리고 `>>>>>>>` 를 없애주어야 한다. 

그러고 나서 커밋하면 최종적으로 `merge commit` 이 생성되며 병합이 완료된다! 

## 원격 레포지토리의 브랜치 관리 시나리오 

- Remote references : 브랜치, 태그 등을 포함한 원격 레포지토리의 레퍼런스를 뜻한다. 

- `git ls-remote <remove>` : 원격 레포지토리의 레퍼런스를 출력한다.

- `git remote show <remove>` : 원격 레포지토리의 레퍼런스를 출력한다.

- Remote-tracking branch : 원격 레포지토리의 브랜치의 로컬 레퍼런스이다. 

  - `<remote>/<branch>` 로 명칭된다. 

  - 예시 
  
    `origin` 원격 레포지토리의 `master` 브랜치를 확인하려면 `origin/master` 로컬 브랜치를 보면 된다.

이제 `git.ourcompany.com` 이라는 서버에서 레포지토리를 `clone` 해왔다고 하자. `git clone` 명령어는 `origin` 이라는 원격 레퍼런스를 자동으로 생성하고 `master` 브랜치가 그것을 가르키도록 만든다. 그리고 `master` 를 Remote-tracking branch 로써 `origin/master` 로컬 브랜치로 이름짓는다.

현재상황 :

![](https://git-scm.com/book/en/v2/images/remote-branches-1.png)

만약 `master` 브랜치에서 작업을 하며 커밋을 했고 또 다른 누군가가 원격 레포지토리를 업데이트 했다고 하자. 그럼에도 로컬에서 원격 레포지토리를 가르키는 `origin/master` 는 변하지 않는다. 

현재상황 :

![](https://git-scm.com/book/en/v2/images/remote-branches-2.png)

- `git fetch <remote>` : 원격 레포지토리의 업데이트  사항들을 로컬에 동기화한다. 

이때 누군가 업데이트 한 것을 동기화하기 위하여 `origin/master` 를 업데이트하기 위해서 `git fetch origin` 명령어를 사용했다고 하자.

현재상황 :

![](https://git-scm.com/book/en/v2/images/remote-branches-3.png)

그러면 위와 같이 `origin/master` 가 업데이트되어 새로운 커밋을 가르키게 되었다. 

## 다중 원격 레포지토리 브랜치 관리 시나리오 

이제 당신의 소규모 팀이 개인적으로 사용하는 또 다른 서버 `git.team1.ourcompany.com` 이라는 원격 레포지토리를 `git remote add teamone git://git.team1.ourcompany.com` 를 통하여 추가했다고 하자.

현재상황 : 

![](https://git-scm.com/book/en/v2/images/remote-branches-4.png)

그러나 아직 `teamone` 으로부터 그 어떤 데이터도 가져오지 못했다. 그러니 `git fetch teamone` 을 통해 모든 데이터를 가져오자. 

현재상황 : 

![](https://git-scm.com/book/en/v2/images/remote-branches-5.png)

이제 작업한 것을 원격 레포지토리에 `push` 하여 공유하고 싶다고 하자. 

- `git push <remote> <branch>` : 원격 레포지토리에 `<branch>` 를 업데이트한다. 

  - `serverfix` 라는 브랜치를 갖고 있고 이것을 서버에 업데이트 하고 싶다면 `git push origin serverfix` 라고 입력한다. 

  - 이것은 `git push origin refs/heads/server:refs/heads/server` 의 줄임말이고 "로컬에 있는 `serverfix` 브랜치를 원격 레포지토리의 `serverfix` 브랜치에 업데이트 하겠다" 는 뜻이다. 

  - `git push origin serverfix:serverfix` 도 동일한 기능을 한다. 

  - 만약 원격 레포지토리에 추가되어 업데이트될 브랜치 이름을 `awesomebranch` 로 변경하고 싶다면 `git push origin serverfix:awesomebranch` 라고 실행하면 된다.

이후의 시나리오 : 

- `git fetch origin` : 이제 또 다른 누군가 `git fetch origin` 를 실행하면 당신이 `push` 한 `serverfix` 브랜치도 가져오게 된다.

  - `git merge origin/serverfix` : 하지만 단지 `origin/serverfix` 라는 포인터가 생겼을 뿐이다! 만약 현재 브랜치에 병학하여 작업하고 싶다면 이 명령어를 실행하자. 

  - `git checkout -b serverfix origin/serverfix` : 하지만 로컬에서 `serverfix` 라는 브랜치를 생성하고 그곳에서 작업하고 싶다면 이 명령어를 실행하면 된다. 

    - `git checkout --track origin/serverfix` 가 동일한 기능을 하기 때문에 이런 줄임 형태로도 많이 쓰인다. 

  - `git checkout -b sf origin/serverfix` : 서버에서 사용하는 `serverfix` 라는 이름이 마음에 들지 않아서 로컬에서는 `sf` 라는 이름을 사용하고 싶다면 이 명령어를 입력한다. 

  - `git branch -u origin/serverfix` : 만약 이미 로컬 브랜치가 존재하는데 이것을 원격 레포지토리의 브랜치로 업데이트하고 싶다면 `-u` 옵션 또는 `--set-upstream-to` 옵션을 붙혀서 이 명령어를 실행한다. 

- `git branch -vv` : 브랜치들의 상황정보를 ahead, behind 정보와 함께 보여준다. 

  - 예시 

    ```shell
    $ git branch -vv
      iss53     7e424c3 [origin/iss53: ahead 2] forgot the brackets
      master    1ae2a45 [origin/master] deploying index fix
    * serverfix f8674d9 [teamone/server-fix-good: ahead 3, behind 1] this should do it
      testing   5ea463a trying something new
    ```

    위 예시에서 `origin/iss53` 의 `ahead 2` 는 서버에 `push` 되지 않은 로컬의 커밋이 `2` 개 있다는 뜻이다. 
    
    `origin/master` 브랜치는 업데이트 할 것이 없다.

    `serverfix` 브랜치는 `teamone` 서버의 `server-fix-good` 브랜치를 포인팅하고 있는데 아직 `push` 되지 않은 로컬 커밋이 `3` 개 있고 서버에서 병합해야 할 커밋이 `1` 개 있다는 뜻이다. 

    `testing` 브랜치는 어떤 원격 레포지토리도 포인팅하고 있지 않는 것을 알 수 있다.
  
  - 위 예시에서의 ahead 와 behind 의 숫자들은 마지막 `fetch` 로부터 얻은 정보들일 뿐이다. 이 명령어는 서버의 최신 상황을 반영해주지는 않는다. 따라서 실제 최신 정보를 보기 위하여 다음 명령어를 입력해야 한다.

    ```shell
    git fetch --all; git branch -vv
    ```

- `git pull <remote> <branch>` : 원격 레포지토리에서 데이터를 가져옴과 동시에 병합을 해준다.

  - `git fetch` 가 단순히 원격 레포지토리에서 데이터를 가져오기만 하기 때문에 `git merge` 로 병합을 해주어야 하는 반면 `git pull` 은 데이터를 가져옴과 동시에 병합을 해준다.

- `git push <remote> --delete <branch>` : 원격 레포지토리의 브랜치를 삭제한다. 

  - 특정 브랜치에서의 모든 작업이 끝났고 `master` 브랜치에도 병합을 했다면 원격레포지토리의 브랜치를 삭제할 수 있다. `origin` 서버의 `serverfix` 브랜치를 삭제하고 싶다면 다음과 같이 입력한다.

    ```shell
    git push origin --delete serverfix
    ```

# 기타 

## 자동 로그인

- `git config --global credential.helper cache` : 원격 레포지토리의 아이디와 비밀번호를 임시적으로 저장한다.

- `git config --global credential.helper store` : 원격 레포지토리의 아이디와 비밀번호를 `~/.git-credentials` 에 영구적으로 저장한다.
