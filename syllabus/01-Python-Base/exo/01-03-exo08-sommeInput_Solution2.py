# Demander à l’utilisateur de rentrer des nombres.
# Dès que l’utilisateur rentre la lettre 'q',
# afficher la somme des nombres

s = 0 
while True:
    x = input("entrez un nombre ou 'q': ")
    if x == 'q' :
        break
    s += int(x)
print("somme =", s )
