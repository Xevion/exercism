def translate(text):
    return ' '.join(list(map(translate_word, text.split())))

vowels = "aeiou"
def translate_word(word):
    # Rule 1
    if word[0] in vowels or word[0:2] in ["xr", "yt"]:
        return word + "ay"
    # Rule 2
    else:
        i = [word.find(v) for v in vowels if word.find(v) != -1]
        i = min(i) if i else 999
        # Rule 4
        if 'y' in word[1:]:
            temp = word[1:].find('y')
            if temp != -1 and temp < i: i = temp + 1
        # Rule 3
        if 'qu' in word:
            temp = word.find('qu')
            if temp != -1: i = temp + 2
        return word[i:] + word[:i] + "ay"