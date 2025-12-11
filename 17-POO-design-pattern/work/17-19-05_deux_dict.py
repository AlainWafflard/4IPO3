class Storage:
	__storage = None

	def __new__(cls, *args, **kwargs):
		if cls.__storage is None :
			print("cls.__storage est créé")
			cls.__storage = super().__new__(cls)
		else:
			print("cls.__storage existe déjà")
		return  cls.__storage

	def __init__(self):
		# if self.__storage is not None:
		# 	raise Exception("use singleton please")
		self.__data = {}  # Data storage as Dictionnary

	def __str__(self):
		output = "Storage:\n"
		for k in self.__data:
			output += " - clé {} : valeur {}\n".format(k, self.__data[k])
		return output

	# @classmethod
	# def singleton(cls):
	# 	if cls.__storage is None :
	# 		print("cls.__storage est créé")
	# 		cls.__storage = cls()
	# 	else:
	# 		print("cls.__storage existe déjà")
	# 	return  cls.__storage

	def append(self, k, v):
		if k in self.__data.keys():
			raise Exception("key {} already exists".format(k))
		self.__data[k] = v


if __name__ == "__main__":

	# Dans un certain module, il se passe ceci :
	s = Storage()
	s.append( "fname", "Kevin")

	# Dans un autre module, il se passe cela :
	t = Storage()
	t.append( "lname", "Brian")

	u = Storage()
	u.append( "street", "Buedts")

	print("s:", s)
	print("t:", t)
	print("u:", u)
	print("s == t ?", s == t)
	print("s is t ?", s is t)

