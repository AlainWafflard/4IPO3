"""Feu de signalisation lié à une voiture autonome.

Le feu (Light) commande la voiture (Car) : start() au vert, stop() au rouge.
Convention : attributs privés (__attr), accès par @property / @x.setter.
"""
from enum import Enum


class Color(Enum):
    # l'ordre de déclaration est l'ordre du cycle : RED -> GREEN -> YELLOW -> RED
    RED = 1
    GREEN = 2
    YELLOW = 3


class Car:
    def __init__(self, name):
        self.__name = name
        self.__state = "waiting green light"

    def __str__(self):
        return f"{self.__name}: {self.__state}"

    @property
    def name(self):                 # «get»
        return self.__name

    @property
    def state(self):                # «get»
        return self.__state

    def start(self):
        self.__state = "running on the road"

    def stop(self):
        self.__state = "waiting green light"


class Light:
    def __init__(self, car):
        self.__car = car            # rôle -car : le feu connaît sa voiture
        self.__color = Color.RED
        self.__car.stop()           # le feu est rouge : la voiture attend

    def __str__(self):
        return f"Light: {self.__color.name}, follow {self.__car.name}"

    @property
    def color(self):                # «get»
        return self.__color

    @color.setter
    def color(self, value):         # «set»
        if not isinstance(value, Color):
            raise TypeError(f"Color attendu, reçu : {value!r}")
        self.__color = value

    def change(self):
        # passer à la couleur suivante dans l'ordre de Color
        colors = list(Color)
        self.color = colors[(colors.index(self.__color) + 1) % len(colors)]
        # commander la voiture ; au jaune, elle continue de rouler
        if self.__color is Color.GREEN:
            self.__car.start()
        elif self.__color is Color.RED:
            self.__car.stop()


if __name__ == "__main__":
    voiture_A = Car("Peugeot")
    feu01 = Light(voiture_A)
    print(feu01)
    print(voiture_A)
    for i in range(4):
        feu01.change()
        print(feu01)
        print(voiture_A)
