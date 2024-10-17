class Compte:

    def __init__(self, titulaire):
        self.__titulaire = titulaire
        self.__solde = -10

    def __str__(self):
        return f"compte de {self.titulaire()} : solde {self.solde()}"

    def titulaire(self):
        return self.__titulaire

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


if __name__ == "__main__":
    a = Compte("Albert")
    # a.solde = 1000
    # a.__solde = 1000
    # print(a.solde)
    # print(a.solde)
    print(a.solde())
    print(a)
    a.deposer(5000)
    print(a)
    a.retirer(1000)
    print(a)

