# Design Pattern Iterator
# A simple Python program to demonstrate
# working of iterators using an example type
# that iterates from 10 to given value

class CountDown:
	"""
	An iterable user defined type
	"""
	def __init__(self, start):
		self.__counter = start

	def __iter__(self):
		"""
		Creates iterator object
		Called when iteration is initialized
		:return: CountDown generator
		"""
		self.__target = 0
		return self

	def __next__(self):
		"""
		To move to next element.
		:return: integer
		"""
		# decrement
		self.__counter -= 1

		# Stop iteration if target is reached
		if self.__counter <= self.__target :
			raise StopIteration

		# Else return value
		return self.__counter


# MAIN
if __name__ == '__main__':

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

