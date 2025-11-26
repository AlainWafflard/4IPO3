from renaissance import CompteRenaissance


class CompteCourant(CompteRenaissance):
	_type = "Compte Courant"

	__frais_retrait = 0.05
	__limite_retrait = -1000

	def __init__(self, owner):
		super().__init__(owner)
		# reste du code du constructeur ...

	def retirer(self, somme):
		if not self.__check_balance(somme):
			# cas alternatif
			print("solde insuffisant")
			return
		# cas positif
		super().retirer(somme)
		self.balance -= self.__frais_retrait
		print(f"argent retiré ({somme:8.2f})")

	def transferer(self, compteDest, somme ):
		if not self.__check_balance(somme) :
			# cas alternatif
			print("solde insuffisant")
			return
		# cas positif
		self.retirer(somme)
		compteDest.deposer(somme)
		print(f"transfert réussi ({somme:8.2f})")

	def __check_balance(self, somme):
		return self.balance - somme > self.__limite_retrait


if __name__ == ("__main__"):
	# MAIN
	kim_c = CompteCourant("Kim")
	kim_c.deposer(1000)
	print(kim_c)

	clijster_c = CompteCourant("Clijster")
	print(clijster_c)

	kim_c.transferer(clijster_c, 500)
	kim_c.retirer(200)
	kim_c.transferer(clijster_c, 800)
	kim_c.transferer(clijster_c, 1000)
	clijster_c.retirer(2500)
	clijster_c.transferer(kim_c, 50)

	print(kim_c)
	print(clijster_c)
