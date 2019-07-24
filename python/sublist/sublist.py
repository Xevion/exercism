"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3

def subfinder(mylist, pattern):
    matches = []
    for i, val in enumerate(mylist):
        if val == pattern[0] and mylist[i:i+len(pattern)] == pattern:
            matches.append(pattern)
    return matches

def sublist(one, two):
    if one == two: return EQUAL
    if not one or not two: return SUBLIST if not one else SUPERLIST if not two else UNEQUAL    
    return SUPERLIST if subfinder(one, two) else SUBLIST if subfinder(two, one) else UNEQUAL

x, y = [1, 2, 4], [5, 6, 1, 1, 2, 4, 7, 8]
print(sublist(x, y))
print(sublist(y, x))