DROP TABLE AlbumArtists;
DROP TABLE AlbumFeatures;
DROP TABLE Albums;
DROP TABLE Artists;

-- Create Albums table
CREATE TABLE Albums (
    spotify_id CHAR(22) NOT NULL,
    name VARCHAR(125) NOT NULL,
    PRIMARY KEY (spotify_id)
);

CREATE TEMPORARY TABLE TempAlbums (
    spotify_id CHAR(22) NOT NULL,
    name VARCHAR(125) NOT NULL,
    artists VARCHAR(150) NOT NULL,
    PRIMARY KEY (spotify_id)
);

\copy TempAlbums FROM 'Albums.csv' DELIMITER ',' CSV HEADER;

INSERT INTO Albums(spotify_id, name)
SELECT spotify_id, name
FROM TempAlbums;

DROP TABLE TempAlbums;

-- Create Artists table
CREATE TABLE Artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(40) NOT NULL
);

\copy Artists FROM 'Artists.csv' DELIMITER ',' CSV HEADER;

-- Create AlbumFeatures table
CREATE TABLE AlbumFeatures (
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

\copy AlbumFeatures FROM 'AlbumFeatures.csv' DELIMITER ',' CSV HEADER;

-- Create AlbumArtists table
CREATE TABLE AlbumArtists (
    spotify_id CHAR(22) NOT NULL,
    artist_id INTEGER NOT NULL,
    FOREIGN KEY (spotify_id) REFERENCES Albums(spotify_id),
    FOREIGN KEY (artist_id) REFERENCES Artists(id)
);

CREATE TEMPORARY TABLE TempAlbumArtists (
    spotify_id CHAR(22) NOT NULL,
    artist VARCHAR(40) NOT NULL
);

\copy TempAlbumArtists FROM 'AlbumArtists.csv' DELIMITER ',' CSV HEADER;

INSERT INTO AlbumArtists(spotify_id, artist_id)
SELECT spotify_id, id AS artist_id
FROM TempAlbumArtists INNER JOIN Artists ON TempAlbumArtists.artist = Artists.name;

DROP TABLE TempAlbumArtists;