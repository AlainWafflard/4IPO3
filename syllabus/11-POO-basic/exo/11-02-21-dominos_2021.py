class Domino:
    """
    Le constructeur initialisera les valeurs des points présents
    sur les deux faces A et B du domino (valeurs par défaut = 0).
    Méthodes
    affiche_points() : affiche les points présents sur les deux faces.
    somme_valeur() : renvoie la somme des points présents sur les 2 faces.
    """
    print_config = "long"

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.print_config=="long":
            return "face A : {} / face B : {}".format(self.a,self.b)
        elif self.print_config=="short":
            return "{}-{}".format(self.a, self.b)

    def somme_valeur(self):
        return self.a + self.b


#MAIN
d1 = Domino(2,6)
d2 = Domino(4,3)
print(d1) # face A : 2 / face B : 6
print(d2) # face A : 4 / face B : 3
print( "total des points :", d1.somme_valeur() + d2.somme_valeur() )  #15

l_dominos = []
for i in range(7):
    mon_domino = Domino(6, i)
    mon_domino.print_config="short"
    print(mon_domino)
    mon_domino.print_config="long"
    l_dominos.append(mon_domino)

print()

for i in range(7):
    print(l_dominos[i])

