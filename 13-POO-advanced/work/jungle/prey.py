class Prey:

    def __init__(self, position):
        self.__position = position
        self.__predator = None
        self.__water = None
        self.__plant = None

    def __sub__(self, other):
        return self.position - other.position

    @property
    def position(self):
        return self.__position

    def set_predator(self, predator):
        self.__predator = predator

    def set_water(self, water):
        self.__water = water

    def set_plant(self, plant):
        self.__plant = plant

    def move(self):
        if abs(self.__position - self.__predator.position ) <= 20:
            if self.__predator.position > self.position :
                self.__position -= 7
            else:
                self.__position += 7
        elif abs(self.__water.position - self.position) <= 5:
            print(f"prey is drinking water ({self.position})")

        elif abs(self.__plant.position - self.position) <= 5 and self.__plant.size > 0 :
            self.__plant.decrease()
            print(f"prey is eating plan ({self.position})")

        elif self.__water.position < self.position:
            self.__position -= 5
        else:
            self.__position += 5
        # else: # pas nécessaire
        print(f"prey at {self.__position}")


