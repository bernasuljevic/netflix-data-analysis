import pandas as pd
import matplotlib.pyplot as plt


def load_data():
    df = pd.read_csv("netflix_titles.csv")
    df = df.dropna()
    return df


def plot_type_distribution(df):
    plt.figure()
    df["type"].value_counts().plot(kind="bar")
    plt.title("Movies vs TV Shows")
    plt.xlabel("Type")
    plt.ylabel("Count")
    plt.show()


def plot_top_genres(df):
    genres = df["listed_in"].str.split(", ")
    
    all_genres = []
    for g in genres:
        all_genres.extend(g)

    genre_series = pd.Series(all_genres)

    plt.figure()
    genre_series.value_counts().head(10).plot(kind="bar")
    plt.title("Top Genres")
    plt.xlabel("Genre")
    plt.ylabel("Count")
    plt.show()


def plot_release_trend(df):
    plt.figure()
    df["release_year"].value_counts().sort_index().plot()
    plt.title("Content Release Over Years")
    plt.xlabel("Year")
    plt.ylabel("Count")
    plt.show()


def main():
    df = load_data()

    print(df.head())
    print(df.isnull().sum())

    plot_type_distribution(df)
    plot_top_genres(df)
    plot_release_trend(df)


if __name__ == "__main__":
    main()