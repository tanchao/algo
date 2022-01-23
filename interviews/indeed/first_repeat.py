#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'

"""
Find the first repeating string in a text.
"""


def first_repeat(s):
    len_s = len(s)
    if len_s < 2:  # no repeat
        return ''
    list_s = []
    for i in range(len_s):
        if s[i] in list_s:
            return s[i]
        else:
            list_s.append(s[i])
    return ''


if __name__ == '__main__':
    pass