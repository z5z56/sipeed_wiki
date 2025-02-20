---
title: MaixII M2dock 烧录系统
keywords: MaixII, MaixPy3, Python, Python3, M2dock
desc: maixpy doc: MaixII M2dock 烧录系统
---

> ！！！一定要严格按照步骤操作！！！请使用大于 1G 的 TF/SD 卡进行烧录，开源版本要求使用 TF/SD 卡来启动系统。

V831 为全志的 SOC， 所以 Windwos 使用 **PhoenixSuit**, Linux 上使用 **Livesuit** 烧录镜像文件。

- 从下载站获取最新的 V831 系统镜像 [SDK_MaixII/release](https://dl.sipeed.com/shareURL/MaixII/SDK/release) ，找不到就搜索 V831 获取最新的镜像。

- 下载站中有连个同版本不同大小的镜像系统，文件较大的镜像是需要使用dd命令进行系统的烧录。（目前只能在linux系统上进行系统的烧录--2021.06.26）
- 解压 V831 镜像压缩包，得到一个 xxxx.img 文件。

- 从网上获取 PhoenixSuit(Windows) 烧录工具。
  - [baidu-PhoenixSuit](https://www.baidu.com/s?wd=PhoenixSuit)
  - [bing-PhoenixSuit](https://www.bing.com/search?q=PhoenixSuit&FORM=BESBTB&mkt=zh-CN) 
  - [github-PhoenixSuit](https://github.com/colorfulshark/PhoenixSuit)
  - [lo4d-PhoenixSuit](https://phoenixsuit.en.lo4d.com/windows)

## Windows 上使用 PhoenixSuit 烧录

解压 PhoenixSuit(Windows) 工具压缩包，不插入 SD 卡，将 V831 USB OTG 接口连接到 PC， 打开设备管理器， 安装驱动文件

![](./asserts/flash_01.png)

![](./asserts/flash_03.png)

打开烧录软件,  并浏览打开镜像文件

![](./asserts/flash_05.png)

重新插拔板子（上电不插入 SD 卡），软件提示是否要清空烧录，提示是否需要升级，点击 `YES` 

![](./asserts/flash_07.png)

插入 sd 卡，提示是否强制格式化，再次点击 `YES`开始烧录（大约 40S）

![](./asserts/flash_09.png)

可能需要等待几秒才会更新状态，然后等待提示“固件升级成功”，即可断开 USB ，至此固件烧录完毕

![](./asserts/flash_11.png)

![](./asserts/flash_13.png)

## Linux(Ubuntu) 使用 Livesuit 烧录

> [https://linux-sunxi.org/LiveSuit](https://linux-sunxi.org/LiveSuit)

> [ubuntu 安装 LiveSuit 刷机工具](https://www.codenong.com/cs105573875/)

> [https://github.com/QinYUN575/allwinner-livesuit.git](https://github.com/QinYUN575/allwinner-livesuit.git)

### 安装烧录工具 Livesuit 

> **每次更新系统 linux kernel 之后需要重新安装软件**

1. 安装依赖 dkms

```shell
sudo apt install dkms
```

1. 安装 libpng1.2（一定要使用这个版本）

```shell
wget http://archive.ubuntu.com/ubuntu/pool/main/libp/libpng/libpng_1.2.54.orig.tar.xz
tar xvf  libpng_1.2.54.orig.tar.xz
```

```shell
cd libpng-1.2.54
./autogen.sh
./configure
make -j8
sudo make install
```

更新链接库:

```shell
sudo ldconfig
```

1. 安装 **livesuit**

```shell
git clone --recursive https://github.com/QinYUN575/allwinner-livesuit.git
cd allwinner-livesuit
chmod +x livesuit_installer.run
sudo ./livesuit_installer.run
```



### 使用 Livesuit 烧录

`sudo livesuit` 打开烧录工具，并点击“固件”选择镜像文件

![](./asserts/flash_15.png)

不插入 SD 卡，将 V831 USB OTG 接口连接到 PC, 提示是否格式化分区，这时候插入 SD 卡，之后点击 `YES`

![](./asserts/flash_17.png)

等待烧录完成，提示“固件升级成功”，即可断开 USB ，至此固件烧录完毕

![](./asserts/flash_19.png)

![](./asserts/flash_21.png)

> 以上烧录方式适合在镜像文件较小的那个（非dd版本）

## Linux(Ubuntu) 使用 dd镜像 烧录

[下载dd镜像](https://dl.sipeed.com/shareURL/MaixII/SDK/release)带有xx-dd.img文件即可

>经过测试，目前支持在windows上使用phoenixsuit进行系统烧录，不支持在windows上使用镜像烧录工具dd镜像系统包的烧录，建议在linux上使用dd命令进行烧录 ——— 21.06.24 

使用dd命令之前，通过命令 `fdisk -l` 查看tf卡的名称

![dd_1](./../../../assets/images/dd_1.png)

dd命令烧录

```base
dd if=sipedd-v8310-210606-dd.img of=/dev/sdd
```
![dd_2](./../../../assets/images/dd_2.png)
出现为烧录成功

或者直接使用镜像恢复软件打开dd镜像文件

右键打开dd镜像，选择用其他应用程序打开，选择镜像恢复

![dd_3](./../../../assets/images/dd_3.png)
![dd_3](./../../../assets/images/dd_4.png)

点击开始恢复，即可烧录成功
## 常见问题：

系统烧录步骤严格按照文档要求，先打开软件，拔 SD 卡后插入电脑，等待提示确认后再插入 SD 卡自动完成安装。

《[error while loading shared libraries: libpng12.so.0](https://askubuntu.com/questions/895897/error-while-loading-shared-libraries-libpng12-so-0)》

