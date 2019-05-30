K210 development boards
============



| Board | WiFi | Bluetooth | USB to Serial | USB interface | Pin header type| power supply | Camera interface | LCD interface | On board Mic | Accelerometer | Audio PA | Micro SD card slot | RAM size | Flash size |
| ----- |  ---- | --- | -------------- | ------- | --------- | --- | -------- | ------- | ------- | ------ | ------- | ------------ | ------- | --------- |
| [Dock](dock.md)  ![](../../../assets/Dan_Dock.png) | No with `M1` module/ Yes with `M1W` module（esp8285） | No |  CH340 | Type-C | 2.54mm via | USB/External 5V supply | FPC interface | FPC interface | Yes | No | PAM8403(2 channel)  | Yes | 6+2MB | 16MB|
| [Bit](bit.md)  ![](../../../assets/BiT.png) | No | No |  CH340 on old version / CH552 on new version | Type-C | 2.54mm male pin | USB / External 5V supply | FPC | FPC | No/ Yes on new version | No | No | Yes | 6+2MB | 16MB|
| [Go](go.md)  ![](../../../assets/Go.jpg) | Yes（`esp8285`） | No |  STM32f103 simulate  | Type-C | 2.54mm male short pin | USB / 5V / Lithium battery powered  | FPC | FPC | Yes | MSA300 | PAM8403(2 channel) | Yes | 6+2MB | 16MB|
| [Maixduino](maixduino.md)  ![](../../../assets/maixduino_0.png) | Yes（esp32） | Yes（esp32） |  CH552 simulate | Type-C | 2.54mm female connector  | USB / DC-050 2.1mm 6V~12V | FPC | FPC | Yes | No | NS4150 single channel + 1.25mm connector | Yes | 6+2MB | 16MB|

