from math import sqrt

def dist(x1, y1, x2=0, y2=0):
    return sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

def score(x, y):
    distance = dist(x, y)
    return 10 if distance <= 1 else 5 if distance <= 5 else 1 if distance <= 10 else 0