#!/usr/bin/python3
"""function def pascal_triangle(n): that returns a list of lists of integers
representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal’s triangle

    Args:
        n (int): triangle height

    Returns:
        list: the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1], [1, 1]]
    if n == 1:
        return ([[1]])

    for i in range(2, n):
        list = [1]
        for j in range(1, i + 1):
            if j == i:
                list.append(1)
                break
            else:
                element = triangle[i - 1][j - 1] + triangle[i - 1][j]
                list.append(element)
        triangle.append(list)
    return (triangle)
