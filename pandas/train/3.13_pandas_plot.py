"""
3.13 Pandas 可视化 —— 练习

知识点回顾：
    pandas 的绘图底层依赖 Matplotlib，可直接在 Series/DataFrame 上调用 plot 方法。
    1. 单变量：
       - 柱状图：series.plot.bar()          （对比各类别数量）
       - 折线图：series.plot()              （展示趋势；常配合 sort_index()）
       - 面积图：series.plot.area()         （折线图填充线下的区域）
       - 直方图：series.plot.hist()         （展示分布）
       - 饼状图：series.plot.pie()          （展示占比）
    2. 双变量：
       - 散点图：df.plot.scatter(x=..., y=...)            （看两变量的相关趋势）
       - 蜂窝图：df.plot.hexbin(x=..., y=..., gridsize=10)（大量点看密度）
    3. 多系列：先 pivot_table 得到交叉表，再 pt.plot.bar(stacked=True) 画堆叠柱状图，
       或 pt.plot.line() 画多条折线
    4. 常见技巧：
       - pd.cut(值, bins).value_counts() 统计各分箱的频次
       - 建议显式创建画布并把 ax 传给 plot：fig, ax = plt.subplots(); s.plot.bar(ax=ax)
         （否则 pandas 会复用当前坐标轴，多题连跑时结果会相互叠加）
       - 常用校验：len(ax.patches) 柱/扇形数，len(ax.lines) 折线数，
         len(ax.collections) 散点/多边形集合数

说明：
    下面的 _sleep() 从 data/sleep.csv 加载睡眠数据（400 行，教材原示例数据）。
    你只需要把每个练习函数中的 pass 替换成自己的实现，函数返回题目要求的结果
    （这些返回值便于自测校验；如果想看图，可在 __main__ 中调用 plt.show()）。
"""

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

DATA_DIR = Path(__file__).resolve().parents[2] / "data"


def _sleep():
    """从 data/sleep.csv 加载睡眠数据（400 行）"""
    return pd.read_csv(DATA_DIR / "sleep.csv")


def ex1():
    """
    练习1：柱状图 plot.bar()
    df = _sleep()
    counts = pd.cut(df["sleep_duration"], [0, 5, 6, 7, 8, 9, 10, 11, 12]).value_counts()
    fig, ax = plt.subplots(); counts.plot.bar(ax=ax)
    返回柱形（patches）个数
    预期：8
    """
    pass


def ex2():
    """
    练习2：折线图 plot()
    counts = pd.cut(df["sleep_duration"], [0, 5, 6, 7, 8, 9, 10, 11, 12]).value_counts().sort_index()
    fig, ax = plt.subplots(); counts.plot(ax=ax)
    返回元组 (排序后的频次列表, 折线条数)
    预期：([61, 47, 43, 43, 47, 53, 61, 45], 1)
    """
    pass


def ex3():
    """
    练习3：面积图 plot.area()
    在练习2的 counts 上调用 counts.plot.area(ax=ax)
    返回元组 (Axes 类型名, collections 个数)
    预期：("Axes", 1)
    """
    pass


def ex4():
    """
    练习4：直方图 plot.hist()
    fig, ax = plt.subplots(); df["sleep_duration"].value_counts().plot.hist(ax=ax)
    返回柱形（patches）个数
    预期：10
    """
    pass


def ex5():
    """
    练习5：饼状图 plot.pie()
    counts = pd.cut(df["sleep_duration"], [0, 5, 6, 7, 8, 9, 10, 11, 12]).value_counts().sort_index()
    fig, ax = plt.subplots(); counts.plot.pie(ax=ax)
    返回扇形（patches）个数
    预期：8
    """
    pass


def ex6():
    """
    练习6：散点图 df.plot.scatter()
    fig, ax = plt.subplots()
    df.plot.scatter(x="sleep_duration", y="sleep_quality", ax=ax)
    返回散点个数（提示：ax.collections[0].get_offsets().shape[0]）
    预期：400
    """
    pass


def ex7():
    """
    练习7：蜂窝图 df.plot.hexbin()
    fig, ax = plt.subplots()
    df.plot.hexbin(x="sleep_duration", y="sleep_quality", gridsize=10, ax=ax)
    返回 collections 个数
    预期：1
    """
    pass


def _pt():
    """
    练习8、9 共用的交叉表：
    df["sleep_quality_stage"] = pd.cut(df["sleep_quality"], range(11))
    df["sleep_duration_stage"] = pd.cut(df["sleep_duration"], [0, 5, 6, 7, 8, 9, 10, 11, 12])
    pt = df.pivot_table(values="person_id", index="sleep_quality_stage",
                        columns="sleep_duration_stage", aggfunc="count")
    """
    pass


def ex8():
    """
    练习8：堆叠柱状图 plot.bar(stacked=True)
    先实现 _pt() 得到交叉表，再 fig, ax = plt.subplots(); pt.plot.bar(stacked=True, ax=ax)
    返回元组 (pt 的二维计数之和，空值不计, 柱形 patches 个数)
    提示：计数之和用 int(np.nansum(pt.values))
    预期：(400, 80)
    """
    pass


def ex9():
    """
    练习9：折线图 plot.line()
    在练习8的 pt 上调用 pt.plot.line(ax=ax)，返回折线条数
    预期：8
    """
    pass


if __name__ == "__main__":
    # 完成后可取消注释逐一自测
    print("ex1:", ex1())
    # print("ex2:", ex2())
    # print("ex3:", ex3())
    # print("ex4:", ex4())
    # print("ex5:", ex5())
    # print("ex6:", ex6())
    # print("ex7:", ex7())
    # print("ex8:", ex8())
    # print("ex9:", ex9())
    # plt.show()  # 想看图形时取消注释
