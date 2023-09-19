#!/usr/bin/python3
"""
    Divides all elements of a matrix.

    Args:
        matrix (list of lists): A matrix containing integers or floats.
        div (int or float): The number by which to divide all elements of the
            matrix.

    Returns:
        list of lists: A new matrix with all elements divided by div,\
            rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats,
                   if each row of the matrix does not have the same size,
                   or if div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.
"""


def matrix_divided(matrix, div):
    """_summary_

    Args:
        matrix (_type_): _description_
        div (_type_): _description_

    Raises:
        TypeError: _description_
        ZeroDivisionError: _description_

    Returns:
        _type_: _description_
    """
    if (
        not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(num, (int, float))
                    for row in matrix for num in row)):
        raise
    TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise
    TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
