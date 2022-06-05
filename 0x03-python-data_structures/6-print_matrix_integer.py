#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0:
        print()
    else:
        for row in range(len(matrix)):
            print(*matrix[row])
