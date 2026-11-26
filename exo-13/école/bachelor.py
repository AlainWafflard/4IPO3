from course import Course

class Bachelor:

    def __init__(self, name):
        self.__name = name   # "BIG"
        self.course_d = {}

    def __str__(self):
        out = f"  bachelier : {self.__name}\n"
        for ck, co in self.course_d.items():
            out += str(co)
        return out

    def add_course(self, course_name):
        self.course_d[course_name] = Course(course_name)

    def register_student(self, student_name, course_name):
        self.course_d[course_name].register_student(student_name)

