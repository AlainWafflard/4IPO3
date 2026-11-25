from higherschool import HigherSchool

if __name__ == "__main__":

    # Scénario d'utilisation
    # ▪ Créer une école "IFC".
    hs = HigherSchool("IFC")

    # ▪ Créer un bachelier "BIG"
    hs.add_bachelor("BIG")

    # avec trois cours:
    # ▪ Statistiques
    hs.add_course_to_bachelor( "BIG", "Statistiques" )

    # ▪ Algorithmique
    hs.add_course_to_bachelor( "BIG", "Algorithmique" )

    # ▪ Database
    hs.add_course_to_bachelor( "BIG", "Database" )

    # ▪ Créer deux étudiants : Rudy et Ali.
    people = People()
    people.reg_student( "Rudy" )
    people.reg_student( "Ali" )
    people.connect(hs)

    # ▪ Créer l'inscription de chaque étudiant à deux cours.
    # ▪ Rudy : algorithmique, database
    people.reg_student_to_course( "Rudy", "BIG", "Algorithmique")
    people.reg_student_to_course( "Rudy", "BIG", "Database")

    # ▪ Ali : database, statistiques
    people.reg_student_to_course( "Ali", "BIG", "Database")
    people.reg_student_to_course( "Ali", "BIG", "Statistiques")

    # ▪ Imprimer l'état des inscriptions dans les bacheliers
    print(hs)

    # BIG
    # ▪ par cours
    # ▪ par étudiant
    # ▪ Supprimer le cours
    # d'Algorithmique.
    # ▪ Désinscrire l'étudiant Rudy du
    # cours de Database
    # ▪ Renvoyer l'étudiant Ali.
    # ▪ Ajouter l'étudiant Youssef,
    # inscrit à tous les cours.
    # ▪ Imprimer l'état des
    # inscriptions.