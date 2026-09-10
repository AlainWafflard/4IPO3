
lst = [ "BRUXELLES", "LOUVAIN","MONS" ]

# imprimer verticalement, en séquentiel
for ville in lst:
    for lettre in ville:
        print( "<{0:^3}>".format(lettre) )
    print()

# imprimer verticalement, côte à côte
for i in range(15):
    for ville in lst:
        try:
            print( "| {0} |   ".format(ville[i]), end=" " )
        except:
            print( "| {0} |   ".format(" "), end=" " )
    print()

