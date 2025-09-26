import time


class Water:
	def __init__(self, pos):
		self.__position = pos

	@property
	def position(self):
		return self.__position


class Predator:
	__name = "predator"
	__speed = 2
	__water_distance = 50  # distance en dessous de laquelle le prédateur voit l'eau
	__proximity_distance = 20  # distance en dessous de laquelle le prédateur sent la proie

	def __init__(self, pos):
		self.position = pos
		self.prey = None
		self.water = None

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

	@property
	def water(self):
		return self.__water

	@water.setter
	def water(self, v):
		self.__water = v

	def go(self):
		# différents aspects de la vie du prédateur
		if abs(self.position - self.prey.position) < 1:
			# la proie est capturée
			self.prey_caught = True
			print(self.__name + " : prey caught ", end="")
		elif abs(self.position - self.prey.position) <= self.__proximity_distance:
			# le prédateur voit sa proie
			# quand celui-ci est à moins de 50m
			# la prédateur se met à accélérer
			if self.position > self.prey.position:
				self.position -= 3*self.__speed
			else:
				self.position += 3*self.__speed
			print(self.__name + " : miam ", end="")
		elif abs(self.position - self.water.position) <= 2:
			# la bête boit de l'eau
			self.position = self.water.position
			print(self.__name + " : glooh glooh", end="")
		elif abs(self.position - self.water.position) <= self.__water_distance:
			# le prédateur voit l'eau et s'en approche
			if self.position > self.water.position:
				self.position -= 2*self.__speed
			else:
				self.position += 2*self.__speed
			print(self.__name + " : wanna drink ", end="")
		else:
			# le prédateur avance simplement
			self.position += self.__speed
			print(self.__name + " : quiet ", end="")
		print(self.position)

	def prey_caught(self):
		# retourne true si la proie et le prédateur sont très proches
		if abs(self.position - self.prey.position) <= 1:
			print("predator caught prey at position {}".format(self.position))
			return True
		else:
			return False


class Prey:
	__name = "prey"
	__speed = 1  # vitesse de marche "normale"
	__proximity_distance = 20  # distance en dessous de laquelle la proie sent le prédateur
	__water_distance = 50  # distance en dessous de laquelle le proie voit l'eau

	def __init__(self, pos):
		self.position = pos
		self.predator = None
		self.water = None

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

	@property
	def water(self):
		return self.__water

	@water.setter
	def water(self, v):
		self.__water = v

	def go(self):
		# différents aspects de la vie de la proie
		if abs(self.position - self.__predator.position) < 1:
			# la proie est capturée
			print(self.__name + " : I'm proud to be eaten by my predator ", end="")
		elif abs(self.position - self.__predator.position) <= self.__proximity_distance:
			# la proie voit son prédateur
			# quand celui-ci est à moins de 20m
			# la proie se met alors à fuir
			if self.position > self.__predator.position:
				self.__position += 4*self.__speed
			else:
				self.__position -= 4*self.__speed
			print(self.__name + " : escaping ", end="")
		elif abs(self.position - self.water.position) <= 2:
			# la bête boit de l'eau
			self.position = self.water.position
			print(self.__name + " : glooh glooh ", end="")
		elif abs(self.position - self.water.position) <= self.__water_distance:
			# la proie voit l'eau et s'en approche
			if self.position > self.water.position:
				self.__position -= 2*self.__speed
			else:
				self.__position += 2*self.__speed
			print(self.__name + " : wanna drink ", end="")
		else:
			# la proie avance simplement
			self.__position += 1
			print(self.__name + " : quiet ", end="")
		print(self.position)

	def prey_caught(self):
		return False


# MAIN
lion = Predator(50)
buffle = Prey(20)
lac = Water(80)
lion.prey = buffle
lion.water = lac
buffle.predator = lion
buffle.water = lac

animal_l = [lion, buffle]
while True:
	time.sleep(0.5)
	for animal in animal_l:
		animal.go()

	prey_caught = False
	for animal in animal_l:
		if animal.prey_caught():
			prey_caught = True
			break
	if prey_caught: break

print("Bon appétit !")
