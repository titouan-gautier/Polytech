tab = {"0": 0, "1": 1, "2": 1}


def fibonacci(n: int):
    if n <= 2:
        return 1

    if n in tab:
        return tab[n]

    else:
        tab[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return tab[n]


print([fibonacci(n) for n in range(1, 100)])
