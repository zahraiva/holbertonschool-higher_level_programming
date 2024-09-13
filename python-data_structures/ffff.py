#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for x in matrix:
        temp = []
        for y in x:
            temp.append(y**2)
        new_matrix.append(temp)    
        
    return new_matrix        
    
def square_matrix_simple_map(matrix=[]):
    new_matrix = []
    for x in matrix:
        new_matrix.append(list(map(lambda x: x**2, x)))
        
    return new_matrix    
    
    
    
def search_replace(my_list, search, replace):
    new_list = []
    for x in my_list:
        if x == search:
            new_list.append(replace)
        else:
            new_list.append(x)
        
    return new_list



def uniq_add(my_list=[]):
    return sum(set(my_list))


def common_elements(set_1, set_2):
    return set_1 & set_2
    
def number_keys(a_dictionary):
    return len(a_dictionary)


def print_sorted_dictionary(a_dictionary):
    sort_olunmus = sorted(a_dictionary.items())
    for key, val in sort_olunmus:
        print("{}: {}".format(key, val))
        
        
def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary

    
a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
new_dict = update_dictionary(a_dictionary, 'language', "Python")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)

print("--")
print("--")

new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)