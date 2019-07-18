numerals = {1 : 'I', 5 : 'V', 10 : 'X', 50 : 'L', 100 : 'C', 500 : 'D', 1000 : 'M', 5_000 : '_V', 10_000 : '_X', 50_000 : '_L', 100_000 : '_C', 500_000 : '_D', 1_000_000 : '_M'}
match = {'V' : 'I', 'X' : 'I', 'L' : 'X', 'C' : 'X', 'D' : 'C', 'M' : 'C'}

def first(n, s=0):
    return (n, 10 ** s) if n < 10 else first(n // 10, s=s+1)

def roman(n):
    if n % 10 != 0 and len(str(n).strip('0')) > 1:
        temp = map(lambda item : int(item[1] + '0' * (len(str(n)) - 1 - item[0])), enumerate(str(n)))
        return ''.join(map(roman, temp))
    if n in numerals: return numerals[n]
    if n > 3 and (first(n)[0] + 1) * first(n)[1] in numerals:
        top = (first(n)[0] + 1) * first(n)[1]
        if n >= 4000:
            if numerals[top].startswith('_'):
                return '_' + match[numerals[top][1:]] + numerals[top]
        return match[numerals[top]] + numerals[top]
    else:
        res = ''
        while n > 0:
            best = max(numerals.keys(), key=lambda item : 0 if item > n else item)
            n -= best
            res += numerals[best]
        return res

for i in range(2950, 35000, 13):
    print('{} -> {}'.format(i, roman(i)))