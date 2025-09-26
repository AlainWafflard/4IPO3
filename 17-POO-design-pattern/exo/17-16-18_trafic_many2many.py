from abc import ABC, abstractmethod
import time


class Traffic:
    """ event engine(en abrégé : EE) """

    def __init__(self):
        # self.observer_l = []
        self.observable_l = []

    def subscribe_observable(self, o):
        self.observable_l.append(o)

    def notify(self, observer):
        """ OE signale à EE un changement de position
            cet OE sera souscrit ou non à un feu en fonction de sa position
            si OE est à hauteur d'un feu, il est souscrit à ce feu
            sinon il est désouscrit de tous les feux
        """
        for oa in self.observable_l:
            if oa.position - 1 <= observer.position <= oa.position:
                # observer est à hauteur de oa => notification
                # print("Yes, subscribe ! ", oa.name, "oe {}, oa {}".format(observer.position, oa.position))
                oa.subscribe(observer)
            elif oa.position < observer.position:
                # la voiture a dépassé le feu => désouscrire
                # print("No, unsubscribe !")
                oa.unsubscribe(observer)
            else:
                # la voiture est très en avant du feu
                # print("No!")
                pass

    def next(self):
        # changement des feux, ordre envoyé aux feux
        for oa in self.observable_l:
            oa.next()


class Light:
    """ sujet : feu de signalisation (abrégé : OA) """
    name_l = ["", "RED", "GREEN", "YELLOW"]

    def __init__(self, name, event_engine, time=0, position=0):
        self.name = name
        self.observer_l = []
        self.time = time
        self.color = None
        self.set_color()
        event_engine.subscribe_observable(self)
        self.position = position

    def __str__(self):
        out = ""
        for o in self.observer_l:
            out += o.brand + ", "
        if out == "" : out = "nobody"
        return "Light {} : color {}, subscribed : {}".format(
            self.name,
            Light.name_l[self.color],
            out )

    def next(self):
        """ le feu change en boucle suivant un certain schedule """
        self.time += 1
        if self.time > 9:
            self.time = 0
        self.set_color()
        self.notify_observer_l()

    def subscribe(self, o):
        """ souscription des observateurs (OE) au sujet """
        if o not in self.observer_l:
            self.observer_l.append(o)
            print(o.brand, "is subscribed to", self.name)

    def unsubscribe(self, o):
        """ désouscription des observateurs (OE) au sujet """
        if o in self.observer_l:
            self.observer_l.remove(o)
            print(o.brand, "is unsubscribed from", self.name)

    def notify_observer_l(self):
        # print(self.name, "observer list:", self.observer_l)
        for obs in self.observer_l:
            # print(self.name, "is notifying", obs.brand)
            obs.notify(self)

    def set_color(self):
        """ la couleur est fonction du temps
            i = 0 to 4 : rouge
            i = 5 to 8 : vert
            i = 9      : orange
        """
        if self.time in range(0, 5):
            self.color = 1
        elif self.time in range(5, 9):
            self.color = 2
        elif self.time in range(9, 10):
            self.color = 3
        else:
            raise Exception('time value KO : ', self.time)


class Vehicle(ABC):
    """ observateur (en abrégé : OE) """

    def __init__(self, brand, event_engine):
        self.brand = brand
        self.running = True
        self.event_engine = event_engine
        self.position = 0

    def __str__(self):
        if self.running:
            return "{} : running, position {}".format(self.brand, self.position)
        else:
            return "{} : waiting, position {}".format(self.brand, self.position)

    def next(self):
        # OE roule si état = running
        # print("debug, def move, {}".format(self.brand))
        if self.running:
            # print("debug, is running")
            self.position += 1
            self.event_engine.notify(self)

    def start(self):
        # OE change d'état en "running"
        # OE signale son changement d'état à EE
        # print("debug, {} start".format(self.brand))
        if not self.running:
            self.running = True
            # print("debug, {} start, changed".format(self.brand))
            self.event_engine.notify(self)

    def stop(self):
        # OE change d'état en "not running"
        # OE signale son changement d'état à EE
        # print("debug, {} stop".format(self.brand))
        if self.running:
            self.running = False
            # print("debug, {} stop, changed".format(self.brand))
            self.event_engine.notify(self)

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
        if light.color == 2 or light.color == 2:
            self.start()
        elif light.color == 1:
            self.stop()


class VeryBadCar(Vehicle):
    # def __init__(self, brand, event_m):
    #     """ la voiture est toujours roulante """
    #     super().__init__(brand, event_m)
    #     self.running = False

    def notify(self, light):
        """ la voiture passe le feu sans s'arrêter """
        self.start()


if __name__ == '__main__':
    trafic = Traffic()
    feu_l = [
        Light("Feu01", trafic, 1, 5),
        Light("Feu02", trafic, 5, 10),
        Light("Feu03", trafic, 8, 15),
        Light("Feu04", trafic, 3, 20),
    ]
    voiture_l = [
        Car("Peugeot", trafic),
        BadCar("BMW", trafic),
        VeryBadCar("Lada", trafic),
        Car("Tesla", trafic)
    ]

    for i in range(25):
        for v in voiture_l:
            v.next()
            print(v)
        for f in feu_l:
            print(f)
        print()
        time.sleep(3)
        trafic.next()
