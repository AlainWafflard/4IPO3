from renaissance import CompteRenaissance
from saving_account import CompteEpargne
from current_account import CompteCourant


# kim_c = CompteRenaissance("Kim")
# kim_c.deposer(1000)
# print(kim_c)
# kim_c.retirer(200)
# print(kim_c)
# kim_c.retirer(1200)
# print(kim_c)

kim_c = CompteEpargne("Kim")
kim_c.deposer(1000)
print(kim_c)
kim_c.retirer(200)
print(kim_c)
kim_c.retirer(2000)
print(kim_c)
# print(kim_c.interet)

kim_c = CompteCourant("Kim")
kim_c.deposer(1000)
print(kim_c)

clijster_c = CompteCourant("Clijster")
print(clijster_c)

kim_c.transferer(clijster_c, 500)
kim_c.retirer(200)
kim_c.transferer(clijster_c, 800)
kim_c.transferer(clijster_c, 1000)
clijster_c.retirer(2500)
clijster_c.transferer(kim_c, 50)

print(kim_c)
print(clijster_c)
