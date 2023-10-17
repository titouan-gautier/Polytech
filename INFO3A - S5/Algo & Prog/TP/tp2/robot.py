import numpy as np


def robot_cupide(damier: list[list[int]], x: int = 0, y: int = 0, nbCase: int = 0) -> int:

    if x == len(damier[len(damier) - 1]) - 1 and y == len(damier) - 1:
        nbCase += damier[x][y]
        print(f"{nbCase} Bitcoin on été récupéré")
        return nbCase
    else:
        if x != len(damier[len(damier) - 1]) - 1 and y != len(damier) - 1:

            nbCase += damier[x][y]
            droite = damier[x + 1][y]
            bas = damier[x][y + 1]

            if droite >= bas:
                x = x + 1
            else:
                y = y + 1

            robot_cupide(damier, x, y, nbCase)


        elif x != len(damier[len(damier) - 1]) - 1 and y == len(damier) - 1:
            nbCase += damier[x][y]
            x = x + 1
            robot_cupide(damier, x, y, nbCase)

        else:
            nbCase += damier[x][y]
            y = y + 1
            robot_cupide(damier, x, y, nbCase)


damier = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])

print(robot_cupide(damier))
