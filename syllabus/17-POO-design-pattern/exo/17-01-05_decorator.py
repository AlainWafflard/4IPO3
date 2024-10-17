# reference
# https://www.tutorialsteacher.com/python/decorators

def greet_one():
	print('Hello One! ', end='')


def embedding(fn):
	"""
	embedding() takes a function fn() as an argument.
	It calls fn() and prints additional things.
	It extends the functionality fn() without modifying it.
	"""
	print("function embedding ... ", end='')
	fn()
	print('How are you?')


def my_decorator(fn):
	"""
	my_decorator(fn) is the decorator for fn().
	The mydecorator function returns an inner function.
	"""

	def inner_function():
		"""
		The inner function inner_function() can access the outer function's argument
		so it executes some code before or after to extend the functionality
		before calling the argument function.
		"""
		print("function decorator ... ", end='')
		fn()
		print('How are you?')

	return inner_function


@my_decorator
def greet_two():
	print('Hello Two! ', end='')


@my_decorator
def greet_three():
	print('Hello Three! ', end='')


# MAIN

# playing with an embedded function
greet_one()
print()
embedding(greet_one)

# playing with a decorator
# The decorator in Python can be defined over any appropriate function
# using the @decorator_function_name syntax
# to extend the functionality of the underlying function.
my_decorator(greet_one) # ceci n'affiche rien
my_decorator(greet_two) # ceci n'affiche rien
greet_two()
greet_three()

# Note : @my_decorator can be applied to any function that does not require any argument
