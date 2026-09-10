"""
3.3 Pandas 数据结构 —— DataFrame —— 参考答案
"""

import pandas as pd


def ex1():
    """指定列顺序与行索引创建 DataFrame"""
    df = pd.DataFrame(
        data={"age": [20, 30, 40], "name": ["张三", "李四", "王五"]},
        columns=["name", "age"],
        index=[101, 102, 103],
    )
    return df.shape, df.columns.tolist(), df.index.tolist()


def ex2():
    """常用属性"""
    df = pd.DataFrame(
        data={"id": [101, 102, 103], "name": ["张三", "李四", "王五"], "age": [20, 30, 40]},
        index=["aa", "bb", "cc"],
    )
    return df.index.tolist(), df.columns.tolist(), df.ndim, df.shape, df.size, [str(d) for d in df.dtypes]


def ex3():
    """loc / iloc / at / iat"""
    df = pd.DataFrame(
        data={"id": [101, 102, 103], "name": ["张三", "李四", "王五"], "age": [20, 30, 40]},
        index=["aa", "bb", "cc"],
    )
    return (
        df.loc["aa":"cc"].shape,
        df.loc[:, ["id", "name"]].shape,
        df.iloc[0:1].shape,
        df.iloc[0:3, 2].tolist(),
        df.at["aa", "name"],
        df.iat[0, 1],
    )


def ex4():
    """针对 age 列的常用统计方法"""
    df = pd.DataFrame(
        data={
            "id": [101, 102, 103, 104, 105, 106, 101],
            "name": ["张三", "李四", "王五", "赵六", "冯七", "周八", "张三"],
            "age": [10, 20, 30, 40, None, 60, 10],
        },
        index=["aa", "bb", "cc", "dd", "ee", "ff", "aa"],
    )
    return df["age"].sum(), round(df["age"].mean(), 2), df["age"].min(), df["age"].max(), df["age"].median(), df["age"].count()


def ex5():
    """0.5 分位数"""
    df = pd.DataFrame(
        data={
            "id": [101, 102, 103, 104, 105, 106, 101],
            "name": ["张三", "李四", "王五", "赵六", "冯七", "周八", "张三"],
            "age": [10, 20, 30, 40, None, 60, 10],
        },
        index=["aa", "bb", "cc", "dd", "ee", "ff", "aa"],
    )
    return df["age"].quantile(0.5)


def ex6():
    """累计函数与差分"""
    df3 = pd.DataFrame({"A": [2, 5, 3, 7, 4], "B": [1, 6, 2, 8, 3]})
    return (
        df3["A"].cumsum().tolist(),
        df3["A"].cummax().tolist(),
        df3["A"].cummin().tolist(),
        df3["A"].cumprod().tolist(),
        df3["A"].diff().tolist(),
    )


def ex7():
    """排序"""
    df = pd.DataFrame(
        data={
            "id": [101, 102, 103, 104, 105, 106, 101],
            "name": ["张三", "李四", "王五", "赵六", "冯七", "周八", "张三"],
            "age": [10, 20, 30, 40, None, 60, 10],
        },
        index=["aa", "bb", "cc", "dd", "ee", "ff", "aa"],
    )
    return (
        df.sort_values("age")["age"].tolist(),
        df.nlargest(2, "age")["age"].tolist(),
        df.nsmallest(1, "age")["age"].tolist(),
    )


def ex8():
    """更改操作综合：set_index / rename / 添加与删除列 / insert"""
    df = pd.DataFrame(
        {"id": [101, 102, 103, 104], "age": [20, 30, 40, 10], "name": ["张三", "李四", "王五", "赵六"]}
    )
    df.set_index("id", inplace=True)
    df.rename(
        index={101: "一", 102: "二", 103: "三", 104: "四"},
        columns={"age": "年龄", "name": "姓名"},
        inplace=True,
    )
    df["phone"] = ["13333333333", "14444444444", "15555555555", "16666666666"]
    del df["phone"]
    df.insert(loc=0, column="score", value=df["年龄"] * 2)
    return df.index.tolist(), df.columns.tolist(), df["score"].tolist()


def ex9():
    """布尔索引"""
    df = pd.DataFrame(
        data={"age": [20, 30, 40, 10], "name": ["张三", "李四", "王五", "赵六"]},
        columns=["name", "age"],
        index=[101, 104, 103, 102],
    )
    return df[df["age"] > 25].index.tolist()


def ex10():
    """DataFrame 与 DataFrame 运算的标签对齐"""
    df1 = pd.DataFrame(
        data={"age": [10, 20, 30, 40], "name": ["张三", "李四", "王五", "赵六"]},
        columns=["name", "age"],
        index=[101, 102, 103, 104],
    )
    df2 = pd.DataFrame(
        data={"age": [10, 20, 30, 40], "name": ["张三", "李四", "王五", "田七"]},
        columns=["name", "age"],
        index=[102, 103, 104, 105],
    )
    return (df1 + df2)["age"].tolist()


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
