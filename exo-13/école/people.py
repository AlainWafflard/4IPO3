class People:

    def __init__(self):
        self.student_l = []
        self.higherschool = None

    def setHigherSchool(self, hso):
        self.higherschool = hso

    def register_student(self, name):
        self.student_l.append(name)

    def register_student_to_course(self, student_name, bachelor_name, course_name ):
        if student_name not in self.student_l:
            print( "étudiant non enregistré, exit : " + student_name)
        self.higherschool.register_student( student_name, bachelor_name, course_name )

