class Carre:
    nom = "carré"

    def __init__(self, cote_l):
        # self.cote = int(input(" côté ? "))
        self.cote = cote_l[0]
        # self.nom = "carré"

    def __ge__(self, other):
        return self.surface() >= other.surface()

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

    def __ge__(self, other):
        return self.surface() >= other.surface()

    def surface(self):
        return self.long * self.larg

    def perimetre(self):
        return 2 * (self.long + self.larg)


if __name__ == "__main__":
    coteA_l = [ 3, 4 ]
    coteB_l = [ 3, 3 ]
    # cote_l.append(int(input(" côté 1 ? ")))
    # cote_l.append(int(input(" côté 2 ? ")))

    if coteA_l[0] != coteA_l[1]:
        formeA_o = Rectangle(coteA_l)
    else:
        formeA_o = Carre(coteA_l)

    if coteB_l[0] != coteB_l[1]:
        formeB_o = Rectangle(coteB_l)
    else:
        formeB_o = Carre(coteB_l)

    print("surface :", formeA_o.surface())
    print("surface :", formeB_o.surface())
    print(" A <= B ? ", formeA_o <= formeB_o )

