from predator import Predator
from prey import Prey
from water import Water
from archaeplastida import Archaeplastida

lac = Water(100)
plant = Archaeplastida(50)

lion = Predator(150, lac)
buffle = Prey(0, lac, plant)
# buffle2 = Prey(5)

lion.set_prey(buffle)
buffle.set_predator(lion)
# buffle2.set_predator(lion)

# lion.set_water(lac)
# buffle.set_water(lac)
# # buffle2.set_water(lac)
#
# buffle.set_plant(plant)
# # buffle2.set_plant(plant)

while True:
    lion.move()
    buffle.move()
    # buffle2.move()
    if abs( buffle - lion ) < 10:
        print("Bon appétit !")
        break
