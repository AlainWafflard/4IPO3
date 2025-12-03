from predator import Predator
from prey import Prey
from water import Water
from archaeplastida import Archaeplastida

lion = Predator(150)
buffle = Prey(0)
buffle2 = Prey(5)

lion.set_prey(buffle)
buffle.set_predator(lion)
buffle2.set_predator(lion)

lac = Water(100)
lion.set_water(lac)
buffle.set_water(lac)
buffle2.set_water(lac)

plant = Archaeplastida(50)
buffle.set_plant(plant)
buffle2.set_plant(plant)

while True:
    lion.move()
    buffle.move()
    buffle2.move()
    if abs( buffle - lion ) < 10:
        print("Bon appétit !")
        break
