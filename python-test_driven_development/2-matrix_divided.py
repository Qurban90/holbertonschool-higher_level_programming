#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.
It supplies one function, matrix_divided(matrix, div).
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.
    Returns a new matrix with elements rounded to 2 decimal places.
    """
    msg_type = "matrix must be a matrix (list of lists) of integers/floats"ı
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg_type)
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg_type)
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(msg_type)ı
    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in row] for row in matrix]
