荔枝糖 Hex
========

![](../../assets/tang_hex.png)


**开发板主要包含：**

* FPGA： Zynq XC7Z020
* NAND Flash： 2Gb
* LPDDR3： 1GB
* 100M 网口: x1
* USB 2.0： x4
* TF 卡槽: x1

 

**主要芯片介绍:**

* 主芯片： XC7Z020-1CLG484

Zynq®-7000 SoC 系列集成 ARM® 处理器的软件可编程性与 FPGA 的硬件可编程性，不仅可实现重要分析与硬件加速，同时还在单个器件上高度集成 CPU、 DSP、 ASSP 以及混合信号功能。
本开发板使用芯片具体特性：
  * PS 部分：
Cortex-A9， 双核 667MHz，L1： 32KB 指令空间， 32KB 数据空间每核， L2： 512KB 片上存储空间 256KB。
  * PL 部分：
Artix-7 FPGA, 可编程逻辑单元： 85K，
LUTs： 53200， Block RAM： 4.9Mb

* 内存芯片： MT41K256M16TW-107

容量： 512MB ； 32Meg x 16 x8 banks。
DDR3L SDRAM (1.35V), 向上兼容 1.5V

* NAND FLASH 存储芯片： MT29F2G08ABAEAWP

* ONFI 1.0 接口标准
* SLC 技术
* 结构：
  Page size x8 
  2112 bytes(2048+64bytes)
  Block size 
  64 pages(128K + 4K bytes)
  Plane size 
  2 planes x 1024 blocks per plane
  Device size 
  2Gb： 2048 blocks

* ULPI 桥片： USB3320C

  USB3320 是高度集成的全功能高速 USB 2.0 收发器，基于 Microchip ULPI 接口。
  2.1.5 USB HUB & 10/100 网卡芯片： LAN9514-JZX
  USB Hub：
  1 x 上行 USB2.0 PHY， 4 x 下行 USB2.0 PHY

* 网卡：
  集成 MAC 和 PHY，支持 10BASE-T 和 100BASE-TX


## 资料

* [资料](http://dl.sipeed.com/TANG/Hex/)

