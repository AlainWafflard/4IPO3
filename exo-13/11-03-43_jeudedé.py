import random


class Jeu:
    __nb_des = 3

    def __init__(self):
        # on crée le jeu, càd les trois dés dans un tuple
        self.__de_l = tuple(De() for _ in range(self.__nb_des))
        self.__des_values_t = []

    def __del__(self):
        print("jeu mort")

    def __gt__(self, other):
        return self.value_sum > other.value_sum

    def __lt__(self, other):
        return self.value_sum < other.value_sum

    def __eq__(self, other):
        return self.value_sum == other.value_sum

    @property
    def value_sum(self):
        return sum(self.__des_values_t)

    def lancer(self):
        # on lance les 3 dés et on récupère les valeurs dans le tuple .__des_values_t
        # on retourne ce tuple
        self.__des_values_t = tuple( de.lancer() for de in self.__de_l )
        return self.__des_values_t


class De:
    __nb_faces = 6

    def __init__(self):
        self.__value = None

    def __del__(self):
        print("dé mort")

    def lancer(self):
        self.__value = random.randint(1, self.__nb_faces)
        return self.__value


if __name__ == "__main__":

    monjeu = Jeu()
    exit()



    tonjeu = Jeu()
    sonjeu = Jeu()

    mes_valeurs = monjeu.lancer()
    print(mes_valeurs)

    tes_valeurs = tonjeu.lancer()
    print(tes_valeurs)

    ses_valeurs = sonjeu.lancer()
    print(ses_valeurs)

    # print( mes_valeurs >  tes_valeurs )
    # print(monjeu > tonjeu)

    print(sorted( (mes_valeurs, tes_valeurs, ses_valeurs )))

