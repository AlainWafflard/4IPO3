
class Banque:

    def __init__(self, name ):
        self.__name = name
        self.__compte_l = []

    def __str__(self):
        """
        banque de nom: Belfius
        compte de Kim
        compte de Sandra
        """
        out = f"""
banque de nom : {self.__name}         """
        for c in self.__compte_l:
            out += f"""
compte de {c.titulaire}            """
        return out

    def __del__(self):
        """
        compte de Kim détruit
        compte de Sandra détruit
        banque détruite
        """
        # self.__compte_l = None
        print(f"banque détruite")

    def ajouter_compte(self, name):
        self.__compte_l.append( Compte(name) )


class Compte :
    __taux_interet = 0.01

    def __init__(self, titulaire ):
        self.__titulaire = titulaire
        self.__setSolde(0)

    def __del__(self):
        print(f"compte de {self.__titulaire} détruit")

    @property
    def titulaire(self):
        return self.__titulaire

    @classmethod
    def taux_interet(cls):
        return cls.__taux_interet

    def solde(self):
        return self.__solde

    def __setSolde(self, v):
        # seul endroit où on modifie le solde
        # print("log : solde modifié à ", v)
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

    b = Banque("Belfius")
    b.ajouter_compte("Kim")
    b.ajouter_compte("Sandra")
    print(b)

    # banque de nom: Belfius
    # compte de Kim
    # compte de Sandra

    b = None

    # compte de Kim détruit
    # compte de Sandra détruit
    # banque détruite
