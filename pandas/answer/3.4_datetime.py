"""
3.4 Pandas 日期数据处理初识 —— 答案
"""

import pandas as pd


def _df():
    df = pd.DataFrame({"gmv": [100, 200, 300, 400],
                       "trade_date": ["2025-01-06", "2023-10-31", "2023-12-31", "2023-01-05"]})
    df["ymd"] = pd.to_datetime(df["trade_date"])
    return df


def ex1():
    s = pd.Series(pd.to_datetime(["2025-01-06", "2023-10-31", "2023-12-31", "2023-01-05"]))
    return s


def ex2():
    return str(_df()["ymd"].dtype)


def ex3():
    ymd = _df()["ymd"]
    return ymd.dt.year.tolist(), ymd.dt.month.tolist(), ymd.dt.day.tolist()


def ex4():
    ymd = _df()["ymd"]
    return ymd.dt.day_name().tolist(), ymd.dt.quarter.tolist()


def ex5():
    ymd = _df()["ymd"]
    return ymd.dt.is_month_end.tolist(), ymd.dt.is_year_end.tolist()


def ex6():
    ymd = _df()["ymd"]
    return (ymd.dt.to_period("Y").astype(str).tolist(),
            ymd.dt.to_period("M").astype(str).tolist(),
            ymd.dt.to_period("Q").astype(str).tolist())


def ex7():
    s = pd.Series(pd.to_datetime(["2024-05-15", "bad-date", "2023-12-31"], errors="coerce"))
    return len(s), s.isna().tolist(), s.iloc[2]


def ex8():
    s = pd.Series(pd.to_datetime(["10/11/12", "02/03/04"], dayfirst=True))
    return s.dt.strftime("%Y-%m-%d").tolist()


if __name__ == "__main__":
    print("ex1:", ex1())
    print("ex2:", ex2())
    print("ex3:", ex3())
    print("ex4:", ex4())
    print("ex5:", ex5())
    print("ex6:", ex6())
    print("ex7:", ex7())
    print("ex8:", ex8())
