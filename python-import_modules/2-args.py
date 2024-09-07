#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    num = len(sys.argv) - 1
    if num <= 1:
        print("{} arguments".format(num))
    elif num == 1:
        print("{} arguments\n {}".format(num))
    else:
        print("{} arguments".format(num))
        for a in range(1, len(argv)):
            print("{}: {}".format(a, argv[a]))
