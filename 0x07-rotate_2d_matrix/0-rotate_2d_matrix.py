#!/usr/bin/python3

"""Rotates 2D Matrix Interview Question"""


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix 90-degrees clockwise"""
    t_matrix = list(zip(*matrix))

    for i, row in enumerate(t_matrix):
        row = list(t_matrix[i])
        row.reverse()

        matrix[i] = row
