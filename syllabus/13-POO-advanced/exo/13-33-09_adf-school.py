# Tous les attributs sont mis publics, afin d'alléger l'écriture.
# Mettre ces attributs privés serait l'étape suivante.

class Higherschool:
    # la classe "école" gère les bacheliers et les étudiants
    def __init__(self, name):
        self.name = name
        self.bachelor_d = {}
        self.student_d = {}

    def __str__(self):
        out = "nom : " + self.name + "\n"
        out += "liste bacheliers:" + "\n"
        for bac_o in self.bachelor_d.values():
            out += "    " + str(bac_o) + "\n"
        out += "liste étudiants:" + "\n"
        for stud_o in self.student_d.values():
            out += "    " + str(stud_o) + "\n"
        return out

    def add_bachelor(self, bac_name):
        # ajouter le bachelier au dictionnaire
        self.bachelor_d[bac_name] = Bachelor(bac_name)

    def del_bachelor(self, bac_name):
        # non implanté
        pass

    def add_lecture(self, bach_n, lect_n):
        # ajouter le cours au bachelier
        self.bachelor_d[bach_n].add_lecture(lect_n)

    def del_lecture(self, bach_n, lect_n):
        # supprimer le cours du bachelier
        self.bachelor_d[bach_n].del_lecture(lect_n)
        # supprimer les étudiants inscrits 
        for k, st in self.student_d.items():
            st.unregister(lect_n)

    def add_student(self, stud_n):
        # inscrire l'étudiant à l'école
        self.student_d[stud_n] = Student(stud_n)

    def del_student(self, stud_n):
        # supprimer l'étudiant
        # mais avant, le désinscrire de tous les cours 
        this_stud = self.student_d[stud_n]
        for bac in self.bachelor_d.values():
            bac.unregister(this_stud)
        # self.student_d[stud_n] = None : KO
        del(self.student_d[stud_n])

    def register(self, stud_n, bach_n, lect_n):
        # inscrire l'étudiant au cours du bachelier
        this_bac = self.bachelor_d[bach_n]
        this_stud = self.student_d[stud_n]
        this_bac.register(this_stud, lect_n)
        # ou :
        # self.bachelor_d[bach_n].register( self.student_d[stud_n], lect_n )

    def unregister(self, stud_n, bach_n, lect_n):
        # désinscrire l'étudiant du cours du bachelier
        self.bachelor_d[bach_n].unregister(self.student_d[stud_n], lect_n)
        self.student_d[stud_n].unregister(lect_n)


class Bachelor:
    """ la classe "bachelier" gère les cours
    """
    def __init__(self, name):
        self.name = name
        self.lecture_d = {}

    def __str__(self):
        out = "bachelier : " + self.name + "\n"
        for lect_o in self.lecture_d.values():
            out += "        " + str(lect_o)
        return out

    def add_lecture(self, name):
        self.lecture_d[name] = Lecture(name)

    def del_lecture(self, name):
        # self.lecture_d[name] = None : KO
        del(self.lecture_d[name])

    def register(self, stud_o, lect_n ):
        self.lecture_d[lect_n].register(stud_o)

    def unregister(self, stud_o, lect_n=None ):
        if lect_n is None:
            # désinscrire l'étudiant de tous les cours
            for lect_o in self.lecture_d.values():
                lect_o.unregister(stud_o)
        else:
            # désinscrire l'étudiant du cours donné en param
            self.lecture_d[lect_n].unregister(stud_o)


class Lecture:
    """ la classe "cours" gère les inscriptions des étudiants
    """
    def __init__(self, name):
        self.name = name
        self.student_d = {}

    def __str__(self):
        out = "cours : " + self.name + "\n"
        for stud in self.student_d.values():
            out += "          " + repr(stud) + "\n"
        return out

    def register(self, stud_o):
        self.student_d[stud_o.name] = stud_o
        stud_o.register(self)

    def unregister(self, stud_o):
        # on désinscrit l'étudiant du cours
        # si l'étudiant n'y était pas inscrit, alors passer
        try:
            # self.student_d[stud_o.name] = None : KO
            del(self.student_d[stud_o.name])
        except:
            pass


class Student:
    """ la classe "étudiant" gère les cours auquel il s'est inscrit
    """
    def __init__(self, name):
        self.name = name
        self.lecture_d = {}

    def __str__(self):
        # retourne le nom de l'étudiant et les cours suivis par celui-ci
        s = "  student : " + self.name + " : " + ", ".join(self.lecture_d.keys())
        return s

    def __repr__(self):
        # retourne le nom de l'étudiant
        s = "  student : " + self.name
        return s

    # def __del__(self):
    #     print("etudiant détruit", self.name)

    def register(self, lect_o):
        self.lecture_d[lect_o.name] = lect_o

    def unregister(self, lect_n):
        # on désinscrit le cours de l'étudiant
        # si l'étudiant n'y était pas inscrit, alors passer
        # print(f"debug unregister {self.name} from {lect_n}", self)
        try:
            # self.lecture_d[lect_n] = None
            del (self.lecture_d[lect_n])
        except:
            pass



if __name__ == "__main__":
    # Créer une école "IFC".
    s = Higherschool("IFC")

    # Créer un bachelier "BIG" avec trois cours:
    s.add_bachelor("BIG")
    s.add_lecture("BIG", "statistiques")
    s.add_lecture("BIG", "algorithmique")
    s.add_lecture("BIG", "database")

    # Pour le fun, créer un bachelier "BII" avec deux cours:
    s.add_bachelor("BII")
    s.add_lecture("BII", "interface")
    s.add_lecture("BII", "électronique")

    # Créer deux étudiants.
    s.add_student("Rudy")
    s.add_student("Ali")

    # Créer l'inscription de chaque étudiant à deux cours.
    # Rudy : AL, BD
    # Ali : BD, ST
    s.register("Rudy", "BIG", "algorithmique")
    s.register("Rudy", "BIG", "database")
    s.register("Rudy", "BII", "électronique")
    s.register("Rudy", "BIG", "statistiques")
    s.register("Ali", "BIG", "database")
    s.register("Ali", "BIG", "statistiques")

    # Imprimer l'état des inscriptions
    print(s, "--------------------------")
    
    # Terminer le cours Algorithmique.
    s.del_lecture("BIG", "algorithmique")

    # Désinscrire l'étudiant Rudy du cours "database"
    s.unregister("Rudy", "BIG", "database")

    # Désinscrire Ali de l'école
    s.del_student("Ali")

    # Ajouter l'étudiant Youssef, inscrit à tous les cours
    s.add_student("Youssef")
    s.register("Youssef", "BIG", "database")
    s.register("Youssef", "BII", "électronique")
    s.register("Youssef", "BIG", "statistiques")
    s.register("Youssef", "BII", "interface")

    # Imprimer l'état des inscriptions.
    print(s, "--------------------------")

