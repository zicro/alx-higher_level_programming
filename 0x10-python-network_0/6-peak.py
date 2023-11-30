#!/usr/bin/python3
"""Defines peak-finding algorithm"""


def find_peak(list_of_integers):
    """Return the peak"""
    if list_of_integers == []:
        return None
    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)

    mid = int(size / 2)
    ans = list_of_integers[mid]
    if ans > list_of_integers[mid - 1] and ans > list_of_integers[mid + 1]:
        return ans
    elif ans < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
