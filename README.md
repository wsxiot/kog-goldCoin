## 夜神模拟器王者荣耀刷金币
##### 使用步骤
- 下载夜神模拟器，在模拟器中下载王者荣耀
- 将夜神模拟器bin目录加入环境变量
- 打开夜神模拟器开发者选项
- 在开发者选项中打开调试
- 使用adb命令连接夜神模拟器，`adb connect 127.0.0.1:62001`
- 在kog.py中设置参数
- 在夜神模拟器中打开冒险模式，就是带更换阵容和闯关两个按钮的页面
- 运行kog.py程序
##### adb常用命令
- 截屏并保存
- `adb shell screencap -p /sdcard/temp.png`
- 将android上的图片发送到电脑当前目录上
- `adb pull /sdcard/autojump.png .`
- 模拟点击
- `adb shell input tap {x} {y}`
- 显示连接的设备
- `adb devices`
- adb使用socket连接设备
- `adb connect {host}:{port}`
##### 说明
- 参考 `https://github.com/tobyqin/kog-money`
- 本程序是冒险模式堕落的祸源-稷下战场