
class Student:

    def __init__(self, name):
        self.name = name
        self.course_d = {}

    def __str__(self):
        out = f"    student : {self.name} : "
        out += ", ".join(self.course_d.keys())
        return out

    def append_course(self, course_ref):
        self.course_d[course_ref.name] = course_ref

    def delete_course(self, course_name):
        if course_name in self.course_d.keys():
            del self.course_d[course_name]


