class Carre:
    def __init__(self):
        self.cote = int(input(" côté ? "))

    def surface(self):
        return self.cote * self.cote

    def perimetre(self):
        return 4 * self.cote

class Rectangle:
    def __init__(self):
        self.long = int(input(" côté long ? "))
        self.larg = int(input(" côté court ? "))

    def surface(self):
        return self.long * self.larg

    def perimetre(self):
        return 2 * (self.long + self.larg)


if __name__ == "__main__":
    forme_s = input(" forme ? R ou C ? ")
    if forme_s == "R" :
        forme_o = Rectangle()
    else:
        forme_o = Carre()

    # if forme_s == "R":
    #     surf = forme_o.long * forme_o.larg
    # else :
    #     surf = forme_o.cote * forme_o.cote

    print("surface :", forme_o.surface())
    # print("surface : ", surf)

