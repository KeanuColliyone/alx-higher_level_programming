#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
    matrix (list of lists): Matrix containing integers or floats.
    div (int or float): Number to divide the matrix elements by.

    Returns:
    list of lists: New matrix with elements divided by 'div'.

    Raises:
    TypeError: If the matrix is not a list of lists of integers/floats,
               if each row of the matrix doesn't have the same size, or
               if 'div' is not a number (integer or float).
    ZeroDivisionError: If 'div' is equal to 0.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list)
            for row in matrix):
        raise TypeError("matrix must be a matrix of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number (integer or float)")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for elem in row:
            result = round(elem / div, 2)
            new_row.append(result)
        new_matrix.append(new_row)

    return new_matrix
