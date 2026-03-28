import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import os

sns.set(style="whitegrid")

# Sayfa ayarı
st.set_page_config(layout="wide")

# Başlık
st.title("📊 Netflix Data Analysis Dashboard")


@st.cache_data
def load_data():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(BASE_DIR, "netflix_titles.csv")

    df = pd.read_csv(file_path)
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
    (2000, 2025)
)

# 🔍 SEARCH (ekledim sana 🔥)
search_title = st.sidebar.text_input("Search Title")

# Filtre uygula
filtered_df = df[
    (df["type"].isin(selected_type)) &
    (df["release_year"].between(year_range[0], year_range[1]))
]

if search_title:
    filtered_df = filtered_df[
        filtered_df["title"].str.contains(search_title, case=False)
    ]

# Eğer veri yoksa
if filtered_df.empty:
    st.warning("No data available for selected filters.")
    st.stop()

# 🔹 METRICS
st.markdown("## 📊 Overview")

total_titles = len(filtered_df)
total_movies = len(filtered_df[filtered_df["type"] == "Movie"])
total_tv = len(filtered_df[filtered_df["type"] == "TV Show"])
avg_year = int(filtered_df["release_year"].mean())

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Titles", total_titles)
col2.metric("Movies", total_movies)
col3.metric("TV Shows", total_tv)
col4.metric("Avg Release Year", avg_year)

# 🔹 1. Movies vs TV Shows
st.subheader("🎬 Movies vs TV Shows")

fig1, ax1 = plt.subplots(figsize=(8, 5))
sns.countplot(x="type", data=filtered_df, palette="pastel", ax=ax1)

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

countries = filtered_df["country"].str.split(", ")
all_countries = []

for c in countries:
    all_countries.extend(c)

country_series = pd.Series(all_countries)
top_countries = country_series.value_counts().head(10)

fig4, ax4 = plt.subplots(figsize=(10, 6))
sns.barplot(x=top_countries.values, y=top_countries.index, palette="viridis", ax=ax4)

st.pyplot(fig4)