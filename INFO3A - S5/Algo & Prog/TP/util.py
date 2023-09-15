def saisir_entier(invite: str = 'Saisir un nombre entier : ', escape: str | None = None) -> int | None:
    return int(input(invite))


def test_saisir():
    a = ""
    while type(a) != int:
        try:
            a = saisir_entier()
        except ValueError:
            print("Valeur entiere stp")
            continue
    return a


test_saisir()
