import random
import math
from S1_Q35_output import TextOutput1
from S1_Q35_output import GraphicalOutput1


class PointAggregation1:
    """
    Cette classe créée, groupe et gère tous les points (classe Point)
    """

    def __init__(self, out, nb_points, nb_iter):
        self.__point_d = {}
        self.__output = out
        for j in range(nb_points):
            p = Point1(random.randint(0, 10), random.randint(0, 10))
            self.__point_d[p] = ""
        self.__output.set_point_d(self.__point_d)
        self.__nb_iter = nb_iter

    def __repr__(self):
        return repr(self.__output)

    def forward(self):
        for p in self.__point_d.keys():
            p.forward()

    def go(self):
        # on affiche les points
        print(repr(self))

        # on fait bouger les points et on réaffiche
        for i in range(self.__nb_iter):
            point_a.forward()
            print(repr(self))


class Point1:
    """
    classe Point : Un point est représenté par son abscisse x, son ordonnée y et sa couleur aléatoire
    """

    __COLORS = ['red', 'green', 'blue', 'yellow', 'orange', 'black', 'white', 'magenta', 'cyan']

    def __init__(self, x=0, y=0, color=None):
        """
        Constructeur : coordonnées (0, 0) par défaut
        Couleur par défaut : aléatoire
        """
        self.__x = x
        self.__y = y
        self.__distance = -1  # la distance sera calculée "on the fly"
        if color is None:
            self.__color = random.sample(self.__COLORS, 1)[0]
        else:
            self.__color = color

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def color(self):
        return self.__color

    @property
    def distance(self):
        """
        Méthode "distance" : calcule et renvoie la distance du point avec l’origine (0, 0)
        La distance est calculée seulement quand on en a besoin, et alors une seule fois.
        """
        if self.__distance < 0:
            self.__distance = math.sqrt(self.__x ** 2 + self.__y ** 2)
        return self.__distance

    def forward(self):
        """
        on fait avancer le point de "2" (càd 20 pixels) vers la droite
        la distance calculée n'étant plus bonne, on la réinitialise à -1
        """
        self.__x += 2
        self.__distance = -1


if __name__ == '__main__':
    o = int(input(" Output ? 1 pour texte, 2 pour graphique "))
    match o:
        case 2:
            output = GraphicalOutput1()
        case _:
            output = TextOutput1()

    # on crée les points (random)
    point_a = PointAggregation1(output, 10, 10)  # on crée 5 points dans le PointAggregation
    point_a.go()

