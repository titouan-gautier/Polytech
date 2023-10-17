def championnat(n: int):
    if n % 2 == 0:
        np = n
    else:
        np = n + 1

    j = np - 1
    nbmatch = np // 2

    equipe_dom = 0
    equipe_ext = 0

    for jour in range(j):
        print(f"Journée {jour + 1} : \n")
        for match in range(nbmatch):
            if match + 1 == 1:
                if n % 2 == 0:
                    equipe_dom = np
                else:
                    equipe_dom = 0
            else:
                equipe_dom = (((jour + 1) + (match + 1) - 2) % (np - 1)) + 1

            equipe_ext = (((jour + 1) - (match + 1) + np - 1) % (np - 1)) + 1

            print(f"Equipe {equipe_dom} reçoit {equipe_ext}")
        print("")


championnat(4)
