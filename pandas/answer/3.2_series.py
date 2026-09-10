"""
3.2 Pandas 数据结构 —— Series —— 参考答案
"""

import numpy as np
import pandas as pd


def ex1():
    """用列表创建 Series"""
    return pd.Series([4, 7, -5, 3])


def ex2():
    """指定索引与名称"""
    s = pd.Series([4, 7, -5, 3], index=["a", "b", "c", "d"], name="hello_python")
    return list(s.index), s.name, s.tolist()


def ex3():
    """字典创建 Series 并取子集"""
    dic = {"a": 4, "b": 7, "c": -5, "d": 3}
    s = pd.Series(dic)
    return pd.Series(s, index=["a", "c"], name="aacc")


def ex4():
    """常用属性"""
    s = pd.Series([11, 22, 33, 44, 55], name="atguigu", index=["a", "b", "c", "d", "e"])
    return s.ndim, s.shape, s.size, str(s.dtype), s.name


def ex5():
    """loc / iloc / at / iat"""
    s = pd.Series([11, 22, 33, 44, 55], name="atguigu", index=["a", "b", "c", "d", "e"])
    return s.loc["c"], s.loc["c":"d"].tolist(), s.iloc[0], s.iloc[0:3].tolist(), s.at["a"], s.iat[3]


def ex6():
    """常用统计方法"""
    arrs = pd.Series([11, 22, np.nan, None, 44, 22], index=["a", "b", "c", "d", "e", "f"])
    return (
        arrs.sum(),
        arrs.mean(),
        arrs.median(),
        arrs.mode().tolist(),
        arrs.quantile(0.25, interpolation="midpoint"),
        arrs.count(),
        len(arrs),
    )


def ex7():
    """去重相关方法"""
    arrs = pd.Series([11, 22, np.nan, None, 44, 22], index=["a", "b", "c", "d", "e", "f"])
    return arrs.drop_duplicates().tolist(), arrs.unique().tolist(), arrs.nunique()


def ex8():
    """布尔索引"""
    s = pd.Series({"a": -1.2, "b": 3.5, "c": 6.8, "d": 2.9})
    return s[s > s.mean()].index.tolist()


def ex9():
    """Series 与 Series 运算的标签对齐"""
    s1 = pd.Series([1, 1, 1, 1])
    s2 = pd.Series([2, 2, 2, 2], index=[1, 2, 3, 4])
    return (s1 + s2).tolist()


def ex10():
    """corr() 与 cov()"""
    arr1 = pd.Series([1, 2, 3])
    arr3 = pd.Series([3, 2, 1])
    arr4 = pd.Series([6, 7, 8])
    return round(arr1.corr(arr3), 2), round(arr1.corr(arr4), 2), round(arr1.cov(arr3), 2)


if __name__ == "__main__":
    print("ex1:\n", ex1())
    print("ex2:", ex2())
    print("ex3:\n", ex3())
    print("ex4:", ex4())
    print("ex5:", ex5())
    print("ex6:", ex6())
    print("ex7:", ex7())
    print("ex8:", ex8())
    print("ex9:", ex9())
    print("ex10:", ex10())
