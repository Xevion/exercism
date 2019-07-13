def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError(f'strand_a (length {len(strand_a)}) has a different length from strand_b (length {len(strand_b)}), hamming distance cannot be computed.')
    return len(strand_a) - len([char for index, char in enumerate(strand_a) if char == strand_b[index]])