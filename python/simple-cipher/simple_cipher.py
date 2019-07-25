from string import ascii_lowercase as alphabet
from pprint import PrettyPrinter
import random
print = PrettyPrinter().pprint

class Cipher(object):
    def __init__(self, key=None):
        if key:
            self.key = ''.join(dict.fromkeys(self.key)) # Key with repeated characters is completely useless
        elif not key:
            self.key = list(alphabet)
            random.shuffle(self.key)
            self.key = ''.join(self.key)

        key_values = [self.keyvalue(i) for i in range(len(self.key))]
        self.key_alphabets = [(alphabet[index:] + alphabet[: index]) for index in key_values]

    def encode(self, text):
        return ''.join(self.key_alphabets[index][alphabet.find(char)]
        for index, char in enumerate(text.lower()))

    def decode(self, text):
        return ''.join(alphabet[self.key_alphabets[index].find(char)]
        for index, char in enumerate(text.lower()))

    # Gets the shifting value of the key at the index specified
    def keyvalue(self, index):
        return alphabet.find(self.key[index % len(self.key)])

random.seed(0)
c = Cipher()
print(c.decode(c.encode('Hello World')))