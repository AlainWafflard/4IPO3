from predator import Predator
from prey import Prey

lion = Predator(0)
buffle = Prey(100)
lion.set_prey(buffle)
buffle.set_predator(lion)

while True:
    lion.move_to_prey()
    buffle.escape()
    if abs( buffle - lion ) < 5:
        print("Bon appétit !")
        break
