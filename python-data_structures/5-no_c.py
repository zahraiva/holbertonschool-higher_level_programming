#!/usr/bin/python3
def no_c(my_string):
    new_string = ''
    for letter in my_string:
        if letter == 'c':
            continue
        if letter == 'C':
            continue
        new_string += letter
    return new_string


if __name__ == '__main__':
    print(no_c("Best School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))
