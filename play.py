import cuda_func
import generator
import intelligence


def play_a_game() :
    g = [0,0,0,0,0,0,0,0,0]
    a = intelligence.intelligence("A1")
    gen = generator.generator()
    best_set = []
    base = gen.get_base_options()

    with open("best_set.txt", "r") as file:
        int_set = file.read().split(",")
        for x in int_set:
            if(x != "") :
                best_set.append(int(x))

    a.set = best_set

    while cuda_func.is_winned(g) == False:
        print(g[0], " | " , g[1], " | " , g[2])
        print("--------------")
        print(g[3], " | " , g[4], " | " , g[5])
        print("--------------")
        print(g[6], " | " , g[7], " | " , g[8])
        user_case = input("Where do you want to write >>> ")
        while(g[int(user_case)] != 0) :
            user_case = input("Case already occuped, try another ! >>> ")
        g[int(user_case)] = 1
        print(g[0], " | ", g[1], " | ", g[2])
        print("--------------")
        print(g[3], " | ", g[4], " | ", g[5])
        print("--------------")
        print(g[6], " | ", g[7], " | ", g[8])
        print("APG working ...")
        g[a.play(g, base)] = 2


    print(cuda_func.get_winner(g), " winned !")