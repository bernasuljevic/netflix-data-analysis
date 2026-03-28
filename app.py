import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style="whitegrid")

# Sayfa ayarı
st.set_page_config(layout="wide")

# Başlık
st.title("📊 Netflix Data Analysis Dashboard")


@st.cache_data
def load_data():
    df = pd.read_csv("netflix_titles.csv")
    df = df.dropna()
    return df


df = load_data()

# 🎯 FİLTRELER
st.sidebar.header("Filters")

selected_type = st.sidebar.multiselect(
    "Select Type",
    options=df["type"].unique(),
    default=df["type"].unique()
)

year_range = st.sidebar.slider(
    "Select Release Year Range",
    int(df["release_year"].min()),
    int(df["release_year"].max()),
    (2000, 2020)
)

# Filtre uygula
filtered_df = df[
    (df["type"].isin(selected_type)) &
    (df["release_year"].between(year_range[0], year_range[1]))
]

# 🔹 1. Movies vs TV Shows
st.subheader("🎬 Movies vs TV Shows")

fig1, ax1 = plt.subplots(figsize=(8, 5))
sns.countplot(x="type", data=filtered_df, palette="pastel", ax=ax1)

for p in ax1.patches:
    ax1.annotate(f'{int(p.get_height())}',
                 (p.get_x() + p.get_width()/2., p.get_height()),
                 ha='center', va='bottom')

st.pyplot(fig1)

# 🔹 2. Top Genres
st.subheader("🎭 Top Genres")

genres = filtered_df["listed_in"].str.split(", ")
all_genres = []

for g in genres:
    all_genres.extend(g)

genre_series = pd.Series(all_genres)
top_genres = genre_series.value_counts().head(10)

fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(x=top_genres.values, y=top_genres.index, palette="coolwarm", ax=ax2)

st.pyplot(fig2)

# 🔹 3. Release Trend
st.subheader("📈 Release Trend")

release_counts = filtered_df["release_year"].value_counts().sort_index()

fig3, ax3 = plt.subplots(figsize=(10, 5))
sns.lineplot(x=release_counts.index, y=release_counts.values, ax=ax3)

st.pyplot(fig3)
# 🔹 4. Top Countries
st.subheader("🌍 Top Countries Producing Content")

# country sütununu parçala
countries = filtered_df["country"].str.split(", ")
all_countries = []

for c in countries:
    all_countries.extend(c)

country_series = pd.Series(all_countries)
top_countries = country_series.value_counts().head(10)

fig4, ax4 = plt.subplots(figsize=(10, 6))
sns.barplot(x=top_countries.values, y=top_countries.index, palette="viridis", ax=ax4)

st.pyplot(fig4)