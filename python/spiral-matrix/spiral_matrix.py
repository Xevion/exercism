# Two lines, dude. ez.
def spiral_matrix(size):
    return [] if size < 1 else Matrix(size).matrix

# Class for a pathfinding based spiral generation
class Matrix:
    def __init__(self, size):
        self.size = size
        self.matrix = [[None for y in range(size)] for x in range(size)]
        self.i = 1
        self.cur = (0, 0)
        self.cardinals = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        self.dir_index = 0
        self.loop()

    # Loop that builds the spiral matrix
    def loop(self):
        # While the current number is less than the maximum number
        while self.i < (self.size ** 2):
            # If the next position is not valid, turn
            if not self.valid(self.nextpos):
                self.dir_index = (self.dir_index + 1) % 4
            else:
                self.access()
                self.cur = self.nextpos
        self.access()
    
    # Access a position and increment the counter
    def access(self):
        self.matrix[self.cur[0]][self.cur[1]] = self.i
        self.i += 1

    # Just the current direction (as an offset)
    @property
    def direction(self):
        return self.cardinals[self.dir_index]

    # Next position for access based on the current direction
    @property
    def nextpos(self):
        return (self.cur[0] + self.direction[0], self.cur[1] + self.direction[1])

    # Determine whether a position is valid to be approached
    def valid(self, pos):
        return self.validxy(pos[0], pos[1]) and not self.matrix[pos[0]][pos[1]]

    # Determine whether a position is 
    def validxy(self, x, y):
        return x >= 0 and x < self.size and y >= 0 and y < self.size
    
    # Printable Matrix with proper character space justification
    def __repr__(self):
        return '\n'.join([' '.join(map(lambda item : str(item or '?').rjust(len(str(self.size ** 2))), sub)) for sub in self.matrix])