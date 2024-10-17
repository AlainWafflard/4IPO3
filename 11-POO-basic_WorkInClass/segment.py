import math
# import point
from point import Point

# Définissez une classe Segment
# • Un segment est défini par deux
# points.
# • Méthodes
# • longueur_pythagore()
# • retourne la longueur
# pythagorienne du segment
# • = √(𝑥𝑇 − 𝑥𝑆)² + (𝑦𝑇 − 𝑦𝑆)²
# • longueur_manhattan()
# • retourne la longueur
# manhattanienne du segment
# • = | xT – xS | + | yT – yS |

class Segment:
    def __init__(self, pa, pb ):
        self.pa = pa
        self.pb = pb

    def longueur_Pythagore(self):
        dist = math.sqrt( (self.pa.x - self.pb.x)**2
                          + (self.pa.y - self.pb.y)**2 )
        return dist

    def longueur_Manhattan(self):
        dist = (abs( self.pa.x - self.pb.x )
                + abs( self.pa.y -self.pb.y ))
        return dist

    def longueur(self, type="Manhattan"):
        match type:
            case "Manhattan":
                return self.longueur_Manhattan()
            case "Pythagore":
                return self.longueur_Pythagore()
            case _ :
                return self.longueur_Manhattan()


if __name__ == "__main__":
    p1 = Point(3,4)
    p2 = Point(6,0)
    mon_segment = Segment(p1,p2)
    print(mon_segment.longueur_Pythagore())
    # // 5
    print(mon_segment.longueur_Manhattan())
    # // 7

    mon_segment2 = Segment( Point(1,2), Point(5,6) )
    print(mon_segment2.longueur_Manhattan())

    print(mon_segment.longueur())
    print(mon_segment.longueur("Pythagore"))
    print(mon_segment.longueur("brol"))

