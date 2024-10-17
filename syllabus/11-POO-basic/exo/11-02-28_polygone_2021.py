import math


class Point:
    """ Un point est représenté par son abscisse x et son ordonnée y.
        Dans la classe Point, on accède directement aux valeurs de x et y
        qui sont publiques (non protégées).
    """

    def __init__(self, x=0, y=0):
        """ Constructeur : coordonnées (0, 0) par défaut
        """
        self.x = x
        self.y = y

    def __str__(self):
        return ("Point({},{})".format(self.x, self.y))

    def distance_pythagore(self):
        """ distance pythagorienne du point avec l’origine (0, 0)
            racine carrée de la somme des carrés de x et y 
        """
        d = math.sqrt(self.x * self.x + self.y * self.y)
        return d

    def distance_manhattan(self):
        """ distance manhattan du point avec l’origine (0, 0)
            somme des valeurs absolues de x et y
            on convertit la valeur en float pour retourner le même type
            de valeur quelque soient les valeurs de x et y 
        """
        d = float(abs(self.x) + abs(self.y))
        return d


######################################################################

class Segment:
    """ Un Segment est représenté par deux objets de type Point.
    """

    def __init__(self, p1, p2):
        # le constructeur vérifie si les deux arguments sont bien des
        # objets de type Point
        if (not isinstance(p1, Point) or not isinstance(p2, Point)):
            raise Exception('La classe Segment se construit à partir de deux objets de type Point')
        # les deux objets Point sont stockés comme attributs privés
        self.__p1 = p1
        self.__p2 = p2
        # Par défaut, la longueur du segment sera de type pythagorien.
        self.set_mode("pythagore")

    def set_mode(self, m):
        if m not in ["pythagore", "manhattan"]:
            raise Exception('choose mode as "pythagore" or "manhattan"')
        self.__mode = m
        # print("mode set to", self.__mode)

    def get_mode(self):
        return self.__mode

    def __str__(self):
        return "P1=({},{}) P2=({},{})".format(self.__p1.x, self.__p1.y, self.__p2.x, self.__p2.y)

    def __distance_pythagore(self):
        """ distance pythagorienne
            racine carrée de la somme des carrés des différences de x et de y
        """
        # méthode privée pour forcer l'appel aux méthodes "set_mode" et "distance"
        d = math.sqrt((self.__p1.x - self.__p2.x) ** 2 + (self.__p1.y - self.__p2.y) ** 2)
        return d

    def __distance_manhattan(self):
        """ distance manhattan
            somme des valeurs absolues des différences de x et de y
        """
        # méthode privée pour forcer l'appel aux méthodes "set_mode" et "distance"
        d = float(abs(self.__p1.x - self.__p2.x) + abs(self.__p1.y - self.__p2.y))
        return d

    def distance(self):
        """ grouper les deux calculs de longueur en une seule méthode
        """
        if (self.get_mode() == "pythagore"):
            return self.__distance_pythagore()
        elif (self.get_mode() == "manhattan"):
            return self.__distance_manhattan()
        else:
            return ("error, bad mode, please specify manhattan or pythagore")

    def pente(self):
        """ calcule et retourne la pente (%) du segment, càd la division
            de la hauteur par la largeur
        """
        p = (self.__p1.y - self.__p2.y) / (self.__p1.x - self.__p2.x)
        return p



######################################################################

class Polygone:
    """
    classe Polygone : modélise un polygone quelconque à partir de N points
    basé sur les classes Point et Segment
    """

    def __init__(self, point_l):
        # une liste de points est donnée en unique paramètre
        self.__segment_l = []
        nb_points = len(point_l)
        for i in range(nb_points - 1):
            # on crée les segments p0-p1, p1-p2, p2-p3, etc.
            self.__segment_l.append(Segment(point_l[i], point_l[i + 1]))
        # on crée le dernier segment : pn-p0
        self.__segment_l.append(Segment(point_l[nb_points - 1], point_l[0]))

    def perimeter(self):
        perim = 0
        for s in self.__segment_l:
            perim += s.distance()
        return perim


######################################################################
# MAIN
# cf schéma 11-02-exo28_polygone_2021.jpg
p = Point(3, 4)
q = Point(0, 0)
r = Point(3, 0)
s = Point(6, 4)

poly = Polygone((q, r, s, p))

print(poly.perimeter())
