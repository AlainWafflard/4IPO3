from abc import ABC, abstractmethod


class JungleElement(ABC):
    __predator_l = [ "lion", "hyene", "crocodile" ]
    __prey_l = [ "buffle", "girafe", "gazelle" ]

    @classmethod
    def factory(self, animal_type, position):
        from predator import Predator
        from prey import Prey

        if animal_type in self.__predator_l :
            return Predator(position)
        if animal_type in self.__prey_l :
            return Prey(position)

    def __init__(self, position):
        self._position = position

    @property
    def position(self):
        return self._position

