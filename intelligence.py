class intelligence:


    winned = 0
    name = ""
    set = []
    marker = ""

    def addition(self, var):
        work = True;
        i = 0;
        var[0] += 1
        for x in var:
            if x > 2:
                var[i] = 0
                var[i + 1] += 1
            i += 1
        return var

    def __init__(self, name):
        self.name = name

    def load(self, file_name):
        file = open(file_name, "r")
        first = file.read().split(";")
        second = []
        for x in first :
            second.append(x.split(","))
        self.set = second

    def play(self, game, base):
        i = 0
        for x in base :
            if(game == x) :
                return self.set[i]
            i += 1