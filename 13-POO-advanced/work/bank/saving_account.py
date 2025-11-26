from renaissance import CompteRenaissance


class CompteEpargne(CompteRenaissance):
    _type = "Compte Epargne"
    __taux_interet = 0.02

    def __str__(self):
        out = super().__str__()
        out +=  f" | intérêt : {self.interet}"
        return out

    @property
    def interet(self):
        return self.balance * self.__taux_interet


if __name__ == ("__main__"):

    # MAIN
    kim_c = CompteEpargne("Kim")
    kim_c.deposer(1000)
    print(kim_c)
    kim_c.retirer(200)
    print(kim_c)
    kim_c.retirer(2000)
    print(kim_c)
    # print(kim_c.interet)

