
class Light:

    def __init__(self, car_o ):
        self.__car_o = car_o
        self.__color = 1

    def __str__(self):
        """
        Light: RED, follow Peugeot
        Light: GREEN, follow Peugeot
        """
        return f"Light: {self.__color}, following {self.__car_o.name}"

    def change(self):
        self.__color += 1
        if self.__color > 3 :
            self.__color = 1
        self.__send_command()

    def __send_command(self):
        match self.__color:
            case 1 | 3 :
                # rouge
                self.__car_o.stop()
            case 2 :
                # vert
                self.__car_o.start()


class Car:

    def __init__(self, name):
        self.__name = name
        self.__status = ""
        self.stop()

    def __str__(self):
        """
        Peugeot: waiting green light
        Peugeot: running on the road
        """
        return f"{self.__name}: {self.__status}"

    @property
    def name(self):
        return self.__name

    def start(self):
        self.__status = "running on the road"

    def stop(self):
        self.__status = "waiting green light"



if __name__ == "__main__":
    voiture_A = Car("Peugeot")
    feu01 = Light(voiture_A)
    print(feu01)
    print(voiture_A)
    for i in range(4):
        feu01.change()
        print(feu01)
        print(voiture_A)

