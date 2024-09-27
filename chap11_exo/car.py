# Programmez une voiture autonome
# • classe Car
# • contructeur, arguments :
# • nom de la voiture
# • vitesse de démarrage  zéro par défaut
# • changement de vitesse,
# méthodes :
# • increment()
# • decrement()
# • increment(n)
# • Output
# Peugeot: speed 0 km/h
# Peugeot: speed 1 km/h
# Peugeot: speed 11 km/h
# Peugeot: speed 10 km/h

class Car:

    def __init__(self, name, start_speed=0):
        self.name = name
        self.speed = start_speed

    def __str__(self):
        return f"{self.name}: speed {self.speed} km/h"

    def decrement(self):
        self.speed -= 1
        if self.speed < 0 : self.speed = 0

    def increment(self, n=1 ):
        self.speed += n


if __name__ == "__main__":
    voiture_A = Car("Peugeot")
    print(voiture_A)
    voiture_A.increment()
    print(voiture_A)
    voiture_A.increment(3)
    print(voiture_A)
    voiture_A.decrement()
    voiture_A.decrement()
    voiture_A.decrement()
    voiture_A.decrement()
    voiture_A.decrement()
    voiture_A.decrement()
    voiture_A.decrement()
    voiture_A.decrement()
    print(voiture_A)
