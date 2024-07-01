def is_winned(game):
    winnings = [[1, 0, 0, 0, 1, 0, 0, 0, 1], [1, 0, 0, 0, 1, 0, 0, 0, 1],
                [1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 1, 1], [1, 0, 0, 1, 0, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 0, 0, 1, 0], [0, 0, 1, 0, 0, 1, 0, 0, 1]]

    tocheck = []
    for x1 in game :
        find = False
        for x2 in tocheck :
            if x1 == x2 and x1 != 0:
                find = True
        if find == False and x1 != 0 :
            tocheck.append(x1)

    for x3 in tocheck :
        for x1 in winnings :
            matching = 0
            i = 0
            for x2 in game :
                if x2 == x3 and x1[i] == 1 :
                    matching += 1
                    if matching == 3:
                        return True
                i += 1

    nonempty = 0
    for x in game :
        if x != 0 :
            nonempty += 1
    if nonempty == len(game) :
        return None
    return False

def get_winner(game):
    winnings = [[1,0,0,0,1,0,0,0,1], [1,0,0,0,1,0,0,0,1],
                [1,1,1,0,0,0,0,0,0], [0,0,0,1,1,1,0,0,0],
                [0,0,0,0,0,0,1,1,1], [1,0,0,1,0,0,1,0,0],
                [0,1,0,0,1,0,0,1,0], [0,0,1,0,0,1,0,0,1]]

    tocheck = []
    for x1 in game :
        find = False
        for x2 in tocheck :
            if x1 == x2 and x1 != 0:
                find = True
        if find == False and x1 != 0 :
            tocheck.append(x1)

    for x3 in tocheck :
        for x1 in winnings :
            matching = 0
            i = 0
            for x2 in game :
                if x2 == x3 and x1[i] == 1 :
                    matching += 1
                    if matching == 3:
                        return x3
                i += 1

    nonempty = 0
    for x in game :
        if x != 0 :
            nonempty += 1
    if nonempty == len(game) :
        return None
    return None