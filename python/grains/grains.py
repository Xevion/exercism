square = lambda number : exec('raise ValueError(\'Value {} is invalid ({}).\')'.format(number, 'too high' if number > 64 else 'too low')) if number > 64 or number < 1 else 2 ** (number - 1)
total = lambda number : exec('raise ValueError(\'Value {} is invalid (too low).\')'.format(number)) if number < 1 else sum([square(i) for i in range(1, number+1)])