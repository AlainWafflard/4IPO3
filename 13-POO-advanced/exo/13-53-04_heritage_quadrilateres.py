# Exo 13-11-03 : les quadrilatères
# from pprint import pprint
from inspect import getmembers
from types import FunctionType


def dump(obj):
	""" imprime tous les attributs publics
	    https://stackoverflow.com/questions/192109/is-there-a-built-in-function-to-print-all-the-current-properties-and-values-of-a
	"""
	disallowed_names = {
		name for name, value in getmembers(type(obj))
		if isinstance(value, FunctionType)
	}
	attr_l =  {
		name: getattr(obj, name) for name in dir(obj)
		if name[0] != '_' and name not in disallowed_names and hasattr(obj, name)
	}
	print()
	# print(title)
	print("*** " + attr_l["name"])
	for k in attr_l:
		print(k, ":", attr_l[k])


class Quadrilatere:
	name = "Quadrilatère"
	quatre_cotes = True


class Trapeze(Quadrilatere):
	name = "Trapèze"
	deux_cotes_paralleles = True


class Parallelogram(Trapeze):
	name = "Parallélogramme"
	deux_autres_cotes_paralleles = True


class Losange(Parallelogram):
	name = "Losange"
	quatre_cotes_egaux = True


class Rectangle(Parallelogram):
	name = "Rectangle"
	quatre_angles_droits = True


dump(Quadrilatere)
dump(Trapeze)
dump(Parallelogram)
dump(Losange)
dump(Rectangle)


