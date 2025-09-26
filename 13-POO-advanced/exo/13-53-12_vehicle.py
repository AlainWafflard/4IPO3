class Vehicle:
    seating_capacity = 4
    color = "white"

    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def __str__(self):
        return "Name: {}, Color : {}, Seats : {}".format(self.name, self.color, self.seating_capacity)


class Bus(Vehicle):
    seating_capacity = 50


modelX = Vehicle("Tesla", 180)
print(modelX)

modelBus = Bus("Volvo", 120)
print(modelBus)



