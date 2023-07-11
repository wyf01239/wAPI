# GraphCalc

数学图形计算器

支持:
- *四边形
- *三角形
- *(正)圆
- *正方体
- *长方体
- *圆锥
- *圆柱

带 ```*``` 的计划支持

调用: wapi.wMath.GraphCalc.```xxx```

```xxx``` (本子库支持的属性或方法):

# 目录结构

```python
wapi/wMath/GraphCalc/
    2/ # 二维图形
        Circle.py # 2.Circle()
    3/ # 三维
```

# 使用

## Circle

TODO: 重构图形计算器, 支持平面和立体图形计算

"**简单**"的圆算器

支持计算半径, 直径, 周长, 面积

提示: PAI 如不指定, 默认值为 3.14, 详见下面

出现错误时会被抛出, 注意处理错误 (除原版)

测试 Python 版本: **3.11.1**

### 使用:

1. 原版
    - 调用: wapi.CircleCalc.Original
    - 参数: 无
    - 返回: 无
    - ***Dobastickrn 提供的原版, 自带输入输出且无参数和返回, 不建议使用**

2. 半径求其他
    - 调用: wapi.CircleCalc.r_(r, pai = 3.14)
    - 参数
        - r: int / float
        - pai: int / float
    - 返回: tuple (直径(float), 周长(float), 面积(float))

3. 直径求其他
    - 调用: wapi.CircleCalc.d_(r, pai = 3.14)
    - 参数
        - d: int / float
        - pai: int / float
    - 返回: tuple (半径(float), 周长(float), 面积(float))

4. 周长求其他
    - 调用： wapi.CircleCalc.C_(C, pai = 3.14)
    - 参数
        - C: int / float
        - pai: int / float
    - 返回: tuple (半径(float), 直径(float), 面积(float))

5. 面积求其他
    - 调用： wapi.CircleCalc.S_(S, pai = 3.14)
    - 参数
        - S: int / float
        - pai: int / float
    - 返回: tuple (半径(float), 直径(float), 周长(float))
