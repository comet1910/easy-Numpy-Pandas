"""
2.3 ndarray 的属性 —— 参考答案
"""

import numpy as np


def ex1():
    """创建二维数组 [[1, 2, 3], [4, 5, 6]]，返回 (ndim, shape, size)"""
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    return arr.ndim, arr.shape, arr.size


def ex2():
    """返回 (dtype, itemsize)"""
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    return str(arr.dtype), arr.itemsize


def ex3():
    """创建三维数组 np.arange(24).reshape(2, 3, 4)，返回 (ndim, shape, size)"""
    arr = np.arange(24).reshape(2, 3, 4)
    return arr.ndim, arr.shape, arr.size


def ex4():
    """创建浮点数组 np.array([1.5, 2.5])，返回 (ndim, shape, size, dtype, itemsize)"""
    arr = np.array([1.5, 2.5])
    return arr.ndim, arr.shape, arr.size, str(arr.dtype), arr.itemsize


def ex5():
    """返回 (一维的 ndim, 二维的 ndim)"""
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([[1, 2, 3]])
    return arr1.ndim, arr2.ndim


if __name__ == "__main__":
    print("ex1:", ex1())
    print("ex2:", ex2())
    print("ex3:", ex3())
    print("ex4:", ex4())
    print("ex5:", ex5())
