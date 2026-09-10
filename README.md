# easy-numpy-pandas

一套面向 **NumPy 与 Pandas** 的数据分析入门练习项目。

项目以《尚硅谷大模型技术之 numpy 与 pandas 2.0》教材为蓝本，把每一节的知识点拆成
可直接运行的小练习：`train/` 里只保留题目和 `pass`，`answer/` 里给出可运行的参考实现。
练习使用的数据集统一放在 `data/` 目录，配套学习笔记放在 `numpy/numpy.md` 与 `pandas/pandas.md`。

## 项目结构

```
easy-numpy-pandas/
├── data/                       # 练习用 CSV 数据集（练习题统一从这里加载）
│   ├── weather.csv             # 逐日天气数据（1461 行 × 6 列）
│   ├── weather_withna.csv      # 含缺失值的天气数据（用于缺失值处理练习）
│   ├── employees.csv           # 员工数据（107 行 × 10 列）
│   ├── sleep.csv               # 睡眠健康数据（400 行 × 13 列）
│   ├── house_sales.csv         # 房屋销售数据（10000 行 × 19 列，综合案例用）
│   └── penguins.csv            # 企鹅数据集（备用）
├── docs/                       # 教材原文（.docx，本地文件，已被 .gitignore 忽略）
├── numpy/
│   ├── numpy.md                # NumPy 学习笔记
│   ├── train/                  # 第 2 章练习题：2.3 ~ 2.9
│   └── answer/                 # 对应的参考答案
├── pandas/
│   ├── pandas.md               # Pandas 学习笔记
│   ├── images/                 # 笔记中的配图
│   ├── train/                  # 第 3 章练习题：3.2 ~ 3.13
│   └── answer/                 # 对应的参考答案
├── demo/
│   └── demo1/                  # 第 4 章综合案例：房地产市场洞察与价值评估
│       ├── house_sales_exercise.py   # 综合练习题
│       └── house_sales_answer.py     # 答案解析
├── main.py
├── pyproject.toml
└── README.md
```

## 环境准备

项目依赖 `numpy`、`pandas`、`matplotlib` 三个库，验证环境如下：

| 依赖 | 版本 |
|------|------|
| Python | 3.11（实测 3.11.7） |
| numpy | 1.26.3 |
| pandas | 2.1.4 |
| matplotlib | 3.8.0 |

安装依赖：

```bash
pip install numpy pandas matplotlib
```

## 使用方式

### 1. 做练习

打开 `numpy/train/` 或 `pandas/train/` 下任意一个文件，按提示完成即可：

- 文件顶部的文档字符串列出该小节的知识点回顾；
- 每个 `exN` 函数都有题目说明和"预期"结果，函数体目前是 `pass`；
- 把 `pass` 替换成自己的实现，并 `return` 题目要求的结果；
- 完成后取消 `if __name__ == "__main__":` 中对应 `print` 的注释，逐一自测。

```python
if __name__ == "__main__":
    # 完成后可取消注释逐一自测
    print("ex1:", ex1())
    # print("ex2:", ex2())
    # print("ex3:", ex3())
```

### 2. 运行与自测

在仓库根目录直接运行文件即可（数据通过文件绝对路径定位，无需关心当前工作目录）：

```bash
# 运行练习题
python numpy/train/2.3_ndarray_attributes.py

# 运行参考答案，对照输出
python numpy/answer/2.3_ndarray_attributes.py
```

绘图类练习（3.12 / 3.13 / demo1）默认只创建画布、不弹窗；想看图形时，在 `__main__`
中取消注释 `plt.show()` 即可。

### 3. 数据加载约定

所有依赖数据的练习都通过统一的 `DATA_DIR` 定位到仓库的 `data/` 目录，因此可任意位置运行：

```python
from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[2] / "data"
df = pd.read_csv(DATA_DIR / "weather.csv")
```

## 数据集说明

| 文件 | 行 × 列 | 主要字段 |
|------|---------|----------|
| `weather.csv` | 1461 × 6 | date, precipitation, temp_max, temp_min, wind, weather |
| `weather_withna.csv` | 1461 × 6 | 同上，字段含缺失值 |
| `employees.csv` | 107 × 10 | employee_id, first_name, last_name, email, phone_number, job_id, salary, commission_pct, manager_id, department_id |
| `sleep.csv` | 400 × 13 | person_id, gender, age, occupation, sleep_duration, sleep_quality, physical_activity_level, stress_level, bmi_category, blood_pressure, heart_rate, daily_steps, sleep_disorder |
| `house_sales.csv` | 10000 × 19 | id, date, price, bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, condition, grade, sqft_above, sqft_basement, yr_built, yr_renovated, zipcode, lat, long |
| `penguins.csv` | - | species, island, bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g, sex |

## 练习索引

### 第 2 章 NumPy（`numpy/train`）

| 文件 | 主题 | 题量 |
|------|------|------|
| 2.3_ndarray_attributes.py | ndarray 的属性 | 5 |
| 2.4_ndarray_creation.py | ndarray 的创建 | 8 |
| 2.5_ndarray_dtype.py | 数据类型 dtype | 4 |
| 2.6_slicing_indexing.py | 切片与索引 | 6 |
| 2.7_common_functions.py | 常用函数 | 8 |
| 2.8_operations_broadcast.py | 运算与广播 | 6 |
| 2.9_matmul.py | 矩阵乘法 | 5 |

### 第 3 章 Pandas（`pandas/train`）

| 文件 | 主题 | 数据源 | 题量 |
|------|------|--------|------|
| 3.2_series.py | Series | 内联示例 | 10 |
| 3.3_dataframe.py | DataFrame | 内联示例 | 10 |
| 3.4_datetime.py | 日期时间 | 内联示例 | 8 |
| 3.5_data_analysis.py | DataFrame 数据分析入门 | weather.csv / employees.csv | 10 |
| 3.6_combine.py | 数据合并 | 内联示例 | 12 |
| 3.7_missing.py | 缺失值处理 | weather_withna.csv | 12 |
| 3.8_apply.py | apply 应用 | 内联示例 | 9 |
| 3.9_groupby.py | 分组聚合 | employees.csv | 15 |
| 3.10_pivot_table.py | 透视表 | sleep.csv | 10 |
| 3.11_timeseries.py | 时间序列 | weather.csv | 11 |
| 3.12_matplotlib.py | matplotlib 绘图 | weather.csv | 8 |
| 3.13_pandas_plot.py | Pandas 绘图 | sleep.csv | 9 |

### 第 4 章 综合案例（`demo/demo1`）

| 文件 | 说明 | 题量 |
|------|------|------|
| house_sales_exercise.py | 房地产市场洞察与价值评估：数据清洗 → 特征工程 → 探索性分析 → 分组聚合 → 可视化 | 19 |
| house_sales_answer.py | 综合案例的完整答案解析 | 19 |

## 约定与提示

- **先做后对**：建议先完成 `train/` 中的练习，再对照 `answer/` 检查；不要直接抄答案。
- **预期值即验收标准**：每个 `exN` 的文档字符串里都写了"预期"结果，返回后可直接比对。
- **真实数据量较大**：如 weather 有 1461 行、house_sales 有 10000 行，涉及整列统计的题目在
  "预期"中只列出部分结果作为参考，实际返回完整结果。
- **Pandas 频率别名**：在 pandas 2.1.x 下请使用 `M` / `Q` / `A` 等旧别名（教材中的
  `ME` / `QE` / `YE` 该版本尚不支持）。
- **绘图自测技巧**：不弹窗也能校验图形，例如 `len(ax.patches)` 看柱子数量、
  `ax.collections[0].get_offsets().shape[0]` 看散点数量。
