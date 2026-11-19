
class Compte :
    __taux_interet = 0.01

    def __init__(self, titulaire ):
        self.__titulaire = titulaire
        self.__setSolde(0)

    @classmethod
    def taux_interet(cls):
        return cls.__taux_interet

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

    print("taux d'intéret :", Compte.taux_interet())

    k = Compte("Kim")
    print("taux d'intéret k :", k.taux_interet())

    s = Compte("Siegfried")
    # print("solde=", k.solde())
    #
    # k.deposer(1000)
    # print("solde=", k.solde())
    #
    # k.deposer(-500)
    # print("solde=", k.solde())
    #
    # k.retirer(-200)
    # k.retirer(100)
    # print("solde=", k.solde())

    # k.__setSolde(10000)
    # print("solde=", k.solde())
    print("taux d'intéret :", k.taux_interet())
    print("taux d'intéret :", s.taux_interet())

    # Compte.taux_interet = 0.05 # pédagogique uniquement
    print("taux d'intéret classe :", Compte.taux_interet())
    print("taux d'intéret k :", k.taux_interet())
    print("taux d'intéret s :", s.taux_interet())

    # k.taux_interet = 0.10
    print("taux d'intéret classe :", Compte.taux_interet())
    print("taux d'intéret k :", k.taux_interet())
    print("taux d'intéret s :", s.taux_interet())

