# Calculez l'accroissement d'un capital,
# connaissant l'intérêt auquel il est placé

capital_s= float(input("capital (€) ? "))
interet  = float(input("intérêt (%) ? "))
duree    = float(input("durée (ans) ? "))
accroiss = 1 + interet/100

# intérêt versé annuellement 
capital = capital_s
for i in range(int(duree)):
    capital_plus_interet = capital * accroiss
    print("Après", i+1, "an(s), capital=", capital_plus_interet )
    capital = capital_plus_interet

print("simulation terminée (ans)")
print()

# intérêt versé mensuellement 
capital = capital_s
accroiss = 1 + interet/(100*12)
for i in range((int(duree))*12):
    capital_plus_interet = capital * accroiss
    print("Après", i+1, "mois, capital=", capital_plus_interet )
    capital = capital_plus_interet

print()
