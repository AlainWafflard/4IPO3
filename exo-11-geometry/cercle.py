from segment import *

class Cercle :

    def __init__(self, c, r ):
        self.c = c
        self.r = r

    def isInside(self, p ):
        seg = Segment( self.c, p )
        seg.setDistance("pythagore")
        d = seg.distance()
        return d <= self.r

