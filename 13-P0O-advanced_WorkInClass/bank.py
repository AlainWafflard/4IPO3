from account import *

class Bank:

    def __init__(self, name):
        self.name = name
        self.account_d = {}

    def __del__(self):
        print(f"banque {self.name} détruite")

    def __str__(self):
        out = f"banque de nom {self.name}\n"
        for name, account_o in self.account_d.items():
            # out += f" compte de {k}\n"
            out += str(account_o) + "\n"
        return out

    def ajouter_compte(self, name):
        self.account_d[name] = Account(name)
        self.account_d[name].deposer(10)

    def deposer(self, name, amount ):
        self.account_d[name].deposer(amount)


if __name__ == "__main__":
    b = Bank("Belfius")
    b.ajouter_compte("Kim")
    b.ajouter_compte("Sandra")
    b.deposer( "Kim", 100 )
    print(b) # banque de nom: Belfius, compte de Kim, compte de Sandra
    # c = b
    b = None # compte de Kim détruit, compte de Sandra détruit, banque détruite
    print("eop")
