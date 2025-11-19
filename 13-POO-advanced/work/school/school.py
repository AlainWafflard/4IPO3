from bachelor import Bachelor
from student import Student


class School:

    def __init__(self, name):
        self.name = name
        self.bach_d = {}
        self.stud_d = {}

    def __str__(self):
        out = f"name : {self.name}\n"
        out += "liste bacheliers :\n"
        for k, bach in self.bach_d.items():
            out += str(bach) + "\n"
        out += "liste étudiants :\n"
        for k, stud in self.stud_d.items():
            out += str(stud) + "\n"
        return out

    def append_bachelor(self, bach_name):
        self.bach_d[bach_name] = Bachelor(bach_name)

    def append_course(self, bach_name, course_name ):
        self.bach_d[bach_name].append_course(course_name)

    def delete_course(self, bach_name, course_name):
        # ordre envoyé au bachelier
        self.bach_d[bach_name].delete_course(course_name)
        # ordre envoyé à chaque étudiant
        for stud_o in self.stud_d.values():
            stud_o.delete_course(course_name)

    def append_student(self, stud_name):
        self.stud_d[stud_name] = Student(stud_name)

    def subscribe_student(self, stud_name, bach_name, course_l ):
        for c in course_l:
            # on attache le  cours à l'étudiant
            c_ref = self.bach_d[bach_name].get_course(c)
            self.stud_d[stud_name].append_course(c_ref)
            # on attache l'étudiant au cours
            self.bach_d[bach_name].subscribe_student(self.stud_d[stud_name], c)



