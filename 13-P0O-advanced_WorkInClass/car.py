# Programmez une voiture autonome

# • Output
# Peugeot: speed 0 km/h
# Peugeot: speed 1 km/h
# Peugeot: speed 11 km/h
# Peugeot: speed 10 km/h

class Car:

    def __init__(self, name):
        self.__name = name
        self.speed = 0
        self.duration = 0
        self.__position = 0

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, val):
        if val < 0 :
            val = 0
            print("speed mise à 0")
        elif val > 50 :
            val = 50
            print("speed mise à 50")
        self.__speed = val

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, val):
        if val < 0 :
            val = 0
            print("duration mise à 0")
        self.__duration = val

    def __str__(self):
        """
        A: sp 50km/h, ti 1.5h, po  75.0km
        """
        return f"{self.__name}: sp {self.speed}km/h, ti {self.duration}h, po  {self.__position}km"

    def forward(self):
        self.__position += self.speed * self.duration

    def start(self):
        self.speed = 50
        self.duration = 10
        self.forward()

    def stop(self):
        self.speed = 0


if __name__ == "__main__":
    voiture_A = Car("mon auto")
    print(voiture_A)

    voiture_A.speed = 50
    voiture_A.duration = 1
    voiture_A.forward()
    print(voiture_A)

    voiture_A.duration = 0.5
    voiture_A.position = 1000
    voiture_A.forward()
    print(voiture_A)

    voiture_A.speed = 100
    voiture_A.duration = -12
    voiture_A.forward()
    print(voiture_A)
    # print(voiture_A.speed)

