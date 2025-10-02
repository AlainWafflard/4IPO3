class Light :
    """
    light color is 1
    light color is 2
    light color is 3
    light color is 1
    """

    def __init__(self):
        self.__color = 1

    def __str__(self):
        return f"light color is {self.__color}"

    def change(self):
        self.__color += 1
        if self.__color > 3 :
            self.__color = 1


if __name__ == "__main__":
    feu01 = Light()
    feu01.__color = 1
    print(feu01)
    feu01.change()
    print(feu01)
    feu01.change()
    print(feu01)
    feu01.change()
    feu01.__color = 2
    print(feu01)
    feu01.change()
    print(feu01)
    feu01.change()
    print(feu01)
