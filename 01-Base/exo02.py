
def hello(name):
    """
    Retourner un message d'accueil
    :param name nom de la personne à accueillir
    :return:
    """
    return f"bonjour {name}, bienvenue chez nous"

def oper( a, b ):
    s = a + b
    d = a - b
    return (s, d)

# print(hello("Kim"))
# m = hello("Sam")
# print(m)
#
# r = range(50)

# for i in r :
#     print(i)

v = [ [ 1 , 2], [ 3 , 4 ]]
v.append( [ 5 ,6 ] )
w = ( ( 1 , 2 ), ( 3 , 4 ) )
# w.append( [ 5 ,6 ] )

for l in v :
    for i in l :
        print(i)

# for l in w :
#     for i in l :
#         print(i)

retour = oper( 6, 2 )
print(retour)
# retour.append(5)

plus, moins = oper( 10, 7 )
plus += 1
print( plus, moins)

villes = [  "Etterbeek", "Ixelles", "Uccle", "Forest", "Anderlecht"]
# for ville in villes :
#     print(ville)
for index, ville in enumerate(villes) :
    if index > 1 :
        villes[index] = "Out of Brussels"

print(villes)










