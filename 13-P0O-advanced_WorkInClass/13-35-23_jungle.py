class Predator:
    speed = 10
    name = "predator"

    def __init__(self, position):
        self.position = position
        # self.__prey_caught = False
        self.prey = None
        self.water = None

    @property
    def prey_caught(self):
        return abs(self.position - self.prey.position) < 2

    def set_prey(self, prey):
        self.prey = prey

    def set_water(self, water):
        self.water = water

    def move(self):
        # le lion bouge ...
        if abs( self.position - self.water.position ) < 2 :
            pass
        elif self.position < self.water.position :
            self.position += self.speed
        elif self.position > self.water.position :
            self.position -= self.speed

        print(f"{self.name} : {self.position}")


class Prey:
    speed = 5
    name = "prey"

    def __init__(self, position):
        self.position = position
        # self.prey_caught = False
        self.predator = None
        self.water = None

    def set_predator(self, predator):
        self.predator = predator

    def set_water(self, water):
        self.water = water

    def move(self):
        if abs(self.position - self.predator.position) <= 20:
            if self.position < self.predator.position:
                self.position -= self.speed
            else:
                self.position += self.speed
        elif abs(self.position - self.water.position) < 2:
            pass    # boire
        elif self.position < self.water.position:
            self.position += self.speed # aller vers l'eau
        elif self.position > self.water.position:
            self.position -= self.speed # aller vers l'eau

        print(f"{self.name} : {self.position}")


class Water:
    def __init__(self, position):
        self.position = position


if __name__ == "__main__":
    lion = Predator(0)
    buffle = Prey(100)
    lac = Water(150)
    lion.set_prey(buffle)
    buffle.set_predator(lion)
    lion.set_water(lac)
    buffle.set_water(lac)
    while True:
        lion.move()
        buffle.move()
        if lion.prey_caught:
            print("Bon appétit !")
            break
