from functools import partial
flatten_base = lambda l : [l] if type(l) != list else sum(map(flatten_base, l), [])
flatten = lambda l : list(filter(lambda item : item is not None, flatten_base(l)))