#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'


def find_min(A):
    if not A: return None
    if len(A) == 1: return A[0]
    left, right = 0, len(A) - 1
    while left < right and A[left] >= A[right]:
        mid = left + (right - left) / 2
        if A[mid] < A[right]:
            right = mid
        elif A[mid] > A[left]:
            left = mid + 1
        else:
            left += 1
    return A[left]


if __name__ == '__main__':
    print find_min([3,4,5,6,7,0,1,2])
    print find_min([])
    print find_min([3])
    print find_min([3,4,1,2])
    print find_min([3,1,2])
    print find_min([3,3,3,3,2])
    print find_min([3,4,1,2,2,2,2,2,2,2])
    print find_min([3,2,2,2,2,2])
    print find_min([1,1,1,1,1,1,1,1,1,2,2,2,2,2])