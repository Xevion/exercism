from itertools import takewhile

# Processing of data into a dictionary from a list taken from the site.
# I would have preferred being able to process the data from a module, or maybe a text file,
# but that's a whole lot of effort for something as simple as this.
data = [['AUG', 'Methionine'],
        ['UUU', 'UUC',	'Phenylalanine'],
        ['UUA', 'UUG',	'Leucine'],
        ['UCU', 'UCC', 'UCA', 'UCG', 'Serine'],
        ['UAU', 'UAC',	'Tyrosine'],
        ['UGU', 'UGC',	'Cysteine'],
        ['UGG', 'Tryptophan'],
        ['UAA', 'UAG', 'UGA', 'STOP']]
protein_definitions = {codon : definition for definition, codons in [(subarray[-1], subarray[:-1]) for subarray in data] for codon in codons }

def proteins(strand):
    strand = [strand[index * 3:(index * 3)+3] for index, char in enumerate(strand[::3])]
    strand = takewhile(lambda x : x != 'STOP', (protein_definitions[codon] for codon in strand))
    return list(strand)