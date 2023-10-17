import tp0.util as util
from ctypes import Array

def inversion(n : int) -> Array :
    tab : Array = util.saisir_tableau(n)

    j : int = len(tab) - 1

    for i in range(len(tab)//2) :

        tab[i],tab[j] = tab[j],tab[i]
        j = j - 1

    return tab

print(util.print_tab(inversion(5)))