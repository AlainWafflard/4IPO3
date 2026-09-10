# demander un nombre [n]
# écrire “Le nombre est pair” si n est pair
# sinon écrire “Le nombre est impair”

n = int(input("Entrez un nombre entier : "))

if n % 2 == 0 :
    print( n, "est pair")
else:
    print( n, "est impair")

