def factors(value):
    factors, n = [], 2
    while value > 1:
        while value % n == 0:
            factors.append(n)
            value /= n
        n += 1
    return factors