# Ecrivez une classe « Stock » qui gère le stock d’une entreprise.
# En pratique, cette classe gère :
# stock de papier (bloc de 500 feuilles) : 20 actuellement
# stock de crayons : 8 actuellement
# tous ces attributs sont privés.
# Un « seuil de recommande » est défini, en dessous duquel une recommande est nécessaire :
# Papier : 2 blocs
# Crayons : 1
# Ecrivez les méthodes permettant les actions suivantes
# Connaître la valeur du stock
# Retirer un élément du stock, tant que celui-ci le permet.
# Si la valeur du stock est inférieure ou égale au seuil, alors un message est envoyé à l’utilisateur lui demandant une recommande.


class Stock:

    def __init__(self, papier=0, crayon=0 ):
        self.papier = papier
        self.crayon = crayon

    def __str__(self):
        return f"""
        stock : papier = {self.papier} ; crayon = {self.crayon} 
        """

    def seuil_de_recommande(self,  papier=0, crayon=0 ):
        self.seuil_papier = papier
        self.seuil_crayon = crayon

    def retirer(self, papier=0, crayon=0 ):
        if papier < self.papier:
            self.papier -= papier
        if crayon < self.crayon:
            self.crayon -= crayon
        print(self.valeur())

    def valeur(self):
        recom_papier = self.papier <= self.seuil_papier
        recom_crayon = self.crayon <= self.seuil_crayon

        return f"""
        produit / stock / seuil / recommande ? 
        papier / {self.papier} / {self.seuil_papier} / {recom_papier}
        crayon / {self.crayon} / {self.seuil_crayon} / {recom_crayon}
        """


if __name__ == "__main__":
    stock = Stock( papier=20, crayon=8 )
    stock.seuil_de_recommande(papier=2, crayon=1 )
    print(stock) # imprime état du stock – tout va bien
    stock.retirer( papier=12, crayon=6 )
    print(stock)
    stock.retirer(papier=7 ) # message de recommande
    print(stock)
    stock.retirer(crayon=1) # message de recommande
    print(stock)
    print(stock.valeur()) # message de recommande
