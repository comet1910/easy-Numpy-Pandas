"""
3.5 DataFrame 数据分析入门 —— 答案
（数据来自 data/ 目录下的 weather.csv / employees.csv，与教材一致）
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[2] / "data"


def _weather():
    """从 data/weather.csv 加载天气数据，并派生 month、year 两列"""
    df = pd.read_csv(DATA_DIR / "weather.csv")
    df["month"] = pd.to_datetime(df["date"]).dt.to_period("M").astype(str)
    df["year"] = pd.to_datetime(df["date"]).dt.to_period("Y").astype(str)
    return df


def _employees():
    """从 data/employees.csv 加载员工数据"""
    return pd.read_csv(DATA_DIR / "employees.csv")


def ex1():
    df = _weather()
    return df.shape, df.columns.tolist()


def ex2():
    df = _weather()
    return df.head(2)["date"].tolist(), df.tail(2)["date"].tolist()


def ex3():
    df = _weather()
    return type(df["date"]).__name__, type(df[["date"]]).__name__, df[["date", "temp_max"]].shape


def ex4():
    df = _weather()
    return (df.loc[1, "precipitation"],
            df.iloc[:2, 2:4].shape,
            df.iloc[:, [3, 5, -1]].columns.tolist())


def ex5():
    df = _weather()
    g = df.groupby("month")[["temp_max", "temp_min"]].mean()
    return g.index.tolist(), g["temp_max"].round(2).tolist(), g["temp_min"].round(2).tolist()


def ex6():
    df = _weather()
    return df.groupby("month")["weather"].nunique().tolist()


def ex7():
    s = _weather()["temp_max"]
    return round(s.mean(), 2), round(s.std(), 2), s.median()


def ex8():
    df = _weather()
    df_sort = df.sort_values(["year", "temp_max"], ascending=[True, False]).drop_duplicates(subset="year")
    return df_sort["year"].tolist(), df_sort["temp_max"].tolist()


def ex9():
    emp = _employees()
    return (emp.loc[emp["salary"] == emp["salary"].min(), "first_name"].tolist(),
            emp.loc[emp["salary"] == emp["salary"].max(), "first_name"].tolist())


def ex10():
    emp = _employees()
    counts = emp.groupby("department_id")["employee_id"].count()
    top_dept = emp.groupby("department_id")["salary"].mean().nlargest(1)
    return counts.to_dict(), top_dept.index.tolist()[0]


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
