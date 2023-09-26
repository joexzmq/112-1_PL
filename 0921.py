import numpy as np
import pandas as pd
import csv
import matplotlib
import seaborn as sns

file_names = ['misterdonut.csv', 'starbucks.csv']  # 將檔案名稱加入清單中
dfs = [pd.read_csv(file)['country'] for file in file_names]  # 使用清單推導式讀取country欄位資料

# 將國家名稱轉換為 set 資料型態
set_1 = set(dfs[0])
set_2 = set(dfs[1])
