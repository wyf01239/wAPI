# CheckLib

检测用户是否安装了指定的 Python 库, 如未安装则自动安装

测试 Python 版本: **3.11.1**

**PS: 不能省略参数**

TODO: 重构模块

## 调用: 

wapi.CheckLib.wMain (name, file, url, urliswhl)

参数:
- name: str, 库名称, (最好)能在 Pypl 上搜索到
- file: str, 本地安装文件 (whl / tar.gz) 地址, 格式: "./xxx/xxx/xxx.tar.gz" or "./xxx/xxx/xxx.whl"
- url: str, 自定义安装文件下载地址, 文件后缀只能为 .whl 或 .tar.gz
- urliswhl: True / False, 指定下载地址指向的文件是否为 .whl 格式, 如此参数为 False 代表下载地址指向的文件为 .tar.gz 格式

PS: 
- 从指定 URL 安装仅在 Windows 10 21H1 及以上可用
- <del>如果不想指定安装文件或下载地址, 请设置为 None.</del>

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
from wapi import CheckLib as wCL
test = wCL.wMain("pygame", "./Libs/pygame.whl", "http://localhost/pygame.whl", True)
print ("Return: "test)
```

返回:

```python
Return: -1
```