#!/usr/bin/env python3
"""
    Technical interview preparation:
"""


def find_peak(integer):
    """
        A function that finds a peak in a list of unsorted integers
    """
    length = len(integer)
    if length == 0:
        return None
    if length == 1:
        return (integer[0])
    if length == 2:
        return integer[0] if integer[0] >= integer[1] else integer[1]

    for idx in range(0, length):
        value = integer[idx]
        if (idx > 0 and idx < length - 1 and
                integer[idx + 1] <= value and integer[idx - 1] <= value):
                return value
        elif idx == 0 and integer[idx + 1] <= value:
            return value
        elif idx == length - 1 and numbr[idx - 1] <= value:
            return value
    return pick
