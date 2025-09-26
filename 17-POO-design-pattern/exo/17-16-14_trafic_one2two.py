
class Light:
    """ sujet : feu de signalisation
        color = 1 = RED
              = 2 = GREEN
              = 3 = YELLOW
    """
    color_name_a = [ "", "RED", "GREEN", "YELLOW"]

    def __init__(self):
        self.observer_l = []
        self.color = 1

    def __str__(self):
        out = ""
        for o in self.observer_l:
            out += o.brand + ", "
        return "Light says : My color is {}; I follow the cars {}".format(
            Light.color_name_a[self.color],
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

    def notify(self, light):
        """ la voiture passe au vert et s'arrête au rouge et à l'orange """
        if light.color == 2:
            self.start()
        elif light.color == 1 or light.color == 3:
            self.stop()


class BadCar(Car):
    def notify(self, light):
        """ la voiture passe au vert et à l'orange et s'arrête au rouge """
        if light.color == 2 or light.color == 2 :
            self.start()
        elif light.color == 1:
            self.stop()


if __name__ == '__main__':
    voiture_A = Car("Peugeot")
    voiture_B = BadCar("BMW")
    feu01 = Light()
    feu01.subscribe(voiture_A)
    feu01.subscribe(voiture_B)

    for i in range(6):
        print(feu01)
        print(voiture_A)
        print(voiture_B)
        feu01.change()
