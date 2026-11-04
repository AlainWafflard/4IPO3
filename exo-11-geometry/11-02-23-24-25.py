from point import *
from segment import *
from cercle import *


if __name__ == "__main__":
    # on crée un point a
    a = Point( 2, 3 )
    print(a)
    print(f"{a.distance():.2f}")

    # on crée un point b
    b = Point( 3, 4 )
    print(b)
    print(f"{b.distance():.2f}")

    # on crée un point c
    c = Point( 5, 4 )
    print(c)
    print(f"{c.distance():.2f}")

    # on crée un point d
    d = Point( 4, 3 )
    print(d)
    print(f"{d.distance():.2f}")

    seg = Segment( a, b )
    print(seg)
    # print(seg.longueur_manhattan())
    # print(seg.longueur_pythagore())

    # seg.setDistance("manhattan")
    # print(seg.distance())
    seg.setDistance("pythagore")
    print(seg.distance())
    # seg.setDistance("brol")
    print(seg.distance())
    print(seg.distance())

    seg2 = Segment( a, c )
    print(seg2)

    print("pente :", seg.pente() )
    print("pente :", seg2.pente() )

    cercle = Cercle( a, 2 )
    print(cercle.isInside(b))  # True
    print(cercle.isInside(c))  # False
    print(cercle.isInside(d))  # True, cas limite
