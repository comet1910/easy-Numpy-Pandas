"""
2.4 ndarray 的创建方式 —— 练习

知识点回顾：
    np.array() / np.asarray()     由序列创建，array 会 copy，asarray 传入 ndarray 时不 copy
    np.zeros / np.ones / np.empty 以及 zeros_like / ones_like / empty_like
    np.full / np.full_like
    np.arange(start, stop, step)
    np.linspace / np.logspace
    np.random.rand / randint / uniform / randn
    np.matrix

要求：把下面每个函数中 pass 替换成自己的实现，函数返回题目要求的结果。
"""

import numpy as np


def ex1():
    """
    练习1：array 与 asarray 的 copy 行为
    先 arr = np.array([1, 2, 3])，
    再分别用 np.array(arr) 和 np.asarray(arr) 得到 arr_copy、arr_view，
    返回元组 (arr_copy 与 arr 是否共享内存, arr_view 与 arr 是否共享内存)
    提示：np.shares_memory(a, b)
    预期：(False, True)
    """
    pass


def ex2():
    """
    练习2：用 np.zeros 创建形状 (2, 5) 的全 0 数组 arr1，
    再用 np.ones_like(arr1) 创建同形状的全 1 数组，
    返回两者相加的结果（应为一个 (2, 5) 全 1 的数组）
    """
    pass


def ex3():
    """
    练习3：用 np.full((3, 2), 7) 创建数组并返回
    """
    pass


def ex4():
    """
    练习4：用 np.arange(0, 20, 3) 创建一维数组并返回
    预期：[ 0  3  6  9 12 15 18]
    """
    pass


def ex5():
    """
    练习5：
        arr1 = np.linspace(0, 10, 5)                    默认 endpoint=True
        arr2 = np.linspace(0, 10, 5, endpoint=False)    不包含终点
    返回元组 (arr1, arr2)
    预期：arr1 = [ 0. 2.5 5. 7.5 10.]，arr2 = [0. 2. 4. 6. 8.]
    """
    pass


def ex6():
    """
    练习6：用 np.logspace(start=2, stop=5, num=5, base=2) 创建等比数列并返回
    预期：[ 4.  6.72717132 11.3137085 19.02731384 32. ]
    """
    pass


def ex7():
    """
    练习7：随机数组（先执行 np.random.seed(0) 保证结果可复现）
        arr1 = np.random.randint(0, 10, (2, 3))   随机整数
        arr2 = np.random.uniform(3, 6, (2, 3))    随机浮点数
        arr3 = np.random.randn(2, 3)              标准正态分布
    返回元组 (arr1.shape, arr2.shape, arr3.shape)，应当都是 (2, 3)
    """
    pass


def ex8():
    """
    练习8：用 np.matrix("1 2; 3 4") 创建矩阵并返回它的值（np.asarray 转成普通数组）
    预期：[[1 2]
           [3 4]]
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
