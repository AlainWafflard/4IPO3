from fauna import Fauna


class Predator(Fauna):

    def __init__(self, position, water):
        super().__init__(position, water)
        self.__prey = None

    def set_prey(self, prey):
        self.__prey = prey

    def move(self):
        if abs(self.__prey.position - self.position) < 25:
            # lion court après buffle
            if self.__prey.position > self.position :
                self._position += 10
            else:
                self._position -= 10
        elif abs(self._water.position - self.position) <= 5:
            print(f"predator is drinking water ({self.position})")
        elif self._water.position < self.position:
            self._position -= 5
        else:
            self._position += 5
        print(f"predator at {self.position}")

    # @property
    # def prey_caught(self):
    #     return abs( self.position - self.__prey.position ) < 5

