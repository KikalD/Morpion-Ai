import random


class generator :

    chance_of_modification = 3

    def choose_case(self, var):
        i = 0
        positions = []
        for x in var:
            if x == 0:
                positions.append(i)
            i += 1
        if len(positions) == 0:
            return -1
        else:
            return random.choice(positions)

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

    def generate(self, base):
        var = []
        for x in base :
            var.append(self.choose_case(x))
        return var

    def get_base_options(self):
        final_string = ""
        actual = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        while actual != [2, 2, 2, 2, 2, 2, 2, 2, 2]:
            final_string += "/"
            for x in actual :
                final_string += f"{x},"
            actual = self.addition(actual)
        recomposition = []
        for x in final_string.split("/") :
            list_t = []
            for x2 in x.split(",") :
                if x2 != "" :
                    list_t.append(int(x2))
            recomposition.append(list_t)
        return recomposition

    def decline(self, set1, base):
        set2 = self.generate(base)
        i = 0
        for x in set1 :
            if(0 < random.randint(0, 100) < self.chance_of_modification) :
                x = set2[i]
            i += 1
        return set2