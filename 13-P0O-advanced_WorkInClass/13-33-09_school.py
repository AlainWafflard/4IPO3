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
        out += f'liste étudiants:\n'
        for stu_o in self.student_d.values():
            out += str(stu_o)
        return out

    def add_bachelor(self, name):
        self.bachelor_d[name] = Bachelor(name)

    def add_course(self, bac_name, cou_name):
        self.bachelor_d[bac_name].add_course(cou_name)

    def del_course(self, bac_name, cou_name):
        cou_o = self.bachelor_d[bac_name].get_course_o(cou_name)
        # enlever ce cours de la liste des inscriptions des étudiants
        for stu_o in self.student_d.values():
            stu_o.unregister_course(cou_o)
        # enlever le cours du bac
        self.bachelor_d[bac_name].del_course(cou_name)

    def register_student(self,name):
        self.student_d[name] = Student(name)

    def register_course(self, stu_name, bac_name, cou_name):
        stu_o = self.student_d[stu_name]
        self.bachelor_d[bac_name].register_course(stu_o, cou_name)
        cou_o = self.bachelor_d[bac_name].get_course_o(cou_name)
        stu_o.register_course(cou_o)


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

    def del_course(self, cou_name):
        del self.course_d[cou_name]

    def register_course(self, stu_o, cou_name):
        self.course_d[cou_name].register(stu_o)

    def get_course_o(self,cou_name):
        return self.course_d[cou_name]


class Course:

    def __init__(self,cou_name):
        self.name = cou_name
        self.student_d = {}

    def __str__(self):
        out = f"        cours {self.name}\n"
        for stu_o in self.student_d.values():
            out += repr(stu_o)
        return out

    def register(self, stu_o):
        self.student_d[stu_o.name] = stu_o


class Student:

    def __init__(self, name):
        self.name = name
        self.course_d = {}

    def __repr__(self):
        return f"            student : {self.name}\n"

    def __str__(self):
        out = f"    student {self.name} : "
        for cou_s in self.course_d.keys():
            out += cou_s + ", "
        out += "\n"
        return out

    def register_course(self, cou_o):
        self.course_d[cou_o.name] = cou_o

    def unregister_course(self, cou_o):
        try:
            del self.course_d[cou_o.name]
        except:
            pass


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
    school.register_course("Ali", "BIG", "stats")
    print(school)

    school.del_course("BIG", "stats")
    print(school)

