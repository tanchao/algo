#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'

import sys


def details(line_):
    lines_ = line_.split(',')
    min_, count_ = 40, 40  # matrix max size
    for row_ in lines_:
        last_x_index = row_.rindex('X')
        first_y_index = row_.index('Y')
        count_ = first_y_index - last_x_index - 1  # 1 step
        if count_ == 0:
            min_ = 0
            break
        elif count_ < min_:
            min_ = count_
    return min_


with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        print details(test)