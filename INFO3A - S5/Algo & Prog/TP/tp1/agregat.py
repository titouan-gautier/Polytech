import tp0.util as util


def agregat():
    res = util.saisir_entier()

    if res == "":
        return

    max: int = res
    min: int = res
    moy: float = res

    while res != "":

        moy = (moy + res) / 2
        if res > max:  max = res
        if res < min: min = res

        print(f"Moyenne : {moy} , Mini : {min} , Max : {max}")

        res = util.saisir_entier()

    return


agregat()
