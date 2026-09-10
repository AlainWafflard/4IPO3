import random

class Jeu:
    def __init__(self):
        self.nb_des = 3
        self.des_l = []
        for i in range(self.nb_des):
            self.des_l.append(De())

    def __str__(self):
        out = ""
        for chaque_de in self.des_l:
            out += str(chaque_de.score)
        return out

    def lancer(self):
        for chaque_de in self.des_l:
            chaque_de.lancer()


class De:
    def __init__(self, nb_faces=6):
        self.nb_faces = nb_faces

    def lancer(self):
        self.score = random.randint(1,self.nb_faces)


# Instancier un jeu de 3 dés
# afficher le résultat d’un lancer
j1 = Jeu()
for i in range(20):
    j1.lancer()
    print(j1)
