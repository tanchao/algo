#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'

import sys


def shortest_repetition(line_):
    width_, len_ = 1, len(line_)  # max 80 chars
    head_ = line_[0]
    while True:
        pattern_ = line_[:width_]
        count_ = line_.count(pattern_)
        if line_ == pattern_ * count_:
            return width_
        else:
            if count_ < 1 or line_[width_ + 1:].find(head_) < 0:
                return len_
            width_ = line_[width_ + 1:].index(head_) + width_ + 1
            if width_ >= len_:
                return len_


with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.strip()
        if test:  # remove ending code '\n' and not empty string
            print shortest_repetition(test)