# CircleCalc

TODO: 重构图形计算器, 支持平面和立体图形计算

"**简单**"的圆算器

支持计算半径, 直径, 周长, 面积

提示: 程序默认设置 PAI 为 **3.14**, 详见下面

测试 Python 版本: **3.11.1**

## 使用:

1. 原版
    - 调用: wapi.CircleCalc.Original
    - 参数: 无
    - 返回: 无
    - ***Dobastickrn 提供的原版, 自带输入输出且无参数和返回, 不建议使用**

2. 半径求其他
    - 调用: wapi.CircleCalc.r(r)
    - 参数
        - r: int / float
    - 返回
        - 正常返回: tuple (直径(float), 周长(float), 面积(float))
        - 错误: None

3. 半径求其他 (自定义 PAI)
    - 调用: wapi.CircleCalc.r_(r, pai)
    - 参数
        - r: int / float
        - pai: int / float
    - 返回
        - 正常返回: tuple (直径(float), 周长(float), 面积(float))
        - 错误: None

4. 直径求其他
    - 调用: wapi.CircleCalc.d(d)
    - 参数
        - d: int / float
    - 返回
        - 正常返回: tuple (半径(float), 周长(float), 面积(float))
        - 错误: None

5. 直径求其他 (自定义 PAI)
    - 调用: wapi.CircleCalc.d_(r, pai)
    - 参数
        - d: int / float
        - pai: int / float
    - 返回
        - 正常返回: tuple (半径(float), 周长(float), 面积(float))
        - 错误: None

6. 周长求其他
    - 调用： wapi.CircleCalc.C(C)
    - 参数
        - C: int / float
    - 返回
        - 正常返回: tuple (半径(float), 直径(float), 面积(float))
        - 错误: None

7. 周长求其他 (自定义 PAI)
    - 调用： wapi.CircleCalc.C_(C, pai)
    - 参数
        - C: int / float
        - pai: int / float
    - 返回
        - 正常返回: tuple (半径(float), 直径(float), 面积(float))
        - 错误: None

8. 面积求其他
    - 调用： wapi.CircleCalc.S(S)
    - 参数
        - S: int / float
    - 返回
        - 正常返回: tuple (半径(float), 直径(float), 周长(float))
        - 错误: None

9. 面积求其他 (自定义 PAI)
    - 调用： wapi.CircleCalc.S_(S, pai)
    - 参数
        - S: int / float
        - pai: int / float
    - 返回
        - 正常返回: tuple (半径(float), 直径(float), 周长(float))
        - 错误: None