import sqlite3
import pandas as pd
from utils import replace_separators

db_con = sqlite3.connect('../albums.db')

df_albums = pd.read_sql_query('SELECT * FROM albums', db_con)
df_albums['artists'] = df_albums['artists'].apply(replace_separators)
df_albums.set_index('spotify_id', inplace=True)
album_ids = list(df_albums.index)

df_album_artists = pd.DataFrame(columns=['spotify_id', 'artist'])
for album_id in album_ids:
    album_artists = df_albums.loc[album_id, 'artists'].split('|')
    for artist in album_artists:
        df_album_artists = df_album_artists.append({'spotify_id': album_id, 'artist': artist}, ignore_index=True)

df_album_artists.to_sql('AlbumArtists', db_con, if_exists='replace', index=False)

db_con.close()