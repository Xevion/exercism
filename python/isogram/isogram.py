def is_isogram(string):
    string = ''.join([c for c in string.casefold() if c not in ' -'])
    return len(list(set(string))) == len(string)