# implémenter cette classe en Python, en privatisant les attributs.
# constructeur :
# prévoir un dispositif pour éviter les dates impossibles (du genre 32/14/2020)
# Génération d’une erreur : instruction raise
# méthode __str__()
# afficher la date sous la forme "25 janvier 2023"
# noms des mois définis comme attribut de classe à l’aide d’une liste
# Méthode __repr__()
# afficher la date sous la forme "20230125"
# méthode __lt__()
# comparer deux dates
# d1 < d2 renvoie True ou False
# Référence : https://info.blaisepascal.fr/nsi-exercices-poo

class Date:
    __nom_des_mois  = {
        10 : "octobre",
        11 : "novembre",
        12 : "décembre",
    }

    def __init__(self, jour, mois, annee ):
        self.jour = jour
        self.mois = mois
        self.annee = annee

    def __str__(self):
        """ # afficher la date sous la forme "25 janvier 2023" """
        return f"{self.jour} {self.__nom_des_mois[self.mois]} {self.annee}"

    def __repr__(self):
        return f"{self.annee}{self.mois:02d}{self.jour:02d}"

    def __lt__(self, other):
        if self.annee < other.annee : return True
        if self.annee > other.annee : return False
        if self.mois < other.mois : return True
        if self.mois > other.mois : return False
        if self.jour < other.jour : return True
        if self.jour >= other.jour : return False
 
    def __eq__(self, other):
        return ( self.annee == other.annee and self.mois == other.mois and self.jour == other.jour )

        # __ge__  >=
        # __le__  <=
        # __gt__ >
        # __eq__ ==
        # __ne__ !=

    @property
    def jour(self):
        return self.__jour

    @jour.setter
    def jour(self, val):
        if val < 0 or val > 31 :
            raise Exception("numéro de jour impossible, doit être compris entre de 0 à 31")
        self.__jour = val

    @property
    def mois(self):
        return self.__mois

    @mois.setter
    def mois(self, val):
        if val < 0 or val > 12 :
            raise Exception("numéro de mois impossible, doit être compris entre de 0 à 12")
        self.__mois = val

    @property
    def annee(self):
        return self.__annee

    @annee.setter
    def annee(self, val):
        if val < 300 :
            raise Exception("année impossible, doit être supérieure à 300")
        self.__annee = val


if __name__ == "__main__":
    d1 = Date( 7, 11, 2024)
    print(d1)
    print( repr(d1) )

    try:
        d2 = Date( 30, 12, 250 )
        print(d2)
        print( repr(d2) )
    except Exception as e:
        print( "Exception:", e)

    d3 = Date( 6, 11, 2024)
    print(d1 < d3)  # False
    d4 = Date( 30, 11, 2024)
    d5 = Date( 30, 11, 2024)
    d6 = Date( 30, 1, 2024)
    print(d1 < d4)  # True

    ld = [ d1, d3, d4, d6 ]
    ld.sort()
    print(ld)
    print( d4 == d5 )
    print( d4 == d1 )

