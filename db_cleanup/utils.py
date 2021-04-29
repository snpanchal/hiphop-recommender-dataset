from re import search

def replace_separators(artists):
    if search('Devin the Dude, Lil\' Flip', artists):
        return 'Devin the Dude, Lil\' Flip|Devin The Dude|Lil\' Flip'
    elif artists != 'Tyler, The Creator':
        return artists.replace(', ', '|')
    return artists