"""
3.9 Pandas 的数据聚合、转换、过滤函数 —— 答案
"""

import numpy as np
import pandas as pd


def _employees():
    return pd.DataFrame({
        "employee_id": [100, 101, 102, 103, 104, 105, 106, 107],
        "last_name": ["Whalen", "Hartstein", "Fay", "Raphaely", "Khoo", "Baida", "Tobias", "King"],
        "job_id": ["AD_ASST", "MK_MAN", "MK_REP", "PU_MAN", "PU_CLERK", "PU_CLERK", "PU_CLERK", "PU_MAN"],
        "salary": [4400, 13000, 6000, 11000, 2600, 2900, 2800, 11000],
        "commission_pct": [0.1, 0.2, 0.3, np.nan, 0.4, 0.5, 0.6, np.nan],
        "department_id": [10, 20, 20, 30, 30, 30, 30, 30],
    })


def ex1():
    return type(_employees().groupby("department_id")).__name__


def ex2():
    return _employees().groupby("department_id").groups


def ex3():
    return _employees().groupby("department_id").get_group(20).index.tolist()


def ex4():
    return _employees().groupby("department_id")["salary"].mean().tolist()


def ex5():
    return [(dept, g.shape) for dept, g in _employees().groupby("department_id")]


def ex6():
    return _employees().groupby(["department_id", "job_id"])[["salary", "commission_pct"]].mean().index.tolist()


def ex7():
    return _employees().groupby(["department_id", "job_id"], as_index=False)[["salary", "commission_pct"]].mean().columns.tolist()


def ex8():
    salary = pd.Series([4400, 13000, 6000, 11000, 2600])
    return pd.cut(salary, [0, 10000, 20000]).astype(str).tolist()


def ex9():
    salary = pd.Series([4400, 13000, 6000, 11000, 2600])
    return pd.cut(salary, [0, 10000, 20000], labels=["low", "high"]).tolist()


def ex10():
    return _employees().groupby("department_id")["salary"].agg(["min", "median", "max"]).values.tolist()


def ex11():
    df = _employees()
    g = df.groupby("department_id")
    return g["job_id"].nunique().tolist(), g["commission_pct"].mean().tolist()


def ex12():
    renamed = (
        _employees().groupby("department_id")
        .agg({"job_id": "nunique", "commission_pct": "mean"})
        .rename(columns={"job_id": "工种数", "commission_pct": "佣金比例平均值"})
    )
    return renamed.columns.tolist()


def ex13():
    def first_letters(x):
        return sorted({name[0] for name in x})

    return _employees().groupby("department_id")["last_name"].agg(first_letters).tolist()


def ex14():
    result = _employees().groupby("department_id")["salary"].transform(lambda x: x - x.mean())
    return [round(v, 2) for v in result.tolist()]


def ex15():
    filtered = _employees().groupby("department_id").filter(
        lambda x: x["commission_pct"].notnull().all()
    )
    return filtered["department_id"].tolist()


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
    print("ex13:", ex13())
    print("ex14:", ex14())
    print("ex15:", ex15())
