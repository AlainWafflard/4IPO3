# Ecrivez le POO d'une école
# ▪ L'école organise des bacheliers, ceux-ci
# constitués d'un ensemble de cours.
# ▪ L'école organise un cours dans un bachelier
# en y inscrivant les étudiants.
# ▪ Un étudiant peut se désinscrire d'un cours.
# ▪ L'école peut renvoyer un étudiant.
# ▪ L'écoel peut supprimer un cours.
# ▪ Cf schéma, slide suivant

from school import School

if __name__ == "__main__":
    # ▪ Scénario d'utilisation
    # ▪ Créer une école "IFC".
    school_o = School("IFC")
    # ▪ Créer un bachelier "BIG" avec trois cours:
    school_o.append_bachelor("BIG")
    school_o.append_bachelor("BII")
    # ▪ Statistiques
    school_o.append_course("BIG", "statistiques")
    # ▪ Algorithmique
    school_o.append_course("BIG", "algorithmique")
    # ▪ Database
    school_o.append_course("BIG", "database")
    school_o.append_course("BII", "électronique")
    school_o.append_course("BII", "statistiques")

    # ▪ Créer deux étudiants : Rudy et Ali.
    school_o.append_student("Rudy")
    school_o.append_student("Ali")
    # ▪ Créer l'inscription de chaque étudiant à deux cours.
    # ▪ Rudy : algorithmique, database
    school_o.subscribe_student("Rudy", "BIG", [ "algorithmique", "database" ])
    school_o.subscribe_student("Rudy", "BII", [ "statistiques" ])
    # ▪ Ali : database, statistiques
    school_o.subscribe_student("Ali",  "BIG", [ "database" ])
    school_o.subscribe_student("Ali",  "BII", [ "statistiques" ])

    # ▪ Imprimer l'état des inscriptions dans le
    print(school_o)

    # ▪ Supprimer le cours d'Algorithmique.
    school_o.delete_course("BIG", "algorithmique")
    print(school_o)

    # ▪ Désinscrire l'étudiant Rudy du cours de Database
    # ▪ Renvoyer l'étudiant Ali.
    # ▪ Ajouter l'étudiant Youssef, inscrit à tous les
    # cours.
    # ▪ Imprimer l'état des inscriptions.