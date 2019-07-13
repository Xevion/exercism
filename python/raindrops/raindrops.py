def convert(n):
    return ''.join(['Pling' if n % 3 == 0 else '', 'Plang' if n % 5 == 0 else '', 'Plong' if n % 7 == 0 else '']) or str(n)
