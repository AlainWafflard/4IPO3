import random

class Jeu:
    def __init__(self):
        self.nb_des = 3
        self.des_l = []
        for i in range(self.nb_des):
            self.des_l.append(De())

    @property
    def score(self):
        score = 0
        for chaque_de in self.des_l:
            score += chaque_de.score
        return score

    def __gt__(self, other):
        """ comparer deux jeux """
        return self.score > other.score

    def __ge__(self, other):
        """ comparer deux jeux """
        return self.score >= other.score

    def __str__(self):
        out = ""
        for chaque_de in self.des_l:
            out += str(chaque_de.score)
        return out

    def lancer(self):
        # val_l = [] # liste des valeurs affichées sur chaque dé
        for chaque_de in self.des_l:
            chaque_de.lancer()
            # val_l.append( face )
        # return val_l@


class De:
    def __init__(self, nb_faces=6):
        self.nb_faces = nb_faces
        self.__score = 0

    @property
    def nb_faces(self):
        return self.__nb_faces

    @nb_faces.setter
    def nb_faces(self, val):
        if val < 4 : val = 4
        self.__nb_faces = val

    @property
    def score(self):
        return self.__score

    # @score.setter
    # def score(self, val):
    #     self.__score = val

    def lancer(self):
        self.__score = random.randint(1,self.nb_faces)


# Instancier un jeu de 3 dés
# afficher le résultat d’un lancer
j1 = Jeu()
j1.lancer()
print("j1=", j1, j1.score)

# j2 = Jeu()
# j2.lancer()
# print(j2)
#
# print( j1 > j2 )
# print( j1 >= j2 )

# Soit deux jeux, j1 et j2
# j1 est lancé (et conservé)
# j2 est lancé de manière itérative
# L’itération s’arrête quand j2 > j1
j2 = Jeu()
while True:
    j2.lancer()
    print("j2=", j2, j2.score)
    if( j2 >= j1 ): break
print("done")
