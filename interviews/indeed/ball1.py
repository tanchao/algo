#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'


def ball(balls_, data_):
    for a, b in data_:
        balls_[a - 1], balls_[b - 1] = balls_[b - 1], balls_[a - 1]
    return balls_


n = int(raw_input())
balls = ['1','2','3','4','5','6','7','8']
data = [(1,3),(6,8),(3,5),(2,6),(3,7),(3,4),(4,7),(2,4),(1,3),(2,7),(2,4),(6,7),(1,7),(3,4),(1,6)]
for x in range(n):
    balls = ball(balls, data)
    print x, balls
print ' '.join(list(balls))
