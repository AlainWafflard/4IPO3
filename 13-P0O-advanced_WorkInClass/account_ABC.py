from abc import ABC, abstractmethod


class Account(ABC):
    _taux = 0.01

    def __init__(self, titulaire):
        self._titulaire = titulaire
        self._solde = 0

    # def __del__(self):
    #     print(f"Account de {self.titulaire} détruit")

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

    @abstractmethod
    def deposer(self,somme):
        pass

    @abstractmethod
    def retirer(self,somme):
        pass


class CompteEpargne(Account):
    _taux = 0.02

    def __str__(self):
        interest = self.solde * self._taux
        parent_str = super().__str__()
        # parent_str = Account.__str__()
        return f"{parent_str}. Intérêt : {interest}."

    def deposer(self,somme):
        self._solde += somme

    def retirer(self,somme):
        if somme < self.solde:
            self._solde -= somme
        else:
            print("solde insuffisant")


class CompteEnfant(Account):
    _taux = 0.01

    def deposer(self,somme):
        self._solde += somme

    def retirer(self,somme):
        print("retrait interdit")


class CompteCourant(Account):
    __frais_transfert = 0.5

    def deposer(self,somme):
        self._solde += somme
        self._solde -= self.__frais_transfert

    def retirer(self,somme):
        self._solde -= somme
        self._solde -= self.__frais_transfert

    def transferer(self, compte, somme ):
        self.retirer(somme)
        compte.deposer(somme)


# nouveau compte courant en 2025
# interdit de descendre en dessous de -1000
class CompteCourant2025(Account):
    __frais_transfert = 0.5

    def deposer(self,somme):
        self._solde += somme
        self._solde -= self.__frais_transfert

    def retirer(self,somme):
        if self._solde - somme > -1000:
            super().retirer(somme)
        else:
            print("solde insuffisant")


if __name__ == "__main__":
    cca = CompteCourant("Albert")
    cca.deposer(500)
    # print(cca)
    cca.retirer(100)
    print(cca)

    cca2025 = CompteCourant2025("Albert 2025")
    cca2025.deposer(500)
    cca2025.retirer(100)
    cca2025.retirer(2000)
    print(cca2025)

    # cold = Account("Jacques")
    # cold.deposer(100)
    # print(cold)

    cchild = CompteEnfant("Hubert")
    cchild.deposer(500)
    cchild.retirer(100)
    print(cchild)


