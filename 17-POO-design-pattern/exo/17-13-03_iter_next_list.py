# Utilisation des fonctions iter() et next()

# tuple de départ : non itératif
mytuple = ("apple", "banana", "cherry")
print(mytuple)

# construction de l'itérateur
myit = iter(mytuple)
# print(myit)

# itération
while True:
	try:
		fruit = next(myit)
	except StopIteration:
		break
	print(fruit)

# construction de l'itérateur
myit = iter(mytuple)

# itération
while True:
	fruit = next(myit , None)
	if fruit is None : break
	print(fruit)

# ou, plus simple à lire :
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))

