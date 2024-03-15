from random import shuffle as __shuffle

def __debuggingTesting():
    result = weightedRandom(a = 7, b = 5, c = 4, divider = 16)
    #result = weightedRandom(produceBeats = 6, spitSomeBars = 4,
                            #makeLAvideos = 1, divider = -1)
    print(result)

def weightedRandom(**kwargs):
    returnValue = None
    if kwargs.get("divider") == False:
        __system_exit("divider keyword required to be entered")
    divider = kwargs.pop("divider")
    if divider != -1 and sum(kwargs.values()) != divider:
        __system_exit("sum of args not equal to the divider")
    else:
        bag = []
        for outcome in kwargs:
            bag += [outcome]*kwargs[outcome]
        __shuffle(bag)
        returnValue = bag[0]
    return returnValue
            

def __system_exit(msg = "no quit message appended."):
    print("Error: " + msg)
    #quit()

if __name__ == "__main__":
    __debuggingTesting()
