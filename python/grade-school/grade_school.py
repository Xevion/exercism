class School(object):
    def __init__(self):
        self.data = {}

    # Just an easier way of handling self.grade & self.add_student, less typing
    def get(self, grade):
        return self.data[grade] if grade in self.data.keys() else []

    def add_student(self, name, grade):
        self.data[grade] = self.get(grade) + [name]
        
    def roster(self):
        return sum([sorted(seq[1]) for seq in sorted(self.data.items(), key=lambda item : item[0])], [])

    def grade(self, grade):
        return sorted(self.get(grade))