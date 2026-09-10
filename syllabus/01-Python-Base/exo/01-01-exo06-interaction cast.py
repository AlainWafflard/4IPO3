# Interaction
# Demander à l’utilisateur un premier nombre
# Demander à l’utilisateur un second nombre
# Calculer l’addition des deux nombres et l’afficher à l’écran:
# Le resultat de [?] + [?] vaut: [réponse]
    
x = int(input("Premier nombre ? "))
y = int(input("Deuxième nombre ? "))
# cast nécessaire, car les nombres introduits à la console sont des strings.
z = x + y

# print, le plus simple, avec plusieurs arguments 
print("Le résultat de", x, "+", y, "vaut:", z )

# print, avec un seul aregument, un string qu'il faut construire 
print("Le résultat de " + str(x) + " + " + str(y) + " vaut: " + str(z) )

