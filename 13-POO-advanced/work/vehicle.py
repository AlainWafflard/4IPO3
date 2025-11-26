class Vehicle:
    __color = "white"
    _seating_capacity = 4

    def __init__(self, name, max_speed):
        self.__name = name
        self.__max_speed = max_speed

    def __str__(self):
        # return f"name:{self.__name}, speed:{self.__max_speed}, color:{self.__color}, seats:{self.__seating_capacity}"
        return f"name:{self.__name}, color:{self.__color}, seats:{self._seating_capacity}, fare:{self.fare()}"

    def fare(self):
        return self._seating_capacity * 50


class Bus(Vehicle):
    _seating_capacity = 50

    def fare(self):
        return super().fare() * 1.1


if __name__ == "__main__":
    v = Vehicle("Tesla", 180)
    print(v)
    b = Bus("Volvo", 120)
    print(b)

