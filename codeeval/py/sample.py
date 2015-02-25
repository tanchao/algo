#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'

import sys


with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.strip()
        if test:  # remove ending code '\n' and not empty string
            print 'todo'