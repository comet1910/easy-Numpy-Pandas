"""
2.4 ndarray 的创建方式 —— 参考答案
"""

import numpy as np


def ex1():
    """验证 array 与 asarray 的 copy 行为，返回 (是否共享内存, 是否共享内存)"""
    arr = np.array([1, 2, 3])
    arr_copy = np.array(arr)
    arr_view = np.asarray(arr)
    return np.shares_memory(arr_copy, arr), np.shares_memory(arr_view, arr)


def ex2():
    """zeros((2, 5)) 与 ones_like 相加"""
    arr1 = np.zeros((2, 5))
    arr2 = np.ones_like(arr1)
    return arr1 + arr2


def ex3():
    """np.full((3, 2), 7)"""
    return np.full((3, 2), 7)


def ex4():
    """np.arange(0, 20, 3)"""
    return np.arange(0, 20, 3)


def ex5():
    """linspace 的 endpoint 参数"""
    arr1 = np.linspace(start=0, stop=10, num=5)
    arr2 = np.linspace(start=0, stop=10, num=5, endpoint=False)
    return arr1, arr2


def ex6():
    """np.logspace(start=2, stop=5, num=5, base=2)"""
    return np.logspace(start=2, stop=5, num=5, base=2)


def ex7():
    """随机数组的 shape"""
    np.random.seed(0)
    arr1 = np.random.randint(0, 10, (2, 3))
    arr2 = np.random.uniform(3, 6, (2, 3))
    arr3 = np.random.randn(2, 3)
    return arr1.shape, arr2.shape, arr3.shape


def ex8():
    """np.matrix("1 2; 3 4")"""
    arr = np.matrix("1 2; 3 4")
    return np.asarray(arr)


if __name__ == "__main__":
    print("ex1:", ex1())
    print("ex2:\n", ex2())
    print("ex3:\n", ex3())
    print("ex4:", ex4())
    print("ex5:", ex5())
    print("ex6:", ex6())
    print("ex7:", ex7())
    print("ex8:\n", ex8())
