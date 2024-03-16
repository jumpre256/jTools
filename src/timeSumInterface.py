from timeSum import *

commands = ["calc", "quit", "ls", "help"]
availableCommands = commands

def interface():
    usrInput = None
    timesInputs = []
    while True:
        usrInput = input("> ")
        if usrInput == "quit":
            quit()
        elif usrInput == "help":
            print(availableCommands)
        elif usrInput == "calc":
            print(addMinSec(timesInputs))
            timesInputs.clear()
        elif usrInput == "ls":
            print(timesInputs)
        else:
            timesInputs.append(usrInput)


if __name__ == "__main__":
    interface()