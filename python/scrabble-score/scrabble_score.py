dat = [('AEIOULNRST', 1), ('DG', 2), ('BCMP', 3), ('FHVWY', 4), ('K', 5), ('JX', 8), ('QZ',10)]
def score(word):
    return sum([subarr[1][1] for subarr in enumerate(dat) if char.upper() in subarr[1][0]][0] for char in word)