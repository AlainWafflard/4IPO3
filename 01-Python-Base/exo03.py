def brol(x):
    y = x + 1
    x -= 1
    return y

a = 4
b = brol(a)
print(a, b)


def mod_villes(liste_de_villes):
    liste_de_villes.append("Koekelberg")
    del liste_de_villes[0]


villes = [  "Etterbeek", "Ixelles", "Ixelles", "Ixelles", "Uccle", "Forest", "Anderlecht"]
print(villes)
mod_villes(villes)
print(villes)
villes.remove("Ixelles")
if "Liège" in villes: villes.remove("Liège")
print(villes)
del villes[3:]
print(villes)

# communes = villes
# del villes

# print(communes)
# del communes
# print(villes)



# villes.append("Jette")
#
# print(communes)
# print(villes)
