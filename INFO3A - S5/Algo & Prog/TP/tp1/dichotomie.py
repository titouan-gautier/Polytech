import tp0.util as util
from random import randint


def dichotomie():
    nb: int = randint(0, 100)
    res = 110

    while res != nb:
        res = util.saisir_entier()

        if res < nb:
            print("Supérieur")
        elif res > nb:
            print('Inférieur')

    return "Trouvé"


def dichotomie_inverse():
    nb_min: int = 0
    nb_max: int = 100

    nb_donne: int = 50

    res: int = 1

    while res != 0:

        print(f"T'on nombres est il {nb_donne} ?")

        res = util.saisir_entier()

        if res == 1:  # Inférieur
            nb_max = nb_donne
            nb_donne = nb_min + (nb_max - nb_min) // 2


        elif res == 2:
            nb_min = nb_donne
            nb_donne = nb_min + (nb_max - nb_min) // 2

        print(nb_min, nb_max)

    return f"Ton nombre est {nb_donne}"


print(dichotomie_inverse())
