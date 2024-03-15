

def __unitTest():
    print("hello world")

def interface():
    usrInput = None
    timesInputs = []
    while True:
        usrInput = input("> ")
        if usrInput == "quit":
            quit()
        elif usrInput == "calc":
            print(addMinSec(timesInputs))
            timesInputs.clear()
        else:
            timesInputs.append(usrInput)


def addMinSec(*args) -> str: #all arguments passed to this method should be of type string.
    if len(args) == 1 and type(args[0]) == list:
        args = args[0]
    times = []
    for arg in args:
        times.append([float(x) for x in arg.split("m")])
    timeSeconds = [minuteSecToSecs(time) for time in times]
    totalSeconds = sum(timeSeconds)
    inMinuteSeconds = secsToMinuteSec(totalSeconds)
    return minuteSecOutputFormat(inMinuteSeconds)

def minuteSecOutputFormat(timeObject) -> str: #timeObject should be a tuple or list of two elements.
    return str(timeObject[0]) + "m" + str(timeObject[1])

def minuteSecToSecs(timeObject) -> float: #timeObject should be a tuple or list of two elements.
    return timeObject[1] + (60 * timeObject[0])

def secsToMinuteSec(secs: float) -> tuple:
    intComponent = int(secs)
    decimalComponent = secs - intComponent
    minutes = intComponent // 60
    seconds = intComponent % 60
    return (minutes, seconds + decimalComponent)


if __name__ == "__main__":
    __unitTest()