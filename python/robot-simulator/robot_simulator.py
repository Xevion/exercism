import re

# Globals for the bearings
# Change the values as you see fit
EAST = (1, 0)
NORTH = (0, 1)
WEST = (-1, 0)
SOUTH = (0, -1)
BEARINGS = [NORTH, EAST, SOUTH, WEST]
BEARINGSF = ['North', 'East', 'South', 'West']

class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.x, self.y, self.bearing = x, y, bearing
        self.turn_left, self.turn_right = lambda : self.turn(), lambda : self.turn(isright=True)    
    @property
    def coordinates(self):
        return (self.x, self.y)

    def simulate(self, commands):
        [self.turn(True, n=len(c)) if c[0] == 'R' else self.turn(n=len(c)) if c[0] == 'L' else self.advance(n=len(c)) if c[0] == 'A' else None for c in map(lambda item : item[0], re.finditer(r'(\w)\1*', commands))]
    
    def advance(self, n=1):
        self.x, self.y = self.x + (self.bearing[0] * n), self.y + (self.bearing[1] * n)

    def turn(self, isright=False, n=1):
        for _ in range(n):
            index = (BEARINGS.index(self.bearing) + (1 if isright else -1))
            self.bearing = BEARINGS[0 if index == 4 else index]

    def __repr__(self):
        return f'<Robot ({self.x}, {self.y})/{BEARINGSF[BEARINGS.index(self.bearing)]}>'