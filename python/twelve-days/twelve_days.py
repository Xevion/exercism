nouns =['twelve Drummers Drumming,', 'eleven Pipers Piping,', 'ten Lords-a-Leaping,', 'nine Ladies Dancing,', 'eight Maids-a-Milking,','seven Swans-a-Swimming,','six Geese-a-Laying,', 'five Gold Rings,', 'four Calling Birds,', 'three French Hens,', 'two Turtle Doves,', 'a Partridge in a Pear Tree.']
positions = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
expression = [['On the {} day of Christmas my true love gave to me:'.format(position)] for position in positions]
for i in range(len(expression)):
    build = nouns[12-i-1:]
    if i != 0: build[-1] = 'and ' + build[-1] # [and] a Partridge in a Pear Tree
    expression[i] = ' '.join(expression[i] + build)

def recite(start=1, end=12):
    if start > end or start < 1 or end > 12:
        raise ValueError(f'Incorrect Parameters, sentence selection {start} to {end} is invalid.')
    return expression[start-1:end]