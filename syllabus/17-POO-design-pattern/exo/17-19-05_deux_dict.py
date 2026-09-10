class Storage:

	def __init__(self):
		self.__data = {}  # Data storage as Dictionnary

	def __str__(self):
		output = "Storage:\n"
		for k in self.__data:
			output += " - clé {} : valeur {}\n".format(k, self.__data[k])
		return output

	def append(self, k, v):
		if k in self.__data.keys():
			raise Exception("key {} already exists".format(k))
		self.__data[k] = v


# Dans un certain module, il se passe ceci :
s = Storage()
s.append( "fname", "Kevin")

# Dans un autre module, il se passe cela :
t = Storage()
t.append( "lname", "Brian")

print("s:", s)
print("t:", t)
print("s == t ?", s == t)
print("s is t ?", s is t)

