#!/usr/bin/python3
def no_c(my_string):
    my_string = my_string.replace('c', '')
    my_string = my_string.replace('C', '')
    return my_string


if __name__ == '__main__':
    print(no_c("Best School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))
