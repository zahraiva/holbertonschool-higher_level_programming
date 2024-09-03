#!/usr/bin/python3
import string
alp = string.ascii_lowercase.replace('e', '').replace('q', '')
for i in alp:
    print("{}".format(alp), end="")
    break
