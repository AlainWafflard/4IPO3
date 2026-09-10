# DONNÉES EN ENTRÉE:
# P : prix hors TVA de l’article acheté en €
# Q : quantité commandée de l’article en €
# T : taux de TVA à appliquer en décimal (ex.: 0.21)
#
# PRE-CONDITIONS:
# P : réel strictement positif 
# Q : entier strictement positif 
# T : réel compris entre 0 et 1
#
# RÉSULTATS:
# Affiche le montant à payer TVA comprise (21%)
# Si le montant HTVA est supérieur à 500€, le client a droit à une remise de 10% sur le montant TTC.

p = float(input("prix unitaire: "))
q = int(input("quantité : "))
t = float(input(" taxe : "))

p_htva = p * q
taxe = p_htva * t
p_ttc = p_htva + taxe

if p_htva > 500 or q > 10 :
    remise = p_ttc * 10/100
else:
    remise = 0 
p_ttc -= remise 

print( "montant HTVA=", p_htva, "€")
print( "taxes=", taxe, "€" )
print( "montant TTC=", p_ttc, "€" )
if( remise > 0 ):
    print("bravo, vous avez obtenu une remise de", remise )
else:
    print("pas de remise; achetez plus")
