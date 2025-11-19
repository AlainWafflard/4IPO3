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

    def delete_course(self, course_name):
        del self.course_d[course_name]

    def get_course(self, course_name):
        return self.course_d[course_name]

    def subscribe_student(self, stud_ref, course_name):
        self.course_d[course_name].subscribe_student(stud_ref)

