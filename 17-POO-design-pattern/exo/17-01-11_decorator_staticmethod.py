from datetime import date


class Employee:
	__min_age = 25

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __str__(self):
		return f" Employee {self.name}, aged {self.age} years old"

	@staticmethod
	def isAdult(age):
		"""
		Cette méthode statique se comporte comme une simple fonction.
		Elle ne fait aucune référence à la classe où elle se trouve.  Elle pourrait même être déplacée à l'extérieur de la classe.
		Il n'y a pas d'argument "cls" ou "self" !
		"""
		if age > 18:
			return True
		else:
			return False

	# def factory(self):
	# 	pass

	@classmethod
	def factory(cls, name, year):
		"""
		Cette méthode statique se comporte comme une simple fonction.
		Toutefois, elle peut faire référence à la classe où elle se trouve.  Elle ne peut pas être déplacée à l'extérieur de la classe.
		Il y a un argument "cls" qui permet d'utiliser des références de la classe, par ex. cls.__min_age
		"""
		current_age = date.today().year - year
		if cls.isAdult(current_age) and current_age >= cls.__min_age:
			return cls(name, current_age)
		else:
			return None

	@classmethod
	def set_age_to_work(cls, new_age):
		cls.__min_age = 18


if __name__ == '__main__':
	print(f" Adulte à 30 ans  ?", Employee.isAdult(30))
	print(f" Adulte à 15 ans  ?", Employee.isAdult(15))

	Employee.set_age_to_work(18)

	e = Employee('Eric', 30)
	print(e)

	f = Employee('Fatima', 16)
	print(f)

	g = Employee.factory( "Gaga", 2020)
	print(g)

	h = Employee.factory("Harry", 1999)
	print(h)

