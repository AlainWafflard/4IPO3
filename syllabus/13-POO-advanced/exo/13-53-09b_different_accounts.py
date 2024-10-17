# héritage hiérarchique
# Classe mère : Compte
# Deux classes enfants : CompteCourant et CompteEpargne
# le retrait d'argent suit des règles différentes

class Compte:
	_type = "Renaissance"
	_interet_crediteur = 0

	def __init__(self, owner):
		self.owner = owner
		self.balance = 0

	def deposer(self, somme):
		self.balance += somme

	def retirer(self, somme):
		if somme > self.balance :
			# solde insuffisant => retrait interdit
			print("{0} ({3}) : solde insuffisant ({1}) pour procéder à un retrait de {2}".format(self.owner, self.balance, somme, self._type ))
			return
		self.balance -= somme

	def __str__(self):
		interest = self.balance * self._interet_crediteur
		return "{} ({}) : balance : {}; interest : {}".format( self.owner, self._type, self.balance, interest)


class CompteCourant(Compte):
	__frais_retrait = 1
	_type = "CC"

	def retirer(self, somme):
		if somme > self.balance:
			print("attention, solde négatif")
		self.balance -= somme
		self.balance -= self.__frais_retrait

	def transferer(self, compteDest, somme ):
		self.retirer(somme)
		compteDest.deposer(somme)


class CompteEpargne(Compte):
	__frais_retrait = 0
	_type = "CE"
	_interet_crediteur = 0.01



# MAIN
kim_cr = Compte("Kim")
kim_cr.deposer(200)
print(kim_cr)
kim_cr.retirer(500)
print(kim_cr)

kim_cc = CompteCourant("Kim")
kim_cc.deposer(200)
print(kim_cc)
kim_cc.retirer(500)
print(kim_cc)

kim_ce = CompteEpargne("Kim")
kim_ce.deposer(200)
print(kim_ce)
kim_ce.retirer(500)
print(kim_ce)

