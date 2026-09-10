"""
3.6 Pandas 的数据组合函数（concat / merge / join） —— 练习

知识点回顾：
    1. concat：沿轴堆叠多个对象
       - axis=0 按行连接（默认），axis=1 按列连接
       - 匹配不上的位置用 NaN 填充
       - ignore_index=True 重置索引
       - join="outer"（默认，取并集）/ join="inner"（取交集）
    2. merge：通过一个或多个列把行连接起来
       - 连接类型：一对一、多对一、多对多（多对多是行的笛卡尔积）
       - 用 on="列名"（有同名列时）；列名不同用 left_on / right_on
       - 用 left_index=True / right_index=True 按索引合并
       - how：inner（默认交集）/ outer（并集）/ left / right
       - suffixes：重名列后缀，默认 ("_x", "_y")
    3. join：DataFrame 的方法，按索引合并，用 lsuffix / rsuffix 处理重名列

说明：把下面每个函数中的 pass 替换成自己的实现，函数返回题目要求的结果。
"""

import pandas as pd


def ex1():
    """
    练习1：Series 与 Series 的 concat
    s1=pd.Series(["A","B"], index=[1,2])、s2=pd.Series(["D","E"], index=[4,5])、
    s3=pd.Series(["G","H"], index=[7,8])
    返回元组 (按行连接的取值列表, 按列连接(axis=1)后的 shape)
    预期：(['A', 'B', 'D', 'E', 'G', 'H'], (6, 3))
    """
    pass


def ex2():
    """
    练习2：DataFrame 与 Series 的 concat
    df1=pd.DataFrame(data={"a":[1,2],"b":[4,5]}, index=[1,2])
    s1=pd.Series(data=[7,10], index=[1,2], name="a")
    返回元组 (按行连接后的 shape, 按列连接后的列名列表)
    预期：((4, 3), ['a', 'b', 'a'])
    """
    pass


def ex3():
    """
    练习3：DataFrame 与 DataFrame 的 concat（axis=1）
    df1=pd.DataFrame(data={"a":[1,2],"b":[4,5]}, index=[1,2])
    df2=pd.DataFrame(data={"a":[7,8],"b":[10,11]}, index=[1,2])
    返回元组 (按列连接后的列名列表, 按列连接后的 shape)
    预期：(['a', 'b', 'a', 'b'], (2, 4))
    """
    pass


def ex4():
    """
    练习4：concat 的 ignore_index
    基于练习3的 df1、df2，按行连接并重置索引
    返回重置后的行索引列表
    预期：[0, 1, 2, 3]
    """
    pass


def ex5():
    """
    练习5：concat 的 join（类似 join 的连接）
    df1=pd.DataFrame(data={"a":[1,2],"b":[4,5]}, index=[1,2])
    df2=pd.DataFrame(data={"b":[7,8],"c":[10,11]}, index=[2,3])
    返回元组 (默认 outer 连接的列名列表, join="inner" 的列名列表)
    预期：(['a', 'b', 'c'], ['b'])
    """
    pass


def ex6():
    """
    练习6：merge 一对一连接
    df1: employee=["Bob","Jake","Lisa","Sue"], group=["Accounting","Engineering","Engineering","HR"]
    df2: employee=["Lisa","Bob","Jake","Sue"], hire_date=[2004,2008,2012,2014]
    返回元组 (pd.merge(df1, df2) 的 shape, hire_date 列表)
    预期：((4, 3), [2008, 2012, 2004, 2014])
    """
    pass


def ex7():
    """
    练习7：merge 多对一连接
    df1: employee=["Bob","Jake","Lisa","Sue"], group=["Accounting","Engineering","Engineering","HR"]
    df2: group=["Accounting","Engineering","HR"], supervisor=["Carly","Guido","Steve"]
    返回 pd.merge(df1, df2) 的 supervisor 列表
    预期：['Carly', 'Guido', 'Guido', 'Steve']
    """
    pass


def ex8():
    """
    练习8：merge 多对多连接（行的笛卡尔积）
    df1: employee=["Bob","Jake","Lisa","Sue"], group=["Accounting","Engineering","Engineering","HR"]
    df2: group=["Accounting","Accounting","Engineering","Engineering","HR","HR"],
         skills=["math","spreadsheets","coding","linux","spreadsheets","organization"]
    返回 pd.merge(df1, df2) 的行数
    预期：8
    """
    pass


def ex9():
    """
    练习9：列名不同时用 left_on / right_on
    df1: employee=["Bob","Jake","Lisa","Sue"], group=["Accounting","Engineering","Engineering","HR"]
    df2: name=["Bob","Jake","Lisa","Sue"], salary=[70000,80000,120000,90000]
    返回元组 (pd.merge(df1, df2, left_on="employee", right_on="name") 的列名列表, salary 列表)
    预期：(['employee', 'group', 'name', 'salary'], [70000, 80000, 120000, 90000])
    """
    pass


def ex10():
    """
    练习10：how 参数（集合操作规则）
    df1: name=["Peter","Paul","Mary"], food=["fish","beans","bread"], columns=["name","food"]
    df2: name=["Mary","Joseph"], drink=["wine","beer"], columns=["name","drink"]
    返回元组 (默认 inner 的行数, how="outer" 的行数, how="left" 的行数)
    预期：(1, 4, 3)
    """
    pass


def ex11():
    """
    练习11：重名列与 suffixes
    df1: name=["Bob","Jake","Lisa","Sue"], rank=[1,2,3,4]
    df2: name=["Bob","Jake","Lisa","Sue"], rank=[3,1,4,2]
    返回元组 (默认后缀合并后的列名列表, suffixes=("_df1","_df2") 后的列名列表)
    预期：(['name', 'rank_x', 'rank_y'], ['name', 'rank_df1', 'rank_df2'])
    """
    pass


def ex12():
    """
    练习12：用 left_index / right_index 按索引合并
    df1: employee=["Bob","Jake","Lisa","Sue"], group=["Accounting","Engineering","Engineering","HR"]
    df2: employee=["Lisa","Bob","Jake","Sue"], hire_date=[2004,2008,2012,2014]
    先分别 set_index("employee")，再 pd.merge(..., left_index=True, right_index=True)
    返回合并结果的行索引列表
    预期：['Bob', 'Jake', 'Lisa', 'Sue']
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
    # print("ex12:", ex12())
