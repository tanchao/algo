#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'


class Solution:
    def __init__(self):
        pass

    def maxProfit(self, prices):
        """
        Given an array of prices in a stock market
        find the highest profit you can gain.
        :param : int[] prices
        :rtype : int
        """
        if len(prices) < 2:
            return 0
        profit, total = 0, 0
        bottom, top = 10000, 0  # should init as INT_MAX
        for p in prices:
            if p < bottom:
                bottom = p
                top = 0  # new bottom only accept future top
            if p > top:
                top = p
            if profit < top - bottom:
                profit = top - bottom
                total += profit
                bottom, top, profit = top, 0, 0  # should init as INT_MAX
        return total


if __name__ == '__main__':
    pass