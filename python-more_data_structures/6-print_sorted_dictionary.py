#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_olunmus = sorted(a_dictionary.items())
    for key, val in sort_olunmus:
        print("{}: {}".format(key, val))

# if __name__ == "__main__":
#     a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
#     print_sorted_dictionary(a_dictionary)
