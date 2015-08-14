#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'

import re


def lexicographical_compare(str1, str2):
    len1, len2 = len(str1), len(str2)
    len_ = min(len1, len2)
    for i in range(len_):
        if ord(str1[i]) > ord(str2[i]):
            return 1
        if ord(str1[i]) < ord(str2[i]):
            return -1
        # else continue
    if len1 == len2:
        return 0
    elif len1 > len2:
        return 1
    else:
        return -1


def filter_emails(strs):
    # filter valid emails
    emails = list(filter(lambda x: re.match(r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', x), strs))
    # sort emails in lexicographical order
    emails.sort(lambda x, y: lexicographical_compare(x, y))
    return emails


n = int(raw_input())
lines = []
for i in range(n):
    line = raw_input()
    lines.append(line)
res = filter_emails(lines)
print res