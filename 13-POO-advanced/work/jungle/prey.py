class Prey:

    def __init__(self, position):
        self.__position = position
        self.__predator = None

    def __sub__(self, other):
        return self.position - other.position

    @property
    def position(self):
        return self.__position

    def set_predator(self, predator):
        self.__predator = predator

    def escape(self):
        if abs(self.__position - self.__predator.position ) <= 20:
            self.__position += 5
        # else: # pas nécessaire
        print(f"prey at {self.__position}")


