def somme(n: int) -> float:
    return n * (n + 1) / 2


print(somme(3.))


def est_divisible_par(n: int, k: int) -> bool:
    return n % k == 0


print(est_divisible_par(6, 2), est_divisible_par(5, 3), est_divisible_par(9, 3))


def est_pair(x: int):
    return est_divisible_par(x, 2)


print(est_pair(2), est_pair(4), est_pair(3), est_pair(7))


def est_compris_dans(a: int, b: int, c: int) -> bool:
    if b > c:
        b, c = c, b
    return c >= a >= b

print (est_compris_dans(2,1,3), est_compris_dans(2,2,2), est_compris_dans(1,2,2),est_compris_dans(5,6,3))
