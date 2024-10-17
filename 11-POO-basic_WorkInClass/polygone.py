# Définissez une classe Polygone
# modélisant un polygone  quelconque à partir de N points
# avec une méthode perimeter()
# en vous basant sur les classes Point et Segment
import point
import segment
import turtle


class Polygone:

    def __init__(self, point_l ):
        self.point_l = point_l
        self.turtle = turtle.Turtle()

    def perimeter(self):
        long = len(self.point_l)
        perim = 0
        for i in range(long):
            i_next = i + 1
            if i_next >= long : i_next = 0
            seg = segment.Segment(  self.point_l[i], self.point_l[i_next]  )
            perim += seg.longueur("Pythagore")
        return perim

    def draw(self):
        """ affichage grâce à la tortue """
        pass


if __name__ == "__main__":
    my_points = [
        point.Point(0, 0),
        point.Point(10, 0),
        point.Point(15, 5),
        point.Point(0, 5)
    ]
    pol = Polygone( my_points )
    print(pol.perimeter())

    pol.draw()    # dessiner à la Tortue

