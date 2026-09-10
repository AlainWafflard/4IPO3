import gc  # imbrication dans le code des fonctionnalités du ramasse-miettes


class MaClasse:
	monAO = None

	def __init__(self, name):
		self.name = name
		print(f"object {self.__class__.__name__} created with name {self.name} :-)")
		self.monAO = MonAutreClasse()

	def __del__(self):
		print(f"objet {self.__class__.__name__} dead.  RIP {self.name} :-(")

	def __str__(self):
		return f"{self.name}, of class {self.__class__.__name__}"


class MonAutreClasse:

	def __init__(self):
		print(f"objet {self.__class__.__name__} created :-)")

	def __del__(self):
		print(f"objet {self.__class__.__name__} dead :-(")


# MAIN
O1 = MaClasse("O1")
O2 = MaClasse("O2")
O3 = MaClasse("O3")
O4 = O3
print("", "print:", O1, O2, O3, O4, "", sep="\n")

O2 = None
O3 = None
print("", "print:", O1, O2, O3, O4, "", sep="\n")

gc.collect()
print("", "print:", O1, O2, O3, O4, "", sep="\n")
print("-------------")
# les objets O1 et O4 sont détruits quand le programme se termine 

# Scénario alternatif :
# remplacer "O2 = None" par "del O2" (idem pour O3)
# et constater la différence
