# deux classes indépendantes
# on constate déjà des similitudes entre les deux classes

class Predator:
    speed = 2 # vitesse de marche "normale"

    def __init__(self, pos):
        self.position = pos
        self.prey = None

    def set_prey(self, prey):
        self.prey = prey

    def go(self):
        # le lion bouge vers le buffle
        if self.position >= self.prey.position:
            # lion à droite du buffle => aller vers la gauche
            self.position -= self.speed
        else:
            # lion à gauche  du buffle => aller vers la droite
            self.position += self.speed
        # on affiche le statut
        print("predator : " + str(self.position) )

    def prey_caught(self):
        # retourne true si la proie et le prédateur sont très proches
        if abs(self.position - self.prey.position) <= 1 :
            return True
        else:
            return False


class Prey:
    speed = 1  # vitesse de marche "normale"
    proximity_distance = 20  # distance en dessous de laquelle la proie sent le prédateur

    def __init__(self, pos):
        self.position = pos
        self.predator = None

    def set_predator(self, predator):
        self.predator = predator

    def go(self):
        if abs(self.position - self.predator.position) <= self.proximity_distance :
            # si distance predator-prey trop courte alors prey tente de s'échapper
            if self.position > self.predator.position :
                # buffle à droite du lion => filer vers la droite
                self.position += self.speed
            else:
                # buffle à gauche du lion => filer vers la gauche
                self.position -= self.speed
        else:
            # sinon prey broute de l'herbe et ne bouge pas
            pass
        # on affiche l'état
        print("prey : " + str(self.position))

    def prey_caught(self):
        # afin de pouvoir uniformiser les deux classes Prey et Predator
        # et les utiliser dans une boucle sur une liste
        return False


# MAIN
lion = Predator(0) # position 0
buffle = Prey(100) # position 100
lion.set_prey(buffle)
buffle.set_predator(lion)

animal_l = [ lion, buffle ]
while True:
    # chaque animal bouge
    for animal in animal_l: animal.go()

    # on vérifie si un animal est attrapé
    # si oui, alors on arrête le pgm
    prey_caught = False
    for animal in animal_l:
        if animal.prey_caught():
            prey_caught = True
            break
    if prey_caught:
        print("Bon appétit !")
        break

