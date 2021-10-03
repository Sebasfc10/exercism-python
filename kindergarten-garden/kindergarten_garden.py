class Garden(object):
    plant_names = {
        'C': 'Clover',
        'G': 'Grass',
        'R': 'Radishes',
        'V': 'Violets'
    }
    def __init__(self, diagram, students=['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']):
        self.rows = diagram.split()
        self.students = sorted(students)
    def plants(self, student):
        i = self.students.index(student) * 2
        return [Garden.plant_names[plant] for row in self.rows for plant in row[i:i+2]]
