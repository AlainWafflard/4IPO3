class Light :
    """
    light color is 1
    light color is 2
    light color is 3
    light color is 1
    """
    __color_name_d = {
        1: "rouge",
        2: "vert",
        3: "orange"
    }

    def __init__(self):
        self.__color = 1

    def __str__(self):
        return f"light color is {self.__color}"

    @property
    def couleur(self):
        return self.__color_name_d[self.__color]

    def change(self):
        self.__color += 1
        if self.__color > 3 :
            self.__color = 1


if __name__ == "__main__":
    feu01 = Light()
    print(feu01.couleur)
    feu01.change()
    print(feu01.couleur)
    feu01.change()
    print(feu01.couleur)
    feu01.change()
    print(feu01.couleur)
    feu01.change()
    print(feu01.couleur)
    feu01.change()
    print(feu01.couleur)

    # feu01 = Light()
    # print(str(feu01.color))
    # feu01.change()
    # print(str(feu01.color))
    # feu01.change()
    # print(str(feu01.color))
    # feu01.change()
    # print(str(feu01.color))

