#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'


def service_lane(width_, i_, j_):
    return min(width_[i_:j_ + 1])


n, t = raw_input().split()
n, t = int(n), int(t)
width = raw_input().split()

for i in range(n):
    i, j = raw_input().split()
    i, j = int(i), int(j)
    res = service_lane(width, i, j)
    print res