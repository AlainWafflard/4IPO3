class Account:

    _taux = 0.01

    def __init__(self, titulaire):
        self._titulaire = titulaire
        self._solde = 0

    def __del__(self):
        print(f"Account de {self.titulaire} détruit")

    def __str__(self):
        return f"Account de {self.titulaire} : solde {self.solde}; taux {self._taux}"

    @classmethod
    def taux(cls):
        return cls._taux

    @property
    def titulaire(self):
        return self._titulaire

    @property
    def solde(self):
        return self._solde
        # if self._solde < 0 :
        #     return 0
        # else:
        #     return self._solde

    def deposer(self,somme):
        self._solde += somme


class CompteEpargne(Account):
    _taux = 0.02

    def __str__(self):
        interest = self.solde * self._taux
        parent_str = super().__str__()
        # parent_str = Account.__str__()
        return f"{parent_str}. Intérêt : {interest}."

    def retirer(self,somme):
        if somme < self.solde:
            self._solde -= somme
        else:
            print("solde insuffisant")


class CompteCourant(Account):
    __frais_transfert = 0.5

    def retirer(self,somme):
        self._solde -= somme
        self._solde -= self.__frais_transfert

    def transferer(self, compte, somme ):
        self.retirer(somme)
        compte.deposer(somme)


# nouveau compte courant en 2025
# interdit de descendre en dessous de -1000
class CompteCourant2025(CompteCourant):
    def retirer(self,somme):
        if self._solde - somme > -1000:
            self._solde -= somme
        else:
            print("solde insuffisant")


if __name__ == "__main__":
    cca = CompteCourant("Albert")
    cca.deposer(500)
    # print(cca)
    cca.retirer(1600)
    print(cca)

    cca2025 = CompteCourant2025("Albert 2025")
    cca2025.deposer(1)
    cca2025.retirer(1500)
    print(cca2025)

    cea = CompteEpargne("Albertine")
    cea.deposer(1000)
    # print(cea)
    cea.retirer(400)
    print(cea)

    cca.transferer( cea, 750 )
    print(cca)
    print(cea)

    # cea.transferer( cca, 50 )



