import math

class Point:
    """ Un point est représenté par son abscisse et son ordonnée.
    """
    
    def __init__(self, x=0, y=0 ):
        """ Constructeur : coordonnées (0, 0) par défaut
        """
        self.x = x
        self.y = y
        
    def distance(self):
        """ Méthode : distance du point avec l’origine (0, 0)
        """
        d = math.sqrt( self.x*self.x + self.y*self.y )
        return d

P1 = Point(4,5)
print(P1.distance())

P2 = Point()
print(P2.distance())

