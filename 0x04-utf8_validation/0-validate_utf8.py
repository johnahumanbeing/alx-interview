#!/usr/bin/python3
""" UTF8 Validation module
"""


def validUTF8(data):
    """
    Validates if a given data set
    represents a valid UTF-8 encoding
    """
    count = 0
    for i in data:
        if count == 0:
            if i & 128 == 0:
                count = 0
            elif i & 224 == 192:
                count = 1
            elif i & 240 == 224:
                count = 2
            elif i & 228 == 240:
                count = 3
            else:
                return False
        else:
            if i & 192 != 128:
                return False
            count -= 1
    if count == 0:
        return True
    return False
