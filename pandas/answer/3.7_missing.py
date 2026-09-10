"""
3.7 Pandas 的缺失值处理函数 —— 答案
"""

import numpy as np
import pandas as pd


def _dfna():
    return pd.DataFrame({
        "date": ["2015-12-27", "2015-12-31"],
        "precipitation": [np.nan, 20.6],
        "temp_max": [np.nan, 12.2],
        "temp_min": [np.nan, 5.0],
        "wind": [np.nan, 3.8],
        "weather": [np.nan, "rain"],
    })


def ex1():
    s = pd.Series([np.nan, None, pd.NA])
    return s.isnull().tolist(), s.isnull().sum()


def ex2():
    df = pd.DataFrame({
        "date": ["d1", "d2", "d3", "d4"],
        "temp_max": [11.1, np.nan, np.nan, 12.2],
        "weather": ["sun", np.nan, np.nan, "rain"],
    })
    return df.isnull().sum().tolist()


def ex3():
    s = pd.Series([1, pd.NA, None])
    return s.dropna().tolist()


def ex4():
    df = pd.DataFrame([[1, pd.NA, 2], [2, 3, 5], [pd.NA, 4, 6]])
    return df.dropna().index.tolist()


def ex5():
    df = pd.DataFrame([[1, pd.NA, 2], [2, 3, 5], [pd.NA, 4, 6]])
    return df.dropna(axis=1).columns.tolist()


def ex6():
    df = pd.DataFrame([[1, pd.NA, 2], [pd.NA, pd.NA, 5], [pd.NA, pd.NA, pd.NA]])
    return df.dropna(how="all").shape[0], df.dropna(thresh=2).shape[0]


def ex7():
    df = pd.DataFrame([[1, pd.NA, 2], [pd.NA, pd.NA, 5], [pd.NA, pd.NA, pd.NA]])
    return df.dropna(subset=[0]).index.tolist()


def ex8():
    return _dfna().fillna(0)["temp_max"].tolist()


def ex9():
    df = _dfna().fillna({"temp_max": 60, "temp_min": -60})
    return df[["temp_max", "temp_min"]].values.tolist()


def ex10():
    df = _dfna()
    return df.fillna(df[["temp_max"]].mean())["temp_max"].tolist()


def ex11():
    s = pd.Series([1.0, np.nan, np.nan, 4.0])
    return s.ffill().tolist(), s.bfill().tolist()


def ex12():
    s = pd.Series([1, np.nan, 3, 4, np.nan, 6])
    return s.interpolate().tolist()


if __name__ == "__main__":
    print("ex1:", ex1())
    print("ex2:", ex2())
    print("ex3:", ex3())
    print("ex4:", ex4())
    print("ex5:", ex5())
    print("ex6:", ex6())
    print("ex7:", ex7())
    print("ex8:", ex8())
    print("ex9:", ex9())
    print("ex10:", ex10())
    print("ex11:", ex11())
    print("ex12:", ex12())
