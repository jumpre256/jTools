from sys import exit

def __unitTest():
    print("hello world")

def system_exit(msg = "no quit message appended."):
    print("Error: " + msg)
    exit(-1)

if __name__ == "__main__":
    __unitTest()