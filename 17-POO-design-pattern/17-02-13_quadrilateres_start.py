# Exo 13-11-03 : les quadrilatères
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
    quatre_cotes_egaux = True


class Rectangle(Parallelogramme):
    quatre_angles_droits = True


class Carre(Losange, Rectangle):
    pass


forme1 = Trapeze
dump(forme1, "*** Trapèze")

forme2 = Carre
dump(forme2, "*** Carré")

forme3 = Rectangle
dump(forme3, "*** Rectangle")
