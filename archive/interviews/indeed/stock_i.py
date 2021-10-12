#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'

"""
Given an array of prices in a stock market, find the highest price you can gain.
"""

class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        profit = -1
        bottom, top = 10000, 0  # should init as INT_MAX
        for p in prices:
            if p < bottom:
                bottom = p
                top = 0  # new bottom only accept future top
            if p > top:
                top = p
            if profit < top - bottom:
                profit = top - bottom
        return profit


if __name__ == '__main__':
    pass