# class abstraite mère : Compte
# Deux classes enfants : CompteCourant et CompteEpargne
from abc import ABC, abstractmethod


class Compte(ABC):
	_type = ""

	def __init__(self, owner):
		self.owner = owner
		self.balance = 0

	def deposer(self, somme):
		self.balance += somme

	@abstractmethod
	def retirer(self, somme):
		self.balance -= somme

	def __str__(self):
		return "{0} ({2}) : solde de {1}".format( self.owner, self.balance, self._type)


class CompteCourant(Compte):
	__frais_retrait = 1
	_type = "CC"

	def retirer(self, somme):
		super().retirer(somme + self.__frais_retrait)
		if self.balance < 0 :
			# compte en négatif => on prévient le client
			print("{0} ({2}) : solde négatif ({1}), attention aux intérêts débiteurs".format(self.owner, self.balance, self._type ))

	def transferer(self, compteDest, somme ):
		self.retirer(somme)
		compteDest.deposer(somme)


class CompteEpargne(Compte):
	__frais_retrait = 0
	_type = "CE"

	def retirer(self, somme):
		if somme > self.balance :
			# solde insuffisant => retrait interdit
			print("{0} ({3}) : solde insuffisant ({1}) pour procéder à un retrait de {2}".format(self.owner, self.balance, somme, self._type ))
			return
		super().retirer(somme)


# MAIN
try:
	kim_cr = Compte("Kim")
except Exception as err:
	print("ERROR : " + str(err))


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

