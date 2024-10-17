import math

# Définissez une classe Point
# • Un point est représenté par
# son abscisse et son ordonnée
# • Constructeur : coordonnées
# (0, 0) par défaut
# • Méthode « distance » :
# calcule et renvoie la distance
# du point avec l’origine (0, 0)

class Point:

    def __init__(self, x=0, y=0, z=0 ):
        self.x = x
        self.y = y
        self.z = z
        self.dist = -1

    def distance(self):
        if self.dist < 0:
            self.dist = math.sqrt( self.x**2 + self.y**2 )
        return self.dist


if __name__ == "__main__":
    a = Point( 3, 4, 1 )
    b = Point( z=7, x=1 )
    c = Point()
    print(a.distance())
    print(a.distance())

