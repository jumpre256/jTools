from random import shuffle as __shuffle
import core #currently untested.

def __debuggingTesting():
    result = weightedRandom(a = 7, b = 5, c = 4, divider = 16)
    #result = weightedRandom(produceBeats = 6, spitSomeBars = 4,
                            #makeLAvideos = 1, divider = -1)
    print(result)

def weightedRandom(**kwargs):
    returnValue = None
    if kwargs.get("divider") == False:
        core.system_exit("divider keyword required to be entered")
    divider = kwargs.pop("divider")
    if divider != -1 and sum(kwargs.values()) != divider:
        core.system_exit("sum of args not equal to the divider")
    else:
        bag = []
        for outcome in kwargs:
            bag += [outcome]*kwargs[outcome]
        __shuffle(bag)
        returnValue = bag[0]
    return returnValue
            

if __name__ == "__main__":
    __debuggingTesting()
