#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'


def utopian_tree(circle):
    height = 1  # init height
    for i in range(circle):
        if i % 2 == 0:  # spring
            height *= 2
        else:  # summer
            height += 1
    return height


n = int(raw_input())

for i in range(n):
    circle = int(raw_input())
    res = utopian_tree(circle)
    print res
