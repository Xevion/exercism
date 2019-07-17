def primes(limit):
    v = [False] * 2 + [True] * (limit+1)
    for (i, prime) in enumerate(v):
        if prime:
            for x in range(i * i, limit+1, i):
                v[x] = False
    return [x for x, y in enumerate(v) if y and x <= limit]