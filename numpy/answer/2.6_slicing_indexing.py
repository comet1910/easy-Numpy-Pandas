"""
2.6 ndarray 切片和索引 —— 参考答案
"""

import numpy as np


def ex1():
    """arr[2] 与 arr[2:9:2]"""
    arr = np.arange(10)
    return arr[2], arr[2:9:2]


def ex2():
    """用 slice 函数切片"""
    arr = np.arange(10)
    return arr[slice(2, 9, 2)]


def ex3():
    """arr[2:] 与 arr[2:9]"""
    arr = np.arange(10)
    return arr[2:], arr[2:9]


def ex4():
    """二维数组：第 2 行、第 2 列、前两行前两列"""
    arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    return arr2[1], arr2[:, 1], arr2[0:2, 0:2]


def ex5():
    """验证切片是视图，修改会影响原数组"""
    arr = np.arange(5)
    arr[1:3] = 0
    return arr


def ex6():
    """验证 copy 副本不影响原数组"""
    arr = np.arange(5)
    sub = arr[1:3].copy()
    sub[:] = 100
    return arr, sub


if __name__ == "__main__":
    print("ex1:", ex1())
    print("ex2:", ex2())
    print("ex3:", ex3())
    print("ex4:", ex4())
    print("ex5:", ex5())
    print("ex6:", ex6())
