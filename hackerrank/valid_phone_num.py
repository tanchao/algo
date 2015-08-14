#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'

import re


def valid_phone_num(num_):
    if re.match(r'^[789](\d){9}$', num_):
        return 'YES'
    return 'NO'


n = int(raw_input())
for i in range(n):
    num = raw_input()
    res = valid_phone_num(num)
    print res