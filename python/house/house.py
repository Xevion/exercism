# Constants for building the rhyme
secondaries = ['sowing his corn', 'that crowed in the morn', 'all shaven and shorn', 'all tattered and torn', 'all forlorn', 'with the crumpled horn']
verbs = ['belonged to', 'kept', 'woke', 'married', 'kissed', 'milked', 'tossed', 'worried', 'killed', 'ate',]
nouns = ['farmer', 'rooster', 'priest', 'man', 'maiden', 'cow', 'dog', 'cat', 'rat', 'malt',]
intial = 'This is the house that Jack built.'
first = 'This is the horse and the hound and the horn'
last = 'that lay in the house that Jack built.'
# Build the array of verses
lines = (["that {} the {}{}".format(verbs[i], nouns[i], '' if i > 5 else ' ' + secondaries[i]) for i in range(10)])[::-1]

# Build a specific verse
def verse(n):
    if n == 1: return [intial]
    if n == 12: return [first] + [lines[-1]] +  verse(11)[1:]
    return ["This is the {}{}".format(
            nouns[len(nouns) - n + 1],
            '' if n < 6 else f' {secondaries[-n + 5 ]}')] + [lines[i - 3] for i in range(n, 2, -1)] + [last]
recite = lambda start, end : [' '.join(verse(x)) for x in range(start, end + 1)]