#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'

class Solution:
    # @param str: a string
    # @return an integer
    def atoi(self, str):
        result = 0
        flag = 1
        str = str.strip()
        if str.startswith('-'):  # flag stored separately
            flag = -1
            str = str[1:]
        if str.startswith('+'):  # flag stored separately
            flag = 1
            str = str[1:]
        for char_ in str:
            if char_.isdigit():
                result = result * 10 + int(char_)
            #elif char_ == '.':  # integer only check digits before .
            #    break  # as it was handled in error char case
            else:
                break  # error input, ignore the rest
        if result > 2147483648 and flag == -1:
            return -2147483648
        if result > 2147483647 and flag == 1:
            return 2147483647
        return result * flag


if __name__ == '__main__':
    pass