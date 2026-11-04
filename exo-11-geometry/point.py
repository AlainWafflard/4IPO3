import math


class Point:
    """
    Définissez une classe Point
    ▪ Un point est représenté par son abscisse et son ordonnée
    ▪ Constructeur : coordonnées (0, 0) par défaut
    ▪ Méthode « distance » : calcule et renvoie la distance du point avec l’origine (0, 0)
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f" point({self.x}, {self.y})"

    def distance(self):
        d = math.sqrt( self.x**2 + self.y**2 )
        return d
