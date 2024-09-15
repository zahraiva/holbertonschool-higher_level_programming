#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        idx = 0
        for i in range(x):
            print("{:d}".format(my_list[i]), end='')
            idx += 1
    except (TypeError, ValueError):
        print()
        return idx
    