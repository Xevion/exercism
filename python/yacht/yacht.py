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


# Score categories.
# Change the values as you see fit.
ONES = 0
TWOS = 1
THREES = 2
FOURS = 3
FIVES = 4
SIXES = 5
FULL_HOUSE = 6
FOUR_OF_A_KIND = 7
LITTLE_STRAIGHT = 8
BIG_STRAIGHT = 9
CHOICE = 10
YACHT = 11

def score(dice, category):
    dice.sort()
    if any(map(lambda cat : cat == category, [ONES, TWOS, THREES, FOURS, FIVES, SIXES])):
        return (category + 1) * len([roll for roll in dice if roll == (category + 1)])
    elif category is LITTLE_STRAIGHT:
        return 30 if dice == [1,2,3,4,5] else 0
    elif category is BIG_STRAIGHT:
        return 30 if dice == [2,3,4,5,6] else 0        
    elif category is FULL_HOUSE or category is FOUR_OF_A_KIND:
        dif = sorted({num : dice.count(num) for num in dice}.items(), reverse=True, key=lambda item : item[1])
        if category is FULL_HOUSE:
            return sum(dice) if dif[0][1] == 3  and dif[1][1] == 2 else 0
        elif category is FOUR_OF_A_KIND:
            return min(dif[0][1], 4) * dif[0][0] if dif[0][1] >= 4 else 0
    elif category is CHOICE:
        return sum(dice)
    elif category is YACHT:
        return 50 if len(set(dice)) == 1 else 0