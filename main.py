import pandas as pd

# 需求1：读取数据并打印概览
try:
    df = pd.read_csv("pdd-01.csv")
    print(f"一共有 {len(df)} 行数据。")
    print("每列空值数量：")
    print(df.isnull().sum())
    print(f"完全重复的行数：{df.duplicated().sum()}")
except Exception as e:
    print(f"读取 CSV 失败，请检查 pdd-01.csv 文件是否存在。错误信息：{e}")
