class Stock:
    """ seulement deux méthodes publiques : "seuil_de_recommande()" et "retirer()"
    """

    def __init__(self, papier=0, crayon=0):
        self.__stock = { "papier" : papier, "crayon" : crayon }
        self.seuil_de_recommande()

    def __get_stock(self, type):
        if self.__stock[type] <= self.__reorder[type]:
            print("A RECOMMANDER: {}".format(type))
        return self.__stock[type]

    def __set_stock(self, type, value=0 ):
        self.__stock[type] = value 

    def __str__(self):
        return("STOCK : papier={} (seuil : {}) \nSTOCK : crayon={} (seuil : {})".format( \
            self.__get_stock("papier"), self.__reorder["papier"], \
            self.__get_stock("crayon"), self.__reorder["crayon"], 
        ))

    def seuil_de_recommande(self, papier=0, crayon=0):
        self.__reorder = { "papier" : papier, "crayon" : crayon }

    def retirer(self, papier=0, crayon=0):

        if self.__get_stock("papier") >= papier:
            # on peut retirer du stock si la demande est inférieure au stock
            self.__set_stock( "papier", self.__get_stock("papier") - papier )
            demande, retire, stock = papier, papier, self.__get_stock("papier")
        else:
            # sinon pas de retrait et message d'erreur
            demande, retire, stock = papier, 0, self.__get_stock("papier")
        print("papier demandé : {} - retiré : {} - stock {}".format(demande, retire, stock ))

        if self.__get_stock("crayon") >= crayon:
            # on peut retirer du stock si la demande est inférieure au stock
            self.__set_stock( "crayon", self.__get_stock("crayon") - crayon )
            demande, retire, stock = crayon, crayon, self.__get_stock("crayon")
        else:
            # sinon pas de retrait et message d'erreur
            demande, retire, stock = crayon, 0, self.__get_stock("crayon")
        print("crayon demandé : {} - retiré : {} - stock {}".format(demande, retire, stock ))

######################################################################

stock = Stock( crayon=8, papier=20 )
stock.seuil_de_recommande(papier=2,crayon=1)
print(stock) # imprime état du stock – tout va bien
stock.retirer( papier=12, crayon=6 )
print(stock)
stock.retirer( papier=7 ) # message de recommande
print(stock) # message de recommande
stock.retirer( crayon=1 ) # message de recommande
print(stock) # message de recommande
stock.retirer( papier=12, crayon=6 ) # message de recommande et refus

