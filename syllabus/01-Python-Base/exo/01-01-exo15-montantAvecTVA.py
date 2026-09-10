# Ecrivez le programme qui répond à la spécification suivante :
# Demandez le prix unitaire HT d’un article
# Demandez la quantité commandée
# Demandez le taux de TVA appliqué
# Le programme doit calculer le montant TVA comprise
# d’une facture pour un produit donné

pu = float(input("prix unitaire HT d’un article ? "))
qc = int(input("quantité commandée ? "))
tt = float(input("taux de TVA appliqué ? "))

p_ht = pu * qc
p_tc = p_ht * ( 1 + tt )
print( "prix hors taxe=", p_ht, "prix TTC=", p_tc)

