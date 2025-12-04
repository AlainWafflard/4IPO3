from renaissance import CompteRenaissance


class CompteEpargne(CompteRenaissance):
    _type = "Compte Epargne"
    __taux_interet = 0.02

    def __init__(self, owner):
        super().__init__(owner)

    def retirer(self, somme):
        super().retirer(somme)

    def deposer(self, somme):
        super().deposer(somme)

    def __str__(self):
        out = super().__str__()
        out +=  f" | intérêt : {self.interet}"
        return out

    @property
    def interet(self):
        return self.balance * self.__taux_interet

#
# if __name__ == ("__main__"):
#
#     # MAIN
#
