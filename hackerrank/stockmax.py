#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'


def stockmax(prices_):
    """
    Given an array of prices in a stock market
    find the highest profit you can gain.
    :param : int[] prices
    :rtype : int
    """
    if len(prices_) < 2:
        return 0
    profit, peak = 0, prices_[-1]
    for i in range(len(prices_) - 1, -1, -1):
        if prices_[i] > peak:  # peak is current highest
            peak = prices_[i]
        elif prices_[i] < peak:  # previous than peak gain all profits
            profit += peak - prices_[i]
    return profit


t = int(raw_input())
for i in range(t):
    n = int(raw_input())
    prices = map(int, raw_input().split())
    if n == len(prices):  # should equal
        res = stockmax(prices)
        print res