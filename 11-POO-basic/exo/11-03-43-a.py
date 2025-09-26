import random

class Jeu:
    def __init__(self):
        self.nb_des = 3
        self.des_l = []
        for i in range(self.nb_des):
            self.des_l.append(De())

    def lancer(self):
        val_l = [] # liste des valeurs affichées sur chaque dé
        for chaque_de in self.des_l:
            face = chaque_de.lancer()
            val_l.append( face )
        return val_l


class De:
    def __init__(self, nb_faces=6):
        self.nb_faces = nb_faces

    def lancer(self):
        return random.randint(1,self.nb_faces)


# Instancier un jeu de 3 dés
# afficher le résultat d’un lancer
j1 = Jeu()
for i in range(20):
    print(j1.lancer())
