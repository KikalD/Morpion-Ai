import ai
import play

is_finished = False

def exit() :
    is_finished = True

def get_help() :
    print(" ")
    for x in commands :
        print(f"{x[0]:10} | {x[2]}")
    print(" ")

def train(var) :
    ai.do_some_training(var[1], var[2])

commands = []
commands.append(["exit", exit, "Exit the program",[], "exit"])
commands.append(["help", get_help, "Show all the possible commands",[],"help"])
commands.append(["train", train, "Train the ai", ["number of ais", "number of generations"], "train {Number of ai} {Number of generations}"])
commands.append(["play", play.play_a_game, "Play a game against the ai", [], "play"])

while(not is_finished) :
    user_input = input(">>>")
    exists = False
    wrong_arguments = False
    for x in commands :
        if(user_input.split(" ")[0] == x[0]) :
            exists = True

            if((len(user_input.split(" "))-1) != len(x[3])) :
                wrong_arguments == True
                pass

            command = x[1]
            if(True):
                if(len(x[3]) > 0) :
                    command(user_input.split(" "))
                else:
                    command()
    if(exists == False) :
        print("This command doesnt exist [/help for all the existing commands]")
