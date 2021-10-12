#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'

"""
The problem is to find in an array A of int values the number of all pairs of indices (i,j) so that A[i] + A[j] == K.
For example, let A = { 1, 5, 9 } with K = 10 we get the pairs (0, 2), (2,0), and (1,1) and the result of the algorithm
should be 3.
"""


def comp_pair(k, A):
    counts, pairs = 0, {}
    for a in A:
        target = k - a
        tmp = 0 if target not in pairs else pairs[target]
        pairs[target] = tmp + 1
    # print pairs
    for t in A:
        if t in pairs:
            counts += pairs[t]
    return counts


if __name__ == '__main__':
    print comp_pair(10, [1, 5, 9, 4, 6, 3])
    print comp_pair(10, [5])
    print comp_pair(10, [1, 3])
    print comp_pair(10, [1, 5, 9])
