# Encapsulation : attributs privés publics
# getter setter : méthode pythonienne : avec les décorateurs

class Light:
    """ modélisation du feu de signalisation
        color = 1 = RED
              = 2 = GREEN
              = 3 = YELLOW
    """
    color_name_a = ("", "RED", "GREEN", "YELLOW")

    def __init__(self, car):
        self.__color = 1
        self.__car = car

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, v):
        """ on valide la nouvelle valeur (range(1,4))
            si valeur invalide, alors on pose valeur = 1 (rouge)
        """
        if v in range(1, 4):
            self.__color = v
        else:
            self.__color = 1
        print("new color for light : {}".format(self.__color))

    @property
    def car(self):
        return self.__car

    def change(self):
        """ on change la couleur du feu
            si rouge alors voiture stoppe
            si vert alors voiture démarre
        """
        self.color += 1
        if self.color == 2:
            self.car.start()
        elif self.color == 1:
            self.car.stop()

    def __str__(self):
        # notice the expression "self.car.brand"
        # it seems to be a direct access to the attribute "brand" ...
        # but it is not : A getter is used in class Car !
        return "Light says : My color is {}; I follow the car {}".format(
            self.color_name_a[self.color],
            self.car.brand)


class Car:

    def __init__(self, brand):
        self.__brand = brand
        self.__running = False

    @property
    def brand(self):
        # brand getter via @property décorator
        return self.__brand

    @brand.setter
    def brand(self, val):
        # brand setter via @brand.setter décorator
        self.__brand = val

    @property
    def running(self):
        return self.__running

    @running.setter
    def running(self, v):
        if v == True or v == False:
            self.__running = v
        else:
            print("KO")
            return

    def start(self):
        # malgré les apparences, "running" est bien un attribut privé
        self.running = True

    def stop(self):
        # malgré les apparences, "running" est bien un attribut privé
        self.running = False

    def __str__(self):
        if self.running == True :
            return "{} says: Yeah, running on the road 66.".format(self.brand)
        else :
            return "{} says: Arghh, waiting for the green light.".format(self.brand)


if __name__ == '__main__':
    voiture_A = Car("Peugeot")
    feu01 = Light(voiture_A)
    print(feu01)
    print(voiture_A)

    for i in range(4):
        feu01.change()
        print(feu01)
        print(voiture_A)


