"""
3.4 Pandas 日期数据处理初识 —— 练习

知识点回顾：
    1. pd.to_datetime(arg)：把字符串/列表/Series 转换为 datetime64 类型
       - errors：{'ignore', 'raise', 'coerce'}，'coerce' 会把无法解析的值置为 NaT
       - dayfirst / yearfirst：控制“日月年”的解析顺序
       - format：指定日期字符串格式
    2. Series.dt 访问器：对 datetime 列批量取日期属性
       - dt.year / dt.month / dt.day / dt.day_name()
       - dt.quarter / dt.is_month_end / dt.is_year_end
    3. Series.dt.to_period(freq)：转换为周期（Period）
       - "D" 天 / "W" 周 / "M" 月 / "Q" 季 / "A"（或 "Y"）年
       - 转换后可用 .astype(str) 得到形如 2024-05、2024Q2、2024 的字符串

说明：把下面每个函数中的 pass 替换成自己的实现，函数返回题目要求的结果。
"""

import pandas as pd


def ex1():
    """
    练习1：将字符串列表 ["2025-01-06", "2023-10-31", "2023-12-31", "2023-01-05"]
    转换为 datetime 类型，返回转换后的 Series（保持顺序）
    预期：dtype 为 datetime64[ns]，第一个元素为 2025-01-06 00:00:00
    """
    pass


def ex2():
    """
    练习2：创建 df = pd.DataFrame({"gmv": [100, 200, 300, 400],
        "trade_date": ["2025-01-06", "2023-10-31", "2023-12-31", "2023-01-05"]})
    新增列 ymd（由 trade_date 转换而来），返回 df["ymd"] 的 dtype 字符串
    预期：'datetime64[ns]'
    """
    pass


def ex3():
    """
    练习3：基于练习2的 df，用 dt 访问器拆分出年、月、日
    返回元组 (年列表, 月列表, 日列表)
    预期：([2025, 2023, 2023, 2023], [1, 10, 12, 1], [6, 31, 31, 5])
    """
    pass


def ex4():
    """
    练习4：基于练习2的 df 的 ymd 列
    返回元组 (星期名称列表, 季度列表)
    预期：(['Monday', 'Tuesday', 'Sunday', 'Thursday'], [1, 4, 4, 1])
    """
    pass


def ex5():
    """
    练习5：基于练习2的 df 的 ymd 列，判断是否月底、是否年底
    返回元组 (is_month_end 列表, is_year_end 列表)
    预期：([False, True, True, False], [False, False, True, False])
    """
    pass


def ex6():
    """
    练习6：基于练习2的 df 的 ymd 列，用 to_period 转换统计周期
    返回元组 (按年周期字符串列表, 按月周期字符串列表, 按季度周期字符串列表)
    预期：(['2025', '2023', '2023', '2023'], ['2025-01', '2023-10', '2023-12', '2023-01'],
           ['2025Q1', '2023Q4', '2023Q4', '2023Q1'])
    """
    pass


def ex7():
    """
    练习7：把 ["2024-05-15", "bad-date", "2023-12-31"] 转换为 datetime，
    无法解析的值用 errors="coerce" 变成 NaT
    返回 (长度, 是否缺失列表, 第 3 个元素)  其中是否缺失列表由 isna() 得到
    预期：(3, [False, True, False], Timestamp('2023-12-31 00:00:00'))
    """
    pass


def ex8():
    """
    练习8：练习 dayfirst / yearfirst
    某工具导出的日期字符串为 ["10/11/12", "02/03/04"]，格式为 日/月/年
    使用 dayfirst=True 转换，返回转换结果的字符串列表（格式 YYYY-MM-DD）
    预期：['2012-11-10', '2004-03-02']
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
