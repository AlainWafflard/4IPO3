#Présentez l’accroissement d’une population de lapins au fil des mois. 
#- Avec alignement (cf figure)
#- Chaque couple de lapin procrée à partir du 3e mois de vie, et donne
#  la vie à deux lapereaux, chaque mois.  
#- Chaque mois, la population s’accroit donc du nombre de lapins
#  présents deux mois auparavant.
#- Au début (mois 1), il y a un couple de lapereaux âgés d’un mois.

print("méthode classique")
print("**************")
m = 0
n = 1
print( "* {0:>3} : {1:>4} *".format( 0, 1 ) )
for i in range(1,12):
    p = n+m
    m = n
    n = p
    print( "* {0:>3} : {1:>4} *".format( i, p ) )
print("**************")
print()

######################################################################
# méthode récursive, non optimisée 

def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print("méthode récursive")
print("**************")
for i in range(0,12):
    print( "* {0:>3} : {1:>4} *".format( i, fibonacci(i)) )
print("**************")

