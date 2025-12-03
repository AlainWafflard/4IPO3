class Archaeplastida:

    def __init__(self, position):
        self.__position = position
        self.__size = 10

    @property
    def position(self):
        return self.__position

    @property
    def size(self):
        return self.__size

    def decrease(self):
        self.__size -= 1
