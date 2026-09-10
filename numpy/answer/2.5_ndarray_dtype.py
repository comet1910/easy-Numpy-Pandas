"""
2.5 ndarray 的数据类型 —— 参考答案
"""

import numpy as np


def ex1():
    """np.array([1, 2, 3], dtype=np.float64)"""
    return np.array([1, 2, 3], dtype=np.float64)


def ex2():
    """np.array([0.2, 2.5, 4.8], dtype="i8")"""
    return np.array([0.2, 2.5, 4.8], dtype="i8")


def ex3():
    """float64 数组 astype(np.int64)"""
    arr1 = np.array([1, 2, 3], dtype=np.float64)
    return arr1.astype(np.int64)


def ex4():
    """np.arange(5) 默认 dtype，以及转 float32 后的 dtype"""
    arr = np.arange(5)
    return str(arr.dtype), str(arr.astype(np.float32).dtype)


if __name__ == "__main__":
    print("ex1:", ex1())
    print("ex2:", ex2())
    print("ex3:", ex3())
    print("ex4:", ex4())
