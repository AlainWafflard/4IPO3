class Thermometre :
	""" modélisation d'un thermomètre
		avec getter/setter implanté "classiquement", par des fonctions dédiées
	"""

	def __init__(self):
		self.__value_celsius = 0

	def get_value_celsius(self):
		# value_celsius getter via dedicated method
		return self.__value_celsius

	def set_value_celsius(self, val):
		# value_celsius getter via dedicated method
		if val < -273.15 : val = -273.15 # aucune température ne peut descendre en dessous de -273.15
		self.__value_celsius = val


if __name__ == '__main__':
	therm_o = Thermometre()
	print(therm_o.get_value_celsius())
	therm_o.set_value_celsius(100)
	print(therm_o.get_value_celsius())
	therm_o.set_value_celsius(-200)
	print(therm_o.get_value_celsius())
	therm_o.set_value_celsius(-300)
	print(therm_o.get_value_celsius())

