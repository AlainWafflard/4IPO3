import math
# Définissez une classe Point
# Un point est représenté par son abscisse et son ordonnée
# Constructeur : coordonnées (0, 0) par défaut
# Méthode distance() :
# calcule et renvoie la distance du point avec l’origine
from math import ceil


class Point:
    def __init__(self, abs, ord):
        self.abs = abs
        self.ord = ord

    def __str__(self):
        return "POINT({},{})".format( self.abs, self.ord)

    def distance(self):
        dist = abs(self.abs) + abs(self.ord)
        return dist


class Segment:
    def __init__(self, pa, pb ):
        self.pa = pa
        self.pb = pb
        self.dist_manhattan = abs(self.pa.abs - self.pb.abs) + abs(self.pa.ord - self.pb.ord)
        self.dist_pythagore = math.sqrt( (self.pa.abs - self.pb.abs)**2 + (self.pa.ord - self.pb.ord)**2 )
        self.set_mode("manhattan")

    def set_mode(self,nouveau_mode):
        if nouveau_mode in ( "manhattan", "pythagore" ):
            self.mode = nouveau_mode

    def longueur(self):
        if self.mode == "manhattan":
            return self.dist_manhattan
        elif self.mode == "pythagore":
            return self.dist_pythagore


class Cercle:
    def __init__(self, abs, ord, rayon ):
        self.abs = abs
        self.ord = ord
        self.rayon = rayon

    def __str__(self):
        return "CERCLE({},{},{})".format( self.abs, self.ord, self.rayon)

    def getPerimeter(self):
        p = self.rayon * 2 * math.pi
        return round(p, 2)

    def getSurface(self):
        s = self.rayon * self.rayon * math.pi
        return round(s, 2)

    def isInside(self, point):
        # seg = Segment( point, Point( self.abs, self.ord) )
        # dist = Segment( point, Point( self.abs, self.ord) ).longueur()
        return Segment( point, Point( self.abs, self.ord) ).longueur() <= self.rayon


if __name__ == "__main__":
    # Donner l'abscisse du centre: 1
    # Donner l'ordonné du centre: 2
    # Donner le rayon: 3
    cercle_o = Cercle( 1, 2, 3 )
    print(cercle_o)  # CERCLE(1,2,3)
    print(cercle_o.getPerimeter())         # Le périmétre est : 18,85
    print(cercle_o.getSurface())           # La surface est : 28,27

    # Donner un point: # X:2 # Y:3
    p = Point( 2, 3 )
    print(p, cercle_o.isInside(p) )        #  POINT(2,3) ; le point appartient au cercle

    # Donner un point: # X:2 # Y:10
    p = Point( 2, 10 )
    print(p, cercle_o.isInside(p) )        #  POINT(2,10) ; point hors cercle

