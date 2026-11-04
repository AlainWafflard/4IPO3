
class Compte :

    def __init__(self, titulaire ):
        self.__titulaire = titulaire
        self.__setSolde(0)

    def solde(self):
        return self.__solde

    def __setSolde(self, v):
        # seul endroit où on modifie le solde
        print("log : solde modifié à ", v)
        self.__solde = v

    def deposer(self, v):
        if v <= 0 :
            print("erreur : le montant déposé doit être positif")
            return
        self.__setSolde( self.solde() + v )

    def retirer(self, v):
        if v <= 0 :
            print("erreur : le montant à retirer doit être positif")
            return
        if v > self.solde():
            print("erreur : le solde est insuffisant")
            return
        self.__setSolde( self.solde() - v )




if __name__ == "__main__":

    k = Compte("Kim")
    s = Compte("Siegfried")
    print("solde=", k.solde())

    k.deposer(1000)
    print("solde=", k.solde())

    k.deposer(-500)
    print("solde=", k.solde())

    k.retirer(-200)
    k.retirer(100)
    print("solde=", k.solde())

    # k.__setSolde(10000)
    # print("solde=", k.solde())
