class Thermometre :
	""" modélisation d'un thermomètre
		avec getter/setter implanté par décorateurs
	"""

	def __init__(self):
		self.__value_celsius = 0

	@property
	def value_celsius(self):
		# value_celsius getter via @property decorator
		return self.__value_celsius

	@value_celsius.setter
	def value_celsius(self, val):
		# value_celsius getter via @brand.setter decorator
		if val < -273.15 : val = -273.15 # aucune température ne peut descendre en dessous de -273.15
		self.__value_celsius = val


if __name__ == '__main__':
	therm_o = Thermometre()
	print(therm_o.value_celsius)
	therm_o.value_celsius = 100
	print(therm_o.value_celsius)
	therm_o.value_celsius = -200
	print(therm_o.value_celsius)
	therm_o.value_celsius = -300
	print(therm_o.value_celsius)
