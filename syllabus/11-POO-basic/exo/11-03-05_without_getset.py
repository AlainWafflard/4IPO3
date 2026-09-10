class Thermometre :
	""" modélisation d'un thermomètre
		sans getter/setter
		=> aucun test ne peut être fait sur les attributs
		   qui sont en fait publics
	"""

	def __init__(self):
		self.value_celsius = 0


if __name__ == '__main__':
	therm_o = Thermometre()
	print(therm_o.value_celsius)
	therm_o.value_celsius = 100
	print(therm_o.value_celsius)
	therm_o.value_celsius = -200
	print(therm_o.value_celsius)
	therm_o.value_celsius = -300  # bug : valeur acceptée
	print(therm_o.value_celsius)
