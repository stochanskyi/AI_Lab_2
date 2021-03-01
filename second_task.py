from array_generation import *


def multiply_row_on_max(matrix):
    for row in matrix:
        row_max = np.max(row)
        row[:] = row[:] * row_max

    return matrix