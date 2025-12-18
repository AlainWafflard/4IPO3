from fauna import Fauna
from water import Water


class Predator(Fauna):

    def __init__(self, position):
        super().__init__(position)
        self.__prey = None

    def set_prey(self, prey):
        self.__prey = prey

    def move(self):
        w = Water.singleton()

        if abs(self.__prey.position - self.position) < 25:
            # lion court après buffle
            if self.__prey.position > self.position :
                self._position += 10
            else:
                self._position -= 10
        elif abs(w.position - self.position) <= 5:
            print(f"predator is drinking water ({self.position})")
        elif w.position < self.position:
            self._position -= 5
        else:
            self._position += 5
        print(f"predator at {self.position}")

    # @property
    # def prey_caught(self):
    #     return abs( self.position - self.__prey.position ) < 5

