import cuda_func


class game :

    winner = ""
    defgame = []

    def __init__(self, a1, a2, base):
        game_plate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        inv = False
        while cuda_func.is_winned(game_plate) == False:
            if inv:
                game_plate[a1.play(game_plate, base)] = a1.marker
            else:
                game_plate[a2.play(game_plate, base)] = a2.marker
            inv = not inv
        self.winner = cuda_func.get_winner(game_plate)
        self.defgame = game_plate