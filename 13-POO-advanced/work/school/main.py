# Ecrivez le POO d'une école
# ▪ L'école organise des bacheliers, ceux-ci
# constitués d'un ensemble de cours.
# ▪ L'école organise un cours dans un bachelier
# en y inscrivant les étudiants.
# ▪ Un étudiant peut se désinscrire d'un cours.
# ▪ L'école peut renvoyer un étudiant.
# ▪ L'écoel peut supprimer un cours.
# ▪ Cf schéma, slide suivant
from bachelor import Bachelor

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
        return out

    def append_bachelor(self, bach_name):
        self.bach_d[bach_name] = Bachelor(bach_name)

    def append_course(self, bach_name, course_name ):
        self.bach_d[bach_name].append_course(course_name)

    def append_student(self, stud_name):
        pass

    def subscribe_student(self, stud_name, course_l ):
        pass


if __name__ == "__main__":
    # ▪ Scénario d'utilisation
    # ▪ Créer une école "IFC".
    school = School("IFC")
    # ▪ Créer un bachelier "BIG" avec trois cours:
    school.append_bachelor("BIG")
    school.append_bachelor("BII")
    # ▪ Statistiques
    school.append_course("BIG", "statistiques")
    # ▪ Algorithmique
    school.append_course("BIG", "algorithmique")
    # ▪ Database
    school.append_course("BIG", "database")
    school.append_course("BII", "électronique")
    school.append_course("BII", "statistiques")

    # ▪ Créer deux étudiants : Rudy et Ali.
    school.append_student("Rudy")
    school.append_student("Ali")
    # ▪ Créer l'inscription de chaque étudiant à deux cours.
    # ▪ Rudy : algorithmique, database
    school.subscribe_student("Rudy", [ "algorithmique", "database" ])
    # ▪ Ali : database, statistiques
    school.subscribe_student("Ali", [ "database", "statistiques" ])
    # ▪ Imprimer l'état des inscriptions dans le
    # bachelier BIG
    print(school)
    # ▪ par cours
    # ▪ par étudiant
    # ▪ Supprimer le cours d'Algorithmique.
    # ▪ Désinscrire l'étudiant Rudy du cours de Database
    # ▪ Renvoyer l'étudiant Ali.
    # ▪ Ajouter l'étudiant Youssef, inscrit à tous les
    # cours.
    # ▪ Imprimer l'état des inscriptions.