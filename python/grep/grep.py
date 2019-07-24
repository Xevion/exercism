<<<<<<< HEAD
from functools import partial

all_flags = ['n', 'l', 'i', 'v', 'x', 'm'] # m for multiple files

# Main grep function that works on multiple files
def grep(pattern, flags, files):
    # Parse the flags into a dictionary
    flags = [flag.strip('-').strip() for flag in flags.split()]
    flags = {k : k in flags for k in all_flags}
    flags['m'] = len(files) > 1
    # Parse all the files given and then concatenate into a string
    res = [grep_individual(pattern, flags, filename) for filename in files]
    res = '\n'.join(list(filter(None, res))) # Filters out empty strings
    return res + '\n' if len(res) > 0 else ''

# Matching function with options for case, full match and inversion
def match(subtext, text, case=True, full=False, invert=False):
    if not case:
        subtext, text = subtext.lower(), text.lower()
    res = (subtext == text) if full else (subtext in text)
    return not res if invert else res

# Function for processing against a individual file
def grep_individual(pattern, flags, filename):
    # Create a local matching function using partial with the flags set
    localmatch = partial(match, case=not flags['i'], full=flags['x'], invert=flags['v'])
    text = open(filename, 'r').read()
    result = []
    if not flags['l']:
        for i, line in enumerate(text.split('\n')):
            if localmatch(pattern, line):
                pieces = [line]
                # Add number to beginning
                if flags['n']:
                    pieces.insert(0, str(i + 1))
                # If multiple files, add the file name to the front furthermore
                if flags['m']:
                    pieces.insert(0, filename)
                # Kind of a funky way to be doing it, but it's alright.
                res = ':'.join(pieces)
                result.append(res)
        return '\n'.join(result)
    # File name only flags
    elif flags['l']:
        for line in text.split('\n'):
            # Returns as soon as a match is found
            if localmatch(pattern, line):
                return filename
        return ''