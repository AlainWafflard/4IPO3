import tkinter
import math
import random
import time


# 3 modifications :
# - methode __repr__() OK
# - color => Point OK
# - print via classe "aggrégation de points"  OK

class TextOutput:
    """ Manages the textual output """

    def __init__(self):
        # self.__point_l = []  # liste des points à afficher
        self.__point_d = {}

    def __repr__(self):
        """
        on imprime les points en mode texte
        """
        out = ""
        for point in self.__point_d.keys():
            out += f"Point({point.x},{point.y}) ; dist = {point.distance:5.2f} ; color = {point.color}\n"
        return out

    # def append(self, point):
    #     self.__point_l.append(point)

    def set_point_d(self, point_d):
        self.__point_d = point_d


class GraphicalOutput:
    """ Manages the graphical output """

    def __init__(self):
        # Création du widget principal
        self.win = tkinter.Tk()
        self.win.title("POINT - graphical output")

        # création des widgets encastrés
        self.canvas = tkinter.Canvas(self.win, bg='dark grey', height=400, width=800)
        self.canvas.pack(side=tkinter.LEFT)
        # tkinter.Button(self.win, text='Quitter', command=self.win.destroy).pack(side=tkinter.BOTTOM)

        # dictionnaire : point object => shape object
        # vide à la construction
        self.__point_d = {}

    def __repr__(self):
        """
        on imprime les points en mode graphique (tkinter/canvas)
        on place le shape du point à sa (nouvelle) place,
        le point est représenté par un carré de 10 pixels de côté
        """
        for point, shape in self.__point_d.items():
            # sh = self.__point_d[point]
            x1 = point.x * 30
            y1 = point.y * 30
            # print(x1, y1)
            self.canvas.coords(shape, x1, y1, x1 + 10, y1 + 10)
        self.win.update_idletasks()
        self.win.update()
        time.sleep(1)
        return ""

    # def append(self, point):
    #     # si c'est un nouveau point, alors on l'ajoute dans le dictionnaire
    #     fill = point.color
    #     self.__point_d[point] = self.canvas.create_rectangle(0, 0, 0, 0, width=4, fill=fill)

    def set_point_d(self, point_d):
        self.__point_d = point_d
        for p in self.__point_d.keys():
            self.__point_d[p] = self.canvas.create_rectangle(0, 0, 0, 0, width=4, fill=p.color)


class Point:
    """ classe Point : Un point est représenté par son abscisse et son ordonnée """

    __COLORS = ['red', 'green', 'blue', 'yellow', 'orange', 'black', 'white', 'magenta', 'cyan']

    def __init__(self, x=0, y=0 ):
        """
        Constructeur : coordonnées (0, 0) par défaut
        l'object point est envoyé à l'objet output qui est textuel ou  graphique
        """
        self.__x = x
        self.__y = y
        # self.__output = output
        self.__distance = -1    # la distance sera calculée "on the fly"
        self.__color = random.sample(self.__COLORS, 1)[0]
        # self.__output.append(self)

    def __repr__(self):
        """
        pas de méthode ___str__ car la classe Point
        ne s'occupe pas de l'affichage, qui est confié à un autre objet
        """
        pass

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
        if self.__distance < 0  :
            self.__distance = math.sqrt( self.__x**2 + self.__y**2 )
        return self.__distance

    def forward(self):
        """
        on fait avancer le point de "2" (càd 20 pixels) vers la droite
        la distance calculée n'étant plus bonne, on la réinitialise à -1
        """
        self.__x += 2
        self.__distance = -1


class PointAggregation:

    def __init__(self, out, nb_points ):
        self.__point_d = {}
        self.__output = out
        for i in range(nb_points):
            p = Point(random.randint(0,10), random.randint(0,10))
            self.__point_d[p] = ""
        self.__output.set_point_d(self.__point_d)

    def __repr__(self):
        return repr(self.__output)

    def forward(self):
        for p in self.__point_d.keys():
            p.forward()


#------ Programme principal -------
if __name__ == '__main__':
    o = int(input(" Output ? 1 pour texte, 2 pour graphique "))
    match o:
        case 2:
            output = GraphicalOutput()
        case _:
            output = TextOutput()

    # on crée les points (random)
    point_a = PointAggregation( output, 5 )   # on crée 5 points dans le PointAggregation

    # on affiche les points
    print(repr(point_a))

    # on fait bouger les points et on réaffiche
    for i in range(10):
        point_a.forward()
        print(repr(point_a))




