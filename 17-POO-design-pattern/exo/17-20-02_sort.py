from abc import ABC, abstractmethod


class SortStrategy(ABC):
    @classmethod
    @abstractmethod
    def trier(self, data):
        pass


class TriAlphaDirect(SortStrategy):
    @classmethod
    def trier(self, data):
        return sorted(data)


class TriAlphaInverse(SortStrategy):
    @classmethod
    def trier(self, data):
        return sorted(data, reverse=True)


class SortContext:
    __tri_d = {
        "alpha-direct" : TriAlphaDirect,
        "alpha-inverse" : TriAlphaInverse,
    }

    def __init__(self):
        self.__strategy = None

    def set_strategy(self, strategy_name):
        self.__strategy = self.__tri_d[strategy_name]

    def sort(self, data):
        return self.__strategy.trier(data)


if __name__ == "__main__":
    mylist = [5, 2, 8, 1, 3]
    contexte = SortContext()

    # Utilisation du tri direct
    contexte.set_strategy("alpha-direct")
    print( "Tri direct appliqué :", contexte.sort(mylist) )

    # Changement dynamique de stratégie : utilisation du tri inverse
    contexte.set_strategy("alpha-inverse")
    print("Tri inverse appliqué :", contexte.sort(mylist))

