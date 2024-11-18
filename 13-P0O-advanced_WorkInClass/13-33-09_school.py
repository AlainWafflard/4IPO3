class School:

    def __init__(self, name):
        self.name = name
        self.bachelor_d = {}
        self.student_d = {}

    def __str__(self):
        out = f"nom : {self.name}\n"
        out += f'liste bacheliers:\n'
        for bac_o in self.bachelor_d.values():
            out += str(bac_o)
        return out

    def add_bachelor(self, name):
        self.bachelor_d[name] = Bachelor(name)

    def add_course(self, bac_name, cou_name):
        self.bachelor_d[bac_name].add_course(cou_name)

    def register_student(self,name):
        self.student_d[name] = Student(name)

    def register_course(self, stu_name, bac_name, cou_name):
        stu_o = self.student_d[stu_name]
        self.bachelor_d[bac_name].register_course(stu_o, cou_name)


class Bachelor:

    def __init__(self, name):
        self.name = name
        self.course_d = {}

    def __str__(self):
        out = f"    bachelier {self.name}\n"
        for cou_o in self.course_d.values():
            out += str(cou_o)
        return out

    def add_course(self, cou_name):
        self.course_d[cou_name] = Course(cou_name)

    def register_course(self, stu_o, cou_name):
        self.course_d[cou_name].register(stu_o)


class Course:

    def __init__(self,cou_name):
        self.name = cou_name
        self.student_d = {}

    def __str__(self):
        out = f"        cours {self.name}\n"
        for stu_o in self.student_d.values():
            out += str(stu_o)
        return out

    def register(self, stu_o):
        self.student_d[stu_o.name] = stu_o


class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"            student : {self.name}\n"


if __name__ == "__main__":

    school = School("ISFCE")
    school.add_bachelor("BIG")
    school.add_course( "BIG", "stats")
    school.add_course( "BIG", "db")
    school.add_course( "BIG", "algo")
    school.add_bachelor("BII")
    school.add_course( "BII", "stats")
    school.add_course( "BII", "réseaux")
    school.add_course( "BII", "os")
    school.register_student("Rudy")
    school.register_course("Rudy", "BIG", "algo")
    school.register_course("Rudy", "BIG", "db")
    school.register_student("Ali")
    school.register_course("Ali", "BIG", "db")
    school.register_course("Ali", "BII", "stats")
    print(school)

