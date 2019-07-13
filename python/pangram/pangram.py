import string
charset = string.ascii_lowercase

def is_pangram(sentence):
    dictionary = {char : True if char in sentence.lower() else False for char in charset}
    return all(dictionary.values())
