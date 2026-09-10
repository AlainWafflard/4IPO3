# Demander à l’utilisateur de rentrer des nombres.
# Dès que l’utilisateur rentre la lettre 'q',
# afficher la somme des nombres

x = input("entrez un nombre ou 'q': ")
s = 0 
while x != 'q':
    s += int(x)
    x = input("entrez un nombre ou 'q': ")
print("somme =", s )
