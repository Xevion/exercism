import re

def encode(string):
    return ''.join(map(lambda item : '{}{}'.format(len(item.group(0)), item.group(0)[0]) if len(item.group(0)) > 1 else item.group(0), re.finditer(re.compile(r'(.)\1{0,}'), string)))

def decode(string):
    return ''.join([sub[-1] * int(sub[:-1]) if len(sub) >= 2 else sub for sub in re.findall(re.compile(r'(\d*.)'), string)])