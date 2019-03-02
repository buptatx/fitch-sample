# fitch-sample

这是一个用于描述如何使用 [fitch](https://github.com/williamfzc/fitch) 的示例工程。

## 使用

**只支持python3。**

### 安装与配置

```shell
git clone https://github.com/williamfzc/fitch-sample.git
cd fitch-sample
```

### 正常方式

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
