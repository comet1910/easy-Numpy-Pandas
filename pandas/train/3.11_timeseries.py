"""
3.11 Pandas 时间序列 —— 练习

知识点回顾：
    1. 三种时间类型（底层都是 numpy 的 datetime64/timedelta64）：
       - Timestamp：单个时间戳，pd.to_datetime(单个值) 返回它
       - Period：固定频率的时间周期（如 2012Q1、2012-01）
       - Timedelta：时间增量，两个时间相减得到，索引结构为 TimedeltaIndex
    2. 日期解析：pd.to_datetime() 单个值返回 Timestamp，序列返回 DatetimeIndex
       （注意：DatetimeIndex 没有 .iloc/.dt，需要时用 pd.Series(...) 包一层）
    3. 提取日期部分：
       - Timestamp 直接用属性：d.year / d.month / d.day / d.hour / d.minute / d.second
       - Series 用 dt 访问器：s.dt.year / s.dt.to_period("Q") / s.dt.strftime(...)
    4. DatetimeIndex：把 datetime64 列 set_index 后，可用 df.loc["2013-01":"2013-06"] 切片
    5. 生成时间序列 pd.date_range(start, end/periods, freq)：
       - 默认 freq="D"（自然日）；"B" 工作日、"h" 小时、"min" 分钟
       - 月末 M、月初 MS、季末 Q、年初/年末 A(Y)；频率可组合，如 "2h30min"
       - 后面可加月份缩写改变季/年边界（如 "Q-JAN"），加星期缩写改变周边界（如 "W-WED"）
    6. resample(频率)：按新频率对时间序列重新采样后再聚合（mean/sum/count...）
    7. 注意：本机 pandas 2.1.4 请使用旧频率别名 M/Q/A（教材里的 ME/QE/YE 会报
       Invalid frequency，本套练习统一用 M/Q/A）

说明：
    下面的 _daily() 从 data/weather.csv 加载逐日天气数据（2012-01-01 ~ 2015-12-31，
    教材原示例数据）。你只需要把每个练习函数中的 pass 替换成自己的实现，函数返回
    题目要求的结果。
"""

from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[2] / "data"


def _daily():
    """从 data/weather.csv 加载逐日天气数据"""
    return pd.read_csv(DATA_DIR / "weather.csv")


def ex1():
    """
    练习1：date_range 按起止日期生成日期序列
    pd.date_range("2015-07-03", "2015-07-10")（省略 freq 默认按天 D）
    返回元组 (序列长度, 首日 "%Y-%m-%d" 字符串, 末日 "%Y-%m-%d" 字符串)
    预期：(8, "2015-07-03", "2015-07-10")
    """
    pass


def ex2():
    """
    练习2：用 periods 指定周期数
    pd.date_range("2015-07-03", periods=5)（默认按天）
    返回 "%Y-%m-%d" 格式的日期字符串列表（共 5 个）
    预期：["2015-07-03", "2015-07-04", "2015-07-05", "2015-07-06", "2015-07-07"]
    """
    pass


def ex3():
    """
    练习3：用 freq="h" 按小时生成
    pd.date_range("2015-07-03", periods=5, freq="h")
    返回 "%Y-%m-%d %H:%M" 格式的字符串列表
    预期：["2015-07-03 00:00", "2015-07-03 01:00", "2015-07-03 02:00",
           "2015-07-03 03:00", "2015-07-03 04:00"]
    """
    pass


def ex4():
    """
    练习4：组合频率——2 小时 30 分钟
    pd.date_range("2015-07-03", periods=4, freq="2h30min")
    返回 "%H:%M" 格式的字符串列表
    预期：["00:00", "02:30", "05:00", "07:30"]
    """
    pass


def ex5():
    """
    练习5：用星期缩写改变一周的边界
    pd.date_range("2015-07-03", periods=3, freq="W-WED")（以周三为一周的边界）
    返回 "%Y-%m-%d" 格式的字符串列表
    预期：["2015-07-08", "2015-07-15", "2015-07-22"]
    """
    pass


def ex6():
    """
    练习6：从 Timestamp 中提取时间各部分
    d = pd.Timestamp("2015-01-01 09:08:07.123456")
    返回元组 (year, month, day, hour, minute, second, microsecond)
    预期：(2015, 1, 1, 9, 8, 7, 123456)
    """
    pass


def ex7():
    """
    练习7：用 dt 访问器把日期转成周期（季度）
    s = pd.Series(pd.to_datetime(["2012-01-01", "2012-04-15", "2013-07-01"]))
    s.dt.to_period("Q")，再转成字符串
    返回字符串列表
    预期：["2012Q1", "2012Q2", "2013Q3"]
    """
    pass


def ex8():
    """
    练习8：时间增量 timedelta64——两个日期相减
    dates = pd.to_datetime(["2015-01-01", "2015-01-06", "2015-01-11"])
    delta = dates - dates[0]
    返回元组 (delta 的 dtype 字符串, 每个时间增量的天数列表)
    预期：("timedelta64[ns]", [0, 5, 10])
    """
    pass


def ex9():
    """
    练习9：将日期列设为 DatetimeIndex 后按时间切片
    df = _daily()，把 date 列转为 datetime 并 set_index("date")
    取 df.loc["2015-03":"2015-05"]，返回其行数
    预期：92（2015 年 3、4、5 月共 92 天）
    """
    pass


def ex10():
    """
    练习10：resample 重新采样——按季度求平均温度
    df = _daily()，把 date 列转为 datetime 后 set_index("date")
    df[["temp_max", "temp_min"]].resample("Q").mean()，每个值保留 2 位小数
    返回二维列表（外层为季度，内层为 [temp_max, temp_min]，共 16 个季度）
    预期：[[8.61, 2.51], [17.08, 8.22], [23.89, 12.74], [11.47, 5.64],
           [9.43, 3.33], [19.05, 9.93], [24.56, 14.34], [11.09, 4.93],
           [10.3, 4.1], [18.98, 9.57], [25.51, 14.19], [13.07, 6.69],
           [12.34, 5.53], [20.53, 9.91], [24.87, 13.88], [11.89, 5.96]]
    """
    pass


def ex11():
    """
    练习11：resample 按年汇总——全年降水量之和
    df = _daily()，把 date 列转为 datetime 后 set_index("date")
    df["precipitation"].resample("A").sum()
    返回列表
    预期：[1226.0, 828.0, 1232.8, 1139.2]（2012~2015 各年）
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
