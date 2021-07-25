
# Install Arch Linux in VirtualBox

기본적으로 이곳(https://wiki.archlinux.org/index.php/Installation_guide)의 가이드를 기반으로 설치 

# 1

2. 시스템 시간 설정 : `timedatectl set-ntp true` 로 시스템 시간을 설정하고 `timedatectl status` 로 상태를 체크

    ```
    /dev/sda1 - ext4
    ```

1. `cfdisk` 명령어로 위와 같은 파티션 구조로 설정

  - 시작 시 `dos` 를 선택 

3. `/dev/sda3 - ext4` 파티션 

    - `New` 버튼으로 크기는 나머지 크기로 지정 

    - `primary` 선택 

    - `Bootable` 선택

5. `Write` 선택 후 `yes` 를 입력. 그리고 `Quit` 으로 `cfdisk` 종료 

6. 파일시스템 포맷

    ```shell
    mkfs.ext4 /dev/sda1
    ```

7. 마운트 : 파티션을 사용하기 위해 리눅스 파일 시스템에 연결을 해야 함.

    ```shell
    mount /dev/sda1 /mnt
    ```

1. `vi /etc/pacman.d/mirrorlist` 로 미러리스트를 열고 한국 미러링크인 `Server = http://mirror.premi.st/archlinux/$repo/os/$arch` 를 맨 위에 써줌. 

2. base 패키지 설치하기

`pacstrap /mnt base base-devel linux linux-firmware`

3. `genfstab -U /mnt >> /mnt/etc/fstab` 으로 `fstab (file system table)` 을 만듦. 파일 시스템이 어떻게 마운트되었나 알려주는 파일임. (genfstab : GENerate File System TABle)

## 3

1. 파일시스템 내부로 진입 `arch-chroot /mnt`

4. `pacman -S vim dhcpcd` 로 필요 패키지 설치 

4. 로케일 설정 : `vi /etc/locale.gen` 로 파일에 들어가서 **en_US.UTF-8 UTF-8** 와 **ko_KR.UTF-8 UTF-8** 의 주석을 지워줌. 그리고 `locale-gen` 로 로케일을 생성해준다.

4. 언어설정 : `locale.conf` 를 설정해주는데 시스템 전반의 언어를 관리하는 파일임. `echo LANG=en_US.UTF-8 > /etc/locale.conf` 로 설정해줌. 한글 디렉토리 이름을 선호하면 `ko_KR.UTF-8` 을 입력. `export LANG=en_US.UTF-8` 명령어로 현재 쉘의 언어를 선언해줌

5. PC 이름 설정 : `echo ccsss > /etc/hostname`

6. hosts 설정 : `vi /etc/hosts` 로 `hosts` 를 열고 다음과 같이 변경 

    ```shell
    127.0.0.1	localhost
    ::1		    localhost
    127.0.1.1	ccsss.localdomain	ccsss
    ```

6. `passwd` 로 루트 비밀번호 설정 

7. `useradd -m -G users,wheel -s /bin/bash ccsss` 로 사용자 추가

    - `-G` 옵션 : 뒤따라오는 옵션의 그룹에 ccsss 를 추가함. 이 경우 users 와 wheel 그룹에 추가됨.
      
    - `users` 그룹 : 표준 유저 그룹
      
    - `wheel` 그룹 : sudo 와 su 를 사용할 수 있는 그룹

8. `passwd ccsss` 명령어로 비밀번호를 생성한다.

9. `visudo` 명령어로 파일을 열고 `# %wheel ALL=(ALL) ALL` 이라고 주석처리된 문장의 주석을 해제하면 wheel 그룹에 sudo 권한이 주어짐. 

8. 부트로더 설치 : **grub** 은 대부분 배보판에서 사용하기에 익혀두면 좋음. `pacman -S grub` 로 설치. 그리고 `grub-install /dev/sda1` 로 grub 으로 부팅하도록 설정. 그리고 `grub-mkconfig -o /boot/grub/grub.cfg` 로 설정 파일을 만듦.

- `sudo vi /etc/default/grub` 으로 `GRUB_TIMEOUT=5` 를 `GRUB_TIMEOUT=0` 로 변경 


9. 리부팅 

    - `exit` 로 쉘을 나가고

    - `umount -R /mnt` 로 장치를 언마운트
      
    - `reboot` 로 재부팅하고 컴퓨터가 종료되고 다시 시작될 때 usb 를 빼주면 됨.

`sudo vim /etc/pacman.conf` 로 설정파일에서 `Color` 의 주석해제 

`sudo pacman -Syu`

4. `powerpill` 설치 

`sudo pacman -S git`

- **AUR** installer `yay` 를 다음 명령어로 설치

```shell
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
```

`yay -S --noconfirm powerpill`

# Core Util

## Core Devel

- `sudo powerpill -S --noconfirm python python-pip python2 python2-pip`

## Core CLI

- `sudo powerpill -S --noconfirm zsh openssh tmux wget tcpdump gdb nmap radare2 lsd zip unzip neofetch scrot sshpass bat fd jq alsa-utils colordiff`

- `yay -S --noconfirm gotop pkgtop downgrade`
