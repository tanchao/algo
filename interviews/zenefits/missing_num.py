#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'


def missing_num(nums):
    gaps, right_gap, wrong_gap = dict(), 0, 0
    for j in range(1, len(nums)):
        i = j - 1
        gap = nums[j] - nums[i]
        if gap in gaps:
            gaps[gap] += 1
            right_gap = gap
        else:
            gaps[gap] = 1
    if len(gaps) != 2:
        print 'unexpected scene'  # error input
    for i in range(1, len(nums)):
        miss_num = nums[0] + i * right_gap
        if miss_num != nums[i]:
            return miss_num
    return 0


n = int(raw_input())
ints = map(int, raw_input().split())
if n == len(ints):
    print str(missing_num(ints))
