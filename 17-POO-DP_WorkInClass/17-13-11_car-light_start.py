# une voiture
# un feu

class Car:
    def __init__(self, name, position=0):
        self.name = name
        self.is_running = False # à l'arrêt

    def __str__(self):
        # Peugeot: waiting green light
        if self.is_running == True:
            return f"Car {self.name}: moving ... "
        else:
            return f"Car {self.name}: waiting for the green light"

    def stop(self):
        # voiture à l'arrêt
        self.is_running = False

    def start(self):
        # voiture en marche
        self.is_running = True


class Light:
    # state 1 = RED
    # state 2 = ORANGE
    # state 3 = GREEN

    def __init__(self, car):
        self.car = car
        self.state = 1  # RED

    def __iter__(self):
        return self

    def __str__(self):
        # Light following a car
        return f"Light: {self.state}, following {self.car.name}"

    def __next__(self):
        # changement de couleur
        self.state -= 1
        if self.state > 3:
            self.state = 1
        if self.state < 1:
            self.state = 3
        # message envoyé à la voiture
        if self.state == 3:
            self.car.start()
        elif self.state == 2:
            pass
        elif self.state == 1:
            self.car.stop()


if __name__ == '__main__':
    # main
    voiture_A = Car("ma bécane")
    feu01 = Light(voiture_A)
    feu01_it = iter(feu01)
    print(feu01_it)
    print(voiture_A)
    for i in range(10):
        next(feu01_it)
        print(feu01_it)
        print(voiture_A)

