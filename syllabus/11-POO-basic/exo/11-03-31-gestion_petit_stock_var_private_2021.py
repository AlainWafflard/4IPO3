class Stock:

    def __init__(self, papier=0, crayon=0):
        self.__stock = {
            "papier" : papier,
            "crayon" : crayon
        }
        self.seuil_de_recommande()

    def __str__(self):
        out = "STOCK : papier={} (seuil : {}) \nSTOCK : crayon={} (seuil : {})".format( \
            self.__stock["papier"], self.__reorder["papier"], \
            self.__stock["crayon"], self.__reorder["crayon"],
        )
        out += "\n" + self.__check_reorder()
        return out

    def seuil_de_recommande(self, papier=0, crayon=0):
        self.__reorder = {
            "papier": papier,
            "crayon": crayon
        }

    def retirer(self, papier=0, crayon=0):
        """ retire les éléments demandés du stock
            dans les limites disponibles
        """
        # papier
        if self.__stock["papier"] >= papier :
            # stock suffisant
            print("{} papier demandés, {} papier retirés".format(papier,papier))
            self.__stock["papier"] -= papier
        else:
            # stock insuffisant
            print("{} papier demandés, {} papier retirés".format(papier,self.__stock["papier"]))
            self.__stock["papier"] = 0
        # crayon
        if self.__stock["crayon"] >= crayon :
            # stock suffisant
            print("{} crayon demandés, {} crayon retirés".format(crayon,crayon))
            self.__stock["crayon"] -= crayon
        else:
            # stock insuffisant
            print("{} crayon demandés, {} crayon retirés".format(crayon,self.__stock["crayon"]))
            self.__stock["crayon"] = 0
        print(self.__check_reorder())

    def __check_reorder(self):
        """ vérifie état du stock
            imprime message de recommande si nécessaire
        """
        out = ""
        if self.__stock["papier"] < self.__reorder["papier"]:
            out += " Papier à recommander ! "
        if self.__stock["crayon"] < self.__reorder["crayon"]:
            out += " Crayon à recommander ! "
        # if len(out)>0 :
        return out


# MAIN
stock = Stock(papier=20, crayon=8)
stock.seuil_de_recommande(papier=2, crayon=1)
print(stock)  # imprime état du stock – tout va bien
stock.retirer(papier=12, crayon=6)
print(stock)
stock.retirer(papier=7 ) # message de recommande
print(stock)
stock.retirer(papier=3) # message de recommande
print(stock)
stock.retirer(crayon=3, papier=3)  # message de recommande
print(stock)

