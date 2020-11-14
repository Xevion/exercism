import math, string

def cipher_text(plain_text):
    # Normalize the input
    translation = str.maketrans({k : '' for k in string.punctuation})
    plain_text = plain_text.translate(translation).replace(' ', '').lower()
    if len(plain_text) == 0: return ''
    # Calculate the dimensions of the crypto square (rectangle)
    columns, matrix = math.ceil(math.sqrt(len(plain_text))), []
    rows = math.ceil(len(plain_text) / columns)
    for row in range(rows):
        # Calculate the indexes
        start, end = (row * columns), (row * columns) + columns
        # Add pieces of the matrix, adding trailing space padding
        matrix.append(plain_text[start:end].ljust(columns))
    # Rotate the matrix so you can read by column
    matrix = list(zip(*matrix))
    return ' '.join(''.join(column) for column in matrix)