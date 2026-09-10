"""
3.9 Pandas 的数据聚合、转换、过滤函数 —— 练习

知识点回顾：
    1. groupby 返回 DataFrameGroupBy 对象（惰性，未调用聚合函数前不计算）
       - .groups 查看分组字典（键为组标签，值为该组行索引列表）
       - .get_group(标签) 取出某组
       - .groupby("列")["列"] 取出 SeriesGroupBy
       - 支持按组迭代：for dept, group in df.groupby("列")
       - 按多字段分组得到复合索引；as_index=False 或 reset_index() 可还原为列
    2. pd.cut(x, bins, right, labels)：分箱
       - bins 为整数表示等宽分成 n 段；为列表表示指定边界；labels 指定区间标签
    3. 聚合 agg：一次算多个统计值（agg(["min","median","max"])），
       或多列用不同统计值（agg({"列A": "nunique", "列B": "mean"})），
       也可传入自定义函数（参数是每一组的 Series）
    4. transform：转换后形状与原数据一致（如各组减去组均值做标准化、按组均值填充缺失值）
    5. filter：按分组的属性丢弃整组（如只保留 commission_pct 全非空的组）

说明：
    下面的 _employees() 从 data/employees.csv 加载数据（与教材一致）。
    你只需要把每个练习函数中的 pass 替换成自己的实现，函数返回题目要求的
    结果。
    注意：真实数据量较大（107 行、11 个部门），涉及整列处理的题目在"预期"
    中只列出前/后若干项作为参考，实际返回完整结果。
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[2] / "data"


def _employees():
    """从 data/employees.csv 加载员工数据"""
    return pd.read_csv(DATA_DIR / "employees.csv")


def ex1():
    """
    练习1：返回 df.groupby("department_id") 的类名（字符串）
    预期：'DataFrameGroupBy'
    """
    pass


def ex2():
    """
    练习2：返回 df.groupby("department_id").groups（分组字典）
    键为 department_id，值为该组的行索引；共 11 个分组。
    预期：{10.0: [100], 20.0: [101, 102], 30.0: [14, 15, 16, 17, 18, 19],
           40.0: [103], 50.0: [20, ..., 99], 60.0: [3, 4, 5, 6, 7], ...}
    """
    pass


def ex3():
    """
    练习3：用 get_group(20) 取出分组为 20 的数据，返回其行索引列表
    预期：[101, 102]
    """
    pass


def ex4():
    """
    练习4：按 department_id 分组，计算 salary 平均值，返回结果列表
    预期（11 项，未四舍五入）：
          [4400.0, 9500.0, 4150.0, 6500.0, 3475.5555555555557, 5760.0,
           10000.0, 8955.882352941177, 19333.333333333332, 8600.0, 10150.0]
    """
    pass


def ex5():
    """
    练习5：按组迭代，返回列表 [(组标签, 该组 shape), ...]
    预期：[(10.0, (1, 10)), (20.0, (2, 10)), (30.0, (6, 10)), (40.0, (1, 10)),
           (50.0, (45, 10)), (60.0, (5, 10)), (70.0, (1, 10)), (80.0, (34, 10)),
           (90.0, (3, 10)), (100.0, (6, 10)), (110.0, (2, 10))]
    """
    pass


def ex6():
    """
    练习6：按多字段分组
    df.groupby(["department_id", "job_id"])[["salary", "commission_pct"]].mean()
    返回该结果的索引列表（复合索引，每个元素是元组）
    预期：共 19 项，如
          [(10.0, 'AD_ASST'), (20.0, 'MK_MAN'), (20.0, 'MK_REP'),
           (30.0, 'PU_CLERK'), (30.0, 'PU_MAN'), ...,
           (110.0, 'AC_ACCOUNT'), (110.0, 'AC_MGR')]
    """
    pass


def ex7():
    """
    练习7：同上但使用 as_index=False，返回结果的列名列表
    预期：['department_id', 'job_id', 'salary', 'commission_pct']
    """
    pass


def ex8():
    """
    练习8：cut 分箱（指定边界）
    salary = pd.Series([4400, 13000, 6000, 11000, 2600])
    pd.cut(salary, [0, 10000, 20000])，返回转成字符串后的列表
    预期：['(0, 10000]', '(10000, 20000]', '(0, 10000]', '(10000, 20000]', '(0, 10000]']
    """
    pass


def ex9():
    """
    练习9：cut 分箱并指定标签
    同样的 salary，pd.cut(salary, [0, 10000, 20000], labels=["low", "high"])
    返回结果列表
    预期：['low', 'high', 'low', 'high', 'low']
    """
    pass


def ex10():
    """
    练习10：一次计算多个统计值
    按 department_id 分组，对 salary 用 agg(["min", "median", "max"])
    返回结果的二维值列表
    预期（11 行）：
          [[4400.0, 4400.0, 4400.0], [6000.0, 9500.0, 13000.0],
           [2500.0, 2850.0, 11000.0], [6500.0, 6500.0, 6500.0],
           [2100.0, 3100.0, 8200.0], [4200.0, 4800.0, 9000.0],
           [10000.0, 10000.0, 10000.0], [6100.0, 8900.0, 14000.0],
           [17000.0, 17000.0, 24000.0], [6900.0, 8000.0, 12000.0],
           [8300.0, 10150.0, 12000.0]]
    """
    pass


def ex11():
    """
    练习11：不同列用不同统计值
    按 department_id 分组，分别求 job_id 的 nunique 与 commission_pct 的 mean
    返回元组 (job_id 种类数列表, commission_pct 均值列表)
    预期：([1, 2, 2, 1, 3, 1, 1, 2, 2, 2, 2],
           [nan, nan, nan, nan, nan, nan, nan, 0.225, nan, nan, nan])
    """
    pass


def ex12():
    """
    练习12：重命名统计值
    基于练习11的 agg 结果，用 rename 把列名改为
    {"job_id": "工种数", "commission_pct": "佣金比例平均值"}
    返回重命名后的列名列表
    预期：['工种数', '佣金比例平均值']
    """
    pass


def ex13():
    """
    练习13：向 agg 传入自定义函数
    定义函数接收一组 last_name（Series），返回该组 last_name 首字母的排序去重列表。
    按 department_id 分组后 agg，返回结果列表
    预期：共 11 项，如 [['W'], ['F', 'H'], ['B', 'C', 'H', 'K', 'R', 'T'], ...]
    """
    pass


def ex14():
    """
    练习14：分组转换 transform——每组 salary 减去该组均值（标准化）
    返回结果列表（每个值保留 2 位小数，共 107 项）
    预期：前5项 [4666.67, -2333.33, -2333.33, 3240.0, 240.0]
    """
    pass


def ex15():
    """
    练习15：分组过滤 filter
    按 department_id 分组，只保留 commission_pct 不含空值的分组
    返回过滤后数据的 department_id 列表
    预期：共 34 行，department_id 全部为 80.0
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
    # print("ex13:", ex13())
    # print("ex14:", ex14())
    # print("ex15:", ex15())
