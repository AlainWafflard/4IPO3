import time


class Resource:
	_quantity = 0

	def __init__(self, pos):
		self.__position = pos

	@property
	def position(self):
		return self.__position

	def __str__(self):
		return "{}: level {}".format( type(self).__name__, self._quantity)


class Water(Resource):
	__instance = None
	_quantity = 1000

	@staticmethod
	def singleton():
		if Water.__instance is None:
			Water.__instance = Water(100)
		return Water.__instance

	def __init__(self, pos):
		if Water.__instance is not None:
			raise Exception("Water is a singleton!")
		# Sequel of the constructor
		super().__init__(pos)

	def decrease(self):
		self._quantity -= 25
		print(self)


class Archaeplastida(Resource):
	__instance = None
	_quantity = 1000

	@staticmethod
	def singleton():
		if Archaeplastida.__instance is None:
			Archaeplastida.__instance = Archaeplastida(50)
		return Archaeplastida.__instance

	def __init__(self, pos):
		if Archaeplastida.__instance is not None:
			raise Exception("Archaeplastida is a singleton!")
		# Sequel of the constructor
		super().__init__(pos)

	def decrease(self):
		self._quantity -= 50
		print(self)


class Fauna:
	__str_base = "{}: {}, pos {}, energy {}"
	_name = ""

	def __init__(self, pos):
		self._position = pos
		self._water = Water.singleton()
		# self._food = Archaeplastida.singleton()
		self._food = None
		self._energy = 100
		self._speed = +1
		self._action = ""

	@property
	def position(self):
		return self._position

	# def set_water(self, w):
	# 	self._water = w

	def __str__(self):
		return self.__str_base.format(self._name, self._action, self._position, self._energy)


class Predator(Fauna):
	_name = "Lion"
	prey_caught = False

	# def __init__(self, pos):
	# 	super().__init__(pos)

	def set_food(self, f):
		self._food = f

	def go(self):
		# différents aspects de la vie du prédateur
		if abs(self.position - self._food.position) < 1 :
			# la proie est capturée
			self.prey_caught = True
			self._energy += 50
			self._action = "miam miam"
		elif abs(self.position - self._food.position) <= 50:
			# le prédateur voit sa proie
			# quand il est à moins de 50m, il accélère
			# if self.position > self.__prey.position :
			# 	self.__position -= 6 * self.__speed
			# else:
			self._position += 6 * self._speed
			self._energy -= 6
			self._action = "gonna eat"
		elif abs(self.position - self._water.position) <= 1 and self._energy < 100 :
			# la bête boit de l'eau
			self._energy += 1
			self._water.decrease()
			self._action = "glooh glooh"
		elif abs(self.position - self._water.position) <= 25 and self._energy < 100 :
			# le prédateur voit l'eau et s'en approche
			if self._position > self._water.position :
				self._position -= 2 * self._speed
			else:
				self._position += 2 * self._speed
			self._energy -= 2
			self._action = "gonna drink"
		else:
			# la proie circule simplement entre 0 et 200
			# par défaut, elle se rapproche de 100
			if self._position >= 100 :
				self._speed = -1
			else:
				self._speed = +1
			self._position += self._speed
			self._energy -= 1
			self._action = "quiet"
		print(self)
		# print("{}: {}, pos {}, energy {}".format(self.name, self._action, self.__position, self._energy))


class Prey(Fauna):
	_name = "Buffle"
	alive = True

	def __init__(self, pos):
		super().__init__(pos)
		self.__predator = None
		self._food = Archaeplastida.singleton()

	def set_predator(self, predator):
		self.__predator = predator

	def go(self):
		# différents aspects de la vie de la proie
		if abs(self._position - self.__predator.position) <= 1 :
			# la proie est capturée
			self.alive = False
			self._action = "proud to be eaten by my predator "
		elif abs(self._position - self.__predator.position) <= 25 :
			# la proie voit son prédateur
			# quand celui-ci est à moins de 20m
			# la proie se met alors à fuir
			if self.position > self.__predator.position :
				self._position += 4 * self._speed
			else:
				self._position -= 4 * self._speed
			self._energy -= 4
			self._action = "escaping"
		elif abs(self.position - self._water.position) <= 1 and self._energy < 100:
			# la bête boit de l'eau
			self._energy += 25
			self._water.decrease()
			self._action = "glooh glooh"
		elif abs(self.position - self._water.position) <= 25 and self._energy < 100:
			# la proie voit l'eau et s'en approche
			self._position += 2 * self._speed
			self._energy -= 2
			self._action = "gonna drink"
		elif abs(self.position - self._food.position) <= 1 and self._energy < 100:
			# la bête mange la plante
			self._energy += 50
			self._food.decrease()
			self._action = "miam miam"
		elif abs(self.position - self._food.position) <= 25 and self._energy < 100:
			# la proie voit la plante et s'en approche
			self._position += 2 * self._speed
			self._energy -= 2
			self._action = "gonna eat"
		else:
			# la proie avance simplement
			if self._position >= 200 :
				self._speed = -1
			elif self._position < 0 :
				self._speed = +1
			self._position += self._speed
			self._energy -= 1
			self._action = "quiet"
		# print("{}: {}, pos {}, energy {}".format(self.name, self._action, self.__position, self._energy))
		print(self)


# MAIN
if __name__ == "__main__" :
	lion = Predator(150)
	buffle = Prey(95)
	# lac = Water(100)
	# buisson = Archaeplastida(50)

	lion.set_food(buffle)
	# lion.set_water(lac)
	buffle.set_predator(lion)
	# buffle.set_water(lac)
	# buffle.set_food(buisson)

	continue_condition = True
	while continue_condition:
		time.sleep(0.5)
		buffle.go()
		lion.go()
		continue_condition = ( not lion.prey_caught ) and buffle.alive

	print("Bon appétit, cher lion !")
	print(Water.singleton())
	print(Archaeplastida.singleton())


