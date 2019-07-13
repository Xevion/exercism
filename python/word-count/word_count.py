import string, re
def count_words(sentence):
    sentence = [x.strip(string.punctuation) for x in [word for word in re.split(r'[_,\s]+', sentence.casefold()) if len(word.strip(string.punctuation + string.whitespace)) >= 1]]
    return {k : sentence.count(k) for k in list(dict.fromkeys(sentence))}