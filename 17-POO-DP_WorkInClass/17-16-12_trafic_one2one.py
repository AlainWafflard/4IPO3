# Pas d'encapsulation : tous attributs publics

class Light:
    """ OBSERVABLE
        modélisation du feu de signalisation
        color = 1 = RED
              = 2 = GREEN
              = 3 = YELLOW
    """
    color_name_a = ["", "RED", "GREEN", "YELLOW"]

    def __init__(self):
        self.__observer_l = []
        self.color = 1
        # self.car = car
        # self.subscribe(car)

    def subscribe(self, observer):
        self.__observer_l.append(observer)

    def unsubscribe(self, observer):
        self.__observer_l.remove(observer)

    def notify_observer(self):
        for obs in self.__observer_l:
            obs.notify(self.color)

    def change(self):
        self.color += 1
        if self.color > 3:
            self.color = 1
        # if self.color == 2:
        #     self.car.start()
        # elif self.color == 1:
        #     self.car.stop()
        self.notify_observer()

    def __str__(self):
        return f"Light says : My color is {self.color_name_a[self.color]};"


class Car :
    """ OBSERVER """

    def __init__(self, observable, brand):
        self.brand = brand
        self.running = False
        observable.subscribe(self)

    def notify( self, color ):
        if color == 2:
            self.start()
        elif color == 1 or color == 3:
            self.stop()

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
    feu01 = Light()
    voiture_A = Car( feu01, "Peugeot")
    print(feu01)
    print(voiture_A)

    for i in range(4):
        feu01.change()
        print(feu01)
        print(voiture_A)
