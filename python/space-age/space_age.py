from functools import partial

class SpaceAge(object):
    def __init__(self, seconds):
        self.seconds = seconds
        self.gen = lambda n : partial(self.factor, n)
        self.on_mercury = self.gen(0.241)
        self.on_venus = self.gen(0.615)
        self.on_earth = self.gen(1.00070137)
        self.on_mars = self.gen(1.881)
        self.on_jupiter = self.gen(11.862)
        self.on_saturn = self.gen(29.457)
        self.on_uranus = self.gen(84.011)
        self.on_neptune = self.gen(164.79)

    def factor(self, n):
        return round(self.seconds / (n * 365 * 24 * 60 * 60), 2)