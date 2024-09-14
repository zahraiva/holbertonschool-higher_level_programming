#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        return a_dictionary
    else:
        return None
    return max(a_dictionary, key=a_dictionary.get)


if __name__ == "__main__":
    best_key = best_score(a_dictionary)
    print("Best score: {}".format(best_key))

    best_key = best_score(None)
    print("Best score: {}".format(best_key))
