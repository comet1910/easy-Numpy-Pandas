"""
2.3 ndarray 的属性 —— 练习

知识点回顾：
    ndim      维度（几维数组）
    shape     形状（每个维度上有多少个元素）
    size      元素总个数
    dtype     元素的数据类型
    itemsize  每个元素占用的字节数

要求：把下面每个函数中 pass 替换成自己的实现，函数返回题目要求的结果。
"""

import numpy as np


def ex1():
    """
    练习1：创建二维数组 [[1, 2, 3], [4, 5, 6]]
    返回元组 (ndim, shape, size)
    预期：(2, (2, 3), 6)
    """
    pass


def ex2():
    """
    练习2：创建二维数组 [[1, 2, 3], [4, 5, 6]]
    返回元组 (dtype, itemsize)（提示：dtype 用 str() 转成字符串便于比较）
    预期：('int64', 8)，32 位系统上 itemsize 可能是 4
    """
    pass


def ex3():
    """
    练习3：创建三维数组 np.arange(24).reshape(2, 3, 4)
    返回元组 (ndim, shape, size)
    预期：(3, (2, 3, 4), 24)
    """
    pass


def ex4():
    """
    练习4：创建浮点数组 np.array([1.5, 2.5])
    返回元组 (ndim, shape, size, dtype, itemsize)
    预期：(1, (2,), 2, 'float64', 8)
    """
    pass


def ex5():
    """
    练习5：一维数组 np.array([1, 2, 3]) 和二维数组 np.array([[1, 2, 3]]) 的 ndim 分别是多少？
    返回元组 (一维的 ndim, 二维的 ndim)
    预期：(1, 2)
    """
    pass


if __name__ == "__main__":
    # 完成后可取消注释逐一自测
    print("ex1:", ex1())
    # print("ex2:", ex2())
    # print("ex3:", ex3())
    # print("ex4:", ex4())
    # print("ex5:", ex5())
