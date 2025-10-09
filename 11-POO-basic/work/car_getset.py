
class Car :
    """
    Peugeot: speed 0 km/h
    Peugeot: speed 1 km/h
    Peugeot: speed 11 km/h
    Peugeot: speed 10 km/h
    """

    def __init__(self, name ):
        """
        contructeur, arguments :
        nom de la voiture
        vitesse de démarrage, zéro par défaut
        """
        self.__name = name
        self.speed = 0
        self.duration = 0
        self.__position = 0

    def __str__(self):
        return f"{self.__name}: sp {self.speed}km/h, ti {self.duration}h, po {self.__position}km"
        # return f"{self.name}: speed {self.speed} km/h"

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, val):
        if val < 0 : val = 0
        if val > 70 : val = 70
        self.__speed = val

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, val):
        if val < 0 : val = 0
        self.__duration = val

    def forward(self):
        self.__position += self.speed * self.duration


if __name__ == "__main__":
    voiture_A = Car("A")
    print(voiture_A)
    voiture_A.speed = 50
    voiture_A.duration = 1
    voiture_A.forward()
    print(voiture_A)
    voiture_A.speed = 100
    voiture_A.duration = 0.5
    voiture_A.forward()
    print(voiture_A)
    voiture_A.duration = 1
    voiture_A.forward()
    print(voiture_A)

    # voiture_A = Car("Peugeot")
    # print(voiture_A)
    # voiture_A.increment()
    # print(voiture_A)
    # voiture_A.increment(10)
    # print(voiture_A)
    # voiture_A.decrement()
    # print(voiture_A)
    #
    # voiture_B = Car("BMW", 50 )
    # print(voiture_B)
    # voiture_B.increment()
    # print(voiture_B)
    # voiture_B.increment(100)
    # print(voiture_B)
    # voiture_B.decrement()
    # print(voiture_B)
    #
