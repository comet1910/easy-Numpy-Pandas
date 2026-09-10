"""
3.13 Pandas 可视化 —— 答案

说明：下面每个练习都用 fig, ax = plt.subplots() 新建一块画布，并把 ax 传给
pandas 的 plot 方法（ax=ax），这样各题互不影响，图形也是独立的。
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def _sleep():
    """内联数据（等价于教材 sleep.csv 的简化版，12 行）"""
    return pd.DataFrame({
        "person_id": list(range(1, 13)),
        "gender": ["F", "M", "F", "M", "F", "M", "F", "M", "F", "M", "F", "M"],
        "sleep_duration": [5.5, 6.5, 7.5, 4.5, 8.5, 6.0, 7.0, 5.0, 9.0, 6.8, 7.2, 5.8],
        "sleep_quality": [7, 8, 6, 5, 9, 7, 8, 6, 9, 7, 8, 5],
    })


def _duration_stage(df):
    """把睡眠时长按 [0,5,6,7,8,9,10,11,12] 分箱"""
    return pd.cut(df["sleep_duration"], [0, 5, 6, 7, 8, 9, 10, 11, 12])


def ex1():
    """
    练习1：柱状图 plot.bar()
    counts = _duration_stage(df).value_counts()
    fig, ax = plt.subplots(); counts.plot.bar(ax=ax)
    返回柱形（patches）个数
    预期：8
    """
    fig, ax = plt.subplots()
    _duration_stage(_sleep()).value_counts().plot.bar(ax=ax)
    return len(ax.patches)


def ex2():
    """
    练习2：折线图 plot()
    counts = _duration_stage(df).value_counts().sort_index()
    fig, ax = plt.subplots(); counts.plot(ax=ax)
    返回元组 (排序后的频次列表, 折线条数)
    预期：([2, 3, 3, 2, 2, 0, 0, 0], 1)
    """
    counts = _duration_stage(_sleep()).value_counts().sort_index()
    fig, ax = plt.subplots()
    counts.plot(ax=ax)
    return counts.tolist(), len(ax.lines)


def ex3():
    """
    练习3：面积图 plot.area()
    在练习2的 counts 上调用 counts.plot.area(ax=ax)
    返回元组 (Axes 类型名, collections 个数)
    预期：("Axes", 1)
    """
    counts = _duration_stage(_sleep()).value_counts().sort_index()
    fig, ax = plt.subplots()
    counts.plot.area(ax=ax)
    return type(ax).__name__, len(ax.collections)


def ex4():
    """
    练习4：直方图 plot.hist()
    fig, ax = plt.subplots(); df["sleep_duration"].value_counts().plot.hist(ax=ax)
    返回柱形（patches）个数
    预期：10
    """
    fig, ax = plt.subplots()
    _sleep()["sleep_duration"].value_counts().plot.hist(ax=ax)
    return len(ax.patches)


def ex5():
    """
    练习5：饼状图 plot.pie()
    counts = _duration_stage(df).value_counts().sort_index()
    fig, ax = plt.subplots(); counts.plot.pie(ax=ax)
    返回扇形（patches）个数
    预期：8
    """
    counts = _duration_stage(_sleep()).value_counts().sort_index()
    fig, ax = plt.subplots()
    counts.plot.pie(ax=ax)
    return len(ax.patches)


def ex6():
    """
    练习6：散点图 df.plot.scatter()
    fig, ax = plt.subplots()
    df.plot.scatter(x="sleep_duration", y="sleep_quality", ax=ax)
    返回散点个数
    预期：12
    """
    fig, ax = plt.subplots()
    _sleep().plot.scatter(x="sleep_duration", y="sleep_quality", ax=ax)
    return ax.collections[0].get_offsets().shape[0]


def ex7():
    """
    练习7：蜂窝图 df.plot.hexbin()
    fig, ax = plt.subplots()
    df.plot.hexbin(x="sleep_duration", y="sleep_quality", gridsize=10, ax=ax)
    返回 collections 个数
    预期：1
    """
    fig, ax = plt.subplots()
    _sleep().plot.hexbin(x="sleep_duration", y="sleep_quality", gridsize=10, ax=ax)
    return len(ax.collections)


def _pt():
    """练习8、9 共用的交叉表：行=睡眠质量分箱，列=睡眠时长分箱，值=人数"""
    df = _sleep()
    df["sleep_quality_stage"] = pd.cut(df["sleep_quality"], range(11))
    df["sleep_duration_stage"] = _duration_stage(df)
    return df.pivot_table(values="person_id", index="sleep_quality_stage",
                          columns="sleep_duration_stage", aggfunc="count")


def ex8():
    """
    练习8：堆叠柱状图 plot.bar(stacked=True)
    pt = _pt(); fig, ax = plt.subplots(); pt.plot.bar(stacked=True, ax=ax)
    返回元组 (pt 的二维计数之和，空值不计, 柱形 patches 个数)
    预期：(12, 80)
    """
    pt = _pt()
    fig, ax = plt.subplots()
    pt.plot.bar(stacked=True, ax=ax)
    return int(np.nansum(pt.values)), len(ax.patches)


def ex9():
    """
    练习9：折线图 plot.line()
    pt = _pt(); fig, ax = plt.subplots(); pt.plot.line(ax=ax)
    返回折线条数
    预期：8
    """
    pt = _pt()
    fig, ax = plt.subplots()
    pt.plot.line(ax=ax)
    return len(ax.lines)
