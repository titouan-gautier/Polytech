from ctypes import Array
from dataclasses import dataclass
import tp0.util as util


@dataclass
class ArrayList:
    tab: Array
    size: int
    max_size: int

@dataclass
class Stack(ArrayList) :
    size = 10



def al_new(m: int = 10, l: list[int] = None) -> ArrayList:
    assert not l or m >= len(l)

    l = l or []

    tab: Array = util.alloc(m)

    for i in range(len(l)):
        tab[i] = l[i]

    return ArrayList(tab, len(l), m)


def al_len(tab: ArrayList):
    return tab.size


def al_is_empty(tab: ArrayList):
    return tab.size == 0


def al_str(tab: ArrayList):
    assert tab.size >= 0

    if tab.tab is None:
        tab.tab = []

    string: str = "["

    for i in range(tab.size):

        if i == tab.size - 1:
            string += str(tab.tab[i])
        else:
            string += str(tab.tab[i]) + ", "

    return string + "]"


def al_get(tab: ArrayList, i: int) -> int:
    if tab.tab is None:
        tab.tab = []

    if i < 0:
        raise IndexError("Position incorrecte")

    if i >= tab.size:
        raise IndexError("Position incorrecte")

    return tab.tab[i]


def al_set(tab: ArrayList, i: int, item: int) -> ArrayList:
    if i < 0:
        raise IndexError("Position incorrecte")

    if i >= tab.size:
        raise IndexError("Position incorrecte")

    tab.tab[i] = item

    return tab


def al_lookup(tab: ArrayList, item: int):
    for i in range(tab.size):
        if tab.tab[i] == item:
            return i

    return None


def al_remove(tab: ArrayList, i: int) -> ArrayList:
    if i < 0:
        raise IndexError("Position incorrecte")

    if i >= tab.size:
        raise IndexError("Position incorrecte")

    if tab.size <= 0:
        raise IndexError("Position incorrecte")

    tab.tab[i] = 0

    for j in range(i, len(tab.tab) - 1):
        tab.tab[j] = tab.tab[j + 1]

    tab.tab[len(tab.tab) - 1] = 0
    tab.size -= 1

    return tab


def al_insert(tab: ArrayList, i: int, item: int) -> ArrayList:
    if i < 0:
        raise IndexError("Position incorrecte")

    if i > tab.size:
        raise IndexError("Position incorrecte")

    if tab.size < 0:
        raise IndexError("Position incorrecte")

    if tab.size >= tab.max_size:
        raise OverflowError("Débordement de capacité")

    for j in reversed(range(i, len(tab.tab) - 1)):
        tab.tab[j + 1] = tab.tab[j]

    tab.tab[i] = item
    tab.size += 1

    return tab


def al_prepend(tab: ArrayList, item: int) -> ArrayList:
    return al_insert(tab, 0, item)


def al_append(tab: ArrayList, item: int) -> ArrayList:
    return al_insert(tab, tab.size, item)


def al_extend(tab1: ArrayList, tab2: ArrayList) -> ArrayList:
    if tab1.size + tab2.size > tab1.max_size:
        raise OverflowError("Débordement de capacité")

    for i in range(tab2.size):
        al_append(tab1, tab2.tab[i])

    return tab1


def quicksort(tab: ArrayList) -> None:
    debut = 0
    fin = tab.size - 1

    def sort(tab, debut, fin):

        if debut < fin:
            pivot = tab.tab[debut]
            i, j = debut, fin

            while i < j:

                while tab.tab[i] < pivot:
                    i += 1
                    tab.tab[i], tab.tab[j] = tab.tab[j], tab.tab[i]

                while tab.tab[j] > pivot:
                    j -= 1
                    tab.tab[j], tab.tab[i] = tab.tab[i], tab.tab[j]

                if i < j:
                    tab.tab[i], tab.tab[j] = tab.tab[j], tab.tab[i]

            tab.tab[i], tab.tab[j] = tab.tab[j], tab.tab[i]

            sort(tab, debut, j)
            sort(tab, j + 1, fin)

    sort(tab, debut, fin)

'''

def dichotomie(tab: ArrayList):
    
    quicksort(tab)
    
    res = "aaa"

    while res != "":

        res = input("Entrer un nombre :")

        if res == "":
            return

        def recherhce(nb : int, debut : int, fin : int, tab : ArrayList) :
            
            if debut == fin :
                return debut
            
'''



al = al_new(10, [8, 0, 4, 7, 2, 5, 9, 1, 6, 3])

quicksort(al)

print(al_str(al))


def s_new(n: int = 10) -> Stack :
    return al_new(n,[])

def s_size(s: Stack) -> int :
    return al_len(s)