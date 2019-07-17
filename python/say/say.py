sub = {
    1_000_000_000_000 : 'trillion',
    1_000_000_000 : 'billion',
    1_000_000 : 'million',
    1000 : 'thousand',
    100 : 'hundred',
    90 : 'ninety',
    80 : 'eighty',
    70 : 'seventy',
    60 : 'sixty',
    50 : 'fifty',
    40 : 'forty',
    30 : 'thirty',
    20 : 'twenty',
}

number = {
    12 : 'twelve',
    11 : 'eleven',
    10 : 'ten',
    9 : 'nine',
    8 : 'eight',
    7 : 'seven',
    6 : 'six',
    5 : 'five',
    4 : 'four',
    3 : 'three',
    2 : 'two',
    1 : 'one',
    0 : 'zero'
}

teen = {i + 10 : number[i] + 'teen' for i in range(3, 10)}
teen[13] = 'thirteen';teen[15] = 'fifteen';teen[18] = 'eighteen'

def say(n):
    if n < 0:
        raise ValueError(f'Cannot parse negative number \'{n}\'')
        # return 'negative ' + say(abs(n))
    elif n < 13:
        return number[n]
    elif n < 20:
        return teen[n]
    elif n < 100:
        return sub[n // 10 * 10] + (('-' + number[n % 10]) if n % 10 != 0 else '')
    elif max(*tuple(sub.keys()), n) == n:
        raise ValueError(f'Cannot support large number \'{n}\'')
    else:
        res = []
        while n > 0:
            if n >= 100:
                temp = max(sub.keys(), key=lambda item: 0 if item > n else item)
                prefix = n // temp
                n = n % temp
                res.append(say(prefix) + ' ' + sub[temp])
            else:
                res.append(say(n))
                n = 0
        if len(res) < 2: return ' '.join(res)
        return ' '.join(res[:-1]) + ' and ' + res[-1]