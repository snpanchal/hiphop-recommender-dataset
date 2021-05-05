DROP TABLE album_artists;
DROP TABLE album_features;
DROP TABLE albums;
DROP TABLE artists;

-- Create Albums table
CREATE TABLE albums (
    spotify_id CHAR(22) NOT NULL,
    name VARCHAR(255) NOT NULL,
    PRIMARY KEY (spotify_id)
);

CREATE TEMPORARY TABLE temp_albums (
    spotify_id CHAR(22) NOT NULL,
    name VARCHAR(255) NOT NULL,
    artists VARCHAR(255) NOT NULL,
    PRIMARY KEY (spotify_id)
);

\copy temp_albums FROM 'Albums.csv' DELIMITER ',' CSV HEADER;

INSERT INTO albums(spotify_id, name)
SELECT spotify_id, name
FROM temp_albums;

DROP TABLE temp_albums;

-- Create Artists table
CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

\copy artists FROM 'Artists.csv' DELIMITER ',' CSV HEADER;

-- Create AlbumFeatures table
CREATE TABLE album_features (
    spotify_id CHAR(22) NOT NULL,
    explicit BOOLEAN,
    acousticness NUMERIC(11, 10),
    danceability NUMERIC(11, 10),
    energy NUMERIC(11, 10),
    instrumentalness NUMERIC(11, 10),
    liveness NUMERIC(11, 10),
    loudness NUMERIC(8, 6),
    speechiness NUMERIC(11, 10),
    valence NUMERIC(11, 10),
    tempo NUMERIC(8, 5),
    PRIMARY KEY (spotify_id),
    FOREIGN KEY (spotify_id) REFERENCES Albums(spotify_id)
);

\copy album_features FROM 'AlbumFeatures.csv' DELIMITER ',' CSV HEADER;

-- Create AlbumArtists table
CREATE TABLE album_features (
    album_id CHAR(22) NOT NULL,
    artist_id INTEGER NOT NULL,
    FOREIGN KEY (album_id) REFERENCES Albums(spotify_id),
    FOREIGN KEY (artist_id) REFERENCES Artists(id),
    PRIMARY KEY (album_id, artist_id)
);

CREATE TEMPORARY TABLE temp_album_artists (
    album_id CHAR(22) NOT NULL,
    artist VARCHAR(255) NOT NULL
);

\copy temp_album_artists FROM 'AlbumArtists.csv' DELIMITER ',' CSV HEADER;

INSERT INTO album_artists(album_id, artist_id)
SELECT album_id, id AS artist_id
FROM temp_album_artists INNER JOIN Artists ON temp_album_artists.artist = artists.name;

DROP TABLE temp_album_artists;