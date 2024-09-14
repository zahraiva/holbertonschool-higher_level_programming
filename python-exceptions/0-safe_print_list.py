#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    length = 0
    
    try :
        for idx in range(x):
            print(my_list[idx], end='')
            length += 1
        print()
    except IndexError:
        print()
        return length 
        
    return length
