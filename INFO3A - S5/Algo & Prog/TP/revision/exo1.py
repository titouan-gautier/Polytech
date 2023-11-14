def plps(s):
    for l in range(len(s) - 1, -1, -1):
        i: int = 0
        while s[i] == s[len(s) - l + i]:
            i += 1
            if i == l:
                return [s[i] for i in range(l)]


print(plps("mentalement"))


def plps_moi(s):
    i, j = 0, len(s) - 1
    debut, fin = "", ""
    res = ""

    while i != len(s) - 1 and j != 0:

        debut += s[i]
        fin = s[j] + fin

        if debut == fin and debut != s:
            res = debut

        i += 1
        j -= 1

    return res


print(plps_moi("mentalement"))

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