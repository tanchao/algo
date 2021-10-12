#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'

import sys


def major_element(text_):
    nums_ = text_.split(',')
    map_, len_ = {}, len(nums_)
    for num_ in nums_:
        if num_ in map_:
            map_[num_] += 1
        else:
            map_[num_] = 1
        if map_[num_] > len_ / 2:
            return str(num_)
    max_ = max(map_.values())
    if max_ > len_ / 2:
        return str(max_)
    else:
        return 'None'

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.strip()
        if test:  # remove ending code '\n' and not empty string
            print major_element(test)