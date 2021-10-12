#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'

import sys


def longest_word(text_):
    words_ = text_.split(' ')
    longest_, len_ = '', 0
    for word_ in words_:
        if len(word_) > len_:
            longest_ = word_
            len_ = len(longest_)
    return longest_

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.strip()
        if test:  # remove ending code '\n' and not empty string
            print longest_word(test)