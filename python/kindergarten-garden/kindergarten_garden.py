names = {'V' : 'Violets', 'R' : 'Radishes', 'C' : 'Clover', 'G' : 'Grass'}
default = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']

class Garden(object):
    def __init__(self, diagram, students=default):
        self.diagram, self.students = diagram, students
        self.diagram = [list(row) for row in self.diagram.split('\n')]
        self.diagram = [[(row[i], row[i+1]) for i in range(0, len(row), 2)] for row in self.diagram]
        # Zip everything so that top and bottom become a single row. This should support multiple rows.
        self.diagram = list(zip(*(row for row in self.diagram)))
        # Merge the zipped stuff out of it's paired form
        self.diagram = [sum(set, ()) for set in self.diagram]
        # Get the proper names of everything in the list
        self.diagram = [list(map(lambda short : names[short], seq)) for seq in self.diagram]
        # print(self.diagram)

    def plants(self, student):
        if student not in self.students:
            raise ValueError(f'Student \'{student}\' does not exist.')
        return self.diagram[self.students.index(student)]