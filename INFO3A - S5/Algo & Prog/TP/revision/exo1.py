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