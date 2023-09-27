import numpy as np
import pandas as pd
import csv
import matplotlib
import seaborn as sns

file_names = ['nba0001.csv', 'nba2223.csv']  # 將檔案名稱加入清單中
df1 = [pd.read_csv(file)['team'] for file in file_names]  # 使用清單推導式讀取team欄位資料
df2 = [pd.read_csv(file)['rate'] for file in file_names]  # 使用清單推導式讀取rate欄位資料
df0 = [pd.read_csv(file) for file in file_names]  # 使用清單推導式讀取team欄位資料

# 將欄位資料轉換為 set 資料型態
set1_1 = set(df1[0])
set1_2 = set(df1[1])
set2_1 = set(df2[0])
set2_2 = set(df2[1])

team = np.arange(30)
rate = np.arange(58)

years = np.linspace(1960, 2017, 58)
numbers = np.arange(58)

trace = sns.scatterplot(
    x = years,
    y = numbers)

print(df0)
