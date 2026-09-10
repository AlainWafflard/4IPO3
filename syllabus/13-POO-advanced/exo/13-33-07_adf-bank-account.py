# Association directionnelle forte
# "banque détruite => tous comptes détruits
# Attention au rôle du destructeur

class Compte:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        print("compte créé pour " + owner)

    def __str__(self):
        return "    compte de " + self.owner + "\n"

    def __del__(self):
        print("compte de " + self.owner + " détruit")


class Banque:
    def __init__(self, name):
        """ création de la banque
            attention : __account_l, la liste des comptes
            doit être une variable privée
        :param name: nom de la banque
        """
        self.__name = name
        self.__account_l = []
        print()
        print("banque créée : " + name)

    def __str__(self):
        # banque de nom : Belfius
        # compte de Kim
        # compte de Sandra
        out = "banque de nom : " + self.__name + "\n"
        for c in self.__account_l:
            out += str(c)
        return out

    def __del__(self):
        print("banque détruite")

    def ajouter_compte(self, name):
        """ création des objets Compte
            5 € sont offerts à la création
        """
        c = Compte(name, 5)
        self.__account_l.append(c)



# MAIN
b = Banque("Belfius")
b.ajouter_compte("Kim")
b.ajouter_compte("Sandra")
print(b)
# banque de nom : Belfius
# compte de Kim
# compte de Sandra

b = None
# compte de Kim détruit
# compte de Sandra détruit
# banque détruite

b = Banque("CBC")
b.ajouter_compte("Philippe")
print(b)
print("---------------------")
# banque détruite
# compte de Philippe détruit