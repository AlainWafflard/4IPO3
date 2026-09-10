class bcolors:
	""" to print colored text
		eg:print(bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)
		https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal
	"""
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'


class Car:

	def __init__(self, brand, color=bcolors.OKBLUE, position=0):
		self.__brand = brand
		self.__speed = 0
		self.__position = float(position)
		self.__time = 0.0
		self.__duration = 0.0
		self.__color = color

	@property
	def speed(self):
		return self.__speed

	@speed.setter
	def speed(self, v=0):
		if v < 0 : v = 0
		if v > 120 : v = 120
		self.__speed = v

	@property
	def duration(self):
		return self.__duration

	@duration.setter
	def duration(self, v):
		# ce setter, non seulement enregistre la duration
		# mais il fait avancer la voiture (calcul de la nouvelle position)
		# approche discutable car non intuitive
		self.__duration = float(v)
		self.__time += self.__duration
		self.__position += self.__duration * self.speed

	def __str__(self):
		if self.__position > self.friend.__position:
			friend_s = "   cool, my friend {4} is behind me "
		else:
			friend_s = "   oups, my friend {4} is beyond me"
		pos_s = "{0}: sp {1:3} km/h, ti {3:4.1f} h, po {2:5.1f} km"
		full_s = self.__color + pos_s + "\n" + friend_s + bcolors.ENDC
		return full_s.format(self.__brand, self.speed, self.__position, self.__time, self.friend.__brand)


# MAIN
if __name__ == '__main__':
	# on déclare la voiture A
	voiture_A = Car("A")
	voiture_A.speed = 120
	# on déclare la voiture B
	voiture_B = Car("B", bcolors.OKGREEN , 10)
	voiture_B.speed = 60
	# on lie les deux voitures
	voiture_B.friend = voiture_A
	voiture_A.friend = voiture_B
	print(voiture_A)
	print(voiture_B)
	for i in range(6):
		# les voitures se mettent à rouler
		# duration = 1/12 h = 5 min
		voiture_A.duration = voiture_B.duration = 1/12
		print(voiture_A)
		print(voiture_B)

