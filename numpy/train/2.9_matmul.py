"""
2.9 矩阵乘法 —— 练习

知识点回顾：
    * 和 np.multiply() 是元素对位相乘，不是矩阵乘法。
    np.dot()、ndarray.dot()、@ 才是矩阵乘法，
    要求第一个矩阵的列数等于第二个矩阵的行数。
    二维数组 @ 一维数组，结果是一维数组。

要求：把下面每个函数中 pass 替换成自己的实现，函数返回题目要求的结果。
"""

import numpy as np


def ex1():
    """
    练习1（对位乘法）：
        arr1 = np.array([[1, 2, 3], [4, 5, 6]])
        arr2 = np.array([[6, 5, 4], [3, 2, 1]])
    返回元组 (arr1 * arr2, np.multiply(arr1, arr2))，两者结果应相同
    预期：[[ 6 10 12]
           [12 10  6]]
    """
    pass


def ex2():
    """
    练习2（矩阵乘法）：
        arr1 = np.array([[1, 2, 3], [4, 5, 6]])          形状 (2, 3)
        arr2 = np.array([[6, 5], [4, 3], [2, 1]])        形状 (3, 2)
    用 np.dot()、ndarray.dot()、@ 三种方式各算一次，
    返回元组 (np.dot 结果, arr1.dot(arr2) 结果, arr1 @ arr2 结果)
    预期：[[20 14]
           [56 41]]
    """
    pass


def ex3():
    """
    练习3（二维 @ 一维）：
        arr1 = np.array([[1, 2, 3], [4, 5, 6]])
        arr3 = np.array([6, 5, 4])
    返回 arr1 @ arr3
    预期：[28 73]（1*6+2*5+3*4=28，4*6+5*5+6*4=73）
    """
    pass


def ex4():
    """
    练习4（手写矩阵乘法）：
        arr1 = np.array([[1, 2, 3], [4, 5, 6]])          形状 (2, 3)
        arr2 = np.array([[6, 5], [4, 3], [2, 1]])        形状 (3, 2)
    不用 np.dot / @，用双重循环（或三重循环）实现矩阵乘法，
    结果记为 result，返回 result
    预期：[[20 14]
           [56 41]]
    """
    pass


def ex5():
    """
    练习5（形状检查）：
        arr1 = np.array([[1, 2, 3], [4, 5, 6]])          形状 (2, 3)
    用 try/except 捕获"arr1 @ arr1"抛出的异常，返回异常类名（字符串）
    预期：'ValueError'（(2,3) 与 (2,3) 不满足第一个矩阵列数=第二个矩阵行数）
    """
    pass


if __name__ == "__main__":
    print("ex1:", ex1())
    # print("ex2:", ex2())
    # print("ex3:", ex3())
    # print("ex4:", ex4())
    # print("ex5:", ex5())
