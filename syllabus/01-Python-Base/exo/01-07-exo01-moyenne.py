# Concevoir un algorithme qui calcule la moyenne d’une liste de nombres.

l = [ 2, 3, 4, 5 ]

s = 0
p = 1 

for n in range(1, 7):
    s += n
    p *= n

print('somme=',s)
print('produit=', p)
