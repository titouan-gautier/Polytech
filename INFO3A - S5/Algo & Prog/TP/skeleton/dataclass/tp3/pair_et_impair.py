from ctypes import Array
import tp0.util as util

def pair_et_impair() -> Array:

    tab : Array = util.remplir_tableau(10,0,100)

    pair = []
    impair = []

    for i in tab :
        if i % 2 == 0 :
            pair.append(i)
        else :
            impair.append(i)

    return pair + impair


def pair_et_impair_en_place() -> Array :

    tab: Array = util.remplir_tableau(10, 0, 100)

    print(util.print_tab(tab))

    for i in range(len(tab)) :

        if tab[i] % 2 != 0 :
            for j in range(i,len(tab)) :
                 if tab[j] % 2 == 0 :
                     tab[j],tab[i] = tab[i],tab[j]

    return tab

def pair_et_impair_en_place2() -> Array :

    tab: Array = util.remplir_tableau(10, 1, 100)

    j : int = len(tab) - 1

    for i in range(len(tab)) :

        while tab[i] % 2 != 0 and j > len(tab)//2 :
            tab[i],tab[j] = tab[j],tab[i]
            j = j - 1

    return tab

print(util.print_tab(pair_et_impair_en_place2()))




