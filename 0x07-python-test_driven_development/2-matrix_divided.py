#!/usr/bin/python3
"""Define matrix division func"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix
    
     Args:
         matrix (list): A list of lists of ints or floats
         div: The divider.
     Errors:
         TypeError: If the natrix contains non-numbers.
         TypeError: If the matrix contains rows of differnet sizes.
         TypeError: If div is not an int or float.
         ZeroDivisionError: If div is 0
     Returns:
         A new matrix reoresents the result of the division
     """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if all elements are integers or floats
    if not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    row_sizes = {len(row) for row in matrix}
    if len(row_sizes) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Divide all elements by div and round to 2 decimal places
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]
    
    return new_matrix

