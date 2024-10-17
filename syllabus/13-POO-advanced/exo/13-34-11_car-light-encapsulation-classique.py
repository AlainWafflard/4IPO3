# Encapsulation : attributs privés publics
# getter setter : approche classique : avec méthodes "get_xxx" et "set_xxx"

class Light :
    """ modélisation du feu de signalisation
        color = 1 = RED
              = 2 = GREEN
              = 3 = YELLOW
    """
    __color_name_a = ["", "RED", "GREEN", "YELLOW"]  # variable de classe (statique)

    def __init__(self, car):
        self.__color = 1
        self.__car = car

    def change(self):
        self.__color += 1
        if self.__color > 3:
            self.__color = 1
        if self.__color == 2:
            self.__car.start()
        elif self.__color == 1:
            self.__car.stop()

    def __str__(self):
        return "Light : My color is {}; I follow the car {}".format(
            self.__color_name_a[self.__color],
            self.__car.get_brand() )

class Car :
    """ modélisation de la voiture
        il faut écrire un getter et un setter pour l'attribut brand;
    """

    def __init__(self, brand):
        self.set_brand(brand)
        self.__running = False

    def get_brand(self):
        # brand "getter"
        return self.__brand

    def set_brand(self, val):
        # brand "setter"
        self.__brand = val

    def start(self):
        self.__running = True

    def stop(self):
        self.__running = False

    def __str__(self):
        if self.__running == True :
            return "{} says: Yeah, running on the road 66.".format(self.__brand)
        else :
            return "{} says: Arghh, waiting for the green light.".format(self.__brand)


if __name__ == '__main__':
    voiture_A = Car("Peugeot")
    feu01 = Light(voiture_A)
    print(feu01)
    print(voiture_A)

    for i in range(4):
        feu01.change()
        print(feu01)
        print(voiture_A)

