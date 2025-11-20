class Compte:
	"""
	Exo 13-03-01 : le compte en banque "Renaissance"
	"""
	def __init__(self, owner):
		self.owner = owner
		self.balance = 0

	def deposer(self, somme):
		self.balance += somme

	def retirer(self, somme):
		self.balance -= somme

	def __str__(self):
		return "owner : {}; balance : {}".format( self.owner, self.balance)


if __name__ == ("__main__"):

	# MAIN
	kim_c = Compte("Kim")
	kim_c.deposer(1000)
	print(kim_c)
	kim_c.retirer(200)
	print(kim_c)
