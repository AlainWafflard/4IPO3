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
    def __init__(self, name, color=bcolors.OKBLUE, position=0):
        self.position = position
        self.name = name
        self.speed = 0
        self.friend = None
        self.duration = 0
        self.time = 0
        self.color = color

    def __str__(self):
        if self.position > self.friend.position:
            friend_s = "   cool, my friend {4} is behind me "
        else:
            friend_s = "   oups, my friend {4} is beyond me"
        pos_s = "{0}: sp {1:3} km/h, ti {3:4.1f} h, po {2:5.1f} km"
        full_s = self.color + pos_s + "\n" + friend_s + bcolors.ENDC
        return full_s.format(self.name, self.speed, self.position, self.time, self.friend.name)

    def move(self):
        self.time += self.duration
        self.position += self.duration * self.speed


# on déclare la voiture A
voiture_A = Car("A",bcolors.OKBLUE)
voiture_A.speed = 120
# on déclare la voiture B
voiture_B = Car("B", bcolors.OKGREEN, 10)
voiture_B.speed = 60
# on lie les deux voitures
voiture_B.friend, voiture_A.friend = voiture_A, voiture_B
print(voiture_A)
print(voiture_B)
# duration = 1/12 h = 5 min
voiture_A.duration = voiture_B.duration = 1/12

for i in range(6):
    # les voitures se mettent à rouler
    voiture_A.move()
    voiture_B.move()
    print(voiture_A)
    print(voiture_B)

