from random import choices
from string import ascii_uppercase
from itertools import product
from random import shuffle

nums = (str(x).zfill(3) for x in range(1000))
front = (''.join(fr) for fr in product(ascii_uppercase, ascii_uppercase))
names = [l + n for l, n in product(front, nums)]
shuffle(names)
name_iter = iter(names)

class Robot(object):
    def __init__(self):
        self.reset()

    def reset(self):
        self.name = next(name_iter)