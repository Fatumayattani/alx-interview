#!/usr/bin/python3

"""A function to rotate a matrix by 90 degrees clockwise"""


def rotate_matrix_90_degrees(matrix):
    """Returns a matrix rotated by 90 degrees clockwise"""

    copy_matrix = matrix.copy()
    matrix.clear()

    copy_matrix.reverse()

    for idx in range(len(copy_matrix)):
        temp_row = [element[idx] for element in copy_matrix]
        matrix.append(temp_row)
