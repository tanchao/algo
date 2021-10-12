#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'

import sys

SIZE = 256  # defined in challenge description
MATRIX = [[0] * SIZE for i in range(SIZE)]


def set_col(orders_):
    col_ = orders_[1] - 1
    val_ = orders_[2]
    for i in range(SIZE):
        MATRIX[i][col_] = val_


def set_row(orders_):
    row_ = orders_[1] - 1
    val_ = orders_[2]
    for j in range(SIZE):
        MATRIX[row_][j] = val_


def query_col(orders_):
    col_ = orders_[1] - 1
    sum_ = 0
    for i in range(SIZE):
        sum_ += MATRIX[i][col_]
    print sum_


def query_row(orders_):
    row_ = orders_[1] - 1
    sum_ = 0
    for j in range(SIZE):
        sum_ += MATRIX[row_][j]
    print sum_


def query_board(order_):
    orders_ = order_.split(' ')  # no validation on input
    orders_[1] = int(orders_[1])
    if len(orders_) == 3:
        orders_[2] = int(orders_[2])
    if orders_[0] == 'SetCol':
        set_col(orders_)
    if orders_[0] == 'SetRow':
        set_row(orders_)
    if orders_[0] == 'QueryCol':
        query_col(orders_)
    if orders_[0] == 'QueryRow':
        query_row(orders_)


with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.strip()
        if test:  # remove ending code '\n' and not empty string
            query_board(test)