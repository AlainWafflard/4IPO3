from fauna import Fauna


class Prey(Fauna):

    def __init__(self, position, water, plant):
        super().__init__(position, water)
        self.__predator = None
        self.__plant = plant

    def set_predator(self, predator):
        self.__predator = predator

    # def set_plant(self, plant):
    #     self.__plant = plant

    def move(self):
        if abs(self._position - self.__predator.position ) <= 20:
            if self.__predator.position > self.position :
                self._position -= 7
            else:
                self._position += 7
        elif abs(self._water.position - self.position) <= 5:
            print(f"prey is drinking water ({self.position})")

        elif abs(self.__plant.position - self.position) <= 5 and self.__plant.size > 0 :
            self.__plant.decrease()
            print(f"prey is eating plan ({self.position})")

        elif self._water.position < self.position:
            self._position -= 5
        else:
            self._position += 5
        # else: # pas nécessaire
        print(f"prey at {self._position}")


