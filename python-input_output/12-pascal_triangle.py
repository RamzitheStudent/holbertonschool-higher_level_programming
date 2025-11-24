#!/usr/bin/python3
"""Function that returns Pascal's triangle."""


def pascal_triangle(n):
    """
    Return a list of lists representing Pascal's triangle of n.
    Empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        # Hər sətrin başlanğıcı 1-dən ibarət olur
        row = [1]

        if i > 0:
            prev_row = triangle[i - 1]

            # Ortadakı elementlər: prev_row[j] + prev_row[j - 1]
            for j in range(1, i):
                row.append(prev_row[j] + prev_row[j - 1])

            # Hər sətrin sonu da 1 olur
            row.append(1)

        triangle.append(row)

    return triangle
