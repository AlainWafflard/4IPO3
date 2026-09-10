# Ecrivez une fonction double_sqrt(n) qui renvoie le double de la
# racine carrée d’un nombre fourni en paramètre.
#
# Le retour de la fonction est un tuple avec deux éléments : 
#   1- True si l’opération s’est bien passée, False sinon
#   2- Le résultat du calcul
#
# Exemples:
#   double_sqrt(-1) renvoie le tuple (False, 0)
#   double_sqrt(9) renvoie le tuple (True, 6)

import math

def double_sqrt(x):
    """ La fonction double_sqrt(n) renvoie
        le double de la racine carrée
        d’un nombre fourni en paramètre.
    """
    # cas pathologique
    if x < 0 :
        return ( False, 0 )
    # cas sain
    return( True, 2 * math.sqrt(x) )

print( double_sqrt(-4) )
print( double_sqrt(4) )

