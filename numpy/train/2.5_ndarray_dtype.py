"""
2.5 ndarray 的数据类型 —— 练习

知识点回顾：
    创建数组时可用 dtype 参数指定类型，如 np.float64、"i8"
    ndarray.astype() 可以转换数组的元素类型

要求：把下面每个函数中 pass 替换成自己的实现，函数返回题目要求的结果。
"""

import numpy as np


def ex1():
    """
    练习1：创建 np.array([1, 2, 3], dtype=np.float64)
    返回该数组的值（预期 [1. 2. 3.]）
    """
    pass


def ex2():
    """
    练习2：创建 np.array([0.2, 2.5, 4.8], dtype="i8")
    返回该数组的值（浮点转整型会截断小数部分，预期 [0 2 4]）
    """
    pass


def ex3():
    """
    练习3：创建 arr1 = np.array([1, 2, 3], dtype=np.float64)，
    用 astype(np.int64) 转换为整型数组并返回
    预期：[1 2 3]
    """
    pass


def ex4():
    """
    练习4：np.arange(5) 默认的 dtype 是什么？把它转成 np.float32 后再返回新的 dtype
    返回元组 (默认 dtype 字符串, 转换后的 dtype 字符串)
    预期：('int64', 'float32')
    """
    pass


if __name__ == "__main__":
    print("ex1:", ex1())
    # print("ex2:", ex2())
    # print("ex3:", ex3())
    # print("ex4:", ex4())
