import random


class Halloween:
	"""
	Vous devez écrire la classe Halloween.  Toutes les attributs d'objet
	doivent être privés.  Vous devez utiliser les accesseurs propres à Python,
	càd les décorateurs @property, @setter,  etc.

	La classe Halloween a pour but de produire un message de paix et d'amour.
	Cf méthode __str__() et scénario nominal (print). Mais ce message ne peut
	être produit que si
	1) le code appelant crée un mot de passe correct, via
	   les accesseurs.  Cf scénario nominal : h.password = "aaaaaaaa" ;
	   attention, .password est privé.
	2) l'utilisateur réussit le petit jeu (répondre à une question);
	3) l'utilisateur donne le mot de passe correct

	# consignes par groupes (cf vos codes)
	# 1- en lien avec TEST 2 : le mot de passe doit avoir au moins 6 caractères
	# 2- en lien avec TEST 2 : le mot de passe doit contenir au moins une lettre majuscule
	# 3- en lien avec TEST 2 : le mot de passe doit contenir au moins une lettre minuscule
	# 4- en lien avec TEST 2 : le mot de passe doit contenir le caractère spécial "$"
	# 5- en lien avec TEST 2 : le premier caractère du mot de passe doit être "*"
	# 6- en lien avec TEST 2 : le mot de passe ne peut contenir que des lettres
	# 7- TEST 3 modifié : print(h.password) affiche "********" (pas d'erreur)
	# 8- TEST 3 : print(h.password) n'affiche pas le mot de passe (consigne inchangée)
	# 9- TEST 3 modifié : print(h.password) affiche le mot de passe à l'envers
	# A- Implanter la méthode .play() "A"
	# B- Implanter la méthode .play() "B"
	# C- Implanter la méthode .play() "C"
	"""
	__question_l =  [
		[ "Quel est le jour d'octobre réservé à la fête d'Halloween ? (nombre) ", 31],
		[ "Combien de jours y a-t-il en octobre ? (nombre) ", 31 ],
		[ "Les couleurs dominantes d'Halloween sont-elles le noir et l'orange ? (oui/non) ", "oui" ],
		[ "Les couleurs dominantes d'Halloween sont-elles le rouge et le bleu ? (oui/non) ", "non" ],
	]
	__roulette_l = [
		"citrouille",
		"sorcière",
		"squelette"
	]

	def __str__(self):
		return "I witch you a happy Halloween, Silver Shamrock !"

	def play(self):
		"""
		Petit jeu d'Halloween.
		Si l'utilisateur échoue, alors l'app s'arrête avec le message moralisateur suivant
		"Va travailler plutôt que de perdre ton temps avec cette fête païenne,
		 grotesque et commerciale."
		Consigne du jeu (fonction de votre groupe):
		A. L'app pose une question tirée de .__question_l;
		   on y trouve l'énoncé de la question et la réponse correcte;
		   l'app compare la réponse correcte avec la réponse de l'utilisateur.
		B. Roulette russe; l'app demande "Qu'est-ce qui se trouve devant votre porte ?"
		   et tire un mot au hasard parmi la liste .__roulette_l;
		   l'utilisateur doit deviner ce mot en un seul essai (la liste lui est fournie)
		C. L'app demande "Combien d'araignées descendent-elles du plafond ? (1-10)";
		   à chaque valeur proposée par l'utilisateur, l'app répond "plus", "moins", ou "gagné";
		   3 essais maximum.
		"""
		pass


if __name__ == "__main__":

	# scénario nominal
	##################

	# L'app crée l'objet
	print("TEST 0 (nominal):")
	h = Halloween()

	# L'app initialise l'objet avec un mot de passe correct.  Dans cet exemple,
	# on suppose que "aaaaaaaa" est un password correct. Il est à modifier
	# selon vos consignes de groupe, cf vos codes.
	h.password = "aaaaaaaa"

	# L'utilisateur doit réussir le petit jeu d'Halloween.
	# S'il réussit, alors l'app passe à l'étape suivante.
	# S'il échoue, alors l'app s'arrête.
	h.play()

	# L'app identifie l'utilisateur, càd lui demande le password (fonction
	# input()).  Ceci signifie donc qu'il y a input() dans .__str__().
	# Ensuite l'app retourne le message de paix et d'amour.
	# Résultat de print(h), après identification:
	# "I witch you a happy Halloween, Silver Shamrock !"
	print(h)

	# fin du scénario nominal

	# scénarii alternatifs, générant une exception
	##############################################

	# test 1 : on ne peut pas printer l'instance sans lui donner un mot de passe
	try :
		print(Halloween())
	except Exception as e :
		print("TEST 1 : ERREUR :", e)

	# test 2 : mot de passe incorrect
	# dans cet exemple, on suppose que "aaaa" est un password incorrect
	# à modifier selon vos consignes, cf vos codes
	try:
		h = Halloween()
		h.password = "aaaa"
	except Exception as e :
		print("TEST 2 : ERREUR :", e)

	# test 3 : le mot de passe encodé ne peut pas être lu (variable suivant le groupe)
	try:
		print(h.password)
	except Exception as e :
		print("TEST 3 : ERREUR :", e)

	# test 4 : le message de paix et d'amour ne peut pas être produit si
	# l'utilisateur ne joue pas le jeu
	try:
		h = Halloween()
		h.password = "aaaaaaaa"
		# h.play() is skipped
		print(h)
	except Exception as e :
		print("TEST 4 : ERREUR :", e)

	# Finalement, l'output est globalement le suivant, mais peut varier
	# suivant vos consignes de groupe.
	"""
	TEST 0 (nominal):
	Répondez à la question suivante : [...]
	Bonne réponse !
	Enter the password : aaaaaaaa
	I witch you a happy Halloween, Silver Shamrock !
	TEST 1 : ERREUR : password not set
	TEST 2 : ERREUR : password incorrectly set
	TEST 3 : ERREUR : this property has no getter!
	TEST 4 : ERREUR : game not played
	"""
