from abc import ABC, abstractmethod


class Light:
    """ sujet : feu de signalisation
        color = 1 = RED
              = 2 = GREEN
              = 3 = YELLOW
    """
    name_l = [ "", "RED", "GREEN", "YELLOW" ]

    def __init__(self):
        self.observer_l = []
        self.color = 1

    def __str__(self):
        out = ""
        for o in self.observer_l:
            out += o.brand + ", "
        return "Light says : My color is {}; I follow the cars {}".format(
            Light.name_l[self.color],
            out )

    def change(self):
        self.color += 1
        if self.color > 3:
            self.color = 1
        self.notify_observer_l()

    def notify_observer_l(self, *args, **kwargs):
        for obs in self.observer_l:
            obs.notify(self, *args, **kwargs)

    def subscribe(self, observer):
        self.observer_l.append(observer)

    def unsubscribe(self, observer):
        self.observer_l.remove(observer)


class Vehicle(ABC):
    """ observateur """

    def __init__(self, brand):
        self.brand = brand
        self.running = False

    def __str__(self):
        if self.running == True :
            return "{} says: Yeah, running on the road 66.".format(self.brand)
        else :
            return "{} says: Arghh, waiting for the green light.".format(self.brand)

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    @abstractmethod
    def notify(self, light):
        pass


class Car(Vehicle):
    def notify(self, light):
        """ la voiture passe au vert et s'arrête au rouge et à l'orange """
        if light.color == 2:
            self.start()
        elif light.color == 1 or light.color == 3:
            self.stop()


class BadCar(Vehicle):
    def notify(self, light):
        """ la voiture passe au vert et à l'orange et s'arrête au rouge """
        if light.color == 2 or light.color == 2 :
            self.start()
        elif light.color == 1:
            self.stop()


class VeryBadCar(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)
        self.running = True

    def notify(self, light):
        """ la voiture passe le feu sans jamais s'arrêter """
        self.start()


if __name__ == '__main__':
    voiture_A = Car("Peugeot")
    voiture_B = BadCar("BMW")
    voiture_C = VeryBadCar("Lada")
    feu01 = Light()
    feu01.subscribe(voiture_A)
    feu01.subscribe(voiture_B)
    feu01.subscribe(voiture_C)

    for i in range(6):
        print(feu01)
        print(voiture_A)
        print(voiture_B)
        print(voiture_C)
        print()
        feu01.change()
