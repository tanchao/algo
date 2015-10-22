#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
You are given a sorted list of distinct integers from 0 to 99, for instance [0, 1, 2, 50, 52, 75].
Your task is to produce a string that describes numbers missing from the list; in this case "3-49,51,53-74,76-99".

The items should be sorted in ascending order and separated by commas.
When a gap spans only one number, the item is the number itself;
when a gap is longer, the item comprises the start and the end of the gap, joined with a minus sign.
"""

__author__ = 'tanchao'


def find_miss(A):
    """
    min = 0 max = 99
    :param A:
    :return:
    """
    res = ''
    start, end = -1, -1
    if A:
        for i in xrange(99):  # handle 99 later
            if i not in A:
                if start < 0:
                    start = i
            else:
                if start >= 0:  # already has mark
                    end = i - 1
                    if end > start:
                        res += str(start) + '-' + str(end) + ','
                    else:
                        res += str(start) + ','
                    start = -1
        if 99 in A:
            if start >= 0:
                res += str(start) + '-' + str(98)
        else:
            if start >= 0:
                res += str(start) + '-' + str(99)
            else:
                res += str(99)
    else:
        res = '0-99'  # empty A
    print res
    return res

if __name__ == '__main__':
    find_miss([0, 1, 2, 50, 52, 75])
    find_miss([0, 1, 2, 4, 50, 52, 75])
    find_miss([])
    find_miss([50])
    find_miss([1,99])