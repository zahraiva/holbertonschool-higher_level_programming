#!/usr/bin/python3
"""pascal's triangle"""


def pascal_triangle(n):
    """returning pascal's triangle"""
    if n <= 0:
        return []
    x = [[1]]
    for i in range(1, n):
        new_list = []
        for index in range(i + 1):
            if index != 0 and index != i:
                new_list.append(x[i - 1][index - 1] + x[i - 1][index])
            else:
                new_list.append(1)
        x.append(new_list)
    return x
