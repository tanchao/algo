#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'


def maxThreats(a):
    """ left_threads stores threads in left-top-to-right-bottom direction
        right_threads stores threads in right-top-to-left-bottom direction"""
    left_threads, right_threads = dict(), dict()
    max_threads, threads = 0, [0] * len(a)
    for row, col in enumerate(a):
        col -= 1  # define top-left position as (0, 0)
        left = col - row
        right = col + row
        if left in left_threads:  # exists thread
            threads[left_threads[left]] += 1  # nearest queen
            if threads[left_threads[left]] == 4:
                return 4  # max threads reached
            threads[row] += 1  # current queen
        left_threads[left] = row  # mark nearest left-thread queen
        if right in right_threads:
            threads[right_threads[right]] += 1
            if threads[right_threads[right]] == 4:
                return 4  # max threads reached
            threads[row] += 1
        right_threads[right] = row  # mark nearest right-thread queen
    return max(threads)


n = int(raw_input())
a = []
for i in range(0, n):
    pos = int(raw_input())
    a.append(pos)
res = maxThreats(a)
print res