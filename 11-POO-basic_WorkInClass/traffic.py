# Programmez un feu de signalisation
# • classe Light
# • trois états, cf image
# • pas d'aspect graphique
# • pas de constructeur
# • Output
# light color is 1
# light color is 2
# light color is 3
# light color is 1
# • Input

class Light:

    def __init__(self, color=1):
        self.color = color

    def __str__(self):
        return f"light color is {self.color}"

    def change(self):
        self.color += 1
        if self.color > 3:
            self.color = 1


if __name__ == "__main__":
    feu01 = Light(3)
    # feu01.color = 1
    print(feu01)
    feu01.change()
    print(feu01)
    feu01.change()
    print(feu01)
    feu01.change()
    print(feu01)
    feu01.change()
    print(feu01)
    feu01.change()
    print(feu01)
    feu01.change()
    print(feu01)

