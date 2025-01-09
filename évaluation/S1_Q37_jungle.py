from abc import ABC, abstractmethod
import time


class Jungle:
	""" Sujet (Observable) """
	pass


class Jungle_item(ABC):
	pass


class Resource(Jungle_item):
	pass


class Water(Resource):
	pass


class Archaeplastida(Resource):
	pass


class Fauna(Jungle_item):
	pass


class Predator(Fauna):
	pass


class Prey(Fauna):
	pass


# MAIN
# Exemple d'utilisation
if __name__ == "__main__":

	# Création de la jungle
	jungle = Jungle()

	# Création des animaux et ressources (observateurs)
	buffle = Prey(0)
	lion = Predator(200)
	lac = Water(100)
	buisson = Archaeplastida(90)

	# Ajout des observateurs
	jungle.subcribe_observer(lion)
	jungle.subcribe_observer(buffle)
	jungle.subcribe_observer(lac)
	jungle.subcribe_observer(buisson)

	lion.set_food(buffle)
	lion.set_water(lac)
	buffle.set_predator(lion)
	buffle.set_water(lac)
	buffle.set_food(buisson)

	iter_nb = 0
	while iter_nb < 200:
		time.sleep(0.5)
		print(f'Iter {iter_nb} -- ', end='')

		# Génération d'événements
		match iter_nb:
			case 1:
				jungle.generate_event("pluie-start")
			case 2:
				jungle.generate_event("pluie-stop")

		# Mouvement des animaux
		buffle.go()
		lion.go()
		if lion.prey_caught or not buffle.alive :
			print("Bon appétit, cher lion !")
			break
		iter_nb += 1

	print(lac)
	print(buisson)
