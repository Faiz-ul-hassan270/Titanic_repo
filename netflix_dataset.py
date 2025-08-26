import numpy as np
import pandas as pd

df = pd.read_csv('netflix_titles.csv',encoding='utf-8')

print('Top 10 rows are:'.center(120,'='))
print(df.head(10))

print('Coloumn names of dataset are:'.center(120,'='))
print(df.columns)

print('Total movies and shows :'.center(120,'='))
print(df['type'].value_counts())

print('Unique ratings in dataset are :'.center(120,'='))
print(df['rating'].unique())

print('First Five records where type is movie :'.center(120,'='))
df['type'] = df['type'].str.strip().str.lower()
movie_df = df[df['type'] == 'movie']
sorted_movies = movie_df.sort_values(by='title', ascending=True)
print(sorted_movies.head(5))

# Count titles released in 2020
titles_2020 = df[df['release_year'] == 2020]
print("Number of titles released in 2020:", len(titles_2020))
print(titles_2020['type'].value_counts())

print('All shows by Rajiv chilaka :'.center(120,'='))
df['director']=df['director'].str.strip().str.lower()
rajiv_chilaka  = df[df['director']=='rajiv chilaka']
print(rajiv_chilaka[['title','director']])

print('Top 10 countries with the most Netflix titles:'.center(120, '='))
country_counts = df['country'].value_counts().head(10)
print(country_counts)

print('Most Common type:'.center(120,'='))
most_common_type = df['type'].value_counts().idxmax()
print(most_common_type)

print('Horror movies titles are :'.center(120,'='))
df['type'] = df['type'].str.strip().str.lower()
df['title'] = df['title'].str.strip().str.lower()
horror_movies = df[(df['type']=='movie') & (df['title'].str.contains('horror'))]
print(horror_movies[['title']])

print('Unique director are :'.center(120,'='))
unique_directors = df['director'].unique()
print(len(unique_directors))

print('Where India listed as a country :'.center(120,'='))
india = df[df['country']=='India']
print(india[['title','type','country']])

print('Earliest release year :'.center(120,'='))
earliest = df['release_year'].min()
print(earliest)

print('Latest release year :'.center(120,'='))
latest = df['release_year'].max()
print(latest)

print('5 random samples from the dataset :'.center(120,'='))
random_samples = df.sample(n=5)
print(random_samples)

print('Titles each country produce :'.center(120,'='))
titles = df['title'].value_counts()
print(titles)

print('Top 10 directors with most titles :'.center(120,'='))
most_titles = df['director'].value_counts().head(10)
print(most_titles)

print('TV shows with more than 3 seasons :'.center(120, '='))
df['type'] = df['type'].str.strip().str.lower()
df['duration'] = df['duration'].str.strip().str.lower()
tv_shows = df[df['type'] == 'tv show']
tv_shows['num_seasons'] = tv_shows['duration'].str.extract(r'(\d+)').astype(float)
tv_shows_more_than_3 = tv_shows[tv_shows['num_seasons'] > 3]
print(tv_shows_more_than_3[['title', 'duration']])

print('Group by type,Fing mean for release year movies vs tvshow  :'.center(120,'='))
type_group = df.groupby('type')['release_year'].mean()
print(type_group)

print('Show the titles that have both "Drama" and "International" in their listed_in.:'.center(120,'='))
titles_contained = df[(df['listed_in'].str.contains('Drama')) & (df['listed_in'].str.contains('International'))]
print(titles_contained[['title','listed_in']])

print('Movies added in 2021:'.center(120,'='))
release = df[df['release_year']==2021]
print(len(release[['title','release_year']]))

print('Month with the most titles added :'.center(120, '='))
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['month_added'] = df['date_added'].dt.month_name()
month_counts = df['month_added'].value_counts()
print(month_counts)

print('distribution (count) of shows by rating. :'.center(120, '='))
df['type'] = df['type'].str.strip().str.lower()
tv_shows = df[df['type'] == 'tv show']
count_distribution = tv_shows['rating'].value_counts()
print(count_distribution)

print('Oldest movie available on Netflix:'.center(120, '='))
df['type'] = df['type'].str.strip().str.lower()
df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')
movies = df[df['type'] == 'movie']
oldest_year = movies['release_year'].min()
oldest_movies = movies[movies['release_year'] == oldest_year]
print(oldest_movies[['title', 'release_year']])

print('latest movie available on Netflix:'.center(120, '='))
df['type'] = df['type'].str.strip().str.lower()
df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')
movies = df[df['type'] == 'movie']
latest_year = movies['release_year'].max()
latest_movies = movies[movies['release_year'] == latest_year]
print(latest_movies[['title', 'release_year']])

print('Number of titles by country and type:'.center(120, '='))
pivot_country_type = pd.pivot_table(df, 
                                    index='country', 
                                    columns='type', 
                                    values='title', 
                                    aggfunc='count', 
                                    fill_value=0)
print(pivot_country_type)

print('Pivot table showing average release year by rating:'.center(120, '='))
pivot_rating_year = pd.pivot_table(df, 
                                   index='rating', 
                                   values='release_year', 
                                   aggfunc='mean')
print(pivot_rating_year)

print('pivot table showing the count of titles by year (rows) and type (columns):'.center(120, '='))
pivot_year_type = pd.pivot_table(df,
                                 index='release_year',
                                 columns='type',
                                 values='title',
                                 aggfunc='count',
                                 fill_value=0
                                 )
print(pivot_year_type)

print('pivot table to find the most common listed_in (genre) per country:'.center(120, '='))
pivot_listed_in = pd.pivot_table(df,
                                 index='listed_in',
                                 columns='country',
                                 )

df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month_name()

print('Most common genre (listed_in) per country:'.center(120, '='))
df_clean = df[['country', 'listed_in']].dropna()
def most_common_genre(genres):
    return genres.mode().iloc[0] if not genres.mode().empty else None
genre_by_country = df_clean.groupby('country')['listed_in'].agg(most_common_genre)
print(genre_by_country)
