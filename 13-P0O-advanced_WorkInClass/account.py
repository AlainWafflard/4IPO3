class Account:

    _taux = 0.01

    def __init__(self, titulaire):
        self.__titulaire = titulaire
        self.__solde = 0

    def __del__(self):
        print(f"Account de {self.titulaire} détruit")

    def __str__(self):
        return f"Account de {self.titulaire} : solde {self.solde}; taux {self._taux}"

    @classmethod
    def taux(cls):
        return cls.__taux

    @classmethod
    def set_taux(cls, val):
        cls.__taux = val

    @property
    def titulaire(self):
        return self.__titulaire

    @property
    def solde(self):
        if self.__solde < 0 :
            return 0
        else:
            return self.__solde

    def deposer(self,somme):
        self.__solde += somme

    def retirer(self,somme):
        if somme < self.solde():
            self.__solde -= somme
        else:
            print("solde insuffisant")


class CompteEpargne(Account):
    _taux = 0.02


if __name__ == "__main__":
    a = Account("Albert")
    print(a)

    b = CompteEpargne("Bill")
    print(b)

    # Account.set_taux(0.05)
    # a = Account("Albert")
    # b = Account("Bernard")
    # print(a)
    # print(b)
    # Account.set_taux(0.03)
    # print(a)
    # print(b)
    # # a.set_taux(0.02)
    # print(a)
    # print(b)
    # Account.set_taux(0.04)
    # print(a)
    # print(b)

    # a.solde = 1000
    # a.__solde = 1000
    # print(a.solde)
    # print(a.solde)
    # print(a.solde())
    # print(a)
    # a.deposer(5000)
    # print(a)
    # a.retirer(1000)
    # print(a)

