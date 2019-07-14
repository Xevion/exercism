import re

def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False
    for line in lines:
        if re.match('###### (.*)', line) is not None:
            line = '<h6>' + line[7:] + '</h6>'
        elif re.match('## (.*)', line) is not None:
            line = '<h2>' + line[3:] + '</h2>'
        elif re.match('# (.*)', line) is not None:
            line = '<h1>' + line[2:] + '</h1>'
        m = re.match(r'\* (.*)', line)
        if m:
            in_list, is_bold, is_italic = not in_list, False, False
            current_line = m.group(1)
            # Bold
            strongmatch = re.match('(.*)__(.*)__(.*)', current_line)
            if strongmatch:
                current_line = strongmatch.group(1) + '<strong>' + \
                    strongmatch.group(2) + '</strong>' + strongmatch.group(3)
                is_bold = True
            # Italics
            italicmatch = re.match('(.*)_(.*)_(.*)', current_line)
            if italicmatch:
                current_line = italicmatch.group(1) + '<em>' + italicmatch.group(2) + \
                    '</em>' + italicmatch.group(3)
                is_italic = True
                
            line = '<ul><li>' + current_line + '</li>' if not in_list else '<li>' + current_line + '</li>'
        else:
            if in_list:
                in_list_append = True
                in_list = False

        m = re.match('<h|<ul|<p|<li', line)
        if not m:
            line = '<p>' + line + '</p>'
        m = re.match('(.*)__(.*)__(.*)', line)
        if m:
            line = m.group(1) + '<strong>' + m.group(2) + '</strong>' + m.group(3)
        m = re.match('(.*)_(.*)_(.*)', line)
        if m:
            line = m.group(1) + '<em>' + m.group(2) + '</em>' + m.group(3)
        if in_list_append:
            line = '</ul>' + line
            in_list_append = False
        res += line
    if in_list:
        res += '</ul>'
    return res
