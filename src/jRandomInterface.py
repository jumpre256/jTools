from jRandom import *
import hk_like as HK

commands = ["python*", "quit", "help"]
availableCommands = commands

def interface():
    usrInput = None
    while True:
        usrInput = input("> ")
        if usrInput == "quit":
            quit()
        elif usrInput == "help":
            print(availableCommands)
        elif HK.match("python*", usrInput) != False:
            rawData = HK.match("python*", usrInput).strip()
            command = "weightedRandom(" + rawData + ")"
            print(eval(command))
        else:
            print("Unrecognized comamnd. Try 'help'.")


if __name__ == "__main__":
    interface()