import pandas as pd
import sqlite3
from sklearn.metrics.pairwise import cosine_similarity
from re import search


def replace_separators(artists):
    if search('Devin the Dude, Lil\' Flip', artists):
        return 'Devin the Dude, Lil\' Flip|Devin The Dude|Lil\' Flip'
    elif artists != 'Tyler, The Creator':
        return artists.replace(', ', '|')
    return artists


def filter_out_rated_album(album):
    return not df_albums_info.iloc[album[0]]['spotify_id'] in test_ratings.index


db_con = sqlite3.connect('albums.db')
df_albums = pd.read_sql_query('SELECT * FROM albums', db_con)
df_albums_info = df_albums[['spotify_id', 'name', 'artists']]
df_albums.drop(columns=['index', 'name', 'explicit'], inplace=True)
df_albums.set_index('spotify_id', inplace=True)

album_artists = df_albums['artists'].apply(replace_separators)
df_albums.drop(columns='artists', inplace=True)

df_album_artists = album_artists.str.get_dummies()
df_albums = pd.concat([df_albums, df_album_artists], axis=1)

test_ratings = pd.Series({
    '41GuZcammIkupMPKH2OJ6I': 5.0,
    '4yP0hdKOZPNshxUOjY0cZj': 3.0
})
total_score = 0
for score in test_ratings:
    total_score += score
test_ratings = test_ratings.map(lambda score: score / total_score)

working_df = df_albums.mul(test_ratings, axis=0)
user_profile = working_df.sum(axis=0)
for album_id in test_ratings.index:
    artists_value = df_albums_info[df_albums_info['spotify_id']
                                   == album_id]['artists'].iloc[0]
    album_artists = replace_separators(artists_value).split('|')
    for artist in album_artists:
        user_profile[artist] = 1

df_albums = df_albums.append(user_profile, ignore_index=True)
user_row_id = len(df_albums) - 1

cosine_sim = cosine_similarity(df_albums)
similar_albums = []
for i in range(len(cosine_sim[-1])):
    similar_albums.append((i, cosine_sim[-1][i]))
recommended_albums = sorted(similar_albums, key=lambda a: a[1], reverse=True)
recommended_albums = list(filter(
    filter_out_rated_album, recommended_albums[1:]
))

for album in recommended_albums[1:21]:
    album_index = album[0]
    album_match = album[1]

    album_id = df_albums_info.iloc[album_index]['spotify_id']
    album_name = df_albums_info.iloc[album_index]['name']
    album_artists = df_albums_info.iloc[album_index]['artists']
    print('{} - {} (by {}), {}'.format(album_id, album_name, album_artists, album_match))

db_con.close()
