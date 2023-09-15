import math
from fractions import Fraction


def getDeterminant(a: float, b : float, c : float) -> float :
    return (b ** 2) - (4 * a * c)

def eqn_second_degre(a: float, b: float, c: float) -> None:

    delta : float = getDeterminant(a,b,c)

    if delta == 0:
        res = -b / 2 * a
        print(res)
    else:

        res1 = Fraction(-b - math.sqrt(delta) , 2 * a)
        res2 = Fraction(-b + math.sqrt(delta) , 2 * a)

        print(Fraction(res1, res2, res1Up,res2Up)


eqn_second_degre(-4, -3, 10)
