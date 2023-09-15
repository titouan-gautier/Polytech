import math
from fractions import Fraction


def getDeterminant(a: float, b: float, c: float) -> float:
    return (b ** 2) - (4 * a * c)


def eqn_second_degre(a: float, b: float, c: float) -> None:
    delta: float = getDeterminant(a, b, c)

    if delta == 0:
        res = -b / 2 * a
        print(res)
    elif delta < 0 :
        print("Nul")
    else:

        res1up = int(-b - math.sqrt(delta))
        res1down = 2 * a

        res2up = int(-b + math.sqrt(delta))
        res2down = 2 * a

        res1 = Fraction(res1up, res1down)
        res2 = Fraction(res2up, res2down)

        print(res1, res2)


eqn_second_degre(-1, -5, 14)
eqn_second_degre(3,5,7)
eqn_second_degre(1,-6,9)
eqn_second_degre(1,-(7/6),1/3)
