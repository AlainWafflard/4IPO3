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
		if age > 18:
			return True
		else:
			return False

	@classmethod
	def factory(cls, name, year):
		current_age = date.today().year - year
		if cls.isAdult(current_age) and current_age >= cls.__min_age:
			return cls(name, current_age)

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

	g = Employee.factory( "Gaga", 2010)
	print(g)

	h = Employee.factory("Harry", 1999)
	print(h)

