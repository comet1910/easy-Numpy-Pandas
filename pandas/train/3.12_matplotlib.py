"""
3.12 Matplotlib 可视化 —— 练习

知识点回顾：
    1. 脚本中画图必须调用 plt.show() 才会显示；Notebook 中会自动内嵌显示
    2. 两种绘图接口：
       - 状态接口（MATLAB 风格）：plt.figure() / plt.subplot(2, 1, 1) / plt.plot(...)
         / plt.xlabel(...) / plt.ylabel(...) / plt.title(...) / plt.xlim(...) / plt.ylim(...)
         当前坐标轴可用 plt.gca() 取到
       - 面向对象接口：fig, ax = plt.subplots(2, figsize=(10, 6))，
         再用 ax[0].plot(...)、ax[0].set_xlabel(...)、ax[0].set_title(...) 等
    3. 常用图：hist（直方图）、scatter（散点图）
       - ax.hist(data, bins=5) 返回 (每组频次 n, 分组边界 bins, 柱形对象 patches)
       - ax.scatter(x, y, c=颜色, alpha=透明度)，散点数据在 ax.collections[0].get_offsets()
    4. 常用查询：ax.get_xlabel()/get_ylabel()/get_title()/get_xlim()/get_ylim()，
       fig.get_size_inches()，len(ax.lines)/len(ax.collections)/len(ax.patches)
    5. 中文字体需设置 rcParams["font.sans-serif"]，并设 rcParams["axes.unicode_minus"]=False

说明：
    下面的 _data() 与 _year_color() 已给出，你只需要把每个练习函数中的 pass
    替换成自己的实现，函数返回题目要求的结果（这些返回值便于自测校验；
    如果想看图，可在 __main__ 中调用 plt.show()）。
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def _data():
    """内联数据：一组用于画直方图的一维数据"""
    return [1.2, 2.3, 2.8, 3.1, 3.3, 3.7, 4.0, 4.2, 4.5, 5.1,
            5.4, 5.9, 6.2, 6.6, 7.0, 7.3, 7.8, 8.1, 8.6, 9.2]


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
    提示：axes 数量用 plt.gcf().axes，当前坐标轴用 plt.gca()
    预期：(1, "x", "y", "平方曲线", 100)
    """
    pass


def ex2():
    """
    练习2：面向对象接口创建多个子图
    x = np.linspace(0, 10, 100)，fig, ax = plt.subplots(2, figsize=(10, 6))
    ax[0] 画 sin(x) 标题 "sin"，ax[1] 画 cos(x) 标题 "cos"
    返回元组 (子图数量, ax[0] 标题, ax[1] 标题, ax[0] 折线数据点个数)
    预期：(2, "sin", "cos", 100)
    """
    pass


def ex3():
    """
    练习3：直方图 hist
    fig, ax = plt.subplots()，n, bins, patches = ax.hist(_data(), bins=5)
    返回元组 (分组的组数, 每组频次列表, 柱形对象个数)
    预期：(5, [2.0, 6.0, 4.0, 4.0, 4.0], 5)
    """
    pass


def ex4():
    """
    练习4：直方图的频次之和与分组边界个数
    fig, ax = plt.subplots()，n, bins, _ = ax.hist(_data(), bins=5)
    返回元组 (频次之和, 分组边界个数)
    预期：(20, 6)
    """
    pass


def ex5():
    """
    练习5：散点图 scatter
    x = [1, 2, 3, 4, 5]，y = [2, 4, 5, 4, 5]
    fig, ax = plt.subplots()，ax.scatter(x, y)，并设置 xlabel="x"、ylabel="y"
    返回元组 (collections 个数, 散点个数, xlabel)
    提示：散点个数取 ax.collections[0].get_offsets().shape[0]
    预期：(1, 5, "x")
    """
    pass


def ex6():
    """
    练习6：多变量散点图——按年份着色
    构造 DataFrame（date 为 6 个跨年日期：2012-01-01、2012-06-01、2013-01-01、
    2013-06-01、2014-01-01、2015-01-01；temp_max 与 precipitation 自定）
    用 df["date"].apply(_year_color) 生成 color 列，
    再用 ax.scatter(df["temp_max"], df["precipitation"], c=df["color"], alpha=0.5) 绘制
    返回元组 (color 列取值列表, collections 个数)
    预期：(["r", "r", "g", "g", "b", "k"], 1)
    """
    pass


def ex7():
    """
    练习7：设置画布大小
    fig, ax = plt.subplots(figsize=(10, 6))
    返回 fig.get_size_inches() 转成的浮点数列表
    预期：[10.0, 6.0]
    """
    pass


def ex8():
    """
    练习8：设置坐标轴范围
    x = np.linspace(0, 10, 100)，绘制 sin(x)，并 set_xlim(0, 10)、set_ylim(-1, 1)
    返回元组 (x 轴范围列表, y 轴范围列表)
    预期：([0.0, 10.0], [-1.0, 1.0])
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
    # plt.show()  # 想看图形时取消注释
