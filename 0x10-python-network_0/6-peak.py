#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers
"""


def find_peak(integers_list):
    """
    Args:
        integers_list(int): list of integers to find peak of
    Returns: peak of integers_list or None
    """
    size = len(integers_list)
    mid_e = size
    mid = size // 2

    if size == 0:
        return None

    while True:
        mid_e = mid_e // 2
        if (mid < size - 1 and
                integers_list[mid] < integers_list[mid + 1]):
            if mid_e // 2 == 0:
                mid_e = 2
            mid = mid + mid_e // 2
        elif mid_e > 0 and integers_list[mid] < integers_list[mid - 1]:
            if mid_e // 2 == 0:
                mid_e = 2
            mid = mid - mid_e // 2
        else:
            return integers_list[mid]
