import re, operator
import tp0.util as util


def calculatrice():
    res = util.saisir_string()
    ops = {"+": operator.add, "/": operator.floordiv, "*": operator.mul, "%": operator.mod}

    nbs = re.findall("\d+", res)
    sign = re.findall("([+,//,*,%,=])+", res)
    sign_clean = []

    for s in sign :
        sign_clean.append(s.replace(" ",""))

    print(nbs)
    print(sign_clean)

    if len(nbs) < 2 :
        return "Nombre manquant"
    elif len(nbs) != len(sign_clean) :
        return "Nombre manquant ou caractère incorrect"

    if len(sign_clean) == 0:
        return "Format incorrect"
    elif sign_clean[len(sign_clean) - 1] != "=":
        return "Signe égal manquant"

    res_final = int(nbs[0])

    for n in range(len(nbs)-1) :
        res_final = ops[sign_clean[n]](res_final,int(nbs[n+1]))

    return res_final



print(calculatrice())
