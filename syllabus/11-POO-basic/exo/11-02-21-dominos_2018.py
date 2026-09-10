# Définissez une classe Domino() pour instancier des objets simulant 
# les pièces d'un jeu de dominos. 
# Le constructeur initialisera les valeurs des points présents sur les
# deux faces A et B du domino (valeurs par défaut = 0).
# Méthodes
# Affiche_points() : affiche les points présents sur les deux faces.
# Somme_valeur() : renvoie la somme des points présents sur les 2 faces.

class Domino :
    
    def __init__(self, a, b ):
        self.a = a
        self.b = b

    def somme_valeur(self):
        return self.a + self.b

    # première implantation de l'impression :
    # par une méthode classique "affiche_points"
    def affiche_points(self):
        print("(affiche_points) face A : {} / face B : {}".format( self.a, self.b ))
        return

    # deuxième implantation de l'impression :
    # par la méthode magique "__str__"
    def __str__(self):
        return "(__str__) face A : {} / face B : {}".format( self.a, self.b )

######################################################################

d1 = Domino(2,6)
d2 = Domino(4,3)

d1.affiche_points() # print : "face A : 2 / face B : 6"
d2.affiche_points() # print : "face A : 4 / face B : 3"
print( "total des points :", d1.somme_valeur() + d2.somme_valeur() ) # print : "15"

liste_dominos = [ Domino(6, i) for i in range(7) ]
for o in liste_dominos:
    # deux manières : par "print(o)" et méthode magique __str__,
    # ou par une méthode classique "affiche_points"
    # (une des deux suffit)
    print(o)
    o.affiche_points()

