#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'


# @param {integer[]} nums
# @return {string}
def comprehensible_ints(nums):
    len_ = len(nums)
    if len_ == 0:
        return ''
    if len_ == 1:
        return str(nums[0])
    i, res, flag = 0, '', False
    for j in range(1, len_):  # check i+1 for i input
        i = j - 1
        if nums[i] + 1 == nums[j]:
            if not flag:
                res += str(nums[i]) + '-'
                flag = True  # flag means last char is '-'
        else:
            res += str(nums[i]) + ','
            flag = False
        if j == len_ - 1:
            res += str(nums[j])
    return res


if __name__ == '__main__':
    ipt = raw_input()
    n = map(int, ipt.split())
    print comprehensible_ints(n)