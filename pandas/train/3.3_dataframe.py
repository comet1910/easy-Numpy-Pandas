"""
3.3 Pandas 数据结构 —— DataFrame —— 练习

知识点回顾：
    1. 创建：pd.DataFrame(data=字典, columns=[...], index=[...])
       - 列顺序由 columns 指定，行索引由 index 指定
    2. 常用属性：index / columns / values / ndim / shape / size / dtypes / T
    3. 索引器：loc[](标签)、iloc[](位置)、at[](单个标签)、iat[](单个位置)
       - loc / iloc 的逗号前是行规则，逗号后是列规则
    4. 常用方法：head / tail / isin / isna / sum / mean / min / max / var /
       std / median / mode / quantile / describe / info / value_counts /
       count / drop_duplicates / duplicated / sample / replace / equals /
       cummax / cummin / cumsum / cumprod / diff / sort_index / sort_values /
       nlargest / nsmallest
       - axis=0（'index'）按列处理；axis=1（'columns'）按行处理
    5. 布尔索引：df[df["列名"] > 值]
    6. 更改操作：set_index / reset_index / rename / 直接给 index、columns 赋值 /
       添加列 df["新列"] / drop / del / insert
    7. 运算：与标量逐元素计算；与 DataFrame 按标签对齐，匹配不上填 NaN
    8. 导入导出：to_csv / to_pickle / read_csv 等

说明：把下面每个函数中的 pass 替换成自己的实现，函数返回题目要求的结果。
"""

import pandas as pd


def ex1():
    """
    练习1：用数据 {"age": [20, 30, 40], "name": ["张三", "李四", "王五"]}
    创建 DataFrame，列顺序为 ["name", "age"]，行索引为 [101, 102, 103]
    返回元组 (shape, 列名列表, 行索引列表)
    预期：((3, 2), ['name', 'age'], [101, 102, 103])
    """
    pass


def ex2():
    """
    练习2：创建 df = pd.DataFrame({"id": [101, 102, 103], "name": ["张三", "李四", "王五"],
    "age": [20, 30, 40]}, index=["aa", "bb", "cc"])
    返回元组 (行索引列表, 列名列表, ndim, shape, size, dtypes 字符串列表)
    预期：(['aa', 'bb', 'cc'], ['id', 'name', 'age'], 2, (3, 3), 9, ['int64', 'object', 'int64'])
    """
    pass


def ex3():
    """
    练习3：基于练习2的 df，练习 loc / iloc / at / iat
    返回元组：
        (df.loc["aa":"cc"].shape, df.loc[:, ["id", "name"]].shape, df.iloc[0:1].shape,
         df.iloc[0:3, 2].tolist(), df.at["aa", "name"], df.iat[0, 1])
    预期：((3, 3), (3, 2), (1, 3), [20, 30, 40], '张三', '张三')
    """
    pass


def ex4():
    """
    练习4：创建 df = pd.DataFrame(
        data={"id": [101, 102, 103, 104, 105, 106, 101],
              "name": ["张三", "李四", "王五", "赵六", "冯七", "周八", "张三"],
              "age": [10, 20, 30, 40, None, 60, 10]},
        index=["aa", "bb", "cc", "dd", "ee", "ff", "aa"])
    针对 age 列，返回元组 (sum(), round(mean(), 2), min(), max(), median(), count())
    预期：(170.0, 28.33, 10.0, 60.0, 25.0, 6)
    """
    pass


def ex5():
    """
    练习5：基于练习4的 df，返回 age 列的 0.5 分位数
    预期：25.0
    """
    pass


def ex6():
    """
    练习6：创建 df3 = pd.DataFrame({"A": [2, 5, 3, 7, 4], "B": [1, 6, 2, 8, 3]})
    返回元组 (A 列的 cumsum 列表, A 列的 cummax 列表, A 列的 cummin 列表,
              A 列的 cumprod 列表, A 列的 diff 列表)
    预期：([2, 7, 10, 17, 21], [2, 5, 5, 7, 7], [2, 2, 2, 2, 2],
           [2, 10, 30, 210, 840], [nan, 3, -2, 4, -3])
    """
    pass


def ex7():
    """
    练习7：基于练习4的 df，练习排序
    返回元组 (sort_values("age") 的 age 列表, nlargest(2, "age") 的 age 列表,
              nsmallest(1, "age") 的 age 列表)
    预期：([10.0, 10.0, 20.0, 30.0, 40.0, 60.0, nan], [60.0, 40.0], [10.0])
    """
    pass


def ex8():
    """
    练习8：更改操作综合
    1) 创建 df = pd.DataFrame({"id": [101, 102, 103, 104], "age": [20, 30, 40, 10],
       "name": ["张三", "李四", "王五", "赵六"]})
    2) 用 set_index("id") 把 id 设为行索引
    3) 用 rename 把行索引改为 {"一": ..., 示例: 101->"一", 102->"二", 103->"三", 104->"四"}，
       把列名改为 {"age": "年龄", "name": "姓名"}
    4) 添加列 phone，再删除该列
    5) 用 insert 在位置 0 插入列 "score"，值为 "年龄" 列 * 2
    返回元组 (行索引列表, 列名列表, score 列的值列表)
    预期：(['一', '二', '三', '四'], ['score', '年龄', '姓名'], [40, 60, 80, 20])
    """
    pass


def ex9():
    """
    练习9：布尔索引
    创建 df = pd.DataFrame(data={"age": [20, 30, 40, 10], "name": ["张三", "李四", "王五", "赵六"]},
        columns=["name", "age"], index=[101, 104, 103, 102])
    返回 df[df["age"] > 25] 的行索引列表
    预期：[104, 103]
    """
    pass


def ex10():
    """
    练习10：DataFrame 与 DataFrame 运算的标签对齐
    df1: age=[10, 20, 30, 40], name=["张三", "李四", "王五", "赵六"], index=[101, 102, 103, 104]
    df2: age=[10, 20, 30, 40], name=["张三", "李四", "王五", "田七"], index=[102, 103, 104, 105]
    返回 (df1 + df2)["age"] 的值列表
    预期：[nan, 30.0, 50.0, 70.0, nan]
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
