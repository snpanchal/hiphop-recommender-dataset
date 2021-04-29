import sqlite3
import pandas as pd
from utils import replace_separators

db_con = sqlite3.connect('../albums.db')

df_albums = pd.read_sql_query('SELECT * FROM albums', db_con)
df_albums['artists'] = df_albums['artists'].apply(replace_separators)

all_artists = set()
for a in df_albums['artists']:
    all_artists.update(a.split('|'))

all_artists = list(all_artists)
df_artists = pd.DataFrame({'artist': all_artists})
df_artists.set_index('artist')
df_artists.to_sql('Artists', db_con, if_exists='replace', index_label='id')

db_con.close()