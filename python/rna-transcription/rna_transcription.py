transition = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}
def to_rna(dna_strand):
    return ''.join(transition[char] for char in dna_strand)