# Choisissez la bonne version de Python : 3.12, 3.13 ou 3.14
from Q61_calc import Calculator
# from Q61_calc_314 import Calculator
# from Q61_calc_313 import Calculator
# from Q61_calc_312 import Calculator

# pytest est un framework de test en Python,
# - pytest cherche automatiquement les fichiers et fonctions de test
#   en fonction de certaines conventions
# - utilisation de assert
import pytest


@pytest.fixture
def calc():
    """
    Les fixtures permettent de factoriser du code (ici: initialisation de l'objet calc ) et
    de le réutiliser entre les tests.
    """

    # Instanciation de l'objet
    # indiquez le nom de votre groupe en argument, par ex. "Héritiers" ou "Pascal Case"
    return Calculator("<nom_groupe>")


def test_somme(calc):
    """
    Convention simple mais stricte :
    - Les fonctions de test doivent commencer par test_ (en minuscules).
    - Le nom doit décrire ce qui est testé et le comportement attendu.
    """
    assert calc.plus(3, 4) == 7     # Réussi car 3 + 4 == 7
    assert calc.plus(30, 40) == 70  # Echoue à cause d'un bug


def test_produit(calc):
    assert calc.fois(2, 5) == 10    # Réussi car 2 * 5 == 10

