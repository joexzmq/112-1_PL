import pandas as pd

# 讀取多個檔案
# 使用 pandas 的 read_csv 函式讀取 CSV 檔案並將其轉換為 DataFrame
file_names = ['misterdonut.csv', 'starbucks.csv']  # 將檔案名稱加入清單中
dfs = [pd.read_csv(file) for file in file_names]  # 使用清單推導式讀取所有檔案

# 產生交集
intersection = pd.merge(dfs[0], dfs[1], how='inner')
for df in dfs[2:]:
    intersection = pd.merge(intersection, df, how='inner')
data1 = set(intersection['country'])

# 產生差集
difference = pd.concat(dfs).drop_duplicates(keep=False)
data2 = set(difference['country'])

# 產生聯集
union = pd.concat(dfs).drop_duplicates()
data3 = set(union['country'])

# 印出結果
print("交集：")
print(data1)

print("\n差集：")
print(data2)

print("\n聯集：")
print(data3)

