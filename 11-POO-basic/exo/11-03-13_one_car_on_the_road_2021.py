class Car:

    def __init__(self, name):
        self.__name = name
        self.__speed = 0
        self.__time = 0
        self.__position = 0
        self.__duration = 0

    def __str__(self):
        s = "{0}: sp {1:3} km/h, ti {3:4.1f} h, po {2:5.1f} km"
        return s.format(self.__name, self.speed, self.__position, self.__time)

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, val):
        # si vitesse fournie invalide alors vitesse courante inchangée
        # alternative :
        # si vitesse fournie invalide alors la modifier en la rendant valide
        # par exemple :
        # if v < 0 : v = 0
        # if v > 120 : v = 120
        if val > 50 or val < 0 :
            print("vitesse {} non acceptée, vitesse courante inchangée".format(val))
        else:
            self.__speed = val

    @property
    def duration(self):
        # en fait ceci est inutile
        return self.__duration

    @duration.setter
    def duration(self, val):
        if val <= 0 :
            print("duration doit être strictement positif, valeur rejetée")
            return
        self.__duration = val

    def forward(self):
        """ forward() fait avancer la voiture en fonction de duration et speed """
        self.__time += self.__duration
        self.__position += self.__duration * self.__speed


# MAIN
voiture_A = Car("A")
print(voiture_A)
voiture_A.speed = 150
voiture_A.duration = -0.5
print(voiture_A)
voiture_A.speed = 30
voiture_A.duration = 0.5
voiture_A.forward()
print(voiture_A)
voiture_A.forward()
print(voiture_A)
voiture_A.speed = 50
voiture_A.duration = 0.5
voiture_A.forward()
print(voiture_A)
