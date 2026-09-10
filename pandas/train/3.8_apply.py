"""
3.8 Pandas 的 apply 函数与向量化 —— 练习

知识点回顾：
    1. Series.apply(func)：func 的参数是 Series 中的一个元素
       - 可传 lambda；传带参数的函数时，额外参数必须用关键字传参，如 s.apply(func1, p1=3)
    2. DataFrame.apply(func, axis=0/1)：
       - axis=0（默认）按列处理，func 收到的是每一列（Series），对列做统计
       - axis=1 按行处理，func 收到的是每一行（Series），可同时访问一行中的多列
    3. 向量化：当函数里用 if 判断向量时（如 y == 0）会报错，
       可用 np.vectorize() 把标量函数向量化，或直接用 @np.vectorize 装饰器

说明：把下面每个函数中的 pass 替换成自己的实现，函数返回题目要求的结果。
"""

import numpy as np
import pandas as pd


def ex1():
    """
    练习1：Series 的 apply
    定义 func(item) 返回 item * 20，对 pd.Series([10, 20, 30]) 调用 apply
    返回结果列表
    预期：[200, 400, 600]
    """
    pass


def ex2():
    """
    练习2：用 lambda 表达式实现与练习1相同的效果
    返回结果列表
    预期：[200, 400, 600]
    """
    pass


def ex3():
    """
    练习3：传入带参数的函数
    定义 func1(item, p1) 返回 item * p1，对 pd.Series([10, 20, 30]) 调用 apply，p1=3
    返回结果列表
    预期：[30, 60, 90]
    """
    pass


def ex4():
    """
    练习4：DataFrame 的 apply（axis=0）
    df = pd.DataFrame({"a": [10, 20, 30], "b": [40, 50, 60]})
    对每列求和（func 接收每一列 Series，返回 s.sum()），返回结果列表
    预期：[60, 150]
    """
    pass


def ex5():
    """
    练习5：DataFrame 的 apply（axis=1）
    基于同样的 df，对每行求和，返回结果列表
    预期：[50, 70, 90]
    """
    pass


def ex6():
    """
    练习6：apply(axis=1) 同时使用一行中的两列
    df = pd.DataFrame({"a": [10, 20, 30], "b": [40, 50, 60]})
    定义 func(s) 返回 s["a"] / s["b"]，按行应用，返回结果列表
    预期：[0.25, 0.4, 0.5]
    """
    pass


def ex7():
    """
    练习7：用 np.vectorize() 向量化
    def f(x, y): 若 y == 0 返回 np.nan，否则返回 x / y
    df = pd.DataFrame({"a": [10, 20, 30], "b": [40, 0, 60]})
    返回 f_vec(df["a"], df["b"]) 的结果列表
    预期：[0.25, nan, 0.5]
    """
    pass


def ex8():
    """
    练习8：用 @np.vectorize 装饰器实现与练习7相同的效果
    返回结果列表
    预期：[0.25, nan, 0.5]
    """
    pass


def ex9():
    """
    练习9：综合应用
    s = pd.Series([95, 85, 72, 60, 45])，定义一个把分数转成等级的函数：
        >=90 -> 'A'，>=80 -> 'B'，>=70 -> 'C'，>=60 -> 'D'，否则 'E'
    用 apply 转换，返回等级列表
    预期：['A', 'B', 'C', 'D', 'E']
    """
    pass


if __name__ == "__main__":
    # 完成后可取消注释逐一自测
    print("ex1:", ex1())
    # print("ex2:", ex2())
    # print("ex3:", ex3())
    # print("ex4:", ex4())
    # print("ex5:", ex5())
    # print("ex6:", ex6())
    # print("ex7:", ex7())
    # print("ex8:", ex8())
    # print("ex9:", ex9())
