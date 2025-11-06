class Carre:
    nom = "carré"

    def __init__(self, cote_l):
        # self.cote = int(input(" côté ? "))
        self.cote = cote_l[0]
        # self.nom = "carré"

    def surface(self):
        return self.cote * self.cote

    def perimetre(self):
        return 4 * self.cote


class Rectangle:
    nom = "rectangle"

    def __init__(self, cote_l):
        # self.long = int(input(" côté long ? "))
        # self.larg = int(input(" côté court ? "))
        self.long = cote_l[0]
        self.larg = cote_l[1]
        # self.nom = "box"

    def surface(self):
        return self.long * self.larg

    def perimetre(self):
        return 2 * (self.long + self.larg)


if __name__ == "__main__":
    cote_l = []
    cote_l.append(int(input(" côté 1 ? ")))
    cote_l.append(int(input(" côté 2 ? ")))

    if cote_l[0] != cote_l[1]:
        forme_o = Rectangle(cote_l)
    else:
        forme_o = Carre(cote_l)

    print("surface :", forme_o.surface(), f"( c'est un {forme_o.nom})")
    print(Rectangle.nom)

