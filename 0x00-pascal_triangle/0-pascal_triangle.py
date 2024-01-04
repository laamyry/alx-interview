#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """Pascal's Triangle"""
    result = []
    if n > 0:
        for m in range(1, n + 1):
            lev = []
            j = 1
            for k in range(1, m + 1):
                lev.append(j)
                j = j * (m - k) // k
            result.append(lev)
    return result
