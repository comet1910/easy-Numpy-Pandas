"""
2.7 numpy 常用函数 —— 参考答案
"""

import numpy as np


def ex1():
    """基本函数：abs / ceil / floor / rint"""
    arr = np.array([-1.5, 2.3, -3.7])
    return np.abs(arr), np.ceil(arr), np.floor(arr), np.rint(arr)


def ex2():
    """基本函数：multiply / divide / where"""
    arr = np.array([1, 2, 3, 4])
    return np.multiply(arr, 2), np.divide(arr, arr), np.where(arr > 2, 1, 0)


def ex3():
    """统计函数：整体统计"""
    np.random.seed(0)
    arr = np.random.randint(1, 5, (2, 3))
    return np.mean(arr), np.sum(arr), np.max(arr), np.min(arr)


def ex4():
    """统计函数：指定 axis"""
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    return np.sum(arr, axis=0), np.sum(arr, axis=1), np.mean(arr, axis=0), np.max(arr, axis=1)


def ex5():
    """arg 与累积函数"""
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    return np.argmax(arr), np.argmin(arr), np.cumsum(arr), np.cumprod(arr, axis=1)


def ex6():
    """比较函数：any / all"""
    arr = np.array([1, 2, 3, 4, 5])
    return np.any(arr > 3), np.all(arr > 3)


def ex7():
    """排序函数：np.sort 返回副本，ndarray.sort 就地排序"""
    arr = np.array([[6, 5, 4], [3, 1, 2]])
    sorted_copy = np.sort(arr)          # 返回副本，arr 不变
    arr_copy = arr.copy()
    arr_copy.sort(axis=0)               # 按列就地排序
    return sorted_copy, arr, arr_copy


def ex8():
    """去重函数：np.unique"""
    arr = np.array([[3, 1, 3], [1, 2, 2]])
    return np.unique(arr)


if __name__ == "__main__":
    print("ex1:", ex1())
    print("ex2:", ex2())
    print("ex3:", ex3())
    print("ex4:", ex4())
    print("ex5:", ex5())
    print("ex6:", ex6())
    print("ex7:", ex7())
    print("ex8:", ex8())
