"""École, bacheliers, cours (Course) et étudiants -- version 6.

Choix pédagogique conservé : tous les attributs sont publics, afin d'alléger
l'écriture. Mettre ces attributs privés serait l'étape suivante.

Règles de conception
--------------------
- Chaque classe ne manipule DIRECTEMENT que les objets de la classe qu'elle gère :
      HigherSchool  ->  Bachelor et Student
      Bachelor      ->  Course
      Course        ->  Student   (association à sens unique)
  Pour atteindre un objet situé plus bas, on passe son NOM au niveau intermédiaire.

- COMPOSITION = propriété = arbre de références fortes :
      HigherSchool -> Bachelor -> Course
  Supprimer un objet, c'est le retirer de son propriétaire (un simple `del`).
  Son __del__ fait alors le nettoyage :
      HigherSchool.__del__ : détruit ses bacheliers et ses étudiants
      Bachelor.__del__     : détruit ses cours
      Course.__del__       : désinscrit ses étudiants
  (la liste des inscrits est DANS le cours : quand le cours disparaît, ses
  inscriptions disparaissent avec lui)

- Association Course -> Student : à sens unique. Le Student ne connaît pas ses cours,
  donc il n'y a aucune boucle de références et __del__ fonctionne sans weakref.

- Student n'a pas de __del__ : il est référencé par les cours auxquels il est inscrit,
  donc il ne disparaît pas tant qu'il y est inscrit. Renvoyer un étudiant se fait
  explicitement : HigherSchool.del_student le désinscrit de tous les cours.

- Limites de __del__ : le moment d'exécution n'est garanti que si plus aucune autre
  référence forte ne traîne (variable locale, liste, ...) ; une exception dans
  __del__ est ignorée (seulement affichée).
"""


class HigherSchool:
    # la classe "école" gère les bacheliers et les étudiants
    def __init__(self, name):
        self.name = name
        self.bachelor_d = {}   # nom -> Bachelor
        self.student_d = {}    # nom -> Student

    def __str__(self):
        out = "nom : " + self.name + "\n"
        out += "liste bacheliers:" + "\n"
        for bac_o in self.bachelor_d.values():
            out += "    " + str(bac_o) + "\n"
        out += "liste étudiants:" + "\n"
        for stud_o in self.student_d.values():
            # les cours de l'étudiant sont demandés aux bacheliers
            course_names = []
            for bac_o in self.bachelor_d.values():
                course_names += bac_o.course_names_of(stud_o)
            out += "    " + str(stud_o) + " : " + ", ".join(course_names) + "\n"
        return out

    def __del__(self):
        # l'école disparaît : ses bacheliers et ses étudiants disparaissent
        self.bachelor_d.clear()
        self.student_d.clear()

    def add_bachelor(self, bac_name):
        # ajouter le bachelier au dictionnaire (sans écraser un bachelier existant)
        if bac_name in self.bachelor_d:
            raise ValueError(f"bachelier déjà existant : {bac_name}")
        self.bachelor_d[bac_name] = Bachelor(bac_name)

    def del_bachelor(self, bac_name):
        # le bachelier n'est plus référencé : Bachelor.__del__ fait le reste
        del self.bachelor_d[bac_name]

    def add_course(self, bach_n, course_n):
        # l'école ne touche pas aux cours : elle délègue au bachelier
        self.bachelor_d[bach_n].add_course(course_n)

    def del_course(self, bach_n, course_n):
        self.bachelor_d[bach_n].del_course(course_n)

    def add_student(self, stud_n):
        # inscrire l'étudiant à l'école (sans écraser un étudiant existant)
        if stud_n in self.student_d:
            raise ValueError(f"étudiant déjà existant : {stud_n}")
        self.student_d[stud_n] = Student(stud_n)

    def del_student(self, stud_n):
        # retirer l'étudiant de l'école...
        stud_o = self.student_d.pop(stud_n)
        # ... et le désinscrire de tous les cours (les cours le référencent encore)
        for bac_o in self.bachelor_d.values():
            bac_o.unregister_all(stud_o)

    def register(self, stud_n, bach_n, course_n):
        # inscrire l'étudiant au cours du bachelier
        self.bachelor_d[bach_n].register(self.student_d[stud_n], course_n)

    def unregister(self, stud_n, bach_n, course_n):
        # désinscrire l'étudiant du cours du bachelier
        self.bachelor_d[bach_n].unregister(self.student_d[stud_n], course_n)

    def register_all(self, stud_n):
        # inscrire l'étudiant à tous les cours de tous les bacheliers
        stud_o = self.student_d[stud_n]
        for bac_o in self.bachelor_d.values():
            bac_o.register_all(stud_o)


class Bachelor:
    """ la classe "bachelier" gère les cours
    """
    def __init__(self, name):
        self.name = name
        self.course_d = {}     # nom -> Course

    def __str__(self):
        out = "bachelier : " + self.name + "\n"
        for course_o in self.course_d.values():
            out += "        " + str(course_o)
        return out

    def __del__(self):
        # le bachelier disparaît : ses cours disparaissent (chacun fait son nettoyage)
        self.course_d.clear()

    def add_course(self, course_n):
        if course_n in self.course_d:
            raise ValueError(f"cours déjà existant : {course_n}")
        self.course_d[course_n] = Course(course_n)

    def del_course(self, course_n):
        # le cours n'est plus référencé : Course.__del__ désinscrit ses étudiants
        del self.course_d[course_n]

    def register(self, stud_o, course_n):
        self.course_d[course_n].register(stud_o)

    def unregister(self, stud_o, course_n):
        self.course_d[course_n].unregister(stud_o)

    def register_all(self, stud_o):
        # inscrire l'étudiant à tous les cours du bachelier
        for course_o in self.course_d.values():
            course_o.register(stud_o)

    def unregister_all(self, stud_o):
        # désinscrire l'étudiant de tous les cours du bachelier
        for course_o in self.course_d.values():
            course_o.unregister(stud_o)

    def course_names_of(self, stud_o):
        # noms des cours de ce bachelier auxquels l'étudiant est inscrit
        return [course_o.name for course_o in self.course_d.values()
                if course_o.has_student(stud_o)]


class Course:
    """ la classe "cours" gère les inscriptions des étudiants
    """
    def __init__(self, name):
        self.name = name
        self.student_d = {}    # nom -> Student

    def __str__(self):
        out = "cours : " + self.name + "\n"
        for stud_o in self.student_d.values():
            out += "          " + str(stud_o) + "\n"
        return out

    def __del__(self):
        # le cours disparaît : ses étudiants sont désinscrits
        self.student_d.clear()

    def register(self, stud_o):
        self.student_d[stud_o.name] = stud_o

    def unregister(self, stud_o):
        # s'il n'était pas inscrit, il ne se passe rien
        self.student_d.pop(stud_o.name, None)

    def has_student(self, stud_o):
        return self.student_d.get(stud_o.name) is stud_o


class Student:
    """ la classe "étudiant" ne connaît que son nom
    """
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "student : " + self.name

    def __repr__(self):
        # représentation destinée au développeur
        return f"Student({self.name!r})"


def scenario():
    # Créer une école "IFC".
    s = HigherSchool("IFC")

    # Créer un bachelier "BIG" avec trois cours:
    s.add_bachelor("BIG")
    s.add_course("BIG", "statistiques")
    s.add_course("BIG", "algorithmique")
    s.add_course("BIG", "database")

    # Pour le fun, créer un bachelier "BII" avec deux cours:
    s.add_bachelor("BII")
    s.add_course("BII", "interface")
    s.add_course("BII", "électronique")

    # Créer deux étudiants.
    s.add_student("Rudy")
    s.add_student("Ali")

    # Créer l'inscription de chaque étudiant à deux cours.
    # Rudy : algorithmique, database
    # Ali : database, statistiques
    s.register("Rudy", "BIG", "algorithmique")
    s.register("Rudy", "BIG", "database")
    s.register("Ali", "BIG", "database")
    s.register("Ali", "BIG", "statistiques")

    # Imprimer l'état des inscriptions
    print(s, "--------------------------")

    # Terminer le cours Algorithmique.
    s.del_course("BIG", "algorithmique")

    # Désinscrire l'étudiant Rudy du cours "database"
    s.unregister("Rudy", "BIG", "database")

    # Désinscrire Ali de l'école
    s.del_student("Ali")

    # Ajouter l'étudiant Youssef, inscrit à tous les cours (de tous les bacheliers)
    s.add_student("Youssef")
    s.register_all("Youssef")

    # Imprimer l'état des inscriptions.
    print(s, "--------------------------")


def check_destructions():
    """Vérifie que les __del__ font leur travail (test "boîte blanche").

    Aucune variable locale ne garde une référence à un cours ou à un bachelier :
    sinon l'objet ne serait pas détruit par le `del`.
    """
    detruits = []                                  # espion : cours réellement détruits
    del_origine = Course.__del__
    Course.__del__ = lambda self: (detruits.append(self.name), del_origine(self))
    try:
        s = HigherSchool("IFC")
        for bac in ("BIG", "BII"):
            s.add_bachelor(bac)
            s.add_course(bac, "database")          # deux cours homonymes
        s.add_student("Rudy")
        s.add_student("Ali")
        for stud in ("Rudy", "Ali"):
            s.register(stud, "BIG", "database")
            s.register(stud, "BII", "database")

        def cours_de(stud_n, bac_n):
            return s.bachelor_d[bac_n].course_names_of(s.student_d[stud_n])

        assert cours_de("Rudy", "BIG") == cours_de("Rudy", "BII") == ["database"]

        # Course.__del__ : le cours BIG/database est détruit, BII/database est intact
        s.del_course("BIG", "database")
        assert detruits == ["database"]
        assert cours_de("Rudy", "BII") == ["database"]

        # del_student : Rudy est désinscrit des cours restants
        s.del_student("Rudy")
        assert list(s.bachelor_d["BII"].course_d["database"].student_d) == ["Ali"]

        # Bachelor.__del__ : BII disparaît, son cours aussi
        s.del_bachelor("BII")
        assert detruits == ["database", "database"]

        # refus de l'écrasement silencieux
        for appel in (lambda: s.add_student("Ali"), lambda: s.add_bachelor("BIG")):
            try:
                appel()
            except ValueError:
                pass
            else:
                raise AssertionError("l'écrasement silencieux devrait être refusé")
    finally:
        Course.__del__ = del_origine
    print("check_destructions : OK")


if __name__ == "__main__":
    scenario()
    check_destructions()
