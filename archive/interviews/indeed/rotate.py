#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'


def rotate(s, l, r, k):
    l -= 1
    mid_s = s[l:r]
    mid_s = mid_s[-k:] + mid_s[:len(mid_s) - k]  # rotate k
    return s[:l] + mid_s + s[r:]


n = int(raw_input())
s = raw_input()
m = int(raw_input())
for x in range(m):
    l, r, k = map(int, raw_input().split())
    if n > 1 and r > l and k > 0 and k % (r - l + 1) > 0:
        k %= (r - l + 1)  # mid string length mode
        s = rotate(s, l, r, k)
print s