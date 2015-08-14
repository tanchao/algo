#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'


class Solution:
    # @param {string} s
    # @return {boolean}
    def is_valid(self, s):
        len_ = len(s)
        if len_ < 2 or len_ % 2 != 0:
            return False
        res = []
        d = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in d.values():
                res.append(c)
            elif c in d.keys():
                if len(res) == 0 or res[-1] != d[c]:
                    return False  # mismatch
                else:
                    res.pop()
            else:
                return False  # invalid char
        return len(res) == 0


if __name__ == '__main__':
    pass