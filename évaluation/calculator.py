import math
import random
import time

class CalculatorToolBox:
    """
    Class Calculator_ToolBox : classe utilisée comme boîte à outils

    Fonctionnalités :
    - elle simule le comportement d'une petite calculatrice
    - elle effectue l'addition, la soustraction, la multiplication, la division, la puissance, la racine carrée
    - elle gère une "mémoire" avec les fonctionnalités : ajouter, soustraire, effacer, récupérer la valeur
    Remarque : Cette classe ne peut pas être modifiée.
    """
    def __init__(self):
        self.memory = 0

    def plus(self, x, y ):
        """ addition des deux nombres x et y """
        return x + y

    def minus(self, x, y ):
        """ soustraction de deux nombres x et y """
        return x - y

    def times(self, x, y ):
        """ multiplication des deux nombres x et y """
        return x * y

    def divide(self, x, y ):
        """ division de deux nombres x et y """
        return x / y

    def power(self, x, y):
        return x**y

    def square(self, x):
        return x**2

    def square_root(self, x):
        return x**0.5

    def memory_plus(self, x ):
        self.memory += x

    def memory_minus(self, x ):
        self.memory -= x

    def memory_del(self):
        self.memory = 0

    def memory_get(self):
        return self.memory


class TextOutput():
    """ Manages the textual output """

    # séquence ANSI des couleurs
    # ['red', 'green', 'blue', 'yellow', 'orange', 'black', 'white', 'magenta', 'cyan']
    __COLORS = {
        "noir":          "\033[30m",
        "rouge":         "\033[31m",
        "vert":          "\033[32m",
        "jaune":         "\033[33m",
        "bleu":          "\033[34m",
        "magenta":       "\033[35m",
        "cyan":          "\033[36m",
        "blanc":         "\033[37m",
        "gris":          "\033[90m",
        "rouge_clair":   "\033[91m",
        "vert_clair":    "\033[92m",
        "jaune_clair":   "\033[93m",
        "bleu_clair":    "\033[94m",
        "magenta_clair": "\033[95m",
        "cyan_clair":    "\033[96m",
        "blanc_clair":   "\033[97m",
        "reset":         "\033[0m"  # Réinitialiser les couleurs
    }

    def __init__(self):
        self.__string_l = []
        self.__color_name_l = list(self.__COLORS.keys())

    def __str__(self):
        """ on imprime la liste donnée en couleurs """
        time.sleep(1)
        out = "calcul : "
        color_reset = self.__COLORS["reset"]

        for s in self.__string_l:
            color_name = random.sample(self.__color_name_l, 1)[0]
            color_ansi = self.__COLORS[color_name]
            out += f" {color_ansi}{s}{color_reset}"

        out += "\n"
        return out

    def append(self, string_list):
        for s in string_list: self.__string_l.append(s)

    def reset(self):
        self.__string_l = []  # liste de strings à afficher

