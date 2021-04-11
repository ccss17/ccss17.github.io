
컴퓨터 공학자에게 기반 지식이 되는 **수학의 역사**, **괴델의 불완전성 정리**, **튜링기계**, **기술적 특이점** 등과 프로그래머에게 유용한 툴(**Docker**, **Git**, **VSCode**, **vim**, **tmux**, **zsh**, **make**, **bazel** 등)과 그것의 생산성을 최대화할 수 있는 여러가지 팁들을 5일 동안 가이드해주는 레포지토리입니다.

## inspired by

이 프로젝트는 **MIT** 의 **[Missing Semester](https://missing.csail.mit.edu/)** 에서 영감을 받아서 만들어졌습니다. **Missing Semester** 의 서문은 다음과 같이 프로그래머들이 컴퓨터 공학적 지식을 배우는데에는 많은 배움을 얻을 수 있지만, 정작 그들이 수많은 시간을 쏟게 되는 툴과 툴을 효율적으로 사용할 수 있는 방법에 대한 적절한 리드를 받을 수 없었던 상황을 지적합니다. 

!!! note ""

    Classes teach you all about advanced topics within CS, from operating systems to machine learning, but **there’s one critical subject that’s rarely covered, and is instead left to students to figure out on their own: proficiency with their tools.** We’ll teach you how to master the command-line, use a powerful text editor, use fancy features of version control systems, and much more!

    Students spend hundreds of hours using these tools over the course of their education (and thousands over their career), so **it makes sense to make the experience as fluid and frictionless as possible.** Mastering these tools not only enables you to spend less time on figuring out how to bend your tools to your will, but it also lets you solve problems that would previously seem impossibly complex.

이 5일짜리 가이드는 이러한 아이디어에서 착안하여 제가 주관적으로 선정한 프로그래밍을 할 때 필요한 여러가지 툴들과 **Linux** 에 관련된 내용과 컴퓨터에 대한 약간 철학적인 이야기에 대한 내용을 담고 있습니다.

## Notice 

- 모든 내용은 편의를 위하여 [Ubuntu 도커 컨테이너](https://hub.docker.com/_/ubuntu) 위에 실습 환경을 만든 [ccss17/ubuntu](https://github.com/ccss17/ubuntu-unminimize) 에서 진행하는 것을 전제합니다. 다음을 실행하여 간단히 실습환경을 구축 할 수 있습니다.

    **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

    ```shell
    $ docker run -it ccss17/ubuntu
    ```

    **Docker** 설치와 컨테이너 실행에 관한 내용은 [여기](docker.md#%EB%8F%84%EC%BB%A4-%EC%84%A4%EC%B9%98)에서 더 자세히 설명합니다.

- 본문에서 말하는 "교재" 란 http://www.linuxcommand.org/tlcl.php 에서 제공하는 PDF 파일을 뜻합니다. 

## 읽는 법

- **N 번째** 날에는 **Day N** 을 **정독** 하면 됩니다. 

- 다음의 표시가 있는 코드 부분은 실제로 직접 실행해보면 실습하면 됩니다. 

    **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

    ```shell
    $ (execute-me)
    ```

## 읽지 않는 법 

- 맥락에서 약간 벗어나지만 나름대로 필요한 내용은 

    > (맥락에서 약간 벗어나지만 나름대로 필요한 내용)

    으로 표시했습니다. 이 부분은 시간절약을 위해 아예 안봐도 됩니다.

- 만약

    **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

    가 없는 코드 부분은 굳이 실행하지 않아도 되고 실행해도 됩니다. 시간 절약을 위하여 넘겨도 됩니다. 

# Contents

## [Day 1](01-Day1/readme.md)

Docker, 리눅스 교재

## [Day 2](02-Day2/readme.md)

리눅스 교재, Stackoverflow Survey, Git, Github, VSCode, Markdown

## [Day 3](03-Day3/readme.md)

리눅스 교재, vim, tmux

## [Day 4](04-Day4/readme.md)

CLI,더 빨라진 git,`bash` ➜ `zsh`,더 빨라진 tmux,더 빨라진 vim,VSCode 업그레이드,VSCode Vim,VSCode 디버깅

## [Day 5](05-Day5/readme.md)

Git 과 Github 못다한 이야기(Git Branch, Github pull request, Git Stash, Git Reset), Build System(Makefile, Bazel), Coding Convention(C++, Python), 좋은 정보 얻기, 리눅스 교재, Funny CLI

## Content List

위에서 **Day1** 부터 **Day5** 까지 컨텐츠들을 5일 동안 학습할 수 있도록 순서를 적절히 배치해놓았는데, 해당 내용의 일관된 내용을 살펴보고 싶으시다면 다음의 리스트를 보시면 됩니다.

- **[Docker](docker.md)**

- **[Information](information.md)**

- **[Build System](build.md)**

- **[Coding Convention](codingconvention.md)**

- **[Git](git.md)**

- **[VSCode](vscode.md)**

- **[Markdown](markdown.md)**

- **[Tmux](tmux.md)**

- **[Vim](vim.md)**

- **[CLI](cli.md)**

## 조금은 철학적인 이야기

- [수학의 역사](../Math/MathHistory.md)

- [괴델의 불완전성 정리](../Math/incompleteness.md)

- [튜링의 증명](../Math/turing.md)

- [기술적 특이점 - "Why the future doesn't need us"](../Computer/future.md)
