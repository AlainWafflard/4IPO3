from typing import Protocol


# Le contrat : tout objet ayant ces deux méthodes
class Lisible(Protocol):
    def lire(self) -> str: ...
    def fermer(self) -> None: ...


# Deux classes SANS lien d'héritage entre elles
class Fichier:
    def __init__(self, chemin):
        self.chemin = chemin

    def lire(self) -> str:
        return f"contenu de {self.chemin}"

    def fermer(self) -> None:
        print("fichier fermé")


class CapteurTemperature:
    def lire(self) -> str:
        return "23.5 °C"

    def fermer(self) -> None:
        print("capteur éteint")


# Une seule fonction, aveugle aux classes concrètes
# mais respectant le contrat défini dans la classe Lisible
def afficher(source: Lisible):
    print(source.lire())
    source.fermer()


if __name__ == "__main__":
    # Les deux objets satisfont le protocole
    f = Fichier("notes.txt")
    c = CapteurTemperature()
    afficher(f)   # contenu de notes.txt / fichier fermé
    afficher(c)   # 23.5 °C / capteur éteint

