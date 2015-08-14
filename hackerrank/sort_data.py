#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'


def sort_data(data_, k_):
    data_.sort(key=lambda x: int(x[k_]))
    for i in data_:
        print ' '.join(i)


n, m = raw_input().split()
n, m = int(n), int(m)
data = []
for i in range(n):
    line = raw_input()
    lines = line.split()
    if len(lines) == m:
        data.append(lines)
    else:
        print 'error data'
k = int(raw_input())
sort_data(data, k)