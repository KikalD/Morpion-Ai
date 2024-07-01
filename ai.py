import os

import generation
from generator import generator

gen = generator()
def do_some_training(ai_number, generations) :
    i5 = 0
    best_set  = None

    ai_number = int(ai_number)
    generations = int(generations)

    base = gen.get_base_options()

    if os.path.exists("best_set.txt"):
        with open("best_set.txt", "r") as file :
            best_set = file.read().split(",")

    while(i5 < generations) :

        print(f"<<< ({i5 + 1:3}/{generations}) Generation >>> ({ai_number} ais) ( {ai_number * ai_number} games)")

        datas = []

        if best_set is not None :
            i2 = 0
            while i2 < ai_number :
                try :
                    datas.append(gen.decline(best_set, base))
                except :
                    i2 -= 1
                i2 += 1
        else:
            for i in range(0, ai_number) :
                datas.append(gen.generate(base))

        best_set = generation.generate(datas, i2, base)

        i5 += 1

        with open("best_set.txt", "w+") as file:
            final_string = ""
            for x in best_set:
                final_string += str(x) + ","
            file.write(final_string)