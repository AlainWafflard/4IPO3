from abc import ABC, abstractmethod


class Observable(ABC):
    """ sujet """

    def __init__(self):
        self._observer_l = []

    def subscribe(self, observer):
        self._observer_l.append(observer)

    def notify_observer(self, msg):
        for obs in self._observer_l:
            obs.notify(msg)

    def unsubscribe(self, observer):
        self._observer_l.remove(observer)


class Observer(ABC):
    """ observateur """

    def __init__(self, observable):
        observable.subscribe(self)

    @abstractmethod
    def notify( self, message ):
        pass
        # print (f' {self.name} got this message from Observable : {message}')


class Light(Observable):
    """ modélisation du feu de signalisation
        color = 1 = RED
              = 2 = GREEN
              = 3 = YELLOW
    """
    color_name_a = ["", "RED", "GREEN", "YELLOW"]

    def __init__(self):
        super().__init__()
        self.color = 1
        # self.car = car

    def __str__(self):
        car_s = ""
        for car in self._observer_l:
            car_s += " " + car.brand
        return "Light says : My color is {}; I follow the car(s) {}".format(
            self.color_name_a[self.color],
            car_s )

    def change(self):
        self.color += 1
        if self.color > 3:
            self.color = 1
        self.notify_observer(self.color)

        # if self.color == 2:
        #     self.car.start()
        # elif self.color == 1:
        #     self.car.stop()


class Vehicle(Observer):

    def __init__(self, brand, observable):
        super().__init__(observable)
        self.brand = brand
        self.running = False

    def __str__(self):
        if self.running == True :
            return "{} says: Yeah, running on the road 66.".format(self.brand)
        else :
            return "{} says: Arghh, waiting for the green light.".format(self.brand)

    @abstractmethod
    def notify( self, message ):
        pass


class Car(Vehicle) :
    def notify(self, color):
        match color:
            case 1 :
                self.running = False
            case 2 :
                self.running = True
            case 3 :
                self.running = False


class BadCar(Vehicle):
    def notify(self, color):
        match color:
            case 1 :
                self.running = False
            case 2 :
                self.running = True
            case 3 :
                self.running = True


class VeryBadCar(Vehicle):
    def __init__(self, brand, observable):
        super().__init__(brand, observable)
        self.running = True

    def notify(self, color):
        match color:
            case 1 :
                self.running = True
            case 2 :
                self.running = True
            case 3 :
                self.running = True


if __name__ == '__main__':
    feu01 = Light()
    voiture_A = Car("Peugeot", feu01)
    voiture_B = BadCar("BMW", feu01)
    voiture_C = VeryBadCar("Trottinette", feu01)

    print(feu01)
    print(voiture_A)
    print(voiture_B)
    print(voiture_C)
    print()

    for i in range(4):
        feu01.change()
        print(feu01)
        print(voiture_A)
        print(voiture_B)
        print(voiture_C)
        print()

