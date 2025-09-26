import copy


class Stock:
    def __init__(self):
        """
        exemple de dictionnaire représentant le stock
        stock_d = {
            "papier" : {
                "valeur" : 20,
                "recommande" : 5
            },
            "crayon" : {
                "valeur" : 8,
                "recommande" : 2
            },
            "gomme"  : {
                "valeur" : 3,
                "recommande" : 1
            },
            "trombone" : {
                "valeur" : 350,
                "recommande" : 20
            },
        }
        """
        self.stock_d = {}

    @property
    def stock_d(self):
        """
        le getter du stock retourne le stock complet
        :return: stock complet
        """
        return self.__stock_d

    @stock_d.setter
    def stock_d(self, d ):
        """
        le setter du stock ne fonctionne que pour le stock complet
        le setter vérifie ce nouveau stock et génère éventuellement un message si une valeur est trop faible
        :param d: nouveau stock
        :return: none
        """
        for article, stock_article in d.items():
            if stock_article["valeur"] <= stock_article["recommande"]:
                print("recommander", article)
            if stock_article["valeur"] <= 0 :
                print("vide:", article)
                d[article]["valeur"] = 0
        self.__stock_d = d

    def __str__(self):
        out = "stock : "
        for article, stock_article in self.stock_d.items():
            out += "{} = {} | ".format( article, stock_article["valeur"])
        return out

    def seuil_de_recommande(self, article, seuil):
        """
        les accesseurs utilisés ici ne fonctionnent que pour le stock COMPLET
        on ne peut pas accéder directement à une valeur d'un dictionnaire, sinon on ne passe pas par le setter.
        il faut donc créer un nouveau dictionnaire dans cette méthode et l'envoyer au setter
        :param article:
        :param seuil:
        :return: none
        """
        new_stock_d = copy.copy(self.stock_d)
        new_stock_d[article]["recommande"] = seuil
        self.stock_d = new_stock_d

    def retirer(self, article, demande=0):
        """
        un client vient retirer des articles du stock
        cf explication méthode ".seuil_de_recommande()"
        :param article: clé dictionnaire
        :param demande: valeur du retrait
        :return: none
        """
        new_stock_d = copy.copy(self.stock_d)
        new_stock_d[article]["valeur"] -= demande
        self.stock_d = new_stock_d

    def ajouter(self, article, ajout=0):
        """
        un gestionnaire du stock ajoute des produits au stock
        (pour initialiser ou suite à une recommande)
        cf explication méthode ".seuil_de_recommande()"
        :param article: key
        :param ajout: quantité ajoutée
        :return: none
        """
        new_stock_d = copy.copy(self.stock_d)
        try:
            # fonctionnement normal : on ajoute au stock
            new_stock_d[article]["valeur"] += ajout
        except :
            # initialisation du stock
            # ce code est exécuté si la clé "article" n'existe pas
            new_stock_d[article] = {
                "valeur" : ajout,
                "recommande" : 0
            }
        self.stock_d = new_stock_d


if __name__ == "__main__":
    # on crée le stock, vide
    stock = Stock()

    # initaliser le stock : via la méthode .ajouter()
    stock.ajouter( "papier", 20)
    stock.seuil_de_recommande( "papier", 2 )
    stock.ajouter( "crayon", 8)
    stock.seuil_de_recommande( "crayon", 2 )
    stock.ajouter( "gomme", 3)
    stock.seuil_de_recommande( "gomme", 2 )
    stock.ajouter( "trombone", 350)
    stock.seuil_de_recommande( "trombone", 2 )
    stock.ajouter( "oreiller", 1)
    stock.seuil_de_recommande( "oreiller", 2 )
    print(stock) # imprime état du stock – tout va bien

    # le stock travaille : retrait, commande et ajout successifs
    stock.retirer( "papier", 6 )
    stock.retirer( "crayon", 6 )
    print(stock)
    stock.retirer( "gomme", 7 ) # message de recommande
    print(stock)  # message de recommande
    stock.retirer( "papier", 1) # message de recommande
    print(stock)  # message de recommande
    stock.retirer( "papier", 27 ) # message de recommande
    print(stock)  # message de recommande
    stock.retirer( "gomme", 10) # message de recommande
    print(stock)  # message de recommande
    stock.ajouter( "papier", 100)
    stock.ajouter( "gomme", 100)
    stock.ajouter( "crayon", 100)
    print(stock)

