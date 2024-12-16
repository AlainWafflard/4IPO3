# reference
# https://www.tutorialsteacher.com/python/decorators

def greet_one():
	print('Hello One! ', end='')


def my_embedding_function(my_embedded_function):
	"""
	my_embedding_function() takes a function my_embedded_function() as an argument.
	It calls my_embedded_function() and prints additional things.
	It extends the functionality my_embedded_function() without modifying it.
	"""
	print("function my_embedding_function ... ", end='')
	my_embedded_function()
	print('How are you?')


def my_decorator(my_function):
	"""
	my_decorator(my_function) is the decorator for my_function().
	The mydecorator function returns an inner function.
	"""
	def inner_function():
		"""
		The inner function inner_function() can access the outer function's argument
		so it executes some code before or after to extend the functionality
		before calling the argument function.
		"""
		print("function decorator ... ", end='')
		my_function()
		print('How are you?')
	return inner_function

@my_decorator
def greet_two():
	print('Hello Two! ', end='')


@my_decorator
def greet_three():
	print('Hello Three! ', end='')


# MAIN
if __name__ == "__main__":

	# playing with an embedded function
	greet_one()
	print()
	my_embedding_function(greet_one)

	# playing with a decorator
	# The decorator in Python can be defined over any appropriate function
	# using the @decorator_function_name syntax
	# to extend the functionality of the underlying function.
	my_decorator(greet_one) # ceci n'affiche rien
	my_decorator(greet_two) # ceci n'affiche rien
	greet_two()
	greet_three()

	# Note : @my_decorator can be applied to any function that does not require any argument
