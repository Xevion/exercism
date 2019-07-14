import re

def parse(markdown):
    lines = markdown.split('\n')
    result, in_list, finish_list = '', False, False

    for line in lines:
        # Heading formatting
        if re.match('###### (.*)', line) is not None:
            line = '<h6>' + line[7:] + '</h6>'
        elif re.match('## (.*)', line) is not None:
            line = '<h2>' + line[3:] + '</h2>'
        elif re.match('# (.*)', line) is not None:
            line = '<h1>' + line[2:] + '</h1>'

        # List detection  
        is_list = re.match(r'\* (.*)', line) or False
        line = is_list.group(1) if is_list else line

        # Bold
        strongmatch = re.match('(.*)__(.*)__(.*)', line)
        if strongmatch:
            line = strongmatch.group(1) + '<strong>' + \
                strongmatch.group(2) + '</strong>' + strongmatch.group(3)

        # Italics
        italicmatch = re.match('(.*)_(.*)_(.*)', line)
        if italicmatch:
            line = italicmatch.group(1) + '<em>' + italicmatch.group(2) + \
                '</em>' + italicmatch.group(3)
        
        # If a list has been detected
        if is_list:
            if not in_list:
                line = '<ul><li>' + line + '</li>'
                in_list = True
            else:
                line = '<li>' + line + '</li>'
        else:
            # If a list wasn't detected, but it's supposedly trying to continue a list 
            if in_list:
                finish_list = True
                in_list = False

        # Detect whether a heading, list or text paragraph has already been started
        # This is just to ensure it's wrapped in something at the very least, and follows HTML sytnax.
        occupied = re.match('<h|<ul|<p|<li', line)
        if not occupied:
            line = '<p>' + line + '</p>'    
        
        # If a list has ended and it needs to be formally ended
        if finish_list:
            line = '</ul>' + line
            is_list = False
            finish_list = False

        # Finish this line and add it to the result.  
        result += line

    # If we have somehow not ended a list yet, complete it now.
    if in_list:
        result += '</ul>'
    
    return result