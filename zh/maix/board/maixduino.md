开发板 Maixduino
===========

![](https://cdn.sipeed.com/wiki/maix/board/maixduino_0.png)
![](https://cdn.sipeed.com/wiki/maix/board/maixduino_1.png)
![](https://cdn.sipeed.com/wiki/maix/board/maixduino_3.jpg)

![](https://cdn.sipeed.com/wiki/maix/maixduino/maixduino_pins_1920_914.png)


* `Arduino UNO R3` 外形和引脚兼容 (**注意** 电平不兼容， `Arduino` 采用 `5V`， `Maixduino` 引脚都是 `3.3V` 或者 `1.8V`, 所有引脚均**不支持** `5V` 耐受)
* Maix M1 模组
* ESP32-WROOM-32 WiFi 模组（2.4G WiFi+蓝牙）
* 4 个指示灯（esp32 和 k210 串口发送接收指示灯）
* 2 个按钮（复位和启动选择(开机后可自定义功能)按钮）
* Type-C 接口
* Micro SD 卡槽
* 1 个 CH552 USB 转 TTL 芯片
* 2 个 FPC 座子（摄像头和屏幕）
* 1 个 Mic
* 1 个单声道音频功放（NS4150）
* 1 个 LCD 触摸屏幕（可选）
* 1 个 1.25mm 音频输出母座

## 注意

虽然外形和 `Pin` 兼容 `Arduino UNO R3`， 但是电平是不兼容的，这需要非常注意，否则可能造成板子损坏！

`Maixduino`支持 `3.3V` 和 `1.8V` 电平， 并且引脚被分为几个 `BANK`， 每个`BANK`可以通过软件设置电压为`1.8V` 或者`3.3V`，
但是， 这些**引脚都不是 `5V` 耐受的**。

所以，在使用 `Arduino` 的外设器件时一定要注意，不要将`5V`短接到引脚或者`RST`（`1.8V`）引脚， 否则可能导致板子损坏！

> 比如这款[Base Shield V2扩展板](http://wiki.seeedstudio.com/Base_Shield_V2/)：
> 
> ![](https://cdn.sipeed.com/wiki/maix/board/seeed_base_shield_v2_2.png)
> ![](https://cdn.sipeed.com/wiki/maix/board/seeed_base_shield_v2.png)
> 
> 如上图的设计可以看到，由于扩展板设计了兼容 `5V` 和 `3.3V` 设计， 所以**一定不要**将开关拨到 `5V` 处， 否则板子将会被损坏！
> 
> 对于这个扩展板，如果一定要防止自己这个问题发生，鉴于上面的电路图，可以把转接板的 `RST` 引脚减掉或者将电阻 `R2` 焊掉。 当然，这只能防止扩展版上没有接任何器件的时候不出问题！





## 组装

注意摄像头和屏幕的安装方向，否则可能无法工作或损坏器件

摄像头朝背面：

![](https://cdn.sipeed.com/wiki/maix/board/maixduino_00.png)

屏幕朝正面

![](https://cdn.sipeed.com/wiki/maix/board/maixduino_01.png)

## 资料

* [引脚图 PNG 下载](https://cdn.sipeed.com/wiki/maix/maixduino/maixduino_pins.png)
* 规格书（包含引脚连接表格）：[Specifications](http://dl.sipeed.com/MAIX/HDK/Maixduino/Specifications/)
* 硬件资料： [dl.sipeed.com](http://dl.sipeed.com/MAIX/HDK/Maixduino/)
* [SDK](../sdk/README.md)： 适用于 k210 系列所有 SDK


