from higherschool import HigherSchool
from people import People

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

    # bachelier BII
    hs.add_bachelor("BII")
    hs.add_course_to_bachelor("BII", "Réseaux")
    hs.add_course_to_bachelor("BII", "Connectique")

    # print(hs)
    # exit()

    # ▪ Créer deux étudiants : Rudy et Ali.
    people = People()
    people.register_student( "Rudy" )
    people.register_student( "Ali" )
    people.setHigherSchool(hs)

    # ▪ Créer l'inscription de chaque étudiant à deux cours.
    # ▪ Rudy : algorithmique, database
    people.register_student_to_course( "Rudy", "BIG", "Algorithmique")
    people.register_student_to_course( "Rudy", "BIG", "Database")
    people.register_student_to_course( "Bernard", "BIG", "Database")

    # ▪ Ali : database, statistiques
    people.register_student_to_course( "Ali", "BIG", "Database")
    people.register_student_to_course( "Ali", "BIG", "Statistiques")
    people.register_student_to_course( "Ali", "BII", "Connectique")
    people.register_student_to_course( "Ali", "BII", "Réseaux")

    # ▪ Imprimer l'état des inscriptions dans les bacheliers
    print(hs)
    print(repr(hs))

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