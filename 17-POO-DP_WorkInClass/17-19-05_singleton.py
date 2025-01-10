class Storage:
	__instance = None
	__data  = None

	def __new__(cls):
		if cls.__instance is None:
			# objet créé uniquement s'il n'existe pas
			cls.__instance = super().__new__(cls)
		return cls.__instance  # objet retourné

	def __init__(self):
		# if self.__instance is not None:
		# 	raise Exception("This class is a singleton!  Use Storage.singleton()")
		# self.__data = {}  # Data storage as Dictionnary
		# Data storage as Dictionnary
		# if not hasattr(self, "data"):
		if self.__data is None:
			# creating dict only once
			self.__data = {}

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

# Dans un autre module, il se passe cela :
u = Storage()
u.append( "bday", "2000/01/01")


print("s:", s)
print("t:", t)
# print("u:", u)
print("s == t ?", s == t)
print("s is t ?", s is t)

