# encapsulation
# Classe mère : Compte
# Deux classes enfants : CompteCourant et CompteEpargne

class Compte:
	frais_retrait = 0
	_type = "Renaissance"
	__codedacces = "abcd"

	def get_codedacces(self):
		return self.__codedacces

class CompteCourant(Compte):
	_type = "Courant"
	frais_retrait = 1


class CompteEpargne(Compte):
	_type = "Epargne"
	frais_retrait = 0.5

	def get_codedacces(self):
		return self.__codedacces


# MAIN
try:
	cr = Compte()
	cc = CompteCourant()
	ce = CompteEpargne()

	print( cr.frais_retrait, cr._type )
	print( cr.get_codedacces() )

	print( cc.frais_retrait, cc._type )
	print( cc.get_codedacces() ) # OK
	# Pourquoi ça marche ?

	print( ce.frais_retrait, ce._type )
	print( ce.get_codedacces() ) # ERREUR
	# Pourquoi erreur ;-) ?

except Exception as err:
	print("ERROR : " + str(err))

