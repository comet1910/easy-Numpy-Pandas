"""
2.8 基本运算（矢量化运算与广播）—— 参考答案
"""

import numpy as np


def ex1():
    """同形状数组的元素级运算"""
    arr1 = np.array([[1, 2, 3], [4, 5, 6]])
    arr2 = np.array([[7, 8, 9], [10, 11, 12]])
    return arr1 + arr2, arr1 - arr2, arr1 * arr2, arr1 / arr2


def ex2():
    """标量广播"""
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    return arr + 100, arr * 100


def ex3():
    """广播规则1：(3,) 与 (3, 1) 相加"""
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([[4], [5], [6]])
    return arr1 + arr2


def ex4():
    """广播规则1：(4,) 与 (3, 1) 相加后的形状"""
    arr1 = np.array([1, 2, 3, 4])
    arr2 = np.array([[10], [20], [30]])
    return (arr1 + arr2).shape


def ex5():
    """广播规则2：(1, 3) 与 (3, 1) 相加"""
    arr3 = np.array([[1, 2, 3]])
    arr4 = np.array([[4], [5], [6]])
    return arr3 + arr4


def ex6():
    """广播规则3：形状不兼容时抛出异常"""
    try:
        np.array([1, 2, 3]) + np.array([4, 5])
    except Exception as e:
        return type(e).__name__


if __name__ == "__main__":
    print("ex1:", ex1())
    print("ex2:", ex2())
    print("ex3:\n", ex3())
    print("ex4:", ex4())
    print("ex5:\n", ex5())
    print("ex6:", ex6())
