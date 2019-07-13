class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.rows = [list(map(int, row.split(' '))) for row in self.matrix_string.split('\n')]
        self.columns = [list(column) for column in zip(*(row for row in self.rows))]

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        return self.columns[index - 1]