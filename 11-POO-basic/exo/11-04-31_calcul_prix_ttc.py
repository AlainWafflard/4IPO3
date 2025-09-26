class Article:
    """
    Créer la classe Article caractérisée par les attributs :
    Référence, PrixHT, TauxTVA.

    Le taux de TVA est en fait commun à tous les articles.
    Pour éviter toute redondance de cet attribut, vous devriez donc la déclarer comme
    partagée au niveau de la classe Article et non comme un attribut spécifique des
    objets instanciés à partir de la classe.
    """
    taux_tva = 21

    def __init__(self, ref, prix_ht):
        self.ref = ref
        self.prix_ht = prix_ht
        self.prix_ttc = None

    def __str__(self):
        """
        affiche les informations de l’article
        :return: string
        """
        return "article réf {0:3s}, prix TTC {2:6.2f} (prix HT {1:6.2f})".format( self.ref, self.prix_ht, self.calculer_prix_ttc())

    def calculer_prix_ttc(self):
        """
        Cette méthode calcule et retourne le prix TTC d’un article :
        = PrixHT + (PrixHT*TauxTVA/100)
        Optimisation : le calcul est effectué seulement s'il est demandé, et une seule fois.
        :return: prix TTC
        """
        if self.prix_ttc is None:
            self.prix_ttc = self.prix_ht * (1 + self.taux_tva / 100)
        return self.prix_ttc


# Créer un programme de test où il faut créer des objets
# et leur calculer le prix TTC.
if __name__ == "__main__":
    article_o = Article( "ABC", 50.50 )
    print(article_o)
    print(article_o.calculer_prix_ttc())    # 61.105
    article_o.prix_ht = 150
    print(article_o.calculer_prix_ttc())    # prix TTC inchangé ... pourquoi ?


