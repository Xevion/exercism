def tally(rows):
    # Subcommand that adds teams if not yet added, and processes the result from them
    def process(team, result):
        if team not in teams.keys():
            teams[team] = {'MP' : 0, 'W' : 0, 'D' : 0, 'L' : 0, 'P' : 0}
        if result == 'win':
            teams[team]['W'] += 1
            teams[team]['P'] += 3
        elif result == 'draw':
            teams[team]['D'] += 1
            teams[team]['P'] += 1
        elif result == 'loss':
            teams[team]['L'] += 1
        teams[team]['MP'] += 1
    teams, output = {}, ['Team'.ljust(31) + '| MP |  W |  D |  L |  P']
    # Quick lambda that swaps the result for the enemy team
    swap = lambda result : 'win' if result == 'loss' else 'loss' if result == 'win' else 'draw'
    for row in rows:
        team1, team2, result = row.split(';')
        process(team1, result); process(team2, swap(result))
    # Process all the data with formatting. rjust and ljust add proper spacing for the scoring, so it allows double digit scores
    for teamname, data in sorted(teams.items(), key=lambda item : (max([t['P'] for t in teams.values()]) - int(item[1]['P']), item[0])):
        output.append('{}| {} | {} | {} | {} | {}'.format(teamname.ljust(31), str(data['MP']).rjust(2), str(data['W']).rjust(2), str(data['D']).rjust(2), str(data['L']).rjust(2), str(data['P']).rjust(2)))
    return output