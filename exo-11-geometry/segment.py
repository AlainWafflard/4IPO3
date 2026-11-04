import math

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
    typeAuthDistance_l = [ "manhattan", "pythagore" ]

    def __init__(self, p1, p2 ):
        self.p1 = p1
        self.p2 = p2
        self.setDistance("manhattan")
        self.PythagoreDistanceCache = -1

    def __str__(self):
        return f"segment défini par {self.p1} et {self.p2}"

    def setDistance(self, distanceType):
        # tests de validation
        if distanceType not in self.typeAuthDistance_l :
            # scenario alternatif : mauvais type de distance
            print("erreur ....")
            return

        # scenario nominal
        self.typeDistance = distanceType

    def longueur_manhattan(self):
        d = abs( self.p1.x - self.p2.x ) + abs( self.p1.y - self.p2.y )
        return d

    def longueur_pythagore(self):
        if self.PythagoreDistanceCache < 0 :
            print("create cache value")
            self.PythagoreDistanceCache = math.sqrt( (self.p1.x - self.p2.x )**2 + ( self.p1.y - self.p2.y)**2 )
        return self.PythagoreDistanceCache

    def distance(self):
        match self.typeDistance :
            case "manhattan" :
                return self.longueur_manhattan()
            case "pythagore" :
                return self.longueur_pythagore()
            case _ :
                return "erreur .... "

    def pente(self):
        """ retourne l'angle du segment, en degrés """
        dy = self.p2.y - self.p1.y
        dx = self.p2.x - self.p1.x
        pente = math.atan(dy/dx) * (180/math.pi)
        return pente
