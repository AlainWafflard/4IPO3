class Compte:

    def __init__(self, client_name):
        self.client_name = client_name
        self.solde = 0

    def __str__(self):
        return f" compte de {self.client_name}, solde {self.solde}"

    def __del__(self):
        print(f"compte de {self.client_name} détruit")
        self.client_name = None
        self.solde = 0


class Banque:

    def __init__(self, name):
        self.name = name
        self.compte_d =  {}

    def __del__(self):
        print('destruction des comptes')
        for k in self.compte_d.keys():
            self.compte_d[k] = None
        print(f"destruction de la banque {self.name}")

    def __str__(self):
        out = f"nom : {self.name}\n"
        for compte in self.compte_d.values():
            # out += f" compte de {compte.client_name}, solde {compte.solde}\n"
            out += str(compte) + "\n"
        return out

    def ajouter_compte(self, client_name):
        self.compte_d[client_name] = Compte(client_name)


if __name__ == "__main__" :
    b = Banque("Belfius")
    b.ajouter_compte("Kim")
    b.ajouter_compte("Sandra")
    print(b)
    # banque de nom : Belfius
    # compte de Kim
    # compte de Sandra
    b = None
    print("après None")
    # del b
    # compte de Kim détruit
    # compte de Sandra détruit
    # banque détruite
