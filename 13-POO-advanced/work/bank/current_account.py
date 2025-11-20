from renaissance import Compte


class CompteCourant(Compte):
	__frais_retrait = 0.05

	def retirer(self, somme):
		# self.balance -= somme
		super().retirer(somme)
		self.balance -= self.__frais_retrait

	def transferer(self, compteDest, somme ):
		if somme <= self.balance:
			self.retirer(somme)
			compteDest.deposer(somme)
			print("transfert réussi")
		else:
			print("solde insuffisant")


if __name__ == ("__main__"):
	# MAIN
	kim_c = CompteCourant("Kim")
	kim_c.deposer(1000)
	print(kim_c)

	clijster_c = CompteCourant("Clijster")
	print(clijster_c)

	kim_c.transferer(clijster_c, 150)
	kim_c.transferer(clijster_c, 150)
	kim_c.retirer(200)
	kim_c.transferer(clijster_c, 800)
	clijster_c.retirer(100)

	print(kim_c)
	print(clijster_c)
