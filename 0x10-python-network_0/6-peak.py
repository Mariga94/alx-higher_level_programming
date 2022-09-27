#!/usr/bin/python3
"""Define a peak-find algo"""


def find_peak(lst):
    """
    """
    if lst == []:
        return None
    if len(lst) == 1:
        return lst[0]
    elif len(lst) == 2:
        return max(lst)

    mid = int(len(lst) / 2)
    peak = lst[mid]
    if peak > lst[mid - 1] and peak > lst[mid + 1]:
        return peak
    elif peak < lst[mid - 1]:
        return find_peak(lst[:mid])
    else:
        return find_peak(lst[mid + 1:])
