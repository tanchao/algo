#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'

import sys


def roman_numerals(num_=0):
    roman_ = ''
    if num_ >= 1000:
        count_1000 = num_ / 1000
        roman_ += 'M' * count_1000
        num_ -= count_1000 * 1000
    if num_ >= 900:
        roman_ += 'CM'
        num_ -= 900
    if num_ >= 500:
        roman_ += 'D'
        num_ -= 500
    if num_ >= 400:
        roman_ += 'XD'
        num_ -= 400
    if num_ >= 100:
        count_100 = num_ / 100
        roman_ += 'C' * count_100
        num_ -= count_100 * 100
    if num_ >= 90:
        roman_ += 'XC'
        num_ -= 90
    if num_ >= 50:
        roman_ += 'L'
        num_ -= 50
    if num_ >= 40:
        roman_ += 'XL'
        num_ -= 40
    if num_ >= 10:
        count_10 = num_ / 10
        roman_ += 'X' * count_10
        num_ -= count_10 * 10
    if num_ >= 9:
        roman_ += 'IX'
        num_ -= 9
    if num_ >= 5:
        roman_ += 'V'
        num_ -= 5
    if num_ >= 4:
        roman_ += 'IV'
        num_ -= 4
    if num_ >= 1:
        roman_ += 'I' * num_
    return roman_


with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.strip()
        if test:  # remove ending code '\n' and not empty string
            print test, roman_numerals(int(test))