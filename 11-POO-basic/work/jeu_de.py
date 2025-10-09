
class Jeu :
    def __init__(self, nbDe, nbFace):
        self.nbDe = nbDe
        self.nbFace = nbFace
        self.de_l = []
        for i in range(nbDe):
            self.de_l.append( De(self.nbFace) )

    def __str__(self):
        return ""

    def lancer(self):
        pass


class De :
    def __init__(self, nbFace):
        self.nbFace = nbFace


if __name__ == "__main__" :
    jeu = Jeu(3, 6)
    jeu.lancer()
    print(jeu)

