class pupils:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):
        print(self.name, self.marks)

    def update_mark(self, new_marks):
        self.marks = new_marks