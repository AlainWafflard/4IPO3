class Compte:

	def __init__(self, owner):
		self.owner = owner
		self.balance = 0

	def deposer(self, somme):
		self.balance += somme

	def retirer(self, somme):
		self.balance -= somme

	def __str__(self):
		return "owner : {}; balance : {}".format( self.owner, self.balance)


class CompteCourant(Compte):

	def transferer(self, compteDest, somme ):
		self.retirer(somme)
		compteDest.deposer(somme)


# MAIN
kim_c = CompteCourant("Kim")
kim_c.deposer(1000)
print(kim_c)

clijster_c = Compte("Clijster")
print(clijster_c)

kim_c.transferer(clijster_c, 150)
kim_c.transferer(clijster_c, 150)
kim_c.retirer(200)
clijster_c.retirer(100)

print(kim_c)
print(clijster_c)
