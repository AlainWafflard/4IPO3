# deux classes indépendantes
# on constate déjà des similitudes entre les deux classes
# variables privées
import time


class Predator:
	__speed = 2

	def __init__(self, pos):
		self.position = pos
		self.prey = None

	@property
	def position(self):
		return self.__position

	@position.setter
	def position(self, v ):
		self.__position = v

	@property
	def prey(self):
		return self.__prey

	@prey.setter
	def prey(self, v):
		self.__prey = v

	def go(self):
		# le prédateur voit sa proie de loin et
		# s'en approche de 10 à chaque itération
		if self.prey.position - self.position > 0:
			self.position += self.__speed
		else:
			self.position -= self.__speed
		# on affiche le statut
		print("predator : {}".format(self.position))

	def prey_caught(self):
		# retourne true si la proie et le prédateur sont très proches
		if abs(self.position - self.prey.position) <= 1:
			print("predator caught prey at position {}".format(self.position))
			return True
		else:
			return False


class Prey:
	__speed = 1  # vitesse de marche "normale"
	__proximity_distance = 20  # distance en dessous de laquelle la proie sent le prédateur

	def __init__(self, pos):
		self.__position = pos
		self.__predator = None

	@property
	def position(self):
		return self.__position

	@position.setter
	def position(self, v):
		self.__position = v

	@property
	def predator(self):
		return self.__predator

	@predator.setter
	def predator(self, v):
		self.__predator = v

	def go(self):
		# la proie voit son prédateur ... quand il est trop tard
		if abs(self.position - self.predator.position) == 0:
			# la proie est capturée
			print("prey : I'm proud to be eaten by my predator ", end="")
		elif abs(self.position - self.predator.position) <= self.__proximity_distance:
			# la proie ne voit le prédateur que quand celui-ci est à moins de 20
			# la proie se met alors à fuir dans la direction opposée
			if self.position - self.predator.position > 0:
				self.position += self.__speed
			else:
				self.position -= self.__speed
		else:
			# tranquille, le prédateur est loin
			pass
		print("prey : {}".format(self.position))

	def prey_caught(self):
		# afin de pouvoir uniformiser les deux classes Prey et Predator
		# et les utiliser dans une boucle sur une liste
		return False


# MAIN
lion = Predator(0)  # position 0
buffle = Prey(100)  # position 100
lion.prey = buffle
buffle.predator = lion

animal_l = [ lion, buffle ]
while True:
	time.sleep(0.5)
	# chaque animal bouge
	for animal in animal_l: animal.go()

	# on vérifie si un animal est attrapé
    # si oui, alors on arrête le pgm
	prey_caught = False  # juste pour pouvoir sortir de la boucle
	for animal in animal_l:
		if animal.prey_caught():
			prey_caught = True
			break
	if prey_caught: break

print("Bon appétit !")
