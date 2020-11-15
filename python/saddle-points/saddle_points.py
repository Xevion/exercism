def saddle_points(matrix):
    # Check a single point in the matrix for if it's a saddle point
    def saddle(point):
        row = matrix[point[0]]
        column = [row[point[1]] for row in matrix]
        return max(row) == row[point[1]] and min(column) == column[point[0]]
    # Raise a value error if the matrix lengths are not consistent
    if len(set(list(map(len, matrix)))) > 1:
        d = {i : len(m) for i, m in enumerate(matrix)}
        d = sorted(list(set(list(d.values()))), reverse=True)
        raise ValueError(f'Matrix Length of {d[-1]} instead of usual {d[0]} found.')
    saddles = []
    # Check every point for if it's a saddle point
    for x, row in enumerate(matrix):
        for y, point in enumerate(row):
            if saddle((x, y)):
                saddles.append({'row' : x + 1, 'column' : y + 1})
    return saddles or [{}]