# Définissez une classe Point
# Un point est représenté par son abscisse et son ordonnée
# Constructeur : coordonnées (0, 0) par défaut
# Méthode .distance() : calcule et renvoie la distance du point avec l’origine (0, 0)
# import math
from math import *

class Point :
    def __init__(self, x=0, y=0 ):
        self.classname = "Classe Point"
        self.modify(x,y)

    def modify(self, x=0, y=0 ):
        self.__x = x
        self.__y = y
        self.d = -1

    def distance(self):
        if self.d < 0 :
            self.d = sqrt( self.__x**2 + self.__y**2 )
            print("calcul")
        return self.d


if __name__ == "__main__":
    A = Point( 3, 6 )
    print(round(A.distance(),2))
    print(round(A.distance(),2))

    A.modify( 4, 5 )
    print(round(A.distance(),2))
    print(round(A.distance(),2))




