"""
3.12 Matplotlib 可视化 —— 答案
数据源：data/weather.csv（教材原示例即使用 weather.csv）
"""

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

DATA_DIR = Path(__file__).resolve().parents[2] / "data"


def _weather():
    """从 data/weather.csv 加载逐日天气数据"""
    return pd.read_csv(DATA_DIR / "weather.csv")


def _data():
    """画直方图用的一维数据：weather.csv 的降水量 precipitation 列"""
    return _weather()["precipitation"]


def _year_color(x):
    """为不同年份的数据返回不同颜色"""
    if x.year == 2012:
        return "r"
    elif x.year == 2013:
        return "g"
    elif x.year == 2014:
        return "b"
    else:
        return "k"


def ex1():
    """
    练习1：状态接口绘制曲线
    x = np.linspace(0, 10, 100)，y = x ** 2
    用 plt.figure(figsize=(10, 6)) + plt.subplot(1, 1, 1) + plt.plot 绘制，
    并设置 plt.xlabel("x")、plt.ylabel("y")、plt.title("平方曲线")
    返回元组 (figure 的 axes 数量, xlabel, ylabel, title, 折线数据点个数)
    预期：(1, "x", "y", "平方曲线", 100)
    """
    x = np.linspace(0, 10, 100)
    plt.figure(figsize=(10, 6))
    plt.subplot(1, 1, 1)
    plt.plot(x, x ** 2)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("平方曲线")
    ax = plt.gca()
    return len(plt.gcf().axes), ax.get_xlabel(), ax.get_ylabel(), ax.get_title(), len(ax.lines[0].get_xdata())


def ex2():
    """
    练习2：面向对象接口创建多个子图
    x = np.linspace(0, 10, 100)，fig, ax = plt.subplots(2, figsize=(10, 6))
    ax[0] 画 sin(x) 标题 "sin"，ax[1] 画 cos(x) 标题 "cos"
    返回元组 (子图数量, ax[0] 标题, ax[1] 标题, ax[0] 折线数据点个数)
    预期：(2, "sin", "cos", 100)
    """
    x = np.linspace(0, 10, 100)
    fig, ax = plt.subplots(2, figsize=(10, 6))
    ax[0].plot(x, np.sin(x))
    ax[0].set_title("sin")
    ax[1].plot(x, np.cos(x))
    ax[1].set_title("cos")
    return len(ax), ax[0].get_title(), ax[1].get_title(), len(ax[0].lines[0].get_xdata())


def ex3():
    """
    练习3：直方图 hist
    fig, ax = plt.subplots()，ax.hist(_data(), bins=5)
    返回元组 (分组的组数, 每组频次列表, 柱形对象个数)
    预期：(5, [1329.0, 93.0, 28.0, 6.0, 5.0], 5)
    """
    fig, ax = plt.subplots()
    n, bins, patches = ax.hist(_data(), bins=5)
    return len(n), n.tolist(), len(patches)


def ex4():
    """
    练习4：直方图的频次之和与分组边界个数
    fig, ax = plt.subplots()，n, bins, _ = ax.hist(_data(), bins=5)
    返回元组 (频次之和, 边界个数)
    预期：(1461, 6)（等于 weather.csv 的行数）
    """
    fig, ax = plt.subplots()
    n, bins, _ = ax.hist(_data(), bins=5)
    return int(n.sum()), len(bins)


def ex5():
    """
    练习5：散点图 scatter
    x = [1, 2, 3, 4, 5]，y = [2, 4, 5, 4, 5]
    fig, ax = plt.subplots()，ax.scatter(x, y)，并设置 xlabel="x"、ylabel="y"
    返回元组 (collections 个数, 散点个数, xlabel)
    预期：(1, 5, "x")
    """
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 5, 4, 5]
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    return len(ax.collections), ax.collections[0].get_offsets().shape[0], ax.get_xlabel()


def ex6():
    """
    练习6：多变量散点图——按年份着色
    读取 weather.csv，用 df["date"].apply(_year_color) 生成 color 列，
    再用 ax.scatter(df["temp_max"], df["precipitation"], c=df["color"], alpha=0.5) 绘制
    返回元组 (color 取值计数字典, collections 个数)
    预期：({'r': 366, 'g': 365, 'b': 365, 'k': 365}, 1)
    """
    df = _weather()
    df["date"] = pd.to_datetime(df["date"])
    df["color"] = df["date"].apply(_year_color)
    fig, ax = plt.subplots()
    ax.scatter(df["temp_max"], df["precipitation"], c=df["color"], alpha=0.5)
    return df["color"].value_counts().to_dict(), len(ax.collections)


def ex7():
    """
    练习7：设置画布大小
    fig, ax = plt.subplots(figsize=(10, 6))
    返回 fig.get_size_inches() 转成的浮点数列表
    预期：[10.0, 6.0]
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    return [float(v) for v in fig.get_size_inches()]


def ex8():
    """
    练习8：设置坐标轴范围
    x = np.linspace(0, 10, 100)，绘制 sin(x)，并 set_xlim(0, 10)、set_ylim(-1, 1)
    返回元组 (x 轴范围列表, y 轴范围列表)
    预期：([0.0, 10.0], [-1.0, 1.0])
    """
    x = np.linspace(0, 10, 100)
    fig, ax = plt.subplots()
    ax.plot(x, np.sin(x))
    ax.set_xlim(0, 10)
    ax.set_ylim(-1, 1)
    return list(ax.get_xlim()), list(ax.get_ylim())
