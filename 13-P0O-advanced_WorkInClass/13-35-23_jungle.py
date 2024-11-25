class Predator:
    speed = 5
    run_speed = 15
    name = "predator"
    threshold_distance = 50

    def __init__(self, position):
        self.position = position
        # self.__prey_caught = False
        self.prey = None
        self.water = None

    def __str__(self):
        return f"{self.name} : {self.position}"

    @property
    def prey_caught(self):
        return abs(self.position - self.prey.position) <= 10

    def set_prey(self, prey):
        self.prey = prey

    def set_water(self, water):
        self.water = water

    def move(self):
        # le lion bouge ...
        if abs(self.position - self.prey.position) <= self.threshold_distance:
            if self.position < self.prey.position:
                self.position += self.run_speed
            else:
                self.position -= self.run_speed
        elif abs( self.position - self.water.position ) < self.threshold_distance :
            pass # boire
        elif self.position < self.water.position :
            self.position += self.speed # aller vers l'eau
        elif self.position > self.water.position :
            self.position -= self.speed # aller vers l'eau


class Prey:
    speed = 5
    run_speed = 10
    name = "prey"
    threshold_distance = 25

    def __init__(self, position):
        self.position = position
        # self.prey_caught = False
        self.predator = None
        self.water = None

    def __str__(self):
        return f"{self.name} : {self.position}"

    def set_predator(self, predator):
        self.predator = predator

    def set_water(self, water):
        self.water = water

    def move(self):
        if abs(self.position - self.predator.position) <= self.threshold_distance:
            if self.position < self.predator.position:
                self.position -= self.run_speed
            else:
                self.position += self.run_speed
        elif abs(self.position - self.water.position) < 5:
            pass    # boire
        elif self.position < self.water.position:
            self.position += self.speed # aller vers l'eau
        elif self.position > self.water.position:
            self.position -= self.speed # aller vers l'eau


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
        print( lion, buffle )
        if lion.prey_caught:
            print("Bon appétit !")
            break
