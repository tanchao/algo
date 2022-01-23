#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'

def pairs(s):
    res = {}
    s_ary = s.split()
    if len(s_ary) <= 2:
        res[s_ary] = 1
    else:
        for i in xrange(len(s_ary) - 1):
            pair = s_ary[i] + ' ' + s_ary[i+1]
            if pair in res:
                res[pair] += 1
            else:
                res[pair] = 1
    for (k, v) in res.iteritems():
        print k, v


if __name__ == '__main__':
    pairs("The quick, brown fox jumped over the lazy dogs")