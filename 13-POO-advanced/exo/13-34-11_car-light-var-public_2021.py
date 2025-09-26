# Pas d'encapsulation : tous attributs publics

class Car:
    def __init__(self, name):
        self.name = name
        self.state = False # à l'arrêt

    def __str__(self):
        # Peugeot: waiting green light
        if self.state == True:
            return "Car {}: moving ... ".format(self.name)
        else:
            return "Car {}: waiting for the green light".format(self.name)

    def stop(self):
        # voiture à l'arrêt
        self.state = False

    def start(self):
        # voiture en marche
        self.state = True


class Light:
    def __init__(self, car):
        self.car = car
        self.state = 1  # RED

    def __str__(self):
        # Light: RED, follow Peugeot
        return "Light: {}, following {}".format( self.state, self.car.name)

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
    voiture_A = Car("Peugeot")
    feu01 = Light(voiture_A)
    print(feu01)
    print(voiture_A)
    for i in range(4):
        feu01.change()
        print(feu01)
        print(voiture_A)
