import pandas as pd

df = pd.read_csv("netflix_titles.csv")

print(df.head())
# Eksik verileri kontrol et
print(df.isnull().sum())

# Eksik değerleri doldur veya sil
df = df.dropna()
print(df["type"].value_counts())
