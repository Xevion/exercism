intro = "I know an old lady who swallowed a {}."
intro_addendums = [
    "It wriggled and jiggled and tickled inside her.",
    "How absurd to swallow a bird!",
    "Imagine that, to swallow a cat!",
    "What a hog, to swallow a dog!",
    "Just opened her throat and swallowed a goat!",
    "I don't know how she swallowed a cow!"
]
names = [
    "fly",
    "spider",
    "bird",
    "cat",
    "dog",
    "goat",
    "cow",
    "horse"
]

middle = "She swallowed the {} to catch the {}."
outro = "I don't know why she swallowed the fly. Perhaps she'll die."
last = "She\'s dead, of course!"
special_middle = "that wriggled and jiggled and tickled inside her"

# Just does the math for constructing single and multiple verses. I realized only halfway through that
# everything was going to be in lists, so I just used split, which honestly is easier than needing some kind of flattening
# or list extending setup to get the lists to be in proper order
def recite(start_verse, end_verse):
    if start_verse == end_verse:
        return construct(start_verse - 1).split('\n')
    return '\n\n'.join(construct(verse) for verse in range(start_verse - 1, end_verse)).split('\n')

# Constructs a specific verse
def construct(verse):
    # Constructs the middle part. Only the spider verse makes this function required.
    def makemiddle(versen):
        # Special spider inner verse
        if versen == 2:
            return middle.format(names[versen], names[versen-1] + ' ' + special_middle)
        return middle.format(names[versen], names[versen-1])
    # Horse verse
    if verse == 7:
        return "{}\n{}".format(intro.format(names[verse]), last)
    # Constructs the intoduction of a verse
    constructed_intro = '{}{}'.format(
        intro.format(names[verse]),
        '\n' + intro_addendums[verse-1] if verse > 0 else ''
    )
    # Constructs the middle verse using make middle
    constructed_middle = '\n'.join([''] + [makemiddle(versen) for versen in range(verse, 0, -1)]) if verse >= 1 else ''
    # Finally constructs the entire properly.
    return "{}{}{}".format(constructed_intro, constructed_middle, '\n' + outro)