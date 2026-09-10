l = [ 3, 2, 654, 321, 65, 987, 254, 65 ]
m = [ 5, 6,  43, 965, 52, 954, 358, 96 ]
print("l =", l)
print("m =", m)
print("nombre d'éléments =", len(l))

# sous-question 1
# moyenne
somme = 0 
for x in l:
    somme += x
moyenne = somme / len(l)
print("SQ1 : moyenne=", moyenne)

# sous-question 2
# nombre éléments supérieurs à 10 
nb_sup = 0 
for x in l:
    if x >= 10:
        nb_sup += 1 
print("SQ2 : nombre d'éléments supérieurs à 10 =", nb_sup)

# sous-question 3
# multiplier les deux listes
n = [ l[i]*m[i] for i in range(len(l)) ]
print("SQ3 : l * m =", n)

# sous-question 4
# trouver les max et min de la liste
max = min = l[0]
for x in l:
    if x > max:
        max = x
    if x < min:
        min = x
print( "SQ4 : max={}, min={}".format( max, min ) )

# sous-question 5
# construire liste en ordre inverse
# méthode 1
p = [ l[ len(l)-i-1 ] for i in range(len(l)) ]
print("SQ5/1 : l inversé =", p )
# méthode 2
q = [ l[ i ] for i in range(len(l)-1,-1,-1) ]
print("SQ5/2 : l inversé =", q )
# méthode 3
r = [ l[ i ] for i in range(-1,-len(l)-1,-1) ]
print("SQ5/3 : l inversé =", r )

# sous-question 6
# A partir d’un « custom input » contenant une série de nombres
# terminée par un « q », construisez une liste.
lst = []
while True:
    x = input("Donnez un élément de la liste :")
    if( x == "q" ):
        break
    lst.append(x)
print(lst)

