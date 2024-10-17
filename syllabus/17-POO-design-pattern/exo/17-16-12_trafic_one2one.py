
class Light:
    """ sujet : feu de signalisation
        color = 1 = RED
              = 2 = GREEN
              = 3 = YELLOW
    """
    color_name_a = [ "", "RED", "GREEN", "YELLOW"]

    def __init__(self, car):
        self.observer = car
        self.color = 1

    def __str__(self):
        return "Light says : My color is {}; I follow the car {}".format(
            Light.color_name_a[self.color],
            self.observer.brand )

    def change(self):
        self.color += 1
        if self.color > 3:
            self.color = 1
        self.notify_observers()

    def notify_observers(self):
        self.observer.notify(self.color)


class Car :
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

    def notify(self, color):
        if color == 2:
            self.start()
        elif color == 1:
            self.stop()


if __name__ == '__main__':
    voiture_A = Car("Peugeot")
    feu01 = Light(voiture_A)

    for i in range(10):
        print(feu01)
        print(voiture_A)
        feu01.change()
