from math import log2, ceil

scores = {
    1 : 'eggs',
    2 : 'peanuts',
    4 : 'shellfish',
    8 : 'strawberries',
    16 :'tomatoes',
    32 : 'chocolate',
    64 : 'pollen',
    128 : 'cats'
}

class Allergies(object):
    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        return item.lower().strip() in self.lst

    @property
    def lst(self):
        temp1 = []
        if self.score > (2 ** len(scores)):
            self.score -= (2 ** (ceil(log2(self.score)) - 1))
        while self.score > 0:
            temp2 = max(scores.keys(), key= lambda item : 0 if item > self.score else item)
            self.score -= temp2
            temp1.append(scores[temp2])
        return list(dict.fromkeys(temp1))