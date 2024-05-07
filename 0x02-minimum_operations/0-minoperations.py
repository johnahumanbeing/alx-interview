#!/usr/bin/python3
""" Minimum operations
"""


def minOperations(n):
    """ Calculate the minimum number of operations to reach n
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            n = n // divisor
            operations += divisor
        else:
            divisor += 1

    return operations
