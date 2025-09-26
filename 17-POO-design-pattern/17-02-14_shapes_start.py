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
		pass


class Rectangle(Shape):
	def __init__(self, height, width):
		self.height = height
		self.width = width


class Square(Shape):
	def __init__(self, width):
		self.width = width


class Circle(Shape):
	def __init__(self, radius):
		self.radius = radius


# MAIN
shape_name = input("Enter the name of the shape: ")
shape = Shape.factory(shape_name)

print("The type of object created: {}".format(type(shape)))
print("The area of the {} is {}:".format(shape_name, shape.calculate_area()))
print("The perimeter of the {} is: {}".format(shape_name, shape.calculate_perimeter()))
