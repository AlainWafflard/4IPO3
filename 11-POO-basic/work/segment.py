import point
from math import *

class Segment:
    def __init__(self, a:point.Point, b:point.Point ):
        self.a = a
        self.b = b
        self.distanceManhattanEnabled = False

    def longueur_pythagore(self):
        lp = sqrt( (self.a.__x - self.b.__x)**2 + (self.a.__y - self.b.__y)**2 )
        return lp

    def longueur_Manhattan(self):
        lm = abs( self.a.__x - self.b.__x) + abs(self.a.__y - self.b.__y)
        return lm

    def longueur(self):
        if self.distanceManhattanEnabled:
            return self.longueur_Manhattan()
        else:
            return self.longueur_pythagore()


if __name__ == "__main__":
    P1 = point.Point(3,4)
    P2 = point.Point(6,0)
    Mon_segment = Segment(P1,P2)
    print(Mon_segment.longueur_pythagore())
    # // 5
    print(Mon_segment.longueur_Manhattan())
    # // 7

    print(Mon_segment.longueur())
    Mon_segment.distanceManhattanEnabled = True
    print(Mon_segment.longueur())

