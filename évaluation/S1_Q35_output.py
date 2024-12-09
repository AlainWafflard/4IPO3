import time
import tkinter


class TextOutput1:
    """ Manages the textual output of a series of points """

    def __init__(self):
        self.__point_d = {}

    def __repr__(self):
        """
        créer un string avec les coordonnées des points
        """
        out = ""
        for point in self.__point_d.keys():
            out += f"Point({point.x},{point.y}) ; dist = {point.distance:5.2f} ; color = {point.color}\n"
        return out

    def set_point_d(self, point_d):
        """
        set the dictionary with points from the aggregator
        :param point_d: dictionary with points
        """
        self.__point_d = point_d


class GraphicalOutput1:
    """ Manages the graphical output of a series of points """

    def __init__(self):
        # Création du widget principal
        self.win = tkinter.Tk()
        self.win.title("POINT - graphical output")
        self.win.wm_attributes('-topmost', 1)

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

    def set_point_d(self, point_d):
        """
        set the dictionary with points from the aggregator
        enrich this dictionary with Tkinter.Shape object, so we get the structure
            key : Point object => value Shape object
        :param point_d: dictionary with points
        """
        self.__point_d = point_d
        for p in self.__point_d.keys():
            self.__point_d[p] = self.canvas.create_rectangle(0, 0, 0, 0, width=4, fill=p.color)
