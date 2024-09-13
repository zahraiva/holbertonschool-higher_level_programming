#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_olunmus = sorted(a_dictionary.items())
    for key, val in sort_olunmus:
        print("{}: {}".format(key, val))
