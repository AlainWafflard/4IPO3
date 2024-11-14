from car import *


class Light:

    def __init__(self, car_o):
        self.color = 1
        self.car_o = car_o

    def __str__(self):
        return f"light color is {self.color}"

    def change(self):
        self.color += 1
        if self.color > 3:
            self.color = 1
        match self.color:
            case 1 :
                self.car_o.stop()
            case 2 :
                self.car_o.stop()
            case 3 :
                self.car_o.start()


if __name__ == "__main__":
    voiture_A = Car("Peugeot")
    feu01 = Light(voiture_A)
    print(feu01)
    print(voiture_A)
    for i in range(4):
        feu01.change()
        print(feu01)
        print(voiture_A)
    feu01 = None
    print(voiture_A)

