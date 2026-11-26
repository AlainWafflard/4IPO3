class Course:

    def __init__(self, name):
        self.__name = name
        self.student_l = []

    def __str__(self):
        out = f"    cours : {self.__name}\n"
        for student_name in self.student_l:
            out += f"      student : {student_name}\n"
        return out

    def register_student(self, student_name):
        self.student_l.append(student_name)

