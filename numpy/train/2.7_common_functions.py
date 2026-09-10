"""
2.7 numpy 常用函数 —— 练习

知识点回顾：
    基本函数：np.abs / np.ceil / np.floor / np.rint / np.isnan / np.multiply / np.divide / np.where
    统计函数：np.mean / np.sum / np.max / np.min / np.std / np.var / np.argmax / np.argmin /
              np.cumsum / np.cumprod，可用 axis 指定轴（axis=0 按列，axis=1 按行）
    比较函数：np.any / np.all
    排序函数：ndarray.sort() 就地排序；np.sort() 返回副本；axis 默认 -1
    去重函数：np.unique()

要求：把下面每个函数中 pass 替换成自己的实现，函数返回题目要求的结果。
随机数相关的题目请先调用 np.random.seed(0) 保证可复现。
"""

import numpy as np


def ex1():
    """
    练习1（基本函数）：arr = np.array([-1.5, 2.3, -3.7])
    返回元组 (np.abs(arr), np.ceil(arr), np.floor(arr), np.rint(arr))
    预期：(array([1.5, 2.3, 3.7]), array([-1.,  3., -3.]),
           array([-2.,  2., -4.]), array([-2.,  2., -4.]))
    """
    pass


def ex2():
    """
    练习2（基本函数）：arr = np.array([1, 2, 3, 4])
    返回元组 (np.multiply(arr, 2), np.divide(arr, arr), np.where(arr > 2, 1, 0))
    预期：([2 4 6 8], [1. 1. 1. 1.], [0 0 1 1])
    """
    pass


def ex3():
    """
    练习3（统计函数）：np.random.seed(0) 后 arr = np.random.randint(1, 5, (2, 3))
    返回元组 (np.mean(arr), np.sum(arr), np.max(arr), np.min(arr))
    注意返回的是整体统计的标量
    """
    pass


def ex4():
    """
    练习4（统计函数 + axis）：arr = np.array([[1, 2, 3], [4, 5, 6]])
    返回元组 (按列求和, 按行求和, 按列求均值, 按行求最大值)
    预期：([5 7 9], [ 6 15], [2.5 3.5 4.5], [3 6])
    """
    pass


def ex5():
    """
    练习5（arg 与累积函数）：arr = np.array([[1, 2, 3], [4, 5, 6]])
    返回元组 (np.argmax(arr), np.argmin(arr), np.cumsum(arr), np.cumprod(arr, axis=1))
    预期：(5, 0, [ 1  3  6 10 15 21], [[  1   2   6] [  4  20 120]])
    """
    pass


def ex6():
    """
    练习6（比较函数）：arr = np.array([1, 2, 3, 4, 5])
    返回元组 (np.any(arr > 3), np.all(arr > 3))
    预期：(np.True_, np.False_)
    """
    pass


def ex7():
    """
    练习7（排序函数）：
        arr = np.array([[6, 5, 4], [3, 1, 2]])
        sorted_copy = np.sort(arr)     不修改原数组，返回副本
        arr_copy = arr.copy() 后调用 arr_copy.sort(axis=0)  按列就地排序
    返回元组 (sorted_copy, arr, arr_copy)
    其中 arr 应保持原样；sorted_copy 按行排序；arr_copy 按列排序
    预期：sorted_copy = [[4 5 6] [1 2 3]]
          arr         = [[6 5 4] [3 1 2]]
          arr_copy    = [[3 1 2] [6 5 4]]
    """
    pass


def ex8():
    """
    练习8（去重函数）：arr = np.array([[3, 1, 3], [1, 2, 2]])
    返回 np.unique(arr)
    预期：[1 2 3]
    """
    pass


if __name__ == "__main__":
    print("ex1:", ex1())
    # print("ex2:", ex2())
    # print("ex3:", ex3())
    # print("ex4:", ex4())
    # print("ex5:", ex5())
    # print("ex6:", ex6())
    # print("ex7:", ex7())
    # print("ex8:", ex8())
