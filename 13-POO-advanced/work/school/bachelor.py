from course import Course

class Bachelor:

    def __init__(self, name):
        self.name = name
        self.course_d = {}

    def __str__(self):
        out = f"   bachelier: {self.name}\n"
        for course in self.course_d.values():
            out += str(course) + "\n"
        return out

    def append_course(self, course_name):
        self.course_d[course_name] = Course(course_name)

