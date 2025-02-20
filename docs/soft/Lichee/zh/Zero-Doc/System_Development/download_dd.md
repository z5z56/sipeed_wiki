---
title: dd镜像烧录
---

## 简介

在windows环境下可以方便的运用Win32DiskImage等工具烧录，而Linux环境下，用dd命令烧录不妨是个好选择，今天，本篇介绍dd烧录的操作步骤以及需注意的细节

两面性：
- 优点：对于喜欢此方式烧录镜像的人来说方便快捷

- 缺点：要敲命令行（对于初学者来说也是个学习了解类Linux环境的机会）

材料准备：
- 内存卡+读卡器+荔枝派Zero+支持完整指令集的x86设备一台（电脑）

或：
- U盘+荔枝派Zero+支持完整指令集的x86设备一台（电脑）

推荐待烧录存储器大小：8GB及以上

推荐镜像下载位址：
- hack to 环荣内网 then //192.168.1.89/musume/Lichee/ubuntu0.5.1-Lichee-20170811G.rar

## dd烧录步骤


### 查看盘符路径先

首先，打开Linux的终端机界面（也就是命令行）
插入一个大小合适的U盘或内存卡与读卡器的组合（荔枝派Zero较适于内存卡）
随便敲一个diskutil list 命令 便会有一堆文字列出

> 可以看到u盘的盘符是 /dev/disknani

### 取消系统对于该盘符的挂载


照顾到大家电脑系统环境的不同，以下两组代码中至少有一组能够正常显示，请直接观看您电脑能正常显示的那组

> :: diskutil umountDisk /dev/disk2
>
> Shell
>
> 1 2 3 arefly:\~ arefly\$ diskutil unmountDisk [内存卡位置] Unmount of
> all volumes on [内存卡位置] was successful arefly:\~ arefly\$
> arefly:\~ arefly\$ diskutil unmountDisk [内存卡位置] Unmount of all
> volumes on [内存卡位置] was successful arefly:\~ arefly\$

### 写入镜像


`sudo dd if=源路径 of=/dev/r卷标 bs=1m ［‘r’ 会让命令执行加快一点］ ［‘bs’为一次填充的容量］`

也就是dd命令

### 弹出内存卡


下电拔卡

或

敲 `diskutil eject [内存卡位置]`

然后热插拔

### 完成前的事项


将内存卡装载到荔枝派Zero，上电运行，您就可开启您的荔枝派Linux之途
