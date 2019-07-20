from string import ascii_letters, punctuation, whitespace

rev = ascii_letters[25::-1] + ascii_letters[:25:-1]
enc = str.maketrans(ascii_letters, rev)
dec = str.maketrans(rev, ascii_letters)
san = str.maketrans('', '', punctuation)

def groupings(text, groupby=5):
    for i in range(0, len(text), groupby):
        yield  text[i:i + groupby]

def sanitize(text):
    return ''.join(text.translate(san).split())

def encode(plain_text, groupby=5):
    return ' '.join(groupings(sanitize(plain_text.translate(enc).lower()), groupby=groupby))

def decode(ciphered_text):
    return ''.join(ciphered_text.translate(dec).lower().split())