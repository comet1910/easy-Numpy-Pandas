"""
3.10 Pandas 透视表 —— 练习

知识点回顾：
    1. 透视表根据行分组键、列分组键对数据聚合，把结果分配到各个矩形区域
    2. 两种写法：DataFrame.pivot_table(...) 与 pandas.pivot_table(data, ...)
    3. 常用参数：
       - values：待聚合的列（默认聚合所有数值列）
       - index：行维度（分组键，可为列表）
       - columns：列维度（分组键，可为列表）
       - aggfunc：聚合函数（默认 "mean"，可为列表或字典）
       - fill_value：替换结果表中的缺失值
       - margins：是否添加"总计"行/列（默认 False）
       - dropna：是否排除含缺失值的行列（默认 True）
    4. 常配合 pd.cut() 把连续字段分箱后再作为 index

说明：
    下面的 _sleep() 已给出内联数据（等价于教材的 sleep.csv），你只需要把每个
    练习函数中的 pass 替换成自己的实现，函数返回题目要求的结果。
"""

import pandas as pd


def _sleep():
    return pd.DataFrame({
        "person_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "gender": ["F", "M", "F", "M", "F", "M", "F", "M", "F", "M"],
        "occupation": ["Office Worker", "Student", "Retired", "Manual Labor",
                       "Office Worker", "Student", "Retired", "Manual Labor",
                       "Office Worker", "Student"],
        "sleep_duration": [5.5, 6.5, 7.5, 4.5, 8.5, 6.0, 7.0, 5.0, 9.0, 6.8],
        "sleep_quality": [7, 8, 6, 5, 9, 7, 8, 6, 9, 7],
        "stress_level": [2, 5, 8, 3, 1, 6, 4, 9, 2, 7],
    })


def ex1():
    """
    练习1：按性别统计平均睡眠质量
    df.pivot_table(values="sleep_quality", index="gender", aggfunc="mean")
    返回元组 (结果索引列表, sleep_quality 列取值列表)
    预期：([F, M], [7.8, 6.6])
    """
    pass


def ex2():
    """
    练习2：两个行维度——按 gender、occupation 统计平均睡眠质量
    index=["gender", "occupation"]，返回元组 (复合索引列表, sleep_quality 取值列表，保留2位小数)
    预期：([('F', 'Office Worker'), ('F', 'Retired'), ('M', 'Manual Labor'), ('M', 'Student')],
           [8.33, 7.0, 5.5, 7.33])
    """
    pass


def ex3():
    """
    练习3：增加列维度——columns="occupation"
    values="sleep_quality", index="gender", aggfunc="mean"
    返回结果的列名列表
    预期：['Manual Labor', 'Office Worker', 'Retired', 'Student']
    """
    pass


def ex4():
    """
    练习4：使用 fill_value=0 填充缺失的组合
    在练习3的基础上加 fill_value=0，返回结果的二维值列表（每个值保留2位小数）
    预期：[[0.0, 8.33, 7.0, 0.0], [5.5, 0.0, 0.0, 7.33]]
    """
    pass


def ex5():
    """
    练习5：统计交叉表中的缺失组合个数
    在练习3（不加 fill_value）的结果上，返回其缺失值总个数（result.isnull().values.sum()）
    预期：4
    """
    pass


def ex6():
    """
    练习6：添加总计——margins=True
    在练习3基础上加 margins=True，返回结果的行索引列表
    预期：['F', 'M', 'All']
    """
    pass


def ex7():
    """
    练习7：更换聚合函数——aggfunc="count"
    values="sleep_quality", index="gender"，返回结果取值列表
    预期：[5, 5]
    """
    pass


def ex8():
    """
    练习8：先用 cut 分箱再透视
    duration_stage = pd.cut(df["sleep_duration"], [0, 6, 8, 10])
    df.pivot_table(values="sleep_quality", index=[duration_stage], aggfunc="mean")
    返回元组 (索引字符串列表, sleep_quality 取值列表)
    预期：(["(0, 6]", "(6, 8]", "(8, 10]"], [6.25, 7.25, 9.0])
    """
    pass


def ex9():
    """
    练习9：使用 pandas.pivot_table 形式，并聚合多列
    pd.pivot_table(df, values=["sleep_quality", "sleep_duration"], index="occupation", aggfunc="mean")
    返回结果的列名列表
    预期：['sleep_duration', 'sleep_quality']
    """
    pass


def ex10():
    """
    练习10：aggfunc="max" 且带总计行
    values="sleep_quality", index="gender", columns="occupation", aggfunc="max", margins=True
    返回元组 (结果列名列表, 结果中 "All" 行的取值列表)
    预期：(['Manual Labor', 'Office Worker', 'Retired', 'Student', 'All'], [6.0, 9.0, 8.0, 8.0, 9.0])
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
