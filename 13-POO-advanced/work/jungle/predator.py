class Predator:

    def __init__(self, position):
        self.__position = position
        self.__prey = None

    def __sub__(self, other):
        return self.position - other.position

    @property
    def position(self):
        return self.__position

    def set_prey(self, prey):
        self.__prey = prey

    def move_to_prey(self):
        self.__position += 10
        print(f"predator at {self.position}")

    # @property
    # def prey_caught(self):
    #     return abs( self.position - self.__prey.position ) < 5

