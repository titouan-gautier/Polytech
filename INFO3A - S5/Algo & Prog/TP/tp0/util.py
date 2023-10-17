import random


def saisir_entier(invite: str = 'Saisir un nombre entier :', escape: str = ""):
    res = input(invite)

    if res == escape:
        print("oui")
        return ""

    return int(res)


def saisir_string(invite: str = 'Saisir un nombre entier :', escape: str = ""):
    res = input(invite)

    if res == escape:
        return ""

    return str(res)


def test_saisir():
    a = ""
    while type(a) != int:
        try:
            a = saisir_entier()
        except ValueError:
            print("Valeur entiere stp")
            continue
    return a


from ctypes import Array, c_int


def alloc(m: int) -> Array:
    IntArrayType = c_int * m  # création d'un type "tableau de m entiers"
    return IntArrayType()


def saisir_tableau(n: int) -> Array:
    tab: Array = alloc(n)

    for i in range(len(tab)):
        tab[i] = int(input(f"Entrer la valeur numero {i} : "))

    return tab


def remplir_tableau(n: int, a: int = 0, b: int = 100) -> Array:
    tab: Array = alloc(n)

    for i in range(len(tab)):
        tab[i] = random.randint(a, b)

    return tab

def print_tab(tab : Array) :

    tab2 = []

    for i in tab :
        tab2.append(i)
    return tab2


if __name__ == '__main__':
    test_saisir()
    pass
