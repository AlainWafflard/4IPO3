import math
from point import Point
from segment import Segment

# Un cercle est défini par :
# • Un point C qui représente son centre
# • Son rayon r
# • Méthodes de la classe Cercle :
# • Constructeur : On crée un cercle en précisant son centre C
# et son rayon r.
# • getPerimetre(): retourne le périmètre du cercle.
# • getSurface() : retourne la surface du cercle.
# • isInside(Point p) : retourne True si p appartient
# au cercle, càd si la longueur du segment(p , r) est
# inférieure au rayon.
# • __str__() : retourne chaîne de type "CERCLE(x,y,R)"

class Cercle:
    def __init__(self, center, radius ):
        self.center = center
        self.radius = radius

    def __str__(self):
        return f"CERCLE({self.center.x},{self.center.y},{self.radius})"

    def getPerimeter(self):
        return 2 * math.pi * self.radius

    def getSurface(self):
        return math.pi * self.radius**2

    def isInside(self, other_point ):
        seg = Segment( self.center, other_point )
        dist = seg.longueur("Pythagore")
        return dist <= self.radius


if __name__ == "__main__":
    c = Cercle( Point(1,1), 3 )
    print(c.getPerimeter())
    print(c.getSurface())
    print(c.isInside( Point(10,0) ))
    print(c.isInside( Point(0,0) ))

