# Définissez une classe Triangle
# modélisant un triangle quelconque à partir de trois points
# avec une méthode perimeter()
# en vous basant sur les classes Point et Segment

import point
import segment


class Triangle:

    def __init__(self, pa, pb, pc ):
        self.pa = pa
        self.pb = pb
        self.pc = pc

    def perimeter(self):
        sab = segment.Segment(self.pa, self.pb)
        sac = segment.Segment(self.pa, self.pc)
        sbc = segment.Segment(self.pc, self.pb)
        perim = sab.longueur("Pythagore") + sac.longueur("Pythagore") + sbc.longueur("Pythagore")
        return perim


if __name__ == "__main__":
    pa = point.Point(0,0)
    pb = point.Point(10,0)
    pc = point.Point( 0,5)
    t = Triangle( pa, pb, pc )
    print(t.perimeter())

