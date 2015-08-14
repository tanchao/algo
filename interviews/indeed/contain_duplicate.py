#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'


# @param {integer[]} nums
# @return {boolean}
def containsDuplicate(nums):
    res = False
    if len(nums) < 2:
        return res
    tmp = set()
    for n in nums:
        if n in tmp:
            res = True
            break
        else:
            tmp.add(n)
    return res


if __name__ == '__main__':
    pass