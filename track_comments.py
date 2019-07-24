import progressbar as pb
import requests
import pprint
import datetime
import bs4
import re
import os
import sys
import time

# A basic function for handling responses from the request module, as well as handling timing and data sizes of the web pages downloaded. 
def simpleReq(url):
    start = time.time()
    data = requests.get(url)
    if data.status_code != 200:
        raise ConnectionError(f'A status code other than 200 was received. ({data.status_code} @ {url})')
    end = time.time()
    request_timings.append((end - start, len(data.text.encode('utf-16-le'))))
    return data.text

def parseComment(name, url, soup):
    comment = soup.find(get_reflection)
    if comment['class'] == ['reflection']:
        return '\n\n'.join(list(map(lambda item : item.text, comment.find_all('p'))))
    return ''

# This script works on the assumption that you have a setup similar to mine.
# I have a GitHub repository linked so that on any computer I can have my Exercism progress kept in one place.
# This script may break if you don't have a track folder available (i.e you have a `java` track started but no folder on the computer available.)

# Constants & Reused Lambdas
username = 'Xevion' # CaSe SeNsItIvE Username from `Exercism.io`.
t1 = time.time()
request_timings = []
descend = lambda thing : list(thing.children)
get_solutions = lambda tag : ['solution'] == tag['class'] if tag.has_attr('class') else False
get_reflection = lambda tag : any(['reflection' in classtag for classtag in tag['class']]) if tag.has_attr('class') else False
get_url = lambda url : re.findall(r'exercism.io\/tracks\/([a-z-]+)\/exercises\/', url)[0]
get_name_from_url = lambda url : re.search(r'exercism.io\/tracks\/[a-z-]+\/exercises\/([a-z-]+)\/solutions\/', url).group(1)
pp = pprint.PrettyPrinter()
print('Requesting Profile Page Data')
data = simpleReq('https://exercism.io/profiles/{}'.format(username))
soup = bs4.BeautifulSoup(data, 'html.parser')
comments_top = """# {0} Track Comments\n\nThis page represents all my comments from my solutions currently hosted on [Exercism.io](https://exercism.io/). You can view my profile [here](https://exercism.io/profiles/Xevion).
The reason for this is simply to have a place where I can collect my comments, as well as just have some fun with Python and webscraping. Exercise file and exercise submission links will be provided for each and every exercise.
This file is for the **{0}** track, contains **{1}** submissions, **{2}** of which have comments. This file was built {3}.\n\n"""

# Find all completed exercises, find the URL to the Solution by the user and create for parsing.
# Also creates dictionary of all available tracks
solutions = soup.find_all(get_solutions)
solutions = [(descend(descend(solution)[2])[1].text, 'https://exercism.io{}'.format(descend(solution.parent)[1]['href'])) for solution in solutions]
tracks = {k : list() for k in dict.fromkeys(list(map(lambda i : get_url(i[1]), solutions)))}

# Get all comment data & parse, then put into track dictionary
print('Requesting Page Data for {} solution{} from {} {}'.format(len(solutions), 's' if len(solutions) > 1 else '', len(tracks.keys()), 'different tracks' if abs(len(tracks.keys())) != 1 else 'track'))
# Progress bar
temp = []
for solution in pb.progressbar(solutions):
    soup = bs4.BeautifulSoup(simpleReq(solution[1]), 'html.parser')
    temp.append((solution[0], solution[1], soup))
solutions = temp
solutions = [{'name' : solution[0], 'url' : solution[1], 'comment' : parseComment(*solution)} for solution in solutions]

# Send all the solutions to their appropriate tracks.
for solution in solutions:
    track = get_url(solution['url'])
    tracks[track].append(solution)

# Parse into a readable markdown format
print('Parsing all solution comments')
for track in tracks.keys():
    # Getting the path and formatting the top portion of the markdown file.
    path = os.path.join(sys.path[0], track, 'COMMENTS.md')
    submission_comments = len(list(filter(lambda item : item['comment'] != '', tracks[track])))
    top = comments_top.format(track.title(), len(tracks[track]), submission_comments, datetime.datetime.utcnow().strftime('on **%d-%m-%Y** at **%H:%M:%S UTC**'))
    
    # Adding all the comments with proper formatting and links.
    markdown_comments = []
    for submission in tracks[track]:
        true_name = get_name_from_url(submission['url'])
        file_url = './{}/{}'.format(true_name, true_name.replace('-', '_') + '.py')
        comment = "## {}\n\n[Link to File]({}) | [Link to Submission]({})\n\n{}".format(submission['name'], file_url, submission['url'], submission['comment'])
        markdown_comments.append(comment)
    
    # Join into a single string and then write it into a file.
    markdown = top + '\n\n'.join(markdown_comments)
    with open(path, 'w+') as file:
        file.write(markdown)
    print('Wrote {} KiB file for {} track'.format(round(os.path.getsize(path) / 1024, 2), track))
t2 = time.time()

# Sorry for this ridiculously long line. ;-;
print('Downloaded {} MiB in webpages.\nDownloaded & parsed in {} seconds with {}ms on average request time.'.format(round(sum([i[1] for i in request_timings]) / (1024 ** 2), 2), round(t2 - t1, 2), round((sum(i[0] for i in request_timings) / len(request_timings)) * 1000, 2)))
