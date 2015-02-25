#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'

import sys


__DIC__ = {
    'a': '0',
    'b': '1',
    'c': '2',
    'd': '3',
    'e': '4',
    'f': '5',
    'g': '6',
    'h': '7',
    'i': '8',
    'j': '9'
}


def hidden_digits(line_):
    result_ = ''
    for char in line_:
        if char.isdigit():
            result_ += char
        if char in __DIC__:
            result_ += __DIC__[char]
    if not result_:
        result_ = 'NONE'
    return result_


with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.strip()
        if test:  # remove ending code '\n' and not empty string
            print hidden_digits(test)