class Vehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def __str__(self):
        return "Name: {}, Speed: {}".format(self.name, self.max_speed)


class Bus(Vehicle):
    pass


modelX = Vehicle("Tesla", 180)
print(modelX)

modelBus = Bus("Volvo", 120)
print(modelBus)



