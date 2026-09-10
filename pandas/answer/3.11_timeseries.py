"""
3.11 Pandas 时间序列 —— 答案
"""

import pandas as pd


def _daily():
    """内联数据：2015 年 12 个月的月度天气数据（等价于教材 weather.csv 的简化版）"""
    return pd.DataFrame({
        "date": pd.date_range("2015-01-01", periods=12, freq="MS"),
        "precipitation": [0.0, 1.0, 2.0, 0.5, 3.0, 0.0, 1.5, 2.5, 0.0, 4.0, 1.0, 0.5],
        "temp_max": [5.0, 6.0, 8.0, 10.0, 12.0, 15.0, 18.0, 20.0, 17.0, 14.0, 10.0, 7.0],
        "temp_min": [-2.0, -1.0, 1.0, 3.0, 5.0, 8.0, 11.0, 13.0, 10.0, 7.0, 3.0, 1.0],
    })


def ex1():
    """
    练习1：date_range 按起止日期生成日期序列
    pd.date_range("2015-07-03", "2015-07-10")（省略 freq 默认按天 D）
    返回元组 (序列长度, 首日 "%Y-%m-%d" 字符串, 末日 "%Y-%m-%d" 字符串)
    预期：(8, "2015-07-03", "2015-07-10")
    """
    idx = pd.date_range("2015-07-03", "2015-07-10")
    return len(idx), idx[0].strftime("%Y-%m-%d"), idx[-1].strftime("%Y-%m-%d")


def ex2():
    """
    练习2：用 periods 指定周期数
    pd.date_range("2015-07-03", periods=5)（默认按天）
    返回日期字符串列表
    预期：["2015-07-03", "2015-07-04", ..., "2015-07-07"]（共 5 个）
    """
    idx = pd.date_range("2015-07-03", periods=5)
    return [d.strftime("%Y-%m-%d") for d in idx]


def ex3():
    """
    练习3：用 freq="h" 按小时生成
    pd.date_range("2015-07-03", periods=5, freq="h")
    返回 "%Y-%m-%d %H:%M" 格式的字符串列表
    预期：["2015-07-03 00:00", "2015-07-03 01:00", ..., "2015-07-03 04:00"]
    """
    idx = pd.date_range("2015-07-03", periods=5, freq="h")
    return [d.strftime("%Y-%m-%d %H:%M") for d in idx]


def ex4():
    """
    练习4：组合频率——2 小时 30 分钟
    pd.date_range("2015-07-03", periods=4, freq="2h30min")
    返回 "%H:%M" 格式的字符串列表
    预期：["00:00", "02:30", "05:00", "07:30"]
    """
    idx = pd.date_range("2015-07-03", periods=4, freq="2h30min")
    return [d.strftime("%H:%M") for d in idx]


def ex5():
    """
    练习5：用星期缩写改变一周的开始
    pd.date_range("2015-07-03", periods=3, freq="W-WED")（以周三为一周的边界）
    返回 "%Y-%m-%d" 格式的字符串列表
    预期：["2015-07-08", "2015-07-15", "2015-07-22"]
    """
    idx = pd.date_range("2015-07-03", periods=3, freq="W-WED")
    return [d.strftime("%Y-%m-%d") for d in idx]


def ex6():
    """
    练习6：从 Timestamp 中提取时间各部分
    d = pd.Timestamp("2015-01-01 09:08:07.123456")
    返回元组 (year, month, day, hour, minute, second, microsecond)
    预期：(2015, 1, 1, 9, 8, 7, 123456)
    """
    d = pd.Timestamp("2015-01-01 09:08:07.123456")
    return d.year, d.month, d.day, d.hour, d.minute, d.second, d.microsecond


def ex7():
    """
    练习7：用 dt 访问器把日期转成周期（季度）
    s = pd.Series(pd.to_datetime(["2012-01-01", "2012-04-15", "2013-07-01"]))
    s.dt.to_period("Q")，再转成字符串
    返回字符串列表
    预期：["2012Q1", "2012Q2", "2013Q3"]
    """
    s = pd.Series(pd.to_datetime(["2012-01-01", "2012-04-15", "2013-07-01"]))
    return s.dt.to_period("Q").astype(str).tolist()


def ex8():
    """
    练习8：时间增量 timedelta64——两个日期相减
    dates = pd.to_datetime(["2015-01-01", "2015-01-06", "2015-01-11"])
    delta = dates - dates[0]
    返回元组 (delta 的 dtype 字符串, 每个时间增量的天数列表)
    预期：("timedelta64[ns]", [0, 5, 10])
    """
    dates = pd.to_datetime(["2015-01-01", "2015-01-06", "2015-01-11"])
    delta = dates - dates[0]
    return str(delta.dtype), [d.days for d in delta]


def ex9():
    """
    练习9：将日期列设为 DatetimeIndex 后按时间切片
    df = _daily()，把 date 列转为 datetime 并 set_index("date")
    取 df.loc["2015-03":"2015-05"]，返回其行数
    预期：3
    """
    df = _daily()
    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace=True)
    return df.loc["2015-03":"2015-05"].shape[0]


def ex10():
    """
    练习10：resample 重新采样——按季度求平均温度
    df = _daily().set_index("date")
    df[["temp_max", "temp_min"]].resample("Q").mean()，每个值保留 2 位小数
    返回二维列表（外层为季度，内层为 [temp_max, temp_min]）
    预期：[[6.33, -0.67], [12.33, 5.33], [18.33, 11.33], [10.33, 3.67]]
    """
    df = _daily().set_index("date")
    return df[["temp_max", "temp_min"]].resample("Q").mean().round(2).values.tolist()


def ex11():
    """
    练习11：resample 按年汇总——全年降水量之和
    df = _daily().set_index("date")
    df["precipitation"].resample("A").sum()
    返回列表
    预期：[16.0]
    """
    df = _daily().set_index("date")
    return df["precipitation"].resample("A").sum().round(2).tolist()
