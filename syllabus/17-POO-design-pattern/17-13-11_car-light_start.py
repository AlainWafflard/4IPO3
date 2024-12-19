# une voiture
# un feu

class Car:
    def __init__(self, name, position=0):
        self.name = name
        self.is_running = False # à l'arrêt

    def __str__(self):
        # Peugeot: waiting green light
        if self.is_running:
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
    def __init__(self, car):
        self.car = car
        self.state = 1  # RED

    def __str__(self):
        # Light following a car
        return f"Light: {self.state}, following {self.car.name}"

    def change(self):
        # changement de couleur
        self.state += 1
        if self.state > 3:
            self.state = 1
        # message envoyé à la voiture
        if self.state == 2:
            self.car.start()
        elif self.state == 3:
            pass
        elif self.state == 1:
            self.car.stop()


if __name__ == '__main__':
    # main
    voiture_A = Car("ma bécane")
    feu01 = Light(voiture_A)
    print(feu01)
    print(voiture_A)
    for i in range(10):
        feu01.change()
        print(feu01)
        print(voiture_A)

