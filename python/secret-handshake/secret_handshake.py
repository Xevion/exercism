action_codes = {'wink' : 4, 'double blink' : 3, 'close your eyes' : 2, 'jump' : 1, 'reverse' : 0}
rev_action_codes = {v : k for k, v in action_codes.items()}

def commands(number):
    number = number % 32
    # Turn it into a enumerated int list via bin
    numbers = list(enumerate(map(int, bin(number)[2:].zfill(5))))
    # Turn enabled bits into encoded items
    numbers = list(map(lambda item : rev_action_codes[item[0]] if item[1] else item[0], numbers))
    # Filter out the remaining disabled ints
    numbers = list(filter(lambda item : type(item) is str, numbers))
    if 'reverse' in numbers:
        return numbers[1:]        
    return list(reversed(numbers))

# Supports reverse actions
def secret_code(actions):
    reverse = 16 if len(actions) >= 2 and action_codes[actions[0]] < action_codes[actions[-1]] else 0    
    actions = ['1' if action in actions else '0' for action in action_codes]
    return reverse + int(''.join(actions)[::-1], base=2)