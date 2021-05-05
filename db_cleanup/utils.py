from re import search

def replace_separators(artists):
    if artists != 'Tyler, The Creator':
        return artists.replace(', ', '|')
    return artists