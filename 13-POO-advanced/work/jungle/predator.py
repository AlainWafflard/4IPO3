class Predator:

    def __init__(self, position):
        self.__position = position
        self.__prey = None
        self.__water = None

    def __sub__(self, other):
        return self.position - other.position

    @property
    def position(self):
        return self.__position

    def set_prey(self, prey):
        self.__prey = prey

    def set_water(self, water):
        self.__water = water

    def move(self):
        if abs(self.__prey.position - self.position) < 25:
            # lion court après buffle
            if self.__prey.position > self.position :
                self.__position += 10
            else:
                self.__position -= 10
        elif abs(self.__water.position - self.position) <= 5:
            print(f"predator is drinking water ({self.position})")
        elif self.__water.position < self.position:
            self.__position -= 5
        else:
            self.__position += 5
        print(f"predator at {self.position}")

    # @property
    # def prey_caught(self):
    #     return abs( self.position - self.__prey.position ) < 5

