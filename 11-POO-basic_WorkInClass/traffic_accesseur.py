# Programmez un feu de signalisation
# • classe Light
# • trois états, cf image
# • pas d'aspect graphique
# • pas de constructeur
# avec l'attribut color privé et ses getter / setter.

# • Output
# light color is 1
# light color is 2
# light color is 3
# light color is 1
# • Input

class Light:

    def __init__(self, color=1):
        if color < 1 : color = 1
        if color > 3 : color = 3
        self.__color = color

    # @property
    # def color(self):
    #     return self.__color

    # @color.setter
    # def color(self, val):
    #     if val < 1 : val = 1
    #     if val > 3 : val = 3
    #     self.__color = val

    def __str__(self):
        return f"light color is {self.__color}"

    def change(self):
        self.__color += 1
        if self.__color > 3:
            self.__color = 1


if __name__ == "__main__":
    feu01 = Light(5)
    # feu01.color = 1
    print(feu01)
    # print(feu01.color)
    feu01.change()
    print(feu01)
    feu01.change()
    # feu01.color = 3
    print(feu01)
    feu01.change()
    # feu01.color = 3
    print(feu01)
    feu01.change()
    print(feu01)
    feu01.change()
    print(feu01)
    feu01.change()
    print(feu01)

