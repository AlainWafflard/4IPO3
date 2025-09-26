import math

class Point:
    """ classe Point : Un point est représenté par son abscisse et son ordonnée """
    d = -1

    def __init__(self, x=0, y=0 ):
        """ Constructeur : coordonnées (0, 0) par défaut """
        self.x = x
        self.y = y
        # self.d = math.sqrt( self.x**2 + self.y**2 )

    def distance(self):
        """ Méthode "distance" : calcule et renvoie la distance du point avec l’origine (0, 0)
            La distance est calculée seulement quand on en a besoin, et alors une seule fois.
        """
        if self.d < 0  :
            print("calcul ...", end="  ")
            self.d = math.sqrt( self.x**2 + self.y**2 )
        return self.d


if __name__ == '__main__':
    p = Point( 1, 1 )
    print(p.d)
    print(p.distance())
    print(p.d)
    print(p.distance())

