class Course:

    def __init__(self, name):
        self.name = name
        self.stud_d = {}

    def __str__(self):
        out = f"       cours: {self.name} : "
        out += ", ".join(self.stud_d.keys())
        return out

    def subscribe_student(self, stud_ref):
        self.stud_d[stud_ref.name] = stud_ref
