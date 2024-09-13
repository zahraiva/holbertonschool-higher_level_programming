#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for x in matrix:
        temp = []
        for y in x:
            temp.append(y**2)
        new_matrix.append(temp)
    return new_matrix


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    new_matrix = square_matrix_simple(matrix)
    print(new_matrix)
    print(matrix)
