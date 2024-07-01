import sys

from game import game
from intelligence import intelligence


def generate(datas, gen_i, base) :

    ais = []

    i = 0
    for x in datas:
        current = intelligence(str(i))
        current.set = x
        ais.append(current)
        i += 1

    totalofgames = len(ais) * len(ais)
    i = 0
    datasize = sys.getsizeof(datas)
    ai_number = len(ais)

    for ai1 in ais :
        for ai2 in ais :
            if ai1.name == ai2.name :
                pass
            ai1.marker = 1
            ai2.marker = 2
            gm = game(ai1, ai2, base)
            if(gm.winner == ai1.marker) :
                ai1.winned += 1
            if (gm.winner == ai2.marker):
                ai2.winned += 1
            i += 1

    def func(a) :
        return a.winned

    ais.sort(reverse=True, key=func)
    return ais[0].set