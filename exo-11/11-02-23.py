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



class Segment:
    """
    Définissez une classe Segment
    ▪ Un segment est défini par deux points.
    ▪Méthodes
    ▪ longueur_pythagore() retourne la longueur pythagorienne du segment
    ▪ = √(𝑥𝑇 − 𝑥𝑆)² + (𝑦𝑇 − 𝑦𝑆)²
    ▪ longueur_manhattan() retourne la longueur manhattanienne du segment
    ▪ = | xT – xS | + | yT – yS |
    """
    def __init__(self, p1, p2 ):
        self.p1 = p1
        self.p2 = p2
        self.typeDistance = "manhattan"

    def __str__(self):
        return f"segment défini par {self.p1} et {self.p2}"

    def setDistance(self, v):
        # ajouter une validation ...
        self.typeDistance = v

    def longueur_manhattan(self):
        d = abs( self.p1.x - self.p2.x ) + abs( self.p1.y - self.p2.y )
        return d

    def longueur_pythagore(self):
        d = math.sqrt( (self.p1.x - self.p2.x )**2 + ( self.p1.y - self.p2.y)**2 )
        return d

    def distance(self):
        match self.typeDistance :
            case "manhattan" :
                return self.longueur_manhattan()
            case "pythagore" :
                return self.longueur_pythagore()
            case _ :
                return "erreur .... "


if __name__ == "__main__":
    # on crée un point a
    a = Point( 2, 3 )
    print(a)
    print(f"{a.distance():.2f}")

    # on crée un point b
    b = Point( 3, 4 )
    print(b)
    print(f"{b.distance():.2f}")

    seg = Segment( a, b )
    print(seg)
    # print(seg.longueur_manhattan())
    # print(seg.longueur_pythagore())

    seg.setDistance("manhattan")
    print(seg.distance())
    seg.setDistance("pythagore")
    print(seg.distance())
    seg.setDistance("brol")
    print(seg.distance())
