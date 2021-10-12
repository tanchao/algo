#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'

import sys


def is_armstrong_number(num_):
    len_ = len(num_)
    num_ = int(num_)
    power_num = num_
    while 0 < num_:
        power_num -= pow(num_ % 10, len_)
        num_ /= 10
    return power_num == 0


with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        print is_armstrong_number(test.strip())