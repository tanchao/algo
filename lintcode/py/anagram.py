#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'

class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(self, s, t):
        result = True
        if len(s) == len(t):
            len_ = len(s)
            d_s, d_t = dict(), dict()
            for i in range(len_):  # full scan on each str
                if s[i] in d_s.keys():
                    d_s[s[i]] += 1
                else:
                    d_s[s[i]] = 1
                if t[i] in d_t.keys():
                    d_t[t[i]] += 1
                else:
                    d_t[t[i]] = 1
            if not d_s == d_t:
                result = False
        else:
            result = False
        return result


if __name__ == '__main__':
    pass