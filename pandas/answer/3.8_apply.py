"""
3.8 Pandas 的 apply 函数与向量化 —— 答案
"""

import numpy as np
import pandas as pd


def ex1():
    def func(item):
        return item * 20

    return pd.Series([10, 20, 30]).apply(func).tolist()


def ex2():
    s = pd.Series([10, 20, 30])
    return s.apply(lambda item: item * 20).tolist()


def ex3():
    def func1(item, p1):
        return item * p1

    s = pd.Series([10, 20, 30])
    return s.apply(func1, p1=3).tolist()


def ex4():
    df = pd.DataFrame({"a": [10, 20, 30], "b": [40, 50, 60]})
    return df.apply(lambda s: s.sum(), axis=0).tolist()


def ex5():
    df = pd.DataFrame({"a": [10, 20, 30], "b": [40, 50, 60]})
    return df.apply(lambda s: s.sum(), axis=1).tolist()


def ex6():
    def func(s):
        return s["a"] / s["b"]

    df = pd.DataFrame({"a": [10, 20, 30], "b": [40, 50, 60]})
    return df.apply(func, axis=1).tolist()


def ex7():
    def f(x, y):
        if y == 0:
            return np.nan
        return x / y

    df = pd.DataFrame({"a": [10, 20, 30], "b": [40, 0, 60]})
    f_vec = np.vectorize(f)
    return f_vec(df["a"], df["b"]).tolist()


def ex8():
    @np.vectorize
    def f(x, y):
        if y == 0:
            return np.nan
        return x / y

    df = pd.DataFrame({"a": [10, 20, 30], "b": [40, 0, 60]})
    return f(df["a"], df["b"]).tolist()


def ex9():
    def grade(score):
        if score >= 90:
            return "A"
        if score >= 80:
            return "B"
        if score >= 70:
            return "C"
        if score >= 60:
            return "D"
        return "E"

    s = pd.Series([95, 85, 72, 60, 45])
    return s.apply(grade).tolist()


if __name__ == "__main__":
    print("ex1:", ex1())
    print("ex2:", ex2())
    print("ex3:", ex3())
    print("ex4:", ex4())
    print("ex5:", ex5())
    print("ex6:", ex6())
    print("ex7:", ex7())
    print("ex8:", ex8())
    print("ex9:", ex9())
