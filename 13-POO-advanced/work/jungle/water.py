class Water:

    def __init__(self, position):
        self.__position = position

    @property
    def position(self):
        return self.__position
