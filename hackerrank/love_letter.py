#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'


def calc_char_gap(a, b):
    return abs(ord(b) - ord(a))


def love_letter(str):
    res = 0
    len_ = len(str)
    for i in range((len_ + 1) / 2):
        res += calc_char_gap(str[i], str[len_ - 1 - i])
    return res

n = int(raw_input())

for i in range(n):
    letter = raw_input()
    res = love_letter(letter)
    print res