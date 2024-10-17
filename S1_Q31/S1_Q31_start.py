import json


class Magasin:
    def __init__(self):
        self.produit_d = {}
        self.commande_l = []
        self.client_d = {}
        self.facture_l = []

    def __str__(self):
        pass

    def load_product_f(self, file):
        with open(file, 'r', encoding='utf-8') as fichier: produit_json = json.load(fichier)
        for d in produit_json: self.__load_product(d)

    def __load_product(self, p):
        pass

    def load_order_f(self, file):
        pass

    def __load_order(self, c):
        """
        traite la commande c
        crée le client
        ajoute la commande au panier du client
        n'exécute pas la commande
        """
        pass

    def commit_order(self):
        """
        on exécute les commandes des clients
        # on crée une facture vide
        # traitement des commandes
        # création des détails facture
        # émission de la facture (un print suffit)
        """
        pass


class Client :
    def __init__(self, name):
        pass

    def __str__(self):
        pass

    def append_order(self, ol ):
        """ ajoute les commandes au panier """
        pass

    def commit_order(self, product_l, invoice_o):
        """
        # traitement de la commande (boucle)
            # produit existant ?
            # produit en stock ?
            # on ajoute l'élément acheté à la facture
            # on régularise le stock
        # on efface le panier
        """
        pass


class Facture :
    def __init__(self, name):
        pass

    def __str__(self):
        pass

    def append(self, p, price, qty ):
        pass

    def make(self):
        pass


class Produit:
    """ Classe Produit avec gestion des seuils de stock """

    def __init__(self, name, price, qty, category, reorder_threshold):
        pass

    def __str__(self):
        pass

    def is_stock_enough(self, qty ):
        pass

    def stock_decrease(self, qty ):
        pass


if __name__ == "__main__":

    # Créer magasin
    mag_o = Magasin()

    # Charger les produits depuis un fichier JSON
    mag_o.load_product_f('S1_Q31_produit_in.json')

    # Charger les commandes client
    mag_o.load_order_f('S1_Q31_commande.json')

    # Exécuter les commandes client et établir les factures
    mag_o.commit_order()

