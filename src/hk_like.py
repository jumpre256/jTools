import core

def __unitTest():
    print("hello world")

def match(pattern: str, datum) -> bool:
    rtnValue = True
    patternData = None
    datum = str(datum)
    if pattern[len(pattern) - 1] != "*":
        core.system_exit("match method: pattern must end with a star (*).")
    else:
        patternData = pattern[:len(pattern) - 1]

    ##print(datum[:len(patternData) - 1])

    if len(datum) < len(patternData):
        ###core.system_exit("match method: inputted datum cannot be smaller than pattern.")
        rtnValue = False
    elif datum[:len(patternData)] != patternData:
        rtnValue = False

    if rtnValue == True:
        rtnValue = datum[len(patternData):]

    return rtnValue


if __name__ == "__main__":
    main()