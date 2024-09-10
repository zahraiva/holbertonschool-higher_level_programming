#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for element in my_list:
        print('{:d}'.format(element))


if __name__ == "__main__":
    print_list_integer([1, 2, 3, 4, 5])
