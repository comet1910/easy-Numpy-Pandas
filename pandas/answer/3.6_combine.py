"""
3.6 Pandas 的数据组合函数（concat / merge / join） —— 答案
"""

import pandas as pd


def ex1():
    s1 = pd.Series(["A", "B"], index=[1, 2])
    s2 = pd.Series(["D", "E"], index=[4, 5])
    s3 = pd.Series(["G", "H"], index=[7, 8])
    return pd.concat([s1, s2, s3]).tolist(), pd.concat([s1, s2, s3], axis=1).shape


def ex2():
    df1 = pd.DataFrame(data={"a": [1, 2], "b": [4, 5]}, index=[1, 2])
    s1 = pd.Series(data=[7, 10], index=[1, 2], name="a")
    return pd.concat([df1, s1]).shape, pd.concat([df1, s1], axis=1).columns.tolist()


def ex3():
    df1 = pd.DataFrame(data={"a": [1, 2], "b": [4, 5]}, index=[1, 2])
    df2 = pd.DataFrame(data={"a": [7, 8], "b": [10, 11]}, index=[1, 2])
    return pd.concat([df1, df2], axis=1).columns.tolist(), pd.concat([df1, df2], axis=1).shape


def ex4():
    df1 = pd.DataFrame(data={"a": [1, 2], "b": [4, 5]}, index=[1, 2])
    df2 = pd.DataFrame(data={"a": [7, 8], "b": [10, 11]}, index=[1, 2])
    return pd.concat([df1, df2], ignore_index=True).index.tolist()


def ex5():
    df1 = pd.DataFrame(data={"a": [1, 2], "b": [4, 5]}, index=[1, 2])
    df2 = pd.DataFrame(data={"b": [7, 8], "c": [10, 11]}, index=[2, 3])
    return pd.concat([df1, df2]).columns.tolist(), pd.concat([df1, df2], join="inner").columns.tolist()


def ex6():
    df1 = pd.DataFrame({"employee": ["Bob", "Jake", "Lisa", "Sue"],
                        "group": ["Accounting", "Engineering", "Engineering", "HR"]})
    df2 = pd.DataFrame({"employee": ["Lisa", "Bob", "Jake", "Sue"], "hire_date": [2004, 2008, 2012, 2014]})
    merged = pd.merge(df1, df2)
    return merged.shape, merged["hire_date"].tolist()


def ex7():
    df1 = pd.DataFrame({"employee": ["Bob", "Jake", "Lisa", "Sue"],
                        "group": ["Accounting", "Engineering", "Engineering", "HR"]})
    df2 = pd.DataFrame({"group": ["Accounting", "Engineering", "HR"], "supervisor": ["Carly", "Guido", "Steve"]})
    return pd.merge(df1, df2)["supervisor"].tolist()


def ex8():
    df1 = pd.DataFrame({"employee": ["Bob", "Jake", "Lisa", "Sue"],
                        "group": ["Accounting", "Engineering", "Engineering", "HR"]})
    df2 = pd.DataFrame({
        "group": ["Accounting", "Accounting", "Engineering", "Engineering", "HR", "HR"],
        "skills": ["math", "spreadsheets", "coding", "linux", "spreadsheets", "organization"],
    })
    return pd.merge(df1, df2).shape[0]


def ex9():
    df1 = pd.DataFrame({"employee": ["Bob", "Jake", "Lisa", "Sue"],
                        "group": ["Accounting", "Engineering", "Engineering", "HR"]})
    df2 = pd.DataFrame({"name": ["Bob", "Jake", "Lisa", "Sue"], "salary": [70000, 80000, 120000, 90000]})
    merged = pd.merge(df1, df2, left_on="employee", right_on="name")
    return merged.columns.tolist(), merged["salary"].tolist()


def ex10():
    df1 = pd.DataFrame({"name": ["Peter", "Paul", "Mary"], "food": ["fish", "beans", "bread"]},
                       columns=["name", "food"])
    df2 = pd.DataFrame({"name": ["Mary", "Joseph"], "drink": ["wine", "beer"]}, columns=["name", "drink"])
    return (pd.merge(df1, df2).shape[0],
            pd.merge(df1, df2, how="outer").shape[0],
            pd.merge(df1, df2, how="left").shape[0])


def ex11():
    df1 = pd.DataFrame({"name": ["Bob", "Jake", "Lisa", "Sue"], "rank": [1, 2, 3, 4]})
    df2 = pd.DataFrame({"name": ["Bob", "Jake", "Lisa", "Sue"], "rank": [3, 1, 4, 2]})
    return (pd.merge(df1, df2, on="name").columns.tolist(),
            pd.merge(df1, df2, on="name", suffixes=("_df1", "_df2")).columns.tolist())


def ex12():
    df1 = pd.DataFrame({"employee": ["Bob", "Jake", "Lisa", "Sue"],
                        "group": ["Accounting", "Engineering", "Engineering", "HR"]})
    df2 = pd.DataFrame({"employee": ["Lisa", "Bob", "Jake", "Sue"], "hire_date": [2004, 2008, 2012, 2014]})
    df1.set_index("employee", inplace=True)
    df2.set_index("employee", inplace=True)
    return pd.merge(df1, df2, left_index=True, right_index=True).index.tolist()


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
