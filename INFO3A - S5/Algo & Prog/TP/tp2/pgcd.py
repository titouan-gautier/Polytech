def pgcd_recursif(a:int , b : int) -> int:
    if b == 0:
        return a
    else:
        return pgcd_recursif(b, a % b)

print(pgcd_recursif(8,12))

def pgcd_iteratif(a : int,b : int) -> int :

    while b != 0 :
        a,b = b , a % b

    return a

print(pgcd_iteratif(8,12))

