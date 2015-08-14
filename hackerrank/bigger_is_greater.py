#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'


def bigger_is_greater(str_):
    res_ = 'no answer'  # descending order means biggest
    len_ = len(str_)
    if len_ > 1:  # empty or single char means biggest
        for i in range(len_ - 2, -1, -1):
            left_part = str_[:i]
            right_part = str_[i:]  # starts with 2 chars
            rights = list(right_part)
            if not rights[0] == max(rights):  # note the right part always in descending order
                for j in range(len(rights) - 1, 0, -1):
                    if ord(right_part[j]) > ord(rights[0]):  # first larger char
                        tmp = rights[j]
                        rights[j] = rights[0]
                        rights[0] = tmp  # swap 0, j
                        rights = rights[1:]
                        rights.sort()  # sort right part to get smallest
                        right_part = tmp + ''.join(rights)
                        res_ = left_part + right_part
                        return res_
    return res_

'''
n = int(raw_input())

for i in range(n):
    line = raw_input()
    res = bigger_is_greater(line.strip())
    print res
'''

if __name__ == '__main__':
    output = open('output', 'w')
    with open('input', 'r') as input_:
        fh = input_.readlines()
        if not int(fh[0]) == len(fh) - 1:
            print 'error test data', fh
            exit(1)
        for line in fh[1:]:
            res = bigger_is_greater(line.strip())
            output.write(res + '\n')
    output.close()