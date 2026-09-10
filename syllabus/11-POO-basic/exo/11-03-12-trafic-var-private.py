class Light :

    def __init__(self):
        self.__color = 1

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, v ):
        if v > 3 : v = 1
        self.__color = v

    def change(self):
        # puisqu'on écrit "self.color ..." et non "self.__color"
        # la nouvelle valeur de l'attribut
        # sera attribuée via le setter du même nom
        # self.color += 1
        # si on écrit
        self.__color += 1
        # alors on court-circuite le setter et BUG !
        # (testez pour voir :-) )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    feu01 = Light()
    print("color : " + str(feu01.color))
    feu01.change()
    print("color : " + str(feu01.color))
    feu01.change()
    print("color : " + str(feu01.color))
    feu01.change()
    print("color : " + str(feu01.color))
    feu01.change()
    print("color : " + str(feu01.color))
