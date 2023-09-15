import tp0.util as util
import math


def perimetreDisque(rayon: int):
    return math.pi * (rayon ** 2)


def surfaceDisque(rayon: int):
    return math.pi * (rayon * 2)


def getInfoDisque():
    res = util.saisir_entier()
    return f"Surface du disque {surfaceDisque(res)} ; Perimetre du disque {perimetreDisque(res)}"

def getInfoCylindre() :
    rayon = util.saisir_entier()
    hauteur = util.saisir_entier()

    return f"Surface du cylindre {2* surfaceDisque(rayon)} ; Volume du cylindre {perimetreDisque(rayon)* hauteur}"


print(getInfoCylindre())
