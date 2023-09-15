Point = tuple[int, int]  # alias de type


def intersect(O: Point, A: Point, B: Point) -> bool:
    (xO, yO), (xA, yA), (xB, yB) = O, A, B
    return (
            (yO <= yA) == (yO > yB) and  # ordonnée dans l'intervalle
            xO < (xB - xA) * (yO - yA) / (yB - yA) + xA  # point du bon côté
    )


Polygone = list[tuple[Point, Point]]


def in_or_out(P: Polygone, O: Point):
    count: int = 0

    for e in P:

        if intersect(O, e[0], e[1]):
            count += 1

    if count != 0:
        return count % 2 == 0, count

    return False


print(in_or_out([((0, 0), (0, 2)), ((0, 0), (2, 0)), ((2, 0), (2, 2)), ((2, 2), (2, 0))], (1,1)))
