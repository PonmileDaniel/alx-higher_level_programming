#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = matrix.copy()
    for i in range(len(matrix)):
        newMatrix[i] = [x**2 for x in matrix[i]]
    return (newMatrix)