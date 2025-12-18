from fauna import Fauna
from water import Water
from archaeplastida import Archaeplastida

class Prey(Fauna):

    def __init__(self, position):
        super().__init__(position)
        self.__predator = None
        # self.__plant = plant

    def set_predator(self, predator):
        self.__predator = predator

    # def set_plant(self, plant):
    #     self.__plant = plant

    def move(self):
        w = Water.singleton()
        p = Archaeplastida.singleton()

        if abs(self._position - self.__predator.position ) <= 20:
            if self.__predator.position > self.position :
                self._position -= 7
            else:
                self._position += 7
        elif abs(w.position - self.position) <= 5:
            print(f"prey is drinking water ({self.position})")

        elif abs(p.position - self.position) <= 5 and p.size > 0 :
            p.decrease()
            print(f"prey is eating plan ({self.position})")

        elif w.position < self.position:
            self._position -= 5
        else:
            self._position += 5
        # else: # pas nécessaire
        print(f"prey at {self._position}")


