"""
2.6 ndarray 切片和索引 —— 练习

知识点回顾：
    索引：arr[i] 取第 i 个元素（从 0 开始）
    切片：arr[start:stop:step]，不含 stop；也可用 slice(start, stop, step)
    二维数组：arr[行切片, 列切片]
    切片得到的是视图，修改它会影响到原数组；需要独立副本时用 .copy()

要求：把下面每个函数中 pass 替换成自己的实现，函数返回题目要求的结果。
"""

import numpy as np


def ex1():
    """
    练习1：arr = np.arange(10)
    返回元组 (arr[2], arr[2:9:2])
    预期：(2, array([2, 4, 6, 8]))
    """
    pass


def ex2():
    """
    练习2：arr = np.arange(10)
    要求用内置 slice 函数完成"从索引 2 开始到索引 9（不含）结束，间隔为 2"的切片，
    返回结果（预期 [2 4 6 8]）
    """
    pass


def ex3():
    """
    练习3：arr = np.arange(10)
    返回元组 (arr[2:], arr[2:9])
    预期：([2 3 4 5 6 7 8 9], [2 3 4 5 6 7 8])
    """
    pass


def ex4():
    """
    练习4：arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    返回元组 (第 2 行, 第 2 列, 前两行前两列组成的子数组)
    预期：([4 5 6], [2 5 8], [[1 2] [4 5]])
    """
    pass


def ex5():
    """
    练习5：验证切片是视图
    arr = np.arange(5)，执行 arr[1:3] = 0 后返回 arr
    预期：[0 0 0 3 4]
    """
    pass


def ex6():
    """
    练习6：切片的副本
    arr = np.arange(5)，用 .copy() 取 arr[1:3] 的副本 sub，
    修改 sub[:] = 100 后返回元组 (arr, sub)，
    验证修改副本不会影响原数组
    预期：(array([0, 1, 2, 3, 4]), array([100, 100]))
    """
    pass


if __name__ == "__main__":
    print("ex1:", ex1())
    # print("ex2:", ex2())
    # print("ex3:", ex3())
    # print("ex4:", ex4())
    # print("ex5:", ex5())
    # print("ex6:", ex6())
