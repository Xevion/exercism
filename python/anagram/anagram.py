def find_anagrams(word, candidates):
    word, lowercandidates = word.lower(), list(map(lambda item : item.lower(), candidates))
    build = {char : word.count(char) for char in word.lower()}
    return [candidates[index] for index, candidate in enumerate(lowercandidates) if {char : candidate.count(char) for char in candidate} == build and candidate != word]