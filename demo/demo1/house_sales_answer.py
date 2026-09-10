"""
第 4 章 综合案例：房地产市场洞察与价值评估 —— 答案解析

运行方式：python house_sales_answer.py
数据源：../../data/house_sales.csv（10000 行 × 19 列）

════════════════════════════════════════════════════════════════════════
结果速览
════════════════════════════════════════════════════════════════════════
    1. 数据读取            shape = (10000, 19)
    2. 缺失值              全列为 0（无需实际删除任何行）
    3. IQR 异常值处理      Q1=432656.32、Q3=568049.52，剔除 70 行后剩 9930 行
    4. 特征工程            age 最大 124 年；已翻新房屋 2935 套
    5. 清洗后数据集        (9930, 21)   （19 原始列 + age + is_renovated）
    6. 描述性统计          房价：均值 501121.77、标准差 97124.95、中位数 501561.09、最大 770223.22
    7. 相关性              与房价相关性最强的特征是 yr_built（≈0.013，极弱）
    8. 按邮编分组          共 10 个邮编，平均房价最高的是 98006
    9. 按是否翻新分组      未翻新 501126.10 vs 已翻新 501111.47（几乎无差异）
   10. 按房龄分组（5 箱）  各区间的平均房价非常接近（约 49.7 万 ~ 50.3 万）
   11. 每年平均房价        123 个年份，均值最高出现在 1914 年
   12. 年 × 翻新 分组      共 240 个组合条目
   13~19. 可视化           直方图 30 柱 / 散点 9930 点 / 热力图 20×20 /
                           邮编柱状图 10 柱 / 折线 123 点 / 箱线图 14 条线 / 散点 9930 点

════════════════════════════════════════════════════════════════════════
结论分析
════════════════════════════════════════════════════════════════════════
    · 本数据集各特征与房价的相关系数都在 ±0.02 以内（趋近于 0），说明在这份数据里
      房屋特征与房价几乎没有线性关系，房价更接近随机分布。这与真实房产数据的常识
      （面积越大、评分越高，房价越高）不符，属于典型的“数据本身无信号”的情形。
      → 结论：分析流程（清洗 → 特征工程 → 分组 → 时间序列 → 可视化）完全正确，
        但在对该数据建模前应先做数据质量核查，否则模型不会有任何预测能力。
    · 时间序列上，各年份平均房价围绕 50 万上下波动，没有明显的上升/下降趋势。
    · 翻新与否、房龄高低对平均房价的影响都可以忽略（差异不足 0.1%）。

    下面是逐题解析。想看图时可在 __main__ 中取消 plt.show() 的注释。
"""

from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

_PATH = Path(__file__).resolve().parents[2] / "data" / "house_sales.csv"


def _raw():
    """读取原始 CSV。"""
    return pd.read_csv(_PATH)


def _clean():
    """
    数据准备：读取 -> 去缺失 -> IQR 异常值处理 -> 日期转换 -> 特征工程。

    解析：
        · dropna()：默认按行删除，只要该行有任一缺失值就删除。
        · IQR 法：Q1/Q3 由 quantile(0.25/0.75) 得到，1.5 是经验系数；
          超出 [Q1-1.5IQR, Q3+1.5IQR] 的视为异常值。
        · 布尔索引里两个条件必须用 & 连接，且各自加括号（& 优先级高于比较）。
        · age 用销售年份减建造年份；is_renovated 用 apply+lambda 把 >0 映射为 1。
    """
    data = _raw().dropna()

    q1 = data["price"].quantile(0.25)
    q3 = data["price"].quantile(0.75)
    iqr = q3 - q1
    data = data[(data["price"] >= q1 - 1.5 * iqr) & (data["price"] <= q3 + 1.5 * iqr)].copy()

    data["date"] = pd.to_datetime(data["date"])
    data["age"] = data["date"].dt.year - data["yr_built"]
    data["is_renovated"] = data["yr_renovated"].apply(lambda x: 1 if x > 0 else 0)
    return data


def _numeric(df):
    """返回数值型列名（供描述性统计与相关性使用）。"""
    return df.select_dtypes(include=[np.number]).columns


def ex1():
    """返回数据形状。解析：df.shape 是 (行数, 列数) 元组。"""
    return _raw().shape


def ex2():
    """返回缺失值总数。解析：isnull().sum() 得到每列缺失数，再 .sum() 汇总。"""
    return int(_raw().isnull().sum().sum())


def ex3():
    """返回 (Q1, Q3, 处理后行数)。解析：IQR 法上下界筛选。"""
    data = _raw().dropna()
    q1 = data["price"].quantile(0.25)
    q3 = data["price"].quantile(0.75)
    iqr = q3 - q1
    data = data[(data["price"] >= q1 - 1.5 * iqr) & (data["price"] <= q3 + 1.5 * iqr)]
    return round(q1, 2), round(q3, 2), len(data)


def ex4():
    """返回 (age 最大值, 已翻新套数)。解析：to_datetime + dt.year 计算房龄。"""
    data = _raw().dropna()
    q1 = data["price"].quantile(0.25)
    q3 = data["price"].quantile(0.75)
    iqr = q3 - q1
    data = data[(data["price"] >= q1 - 1.5 * iqr) & (data["price"] <= q3 + 1.5 * iqr)].copy()
    data["date"] = pd.to_datetime(data["date"])
    data["age"] = data["date"].dt.year - data["yr_built"]
    data["is_renovated"] = data["yr_renovated"].apply(lambda x: 1 if x > 0 else 0)
    return int(data["age"].max()), int(data["is_renovated"].sum())


def ex5():
    """返回清洗后数据集形状。解析：19 原始列 + age + is_renovated = 21 列。"""
    return _clean().shape


def ex6():
    """返回 price 的 [均值, 标准差, 中位数, 最大值]（保留 2 位）。"""
    df = _clean()
    desc = df[_numeric(df)].describe(percentiles=[0.25, 0.5, 0.75])
    return [round(float(desc.loc[k, "price"]), 2) for k in ["mean", "std", "50%", "max"]]


def ex7():
    """返回 (与 price 相关性绝对值最强的特征, 相关系数)。"""
    df = _clean()
    corr = df[_numeric(df)].corr()
    pc = corr["price"].drop("price")
    feat = pc.abs().idxmax()
    return feat, round(float(pc[feat]), 4)


def ex8():
    """返回 (邮编个数, 平均房价最高的邮编)。"""
    df = _clean()
    stats = df.groupby("zipcode").agg({"price": "mean", "sqft_living": "mean", "bedrooms": "mean"})
    stats.columns = ["avg_price", "avg_sqft_living", "avg_bedrooms"]
    return len(stats), int(stats["avg_price"].idxmax())


def ex9():
    """返回 (未翻新平均房价, 已翻新平均房价)。"""
    df = _clean()
    avg = df.groupby("is_renovated")["price"].mean()
    return round(float(avg.loc[0]), 2), round(float(avg.loc[1]), 2)


def ex10():
    """返回各房龄区间的平均房价列表。
    解析：pd.cut(age, bins=5) 生成 Categorical，groupby 时传 observed=False 以保留空箱。
    """
    df = _clean()
    age_group = pd.cut(df["age"], bins=5)
    avg = df.groupby(age_group, observed=False)["price"].mean()
    return [round(float(v), 2) for v in avg.tolist()]


def ex11():
    """返回 (年份个数, 平均房价最高的年份)。"""
    df = _clean()
    yearly = df.groupby(df["date"].dt.year)["price"].mean()
    return len(yearly), int(yearly.idxmax())


def ex12():
    """返回 年 × 翻新 分组的条目数。解析：多键 groupby 得到 MultiIndex 的 Series。"""
    df = _clean()
    grouped = df.groupby([df["date"].dt.year, "is_renovated"])["price"].mean()
    return len(grouped)


def ex13():
    """房价分布直方图，返回柱子数。解析：bins=30 -> 30 个柱。"""
    df = _clean()
    fig, ax = plt.subplots()
    ax.hist(df["price"], bins=30, edgecolor="k")
    return len(ax.patches)


def ex14():
    """卧室数量 vs 房价 散点图，返回散点数。"""
    df = _clean()
    fig, ax = plt.subplots()
    ax.scatter(df["bedrooms"], df["price"])
    return ax.collections[0].get_offsets().shape[0]


def ex15():
    """相关性热力图，返回矩阵形状。解析：imshow 把相关系数矩阵渲染成颜色网格。"""
    df = _clean()
    corr = df[_numeric(df)].corr()
    fig, ax = plt.subplots()
    im = ax.imshow(corr, cmap="coolwarm", interpolation="nearest")
    fig.colorbar(im, ax=ax)
    return im.get_array().shape


def ex16():
    """各邮编平均房价柱状图，返回柱子数。解析：每个邮编一根柱。"""
    df = _clean()
    avg_price = df.groupby("zipcode")["price"].mean()
    fig, ax = plt.subplots()
    ax.bar(avg_price.index.astype(str), avg_price.values)
    return len(ax.patches)


def ex17():
    """每年平均房价折线图，返回折线点数。"""
    df = _clean()
    yearly = df.groupby(df["date"].dt.year)["price"].mean()
    fig, ax = plt.subplots()
    ax.plot(yearly.index, yearly)
    return len(ax.lines[0].get_xdata())


def ex18():
    """不同翻新情况房价箱线图，返回线条数。
    解析：箱线图由若干 Line2D 组成（每个箱体含中位数线、箱体边、上下须等）。
          本环境（matplotlib 3.8）实测每个箱体 7 条线，2 个分组共 14 条。
    """
    df = _clean()
    fig, ax = plt.subplots()
    df.boxplot(column="price", by="is_renovated", ax=ax)
    return len(ax.lines)


def ex19():
    """房屋使用年限 vs 房价 散点图，返回散点数。"""
    df = _clean()
    fig, ax = plt.subplots()
    ax.scatter(df["age"], df["price"])
    return ax.collections[0].get_offsets().shape[0]


if __name__ == "__main__":
    for i, fn in enumerate(
        [ex1, ex2, ex3, ex4, ex5, ex6, ex7, ex8, ex9, ex10,
         ex11, ex12, ex13, ex14, ex15, ex16, ex17, ex18, ex19], start=1
    ):
        try:
            print(f"ex{i}:", fn())
        except Exception as exc:  # 便于定位错误
            print(f"ex{i}: ERROR -> {exc}")
    # plt.show()  # 想看图形时取消注释
