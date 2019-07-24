from string import ascii_lowercase as low

class Cipher(object):   
    def __init__(self, key=None):
        self.key = key
        self.shift = 27 - (sum([low.index(char) for char in self.key]) % 25)
        shifted = low[self.shift:] + low[:self.shift]
        print(low)
        print(shifted)
        self.encode_ = str.maketrans(low, shifted)
        self.decode_ = str.maketrans(shifted, low)

    def encode(self, text):
        return text.translate(self.encode_)

    def decode(self, text):
        return text.translate(self.decode_)

x = list(zip('iamapandabear', 'ldpdsdqgdehdu'))
x = sorted(dict.fromkeys(x))
x = 
from pprint import PrettyPrinter
print = PrettyPrinter().pprint

# c = Cipher('d' * 18)
# print(c.encode('iamapandabear'))