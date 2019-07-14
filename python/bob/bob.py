def response(hey_bob):
    if hey_bob.strip() == '':
        return "Fine. Be that way!"
    elif hey_bob.upper() == hey_bob and ''.join(x.upper() for x in hey_bob if x.upper() in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ') != '':
        return "Calm down, I know what I'm doing!" if hey_bob.strip().endswith('?') else "Whoa, chill out!"
    elif hey_bob.strip().endswith('?'):
        return "Sure."
    else:
        return "Whatever."