from string import ascii_letters

def rotate(text, key):
    key = key % 26
    return text.translate(str.maketrans(ascii_letters, ascii_letters[key:26] + ascii_letters[:key] + ascii_letters[26+key:] + ascii_letters[26:26 + key]))