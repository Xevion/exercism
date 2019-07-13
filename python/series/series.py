from itertools import takewhile
def slices(series, length):
    if length > len(series) or length <= 0:
        raise ValueError('[length] parameter cannot be {}.'.format('longer than [series]' if length > len(series) else 'shorter than zero'))
    return list(takewhile(lambda x : len(x) == length, (series[index:index+length] for index in range(len(series)))))