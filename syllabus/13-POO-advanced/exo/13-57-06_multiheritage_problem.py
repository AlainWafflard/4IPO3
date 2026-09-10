# Exo 13-11-06 : les quadrilatères
# Cet exo montre un problème avec l'héritage multiple
# Quand le même attribut ou la même méthode est définie dans chacune des classes parentes
#
# from pprint import pprint
from inspect import getmembers
from types import FunctionType

def dump(obj, title=""):
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
	print(title)
	for k in attr_l:
		print(k, ":", attr_l[k])


class Quadrilatere:
	quatre_cotes = True


class Trapeze(Quadrilatere):
    deux_cotes_paralleles = True


class Parallelogramme(Trapeze):
    deux_autres_cotes_paralleles = True


class Losange(Parallelogramme):
	""" attribut "name" défini dans les deux classes Losange et Rectangle	"""
	name = "Losange"
	quatre_cotes_egaux = True


class Rectangle(Parallelogramme):
	""" attribut "name" défini dans les deux classes Losange et Rectangle	"""
	name = "Rectangle"
	quatre_angles_droits = True


class Carre(Losange, Rectangle):
    pass


forme1 = Trapeze
dump(forme1, "*** Trapèze")

forme2 = Carre
dump(forme2, "*** Carré")
# On constate que le Carré a pour nom "losange" car c'est la première classe donnée comme parent
# dans l'expression "class Carre(Losange, Rectangle)"
# Le lecteur est invité à modifier le code comme suit :
# 	class Carre(Rectangle, Losange):
#	    pass
# avec Rectangle en premier lieu
# et de constater l'impact sur le dump


