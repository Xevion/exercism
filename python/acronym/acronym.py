import string, re
def abbreviate(words):
    return ''.join(word.strip(string.punctuation)[0] for word in re.split(r'[\s-]+', words)).upper()