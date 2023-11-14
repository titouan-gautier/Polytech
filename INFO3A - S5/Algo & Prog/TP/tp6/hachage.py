def exo01(d: dict, m: int):
    res = []
    collision = 0

    for i in range(m):
        res.append([])

    for i in d.keys():
        a = encodage(d[i])
        b = compresion(a, m)

        if len(res[b]) >= 1:
            collision += 1
        res[b].append(d[i])

    return collision,res


def exo1_python(d,m) :
    res = []
    collision = 0

    for i in range(m):
        res.append([])

    for i in d.keys():
        a = hash(d[i])
        b = compresion(a, m)

        if len(res[b]) >= 1:
            collision += 1
        res[b].append(d[i])

    return collision


def encodage(s: str) -> int:
    return int(''.join(str(ord(c)) for c in s))


def compresion(n: int, m: int) -> int:
    return n % m

def create_dict(f: str):
    file1 = open(f, 'r')
    lines = file1.readlines()
    lines = lines[1:]
    d = {}

    for i, l in enumerate(lines):
        d[i] = l[:len(l) - 1]
    return d




def write_dict(d: dict):
    res = []

    for cle, valeur in d.items():
        res.append(f"{cle} : {valeur}\n")

    file1 = open("test.txt", "w")
    file1.writelines(res)

