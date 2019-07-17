ismultiple = lambda num, multiples: any(num % sub == 0 for sub in multiples)

def sum_of_multiples(limit, multiples):
    multiples = [mult for mult in multiples if mult != 0]
    return sum([i for i in range(1, limit) if ismultiple(i, multiples)])