"""
3.5 DataFrame 数据分析入门 —— 答案
（教材原示例使用 weather.csv / employees.csv，这里用等价的内联数据代替）
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
