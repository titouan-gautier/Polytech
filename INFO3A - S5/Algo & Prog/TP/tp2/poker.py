def poker():
    number = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12,
              "K": 13, "A": 14}

    sign = {"S": 0, "H": 0, "D": 0, "C": 0}

    lines = []
    with open("poker.txt", "r") as f:
        lines = f.readlines()

    player_1 = []
    player_2 = []
    winner = 0

    for i in lines :
        player_1.append(i[:14])
        player_2.append(i[15:len(i)-1])



    for i in range(len(lines)) :

        number_1 = []
        number_2 = []
        sign_1 = []
        sign_2 = []

        for j in range(0,12,3) :
            number_1.append(player_1[i][j])
            number_2.append(player_2[i][j])

            sign_1.append(player_1[i][j+1])
            sign_2.append(player_2[i][j + 1])

        number_1.append(player_1[i][len(player_1[i])-2])
        number_2.append(player_2[i][len(player_2[i]) - 2])

        sign_1.append(player_1[i][len(player_1[i])-1])
        sign_2.append(player_2[i][len(player_2[i])-1])




poker()
