# A: sp 0km/h, ti 0.0h, po 0.0km
# A: sp 50km/h, ti 1.0h, po 50.0km
# A: sp 50km/h, ti 1.5h, po 75.0km
# A: sp 50km/h, ti 2.5h, po 125.0km

class Car:

    def __init__(self, name):
        self.__name = name
        self.speed = 0
        self.duration = 0
        self.__position = 0
        self.__time = 0

    def __str__(self):
        return f"{self.__name}: sp {self.speed}km/h, ti {self.time}h, po {self.position}km"

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, val ):
        if val < -5 : val = -5
        if val > 120 : val = 120
        self.__speed = val

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, val ):
        if val < 0 : val = 0
        self.__duration = val

    @property
    def time(self):
        return self.__time

    @property
    def position(self):
        return self.__position

    # @duration.setter
    # def duration(self, val ):
    #     self.__duration = val


    def forward(self):
        self.__time += self.duration
        self.__position += self.duration * self.speed


if __name__ == "__main__":
    voiture_A = Car("A")
    print(voiture_A)
    voiture_A.speed = 50
    voiture_A.duration = 1
    voiture_A.forward()
    print(voiture_A)
    voiture_A.speed = 100
    voiture_A.duration = 0.25
    voiture_A.forward()
    print(voiture_A)

    try:
        voiture_A.time = 0
    except:
        print("error time")
    try:
        voiture_A.position = 0
    except:
        print("error position")

    voiture_A.duration = -10
    voiture_A.forward()
    print(voiture_A)
    voiture_A.speed = -10
    voiture_A.duration = 1
    voiture_A.forward()
    print(voiture_A)

