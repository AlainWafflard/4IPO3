class Vehicle:
    seating_capacity = 4
    color = "white"

    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def __str__(self):
        return "Name: {}, Tarif : {}".format(self.name, self.fare() )

    def fare(self):
        return self.seating_capacity * 50


class Bus(Vehicle):
    seating_capacity = 50

    def fare(self):
        return self.seating_capacity * 50 * 1.10


modelX = Vehicle("Tesla", 180)
print(modelX)

modelBus = Bus("Volvo", 120)
print(modelBus)



