# Définissez une classe Point
# ▪ Un point est représenté par
# son abscisse et son ordonnée
# ▪ Constructeur : coordonnées
# (0, 0) par défaut
# ▪ Méthode « distance » :
# calcule et renvoie la distance
# du point avec l’origine (0, 0)

import math


class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f" point x={self.x} y={self.y}"

    def distance(self):
        d = math.sqrt( self.x**2 + self.y**2 )
        return d


if __name__ == "__main__":
    # on crée un point a
    a = Point( 2, 3 )
    print(a)
    print(f"{a.distance():.2f}")

    # on crée un point b
    b = Point( 3, 4 )
    print(b)
    print(f"{b.distance():.2f}")

