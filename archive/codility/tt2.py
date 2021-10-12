__author__ = 'tanchao@github'

import math


def solution(A):
    # write your code in Python 2.7
    print digital(A)
    return A


def digital(A):
    res = 0
    for i, v in enumerate(A):
        res += v * math.pow(-2, i)
    return int(res)

if __name__ == '__main__':
    print solution([1,0,0,1,1,1])
