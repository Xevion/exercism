from string import ascii_lowercase as abc
from random import shuffle

class Cipher(object):
    def __init__(self, key=None):
        if key:
            self.key = ''.join(dict.fromkeys(self.key)) # Key with repeated characters is completely useless
        elif not key:
            self.key = list(abc)
            shuffle(self.key)
            self.key = ''.join(self.key)

        key_values = [self.keyvalue(i) for i in range(len(self.key))]
        self.key_alphabets = [(abc[index:] + abc[: index]) for index in key_values]

    def encode(self, text):
        return ''.join(self.key_alphabets[index][abc.find(char)]
        for index, char in enumerate(text.lower()))

    def decode(self, text):
        return ''.join(abc[self.key_alphabets[index].find(char)]
        for index, char in enumerate(text.lower()))

    # Gets the shifting value of the key at the index specified
    def keyvalue(self, index):
        return abc.find(self.key[index % len(self.key)])