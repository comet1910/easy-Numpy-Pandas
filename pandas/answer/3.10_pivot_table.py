"""
3.10 Pandas 透视表 —— 答案
（教材原示例使用 sleep.csv，这里用等价的内联数据代替）
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
    result = _sleep().pivot_table(values="sleep_quality", index="gender", aggfunc="mean")
    return result.index.tolist(), result["sleep_quality"].tolist()


def ex2():
    result = _sleep().pivot_table(values="sleep_quality", index=["gender", "occupation"], aggfunc="mean")
    return result.index.tolist(), [round(v, 2) for v in result["sleep_quality"].tolist()]


def ex3():
    result = _sleep().pivot_table(values="sleep_quality", index="gender",
                                  columns="occupation", aggfunc="mean")
    return result.columns.tolist()


def ex4():
    result = _sleep().pivot_table(values="sleep_quality", index="gender",
                                  columns="occupation", aggfunc="mean", fill_value=0)
    return [[round(v, 2) for v in row] for row in result.values.tolist()]


def ex5():
    result = _sleep().pivot_table(values="sleep_quality", index="gender",
                                  columns="occupation", aggfunc="mean")
    return result.isnull().values.sum()


def ex6():
    result = _sleep().pivot_table(values="sleep_quality", index="gender",
                                  columns="occupation", aggfunc="mean", margins=True)
    return result.index.tolist()


def ex7():
    result = _sleep().pivot_table(values="sleep_quality", index="gender", aggfunc="count")
    return result["sleep_quality"].tolist()


def ex8():
    duration_stage = pd.cut(_sleep()["sleep_duration"], [0, 6, 8, 10])
    result = _sleep().pivot_table(values="sleep_quality", index=[duration_stage], aggfunc="mean")
    return [str(i) for i in result.index.tolist()], result["sleep_quality"].tolist()


def ex9():
    result = pd.pivot_table(_sleep(), values=["sleep_quality", "sleep_duration"],
                            index="occupation", aggfunc="mean")
    return result.columns.tolist()


def ex10():
    result = _sleep().pivot_table(values="sleep_quality", index="gender",
                                  columns="occupation", aggfunc="max", margins=True)
    return result.columns.tolist(), result.loc["All"].tolist()


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
