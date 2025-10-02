# Programmez une voiture autonome
# classe Car
# changement de vitesse, méthodes
# increment()
# decrement()
# increment(n)

class Car :
    """
    Peugeot: speed 0 km/h
    Peugeot: speed 1 km/h
    Peugeot: speed 11 km/h
    Peugeot: speed 10 km/h
    """

    def __init__(self, name, speed=0 ):
        """
        contructeur, arguments :
        nom de la voiture
        vitesse de démarrage, zéro par défaut
        """
        self.name = name
        self.speed = speed

    def __str__(self):
        return f"{self.name}: speed {self.speed} km/h"

    def increment(self, n=1 ):
        self.speed += n

    def decrement(self):
        self.speed -= 1


if __name__ == "__main__":
    voiture_A = Car("Peugeot")
    print(voiture_A)
    voiture_A.increment()
    print(voiture_A)
    voiture_A.increment(10)
    print(voiture_A)
    voiture_A.decrement()
    print(voiture_A)

    voiture_B = Car("BMW", 50 )
    print(voiture_B)
    voiture_B.increment()
    print(voiture_B)
    voiture_B.increment(100)
    print(voiture_B)
    voiture_B.decrement()
    print(voiture_B)

