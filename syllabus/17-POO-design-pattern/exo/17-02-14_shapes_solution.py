# Exo 13-11-03 : les quadrilatères
# from pprint import pprint
from inspect import getmembers
from types import FunctionType
import abc


class Shape(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def calculate_area(self):
		pass

	@abc.abstractmethod
	def calculate_perimeter(self):
		pass

	@classmethod
	def factory(cls, name):
		if name == 'circle':
			radius = input("Enter the radius of the circle: ")
			return Circle(float(radius))

		elif name == 'rectangle':
			height = input("Enter the height of the rectangle: ")
			width = input("Enter the width of the rectangle: ")
			return Rectangle(int(height), int(width))

		elif name == 'square':
			width = input("Enter the width of the square: ")
			return Square(int(width))


class Rectangle(Shape):
	def __init__(self, height, width):
		self.height = height
		self.width = width

	def calculate_area(self):
		return self.height * self.width

	def calculate_perimeter(self):
		return 2 * (self.height + self.width)


class Square(Shape):
	def __init__(self, width):
		self.width = width

	def calculate_area(self):
		return self.width ** 2

	def calculate_perimeter(self):
		return 4 * self.width


class Circle(Shape):
	def __init__(self, radius):
		self.radius = radius

	def calculate_area(self):
		return 3.14 * self.radius * self.radius

	def calculate_perimeter(self):
		return 2 * 3.14 * self.radius


# MAIN
shape_name = input("Enter the name of the shape: ")
shape = Shape.factory(shape_name)

print("The type of object created: {}".format(type(shape)))
print("The area of the {} is {}:".format(shape_name, shape.calculate_area()))
print("The perimeter of the {} is: {}".format(shape_name, shape.calculate_perimeter()))
