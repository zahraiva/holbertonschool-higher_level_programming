#!/usr/bin/python3
def reversed_alp():
    res = ''
    for i in range(25, -1, -1):
        char = chr(122 - i)
        if i % 2 == 0:
            res += char
        else:
            res += char.upper()
    print('{}'.format(res[::-1]), end='')
reversed_alp()
