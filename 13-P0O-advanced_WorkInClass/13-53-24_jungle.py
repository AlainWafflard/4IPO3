class JungleActor:
    def __init__(self, position):
        self.position = position


class Fauna(JungleActor):
    speed = 5
    energy_max = 100
    energy_min = 0

    def __init__(self, position):
        super().__init__(position)
        self.water = None
        self.energy = 50

    def __str__(self):
        return f"{self.name} : {self.position} ({self.energy})"

    def set_water(self, water):
        self.water = water


class Predator(Fauna):
    run_speed = 15
    name = "predator"
    threshold_distance = 50

    def __init__(self, position):
        super().__init__(position)
        self.prey = None

    @property
    def prey_caught(self):
        return abs(self.position - self.prey.position) <= 10

    def set_prey(self, prey):
        self.prey = prey

    def move(self):
        # le lion bouge ...
        if abs(self.position - self.prey.position) <= self.threshold_distance and self.energy < self.energy_max:
            if self.energy > 0:
                speed = self.run_speed
                self.energy -= 5
            else:
                speed = self.speed
            if self.position < self.prey.position:
                self.position += speed
            else:
                self.position -= speed
        elif abs( self.position - self.water.position ) < 10 :
            self.energy += 1  # boire
        elif self.position < self.water.position :
            self.position += self.speed # aller vers l'eau
        elif self.position > self.water.position :
            self.position -= self.speed # aller vers l'eau


class Prey(Fauna):
    run_speed = 10
    name = "prey"
    threshold_distance = 25

    def __init__(self, position):
        super().__init__(position)
        self.predator = None
        self.food = None

    def set_predator(self, predator):
        self.predator = predator

    def set_food(self, food):
        self.food = food

    def move(self):
        if abs(self.position - self.predator.position) <= self.threshold_distance: # predator
            if self.energy > 0 :
                speed = self.run_speed
                self.energy -= 5
            else:
                speed = self.speed
            if self.position < self.predator.position:
                self.position -= speed
            else:
                self.position += speed
        elif abs(self.position - self.water.position) < 5 and self.energy < self.energy_max : # boire
            self.energy += 1
        elif abs(self.position - self.food.position) < 5 and self.energy < self.energy_max : # manger
            self.energy += 2
        elif self.position < self.water.position:
            self.position += self.speed # aller vers l'eau
        elif self.position > self.water.position:
            self.position -= self.speed # aller vers l'eau


class Resource(JungleActor):
    pass


class Water(Resource):
    pass


class Archaeplastida(Resource):
    pass


if __name__ == "__main__":
    lion = Predator(150)
    buffle = Prey(0)
    lac = Water(100)
    buisson = Archaeplastida(50)
    lion.set_prey(buffle)
    buffle.set_predator(lion)
    lion.set_water(lac)
    buffle.set_water(lac)
    buffle.set_food(buisson)
    cpt = 200
    while cpt > 0:
        lion.move()
        buffle.move()
        print( lion, buffle )
        if lion.prey_caught:
            print("Bon appétit !")
            break
        cpt -= 1
