from car import Car
from light import Light

voiture_A = Car("Peugeot")
feu01 = Light(voiture_A)
print(feu01)
print(voiture_A)
for i in range(4):
    feu01.change()
    print(feu01)
    print(voiture_A)
