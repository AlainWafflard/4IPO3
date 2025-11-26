class CompteRenaissance:
	"""
	Exo 13-03-01 : le compte en banque "Renaissance"
	"""
	_type = "Compte Renaissance"

	def __init__(self, owner):
		self.owner = owner
		self.balance = 0

	def __str__(self):
		# return "owner : {}; balance : {}".format( self.owner, self.balance)
		return f"owner : {self.owner:10s} | type : {self._type} | balance : {self.balance:7.2f}"

	def deposer(self, somme):
		self.balance += somme

	def retirer(self, somme):
		if somme > self.balance:
			print("solde insuffisant")
			return
		# cas positif
		# super().retirer(somme)
		self.balance -= somme
		print(f"argent retiré ({somme:8.2f})")


if __name__ == ("__main__"):

	# MAIN
	kim_c = CompteRenaissance("Kim")
	kim_c.deposer(1000)
	print(kim_c)
	kim_c.retirer(200)
	print(kim_c)
	kim_c.retirer(1200)
	print(kim_c)
