
# Install Arch Linux 

기본적으로 이곳 https://wiki.archlinux.org/index.php/Installation_guide 의 가이드를 기반으로 설치 

[VirtualBox 에 Arch Linux 설치하기](install-vm.md)

# 1

1. https://www.archlinux.org/download 에서 **Arch Linux** iso 파일 다운로드 

2. USB 플래싱 

    - Arch Linux 

      **Etcher** 로 USB 플래싱 (`yay etcher` -> `etcher-bin` 설치)
    
    - Windows

      **Win32DiskImager** 또는 **rufus** 로 USB 플래싱

3. 플래싱 된 `USB` 로 컴퓨터를 부팅

# 2

1. 네트워크 확인

    - `ping 8.8.8.8` 명령어로 인터넷 연결 상태 확인

    - 와이파이 사용 시 `wifi-menu` 로 확인. 명령어로 wifi 설정 후 확인해야 함

    - **WPA Enterprise** 사용시 `/etc/netctl/` 의 경로에 `profile` 파일을 만들고 다음의 내용으로 저장함.

      ```shell
      Description='Profile description'
      Interface=wlan0 <-- WIRELESS_INTERFACE
      Connection=wireless
      Security=wpa-configsection
      IP=dhcp
      ESSID=HGU_WLAN <-- UNIVERSITY_SSID
      WPAConfigSection=(
      'ssid="HGU_WLAN <-- UNIVERSITY_SSID"'
      'proto=RSN'
      'key_mgmt=WPA-EAP'
      'eap=PEAP'
      'group=CCMP'
      'pairwise=CCMP'
      'identity="UNIVERSITY_USERNAME"'
      'password="UNIVERSITY_PASSWORD"'
      'phase2="auth=MSCHAPV2"'
      )
      ```
    
    - `netctl start profile` 실행 


2. 시스템 시간 설정 : `timedatectl set-ntp true` 로 시스템 시간을 설정하고 `timedatectl status` 로 상태를 체크

3. UEFI 부팅 가능 확인 : `ls /sys/firmware/efi` 명령어 입력 후 efivars 폴더가 있으면 UEFI 부팅 가능

1. `lsblk` 로 디바이스 확인 후 파티션 계획을 다음과 같이 세움. 

    ```
    /dev/sda1 - UEFI    512MB
    /dev/sda2 - SWAP    3GB (8GB 램에서)
    /dev/sda3 - ext4    나머지
    ```

1. `cfdisk` 명령어로 위와 같은 파티션 구조로 설정

2. 모든 파티션을 `Delete` 해서 깨끗한 상태로 만듦 

3. `/dev/sda1 - UEFI` 파티션 

    - `New` 버튼으로 크기를 `512M` 으로 지정

    - `primary` 선택 

    - `Type` 에서 `EFI` 선택  

4. `/dev/sda2 - SWAP` 파티션 

    - `free -h` 명령어로 **RAM** 크기 확인 

    - https://itsfoss.com/swap-size/ 의 표를 참고해서 `SWAP` 사이즈 결정. 이 경우 `16GB` 램이기에 `20GB` 의 `SWAP` 사이즈로 결정함 

    - `New` 버튼으로 크기를 `20G` 으로 지정

    - `primary` 선택 

    - `Type` 에서 `Linux swap / Solaris` 선택  

4. `/dev/sda3 - ext4` 파티션 

    - `New` 버튼으로 크기는 나머지 크기로 지정 

    - `primary` 선택 

    - `Type` 에서 `Linux` 선택. 

5. `Write` 선택 후 `yes` 를 입력. 그리고 `Quit` 으로 `cfdisk` 종료 

6. 각각의 파일시스템으로 포맷

    ```shell
    mkfs.fat -F32 /dev/sda1
    mkswap /dev/sda2
    swapon /dev/sda2
    mkfs.ext4 /dev/sda3
    ```

7. 마운트 : 파티션을 사용하기 위해 리눅스 파일 시스템에 연결을 해야 함.

    ```shell
    mount /dev/sda3 /mnt
    mkdir /mnt/boot
    mount /dev/sda1 /mnt/boot
    ```

1. `vi /etc/pacman.d/mirrorlist` 로 미러리스트를 열고 한국 미러링크인 `Server = http://mirror.premi.st/archlinux/$repo/os/$arch` 를 맨 위에 써줌. 

2. base 패키지 설치하기

`pacstrap /mnt base base-devel linux linux-firmware`

3. `genfstab -U /mnt >> /mnt/etc/fstab` 으로 `fstab (file system table)` 을 만듦. 파일 시스템이 어떻게 마운트되었나 알려주는 파일임. (genfstab : GENerate File System TABle)

## 3

1. 파일시스템 내부로 진입 `arch-chroot /mnt`

2. 시간 설정 : `ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime` 명령어로 링크를 걸어줌. 이로써 /etc/localtime 을 다룰 때 `/usr/share/zoneinfo/Asia/Seoul` 이 참조됨.

3. `hwclock --systohc --utc` 명령어로 하드웨어 시간 설정을 해줌. 

4. `pacman -S vim networkmanager grub efibootmgr` 로 필요 패키지 설치 

4. 로케일 설정 : `vim /etc/locale.gen` 로 파일에 들어가서 **en_US.UTF-8 UTF-8** 와 **ko_KR.UTF-8 UTF-8** 의 주석을 지워줌. 그리고 `locale-gen` 로 로케일을 생성해준다.

4. 언어설정 : `locale.conf` 를 설정해주는데 시스템 전반의 언어를 관리하는 파일임. `echo LANG=en_US.UTF-8 > /etc/locale.conf` 로 설정해줌. 한글 디렉토리 이름을 선호하면 `ko_KR.UTF-8` 을 입력. `export LANG=en_US.UTF-8` 명령어로 현재 쉘의 언어를 선언해줌

5. PC 이름 설정 : `echo ccsss > /etc/hostname`

6. hosts 설정 : `vim /etc/hosts` 로 `hosts` 를 열고 다음과 같이 변경 

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

8. 부트로더 설치 : **grub** 은 대부분 배보판에서 사용하기에 익혀두면 좋음. 그리고 `grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=arch --recheck` 로 grub 으로 부팅하도록 설정. 그리고 `grub-mkconfig -o /boot/grub/grub.cfg` 로 설정 파일을 만듦.

9. 리부팅 

    - `exit` 로 쉘을 나가고

    - `umount -R /mnt` 로 장치를 언마운트
      
    - `reboot` 로 재부팅하고 컴퓨터가 종료되고 다시 시작될 때 usb 를 빼주면 됨.

## 5

- `sudo vim /etc/default/grub` 으로 `GRUB_TIMEOUT=5` 를 `GRUB_TIMEOUT=0` 로 변경 

`sudo vi /etc/pacman.conf` 로 설정파일에서 `Color` 의 주석해제 

- `sudo systemctl enable --now NetworkManager`

1. 인터넷 연결 

    - `wpa2_enterprise` (대학교 WiFi 등) 을 사용할 시

      ```shell
      $ nmcli con add type wifi ifname WIRELESS_INTERFACE con-name CONNECTION_NAME ssid SSID
      $ nmcli con edit id CONNECTION_NAME
      nmcli> set ipv4.method auto
      nmcli> set wifi-sec.key-mgmt wpa-eap
      nmcli> set 802-1x.eap ttls
      nmcli> set 802-1x.phase2-auth pap
      nmcli> set 802-1x.identity USERNAME
      nmcli> set 802-1x.pasword PASSWORD
      nmcli> save
      nmcli> activate
      ```
    
    - `Wpa2 Enterprise` 가 아닐 시 단순히 `nmcli d wifi connect SSID password PASSWORD` 로 연결 

2. pacman 최적화 및 업데이트

    `sudo pacman -Syu`

3. 미러리스트 최적화 

    `sudo pacman -S reflector git`

`sudo reflector --sort rate --country China --country Japan --country "South Korea" --country "Hong Kong" --country India --save /etc/pacman.d/mirrorlist`


이거 설정하는건 GUI 설정한 다음 복붙할수있도록

`/usr/lib/systemd/system/reflector.service`
```
[Unit]
Description=Pacman mirrorlist update
Documentation=https://wiki.archlinux.org/index.php/Reflector
Requires=network-online.target
After=network-online.target

[Service]
Type=oneshot
EnvironmentFile=/usr/share/reflector-timer/reflector.conf
ExecStart=/usr/bin/reflector --country 'United States' --latest "50" --sort "rate" --save /etc/pacman.d/mirrorlist -p "http" -p "https" -p "rsync"
```

`/usr/lib/systemd/system/reflector.timer`
```
[Unit]
Description=Weekly pacman mirrorlist refresh

[Timer]
OnBootSec=5min
OnUnitActiveSec=1d

[Install]
WantedBy=timers.target
```

`sudo systemctl enable --now reflector.timer`

4. `powerpill` 설치 

- **AUR** installer `yay` 를 다음 명령어로 설치

```shell
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
```

`yay -S --noconfirm powerpill`

3. Xorg 설치

`lspci | grep -e VGA -e 3D` 로 그래픽카드를 확인. 

**Intel** 이면 `sudo powerpill -S --noconfirm xorg-server xf86-video-intel mesa` 디스플레이 서버, 그래픽카드드라이버를 설치 

**AMD/ATI** 이면 `sudo powerpill -S --noconfirm xorg-server xf86-video-ati mesa` 디스플레이 서버, 그래픽카드드라이버를 설치 

# DE

## i3-gaps/polybar

- `sudo powerpill -S --noconfirm i3-gaps rofi xorg-xrdb xdg-user-dirs ttf-inconsolata ttf-font-awesome xorg-xrandr`

- `yay -S --noconfirm polybar ly-git compton-tryone-git ttf-material-design-icons ttf-weather-icons ttf-monapo nerd-fonts-hack`

  - `xdg-user-dirs-update`
  
  - `sudo systemctl enable ly`

## 한글 폰트 및 입력기 

- `yay -S --noconfirm ttf-nanum` or `sudo powerpill -S --noconfirm noto-fonts-cjk`

### ibus

- `sudo powerpill -S ibus ibus-hangul`

- `~/.xprofile` 에 다음 내용 입력. 

  ```
  export QT_IM_MODULE=ibus
  export GTK_IM_MODULE=ibus
  export XMODIFIERS=@im=ibus
  ibus-daemon -drx &
  ```

- `ibus-setup` 

  - General - Keyboard Shortcuts - Next input method: <Shift>space 로 변경

  - Input Method - Add - "Korean - Hangul" 추가 

  - Input Method - "Korean - Hangul" - Preferences - Start in Hangul Mode 체크 

# Core Util

## Core Devel

- `sudo powerpill -S --noconfirm python python-pip python2 python2-pip jdk-openjdk nodejs npm`

  - $ sudo pip3 install i3altlayout

  - `sudo pip3 install i3altlayout`

## Core CLI

- `sudo powerpill -S --noconfirm zsh openssh tmux wget tcpdump gdb nmap radare2 lsd zip unzip neofetch scrot sshpass bat fd jq alsa-utils colordiff`

- `yay -S --noconfirm gotop pkgtop downgrade ttf-ubraille`

- `sudo mv /usr/share/fonts/gnu-free /tmp` : `gotop` 의 그래프 폰트를 랜더링해주는 `ttf-ubraille` 을 `gnu-free` 폰트가 씹어버리기 때문에 

## Core GUI

- `sudo powerpill -S --noconfirm firefox vlc deepin-file-manager deepin-icon-theme mupdf feh alacritty network-manager-applet lxappearance`

- `yay -S --noconfirm visual-studio-code-bin google-chrome slack-desktop tusk posy-cursors`

## Font 

https://www.reddit.com/r/archlinux/comments/5r5ep8/make_your_arch_fonts_beautiful_easily/

# dotfiles

## Options

- **Bluetooth** 필요 시 `sudo powerpill -S bluez bluez-utils blueman` 로 설치 후 `sudo systemctl enable --now bluetooth`

- **Dropbox**

- **Android Studio** 필요 시 `yay android-studio` 로 설치 

- **Go** 필요 시 `sudo powerpill -S go` 로 설치 

- **libreoffice** 필요 시 `sudo powerpill -S libreoffice-fresh` 로 설치 

  - https://downloads.sourceforge.net/project/mscorefonts2/rpms/msttcore-fonts-installer-2.6-1.noarch.rpm 에서 **Microsoft-compatible fonts** 를 다운로드 한 후 `pacman -Sy rpmextract xorg-font-utils fontconfig` 로 필요 패키지 설치

  - `rpmextract.sh msttcore-fonts-installer-2.6-1.noarch.rpm` 로 `etc`, `usr` 에 설치 될 파일을 추출한 후 메뉴얼하게 설치해야 함. 

- https://wiki.archlinux.org/index.php/Metasploit_Framework#Installation 

  - **metasploit** 필요 시 `sudo powerpill -S metasploit` 로 설치 

- `yay balena-etcher`

- `yay postman`

- https://wiki.archlinux.org/index.php/VirtualBox#Installation_steps_for_Arch_Linux_hosts

- https://wiki.archlinux.org/index.php/Qt#Installation

- https://wiki.archlinux.org/index.php/Wireshark#Installation

- https://wiki.archlinux.org/index.php/Tor#Installation

- `yay ida-free`
