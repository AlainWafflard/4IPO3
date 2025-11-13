class Course:

    def __init__(self, name):
        self.name = name
        self.stud_d = {}

    def __str__(self):
        out = f"       cours: {self.name}"
        # for course in self.course_d.values():
        #     out += str(course) + "\n"
        return out

