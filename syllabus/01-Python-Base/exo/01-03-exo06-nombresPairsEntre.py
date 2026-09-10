# Les nombres pairs compris entre n et m inclus sont affichés

n = int(input("n ? "))
m = int(input("m ? "))
for i in range( n, m ):
    if i % 2 == 0:
        print(i, end=' ')
print()
