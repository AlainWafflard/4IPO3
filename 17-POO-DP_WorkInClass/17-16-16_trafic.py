# Pas d'encapsulation : tous attributs publics
from abc import ABC, abstractmethod
class Light:
    """ OBSERVABLE
        modélisation du feu de signalisation
        color = 1 = RED
              = 2 = GREEN
              = 3 = YELLOW
    """
    color_name_a = ["", "RED", "GREEN", "YELLOW"]
    time_interval_l = [ 0, 15, 10, 5]

    def __init__(self):
        self.__observer_l = []
        self.color = 1
        self.time_interval = 0

    def subscribe(self, observer):
        self.__observer_l.append(observer)

    def unsubscribe(self, observer):
        self.__observer_l.remove(observer)

    def notify_observer(self):
        for obs in self.__observer_l:
            obs.notify(self.color, self.time_interval)

    def change(self):
        self.color += 1
        if self.color > 3:
            self.color = 1
        self.time_interval = self.time_interval_l[self.color]
        self.notify_observer()

    def __str__(self):
        return f"Light says : My color is {self.color_name_a[self.color]};"


class Vehicle(ABC):
    """ OBSERVER """
    speed = 0

    @abstractmethod
    def notify( self, color, time_interval ):
        pass

    def __init__(self, observable, brand):
        self.brand = brand
        self.running = False
        observable.subscribe(self)
        self.distance = 0

    def start(self, time_interval):
        self.running = True
        self.distance += self.speed * time_interval / 3.6

    def stop(self):
        self.running = False

    def __str__(self):
        if self.running == True :
            return f"{self.brand} says: Yeah, running on the road 66 at distance {self.distance:.2f}."
        else :
            return f"{self.brand} says: Arghh, waiting for the green light at distance {self.distance:.2f}."


class Car(Vehicle) :
    speed = 30

    def notify( self, color, time_interval ):
        if color == 2:
            self.start(time_interval)
        elif color == 1 or color == 3:
            self.stop()


class BadCar(Vehicle):
    speed = 35

    def notify( self, color, time_interval ):
        if color == 2 or color == 3 :
            self.start(time_interval)
        elif color == 1 :
            self.stop()


class Bicycle(Vehicle):
    speed = 20

    def __init__(self, observable, brand):
        super().__init__(observable, brand)
        self.running = True

    def notify( self, color, time_interval ):
        self.start(time_interval)


if __name__ == '__main__':
    feu01 = Light()
    voiture_A = Car( feu01, "Peugeot")
    voiture_B = BadCar( feu01, "BMW")
    velo_C = Bicycle( feu01, "Antoine")
    print(feu01)
    print(voiture_A)
    print(voiture_B)
    print(velo_C)

    for i in range(6):
        feu01.change()
        print(feu01)
        print(voiture_A)
        print(voiture_B)
        print(velo_C)
