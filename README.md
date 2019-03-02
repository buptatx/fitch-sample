# fitch-sample

这是一个用于描述如何使用 [fitch](https://github.com/williamfzc/fitch) 的示例工程。

## 使用

**只支持python3。**

### 安装与配置

```shell
git clone https://github.com/williamfzc/fitch-sample.git
cd fitch-sample
```

确保你的adb可用，且已经连接上android设备。

### 正常方式

在 `framework/config.py` 更新你的设备ID。之后运行：

```shell
pip install -r requirements.txt
python entry.py
```

### docker （只支持linux）

```shell
docker run --rm \
    --privileged \
    -v /dev/bus/usb:/dev/bus/usb \
    -v `pwd`:/usr/src/app \
    williamfzc/fitch
```

如果你需要更加细致的设备管理，可以通过 `--device`：

```shell
--device /dev/bus/usb/001:/dev/bus/usb/001:rwm
```

在实际项目中的应用可以参照 [doringland/ud4d](https://github.com/doringland/ud4d)。
