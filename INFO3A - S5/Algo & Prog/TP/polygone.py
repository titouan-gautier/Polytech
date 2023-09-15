Point = tuple[int, int] # alias de type
def intersect(O: Point, A: Point, B: Point) -> bool:
    (xO, yO), (xA, yA), (xB, yB) = O, A, B
    return (
        (yO <= yA) == (yO > yB) and # ordonnée dans l'intervalle
        xO < (xB - xA) * (yO - yA) / (yB - yA) + xA # point du bon côté
    )


def in_or_out(P, O : Point) :
    count : int = 0
    for i in P :
        if intersect(O,i[0],i[1]) :
            count += 1
    
    if count % 2 == 0 :
        return "L'origine n'est pas dedans"
    else :
        return "L'origine est dedans"




print(in_or_out([(0,0),(2,0),(2,2),(0,2)],(1,1)))