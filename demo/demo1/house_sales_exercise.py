"""
第 4 章 综合案例：房地产市场洞察与价值评估 —— 综合练习题

业务背景：
    某房地产数据研究机构收集了大量房屋销售数据，希望通过对数据的全面分析，
    探究不同房屋特征对房价的影响、分析不同地区（以邮政编码划分）的市场差异、
    研究建造/翻新年份等时间因素与市场趋势，并用可视化手段直观展示结论。

数据源（19 列，10000 行）：
    id, date, price, bedrooms, bathrooms, sqft_living, sqft_lot, floors,
    waterfront, view, condition, grade, sqft_above, sqft_basement,
    yr_built, yr_renovated, zipcode, lat, long
    文件路径：../../data/house_sales.csv（本文件已用 _PATH 给出绝对路径）

知识点回顾：
    1. 读取与概览：pd.read_csv / df.shape / df.dtypes / df.info()
    2. 数据清洗：
       - 缺失值：df.isnull().sum() 统计数量，df.dropna() 删除含缺失值的行
       - 异常值（IQR 四分位距法）：
           Q1 = s.quantile(0.25); Q3 = s.quantile(0.75); IQR = Q3 - Q1
           下界 = Q1 - 1.5 * IQR；上界 = Q3 + 1.5 * IQR
           布尔索引筛选：df[(df[c] >= 下界) & (df[c] <= 上界)]
    3. 类型转换与特征工程：
       - pd.to_datetime(列) 转日期，.dt.year 取销售年份
       - df[列].apply(lambda x: ...) 构造新特征
    4. 探索性分析：
       - df.select_dtypes(include=[np.number]) 选出数值列
       - describe(percentiles=[0.25, 0.5, 0.75]) 描述性统计
       - corr() 皮尔逊相关系数矩阵，corr["price"] 取与房价的相关性
    5. 分组聚合：
       - groupby(键).agg({"列": "mean"}) 多列不同聚合；df.columns = [...] 重命名
       - pd.cut(值, bins=5) 等宽分箱；groupby(分箱列, observed=False) 保留空箱
       - 多键分组 groupby([年份, 列])
    6. 可视化（matplotlib）：
       - hist 直方图 / scatter 散点图 / imshow + colorbar 热力图 /
         bar 柱状图 / plot 折线图 / boxplot 箱线图
       - 自测技巧：len(ax.patches) 柱数、ax.collections[0].get_offsets().shape[0] 散点数、
         len(ax.lines[0].get_xdata()) 折线点数、im.get_array().shape 矩阵形状

说明：
    - 请把每个练习函数里的 pass 替换成自己的实现，并 return 题目要求的结果以便自测。
    - 下方 _raw() 已给出（读取原始数据）；_clean() 需要你实现，
      ex5 会校验它，ex6 及之后的分析题都基于清洗后的数据。
    - 想看图形时，可在 __main__ 中调用 plt.show()（每题都已创建独立画布）。
"""

from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 数据文件绝对路径：本文件位于 demo/demo1/ 下，数据在仓库的 data/ 目录
_PATH = Path(__file__).resolve().parents[2] / "data" / "house_sales.csv"


def _raw():
    """读取原始 CSV（已给出，直接使用）。"""
    return pd.read_csv(_PATH)


def _clean():
    """
    数据准备（请实现）：原始数据 -> 清洗 -> 特征工程。ex6 及之后都依赖它。

    步骤：
        1) 用 _raw() 读取原始数据
        2) 删除缺失值：dropna()
        3) 用 IQR 法剔除 price 的异常值（上下界系数 1.5）
        4) 将 date 列转换为 datetime 类型
        5) 新增 age = 销售年份 - 建造年份（用 .dt.year）
        6) 新增 is_renovated = 1（yr_renovated > 0）否则 0
    返回：处理后的 DataFrame
    """
    pass


def ex1():
    """
    练习1：读取数据并查看基本信息
    df = _raw()，返回 df 的形状（行数, 列数）
    预期：(10000, 19)
    """
    pass


def ex2():
    """
    练习2：缺失值统计
    df = _raw()，返回各列缺失值数量之和（整数）
    预期：0
    """
    pass


def ex3():
    """
    练习3：IQR 方法处理房价异常值
    在 _raw() 上先 dropna()，再对 price 用 IQR 法（系数 1.5）计算上下界并筛选。
    返回元组 (round(Q1, 2), round(Q3, 2), 筛选后的行数)
    预期：(432656.32, 568049.52, 9930)
    """
    pass


def ex4():
    """
    练习4：日期转换与特征工程
    在练习3结果的基础上：
        date 转 datetime；新增 age = 销售年份 - yr_built；新增 is_renovated（yr_renovated>0 记 1）。
    返回元组 (age 的最大值, is_renovated 等于 1 的行数)
    预期：(124, 2935)
    """
    pass


def ex5():
    """
    练习5：实现 _clean() 并校验
    返回 _clean() 处理后数据集的形状（行数, 列数）
    预期：(9930, 21)
    """
    pass


def ex6():
    """
    练习6：数值型列的描述性统计
    df = _clean()；numeric = df.select_dtypes(include=[np.number]).columns；
    desc = df[numeric].describe(percentiles=[0.25, 0.5, 0.75])
    返回 price 的 [均值, 标准差, 中位数, 最大值]，各保留 2 位小数
    预期：[501121.77, 97124.95, 501561.09, 770223.22]
    """
    pass


def ex7():
    """
    练习7：各特征与房价的相关性
    df = _clean()；corr = df[numeric].corr()，取 corr["price"] 去掉 price 自身。
    返回元组 (与 price 相关性绝对值最强的特征名, round(相关系数, 4))
    预期：('yr_built', 0.013)
    """
    pass


def ex8():
    """
    练习8：按邮政编码分组
    df = _clean()；groupby("zipcode").agg({"price": "mean", "sqft_living": "mean", "bedrooms": "mean"})
    返回元组 (邮编个数, 平均房价最高的邮编)
    预期：(10, 98006)
    """
    pass


def ex9():
    """
    练习9：按是否翻新分组
    df = _clean()；groupby("is_renovated")["price"].mean()
    返回元组 (未翻新平均房价, 已翻新平均房价)，各保留 2 位小数
    预期：(501126.1, 501111.47)
    """
    pass


def ex10():
    """
    练习10：按房龄分组
    df = _clean()；用 pd.cut(df["age"], bins=5) 等宽分箱，
    按分箱对 price 求均值（groupby 传 observed=False 保留空箱、避免告警）。
    返回各区间平均房价列表（按区间顺序），各保留 2 位小数
    预期：[501594.63, 500933.82, 501518.89, 496723.14, 503413.04]
    """
    pass


def ex11():
    """
    练习11：时间序列——每年平均房价
    df = _clean()；df.groupby(df["date"].dt.year)["price"].mean()
    返回元组 (年份个数, 平均房价最高的年份)
    预期：(123, 1914)
    """
    pass


def ex12():
    """
    练习12：时间序列——每年不同翻新情况的平均房价
    df = _clean()；df.groupby([df["date"].dt.year, "is_renovated"])["price"].mean()
    返回结果的条目数（整数）
    预期：240
    """
    pass


def ex13():
    """
    练习13：房价分布直方图
    df = _clean()；fig, ax = plt.subplots()；ax.hist(df["price"], bins=30, edgecolor="k")
    返回柱子（patches）数量
    预期：30
    """
    pass


def ex14():
    """
    练习14：卧室数量与房价的散点图
    df = _clean()；fig, ax = plt.subplots()；ax.scatter(df["bedrooms"], df["price"])
    返回散点数量（提示：ax.collections[0].get_offsets().shape[0]）
    预期：9930
    """
    pass


def ex15():
    """
    练习15：各特征与房价的相关性热力图
    df = _clean()；corr = df[numeric].corr()；
    fig, ax = plt.subplots()；im = ax.imshow(corr, cmap="coolwarm", interpolation="nearest")；
    fig.colorbar(im, ax=ax)
    返回相关矩阵的形状（提示：im.get_array().shape）
    预期：(20, 20)
    """
    pass


def ex16():
    """
    练习16：不同邮政编码区域平均房价的柱状图
    df = _clean()；先算每个 zipcode 的平均房价；
    fig, ax = plt.subplots()；ax.bar(均值索引.astype(str), 均值.values)
    返回柱子（patches）数量
    预期：10
    """
    pass


def ex17():
    """
    练习17：每年平均房价的折线图
    df = _clean()；yearly = df.groupby(df["date"].dt.year)["price"].mean()；
    fig, ax = plt.subplots()；ax.plot(yearly.index, yearly)
    返回折线点的个数（提示：len(ax.lines[0].get_xdata())）
    预期：123
    """
    pass


def ex18():
    """
    练习18：不同翻新情况的房价箱线图
    df = _clean()；fig, ax = plt.subplots()；
    df.boxplot(column="price", by="is_renovated", ax=ax)
    返回箱线图中的线条数量（提示：len(ax.lines)）
    预期：14
    """
    pass


def ex19():
    """
    练习19：房屋使用年限与房价的散点图
    df = _clean()；fig, ax = plt.subplots()；ax.scatter(df["age"], df["price"])
    返回散点数量
    预期：9930
    """
    pass


if __name__ == "__main__":
    # 完成后可取消注释逐一自测（建议按顺序，ex6 起依赖 ex5 的 _clean()）
    print("ex1:", ex1())
    # print("ex2:", ex2())
    # print("ex3:", ex3())
    # print("ex4:", ex4())
    # print("ex5:", ex5())
    # print("ex6:", ex6())
    # print("ex7:", ex7())
    # print("ex8:", ex8())
    # print("ex9:", ex9())
    # print("ex10:", ex10())
    # print("ex11:", ex11())
    # print("ex12:", ex12())
    # print("ex13:", ex13())
    # print("ex14:", ex14())
    # print("ex15:", ex15())
    # print("ex16:", ex16())
    # print("ex17:", ex17())
    # print("ex18:", ex18())
    # print("ex19:", ex19())
    # plt.show()  # 想看图形时取消注释
