class Stock:

    def __init__(self, papier=0, crayon=0):
        self.stock = { "papier" : papier, "crayon" : crayon }
        self.seuil_de_recommande()

    def seuil_de_recommande(self, papier=0, crayon=0):
        self.seuil = { "papier" : papier, "crayon" : crayon }

    def __str__(self):
        return("STOCK : papier={} ({}) crayon={} ({})".format( \
            self.stock["papier"], self.seuil["papier"], \
            self.stock["crayon"], self.seuil["crayon"], 
        ))

    def retirer(self, papier=0, crayon=0):
        if self.stock["papier"] >= papier:
            # on peut retirer du stock si la demande est inférieure au stock
            self.stock["papier"] -= papier
            print("papier retiré : {} (stock {})".format(papier, self.stock["papier"]))
        else:
            # sinon pas d eretrait et message d'erreur
            print("papier retiré : 0 (stock {} insuffisant)".format(self.stock["papier"]))
            
        if self.stock["papier"] <= self.seuil["papier"]:
            print("A RECOMMANDER: papier")
        
        if self.stock["crayon"] >= crayon:
            # on peut retirer du stock si la demande est inférieure au stock
            self.stock["crayon"] -= crayon
            print("crayon retiré : {} (stock {})".format(crayon, self.stock["crayon"]))
        else:
            # sinon pas d eretrait et message d'erreur
            print("crayon retiré : 0 (stock {} insuffisant)".format(self.stock["crayon"]))

        if self.stock["crayon"] <= self.seuil["crayon"]:
            print("A RECOMMANDER: crayon")

######################################################################

stock = Stock( crayon=8, papier=20 )
stock.seuil_de_recommande(papier=2)
print(stock) # imprime état du stock – tout va bien
stock.retirer( papier=12, crayon=6 )
stock.retirer( papier=7 ) # message de recommande
print(stock) # message de recommande
stock.retirer( crayon=1 ) # message de recommande
print(stock) # message de recommande
stock.retirer( papier=12, crayon=6 ) # message de recommande et refus

