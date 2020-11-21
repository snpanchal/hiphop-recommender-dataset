class Album:
    def __init__(self, id, name, explicit):
        self.id = id
        self.name = name
        self.explicit = explicit


def remove_duplicates(albums_list):
    albums_map = {}
    for album in albums_list:
        if ((not album.name.lower() in albums_map) or (not albums_map[album.name].explicit)):
            albums_map[album.name.lower()] = album

    return list(albums_map.values())
