class Student:
	name = 'unknown'  # class attribute

	def __init__(self, name, age):
		self.name = name  # instance attribute
		self.age = age  # instance attribute

	@classmethod
	def tostring(cls):
		print('Class "Student", attribute "name"={}'.format(cls.name))

	@classmethod
	def create_object(cls):
		return cls('Steve', 25)

	@classmethod
	def create_object_unknown(cls):
		return cls(cls.name, 30)


if __name__ == "__main__":
	# on appelle la méthode de classe
	Student.tostring()

	# on crée un objet à partir de cette class method
	student = Student.create_object()
	print('Class "Student", attribute "name"={}, "age"={}'.format(student.name, student.age))

	student_unknown = Student.create_object_unknown()
	print('Class "Student", attribute "name"={}, "age"={}'.format(student_unknown.name, student_unknown.age))
