# wAPI / PyModules

这个文件夹存放 Python 的模块集合.

# wAPIMain.py

所有模块的集合

(还没弄)

## [wAPIgetChar.py](./wAPIgetChar.py)

获取单个字符输入

集合了 Windows / Linux 的方法

测试 Python 版本: **3.11.1**

返回单个字符: wAPIgetChar.wMain()

参数: 无

示例:

```python

import wAPIgetChar as wAPIgc
gc = wAPIgc.wMain
print(gc)

```

## [wAPIPrimeNum.py](./wAPIPrimeNum.py)

简单的质数判断器

测试 Python 版本: **3.11.1**

使用方法: wAPIPrimeNum.wMain(num)

参数类型: int

返回类型: True / False

示例:

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