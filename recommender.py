import pandas as pd
import numpy as np
import sqlite3
from sklearn.metrics.pairwise import cosine_similarity


def replace_separators(artists):
    if artists != 'Tyler, The Creator':
        return artists.replace(', ', ' | ')
    return artists


db_con = sqlite3.connect('albums.db')
df_albums = pd.read_sql_query('SELECT * FROM albums', db_con)
df_albums_and_ids = df_albums[['spotify_id', 'name', 'artists']]
df_albums.drop(columns=['index', 'name', 'explicit'], inplace=True)
df_albums.set_index('spotify_id', inplace=True)

album_artists = df_albums['artists'].apply(replace_separators)
df_albums.drop(columns='artists', inplace=True)

print(album_artists)

test_ratings = pd.Series({
    '41GuZcammIkupMPKH2OJ6I': 5.0,
    '6FED8aeieEnUWwQqAO9zT1': 5.0,
    '42WVQWuf1teDysXiOupIZt': 5.0,
    '4PWBTB6NYSKQwfo79I3prg': 5.0
})
total_score = 0
for score in test_ratings:
    total_score += score
test_ratings = test_ratings.map(lambda score: score / total_score)

df_users = pd.DataFrame(columns=df_albums.columns)
working_df = df_albums.mul(test_ratings, axis=0)
user_profile = working_df.sum(axis=0)

df_albums = df_albums.append(user_profile, ignore_index=True)
user_row_id = len(df_albums) - 1

cosine_sim = cosine_similarity(df_albums)
similar_albums = []
for i in range(len(cosine_sim[-1])):
    similar_albums.append((i, cosine_sim[-1][i]))
recommended_albums = sorted(similar_albums, key=lambda a: a[1], reverse=True)
print(recommended_albums)
recommended_albums = list(filter(
    lambda a: df_albums_and_ids.iloc[a[0]]['spotify_id'] in test_ratings.index,
    recommended_albums
))

# for album_rated_id in test_ratings.index:
#     index = int(df_albums_and_ids[df_albums_and_ids['spotify_id']
#                                   == album_rated_id].index)
#     print(index)

for album in recommended_albums[1:11]:
    album_index = album[0]
    album_match = album[1]

    album_id = df_albums_and_ids.iloc[album_index]['spotify_id']
    album_name = df_albums_and_ids.iloc[album_index]['name']
    print('{} ({}), {}'.format(album_name, album_id, album_match))

db_con.close()
