res = []


def hanoi(n: int, depart: int, arrive: int) -> list[tuple[int, int]]:

    if n > 0:
        hanoi(n - 1, depart, 6-depart-arrive)
        res.append((depart,arrive))
        hanoi(n - 1, 6-depart-arrive, arrive)

    return res


print(hanoi(3, 1, 3))
