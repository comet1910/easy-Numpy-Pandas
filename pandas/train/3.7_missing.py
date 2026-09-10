"""
3.7 Pandas 的缺失值处理函数 —— 练习

知识点回顾：
    1. 缺失值：NaN（数值缺失）、None、pd.NA；用 isnull()/isna()/notna() 判断
       - 统计每列缺失数量常用 df.isnull().sum()
    2. 剔除缺失值 dropna()
       - 默认按行剔除（含任意缺失值就删）；axis=1 按列剔除
       - how="all" 全为缺失才删；thresh=n 至少有 n 个非缺失值才保留
       - subset=[列名] 只按指定列的缺失情况剔除
    3. 填充缺失值 fillna()
       - 固定值、字典（按列指定）、统计值（如均值）
       - ffill() 用前面的有效值、bfill() 用后面的有效值
       - interpolate() 线性插值（method="linear"/"time"/"polynomial"）

说明：
    下面的 _dfna() 从 data/weather_withna.csv 加载含缺失值的天气数据
    （与教材一致）。你只需要把每个练习函数中的 pass 替换成自己的实现，
    函数返回题目要求的结果。
    注意：真实数据量较大（1461 行），涉及整列处理的题目在"预期"中只列出
    末尾若干项作为参考，实际返回完整结果。
"""

from pathlib import Path

import numpy as np
import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[2] / "data"


def _dfna():
    """从 data/weather_withna.csv 加载含缺失值的天气数据"""
    return pd.read_csv(DATA_DIR / "weather_withna.csv")


def ex1():
    """
    练习1：s = pd.Series([np.nan, None, pd.NA])
    返回元组 (s.isnull() 的列表, s.isnull() 求和)
    预期：([True, True, True], 3)
    """
    pass


def ex2():
    """
    练习2：查看每列缺失值数量
    df = pd.DataFrame({"date": ["d1","d2","d3","d4"],
                       "temp_max": [11.1, np.nan, np.nan, 12.2],
                       "weather": ["sun", np.nan, np.nan, "rain"]})
    返回 df.isnull().sum() 的列表
    预期：[0, 2, 2]
    """
    pass


def ex3():
    """
    练习3：s = pd.Series([1, pd.NA, None])，返回 dropna() 后的取值列表
    预期：[1]
    """
    pass


def ex4():
    """
    练习4：df = pd.DataFrame([[1, pd.NA, 2], [2, 3, 5], [pd.NA, 4, 6]])
    返回 df.dropna() 后的行索引列表（默认按行剔除）
    预期：[1]
    """
    pass


def ex5():
    """
    练习5：基于练习4的 df，返回 df.dropna(axis=1) 后的列名列表（按列剔除）
    预期：[2]
    """
    pass


def ex6():
    """
    练习6：df = pd.DataFrame([[1, pd.NA, 2], [pd.NA, pd.NA, 5], [pd.NA, pd.NA, pd.NA]])
    返回元组 (df.dropna(how="all") 的行数, df.dropna(thresh=2) 的行数)
    预期：(2, 1)
    """
    pass


def ex7():
    """
    练习7：基于练习6的 df，返回 df.dropna(subset=[0]) 后的行索引列表
    （0 列有缺失值则删除该行）
    预期：[0]
    """
    pass


def ex8():
    """
    练习8：使用固定值填充
    基于 _dfna()，返回 fillna(0) 后的 temp_max 列取值列表
    预期：共 1461 项，末尾 5 项为 [0.0, 0.0, 0.0, 0.0, 12.2]
    """
    pass


def ex9():
    """
    练习9：使用字典填充
    基于 _dfna()，fillna({"temp_max": 60, "temp_min": -60})
    返回 [["temp_max", "temp_min"]] 的值（二维列表）
    预期：共 1461 行，末尾 5 行为
          [[60.0, -60.0], [60.0, -60.0], [60.0, -60.0], [60.0, -60.0], [12.2, 5.0]]
    """
    pass


def ex10():
    """
    练习10：使用均值填充
    基于 _dfna()，用 df[["temp_max"]].mean() 填充，返回 temp_max 列取值列表
    预期：均值约为 15.85146804835924（该列原有 1158 个非空值），
          填充后共 1461 项，末尾 5 项为 [15.85..., 15.85..., 15.85..., 15.85..., 12.2]
    """
    pass


def ex11():
    """
    练习11：s = pd.Series([1.0, np.nan, np.nan, 4.0])
    返回元组 (ffill() 后的列表, bfill() 后的列表)
    预期：([1.0, 1.0, 1.0, 4.0], [1.0, 4.0, 4.0, 4.0])
    """
    pass


def ex12():
    """
    练习12：s = pd.Series([1, np.nan, 3, 4, np.nan, 6])
    返回 s.interpolate() 后的取值列表（线性插值）
    预期：[1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
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
    # print("ex10:", ex10())
    # print("ex11:", ex11())
    # print("ex12:", ex12())
