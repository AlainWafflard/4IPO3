# une voiture
# un feu

class Car:
    def __init__(self, name, position=0):
        self.name = name
        self.is_running = False # à l'arrêt

    def __str__(self):
        # Peugeot: waiting green light
        if self.is_running == True:
            return "Car {}: moving ... ".format(self.name)
        else:
            return "Car {}: waiting for the green light".format(self.name)

    def stop(self):
        # voiture à l'arrêt
        self.is_running = False

    def start(self):
        # voiture en marche
        self.is_running = True


class Light:
    __color = [ "", "RED", "GREEN", "YELLOW"]

    def __init__(self, car):
        self.__car = car

    def __iter__(self):
        self.__state = 0
        return self

    def __str__(self):
        # Light following a car
        col = self.__color[self.__state]
        return "Light: {}, following {}".format( col, self.__car.name)

    def __next__(self):
        # changement de couleur
        self.__state += 1
        if self.__state > 3:
            self.__state = 1
        # message envoyé à la voiture
        if self.__state == 2:
            self.__car.start()
        elif self.__state == 3:
            pass
        elif self.__state == 1:
            self.__car.stop()


if __name__ == '__main__':
    # main
    voiture_A = Car("ma bécane")
    feu01 = iter(Light(voiture_A))
    for i in range(10):
        next(feu01)
        print(feu01)
        print(voiture_A)

