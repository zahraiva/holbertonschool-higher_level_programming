#!/usr/bin/python3
def uppercase(str):
    res = ''
    for i in str:
        if 'a' <= i <= 'z':
            res += "{}".format(chr(ord(i) - 32))
        else:
            res += "{}".format(i)
    print("{}".format(res))
