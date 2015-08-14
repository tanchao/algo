#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'

def solveMeSecond(a,b):
   return a+b
n = int(raw_input())   #faster than n = input() , since input() executes the line as python command
for i in range(0,n):
    a, b = raw_input().split()
    a,b = int(a),int(b)
    res = solveMeSecond(a,b)
    print res

'''

Alternate code
n = int(raw_input())
for _ in range(n):
    a,b = map(int,raw_input().split())
    res = solveMeSecond(a,b)
    print res

'''


if __name__ == '__main__':
    pass