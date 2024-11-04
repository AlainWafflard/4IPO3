from calculator import CalculatorToolBox
from calculator import TextOutput

# Ecrivez le code POO en utilisant les classes Calculator_ToolBox et TextOutput.
#
# Le but est de calculer les expressions suivantes et de présenter les résultats.
# Symbôles : + - * / ... pas de problème
#            √ = racine carrée
#            ^ = puissance
# Respectez les priorités des opérateurs : ^ => * / => + -
#
# Faites les calculs exclusivement à l'aide de Calculator_ToolBox.
# Affichez le résultat exclusivement à l'aide de la classe TextOutput (cf exemple).
#
# Sous-questions par groupe :
# SQ 1 :    ( 3 + 4 ) * ( 3 + 2 )
# SQ 2 :    ( 3 + ( 5 - 2 ) ) * 2
# SQ 3 :    ( 5 * 3 ) + ( 4 * 2 )
# SQ 4 :    (15 + 8 - 3) * 2 / 5 + √49
# SQ 5 :    10 / 2 + √16 * (5 - 2) - 3^2
# SQ 6 :    (12 * 3 - 18) + (4^2 / 8) * √64
# SQ 7 :    ( ( 125 / 5 ) / 5 ) / ( ( 2 / 2 ) - 1 )
# SQ 8 :    ( 3 + 1 + 1 ) / ( 12 - ( ( 2 + 2 ) * 3 ) )
# SQ 9 :    ( 4 * 6 * 4 ) / ( ( 6 - 3 ) - ( 2 + 1 ) )
# SQ A :    (25 / 5) * √81 - (12 / 3) + 2^3
# SQ B :    (30 - 5 / 5) + (8^2 / 4) - √36
# SQ C :    ((7 * 3) + 8^2) / 4 - (2^4 / 2) + √25
# Ne répondez qu'aux sous-questions assignées (cf vos codes) !
#
# Remarques :
# - Utiliser uniquement les deux classes CalculatorToolBox et TextOutput
# - Ne pas modifier ces deux classes.
# - Une seule instance de chaque classe est créée et utilisée.
# - Ne pas utiliser directement les symbôles arithmétiques =, -, *, etc.
# - N'utliser la fonction print() que sur l'instance de TextOutput (cf exemple)
# - En cas d'addition de trois nombres, utiliser la mémoire de l'objet.
# - En cas de problème de calcul (ex: division par zéro), enclencher une exception
#   pour ne pas arrêter l'app; cf exemple ci-dessous
#   cf https://www.w3schools.com/python/python_try_except.asp

c = CalculatorToolBox()
o = TextOutput()

# Exemple 1
# Calculer et afficher le résultat de 1 + 2
tot = c.plus( 1, 2)
o.append([ "exo 1 :", 1, "+", 2, "=", tot])
print(o)

# Exemple 2
# Calculer et afficher le résultat de 10 / 0
try :
	div = c.divide( 10, 0 )
except :
	print("exo 2 : division par zéro impossible")

