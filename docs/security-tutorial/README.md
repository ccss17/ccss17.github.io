# security-tutorial

This is a repository containing the contents of GBC's 4th course, Security Course, which is being held for beginners at HGU computer security club, GHOST.

한동대학교 컴퓨터보안 동아리 **GHOST** 에서 신입기수를 대상으로 진행하는 **GBC** 의 `4` 번째 과정인 **보안** 과정을 진행하기 위한 내용을 담은 레포지토리입니다. 

## Notice

이 가이드는 **10일** 과정으로 구성되며 독자가 **C 언어** 를 알고 있고 **[ProgrammerBase](../ProgrammerBase)** 를 공부하고 왔다고 가정합니다.

## Docker

이제 모든 실습을 Docker 가상 환경에서 할 수 있도록 되었습니다! 서버 비용도 필요 없고 무겁고 느린 가상머신도 필요없어요. 다음 명령어만 입력하면 security-tutorial 을 실습할 모든 준비가 끝납니다.

```shell
$ docker run -it --privileged ccss17/security-tutorial
```

## Contents

### Day 1 : [Base](01-Base/README.md)

- 기술적 특이점(Technological Singularity)

- 약인공지능과 강인공지능(Weak AI and Strong AI)

- 보안에 관한 기본 용어(Basic terminology about security)

### Day 2 : [Computer Principle 1](02-Computer1/README.md)

- 괴델의 불완전성 정리(Godel's Incompleteness Theorem)

- 튜링 머신(Turing Machine)

- 폰 노이만 구조(Von Neumann architecture)

- 데이터 저장방식(How data is stored on computer)

- CPU 레지스터(CPU register)

- 어셈블리어 1 (Assembly Language 1)

### Day 3 : [Computer Principle 2](03-Computer2/README.md)

- 어셈블리어 2 (Assembly Language 2)

- 가상 메모리 시스템 (Virtual Memory System)

- 스택 메모리 영역 (Stack Memory)

- `gdb` 사용법 1 (`gdb` usage 1)

- 함수 호출의 컴퓨터 내부적 원리 (Computer internal principle of function calls)

### Day 4 : [Reversing 1](04-Reversing1/README.md)

- 리버싱의 정의 (Definition of reversing)

- 리버싱 툴 (Reversing tools)

- `gdb` 사용법 2 (`gdb` usage 2)

- `crackme0x00a` ~ `crackme0x03` 연습 및 설명 

- **(HW)** `crackme0x004`, `crackme0x05` 실습 

### Day 5 : [Reversing 2](05-Reversing2/README.md)

- `crackme0x004`, `crackme0x05` 설명 

- `radare2` 사용법 (`radare2` usage)

- xor 암호화 (xor encryption)

- reversing.kr 문제 `easyelf` 풀어보기 

- **(HW)** `bomb` 실습 

### Day 6 : [Exploit 1](06-Exploit1/README.md)

- 리눅스 특수 권한(Linux special permission)

- 버퍼오버플로우를 통한 프로그램 흐름 조작 (Program flow manipulation through buffer overflow)

- `bof1` 설명 

- `bof2` ~ `bof4` 연습 및 설명 

- **(HW)** `bof5` 실습 

### Day 7 : [Exploit 2](07-Exploit2/README.md)

- 쉘코드 (shellcode)

- `bof6` ~ `bof8` 연습 

### Day 8 : [Exploit 3](08-Exploit3/README.md)

- `bof7` 상세 설명 

- `NX bit` 와 `DEP`

- `RTL`

- `bof9` 연습 및 설명 

### Day 9 : [Exploit 4](09-Exploit4/README.md)

- `ASLR`

- `bof10`, `bof11` 연습 및 설명 

### Day 10 : [Pentest + Wrap-up](10-Pentesting/README.md)

- 침투테스트 예시 (Example of pentest)

- 블루투스 취약점 - 블루본 (Bluetooth vulnerability - Blueborne)

- CPU 취약점 - 멜트다운 (CPU vulnerability - Meltdown)

# Read More

CTF

- https://capturetheflag.withgoogle.com/

- https://captf.com/forsalesClienti/Admin/Login/index.php

- https://www.vulnhub.com/

- http://reversing.kr/challenge.php

- https://xss-game.appspot.com/

- https://github.com/JannisKirschner/Google-XSS-Game

- https://www.vulnhub.com/entry/exploit-exercises-nebula-v5,31/

    - https://forelsec.blogspot.com/2013/03/nebula-solutions-all-levels.html

    - https://leonjza.github.io/blog/2015/05/08/playing-exploit-exercises---nebula/

- http://security.cs.rpi.edu/courses/binexp-spring2015/

    - https://dustri.org/b/defeating-ioli-with-radare2.html

- https://www.hackthissite.org/

- https://www.root-me.org/

- http://pwnable.kr/

- https://webhacking.kr/

- http://wargame.kr

Awesome

- https://github.com/sbilly/awesome-security

- https://github.com/onlurking/awesome-infosec

- https://github.com/guardrailsio/awesome-python-security

- https://github.com/enaqx/awesome-pentest

책추천

- 데프콘 공식 추천도서 : https://github.com/enaqx/awesome-pentest

- https://codecondo.com/8-popular-books-to-learn-ethical-hacking/

- https://bonkersabouttech.com/20-best-hacking-books/

- https://www.quora.com/Which-one-is-the-best-book-to-learn-hacking-from-the-basics

- https://www.fromdev.com/2013/02/Hacking-Books.html

- https://jcubic.wordpress.com/2010/11/15/10-books-every-hacker-should-read/

- https://www.reddit.com/r/hacking/comments/79x4iz/top_20_best_hacking_books_you_need_to_read_if_you/

- https://businessinsights.bitdefender.com/five-security-books-you-should-read

- https://www.compsmag.com/best/hacking-books/

기타

- https://teachyourselfcs.com/

- https://infosecwriteups.com/

- https://www.hackerone.com/

- https://googleprojectzero.blogspot.com/

- https://bugs.chromium.org/

- https://0x00sec.org/

- https://msrc-blog.microsoft.com/

- https://overthewire.org/wargames/

- https://www.lazenca.net/

- https://nets.ec/Main_Page

- https://github.com/Maijin/radare2-workshop-2015

- https://www.bottomupcs.com/

- https://www.hacking-tutorial.com/

- https://www.blackhatworld.com/