# cf diagramme de classe UML ci-contre
# implémenter cette classe en Python, en privatisant les attributs.
class Date:
    # noms des mois définis comme attribut de classe à l’aide d’une liste
    __liste_des_mois = [ "", "janvier", "février", "mars " ]

    def __init__(self, j, m , a):
        """
        prévoir un dispositif pour éviter les dates impossibles (du genre 32/14/2020)
        Génération d’une erreur : instruction raise
        :param j:
        :param m:
        :param a:
        """
        self.year = a
        self.month = m
        self.day = j

    @classmethod
    @property
    def liste_des_mois(cls):
        return cls.__liste_des_mois

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, v ):
        self.__year = v

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, m ):
        if m < 1 or m > 12:
            raise Exception("mois incorrect : nombre de 1 à 12 inclus")
        self.__month = m

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, j ):
        if j < 1 or j > 31:
            raise Exception("jour incorrect : nombre de 1 à 31 inclus")
        self.__day = j

    def __repr__(self):
        out = "{} {} {}"
        mois = self.liste_des_mois[self.month]
        return out.format( self.day, mois, self.year)

    def __lt__(self, other) -> bool:
        """
        méthode __lt__()
        comparer deux dates
        d1 < d2 renvoie True ou False
        :param other:
        :return: boolean
        """
        if self.year < other.year :
            return True
        elif self.year > other.year :
            return False
        else:
            # == des années
            if self.month < other.month :
                return True
            elif self.month > other.month :
                return False
            else :
                # == des mois
                if self.day < other.day :
                    return True
                elif self.day > other.day :
                    return False
                else :
                    # == des jours
                    return False


date1 = Date( 12, 2, 2020 )
date2 = Date( 1, 1, 2022 )
print(repr(date1), "\n", repr(date2), "\n", date1 < date2 )

date3 = Date( 2, 1, 2022 )
print(repr(date3), "\n", repr(date2), "\n", date3 < date2 )
print( date1 < date1 )
