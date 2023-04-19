# wAPI / PyModules

这个文件夹存放 Python 的模块集合.

# wAPIMain.py

所有模块的集合

(还没弄)

# [wAPIgetChar.py](./wAPIgetChar.py)

获取单个字符输入

集合了 Windows / Linux 的方法

测试 Python 版本: **3.11.1**

返回单个字符: wAPIgetChar.wMain()

参数: 无

## 示例:

```python
import wAPIgetChar as wAPIgc
gc = wAPIgc.wMain
print(gc)
```

# [wAPIPrimeNum.py](./wAPIPrimeNum.py)

简单的质数判断器

测试 Python 版本: **3.11.1**

## 使用方法: 

wAPIPrimeNum.wMain(num)

参数类型: int

返回类型: True / False

## 示例:

```python
from encodings import utf_8
utf_8
import wAPIPrimeNum as wAPIpn

num = int(64)
ret = wAPIpn.wMain(num)
if ret == True:
    print (num0, " 是质数.")
else:
    print (num0, " 不是质数.")
return 0
```

示例输出:

```
64 不是质数.
```

# [wAPICircleCalc](./wAPICircleCalc.py)

"**简单**"的圆算器

支持计算半径, 直径, 周长, 面积

提示: 程序默认设置 PAI 为 **3.14**, 详见下面

测试 Python 版本: **3.11.1**

## 使用:

1. 原版
    - 调用: wAPICircleCalc.Original
    - 参数: 无
    - 返回: 无
    - ***Dobastickrn 提供的原版, 不建议使用**

2. 半径求其他
    - 调用: wAPICircleCalc.r(r)
    - 参数
        - r: int / float
    - 返回
        - 正常返回: tuple (直径(float), 周长(float), 面积(float))
        - 错误: tuple (0, 0, 0)

3. 半径求其他 (自定义 PAI)
    - 调用: wAPICircleCalc.r_(r, pai)
    - 参数
        - r: int / float
        - pai: int / float
    - 返回
        - 正常返回: tuple (直径(float), 周长(float), 面积(float))
        - 错误: tuple (0, 0, 0)

4. 直径求其他
    - 调用: wAPICircleCalc.d(d)
    - 参数
        - d: int / float
    - 返回
        - 正常返回: tuple (半径(float), 周长(float), 面积(float))
        - 错误: tuple (0, 0, 0)

5. 直径求其他 (自定义 PAI)
    - 调用: wAPICircleCalc.d_(r, pai)
    - 参数
        - d: int / float
        - pai: int / float
    - 返回
        - 正常返回: tuple (半径(float), 周长(float), 面积(float))
        - 错误: tuple (0, 0, 0)

6. 周长求其他
    - 调用： wAPICircleCalc.C(C)
    - 参数
        - C: int / float
    - 返回
        - 正常返回: tuple (半径(float), 直径(float), 面积(float))
        - 错误: tuple (0, 0, 0)

7. 周长求其他 (自定义 PAI)
    - 调用： wAPICircleCalc.C(C, pai)
    - 参数
        - C: int / float
        - pai: int / float
    - 返回
        - 正常返回: tuple (半径(float), 直径(float), 面积(float))
        - 错误: tuple (0, 0, 0)

# [wAPICheckLib.py](./wAPICheckLib.py)

检测用户是否安装了指定的 Python 库, 如未安装则自动安装

测试 Python 版本: **3.11.1**

## 调用: 

wAPICheckLib.wMain (name, file, url, urliswhl)

参数:
- name: str, 库名称, (最好)能在 Pypl 上搜索到
- file: str, 本地安装文件 (whl / tar.gz) 地址, 格式: "./xxx/xxx/xxx.tar.gz" or "./xxx/xxx/xxx.whl"
- url: str, 自定义安装文件下载地址, 文件后缀只能为 .whl 或 .tar.gz
- urliswhl: True / False, 指定下载地址指向的文件是否为 .whl 格式, 如此参数为 False 代表下载地址指向的文件为 .tar.gz 格式

PS: 
- 从指定 URL 安装仅在 Windows 10 21H1 及以上可用
- 如果不想指定安装文件或下载地址, 请设置为 None.

返回:
- -1: 已经安装
- 0: 未找到, 成功安装
- 1: 未找到, 安装失败

## 示例:

要安装的库: **pygame**

本地安装文件: \Libs\pygame.whl

下载 URL: http://localhost/pygame.whl
ps: 此处**假定用户已安装该库**
```python
import wAPICheckLib as wCL
test = wCL.wMain("pygame", "./Libs/pygame.whl", "http://localhost/pygame.whl", True)
print ("Return: "test)
```

返回:

```python
Return: -1
```