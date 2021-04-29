import sqlite3
import pandas as pd

db_con = sqlite3.connect('../albums.db')

# Export data in albums table
df_albums = pd.read_sql_query('SELECT * FROM albums', db_con)
df_albums.to_csv(path_or_buf='../create_psql_db/Albums.csv', index=False)

# Export data in Artists table
df_artists = pd.read_sql_query('SELECT * FROM Artists', db_con)
df_artists.to_csv(path_or_buf='../create_psql_db/Artists.csv', index=False)

# Export data in AlbumArtists table
df_album_artists = pd.read_sql_query('SELECT * FROM AlbumArtists', db_con)
df_album_artists.to_csv(path_or_buf='../create_psql_db/AlbumArtists.csv', index=False)

# Export data in album_features table
df_album_features = pd.read_sql_query('SELECT * FROM album_features', db_con)
df_album_features.to_csv(path_or_buf='../create_psql_db/AlbumFeatures.csv', index=False)

db_con.close()