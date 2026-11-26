from bachelor import Bachelor

class HigherSchool:

    def __init__(self, name):
        self.__name = name
        self.bachelor_d = {}

    def __str__(self):
        """
        nom : IFC
        liste bacheliers:
          bachelier : BIG
            cours : statistiques
              student : Rudy
              student : Ali
            cours : algorithmique
              student : Rudy
            cours : database
               student : Rudy
               student : Ali
        bachelier : BII
        cours : interface
        cours : électronique
        student : Rudy
        liste étudiants:
        student : Rudy : algorithmique, database,
        électronique, statistiques
        student : Ali : database, statistiques
        """
        out = f"nom:{self.__name}\n"
        out += f"liste des bacheliers:\n"
        for bk, bo in self.bachelor_d.items():
            out += str(bo)
        return out

    def __repr__(self):
        return "brol"

    def add_bachelor(self, name):
        self.bachelor_d[name] = Bachelor(name)

    def add_course_to_bachelor(self, bach_name, course_name ):
        self.bachelor_d[bach_name].add_course(course_name)

    def register_student(self, student_name, bachelor_name, course_name ):
        self.bachelor_d[bachelor_name].register_student(student_name, course_name)

