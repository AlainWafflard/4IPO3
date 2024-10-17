# Design Pattern Iterator
# A simple Python program to demonstrate
# working of iterators using an example type
# that iterates from 10 to given value

# An iterable user defined type
class CountDown:
	# Constructor
	def __init__(self, start):
		self.__counter = start

	# Creates iterator object
	# Called when iteration is initialized
	def __iter__(self):
		self.__target = 0
		return self

	# To move to next element.
	def __next__(self):
		# decrement
		self.__counter -= 1

		# Stop iteration if target is reached
		if self.__counter <= self.__target :
			raise StopIteration

		# Else return value
		return self.__counter


# MAIN
# initialization du CountDown à 5
my_iter = iter(CountDown(5))

while True:
	try:
		i = next(my_iter)
		print(i)

	except StopIteration:
		# quand i atteint 0 
		print("Go !")
		break

