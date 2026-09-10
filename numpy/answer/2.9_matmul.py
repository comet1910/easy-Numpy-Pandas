"""
2.9 矩阵乘法 —— 参考答案
"""

import numpy as np


def ex1():
    """对位乘法：* 与 np.multiply"""
    arr1 = np.array([[1, 2, 3], [4, 5, 6]])
    arr2 = np.array([[6, 5, 4], [3, 2, 1]])
    return arr1 * arr2, np.multiply(arr1, arr2)


def ex2():
    """矩阵乘法：np.dot / ndarray.dot / @"""
    arr1 = np.array([[1, 2, 3], [4, 5, 6]])
    arr2 = np.array([[6, 5], [4, 3], [2, 1]])
    return np.dot(arr1, arr2), arr1.dot(arr2), arr1 @ arr2


def ex3():
    """二维 @ 一维"""
    arr1 = np.array([[1, 2, 3], [4, 5, 6]])
    arr3 = np.array([6, 5, 4])
    return arr1 @ arr3


def ex4():
    """手写双重循环实现矩阵乘法"""
    arr1 = np.array([[1, 2, 3], [4, 5, 6]])
    arr2 = np.array([[6, 5], [4, 3], [2, 1]])
    rows, cols = arr1.shape[0], arr2.shape[1]
    result = np.zeros((rows, cols), dtype=arr1.dtype)
    for i in range(rows):
        for j in range(cols):
            result[i, j] = np.sum(arr1[i, :] * arr2[:, j])
    return result


def ex5():
    """形状不满足矩阵乘法时抛出异常"""
    arr1 = np.array([[1, 2, 3], [4, 5, 6]])
    try:
        arr1 @ arr1
    except Exception as e:
        return type(e).__name__


if __name__ == "__main__":
    print("ex1:", ex1())
    print("ex2:", ex2())
    print("ex3:", ex3())
    print("ex4:\n", ex4())
    print("ex5:", ex5())
