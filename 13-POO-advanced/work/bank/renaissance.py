from abc import ABC, abstractmethod, abstractproperty


class CompteRenaissance(ABC):
	"""
	Exo 13-03-01 : le compte en banque "Renaissance"
	"""
	_type = "Compte Renaissance"

	@abstractmethod
	def __init__(self, owner):
		self.owner = owner
		self.balance = 0

	def __str__(self):
		# return "owner : {}; balance : {}".format( self.owner, self.balance)
		return f"owner : {self.owner:10s} | type : {self._type} | balance : {self.balance:7.2f}"

	@abstractmethod
	def deposer(self, somme):
		self.balance += somme

	@abstractmethod
	def retirer(self, somme):
		if somme > self.balance:
			print("solde insuffisant")
			return
		# cas positif
		# super().retirer(somme)
		self.balance -= somme
		print(f"argent retiré ({somme:8.2f})")

#
# if __name__ == ("__main__"):
#
# 	# MAIN
