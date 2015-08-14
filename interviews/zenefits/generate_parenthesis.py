#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'

class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        res, tmp = [], ''
        self.gen(res, tmp, 0, 0, n)
        return res

    def gen(self, res, tmp, left, right, n):
        if left == n:  # all left parentheis used
            tmp += ')' * (n - right)
            res.append(tmp)
            return
        self.gen(res, tmp + '(', left + 1, right, n)
        if left > right:
            self.gen(res, tmp + ')', left, right + 1, n)

    def gen_par(self, n):
        if n == 0:
            return ['']
        if n == 1:
            return ['()']
        res = []
        for i in range(n):
            for inner in self.gen_par(i):
                for outer in self.gen_par(n - i - 1):
                    res.append('(' + inner + ')' + outer)
        return res

if __name__ == '__main__':
    pass