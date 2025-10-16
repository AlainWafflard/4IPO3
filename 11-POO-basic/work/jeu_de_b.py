# import random
from random import randint

class Jeu :
    def __init__(self, nbDe, nbFace):
        self.nbDe = nbDe
        self.__nbFace = nbFace
        self.__de_l = []
        for i in range(self.nbDe):
            self.__de_l.append( De(self.__nbFace) )

    def __str__(self):
        out = ""
        for de in self.__de_l:
            out += repr(de) + ";"
            # out += str(de.value) + ";"
        return out

    @property
    def nbDe(self):
        return self.__nbDe

    @nbDe.setter
    def nbDe(self, val ):
        if not isinstance(val,int) or not val > 0 :
            # raise Exception("valeur ko")
            val = 3
        self.__nbDe = val

    def lancer(self):
        for de in self.__de_l:
            de.lancer()


class De :
    def __init__(self, nbFace):
        self.__nbFace = nbFace
        self.__value = None

    def __repr__(self):
        return f"{self.value}"

    @property
    def value(self):
        return self.__value

    def lancer(self):
        self.__value = randint(1, self.__nbFace)


if __name__ == "__main__" :
    jeu = Jeu(-3, 6)
    jeu.lancer()
    print(jeu)
    jeu.lancer()
    print(jeu)
    print(jeu)

