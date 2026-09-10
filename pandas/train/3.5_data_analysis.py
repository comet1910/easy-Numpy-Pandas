"""
3.5 DataFrame 数据分析入门 —— 练习

知识点回顾：
    1. 加载与查看：read_csv / type / shape / columns / dtypes / info / describe
    2. 查看部分数据：head / tail / 选一列（Series）/ 选多列（DataFrame）
    3. 按标签或位置取数：loc / iloc（逗号前是行规则，逗号后是列规则）
    4. 分组聚合：df.groupby("分组字段")["聚合字段"].聚合函数()
       - 按多个字段分组使用列表；分组字段会变成行索引（多个则为复合索引）
       - 分组频数常用 nunique()
    5. 常用排序：nlargest / nsmallest / sort_values / drop_duplicates
    6. 日期派生列：pd.to_datetime(df["date"]).dt.to_period("M"/"Y").astype(str)

说明：
    下面的 _weather() 与 _employees() 已给出内联数据（等价于教材的
    weather.csv / employees.csv），你只需要把每个练习函数中的 pass
    替换成自己的实现，函数返回题目要求的结果。
"""

import pandas as pd


def _weather():
    df = pd.DataFrame({
        "date": ["2012-01-15", "2012-01-20", "2012-02-10", "2012-02-25",
                 "2013-01-05", "2013-01-18", "2013-02-12", "2013-02-28"],
        "precipitation": [0.0, 2.5, 1.0, 0.0, 5.0, 0.0, 3.0, 1.5],
        "temp_max": [7.0, 9.0, 10.0, 12.0, 6.0, 8.0, 11.0, 13.0],
        "temp_min": [1.0, 3.0, 4.0, 5.0, 0.0, 2.0, 5.0, 6.0],
        "wind": [2.0, 3.0, 1.5, 2.5, 4.0, 2.0, 3.5, 1.0],
        "weather": ["sun", "rain", "rain", "sun", "rain", "sun", "rain", "sun"],
    })
    df["month"] = pd.to_datetime(df["date"]).dt.to_period("M").astype(str)
    df["year"] = pd.to_datetime(df["date"]).dt.to_period("Y").astype(str)
    return df


def _employees():
    return pd.DataFrame({
        "employee_id": [1, 2, 3, 4, 5, 6],
        "first_name": ["A", "B", "C", "D", "E", "F"],
        "salary": [5000, 8000, 3000, 12000, 6000, 4000],
        "department_id": [10, 20, 10, 30, 20, 30],
    })


def ex1():
    """
    练习1：用 _weather() 加载数据，查看基本信息
    返回元组 (shape, 列名列表)
    预期：((8, 8), ['date', 'precipitation', 'temp_max', 'temp_min', 'wind',
                    'weather', 'month', 'year'])
    """
    pass


def ex2():
    """
    练习2：查看前 2 行与后 2 行的 date
    返回元组 (head(2) 的 date 列表, tail(2) 的 date 列表)
    预期：(['2012-01-15', '2012-01-20'], ['2013-02-12', '2013-02-28'])
    """
    pass


def ex3():
    """
    练习3：获取一列（df["date"]）与多列（df[["date"]]）时返回对象的类型
    返回元组 (df["date"] 的类名, df[["date"]] 的类名, df[["date", "temp_max"]].shape)
    预期：('Series', 'DataFrame', (8, 2))
    """
    pass


def ex4():
    """
    练习4：练习 loc / iloc 混合取数
    返回元组 (df.loc[1, "precipitation"], df.iloc[:2, 2:4].shape,
              df.iloc[:, [3, 5, -1]].columns 列表)
    预期：(2.5, (2, 2), ['temp_min', 'weather', 'year'])
    """
    pass


def ex5():
    """
    练习5：按月分组，统计最高温度、最低温度的平均值
    返回元组 (分组后的 month 索引列表, temp_max 均值列表(保留2位),
              temp_min 均值列表(保留2位))
    预期：(['2012-01', '2012-02', '2013-01', '2013-02'], [8.0, 11.0, 7.0, 12.0], [2.0, 4.5, 1.0, 5.5])
    """
    pass


def ex6():
    """
    练习6：分组频数——统计每个月不同天气状况的数量
    返回 nunique() 的结果列表
    预期：[2, 2, 2, 2]
    """
    pass


def ex7():
    """
    练习7：常用统计值——对 temp_max 计算均值、标准差、中位数
    返回元组 (round(mean, 2), round(std, 2), median)
    预期：(9.5, 2.45, 9.5)
    """
    pass


def ex8():
    """
    练习8：排序与去重——找出每年的最高温度
    先按 ["year", "temp_max"] 升序/降序排序，再按 year 去重
    返回元组 (去重后的 year 列表, 对应的 temp_max 列表)
    预期：(['2012', '2013'], [12.0, 13.0])
    """
    pass


def ex9():
    """
    练习9：员工案例——找出薪资最低、最高的员工姓名
    返回元组 (最低薪资员工 first_name 列表, 最高薪资员工 first_name 列表)
    预期：(['C'], ['D'])
    """
    pass


def ex10():
    """
    练习10：员工案例——每个部门的员工数，以及平均薪资最高的部门 id
    返回元组 (部门->员工数 的字典, 平均薪资最高的部门 id)
    预期：({10: 2, 20: 2, 30: 2}, 30)
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
