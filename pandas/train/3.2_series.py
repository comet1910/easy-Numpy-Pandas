"""
3.2 Pandas 数据结构 —— Series —— 练习

知识点回顾：
    1. 创建：pd.Series(data, index=..., name=...)
       - 列表创建：默认索引为 0 ~ N-1 的整数
       - 可以同时指定索引（index）与名称（name）
       - 字典创建：字典的键作为索引，可用 index 参数选取子集
    2. 常用属性：index / values / ndim / shape / size / dtype / name
    3. 索引器：
       - loc[]  显式索引，按标签索引或切片（切片右端闭合）
       - iloc[] 隐式索引，按位置索引或切片（切片右端不闭合）
       - at[]   按标签访问单个元素
       - iat[]  按位置访问单个元素
    4. 常用方法：head / tail / isin / isna / sum / mean / min / max / var /
       std / median / mode / quantile / describe / value_counts / count /
       drop_duplicates / unique / nunique / sample / sort_index /
       sort_values / replace / to_frame / equals / keys / corr / cov / items
    5. 布尔索引：s[s > s.mean()]
    6. 运算：
       - 与标量运算：标量作用于每一个元素
       - 与 Series 运算：按标签对齐，标签没有匹配上的用 NaN 填充

说明：把下面每个函数中的 pass 替换成自己的实现，函数返回题目要求的结果。
"""

import numpy as np
import pandas as pd


def ex1():
    """
    练习1：用列表 [4, 7, -5, 3] 创建 Series
    返回该 Series
    预期：索引为 0~3，值为 4、7、-5、3，dtype 为 int64
    """
    pass


def ex2():
    """
    练习2：用列表 [4, 7, -5, 3] 创建 Series，索引为 ["a", "b", "c", "d"]，名称为 "hello_python"
    返回元组 (索引列表, 名称, 值列表)
    预期：(['a', 'b', 'c', 'd'], 'hello_python', [4, 7, -5, 3])
    """
    pass


def ex3():
    """
    练习3：用字典 {"a": 4, "b": 7, "c": -5, "d": 3} 创建 Series，
    再基于它创建只包含索引 ["a", "c"]、名称为 "aacc" 的 Series
    返回该子 Series
    预期：a 为 4，c 为 -5，Name: aacc，dtype: int64
    """
    pass


def ex4():
    """
    练习4：创建 s = pd.Series([11, 22, 33, 44, 55], name="atguigu", index=["a", "b", "c", "d", "e"])
    返回元组 (ndim, shape, size, dtype 字符串, name)
    预期：(1, (5,), 5, 'int64', 'atguigu')
    """
    pass


def ex5():
    """
    练习5：基于练习4的 Series，练习 label / position 索引
    返回元组：
        (s.loc["c"], s.loc["c":"d"] 的值列表, s.iloc[0], s.iloc[0:3] 的值列表, s.at["a"], s.iat[3])
    预期：(33, [33, 44], 11, [11, 22, 33], 11, 44)
    """
    pass


def ex6():
    """
    练习6：创建 arrs = pd.Series([11, 22, np.nan, None, 44, 22], index=["a", "b", "c", "d", "e", "f"])
    返回元组 (sum(), mean(), median(), mode() 的值列表, quantile(0.25, interpolation="midpoint"), count(), len())
    预期：(99.0, 24.75, 22.0, [22.0], 16.5, 4, 6)（None 也会被当作缺失值，非空元素只有 4 个）
    """
    pass


def ex7():
    """
    练习7：基于练习6的 arrs，练习去重相关方法
    返回元组 (drop_duplicates() 的值列表, unique() 的值列表, nunique())
    预期：([11.0, 22.0, nan, 44.0], [11.0, 22.0, nan, 44.0], 3)
    说明：缺失值只保留第一个；nunique() 不统计缺失值
    """
    pass


def ex8():
    """
    练习8：创建 s = pd.Series({"a": -1.2, "b": 3.5, "c": 6.8, "d": 2.9})
    使用布尔索引筛选出大于平均值的元素
    返回筛选结果的索引列表
    预期：['b', 'c']（平均值是 3.0）
    """
    pass


def ex9():
    """
    练习9：Series 与 Series 运算时的标签对齐
    s1 = pd.Series([1, 1, 1, 1])                      # 默认索引 0~3
    s2 = pd.Series([2, 2, 2, 2], index=[1, 2, 3, 4])
    返回 (s1 + s2) 的值列表
    预期：[nan, 3.0, 3.0, 3.0, nan]（索引 0 与 4 没有匹配上）
    """
    pass


def ex10():
    """
    练习10：相关系数 corr() 与协方差 cov()
    arr1 = pd.Series([1, 2, 3])
    arr3 = pd.Series([3, 2, 1])
    arr4 = pd.Series([6, 7, 8])
    返回元组 (round(arr1.corr(arr3), 2), round(arr1.corr(arr4), 2), round(arr1.cov(arr3), 2))
    预期：(-1.0, 1.0, -1.0)
    """
    pass


if __name__ == "__main__":
    # 完成后可取消注释逐一自测
    print("ex1:\n", ex1())
    # print("ex2:", ex2())
    # print("ex3:\n", ex3())
    # print("ex4:", ex4())
    # print("ex5:", ex5())
    # print("ex6:", ex6())
    # print("ex7:", ex7())
    # print("ex8:", ex8())
    # print("ex9:", ex9())
    # print("ex10:", ex10())
