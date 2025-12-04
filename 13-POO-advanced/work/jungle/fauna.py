from abc import ABC, abstractmethod
from jungle_element import JungleElement


class Fauna(ABC, JungleElement):

    def __init__(self, position, water):
        super().__init__(position)
        self._water = water

    def __sub__(self, other):
        return self.position - other.position

    @abstractmethod
    def move(self):
        pass

