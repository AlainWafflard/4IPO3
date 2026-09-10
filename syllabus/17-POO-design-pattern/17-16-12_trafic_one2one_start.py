# Pas d'encapsulation : tous attributs publics

class Light:
    """ modélisation du feu de signalisation
        color = 1 = RED
              = 2 = GREEN
              = 3 = YELLOW
    """
    color_name_a = ["", "RED", "GREEN", "YELLOW"]

    def __init__(self, car):
        self.color = 1
        self.car = car

    def change(self):
        self.color += 1
        if self.color > 3:
            self.color = 1
        if self.color == 2:
            self.car.start()
        elif self.color == 1:
            self.car.stop()

    def __str__(self):
        return "Light says : My color is {}; I follow the car {}".format(
            self.color_name_a[self.color],
            self.car.brand )


class Car :

    def __init__(self, brand):
        self.brand = brand
        self.running = False

    def start(self):
        self.running = True

    def stop(self):
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
