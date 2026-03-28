import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Stil ayarı
sns.set(style="whitegrid")


def load_data():
    df = pd.read_csv("netflix_titles.csv")
    df = df.dropna()
    return df


def plot_type_distribution(df):
    plt.figure(figsize=(6, 4))

    ax = sns.countplot(x="type", data=df, palette="pastel")

    plt.title("Distribution of Movies vs TV Shows", fontsize=14)
    plt.xlabel("Type")
    plt.ylabel("Count")

    # Üstüne sayı yaz
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}',
                    (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='bottom')

    plt.show()


def plot_top_genres(df):
    genres = df["listed_in"].str.split(", ")

    all_genres = []
    for g in genres:
        all_genres.extend(g)

    genre_series = pd.Series(all_genres)

    top_genres = genre_series.value_counts().head(10)

    plt.figure(figsize=(10, 5))

    sns.barplot(x=top_genres.values, y=top_genres.index, palette="coolwarm")

    plt.title("Top 10 Genres on Netflix", fontsize=14)
    plt.xlabel("Count")
    plt.ylabel("Genre")

    plt.show()


def plot_release_trend(df):
    release_counts = df["release_year"].value_counts().sort_index()

    plt.figure(figsize=(10, 5))

    sns.lineplot(x=release_counts.index, y=release_counts.values)

    plt.title("Content Release Trend Over Years", fontsize=14)
    plt.xlabel("Year")
    plt.ylabel("Number of Titles")

    plt.show()


def main():
    df = load_data()

    plot_type_distribution(df)
    plot_top_genres(df)
    plot_release_trend(df)


if __name__ == "__main__":
    main()