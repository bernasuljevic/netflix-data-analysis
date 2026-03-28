import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("netflix_titles.csv")
df["type"].value_counts().plot(kind="bar")

plt.title("Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()
# Türleri ayır
genres = df["listed_in"].str.split(", ")

# Listeyi düzleştir
all_genres = []
for g in genres:
    all_genres.extend(g)

genre_series = pd.Series(all_genres)

# En popüler türler
genre_series.value_counts().head(10).plot(kind="bar")

plt.title("Top Genres")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.show()

df["release_year"].value_counts().sort_index().plot()

plt.title("Content Release Over Years")
plt.xlabel("Year")
plt.ylabel("Count")
plt.show()

print(df.head())
# Eksik verileri kontrol et
print(df.isnull().sum())

# Eksik değerleri doldur veya sil
df = df.dropna()
print(df["type"].value_counts())
